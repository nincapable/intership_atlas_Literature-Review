# Art Status für ATLAS-Projekt

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
eine feine und mehrdimensionale Beschreibung historischer Stätten, eine präzise Charakterisierung der klimatischen und natürlichen Gefahren, die als Zukunft, Durchführung von Simulationen verschiedener prospektiver Szenarien und Entwicklung wissenschaftlich robuster und operativer Anpassungs-Trajektorien auftreten.

Gefördert von Horizon 2020 in Höhe von EUR ** 5,98 Mio.***
über 48 Monate (2019-2023) stellt das Projekt seine Pilotlösungen für 8 emblematische europäische historische Stätten – Istanbul (Führungspilot), Rom, Valencia, Hamburg usw. – zur Verfügung und stellt alle seine Open Source Software Komponenten (Code, Modelldatenbanken, API, technische Dokumentation) unter kostenlosen Lizenzen zur Verfügung, wodurch die Wiederverwendung und Erweiterung durch andere Institutionen oder Gemeinschaften erleichtert wird.

Die ** konzeptuellen und operativen Ähnlichkeiten* mit dem **ATLAS**-Projekt (im Vergleich zu Zielerbe oder urbaner Widerstandsfähigkeit in einem vergleichbaren Kontext) sind auffällig:

- **Gemeinsame Bedenken*: Verwundbarkeit von historischen Geweben zum Klimawandel (Wärmeinseln, Dürre, Überschwemmungen), Schutzrolle von Grünflächen des Erbes, Notwendigkeit der Entscheidungshilfe Werkzeuge, die gebaut, Vegetation und Gefahren integrieren.
- **Übertragbare technologische Lösungen*:
- Interoperable SOA-Architektur, einfach in bestehende Systeme wie die von ATLAS integriert.
- Reiche und standardisierte HARIS-Datenmodelle (CONSTRUCTION/OBJECT/MEASURE), direkt wiederverwendbar, um ähnliche Websites zu dokumentieren.
- Pipeline DIES → DSS für Multi-Szenario-Simulation (RCP 4.5/8.5, Urbanisation "Gris/Black/Green", Erdbeben/Flotten), anwendbar auf die Probleme von ATLAS.
- 3D-Visualisierungstools und GIS-Dashboards, die bereits mit 8 UNESCO-Sitemanagern validiert wurden.

---

ARCH-Projektbeschränkungen

Trotz ihrer bedeutenden Fortschritte hat das ARCH-Projekt erhebliche Lücken, die seine Vollständigkeit für ein umfassendes Risikomanagement an Kulturstätten begrenzen. Diese Lücken betreffen sowohl die Fülle von beschreibenden Daten als auch dynamische Simulationsfunktionen.

### Anreicherung von beschreibenden Daten

Die feine Darstellung von Standorten über HARIS (Tabellen BASTRUCTION, OBJECT, MASURE) bleibt auf mehreren kritischen Dimensionen perfekt:

- ** Detaillierte technische Merkmale**: Anreicherung von Attributen für Gebäude, Artefakte, Zirkulationsachsen (dynamische Tragfähigkeiten, alternative Konfigurationen).
- **Sozial- und demographische Daten*: Mangel an feiner Einordnung der Bevölkerungen (promanente Einwohner, Touristen, Saisonalität, spezifische Schwachstellen – PMR, Kinder, Senioren).
- **Operationskapazitäten der Rettung**: keine Modellierung von Ansprechinfrastrukturen (Notrufstellen, Wasserpunkte, Fahrzeugzugang, theoretische Ansprechzeiten).
- ** Eine Überprüfung der früheren Ansprüche*: begrenzte Daten über die Opfer (Raumort der menschlichen Auswirkungen, Verletzungen, Verschlimmerungsfaktoren).
- **Heritageökologie**: Schutz von unterentwickelten historischen Pflanzenarten (geschützte Artenlisten, Regulierungsstatus, Klimaschutzstrategien).

In der dynamischen Simulation

ARCH zeichnet sich durch Klima-, seismische und hydrologische Szenarien aus, hat aber zwei große Abwesenheiten:

1. **Simulation der Feuervermehrung*: Obwohl DIES ausgezeichnete Vorindikatoren (SPEI, CDD, Pflanzenkraft, Zündbedingungen) und HARIS Details brennbare Materialien (Holz, trockene Vegetation) bietet, stoppt das Projekt an den "vor" und "nach" Phasen, ohne die Flammenausbreitungsdynamik zu modellieren (Vorzugswege, Vorschubgeschwindigkeiten, Hot Spots, Bauvegetation Interaktion).

Das Team **Soc-SIM-K** füllt diese Leere mit seinen 3D-Feuermodellen, die an dichte Stätten des Erbes angepasst sind, die direkt auf bestehenden HARIS-Basis genutzt werden können.

2. Das menschliche Verhalten unter der Krise: DSS-Simulationen konzentrieren sich auf materielle Schäden, ignorieren menschliche Ströme (panische, Staus, Evakuierungen, Flüchtlingsgebiete). Soc-SIM-K entwickelt realistische Verhaltensweisen (Pedestrianer, Rettungsfahrzeuge, disorientierte Touristen), perfekt kompatibel mit den Geometrien und Kapazitäten der HARIS Verkehrsachsen.

---

# Study C2Impress

1. Allgemeine Rahmenbedingungen und Ziele

C2Impress ist ein von der Gemeinsamen Forschungsstelle (GFS) koordiniertes Projekt von Horizon Europe (2023–2026) mit mehr als 18 europäischen Partnern. Ziel ist es, einen inklusiven Ko-Erstellungsrahmen zu entwickeln, um das Verständnis, die Bereitschaft und die Reaktion auf mehrere natürliche und sozio-environmentale Gefahren zu verbessern, einschließlich Überschwemmungen, Dürre, Brände und Küstengefahren.

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

Ein Entscheidungs-Scoreboard ermöglicht lokalen Akteuren die Verbreitung von Gefahren oder die Entwicklung von Resilienzindikatoren zu visualisieren. Multi-Kriterien-Analysemodule unterstützen Entwicklungsentscheidungen. Diese Instrumente sind für die Aneignung von nicht-Experten-Publikum, ein wichtiger Punkt für die Vermittlung in Kulturstätten, konzipiert.


2.2. Bedrohungen und Gefahreninformationssystem

In C2Impress ist das funktionale Äquivalent von ARCH's DIESES (Threats and Hazard Information System) das SoS4MHRIN (System-of-Systems for Multi-Hazard Risk Intelligence Network). Diese Infrastruktur zentralisiert und analysiert Daten über mehrere Gefahren (Strecken, Brände, Wärmewellen, Mischdürre) in Echtzeit, wobei die Earth System Dynamic Intelligence (ESDI) für feine und dynamische Vorhersagen von Gefahren mit mehreren Gefahren verwendet wird.

- 2.2.1. Multi-Source Sammlung und Integration

SoS4MHRIN orchestriert eine kontinuierliche und heterogene Sammlung von Daten aus mehreren Skalen und Vektoren:

- Satellitenquellen: Copernicus-Daten, MODIS für Feuer und Oberflächentemperaturen, ergänzt durch Wettervorhersagen.
- In situ und IoT-Sensoren: terrestrische Stationsnetze (Regenometer, Anemometer, nasse Bodensensoren), die in Living Labs (z.B. Thessaloniki, Malta) eingesetzt werden, mit erhöhter Dichte in der Nähe historischer kritischer Standorte.
- Urbane und offene Daten: OpenStreetMap, lokale kritische Infrastrukturbasen, historische Hydrometeo-Archive, bereichert von Bürger Crowdsourcing über
mobile Anwendungen (Signale lokaler Anomalien).
- Sozioökonomische Daten: Demographische Schichten (Bevölkerungsdichte, soziale Verwundbarkeit), integriert, um menschliche Expositionen zu kontextualisieren.

Multi-Source-Integration basiert auf dynamischen Strömen, die diese Daten in naher Echtzeit zusammenführen. Datenfusionsansätze (bayesische Statistiken und automatisches Lernen) erzeugen zusammengesetzte Risikokarten, die je nach Gefahr alle 15-60 Minuten aktualisiert werden. Für Kulturgärten kann diese Kapazität der feinen Entwicklung von Wasser und thermischen Bedingungen folgen, die Böden und Vegetation beeinflussen, zum Beispiel durch Überqueren von Satellitenregen mit lokalen Messungen von Wurzelfeuchte.

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
Diese Werkzeuge prognostizieren mit hoher räumlich-temporaler Auflösung (von Ereignis zu Klimaskala) die Risiken von einzigartigen oder multiplen Gefahren unter verschiedenen Klimaszenarien, die sich von einem "gefährdten" Ansatz zu einer orts- und bevölkerungszentrierten Bewertung bewegen. Die Simulationen werden empirisch an vier Pilotstandorten (Egaleo in Griechenland, Ordu in der Türkei und zwei weitere in Südeuropa) validiert, die schutzbedürftige städtische und Küstenkontexte abdecken.

### 3.1. Simulierte Phänomene

Die Simulationen von C2Impress zielen auf das ** Extremkomposit-Wetter* sowie nicht-Standard-Hochschlagsereignisse. Sie modellieren die wichtigsten **meteorologischen Gefahren*: Fluss- und Regenfluten, Waldbrände, Hitzewellen, Erdrutsche, die durch starke Regenfälle hervorgerufen werden, und verlängerte Dürre.

Innovation ist die Erfassung von ** Gefahren** Interaktionen (Kaskadeneffekte oder kombinierter Stress), wie Dürre, die das Brandrisiko erhöht, gefolgt von Nachfeuerflutungen. ** Systemsimulationsmodelle** und **agent-basierte Modelle (ABM)*** bewerten multidimensionale Auswirkungen (Exposure, körperliche/soziale Verwundbarkeit, adaptive Resilienz), mit reduzierter Unsicherheit durch feine Vorhersagen.

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

Diese Simulationen, die in der Ko-Kreation mit lokalen Akteuren verankert sind, bieten dashboards für Kontingenzpläne an historische Stätten angepasst.

---

Naturgebiete, Gärten und Böden als Kulturgüter

Ja.
Mehrere Elemente können diesen Abschnitt dadurch bereichern, dass der konzeptionelle Rahmen von C2Impress, der natürliche Räume als "Natural Heritage Buffers" oder "Green Resilience Layers" in seinen Ontologien und Multi-alean-Modellen behandelt, explizit genutzt wird. Diese Vermögenswerte sind nicht als Verbindlichkeiten integriert, sondern als dynamische Komponenten, die die Exposition und die gesamte Standortverwundbarkeit beeinflussen. Hier ist eine detaillierte Version, mit sachlichen Ergänzungen auf Modellierung, Pilot Nutzungsfälle und direkte Links zu Ihrem Garten-Heritage Thema.

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
- **Entscheidungswerkzeuge*: Interaktive Dashboards, Multi-Kriterien-Mikroservices und probabilistische Alarme.
- **Zur Verlobung**: Mobile Anwendungen und Co-Creation über Living Labs zur Integration lokaler Wahrnehmungen.

---

C2Impress Stationen

Kräfte identifiziert

- **Ein ganzheitlicher Ansatz "Ort und menschenzentriert"*: Die Verschiebung von der Gefahrenzentriert auf eine multidimensionale Bewertung (exposure, sozio-kulturelle Verwundbarkeit, adaptive Resilienz), die Vorhersageunsicherheit reduziert.
- **Interoperabilität und Skalierbarkeit**: Multi-Source-Dynamikflüsse und Feinsimulationen, die als ökologische Puffer für Kulturgärten zur Verfügung stehen.
- ** Inklusive Co-Creation*: Wissenschafts-Citizen-Autorität Engagement für zugängliche Werkzeuge, Förderung des lokalen Eigentums an historischen Stätten und Entscheidungsunterstützung.

Projektbeschränkungen identifizieren

- **Details Technische Daten*: Unzureichende Anreicherung von Attributen für Gebäude, Artefakte, Zirkulationsachsen (dynamische Tragfähigkeiten, alternative Konfigurationen); subgranularisiertes Erbe (begrenzte Vegetation/historische Böden, Mangel an Palynologie oder Landschaftsarchäologie für Gärten).
- **Soziodemographische Daten*: Keine feine Klassifizierung von Populationen (promanente Einwohner, Touristen, Saisonalität, spezifische Schwachstellen – PMR, Kinder, Senioren).
- **Operationskapazitäten der Rettung*: Keine Modellierung von Antwortinfrastrukturen (Notrufstellen, Wasserpunkte, Fahrzeugzugang, theoretische Ansprechzeiten).
- ** Eine Überprüfung der früheren Ansprüche*: begrenzte Daten über die Opfer (Raumort der menschlichen Auswirkungen, Verletzungen, Verschlimmerungsfaktoren).
- **Heritageökologie*: Schutz von unterentwickelten historischen Pflanzenarten (gelistete geschützte Arten, regulatorischer Status, Klimaschutzstrategien).
** Menschenverhalten unter Krise**: Obwohl das menschliche Verhalten berücksichtigt wird, werden die Bevölkerungsströme mit einem flüssigen Ansatz behandelt, unabhängig von Bias, Informationsniveau und der Wirkung der Entlastung.

---
