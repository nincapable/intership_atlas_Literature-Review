# Guide pour chercheurs : specialiser l'ontologie

## Objectif

Ce document explique comment et pourquoi specialiser l'ontologie sans casser son architecture. La specialisation peut consister a ajouter un nouveau type de danger, une nouvelle classe de batiment, un indicateur d'impact, un vocabulaire de population, un profil SMA ou des contraintes propres a un terrain d'etude.

La regle generale est simple : modifier la structure dans les modules OWL, modifier les listes de valeurs dans les thesaurus SKOS, et modifier les obligations de donnees dans SHACL.

## Portee des modules

`Fuse/fe_core.ttl` est le noyau. Il contient les abstractions partagees et importe les autres modules. Il ne doit pas devenir un fichier fourre-tout.

Les modules thematiques ont chacun une responsabilite :

- `fe_site.ttl` : organisation spatiale haute, site, patrimoine, localisation.
- `fe_zone.ttl` : zones d'analyse ou d'evacuation, contenance et capacites.
- `fe_building.ttl` : batiments, styles, materiaux, expositions structurelles.
- `fe_axis.ttl` : circulation, evacuation, connectivite et accessibilite.
- `fe_population.ttl` : groupes humains, effectifs et partitions.
- `fe_cognitive_factor.ttl` : facteurs cognitifs, perception et comportement.
- `fe_hazard_and_safety.ttl` : aleas, securite et conditions de danger.
- `fe_hazard_and_impact.ttl` : exposition, impact, urgence et severite.
- `fe_weather.ttl` : meteo et mesures environnementales.
- `fe_natural_space.ttl` : espaces naturels, especes et traits biologiques.
- `fe_artefacts.ttl` : objets patrimoniaux ou artefacts a proteger.
- `fe_victim.ttl` : victimes, triage et etats critiques.
- `fe_simulation.ttl` : simulation, profils SMA, runs, entrees et sorties.

Quand une notion touche plusieurs modules, choisir le module qui porte l'entite principale, puis creer des proprietes de liaison vers les autres modules.

## Lien avec CIDOC CRM

Les classes `fe:` sont des specialisations du domaine. Elles doivent etre rattachees autant que possible a une classe existante pertinente, dans `fe:` ou CRM :

- Objet ou entite physique : `crm:E70_Thing`, `crm:E25_Man_Made_Feature`, `crm:E18_Physical_Thing`.
- Materiau : `crm:E57_Material`.
- Type ou categorie : `crm:E55_Type`.
- Mesure ou score : `crm:E54_Dimension`.
- Etat : `crm:E3_Condition_State`.
- Evaluation ou attribution : `crm:E13_Attribute_Assignment`.
- Activite ou execution : `crm:E7_Activity`.
- Procedure, profil ou scenario : `crm:E29_Design_or_Procedure`.
- Objet d'information : `crm:E73_Information_Object`.

Pourquoi : CRM fournit une semantique stable, interdisciplinaire et patrimoniale. Les extensions `fe:` ajoutent le vocabulaire incendie, evacuation et simulation sans remplacer CRM.

## Classes d'ontologie et classes de thesaurus

Il faut distinguer trois niveaux.

### Classes metier OWL

Une classe metier represente une categorie d'entites du monde ou du graphe. Exemple :

```ttl
fe:Building a owl:Class ;
    rdfs:subClassOf crm:E25_Man_Made_Feature .
```

Utiliser une classe metier quand il faut decrire des individus avec des proprietes, des relations, des contraintes ou des comportements dans les simulations.

### Classes de classification OWL

Une classe de classification represente une famille de types. Exemple :

```ttl
fe:HazardType a owl:Class ;
    rdfs:subClassOf fe:HazardAndSafetyType .
```

Elle sert souvent de range pour une propriete de type. Elle ne doit pas contenir la liste detaillee des valeurs.

### Concepts de thesaurus SKOS

Un concept SKOS represente une valeur controlee. Exemple :

```ttl
fe:Fire a skos:Concept, fe:HazardType ;
    skos:prefLabel "Incendie"@fr ;
    skos:inScheme fe:HazardTaxonomy .
```

Utiliser un concept SKOS quand il s'agit d'une valeur de referentiel, d'une taxonomie, d'un libelle multilingue ou d'une liste amenageable par discipline.

## Quand ajouter une classe ou un concept

Ajouter une classe OWL si :

- la notion porte ses propres proprietes ;
- elle doit etre ciblee par SHACL ;
- elle est racine d'un sous-modele ;
- elle a un role dans une requete SMA ;
- elle doit etre liee a CRM par une semantique precise.

Ajouter un concept SKOS si :

- la notion est une valeur d'une liste ;
- elle sert surtout a classifier une entite ;
- elle doit avoir des libelles, synonymes, notes ou correspondances ;
- elle peut etre ajoutee sans changer la structure du modele.

Exemple : `fe:Axis` est une classe, car un axe a une longueur, une largeur, une capacite et des connexions. `fe:couloir` est un concept, car c'est une valeur possible de type d'axe.

## Procedure pour specialiser l'ontologie

### 1. Identifier le domaine de la modification

Avant d'editer, choisir le module responsable. Si la modification concerne une propriete d'evacuation, regarder d'abord `fe_axis.ttl`, `fe_zone.ttl`, `fe_population.ttl` ou `fe_simulation.ttl`. Si elle concerne une typologie, regarder le thesaurus correspondant.

### 2. Ajouter la structure OWL si necessaire

Ajouter la classe ou la propriete dans le module `Fuse/` pertinent.

Pour une classe :

```ttl
fe:ExampleImpactAssessment a owl:Class ;
    rdfs:subClassOf fe:ImpactAssessment ;
    rdfs:label "Evaluation d'impact exemple"@fr .
```

Pour une propriete :

```ttl
fe:hasExampleScore a owl:DatatypeProperty ;
    rdfs:subPropertyOf crm:P43_has_dimension ;
    rdfs:domain fe:ExampleImpactAssessment ;
    rdfs:range xsd:decimal ;
    rdfs:label "score exemple"@fr .
```

Pourquoi : la structure OWL rend la notion interoperable avec les autres modules et utilisable dans les profils SMA.

### 3. Ajouter les valeurs de thesaurus

Si la modification ajoute une valeur controlee, l'ajouter dans le fichier `Thesaurus/fe_thesaurus_*.ttl` correspondant.

```ttl
fe:ExampleHazardValue a skos:Concept, fe:HazardType ;
    skos:prefLabel "Valeur d'alea exemple"@fr ;
    skos:inScheme fe:HazardTaxonomy .
```

Pourquoi : les valeurs de referentiel evoluent plus vite que les classes metier. SKOS permet de les documenter, hierarchiser et aligner.

### 4. Relier la valeur a la structure

Une propriete du module OWL doit relier l'entite metier a la classe de classification ou au concept attendu.

Exemple :

```ttl
fe:hasHazardType rdfs:range fe:HazardType .
```

Puis une donnee peut utiliser :

```ttl
fe:Hazard_001 fe:hasHazardType fe:ExampleHazardValue .
```

Pourquoi : l'ontologie garde le sens de la relation, le thesaurus garde la valeur.

### 5. Mettre a jour les contraintes SHACL

Si la nouvelle notion est obligatoire pour un cas d'usage, ajouter une contrainte dans `Constraints/`.

Ne pas rendre obligatoire dans SHACL ce qui n'est requis que par un seul SMA generalement experimental. Dans ce cas, creer une shape specialisee par profil.

### 6. Mettre a jour les profils SMA

Si un SMA doit lire la nouvelle information, ajouter la classe ou propriete dans `Profiles/*.ttl` :

- `fe:requiresClass` si les instances doivent etre extraites ;
- `fe:requiresProperty` si la propriete est necessaire ;
- `fe:optionalProperty` si elle enrichit la simulation sans la bloquer ;
- `fe:producesProperty` si le SMA la renvoie en sortie.

Regenerer ensuite les artefacts :

```sh
python3 Scripts/generate_sma_queries.py Profiles/evacuation_sma_profile.ttl
```

### 7. Ajouter ou adapter des donnees d'exemple

Mettre a jour un fichier RDF d'exemple dans `Request/generated/` ou creer un fichier dedie si la donnee n'est pas strictement liee au profil d'evacuation.

Pourquoi : les exemples servent de tests humains et facilitent la reprise.

## Pourquoi faire les modifications a ces endroits

- Modifier `Fuse/` quand le modele du monde change.
- Modifier `Thesaurus/` quand une liste de valeurs change.
- Modifier `Constraints/` quand une exigence de validite change.
- Modifier `Profiles/` quand le contrat avec un SMA change.
- Modifier `Scripts/` seulement quand le mecanisme d'echange change.
- Modifier `Request/Templates/` seulement quand la forme generale des requetes SPARQL change.

Cette separation evite que des choix propres a une simulation contaminent toute l'ontologie.

## Recommandations de specialisation

- Preferer une sous-classe quand la nouvelle notion a des proprietes propres.
- Preferer un concept SKOS quand la nouvelle notion est seulement une valeur.
- Ne pas dupliquer une classe existante dans un autre module.
- Reutiliser les racines du noyau : dimensions, types, conditions et objets d'information.
- Documenter chaque nouvelle classe avec `rdfs:label` et si possible `rdfs:comment`.
- Garder les proprietes quantitatives alignees avec `crm:P43_has_dimension`.
- Garder les proprietes typologiques alignees avec `crm:P2_has_type`.
- Ajouter une contrainte SHACL uniquement si elle exprime une obligation de donnees.
- Verifier l'impact sur les profils SMA apres toute modification de classe ou propriete.

## Cas typique : ajouter un nouveau type d'alea

1. Verifier que `fe:HazardType` existe dans le noyau ou le module hazard.
2. Ajouter le concept dans `Thesaurus_a_revoir_totalement/fe_thesaurus_alea.ttl`.
3. Le typer comme `skos:Concept` et `fe:HazardType`.
4. Le placer dans le bon `skos:ConceptScheme`.
5. Ajouter `skos:broader` si la taxonomie a une hierarchie.
6. Ne pas creer une nouvelle classe OWL sauf si cet alea necessite des proprietes specifiques.
7. Si un SMA doit l'utiliser, verifier que `fe:hasHazardType` est bien dans le profil.

## Cas typique : ajouter un nouvel indicateur de sortie SMA

1. Ajouter la propriete dans le module metier concerne ou dans `fe_simulation.ttl` si elle porte sur l'execution.
2. Choisir `owl:DatatypeProperty` pour une valeur litterale ou `owl:ObjectProperty` pour une ressource.
3. Definir `rdfs:domain`, `rdfs:range`, `rdfs:label` et si possible `rdfs:comment`.
4. Ajouter la propriete dans `fe:producesProperty` du profil SMA.
5. Regenerer les artefacts.
6. Adapter le CSV de sortie du SMA pour utiliser cette propriete dans la colonne `property`.
7. Ajouter une contrainte SHACL de sortie si la propriete devient obligatoire.
