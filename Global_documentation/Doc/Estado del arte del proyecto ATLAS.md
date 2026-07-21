# Art Status for ATLAS Project

Introducción

El presente estado de arte propone examinar prospectivamente la posible adaptación del proyecto ATLAS a través del acoplamiento de los dispositivos HARIS (arch) y C2Impress (SoS4MHRIN). En esta perspectiva, sería un paso de un simple inventario de patrimonio enriquecido a un entorno digital que integra tanto una base de datos de activos finos como una inteligencia multihazard, participativa y escalable. El análisis explorará el potencial de este vínculo para el establecimiento de un gemelo dinámico del patrimonio digital, capaz de apoyar enfoques predictivos de vulnerabilidad y gestión de crisis.

Al principio, se debatirían los intereses teóricos de tal aproximación, en particular en términos de complementariedad entre datos estructurales detallados y flujos ambientales o sociales. En segundo lugar, se determinarían las necesidades de desarrollo para la integración de un simulador de incendios (Soc-SIM-K) y el modelado del comportamiento de evacuación. Por último, se prestaría especial atención a la necesidad de construir una ontología unificada, basada en una extensión de CIDOC CRM, permitiendo la interoperabilidad semántica entre los dos sistemas y la estandarización de indicadores de riesgo a nivel del proyecto ATLAS.

Estudio ARCH

El proyecto ARCH ofrece un marco tecnológico integrado para analizar, supervisar y mejorar la resiliencia de las zonas históricas, articulando sistemas de información, simulaciones de peligros múltiples y herramientas de apoyo a las decisiones.

##1. Marco general y objetivos

ARCH (Advancing Resilience of Historic Areas against Climate-related and other Hazards) es un proyecto H2020 dedicado a la resiliencia de barrios y lugares históricos a los peligros climáticos y otros peligros naturales. Combina la gestión del riesgo de desastres, la adaptación al cambio climático y la gestión del patrimonio dentro de un ciclo integrado de gestión del riesgo para zonas históricas.

Las soluciones desarrolladas incluyen:

- un marco metodológico de gestión del riesgo (Marco de gestión del riesgo de desastres) adaptado específicamente a las esferas históricas
- un conjunto de herramientas digitales: sistemas de información georreferenciados (HARIS/THIS), sistema de apoyo a las decisiones (DSS), inventario de medición de resiliencia (RMI/RPVT) y autoevaluación de la madurez de resistencia (RAD).

-...

##2. Sistemas de información y gestión de datos

## 2.1. HARIS – Sistema de Información de Áreas Históricas

HARIS es un sistema de información geográfica orientada al patrimonio basado en una arquitectura ** orientada al servicio** (SOA), que gestiona datos georreferenciados sobre el estado histórico y actual de las áreas del patrimonio. Enlaza geometría, materiales, usos y contexto ambiental 2D/3D para alimentar análisis de vulnerabilidad, modelos de envejecimiento y escenarios de daño.

- 2.1.1. Arquitectura y base de datos
- GBS relacionales (RDBMS):

Los datos espaciales y alfanuméricos se almacenan en una base de datos relacional (incluyendo geometría, atributos, metadatos, series temporales), garantizando la integridad, consultas complejas e interoperabilidad con herramientas GIS.

- SOA e interoperabilidad:

Los servicios web exponen datos en forma de servicios estándar (WMS/WFS, REST API), facilitando la reutilización de componentes en otras plataformas (DSS, portales municipales, aplicaciones de campo).

- 2.1.2. Diagrama de Datos del Patrimonio

Los activos del patrimonio se estructuran en bases lógicas amplias, interconectadas por identificadores únicos y relaciones espaciales:

1. CONSTRUCCIÓN DE BASE
- Contenido: edificios históricos, obras de arte, paredes, infraestructura, conjuntos construidos, estructuras arqueológicas.
- Atributos:
- geometría (2D poligones, modelos 3D, niveles/focos);
- materiales (piedra, ladrillo, madera, metal, mortero) y propiedades mecánicas;
- funciones y usos (residentes, culturales, administrativos, culturales);
- estado de conservación, patologías conocidas (grietas, alcantarillas, alteraciones superficiales);
- intervenciones pasadas (campañas, refuerzos, cambios de uso).
2. Base OBJECT
- Contenido: objetos, elementos singulares y componentes: elementos de arquitectura (cornios, columnas, esculturas), muebles urbanos históricos, obras de arte in situ, estructuras vegetales notables (árboles aislados, erizos históricos, alineamientos), elementos de jardines (fontaines, estatuas, cuencas, pergolas).
- Atributos:
- características físicas (dimensiones, masa, materiales, estratigrafía superficial);
- metadatos de ubicación (coordinados, relación con un edificio o jardín, posición en el espacio 3D);
- datos y patologías estatales;
- historia de conservación (fechas, tipos y actores de intervenciones).
3. Base de resultados
- Contenido: series temporales e indicadores ambientales (clima, calidad del aire, hidrología, vibración, etc.).
- Fuentes: sensores in situ (temperatura, humedad, vibración, niveles de agua), estaciones meteorológicas, datos satelitales, modelos climáticos.
Atributos: valor, incertidumbre, tiempo, fuente y calidad de medición.

Esta estructura permite que cada activo (CONSTRUCTION/OBJECT) esté asociado con condiciones ambientales específicas (MEASURE) para análisis combinados (edad, riesgos climáticos).

2.1.3 Herramientas de acceso y análisis

HARIS se opera a través de tres tipos principales de interfaz, integrados en la plataforma ARCH:

1. GIS dashboards
- Mapas interactivos 2D/3D que muestran activos, su vulnerabilidad, peligros asociados y medidas ambientales.
- Funciones: filtración por tipo de activo, período, nivel de fragilidad; superposición de indicadores climáticos y escenarios; exportación de puntos de vista y capas para informes.
2. Hojas electrónicas
- Hojas detalladas por activo (construcción, objeto, elemento jardín) que dan acceso a todos los atributos, metadatos, historia de intervención y enlaces a documentos externos (planos, informes, fotos, escáneres láser).
- Funciones: edición controlada, seguimiento de modificaciones, trazabilidad de fuentes.
3. Visores 3D de alta precisión
- Visualización de modelos 3D (fotogrametría, láser-escan, drones), navegación inmersiva en sitios históricos, acoplamiento con los atributos de HARIS.
- La integración de métodos de visión computarizada y Deep Learning permite la detección automática de las degradaciónes (grietas, desprendimientos, pérdida de materia) o cambios morfológicos en las nubes de puntos y ortofoto.

Por lo tanto, HARIS es una herramienta de análisis (vulnerabilidad, escenarios de daños), una herramienta de simulación (a través de enlaces DSS) y una herramienta de mediación/vulgarización para los encargados de la adopción de decisiones y el público.

##2. Esto – Sistema de Información sobre Amenazas y Riesgos

Este es el sistema gemelo de HARIS dedicado a la descripción y cuantificación de amenazas y peligros ambientales, a diferentes escalas temporales y espaciales. Proporciona indicadores georreferenciados sobre amenazas climáticas y ambientales, análisis de riesgos alimentarios y simulaciones en la plataforma ARCH.

- 2.2.1 Recopilación e integración de múltiples recursos

Este agrega datos de:

- archivos históricos (crónica de eventos extremos, inundaciones, sequías, incendios, terremotos);
- datos en tiempo real: redes de sensores urbanos (medidos elevados, sensores de nivel de agua, estaciones climáticas, estaciones de aire/calidad), sensores estructurales, redes de detección de multitudes (señales ciudadanas a través de aplicaciones, fotos de geolocalización)
- proyecciones climáticas: escenarios SPC, conjuntos de datos bioclimáticos, proyecciones sectoriales (calor extremo, precipitación, sequía)
- servicios climáticos derivados de servicios de Copernicus (incluyendo CAMS/C3S) para proyecciones en diferentes escenarios.

Los datos son armonizados, georeferenciados y almacenados en una base de datos estructurada compatible con las normas de información ambiental.

2.2.2 Indicadores de amenazas

Esto produce un conjunto de indicadores temáticos clave para sitios naturales y jardines históricos:

1. Indicadores bioclimáticos (BIO1–BIO19)
- Ejemplos: temperatura media anual, amplitud térmica anual, estacionalidad y concentración de precipitación, precipitación de mes más húmedo y más seco, temperaturas mes extremas.
- Uso: evaluar las condiciones de supervivencia de las especies vegetales, identificar áreas de estrés térmico o acuático y anticipar cambios en nichos climáticos.
2. Índices de sequía y calor
- Índice Estandarizado de Precipitación-Evapotranspiración (SPEI) para la vigilancia del clima y las sequías agrícolas;
- número de días secos consecutivos (CDD), onda de calor (duración, intensidad, frecuencia), número de días (tropical);
- indicadores de estrés térmico humano (temperatura de alimentación, índices compuestos) para espacios públicos históricos.
3. Riesgo de incendios
- Combinación: sequía (SPEI, CSD), temperaturas extremas, humedad relativa, viento (cuando esté disponible), densidad y tipo de combustible (vegetación, materiales).
- Producción de mapas de posibles probabilidades de ignición y propagación en todo el sitio.
4. Riesgo de inundaciones
- Intercambio de datos topográficos, uso de la tierra, tormenta y sistemas históricos de drenaje de inundaciones, con mediciones de lluvia y nivel de agua.
- Producción de indicadores de profundidad probable del agua, caudal, duración de la sumersión, áreas de estancamiento, específicamente en tejidos urbanos históricos.
5. Servicios especiales para el clima
- Uso de productos Copernicus (CAMS/C3S) para generar escenarios climáticos localizados para diferentes horizontes de tiempo (por ejemplo, ondas de calor en Valencia hasta 2100), bajo varias hipótesis de emisión.
- Generación de series de variables climáticas entrantes para modelos de impacto sobre el patrimonio y la vegetación.

Esto funciona como un repositorio central de los peligros presentes y futuros, junto con HARIS y DSS.

-...

##3. Simulaciones y escenarios

El proyecto ARCH se basa en un sistema integrado de simulación (DSS) para construir y analizar diferentes tipos de escenarios, combinando parámetros climáticos, uso de la tierra y eventos extremos.

### 3.1. Escenarios climáticos a largo plazo

Estas simulaciones se basan en las trayectorias de emisión RCP (IPCC) y cubren varios períodos de tiempo de referencia: histórico, 2011-2040, 2041–2070, 2071–2100.

- 3.1.1. Emission scenarios
- PCR 4.5:

Situación intermedia de estabilización, con medidas de mitigación que limitan el aumento de las concentraciones de gases de efecto invernadero.

- RCP 8.5:

Un escenario muy pesimista, que refleja una tendencia de emisión elevada y prolongada, a menudo elegida en ARCH para explorar el límite de resiliencia de los sitios históricos.

- 3.1.2. fenómenos simulados
1. Olas de calor
- Duración (incluyendo olas de hasta ~30 días o más dependiendo del sitio), intensidad (rango a normal, índice de calor) y temperatura máxima alcanzada.
- Efectos sobre materiales, uso del sitio y supervivencia de especies vegetales en jardines históricos.
2. Sequía
- Cálculo del número máximo de días secos consecutivos (CDD) e índices de sequía (como SPEI), con declinación para actividades agrícolas de suelo, vegetación y patrimonio.
3. Aumento del nivel del mar
- Para las zonas costeras piloto (por ejemplo, Hamburgo), las proyecciones del nivel del mar y los surcos junto con la morfología local, para evaluar la posible sumersión de barrios históricos, intrusiones saladas y daños a la infraestructura.

3.2. Situaciones de uso de la tierra y microclima

ARCH simula el efecto de diferentes patrones de uso de la tierra en el microclima urbano, incluyendo la formación de islas de calor alrededor de áreas patrimoniales.

Los principales escenarios son:

1. Escenario de referencia (Actual)
- Basado en el uso actual de la tierra (construcción, carretera, vegetación, agua) basado en datos de mapas y observaciones locales.
2. escenario "Grey" ( urbanización moderada)
- Urbanización gradual de zonas agrícolas desprotegidas o desperdicios, aumento de superficies minerales y construcción, reducción limitada de las zonas vegetas.
- Objetivo: cuantificar el aumento de la temperatura local y la reducción de la comodidad térmica en las proximidades de las propiedades del patrimonio.
3. escenario negro ( urbanización total)
- Urbanización máxima incluyendo, en un escenario teórico, áreas inicialmente protegidas, sustituidas por edificios o superficies impermeables.
- Uso: expresar el máximo valor protector de la vegetación en comparación con este extremo, más que describir un futuro plausible.
4. Green scenario (restoration/re-naturalization)
- Transformación de áreas abandonadas, impermeables o subutilizadas en áreas vegetadas (parques, jardines, áreas agrícolas) o marcos verdes/azul.
- Objetivo: estimar los avances en el enfriamiento, la reducción de las islas de calor, la mejora de la infiltración de agua y la mitigación de impactos en el edificio histórico.

Los modelos simulan campos de temperatura superficial y aérea, a veces unidos a modelos urbanos de flujo de aire o radiación, para cuantificar los efectos microclimáticos.

### 3.3. Escenarios de desastres repentinos

Estos escenarios exploran la respuesta del sitio a eventos brutales, con cálculos de daño material y humano.

- 3.3.1. Escenarios sismológicos
1. Eventos históricos
- Una serie de terremotos documentados (posición, magnitud, profundidad, mecanismo de falla) para evaluar la respuesta de las estructuras históricas a los acontecimientos que han ocurrido.
2. Eventos definidos por el usuario
- El usuario especifica varios parámetros (epicentre, profundidad, magnitud Mw, tipo de falla, dirección de ruptura, duración del pulso) en la interfaz DSS.
- Se proyectan campos de aceleración y respuesta dinámica en la estructura histórica, lo que permite una estimación de los niveles de daño estructural y pérdidas potenciales (costos, víctimas, falta funcional).
- 3.3.2. Situaciones de lluvia
- Entradas: intensas lluvias ( episodios observados o futuros), modelos urbanos de escorrentía y drenaje, topografía de alta resolución.
- Exits:
- mapas de profundidad y velocidad en calles históricas;
- áreas de acumulación, desbordamiento de redes, interacción con edificios e infraestructura;
- estimación de daños materiales (construmentos, colecciones, carreteras) y consecuencias para las personas (exposición, accesibilidad, evacuación).

## 3.4. escenarios de incendios

ARCH no implementa la simulación de propagación de llamas detallada, sino que enmarca el riesgo aguas arriba y el daño potencial aguas abajo.

1. Evaluación del riesgo anterior al fuego
- Esto mejora las condiciones de ignición: episodios de calor extremo, series prolongadas de días secos, baja humedad del combustible, densidad de vegetación inflamable, viento.
- Mapas de probabilidad de encendido y peligro de incendio se generan para jardines, parques y zonas periurbanas cercanas al patrimonio construido.
2. Estimación posterior al fuego de los daños
- HARIS proporciona las propiedades de materiales ( madera, piedra, metal, mantas, carpintería) y configuración espacial de objetos y construcciones.
- Sobre la base de ello, se estiman las pérdidas probables en caso de incendio (elementos que podrían ser destruidos o degradados severamente), sin modelar con precisión el camino del fuego en el espacio urbano.

-...

##4. Espacios naturales, jardines y suelos como patrimonio

ARCH considera que las áreas naturales (gardens, parques, tierras agrícolas asociadas, humedales) son patrimonio propio, no sólo una decoración alrededor de los monumentos.

### 4.1. Representación semántica y física

1. Objetos naturales en HARIS
- Cada componente significativo de un jardín (árbol remarcable, cobertura histórica, césped masivo y estructurado) puede ser registrado como un "objeto" en la base OBJECT, con sus propiedades físicas (dimensiones, edad estimada, tipo de follaje) y biológica (especie, estado de salud).
- Las relaciones espaciales y funcionales entre estos objetos y el edificio (proximidad de fachadas, sombra, protección contra el viento) se explican en el modelo de datos.
2. Uso de la tierra
- Los mapas de uso de la tierra hacen distinciones finas: bosques, jardines urbanos, tierras cultivables, prados, humedales, superficies impermeabilizadas, superficies de agua.
- Esta distinción se utiliza para simular la absorción de calor (albedo, capacidad térmica, evapotranspiración) y la gestión del agua (infiltración, escorrentía, almacenamiento) alrededor de sitios históricos.

4.2. El papel del "shield" de los jardines y suelos naturales

ARCH es uno de los proyectos que cuantifican explícitamente los beneficios de los jardines y espacios vegetados para la resiliencia de edificios históricos.

1. Regulación térmica
- Modelización del efecto de refrigeración por evapotranspiración y sombra de jardines, reduciendo la intensidad de las islas de calor en los alrededores de los monumentos.
- Evaluación de las ganancias de confort térmico, reducción de la fatiga térmica de materiales y reducción de ciclos extremos de expansión/contracción.
2. Gestión del agua de lluvia
- Los suelos naturales están representados como zonas de absorción/infiltración, con parámetros de permeabilidad, almacenamiento y rugosidad superficial.
- ARCH simula cómo un jardín o parque disminuye el flujo, reduce los niveles de agua en las calles adyacentes, protege las bases de edificios históricos y reduce la carga en las redes de evacuación.

### 4.3. Monitoreo de la "salud" del entorno natural

Esto incluye indicadores específicamente dedicados a la salud ecológica de las zonas naturales

1. Índices de vegetación
- Uso de datos satelitales (por ejemplo NDVI, EVI) y posiblemente de drones para monitorear la fuerza y densidad de vegetación en jardines y parques históricos.
- Detección de áreas de declive, estrés o cambio de cubierta vegetal que pueden aumentar los riesgos (fuego, erosión, deslizamientos).
2. Necesidades de agua y estrés hídrico
- Cálculo del equilibrio entre posible evapotranspiración y precipitación, complementado por información sobre prácticas de riego cuando existen.
- Identificación de períodos cuando un jardín histórico entra en una zona de estrés hídrico, con alerta sobre especies antiguas particularmente vulnerables o difíciles de reemplazar.
3. Indicadores agroclimáticos
- Para los sitios agrícolas del patrimonio ( viñedos históricos, cultivos tradicionales), seguidos de períodos de crecimiento, riesgos de congelación tardía, olas de calor tempranas o de calor durante fases sensibles (florecimiento, madurez).
- Estos indicadores se utilizan para preservar tanto la producción como el patrimonio inmaterial asociado (conocimiento, paisajes culturales).

4.4. La vulnerabilidad y la dinámica del suelo

ARCH no se limita a elementos visibles superficiales, sino que tiene en cuenta la estructura y dinámica de los suelos subyacentes.

1. Microzona geotécnica
- Estudio de la composición (clays, silts, arenas, rocas), heterogeneidad y condiciones de agua de jardines y zonas edificadas.
- Determinación de zonas que puedan experimentar deslizamientos de tierra, asentamientos diferenciales o amplificación local de movimientos sísmicos.
2. Interacción de la estructura del suelo
- Análisis de los efectos del secado del suelo (relacionados con sequías recurrentes) en las arcillas infladoras, que pueden causar retiros estacionales e inflamación.
- Vincular estos fenómenos con la aparición de grietas en paredes, deformación de fundaciones, desestabilización de cercas y paredes de jardines históricos.

-...

##5. Sintesis de tecnologías y enfoques

En el cuadro que figura a continuación se resumen los principales componentes tecnológicos del proyecto ARCH y su función.

- Sí. Componente
---------
HARIS-Heritage Geographic Information System (SOA, RDBMS, GIS, 3D)--Storage and access to asset and condition data, support to vulnerability analysiss and damage scenarios--Active CONSTRUCTION and OBJECT, environmental measures--MEASURE, 2D/3D geometries, historical interventions--
THES: Threat and hazard information system: provision of current and future climate, hydrological and environmental indicators: bioclimatic indicators, drought indices, fire and flood risks, climate/copernicus projections
DSS ARCH
RMI / RPVT
RAD Indicadores de gobernanza, preparación, respuesta, recuperación, integración de activos-clima

ARCH reúne estos módulos (HARIS, EST, DSS y herramientas de apoyo a las decisiones) para construir un ecosistema **digital integrado y completo**,
permitiendo una descripción fina y multidimensional de los sitios
una caracterización precisa de los riesgos climáticos y
la ejecución de simulaciones de escenario
y el desarrollo de las trayectorias de adaptación
científicamente robusta y operativa.

Financiado por Horizon 2020 a la sintonía de EUR **5,98 millones**
más de 48 meses (2019-2023), el proyecto implementa sus soluciones piloto en 8
emblemáticos sitios históricos europeos – Estambul (pista principal),
Roma, Valencia, Hamburgo, etc. – y pone a disposición todos sus componentes de software de código abierto ** (código, bases de datos modulares, API, documentación técnica) bajo
Licencias gratuitas, facilitando así la reutilización y ampliación por otras instituciones o comunidades.

Las similitudes conceptuales y operacionales ** con el proyecto **ATLAS** (presumed to target heritage or urban resilience in a comparable context) son sorprendentes:

- **Problemas comunes**: vulnerabilidad de los tejidos históricos al cambio climático
(islas de calor, sequías, inundaciones), función protectora
áreas del patrimonio verde, necesidad de instrumentos de adopción de decisiones
integrada, vegetación y peligros.
** Soluciones tecnológicas transferibles**:
- Arquitectura interoperable SOA, fácilmente integrada con sistemas existentes como los de ATLAS.
- Modelos de datos HARIS ricos y estandarizados (CONSTRUCTION/OBJECT/MEASURE),
directamente reutilizable para documentar sitios similares.
- Pipeline EST → DSS para simulación multiescenario (RCP 4.5/8.5,
urbanización "Gris/Black/Green", terremotos/floods), aplicable a
problemas de ATLAS.
- Herramientas de visualización 3D y paneles GIS, ya validados con 8 directores de sitios de la UNESCO.

-...

## Identificación de los Límites del Proyecto ARCH

A pesar de su importante progreso, el proyecto ARCH tiene algunas deficiencias.
de los cuales limitó su integridad para la plena gestión
riesgos en los sitios del patrimonio. Estas deficiencias se refieren tanto a
riqueza de datos descriptivos y capacidades de simulación
dinámico.

## Enriquecimiento de datos descriptivos

La buena representación de los sitios a través de HARIS (tablas CONSTRUCCIÓN, OBJECT,
MEASURE) sigue siendo perfecto en varias dimensiones críticas:

- ** Características técnicas detalladas**: enriquecimiento de atributos para edificios, artefactos, ejes de circulación (capacidades de carga dinamicas, configuraciones alternativas).
- ** Datos sociales y demográficos**: falta de clasificación fina de poblaciones (residentes permanentes, turistas, estacionalidad, vulnerabilidades específicas – PMR, niños, ancianos).
- ** Capacidades operativas de rescate**: no modelar infraestructuras de respuesta (postes de emergencia, puntos de agua, acceso a vehículos, tiempos de respuesta teóricos).
**Un examen de las reclamaciones anteriores**: datos limitados sobre las víctimas (ubicación espacial de los impactos humanos, tipos de lesiones, factores agravantes).
- **Ecología de la Tierra**: protección de especies de plantas históricas subdesarrolladas (listas de especies protegidas, estado regulatorio, estrategias de conservación del estrés climático).

## Deficits in dynamic simulation

ARCH destaca en escenarios climáticos, sísmicos e hidrológicos, pero tiene dos ausencias importantes:

1. **Simulación de la propagación del fuego**: aunque esto proporciona excelentes indicadores preliminares (SPEI,
CDD, carga de combustible vegetal, condiciones de encendido) y HARIS
detalles materiales inflamables ( madera, vegetación seca), proyecto
se detiene en las fases "antes" y "después", sin modelar la dinámica
propagación de llamas (carriles preferenciales, velocidades avanzadas,
puntos calientes, interacción con la vegetación construida).

Equipo **Soc-SIM-K** llena precisamente este vacío con su
Modelos de fuego 3D adecuados para sitios de patrimonio densos y explotables
directamente sobre bases HARIS existentes.

2. **Comportamiento humano en crisis**: Las simulaciones de DSS se centran en los daños materiales, ignorando las corrientes humanas (púnica, congestión, evacuaciones, zonas de refugio). Sin embargo **Soc-SIM-K** desarrolla agentes conductuales realistas (peestrios, vehículos de rescate, turistas desorientados), perfectamente compatibles con las geometrías y capacidades de los ejes de tráfico HARIS.

-...

# Study C2Impress

C2Impress es un proyecto Horizon Europe (2023–2026) coordinado por el Centro Conjunto de Investigación (JRC) y con más de 18 socios europeos. Su objetivo es desarrollar un marco de creación conjunta inclusivo para mejorar la comprensión, la preparación y la respuesta a múltiples riesgos naturales y socioambientales, incluidas inundaciones, sequías, incendios y riesgos costeros.

##1. Marco general y objetivos

La visión de C2Impress se basa en:

- Asociación entre ciencia, autoridades locales y ciudadanos;
- El uso de simulaciones de peligros múltiples e indicadores de impacto social y cultural;
- Coconstrucción de instrumentos de adopción de decisiones para fortalecer la resiliencia local.

Los laboratorios vivos* desplegados se utilizan para probar metodologías reproducibles para otros contextos patrimoniales, incluidos sitios históricos y sus entornos paisajísticos.

-...

##2. Sistemas de información y gestión de datos

## 2.1. Sistema de información

- 2.1.1. Arquitectura y base de datos

El sistema central de C2Impress se basa en una arquitectura distribuida e interoperable, de acuerdo con los principios de FAIR (Inscluible, Accesible, Interoperable, Reutilizable). Incorpora datos espaciales-temporales (SIG), observaciones sobre el terreno y resultados de modelado.

Una base geoespacial (PostSIG) permite el cruce de indicadores físicos, humanos y patrimoniales a diferentes escalas (construcción, barrio, cuenca hidrográfica).

- 2.1.2. Diagrama de Datos del Patrimonio

Aunque el proyecto se centra principalmente en la resiliencia urbana, C2Impress introduce el concepto de propiedad cultural como elementos sensibles del territorio, integrados en las capas de vulnerabilidad. Los activos culturales se clasifican según su valor, uso y exposición a los peligros.

Para fines de transposición, un esquema de datos patrimoniales aplicado a jardines históricos podría tomar este modelo: entidades de planta, estructuras hidráulicas, topografía, suelos, valores simbólicos.

2.1.3 Herramientas de acceso y análisis

Un marcador de decisiones permite a los actores locales visualizar la propagación de los riesgos o la evolución de los indicadores de resiliencia. Módulos de análisis multicriterios
apoyar las opciones de desarrollo. Estas herramientas están diseñadas para la apropiación por públicos no expertos, un punto clave para la mediación en sitios de patrimonio.


##2. Las amenazas y el sistema de información sobre peligros

En C2Impress, el equivalente funcional de ARCH's EST (Threats and Hazard Information System) es el SoS4MHRIN (System-of-Systems for Multi-Hazard Risk Intelligence Network).
Esta infraestructura centraliza y analiza datos sobre múltiples peligros (floods, incendios, olas de calor, sequías compuestas) en tiempo real, utilizando la Inteligencia Dinámica del Sistema Tierra (ESDI) para predicciones finas y dinámicas de peligros múltiples.

- 2.2.1 Recopilación e integración de múltiples recursos

SoS4MHRIN orquesta una colección continua y heterogénea de datos de múltiples escalas y vectores:

- Fuentes satélite: Datos copernicus, MODIS para incendios y temperaturas superficiales, complementados con pronósticos meteorológicos.
- Sensores in situ e IoT: redes terrestres de estaciones (rainometers, anemometers, sensores de suelo húmedo), desplegadas en laboratorios vivos (por ejemplo, Thessaloniki, Malta), con mayor densidad cerca de sitios críticos del patrimonio.
- Datos urbanos y abiertos: OpenStreetMap, bases de infraestructuras críticas locales, archivos históricos de hidrometeo, enriquecidos por crowdsourcing ciudadano
Aplicaciones móviles (signales de anomalías locales).
- Datos socioeconómicos: capas demográficas ( densidad de población, vulnerabilidad social), integradas para contextualizar las exposiciones humanas.

La integración de múltiples fuentes se basa en flujos dinámicos que fusionan estos datos en tiempo casi real. Los enfoques de fusión de datos (estadísticas judías y aprendizaje automático) generan mapas de riesgo compuestos actualizados cada 15-60 minutos dependiendo del peligro. Para los jardines del patrimonio, esta capacidad permite seguir
finos cambios en el agua y las condiciones térmicas que afectan a los suelos y la vegetación, por ejemplo, la intersección de lluvias satelitales con mediciones locales de humedad.

2.2.2 Indicadores de amenazas

SoS4MHRIN produce un conjunto de indicadores de amenaza estandarizados (0-1), que abarcan tanto los peligros climáticos extremos como sus impactos ecológicos, adaptados a una evaluación multiescala:

- Variables de clima primario:
- Temperaturas extremas e índice de estrés de calor.
- Intensos precipitaciones (intensidad, duración, frecuencia para inundaciones de tormenta).
- vientos fuertes
- Índices de sequía (SPI, SPEI durante 1-12 meses).
- Parámetros ambientales y ecológicos:
- Salud del suelo ( humedad del volumen, compactación, posible erosión).
- El estrés del agua vegetal.
- Carga de biomasa inflamable y estabilidad de pendiente.

Estos indicadores son composite y probabilísticos, incorporando umbrales de advertencia contextualizados (por ejemplo, alto riesgo de incendios si FWI  Conf 30 Y humedad del suelo < 20%). Son particularmente transferibles a jardines históricos: un jardín puede ser monitoreado a través de un panel personalizado que muestra degradación progresiva o riesgos repentinos. En un contexto patrimonial, estas métricas se pueden utilizar para cuantificar cómo un jardín actúa como un búfer (corte reducido en un 40% mediante infiltración del suelo), al tiempo que identifica sus propias vulnerabilidades (los suelos grises inflados bajo sequía cíclica).

Este enfoque SoS4MHRIN ofrece vigilancia proactiva, que es esencial para preservar los lugares históricos contra los peligros climáticos complejos.

-...

##3. Simulaciones y escenarios

C2Impress integra simulaciones avanzadas dentro de su plataforma **SoS4MHRIN**, principalmente a través de la inteligencia dinámica del sistema** (ESDI)** y **Modelos dinámicos operativos**.
Estas herramientas permiten predecir con alta resolución
riesgo espacial-temporal (desde suceso a escala climática)
de peligros individuales o múltiples bajo diversos escenarios climáticos,
de un enfoque "centrico de peligro" a una evaluación enfocada en
lugares y poblaciones. Las simulaciones son validadas empíricamente
en cuatro sitios piloto (Egaleo en Grecia, Ordu en Turquía, y dos
en Europa meridional), abarcando contextos urbanos y costeros
vulnerable.

### 3.1. fenómenos simulados

Las simulaciones de C2Impress apuntan al clima compuesto extremo **, así como eventos de alto impacto no estándar. Modelan los peligros hidrometeorológicos más grandes**: inundaciones de ríos y lluvias, incendios forestales, olas de calor, deslizamientos inducidos por lluvias pesadas y sequías
extendido.

La innovación es la captura de ** peligros** interacciones (efectos de cascada o estrés combinado), como la sequía que aumenta el riesgo de incendio seguido de inundaciones posteriores al fuego. **Modelos de simulación de sistemas** y modelos basados en agentes (ABM)** evalúan los impactos multidimensionales (exposición, vulnerabilidad)
física/social, resiliencia adaptativa), con menor incertidumbre debido a finas predicciones.

Para las áreas históricas y jardines, estas simulaciones son altamente adaptables: permiten el estudio de la dinámica de agua ** de los suelos** (infiltración/flocación), ** estrés de planta** (pérdida de biomasa bajo calor / sed), o **impactúa en la biodiversidad** (especie sensible a compuestos extremos), etiquetando los jardines como "abuelos naturales" en los modelos.

- 3.1.1. Emission scenarios

C2Impress se basa explícitamente en escenarios climáticos **RCP 4.5** y **RCP 8.5** para sus proyecciones locales de alta resolución. Estos escenarios calibran simulaciones con horizontes medianos (2030-2050) y a largo plazo (2070-2100), probando resiliencia bajo condiciones progresivas o extremas.


3.2. Situaciones de uso de la tierra y microclima

Las proyecciones del uso de la tierra** (LULC)** derivan de series como la cubierta terrestre CORINE, simulada a través de ABM para anticipar la urbanización, la pérdida de cubierta vegetal y sus efectos en **microclimato.** En jardines históricos en ambientes densos, estos escenarios aclaran cómo la vegetación patrimonial mitiga el calor o regula la humedad, mientras evalúa la degradación potencial bajo la urbanización.

### 3.3. Escenarios de desastres repentinos

- 3.3.1. Escenarios sismológicos

Las simulaciones incluyen terremotos, a través de modelos de impacto sobre infraestructura crítica y deslizamientos asociados. Transponible a sitios históricos, evalúan la respuesta de las estructuras patrimoniales (países de apoyo, cuencas de jardín) a la licuefacción de suelos o temblores amplificados por la saturación del agua.

- 3.3.2. Situaciones de lluvia

Modelización de tormentas y inundaciones fluviales, con advertencias en tiempo real y predicciones de extensión. En alta resolución espacial, estas herramientas analizan la gestión de cuencas hidrográficas en parques/gardens, simulando escorrentía, sobrecarga histórica de drenaje y erosión del suelo.

- 3.3.3 escenarios de incendios

Los incendios forestales se simulan mediante la integración de la sequía, los vientos y la biomasa, con alerta temprana y propagación dinámica (por ejemplo, mediante índices como la ICM). Para los jardines patrimoniales, estos modelos guían la planificación de plantas ( especies no inflamables, barreras verdes), evaluando cómo los suelos secos bajo SPC 8.5 aumentan la vulnerabilidad a la quema.


Estas simulaciones, ancladas en una co-creación con actores locales,
proporcionar paneles para planes de contingencia adaptados
sitios históricos.

-...

##4. Espacios naturales, jardines y suelos como patrimonio

Sí,
varios elementos pueden enriquecer esta sección explotando más
explícitamente el marco conceptual de C2Impress, que trata de espacios
natural como **"Natural Heritage Buffers"** o **"Green Resilience Layers"** en sus ontologías y modelos multi-alean. Estos activos se integran no como pasivos sino como componentes **dinámicos**
afectando la exposición y la vulnerabilidad general del sitio. Aquí.
una versión detallada, con adiciones fácticas sobre modelado, casos
y enlaces directos a su tema
Jardines del patrimonio.

### 4.1. Representación semántica y física

C2Impress utiliza una semántica unificada **ontología** para modelar entidades territoriales, que se extienden naturalmente a ** elementos históricos del paisaje** como jardines, camas, alineamientos de árboles o redes históricas hidráulicas. Las clases ontológicas incluyen:
"HeritageAsset" (propiedad construida), "NaturalBuffer" (vegetación/suelo) y "DynamicLayer" (evolución temporal), con propiedades como textura del suelo, cubierta vegetal (NDVI por ciento) o permeabilidad del agua.

Esta representación física se basa en datos de LiDAR y altímetro para el
topografía fina de jardines (relieves micromorfológicos, drenajes subterráneos), junto con gráficos de conocimiento que unen un árbol patrimonial a su función de agua (raíz absorbente) o sísmica (estabilización del suelo).

4.2. Función de los jardines y los suelos naturales

En C2Impress, los espacios verdes y los suelos están posicionados como amplificadores de resiliencia territorial ** activos**, más allá de una simple capa protectora: modulan flujos energéticos/hídricos y absorben choques multialean. Las simulaciones de los sitios piloto cuantifican los beneficios concretos: reducción del 30-50% en el escorrentía de tormentas mediante infiltración en el suelo, mitigación de 3-6°C de las islas de calor por evapotranspiración, y mantenimiento del refugio de biodiversidad del 20-40% bajo estrés combinado.

En los sitios del patrimonio, esta función ecológica se superpone con un ** fuerte valor e identidad cultural**, una dimensión que C2Impress comienza a integrarse a través de indicadores "Cultural Resilience Score".

### 4.3. Monitoreo de la "salud" del entorno natural

C2Impress, vía SoS4MHRIN, combina sensores de teleobservación e IoT (fluencia de humedad, temperatura de suelo/canopía, sensores de estrés hídrico a través de conductividad estomatal). En Living Labs se generan alertas proactivas (por ejemplo, detección temprana del amarillento de hoja seca RCP 4.5), con tableros de control en tiempo real accesibles a los administradores del patrimonio.

Aplicado a jardines históricos, esto permite una vigilancia holística**: vitalidad vegetal, humedad del suelo (valores críticos para arcillas infladoras), temperatura superficial y salud microbiológica (indicadores por permeabilidad). Los bucles de retroalimentación (ciudadanos que reportan anomalías a través de la aplicación) refuerzan la precisión, ideal para la gestión del sitio preventivo.

4.4. La vulnerabilidad y la dinámica del suelo

El análisis multifunción de C2Impress modula la vulnerabilidad **suelo** como un proceso dinámico, expuesto a inundaciones (erosión/sobrecarga), estrés hídrico (gritación de la cadena) e interacciones (terremoto + saturación que conduce a la licuefacción). Indicadores como el Índice de Vulnerabilidad del Petróleo integran compactación, porosidad, carga orgánica y pendiente, prediciendo fallas.

Estas dinámicas se traducen en criadores de resiliencia hereditaria**: un suelo de jardín estable bajo peligros protege las bases históricas y la vegetación; intervenciones de prueba de escenarios.

-...

##5. Sintesis de tecnologías y enfoques

C2Impress implementa un ecosistema tecnológico coherente, centrado en la plataforma **SoS4MHRIN** (System-of-Systems for Multi-Hazard Risk Intelligence Network), con el apoyo de **ESDI (Earth System Dynamic Intelligence)** y **IPAI (Information Physical Artificial Intelligence)**.
Esta arquitectura integra simulaciones dinámicas, ontología semántica unificada y herramientas participativas para la gestión proactiva del riesgo multihazard, validadas en cuatro sitios piloto (Egaleo-Grecia, Ordu-Turkey y otras dos en el sur de Europa).

## Main technologies

- ** Plataforma de inteligencia de riesgo múltiples**: SoS4MHRIN centraliza los datos de satélite (Copernicus/Sentinel), IoT in situ y crowdsourcing ciudadano, con fusión en tiempo real para tarjetas de riesgo de alta resolución.
- **Modelación y simulaciones**: Modelos basados en agentes (ABM) para escenarios LULC y microclima; modelos físicos para peligros compuestos (floods + incendios) bajo RCP4.5/8.5.
- **Ontología y datos**: RDF/OWL diagrama modelando propiedad cultural y "Natural Buffers", almacenados en bases geoespaciales interoperables (FAIR).
- Herramientas de decisión**: Dashboards interactivos, microservicios multicriterios y alertas
probabilistas.
- *Contratación ciudadana* Aplicaciones móviles y co-creación a través de laboratorios vivos para la integración de las percepciones locales.

-...

## C2Impress Stations

## Forces identified

- **Un enfoque holístico "lugar y centrado en las personas"**: La transición del peligro centrado a una evaluación multidimensional (exposición, vulnerabilidad sociocultural, resiliencia adaptativa),
reducir la incertidumbre predictiva.
- **Interoperabilidad y escalabilidad**: Flujos dinámicos de múltiples fuentes y simulaciones finas, yransposable a los jardines del patrimonio como buffers ecológicos.
* Co-creación inclusiva* Participación científica-ciudadana-autoridad para herramientas accesibles, fomentando la propiedad local en sitios históricos y apoyo a la toma de decisiones.
**Comportamiento humano en crisis**: El comportamiento humano es simulado por agentes arquetípicos, que emula el sesgo humano en contextos de crisis. Sin embargo, hay poco espacio para la representación de los niveles de información y el impacto del socorro civil, el tiempo y la capacidad para la invención del socorro.

## Identifique limitaciones del proyecto

- ** especificaciones técnicas detalladas**: Enriquecimiento insuficiente de atributos para edificios, artefactos, ejes de tráfico (capacidades de carga dinamica, configuraciones)
alternativas); patrimonio sub-granularizado ( vegetación limitada/suelos históricos, falta de palinología o arqueología paisajística para jardines).
* Datos sociodemográficos* No hay buena clasificación de poblaciones (permanentes residentes, turistas, estacionalidad, vulnerabilidades específicas – PMR, niños, ancianos).
* Capacidades de rescate operacionales* No modelado de infraestructuras de respuesta (postes de emergencia, puntos de agua, acceso a vehículos, tiempos de respuesta teóricos).
**Un examen de las reclamaciones anteriores**: datos limitados sobre las víctimas (ubicación espacial de los impactos humanos, tipos de lesiones, factores agravantes).
- **Ecología de la Tierra**: Protección de especies de plantas históricas subdesarrolladas (listas)
especies protegidas, estado regulatorio, estrategias de salvaguardia
en la cara del estrés climático).

-...

# Arches-HER Study

El proyecto Arches-HER forma parte del ecosistema de software Arches, un sistema de inventario y gestión inmobiliaria desarrollado por el Getty Conservation Institute (GCI) y el Fondo Mundial de Monumentos (WMF).

###1. Marco general y objetivos

- Arches es una "fuente abierta" Web GIS, estándar, para el inventario y gestión de bienes raíces (sitios arqueológicos, edificios, paisajes culturales, conjuntos de patrimonio).
- Los objetivos estratégicos son: mejora de la gestión de datos para la conservación, adopción amplia en el sector del patrimonio y reconocimiento como sistema de referencia para la gestión normalizada de datos sobre el patrimonio.
- Arches-HER puede ser interpretado como una declinación dedicada al histórico
Environment Records: a framework for structuring, documenting and exploiting territorial heritage data (city, region, state) to inform planning, impact assessment and risk management.

-...

##2. Sistemas de información y gestión de datos

## 2.1. Sistema de Información

- 2.1.1. Arquitectura y base de datos

Arches implementa una arquitectura web corporativa centrada en una base de datos PostgreSQL/PostGIS para datos espaciales y relacionales, enriquecida con un gráfico semántico a través del motor de consulta SPARQL (Arches a menudo utiliza Apache Jena o una capa RDF integrada).

- **Extensión de ontología** : Basada en CIDOC CRM como ontología básica, Arches extiende el modelo con conceptos específicos para el patrimonio inmobiliario (por ejemplo, extensiones específicas para HER para recursos como "Astos históricos", relaciones espaciales, evaluación de flujos de trabajo de condiciones). El repositorio GitHub "archesproject/cido-crm-ontology" incluye "arches crm potencia.xml" para modelar eventos de conservación, amenazas y actores locales, asegurando la interoperabilidad semántica.
- **Ningún sistema integrado de simulación**: No hay aplicación nativa de simulaciones dinámicas (RCP, hidrología, etc.); Los arcos se limitan a la importación de los resultados en forma de capas PostGIS o RDF (por ejemplo, franjas de riesgo meteorológico cruzadas con recursos patrimoniales a través de geo-requestas).
- ¿Qué? Supports multi-source integration via RDF mappings for cross-inventories legacy, LIDAR data, external APIs (e.g. EAMENA, Getty Vocabulary) and open databases (OSM, Copernicus). Las "marcas" y "secciones gráficas" permiten que los flujos de trabajo colaborativos validen cruces sin duplicación.

Este enfoque prioriza la flexibilidad semántica y espacial para HER, con personalización a través de "modelos de recursos" (diseños modulares) y vocabularios controlados.

- 2.1.2. Diagrama de Datos del Patrimonio
- Arches incorpora estándares internacionales para la descripción del patrimonio (Norma de datos del mineral para sitios y monumentos arqueológicos, Índice de datos básicos para edificios históricos) para identificar "mínimo datos esenciales" para documentar lugares del patrimonio.
- El modelo conceptual utiliza la ontología CRM CIDOC como referencia ontología para estructurar información (actors, events, objects, places, temporalities).
- Específicamente, una HER basada en Arcos describe cada recurso patrimonio como
a set of related entities (resource, historical events, conservation interventions, values, threats, documentation sources), rather than simply a flat sheet.
2.1.3 Herramientas de acceso y análisis
- El sistema ofrece interfaces de consulta web, con búsqueda de mapas, filtros, consultas de atributos y visualización de hojas detalladas.
- Está diseñado para servir a ambos administradores (análisis, monitoreo, evaluación de impactos) y al público en general (sensibilidad, valoración), con perfiles de acceso diferenciados.
- Los arcos se pueden utilizar para la preparación de decisiones (planificación urbana, conservación, gestión de riesgos) cruzando datos del patrimonio con otras capas espaciales, gracias a su integración en el SIG. Pero no hay una herramienta integrada de apoyo a la decisión

##2. Las amenazas y el sistema de información sobre peligros

- 2.2.1 Recopilación e integración de múltiples recursos
- Arches apoya la integración de datos de múltiples fuentes: inventarios existentes, mapas históricos, imágenes satelitales, bases de datos nacionales, proyectos de investigación, etc., con la posibilidad de preprocesar y estandarizar datos antes de la integración.
- Las implementaciones regionales muestran su uso para documentar patrimonios en peligro de extinción de diversas fuentes (sitios existentes, imágenes, archivos), en la misma base de datos gestionados y compartidos.
- Para una HER orientada al riesgo, pueden considerarse capas adicionales: peligros (florar, erosión, sísmica), usos de la tierra, infraestructura, datos climáticos, en forma de capas GIS o enlaces a otros sistemas.
2.2.2 Indicadores de amenazas
- Arches apoya la documentación sobre amenazas y riesgos a través de campos y entidades dedicadas (principales categorías, intensidad, probabilidad, efectos de integridad, estado de gestión).
- El sistema puede ser utilizado como base para monitorear las condiciones y amenazas a largo plazo, permitiendo indicadores (número de sitios de alto riesgo, evolución de amenazas por área, etc.), incluso si la construcción de indicadores depende de la personalización
local. Esa prórroga exigiría la aplicación de toda una ampliación de la representación de la Aléa.

-...

##3. Simulaciones y escenarios

### 3.1. fenómenos simulados

- Del mismo modo, Arches no es un motor de simulación para fenómenos físicos (raina, escorrentía, propagación de incendios, etc.), sino un marco para almacenar, georreferir y explotar los resultados de tales modelos.
- Sin embargo, este tipo de almacenamiento podría utilizarse para mejorar la comunicabilidad de los resultados de simulación.

-...

##4. Espacios naturales, jardines y suelos como patrimonio

### 4.1. Representación semántica y física

- Arches permite definir tipos de recursos para paisajes culturales, jardines históricos y conjuntos paisajísticos, con geometría (derecha, límites, elementos internos) y descripción estructurada.
- El modelo CRM CIDOC representa las relaciones entre vegetación, estructuras construidas, intervenciones de gestión y eventos históricos, que se adaptan a jardines y suelos como entidades patrimoniales complejas.
- Los jardines y suelos se pueden modelar como recursos con valores específicos (ecológicos, estéticos, sociales, simbólicos) y funciones (regulación de microclima, infiltración, protección contra la erosión).
- En una HER, pueden integrarse en evaluaciones del impacto del cambio climático o en la urbanización, junto con las funciones de proteger los sitios construidos (por ejemplo, el papel de las zonas de amortiguación vegetada).
- Los arcos pueden almacenar observaciones repetidas (campañas de campo, monitoreo botánico, análisis del suelo, imágenes) y, por lo tanto, apoyar el monitoreo de la condición de jardines y suelos, siempre que los indicadores (cubierta de planta, biodiversidad, humedad) sean definidos por el proyecto.

Se observó que todas estas posibilidades de representación no están integradas nativamente, pero que Arches está adaptado para desplegar tal construcción epistemológica.

-...

##5. Sintesis de tecnologías y enfoques

- Arches-HER se basa en un SIG web de código abierto estructurado por normas patrimoniales (Normas de datos del código, CIDOC CRM) y diseñado para la integración de múltiples fuentes y el seguimiento de amenazas.
- El sistema se posiciona como base de datos y gestión (inventario, monitoreo, apoyo a la decisión) en lugar de un motor de simulación; Interfiere con herramientas externas para escenarios climáticos, hidrológicos o sísmicos.
- Su fuerza radica en la capacidad de armonizar y vincular la información heterogénea (patrimonio construido, paisajes, amenazas, medidas de gestión) para apoyar la conservación, planificación y resiliencia de los sitios históricos.

## Identified Project Limits (Arches-HER as Decline ofArches)

- Dependencia de herramientas externas para simulación dinámica (RCP, inundaciones,
fuego, etc. Arches gestiona los resultados pero no los genera.
- Necesidad de esfuerzos significativos para estandarizar y limpiar los datos históricos antes de la integración, en particular para ajustarse a normas y vocabularios controlados.
- La necesidad de personalización (schema, indicadores, interfaces) para que el sistema responda realmente a las necesidades específicas de una HER y gestión de riesgos, que requiere recursos técnicos y organizativos.

## Enriquecimiento de datos descriptivos

- Arches ofrece un marco rico para la descripción semántica (acdores, eventos, valores, amenazas), pero esta riqueza se explota sólo si se invierte en la estructuración fina de datos (ontologías, vocabularios controlados, enlaces a fuentes).
- Para una HER, un eje clave de enriquecimiento es la anotación sistemática de recursos por sus vulnerabilidades, funciones ecológicas (espacios verdes, suelos) y medidas de adaptación, para ir más allá del simple inventario descriptivo.

## Deficits in dynamic simulation

- El dispositivo diseñado no reemplaza una plataforma integrada de simulación de riesgo múltiple: los vínculos entre escenarios, trayectorias temporales y decisiones siguen siendo establecidos a través de flujos de trabajo y herramientas externas.
- Uno de los riesgos es permanecer estático en lugar de integrar trayectorias y
escenarios dinámicos (con escenarios PCR, cambios en el uso del suelo, ciclos de perturbación).

-...

# Propuesta para adaptarse al proyecto ATLAS

La integración de los proyectos ARCH (HARIS) y C2Impress (SoS4MHRIN) representa una gran oportunidad para el proyecto ATLAS. Este acoplamiento permite fusionar una base de datos de herencia ultracortada con una inteligencia multi-aléas dinámica y participativa.

Aquí hay un análisis estratégico de los intereses de este acoplamiento, las necesidades de desarrollo para el simulador de incendios y el camino hacia una ontología unificada.

## Intereses de emparejamiento: Hacia un Gemelo Digital Dinámico

El acoplamiento entre HARIS y C2Impress permite la transición de un inventario estático de activos a un sistema de gestión predictiva.

Entre otras cosas, esto crearía complementariedad Data/Flux: HARIS aporta precisión estructural (materiales de construcción, tipo de objetos de jardín, geometría 3D), mientras que C2Impress proporciona flujos de datos (humedad de suelo, estrés hídrico, datos de satélite Copernicus) y simulación en tiempo real.

También se podría realizar análisis de vulnerabilidad cruzando la base de datos CONSTRUCTION de HARIS con el "Índice de vulnerabilidad del suelo" de C2Impress, se puede predecir cómo la sequía afecta físicamente los sitios históricos y sus fundaciones.

Finalmente, aumentaríamos significativamente nuestra capacidad de validación por los "Labs vivientes": El enfoque participativo de C2Impress permite la validación de modelos de vulnerabilidad HARIS a través de crowdsourcing, enriquecendo la base de datos de patrimonio con observaciones actualizadas sobre el terreno.

## Desarrollo de una Ontología Uniforme

Para ambos sistemas de comunicación, es imperativo crear una capa semántica común, basada idealmente en una extensión de CIDOC CRM.
Lo que hay que desarrollar:

1. Reconciliación de clase: Crear mapas entre las clases HeritageAsset de C2Impress y las bases CONSTRUCTION/OBJECT de HARIS.
2. Modelización del "Búfer del Patrimonio Natural": Desarrollar una ontología que ya no trate al jardín como una decoración sencilla, sino como una entidad activa con resistencia térmica y propiedades de permeabilidad hidráulica.
3. Normalización de los indicadores: Adoptar el enfoque de C2Impress para estandarizar datos heterogéneos de HARIS, permitiendo así comparar riesgos de naturaleza diferente en la misma escala de decisiones.

## "Plugger" el simulador de fuego Soc-SIM-K

El proyecto ATLAS identifica la ausencia de simulación dinámica de incendios como un límite importante de ARCH. Para integrar el simulador en desarrollo aquí son los puentes para construir:

1. Flujo de datos requerido:

Entradas (de C2Impress): Recuperar en tiempo real el Índice de Tiempo de Fuego (FWI), carga de biomasa inflamable y condiciones de viento.

2. Contexto estructural (desde HARIS):

Extraiga las propiedades combustibles de los materiales (leña, carpintería) y la configuración espacial de los activos para definir los caminos de propagación.

3. Desarrollos necesarios para "Plug-in":

Propagation API Interface: Desarrollar un conector que pueda inyectar los vectores de propagación de Soc-SIM-K en los visores 3D de alta precisión de HARIS.

4. Módulo de comportamiento humano:

Utilice los modelos basados en agentes de C2Impress (ABM) para simular la evacuación de poblaciones (turistas, PMR) a través de ejes documentados de tráfico en HARIS.

5. Retroalimentación sobre daños:

Crear un script que actualiza automáticamente el estado de conservación en HARIS después de una simulación de incendios, estimando pérdidas materiales y degradación del suelo.

6. Condiciones estimadas de evacuación:

Clasificación detallada de perfiles de víctimas, pruebas de escenarios de intervención de servicios de emergencia y simulación de posibles impactos psicológicos.


-...

Conclusión

En conclusión, la adaptación del proyecto ATLAS por el acoplamiento HARIS-C2Impress podría allanar el camino para un gemelo digital dinámico del patrimonio, capaz de articular el conocimiento fino de los objetos y la inteligencia multialean en tiempo casi real. Esta reconciliación transformaría un inventario descriptivo en un sistema de gestión predictiva, donde la vulnerabilidad estructural, la dinámica del suelo, el papel activo de los jardines y el comportamiento humano se integrarían en la misma cadena de adopción de decisiones.

La construcción de una ontología unificada, basada en una extensión de CIDOC CRM, sería la arquitectura clave para el diálogo entre bases patrimoniales, indicadores ambientales y simuladores de incendios, haciendo al mismo tiempo riesgos comparables de naturaleza diferente a escala común. La integración de Soc‐SIM‐K como módulo de simulación de incendios, conectado a modelos de propagación, datos estructurales detallados y modelos de agentes basados en la evacuación, llenaría uno de los principales déficits identificados en ARCH añadiendo una dimensión dinámica y prospectiva.

Así, ATLAS podría posicionarse como una plataforma integrada de resiliencia del patrimonio, donde los laboratorios vivos desempeñarían un papel continuo de retroalimentación, validando modelos, corrigiendo datos y enriqueciendo la comprensión de los impactos psicológicos y sociales de las crisis. Esta visión haría del patrimonio no sólo un objeto a proteger, sino un posible centro para diseñar, probar y ajustar estrategias de adaptación al clima y los riesgos extremos, tanto a nivel local como territorial.
