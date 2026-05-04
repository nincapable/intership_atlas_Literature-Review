from owlready2 import *

# Cache interne pour la session de calcul
_ANIMAL_CACHE = {}

def get_inherited_value(entity, property_name, default_value):
    """
    Parcourt les ancêtres du taxon du plus proche (soi-même) au plus lointain.
    S'arrête et retourne la première valeur trouvée (logique de la feuille).
    """
    # .ancestors() inclut l'entité elle-même
    for cls in entity.ancestors():
        if hasattr(cls, property_name):
            val = getattr(cls, property_name)
            if val is not None:
                # Si c'est une liste (cas fréquent en owlready), on prend le premier
                if isinstance(val, (list, iterators.IndirectList)):
                    if len(val) > 0: return val[0]
                else:
                    return val
    return default_value

def compute_animal_indices(taxon):
    """
    Calcule les indices de risque et de transfert pour un taxon animal.
    Base sa logique sur la mobilité, le stress et la dangerosité vectorielle.
    """
    if not taxon or not hasattr(taxon, "hasFireSensitivity") or not taxon.hasFireSensitivity:
        return 1.0

    if taxon.name in _ANIMAL_CACHE:
        return _ANIMAL_CACHE[taxon.name]

    sensi = taxon.hasFireSensitivity[0]

    # --- RÉCUPÉRATION DES CARACTÉRISTIQUES (Logique Héritée de la Feuille) ---
    
    # Propriétés portées par la sensibilité (ou ses ancêtres de sensibilité)
    m_score = float(get_inherited_value(sensi, "mobilityScore", 0.5))
    p_threshold = float(get_inherited_value(sensi, "panicThreshold", 0.5))
    e_priority = int(get_inherited_value(sensi, "evacuationPriority", 3))

    # Propriété de transfert portée par le Taxon (ou ses classes parentes)
    v_score = float(get_inherited_value(taxon, "fireVectorScore", 0.0))

    # --- LOGIQUE DE CALCUL ---

    # 1. Facteur de Réactivité (Comportemental)
    # Plus la mobilité est faible et le seuil de panique élevé, plus l'animal est "réactif" au danger
    # On ajoute le v_score car un vecteur actif augmente la dangerosité immédiate
    f_reac = p_threshold #associé à l'instabilité (panique)
    sensi.ReactivityFactor = float(f_reac)

    # 2. Potentiels de Transfert (Spotting / Saute de feu)
    # L'animal n'a pas de VT (vertical) ou de barrière, mais il est un vecteur horizontal
    # Le transfert dépend de sa dangerosité (v_score) et de sa capacité à se déplacer (m_score)
    sensi.calculatedHorizontalTransferPotential = float(v_score * m_score * 10.0)
    sensi.calculatedVerticalTransferPotential = 0.0
    
    # Initialisation des barrières à 0 pour éviter les erreurs dans l'agrégateur global
    sensi.calculatedHorizontalBarrierPotential = 0.0
    sensi.calculatedVerticalBarrierPotential = 0.0

    # 3. Risque Général (Vulnérabilité vs Priorité)
    # Combine la réactivité, le score de vecteur et l'importance d'évacuation
    risk = (f_reac * e_priority) + (v_score * 5.0)
    sensi.calculatedGeneralFireRisk = float(risk)

    _ANIMAL_CACHE[taxon.name] = f_reac
    return f_reac