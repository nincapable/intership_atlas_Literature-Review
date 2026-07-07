# Générateur de requêtes SPARQL pour l'initialisation et le déchargement SMA

Ce document décrit le prototype ajouté pour connecter l'ontologie `Fuse/` à des systèmes multi-agents (SMA). L'objectif n'est pas de faire charger toute l'ontologie à chaque simulateur, mais de permettre à chaque SMA de déclarer un profil d'entrée/sortie, puis de générer automatiquement les requêtes SPARQL correspondant à ce profil.

## Vue d'ensemble

Le flux visé est le suivant :

```text
Profil SMA RDF
    -> rdflib
        -> génération de requêtes CONSTRUCT / SELECT
            -> CSV d'entrée SMA
                -> SMA exécute la simulation
                    -> CSV de résultats SMA
                        -> mapping CSV vers RDF
                            -> SPARQL INSERT / RDF output
                                -> Knowledge Graph
```

Les fichiers principaux sont :

```text
Fuse/fe_simulation.ttl
Profiles/evacuation_sma_profile.ttl
Scripts/generate_sma_queries.py
Request/Templates/sma_init_construct_template.sparql
Request/Templates/sma_init_select_template.sparql
Request/Templates/sma_result_insert_template.sparql
Request/generated/evacuation_sma_init_construct.sparql
Request/generated/evacuation_sma_init_select.sparql
Request/generated/evacuation_sma_result_insert.sparql
Request/generated/evacuation_sma_input_mapping.json
Request/generated/evacuation_sma_output_mapping.json
Request/generated/evacuation_sma_results_example.csv
Scripts/export_sma_input_csv.py
Scripts/import_sma_results_csv.py
Constraints/evacuation_sma_input_shape.ttl
```

## Rôle de `fe_simulation.ttl`

Le module `Fuse/fe_simulation.ttl` définit deux familles de concepts.

La première famille décrit le cycle d'exécution d'une simulation :

```ttl
fe:SimulationScenario
fe:SimulationRun
fe:SimulationAgent
fe:SimulationInput
fe:SimulationOutput
fe:StateSnapshot
fe:InitialState
fe:FinalState
```

Ces classes servent à tracer ce qui a été chargé, quelle simulation a été exécutée, et quels résultats ont été produits.

La deuxième famille décrit les profils SMA :

```ttl
fe:SimulationProfile
fe:profileIdentifier
fe:hasRootClass
fe:requiresClass
fe:requiresProperty
fe:optionalProperty
fe:producesClass
fe:producesProperty
fe:hasExtractionQuery
fe:hasResultInsertionQuery
```

Un profil SMA est un contrat déclaratif. Il indique quelles classes et propriétés le SMA consomme pour s'initialiser, et quelles classes/propriétés il est censé produire en sortie.

## Créer un profil SMA

Un profil se place dans `Profiles/`. Le profil d'exemple est :

```text
Profiles/evacuation_sma_profile.ttl
```

Un profil minimal ressemble à ceci :

```ttl
@prefix fe:   <http://example.org/fire_and_evacuation#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

fe:ExampleSMAProfile a fe:SimulationProfile ;
    rdfs:label "Profil exemple"@fr ;
    fe:profileIdentifier "example_sma" ;
    fe:hasRootClass fe:Zone ;
    fe:requiresClass fe:Zone, fe:Axis ;
    fe:requiresProperty fe:hasPopulation,
        fe:isConnectedTo,
        fe:maxFlowCapacity ;
    fe:optionalProperty fe:hasWeatherCondition,
        fe:hasHazardExposure ;
    fe:producesClass fe:SimulationOutput,
        fe:FinalState ;
    fe:producesProperty fe:hasFinalState,
        fe:stateOfEntity,
        fe:hasSimulationStep .
```

### `fe:profileIdentifier`

Identifiant court utilisé pour nommer les fichiers générés.

Exemple :

```ttl
fe:profileIdentifier "evacuation_sma" .
```

Produit :

```text
Request/generated/evacuation_sma_init_construct.sparql
Request/generated/evacuation_sma_init_select.sparql
Request/generated/evacuation_sma_result_insert.sparql
```

Si l'identifiant est absent, le générateur utilise le nom du fichier profil.

### `fe:hasRootClass`

Indique la classe métier principale du profil. Dans le prototype actuel, cette propriété est documentée mais pas encore utilisée pour restreindre les requêtes générées.

Exemple :

```ttl
fe:hasRootClass fe:Zone .
```

Elle sera utile pour une version plus fine du générateur, par exemple pour construire des requêtes autour d'une zone donnée ou d'un scénario donné.

### `fe:requiresClass`

Liste les classes dont les instances doivent être extraites pour initialiser le SMA.

Exemple :

```ttl
fe:requiresClass fe:Zone, fe:Axis, fe:Population, fe:HazardEvent .
```

Le générateur les injecte dans un bloc SPARQL :

```sparql
VALUES ?class {
  fe:Zone
  fe:Axis
  fe:Population
  fe:HazardEvent
}
```

### `fe:requiresProperty`

Liste les propriétés considérées comme nécessaires au SMA.

Exemple :

```ttl
fe:requiresProperty fe:hasPopulation,
    fe:isConnectedTo,
    fe:maxFlowCapacity,
    fe:hasWidth,
    fe:hasLength .
```

Dans le prototype actuel, ces propriétés sont extraites de façon souple avec `OPTIONAL`, pour ne pas bloquer l'extraction. Le fait qu'elles soient réellement obligatoires est vérifié par SHACL, dans `Constraints/`.

### `fe:optionalProperty`

Liste les propriétés utiles mais non bloquantes.

Exemple :

```ttl
fe:optionalProperty fe:containsBuilding,
    fe:hasWeatherCondition,
    fe:hasBlockingState .
```

Le générateur les ajoute dans le même bloc `VALUES ?property` que les propriétés requises.

### `fe:producesClass` et `fe:producesProperty`

Décrivent ce que le SMA est censé produire en sortie.

Exemple :

```ttl
fe:producesClass fe:SimulationOutput,
    fe:FinalState,
    fe:ImpactAssessment .

fe:producesProperty fe:producesOutput,
    fe:hasFinalState,
    fe:stateOfEntity,
    fe:producesAssessment .
```

Dans la version actuelle, `fe:producesProperty` est utilisé pour générer des commentaires dans le template d'insertion de résultats. Ce n'est pas encore une génération complète de résultats, car les valeurs finales dépendent du SMA.

## Lancer le générateur

Commande de base :

```sh
python3 Scripts/generate_sma_queries.py Profiles/evacuation_sma_profile.ttl
```

Sorties générées :

```text
Request/generated/evacuation_sma_init_construct.sparql
Request/generated/evacuation_sma_init_select.sparql
Request/generated/evacuation_sma_result_insert.sparql
Request/generated/evacuation_sma_input_mapping.json
Request/generated/evacuation_sma_output_mapping.json
Request/generated/evacuation_sma_results_example.csv
```

Options disponibles :

```sh
python3 Scripts/generate_sma_queries.py PROFILE.ttl \
  --out-dir Request/generated \
  --template-dir Request/Templates
```

- `PROFILE.ttl` : chemin du profil SMA à lire.
- `--out-dir` : dossier dans lequel écrire les requêtes générées.
- `--template-dir` : dossier contenant les templates SPARQL.

## Fonctionnement interne du générateur

Le script utilise maintenant `rdflib` pour parser le fichier TTL comme un vrai graphe RDF. Le profil reste simple pour le chercheur, mais l'extraction interne lit les valeurs RDF des prédicats suivants :

```text
fe:profileIdentifier
fe:requiresClass
fe:requiresProperty
fe:optionalProperty
fe:producesProperty
```

Les fonctions principales sont :

```python
load_profile(profile_path)
SimulationProfile
generate_deep_construct(profile)
format_values(values)
generated_name(profile_path, profile_id)
```

`load_profile` charge le TTL avec `Graph().parse(..., format="turtle")`, identifie la ressource `fe:SimulationProfile`, puis convertit les URI en QNames lisibles avec le gestionnaire de namespaces de `rdflib`.

### `load_profile`

Charge le profil comme graphe RDF, trouve l'unique ressource `fe:SimulationProfile`, puis remplit une structure `SimulationProfile`.

### Lecture des valeurs RDF

Les valeurs associées aux prédicats du profil sont lues depuis le graphe RDF, puis normalisées en QNames.

Exemple :

```ttl
fe:requiresClass fe:Zone, fe:Axis, fe:Population .
```

devient :

```python
["fe:Zone", "fe:Axis", "fe:Population"]
```

Le profil peut donc rester écrit dans le style Turtle simple existant, mais la lecture n'est plus dépendante d'expressions régulières.

### Littéraux

`fe:profileIdentifier` et les futurs littéraux simples comme `fe:maxDepth` sont lus comme valeurs RDF, pas comme texte brut.

### `generated_name`

Nettoie l'identifiant de profil pour produire des noms de fichiers sûrs.

Exemple :

```ttl
fe:profileIdentifier "evacuation_sma" .
```

produit :

```text
evacuation_sma_init_construct.sparql
```

## Templates SPARQL

Les templates sont dans :

```text
Request/Templates/
```

Ils utilisent la méthode Python `str.format`. Les variables de template sont donc écrites avec des accolades simples :

```text
{PREFIXES}
{CLASS_VALUES}
{PROPERTY_VALUES}
{INPUT_IRI}
{PRODUCED_PROPERTY_HINTS}
```

Les accolades SPARQL normales doivent être doublées dans le template :

```sparql
CONSTRUCT {{
  ?entity a ?class .
}}
WHERE {{
  ?entity a ?class .
}}
```

Après génération, elles redeviennent :

```sparql
CONSTRUCT {
  ?entity a ?class .
}
WHERE {
  ?entity a ?class .
}
```

## Template `sma_init_construct_template.sparql`

Ce template produit une requête `CONSTRUCT`.

Objectif : extraire un sous-graphe RDF typé pour initialiser le SMA.

Structure générée :

```sparql
CONSTRUCT {
  ?entity a ?class .
  ?entity ?property ?value .
  fe:Input_evacuation_sma a fe:SimulationInput ;
      fe:describesEntity ?entity .
}
WHERE {
  VALUES ?class {
    fe:Zone
    fe:Axis
    fe:Population
    fe:HazardEvent
  }

  VALUES ?property {
    fe:hasPopulation
    fe:isConnectedTo
    fe:maxFlowCapacity
  }

  ?entity a ?class .
  OPTIONAL { ?entity ?property ?value . }
}
```

Utilisation recommandée :

- charger le résultat dans un graphe temporaire ;
- transmettre ce sous-graphe RDF au SMA ;
- garder `fe:Input_<profile>` comme trace de l'entrée de simulation.

## Template `sma_init_select_template.sparql`

Ce template produit une requête `SELECT`.

Objectif : fournir une vue tabulaire du même sous-graphe, plus facile à transformer en JSON ou CSV.

Structure générée :

```sparql
SELECT ?entity ?class ?property ?value
WHERE {
  VALUES ?class { ... }
  VALUES ?property { ... }

  ?entity a ?class .
  OPTIONAL { ?entity ?property ?value . }
}
ORDER BY ?class ?entity ?property
```

Utilisation recommandée :

- adaptateur Python/Java/JS qui transforme les lignes en payload SMA ;
- export CSV pour inspecter rapidement les données chargées ;
- debug du profil d'initialisation.

## CSV comme format pivot SMA

Le SMA ne consomme pas directement RDF ou SPARQL. RDF reste le format interne du KG et `rdflib` sert à parser, typer et convertir. Le format d'échange externe avec les simulateurs est CSV.

### Exporter le CSV d'entrée

Commande :

```sh
python3 Scripts/export_sma_input_csv.py \
  --profile Profiles/evacuation_sma_profile.ttl \
  --data data/kg.ttl \
  --out exports/evacuation_sma_input.csv
```

Le CSV contient les colonnes :

```csv
entity,class,property,value,value_type,value_lang
```

Rôle des colonnes :

- `entity` : URI ou QName de l'entité extraite.
- `class` : classe RDF de l'entité.
- `property` : propriété RDF exportée.
- `value` : valeur textuelle.
- `value_type` : datatype RDF si littéral, `uri` si ressource, `bnode` si noeud blanc.
- `value_lang` : langue du littéral si présente.

Exemple :

```csv
entity,class,property,value,value_type,value_lang
fe:Axis_12,fe:Axis,fe:maxFlowCapacity,150,xsd:integer,
fe:Axis_12,fe:Axis,fe:hasWidth,3.5,xsd:double,
fe:Axis_12,fe:Axis,fe:isConnectedTo,fe:Axis_13,uri,
```

Le script utilise le profil RDF pour savoir quelles classes et propriétés exporter. Les types RDF ne sont pas écrasés en chaînes brutes : les littéraux conservent leur datatype et leur langue.

### Mapping d'entrée

Le générateur produit aussi :

```text
Request/generated/evacuation_sma_input_mapping.json
```

Ce fichier décrit les colonnes du CSV d'entrée et reprend :

```text
required_classes
required_properties
optional_properties
```

Il sert de contrat lisible pour l'adaptateur SMA, sans obliger le simulateur à comprendre RDF.

### CSV de résultats SMA

Le SMA doit produire un CSV de résultats avec les colonnes :

```csv
run_id,scenario_id,input_id,output_id,entity,step,time,property,value,value_type
```

Exemple :

```csv
run_id,scenario_id,input_id,output_id,entity,step,time,property,value,value_type
SimulationRun_001,Scenario_001,Input_evacuation_sma,Output_001,Zone_A,120,600.0,fe:hasFinalStatus,evacuated,xsd:string
SimulationRun_001,Scenario_001,Input_evacuation_sma,Output_001,Zone_A,120,600.0,fe:hasEvacuationTime,540.0,xsd:double
```

Un exemple est généré automatiquement dans :

```text
Request/generated/evacuation_sma_results_example.csv
```

### Importer les résultats CSV vers SPARQL INSERT

Commande :

```sh
python3 Scripts/import_sma_results_csv.py \
  --profile Profiles/evacuation_sma_profile.ttl \
  --csv exports/evacuation_sma_results.csv \
  --out Request/generated/evacuation_sma_results_insert.sparql \
  --result-graph http://example.org/fire_and_evacuation/simulation/results
```

Le script reconstruit :

- les URI stables de `fe:SimulationRun`, `fe:SimulationOutput` et `fe:FinalState` ;
- les liens vers le scénario, l'entrée et l'entité mise à jour ;
- les littéraux typés selon `value_type` ;
- une requête `INSERT DATA` vers un graphe de résultats, sans écraser le graphe source.

### Mapping de sortie

Le générateur produit :

```text
Request/generated/evacuation_sma_output_mapping.json
```

Ce fichier décrit les colonnes attendues du CSV de résultats, les propriétés produites par le profil, les datatypes usuels et les règles de génération d'URI.

## Template `sma_result_insert_template.sparql`

Ce template produit une base de requête `INSERT DATA`.

Il ne peut pas tout remplir automatiquement, car les valeurs de sortie viennent du SMA. Il contient donc des placeholders :

```text
__RUN_URI__
__SCENARIO_URI__
__INPUT_URI__
__OUTPUT_URI__
__FINAL_STATE_URI__
__ENTITY_URI__
__STEP__
__TIME__
```

Exemple de fragment généré :

```sparql
INSERT DATA {
  GRAPH <http://example.org/fire_and_evacuation/simulation/results> {
    __RUN_URI__ a fe:SimulationRun ;
        fe:usesScenario __SCENARIO_URI__ ;
        fe:consumesInput __INPUT_URI__ ;
        fe:producesOutput __OUTPUT_URI__ .

    __OUTPUT_URI__ a fe:SimulationOutput ;
        fe:hasFinalState __FINAL_STATE_URI__ ;
        fe:producedByRun __RUN_URI__ .
  }
}
```

C'est au runtime SMA ou à un adaptateur de remplacer les placeholders par des URI et valeurs concrètes.

Exemple :

```text
__RUN_URI__         -> fe:SimulationRun_20260702_001
__SCENARIO_URI__    -> fe:Scenario_FireEvacuation_001
__INPUT_URI__       -> fe:Input_evacuation_sma
__OUTPUT_URI__      -> fe:SimulationOutput_20260702_001
__FINAL_STATE_URI__ -> fe:FinalState_20260702_001
__ENTITY_URI__      -> fe:Zone_A
__STEP__            -> 120
__TIME__            -> 600.0
```

## Rôle des contraintes SHACL

Le fichier d'exemple est :

```text
Constraints/evacuation_sma_input_shape.ttl
```

Il sert à valider qu'un graphe contient les données minimales attendues par le SMA d'évacuation.

Exemples de contraintes :

- une `fe:Zone` doit avoir au moins une `fe:hasPopulation` ;
- un `fe:Axis` doit avoir `fe:maxFlowCapacity` ;
- un `fe:Axis` doit avoir `fe:hasWidth` ;
- un `fe:Axis` doit avoir `fe:hasLength` ;
- une `fe:SimulationOutput` doit pointer vers au moins un `fe:FinalState`.

Pourquoi ne pas rendre ces propriétés obligatoires directement dans la requête SPARQL ?

Parce que l'extraction et la validation ont deux rôles différents :

- la requête extrait ce qui existe ;
- SHACL dit si ce qui existe suffit pour lancer proprement le SMA.

Cela permet aussi de faire du diagnostic : on peut extraire un graphe incomplet, puis produire un rapport SHACL indiquant précisément ce qui manque.

## Cycle complet recommandé

1. Créer ou choisir un profil dans `Profiles/`.
2. Générer les requêtes :

```sh
python3 Scripts/generate_sma_queries.py Profiles/evacuation_sma_profile.ttl
```

3. Exécuter la requête `*_init_construct.sparql` sur le KG pour conserver un sous-graphe RDF de référence.
4. Exécuter la requête `*_init_select.sparql`, ou utiliser `Scripts/export_sma_input_csv.py`, pour produire le CSV d'entrée SMA.
5. Valider le sous-graphe ou le CSV d'entrée avec la shape SHACL correspondante.
6. Transmettre le CSV d'entrée au SMA.
7. Le SMA exécute la simulation et produit un CSV de résultats.
8. Convertir ce CSV avec `Scripts/import_sma_results_csv.py`.
9. Exécuter l'`INSERT DATA` dans un graphe de résultats, sans écraser le graphe initial.

## Créer un nouveau profil pour un autre SMA

Pour créer un profil `artefact_saving_sma`, créer par exemple :

```text
Profiles/artefact_saving_sma_profile.ttl
```

Avec une structure du type :

```ttl
@prefix fe:   <http://example.org/fire_and_evacuation#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

fe:ArtefactSavingSMAProfile a fe:SimulationProfile ;
    rdfs:label "Profil SMA sauvegarde artefacts"@fr ;
    fe:profileIdentifier "artefact_saving_sma" ;
    fe:hasRootClass fe:Artefact ;
    fe:requiresClass fe:Artefact, fe:Zone, fe:Building ;
    fe:requiresProperty fe:hasProtectionPriority,
        fe:hasArtifactFireExposure,
        fe:hasArtifactsMobilityType ;
    fe:optionalProperty fe:containsArtefact,
        fe:hasSavingProcedureDocument,
        fe:hasArtifactFloodExposure ;
    fe:producesClass fe:SimulationOutput,
        fe:FinalState,
        fe:ImpactAssessment ;
    fe:producesProperty fe:producesOutput,
        fe:hasFinalState,
        fe:updatesEntity,
        fe:producesAssessment .
```

Puis lancer :

```sh
python3 Scripts/generate_sma_queries.py Profiles/artefact_saving_sma_profile.ttl
```

## Limites actuelles du prototype

Le générateur est volontairement simple. Il ne fait pas encore :

- résolution complète des imports OWL et des graphes nommés ;
- validation automatique du profil ;
- génération de requêtes centrées sur un scénario ou une zone donnée ;
- génération de payload JSON ;
- génération de plusieurs requêtes spécialisées par classe ;
- remplacement automatique des placeholders de sortie ;
- production automatique de shapes SHACL depuis le profil.

Ces limites sont acceptables pour mesurer le principe. Le prototype utilise déjà `rdflib` pour lire le profil comme graphe RDF ; pour une version de production plus complète, il faudra probablement enrichir cette couche avec validation SHACL, résolution contrôlée des imports, nettoyage RDF et éventuellement Jena/RDF4J côté serveur.

## Évolutions naturelles

Les prochaines évolutions utiles seraient :

1. Générer automatiquement une shape SHACL à partir de `fe:requiresProperty`.
2. Ajouter des filtres de contexte : scénario, site, zone, événement d'aléa.
3. Produire un export JSON structuré pour les SMA qui ne consomment pas RDF.
4. Séparer les requêtes par classe : zones, axes, populations, artefacts.
5. Enrichir l'adaptateur de déchargement CSV pour couvrir des sorties multi-entités plus complexes.
6. Déclarer dans le profil les graphes source et destination.
7. Ajouter des templates spécialisés par domaine lorsque le template générique devient trop plat.

## Point important de conception

Le profil ne doit pas représenter toute la richesse de l'ontologie. Il représente seulement le contrat entre un SMA donné et le KG.

L'ontologie peut rester large et extensible. Le profil dit simplement :

```text
Pour ce SMA précis, voici ce que je lis.
Pour ce SMA précis, voici ce que j'écris.
```

C'est cette séparation qui permet d'avoir plusieurs SMA de domaines différents connectés au même graphe, sans forcer chaque simulateur à comprendre toute l'ontologie.
