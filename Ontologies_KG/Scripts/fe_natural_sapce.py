from owlready2 import *

# 1. Chargement de l'ontologie
onto_path.append(".") # Dossier local
onto = get_ontology("../Modules/fe_natural_space.ttl").load()
thesaurus = get_ontology("../Thesaurus/fe_thesaurus_especes.ttl").load()

def get_all_traits_with_exceptions(taxon_instance):
    traits_potentiels = set()
    exceptions = set()
    a_visiter = [taxon_instance]
    visites = set()

    while a_visiter:
        actuel = a_visiter.pop()
        if actuel in visites: continue
        visites.add(actuel)

        # 1. Collecter les traits normaux
        for prop in ["hasFireAidingTrait", "hasFireResistingTrait"]:
            if hasattr(actuel, prop):
                traits_potentiels.update(getattr(actuel, prop))
        
        # 2. Collecter les exceptions déclarées à ce niveau
        if hasattr(actuel, "isExceptionTo"):
            exceptions.update(getattr(actuel, "isExceptionTo"))

        # 3. Remonter
        if hasattr(actuel, "broader"):
            a_visiter.extend(actuel.broader)

    # Filtrage final : on ne garde que les traits qui ne sont pas dans les exceptions
    traits_finaux = [t for t in traits_potentiels if t not in exceptions]
    
    return traits_finaux

def calculate_hrp_optimized(taxon_instance):
    """Calcule le HRP en une seule passe sur les traits collectés, sans les exceptions."""
    
    # Correction du nom de la fonction appelée
    tous_les_traits = get_all_traits_with_exceptions(taxon_instance)
    
    # Calcul de la somme des potentiels calorifiques
    # On force le float pour s'assurer de la compatibilité xsd:decimal
    total_hrp = sum(
        float(t.heatReleasePotential) 
        for t in tous_les_traits 
        if hasattr(t, "heatReleasePotential") and t.heatReleasePotential is not None
    )

    # Injection du résultat dans la fiche de sensibilité
    if hasattr(taxon_instance, "hasFireSensitivity") and taxon_instance.hasFireSensitivity:
        sensi = taxon_instance.hasFireSensitivity[0]
        sensi.calculatedHeatReleasePotential = total_hrp
        print(f"Calculé : {total_hrp} pour {taxon_instance.name}")
        print(f"Traits retenus : {[t.name for t in tous_les_traits]}")
    else:
        print(f"Attention : {taxon_instance.name} n'a pas de fiche de sensibilité rattachée.")