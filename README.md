# ATLAS — Revue de littérature et ontologie de gestion de crise

Ce dépôt rassemble les travaux réalisés autour du projet **ATLAS** : revue de littérature, ontologie modulaire pour la gestion des incendies et de l'évacuation, contraintes SHACL, thésaurus et prototype d'échange de données avec des systèmes multi-agents (SMA).

## Contenu du dépôt

```text
.
├── Global/                         # Rapport et états de l'art multilingues
├── Material_for_Litterature_review/ # Corpus documentaire ARCH, C2IMPRESS et CIDOC CRM
├── Ontologies_KG/                  # Livrable technique principal
│   ├── Ontologie_OWL/              # Modules RDF/OWL du domaine
│   ├── Constraints/                # Règles de validation SHACL
│   ├── Thesaurus/                  # Vocabulaires contrôlés SKOS/RDF
│   ├── Profiles/                   # Profils déclaratifs des SMA
│   ├── Request/                    # Modèles et requêtes SPARQL générées
│   ├── Scripts/                    # Génération et conversion RDF/CSV/SPARQL
│   ├── Tests/                      # Tests automatisés
│   └── Docs/                       # Documentation scientifique et pratique
├── Reunions/                       # Préparations et comptes rendus
├── translate.py                    # Traduction des états de l'art
└── mapping_file_names.yaml         # Noms des traductions produites
```

Le point d'entrée conceptuel de l'ontologie est [`Ontologies_KG/Ontologie_OWL/fe_core.ttl`](Ontologies_KG/Ontologie_OWL/fe_core.ttl). Les modules couvrent notamment les sites patrimoniaux, bâtiments, axes, populations, aléas, impacts, météo, victimes, espaces naturels et simulations.

## Prérequis et installation

- Python 3.10 ou supérieur ;
- `pip` ;
- un environnement virtuel est recommandé.

```bash
python -m venv .venv
```

Activation sous Linux ou macOS :

```bash
source .venv/bin/activate
```

Activation sous Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

Installation des dépendances :

```bash
python -m pip install -r requirements.txt
```

## Vérification du livrable

Depuis la racine du dépôt :

```bash
python -m unittest discover -s Ontologies_KG/Tests -v
```

Les tests vérifient notamment la syntaxe des fichiers Turtle et SHACL, le chargement des profils SMA, la génération des requêtes et les conversions CSV/SPARQL.

Une validation SHACL peut également être lancée sur un jeu de données :

```bash
pyshacl -s Ontologies_KG/Constraints/evacuation_sma_input_shape.ttl -d chemin/vers/donnees.ttl
```

## Chaîne d'échange avec un SMA

Le prototype utilise RDF comme modèle interne et CSV comme format d'échange avec les simulateurs :

```text
Profil RDF → requêtes SPARQL → graphe de connaissances → CSV d'entrée
            → simulation SMA → CSV de résultats → SPARQL INSERT → graphe de résultats
```

### 1. Générer les requêtes et fichiers de mapping

```bash
python Ontologies_KG/Scripts/generate_sma_queries.py \
  Ontologies_KG/Profiles/evacuation_sma_profile.ttl \
  --out-dir Ontologies_KG/Request/generated \
  --template-dir Ontologies_KG/Request/Templates
```

### 2. Exporter les données du graphe vers CSV

```bash
python Ontologies_KG/Scripts/export_sma_input_csv.py \
  --profile Ontologies_KG/Profiles/evacuation_sma_profile.ttl \
  --data chemin/vers/kg.ttl \
  --out exports/evacuation_sma_input.csv
```

### 3. Convertir les résultats du SMA en SPARQL

```bash
python Ontologies_KG/Scripts/import_sma_results_csv.py \
  --profile Ontologies_KG/Profiles/evacuation_sma_profile.ttl \
  --csv exports/evacuation_sma_results.csv \
  --out Ontologies_KG/Request/generated/evacuation_sma_results_insert.sparql
```

La documentation détaillée du flux, des colonnes CSV et de la création de nouveaux profils se trouve dans [`Ontologies_KG/Docs/SMA_Query_Generator.md`](Ontologies_KG/Docs/SMA_Query_Generator.md).

## Documentation

- [État de l'art](Ontologies_KG/Docs/Etat_de_l_Art/Etat_de_art_pour_projet_ATLAS%20.md)
- [Guide utilisateur SMA](Ontologies_KG/Docs/Guide_et_Documentation_Pratique/Guide_Utilisateurs_SMA.md)
- [Guide de spécialisation pour les chercheurs](Ontologies_KG/Docs/Guide_et_Documentation_Pratique/Guide_Specialisation_Chercheurs.md)
- [Documentation de reprise de l'ontologie](Ontologies_KG/Docs/Guide_et_Documentation_Pratique/Documentation_Repreneur_Ontologie.md)

## Traduction des documents

`translate.py` traduit le document français déclaré dans `mapping_file_names.yaml` vers l'anglais, l'espagnol et l'allemand à l'aide d'Argos Translate. Les modèles de langue manquants sont téléchargés au premier lancement :

```bash
python translate.py
```

Cette commande nécessite donc un accès réseau lors de l'installation initiale des modèles.

## État et limites

Le dépôt contient un **prototype de recherche**. La résolution complète des imports OWL, la génération automatique de shapes SHACL à partir des profils et l'intégration directe à un moteur de simulation ne sont pas encore automatisées. Les fichiers sous `Request/generated/` sont conservés comme exemples reproductibles et peuvent être régénérés à partir du profil fourni.

## Licence et réutilisation

Aucune licence n'est actuellement déclarée dans ce dépôt. En l'absence de fichier `LICENSE`, toute réutilisation ou diffusion doit être autorisée par les responsables du projet et respecter les droits associés aux documents tiers du corpus bibliographique.
