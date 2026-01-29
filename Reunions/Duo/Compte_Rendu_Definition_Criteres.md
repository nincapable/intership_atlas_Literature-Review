# Compte Rendu de Réunion : Définition des Critères et Actions

## 1. Actions à entreprendre
*   **État de l'art :** 
    *   Vérifier l'existant concernant les ontologies et bases de données sur le patrimoine culturel et naturel, ainsi que les risques naturels. 
    *   Vérifier l'existant concernant la classification et les statistiques des blessés notamment d'incendies (bases de données, ontologies, liens).
*   **Méthodologie & Validation :**
    *   Anticiper la possible vérification du modèle via des ontologies et données existantes.
    *   Analyser comment étendre les différents modèles pour intégrer la vérification.
*   **Intégration :** Identifier les entrées (*inputs*) et sorties (*outputs*) de la simulation à intégrer dans l'ontologie.
*   **Communication :** Prendre contact avec les services de secours (pompiers, CRF, CHU), et les historiens du patrimoine alpin.

## 2. Axes de Modélisation (Couverture de l'Ontologie)

### A. Patrimoine
*   **Caractéristiques :** 
    *   ***Intrisèques :*** Dates, noms, etc 
    *   ***structurelles et matérielles :*** materiaux, type d'architecture, fondations sur d'anciens sites, etc.
    *   ***Biens mobiliers et immobiliers :*** amovibilité, fragilité, valeur, etc .
    *   ***Héritage naturel :*** Forêts, jardins, agriculture, espaces avec espèces protégées.
    *   ***Facteur humain :*** Attractivité pour le public.

### B. Catastrophes Naturelles (Focus : Incendies)
*   **Caractéristiques physiques :** Météo, épicentre, surface d'expansion, durée, intensité, exposition
*   **Temporalité et Impact :** Heure de départ, dommages matériels, dommages naturels.

### C. Comportement Humain
*   **Facteurs cognitifs :** Biais cognitifs, perception du risque (conscience du risque) et du danger (visibilité des signaux, etc.).
*   **Préparation :** Communications (moyens, couverture, etc.), entraînements aux evacuations, sensibilisation aux risques.

### D. Populations
*   **Zones :** Habitations vs Touristiques ; Zones de passage vs Statiques.
*   **Classification des acteurs :** Distinguer les *évacués* des *intervenants* avec classes mixtes (ex: évacués-sauveteurs).

### E. Infrastructure et Topologie
*   **Axes de circulation :** Routiers, chemins, axes naturels, atypiques (via ferrata, etc.).
*   **Caractéristiques :** Accessibilité, praticabilité (falaises, rivières, etc.).
*   **Contraintes :** Événements bloquants (barrages de police, éboulements, etc.).

### F. Etudier les autres outputs pertinents de la simulation.

## 3. Métriques et Indicateurs
*   **Délais :**
    *   Temps d'évacuation réel ( etudier la granularité : site, zone, axes).
    *   Temps d'évacuation cible des intervenants.
*   **Impact humain :** Dommages aux victimes (psychologiques, physiques, gravité, classes).
*   **Réponse :** Interventions et moyens déployés.

## 4. Validation des modèles agents
*   Etudier comment une ontologie des incendies sur les sites patrimoniaux pourrait etre utilisée pour verifier les predictions du modele en fonction de ses entrees , sur une base statistique.
    *   On pourrait utiliser le peuplement d'une ontologie pour recuperer les sites qui repondent a n% des critère du site etudier et comparer les resultats de la simulation avec les resultats reels.