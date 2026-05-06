from owlready2 import *

def get_inherited_value(entity, property_name, default_value):
    """
    Récupère une valeur sur l'individu ou ses ancêtres (Classes ou Concepts SKOS).
    Gère l'héritage sémantique pour les coefficients de style.
    """
    if not entity:
        return default_value
        
    # 1. Vérification directe sur l'instance
    if hasattr(entity, property_name):
        val = getattr(entity, property_name)
        if val: 
            return val[0] if isinstance(val, (list, iterators.IndirectList)) else val
    
    # 2. Remontée dans la hiérarchie (is_a pour les classes, broader pour SKOS)
    # Note : Pour SKOS, on peut aussi suivre 'broader' si configuré
    for cls in entity.ancestors():
        if hasattr(cls, property_name):
            val = getattr(cls, property_name)
            if val: 
                return val[0] if isinstance(val, (list, iterators.IndirectList)) else val
                
    return default_value

def compute_building_indices(building):
    """
    Calcule les indicateurs de performance incendie pour un bâtiment.
    Exploite la composition matérielle et les propriétés intrinsèques du style.[cite: 1]
    """
    # Récupération ou création de l'objet de risque
    risk = building.hasBuildingFireRisk[0] if building.hasBuildingFireRisk else None
    if not risk: 
        return

    # --- 1. ANALYSE THERMIQUE DES MATÉRIAUX ---
    total_combustibility = 0.0
    total_smoke = 0.0
    
    # Mapping Euroclasses -> Scores (Normalisés 0.0 - 1.0)[cite: 2, 4]
    reaction_map = {'A1': 0.0, 'A2': 0.1, 'B': 0.3, 'C': 0.5, 'D': 0.7, 'E': 0.9, 'F': 1.0}
    smoke_map = {'s1': 0.2, 's2': 0.6, 's3': 1.0}

    for comp in building.hasMaterialComposition:
        material = comp.refersToMaterial
        if not material: continue
        
        share = float(comp.materialPercentage or 0.0) / 100.0
        
        # Récupération de la réaction au feu (via fe:hasReaction)[cite: 2]
        reaction_info = material.hasReaction[0] if material.hasReaction else None
        if reaction_info:
            # On extrait le label (ex: "A1 (Incombustible)")
            r_class = reaction_info.hasReactionClass.prefLabel[0] if reaction_info.hasReactionClass else 'A1'
            s_class = reaction_info.hasSmokeClass.prefLabel[0] if reaction_info.hasSmokeClass else 's1'
            
            r_code = r_class.split(' ')[0]
            s_code = s_class.split(' ')[0]
            
            total_combustibility += reaction_map.get(r_code, 0.5) * share
            total_smoke += smoke_map.get(s_code, 0.5) * share

    # --- 2. ANALYSE DU STYLE ARCHITECTURAL (Exploitation du Thésaurus) ---
    style = building.hasArchitectureStyle[0] if building.hasArchitectureStyle else None
    
    # Extraction des coefficients maintenant stockés en ontologie
    frag_coeff = float(get_inherited_value(style, "structuralFragility", 1.0))
    exp_factor = float(get_inherited_value(style, "fireExpansionFactor", 1.0))
    inertia_base = float(get_inherited_value(style, "thermalInertiaScore", 0.5))

    # --- 3. CALCUL DES INDICATEURS FINAUX[cite: 1] ---
    
    # Combustibilité globale (Matériaux seuls)
    risk.buildingCombustibility = float(total_combustibility)
    
    # Propension aux fumées
    risk.smokePropensity = float(total_smoke)
    
    # Facteur d'expansion (Hérité du style : ex 2.5 pour Haussmannien via l'effet cheminée)
    risk.fireExpansionFactor = float(exp_factor)
    
    # Fragilité structurelle : Croisement Matériaux * Fragilité intrinsèque du style
    # (ex: Un style Eiffel en acier montera très haut car l'acier perd sa rigidité)
    risk.structuralFragility = float(total_combustibility * frag_coeff)
    
    # Inertie thermique : Basée sur le style et réduite par la combustibilité des matériaux[cite: 1]
    risk.thermalInertiaScore = float(max(0, inertia_base - (total_combustibility * 0.4)))

    return risk