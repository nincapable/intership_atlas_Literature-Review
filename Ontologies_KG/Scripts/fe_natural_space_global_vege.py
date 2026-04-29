from owlready2 import *

# --- CONFIGURATION ---
ONTO_PATH = "../Modules/fe_natural_space_updated.ttl"
OUTPUT_PATH = "../Modules/fe_natural_space_final.ttl"

def compute_natural_space_indices(onto):
    print("--- Agrégation des indices pour les Espaces Naturels ---")
    
    for ns in onto.NaturalSpace.instances():
        total_ignition = 0.0
        total_velocity = 0.0
        total_barrier = 0.0
        total_share = 0.0

        # Accès aux mesures de biomasse
        for meas in ns.hasBiomassState:
            for component in meas.hasComponent:
                taxon = component.refersToTaxon
                if not taxon or not taxon.hasFireSensitivity:
                    continue

                sensi = taxon.hasFireSensitivity[0]
                # Récupération du pourcentage (0.0 à 100.0)
                share = float(getattr(component, "percentageShare", 0.0) or 0.0)
                if share <= 0: continue
                
                weight = share / 100.0
                total_share += share

                # 1. Calcul Probabilité d'Ignition Globale
                # Valette (0-5) * Facteur de Réactivité
                valette = float(getattr(sensi, "ValetteScore", 2) or 2)
                reactivity = float(getattr(sensi, "ReactivityFactor", 1.0) or 1.0)
                total_ignition += (valette * reactivity) * weight

                # 2. Calcul Vélocité de Propagation
                # Moyenne des transferts (H + V)
                v_trans = float(getattr(sensi, "calculatedVerticalTransferPotential", 0.0) or 0.0)
                h_trans = float(getattr(sensi, "calculatedHorizontalTransferPotential", 0.0) or 0.0)
                total_velocity += ((v_trans + h_trans) / 2.0) * weight

                # 3. Calcul Effet Barrière Structural
                # Capacité de résistance physique
                v_bar = float(getattr(sensi, "calculatedVerticalBarrierPotential", 0.0) or 0.0)
                h_bar = float(getattr(sensi, "calculatedHorizontalBarrierPotential", 0.0) or 0.0)
                total_barrier += (v_bar + h_bar) * weight

        # Normalisation si le total des parts n'est pas exactement 100%
        if total_share > 0:
            norm = 100.0 / total_share
            ns.globalIgnitionProbability = float(total_ignition * norm)
            ns.firePropagationVelocity = float(total_velocity * norm)
            ns.structuralFireBarrierEffect = float(total_barrier * norm)
            
            print(f"Espace: {ns.name}")
            print(f"  - Ignition Globale: {ns.globalIgnitionProbability:.2f}")
            print(f"  - Vélocité Prop.:  {ns.firePropagationVelocity:.2f}")
            print(f"  - Effet Barrière:  {ns.structuralFireBarrierEffect:.2f}")

def run():
    # Chargement de l'ontologie mise à jour par le script précédent
    onto = get_ontology(ONTO_PATH).load()
    
    compute_natural_space_indices(onto)
    
    # Sauvegarde finale
    onto.save(file=OUTPUT_PATH, format="turtle")
    print(f"\n--- Calculs terminés. Fichier sauvegardé : {OUTPUT_PATH} ---")

if __name__ == "__main__":
    run()