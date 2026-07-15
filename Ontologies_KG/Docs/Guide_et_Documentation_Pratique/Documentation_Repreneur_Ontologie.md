# Documentation technique pour la reprise de la gestion de l'ontologie

## Objectif general

Cette ontologie sert a representer l'interconnexion entre les domaines du risque autour et sur les sites du patrimoine. Modéliser les sitees, les populations, les batiments, les espaces, artefacts, especes, etc, avec un objectif pratique : alimenter des systemes multi-agents (SMA), recuperer leurs resultats et les rattacher au graphe de connaissances sans perdre l'etat initial.

Le depot est organise autour de quatre familles de fichiers :

- `Fuse/` : modules OWL/RDFS principaux de l'ontologie.
- `Thesaurus/` : vocabulaires SKOS qui portent les listes de valeurs et taxonomies.
- `Constraints/` : contraintes SHACL utilisees pour verifier les donnees.
- `Profiles/`, `Request/`, `Scripts/` : couche d'interoperabilite SMA, generation de requetes, exports CSV et imports de resultats.

Le point d'entree logique est `Fuse/fe_core.ttl`. Il declare les abstractions communes et importe les modules metier, le module simulation et les thesaurus.

## Architecture des modules

### Module noyau

`Fuse/fe_core.ttl` joue le role de racine. Il centralise :

- les imports `owl:imports` vers les autres modules ;
- les grandes abstractions quantitatives heritees de `crm:E54_Dimension` ;
- les grandes abstractions typologiques heritees de `crm:E55_Type` ;
- quelques outils transverses comme `fe:vector3` et `fe:NormalizedValue`.

Les modules ne doivent pas redefinir ces racines si elles existent deja dans le noyau. Ils doivent les reutiliser avec `rdfs:subClassOf`.

### Modules metier

Les modules `Fuse/fe_*.ttl` decrivent les classes et proprietes structurelles du domaine :

- `fe_site.ttl` : sites, lieux patrimoniaux et relations de localisation.
- `fe_zone.ttl` : zones fonctionnelles, contenance, capacites et liens vers batiments, populations, espaces naturels, artefacts.
- `fe_building.ttl` : batiments, styles architecturaux, materiaux, expositions feu/inondation et priorites heritees.
- `fe_axis.ttl` : axes de circulation, connectivite, dimensions utiles, capacite de flux et accessibilite.
- `fe_population.ttl` : populations, partitions, effectifs, caracteristiques humaines et mobilite.
- `fe_cognitive_factor.ttl` : facteurs cognitifs et comportementaux utiles aux simulations.
- `fe_hazard_and_safety.ttl` : aleas, securite, dispositifs, niveaux et conditions de danger.
- `fe_hazard_and_impact.ttl` : exposition, impact, severite, urgence et evaluation.
- `fe_weather.ttl` : conditions et mesures meteorologiques.
- `fe_natural_space.ttl` : espaces naturels, especes, traits biologiques et combustibilite.
- `fe_artefacts.ttl` : artefacts patrimoniaux ou objets a proteger.
- `fe_victim.ttl` : victimes, triage et etats humains critiques.
- `fe_simulation.ttl` : profils SMA, scenarios, executions, entrees, sorties et etats.

Chaque module doit rester responsable de son domaine. Les relations transverses sont normales, mais elles doivent pointer vers des classes stables d'autres modules plutot que dupliquer une notion.

### Lien avec CIDOC CRM

L'ontologie s'appuie sur CIDOC CRM pour garder une semantique patrimoniale et documentaire :

- les entites physiques sont rattachees a des classes comme `crm:E25_Man_Made_Feature`, `crm:E70_Thing` ou `crm:E57_Material` ;
- les mesures et dimensions utilisent `crm:E54_Dimension` ou des proprietes derivees de `crm:P43_has_dimension` ;
- les types et classifications s'appuient sur `crm:E55_Type` ou `crm:P2_has_type` ;
- les etats, evaluations et assertions s'appuient sur `crm:E3_Condition_State` et `crm:E13_Attribute_Assignment` ;
- les procedures et profils SMA utilisent `crm:E29_Design_or_Procedure` ;
- les executions de simulation utilisent `crm:E7_Activity`.

Cette logique evite de creer une ontologie isolee : les classes `fe:` specialisent CRM pour le domaine, tandis que CRM fournit le socle conceptuel.

## Interaction entre modules et thesaurus

Les modules `Fuse/` definissent la structure : classes, proprietes, domaines, ranges et relations. Les fichiers de thesaurus definissent les valeurs controlees : concepts SKOS, hierarchies de concepts, libelles, correspondances et taxonomies.

Exemple de separation :

- `fe:Axis`, `fe:hasAccessibilityLevel` et `fe:AccessibilityLevel` appartiennent a la structure ontologique.
- `fe:WheelchairAccessible`, `fe:PartiallyArrangedPedestrian` ou `fe:InaccessibleDisabledPerson` sont des valeurs de thesaurus.

Les thesaurus utilisent surtout :

- `skos:ConceptScheme` pour nommer un referentiel ;
- `skos:Concept` pour une valeur ;
- `skos:prefLabel`, `skos:definition`, `skos:scopeNote` pour documenter ;
- `skos:broader`, `skos:narrower`, `skos:hasTopConcept`, `skos:topConceptOf` pour hierarchiser ;
- `skos:closeMatch` ou `skos:exactMatch` pour relier des concepts proches.

Certains concepts sont aussi types par une classe `fe:` de classification, par exemple `fe:couloir a skos:Concept, fe:AxisType`. C'est une passerelle pratique entre OWL et SKOS : OWL sait que la valeur appartient au type attendu, SKOS garde la taxonomie et les libelles.

## Contraintes SHACL

Les contraintes dans `Constraints/` servent a verifier les donnees chargees dans le graphe. Elles ne remplacent pas l'ontologie. Elles expriment des regles de qualite ou de completude :

- cardinalites minimales ou maximales ;
- types attendus ;
- datatypes numeriques ;
- bornes de valeurs ;
- messages d'erreur metier.

Exemple : `Constraints/evacuation_sma_input_shape.ttl` impose qu'une `fe:Zone` chargee par le SMA d'evacuation ait au moins une population, et qu'un `fe:Axis` ait une largeur, une longueur et une capacite de flux positives.

La bonne pratique est de garder dans OWL la definition generale du modele, et dans SHACL les exigences propres a un usage, un profil SMA ou une validation de donnees.

## Fonctionnement de la couche SMA

### Module `fe_simulation.ttl`

Le module simulation ajoute deux familles de concepts.

La premiere decrit le cycle d'execution :

- `fe:SimulationScenario` : configuration ou hypothese de simulation.
- `fe:SimulationRun` : execution concrete d'un scenario.
- `fe:SimulationInput` : lot de donnees transmis au SMA.
- `fe:SimulationOutput` : lot de resultats produit.
- `fe:StateSnapshot`, `fe:InitialState`, `fe:FinalState` : etats d'entites a une etape donnee.
- `fe:producedByRun`, `fe:consumesInput`, `fe:producesOutput`, `fe:stateOfEntity` : relations de tracabilite.

La seconde decrit les profils declaratifs :

- `fe:SimulationProfile` ;
- `fe:profileIdentifier` ;
- `fe:hasRootClass` ;
- `fe:requiresClass` ;
- `fe:requiresProperty` ;
- `fe:optionalProperty` ;
- `fe:producesClass` ;
- `fe:producesProperty` ;
- `fe:expandProperty`, `fe:expandClass`, `fe:maxDepth` pour l'extraction profonde.

Un profil est un contrat entre l'ontologie et un simulateur. Il dit ce que le SMA lit, ce qu'il peut ignorer, et ce qu'il doit rendre.

### Scripts de generation

`Scripts/generate_sma_queries.py` lit un fichier profil RDF avec `rdflib`. Il ne fait pas de manipulation textuelle fragile : il parse le Turtle, cherche exactement une ressource de type `fe:SimulationProfile`, extrait les classes/proprietes declarees, puis injecte ces elements dans les templates SPARQL.

Le script produit :

- une requete `*_init_construct.sparql` pour extraire un sous-graphe RDF ;
- une requete `*_init_select.sparql` pour produire une vue tabulaire ;
- une requete `*_result_insert.sparql` avec placeholders pour insertion manuelle ou runtime ;
- un mapping JSON d'entree ;
- un mapping JSON de sortie ;
- un exemple CSV de resultats.

La generation plate utilise les classes `fe:requiresClass` et les proprietes `fe:requiresProperty` + `fe:optionalProperty`. La generation profonde est activee si le profil declare `fe:expandProperty` et `fe:maxDepth`. Dans ce cas, le script construit des chemins optionnels qui suivent les proprietes indiquees jusqu'a la profondeur demandee.

`Scripts/export_sma_input_csv.py` charge le profil et un graphe RDF de donnees, puis exporte un CSV avec les colonnes :

`entity,class,property,value,value_type,value_lang`

Il conserve le type des valeurs : URI, literal type, langue ou blank node.

`Scripts/import_sma_results_csv.py` lit un CSV de resultats avec les colonnes :

`run_id,scenario_id,input_id,output_id,entity,step,time,property,value,value_type`

Il genere un `INSERT DATA` dans le graphe nomme `http://example.org/fire_and_evacuation/simulation/results`. Les resultats sont modelises comme un `fe:SimulationRun`, un `fe:SimulationOutput` et des `fe:FinalState` rattaches aux entites mises a jour.

### Etat actuel : ce qui est deja fait

Le script `Scripts/import_sma_results_csv.py` sait deja transformer un CSV de sortie SMA en requete SPARQL `INSERT DATA`.

Il fait aujourd'hui trois choses :

1. il cree ou reutilise un `fe:SimulationRun` a partir de `run_id` ;
2. il cree un `fe:SimulationOutput` a partir de `output_id` ;
3. il cree des `fe:FinalState` rattaches aux entites simulees avec `fe:stateOfEntity`, `fe:hasSimulationStep`, `fe:hasSimulationTime` et `fe:producedByRun`.

Autrement dit, le script stocke correctement le resultat comme resultat de simulation. Il garde la trace de provenance : quelle execution a produit quelle valeur, pour quelle entite, a quelle etape.

Exemple : si le SMA produit une valeur de resistance au feu pour `fe:Building_001`, le script peut deja creer un etat final du type :

```ttl
fe:FinalState_Output_001_Building_001_120 a fe:FinalState ;
    fe:stateOfEntity fe:Building_001 ;
    fe:hasSimulationStep 120 ;
    fe:hasSimulationTime 600.0 ;
    fe:producedByRun fe:SimulationRun_001 ;
    fe:simulatedFireResistance "0.72"^^xsd:decimal .
```

Ce resultat dit : pendant cette simulation, le batiment a eu une resistance au feu calculee de `0.72`. Il ne dit pas encore : la valeur courante du batiment dans l'ontologie est maintenant `0.72`.

### Limite actuelle : ce qui n'est pas encore fait

Le script ne met pas encore a jour les entites metier du graphe principal. Il n'ecrit pas directement sur `fe:Building`, `fe:BuildingFireExposure`, `fe:Axis`, `fe:Population` ou les autres classes du domaine.

Cette limite est volontairement prudente : une sortie SMA est une valeur calculee, pas forcement une verite a publier dans l'etat courant du graphe. Avant d'ecraser ou de remplacer une valeur, il faut savoir si le resultat doit rester une hypothese de simulation ou devenir une donnee metier validee.

Il manque donc une deuxieme etape, distincte de l'import des resultats : la publication d'une valeur simulee dans l'etat courant de l'ontologie.

### Objectif de l'extension a developper

L'extension attendue doit permettre deux comportements :

- conserver toutes les sorties dans les resultats de simulation, comportement actuel ;
- appliquer certaines sorties comme nouvelles valeurs courantes sur les entites ou sur leurs fiches associees.

Exemple concret : le SMA simule la resistance au feu d'un batiment.

Deux cas sont possibles :

- la valeur doit rester un resultat de simulation : elle reste seulement dans `fe:FinalState` ;
- la valeur est validee comme nouvel etat courant : elle doit aussi etre ecrite sur la ressource metier pertinente.

La ressource metier pertinente n'est pas toujours l'entite de depart. Pour un batiment, une valeur de geometrie ou d'identification peut vivre directement sur `fe:Building`. En revanche, une valeur d'exposition au feu, d'inflammabilite, de resistance thermique ou de vulnerabilite doit plutot vivre sur une fiche associee, par exemple `fe:BuildingFireExposure`, reliee au batiment par `fe:hasFireExposure`.

### Convention CSV proposee

Pour rendre cette intention explicite, ajouter une colonne au CSV de resultats :

```text
update_policy
```

Valeurs recommandees :

- `snapshot_only` : comportement actuel. La valeur est stockee dans `fe:FinalState` uniquement.
- `update_entity` : la valeur est stockee dans `fe:FinalState` et appliquee directement sur `entity`.
- `update_related_resource` : la valeur est stockee dans `fe:FinalState` et appliquee sur une ressource reliee a `entity`.

Pour `update_related_resource`, il faut aussi savoir quelle relation suivre. Deux solutions sont possibles :

- ajouter des colonnes CSV explicites, par exemple `target_relation` et `target_class` ;
- ou declarer ce mapping dans le profil SMA, ce qui est plus propre pour un usage durable.

Exemple de CSV etendu :

```csv
run_id,scenario_id,input_id,output_id,entity,step,time,property,value,value_type,update_policy,target_relation,target_class
SimulationRun_001,Scenario_001,Input_evacuation_sma,Output_001,fe:Building_001,120,600.0,fe:simulatedFireResistance,0.72,xsd:decimal,update_related_resource,fe:hasFireExposure,fe:BuildingFireExposure
```

### Convention de profil a ajouter

Le profil SMA devrait indiquer quelles proprietes de sortie peuvent etre appliquees au graphe courant, et ou les appliquer.

Une convention possible dans `Profiles/*.ttl` serait d'ajouter des ressources de mapping de sortie. Par exemple :

```ttl
fe:EvacuationSMAProfile fe:hasOutputUpdateMapping fe:BuildingFireResistanceUpdate .

fe:BuildingFireResistanceUpdate a fe:OutputUpdateMapping ;
    fe:updatesProperty fe:simulatedFireResistance ;
    fe:updatePolicy "update_related_resource" ;
    fe:targetRelation fe:hasFireExposure ;
    fe:targetClass fe:BuildingFireExposure .
```

Cela implique d'ajouter dans `Fuse/fe_simulation.ttl` les classes et proprietes de configuration necessaires :

```ttl
fe:OutputUpdateMapping a owl:Class .
fe:hasOutputUpdateMapping a owl:ObjectProperty .
fe:updatesProperty a owl:ObjectProperty .
fe:updatePolicy a owl:DatatypeProperty .
fe:targetRelation a owl:ObjectProperty .
fe:targetClass a owl:ObjectProperty .
```

Ces noms sont une proposition. Ils peuvent etre ajustes, mais l'idee doit rester la meme : le profil decrit comment transformer une sortie SMA en mise a jour metier.

### Modifications a faire dans `import_sma_results_csv.py`

Le script doit etre etendu en plusieurs etapes.

1. Lire les nouvelles colonnes optionnelles du CSV : `update_policy`, puis eventuellement `target_relation` et `target_class`.
2. Charger les mappings declares dans le profil SMA si la solution par profil est retenue.
3. Continuer a generer l'insertion actuelle des `fe:SimulationRun`, `fe:SimulationOutput` et `fe:FinalState`.
4. Pour les lignes `snapshot_only`, ne rien faire de plus.
5. Pour les lignes `update_entity`, generer une requete SPARQL `DELETE/INSERT` qui remplace l'ancienne valeur de `entity property oldValue` par `entity property newValue`.
6. Pour les lignes `update_related_resource`, chercher la ressource liee par `target_relation`. Si elle existe, mettre a jour cette ressource. Si elle n'existe pas, la creer puis la relier a `entity`.

Le script ne doit pas remplacer le `INSERT DATA` actuel par une mise a jour directe. Il doit produire les deux couches : provenance de simulation et mise a jour metier optionnelle.

### Requete SPARQL pour `update_entity`

Pour une mise a jour directe de l'entite, le motif est :

```sparql
DELETE {
  GRAPH <http://example.org/fire_and_evacuation/current> {
    ?entity ?property ?oldValue .
  }
}
INSERT {
  GRAPH <http://example.org/fire_and_evacuation/current> {
    ?entity ?property ?newValue .
  }
}
WHERE {
  OPTIONAL {
    GRAPH <http://example.org/fire_and_evacuation/current> {
      ?entity ?property ?oldValue .
    }
  }
}
```

Cette requete doit etre instanciee par le script avec l'entite, la propriete et la valeur issues du CSV.

### Requete SPARQL pour `update_related_resource`

Pour une mise a jour sur une fiche associee, le motif est :

```sparql
DELETE {
  GRAPH <http://example.org/fire_and_evacuation/current> {
    ?target ?property ?oldValue .
  }
}
INSERT {
  GRAPH <http://example.org/fire_and_evacuation/current> {
    ?entity ?targetRelation ?target .
    ?target a ?targetClass ;
        ?property ?newValue .
  }
}
WHERE {
  OPTIONAL {
    GRAPH <http://example.org/fire_and_evacuation/current> {
      ?entity ?targetRelation ?existingTarget .
      ?existingTarget a ?targetClass .
    }
  }
  BIND(COALESCE(?existingTarget, ?mintedTarget) AS ?target)
  OPTIONAL {
    GRAPH <http://example.org/fire_and_evacuation/current> {
      ?target ?property ?oldValue .
    }
  }
}
```

Le point technique important est la creation de `?mintedTarget`. En pratique, le script Python devra generer une IRI stable, par exemple :

```text
fe:BuildingFireExposure_Building_001_SimulationRun_001
```

ou, si l'on veut une valeur courante unique par entite :

```text
fe:BuildingFireExposure_Building_001_Current
```

Le choix depend de la strategie de versioning retenue. Tant que les branches par `SimulationRun` ne sont pas implementees, il est plus simple de separer :

- graphe des resultats simules ;
- graphe courant valide ;
- IRI stable pour la fiche courante.

### Exemple applique : resistance au feu d'un batiment

Si le SMA calcule une resistance au feu pour `fe:Building_001`, la procedure cible devrait etre :

1. Ajouter la propriete dans `Fuse/fe_building.ttl`, par exemple sur `fe:BuildingFireExposure` si elle concerne l'exposition au feu.
2. Ajouter cette propriete dans `fe:producesProperty` du profil SMA.
3. Ajouter un mapping de sortie indiquant que cette propriete met a jour `fe:BuildingFireExposure` via `fe:hasFireExposure`.
4. Faire produire au SMA une ligne CSV avec `update_policy=update_related_resource`.
5. Laisser `import_sma_results_csv.py` generer l'insertion du resultat de simulation et la requete de mise a jour metier.
6. Executer la mise a jour seulement si le resultat est accepte comme nouvelle valeur courante.

Ainsi, on garde les deux informations : la valeur simulee comme resultat historise, et la valeur publiee comme etat courant exploitable par les autres modules.

### Resume de ce qu'il reste a faire

- Ajouter dans `fe_simulation.ttl` un petit modele de mapping de sortie SMA.
- Ajouter dans les profils SMA les mappings entre proprietes produites et cibles metier.
- Etendre le format CSV ou le mapping JSON de sortie avec `update_policy`.
- Modifier `import_sma_results_csv.py` pour generer des requetes `DELETE/INSERT` en plus du `INSERT DATA` actuel.
- Ajouter des tests pour `snapshot_only`, `update_entity` et `update_related_resource`.
- Documenter la politique de validation : une simulation ne doit pas publier automatiquement une valeur courante si elle n'est pas consideree comme acceptee.

## Cycle de maintenance recommande

1. Modifier d'abord le module `Fuse/` concerne.
2. Ajouter ou corriger les valeurs de classification dans le thesaurus correspondant.
3. Ajuster les contraintes SHACL si la modification concerne des donnees requises.
4. Mettre a jour ou creer un profil SMA dans `Profiles/` si le simulateur consomme ou produit de nouvelles donnees.
5. Regenerer les artefacts avec `Scripts/generate_sma_queries.py`.
6. Tester l'export CSV et l'import CSV sur des donnees d'exemple.
7. Documenter la modification dans `Docs/`.

## Prochaine tache : branches propres a chaque simulation run

Le besoin suivant est de permettre a l'ontologie et au graphe de conserver des branches propres a chaque execution de simulation. L'objectif est double :

- ne jamais ecraser l'etat initial ou les donnees sources ;
- pouvoir repartir d'un etat produit par une execution precedente, comme un point de versioning.

### Probleme actuel

La couche actuelle trace deja `SimulationRun`, `SimulationInput`, `SimulationOutput` et `FinalState`. Les resultats sont inseres dans un graphe nomme de resultats. En revanche, l'ontologie ne formalise pas encore completement une branche d'etat par run, ni la relation entre un etat source, un etat derive et un nouveau depart de simulation.

### Modele cible

La solution devrait introduire une logique de versionnement oriente graphe :

- un `SimulationRun` consomme un etat de reference ;
- un `SimulationRun` produit une branche d'etat ;
- chaque branche de run contient des snapshots ou assertions derivees ;
- une nouvelle simulation peut consommer une branche precedente comme etat initial ;
- les entites metier restent stables, mais leurs etats calcules sont branches.

Deux strategies sont possibles :

- utiliser des graphes nommes par run, par exemple `.../simulation/run/SimulationRun_001`;
- utiliser des ressources explicites `fe:StateBranch` ou `fe:SimulationBranch` qui groupent les snapshots et gardent la provenance.

La solution la plus robuste serait de combiner les deux : graphe nomme pour l'isolation technique, ressource RDF pour la description semantique.

### Proprietes a envisager

Ajouter dans `fe_simulation.ttl` :

- `fe:SimulationBranch` : branche d'etat produite par une execution.
- `fe:hasStateBranch` : lie un run ou une sortie a une branche.
- `fe:derivedFromBranch` : indique la branche source.
- `fe:derivedFromRun` : indique le run parent.
- `fe:branchGraphIRI` : IRI du graphe nomme.
- `fe:canInitializeRunFrom` : relation entre scenario/profil et branche reutilisable.
- `fe:branchCreatedAt` ou alignement CRM equivalent pour dater.

Adapter ensuite `import_sma_results_csv.py` pour que le graphe cible ne soit plus seulement le graphe global des resultats, mais un graphe derive de `run_id` ou fourni explicitement par option CLI.

### Points d'attention

- Garder les entites physiques dans le graphe de reference.
- Ne placer dans les branches que les etats, resultats, scores, recommandations ou valeurs calculees.
- Documenter clairement si une propriete represente une observation source ou une valeur simulee.
- Ajouter des contraintes SHACL pour verifier qu'une branche a un run producteur, une source et au moins un snapshot.
- Mettre a jour les profils SMA pour indiquer s'ils initialisent depuis le graphe source ou depuis une branche.
