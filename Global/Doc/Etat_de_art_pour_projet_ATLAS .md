# État de l’art pour projet ATLAS

# Introduction

Le présent état de l’art propose d’examiner de manière prospective l’adaptation possible du projet ATLAS à travers le couplage des dispositifs HArIS (issu d’ARCH) et C2Impress (SoS4MHRIN). Dans cette perspective, il s’agirait de passer d’un simple inventaire patrimonial enrichi à un environnement numérique intégrant à la fois une base de données fine sur les biens et une intelligence multi‑aléas, participative et évolutive. L’analyse envisagera les potentialités de ce couplage pour la mise en place d’un jumeau numérique dynamique du patrimoine, capable de soutenir des approches prédictives en matière de vulnérabilité et de gestion de crise.

Dans un premier temps, les intérêts théoriques d’un tel rapprochement seraient discutés, notamment en termes de complémentarité entre données structurelles détaillées et flux environnementaux ou sociaux. Dans un second temps, les besoins de développement pour l’intégration d’un simulateur d’incendie (Soc‑SIM‑K) et pour la modélisation des comportements d’évacuation seraient identifiés. Enfin, une attention particulière serait portée à la nécessité de construire une ontologie unifiée, fondée sur une extension du CIDOC CRM, permettant l’interopérabilité sémantique entre les deux systèmes et la standardisation des indicateurs de risque à l’échelle du projet ATLAS.

# Étude ARCH

Le projet ARCH propose un cadre technologique intégré pour analyser, surveiller et améliorer la résilience des zones historiques, en articulant systèmes d’information, simulations multi‑aléas et outils d’aide à la décision.

## 1. Cadre général et objectifs d’ARCH

ARCH (Advancing Resilience of Historic Areas against Climate-related and other Hazards) est un projet H2020 dédié à la résilience des quartiers et sites historiques face aux aléas climatiques et autres risques naturels. Il combine gestion des risques de catastrophe, adaptation au changement climatique et gestion du patrimoine au sein d’un cycle intégré de gestion des risques appliqué aux zones historiques.

Les solutions développées comprennent :

- un cadre méthodologique de gestion des risques (ARCH Disaster Risk Management Framework) spécifiquement adapté aux zones historiques
- une suite d’outils numériques : systèmes d’information géoréférencés (HArIS/THIS), système d’aide à la décision (DSS), inventaire de mesures de résilience (RMI/RPVT) et outil d’auto‑évaluation de la maturité de résilience (RAD).

---

## 2. Systèmes d’information et gestion des données

### 2.1. HArIS – Historic Areas Information System

HArIS est un système d’information géographique orienté patrimoine, fondé sur une **architecture** orientée services (SOA), qui gère des données géoréférencées sur l’état historique et actuel des zones patrimoniales. Il relie la géométrie 2D/3D, les matériaux, les usages et le contexte environnemental afin d’alimenter des analyses de vulnérabilité, des modèles de vieillissement et des scénarios de dommages.

- 2.1.1. Architecture et base de données
    - SGBD relationnel (RDBMS) :
        
        Les données spatiales et alphanumériques sont stockées dans une base relationnelle (incluant géométrie, attributs, métadonnées, séries temporelles), assurant intégrité, requêtes complexes et interopérabilité avec les outils GIS.
        
    - SOA et interopérabilité :
        
        Les services web exposent les données sous forme de services standards (WMS/WFS, API REST), facilitant la réutilisation des composants dans d’autres plateformes (DSS, portails municipaux, applications de terrain).
        
- 2.1.2. Schéma de données patrimoniales
    
    Les actifs patrimoniaux sont structurés en grandes bases logiques, interconnectées par des identifiants uniques et des relations spatiales :
    
    1. Base CONSTRUCTION
        - Contenu : bâtiments historiques, ouvrages d’art, murs, infrastructures, ensembles bâtis, structures archéologiques.
        - Attributs :
            - géométrie (polygones 2D, modèles 3D, niveaux/facettes) ;
            - matériaux (pierre, brique, bois, métal, mortier) et propriétés mécaniques ;
            - fonctions et usages (résidentiel, cultuel, administratif, culturel) ;
            - état de conservation, pathologies connues (fissures, remontées capillaires, altérations de surface) ;
            - interventions passées (campagnes de restauration, renforcements, changements d’usage).
    2. Base OBJECT
        - Contenu : objets, éléments singuliers et composants : éléments d’architecture (corniches, colonnes, sculptures), mobilier urbain historique, œuvres d’art in situ, structures végétales remarquables (arbres isolés, haies historiques, alignements), éléments de jardins (fontaines, statues, bassins, pergolas).
        - Attributs :
            - caractéristiques physiques (dimensions, masse, matériaux, stratigraphie de surface) ;
            - métadonnées de localisation (coordonnées, relation à une construction ou un jardin, position dans l’espace 3D) ;
            - données d’état et pathologies ;
            - historique de conservation (dates, types et acteurs des interventions).
    3. Base MEASURE
        - Contenu : séries temporelles et indicateurs environnementaux (climat, qualité de l’air, hydrologie, vibrations, etc.).
        - Sources : capteurs in situ (température, humidité, vibrations, niveaux d’eau), stations météorologiques, données satellites, modèles climatiques.
        - Attributs : valeur, incertitude, pas de temps, provenance et qualité de la mesure.
    
    Cette structuration permet d’associer chaque actif (CONSTRUCTION/OBJECT) à des conditions environnementales spécifiques (MEASURE) pour des analyses couplées (vieillissement, risques climatiques).
    
- 2.1.3. Outils d’accès et d’analyse
    
    HArIS est exploité à travers trois grands types d’interfaces, intégrées au sein de la plateforme ARCH :
    
    1. Tableaux de bord GIS
        - Cartes interactives 2D/3D affichant les actifs, leur vulnérabilité, les aléas associés et les mesures environnementales.
        - Fonctions : filtrage par type d’actif, période, niveau de fragilité ; superposition d’indicateurs climatiques et de scénarios ; export de vues et de couches pour rapports.
    2. Fiches électroniques (Electronic Sheets)
        - Fiches détaillées par actif (bâtiment, objet, élément de jardin) donnant accès à l’ensemble des attributs, métadonnées, historiques d’interventions et liens vers documents externes (plans, rapports, photos, scans laser).
        - Fonctions : édition contrôlée, suivi des modifications, traçabilité des sources.
    3. Visionneuses 3D haute précision
        - Visualisation de modèles 3D (photogrammétrie, laser‑scan, drones), navigation immersive dans les sites historiques, couplage avec les attributs de HArIS.
        - L’intégration de méthodes de vision par ordinateur et de Deep Learning permet de détecter automatiquement, sur les nuages de points et orthophotos, des dégradations (fissures, décollements, pertes de matière) ou des évolutions morphologiques.

HArIS est ainsi à la fois un outil d’analyse (vulnérabilité, scénarios de dommages), un outil de simulation (via les liens au DSS) et un outil de médiation/vulgarisation pour les décideurs et le public.

### 2.2. THIS – Threats and Hazard Information System

THIS est le système « jumeau » de HArIS dédié à la description et à la quantification des menaces environnementales et des aléas, à différentes échelles temporelles et spatiales. Il fournit des indicateurs géoréférencés sur les menaces climatiques et environnementales, alimentant les analyses de risque et les simulations dans la plateforme ARCH.

- 2.2.1. Collecte et intégration multi‑sources
    
    THIS agrège des données issues de :
    
    - archives historiques (chroniques d’événements extrêmes, crues, sécheresses, incendies, séismes) ;
    - données en temps réel : réseaux de capteurs urbains (pluviomètres, capteurs de niveau d’eau, stations climatiques, stations air/qualité), capteurs structurels, réseaux de « crowd‑sensing » (signalements citoyens via applications, photos géolocalisées)
    - projections climatiques : scénarios RCP, jeux de données bioclimatiques, projections sectorielles (chaleur extrême, précipitations, sécheresse)
    - services climatiques dérivés des services Copernicus (notamment CAMS/C3S) pour les projections sous différents scénarios.
    
    Les données sont harmonisées, géoréférencées et stockées dans une base structurée compatible avec les standards d’information environnementale.
    
- 2.2.2. Indicateurs de menaces
    
    THIS produit un ensemble d’indicateurs thématiques essentiels pour les sites naturels et les jardins historiques :
    
    1. Indicateurs bioclimatiques (BIO1–BIO19)
        - Exemples : température moyenne annuelle, amplitude thermique annuelle, saisonnalité et concentration des précipitations, précipitations des mois les plus humides/sec, températures des mois extrêmes.
        - Utilisation : évaluer les conditions de survie des essences végétales, identifier les zones de stress thermique ou hydrique et anticiper des changements de niches climatiques.
    2. Indices de sécheresse et de chaleur
        - Standardised Precipitation-Evapotranspiration Index (SPEI) pour suivre les sécheresses météorologiques et agricoles ;
        - nombre de jours consécutifs secs (CDD), vague de chaleur (durée, intensité, fréquence), nombre de jours “tropicaux” ;
        - indicateurs de stress thermique humain (température ressentie, indices composites) pour les espaces publics historiques.
    3. Risque d’incendie
        - Combinaison : sécheresse (SPEI, CDD), températures extrêmes, humidité relative, vent (lorsque disponible), densité et type de combustible (végétation, matériaux).
        - Production de cartes de probabilités d’allumage et de propagation potentielles à l’échelle des sites.
    4. Risque d’inondation
        - Croisement de données topographiques, occupation des sols, réseaux d’évacuation des eaux pluviales et historiques de crue, avec les mesures de pluie et de niveau d’eau.
        - Production d’indicateurs de profondeur d’eau probable, vitesse d’écoulement, durée de submersion, zones de stagnation, spécifiquement dans les tissus urbains historiques.
    5. Services climatiques ad hoc
        - Utilisation de produits Copernicus (CAMS/C3S) pour générer des scénarios climatiques localisés pour différents horizons temporels (ex. vagues de chaleur à Valence jusqu’en 2100), sous plusieurs hypothèses d’émissions.
        - Génération de séries de variables climatiques entrantes pour les modèles d’impact sur le patrimoine et la végétation.

THIS fonctionne donc comme un référentiel central des aléas présents et futurs, couplé à HArIS et au DSS.

---

## 3. Simulations et scénarios

Le projet ARCH s’appuie sur un système de simulation intégré (DSS) permettant de construire et d’analyser différents types de scénarios, combinant paramètres climatiques, occupation des sols et événements extrêmes.

### 3.1. Scénarios d’aléas climatiques à long terme

Ces simulations reposent sur les trajectoires d’émissions RCP (IPCC) et couvrent plusieurs périodes temporelles de référence : historique, 2011–2040, 2041–2070, 2071–2100.

- 3.1.1. Scénarios d’émissions
    - RCP 4.5 :
        
        Scénario intermédiaire de stabilisation, avec des mesures d’atténuation limitant la hausse des concentrations de gaz à effet de serre.
        
    - RCP 8.5 :
        
        Scénario très pessimiste, correspondant à une tendance d’émissions élevées et prolongées, souvent choisi dans ARCH pour explorer la limite de résilience des sites historiques.
        
- 3.1.2. Phénomènes simulés
    1. Vagues de chaleur
        - Durée (incluant des vagues pouvant atteindre ~30 jours ou plus selon le site), intensité (écart aux normales, indices de canicule) et température maximale atteinte.
        - Effets sur les matériaux, la fréquentation des sites et la survivabilité des essences végétales dans les jardins historiques.
    2. Sécheresse
        - Calcul du nombre maximal de jours secs consécutifs (CDD) et d’indices de sécheresse (comme le SPEI), avec déclinaison pour sols, végétation et activités agricoles patrimoniales.
    3. Élévation du niveau de la mer
        - Pour les zones côtières pilotes (par exemple Hambourg), couplage de projections de niveau marin et de surcotes avec la morphologie locale, afin d’évaluer la submersion potentielle des quartiers historiques, les intrusions salines et les dommages sur infrastructures.

### 3.2. Scénarios d’utilisation des sols et micro‑climat

ARCH simule l’effet de différentes configurations d’occupation du sol sur le micro‑climat urbain, notamment sur la formation d’îlots de chaleur autour des zones patrimoniales.

Les principaux scénarios sont :

1. Scénario de référence (Current)
    - Basé sur l’occupation actuelle des sols (bâti, voirie, végétation, eau) à partir de données cartographiques et d’observations locales.
2. Scénario « Gris » (urbanisation modérée)
    - Urbanisation progressive de zones agricoles non protégées ou de friches, augmentation des surfaces minérales et du bâti, réduction limitée des surfaces végétalisées.
    - Objectif : quantifier l’augmentation de température locale et la réduction du confort thermique dans le voisinage des biens patrimoniaux.
3. Scénario « Noir » (urbanisation totale)
    - Urbanisation maximale incluant, dans un scénario théorique, des zones initialement protégées, remplacées par du bâti ou des surfaces imperméables.
    - Utilisation : exprimer la valeur protectrice maximale de la végétation par comparaison avec cet extrême, plus que décrire un futur plausible.
4. Scénario « Vert » (restauration/ré‑naturalisation)
    - Transformation de zones abandonnées, imperméabilisées ou sous‑utilisées en surfaces végétalisées (parcs, jardins, zones agricoles) ou en trames vertes/bleues.
    - Objectif : estimer les gains de rafraîchissement, la réduction d’îlots de chaleur, l’amélioration de l’infiltration de l’eau et l’atténuation des impacts sur le bâti historique.

Les modèles simulent les champs de température de surface et de l’air, parfois couplés à des modèles d’écoulement d’air urbain ou de rayonnement, pour quantifier les effets micro‑climatiques.

### 3.3. Scénarios de catastrophes soudaines

Ces scénarios explorent la réaction du site à des événements brutaux, avec calcul des dommages matériels et humains.

- 3.3.1. Scénarios sismiques
    1. Événements historiques
        - Rejeu de séismes documentés (position, magnitude, profondeur, mécanisme de faille) pour évaluer la réponse des structures historiques à des événements déjà survenus.
    2. Événements définis par l’utilisateur
        - L’utilisateur spécifie divers paramètres (épicentre, profondeur, magnitude Mw, type de faille, direction de rupture, durée d’impulsion) dans l’interface du DSS.
        - Les champs d’accélération et de réponse dynamique sont projetés sur le bâti historique, permettant une estimation des niveaux de dommage structurel et des pertes potentielles (coûts, victimes, indisponibilité fonctionnelle).
- 3.3.2. Scénarios d’inondations pluviales
    - Entrées : événements de pluie intense (épisodes observés ou futurs), modèles de ruissellement urbain et de drainage, topographie à haute résolution.
    - Sorties :
        - cartes de profondeur d’eau et de vitesse dans les rues historiques ;
        - zones d’accumulation, débordement de réseaux, interactions avec les bâtiments et infrastructures ;
        - estimation des dommages matériels (bâtiments, collections, voirie) et des conséquences pour les personnes (exposition, accessibilité, évacuation).

### 3.4. Scénarios d’incendie

ARCH n’implémente pas la simulation détaillée de la propagation des flammes mais encadre le risque en amont et les dommages potentiels en aval.

1. Avant l’incendie : évaluation du risque
    - THIS agrège les conditions favorables à l’allumage : épisodes de chaleur extrême, séries prolongées de jours secs, faible humidité des combustibles, densité de végétation inflammable, vent.
    - Des cartes de probabilité d’ignition et de danger d’incendie sont générées pour les jardins, parcs et zones périurbaines proches du patrimoine bâti.
2. Après l’incendie : estimation des dommages
    - HArIS fournit les propriétés des matériaux (bois, pierre, métal, couvertures, menuiseries) et la configuration spatiale des objets et constructions.
    - À partir de cela, on estime les pertes probables en cas d’incendie (éléments susceptibles d’être détruits ou fortement dégradés), sans modéliser précisément le cheminement du feu dans l’espace urbain.

---

## 4. Espaces naturels, jardins et sols comme actifs patrimoniaux

ARCH considère les espaces naturels (jardins, parcs, terres agricoles associées, zones humides) comme des actifs patrimoniaux à part entière, et non comme un simple décor autour des monuments.

### 4.1. Représentation sémantique et physique

1. Objets naturels dans HArIS
    - Chaque composant significatif d’un jardin (arbre remarquable, haie historique, massif, pelouse structurée) peut être enregistré comme un « objet » dans la base OBJECT, avec ses propriétés physiques (dimensions, âge estimé, type de feuillage) et biologiques (espèce, état sanitaire).
    - Les relations spatiales et fonctionnelles entre ces objets et le bâti (proximité des façades, ombrage, protection vis‑à‑vis du vent) sont explicitées dans le modèle de données.
2. Occupation des sols (Land Use)
    - Les cartes d’occupation des sols distinguent finement : forêts, jardins urbains, terres arables, prairies, zones humides, surfaces imperméabilisées, surfaces en eau.
    - Cette distinction sert à simuler l’absorption de chaleur (albédo, capacité thermique, évapotranspiration) et la gestion de l’eau (infiltration, ruissellement, stockage) autour des sites historiques.

### 4.2. Rôle de « bouclier » des jardins et sols naturels

ARCH fait partie des projets qui quantifient explicitement les bénéfices des jardins et espaces végétalisés pour la résilience du bâti historique.

1. Régulation thermique
    - Modélisation de l’effet de refroidissement par évapotranspiration et ombrage des jardins, réduisant l’intensité des îlots de chaleur au voisinage des monuments.
    - Évaluation des gains en confort thermique, de la réduction de la fatigue thermique des matériaux et de la diminution des cycles extrêmes de dilatation/contraction.
2. Gestion des eaux pluviales
    - Les sols naturels sont représentés comme zones d’absorption/infiltration, avec des paramètres de perméabilité, stockage et rugosité de surface.
    - ARCH simule comment un jardin ou un parc ralentit l’écoulement, réduit les hauteurs d’eau dans les rues adjacentes, protège les fondations des bâtiments historiques et diminue la charge sur les réseaux d’évacuation.

### 4.3. Surveillance de la « santé » de l’environnement naturel

THIS inclut des indicateurs spécifiquement dédiés à la santé écologique des espaces naturels

1. Indices de végétation
    - Utilisation de données satellites (par exemple NDVI, EVI) et éventuellement de données drone pour suivre la vigueur et la densité de la végétation dans les jardins et parcs historiques.
    - Détection des zones de dépérissement, de stress ou de changement de couverture végétale susceptibles d’accroître les risques (incendie, érosion, glissements).
2. Besoins en eau et stress hydrique
    - Calcul du bilan entre évapotranspiration potentielle et précipitations, complété par des informations sur les pratiques d’irrigation lorsqu’elles existent.
    - Identification des périodes où un jardin historique entre en zone de stress hydrique, avec alerte sur les essences anciennes particulièrement vulnérables ou difficiles à remplacer.
3. Indicateurs agro‑climatiques
    - Pour les sites agricoles patrimoniaux (vignobles historiques, cultures traditionnelles), suivi des périodes de croissance, des risques de gel tardif, de chaleur précoce ou de vagues de chaleur pendant des phases sensibles (floraison, maturité).
    - Ces indicateurs servent à préserver à la fois la production et le patrimoine immatériel associé (savoirs‑faire, paysages culturels).

### 4.4. Vulnérabilité et dynamique des sols

ARCH ne se limite pas aux éléments visibles en surface, mais prend en compte la structure et la dynamique des sols sous‑jacents.

1. Micro‑zonage géotechnique
    - Étude de la composition (argiles, limons, sables, roches), de l’hétérogénéité et des conditions hydriques des sols de jardins et de zones bâties.
    - Identification de secteurs susceptibles de connaître glissements de terrain, tassements différentiels ou amplification locale des mouvements sismiques.
2. Interaction sol–structure
    - Analyse des effets de l’assèchement des sols (liés aux sécheresses récurrentes) sur les argiles gonflantes, pouvant provoquer retraits et gonflements saisonniers.
    - Mise en relation de ces phénomènes avec l’apparition de fissures dans les murs, la déformation de fondations, la déstabilisation de clôtures et murs de jardins historiques.

---

## 5. Synthèse des technologies et approches

Le tableau ci‑dessous résume les principaux composants technologiques du projet ARCH et leur rôle.

| Composant | Type de technologie | Rôle principal | Données clés |
| --- | --- | --- | --- |
| HArIS | Système d’information géographique patrimonial (SOA, RDBMS, GIS, 3D) | Stockage et accès aux données sur les actifs et leur état, support aux analyses de vulnérabilité et scénarios de dommages | Actifs CONSTRUCTION et OBJECT, mesures environnementales MEASURE, géométries 2D/3D, historiques d’interventions |
| THIS | Système d’information sur les menaces et aléas | Fourniture d’indicateurs climatiques, hydrologiques et environnementaux, présents et futurs | Indicateurs bioclimatiques, indices de sécheresse, risques d’incendie et d’inondation, projections climatiques/copernicus |
| DSS ARCH | Plateforme web SIG d’aide à la décision | Construction et analyse de scénarios (climat, occupation des sols, catastrophes), évaluation des risques | Scénarios RCP, configurations d’urbanisation, événements sismiques et pluviométriques, sorties de modèles de dommages |
| RMI / RPVT | Base de mesures de résilience et outil de planification | Identification, évaluation et planification des mesures d’adaptation et de renforcement de la résilience | Catalogue de mesures (structurales, organisationnelles, fondées sur la nature), chemins de mise en œuvre |
| RAD | Outil d’auto‑évaluation de la maturité de résilience | Suivi de la progression d’une zone historique dans son cycle de gestion des risques | Indicateurs de gouvernance, préparation, réponse, récupération, intégration patrimoine–climat |

ARCH réunit ces différents modules (HArIS, THIS, DSS et outils d’aide à la décision) pour constituer un **écosystème numérique intégré et complet**,
 permettant une description fine et multidimensionnelle des sites 
historiques, une caractérisation précise des aléas climatiques et 
naturels présents comme futurs, l’exécution de simulations de scénarios 
prospectifs variés, et l’élaboration de trajectoires d’adaptation 
scientifiquement robustes et opérationnelles.

Financé par le programme Horizon 2020 à hauteur de **5,98 millions d’euros**
 sur 48 mois (2019-2023), le projet déploie ses solutions pilotes sur 8 
sites historiques européens emblématiques – Istanbul (pilote principal),
 Rome, Valence, Hambourg, etc. – et met à disposition l’ensemble de ses **composants logiciels en open source** (code, bases de données modulaires, API, documentation technique) sous 
licences libres, facilitant ainsi réutilisation et extension par d’autres institutions ou collectivités.

Les **similitudes conceptuelles et opérationnelles** avec le projet **ATLAS** (présumé cibler la résilience patrimoniale ou urbaine dans un contexte comparable) sont frappantes :

- **Préoccupations communes** : vulnérabilité des tissus historiques aux changements climatiques
(îlots de chaleur, sécheresses, inondations), rôle protecteur des
espaces verts patrimoniaux, besoin d’outils d’aide à la décision
intégrant bâti, végétation et aléas.
- **Solutions technologiques transférables** :
    - Architecture SOA interopérable, facilement intégrable à des systèmes existants comme ceux d’ATLAS.
    - Modèles de données HArIS riches et normalisés (CONSTRUCTION/OBJECT/MEASURE),
    directement réutilisables pour documenter des sites similaires.
    - Pipeline THIS → DSS pour la simulation multi-scénarios (RCP 4.5/8.5,
    urbanisation "Gris/Noir/Vert", séismes/inondations), applicable aux
    problématiques d’ATLAS.
    - Outils de visualisation 3D et tableaux de bord SIG, déjà validés auprès de 8 gestionnaires de sites UNESCO.

---

## Limites identifiées du projet ARCH

Malgré ses avancées significatives, le projet ARCH présente des lacunes 
notables qui limitent son exhaustivité pour une gestion intégrale des 
risques sur sites patrimoniaux. Ces manques concernent à la fois la 
richesse des données descriptives et les capacités de simulation 
dynamique.

### Enrichissement des données descriptives

La représentation fine des sites via HArIS (tables CONSTRUCTION, OBJECT, 
MEASURE) reste perfectible sur plusieurs dimensions critiques :

- **Caractéristiques techniques détaillées** : enrichissement des attributs pour bâtiments, artefacts, axes de circulation (capacités de charge dynamiques, configurations alternatives).
- **Données socio-démographiques** : absence de classification fine des populations (résidents permanents, touristes, saisonnalité, vulnérabilités spécifiques – PMR, enfants, seniors).
- **Capacités opérationnelles des secours** : pas de modélisation des infrastructures d’intervention (postes de secours, points d’eau, accès véhicules, temps de réponse théoriques).
- **Bilan des sinistres passés** : données limitées sur les victimes (localisation spatiale des impacts humains, typologies de blessures, facteurs aggravants).
- **Écologie patrimoniale** : protection des espèces végétales historiques sous-développée (listesd’essences protégées, statuts réglementaires, stratégies de sauvegardeface aux stress climatiques).

### Déficits en simulation dynamique

ARCH excelle dans les scénarios climatiques, sismiques et hydrologiques, mais présente deux absences majeures :

1. **Simulation de la propagation des incendies** : bien que THIS fournisse des indicateurs préalables excellents (SPEI,
CDD, charge de combustible végétale, conditions d’allumage) et HArIS
détaille les matériaux inflammables (bois, végétation sèche), le projet
s’arrête aux phases « avant » et « après », sans modéliser la dynamique
de propagation des flammes (chemins préférentiels, vitesses d’avancée,
points chauds, interaction bâti-végétation).
    
    L’équipe **Soc-SIM-K** comble précisément ce vide avec ses 
    modèles de feu 3D adaptés aux sites patrimoniaux denses, exploitables 
    directement sur les bases HArIS existantes.
    
2. **Comportements humains sous crise** : les simulations DSS se concentrent sur les dommages matériels,ignorant les flux humains (panique, engorgements, évacuations, zones derefuge). Or **Soc-SIM-K** développe des agents comportementaux réalistes (piétons, véhicules secours, touristes désorientés), parfaitement compatibles avec les géométries et capacités des axes de circulation HArIS.

---

# Étude C2Impress

C2Impress est un projet Horizon Europe (2023–2026) coordonné par le Joint Research Centre (JRC) et impliquant plus de 18 partenaires européens. Son objectif est de développer un cadre intégratif de co‑création pour améliorer la compréhension, la préparation et la réponse aux risques naturels et socio‑environnementaux multiples, notamment les inondations, sécheresses, incendies et aléas côtiers.

## 1. Cadre général et objectifs

La vision de C2Impress repose sur :

- L’association entre science, autorités locales et citoyens ;
- L’utilisation de simulations multi‑aléas et d’indicateurs d’impact social et culturel ;
- La co‑construction d’outils d’aide à la décision pour renforcer la résilience locale.

Les *Living Labs* déployés servent à tester des méthodologies reproductibles pour d’autres contextes patrimoniaux, dont les sites historiques et leurs environnements paysagers.

---

## 2. Systèmes d’information et gestion des données

### 2.1. Système d’Informations

- 2.1.1. Architecture et base de données
    
    Le système central de C2Impress repose sur une architecture distribuée et interopérable, conforme aux principes FAIR (Findable, Accessible, Interoperable, Reusable). Il intègre des données spatio‑temporelles (SIG), observations de terrain et résultats de modélisations.
    
    Une base géospatiale (PostSIG) permet le croisement d’indicateurs physiques, humains et patrimoniaux à différentes échelles (bâtiment, quartier, bassin versant).
    
- 2.1.2. Schéma de données patrimoniales
    
    Bien que le projet cible avant tout la résilience urbaine, C2Impress introduit la notion de biens culturels comme éléments sensibles du territoire, intégrés aux couches de vulnérabilité. Les « cultural assets » sont classés selon leur valeur, leur usage et leur exposition aux aléas.
    
    Dans une optique de transposition, un schéma de données patrimoniales appliqué aux jardins historiques pourrait reprendre ce modèle : entités végétales, ouvrages hydrauliques, topographie, sols, valeurs symboliques.
    
- 2.1.3. Outils d’accès et d’analyse
    
    Un tableau de bord décisionnel permet aux acteurs locaux de visualiser la propagation d’un aléa ou l’évolution d’indicateurs de résilience. Des modules d’analyse multicritère 
    soutiennent les choix d’aménagement. Ces outils sont conçus pour une appropriation par des publics non experts, un point clé pour la médiation dans les sites patrimoniaux.
    

### 2.2. Threats and Hazard Information System

Dans C2Impress, l'équivalent fonctionnel du THIS (Threats and Hazard Information System) d'ARCH est la plateforme SoS4MHRIN (System-of-Systems for Multi-Hazard Risk Intelligence Network).
 Cette infrastructure centralise et analyse en temps réel les données sur les aléas multiples (inondations, incendies, vagues de chaleur, sécheresses composées), en s'appuyant sur l'ESDI (Earth System Dynamic Intelligence) pour des prédictions fines et dynamiques des risques multi-aléas.

- 2.2.1. Collecte et intégration multi-sources
    
    SoS4MHRIN orchestre une collecte continue et hétérogène de données provenant de multiples échelles et vecteurs :
    
    - Sources satellitaires : Données Copernicus, MODIS pour les feux et températures de surface, complétées par des prévisions météo.
    - Capteurs in situ et IoT : Réseaux de stations terrestres (pluviomètres, anémomètres, capteurs humides sols), déployés dans les Living Labs (ex. Thessalonique, Malte), avec densité accrue près des sites critiques patrimoniaux.
    - Données urbaines et ouvertes : OpenStreetMap, bases locales d'infrastructures critiques, archives hydro-météo historiques, enrichies par crowdsourcing citoyen via
    applications mobiles (signalements d'anomalies locales).
    - Données socio-économiques : Couches démographiques (densité population, vulnérabilité sociale), intégrées pour contextualiser les expositions humaines.
    
    L'intégration multi-sources repose sur des flux dynamiques qui fusionnent ces données en temps quasi-réel. Les approches de data fusion (statistiques bayésiennes et apprentissage automatique) génèrent des cartes de risque composites mises à jour toutes les 15-60 minutes selon l'aléa. Pour les jardins patrimoniaux, cette capacité permet de suivre 
    l'évolution fine des conditions hydriques et thermiques affectant les sols et la végétation, en croisant par exemple pluviométrie satellitaire avec mesures locales d'humidité racinaire.
    
- 2.2.2. Indicateurs de menaces
    
    SoS4MHRIN produit un ensemble d'indicateurs de menaces normalisés (0-1), couvrant à la fois les aléas climatiques extrêmes et leurs impacts écologiques, adaptés à une évaluation multi-échelle :
    
    - Variables climatiques primaires :
        - Températures extrêmes et Heat Stress Index (combinaison température/humidité perçue).
        - Pluviométrie intense (intensité, durée, fréquence pour inondations pluviales).
        - Vents forts
        - Indices de sécheresse (SPI, SPEI sur 1-12 mois).
    - Paramètres écologiques et environnementaux :
        - Santé des sols (humidité volumique, compaction, érosion potentielle).
        - Stress hydrique végétal.
        - Charge de biomasse inflammable et stabilité des pentes.

Ces indicateurs sont composites et probabilistes, intégrant des seuils d'alerte contextualisés (ex. risque feu élevé si FWI > 30 ET humidité sol < 20%). Ils sont particulièrement transposables aux jardins historiques : un jardin peut être monitoré via un tableau de bord personnalisé montrant la dégradation progressive ou des risques soudains. Dans un contexte patrimonial, ces métriques permettent notamment de quantifier comment un jardin agit comme tampon (réduction ruissellement de 40% via infiltration sols), tout en identifiant ses vulnérabilités propres (sols argileux gonflants sous sécheresse cyclique).

Cette approche SoS4MHRIN offre ainsi une vigilance proactive, essentielle pour préserver les sites historiques face aux aléas climatiques composés.

---

## 3. Simulations et scénarios

C2Impress intègre des simulations avancées au sein de sa plateforme **SoS4MHRIN**, principalement via l'**Earth System Dynamic Intelligence (ESDI)** et des **modèles dynamiques opérationnels**.
 Ces outils permettent de prédire avec une haute résolution 
spatio-temporelle (de l'échelle événementielle à climatique) les risques
 d'aléas uniques ou multiples sous scénarios climatiques variés, en 
passant d'une approche "hazard-centric" à une évaluation centrée sur les
 lieux et les populations. Les simulations sont validées empiriquement 
dans quatre sites pilotes (Egaleo en Grèce, Ordu en Turquie, et deux 
autres en Europe du Sud), couvrant des contextes urbains et côtiers 
vulnérables.

### 3.1. Phénomènes simulés

Les simulations de C2Impress ciblent les **extrêmes météorologiques composés**, ainsi que des événements non standards à fort impact. Elles modélisent les **dangers hydrométéorologiques principaux** : inondations fluviales et pluviales, feux de forêt, vagues de chaleur, glissements de terrain induits par pluies intenses, et sécheresses 
prolongées.

L'innovation réside dans la capture des **interactions entre aléas** (effets en cascade ou stress combinés), comme une sécheresse amplifiant les risques d'incendie suivie d'inondations post-feu. Des **modèles de simulation par système de systèmes** et **agent-based models (ABM)** évaluent les impacts multidimensionnels (exposition, vulnérabilité 
physique/sociale, résilience adaptative), avec une incertitude réduite grâce à des prédictions fines.

Pour les espaces patrimoniaux et jardins historiques, ces simulations sont hautement adaptables : elles permettent d'étudier la **dynamique hydrique des sols** (infiltration/ruissellement sous inondations), le **stress végétal** (perte de biomasse sous chaleur/sécheresse), ou les **impacts sur la biodiversité** (espèces sensibles aux composés extrêmes), en taguant les jardins comme "natural buffers" dans les modèles.

- 3.1.1. Scénarios d’émissions
    
    C2Impress s'appuie explicitement sur les scénarios climatiques **RCP 4.5** et **RCP 8.5**, pour ses projections locales à haute résolution. Ces scénarios calibrent les simulations à horizons moyen (2030-2050) et long terme (2070-2100), testant la résilience sous conditions progressives ou extrêmes.
    

### 3.2. Scénarios d’utilisation des sols et micro-climat

Les projections d'**utilisation des sols (LULC)** dérivent de séries comme CORINE Land Cover, simulées via ABM pour anticiper l'urbanisation, la perte de couverture végétale, et leurs effets sur le **micro-climat.** Dans les jardins historiques en milieu dense, ces scénarios uantifient comment la végétation patrimoniale atténue la chaleur ou régule l'humidité, tout en évaluant la dégradation potentielle sous urbanisation.

### 3.3. Scénarios de catastrophes soudaines

- 3.3.1. Scénarios sismiques
    
    Les simulations incluent les séismes, via des modèles d'impact sur infrastructures critiques et glissements associés. Transposables aux sites historiques, elles évaluent la réponse des structures patrimoniales (murs de soutènement, bassins de jardins) à la liquéfaction des sols ou secousses amplifiées par saturation hydrique.
    
- 3.3.2. Scénarios d’inondations pluviales
    
    Modélisation des inondations pluviales et fluviales, avec alertes en temps réel et prédictions d'étendue. À haute résolution spatiale, ces outils analysent la gestion des bassins versants dans les parcs/jardins, simulant ruissellement, surcharge drains historiques, et érosion des parterres.
    
- 3.3.3. Scénarios d’incendie
    
    Les feux de forêt sont simulés en intégrant sécheresse, vents et biomasse, avec alertes précoces et propagation dynamique (ex. via indices comme FWI). Pour les jardins patrimoniaux, ces modèles guident la planification végétale (espèces non inflammables, barrières vertes), évaluant comment les sols secs sous RCP 8.5 augmentent la vulnérabilité à l'embrasement.
    

Ces simulations, ancrées dans une co-création avec acteurs locaux, 
fournissent des tableaux de bord pour des plans d'urgence adaptés aux 
sites historiques.

---

## 4. Espaces naturels, jardins et sols comme actifs patrimoniaux

Oui,
 plusieurs éléments peuvent enrichir cette section en exploitant plus 
explicitement le cadre conceptuel de C2Impress, qui traite les espaces 
naturels comme des **"Natural Heritage Buffers"** ou **"Green Resilience Layers"** dans ses ontologies et modèles multi-aléas. Ces actifs sont intégrés non comme passifs, mais comme **composants dynamiques**
 influençant l'exposition et la vulnérabilité globale des sites. Voici 
une version détaillée, avec ajouts factuels sur la modélisation, les cas
 d'usage pilotes et les liens directs à votre thématique 
jardins-patrimoine.

### 4.1. Représentation sémantique et physique

C2Impress utilise une **ontologie sémantique unifiée** pour modéliser les entités territoriales, étendant naturellement aux **éléments paysagers historiques** comme les jardins, parterres, alignements d'arbres ou réseaux hydrauliques patrimoniaux. Les classes ontologiques incluent 
"HeritageAsset" (biens bâtis), "NaturalBuffer" (végétation/sols) et "DynamicLayer" (évolution temporelle), avec propriétés comme texture de sol, couvert végétal (pourcentage NDVI) ou perméabilité hydrique.

Cette représentation physique repose sur des données LiDAR et altimétriques pour la
 topographie fine des jardins (reliefs micro-morphologiques, drains souterrains), couplée à des graphes de connaissances reliant un arbre patrimonial à son rôle hydrique (racines absorbantes) ou sismique (stabilisation sols).

### 4.2. Rôle des jardins et sols naturels

Dans C2Impress, les espaces verts et sols sont positionnés comme **amplificateurs actifs de résilience territoriale**, au-delà d'une simple couche protectrice : ils modulent les flux énergétiques/hydriques et absorbent les chocs multi-aléas. Les simulations des sites pilotes quantifient des bénéfices concrets : réduction de 30-50% du ruissellement pluvial via infiltration sols-jardins, atténuation de 3-6°C des îlots de chaleur par évapotranspiration, et maintien de 20-40% de biodiversité refuge sous stress combiné.

Dans les sites patrimoniaux, cette fonction écologique se superpose à une **valeur culturelle et identitaire forte**, une dimension que C2Impress commence à intégrer via des indicateurs "Cultural Resilience Score".

### 4.3. Surveillance de la « santé » de l’environnement naturel

C2Impress, via SoS4MHRIN, combine télédétection et capteurs IoT (humidité racinaire, température sol/canopée, capteurs de stress hydrique via conductance stomatique). Dans les Living Labs, des alertes proactives sont générées (ex. : détection précoce de jaunissement foliaire sous sécheresse RCP 4.5), avec tableaux de bord temps réel accessibles aux gestionnaires patrimoniaux.

Appliqué aux jardins historiques, cela permet une **surveillance holistique** : vitalité végétale, humidité du sol (seuils critiques pour argiles gonflantes), température de surface, et santé microbiologique (indicateurs via perméabilité). Des boucles de rétroaction (citoyens signalant anomalies via app) renforcent la précision, idéal pour une gestion préventive des sites.

### 4.4. Vulnérabilité et dynamique des sols

L'analyse multi-sources de C2Impress modélise la **vulnérabilité des sols** comme un processus dynamique, exposée aux inondations (érosion/surcharge), stress hydrique (fissuration argileuse) et interactions (séisme + saturation menant à liquéfaction). Des indicateurs comme le "Soil Vulnerability Index" intègrent compaction, porosité, charge organique et pente, prédisant des défaillances .

Ces dynamiques se traduisent en **leviers de résilience patrimoniale** : un sol jardinier stable sous aléas protège fondations historiques et végétation ; des scénarios testent des interventions.

---

## 5. Synthèse des technologies et approches

C2Impress déploie un écosystème technologique cohérent, centré sur la plateforme **SoS4MHRIN** (System-of-Systems for Multi-Hazard Risk Intelligence Network), soutenue par l'**ESDI (Earth System Dynamic Intelligence)** et l'**IPAI (Information Physical Artificial Intelligence)**.
Cette architecture intègre des simulations dynamiques, une ontologie sémantique unifiée et des outils participatifs pour une gestion proactive des risques multi-aléas, validés dans quatre sites pilotes (Egaleo-Grèce, Ordu-Turquie, et deux autres en Europe du Sud).

### Technologies principales

- **Plateforme d'intelligence multi-risques** : SoS4MHRIN centralise données satellitaires (Copernicus/Sentinel), IoT in situ et crowdsourcing citoyen, avec fusion en temps réel pour cartes de risque haute résolution.
- **Modélisation et simulations** : Agent-Based Models (ABM) pour scénarios LULC et micro-climats ; modèles physiques pour aléas composés (inondations + feux) sous RCP4.5/8.5.
- **Ontologie et données** : Schéma RDF/OWL modélisant biens culturels et "Natural Buffers", stocké en bases géospatiales interopérables (FAIR).
- **Outils décisionnels** : Tableaux de bord interactifs, microservices multicritères et alertes
probabilistes.
- **Engagement citoyen** : Applications mobiles et co-création via Living Labs pour intégration perceptions locales.

---

## Bornes de C2Impress

## Forces identifiées

- **Approche holistique "place and people-centred"** : Passage du hazard-centré à une évaluation multidimensionnelle (exposition, vulnérabilité socio-culturelle, résilience adaptative),
réduisant l'incertitude prédictive.
- **Interopérabilité et scalabilité** : Flux dynamiques multi-sources et simulations fines, yransposables aux jardins patrimoniaux comme tampons écologiques.
- **Co-création inclusive** : Implication science-autorités-citoyens pour outils accessibles, favorisant l'appropriation locale dans sites historiques et l’aide à la décision.
- **Comportements humains sous crise** : Les comportements humains sont simulés par des agents archétypaux, qui émule une part des biais humains dans les contextes de crise. Pour autant, il y a peu de place à la représentation des niveaux d’informations et l’impact des secours civils, du temps et des capacités d’inventions des secours..

## Limites identifiées du projet

- **Caractéristiques techniques détaillées** : Enrichissement insuffisant des attributs pour bâtiments, artefacts,axes de circulation (capacités de charge dynamiques, configurations
alternatives) ; actifs patrimoniaux bâtis et naturels sous-granularisés (inventaires végétation/sols historiques limités, absence de palynologie ou archéologie paysagère pour jardins).
- **Données socio-démographiques** : Absence de classification fine des populations (résidents permanents, touristes, saisonnalité, vulnérabilités spécifiques – PMR, enfants, seniors).
- **Capacités opérationnelles des secours** : Pas de modélisation des infrastructures d'intervention (postes de secours, points d'eau, accès véhicules, temps de réponse théoriques).
- **Bilan des sinistres passés** : Données limitées sur les victimes (localisation spatiale des impacts humains, typologies de blessures, facteurs aggravants).
- **Écologie patrimoniale** : Protection des espèces végétales historiques sous-développée (listes
d'essences protégées, statuts réglementaires, stratégies de sauvegarde
face aux stress climatiques).

---

# Étude Arches-HER

Le projet Arches-HER s’inscrit dans l’écosystème du logiciel Arches, un système d’inventaire et de gestion du patrimoine immobilier développé par le Getty Conservation Institute (GCI) et le World Monuments Fund (WMF). 

### 1. Cadre général et objectifs

- Arches est un SIG Web « open source », normalisé, destiné à l’inventaire et à la gestion du patrimoine immobilier (sites archéologiques, bâtiments,paysages culturels, ensembles patrimoniaux).
- Les objectifs stratégiques affichés sont : amélioration de la gestion des données pour la conservation, adoption large dans le secteur patrimonial, et reconnaissance comme système de référence pour la gestion normalisée des données patrimoniales.
- Arches-HER peut donc être interprété comme une déclinaison dédiée aux Historic
Environment Records : un cadre pour structurer, documenter et exploiter des données patrimoniales à l’échelle de territoires (villes, régions, États) afin d’éclairer la planification, l’évaluation d’impact et la gestion des risques.

---

## 2. Systèmes d’information et gestion des données

### 2.1. Information System

- 2.1.1. Architecture et base de données
    
    Arches implémente une architecture Web d'entreprise centrée sur une base de données PostgreSQL/PostGIS pour les données spatiales et relationnelles, enrichie d'un graphe sémantique via le moteur de requête SPARQL (Arches utilise souvent Apache Jena ou une couche RDF triplestore intégrée).
    
    - **Extension d'ontologie** : Fondé sur CIDOC CRM comme ontologie de base, Arches étend le modèle avec des concepts spécifiques au patrimoine immobilier (ex. : HER-specific extensions pour ressources comme "Historic Assets", relations spatiales, workflows de condition assessment). Le dépôt GitHub "archesproject/cidoc-crm-ontology" inclut "arches_crm_enhancements.xml" pour modéliser événements de conservation, menaces et acteurs locaux, assurant l'interopérabilité sémantique.
    - **Pas de système de simulation intégré** : Aucune implémentation native de simulations dynamiques (RCP, hydrologie, etc.) ; Arches se limite à importer des résultats sous forme de couches PostGIS ou RDF (ex. : rasters d'aléas climatiques croisés avec ressources patrimoniales via géo-requêtes).
    - **Bases de données croisées** : Supporte l'intégration multi-sources via mappings RDF pour croiser inventaires legacy, données LIDAR, APIs externes (ex. : EAMENA, Getty Vocabularies) et bases ouvertes (OSM, Copernicus). Les "branches" et "graph branches" permettent des workflows collaboratifs pour valider les croisements sans duplication.
    
    Cette approche priorise la flexibilité sémantique et spatiale pour les HER, avec personnalisation via "resource models" (schémas modulaires) et vocabulaires contrôlés.
    
- 2.1.2. Schéma de données patrimoniales
    - Arches intègre des normes internationales de description du patrimoine (Core Data Standard pour sites et monuments archéologiques, Core Data Index pour bâtiments historiques) permettant d’identifier un « minimum de données essentielles » pour documenter les lieux patrimoniaux.
    - Le modèle conceptuel exploite l’ontologie CIDOC CRM comme ontologie de référence pour structurer les informations (acteurs, événements, objets, lieux, temporalités).
    - Concrètement, un HER basé sur Arches décrit chaque ressource patrimoniale comme un
    ensemble d’entités reliées (ressource, événements historiques, interventions de conservation, valeurs, menaces, sources documentaires), plutôt que comme une simple fiche à plat.
- 2.1.3. Outils d’accès et d’analyse
    - Le système offre des interfaces de consultation Web, avec recherche par carte, filtres, requêtes attributaires, et visualisation des fiches détaillées.
    - Il est conçu pour servir à la fois les gestionnaires (analyse, monitoring, évaluation d’impact) et le grand public (sensibilisation, valorisation), avec des profils d’accès différenciés.
    - Arches peut être utilisé pour la préparation des décisions (planification urbaine, conservation, gestion de risques) en croisant les données patrimoniales avec d’autres couches spatiales, grâce à son intégration SIG. Mais ne bénéficie d’aucun outil intégré d’aide à la décision

### 2.2. Threats and Hazard Information System

- 2.2.1. Collecte et intégration multi‑sources
    - Arches supporte l’intégration de données provenant de multiples sources : inventaires existants, cartes historiques, images satellites, bases nationales, projets de recherche, etc., avec la possibilité de pré-traiter et normaliser les données avant intégration.
    - Les implémentations régionales montrent son usage pour documenter des patrimoines menacés à partir de sources diverses (sites existants, imagerie, archives), dans une même base gérée et partagée.
    - Pour un HER orienté risques, on peut envisager l’intégration de couches supplémentaires : aléas (inondation, érosion, sismicité), usages du sol, infrastructures, données climatiques, sous forme de couches SIG ou de liens vers d’autres systèmes.
- 2.2.2. Indicateurs de menaces
    - Arches prend en charge la documentation des menaces et risques à travers des champs et entités dédiés (catégories de menaces, intensité, probabilité, effets sur l’intégrité, statut de gestion).
    - Le système peut servir de base à un suivi des conditions et des menaces à long terme, ce qui permet d’en dériver des indicateurs (nombre de sites en risque élevé, évolution des menaces par zone, etc.), même si la construction des indicateurs dépend des personnalisations
    locales. Une telle extension demanderait l’implémentation de toute une extension de la représentation de l’Aléa.

---

## 3. Simulations et scénarios

### 3.1. Phénomènes simulés

- De la même façon, Arches n’est pas un moteur de simulation pour les phénomènes physiques (pluie, ruissellement, propagation du feu, etc.), mais un cadre pour stocker, géoréférencer et exploiter les résultats de tels modèles.
- Il serait pour autant envisageable d’exploiter ce type de stockage, pour améliorer la communicabilité des résultats de simulation.

---

## 4. Espaces naturels, jardins et sols comme actifs patrimoniaux

### 4.1. Représentation sémantique et physique

- Arches permet de définir des types de ressources pour les paysages culturels, jardins historiques et ensembles paysagers, avec géométrie (emprise, limites, éléments internes) et description structurée.
- Le modèle fondé sur CIDOC CRM permet de représenter les relations entre végétation, structures bâties, interventions de gestion et événements historiques, ce qui est adapté aux jardins et sols comme entités patrimoniales complexes.
- Les jardins et sols peuvent être modélisés comme des ressources avec des valeurs spécifiques (écologiques, esthétiques, sociales, symboliques) et des fonctions (régulation du micro‑climat, infiltration, protection contre l’érosion).
- Dans un HER, ils peuvent être intégrés dans les analyses d’impact des changements climatiques ou d’urbanisation, en lien avec les fonctions de protection de sites bâtis (par exemple, rôle de zones tampon végétalisées).
- Arches peut stocker des observations répétées (campagnes de terrain, suivis botaniques, analyses de sol, imagerie) et ainsi soutenir un suivi de l’état des jardins et sols, à condition que les indicateurs (couverture végétale, biodiversité, humidité) soient définis par le projet.

Il est a noté que l’ensemble de ces possibilité de représentation n’es pas nativement intégré, mais que Arches, est adapté pour déployer de telles construction épistémologiques.

---

## 5. Synthèse des technologies et approches

- Arches-HER repose sur un SIG Web « open source » structuré par des normes patrimoniales (Core Data Standards, CIDOC CRM) et conçu pour l’intégration multi‑sources et le suivi de menaces.
- Le système se positionne comme un socle de données et de gestion (inventaire, monitoring, appui à la décision) plutôt qu’un moteur de simulation ; il s’interface avec des outils externes pour les scénarios climatiques, hydrologiques ou sismiques.
- Sa force réside dans la capacité à harmoniser et relier des informations hétérogènes (patrimoine bâti, paysages, menaces, mesures de gestion) pour soutenir la conservation, la planification et la résilience des sites historiques.

## Limites identifiées du projet (Arches-HER comme déclinaison d’Arches)

- Dépendance à des outils externes pour la simulation dynamique (RCP, inondations,
incendies, etc.) : Arches gère les résultats mais ne les génère pas.
- Besoin d’efforts importants de normalisation et de nettoyage des données historiques avant intégration, en particulier pour aligner sur les normes et vocabulaires contrôlés.
- Nécessité de personnalisation (schéma, indicateurs, interfaces) pour que le système réponde réellement aux besoins spécifiques d’un HER et de la gestion des risques, ce qui demande des ressources techniques et organisationnelles.

### Enrichissement des données descriptives

- Arches offre un cadre riche pour la description sémantique (acteurs, événements, valeurs, menaces), mais cette richesse n’est exploitée que si l’on investit dans la structuration fine des données (ontologies, vocabulaires contrôlés, liens vers sources).
- Pour un HER, un axe d’enrichissement clé est l’annotation systématique des ressources par leurs vulnérabilités, fonctions écologiques (espaces verts, sols) et mesures d’adaptation, afin de dépasser le simple inventaire descriptif.

### Déficits en simulation dynamique

- Le dispositif tel qu’il est conçu ne remplace pas une plateforme intégrée de simulation multi‑risques : les liens entre scénarios, trajectoires temporelles et décisions restent à paramétrer via des workflows et outils externes.
- L’un des risques est de rester sur une logique statique plutôt que d’intégrer des trajectoires et
scénarios dynamiques (scénarios RCP, évolution des usages du sol, cycles de perturbations).

---

# Proposition d’adaptation au projet ATLAS

L'intégration des projets ARCH (HArIS) et C2Impress (SoS4MHRIN) représente une opportunité majeure pour le projet ATLAS. Ce couplage permet de fusionner une base de données patrimoniale ultra-détaillée avec une intelligence multi-aléas dynamique et participative.

Voici une analyse stratégique des intérêts de ce couplage, des besoins de développement pour le simulateur d'incendie et de la voie vers une ontologie unifiée.

## Intérêts du couplage : Vers un Jumeau Numérique Dynamique

Le couplage entre HArIS et C2Impress permet de passer d'un inventaire statique du patrimoine à un système de gestion prédictive.

Entre autre, cela créerait une complémentarité Données/Flux : HArIS apporte la précision structurelle (matériaux des bâtiments, typologie des objets de jardin, géométrie 3D), tandis que C2Impress fournit les flux de données (humidité des sols, stress hydrique, données satellites Copernicus) et simulation en temps réel .

Aussi les analyse de vulnérabilité pourrait être effectuées en croisant la base CONSTRUCTION de HArIS avec le "Soil Vulnerability Index" de C2Impress, on peut prédire comment la sécheresse impacte physiquement les sites historiques et leurs fondations.

Enfin, on augmenterait significativement nos capacité de validation par les "Living Labs" : L'approche participative de C2Impress permet de valider les modèles de vulnérabilité de HArIS grâce aux signalements citoyens (crowdsourcing), enrichissant la base de données patrimoniale avec des observations de terrain actualisées.

## Développement d'une Ontologie Uniforme

Pour que ces deux systèmes communiquent, il est impératif de créer une couche sémantique commune, idéalement basée sur une extension du CIDOC CRM.
Ce qu'il faut développer :

1. Réconciliation des classes : Créer des correspondances (mappings) entre les classes HeritageAsset de C2Impress et les bases CONSTRUCTION/OBJECT de HArIS.
2. Modélisation du "Natural Heritage Buffer" : Développer une ontologie qui ne traite plus le jardin comme un simple décor, mais comme une entité active possédant des propriétés de résistance thermique et de perméabilité hydraulique.
3. Standardisation des indicateurs : Adopter l'approche de C2Impress pour normaliser les données hétérogènes de HArIS, permettant ainsi de comparer des risques de natures différentes sur une même échelle de décision.

## "Plugger" le simulateur d'incendie Soc-SIM-K

Le projet ATLAS identifie l'absence de simulation dynamique d'incendie comme une limite majeure d'ARCH. Pour intégrer le simulateur en développement voici les passerelles à construire : 

1. Flux de données nécessaires :
    
    Entrées (depuis C2Impress) : Récupérer en temps réel le Fire Weather Index (FWI), la charge de biomasse inflammable et les conditions de vent.
    
2. Contexte structurel (depuis HArIS) : 
    
    Extraire les propriétés combustibles des matériaux (bois, menuiseries) et la configuration spatiale des actifs pour définir les chemins de propagation.
    
3.  Développements requis pour le "Plug-in" :
    
    Interface API de propagation : Développer un connecteur capable d'injecter les vecteurs de propagation du feu de Soc-SIM-K dans les visionneuses 3D haute précision de HArIS.
    
4. Module de comportement humain : 
    
    Utiliser les Agent-Based Models (ABM) de C2Impress pour simuler l'évacuation des populations (touristes, PMR) à travers les axes de circulation documentés dans HArIS.
    
5. Rétroaction sur les dommages : 
    
    Créer un script qui met à jour automatiquement l'état de conservation dans HArIS après une simulation d'incendie, estimant les pertes matérielles et la dégradation des sols.
    
6. Estimation des conditions d’évacuation : 
    
    Classification détaillée des profils de victimes, expérimentation de scénarios d’intervention des services d’urgence et simulation des impacts psychologiques potentiels.
    

---

# Conclusion

En conclusion, l’adaptation du projet ATLAS par le couplage HArIS–C2Impress pourrait ouvrir la voie à un jumeau numérique dynamique du patrimoine, capable d’articuler connaissance fine des objets et intelligence multi‑aléas en temps quasi réel. Ce rapprochement transformerait un inventaire descriptif en un système de gestion prédictive, où la vulnérabilité structurelle, la dynamique des sols, le rôle actif des jardins et les comportements humains seraient intégrés dans une même chaîne décisionnelle.

La construction d’une ontologie unifiée, fondée sur une extension du CIDOC CRM, constituerait la clé d’architecture permettant de faire dialoguer bases patrimoniales, indicateurs environnementaux et simulateurs d’incendie, tout en rendant comparables des risques de nature différente sur une échelle commune. L’intégration de Soc‑SIM‑K comme module de simulation d’incendie, connecté aux modèles de propagation, aux données structurelles détaillées et aux modèles agent‑basés d’évacuation, comblerait l’un des principaux déficits identifiés dans ARCH en ajoutant une dimension dynamique et prospective.

Ainsi, ATLAS pourrait se positionner comme une plateforme intégrée de résilience patrimoniale, où les Living Labs joueraient un rôle de boucle de rétroaction continue, validant les modèles, corrigeant les données et enrichissant la compréhension des impacts psychologiques et sociaux des crises. Cette vision ferait du patrimoine non seulement un objet à protéger, mais un pivot potentiel pour concevoir, tester et ajuster des stratégies d’adaptation face aux risques climatiques et extrêmes, à la fois au niveau des sites et des territoires.