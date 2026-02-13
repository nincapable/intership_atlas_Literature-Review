# State of the Art for ATLAS Project

# ARCH Study

The ARCH project proposes an integrated technological framework to analysis, monitor, and improve the resilience of historical areas, articulating information systems, multi-hazard simulations, and decision support tools.

##1. General Framework and Objectives of ARCH

ARCH (Advancing Resilience of Historical Areas against Climate-related and other Hazards) is an H2020 project dedicated to the resilience of historical districts and sites against climatic hackards and other natural risks. It combines disaster risk management, climate change adaptation, and heritage management within an integrated risk management cycle applied to historic areas.

The integrated solutions include:

- A methodological framework for risk management (ARCH Disaster Risk Management Framework) specifically adapted to historical areas.
- A suite of digital tools: geo-referenced information systems (HARIS/THIS), decision support system (DSS), resilience measurements inventory (RMI/RPVT), and resilience maturity self-assessment tool (RAD).

---

##2. Information Systems and Data Management

## 2.1. HARIS – Historical Areas Information System

HARIS is a heritage-oriented geographic information system, based on a service-oriented **architecture** (SOA), which manages geo-referenced data on the historical and current state of heritage areas. It links 2D/3D geometry, materials, usages, and environmental context to feed vulnerability analyses, aging models, and damage scenarios.

- 2.1.1. Architecture and Database
- DBMS Relational (RDBMS):

Spatial and alphanumeric data are stored in a relational database (including geometry, attributes, metadata, time series), ensuring integrity, complex queries, and interoperability with GIS tools.

- SOA and Interoperability:

Web services exposes data as standard services (WMS/WFS, REST API), facilitating the use of components in other platforms (DSS, municipal portals, field applications).

- 2.1.2. Heritage Data Schema

Heritage assets are structured into broad logical bases, interconnected by unique identifiers and spatial relationships:

1. CONSTRUCTION Base
- Content: Historic buildings, engineering structures, walls, infrastructure, building ensembles, archaeological structures.
- Attributes:
- Geometry (2D polygons, 3D models, levels/facets);
- Materials (stone, brick, wood, metal, mortar) and mechanical properties;
- Functions and uses (residential, religious, administrative, cultural);
State of conservation, known pathologies (cracks, rising damp, surface alterations);
- Past interventions (retoration campaigns, reinforcements, changes of use).
2. OBJECT Base
- Content: Objects, singular elements, and components: architectural elements (cornices, columns, sculptures), historic urban furniture, in situ artworks, remarkable vegetal structures (isolated trees, historic hedges, alignments), garden elements (fountains, statues, basins, pergolas).
- Attributes:
Physical characteristics (dimensions, mass, materials, surface stratigraphy);
- Location metadata (coordinates, relation to a construction or garden, position in 3D space);
State and pathology data;
- Conservation history (dates, types, and actors of interventions).
3. MEASUREMENT Base
- Content: Time series and environmental indicators (climate, air quality, hydrology, vibrations, etc.).
- Sources: In situ sensors (temperature, humidity, vibrations, water levels), weather stations, satellite data, climate models.
- Attributes: Value, uncertainty, time step, provenance, and quality of the measurement.

This structuring allows associating each asset (CONSTRUCTION/OBJECT) with specific environmental conditions (MEASURE) for coupled analyses (aging, climatic risks).

- 2.1.3. Access and Analysis Tools

HARIS is operated through three main types of interfaces, integrated within the ARCH platform:

1. GIS Dashboards
- Interactive 2D/3D maps displaying assets, their vulnerability, associated hackers, and environmental measurements.
- Functions: Filtering by asset type, period, fragility level; overlay of climate indicators and scenarios; export of views and layers for reports.
2. Electronic Sheets
- Detailed sheets per asset (building, object, garden element) giving access to all attributes, metadata, intervention stories, and links to external documents (plans, reports, photos, laser scans).
- Functions: Controlled editing, tracking of modifications, traceability of sources.
3. High-Precision 3D Viewers
- Visualization of 3D models (photogramtry, laser-scan, drones), immersive navigation in historic sites, coupling with HARIS attributes.
- The integration of computer vision and Deep Learning methods allows automatic detection, on point clouds and orthophotos, of degradations (cracks, detachments, material losses) or morphological evolutions.

HARIS is thus at once an analysis tool (vulnerability, damage scenarios), a simulation tool (via links to the DSS), and a mediation/outreach tool for decision-makers and the public.

##2.2. THIS – Threats and Hazard Information System

THIS is the system "twin" of HARIS dedicated to the description and quantification of environmental threats and hazards, at different temporal and spatial scales. It provides geo-referenced indicators on climate and environmental threats, feeling risk analyses and simulations in the ARCH platform.

- 2.2.1. Multi-source Collection and Integration

THIS aggregates data from:

- Historical archives (chronicles of extreme events, floods, droughts, fire, earthquakes);
- Real-time data: Urban sensor networks (rain gauges, water level sensors, climate stations, air/quality stations), structural sensors, crowd-sensing networks (citizen reports via apps, geolocated photos);
- Climate projections: RCP scenarios, bioclimatic dataset, sectoral projections (extreme heat, precipitation, drought);
- Climate services driven from Copernicus services (notably CAMS/C3S) for projections under different scenarios.

Data are harmonized, geo-referenced, and stored in a structured database compatible with environmental information standards.

- 2.2.2. Threat Indicators

THIS produces a set of thematic indicators essential for natural sites and historical gardens:

1. Bioclimatic Indicators (BIO1–BIO19)
- Examples: Annual mean temperature, annual thermal amplitude, seasonality and concentration of precipitation, precipitation of west/driest months, temperatures of extreme months.
- Usage: Assessing survival conditions for plant species, identifying zones of thermal or water stress, and anticipating shifts in climatic niches.
2. Drought and Heat Indices
- Standardized Precipitation-Evapotranspiration Index (SPEI) to monitor meteorological and agricultural droughts;
Number of Consecutive Dry Days (CDD), heat wave (duration, intensity, frequency), number of "tropical" days;
- Human thermal stress indicators (perceived temperature, composite indices) for historical public spaces.
3. Fire Risk
- Combination: Drought (SPEI, CDD), extreme temperatures, relative humidity, wind (when available), density and type of fuel (vegetation, materials).
- Production of maps of ignition probabilities and potential propagation at the scale site.
4. Flood Risk
- Crossing of topographical data, land use, stormwater drainage networks, and flood history, with groove and water level measurements.
- Production of indicators of probable water depth, flow velocity, submersion duration, stagnation zones, specifically in historic urban manufactures.
5. Ad hoc Climate Services
- Use of Copernicus products (CAMS/C3S) to generate localized climate scenarios for different time horizons (e.g., heat waves in Valencia up to 2100), under several emission assumptions.
- Generation of input climate variable series for heritage and vegetation impact models.

THIS these functions as a central resting of present and future hackers, coupled with HARIS and the DSS.

---

##3. Simulations and Scenarios

The ARCH project connects on an integrated simulation system (DSS) allowing the construction and analysis of different types of scenarios, combining climate parameters, land use, and extreme events.

### 3.1. Long-term Climate Hazard Scenarios

These simulations rely on RCP emission trajectories (IPCC) and cover several reference time periods: historical, 2011–2040, 2041–2070, 2071–2100.

- 3.1.1. Emission Scenarios
- SPC 4.5:

Intermediate stability scenario, with mitigation measures limiting the rise in greenhouse gas concentrations.

- RCP 8.5:

Very pessimistic scenario, matching to a trend of high and extended emissions, often thing in ARCH to explore the resilience limit of historic sites.

- 3.1.2. Simulated Phenomena
1. Heat Waves
- Duration (included waves potentially reaching ~30 days or more depending on the site), intensity (division from normals, heatwave indices), and maximum temperature reached.
- Effects on materials, site visitation, and survival of plant species in historic gardens.
2. Drought
- Calculation of the maximum Number of Consecutive Dry Days (CDD) and rought indices (such as SPEI), with breakdown for soils, vegetation, and heritage agricultural activities.
3. Sea Level Rise
- For coastal pilot zones (e.g., Hamburg), coupling of sea level projections and surges with local morphology, to assess potential submersion of historic districts, saline intrusions, and infrastructure damage.

3.2. Land Use and Microclimate Scenarios

ARCH simulates the effect of different land use configurations on the urban micro-climate, notably on the formation of heat islands around heritage zones.

The main scenarios are:

1. Reference Scenario (Current)
- Based on current land use (build-up, roads, vegetation, water) from cartographic data and local observations.
2. "Grey" Scenario (Moderate Urbanization)
- Progressive urbanization of unprotected agricultural zones or summerlands, increase in mineral surfaces and build-up areas, limited reduction of vegetated surfaces.
- Objective: Quantify local temperature increase and reduction of thermal comfort in the vitality of heritage assets.
3. "Black" Scenario (Total Urbanization)
- Maximal urbanization including, in a theoretical scenario, initially protected areas replaced by build-up or impermeable surfaces.
- Usage: Expressing the maximum protective value of vegetation by comparison with this extreme, rather than describing a plausible future.
4. "Green" Scenario
- Transformation of abandoned, salted, or underutilized areas into vegetated surfaces (parks, gardens, agricultural zones) or green/blue grids.
- Objective: Estimated cooling gains, heat island reduction, improvement of water infiltration, and mitigation of impacts on historic fabric.

The models simulate surface and air temperature fields, sometimes coupled with urban airflow or radiation models, to quantify micro-climatic effects.

### 3.3. Sudden Disaster Scenarios

These scenarios explore the site's reaction to brutal events, with calculation of material and human damage.

- 3.3.1. Seismic Scenarios
1. Historical Events
- Replay of documented earthquakes (position, magnitude, depth, fault mechanism) to assess the response of historical structures to events that have already occupied.
2. User-Defined Events
- The user specifications various parameters (epicenter, dept, magnitude Mw, fault type, rupture direction, pulse duration) in the DSS interface.
- Acceleration fields and dynamic response are projected onto the historic fabric, allowing estimation of structural damage levels and potential loses (costs, victims, functional unavailability).
- 3.3.2. Pluvial Flood Scenarios
- Inputs: Intenserain events (observed or future episodes), urban runoff and drainage models, high resolution topography.
- Output:
- Maps of water depth and vegetation in historic streets;
- Accumulation zones, network overflow, interactions with buildings and infrastructures;
- Estimation of material damage (buildings, collections, roads) and consequences for people (exposure, accessibility, evacuation).

## 3.4. Fire Scenarios

ARCH does not implement detailed flame propagation simulation but frameworks the risk upstream and potential damage downstream.

1. Before the fire: Risk assessment
- THIS aggregates favorable conditions to ignition: extreme heat episodes, prolonged series of dry days, low fuel humidity, density of flameble vegetation, wind.
- Ignition probability and fire danger maps are generated for gardens, parks, and peri-urban areas close to build heritage.
2. After the fire: Damage estimate
- HARIS provides materials (wood, stone, metal, roofing, joyery) and the spatial configuration of objects and constructions.
- From this, probable loses in case of fire are estimated (elements likely to be destroyed or heavily degraded), without precise modelling the fire's path in the urban space.

---

##4. Natural Spaces, Gardens, and Soils as Heritage Assets

ARCH considerers natural spaces (gardens, parkes, associated agricultural lands, wetlands) as heritage assets in their own right, and not just as a backdrop around monuments.

### 4.1. Semantic and Physical Representation

1. Natural Objects in HARIS
- Each significant component of a garden (remarkable tree, historic hedge, bed, structured law) can be recorded as an "object" in the OBJECT base, with its physical properties (dimensions, estimated age, foliage type) and biological properties (species, sanitary state).
- Spatial and functional relations between these objects and the building environment (proximity to facades, shade, protection against wind) are made explicit in the data model.
2. Land Use
- Land use maps distinguished finely: forests, urban gardens, arable land, meadows, wetlands, impermeable surfaces, water surfaces.
- This distinction serves to simulate heat absorption (albedo, thermal capacity, evapotranspiration) and water management (infiltration, runoff, storage) around historic sites.

4.2. "Shield" Role of Gardens and Natural Soils

ARCH is among the projects that explicitly quantify the benefits of gardens and verified spaces for the resilience of historic fabric.

1. Thermal Regulation
- Modeling of the cooling effect via evapotranspiration and shade of gardens, reducing heat island intensity in the vitality of monuments.
- Assessment of gains in thermal comfort, reduction of thermal fatigue of materials, and decrease in extreme expansion/contraction cycles.
2. Stormwater Management
- Natural soils are represented as absorption/infiltration zones, with permeability, storage, and surface roughness parameters.
- ARCH simulates how a garden or park slows flow, reduce water heights in adjacent streets, protect historic building foundations, and decrease loads on drainage networks.

### 4.3. Monitoring the Health of the Natural Environment

THIS includes indicators specifically designated to the ecological health of natural spaces.

1. Vegetation Indexes
- Use of satellite data (e.g., NDVI, EVI) and possibly drone data to monitor the vigor and density of vegetation in historic gardens and parks.
- Detection of zones of dieback, stress, or change in vegetation cover likely to increase risks.
2. Water Needs and Water Stress
- Calculation of the balance between potential evapotranspiration and precipitation, supplemented by information on irrigation practices where they exist.
- Identification of periods where a historic garden enters a water stress zone, with alerts on ancient species especially vulnerable or difficult to replace.
3. Agro-climatic Indicators
- For heritage agricultural sites (historic wineyards, traditional crops), monitoring of growth period, late frost risks, early heat, or heat waves during sensory phases (flowing, maturity).
- These indicators serve to preserve both production and the associated intangible heritage (know-how, cultural landscapes).

4.4. Vulnerability and Soil Dynamics

ARCH is not limited to visible surface elements but takes into account the structure and dynamics of underlying soils.

1. Geotechnical Micro-zoning
- Study of the composition (clays, silts, sands, rock), heterogeneity, and water conditions of soils in gardens and build-up areas.
- Identification of sectors likely to experience landslides, different settlement, or local amplification of seismic movements.
2. Silk–Structure Interaction
- Analysis of the effects of soil drying (linked to recurring drives) on swelling clays, which can cause seasonal shrinkage and swelling.
- Correlating these phenomena with the appearance of cracks in walls, foundation deformation, and destabilization of fences and historic garden walls.

---

##5. Synthesis of Technologies and Approaches

The table below summarizes the main technological components of the ARCH project and their role.

- Yes. Component: Technology Type: Main Role: Key Data:
- ...-----------------------------------------
- HARIS - Heritage Geographic Information System (SOA, RDBMS, GIS, 3D) - Storage and access to data on assets and their state, support for vulnerability analyses and damage scenarios CONSTRUCTION and OBJECT assets, environmental measurement, 2D/3D geometries, historical intervention
THEIS: Threats and Hazards Information System: Provision of climatic, hydrological, and environmental indicators, present and future: Bioclimatic indicators, drought indices, fire and flood risks, climate/Copernicus projections:
DSS ARCH
RMI / RPVT
RAD

ARCH units these different modules (HARIS, THIS, DSS, and decision support tools) to constitute an **integrated and complete digital ecosystem**, allowing a fine and multidimensional description of historical sites, a precise characterization of present and future climatic and natural hazards, the execution of varied prospective scenario simulations, and the development of scientifically robust and operational adaptation trajectories.

Funded by the Horizon 2020 program to the tune of **5.98 million euros** over 48 months (2019-2023), the project deployments its pilot solutions on 8 automatic European historic sites – Istanbul (main pilot), Rome, Valencia, Hamburg, etc. – and make all of its **software components available as open source** (code, modular databases, APIs, technical documentation) under free licences, which facilitating use and extension by other institutions or communities.

The **conceptual and operational similarities** with the **ATLAS** project (presumed to target heritage or urban resilience in a comparable context) are structuring:

- **Common Concerns**: Vulnerability of historic manufacturers to climate change (heat islands, droughts, floods), protective role of heritage green spaces, need for decision support tools integrating building environment, vegetation, and hazards.
- **Transferable Technological Solutions**:
- Interoperable SOA architecture, easily integrated into existing systems like that of ATLAS.
- Rich and normalized HARIS data models (CONSTRUCTION/OBJECT/MEASURE), directly useful to document similar sites.
- THIS → DSS pipeline for multi-scenario simulation (RCP 4.5/8.5, "Grey/Black/Green" urbanization, earthquakes/floods), applicable to ATLAS issues.
- 3D visualization tools and GIS dashboards, already validated with 8 UNESCO site managers.

---

## Identified Limits of the ARCH Project

Despite its significant advances, the ARCH project presents notable gaps that limit its understanding for integral risk management on heritage sites. These shortcomings concern both the richness of descriptive data and dynamic simulation capabilities.

##Enrichment of Descriptive Data

The fine representation of sites via HARIS (CONSTRUCTION, OBJECT, MEASURE tables) perfectable on several critical dimensions:

- **Detailed Technical Characteristics**: Enrichment of attributes for buildings, artifacts, traffic axes (dynamic loads capacities, alternative configurations).
- **Socio-demographic Data**: Absence of fine classification of populations (permanent residents, tourists, seasonality, specific vulnerabilities – PRM, children, seniors).
- **Operational Rescue Capacities**: No modelling of intervention infrastructures (rescue stations, water points, vehicle access, theoretical response times).
- **Past Disaster Assessment**: Limited data on victims.
- **Heritage Ecology**: Protection of historic plant species underdeveloped (lists of protected species, regulatory status, safeguard strategies against climate stress).

## Deficits in Dynamic Simulation

ARCH excels in climatic, seismic, and hydrological scenarios but present two major absences:

1. **Fire Propagation Simulation**: Althrough THIS provides excellent prior indicators (SPEI, CDD, vegetation fuel load, ignition conditions) and HARIS details flameble materials (wood, dry vegetation), the project stops at the "before" and "after" phases, without modelling the dynamics of flame propagation (preferential path, advance speed, hot spots, build-vegetation interaction).

The **Soc-SIM-K** team fills precise this void with its 3D fire models adapted to dense heritage sites, directly exploitable on existing HARIS bases.

2. **Human Behaviors Under Crisis**: DSS simulations concentrate on material damage, ignoring human flows (panic, congestion, evacuations, refuge areas). However, **Soc-SIM-K** developments realistic behavioral agents (pedestrians, rescue vehicles, disoriented tourists), perfectly compatible with HARIS circulation geometries and capabilities.

---

# C2Impress Study

##1. General Framework and Objectives

C2Impress is a Horizon Europe project (2023–2026) coordinated by the Joint Research Centre (JRC) and involving more than 18 European partners. Its objective is to develop an integrated co-creation framework to improve understanding, preparedness, and response to multiple natural and socio-environmental risks, notably floods, droughts, fire, and coastal hazards.

The vision of C2Impress links on:

- The association between science, local authorities, and citizens;
- The use of multi-hazard simulations and social and cultural impact indicators;
- The co-construction of decision support tools to strengthen local resilience.

The *Living Labs* used to test replicable methods for other heritage contexts, including historical sites and their diverse environments.

---

##2. Information Systems and Data Management

## 2.1. Information System

- 2.1.1. Architecture and Database

The central system of C2Impress connects on a distributed and interoperable architecture, compliant with FAIR principals (Findable, Accessible, Interoperable, Reusable). It integrates spatio-temporal data (GIS), field observations, and modelling results.

A geospatial database (PostSIG) helps the crossing of physical, human, and heritage indicators at different scales (building, district, watershed).

- 2.1.2. Heritage Data Schema

Through the project targets urban resilience primarily, C2Impress introduces the notion of cultural assets as sensitive elements of the territory, integrated into vulnerability layers. "Cultural assets" are classified according to their value, usage, and exhibition to hackers.

In a transposition perspective, a heritage data scheme applied to historical gardens could adopt this model: vegetable entities, hydraulic works, topography, sols, symbolic values.

- 2.1.3. Access and Analysis Tools

A decisional dashboard allows local actors to visualize the spread of a hazard or the evolution of resilience indicators. Multi-criteria analysis modules support planning choices. These tools are designed for appropriation by non-expert audiences, a key point for mediation in heritage sites.


##2.2. Threats and Hazard Information System

In C2Impress, the functional equivalent of ARCH's THIS (Threats and Hazard Information System) is the SoS4MHRIN platform (System-of-Systems for Multi-Hazard Risk Intelligence Network). This infrastructure centralizes and analyzes in real-time data on multiple hazards (floods, fires, heat waves, compound drives), relying on ESDI (Earth System Dynamic Intelligence) for fine and dynamic multi-hazard risk predictions.

- 2.2.1. Multi-source Collection and Integration

SoS4MHRIN orchestrates a continuous and heterogenous collection of data coming from multiple scales and vectors:

- Satellite Sources: Copernicus data, MODIS for fires and surface temperatures, supplemented by weather forecasts.
- In situ Sensors and IoT: Networks of ground stations, deployed in Living Labs (e.g., Thessaloniki, Malta), with increased density near critical heritage sites.
- Urban and Open Data: OpenStreetMap, local databases of critical infrastructures, historical hydro-meteo archives, enriched by citizen crowdsourcing via mobile apps (reports of local anomalies).
- Socio-economic Data: Demographic layers (population density, social vulnerability), integrated to contextualize human exhibits.

Multi-source integration links on dynamic flows that fuse these data in near real-time. Data fusion approaches (Bayesian statistics and machine learning) generic composite risk maps updated every 15-60 minutes depending on the hazard. For heritage gardens, this capacity allows following the fine evolution of water and thermal conditions affecting soils and vegetation, by crossing for example satellite rainfall with local root mould measurements.

- 2.2.2. Threat Indicators

SoS4MHRIN produced a set of normalized threats indicators (0-1), covering both extreme climatic hackers and their ecological impacts, adapted to a multi-scale assessment:

- Primary Climate Variables:
- Extreme temperatures and Heat Stress Index (perceived temperature/humidity combination).
- Intense rainfall (intensity, duration, frequency for rain floods).
- Strong windows.
- Drought indices (SPI, SPEI over 1-12 months).
- Ecological and Environmental Parameters:
- Soil health (volumetric mould, compaction, potential erosion).
- Plant water stress.
- Flammable biomass load and slope stability.

These indicators are composite and probabilistic, integrating contextualized alert threesholds (e.g., high fire risk if FWI > 30 AND self humidity < 20%). They are particularly transposable to historical gardens: a garden can be monitored via a personalized dashboard showing progressive degradation or southden risks. In a heritage context, these metrics notabably allow quantifying how a garden acts as a buffer (run-off reduction of 40% via self infiltration), while identifying its own vulnerabilities (swelling clay soils under cycling drrought).

This SoS4MHRIN approach thus offers proactive vigilance, essential for preserving historic sites against compound climatic hackers.

---

##3. Simulations and Scenarios

C2Impress integrated advanced simulations within its **SoS4MHRIN** platform, primarily via **Earth System Dynamic Intelligence (ESDI)** and **operational dynamic models**. These tools allow predicting with high spatial-temporal resolution (from event to climatic scale) the risks of single or multiple hazards under varied climatic scenarios, moving from a "hazard-centric" approach to an evaluation centered on places and populations. The simulations are empirically validated in four pilot sites (Egaleo in Greece, Ordu in Turkey, and two others in Southern Europe), covering vulnerable urban and coastal contexts.

### 3.1. Simulated Phenomena

C2Impress simulations target **comound meteorological extremes**, as well as non-standard events with high impact. They model the **main hydrometeorological hazards**: river and rain waters, forest fire, heat waves, landslides induced by intense rays, and prolonged droughts.

The innovation lies in capturing ** interactions between hazards** (cascading effects or combined stresses), like a drought amplifying fire risks followed by post-fire floods. **System-of-systems simulation models** and **agent-based models (ABM)** multidimensional assessments impacts (exposure, physical/social vulnerability, adaptive resilience), with reduced uncertainty thanks to fine predictions.

For heritage spaces and historic gardens, these simulations are highly adaptable: they allow studying **soil water dynamics** (infiltration/runoff under floods), **vegetal stress** (biomass loss under heat/drought), or **impacts on biodiversity** (species sensitive to extreme compounds), by tagging gardens as "natural buffers" in the models.

- 3.1.1. Emission Scenarios

C2Impress connects explicitly on **RCP 4.5** and **RCP 8.5** climatic scenarios for its high-resolution local projections. These scenarios calibrated simulations at medium (2030-2050) and long-term (2070-2100), testing resilience under progressive or extreme conditions.


3.2. Land Use and Microclimate Scenarios

**Land Use and Land Cover (LULC)** projections drive from series like CORINE Land Cover, simulated via ABM to anticipate urbanization, loss of vegetation cover, and their effects on **micro-climate.** In historic gardens in dense environments, these scenarios quantify how heritage vegetation mitigates heat or regulatory humidity, while assessing potential degradation under urbanization.

### 3.3. Sudden Disaster Scenarios

- 3.3.1. Seismic Scenarios

Simulations include earthquakes, via impact models on critical infrastructures and associated landslides. Transposable to historic sites, they assess the response of heritage structures (retaining walls, garden pools) to self liquefaction or tremors enhanced by water saturation.

- 3.3.2. Pluvial Flood Scenarios

Modeling of rain and river floods, with real-time alerts and extent predictions. At high spatial resolution, these tools analyze watershed management in parks/gardens, simulating runoff, historic drain overload, and flowerbed erosion.

- 3.3.3. Fire Scenarios

Forestfires are simulated by integrating drought, windows, and biomass, with early alerts and dynamic propagation (e.g., via FWI-like indices). For heritage gardens, these models guide planning planning (non-flammable species, green barriers), assessing how dry soils under RCP 8.5 increase vulnerability to ignition.


These simulations, anchored in co-creation with local actors, provide dashboards for emergency plans adapted to historic sites.

---

##4. Natural Spaces, Gardens, and Soils as Heritage Assets

Yes, several elements can enrich this section by exploiting more explicitly the conceptual framework of C2Impress, which treaties natural spaces as **"Natural Heritage Buffers"** or **"Green Resilience Layers"** in its ontologies and multi-hazard models. These assets are integrated not as liabilities, but as **dynamic components** influencing the exhibition and overall vulnerability of sites. Here is a detailed version, with factual additions on modelling, pilot use boxes, and direct links to your gardens-heritage theme.

### 4.1. Semantic and Physical Representation

C2Impress uses a **unified semantic onology** to model territorial entities, naturally extending to **historic landscape elements** like gardens, beds, tree alignments, or heritage hydraulic networks. Ontological classes include "HeritageAsset" (build assets), "NaturalBuffer" (vegetation/soils), and "DynamicLayer" (temporal evolution), with properties like soil texture, vegetation cover (NDVI percentage), or water permeability.

This physical representation links on LiDAR and altimetric data for the fine topography of gardens (micro-morphological reliefs, underground drains), coupled with knowledge graphs linking a heritage tree to its hydric role (absorbent roots) or seismic role (soil stability).

4.2. Role of Gardens and Natural Soils

In C2Impress, green spaces and soils are positioned as **active territorial resilience amplifiers**, beyond a simple protective layer: they modulate energy/water flows and absorb multi-hazard shocks. Pilot site simulations quantify concrete benefits: 30-50% reduction in rain runoff via soil-garden infiltration, 3-6°C holding of heat islands by evapotranspiration, and maintenance of 20-40% biodiversity refuge under combined stress.

In heritage sites, this ecological function is super imposed on a **strong cultural and identity value**, a dimension that C2Impress beginnings to integrate via "Cultural Resilience Score" indicators.

### 4.3. Monitoring the Health of the Natural Environment

C2Impress, via SoS4MHRIN, combinations remove sense and IoT sensors (root mould, soil/canopy temperature, water stress sensors via stomatal conductance). In Living Labs, proactive alerts are generated (e.g.: early detection of leaf yellowing under RCP 4.5 Drought), with real-time dashboards accessible to heritage managers.

Applied to historical gardens, this allows **holistic monitoring**: vegetal vitality, soil mould (critical threesholds for swelling clays), surface temperature, and microbiological health (indicators via permeability). Feedback loops (citizens reporting anomalies via app) reinforce precision, ideal for preventive management of sites.

4.4. Vulnerability and Soil Dynamics

The multi-source analysis of C2Impress models **sil vulnerability** as a dynamic process, exposed to floods (erosion/overload), water stress (clay cracking), and interactions (earthquake + saturation leading to liquefaction). Indicators like the "Soil Vulnerability Index" integrated compaction, porosity, organic load, and slope, predicting failures.

These dynamics translate into **heritage resilience levers**: a stable garden self under hedges protect historic foundations and vegetation; scenarios test interventions.

---

##5. Synthesis of Technologies and Approaches

C2Impress deploys a coherent technological ecosystem, centered on the **SoS4MHRIN** platform (System-of-Systems for Multi-Hazard Risk Intelligence Network), supported by **ESDI (Earth System Dynamic Intelligence)** and **IPAI (Information Physical Artificial Intelligence)**. This integrated architecture dynamic simulations, a unified semantic onology, and participatory tools for proactive multi-hazard risk management, validated in four pilot sites (Egaleo-Greene, Ordu-Turkey, and two others in Southern Europe).

##Main Technologies

- **Multi-Risk Intelligence Platform**: SoS4MHRIN centralizes satellite data (Copernicus/Sentinel), in situ IoT, and citizen crowdsourcing, with real-time fusion for high-resolution risk maps.
- **Modeling and Simulations**: Agent-Based Models (ABM) for LULC scenarios and micro-climates; physical models for compound hares (floods + fires) under RCP4.5/8.5.
- **Ontology and Data**: RDF/OWL schema modelling cultural assets and "Natural Buffers", stored in interoperable geospatial databases (FAIR).
- **Decision Tools**: Interactive dashboards, multi-criteria microservices, and probabilistic alerts.
- **Citizen Engagement**: Mobile applications and co-creation via Living Labs for integrating local perceptions.

---

## Boundaries of C2Impress

Identified Strengths

- **Holistic "Place and People-centered" Approach**: Shift from hazard-centered to multidimensional assessment (exposure, socio-cultural vulnerability, adaptive resilience), reducing predictive uncertainty.
- **Interoperability and Scalability**: Dynamic multi-source flows and fine simulations, transposable to heritage gardens as ecological buffers.
- **Inclusive Co-creation**: Science-authority-citizen involvement for accessible tools, fostering local appropriation in historical sites and decision support.

## Identified Limits of the Project

- **Detailed Technical Characteristics**: Inadequate enrichment of attributes for buildings, artifacts, traffic axes (dynamic loads capacities, alternative configurations); building and natural heritage assets under-granularized (limited historical vegetation/sil inventories, absence of palynology or landscape archaeology for gardens).
- **Socio-demographic Data**: Absence of fine classification of populations (permanent residents, tourists, seasonality, specific vulnerabilities – PRM, children, seniors).
- **Operational Rescue Capacities**: No modelling of intervention infrastructures (rescue stations, water points, vehicle access, theoretical response times).
- **Past Disaster Assessment**: Limited data on victims.
- **Heritage Ecology**: Protection of historic plant species underdeveloped (lists of protected species, regulatory status, safeguard strategies against climate stress).
- **Human Behaviors Under Crisis**: Althrough human behavior is taken into account, population flows are approached with a liquid approach, without consideration for biases, information levels, and the impact of rescue efforts.

---
