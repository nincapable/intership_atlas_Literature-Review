# Plan d'Action : Intégration & Optimisation RDF

## 1. Architecture et Nettoyage
- [ ] **Revue des imports**
    - Vérification systématique de chaque fichier `.ttl`.
    - Suppression des dépendances inutilisées et uniformisation des préfixes (fe, skos, crm, etc.).
- [ ] **Mise à jour RML (RDF Mapping Language)**
    - Assurer la compatibilité totale avec les spécifications RML.
    - Refactorisation des mappings existants si nécessaire.

## 2. Modélisation et Connaissances (SKOS & Inférence)
- [ ] **Extension du modèle : human_behavior**
    - Ajout de la section dédiée au comportement humain dans l'ontologie.
- [ ] **Étude approfondie SKOS & Inférence**
    - Analyse des capacités de raisonnement avancé via SKOS.
    - **Développer l'inférence de concepts** : Ex. automatiser la connexion sémantique des chemins traversant des infrastructures spécifiques (connexion de chemins sous un tunnel).
    - Évaluation des hiérarchies sémantiques pour l'inférence spatiale.

## 3. Risques Incendie et Espaces Naturels
- [ ] **Modélisation de la végétation**
    - Représenter l'**inflammabilité** et la **répartition** des strates végétales.
    - Modéliser la **sensibilité au feu** des espaces végétaux (en s'appuyant sur un système analogue à celui des matériaux de construction).
- [ ] **Gestion de l'entretien**
    - Représenter les types d'entretien associés aux espaces (Jardin à la française, jardin japonais, etc.).
    - Relier le type d'entretien à la vulnérabilité/sensibilité aux risques incendie.

## 4. Données, Persistance et Validation
- [ ] **Script de peuplement ARCH**
    - Développement du script d'importation automatique.
- [ ] **Validation GraphDB**
    - Tests de performance et d'intégrité des données.
- [ ] **Intégration SPARQL**
    - Implémentation et optimisation des requêtes de consultation.

## 5. Pipeline, Analyse et Visualisation
- [ ] **Déploiement GraphRAG**
    - Mise en place du pipeline de données vers GraphRAG.
    - Configuration de l'indexation pour la recherche augmentée par graphe.
- [ ] **Démonstration de pertinence (avec Flavien)**
    - Sélectionner un échantillon d'entités clés pour prouver la valeur ajoutée de l'ontologie sur des cas d'usage concrets.

## 6. Communication et Stratégie d'Équipe
- [ ] **Reporting et livrables**
    - Préparer un rapport technique détaillé.
    - Concevoir une présentation pour acter l'état d'avancement de l'ontologie.
- [ ] **Passerelle Ontologie ↔ Simulation**
    - Réflexion stratégique : Comment faire de l'ontologie l'outil pivot (le "pont") entre les experts en simulation et les membres de l'équipe ontologie.
    - Définir des protocoles d'échange de données fluides entre les deux pôles.