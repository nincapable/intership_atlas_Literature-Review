from owlready2 import *

# --- CONFIGURATION ---
ONTO_PATH = "../Modules/fe_natural_space.ttl"
THESAURUS_PATH = "../Thesaurus/fe_thesaurus_especes.ttl"

def load_data():
    try:
        onto = get_ontology(ONTO_PATH).load()
        thesaurus = get_ontology(THESAURUS_PATH).load()
        return onto, thesaurus
    except Exception as e:
        print(f"❌ Erreur de chargement : {e}")
        return None, None

def get_all_traits(taxon):
    """Récupère les traits et gère les exceptions via la hiérarchie SKOS."""
    traits = set()
    exceptions = set()
    to_visit = [taxon]
    visited = set()
    
    relations = ["hasFireAidingTrait", "hasFireResistingTrait", "hasFireResponseStrategy", "hasEmberType", "hasFireFunctionalRole"]

    while to_visit:
        current = to_visit.pop()
        if current in visited: continue
        visited.add(current)

        for prop in relations:
            if hasattr(current, prop):
                traits.update(getattr(current, prop))
        
        if hasattr(current, "isExceptionTo"):
            exceptions.update(getattr(current, "isExceptionTo"))

        if hasattr(current, "broader"):
            to_visit.extend(current.broader)

    return [t for t in traits if t not in exceptions]

def compute_weakness_analysis(taxon, sensi):
    """
    Analyse de vulnérabilité biophysique :
    Détermine le point de rupture le plus bas entre la matière organique de base
    et les faiblesses apportées par les traits.
    """
    traits = get_all_traits(taxon)
    
    # 1. RÉCUPÉRATION DU SOCLE BIOLOGIQUE
    # Défaut à 450.0 si non renseigné (Base Plantae standard)
    t_basis = float(getattr(taxon, "organicIgnitionBasis", 450.0) or 450.0)

    # 2. RÉPARTITION FONCTIONNELLE DES TRAITS
    sources = [] # Traits avec potentiel énergétique (HRP)
    passives = [] # Traits de vulnérabilité simple (sans HRP)
    
    for t in traits:
        hrp = float(getattr(t, "heatReleasePotential", 0.0) or 0.0)
        ign = float(getattr(t, "spontaneousIgnitionThreshold", 0.0) or 0.0)
        
        if hrp != 0:
            sources.append({"ign": ign, "hrp": hrp})
        elif ign != 0:
            passives.append(ign)

    # 3. CALCUL DU POINT DE RUPTURE (Calcul de la Faiblesse)
    
    # Le seuil initial est la base organique (ex: 450 pour bois, 190 pour animal)
    final_ignition = t_basis

    # A. Loi du Maillon Faible (Vulnérabilités passives)
    # Si un organe ou un trait passif est plus sensible que la base, il devient le nouveau seuil.
    if passives:
        min_passive = min(passives)
        if min_passive < final_ignition:
            final_ignition = min_passive

    # B. Loi de la Cascade Énergétique (Sources actives)
    # Si une source (ex: résine, graisse) a un HRP suffisant, elle force la rupture.
    if sources:
        sources.sort(key=lambda x: x["ign"])
        # Seuil de rupture : l'HRP doit vaincre 20% de l'inertie de la base
        breaking_point = t_basis * 0.20 
        
        for s in sources:
            if s["hrp"] > breaking_point:
                # Si la source offre un allumage plus précoce que le seuil actuel
                if s["ign"] < final_ignition:
                    final_ignition = s["ign"]
                    break

    # 4. AGGRÉGATION DES POTENTIELS ET CALCUL DES INDICES CALCULÉS
    def sum_prop(prop_name):
        return sum(float(getattr(t, prop_name, 0.0) or 0.0) for t in traits)

    total_hrp = sum_prop("heatReleasePotential")
    v_trans = sum_prop("verticalTransferPotential")
    h_trans = sum_prop("horizontalTransferPotential")

    # Injection dans l'ontologie
    sensi.calculatedIgnitionThreshold = final_ignition
    sensi.calculatedHeatReleasePotential = total_hrp
    sensi.calculatedVerticalTransferPotential = v_trans
    sensi.calculatedHorizontalTransferPotential = h_trans
    
    # Calcul du risque général : Pondération (Puissance + Propagation)
    sensi.calculatedGeneralFireRisk = (total_hrp * 0.4) + (v_trans * 0.4) + (h_trans * 0.2)
    
    # Niveau d'inflammabilité normalisé (0 à 100)
    # Plus le seuil est bas, plus l'inflammabilité est haute.
    sensi.calculatedFlammabilityLevel = max(0, min(100, (600 - final_ignition) / 4))

    return final_ignition

def main():
    onto, thesaurus = load_data()
    if not onto: return

    print(f"{'Taxon':<25} | {'Base Bio':<10} | {'Ign. Calc':<10} | {'Risk':<8}")
    print("-" * 65)

    for taxon in thesaurus.Taxon.instances():
        if hasattr(taxon, "hasFireSensitivity") and taxon.hasFireSensitivity:
            sensi = taxon.hasFireSensitivity[0]
            ign_calc = compute_weakness_analysis(taxon, sensi)
            
            t_basis = float(getattr(taxon, "organicIgnitionBasis", 450.0) or 450.0)
            print(f"{taxon.name[:24]:<25} | {t_basis:>8.1f} | {ign_calc:>8.1f} | {sensi.calculatedGeneralFireRisk:>7.1f}")

    # Sauvegarde
    onto.save(file="fe_systemic_results.ttl", format="ntriples")
    print(f"\n✅ Analyse de faiblesse terminée. Résultats sauvegardés.")

if __name__ == "__main__":
    main()