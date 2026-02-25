# Art Status für ATLAS-Projekt

# Einführung

Der vorliegende Stand der Technik schlägt vor, die mögliche Anpassung des ATLAS-Projekts durch die Kopplung der HARIS (arch) und C2Impress (SoS4MHRIN)-Geräte prospektiv zu untersuchen. In dieser Perspektive wäre es ein Umzug von einem einfachen bereicherten Erbe Inventar in eine digitale Umgebung, die sowohl eine Fein Asset-Datenbank als auch mehr Gefahren, partizipatorische und skalierbare Intelligenz integriert. Die Analyse wird das Potenzial dieser Verknüpfung für die Schaffung eines dynamischen digitalen Erbes Twin erforschen, der in der Lage ist, prädiktive Ansätze für Verwundbarkeit und Krisenmanagement zu unterstützen.

Zunächst würden die theoretischen Interessen einer solchen Annäherung diskutiert, insbesondere hinsichtlich der Komplementarität zwischen detaillierten Strukturdaten und Umwelt- oder Sozialflüssen. Zweitens würden die Entwicklungsbedürfnisse für die Integration eines Brandsimulators (Soc-SIM-K) und die Modellierung des Evakuierungsverhaltens ermittelt. Schließlich wird besonders auf die Notwendigkeit geachtet, eine einheitliche Ontologie aufzubauen, die auf einer Erweiterung des CIDOC CRM basiert und eine semantische Interoperabilität zwischen den beiden Systemen und die Standardisierung von Risikoindikatoren auf der Ebene des ATLAS-Projekts ermöglicht.

# ARCH study

Das ARCH-Projekt bietet einen integrierten technologischen Rahmen, um die Widerstandsfähigkeit historischer Gebiete zu analysieren, zu überwachen und zu verbessern, indem Informationssysteme, Multi-Hazard-Simulationen und Entscheidungshilfen artikuliert werden.

1. Allgemeine Rahmenbedingungen und Ziele

ARCH (Advancing Resilience of Historic Areas against Climate-based and other Hazards) ist ein H2020-Projekt, das der Widerstandsfähigkeit von Nachbarschaften und historischen Stätten gegenüber Klimagefahren und anderen Naturgefahren gewidmet ist. Es kombiniert das Katastrophenrisikomanagement, die Anpassung des Klimawandels und das Erbemanagement innerhalb eines integrierten Risikomanagementzyklus für historische Gebiete.

Die entwickelten Lösungen umfassen:

- ein risikomanagement methodologischer Rahmen (ARCH Disaster Risk Management Framework) speziell an historische Gebiete angepasst
- eine Reihe von digitalen Werkzeugen: georeferenzierte Informationssysteme (HARIS/THIS), Entscheidungsunterstützungssystem (DSS), Resilienzmessbestand (RMI/RPVT) und Selbstbewertung der Resilienzreife (RAD).

---

• Informationssysteme und Datenmanagement

Â 2.1. HARIS – Historisches Informationssystem

HARIS ist ein historisch-orientiertes geographisches Informationssystem, das auf einer **Service-orientierten** Architektur (SOA) basiert, die georeferenzierte Daten über den historischen und aktuellen Zustand der Kulturgebiete verwaltet. Es verknüpft 2D/3D Geometrie, Materialien, Verwendungen und Umweltkontexte, um Schwachstellenanalysen, Alterungsmodelle und Schadenszenarien zu liefern.

- 2.1.1. Architektur und Datenbank
- Relationshipal GBS (RDBMS):

Spatial- und alphanumerische Daten werden in einer relationalen Datenbank (einschließlich Geometrie, Attribute, Metadaten, Zeitreihen) gespeichert, um Integrität, komplexe Abfragen und Interoperabilität mit GIS-Tools zu gewährleisten.

- SOA und Interoperabilität:

Web-Dienste setzen Daten in Form von Standard-Diensten (WMS/WFS, REST API) aus, wodurch die Wiederverwendung von Komponenten in anderen Plattformen (DSS, Gemeindeportale, Feldanwendungen) erleichtert wird.

- 2.1.2. Datendiagramm

Heritage Assets werden in weite logische Basen strukturiert, die durch eindeutige Kennungen und räumliche Beziehungen miteinander verbunden sind:

1. BASIS BAUGEWERBE
- Inhalt: historische Gebäude, Kunstwerke, Mauern, Infrastruktur, aufgebaute Ensembles, archäologische Strukturen.
- Attribute:
- Geometrie (2D-Polygone, 3D-Modelle, Ebenen/Gesichte);
- Materialien (Stein, Ziegel, Holz, Metall, Mörtel) und mechanische Eigenschaften;
- Funktionen und Verwendungen (Bewohner, Kultur, Verwaltung, Kultur);
- Erhaltungszustand, bekannte Pathologien (Kissen, Haarlifte, Oberflächenveränderungen);
- frühere Interventionen (Restaurantkampagnen, Verstärkungen, Nutzungsänderungen).
2. OBJECT-Basis
- Inhalt: Objekte, einzelne Elemente und Komponenten: Elemente der Architektur (Ecken, Säulen, Skulpturen), historische Stadtmöbel, Kunstwerke in situ, bemerkenswerte Pflanzenstrukturen (isolierte Bäume, historische Hecken, Ausrichtungen), Elemente der Gärten (Fontaine, Statuen, Becken, Pergolas).
- Attribute:
- physikalische Merkmale (Abmessungen, Masse, Materialien, Oberflächenschichtung);
- Standort-Metadaten (Koordinaten, Beziehung zu einem Gebäude oder Garten, Position in 3D-Raum);
- Zustandsdaten und Pathologien;
- Erhaltungsgeschichte (Datum, Arten und Akteure der Interventionen).
3. MASSNAHMEN
- Inhalt: Zeitreihen und Umweltindikatoren (Klima, Luftqualität, Hydraologie, Vibration usw.).
- Quellen: in situ Sensoren (Temperatur, Feuchtigkeit, Vibration, Wasserspiegel), meteorologische Stationen, Satellitendaten, Klimamodelle.
Attribute: Wert, Unsicherheit, keine Zeit, Quelle und Qualität der Messung.

Diese Struktur ermöglicht es jedem Vermögenswert (CONSTRUCTION/OBJECT) spezifische Umweltbedingungen (MEASURE) für gekoppelte Analysen (Alter, Klimarisiken) zuzuordnen.

- 2.1.3. Zugriffs- und Analysewerkzeuge

HARIS wird über drei Hauptschnittstellentypen betrieben, die in die ARCH-Plattform integriert sind:

1. GIS Dashboards
- 2D/3D interaktive Karten mit Vermögenswerten, deren Sicherheitslücke, damit verbundene Gefahren und Umweltmaßnahmen.
- Funktionen: Filterung nach Art der Vermögenswerte, Zeitraum, Grad der Fragilität; Überlagerung von Klimaindikatoren und Szenarien; Export von Ansichten und Schichten für Berichte.
2. Elektronische Bleche
- Detaillierte Blätter pro Anlage (Gebäude, Objekt, Gartenelement) mit Zugriff auf alle Attribute, Metadaten, Interventionsgeschichte und Links zu externen Dokumenten (Plans, Berichte, Fotos, Laserscans).
- Funktionen: kontrolliertes Editieren, Modifizierungsverfolgung, Quellverfolgung.
3. Hohe Präzision 3D-Viewer
- Visualisierung von 3D-Modellen (Photogrammetrie, Laser-Scan, Drohnen), Tauchnavigation in historischen Stätten, Kopplung mit den Attributen von HARIS.
- Die Integration von Computer-Visionsmethoden und Deep Learning ermöglicht die automatische Erkennung von Degradationen (Kisse, Ablösungen, Verlust von Materie) oder morphologische Veränderungen an Punkt- und Orthophotowolken.

HARIS ist somit sowohl ein Analyse-Tool (Vulnerability, Schadensszenarien), ein Simulations-Tool (über DSS-Links) als auch ein Mediation/Vulgalisierungs-Tool für Entscheidungsträger und die Öffentlichkeit.

2,2. DIES – Bedrohungen und Gefahreninformationssystem

DIES ist das Zwillingssystem von HARIS, das sich der Beschreibung und Quantifizierung von Umweltbedrohungen und -gefahren auf unterschiedlichen zeitlichen und räumlichen Skalen widmet. Es bietet georeferenzierte Indikatoren zu Klima- und Umweltbedrohungen, Fütterung von Risikoanalysen und Simulationen in die ARCH-Plattform.

- 2.2.1. Multi-Source Sammlung und Integration

Daten aus:

- historische Archive (Zeitreihen extremer Ereignisse, Überschwemmungen, Dürren, Brände, Erdbeben);
- Echtzeitdaten: urbane Sensornetzwerke (Regenzähler, Wasserstandssensoren, Klimastationen, Luft-/Qualitätsstationen), Struktursensoren, Crowd-Sensing-Netzwerke (Citizen-Signale über Anwendungen, Geolocation-Fotos)
- Klimaprojektionen: SPC-Szenarien, bioklimatische Datensätze, sektorale Projektionen (extreme Wärme, Niederschlag, Dürre)
- Klimadienstleistungen von Copernicus-Diensten (einschließlich CAMS/C3S) für Projektionen unter verschiedenen Szenarien.

Die Daten werden in einer strukturierten Datenbank, die mit Umweltinformationsnormen kompatibel ist, harmonisiert, georeferiert und gespeichert.

- 2.2.2. Schwere Indikatoren

DIESER produziert eine Reihe von Schlüsselthemen für natürliche Stätten und historische Gärten:

1. Bioklimaindikatoren (BIO1–BIO19)
- Beispiele: Jahresdurchschnittstemperatur, jährliche Wärmeamplitude, Saisonalität und Niederschlagskonzentration, feuchteste/trockenste Monatsfällung, Extremmonatstemperaturen.
- Verwendung: Bewertung der Überlebensbedingungen von Pflanzenarten, Identifizierung von Gebieten mit thermischer oder Wasserbelastung und Erprobung von Veränderungen in klimatischen Nischen.
2. Trocken- und Wärmeindizes
- Standardisierter Niederschlags-Evapotranspirationsindex (SPEI) zur Überwachung von Wetter und landwirtschaftlichen Dürren;
- Anzahl der aufeinanderfolgenden Trockentage (CDD), Wärmewelle (Dauer, Intensität, Frequenz), Anzahl der Tage (tropisch);
- Indikatoren der menschlichen thermischen Belastung (Feeling-Temperatur, Composite-Indizes) für historische öffentliche Räume.
3. Feuerrisiko
- Kombination: Dürre (SPEI, CSD), extreme Temperaturen, relative Luftfeuchtigkeit, Wind (wenn vorhanden), Dichte und Art von Brennstoff (Vervegetation, Materialien).
- Erstellung von Karten potentieller ortsweiter Zünd- und Ausbreitungswahrscheinlichkeiten.
4. Überschwemmungsrisiko
- Kreuzung von topographischen Daten, Landnutzung, Sturm und historischen Flutdrainagesysteme, mit Regen- und Wasserstandmessungen.
- Erzeugung von Indikatoren für wahrscheinliche Wassertiefe, Durchflussrate, Tauchdauer, Stagnationsgebiete, insbesondere in historischen städtischen Geweben.
5. Ad-hoc-Klimadienste
- Verwendung von Copernicus-Produkten (CAMS/C3S) zur Erzeugung lokalisierter Klimaszenarien für verschiedene Zeithorizonte (z.B. Wärmewellen in Valencia bis 2100), unter mehreren Emissionsannahmen.
- Erzeugung einer Reihe von eingehenden Klimavariablen für Kultur- und Vegetationseffektmodelle.

Die DIESES fungiert daher als zentrales Projektarchiv der gegenwärtigen und zukünftigen Gefahren, gekoppelt mit HARIS und DSS.

---

Simulationen und Szenarien

Das ARCH-Projekt stützt sich auf ein integriertes Simulationssystem (DSS), um verschiedene Arten von Szenarien zu konstruieren und zu analysieren, Klimaparameter, Landnutzung und extreme Ereignisse zu kombinieren.

### 3.1. Langfristige Klimaszenarien

Diese Simulationen basieren auf den RCP-Emissionstrajektorien (IPCC) und decken mehrere Referenzzeiträume ab: historisch, 2011–2040, 2041–2070, 2071–2100.

- 3.1.1. Emissionsszenarien
- RCP 4.5:

Vorläufiges Stabilisierungssszenario, mit Maßnahmen zur Minderung des Anstiegs der Treibhausgaskonzentrationen.

- RCP 8.5:

Sehr pessimistisches Szenario, das einen hohen und längeren Emissionstrend widerspiegelt, der oft in ARCH gewählt wurde, um die Widerstandsgrenze historischer Stätten zu erkunden.

- 3.1.2. Simulierte Phänomene
1. Wärmewellen
- Dauer (einschließlich Wellen von bis zu ~30 Tagen oder mehr je nach Ort), Intensität (Bereich bis normal, Wärmeindex) und maximale Temperatur erreicht.
- Auswirkungen auf Materialien, Gebrauch und Überleben von Pflanzenarten in historischen Gärten.
2. Drought
- Berechnung der maximalen Anzahl aufeinanderfolgender Trockentage (CDD) und Dürreindizes (z. B. SPEI) mit Deklination für Boden, Vegetation und landwirtschaftliches Erbe.
3. Meeresspiegelanstieg
- Für Pilot-Küstengebiete (z.B. Hamburg), Meeresspiegel-Projektionen und -Überwachungen in Verbindung mit lokaler Morphologie, um das potenzielle Untertauchen historischer Viertel, salziger Einbrüche und Infrastrukturschäden zu bewerten.

3.2. Landnutzungsszenarien und Mikroklima

ARCH simuliert die Wirkung von verschiedenen Mustern der Landnutzung auf städtischen Mikroklima, einschließlich der Bildung von Wärmeinseln um den Kulturerbe.

Die wichtigsten Szenarien sind:

1. Referenzszenario (Current)
- Basierend auf aktuellen Landnutzung (Gebäude, Straße, Vegetation, Wasser) basierend auf Kartendaten und lokalen Beobachtungen.
2. "Grey"-Szenario (moderate Urbanisation)
- schrittweise Verstädterung ungeschützter landwirtschaftlicher Flächen oder Abfallgebiete, erhöhte mineralische Flächen und Gebäude, begrenzte Verringerung der vegetierten Gebiete.
- Ziel: die Erhöhung der lokalen Temperatur und die Verringerung des thermischen Komforts in der Nähe der Eigenschaften des Erbes zu quantifizieren.
3. Schwarzes Szenario (Total Urbanisation)
- Maximale Urbanisierung einschließlich in einem theoretischen Szenario zunächst geschützte Gebiete, ersetzt durch Gebäude oder undurchlässige Oberflächen.
- Verwendung: drücken Sie den maximalen Schutzwert der Vegetation im Vergleich zu dieser extremen, mehr als beschreiben eine plausible Zukunft.
4. Grünes Szenario (Restaurierung/Re-Naturisierung)
- Umwandlung von verlassenen, wasserdichten oder untergebrauchten Flächen in vegetierte Flächen (Parks, Gärten, landwirtschaftliche Flächen) oder grüne/blaue Rahmen.
- Ziel: Schätzung der Kühlgewinne, der Verringerung der Wärmeinseln, der Verbesserung der Wasserinfiltration und der Minderung der Auswirkungen auf das historische Gebäude.

Modelle simulieren Oberflächen- und Lufttemperaturfelder, manchmal gekoppelt mit urbanem Luftstrom oder Strahlungsmodellen, um mikroklimatische Effekte zu quantifizieren.

### 3.3. Szenarien plötzlicher Katastrophen

Diese Szenarien erforschen die Reaktion der Website auf brutale Ereignisse, mit Berechnungen von materiellen und menschlichen Schäden.

- 3.3.1. Seismische Szenarien
1. Historische Ereignisse
- Eine Reihe von dokumentierten Erdbeben (Position, Größe, Tiefe, Fehlermechanismus), um die Reaktion historischer Strukturen auf Ereignisse zu beurteilen, die aufgetreten sind.
2. Benutzerdefinierte Ereignisse
- Der Benutzer gibt verschiedene Parameter (Abbildung, Tiefe, Größe Mw, Fehlerart, Bruchrichtung, Pulsdauer) in der DSS-Schnittstelle an.
- Beschleunigungs- und dynamische Antwortfelder werden auf die historische Struktur projiziert, was eine Schätzung der strukturellen Schäden und potenziellen Verluste (Kosten, Opfer, funktionelle Unverfügbarkeit) ermöglicht.
- 3.3.2. Regenflutszenarien
- Inputs: intensive Regenereignisse (beobachtete oder zukünftige Episoden), urbane Start- und Drainagemodelle, hochauflösende Topographie.
- Exits:
- Wassertiefe und Geschwindigkeitskarten in historischen Straßen;
- Bereiche Akkumulation, Netzüberlauf, Interaktion mit Gebäuden und Infrastruktur;
- Schätzung von Sachschäden (Gebäude, Sammlungen, Straßen) und Folgen für Menschen (Ausstellung, Zugänglichkeit, Evakuierung).

3.4. Feuerszenarien

ARCH implementiert nicht die detaillierte Flammenausbreitungssimulation, sondern bündelt das vorgelagerte Risiko und potenzielle nachgelagerte Schäden.

1. Vorfeuerrisikobewertung
- DIES verbessert die Bedingungen für die Zündung: extreme Hitze Episoden, verlängert trocken-Tage-Serie, geringe Luftfeuchtigkeit, Dichte der brennbaren Vegetation, Wind.
- Karten der Wahrscheinlichkeit der Zündung und der Gefahr des Feuers werden für Gärten, Parks und peri-städtische Gebiete in der Nähe des gebauten Erbes erzeugt.
2. Nachfeuerschätzung des Schadens
- HARIS bietet die Eigenschaften von Materialien (Holz, Stein, Metall, Decken, Zimmerei) und räumliche Konfiguration von Objekten und Konstruktionen.
- Auf dieser Grundlage werden die wahrscheinlichen Verluste im Brandfall (die möglicherweise zerstörten oder stark abgebauten Elemente) geschätzt, ohne den Brandweg im urbanen Raum genau zu modellieren.

---

Naturgebiete, Gärten und Böden als Kulturgüter

ARCH betrachtet Naturgebiete (Garten, Parks, landwirtschaftliche Flächen, Feuchtgebiete) als Kulturgüter in ihrem eigenen Recht, nicht nur eine Dekoration um Denkmäler.

### 4.1. Semantische und physische Darstellung

1. Natürliche Objekte in HARIS
- Jeder signifikante Teil eines Gartens (bemerkenswerter Baum, historische Hecke, massiver, strukturierter Rasen) kann als "Objekt" in der OBJECT-Basis mit seinen physikalischen Eigenschaften (Dimension, geschätztes Alter, Blatttyp) und biologisch (Arten, Gesundheitsstatus) aufgezeichnet werden.
- Im Datenmodell werden die räumlichen und funktionalen Zusammenhänge zwischen diesen Objekten und dem Gebäude (Proximität von Fassaden, Schattierung, Schutz vor Wind) erläutert.
2. Landnutzung
- Landnutzung Karten machen feine Unterschiede: Wälder, Stadtgärten, Ackerland, Wiesen, Feuchtgebiete, unpermeabilisierte Oberflächen, Wasseroberflächen.
- Diese Unterscheidung wird verwendet, um Wärmeabsorption (Albedo, Wärmekapazität, Evapotranspiration) und Wassermanagement (Infiltration, Start, Lagerung) um historische Stätten zu simulieren.

4.2. Die Rolle der "Abschirmung" von natürlichen Gärten und Böden

ARCH ist eines der Projekte, die die Vorteile von Gärten und vegetierten Räumen für die Widerstandsfähigkeit historischer Gebäude explizit quantifizieren.

1. Thermische Regelung
- Modellierung der Kühlwirkung durch Evapotranspiration und Schattierung von Gärten, die Verringerung der Intensität der Wärmeinseln in der Nähe von Denkmälern.
- Bewertung von thermischen Komfortgewinnen, Verringerung der thermischen Ermüdung von Materialien und Verringerung von extremen Zyklen der Expansion/Kontraktion.
2. Regenwassermanagement
- Natürliche Böden sind als Zonen der Absorption/Infiltration mit Parametern der Permeabilität, Lagerung und Oberflächenrauhigkeit dargestellt.
- ARCH simuliert, wie ein Garten oder Park den Fluss verlangsamt, Wasserspiegel in benachbarten Straßen reduziert, die Fundamente historischer Gebäude schützt und die Belastung der Evakuierungsnetze reduziert.

### 4.3. Überwachung der "Gesundheit" der natürlichen Umwelt

Dies schließt Indikatoren ein, die speziell auf die ökologische Gesundheit der natürlichen Gebiete ausgerichtet sind.

1. Vegetationsindizes
- Verwendung von Satellitendaten (z.B. NDVI, EVI) und möglicherweise Drohnendaten zur Überwachung der Vegetationsstärke und -dichte in historischen Gärten und Parks.
- Erfassung von Bereichen des Niedergangs, des Stresss oder der Veränderung der Vegetation, die Risiken (Feuer, Erosion, Erdrutsche) erhöhen können.
2. Wasserbedarf und Wasserbelastung
- Berechnung des Gleichgewichts zwischen potenzieller Evapotranspiration und Niederschlag, ergänzt durch Informationen über Bewässerungspraktiken, wenn sie existieren.
- Identifizierung von Zeiten, in denen ein historischer Garten in eine Zone von Wasserstress eintritt, mit Warnung über alte Arten besonders verletzlich oder schwer zu ersetzen.
3. Agroklimatische Indikatoren
- Für landwirtschaftliche Kulturgüter (historische Weinberge, traditionelle Kulturen), gefolgt von Wachstumsperioden, Risiken von spätem Einfrieren, Frühwärme oder Hitzewellen in sensiblen Phasen (Flüssig, Reife).
- Diese Indikatoren dienen der Erhaltung der Produktion und des damit verbundenen immateriellen Erbes (Wissen, Kulturlandschaften).

4.4. Bodenverwundbarkeit und Dynamik

ARCH ist nicht auf sichtbare Oberflächenelemente beschränkt, sondern berücksichtigt die Struktur und Dynamik der zugrunde liegenden Böden.

1. Geotechnische Mikrozonierung
- Studie über die Zusammensetzung (Clays, Silts, Sande, Felsen), Heterogenität und Wasserbedingungen von Gärten und Bauflächen.
- Identifizierung von Gebieten, die möglicherweise Erdrutsche, Differentialsiedlungen oder lokale Verstärkung von seismischen Bewegungen erfahren.
2. Bodenstruktur-Interaktion
- Analyse der Auswirkungen der Bodentrocknung (bezogen auf wiederkehrende Dürre) auf die aufblasenden Tone, die saisonale Entnahmen und Schwellungen verursachen können.
- Verknüpfung dieser Phänomene mit dem Auftreten von Rissen in Wänden, Verformung von Fundamenten, Destabilisierung von Zäunen und Wänden von historischen Gärten.

---

5. Synthese von Technologien und Ansätzen

Die nachstehende Tabelle enthält die wichtigsten technologischen Komponenten des ARCH-Projekts und deren Rolle.

- Ja. Komponente
...---------------------------------------------------
HARIS-Heritage Geographic Information System (SOA, RDBMS, GIS, 3D)--Speicherung und Zugriff auf Asset- und Condition-Daten, Unterstützung von Schwachstellenanalysen und Schadensszenarien--Active CONSTRUCTION und OBJECT, Umweltmaßnahmen-MEASURE, 2D/3D Geometrien, historische Interventionen---
THES: Bedrohungs- und Gefahreninformationssystem: Bereitstellung aktueller und zukünftiger Klimaindikatoren, hydrologischer und ökologischer Indikatoren: Bioklimaindikatoren, Dürreindizes, Brand- und Überschwemmungsrisiken, Klima-/Kopernikusprognosen
DSS ARCH
RMI / RPVT
RAD Governance Indikatoren, Bereitschaft, Reaktion, Erholung, Asset-Climate-Integration

ARCH vereint diese Module (HARIS, DIESER, DSS und Entscheidungsunterstützungstools), um ein integriertes und umfassendes **digitales Ökosystem* aufzubauen.
eine feine und mehrdimensionale Beschreibung der Standorte
eine präzise Charakterisierung von klimatischen Gefahren und
Durchführung von Szenariosimulationen
und die Entwicklung von Anpassungstrajektorien
wissenschaftlich robust und betriebsbereit.

Gefördert von Horizon 2020 in Höhe von EUR ** 5,98 Mio.***
über 48 Monate (2019-2023) setzt das Projekt seine Pilotlösungen auf 8
emblematische europäische historische Stätten – Istanbul (Hauptpilot),
Rom, Valencia, Hamburg etc. – und stellt alle seine ** Open Source Software Komponenten** (Code, modulare Datenbanken, API, technische Dokumentation) unter
Freie Lizenzen, wodurch die Wiederverwendung und Erweiterung durch andere Institutionen oder Gemeinschaften erleichtert wird.

Die ** konzeptuellen und operativen Ähnlichkeiten* mit dem **ATLAS**-Projekt (im Vergleich zu Zielerbe oder urbaner Widerstandsfähigkeit in einem vergleichbaren Kontext) sind auffällig:

- **Gemeinsame Bedenken*: Verwundbarkeit historischer Gewebe zum Klimawandel
(Wärmeinseln, Dürre, Überschwemmungen), Schutzrolle der
Grüne Kulturgebiete, Notwendigkeit von Entscheidungsinstrumenten
integriert gebaut, Vegetation und Gefahren.
- **Übertragbare technologische Lösungen*:
- Interoperable SOA-Architektur, einfach in bestehende Systeme wie die von ATLAS integriert.
- Reiche und standardisierte HARIS-Datenmodelle (CONSTRUCTION/OBJECT/MEASURE),
direkt wiederverwendbar, um ähnliche Websites zu dokumentieren.
- Pipeline DIES → DSS für Multi-Szenario-Simulation (RCP 4.5/8.5,
Urbanisation "Gris/Black/Green", Erdbeben/Flotten), anwendbar auf
Probleme von ATLAS.
- 3D-Visualisierungstools und GIS-Dashboards, die bereits mit 8 UNESCO-Sitemanagern validiert wurden.

---

ARCH-Projektbeschränkungen

Trotz ihrer erheblichen Fortschritte hat das ARCH-Projekt einige Mängel.
deren Vollständigkeit für die vollständige Verwaltung von
Risiken auf den historischen Stätten. Diese Lücken betreffen sowohl die
reich an beschreibenden Daten und Simulationsfunktionen
dynamisch.

### Anreicherung von beschreibenden Daten

Die feine Darstellung von Standorten über HARIS (Tabellen BASTRUCTION, OBJECT,
MEASURE) bleibt auf mehreren kritischen Dimensionen perfektionierbar:

- ** Detaillierte technische Merkmale**: Anreicherung von Attributen für Gebäude, Artefakte, Zirkulationsachsen (dynamische Tragfähigkeiten, alternative Konfigurationen).
- **Sozial- und demographische Daten*: Mangel an feiner Einordnung der Bevölkerungen (promanente Einwohner, Touristen, Saisonalität, spezifische Schwachstellen – PMR, Kinder, Senioren).
- **Operationskapazitäten der Rettung**: keine Modellierung von Ansprechinfrastrukturen (Notrufstellen, Wasserpunkte, Fahrzeugzugang, theoretische Ansprechzeiten).
- ** Eine Überprüfung der früheren Ansprüche*: begrenzte Daten über die Opfer (Raumort der menschlichen Auswirkungen, Verletzungen, Verschlimmerungsfaktoren).
- **Heritageökologie**: Schutz von unterentwickelten historischen Pflanzenarten (geschützte Artenlisten, Regulierungsstatus, Klimaschutzstrategien).

In der dynamischen Simulation

ARCH zeichnet sich durch Klima-, seismische und hydrologische Szenarien aus, hat aber zwei große Abwesenheiten:

1. **Simulation der Feuervermehrung**: Obwohl dies hervorragende Vorindikatoren bietet (SPEI,
CDD, Anlagenkraft, Zündbedingungen) und HARIS
Details brennbare Materialien (Holz, trockene Vegetation), Projekt
stoppt an den "vor" und "nach" Phasen, ohne die Dynamik zu modellieren
Ausbreitung von Flammen (Vorzugswege, Fortgeschrittene Geschwindigkeiten,
Hot Spots, integrierte Vegetation Interaktion).

Team **Soc-SIM-K** füllt diese Leere mit ihrem
3D Feuermodelle geeignet für dichte, ausbeutebare Stätten
direkt auf bestehenden HARIS-Basis.

2. ** Menschenverhalten in der Krise*: DSS-Simulationen konzentrieren sich auf materielle Schäden, ignorieren menschliche Ströme (panische, Staus, Evakuierungen, Flüchtlingsgebiete). **Soc-SIM-K** entwickelt jedoch realistische Verhaltensweisen (Pedestrianer, Rettungsfahrzeuge, disorientierte Touristen), die perfekt mit den Geometrien und Kapazitäten der HARIS-Verkehrsachsen kompatibel sind.

---

# Study C2Impress

C2Impress ist ein von der Gemeinsamen Forschungsstelle (GFS) koordiniertes Projekt von Horizon Europe (2023–2026) mit mehr als 18 europäischen Partnern. Ziel ist es, einen inklusiven Ko-Erstellungsrahmen zu entwickeln, um das Verständnis, die Bereitschaft und die Reaktion auf mehrere natürliche und sozio-environmentale Gefahren zu verbessern, einschließlich Überschwemmungen, Dürre, Brände und Küstengefahren.

1. Allgemeine Rahmenbedingungen und Ziele

Die Vision von C2Impress basiert auf:

- Vereinigung zwischen Wissenschaft, lokalen Behörden und Bürgern;
- die Verwendung von mehr Gefahrensimulationen und Indikatoren für soziale und kulturelle Auswirkungen;
- Ko-Bau von Entscheidungsinstrumenten zur Stärkung der lokalen Widerstandsfähigkeit.

Die bereitgestellten *Living Labs* werden verwendet, um reproduzierbare Methoden für andere Kulturkontexte, einschließlich historischer Stätten und ihrer Landschaftsumgebungen, zu testen.

---

• Informationssysteme und Datenmanagement

2.1. Informationssystem

- 2.1.1. Architektur und Datenbank

Das zentrale System von C2Impress basiert auf einer verteilten und interoperablen Architektur, entsprechend den FAIR-Prinzipien (Findable, Accessible, Interoperable, Reusable). Es enthält räumlich-temporale (SIG) Daten, Feldbeobachtungen und Modellierungsergebnisse.

Eine geospatiale Basis (PostSIG) ermöglicht die Kreuzung von physikalischen, menschlichen und kulturellen Indikatoren auf verschiedenen Ebenen (Gebäude, Nachbarschaft, Wassersched).

- 2.1.2. Datendiagramm

Obwohl das Projekt in erster Linie auf die städtische Widerstandsfähigkeit ausgerichtet ist, führt C2Impress das Konzept des kulturellen Eigentums als sensible Elemente des Territoriums ein, in die Schichten der Verwundbarkeit integriert. Kulturgüter werden nach ihrem Wert, ihrer Verwendung und ihrer Gefährdung klassifiziert.

Für Transpositionszwecke könnte ein auf historische Gärten angewandtes Erbe-Datensystem dieses Modell annehmen: Anlageneinheiten, hydraulische Strukturen, Topographie, Böden, symbolische Werte.

- 2.1.3. Zugriffs- und Analysewerkzeuge

Ein Entscheidungs-Scoreboard ermöglicht lokalen Akteuren die Verbreitung von Gefahren oder die Entwicklung von Resilienzindikatoren zu visualisieren. Multikriterien-Analysemodule
Unterstützung der Entwicklungsmöglichkeiten. Diese Instrumente sind für die Aneignung von nicht-Experten-Publikum, ein wichtiger Punkt für die Vermittlung in Kulturstätten, konzipiert.


2.2. Bedrohungen und Gefahreninformationssystem

In C2Impress ist das funktionale Äquivalent von ARCH's DIESES (Threats and Hazard Information System) das SoS4MHRIN (System-of-Systems for Multi-Hazard Risk Intelligence Network).
Diese Infrastruktur zentralisiert und analysiert Daten über mehrere Gefahren (Strecken, Brände, Wärmewellen, Mischdürre) in Echtzeit, wobei die Earth System Dynamic Intelligence (ESDI) für feine und dynamische Vorhersagen von Gefahren mit mehreren Gefahren verwendet wird.

- 2.2.1. Multi-Source Sammlung und Integration

SoS4MHRIN orchestriert eine kontinuierliche und heterogene Sammlung von Daten aus mehreren Skalen und Vektoren:

- Satellitenquellen: Copernicus-Daten, MODIS für Feuer und Oberflächentemperaturen, ergänzt durch Wettervorhersagen.
- In situ und IoT-Sensoren: terrestrische Stationsnetze (Regenometer, Anemometer, nasse Bodensensoren), die in Living Labs (z.B. Thessaloniki, Malta) eingesetzt werden, mit erhöhter Dichte in der Nähe historischer kritischer Standorte.
- Urbane und offene Daten: OpenStreetMap, lokale kritische Infrastrukturbasen, historische Hydrometeo-Archive, bereichert von Bürger Crowdsourcing über
mobile Anwendungen (Signale lokaler Anomalien).
- Sozioökonomische Daten: Demographische Schichten (Bevölkerungsdichte, soziale Verwundbarkeit), integriert, um menschliche Expositionen zu kontextualisieren.

Multi-Source-Integration basiert auf dynamischen Strömen, die diese Daten in naher Echtzeit zusammenführen. Datenfusionsansätze (bayesische Statistiken und automatisches Lernen) erzeugen zusammengesetzte Risikokarten, die je nach Gefahr alle 15-60 Minuten aktualisiert werden. Für Kulturgärten, diese Fähigkeit erlaubt zu folgen
feine Veränderungen des Wassers und der thermischen Bedingungen, die die Böden und die Vegetation beeinflussen, z.B. durchschneidende Satellitenregenfälle mit lokalen Wurzelfeuchtemessungen.

- 2.2.2. Schwere Indikatoren

SoS4MHRIN produziert eine Reihe von standardisierten Bedrohungsindikatoren (0-1), die sowohl extreme klimatische Gefahren als auch ihre ökologischen Auswirkungen abdecken, angepasst an eine mehrstufige Bewertung:

- Primärklimavariablen:
- Extreme Temperaturen und Heat Stress Index.
- Intensiver Niederschlag (Intensität, Dauer, Frequenz für Sturmfluten).
- Starker Wind
- Dürreindizes (SPI, SPEI über 1-12 Monate).
- Umwelt und ökologische Parameter:
- Bodengesundheit (Volumenfeuchte, Verdichtung, potentielle Erosion).
- Pflanzenwasserstress.
- Brennbare Biomassebelastung und Neigungsstabilität.

Diese Indikatoren sind zusammengesetzt und probabilistisch, einschließlich kontextualisierter Warnschwellen (z.B. hohes Brandrisiko, wenn FWI > 30 UND Bodenfeuchte < 20 %). Sie sind besonders auf historische Gärten übertragbar: ein Garten kann über ein benutzerdefiniertes Dashboard überwacht werden, das progressive Degradation oder plötzliche Risiken zeigt. In einem historischen Kontext können diese Metriken verwendet werden, um zu quantifizieren, wie ein Garten als Puffer wirkt (vermindert Abfluss um 40% über Bodeninfiltration), während seine eigenen Schwachstellen (Clay-Boden, die unter zyklischer Dürre aufblasen).

Dieser SoS4MHRIN-Ansatz bietet eine proaktive Wachsamkeit, die für die Erhaltung historischer Stätten gegen klimatische Risiken von wesentlicher Bedeutung ist.

---

Simulationen und Szenarien

C2Impress integriert fortschrittliche Simulationen innerhalb der Plattform **SoS4MHRIN***, hauptsächlich über die ***Earth System Dynamic Intelligence (ESDI)* und **operative dynamische Modelle**.
Diese Tools ermöglichen es, mit hoher Auflösung vorherzusagen
Raumtemporal (von Ereignis bis Klima) Risiken
ein oder mehrere Gefahren unter verschiedenen Klimaszenarien,
aus einem "gefährdten" Ansatz einer Bewertung, die sich auf die
Orte und Populationen. Simulationen werden empirisch validiert
in vier Pilotanlagen (Egaleo in Griechenland, Ordu in der Türkei, und zwei
andere in Südeuropa), die städtische und Küstenkontexte abdecken
verletzlich.

### 3.1. Simulierte Phänomene

Die Simulationen von C2Impress zielen auf das ** Extremkomposit-Wetter* sowie nicht-Standard-Hochschlagsereignisse. Sie modellieren die **major hydrometeorologischen Gefahren*: Fluss- und Regenfluten, Waldbrände, Hitzewellen, Erdrutsche durch starke Regenfälle und Dürre
erweitert.

Innovation ist die Erfassung von ** Gefahren** Interaktionen (Kaskadeneffekte oder kombinierter Stress), wie Dürre, die das Brandrisiko erhöht, gefolgt von Nachfeuerflutungen. ** Systemsimulationsmodelle** und **Agent-basierte Modelle (ABM)** Bewertung multidimensionaler Auswirkungen (Exposure, Schwachstelle)
körperliche/soziale, adaptive Widerstandsfähigkeit), mit reduzierter Unsicherheit durch feine Vorhersagen.

Für historische Kulturgebiete und Gärten sind diese Simulationen sehr anpassungsfähig: Sie ermöglichen die Untersuchung der **Wasserdynamik von Böden** (Infiltration/Flut), **Pflanzenbelastung** (Verlust von Biomasse unter Wärme/Trockenheit) oder ** Auswirkungen auf die Biodiversität** (spezielle Verbindungen empfindliche Arten), indem Gärten als "natürliche Puffer" in Modellen markiert werden.

- 3.1.1. Emissionsszenarien

C2Impress basiert explizit auf Klimaszenarien **RCP 4.5* und **RCP 8,5*** für seine lokalen hochauflösenden Projektionen. Diese Szenarien kalibrieren Simulationen mit mittel (2030-2050) und langfristigen (2070-2100) Horizonten, testen Widerstandsfähigkeit unter progressiven oder extremen Bedingungen.


3.2. Landnutzungsszenarien und Mikroklima

Die Projektionen von** Landnutzung (LULC)* stammen aus Serien wie CORINE Land Cover, simuliert über ABM, um Urbanisierung, Verlust von Vegetationsbedeckung und ihre Auswirkungen auf **Mikroklima zu antizipieren.** In historischen Gärten in dichten Umgebungen klären diese Szenarien, wie die Vegetation des Erbes die Wärme abmildert oder Feuchtigkeit reguliert, während sie einen möglichen Abbau unter Urbanisierung beurteilt.

### 3.3. Szenarien plötzlicher Katastrophen

- 3.3.1. Seismische Szenarien

Simulationen umfassen Erdbeben, über Schlagmodelle auf kritische Infrastruktur und damit verbundene Erdrutsche. Übertragbar auf historische Stätten, sie beurteilen die Reaktion der Kulturstrukturen (Stützwände, Gartenbecken) auf die Verflüssigung von Böden oder Tremors durch Wassersättigung verstärkt.

- 3.3.2. Regenflutszenarien

Modellierung von Sturm- und Flussfluten, mit Echtzeitwarnungen und Ausmaßvorhersagen. Bei hoher räumlicher Auflösung analysieren diese Werkzeuge das Wasserschlammmanagement in Parks/Garten, simulieren Abfluss, historische Abflussüberlastung und Bodenerosion.

- 3.3.3. Feuerszenarien

Waldbrände werden simuliert, indem Dürre, Winde und Biomasse mit Frühwarnung und dynamischer Ausbreitung (z.B. über Indizes wie FWI) integriert werden. Für Kulturgärten führen diese Modelle die Pflanzenplanung (nicht entzündliche Arten, grüne Barrieren) durch und bewerten, wie trockene Böden unter SPC 8.5 die Verwundbarkeit des Brennens erhöhen.


Diese Simulationen, in einer Ko-Kreation mit lokalen Akteuren verankert,
Dashboards für Kontingenzpläne, angepasst an
historische Stätten.

---

Naturgebiete, Gärten und Böden als Kulturgüter

Ja.
mehrere Elemente können diesen Abschnitt bereichern, indem mehr
explizit den konzeptionellen Rahmen von C2Impress, der sich mit Räumen beschäftigt
natur wie **"Natural Heritage Buffers"* oder **"Green Resilience Layers"* in seinen Ontologien und Multi-Aalean-Modellen. Diese Vermögenswerte sind nicht als Verbindlichkeiten, sondern als **dynamische Komponenten**
die Exposition und die Gesamtanfälligkeit der Standorte beeinflussen. Hier
eine detaillierte Version, mit sachlichen Ergänzungen zur Modellierung, Fälle
und direkte Links zu Ihrem Thema
Kulturgärten.

### 4.1. Semantische und physische Darstellung

C2Impress verwendet eine einheitliche semantische **ontologie** zur Modellierung von Gebietskörperschaften, die sich natürlich auf **historische Landschaftselemente* wie Gärten, Betten, Baumausrichtung oder Erbe hydraulische Netzwerke erstrecken. Ontologische Klassen umfassen:
"HeritageAsset" (bebaute Immobilie), "NaturalBuffer" (vegetation/soil) und "DynamicLayer" (temporale Evolution), mit Eigenschaften wie Bodentextur, Vegetation Cover (NDVI Prozent) oder Wasserdurchlässigkeit.

Diese physische Darstellung basiert auf LiDAR- und Höhenmeterdaten für die
feine Topographie von Gärten (mikromorphologische Reliefs, unterirdische Drains), gepaart mit Wissensgraphen, die einen Erbebaum mit seiner Wasserfunktion (absorbierende Wurzeln) oder seismischen (Bodenstabilisierung) verbinden.

4.2. Rolle von Gärten und natürlichen Böden

In C2Impress werden grüne Räume und Böden als **aktive territoriale Widerstandsverstärker** positioniert, über eine einfache Schutzschicht hinaus: sie modulieren Energie/hydrische Flussmittel und absorbieren mehrale Schocks. Die Simulationen der Pilotstandorte quantifizieren konkrete Vorteile: 30-50% Reduzierung des Sturmabflusses durch Boden-Garten-Infiltration, 3-6°C-Abschwächung von Wärmeinseln durch Evapotranspiration und Wartung von 20-40% Biodiversitätszuflucht unter kombiniertem Stress.

Diese ökologische Funktion überschneidet sich in historischen Stätten mit einem ** starken kulturellen Wert und einer Identität**, einer Dimension, die C2Impress über Indikatoren für "Cultural Resilience Score" zu integrieren beginnt.

### 4.3. Überwachung der "Gesundheit" der natürlichen Umwelt

C2Impress, via SoS4MHRIN, kombiniert Remote-Sensing- und IoT-Sensoren (Rotfeuchte, Boden-/Kopplungstemperatur, Wasserspannungssensoren über stomatale Leitfähigkeit). In Living Labs werden proaktive Warnungen erzeugt (z.B. Früherkennung von trockener Blattvergilbung RCP 4.5), wobei Echtzeit-Dashboards für Kulturverwalter zugänglich sind.

Angewendet auf historische Gärten, ermöglicht dies eine ganzheitliche **Überwachung*: Pflanzenlebenskraft, Bodenfeuchte (kritische Schwellen für das Aufblasen von Tonen), Oberflächentemperatur und mikrobiologische Gesundheit (Indikatoren über Permeabilität). Feedback Loops (Citizens Reporting-Anomalien via App) verstärken Genauigkeit, ideal für präventives Standortmanagement.

4.4. Bodenverwundbarkeit und Dynamik

Die Multi-Source-Analyse von C2Impress moduliert die **-Soil-Verwundbarkeit** als dynamischer Prozess, der Überschwemmungen ausgesetzt ist (erosion/overload), Wasserspannung (Clay-Cracking) und Interaktionen (Erdquake + Sättigung zur Verflüssigung). Indikatoren wie der Oil Vulnerability Index integrieren Verdichtung, Porosität, organische Belastung und Steigung, Vorhersage von Fehlern.

Diese Dynamik wird in **Heritage Resilienzzüchter** übersetzt: ein stabiler Gartenboden unter Gefahren schützt historische Fundamente und Vegetation; Szenarien Testeingriffe.

---

5. Synthese von Technologien und Ansätzen

C2Impress stellt ein kohärentes technologisches Ökosystem zur Verfügung, das auf der Plattform **SoS4MHRIN*** (System-of-Systems for Multi-Hazard Risk Intelligence Network), die von**ESDI (Earth System Dynamic Intelligence)* und**IPAI (Information Physical Artificial Intelligence)* unterstützt wird.
Diese Architektur integriert dynamische Simulationen, einheitliche semantische Ontologie und partizipative Werkzeuge für proaktives Multi-Hazard-Risikomanagement, validiert an vier Pilotstandorten (Egaleo-Greece, Ordu-Turkey und zwei weitere in Südeuropa).

### Haupttechnologien

- **Multi-risk Intelligence Platform*: SoS4MHRIN zentralisiert Satellitendaten (Copernicus/Sentinel), IoT in situ und Bürger-Crowdsourcing mit Echtzeit-Verschmelzung für hochauflösende Risikokarten.
- **Modelisierung und Simulationen*: Agent-Based Models (ABM) für LULC und Mikroklimaszenarien; physikalische Modelle für Verbundgefahren (Flotten + Brände) unter RCP4.5/8.5.
- ** Ontologie und Daten*: RDF/OWL-Diagramm zur Modellierung von Kulturgut und "Natural Buffers", in interoperablen Geospatialbasen (FAIR) gespeichert.
- **Entscheidungswerkzeuge*: Interaktive Dashboards, Multi-Kriterien-Mikroservices und Alarme
Probabilisten.
- **Zur Verlobung**: Mobile Anwendungen und Co-Creation über Living Labs zur Integration lokaler Wahrnehmungen.

---

C2Impress Stationen

Kräfte identifiziert

- **Ein ganzheitlicher Ansatz "Ort und menschenzentriert"*: Der Übergang von der risikozentrierten zu einer multidimensionalen Bewertung (Exposition, soziokulturelle Verwundbarkeit, adaptive Resilienz),
Verringerung der vorausschauenden Unsicherheit.
- **Interoperabilität und Skalierbarkeit**: Multi-Source-Dynamikflüsse und Feinsimulationen, die als ökologische Puffer für Kulturgärten zur Verfügung stehen.
- ** Inklusive Co-Creation*: Wissenschafts-Citizen-Autorität Engagement für zugängliche Werkzeuge, Förderung des lokalen Eigentums an historischen Stätten und Entscheidungsunterstützung.
** Menschenverhalten unter Krise**: Das menschliche Verhalten wird von archetypischen Agenten simuliert, die menschliche Vorurteile in Krisenkontexten nachempfunden. Allerdings gibt es wenig Raum für die Darstellung der Informationsebenen und die Auswirkungen der zivilen Erleichterung, Zeit und Kapazität für die Erfindung der Erleichterung.

Projektbeschränkungen identifizieren

- **Details Technische Daten*: Unzureichende Anreicherung von Attributen für Gebäude, Artefakte, Verkehrsachsen (dynamische Tragfähigkeiten, Konfigurationen)
Alternativen); subgranularisiertes Erbe (begrenzte Vegetation/historische Böden, Mangel an Palynologie oder Landschaftsarchäologie für Gärten).
- **Soziodemographische Daten*: Keine feine Klassifizierung von Populationen (promanente Einwohner, Touristen, Saisonalität, spezifische Schwachstellen – PMR, Kinder, Senioren).
- **Operationskapazitäten der Rettung*: Keine Modellierung von Antwortinfrastrukturen (Notrufstellen, Wasserpunkte, Fahrzeugzugang, theoretische Ansprechzeiten).
- ** Eine Überprüfung der früheren Ansprüche*: begrenzte Daten über die Opfer (Raumort der menschlichen Auswirkungen, Verletzungen, Verschlimmerungsfaktoren).
- **Heritageökologie*: Schutz von unterentwickelten historischen Pflanzenarten (Listen)
geschützte Arten, Rechtsstatus, Schutzstrategien
im Gesicht der klimatischen Belastung).

---

# Arches-HER Study

Das Arches-HER-Projekt ist Teil des Arches-Software-Ökosystems, eines vom Getty Conservation Institute (GCI) und dem World Monuments Fund (WMF) entwickelten Immobilieninventar- und Managementsystems.

###1. Allgemeine Rahmenbedingungen und Ziele

- Arches ist eine "offene Quelle" Web GIS, Standard, für die Inventur und Verwaltung von Immobilien (archäologische Stätten, Gebäude, Kulturlandschaften, Kultur-Sets).
- Die strategischen Ziele sind: Verbesserung des Datenmanagements für die Erhaltung, breite Annahme im Erbesektor und Anerkennung als Referenzsystem für die standardisierte Bestandsdatenverwaltung.
- Arches-HER kann daher als Deklination für Historic interpretiert werden
Umweltrekorde: ein Rahmen für die Strukturierung, Dokumentation und Nutzung von territorialen Erbe-Daten (Stadt, Region, Staat), um Planung, Folgenabschätzung und Risikomanagement zu informieren.

---

• Informationssysteme und Datenmanagement

2.1. Informationssystem

- 2.1.1. Architektur und Datenbank

Arches implementiert eine auf einer PostgreSQL/PostGIS-Datenbank zentrierte Corporate Web-Architektur für räumliche und relationale Daten, angereichert mit einem semantischen Diagramm über die SPARQL-Abfrage-Engine (Arches verwendet oft Apache Jena oder eine integrierte Tripelstore RDF-Schicht).

- ** Erweiterung der Ontologie* : Basierend auf CIDOC CRM als Basis-Onlogie, Arches erweitert das Modell mit Konzepten, die für das Immobilienerbe (z.B. HER-spezifische Erweiterungen für Ressourcen wie "Historic Assets", räumliche Beziehungen, Zustand Workflows Bewertung). Das GitHub-Repository "archesproject/cido-crm-ontology" umfasst "arches crmEnhances.xml" zur Modellerhaltung von Ereignissen, Bedrohungen und lokalen Akteuren, um die semantische Interoperabilität zu gewährleisten.
- ** Kein integriertes Simulationssystem*: Keine native Implementierung dynamischer Simulationen (RCP, Hydralogie usw.); Arches ist auf den Import von Ergebnissen in Form von PostGIS- oder RDF-Schichten beschränkt (z.B. Cross-Wetter-Risiko-Raster mit Erbe-Ressourcen über Geo-Requests).
- ** Cross-Datenbanken*: Unterstützt die Multi-Source-Integration über RDF-Mappings für Cross-Inventorys, LIDAR-Daten, externe APIs (z.B. EAMENA, Getty Vocabulary) und offene Datenbanken (OSM, Copernicus). Die "Branchen" und "Graphenzweige" ermöglichen kollaborative Workflows, Crossover ohne Duplikation zu validieren.

Dieser Ansatz priorisiert semantische und räumliche Flexibilität für HER, mit Anpassung über "Ressource-Modelle" (modulare Designs) und gesteuerte Vokabulare.

- 2.1.2. Datendiagramm
- Arches enthält internationale Standards für die Beschreibung des Erbes (Core Data Standard for Archaeological Sites and Monuments, Core Data Index for Historic Buildings), um "minimum wesentliche Daten" zu dokumentieren Erbe Orte.
- Das Konzeptmodell verwendet CIDOC CRM-Onlogie als Referenz auf die Strukturinformation (Aktierer, Ereignisse, Objekte, Orte, Zeiträume).
- Speziell beschreibt ein Arches-basiertes HER jede Erberessource als ein
eine Reihe von verwandten Einrichtungen (Ressourcen, historische Ereignisse, Erhaltungseingriffe, Werte, Bedrohungen, Dokumentarfilme), anstatt nur ein flaches Blatt.
- 2.1.3. Zugriffs- und Analysewerkzeuge
- Das System bietet Web-Beratungsschnittstellen, mit Kartensuche, Filtern, Attributabfragen und Visualisierung von Detailblättern.
- Es soll sowohl Managern (Analyse, Überwachung, Folgenabschätzung) als auch der Allgemeinheit (Sensitivität, Bewertung) mit differenzierten Zugangsprofilen dienen.
- Arches kann durch die GIS-Integration zur Vorbereitung von Entscheidungen (Stadtplanung, Erhaltung, Risikomanagement) genutzt werden, indem sie die Bestandsdaten mit anderen räumlichen Schichten überquert. Aber es gibt kein integriertes Entscheidungsunterstützungstool

2.2. Bedrohungen und Gefahreninformationssystem

- 2.2.1. Multi-Source Sammlung und Integration
- Arches unterstützt die Integration von Daten aus mehreren Quellen: bestehende Erfinder, historische Karten, Satellitenbilder, nationale Datenbanken, Forschungsprojekte usw., mit der Möglichkeit, Daten vor der Integration vor der Verarbeitung und Standardisierung zu verarbeiten.
- Regionale Implementierungen zeigen ihre Verwendung, um gefährdete Erbe aus verschiedenen Quellen zu dokumentieren (bestehende Stätten, Bilder, Archive), in der gleichen Datenbank verwaltet und geteilt.
- Für einen risikoorientierten HER können zusätzliche Schichten berücksichtigt werden: Gefahren (Boden, Erosion, Seismizität), Bodennutzung, Infrastruktur, Klimadaten, in Form von GIS-Schichten oder Links zu anderen Systemen.
- 2.2.2. Schwere Indikatoren
- Arches unterstützt Bedrohungs- und Risikodokumentation durch eigene Felder und Organisationen (drei Kategorien, Intensität, Wahrscheinlichkeit, Integritätseffekte, Managementstatus).
- Das System kann als Grundlage für die Überwachung langfristiger Bedingungen und Bedrohungen genutzt werden, was Indikatoren (Anzahl der Hochrisikostandorte, Entwicklung von Bedrohungen nach Gebieten usw.) ermöglicht, auch wenn der Aufbau von Indikatoren von der Anpassung abhängt
lokal. Eine solche Erweiterung würde die Umsetzung einer gesamten Erweiterung der Darstellung der Aléa erfordern.

---

Simulationen und Szenarien

### 3.1. Simulierte Phänomene

- Ebenso ist Arches keine Simulationsmaschine für physikalische Phänomene (Regen, Start, Feuerausbreitung usw.), sondern ein Rahmen für die Speicherung, Georeferenzierung und Nutzung der Ergebnisse solcher Modelle.
- Diese Art der Speicherung könnte jedoch dazu dienen, die Kommunikationsfähigkeit der Simulationsergebnisse zu verbessern.

---

Naturgebiete, Gärten und Böden als Kulturgüter

### 4.1. Semantische und physische Darstellung

- Arches ermöglicht die Definition von Ressourcen für Kulturlandschaften, historische Gärten und Landschafts-Ensembles, mit Geometrie (rechts-of-way, Grenzen, interne Elemente) und strukturierte Beschreibung.
- Das CIDOC CRM-Modell stellt die Beziehungen zwischen Vegetation, gebauten Strukturen, Management-Interventionen und historischen Ereignissen dar, die an Gärten und Böden als komplexe Kulturgüter angepasst sind.
- Gärten und Böden können als Ressourcen mit spezifischen Werten (ökologische, ästhetische, soziale, symbolische) und Funktionen (Regulation von Mikroklima, Infiltration, Schutz vor Erosion) modelliert werden.
- In einem HER können sie in Klimafolgenabschätzungen oder Urbanisierung in Verbindung mit den Funktionen des Schutzes von Baustellen (z.B. der Rolle von vegetierten Pufferzonen) integriert werden.
- Arches kann wiederholte Beobachtungen (Feldkampagnen, botanische Überwachung, Bodenanalyse, Bildgebung) speichern und so die Überwachung des Zustands von Gärten und Böden unterstützen, sofern Indikatoren (Pflanzenabdeckung, Biodiversität, Feuchtigkeit) durch das Projekt definiert werden.

Es wurde darauf hingewiesen, dass alle diese Möglichkeiten der Darstellung nicht native integriert sind, sondern dass Arches angepasst ist, solche epistemologische Konstruktion einzusetzen.

---

5. Synthese von Technologien und Ansätzen

- Arches-HER basiert auf einer Open Source Web GIS, die nach Traditionsstandards (Core Data Standards, CIDOC CRM) aufgebaut ist und für die Multi-Source-Integration und Bedrohungsverfolgung konzipiert ist.
- Das System wird als Datenbank und Management (Erfinder, Überwachung, Entscheidungsunterstützung) anstatt als Simulationsmotor positioniert; Es Schnittstellen mit externen Tools für Klima-, hydrologische oder seismische Szenarien.
- Seine Stärke liegt in der Fähigkeit, heterogene Informationen (Bauerbe, Landschaften, Bedrohungen, Managementmaßnahmen) zu harmonisieren und zu verknüpfen, um die Erhaltung, Planung und Widerstandsfähigkeit historischer Stätten zu unterstützen.

Identified Project Limits (Arches-HER als Decline ofArches)

- Abhängigkeit von externen Werkzeugen für dynamische Simulation (RCP, Fluten,
Feuer, usw.): Arches verwaltet Ergebnisse, erzeugt sie aber nicht.
- Erforderliche Anstrengungen zur Standardisierung und Reinigung historischer Daten vor der Integration, insbesondere zur Angleichung an kontrollierte Standards und Vokabeln.
- Die Notwendigkeit der Anpassung (Schema, Indikatoren, Schnittstellen), so dass das System wirklich den spezifischen Bedürfnissen eines HER und Risikomanagements entspricht, das technische und organisatorische Ressourcen benötigt.

### Anreicherung von beschreibenden Daten

- Arches bietet einen reichen Rahmen für semantische Beschreibung (Aktoren, Ereignisse, Werte, Bedrohungen), aber dieser Reichtum wird nur genutzt, wenn man in die feine Strukturierung von Daten investiert (Ontologien, kontrollierte Vokabulare, Links zu Quellen).
- Für einen HER ist eine Schlüsselanreicherungsachse die systematische Annotation der Ressourcen durch ihre Schwachstellen, ökologische Funktionen (grüne Räume, Böden) und Anpassungsmaßnahmen, um über die einfache beschreibende Inventar hinauszugehen.

In der dynamischen Simulation

- Das konzipierte Gerät ersetzt keine integrierte Multi-Risiko-Simulationsplattform: Die Verbindungen zwischen Szenarien, zeitlichen Trajektorien und Entscheidungen bleiben über Workflows und externe Werkzeuge eingestellt.
- Eines der Risiken ist es, statisch zu bleiben, anstatt Trajektorien zu integrieren und
dynamische Szenarien (PCR-Szenarien, Änderungen der Bodennutzung, Störungszyklen).

---

# Vorschlag zur Anpassung an das ATLAS-Projekt

Die Integration der Projekte ARCH (HARIS) und C2Impress (SoS4MHRIN) stellt eine große Chance für das ATLAS-Projekt dar. Diese Kopplung ermöglicht es, eine Ultra-Cut-Erbe-Datenbank mit einer dynamischen und partizipatorischen Multi-Aleas-Intelligenz zu verschmelzen.

Hier ist eine strategische Analyse der Interessen dieser Kopplung, der Entwicklungsbedarf für den Brandsimulator und der Weg zu einer einheitlichen Ontologie.

Passende Interessen: Auf einen dynamischen digitalen Zwilling

Die Kopplung zwischen HARIS und C2Impress ermöglicht den Übergang von einem statischen Bestand von Vermögenswerten zu einem prädiktiven Managementsystem.

Dies würde unter anderem Komplementarität Data/Flux schaffen: HARIS bringt strukturelle Präzision (Baumaterialien, Art der Gartenobjekte, 3D-Geometrie), während C2Impress Datenflüsse (Bodenfeuchte, Wasserspannung, Copernicus Satellitendaten) und Simulation in Echtzeit bereitstellt.

Auch Schwachstellenanalysen könnten durch Überschreiten der CONSTRUCTION-Datenbank von HARIS mit dem "Soil Vulnerability Index" von C2Impress durchgeführt werden, man kann vorhersagen, wie Dürre physisch historische Stätten und ihre Grundlagen beeinflusst.

Schließlich würden wir unsere Validierungsfähigkeit durch die "Living Labs" deutlich erhöhen: Der partizipatorische Ansatz von C2Impress ermöglicht die Validierung von HARIS-Schwierigkeitsmodellen durch Crowdsourcing und bereichert die Erbe-Datenbank mit aktualisierten Feldbeobachtungen.

Entwicklung einer einheitlichen Ontologie

Für beide Systeme zu kommunizieren, ist es unerlässlich, eine gemeinsame semantische Schicht zu erstellen, ideal basierend auf einer Erweiterung von CIDOC CRM.
Was entwickelt werden muss:

1. Klassenversöhnung: Erstellen Sie Mappings zwischen den HeritageAsset-Klassen von C2Impress und den CONSTRUCTION/OBJECT-Basis von HARIS.
2. Modellierung des "Natural Heritage Buffer": Entwickeln Sie eine Ontologie, die den Garten nicht mehr als einfache Einrichtung behandelt, sondern als aktive Einheit mit thermischer Beständigkeit und hydraulischer Permeabilität.
3. Standardisierung von Indikatoren: Übernehmen Sie den Ansatz von C2Impress, um heterogene Daten von HARIS zu standardisieren und so Risiken unterschiedlicher Art auf derselben Entscheidungsskala zu vergleichen.

"Plugger" der Soc-SIM-K Feuersimulator

Das ATLAS-Projekt identifiziert das Fehlen einer dynamischen Brandsimulation als wesentliches Kriterium der ARCH. Um den Entwicklungssimulator zu integrieren, sind hier die Brücken zu bauen:

1. Datenfluss erforderlich:

Eingänge (von C2Impress): Retrieve in Echtzeit den Fire Weather Index (FWI), brennbare Biomassebelastung und Windbedingungen.

2. Struktureller Kontext (seit HARIS):

Extrahieren Sie die brennbaren Eigenschaften der Materialien (Holz, Schrein) und die räumliche Konfiguration der Vermögenswerte, um die Ausbreitungswege zu definieren.

3. Für "Plug-in" erforderliche Entwicklungen:

Propagation API Interface: Entwickeln Sie einen Steckverbinder, der die Ausbreitungsvektoren von Soc-SIM-K in die hochpräzisen 3D-Viewer von HARIS injizieren kann.

4. Menschliches Verhaltensmodul:

Verwenden Sie die Agent-Based Models von C2Impress (ABM), um die Evakuierung von Populationen (Touristen, PMRs) durch dokumentierte Verkehrsachsen in HARIS zu simulieren.

5. Feedback zum Schaden:

Erstellen Sie ein Skript, das den Erhaltungsstatus in HARIS nach einer Brandsimulation automatisch aktualisiert, Materialverluste und Bodendegradation geschätzt.

6. Geschätzte Evakuierungsbedingungen:

Detaillierte Klassifizierung von Opferprofilen, Prüfung von Notfalldiensteingriffsszenarien und Simulation potenzieller psychologischer Auswirkungen.


---

# Fazit

Die Anpassung des ATLAS-Projekts durch die HARIS–C2Impress-Kopplung könnte den Weg für einen dynamischen digitalen Zwilling des Erbes ebnen, der in der Lage ist, feines Wissen über Objekte und mehrale Intelligenz in naher Echtzeit zu artikulieren. Diese Versöhnung würde ein beschreibendes Inventar in ein vorausschauendes Managementsystem verwandeln, bei dem strukturelle Verwundbarkeit, Bodendynamik, aktive Rolle von Gärten und menschlichem Verhalten in dieselbe Entscheidungskette integriert werden.

Der Aufbau einer einheitlichen Ontologie, die auf einer Erweiterung des CIDOC CRM basiert, wäre die Schlüsselarchitektur für den Dialog zwischen den Erbe-Basis, den Umweltindikatoren und den Brandsimulatoren, wobei vergleichbare Risiken einer anderen Natur auf einem gemeinsamen Maßstab zu machen. Die Integration von Soc‐SIM‐K als Brandsimulationsmodul, verbunden mit Ausbreitungsmodellen, detaillierten Strukturdaten und evakuationsbasierten Agentenmodellen, würde eines der Hauptdefizite ausfüllen, die in ARCH identifiziert werden, indem eine dynamische und prospektive Dimension hinzugefügt wird.

So konnte sich ATLAS als integrierte Resilienzplattform des Erbes positionieren, in der Living Labs eine kontinuierliche Feedback-Loop-Rolle spielen, Modelle validieren, Daten korrigieren und das Verständnis der psychologischen und sozialen Auswirkungen von Krisen bereichern würde. Diese Vision würde das Erbe nicht nur zu schützenden Objekten machen, sondern ein potenzielles Zentrum für die Gestaltung, Prüfung und Anpassung von Anpassungsstrategien an Klima und extreme Risiken, sowohl auf Standort- als auch auf Territoriumsebene.
