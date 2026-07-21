# Art Status for ATLAS Project

# Introduction

The present state of art proposes to prospectively examine the possible adaptation of the ATLAS project through the coupling of the HARIS (arch) and C2Impress (SoS4MHRIN) devices. In this perspective, it would be a move from a simple enriched heritage inventory to a digital environment that integrates both a fine asset database and multi-hazard, participatory and scalable intelligence. The analysis will explore the potential of this linkage for the establishment of a dynamic digital heritage twin, capable of supporting predictive approaches to vulnerability and crisis management.

At first, the theoretical interests of such approximation would be discussed, in particular in terms of complementarity between detailed structural data and environmental or social flows. Secondly, the development needs for the integration of a fire simulator (Soc-SIM-K) and the modelling of evacuation behaviour would be identified. Finally, particular attention would be paid to the need to build a unified ontology, based on an extension of CIDOC CRM, allowing semantic interoperability between the two systems and the standardization of risk indicators at the level of the ATLAS project.

# ARCH study

The ARCH project offers an integrated technological framework to analyse, monitor and improve the resilience of historical areas, by articulating information systems, multi-hazard simulations and decision support tools.

##1. General framework and objectives

ARCH (Advancing Resilience of Historic Areas against Climate-related and other Hazards) is a H2020 project dedicated to the resilience of neighbourhoods and historic sites to climate hazards and other natural hazards. It combines disaster risk management, climate change adaptation and heritage management within an integrated risk management cycle for historic areas.

The solutions developed include:

- a risk management methodological framework (ARCH Disaster Risk Management Framework) specifically adapted to historical areas
- a suite of digital tools: georeferenced information systems (HARIS/THIS), decision support system (DSS), resilience measurement inventory (RMI/RPVT) and self-assessment of resilience maturity (RAD).

---

##2. Information systems and data management

## 2.1. HARIS – Historical Areas Information System

HARIS is a heritage-oriented geographic information system based on a **Service-oriented** architecture (SOA), which manages georeferenced data on the historical and current state of heritage areas. It links 2D/3D geometry, materials, uses and environmental context to feed vulnerability analyses, aging models and damage scenarios.

- 2.1.1. Architecture and database
- Relationshipal GBS (RDBMS):

Spatial and alphanumeric data are stored in a relational database (including geometry, attributes, metadata, time series), ensuring integrity, complex queries and interoperability with GIS tools.

- SOA and interoperability:

Web services expose data in the form of standard services (WMS/WFS, REST API), facilitating the reuse of components in other platforms (DSS, municipal portals, field applications).

- 2.1.2. Heritage Data Diagram

Heritage assets are structured into broad logical bases, interconnected by unique identifiers and spatial relationships:

1. BASIS CONSTRUCTION
- Contents: historical buildings, works of art, walls, infrastructure, built ensembles, archaeological structures.
- Attributes:
- geometry (2D polygons, 3D models, levels/facets);
- materials (stone, brick, wood, metal, mortar) and mechanical properties;
- functions and uses (residential, cultural, administrative, cultural);
- conservation status, known pathologies (cracks, hair lifts, surface alterations);
- past interventions (restaurant campaigns, reinforcements, changes of use).
2. OBJECT Base
- Content: objects, singular elements and components: elements of architecture (corns, columns, sculptures), historic urban furniture, works of art in situ, remarkable plant structures (insulated trees, historic hedges, alignments), elements of gardens (fontaines, statues, basins, pergolas).
- Attributes:
- physical characteristics (dimensions, mass, materials, surface stratigraphy);
- location metadata (coordinates, relation to a building or garden, position in 3D space);
- state data and pathologies;
- conservation history (dates, types and actors of interventions).
3. MEASURE Base
- Content: time series and environmental indicators (climate, air quality, hydrology, vibration, etc.).
- Sources: in situ sensors (temperature, humidity, vibration, water levels), meteorological stations, satellite data, climate models.
Attributes: value, uncertainty, no time, source and quality of measurement.

This structure enables each asset (CONSTRUCTION/OBJECT) to be associated with specific environmental conditions (MEASURE) for coupled analyses (ageing, climate risks).

- 2.1.3. Access and analysis tools

HARIS is operated through three main interface types, integrated into the ARCH platform:

1. GIS dashboards
- 2D/3D interactive maps showing assets, their vulnerability, associated hazards and environmental measures.
- Functions: filtering by type of asset, period, level of fragility; superposition of climate indicators and scenarios; export of views and layers for reports.
2. Electronic Sheets
- Detailed sheets per asset (building, object, garden element) giving access to all attributes, metadata, intervention history and links to external documents (plans, reports, photos, laser scans).
- Functions: controlled editing, modification tracking, source traceability.
3. High precision 3D viewers
- Visualization of 3D models (photogrammetry, laser-scan, drones), immersive navigation in historical sites, coupling with the attributes of HARIS.
- The integration of computer vision methods and Deep Learning allows automatic detection of degradations (cracks, detachments, loss of matter) or morphological changes on point and orthophoto clouds.

HARIS is thus both an analysis tool (vulnerability, damage scenarios), a simulation tool (via DSS links) and a mediation/vulgarization tool for decision makers and the public.

##2.2. THIS – Threats and Hazard Information System

THIS is the twin system of HARIS dedicated to the description and quantification of environmental threats and hazards, at different temporal and spatial scales. It provides georeferenced indicators on climate and environmental threats, feeding risk analyses and simulations into the ARCH platform.

- 2.2.1. Multi-source collection and integration

THIS aggregates data from:

- historical archives (chronics of extreme events, floods, droughts, fires, earthquakes);
- real-time data: urban sensor networks (rain meters, water level sensors, climate stations, air/quality stations), structural sensors, crowd-sensing networks (citizen signals via applications, geolocation photos)
- climate projections: SPC scenarios, bioclimatic data sets, sectoral projections (extreme heat, precipitation, drought)
- climate services derived from Copernicus services (including CAMS/C3S) for projections under different scenarios.

The data are harmonised, georeferenced and stored in a structured database compatible with environmental information standards.

- 2.2.2. Threat indicators

THIS produces a set of key thematic indicators for natural sites and historic gardens:

1. Bioclimatic indicators (BIO1–BIO19)
- Examples: annual average temperature, annual thermal amplitude, seasonality and precipitation concentration, wettest/dryest month precipitation, extreme month temperatures.
- Use: assess the survival conditions of plant species, identify areas of thermal or water stress and anticipate changes in climatic niches.
2. Drought and heat indices
- Standardized Precipitation-Evapotranspiration Index (SPEI) for monitoring weather and agricultural droughts;
- number of consecutive dry days (CDD), heat wave (duration, intensity, frequency), number of days (tropical);
- indicators of human thermal stress (feeling temperature, composite indices) for historical public spaces.
3. Fire risk
- Combination: drought (SPEI, CSD), extreme temperatures, relative humidity, wind (when available), density and type of fuel (vegetation, materials).
- Production of maps of potential site-wide ignition and propagation probabilities.
4. Flood risk
- Crossing of topographic data, land use, storm and historical flood drainage systems, with rain and water level measurements.
- Production of indicators of probable water depth, flow rate, duration of submersion, areas of stagnation, specifically in historical urban tissues.
5. Ad hoc climate services
- Use of Copernicus products (CAMS/C3S) to generate localized climate scenarios for different time horizons (e.g. heat waves in Valencia until 2100), under several emission assumptions.
- Generation of series of incoming climate variables for heritage and vegetation impact models.

THIS therefore functions as a central repository of present and future hazards, coupled with HARIS and DSS.

---

##3. Simulations and scenarios

The ARCH project relies on an integrated simulation system (DSS) to construct and analyse different types of scenarios, combining climate parameters, land use and extreme events.

### 3.1. Long-term climate scenarios

These simulations are based on the RCP emission trajectories (IPCC) and cover several reference time periods: historical, 2011–2040, 2041–2070, 2071–2100.

- 3.1.1. Emission scenarios
- RCP 4.5:

Intermediate stabilization scenario, with mitigation measures limiting the increase in greenhouse gas concentrations.

- RCP 8.5:

Very pessimistic scenario, reflecting a high and prolonged emission trend, often chosen in ARCH to explore the resilience limit of historical sites.

- 3.1.2. Simulated phenomena
1. Heat waves
- Duration (including waves of up to ~30 days or more depending on the site), intensity (range to normal, heat index) and maximum temperature reached.
- Effects on materials, site use and survival of plant species in historic gardens.
2. Drought
- Calculation of the maximum number of consecutive dry days (CDD) and drought indices (such as SPEI), with declination for soil, vegetation and heritage agricultural activities.
3. Sea level rise
- For pilot coastal areas (e.g. Hamburg), sea level projections and surcotes coupled with local morphology, to assess the potential submersion of historic neighbourhoods, salty intrusions and damage to infrastructure.

3.2. Land use scenarios and microclimate

ARCH simulates the effect of different patterns of land use on urban microclimate, including the formation of heat islands around heritage areas.

The main scenarios are:

1. Reference scenario (Current)
- Based on current land use (building, road, vegetation, water) based on map data and local observations.
2. "Grey" scenario (moderate urbanization)
- Gradual urbanisation of unprotected agricultural areas or wasteland, increased mineral surfaces and building, limited reduction of vegetated areas.
- Objective: to quantify the increase in local temperature and the reduction of thermal comfort in the vicinity of heritage properties.
3. Black scenario (total urbanization)
- Maximum urbanisation including, in a theoretical scenario, areas initially protected, replaced by buildings or impermeable surfaces.
- Use: express the maximum protective value of vegetation in comparison with this extreme, more than describe a plausible future.
4. Green scenario (restoration/re-naturalization)
- Transformation of abandoned, waterproofed or underused areas into vegetated areas (parks, gardens, agricultural areas) or green/blue frames.
- Objective: to estimate the gains in cooling, the reduction of heat islands, the improvement of water infiltration and the mitigation of impacts on the historic building.

Models simulate surface and air temperature fields, sometimes coupled with urban air flow or radiation models, to quantify microclimatic effects.

### 3.3. Scenarios of sudden disasters

These scenarios explore the site's response to brutal events, with calculations of material and human damage.

- 3.3.1. Seismic scenarios
1. Historical events
- A series of documented earthquakes (position, magnitude, depth, fault mechanism) to assess the response of historical structures to events that have occurred.
2. User-defined events
- User specifies various parameters (epicentre, depth, magnitude Mw, type of fault, direction of rupture, pulse duration) in the DSS interface.
- Acceleration and dynamic response fields are projected on the historical structure, allowing an estimate of the levels of structural damage and potential losses (costs, victims, functional unavailability).
- 3.3.2. Rain flood scenarios
- Inputs: intense rain events (observed or future episodes), urban runoff and drainage models, high resolution topography.
- Exits:
- water depth and speed maps in historic streets;
- areas of accumulation, network overflow, interaction with buildings and infrastructure;
- estimation of material damage (buildings, collections, roads) and consequences for people (exposure, accessibility, evacuation).

## 3.4. Fire scenarios

ARCH does not implement the detailed flame propagation simulation but frames the upstream risk and potential downstream damage.

1. Pre-fire risk assessment
- THIS improves the conditions for ignition: extreme heat episodes, prolonged dry-day series, low fuel humidity, density of flammable vegetation, wind.
- Maps of probability of ignition and danger of fire are generated for gardens, parks and peri-urban areas close to the built heritage.
2. Post-fire estimate of damage
- HARIS provides the properties of materials (wood, stone, metal, blankets, carpentry) and spatial configuration of objects and constructions.
- Based on this, it is estimated the probable losses in the event of fire (elements likely to be destroyed or severely degraded), without accurately modeling the path of fire in urban space.

---

##4. Natural areas, gardens and soils as heritage assets

ARCH considers natural areas (gardens, parks, associated agricultural lands, wetlands) to be heritage assets in their own right, not just a decoration around monuments.

### 4.1. Semantic and physical representation

1. Natural objects in HARIS
- Each significant component of a garden (remarkable tree, historical hedge, massive, structured lawn) can be recorded as an "object" in the OBJECT base, with its physical properties (dimensions, estimated age, type of foliage) and biological (species, health status).
- The spatial and functional relationships between these objects and the building (proximity of facades, shading, protection against wind) are explained in the data model.
2. Land use
- Land use maps make fine distinctions: forests, urban gardens, arable land, meadows, wetlands, impermeabilised surfaces, water surfaces.
- This distinction is used to simulate heat absorption (albedo, thermal capacity, evapotranspiration) and water management (infiltration, runoff, storage) around historical sites.

4.2. The role of "shield" of natural gardens and soils

ARCH is one of the projects that explicitly quantify the benefits of gardens and vegetated spaces for the resilience of historic buildings.

1. Thermal regulation
- Modelling of cooling effect by evapotranspiration and shading of gardens, reducing the intensity of heat islands in the vicinity of monuments.
- Evaluation of thermal comfort gains, reduction of thermal fatigue of materials and reduction of extreme cycles of expansion/contraction.
2. Rainwater management
- Natural soils are represented as zones of absorption/infiltration, with parameters of permeability, storage and surface roughness.
- ARCH simulates how a garden or park slows down flow, reduces water levels in adjacent streets, protects the foundations of historic buildings and reduces the burden on evacuation networks.

### 4.3. Monitoring the "health" of the natural environment

THIS includes indicators specifically dedicated to the ecological health of natural areas

1. Vegetation indices
- Use of satellite data (e.g. NDVI, EVI) and possibly drone data to monitor vegetation strength and density in historic gardens and parks.
- Detection of areas of decline, stress or change in vegetation cover that may increase risks (fire, erosion, landslides).
2. Water needs and water stress
- Calculation of the balance between potential evapotranspiration and precipitation, supplemented by information on irrigation practices when they exist.
- Identification of periods when a historic garden enters a zone of water stress, with alert about ancient species particularly vulnerable or difficult to replace.
3. Agro-climatic indicators
- For heritage agricultural sites (historical vineyards, traditional crops), followed by periods of growth, risks of late freezing, early heat or heat waves during sensitive phases (flowering, maturity).
- These indicators are used to preserve both production and associated intangible heritage (know-how, cultural landscapes).

4.4. Soil vulnerability and dynamics

ARCH is not limited to surface visible elements, but takes into account the structure and dynamics of the underlying soils.

1. Geotechnical micro-zoning
- Study of the composition (clays, silts, sands, rocks), heterogeneity and water conditions of gardens and built-up areas.
- Identification of areas likely to experience landslides, differential settlements or local amplification of seismic movements.
2. Soil-structure interaction
- Analysis of the effects of soil drying (related to recurrent droughts) on inflating clays, which may cause seasonal withdrawals and swelling.
- Linking these phenomena with the appearance of cracks in walls, deformation of foundations, destabilization of fences and walls of historic gardens.

---

##5. Synthesis of technologies and approaches

The table below summarizes the main technological components of the ARCH project and their role.

- Yes. Component
- ...-----------------------------------------
HARIS--Heritage Geographic Information System (SOA, RDBMS, GIS, 3D)--Storage and access to asset and condition data, support to vulnerability analyses and damage scenarios--Active CONSTRUCTION and OBJECT, environmental measures--MEASURE, 2D/3D geometries, historical interventions--
THES: Threat and hazard information system: provision of current and future climate, hydrological and environmental indicators: bioclimatic indicators, drought indices, fire and flood risks, climate/copernicus projections
DSS ARCH
RMI / RPVT
RAD Governance indicators, preparedness, response, recovery, asset-climate integration

ARCH brings together these modules (HARIS, THIS, DSS and decision support tools) to build an integrated and comprehensive **digital ecosystem**,
allowing a fine and multidimensional description of the sites
a precise characterization of climatic hazards and
the execution of scenario simulations
and the development of adaptation trajectories
scientifically robust and operational.

Funded by Horizon 2020 to the tune of EUR **5.98 million**
over 48 months (2019-2023), the project deploys its pilot solutions on 8
emblematic European historic sites – Istanbul (principal pilot),
Rome, Valencia, Hamburg, etc. – and makes available all its ** open source software components** (code, modular databases, API, technical documentation) under
Free licenses, thus facilitating reuse and extension by other institutions or communities.

The ** conceptual and operational similarities** with the **ATLAS** project (presumed to target heritage or urban resilience in a comparable context) are striking:

- **Common concerns**: vulnerability of historical tissues to climate change
(heat islands, droughts, floods), protective role of
green heritage areas, need for decision-making tools
integrated built, vegetation and hazards.
- **Transferable technological solutions**:
- Interoperable SOA architecture, easily integrated with existing systems such as those of ATLAS.
- Rich and standardized HARIS data models (CONSTRUCTION/OBJECT/MEASURE),
directly reusable to document similar sites.
- Pipeline THIS → DSS for multi-scenario simulation (RCP 4.5/8.5,
urbanisation "Gris/Black/Green", earthquakes/floods), applicable to
problems of ATLAS.
- 3D visualization tools and GIS dashboards, already validated with 8 UNESCO site managers.

---

## Identification of ARCH Project Limits

Despite its significant progress, the ARCH project has some shortcomings.
of which limited its completeness for the full management of
risks on heritage sites. These gaps concern both the
richness of descriptive data and simulation capabilities
dynamic.

### Enrichment of descriptive data

The fine representation of sites via HARIS (tables CONSTRUCTION, OBJECT,
MEASURE) remains perfectable on several critical dimensions:

- **Detailed technical characteristics**: enrichment of attributes for buildings, artifacts, circulation axes (dynamic load capacities, alternative configurations).
- **Social and demographic data**: lack of fine classification of populations (permanent residents, tourists, seasonality, specific vulnerabilities – PMR, children, seniors).
- **Operational capacities of rescue**: no modelling of response infrastructures (emergency posts, water points, vehicle access, theoretical response times).
- **A review of past claims**: limited data on victims (space location of human impacts, types of injuries, aggravating factors).
- **Heritage ecology**: protection of underdeveloped historical plant species (protected species lists, regulatory status, climate stress conservation strategies).

## Deficits in dynamic simulation

ARCH excels in climate, seismic and hydrological scenarios, but has two major absences:

1. **Simulation of fire propagation**: although THIS provides excellent preliminary indicators (SPEI,
CDD, plant fuel load, ignition conditions) and HARIS
details flammable materials (wood, dry vegetation), project
stops at the "before" and "after" phases, without modeling the dynamics
spread of flames (preferential paths, advanced speeds,
hot spots, built-vegetation interaction).

Team **Soc-SIM-K** precisely fills this void with its
3D fire models suitable for dense, exploitable heritage sites
directly on existing HARIS bases.

2. **Human behaviour in crisis**: DSS simulations focus on material damage, ignoring human flows (panic, congestion, evacuations, refuge areas). However **Soc-SIM-K** develops realistic behavioral agents (pedestrians, rescue vehicles, disoriented tourists), perfectly compatible with the geometries and capacities of the HARIS traffic axes.

---

# Study C2Impress

C2Impress is a Horizon Europe project (2023–2026) coordinated by the Joint Research Centre (JRC) and involving more than 18 European partners. Its objective is to develop an inclusive co-creation framework to improve understanding, preparedness and response to multiple natural and socio-environmental hazards, including floods, droughts, fires and coastal hazards.

##1. General framework and objectives

C2Impress's vision is based on:

- Association between science, local authorities and citizens;
- The use of multi-hazard simulations and indicators of social and cultural impact;
- Co-construction of decision-making tools to strengthen local resilience.

The deployed *Living Labs* are used to test reproducible methodologies for other heritage contexts, including historical sites and their landscape environments.

---

##2. Information systems and data management

## 2.1. Information system

- 2.1.1. Architecture and database

The central system of C2Impress is based on a distributed and interoperable architecture, in line with FAIR principles (Findable, Accessible, Interoperable, Reusable). It incorporates spatial-temporal (SIG) data, field observations and modelling results.

A geospatial base (PostSIG) allows the crossing of physical, human and heritage indicators at different scales (building, neighbourhood, watershed).

- 2.1.2. Heritage Data Diagram

Although the project primarily targets urban resilience, C2Impress introduces the concept of cultural property as sensitive elements of the territory, integrated into the layers of vulnerability. Cultural assets are classified according to their value, use and exposure to hazards.

For transposition purposes, a heritage data scheme applied to historic gardens could take up this model: plant entities, hydraulic structures, topography, soils, symbolic values.

- 2.1.3. Access and analysis tools

A decision scoreboard allows local actors to visualize the spread of hazards or the evolution of resilience indicators. Multi-criteria analysis modules
support development choices. These tools are designed for appropriation by non-expert audiences, a key point for mediation in heritage sites.


##2.2. Threats and Hazard Information System

In C2Impress, the functional equivalent of ARCH's THIS (Threats and Hazard Information System) is the SoS4MHRIN (System-of-Systems for Multi-Hazard Risk Intelligence Network).
This infrastructure centralizes and analyses data on multiple hazards (floods, fires, heat waves, compound droughts) in real time, using the Earth System Dynamic Intelligence (ESDI) for fine and dynamic predictions of multi-hazard hazards.

- 2.2.1. Multi-source collection and integration

SoS4MHRIN orchestrates a continuous and heterogeneous collection of data from multiple scales and vectors:

- Satellite sources: Copernicus data, MODIS for fires and surface temperatures, supplemented by weather forecasts.
- In situ and IoT sensors: terrestrial station networks (rainometers, anemometers, wet soil sensors), deployed in Living Labs (e.g. Thessaloniki, Malta), with increased density near heritage critical sites.
- Urban and open data: OpenStreetMap, local critical infrastructure bases, historical hydro-meteo archives, enriched by citizen crowdsourcing via
mobile applications (signals of local anomalies).
- Socio-economic data: Demographic layers (population density, social vulnerability), integrated to contextualize human exposures.

Multi-source integration is based on dynamic flows that merge these data in near real time. Data fusion approaches (bayesian statistics and automatic learning) generate composite risk maps updated every 15-60 minutes depending on the hazard. For heritage gardens, this ability allows to follow
fine changes in water and thermal conditions affecting soils and vegetation, e.g. intersecting satellite rainfall with local root moisture measurements.

- 2.2.2. Threat indicators

SoS4MHRIN produces a set of standardized threat indicators (0-1), covering both extreme climatic hazards and their ecological impacts, adapted to a multi-scale assessment:

- Primary climate variables:
- Extreme temperatures and Heat Stress Index.
- Intense rainfall (intensity, duration, frequency for storm floods).
- Strong winds
- Drought indices (SPI, SPEI over 1-12 months).
- Environmental and ecological parameters:
- Soil health (volume humidity, compaction, potential erosion).
- Plant water stress.
- Flammable biomass load and slope stability.

These indicators are composite and probabilistic, incorporating contextualized warning thresholds (e.g. high fire risk if FWI > 30 AND soil moisture < 20%). They are particularly transferable to historical gardens: a garden can be monitored via a custom dashboard showing progressive degradation or sudden risks. In a heritage context, these metrics can be used to quantify how a garden acts as a buffer (reduced runoff by 40% via soil infiltration), while identifying its own vulnerabilities (clay soils inflating under cyclic drought).

This SoS4MHRIN approach offers proactive vigilance, which is essential to preserve historical sites against compound climatic hazards.

---

##3. Simulations and scenarios

C2Impress integrates advanced simulations within its **SoS4MHRIN** platform, mainly via the**Earth System Dynamic Intelligence (ESDI)** and **operational dynamic models**.
These tools allow to predict with high resolution
spatial-temporal (from event to climate scale) risks
of single or multiple hazards under various climatic scenarios,
from a "hazard-centric" approach to an assessment focused on the
places and populations. Simulations are empirically validated
in four pilot sites (Egaleo in Greece, Ordu in Turkey, and two
other in Southern Europe), covering urban and coastal contexts
vulnerable.

### 3.1. Simulated phenomena

The simulations of C2Impress target the ** extreme composite weather**, as well as non-standard high impact events. They model the **major hydrometeorological hazards**: river and rain floods, forest fires, heat waves, landslides induced by heavy rains, and droughts
extended.

Innovation is the capture of ** hazards** interactions (cascade effects or combined stress), such as drought that increases the risk of fire followed by post-fire flooding. **system simulation models** and **agent-based models (ABM)** assess multidimensional impacts (exposure, vulnerability)
physical/social, adaptive resilience), with reduced uncertainty due to fine predictions.

For historic heritage areas and gardens, these simulations are highly adaptable: they allow the study of the **water dynamics of soils** (infiltration/flooding), **plant stress** (loss of biomass under heat/dryness), or **impacts on biodiversity** (species sensitive to extreme compounds), by tagring gardens as "natural buffers" in models.

- 3.1.1. Emission scenarios

C2Impress is explicitly based on climate scenarios **RCP 4.5** and **RCP 8.5** for its local high-resolution projections. These scenarios calibrate simulations with medium (2030-2050) and long-term (2070-2100) horizons, testing resilience under progressive or extreme conditions.


3.2. Land use scenarios and microclimate

Projections of** land use (LULC)** derive from series such as CORINE Land Cover, simulated via ABM to anticipate urbanization, loss of vegetation cover, and their effects on **microclimate.** In historic gardens in dense environments, these scenarios clarify how heritage vegetation mitigates heat or regulates moisture, while assessing potential degradation under urbanization.

### 3.3. Scenarios of sudden disasters

- 3.3.1. Seismic scenarios

Simulations include earthquakes, via impact models on critical infrastructure and associated landslides. Transposable to historic sites, they assess the response of heritage structures (support walls, garden basins) to liquefaction of soils or tremors amplified by water saturation.

- 3.3.2. Rain flood scenarios

Modelling of storm and river floods, with real-time warnings and extent predictions. At high spatial resolution, these tools analyze watershed management in parks/gardens, simulating runoff, historic drain overload, and soil erosion.

- 3.3.3. Fire scenarios

Forest fires are simulated by integrating drought, winds and biomass, with early warning and dynamic propagation (e.g. via indices like FWI). For heritage gardens, these models guide plant planning (non-flammable species, green barriers), assessing how dry soils under SPC 8.5 increase vulnerability to burning.


These simulations, anchored in a co-creation with local actors,
provide dashboards for contingency plans adapted to
historical sites.

---

##4. Natural areas, gardens and soils as heritage assets

Yes,
several elements can enrich this section by exploiting more
explicitly the conceptual framework of C2Impress, which deals with spaces
natural as **"Natural Heritage Buffers"** or **"Green Resilience Layers"** in its ontologies and multi-alean models. These assets are integrated not as liabilities but as **dynamic components**
affecting exposure and overall site vulnerability. Here
a detailed version, with factual additions on modelling, cases
and direct links to your theme
Heritage gardens.

### 4.1. Semantic and physical representation

C2Impress uses a unified semantic **ontology** to model territorial entities, naturally extending to **historical landscape elements** such as gardens, beds, tree alignments or heritage hydraulic networks. Ontological classes include:
"HeritageAsset" (built property), "NaturalBuffer" (vegetation/soil) and "DynamicLayer" (temporal evolution), with properties such as soil texture, vegetation cover (NDVI percent) or water permeability.

This physical representation is based on LiDAR and altimeter data for the
fine topography of gardens (micromorphological reliefs, underground drains), coupled with knowledge graphs linking a heritage tree to its water function (absorbent roots) or seismic (soil stabilization).

4.2. Role of gardens and natural soils

In C2Impress, green spaces and soils are positioned as **active territorial resilience amplifiers**, beyond a simple protective layer: they modulate energy/hydric fluxes and absorb multi-alean shocks. The simulations of the pilot sites quantify concrete benefits: 30-50% reduction in storm runoff via soil-garden infiltration, 3-6°C mitigation of heat islands by evapotranspiration, and maintenance of 20-40% biodiversity refuge under combined stress.

In heritage sites, this ecological function overlaps with a ** strong cultural value and identity**, a dimension that C2Impress begins to integrate via "Cultural Resilience Score" indicators.

### 4.3. Monitoring the "health" of the natural environment

C2Impress, via SoS4MHRIN, combines remote sensing and IoT sensors (root moisture, soil/canopy temperature, water stress sensors via stomatal conductance). In Living Labs, proactive alerts are generated (e.g. early detection of dry leaf yellowing RCP 4.5), with real-time dashboards accessible to heritage managers.

Applied to historic gardens, this allows a holistic **monitoring**: plant vitality, soil moisture (critical thresholds for inflating clays), surface temperature, and microbiological health (indicators via permeability). Feedback loops (citizens reporting anomalies via app) reinforce accuracy, ideal for preventive site management.

4.4. Soil vulnerability and dynamics

The multi-source analysis of C2Impress modulates the **soil vulnerability** as a dynamic process, exposed to floods (erosion/overload), water stress (clay cracking) and interactions (earthquake + saturation leading to liquefaction). Indicators such as the Oil Vulnerability Index integrate compaction, porosity, organic load and slope, predicting failures.

These dynamics are translated into **heritage resilience breeders**: a stable garden soil under hazards protects historical foundations and vegetation; scenarios test interventions.

---

##5. Synthesis of technologies and approaches

C2Impress deploys a coherent technological ecosystem, centred on the **SoS4MHRIN** platform (System-of-Systems for Multi-Hazard Risk Intelligence Network), supported by**ESDI (Earth System Dynamic Intelligence)** and**IPAI (Information Physical Artificial Intelligence)**.
This architecture integrates dynamic simulations, unified semantic ontology and participatory tools for proactive multi-hazard risk management, validated at four pilot sites (Egaleo-Greece, Ordu-Turkey, and two others in Southern Europe).

### Main technologies

- **Multi-risk intelligence platform**: SoS4MHRIN centralizes satellite data (Copernicus/Sentinel), IoT in situ and citizen crowdsourcing, with real-time merger for high resolution risk cards.
- **Modelization and simulations**: Agent-Based Models (ABM) for LULC and microclimate scenarios; physical models for compound hazards (floods + fires) under RCP4.5/8.5.
- **Ontology and data**: RDF/OWL diagram modeling cultural property and "Natural Buffers", stored in interoperable geospatial bases (FAIR).
- **Decision tools**: Interactive dashboards, multi-criteria microservices and alerts
probabilists.
- **Citizen engagement**: Mobile applications and co-creation via Living Labs for integration local perceptions.

---

## C2Impress Stations

## Forces identified

- **A holistic approach "place and people-centered"**: The transition from the hazard-centered to a multidimensional assessment (exposure, socio-cultural vulnerability, adaptive resilience),
reducing predictive uncertainty.
- **Interoperability and scalability**: Multi-source dynamic fluxes and fine simulations, yransposable to heritage gardens as ecological buffers.
- ** Inclusive co-creation**: Science-citizen-authority involvement for accessible tools, fostering local ownership in historical sites and decision-making support.
**Human behaviour under crisis**: Human behaviour is simulated by archetypal agents, which emulates human bias in crisis contexts. However, there is little room for the representation of levels of information and the impact of civil relief, time and capacity for the invention of relief.

## Identify Project Limitations

- **Detailed technical specifications**: Insufficient enrichment of attributes for buildings, artifacts, traffic axes (dynamic load capacities, configurations)
alternatives); sub-granularized heritage assets (limited vegetation/historical soils, lack of palynology or landscape archaeology for gardens).
- **Socio-demographic data**: No fine classification of populations (permanent residents, tourists, seasonality, specific vulnerabilities – PMR, children, seniors).
- **Operational capacities of rescue**: No modelling of response infrastructures (emergency posts, water points, vehicle access, theoretical response times).
- **A review of past claims**: limited data on victims (space location of human impacts, types of injuries, aggravating factors).
- **Heritage Ecology**: Protection of underdeveloped historical plant species (lists)
protected species, regulatory status, safeguard strategies
in the face of climatic stress).

---

# Arches-HER Study

The Arches-HER project is part of the Arches software ecosystem, a real estate inventory and management system developed by the Getty Conservation Institute (GCI) and the World Monuments Fund (WMF).

###1. General framework and objectives

- Arches is an "open source" Web GIS, standard, for the inventory and management of real estate (archeological sites, buildings, cultural landscapes, heritage sets).
- The strategic objectives are: improved data management for conservation, broad adoption in the heritage sector, and recognition as a reference system for standardized heritage data management.
- Arches-HER can therefore be interpreted as a declination dedicated to Historic
Environment Records: a framework for structuring, documenting and exploiting territorial heritage data (city, region, state) to inform planning, impact assessment and risk management.

---

##2. Information systems and data management

## 2.1. Information System

- 2.1.1. Architecture and database

Arches implements a corporate Web architecture centered on a PostgreSQL/PostGIS database for spatial and relational data, enriched with a semantic graph via the SPARQL query engine (Arches often uses Apache Jena or an integrated triplestore RDF layer).

- **Extension of ontology** : Based on CIDOC CRM as a basic ontology, Arches extends the model with concepts specific to the real estate heritage (e.g. HER-specific extensions for resources such as "Historic Assets", spatial relations, condition workflows assessment). The GitHub repository "archesproject/cido-crm-ontology" includes "arches crm enhances.xml" to model conservation events, threats and local actors, ensuring semantic interoperability.
- **No integrated simulation system**: No native implementation of dynamic simulations (RCP, hydrology, etc.); Arches is limited to importing results in the form of PostGIS or RDF layers (e.g., cross weather hazard rasters with heritage resources via geo-requests).
- ** Cross-databases**: Supports multi-source integration via RDF mappings for cross-inventories legacy, LIDAR data, external APIs (e.g. EAMENA, Getty Vocabulary) and open databases (OSM, Copernicus). The "branches" and "graph branches" allow collaborative workflows to validate crossovers without duplication.

This approach prioritizes semantic and spatial flexibility for HER, with customization via "resource models" (modular designs) and controlled vocabularies.

- 2.1.2. Heritage Data Diagram
- Arches incorporates international standards for the description of heritage (Core Data Standard for Archaeological Sites and Monuments, Core Data Index for Historic Buildings) to identify "minimum essential data" to document heritage places.
- The conceptual model uses CIDOC CRM ontology as a reference ontology to structure information (actors, events, objects, places, temporalities).
- Specifically, an Arches-based HER describes each heritage resource as a
a set of related entities (resource, historical events, conservation interventions, values, threats, documentary sources), rather than simply a flat sheet.
- 2.1.3. Access and analysis tools
- The system offers Web consultation interfaces, with map search, filters, attribute queries, and visualization of detailed sheets.
- It is designed to serve both managers (analysis, monitoring, impact assessment) and the general public (sensitivity, valuation), with differentiated access profiles.
- Arches can be used for the preparation of decisions (urban planning, conservation, risk management) by crossing heritage data with other spatial layers, thanks to its GIS integration. But there is no integrated decision support tool

##2.2. Threats and Hazard Information System

- 2.2.1. Multi-source collection and integration
- Arches supports the integration of data from multiple sources: existing inventories, historical maps, satellite images, national databases, research projects, etc., with the possibility of pre-processing and standardizing data before integration.
- Regional implementations show its use to document endangered heritages from various sources (existing sites, imagery, archives), in the same database managed and shared.
- For a risk-oriented HER, additional layers can be considered: hazards (flooding, erosion, seismicity), land uses, infrastructure, climate data, in the form of GIS layers or links to other systems.
- 2.2.2. Threat indicators
- Arches supports threat and risk documentation through dedicated fields and entities (threat categories, intensity, probability, integrity effects, management status).
- The system can be used as a basis for monitoring long-term conditions and threats, allowing for indicators (number of high-risk sites, evolution of threats by area, etc.), even if the construction of indicators depends on customisation
local. Such an extension would require the implementation of an entire extension of the representation of the Aléa.

---

##3. Simulations and scenarios

### 3.1. Simulated phenomena

- Similarly, Arches is not a simulation engine for physical phenomena (rain, runoff, fire propagation, etc.), but a framework for storing, georeferencing and exploiting the results of such models.
- However, this type of storage could be used to improve the communicability of simulation results.

---

##4. Natural areas, gardens and soils as heritage assets

### 4.1. Semantic and physical representation

- Arches allows to define types of resources for cultural landscapes, historical gardens and landscape ensembles, with geometry (right-of-way, boundaries, internal elements) and structured description.
- The CIDOC CRM model represents the relationships between vegetation, built structures, management interventions and historical events, which is adapted to gardens and soils as complex heritage entities.
- Gardens and soils can be modelled as resources with specific values (ecological, aesthetic, social, symbolic) and functions (regulation of microclimate, infiltration, protection against erosion).
- In a HER, they can be integrated into climate change impact assessments or urbanisation, in conjunction with the functions of protecting built sites (e.g. the role of vegetated buffer zones).
- Arches can store repeated observations (field campaigns, botanical monitoring, soil analysis, imaging) and thus support monitoring of the condition of gardens and soils, provided that indicators (plant cover, biodiversity, humidity) are defined by the project.

It was noted that all these possibilities of representation are not natively integrated, but that Arches is adapted to deploy such epistemological construction.

---

##5. Synthesis of technologies and approaches

- Arches-HER is based on an open source Web GIS structured by heritage standards (Core Data Standards, CIDOC CRM) and designed for multi-source integration and threat tracking.
- The system is positioned as a data base and management (inventory, monitoring, decision support) rather than a simulation engine; It interfaces with external tools for climate, hydrological or seismic scenarios.
- Its strength lies in the ability to harmonize and link heterogeneous information (built heritage, landscapes, threats, management measures) to support the conservation, planning and resilience of historic sites.

## Identified Project Limits (Arches-HER as Decline ofArches)

- Dependence on external tools for dynamic simulation (RCP, floods,
fire, etc.): Arches manages results but does not generate them.
- Need for significant efforts to standardize and clean up historical data before integration, in particular to align with controlled standards and vocabularies.
- The need for customisation (schema, indicators, interfaces) so that the system really meets the specific needs of a HER and risk management, which requires technical and organisational resources.

### Enrichment of descriptive data

- Arches offers a rich framework for semantic description (actors, events, values, threats), but this wealth is exploited only if one invests in the fine structuring of data (ontologies, controlled vocabularies, links to sources).
- For a HER, a key enrichment axis is the systematic annotation of resources by their vulnerabilities, ecological functions (green spaces, soils) and adaptation measures, in order to go beyond the simple descriptive inventory.

## Deficits in dynamic simulation

- The device as designed does not replace an integrated multi-risk simulation platform: the links between scenarios, temporal trajectories and decisions remain to be set through workflows and external tools.
- One of the risks is to remain static rather than integrate trajectories and
dynamic scenarios (PCR scenarios, changes in soil use, perturbation cycles).

---

# Proposal to adapt to the ATLAS project

The integration of the ARCH (HARIS) and C2Impress (SoS4MHRIN) projects represents a major opportunity for the ATLAS project. This coupling allows to merge an ultra-cut heritage database with a dynamic and participatory multi-aléas intelligence.

Here is a strategic analysis of the interests of this coupling, the development needs for the fire simulator and the path to a unified ontology.

## Matching Interests: Towards a Dynamic Digital Twin

The coupling between HARIS and C2Impress allows the transition from a static inventory of assets to a predictive management system.

Among other things, this would create complementarity Data/Flux: HARIS brings structural precision (building materials, type of garden objects, 3D geometry), while C2Impress provides data flows (soil moisture, water stress, Copernicus satellite data) and simulation in real time.

Also vulnerability analysis could be performed by crossing the CONSTRUCTION database of HARIS with the "Soil Vulnerability Index" of C2Impress, one can predict how drought physically impacts historical sites and their foundations.

Finally, we would significantly increase our validation capacity by the "Living Labs": The participatory approach of C2Impress allows the validation of HARIS vulnerability models through crowdsourcing, enriching the heritage database with updated field observations.

## Development of a Uniform Ontology

For both systems to communicate, it is imperative to create a common semantic layer, ideally based on an extension of CIDOC CRM.
What needs to be developed:

1. Class reconciliation: Create mappings between the HeritageAsset classes of C2Impress and the CONSTRUCTION/OBJECT bases of HARIS.
2. Modelization of the "Natural Heritage Buffer": Develop an ontology that no longer treats the garden as a simple decor, but as an active entity with thermal resistance and hydraulic permeability properties.
3. Standardisation of indicators: Adopt the approach of C2Impress to standardize heterogeneous data of HARIS, thus allowing to compare risks of different nature on the same decision scale.

## "Plugger" the Soc-SIM-K fire simulator

The ATLAS project identifies the absence of dynamic fire simulation as a major limit of ARCH. To integrate the developing simulator here are the bridges to build:

1. Data flow required:

Inputs (from C2Impress): Retrieve in real time the Fire Weather Index (FWI), flammable biomass load and wind conditions.

2. Structural context (since HARIS):

Extract the combustible properties of the materials (wood, carpentry) and the spatial configuration of the assets to define the propagation paths.

3. Developments required for "Plug-in":

Propagation API Interface: Develop a connector that can inject the propagation vectors of Soc-SIM-K into the high-precision 3D viewers of HARIS.

4. Human Behaviour Module:

Use C2Impress's Agent-Based Models (ABM) to simulate the evacuation of populations (tourists, PMRs) through documented traffic axes in HARIS.

5. Feedback on Damage:

Create a script that automatically updates the conservation status in HARIS after a fire simulation, estimating material losses and soil degradation.

6. Estimated evacuation conditions:

Detailed classification of victim profiles, testing of emergency service intervention scenarios and simulation of potential psychological impacts.


---

# Conclusion

In conclusion, the adaptation of the ATLAS project by the HARIS–C2Impress coupling could pave the way for a dynamic digital twin of heritage, capable of articulating fine knowledge of objects and multi-alean intelligence in near real time. This reconciliation would transform a descriptive inventory into a predictive management system, where structural vulnerability, soil dynamics, active role of gardens and human behaviour would be integrated into the same decision-making chain.

The construction of a unified ontology, based on an extension of CIDOC CRM, would be the key architecture for dialogue between heritage bases, environmental indicators and fire simulators, while making comparable risks of a different nature on a common scale. The integration of Soc‐SIM‐K as a fire simulation module, connected to propagation models, detailed structural data and evacuation-based agent models, would fill one of the main deficits identified in ARCH by adding a dynamic and prospective dimension.

Thus, ATLAS could position itself as an integrated heritage resilience platform, where Living Labs would play a continuous feedback loop role, validating models, correcting data and enriching understanding of the psychological and social impacts of crises. This vision would make heritage not only an object to be protected, but a potential hub for designing, testing and adjusting adaptation strategies to climate and extreme risks, both at site and territory level.
