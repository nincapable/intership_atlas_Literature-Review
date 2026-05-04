from owlready2 import *

def get_inherited_value(entity, property_name, default_value):
    """Récupère une valeur sur l'individu ou ses ancêtres (Classes)."""
    if hasattr(entity, property_name):
        val = getattr(entity, property_name)
        if val: return val[0] if isinstance(val, list) else val
    
    for cls in entity.is_a:
        if hasattr(cls, property_name):
            val = getattr(cls, property_name)
            if val: return val[0] if isinstance(val, list) else val
    return default_value

def compute_building_indices(building):
    """
    Calcule les scores de risque pour un bâtiment.
    Croise les Matériaux (Réaction au feu) et le Style (Fragilité).
    """
    # Initialisation de l'objet de risque
    risk = building.hasBuildingFireRisk[0] if building.hasBuildingFireRisk else None
    if not risk: return

    # --- 1. ANALYSE DES MATÉRIAUX ---
    total_combustibility = 0.0
    total_smoke = 0.0
    
    # Mapping Euroclasses -> Scores numériques (Normalisés 0-1)
    # A1=0 (Incombustible), F=1 (Très inflammable)
    reaction_map = {'A1': 0.0, 'A2': 0.1, 'B': 0.3, 'C': 0.5, 'D': 0.7, 'E': 0.9, 'F': 1.0}
    smoke_map = {'s1': 0.2, 's2': 0.6, 's3': 1.0}

    for comp in building.hasMaterialComposition:
        material = comp.refersToMaterial
        share = float(comp.materialPercentage or 0.0) / 100.0
        
        # Récupération de la réaction au feu via l'ObjectProperty hasReaction
        reaction_info = material.hasReaction[0] if material.hasReaction else None
        if reaction_info:
            r_class = reaction_info.hasReactionClass.prefLabel[0] if reaction_info.hasReactionClass else 'A1'
            s_class = reaction_info.hasSmokeClass.prefLabel[0] if reaction_info.hasSmokeClass else 's1'
            
            # Extraction du code (ex: "A1" de "A1 (Incombustible)")
            r_code = r_class.split(' ')[0]
            s_code = s_class.split(' ')[0]
            
            total_combustibility += reaction_map.get(r_code, 0.5) * share
            total_smoke += smoke_map.get(s_code, 0.5) * share

    # --- 2. ANALYSE DU STYLE ARCHITECTURAL (Fragilité) ---
    # On définit des coefficients de fragilité par style (Exemple logique)
    style = building.hasArchitectureStyle[0] if building.hasArchitectureStyle else None
    
    # Multiplicateurs de fragilité structurelle (0.1 à 2.0)
    # Gothique (poussées latérales sensibles) > Roman (murs épais)
    style_fragility_map = {
        "Gothique": 1.5,
        "Roman": 0.8,
        "Maison à Pan de Bois / Colombage": 1.8, # Bois + Torchis
        "Haussmannien": 1.0,
        "Brutalisme": 0.5, # Béton massif
        "Gallo-Romain": 0.4
    }
    
    style_label = style.prefLabel[0] if style else "Standard"
    fragility_coeff = style_fragility_map.get(style_label, 1.0)

    # --- 3. MISE À JOUR DES INDICES ---
    risk.buildingCombustibility = float(total_combustibility)
    risk.smokePropensity = float(total_smoke)
    
    # La fragilité dépend du matériau (acier qui fond vs pierre) * style
    risk.structuralFragility = float(total_combustibility * fragility_coeff)
    
    # Inertie thermique : inverse de la combustibilité et du style (pierre épaisse = haute inertie)
    risk.thermalInertiaScore = float(1.0 - (total_combustibility * 0.5) - (fragility_coeff * 0.2))

    return risk