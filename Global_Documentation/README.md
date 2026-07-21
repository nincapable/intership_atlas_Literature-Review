# Documentation globale

Ce dossier constitue la source unique de documentation du projet ATLAS.

```text
Global_Documentation/
├── literature_review/  # État de l'art en français et traductions
├── project/            # Documents de cadrage du projet
├── technical_guides/   # Guides relatifs à l'ontologie et au SMA
└── translation/        # Script et configuration de traduction
```

## Convention de nommage

Les noms de fichiers utilisent des minuscules et des underscores. Les états de l'art suivent la convention `etat_de_l_art_atlas.<langue>.md`, avec les codes `fr`, `en`, `es` et `de`.

Le français est la version source. Les autres langues sont générées par le script de traduction et ne doivent pas être modifiées manuellement sans reporter les changements dans la version française.

## Traductions

Depuis la racine du dépôt :

```bash
python Global_Documentation/translation/translate.py
```

Le fichier `translation/mapping.yaml` déclare les sources et les sorties. Utiliser l'option `--force` pour regénérer des traductions déjà à jour.
