from owlready2 import *

# Cache interne pour la session de calcul
_TAXON_CACHE = {}

def is_combustible_organism(taxon):
    """
    Vérifie si le taxon appartient aux règnes Plantae ou Fungi.
    Cette fonction permet d'isoler la logique thermique des taxons mobiles (animaux).
    """
    # Récupération de l'ascendance complète du taxon
    lineage = [a.name for a in taxon.ancestors()]
    
    # Liste des racines taxinomiques autorisant un calcul de combustion physique
    authorized_keys = ["Plantae", "Fungi", "Végétal", "Champignon"]
    
    return any(key in lineage for key in authorized_keys)

def get_filtered_inherited_traits(entity, property_name):
    """Récupère les traits hérités en gérant les exceptions (isExceptionTo)."""
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

def compute_reactivity_factor(taxon, sensi):
    """Calcule et écrit le facteur de réactivité pour un taxon donné."""
    aiding_traits = get_filtered_inherited_traits(taxon, "hasFireAidingTrait")
    
    t_ref, d_ref = 400.0, 600.0
    min_threshold, min_delay = 400.0, 600.0

    for t in aiding_traits:
        t_physic = float(getattr(t, "spontaneousIgnitionThreshold", 400.0) or 400.0)
        d_physic = float(getattr(t, "ignitionDelay", 600.0) or 600.0)
        
        exposure = 1.0
        if hasattr(t, "hasrecommendedMaintenance"):
            maint = [float(p.maintenanceEfficiency or 0.0) for p in t.hasrecommendedMaintenance if getattr(p, "isMaintained", False)]
            if maint: exposure = 1.0 - max(maint)

        t_eff = t_physic + ((t_ref - t_physic) * (1.0 - exposure))
        d_eff = d_physic + ((d_ref - d_physic) * (1.0 - exposure))

        min_threshold = min(min_threshold, t_eff)
        min_delay = min(min_delay, d_eff)

    i_seuil = t_ref / max(100.0, min_threshold) 
    i_delai = 1.0 + (5.0 / (min_delay + 5.0))
    
    factor = float(i_seuil * i_delai)
    sensi.ReactivityFactor = factor
    return factor

def compute_taxon_full_indices(taxon):
    """
    Calcule tous les indices comportementaux pour un taxon unique.
    N'exécute le calcul que si l'organisme est de type végétal ou fongique.
    """
    # --- TEST SUR LE TYPE D'ORGANISME ---
    if not taxon or not is_combustible_organism(taxon):
        return None

    if not hasattr(taxon, "hasFireSensitivity") or not taxon.hasFireSensitivity:
        return None

    # Utilisation du cache pour éviter la redondance
    if taxon.name in _TAXON_CACHE:
        return _TAXON_CACHE[taxon.name]

    sensi = taxon.hasFireSensitivity[0]

    # 1. Base organique (HRP)
    hrp_base = 0.0
    for cls in taxon.ancestors():
        if hasattr(cls, "organicHRPBasis"): 
            hrp_base = float(cls.organicHRPBasis or 0.0)
            if hrp_base > 0: break

    # 2. Accumulation des traits
    hrp_p = hrp_m = vt_p = vt_m = ht_p = ht_m = 0.0
    sensi.calculatedHorizontalBarrierPotential = 0.0
    sensi.calculatedVerticalBarrierPotential = 0.0

    # Aiding Traits
    for t in get_filtered_inherited_traits(taxon, "hasFireAidingTrait"):
        impact = 1.0
        if hasattr(t, "hasrecommendedMaintenance"):
            maint = [float(p.maintenanceEfficiency or 0.0) for p in t.hasrecommendedMaintenance if getattr(p, "isMaintained", False)]
            if maint: impact = 1.0 - max(maint)
        
        hrp_p += (float(getattr(t, "heatReleasePotential", 0.0) or 0.0) * impact)
        vt_p += (float(getattr(t, "verticalTransferPotential", 0.0) or 0.0) * impact)
        ht_p += (float(getattr(t, "horizontalTransferPotential", 0.0) or 0.0) * impact)

    # Resisting Traits
    for t in get_filtered_inherited_traits(taxon, "hasFireResistingTrait"):
        hrp_m += float(getattr(t, "heatReleasePotential", 0.0) or 0.0)
        vt_m += float(getattr(t, "verticalTransferPotential", 0.0) or 0.0)
        ht_m += float(getattr(t, "horizontalTransferPotential", 0.0) or 0.0)
        
        res_dur = float(getattr(t, "fireResistanceDuration", 0.0) or 0.0)
        sensi.calculatedHorizontalBarrierPotential += (res_dur * 0.7)
        sensi.calculatedVerticalBarrierPotential += (res_dur * 0.3)

    # 3. Synthèse et écriture
    f_reac = compute_reactivity_factor(taxon, sensi)
    
    total_hrp = max(0.0, (hrp_base + hrp_p) - hrp_m)
    total_vt = max(0.0, vt_p - vt_m)
    total_ht = max(0.0, ht_p - ht_m)

    sensi.calculatedHeatReleasePotential = float(total_hrp)
    sensi.calculatedVerticalTransferPotential = float(total_vt)
    sensi.calculatedHorizontalTransferPotential = float(total_ht)
    
    risk_cinetique = (total_hrp * 0.3) + (total_vt * 0.5) + (total_ht * 0.2)
    sensi.calculatedGeneralFireRisk = float(risk_cinetique * f_reac)

    _TAXON_CACHE[taxon.name] = f_reac
    return f_reac