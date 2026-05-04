from owlready2 import *
import Ontologies_KG.Scripts.fe_taxon_vege as veg_engine 
import Ontologies_KG.Scripts.fe_taxon_animal as ani_engine

# --- CONFIGURATION ---
ONTO_PATH = "../Modules/fe_natural_space.ttl"
THESAURUS_PATH = "../Thesaurus/fe_thesaurus_especes.ttl"
OUTPUT_PATH = "../Modules/fe_natural_space_final.ttl"

def get_inherited_value(entity, property_name, default_value):
    """Utilitaire pour récupérer les valeurs sur les ancêtres (logique de la feuille)."""
    for cls in entity.ancestors():
        if hasattr(cls, property_name):
            val = getattr(cls, property_name)
            if val is not None:
                return val[0] if isinstance(val, (list, iterators.IndirectList)) else val
    return default_value

def compute_all_space_indices(natural_space):
    """
    Agrège les indices : 
    - Flore = Ignition + Propagation linéaire
    - Faune = Propagation par saut (Spotting) boostée par la panique
    """
    total_p_ign = 0.0
    total_vel = 0.0
    total_bar = 0.0
    max_protection_weight = 0.0
    
    # On suppose une seule mesure d'état de biomasse par espace pour l'analyse
    measurements = natural_space.hasBiomassState
    for meas in measurements:
        for comp in meas.hasComponent:
            taxon = comp.refersToTaxon
            if not taxon: continue
            
            # 1. Calculs via les moteurs dédiés
            if veg_engine.is_combustible_organism(taxon):
                veg_engine.compute_taxon_full_indices(taxon)
                is_animal = False
            else:
                ani_engine.compute_animal_indices(taxon)
                is_animal = True
            
            sensi = taxon.hasFireSensitivity[0]
            weight = float(getattr(comp, "percentageShare", 0.0) or 0.0) / 100.0
            
            # --- CALCUL DE L'IGNITION (Uniquement Végétal) ---
            if not is_animal:
                # Valette (Structure) * ReactivityFactor (Physique: Seuil/Délai)
                valette = float(get_inherited_value(sensi, "ValetteScore", 2.0))
                f_reac_phys = float(sensi.ReactivityFactor or 1.0)
                total_p_ign += (valette * f_reac_phys) * weight
            # else: total_p_ign += 0  <-- L'animal ne participe pas à l'éclosion
            
            # --- CALCUL DE LA PROPAGATION (VELOCITY) ---
            ht = float(sensi.calculatedHorizontalTransferPotential or 0.0)
            vt = float(sensi.calculatedVerticalTransferPotential or 0.0)
            
            if is_animal:
                # L'animal est un vecteur horizontal. Sa panique (f_reac) 
                # amplifie sa vitesse de déplacement des foyers.
                panic_factor = float(sensi.ReactivityFactor or 0.5) # f_reac animal
                # Plus la panique est forte (seuil bas), plus l'impact est grand
                total_vel += (ht * (1.5 - panic_factor)) * weight
            else:
                # Propagation végétale standard
                total_vel += ((vt + ht) / 2.0) * weight
            
            # --- BARRIÈRE ET PROTECTION ---
            total_bar += float(sensi.calculatedHorizontalBarrierPotential or 0.0) * weight
            
            # Utilisation du poids UICN pour la priorité d'évacuation
            # (Via la fonction définie précédemment ou accès direct au mapping)
            prio = float(get_inherited_value(sensi, "protectionPriorityWeight", 1.0))
            if prio > max_protection_weight:
                max_protection_weight = prio

    # 3. Écriture des résultats sur l'instance NaturalSpace
    natural_space.globalIgnitionProbability = float(total_p_ign)
    natural_space.firePropagationVelocity = float(total_vel)
    natural_space.structuralFireBarrierEffect = float(total_bar)
    natural_space.globalEvacuationUrgency = float(max_protection_weight)
    
    return total_p_ign

def run():
    onto = get_ontology(ONTO_PATH).load()
    get_ontology(THESAURUS_PATH).load()
    sync_reasoner()

    print("--- Analyse des Espaces Naturels (Correction Physique OK) ---")
    for ns in onto.NaturalSpace.instances():
        res = compute_all_space_indices(ns)
        print(f"Espace : {ns.name:20} | P_Ign (Végétale) : {res:5.2f} | Urgency : {ns.globalEvacuationUrgency}")

    onto.save(file=OUTPUT_PATH, format="turtle")

if __name__ == "__main__":
    run()