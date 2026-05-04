from owlready2 import *
# On importe les deux moteurs
import Ontologies_KG.Scripts.fe_taxon_vege as veg_engine 
import Ontologies_KG.Scripts.fe_taxon_animal as ani_engine

# --- CONFIGURATION ---
ONTO_PATH = "../Modules/fe_natural_space.ttl"
THESAURUS_PATH = "../Thesaurus/fe_thesaurus_especes.ttl"
OUTPUT_PATH = "../Modules/fe_natural_space_final.ttl"

def compute_all_space_indices(natural_space):
    """Agrège les indices de tous les taxons (Végétaux & Animaux) présents dans l'espace."""
    total_p_ign = 0.0
    total_vel = 0.0
    total_bar = 0.0
    
    # On accède aux états de biomasse
    measurements = natural_space.hasBiomassState
    for meas in measurements:
        for comp in meas.hasComponent:
            taxon = comp.refersToTaxon
            if not taxon: continue
            
            # --- 1. ROUTAGE ET CALCUL INDIVIDUEL ---
            # On utilise la fonction de vérification du moteur végétal
            if veg_engine.is_combustible_organism(taxon):
                f_reac = veg_engine.compute_taxon_full_indices(taxon)
            else:
                # Si ce n'est pas un végétal/fungi, on considère que c'est un animal
                f_reac = ani_engine.compute_animal_indices(taxon)
            
            # Si le calcul a échoué (None), on passe au suivant
            if f_reac is None: continue

            # --- 2. RÉCUPÉRATION DES DONNÉES CALCULÉES ---
            sensi = taxon.hasFireSensitivity[0]
            share = float(getattr(comp, "percentageShare", 0.0) or 0.0)
            weight = share / 100.0
            
            # A. Ignition (Valette pondéré par la réactivité spécifique)
            valette = float(getattr(sensi, "ValetteScore", 2) or 2)
            total_p_ign += (valette * f_reac) * weight
            
            # B. Propagation (Transferts)
            # Pour les animaux, HT peut être élevé (vecteur) et VT souvent nul.
            vt = float(getattr(sensi, "calculatedVerticalTransferPotential", 0.0) or 0.0)
            ht = float(getattr(sensi, "calculatedHorizontalTransferPotential", 0.0) or 0.0)
            total_vel += ((vt + ht) / 2.0) * weight
            
            # C. Barrière (Principalement végétale)
            vb = float(getattr(sensi, "calculatedVerticalBarrierPotential", 0.0) or 0.0)
            hb = float(getattr(sensi, "calculatedHorizontalBarrierPotential", 0.0) or 0.0)
            total_bar += (vb + hb) * weight

    # --- 3. ÉCRITURE DES RÉSULTATS GLOBAUX SUR L'ESPACE ---
    natural_space.globalIgnitionProbability = float(total_p_ign)
    natural_space.firePropagationVelocity = float(total_vel)
    natural_space.structuralFireBarrierEffect = float(total_bar)
    
    return total_p_ign

def run():
    # Chargement des ontologies
    onto = get_ontology(ONTO_PATH).load()
    get_ontology(THESAURUS_PATH).load()
    
    # Synchronisation du raisonneur pour s'assurer que les ancestors() sont à jour
    sync_reasoner()

    print("--- Analyse Multi-Règne des Espaces Naturels ---")
    for ns in onto.NaturalSpace.instances():
        res = compute_all_space_indices(ns)
        print(f"Espace : {ns.name} | P_Ignition Globale : {res:.2f}")

    # Sauvegarde du graphe enrichi
    onto.save(file=OUTPUT_PATH, format="turtle")
    print(f"Analyse terminée. Fichier sauvegardé : {OUTPUT_PATH}")

if __name__ == "__main__":
    run()