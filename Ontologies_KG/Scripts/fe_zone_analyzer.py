from owlready2 import *

def compute_zone_indices(zone):
    """
    Calcule trois indices distincts pour la zone afin de guider 
    les différentes unités d'intervention.
    """
    # 1. INDICE DE SAUVEGARDE PATRIMONIALE (Artefacts)
    # Reflète la valeur et l'urgence de ce qui doit être sorti.
    artefact_index = 0.0
    for art in zone.containsArtefact:
        prio_level = art.hasProtectionPriority[0] if art.hasProtectionPriority else None
        if prio_level:
            # P1=100, P2=10, P3=1
            score = float(getattr(prio_level, "priorityScore", 0))
            # On peut aussi ajouter un multiplicateur de fragilité ici
            artefact_index += score

    # 2. INDICE D'URGENCE ÉCOLOGIQUE (Espaces Naturels & Espèces)
    # Reflète la rareté biologique et la vulnérabilité du vivant.
    ecological_index = 0.0
    for ns in zone.containsNaturalSpace:
        biomass = ns.hasBiomassState[0] if ns.hasBiomassState else None
        if biomass:
            for component in biomass.hasComponent:
                taxon = component.refersToTaxon
                share = float(getattr(component, "percentageShare", 1.0))
                sensitivity = taxon.hasbioFireSensitivity[0] if taxon.hasbioFireSensitivity else None
                if sensitivity:
                    status = sensitivity.hasProtectionStatus
                    weight = float(getattr(status, "protectionPriorityWeight", 0.0))
                    # On pondère par la part de l'espèce dans la zone
                    ecological_index += (weight * share)

    # 3. INDICE DE PÉRIL STRUCTUREL (Bâtiments)
    # Reflète le danger physique et l'importance de l'enveloppe bâtie.
    structural_index = 0.0
    for bld in zone.containsBuilding:
        risk_data = bld.hasBuildingFireRisk[0] if bld.hasBuildingFireRisk else None
        if risk_data:
            fragility = float(getattr(risk_data, "structuralFragility", 0.0))
            # On remonte l'indice sur une échelle comparable (ex: 0-100)
            structural_index += (fragility * 100)

    # Enregistrement des indices séparés dans la base
    zone.patrimonialUrgencyIndex = artefact_index
    zone.ecologicalUrgencyIndex = ecological_index
    zone.structuralDangerIndex = structural_index

    return {
        "Patrimoine": artefact_index,
        "Ecologie": ecological_index,
        "Structure": structural_index
    }