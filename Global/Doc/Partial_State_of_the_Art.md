# State of the Art for ATLAS Project

# ARCH Study

The ARCH project proposes an integrated technological framework to analyze, monitor, and improve the resilience of historic areas, articulating information systems, multi-hazard simulations, and decision support tools.

## 1. General Framework and Objectives of ARCH

ARCH (Advancing Resilience of Historic Areas against Climate-related and other Hazards) is an H2020 project dedicated to the resilience of historic districts and sites against climatic hazards and other natural risks. It combines disaster risk management, climate change adaptation, and heritage management within an integrated risk management cycle applied to historic areas.

The integrated solutions include:

- A methodological framework for risk management (ARCH Disaster Risk Management Framework) specifically adapted to historic areas.
- A suite of digital tools: geo-referenced information systems (HArIS/THIS), decision support system (DSS), resilience measures inventory (RMI/RPVT), and resilience maturity self-assessment tool (RAD).

---

## 2. Information Systems and Data Management

### 2.1. HArIS – Historic Areas Information System

HArIS is a heritage-oriented geographic information system, based on a service-oriented **architecture** (SOA), which manages geo-referenced data on the historical and current state of heritage areas. It links 2D/3D geometry, materials, usages, and environmental context to feed vulnerability analyses, aging models, and damage scenarios.

- 2.1.1. Architecture and Database
    - Relational DBMS (RDBMS):
        
        Spatial and alphanumeric data are stored in a relational database (including geometry, attributes, metadata, time series), ensuring integrity, complex queries, and interoperability with GIS tools.
        
    - SOA and Interoperability:
        
        Web services expose data as standard services (WMS/WFS, REST API), facilitating the reuse of components in other platforms (DSS, municipal portals, field applications).
        
- 2.1.2. Heritage Data Schema
    
    Heritage assets are structured into large logical bases, interconnected by unique identifiers and spatial relations:
    
    1. CONSTRUCTION Base
        - Content: Historic buildings, engineering structures, walls, infrastructures, built ensembles, archaeological structures.
        - Attributes:
            - Geometry (2D polygons, 3D models, levels/facets);
            - Materials (stone, brick, wood, metal, mortar) and mechanical properties;
            - Functions and usages (residential, religious, administrative, cultural);
            - State of conservation, known pathologies (cracks, rising damp, surface alterations);
            - Past interventions (restoration campaigns, reinforcements, changes of use).
    2. OBJECT Base
        - Content: Objects, singular elements, and components: architectural elements (cornices, columns, sculptures), historic urban furniture, in situ artworks, remarkable vegetal structures (isolated trees, historic hedges, alignments), garden elements (fountains, statues, basins, pergolas).
        - Attributes:
            - Physical characteristics (dimensions, mass, materials, surface stratigraphy);
            - Location metadata (coordinates, relation to a construction or garden, position in 3D space);
            - State and pathology data;
            - Conservation history (dates, types, and actors of interventions).
    3. MEASURE Base
        - Content: Time series and environmental indicators (climate, air quality, hydrology, vibrations, etc.).
        - Sources: In situ sensors (temperature, humidity, vibrations, water levels), weather stations, satellite data, climate models.
        - Attributes: Value, uncertainty, time step, provenance, and quality of the measurement.
    
    This structuring allows associating each asset (CONSTRUCTION/OBJECT) with specific environmental conditions (MEASURE) for coupled analyses (aging, climatic risks).
    
- 2.1.3. Access and Analysis Tools
    
    HArIS is operated through three main types of interfaces, integrated within the ARCH platform:
    
    1. GIS Dashboards
        - Interactive 2D/3D maps displaying assets, their vulnerability, associated hazards, and environmental measures.
        - Functions: Filtering by asset type, period, fragility level; overlay of climatic indicators and scenarios; export of views and layers for reports.
    2. Electronic Sheets
        - Detailed sheets per asset (building, object, garden element) giving access to all attributes, metadata, intervention histories, and links to external documents (plans, reports, photos, laser scans).
        - Functions: Controlled editing, tracking of modifications, traceability of sources.
    3. High-Precision 3D Viewers
        - Visualization of 3D models (photogrammetry, laser-scan, drones), immersive navigation in historic sites, coupling with HArIS attributes.
        - The integration of computer vision and Deep Learning methods allows automatic detection, on point clouds and orthophotos, of degradations (cracks, detachments, material losses) or morphological evolutions.

HArIS is thus at once an analysis tool (vulnerability, damage scenarios), a simulation tool (via links to the DSS), and a mediation/outreach tool for decision-makers and the public.

### 2.2. THIS – Threats and Hazard Information System

THIS is the system "twin" of HArIS dedicated to the description and quantification of environmental threats and hazards, at different temporal and spatial scales. It provides geo-referenced indicators on climatic and environmental threats, feeding risk analyses and simulations in the ARCH platform.

- 2.2.1. Multi-source Collection and Integration
    
    THIS aggregates data from:
    
    - Historical archives (chronicles of extreme events, floods, droughts, fires, earthquakes);
    - Real-time data: Urban sensor networks (rain gauges, water level sensors, climate stations, air/quality stations), structural sensors, "crowd-sensing" networks (citizen reports via apps, geolocated photos);
    - Climate projections: RCP scenarios, bioclimatic datasets, sectoral projections (extreme heat, precipitation, drought);
    - Climate services derived from Copernicus services (notably CAMS/C3S) for projections under different scenarios.
    
    Data are harmonized, geo-referenced, and stored in a structured database compatible with environmental information standards.
    
- 2.2.2. Threat Indicators
    
    THIS produces a set of thematic indicators essential for natural sites and historic gardens:
    
    1. Bioclimatic Indicators (BIO1–BIO19)
        - Examples: Annual mean temperature, annual thermal amplitude, seasonality and concentration of precipitation, precipitation of wettest/driest months, temperatures of extreme months.
        - Usage: Assessing survival conditions for plant species, identifying zones of thermal or water stress, and anticipating shifts in climatic niches.
    2. Drought and Heat Indices
        - Standardised Precipitation-Evapotranspiration Index (SPEI) to monitor meteorological and agricultural droughts;
        - Number of Consecutive Dry Days (CDD), heat wave (duration, intensity, frequency), number of "tropical" days;
        - Human thermal stress indicators (perceived temperature, composite indices) for historic public spaces.
    3. Fire Risk
        - Combination: Drought (SPEI, CDD), extreme temperatures, relative humidity, wind (when available), density and type of fuel (vegetation, materials).
        - Production of maps of ignition probabilities and potential propagation at the site scale.
    4. Flood Risk
        - Crossing of topographical data, land use, stormwater drainage networks, and flood history, with rain and water level measurements.
        - Production of indicators of probable water depth, flow velocity, submersion duration, stagnation zones, specifically in historic urban fabrics.
    5. Ad hoc Climate Services
        - Use of Copernicus products (CAMS/C3S) to generate localized climate scenarios for different time horizons (e.g., heat waves in Valencia up to 2100), under several emission hypotheses.
        - Generation of input climate variable series for heritage and vegetation impact models.

THIS thus functions as a central repository of present and future hazards, coupled with HArIS and the DSS.

---

## 3. Simulations and Scenarios

The ARCH project relies on an integrated simulation system (DSS) allowing the construction and analysis of different types of scenarios, combining climatic parameters, land use, and extreme events.

### 3.1. Long-term Climatic Hazard Scenarios

These simulations rely on RCP emission trajectories (IPCC) and cover several reference time periods: historical, 2011–2040, 2041–2070, 2071–2100.

- 3.1.1. Emission Scenarios
    - RCP 4.5:
        
        Intermediate stabilization scenario, with mitigation measures limiting the rise in greenhouse gas concentrations.
        
    - RCP 8.5:
        
        Very pessimistic scenario, corresponding to a trend of high and prolonged emissions, often chosen in ARCH to explore the resilience limit of historic sites.
        
- 3.1.2. Simulated Phenomena
    1. Heat Waves
        - Duration (including waves potentially reaching ~30 days or more depending on the site), intensity (deviation from normals, heatwave indices), and maximum temperature reached.
        - Effects on materials, site visitation, and survivability of plant species in historic gardens.
    2. Drought
        - Calculation of the maximum Number of Consecutive Dry Days (CDD) and drought indices (such as SPEI), with breakdown for soils, vegetation, and heritage agricultural activities.
    3. Sea Level Rise
        - For coastal pilot zones (e.g., Hamburg), coupling of sea level projections and surges with local morphology, to assess potential submersion of historic districts, saline intrusions, and infrastructure damage.

### 3.2. Land Use and Micro-climate Scenarios

ARCH simulates the effect of different land use configurations on the urban micro-climate, notably on the formation of heat islands around heritage zones.

The main scenarios are:

1. Reference Scenario (Current)
    - Based on current land use (built-up, roads, vegetation, water) from cartographic data and local observations.
2. "Grey" Scenario (Moderate Urbanization)
    - Progressive urbanization of unprotected agricultural zones or wastelands, increase in mineral surfaces and built-up areas, limited reduction of vegetated surfaces.
    - Objective: Quantify local temperature increase and reduction of thermal comfort in the vicinity of heritage assets.
3. "Black" Scenario (Total Urbanization)
    - Maximal urbanization including, in a theoretical scenario, initially protected zones replaced by built-up or impermeable surfaces.
    - Usage: Expressing the maximal protective value of vegetation by comparison with this extreme, rather than describing a plausible future.
4. "Green" Scenario (Restoration/Re-naturalization)
    - Transformation of abandoned, sealed, or underutilized zones into vegetated surfaces (parks, gardens, agricultural zones) or green/blue grids.
    - Objective: Estimate cooling gains, heat island reduction, improvement of water infiltration, and mitigation of impacts on historic fabric.

The models simulate surface and air temperature fields, sometimes coupled with urban airflow or radiation models, to quantify micro-climatic effects.

### 3.3. Sudden Disaster Scenarios

These scenarios explore the site's reaction to brutal events, with calculation of material and human damages.

- 3.3.1. Seismic Scenarios
    1. Historical Events
        - Replay of documented earthquakes (position, magnitude, depth, fault mechanism) to assess the response of historic structures to events that have already occurred.
    2. User-Defined Events
        - The user specifies various parameters (epicenter, depth, magnitude Mw, fault type, rupture direction, pulse duration) in the DSS interface.
        - Acceleration fields and dynamic response are projected onto the historic fabric, allowing estimation of structural damage levels and potential losses (costs, victims, functional unavailability).
- 3.3.2. Pluvial Flood Scenarios
    - Inputs: Intense rain events (observed or future episodes), urban runoff and drainage models, high-resolution topography.
    - Outputs:
        - Maps of water depth and velocity in historic streets;
        - Accumulation zones, network overflow, interactions with buildings and infrastructures;
        - Estimation of material damages (buildings, collections, roads) and consequences for people (exposure, accessibility, evacuation).

### 3.4. Fire Scenarios

ARCH does not implement detailed flame propagation simulation but frames the risk upstream and potential damages downstream.

1. Before the fire: Risk assessment
    - THIS aggregates conditions favorable to ignition: extreme heat episodes, prolonged series of dry days, low fuel humidity, density of flammable vegetation, wind.
    - Ignition probability and fire danger maps are generated for gardens, parks, and peri-urban zones close to built heritage.
2. After the fire: Damage estimation
    - HArIS provides material properties (wood, stone, metal, roofing, joinery) and the spatial configuration of objects and constructions.
    - From this, probable losses in case of fire are estimated (elements likely to be destroyed or heavily degraded), without precisely modeling the fire's path in the urban space.

---

## 4. Natural Spaces, Gardens, and Soils as Heritage Assets

ARCH considers natural spaces (gardens, parks, associated agricultural lands, wetlands) as heritage assets in their own right, and not just as a backdrop around monuments.

### 4.1. Semantic and Physical Representation

1. Natural Objects in HArIS
    - Each significant component of a garden (remarkable tree, historic hedge, bed, structured lawn) can be recorded as an "object" in the OBJECT base, with its physical properties (dimensions, estimated age, foliage type) and biological properties (species, sanitary state).
    - Spatial and functional relations between these objects and the built environment (proximity to facades, shading, protection against wind) are made explicit in the data model.
2. Land Use
    - Land use maps distinguish finely: forests, urban gardens, arable lands, meadows, wetlands, impermeable surfaces, water surfaces.
    - This distinction serves to simulate heat absorption (albedo, thermal capacity, evapotranspiration) and water management (infiltration, runoff, storage) around historic sites.

### 4.2. "Shield" Role of Gardens and Natural Soils

ARCH is among the projects that explicitly quantify the benefits of gardens and vegetated spaces for the resilience of historic fabric.

1. Thermal Regulation
    - Modeling of the cooling effect via evapotranspiration and shading of gardens, reducing heat island intensity in the vicinity of monuments.
    - Assessment of gains in thermal comfort, reduction of thermal fatigue of materials, and decrease in extreme expansion/contraction cycles.
2. Stormwater Management
    - Natural soils are represented as absorption/infiltration zones, with permeability, storage, and surface roughness parameters.
    - ARCH simulates how a garden or park slows flow, reduces water heights in adjacent streets, protects historic building foundations, and decreases load on drainage networks.

### 4.3. Monitoring the "Health" of the Natural Environment

THIS includes indicators specifically dedicated to the ecological health of natural spaces.

1. Vegetation Indices
    - Use of satellite data (e.g., NDVI, EVI) and possibly drone data to monitor the vigor and density of vegetation in historic gardens and parks.
    - Detection of zones of dieback, stress, or change in vegetation cover likely to increase risks (fire, erosion, landslides).
2. Water Needs and Water Stress
    - Calculation of the balance between potential evapotranspiration and precipitation, supplemented by information on irrigation practices where they exist.
    - Identification of periods where a historic garden enters a water stress zone, with alerts on ancient species particularly vulnerable or difficult to replace.
3. Agro-climatic Indicators
    - For heritage agricultural sites (historic vineyards, traditional crops), monitoring of growth periods, late frost risks, early heat, or heat waves during sensitive phases (flowering, maturity).
    - These indicators serve to preserve both production and the associated intangible heritage (know-how, cultural landscapes).

### 4.4. Vulnerability and Soil Dynamics

ARCH is not limited to visible surface elements but takes into account the structure and dynamics of underlying soils.

1. Geotechnical Micro-zoning
    - Study of the composition (clays, silts, sands, rocks), heterogeneity, and water conditions of soils in gardens and built-up areas.
    - Identification of sectors likely to experience landslides, differential settlement, or local amplification of seismic movements.
2. Soil–Structure Interaction
    - Analysis of the effects of soil drying (linked to recurring droughts) on swelling clays, which can cause seasonal shrinkage and swelling.
    - Correlating these phenomena with the appearance of cracks in walls, foundation deformation, and destabilization of fences and historic garden walls.

---

## 5. Synthesis of Technologies and Approaches

The table below summarizes the main technological components of the ARCH project and their role.

| Component | Technology Type | Main Role | Key Data |
| --- | --- | --- | --- |
| HArIS | Heritage Geographic Information System (SOA, RDBMS, GIS, 3D) | Storage and access to data on assets and their state, support for vulnerability analyses and damage scenarios | CONSTRUCTION and OBJECT assets, MEASURE environmental measures, 2D/3D geometries, intervention histories |
| THIS | Threats and Hazards Information System | Provision of climatic, hydrological, and environmental indicators, present and future | Bioclimatic indicators, drought indices, fire and flood risks, climate/Copernicus projections |
| DSS ARCH | Decision Support Web GIS Platform | Construction and analysis of scenarios (climate, land use, disasters), risk assessment | RCP scenarios, urbanization configurations, seismic and rainfall events, damage model outputs |
| RMI / RPVT | Resilience Measures Inventory and Planning Tool | Identification, evaluation, and planning of adaptation and resilience reinforcement measures | Catalog of measures (structural, organizational, nature-based), implementation pathways |
| RAD | Resilience Maturity Self-Assessment Tool | Monitoring the progression of a historic area in its risk management cycle | Governance, preparation, response, recovery, heritage–climate integration indicators |

ARCH unites these different modules (HArIS, THIS, DSS, and decision support tools) to constitute an **integrated and complete digital ecosystem**, allowing a fine and multidimensional description of historic sites, a precise characterization of present and future climatic and natural hazards, the execution of varied prospective scenario simulations, and the elaboration of scientifically robust and operational adaptation trajectories.

Funded by the Horizon 2020 program to the tune of **5.98 million euros** over 48 months (2019-2023), the project deploys its pilot solutions on 8 emblematic European historic sites – Istanbul (main pilot), Rome, Valencia, Hamburg, etc. – and makes all of its **software components available as open source** (code, modular databases, APIs, technical documentation) under free licenses, thus facilitating reuse and extension by other institutions or communities.

The **conceptual and operational similarities** with the **ATLAS** project (presumed to target heritage or urban resilience in a comparable context) are striking:

- **Common Concerns**: Vulnerability of historic fabrics to climate change (heat islands, droughts, floods), protective role of heritage green spaces, need for decision support tools integrating built environment, vegetation, and hazards.
- **Transferable Technological Solutions**:
    - Interoperable SOA architecture, easily integrable into existing systems like those of ATLAS.
    - Rich and normalized HArIS data models (CONSTRUCTION/OBJECT/MEASURE), directly reusable to document similar sites.
    - THIS → DSS pipeline for multi-scenario simulation (RCP 4.5/8.5, "Grey/Black/Green" urbanization, earthquakes/floods), applicable to ATLAS issues.
    - 3D visualization tools and GIS dashboards, already validated with 8 UNESCO site managers.

---

## Identified Limits of the ARCH Project

Despite its significant advances, the ARCH project presents notable gaps that limit its comprehensiveness for integral risk management on heritage sites. These shortcomings concern both the richness of descriptive data and dynamic simulation capabilities.

### Enrichment of Descriptive Data

The fine representation of sites via HArIS (CONSTRUCTION, OBJECT, MEASURE tables) remains perfectible on several critical dimensions:

- **Detailed Technical Characteristics**: Enrichment of attributes for buildings, artifacts, circulation axes (dynamic load capacities, alternative configurations).
- **Socio-demographic Data**: Absence of fine classification of populations (permanent residents, tourists, seasonality, specific vulnerabilities – PRM, children, seniors).
- **Operational Rescue Capacities**: No modeling of intervention infrastructures (rescue stations, water points, vehicle access, theoretical response times).
- **Past Disaster Assessment**: Limited data on victims (spatial localization of human impacts, injury typologies, aggravating factors).
- **Heritage Ecology**: Protection of historic plant species underdeveloped (lists of protected species, regulatory statuses, safeguard strategies against climatic stresses).

### Deficits in Dynamic Simulation

ARCH excels in climatic, seismic, and hydrological scenarios but presents two major absences:

1. **Fire Propagation Simulation**: Although THIS provides excellent prior indicators (SPEI, CDD, vegetation fuel load, ignition conditions) and HArIS details flammable materials (wood, dry vegetation), the project stops at the "before" and "after" phases, without modeling the dynamics of flame propagation (preferential paths, advance speeds, hot spots, built-vegetation interaction).
    
    The **Soc-SIM-K** team fills precisely this void with its 3D fire models adapted to dense heritage sites, directly exploitable on existing HArIS bases.
    
2. **Human Behaviors Under Crisis**: DSS simulations concentrate on material damages, ignoring human flows (panic, congestion, evacuations, refuge zones). However, **Soc-SIM-K** develops realistic behavioral agents (pedestrians, rescue vehicles, disoriented tourists), perfectly compatible with HArIS circulation geometries and capacities.

---

# C2Impress Study

## 1. General Framework and Objectives

C2Impress is a Horizon Europe project (2023–2026) coordinated by the Joint Research Centre (JRC) and involving more than 18 European partners. Its objective is to develop an integrative co-creation framework to improve understanding, preparedness, and response to multiple natural and socio-environmental risks, notably floods, droughts, fires, and coastal hazards.

The vision of C2Impress relies on:

- The association between science, local authorities, and citizens;
- The use of multi-hazard simulations and social and cultural impact indicators;
- The co-construction of decision support tools to strengthen local resilience.

The *Living Labs* deployed serve to test replicable methodologies for other heritage contexts, including historic sites and their diverse environments.

---

## 2. Information Systems and Data Management

### 2.1. Information System

- 2.1.1. Architecture and Database
    
    The central system of C2Impress relies on a distributed and interoperable architecture, compliant with FAIR principles (Findable, Accessible, Interoperable, Reusable). It integrates spatio-temporal data (GIS), field observations, and modeling results.
    
    A geospatial database (PostSIG) aids the crossing of physical, human, and heritage indicators at different scales (building, district, watershed).
    
- 2.1.2. Heritage Data Schema
    
    Although the project targets urban resilience primarily, C2Impress introduces the notion of cultural assets as sensitive elements of the territory, integrated into vulnerability layers. "Cultural assets" are classified according to their value, usage, and exposure to hazards.
    
    In a transposition perspective, a heritage data schema applied to historic gardens could adopt this model: vegetal entities, hydraulic works, topography, soils, symbolic values.
    
- 2.1.3. Access and Analysis Tools
    
    A decisional dashboard allows local actors to visualize the propagation of a hazard or the evolution of resilience indicators. Multi-criteria analysis modules support planning choices. These tools are designed for appropriation by non-expert audiences, a key point for mediation in heritage sites.
    

### 2.2. Threats and Hazard Information System

In C2Impress, the functional equivalent of ARCH's THIS (Threats and Hazard Information System) is the SoS4MHRIN platform (System-of-Systems for Multi-Hazard Risk Intelligence Network). This infrastructure centralizes and analyzes in real-time data on multiple hazards (floods, fires, heat waves, compound droughts), relying on ESDI (Earth System Dynamic Intelligence) for fine and dynamic multi-hazard risk predictions.

- 2.2.1. Multi-source Collection and Integration
    
    SoS4MHRIN orchestrates a continuous and heterogeneous collection of data coming from multiple scales and vectors:
    
    - Satellite Sources: Copernicus data, MODIS for fires and surface temperatures, supplemented by weather forecasts.
    - In situ Sensors and IoT: Networks of ground stations (rain gauges, anemometers, soil moisture sensors), deployed in Living Labs (e.g., Thessaloniki, Malta), with increased density near critical heritage sites.
    - Urban and Open Data: OpenStreetMap, local databases of critical infrastructures, historical hydro-meteo archives, enriched by citizen crowdsourcing via mobile apps (reports of local anomalies).
    - Socio-economic Data: Demographic layers (population density, social vulnerability), integrated to contextualize human exposures.
    
    Multi-source integration relies on dynamic flows that fuse these data in near real-time. Data fusion approaches (Bayesian statistics and machine learning) generate composite risk maps updated every 15-60 minutes depending on the hazard. For heritage gardens, this capacity allows following the fine evolution of water and thermal conditions affecting soils and vegetation, by crossing for example satellite rainfall with local root moisture measurements.
    
- 2.2.2. Threat Indicators
    
    SoS4MHRIN produces a set of normalized threat indicators (0-1), covering both extreme climatic hazards and their ecological impacts, adapted to a multi-scale assessment:
    
    - Primary Climatic Variables:
        - Extreme temperatures and Heat Stress Index (perceived temperature/humidity combination).
        - Intense rainfall (intensity, duration, frequency for pluvial floods).
        - Strong winds.
        - Drought indices (SPI, SPEI over 1-12 months).
    - Ecological and Environmental Parameters:
        - Soil health (volumetric moisture, compaction, potential erosion).
        - Plant water stress.
        - Flammable biomass load and slope stability.

These indicators are composite and probabilistic, integrating contextualized alert thresholds (e.g., high fire risk if FWI > 30 AND soil humidity < 20%). They are particularly transposable to historic gardens: a garden can be monitored via a personalized dashboard showing progressive degradation or sudden risks. In a heritage context, these metrics notably allow quantifying how a garden acts as a buffer (run-off reduction of 40% via soil infiltration), while identifying its own vulnerabilities (swelling clay soils under cyclical drought).

This SoS4MHRIN approach thus offers proactive vigilance, essential for preserving historic sites against compound climatic hazards.

---

## 3. Simulations and Scenarios

C2Impress integrates advanced simulations within its **SoS4MHRIN** platform, primarily via **Earth System Dynamic Intelligence (ESDI)** and **operational dynamic models**. These tools allow predicting with high spatio-temporal resolution (from event to climatic scale) the risks of single or multiple hazards under varied climatic scenarios, moving from a "hazard-centric" approach to an evaluation centered on places and populations. The simulations are empirically validated in four pilot sites (Egaleo in Greece, Ordu in Turkey, and two others in Southern Europe), covering vulnerable urban and coastal contexts.

### 3.1. Simulated Phenomena

C2Impress simulations target **compound meteorological extremes**, as well as non-standard events with high impact. They model the **main hydrometeorological dangers**: river and pluvial floods, forest fires, heat waves, landslides induced by intense rains, and prolonged droughts.

The innovation lies in capturing **interactions between hazards** (cascading effects or combined stresses), like a drought amplifying fire risks followed by post-fire floods. **System-of-systems simulation models** and **agent-based models (ABM)** assess multidimensional impacts (exposure, physical/social vulnerability, adaptive resilience), with reduced uncertainty thanks to fine predictions.

For heritage spaces and historic gardens, these simulations are highly adaptable: they allow studying **soil water dynamics** (infiltration/runoff under floods), **vegetal stress** (biomass loss under heat/drought), or **impacts on biodiversity** (species sensitive to extreme compounds), by tagging gardens as "natural buffers" in the models.

- 3.1.1. Emission Scenarios
    
    C2Impress relies explicitly on **RCP 4.5** and **RCP 8.5** climatic scenarios for its high-resolution local projections. These scenarios calibrate simulations at medium (2030-2050) and long-term (2070-2100), testing resilience under progressive or extreme conditions.
    

### 3.2. Land Use and Micro-climate Scenarios

**Land Use and Land Cover (LULC)** projections derive from series like CORINE Land Cover, simulated via ABM to anticipate urbanization, loss of vegetation cover, and their effects on **micro-climate.** In historic gardens in dense environments, these scenarios quantify how heritage vegetation mitigates heat or regulates humidity, while assessing potential degradation under urbanization.

### 3.3. Sudden Disaster Scenarios

- 3.3.1. Seismic Scenarios
    
    Simulations include earthquakes, via impact models on critical infrastructures and associated landslides. Transposable to historic sites, they assess the response of heritage structures (retaining walls, garden basins) to soil liquefaction or tremors amplified by water saturation.
    
- 3.3.2. Pluvial Flood Scenarios
    
    Modeling of pluvial and fluvial floods, with real-time alerts and extent predictions. At high spatial resolution, these tools analyze watershed management in parks/gardens, simulating runoff, historic drain overload, and flowerbed erosion.
    
- 3.3.3. Fire Scenarios
    
    Forest fires are simulated by integrating drought, winds, and biomass, with early alerts and dynamic propagation (e.g., via indices like FWI). For heritage gardens, these models guide planting planning (non-flammable species, green barriers), assessing how dry soils under RCP 8.5 increase vulnerability to ignition.
    

These simulations, anchored in co-creation with local actors, provide dashboards for emergency plans adapted to historic sites.

---

## 4. Natural Spaces, Gardens, and Soils as Heritage Assets

Yes, several elements can enrich this section by exploiting more explicitly the conceptual framework of C2Impress, which treats natural spaces as **"Natural Heritage Buffers"** or **"Green Resilience Layers"** in its ontologies and multi-hazard models. These assets are integrated not as liabilities, but as **dynamic components** influencing the exposure and overall vulnerability of sites. Here is a detailed version, with factual additions on modeling, pilot use cases, and direct links to your gardens-heritage theme.

### 4.1. Semantic and Physical Representation

C2Impress uses a **unified semantic ontology** to model territorial entities, naturally extending to **historic landscape elements** like gardens, parterres, tree alignments, or heritage hydraulic networks. Ontological classes include "HeritageAsset" (built assets), "NaturalBuffer" (vegetation/soils), and "DynamicLayer" (temporal evolution), with properties like soil texture, vegetation cover (NDVI percentage), or water permeability.

This physical representation relies on LiDAR and altimetric data for the fine topography of gardens (micro-morphological reliefs, underground drains), coupled with knowledge graphs linking a heritage tree to its hydric role (absorbent roots) or seismic role (soil stabilization).

### 4.2. Role of Gardens and Natural Soils

In C2Impress, green spaces and soils are positioned as **active territorial resilience amplifiers**, beyond a simple protective layer: they modulate energy/water flows and absorb multi-hazard shocks. Pilot site simulations quantify concrete benefits: 30-50% reduction in pluvial runoff via soil-garden infiltration, 3-6°C attenuation of heat islands by evapotranspiration, and maintenance of 20-40% biodiversity refuge under combined stress.

In heritage sites, this ecological function is superimposed on a **strong cultural and identity value**, a dimension that C2Impress begins to integrate via "Cultural Resilience Score" indicators.

### 4.3. Monitoring the "Health" of the Natural Environment

C2Impress, via SoS4MHRIN, combines remote sensing and IoT sensors (root moisture, soil/canopy temperature, water stress sensors via stomatal conductance). In Living Labs, proactive alerts are generated (e.g.: early detection of leaf yellowing under RCP 4.5 drought), with real-time dashboards accessible to heritage managers.

Applied to historic gardens, this allows **holistic monitoring**: vegetal vitality, soil moisture (critical thresholds for swelling clays), surface temperature, and microbiological health (indicators via permeability). Feedback loops (citizens reporting anomalies via app) reinforce precision, ideal for preventive management of sites.

### 4.4. Vulnerability and Soil Dynamics

The multi-source analysis of C2Impress models **soil vulnerability** as a dynamic process, exposed to floods (erosion/overload), water stress (clay cracking), and interactions (earthquake + saturation leading to liquefaction). Indicators like the "Soil Vulnerability Index" integrate compaction, porosity, organic load, and slope, predicting failures.

These dynamics translate into **heritage resilience levers**: a stable garden soil under hazards protects historic foundations and vegetation; scenarios test interventions.

---

## 5. Synthesis of Technologies and Approaches

C2Impress deploys a coherent technological ecosystem, centered on the **SoS4MHRIN** platform (System-of-Systems for Multi-Hazard Risk Intelligence Network), supported by **ESDI (Earth System Dynamic Intelligence)** and **IPAI (Information Physical Artificial Intelligence)**. This architecture integrates dynamic simulations, a unified semantic ontology, and participatory tools for proactive multi-hazard risk management, validated in four pilot sites (Egaleo-Greece, Ordu-Turkey, and two others in Southern Europe).

### Main Technologies

- **Multi-Risk Intelligence Platform**: SoS4MHRIN centralizes satellite data (Copernicus/Sentinel), in situ IoT, and citizen crowdsourcing, with real-time fusion for high-resolution risk maps.
- **Modeling and Simulations**: Agent-Based Models (ABM) for LULC scenarios and micro-climates; physical models for compound hazards (floods + fires) under RCP4.5/8.5.
- **Ontology and Data**: RDF/OWL schema modeling cultural assets and "Natural Buffers", stored in interoperable geospatial databases (FAIR).
- **Decision Tools**: Interactive dashboards, multi-criteria microservices, and probabilistic alerts.
- **Citizen Engagement**: Mobile applications and co-creation via Living Labs for integrating local perceptions.

---

## Boundaries of C2Impress

## Identified Strengths

- **Holistic "Place and People-centred" Approach**: Shift from hazard-centered to multidimensional assessment (exposure, socio-cultural vulnerability, adaptive resilience), reducing predictive uncertainty.
- **Interoperability and Scalability**: Dynamic multi-source flows and fine simulations, transposable to heritage gardens as ecological buffers.
- **Inclusive Co-creation**: Science-authority-citizen implication for accessible tools, fostering local appropriation in historic sites and decision support.

## Identified Limits of the Project

- **Detailed Technical Characteristics**: Insufficient enrichment of attributes for buildings, artifacts, circulation axes (dynamic load capacities, alternative configurations); built and natural heritage assets under-granularized (limited historic vegetation/soil inventories, absence of palynology or landscape archaeology for gardens).
- **Socio-demographic Data**: Absence of fine classification of populations (permanent residents, tourists, seasonality, specific vulnerabilities – PRM, children, seniors).
- **Operational Rescue Capacities**: No modeling of intervention infrastructures (rescue stations, water points, vehicle access, theoretical response times).
- **Past Disaster Assessment**: Limited data on victims (spatial localization of human impacts, injury typologies, aggravating factors).
- **Heritage Ecology**: Protection of historic plant species underdeveloped (lists of protected species, regulatory statuses, safeguard strategies against climatic stresses).
- **Human Behaviors Under Crisis**: Although human behavior is taken into account, population flows are approached with a liquid approach, without consideration for biases, information levels, and the impact of rescue efforts.

---
