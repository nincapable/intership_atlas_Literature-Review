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
    unique_traits = {}
    excluded_trait_names = set()

    for cls in entity.ancestors():
        if hasattr(cls, "isExceptionTo"):
            exceptions = getattr(cls, "isExceptionTo")
            if exceptions:
                list_exc = exceptions if isinstance(exceptions, (list, iterators.IndirectList)) else [exceptions]
                for exc in list_exc:
                    excluded_trait_names.add(exc.name)

        if hasattr(cls, property_name):
            values = getattr(cls, property_name)
            if values:
                list_values = values if isinstance(values, (list, iterators.IndirectList)) else [values]
                for t in list_values:
                    if t.name not in excluded_trait_names and t.name not in unique_traits:
                        unique_traits[t.name] = t
    return list(unique_traits.values())

def compute_and_write_reactivity_factor(taxon, sensi):
    """
    Calcule le facteur de réactivité en respectant l'intégrité physique des traits.
    La maintenance n'altère pas les valeurs, elle réduit la probabilité que 
    le trait participe à l'ignition (poids).
    """
    aiding_traits = get_filtered_inherited_traits(taxon, "hasFireAidingTrait")
    
    t_ref = 400.0 
    # On initialise avec les valeurs de référence du bois standard
    min_threshold = 400.0
    min_delay = 600.0

    for t in aiding_traits:
        # 1. On récupère les constantes physiques réelles (immuables)
        t_physic = float(getattr(t, "spontaneousIgnitionThreshold", 400.0) or 400.0)
        d_physic = float(getattr(t, "ignitionDelay", 600.0) or 600.0)
        
        # 2. On évalue l'impact de la maintenance sur la DISPONIBILITÉ du trait
        # L'efficacité (0.0 à 1.0) représente ici la part du trait "neutralisée" ou supprimée.
        residual_exposure = 1.0
        if hasattr(t, "hasrecommendedMaintenance"):
            protocols = t.hasrecommendedMaintenance
            # On cherche l'efficacité de la maintenance si elle est réalisée
            efficiencies = [
                float(getattr(p, "maintenanceEfficiency", 0.0) or 0.0) 
                for p in protocols if getattr(p, "isMaintained", False) == True
            ]
            if efficiencies:
                # L'exposition résiduelle est l'inverse de l'efficacité la plus haute
                residual_exposure = 1.0 - max(efficiencies)

        # 3. Logique de Maillon Faible Modulée
        # Si un trait est très dangereux physiquement MAIS a été maintenu à 90%, 
        # son poids dans la recherche du "min" est drastiquement réduit.
        # On utilise une pondération : si l'exposition est faible, la valeur physique 
        # est "poussée" vers la neutralité pour ne pas fausser le risque global.
        
        t_effective = t_physic + ((t_ref - t_physic) * (1.0 - residual_exposure))
        d_effective = d_physic + ((600.0 - d_physic) * (1.0 - residual_exposure))

        if t_effective < min_threshold:
            min_threshold = t_effective
        if d_effective < min_delay:
            min_delay = d_effective

    # 4. Calcul final basé sur le pire trait "exposé"
    i_seuil = t_ref / max(100.0, min_threshold) 
    i_delai = 1.0 + (5.0 / (min_delay + 5.0))
    
    reactivity_factor = i_seuil * i_delai
    sensi.ReactivityFactor = float(reactivity_factor)
    
    return reactivity_factor

def compute_individual_behavioral_indices(biomass_component):
    taxon = biomass_component.refersToTaxon
    if not taxon or not hasattr(taxon, "hasFireSensitivity") or not taxon.hasFireSensitivity:
        return 1.0 # Facteur de réactivité par défaut

    sensi = taxon.hasFireSensitivity[0]

    # 1. VALEUR DE BASE (HRP BioReign)
    hrp_base = 0.0
    for cls in taxon.ancestors():
        if hasattr(cls, "organicIgnitionBasis"):
            hrp_base = float(cls.organicIgnitionBasis or 0.0)
            if hrp_base > 0: break

    # 2. INITIALISATION / RESET DES COMPTEURS
    hrp_plus = hrp_minus = v_trans_plus = v_trans_minus = h_trans_plus = h_trans_minus = 0.0
    sensi.calculatedHorizontalBarrierPotential = 0.0
    sensi.calculatedVerticalBarrierPotential = 0.0

    # 3. AIDING TRAITS
    aiding_traits = get_filtered_inherited_traits(taxon, "hasFireAidingTrait")
    for t in aiding_traits:
        impact_factor = 1.0
        if hasattr(t, "hasrecommendedMaintenance"):
            protocols = t.hasrecommendedMaintenance
            if any(getattr(p, "isMaintained", False) for p in protocols):
                efficiency = max([float(getattr(p, "maintenanceEfficiency", 0.0) or 0.0) for p in protocols])
                impact_factor = 1.0 - efficiency
        
        hrp_plus += (float(getattr(t, "heatReleasePotential", 0.0) or 0.0) * impact_factor)
        v_trans_plus += (float(getattr(t, "verticalTransferPotential", 0.0) or 0.0) * impact_factor)
        h_trans_plus += (float(getattr(t, "horizontalTransferPotential", 0.0) or 0.0) * impact_factor)

    # 4. RESISTING TRAITS
    resisting_traits = get_filtered_inherited_traits(taxon, "hasFireResistingTrait")
    for t in resisting_traits:
        hrp_minus += float(getattr(t, "heatReleasePotential", 0.0) or 0.0)
        v_trans_minus += float(getattr(t, "verticalTransferPotential", 0.0) or 0.0)
        h_trans_minus += float(getattr(t, "horizontalTransferPotential", 0.0) or 0.0)
        
        res_dur = float(getattr(t, "fireResistanceDuration", 0.0) or 0.0)
        sensi.calculatedHorizontalBarrierPotential += (res_dur * 0.7)
        sensi.calculatedVerticalBarrierPotential += (res_dur * 0.3)

    # 5. SYNTHÈSE CINÉTIQUE
    total_hrp = max(0.0, (hrp_base + hrp_plus) - hrp_minus)
    total_v_trans = max(0.0, v_trans_plus - v_trans_minus)
    total_h_trans = max(0.0, h_trans_plus - h_trans_minus)

    # 6. RÉACTIVITÉ ET RISQUE FINAL
    f_reac = compute_and_write_reactivity_factor(taxon, sensi)
    risk_cinetique = (total_hrp * 0.3) + (total_v_trans * 0.5) + (total_h_trans * 0.2)

    # Écriture finale
    sensi.calculatedHeatReleasePotential = float(total_hrp)
    sensi.calculatedVerticalTransferPotential = float(total_v_trans)
    sensi.calculatedHorizontalTransferPotential = float(total_h_trans)
    sensi.calculatedGeneralFireRisk = float(risk_cinetique * f_reac)
    
    return f_reac

def compute_global_ignition_probability(natural_space):
    total_p_ignition = 0.0
    measurements = natural_space.hasBiomassState
    
    for meas in measurements:
        for component in meas.hasComponent:
            taxon = component.refersToTaxon
            if not taxon: continue
            
            # Calcul individuel et récupération du facteur de réactivité
            f_reac = compute_individual_behavioral_indices(component)
            
            valette_score = 2
            if hasattr(taxon, "hasFireSensitivity") and taxon.hasFireSensitivity:
                valette_score = getattr(taxon.hasFireSensitivity[0], "ValetteScore", 2) or 2
            
            share = float(getattr(component, "percentageShare", 0.0) or 0.0)
            # La probabilité d'ignition globale est boostée par la réactivité locale
            total_p_ignition += (valette_score * (share / 100.0)) * f_reac

    natural_space.globalIgnitionProbability = float(total_p_ignition)
    return total_p_ignition

def run_calculation():
    onto = load_ontology(ONTO_PATH, THESAURUS_PATH)
    print("--- Analyse des Espaces Naturels ---")
    for ns in onto.NaturalSpace.instances():
        p_ign = compute_global_ignition_probability(ns)
        print(f"Espace : {ns.name} | P_Ignition Globale : {p_ign:.2f}")
        
    onto.save(file=OUTPUT_PATH, format="turtle")
    print(f"--- Fichier sauvegardé : {OUTPUT_PATH} ---")

if __name__ == "__main__":
    run_calculation()