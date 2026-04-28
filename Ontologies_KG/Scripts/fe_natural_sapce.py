from owlready2 import *

# --- CONFIGURATION ---
ONTO_PATH = "../Modules/fe_natural_space.ttl"
THESAURUS_PATH = "../Thesaurus/fe_thesaurus_especes.ttl"
OUTPUT_PATH = "../Modules/fe_natural_space_updated.ttl"

def load_ontology(onto_path, thesaurus_path):
    onto = get_ontology(onto_path).load()
    get_ontology(thesaurus_path).load()
    sync_reasoner() 
    return onto

def get_filtered_inherited_traits(entity, property_name):
    """
    Collecte les traits en respectant la priorité (bas vers haut)
    et en filtrant les exceptions (isExceptionTo).
    """
    unique_traits = {}
    excluded_trait_names = set()

    for cls in entity.ancestors():
        # Gestion des exceptions (priorité aux niveaux bas)
        if hasattr(cls, "isExceptionTo"):
            exceptions = getattr(cls, "isExceptionTo")
            if exceptions:
                list_exc = exceptions if isinstance(exceptions, (list, iterators.IndirectList)) else [exceptions]
                for exc in list_exc:
                    excluded_trait_names.add(exc.name)

        # Collecte des traits
        if hasattr(cls, property_name):
            values = getattr(cls, property_name)
            if values:
                list_values = values if isinstance(values, (list, iterators.IndirectList)) else [values]
                for t in list_values:
                    if t.name not in excluded_trait_names and t.name not in unique_traits:
                        unique_traits[t.name] = t
    
    return list(unique_traits.values())

def compute_individual_behavioral_indices(biomass_component):
    taxon = biomass_component.refersToTaxon
    if not taxon or not taxon.hasFireSensitivity:
        return

    sensi = taxon.hasFireSensitivity[0]

    # 1. VALEUR DE BASE
    hrp_base = 0.0
    for cls in taxon.ancestors():
        if hasattr(cls, "organicIgnitionBasis"):
            hrp_base = float(cls.organicIgnitionBasis or 0.0)
            if hrp_base > 0: break

    # 2. INITIALISATION DES COMPTEURS
    # On sépare les forces d'accélération et de résistance
    hrp_plus = 0.0
    hrp_minus = 0.0
    v_trans_plus = 0.0
    v_trans_minus = 0.0
    h_trans_plus = 0.0
    h_trans_minus = 0.0
    
    # 3. TRAITEMENT DES AIDING TRAITS (Accélérateurs)
    aiding_traits = get_filtered_inherited_traits(taxon, "hasFireAidingTrait")
    for t in aiding_traits:
        impact_factor = 1.0
        # Vérification maintenance
        if hasattr(t, "hasrecommendedMaintenance"):
            protocols = t.hasrecommendedMaintenance
            if any(getattr(p, "isMaintained", False) for p in protocols):
                efficiency = max([float(getattr(p, "maintenanceEfficiency", 0.0) or 0.0) for p in protocols])
                impact_factor = 1.0 - efficiency
        
        hrp_plus += (float(getattr(t, "heatReleasePotential", 0.0) or 0.0) * impact_factor)
        v_trans_plus += (float(getattr(t, "verticalTransferPotential", 0.0) or 0.0) * impact_factor)
        h_trans_plus += (float(getattr(t, "horizontalTransferPotential", 0.0) or 0.0) * impact_factor)

    # 4. TRAITEMENT DES RESISTING TRAITS (Modérateurs)
    resisting_traits = get_filtered_inherited_traits(taxon, "hasFireResistingTrait")
    for t in resisting_traits:
        # Note : On ne réduit généralement pas l'efficacité d'un trait de résistance par la maintenance
        # sauf si la maintenance est mauvaise (ex: taille qui crée du bois mort).
        # Ici on prend la pleine valeur de résistance.
        hrp_minus += float(getattr(t, "heatReleasePotential", 0.0) or 0.0)
        v_trans_minus += float(getattr(t, "verticalTransferPotential", 0.0) or 0.0)
        h_trans_minus += float(getattr(t, "horizontalTransferPotential", 0.0) or 0.0)
        
        # On alimente aussi les BarrierPotentials (spécifiques aux traits résistants)
        res_dur = float(getattr(t, "fireResistanceDuration", 0.0) or 0.0)
        sensi.calculatedHorizontalBarrierPotential += (res_dur * 0.7)
        sensi.calculatedVerticalBarrierPotential += (res_dur * 0.3)
        sensi.calculatedHorizontalTransferPotential += (res_dur * 0.3)

    # 5. SYNTHÈSE DES INDICES
    # HRP Final = (Base + Bonus inflammabilité) - Capacités d'absorption thermique
    total_hrp = max(0, (hrp_base + hrp_plus) - hrp_minus)
    
    # Transfert Vertical Final = Potentiel de mèche - Obstacles physiques
    total_v_trans = max(0, v_trans_plus - v_trans_minus)
    
    # Transfert Horizontal Final = Potentiel de mèche - Obstacles physiques
    total_h_trans = max(0, h_trans_plus - h_trans_minus)

    # Écriture dans l'Ontologie
    sensi.calculatedHeatReleasePotential = float(total_hrp)
    sensi.calculatedVerticalTransferPotential = float(total_v_trans)
    
    # Risque Général (Vision Pompier : Puissance vs Capacité d'arrêt)
    # Un arbre avec beaucoup de résistance (ex: Chêne liège) verra son risque chuter drastiquement
    sensi.calculatedGeneralFireRisk = float((total_hrp * 0.4) + (total_v_trans * 0.6))
    
    return sensi

def compute_global_ignition_probability(natural_space):
    """Calcule P_ignition et déclenche les calculs individuels."""
    total_p_ignition = 0.0
    measurements = natural_space.hasBiomassState
    
    for meas in measurements:
        for component in meas.hasComponent:
            taxon = component.refersToTaxon
            if not taxon: continue
            
            # P_ignition pondérée
            valette_score = 2 # Valeur par défaut
            if taxon.hasFireSensitivity:
                valette_score = getattr(taxon.hasFireSensitivity[0], "ValetteScore", 2) or 2
            
            share = getattr(component, "percentageShare", 0.0) or 0.0
            total_p_ignition += (float(valette_score) * (float(share) / 100.0))
            
            # Calcul des indices de l'individu
            compute_individual_behavioral_indices(component)

    natural_space.globalIgnitionProbability = float(total_p_ignition)
    return total_p_ignition

def run_calculation():
    onto = load_ontology(ONTO_PATH, THESAURUS_PATH)
    
    print("--- Analyse des Espaces Naturels ---")
    for ns in onto.NaturalSpace.instances():
        p_ign = compute_global_ignition_probability(ns)
        print(f"Propriété globalIgnitionProbability mise à jour pour {ns.name} : {p_ign:.2f}")
        
    # Sauvegarde finale
    onto.save(file=OUTPUT_PATH, format="turtle")
    print(f"--- Fichier sauvegardé : {OUTPUT_PATH} ---")

if __name__ == "__main__":
    run_calculation()