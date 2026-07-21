# Guide utilisateur SMA : initialiser une simulation et stocker ses resultats

## But du workflow

Le workflow SMA sert a extraire depuis l'ontologie uniquement les donnees necessaires a une simulation, puis a reinjecter les resultats dans le graphe de connaissances avec une tracabilite minimale.

L'idee importante est la suivante : le SMA ne doit pas charger toute l'ontologie. Il doit utiliser un profil d'initialisation qui declare les classes et proprietes utiles. Ce profil rend l'echange reproductible et documente.

Point important : l'import des resultats SMA ne modifie pas automatiquement les valeurs courantes des entites metier. Par defaut, il historise les sorties comme resultats de simulation (`fe:SimulationRun`, `fe:SimulationOutput`, `fe:FinalState`). Une valeur simulee ne devient une valeur courante de l'ontologie que si une etape de validation/publication est explicitement prevue.

## Fichiers utiles

- Profil SMA : `Profiles/evacuation_sma_profile.ttl`
- Generateur de requetes : `Scripts/generate_sma_queries.py`
- Export RDF vers CSV : `Scripts/export_sma_input_csv.py`
- Import CSV resultats vers SPARQL : `Scripts/import_sma_results_csv.py`
- Requetes et mappings generes : `Request/generated/`
- Templates SPARQL : `Request/Templates/`
- Contraintes de validation : `Constraints/evacuation_sma_input_shape.ttl`

## Ordre recommande

### 1. Choisir ou creer un profil SMA

Le profil de reference est `Profiles/evacuation_sma_profile.ttl`.

Il declare :

- `fe:profileIdentifier` : nom court utilise pour nommer les fichiers generes ;
- `fe:hasRootClass` : classe principale du domaine de simulation ;
- `fe:requiresClass` : classes a extraire ;
- `fe:requiresProperty` : proprietes necessaires ;
- `fe:optionalProperty` : proprietes utiles mais non bloquantes ;
- `fe:producesClass` et `fe:producesProperty` : resultats attendus.

Pourquoi : ce fichier est le contrat entre le SMA et l'ontologie. Modifier directement les requetes generees est possible pour tester, mais la modification durable doit se faire dans le profil.

### 2. Generer les requetes et mappings

Commande :

```sh
python3 Scripts/generate_sma_queries.py Profiles/evacuation_sma_profile.ttl
```

Sorties dans `Request/generated/` :

- `evacuation_sma_init_construct.sparql`
- `evacuation_sma_init_select.sparql`
- `evacuation_sma_result_insert.sparql`
- `evacuation_sma_input_mapping.json`
- `evacuation_sma_output_mapping.json`
- `evacuation_sma_results_example.csv`

Pourquoi : les artefacts generes sont synchronises avec le profil. Cela evite qu'un simulateur utilise une requete obsolete.

### 3. Preparer les donnees d'entree

Deux options existent.

La premiere consiste a executer `evacuation_sma_init_select.sparql` ou `evacuation_sma_init_construct.sparql` directement sur un triplestore.

La seconde consiste a exporter un CSV a partir d'un fichier RDF local :

```sh
python3 Scripts/export_sma_input_csv.py \
  --profile Profiles/evacuation_sma_profile.ttl \
  --data Request/generated/evacuation_sma_sample_data.ttl \
  --out Request/generated/evacuation_sma_input_example.csv
```

Le CSV d'entree contient :

```text
entity,class,property,value,value_type,value_lang
```

Pourquoi : le CSV est plus simple a consommer par beaucoup de SMA. Les colonnes `value_type` et `value_lang` permettent de conserver l'information RDF utile.

### 4. Valider les donnees avant simulation

Avant de lancer le SMA, il faut verifier que les donnees d'entree contiennent bien les informations minimales attendues par la simulation. Cette verification evite de lancer un calcul avec des zones sans population, des axes sans largeur, ou des populations sans effectif.

La validation se fait avec un fichier de contraintes SHACL. Pour un utilisateur non specialiste, il faut le comprendre comme une checklist lisible par une machine. Elle dit par exemple : "une zone d'evacuation doit avoir au moins une population" ou "un axe doit avoir une capacite de flux positive".

Pour l'evacuation, la checklist est :

```text
Constraints/evacuation_sma_input_shape.ttl
```

Les donnees a verifier sont les donnees RDF qui serviront a initialiser le SMA, par exemple :

```text
Request/generated/evacuation_sma_sample_data.ttl
```

ou un autre fichier RDF prepare pour la simulation.

#### Commande de validation

Si `pyshacl` est installe, lancer :

```sh
pyshacl \
  -s Constraints/evacuation_sma_input_shape.ttl \
  -d Request/generated/evacuation_sma_sample_data.ttl \
  -f human
```

Sens des options :

- `-s` indique le fichier de contraintes, c'est-a-dire la checklist SHACL.
- `-d` indique le fichier de donnees a verifier.
- `-f human` demande un rapport lisible dans le terminal.

Si `pyshacl` n'est pas installe, l'installer dans l'environnement Python du projet :

```sh
pip install pyshacl
```

#### Comment lire le resultat

Si tout est correct, le rapport indique que les donnees sont conformes. Le mot important a chercher est :

```text
Conforms: True
```

Cela signifie que les donnees respectent les contraintes minimales du profil SMA.

Si le rapport indique :

```text
Conforms: False
```

il faut lire les messages d'erreur. Ils indiquent generalement :

- quelle ressource pose probleme, par exemple une zone, un axe ou une population ;
- quelle propriete manque ou a une valeur incorrecte ;
- quel message metier explique l'erreur.

Exemples de problemes possibles :

- une zone n'a aucune population rattachee ;
- un axe n'a pas de longueur ;
- un axe a une capacite de flux negative ;
- une population n'a pas d'effectif estime ;
- une sortie de simulation ne contient pas d'etat final.

#### Que faire en cas d'erreur

1. Reperer dans le rapport la ressource en erreur, par exemple `fe:Zone_A` ou `fe:Axis_12`.
2. Ouvrir le fichier de donnees RDF utilise avec `-d`.
3. Ajouter ou corriger la propriete manquante.
4. Relancer la commande `pyshacl`.
5. Ne lancer le SMA que lorsque le rapport indique `Conforms: True`.

Exemple simple : si le rapport dit qu'une zone doit avoir une population, il faut ajouter un lien du type :

```ttl
fe:Zone_A fe:hasPopulation fe:Population_A .
fe:Population_A a fe:Population ;
    fe:hasEstimatedCount 120 .
```

Pourquoi : l'ontologie accepte volontairement des donnees partielles, car un graphe de connaissances peut etre incomplet. Un SMA, lui, a besoin d'un minimum de valeurs numeriques et relationnelles pour calculer correctement. La validation sert donc de controle qualite juste avant simulation.

### 5. Lancer la simulation

Le SMA consomme le CSV d'entree ou le sous-graphe RDF extrait.

Il doit conserver les identifiants RDF des entites dans ses sorties. Par exemple, si l'entree contient `fe:Zone_A`, la sortie doit garder `fe:Zone_A` ou `Zone_A`, afin que le script puisse rattacher le resultat a la bonne entite.

Pourquoi : si les identifiants changent, les resultats deviennent difficiles a relier aux entites sources.

### 6. Produire le CSV de resultats

Dans la version actuelle du script, le CSV de sortie doit contenir au minimum ces colonnes obligatoires :

```text
run_id,scenario_id,input_id,output_id,entity,step,time,property,value,value_type
```

Exemple :

```csv
run_id,scenario_id,input_id,output_id,entity,step,time,property,value,value_type
SimulationRun_001,Scenario_001,Input_evacuation_sma,Output_001,Zone_A,120,600.0,fe:hasEvacuationTime,540.0,xsd:double
```

Regles importantes :

- `run_id` identifie l'execution concrete.
- `scenario_id` identifie le scenario.
- `input_id` identifie le lot d'entree.
- `output_id` identifie le lot de sortie.
- `entity` identifie l'entite concernee par le resultat de simulation. Elle n'est pas forcement mise a jour dans le graphe courant.
- `step` et `time` placent le resultat dans le temps de simulation.
- `property` indique la propriete produite.
- `value_type` vaut `uri` pour une ressource, ou un datatype comme `xsd:string`, `xsd:integer`, `xsd:decimal`, `xsd:double`, `xsd:boolean`.

Pourquoi : cette table permet de reconstruire automatiquement des triples RDF de sortie sans connaitre le code interne du SMA.

Dans la version actuelle des scripts, chaque ligne de ce CSV est interpretee comme un resultat historise de simulation. Par exemple, si le SMA calcule une resistance au feu pour un batiment, la ligne indique : "pour ce run, a cette etape, le batiment a cette valeur simulee". Elle n'indique pas encore : "la fiche courante du batiment doit etre remplacee par cette valeur".

Pour preparer une future publication de valeurs courantes, il est recommande d'ajouter, dans les sorties SMA internes ou dans un CSV etendu, une intention de mise a jour :

```text
update_policy
```

Valeurs recommandees :

- `snapshot_only` : la valeur reste uniquement un resultat de simulation.
- `update_entity` : la valeur pourra etre appliquee directement sur l'entite de la colonne `entity`.
- `update_related_resource` : la valeur pourra etre appliquee sur une ressource associee a l'entite, par exemple une fiche `fe:BuildingFireExposure` reliee a un batiment par `fe:hasFireExposure`.

Ces colonnes et politiques ne sont pas encore traitees automatiquement par le script actuel. Elles servent a preparer proprement l'evolution de l'import.

### 7. Convertir le CSV de resultats en SPARQL INSERT

Commande :

```sh
python3 Scripts/import_sma_results_csv.py \
  --profile Profiles/evacuation_sma_profile.ttl \
  --csv Request/generated/evacuation_sma_results_example.csv \
  --out Request/generated/evacuation_sma_result_insert_from_csv.sparql
```

Par defaut, l'insertion cible le graphe nomme :

```text
http://example.org/fire_and_evacuation/simulation/results
```

Il est possible de choisir un autre graphe :

```sh
python3 Scripts/import_sma_results_csv.py \
  --profile Profiles/evacuation_sma_profile.ttl \
  --csv results.csv \
  --out insert_results.sparql \
  --result-graph http://example.org/fire_and_evacuation/simulation/results/run_001
```

Pourquoi : les resultats doivent rester separes des donnees sources. Cela evite de confondre un etat observe avec un etat calcule par simulation.

Ce fichier SPARQL genere une couche de resultats. Il ne fait pas de `DELETE/INSERT` sur le graphe courant des entites metier. C'est le comportement attendu aujourd'hui.

### 8. Inserer les resultats dans le triplestore

Executer le fichier SPARQL genere dans l'interface ou l'API du triplestore.

Les resultats inseres creent :

- un `fe:SimulationRun` ;
- un `fe:SimulationOutput` ;
- un ou plusieurs `fe:FinalState` ;
- des liens `fe:usesScenario`, `fe:consumesInput`, `fe:producesOutput`, `fe:producedByRun`, `fe:stateOfEntity` ;
- les proprietes produites par le SMA.

Pourquoi : cette structure donne une provenance minimale et permet de retrouver quelle execution a produit quelle valeur.

### 9. Publier une valeur simulee comme valeur courante

Cette etape n'est pas encore automatisee dans les scripts actuels. Elle doit etre faite seulement si le resultat SMA est accepte comme nouvelle donnee courante.

Exemple : le SMA simule une resistance au feu pour un batiment.

1. Verifier que la propriete existe dans l'ontologie, par exemple dans `Ontologie_OWL/fe_building.ttl`.
2. Verifier ou la valeur doit vivre : directement sur `fe:Building` si elle decrit le batiment lui-meme, ou sur `fe:BuildingFireExposure` si elle decrit l'exposition ou la resistance au feu.
3. Garder le resultat historise dans `fe:FinalState`.
4. Produire ensuite une requete de mise a jour separee, de type `DELETE/INSERT`, pour remplacer ou ajouter la valeur courante.
5. Executer cette mise a jour seulement apres validation.

Pourquoi : cela evite de confondre une hypothese calculee par un run avec une donnee de reference. Le graphe garde les deux niveaux : le resultat de simulation et l'etat courant publie.

## Bonnes pratiques

- Ne pas renommer les colonnes CSV.
- Utiliser des identifiants stables pour `run_id`, `scenario_id`, `input_id` et `output_id`.
- Garder les entites sources inchangees dans les resultats.
- Ne pas ecrire automatiquement les resultats simules directement sur les entites source si la valeur represente un etat calcule.
- Publier une valeur simulee dans l'etat courant seulement apres validation explicite.
- Choisir la bonne cible de mise a jour : entite directe ou ressource associee comme une fiche d'exposition.
- Ajouter les nouvelles proprietes produites dans `fe:producesProperty` du profil.
- Regenerer les requetes apres chaque modification du profil.
- Valider les entrees et les sorties avec SHACL quand les contraintes existent.

## Ou modifier quoi

- Le SMA a besoin d'une nouvelle donnee en entree : modifier `Profiles/evacuation_sma_profile.ttl`, puis verifier que la classe/propriete existe dans `Ontologie_OWL/`.
- Le SMA produit une nouvelle mesure : ajouter la propriete dans le module `Ontologie_OWL/` approprie, puis dans `fe:producesProperty`.
- Le SMA produit une mesure qui doit devenir une valeur courante : prevoir une politique de mise a jour (`snapshot_only`, `update_entity`, `update_related_resource`) et une requete `DELETE/INSERT` separee.
- Une valeur doit appartenir a une liste controlee : l'ajouter dans le thesaurus correspondant.
- Une donnee devient obligatoire pour la simulation : ajouter ou modifier une contrainte dans `Constraints/`.
- Le format CSV change : modifier d'abord les scripts et les mappings, puis documenter la nouvelle convention.
