from owlready2 import *

# 1. Chargement de l'ontologie
onto_path.append(".") # Dossier local
onto = get_ontology("natural_space.ttl").load()
thesaurus = get_ontology("thesaurus_especes.ttl").load()

def get_full_lineage(taxon):
    """Remonte la hiérarchie SKOS de manière récursive."""
    lineage = [taxon]
    # On cherche le parent via skos:broader
    # Note : Dans Owlready2, les propriétés SKOS sont accessibles 
    # via l'espace de noms du thésaurus
    parents = taxon.broader
    for parent in parents:
        lineage.extend(get_full_lineage(parent))
    return lineage

def calculate_hrp(taxon_instance):
    """Calcule le potentiel de dégagement de chaleur global."""
    
    # Valeur initiale (base neutre)
    total_hrp = 0.0
    traits_trouves = []

    # 1. Récupérer la lignée (Taxon -> Genre -> ... -> Reign)
    lignee = get_full_lineage(taxon_instance)
    
    # 2. Parcourir chaque niveau pour collecter les traits
    for niveau in lignee:
        # On récupère les traits d'aide et de résistance
        # Grâce à ton rdfs:domain fe:BioDivision, ces propriétés sont accessibles
        traits = []
        if hasattr(niveau, "hasFireAidingTrait"):
            traits.extend(niveau.hasFireAidingTrait)
        if hasattr(niveau, "hasFireResistingTrait"):
            traits.extend(niveau.hasFireResistingTrait)
            
        for trait in traits:
            # On récupère la valeur de heatReleasePotential sur le trait
            # On vérifie si la propriété existe sur ce trait précis
            if hasattr(trait, "heatReleasePotential") and trait.heatReleasePotential is not None:
                valeur = float(trait.heatReleasePotential)
                total_hrp += valeur
                traits_trouves.append(f"{trait.name} ({valeur})")

    # 3. Mettre à jour la fiche de sensibilité du Taxon
    # On suppose qu'un taxon a une propriété hasFireSensitivity
    if taxon_instance.hasFireSensitivity:
        sensi_obj = taxon_instance.hasFireSensitivity[0]
        sensi_obj.calculatedHeatReleasePotential = total_hrp
        
        print(f"--- Calcul pour {taxon_instance.name} ---")
        print(f"Traits cumulés : {', '.join(traits_trouves)}")
        print(f"Résultat Final : {total_hrp}")
    else:
        print(f"Erreur : Pas de fiche de sensibilité pour {taxon_instance.name}")

# --- EXEMPLE D'UTILISATION ---
# Supposons que fe:PinusHalepensis soit un individu dans ton ontologie
pin_alep = onto.PinusHalepensis
calculate_hrp(pin_alep)

# Sauvegarder les résultats dans un nouveau fichier
onto.save(file="natural_space_calculated.ttl", format="ntriples")