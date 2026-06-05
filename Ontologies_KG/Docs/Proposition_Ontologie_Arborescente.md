# Proposition d'ontologie plus arborescente

## Diagnostic rapide

À partir de vos fichiers, j'ai identifié des éléments qui rendent la structure difficile à exploiter :

- classes génériques redéfinies dans plusieurs modules (`fe:RiskDimension`, `fe:OperationnalType`, `fe:TechnicalType`)
- relations croisées entre modules sans structure racine claire
- mélange de vocabulaires OWL et SKOS pour des concepts qui pourraient être mieux séparés
- certains axiomes incohérents (par exemple `fe:RiskDimension rdfs:subClassOf fe:RiskDimension`)

## Objectif

Proposer une ontologie plus arborescente, avec :

1. un noyau central clair,
2. des branches thématiques bien séparées,
3. des vocabulaires SKOS pour les listes de types,
4. moins de classes « fourre-tout » et moins de doublons sémantiques.

## Structure proposée

### Racine

- `fe:DomainEntity`
  - `fe:DomainPlace`
    - `fe:Zone`
    - `fe:Building`
    - `fe:NaturalSpace`
    - `fe:HeritageSite`
  - `fe:DomainObject`
    - `fe:Artefact`
    - `fe:MaterialInstance`
  - `fe:PersonGroup`
    - `fe:Population`
    - `fe:Victim`
  - `fe:Condition`
    - `fe:Hazard`
    - `fe:Exposure`
    - `fe:ImpactAssessment`
    - `fe:WeatherCondition`
  - `fe:DataObject`
    - `fe:TopographicDataset`
    - `fe:LidarTile`

### Types et vocabulaires

- `fe:Type` (base pour tous les types de classification)
  - `fe:HazardType`
  - `fe:ZoneUsageType`
  - `fe:MobilityClass`
  - `fe:AccessibilityLevel`
  - `fe:FireSafetyClass`
  - `fe:RiskLevel`

Ces types peuvent être reliés à des schémas SKOS dans `Thesaurus/`.

## Principales règles de simplification

- remplacer plusieurs classes transverses par des sous-classes directement liées à la fonction réelle
- créer une classe unique `fe:Exposure` plutôt que plusieurs classes proches comme `fe:hazardExposure` et `fe:globalHazardExposure`
- fusionner les notions de sécurité du feu sous une même branche `fe:FireSafetyCharacteristic`
- utiliser `owl:imports` dans `fe_core.ttl` pour charger des modules clairs, mais sans multiplier les classes interfacées inutiles

## Exemple concret de réorganisation

### Avant

- `fe:OperationnalType`
- `fe:TechnicalType`
- `fe:HazardType`
- `fe:RiskDimension`

### Proposition

- `fe:Type` comme parent commun
- `fe:ZoneUsageType` subclassOf `fe:Type`
- `fe:AccessibilityLevel` subclassOf `fe:Type`
- `fe:HazardType` subclassOf `fe:Type`
- `fe:Exposure` subclassOf `fe:Condition`
- `fe:AxisVulnerability` subclassOf `fe:Exposure`

## Recommandations immédiates

1. corriger le coeur `fe_core.ttl` pour éviter la récursion de `fe:RiskDimension`
2. restructurer `fe_axis_module.ttl`, `fe_safety.ttl`, `fe_population.ttl` en partant d'un schéma racine
3. réserver les thésaurus SKOS uniquement aux valeurs de classification
4. documenter les relations principales dans un fichier de schéma (diagramme UML / arbre)

## Proposition de fichier TTL

Un squelette de modèle plus arborescent est disponible dans `Ontologies_KG/Modules/fe_arborescence_suggestion.ttl`.
