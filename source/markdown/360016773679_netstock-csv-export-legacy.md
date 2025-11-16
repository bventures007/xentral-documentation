> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Netstock ist eine Cloud-Lösung für professionelles Lagerbestandsmanagement im Online-Handel. Das Tool dient der Lagerbestandsoptimierung und wird über eine 2-Wege-Kommunikation an Xentral angebunden. Informationen (z.B. Aufträge, Lagerbestände, Stücklisten) werden von Xentral zunächst über die Netstock App an Netstock geschickt (Weg 1). Netstock verarbeitet diese und nutzt auch Informationen wie Daten aus den letzten Jahren oder Lagermindestbestände. Das Tool erstellt daraus neue Informationen wie Bestellvorschläge, Produktionsaufträge und weitere Ideen zur Optimierung des Lagerbestands, und schickt diese wiederum an Xentral. Diese eingehenden Informationen kommen dann im[Übertragungen Modul](https://help.xentral.com/hc/de/articles/360016738020#UUID-72f37f06-2871-0785-7286-1f7a2707c88d)an (Weg 2), wo sie weiter verarbeitet werden. Dieses Modul ist notwendig, um eingehende Daten von Netstock zu empfangen und zu verarbeiten.

Im folgenden Abschnitt wird der 1. Weg beschrieben, sprich die ausgehenden Informationen von Xentral an Netstock über die Netstock App. Die Einrichtung wird zukünftig von Netstock unterstützt werden.

## Netstock Anbindung

Die App **Netstock CSV Export ** kann über die Super-Search oder über**App Center > Netstock CSV Export** gefunden werden.

Die Netstock App erzeugt CSV-Dateien, die für die Übertragung von relevanten Informationen an Netstock dienen. Diese können dann entweder per FTP übertragen oder von einem definiertem Ordner auf dem Server abgeholt werden. Der zugehörige **Prozessstarter netstock** muss aktiviert werden um die unten beschriebenen Dateien zu erzeugen und zu übertragen.

### Registerkarte Grundeinstellungen

#### Zugangsdaten (FTP-Upload)

Speicherung der Ausgangs-Dateien über eine FTP-Verbindung.

- **FTP-Server:** Hostname des Servers
- **FTP-Benutzer:** Benutzername
- **FTP-Passwort:** Passwort

#### Konfiguration

- **Lager für Intern (Beistellungen):** Internes Lager für Beistellungen
- **Lager für Extern:** Externes Lager

#### Über Netstock CSV Export

Hier erhalten Sie einen Überblick über die erzeugten Dateien. Die Anwendung erzeugt csv-Dateien für:

- Lager/Filialen (location.csv)
- Lieferanten (supplier.csv)
- Artikelstamm (master.csv)
- Bestand je Lagerort (stock.csv)
- Verkauf & Verbrauch (sales.csv)
- Offene Lieferanten oder Produktionsbestellungen (po.csv)

Die Dateien werden per FTP übertragen und sind im Folgenden detailliert beschrieben.

#### Live Monitor FTP

Im Monitor werden die letzten FTP-Übertragungen sichtbar. Hier können fehlerhafte Verbindungsversuche (z.B. durch Änderung von FTP-Zugangsdaten) erkannt werden.

### Netstock Dateitypen

Folgende Dateitypen finden in XentralAnwendung:

- control.csv: Informationen über die Datenextraktionen
- master.csv: Artikelinformationen (Stammdaten)
- group.csv: Artikelkategorien (Stammdaten)
- bom.csv: Stücklisten (Stammdaten)
- supplier.csv: Aktive Lieferanten
- location.csv: physische Lagerorte (Lager und Filialen)
- stock.csv: Bestand je Lagerort
- sales.csv: Rechnungen und Gutschriften jeweils ab dem 1. Tag des Vormonats
- co.csv: Offene Aufträge
- po.csv: Offene Bestellungen und Produktionen
- pohist.csv: Erfüllte Bestellungen und Produktionen

#### Datei: control.csv

Übersicht über die Grundeinstellungen der Netstock-Schnittstelle. Die Datei umfasst immer nur die folgenden vier Zeilen.

Beispielinhalt für die CSV

Datei:KeyValueINTERFACE_VERSION2.0.8EXTRACTION_DATE2019/07/17EXTRACTION_TIME12:00:36HOST_SYSTEM_VERSION19.3

#### Datei: master.csv

Übersicht über alle Artikel.

Spalten der CSV-Datei und Beschreibung:

- Item Code: Artikelnummer
- Beschreibung: Artikelname
- NETSTOCK Unit of Measure: Artikeleinheit
- Unit Volume: immer leer
- Unit Weight: Artikelgewicht
- Superseded Item Code: immer leer
- Superseded Item Factor: immer leer
- Not used: Artikelfeld 'gesperrt'
- Unique Identifier: Interne ID des Artikels, sichtbar in der URL

#### Datei: group.csv

Umfasst derzeit die Artikelkategorien.

Spalten der CSV-Datei und Beschreibung:

- Identifier: Interne ID
- Value: (Numerischer) Wert
- Beschreibung: Name der Gruppe

#### Datei: bom.csv

Übersicht über die Stücklisten.

Spalten der CSV-Datei und Beschreibung:

- Finished Good Item: Artikelnummer
- Finished Good Item Location: Lager-ID
- Raw Material Item: Artikelnummer
- Raw Material Location: Lager-ID
- Ratio: Menge des Ausgangsartikels in der Stückliste

#### Datei: supplier.csv

Übersicht über die Lieferanten.

Spalten der CSV-Datei und Beschreibung:

- Supplier: Lieferantennummer
- Beschreibung: Name des Lieferanten
- Type: immer leer
- Lead time: Durchnittslieferzeit aus den Einkaufspreisen

#### Datei: location.csv

Physische Bestandsorte / Filialen (nicht Lagerpositionen).

Spalten der CSV-Datei und Beschreibung:

- Location Code: Interne Id des Lagers
- Beschreibung: Bezeichnung des Lagers
- Active: immer 1
- Group: immer leer
- Type: 'ST' (Laden/Filiale) oder 'CW' (Zentrallager, Projekt-ID = 1) abhängig vom Projekt

#### Datei: stock.csv

Der jetzige Bestand je Lagerort. Es werden alle Lagerplätze berücksichtigt, die zum konfigurierten 'Lager für Intern (Beistellungen)' gehören und solche die als Produktionslager gekennzeichnet sind.

Spalten der CSV-Datei und Beschreibung:

- Item Code: Artikelnummer
- Location: Meistens Hauptlager, Konfiguriernbar in der Netstock App
- Date Added: leer
- Inventory Unit Cost: berechneter Einkaufspreis: wenn fehlt, dann "0"
- Purchase Unit Cost: Standard Einkaufspreis 1er Menge, wenn fehlt dann "0"
- Selling Price: Verkaufspreis für Menge 1, wird erst in zweiten Schritt erzeugt; Fallback? > schaut komisch aus > aber kommt der richtig im Schritt 2?
- Stock On Hand: Lagerbestand
- Allocated Stock: immer 0
- Supply Type: Konstanter Wert 'EX'
- Supply Code: Lieferantennummer, Standartlieferant kommt entweder aus EK Fallback Artikel
- Vendor Code: Lieferantennummer, Standartlieferant kommt entweder aus EK Fallback Artikel
- Purchase Unit of Measure: Artikel Einheit
- Purchase Factor: bleibt leer
- Purchase Currency Code: derzeit immer Euro; ggf. Wärung aus kalk. Ek nehmen (PASST, ist IMMER EUR)
- Lead Time: Standard Lieferzeit aus EK in Tagen, Fallback: wenn nicht angegeben, dann "0"
- Stocking Indicator: Ist ein konfigurierbares (Frei-)Feld in der Netstock App
- Minimum Stock: Artikel Mindestlager: wenn leer dann 0
- Minimum Order Qty: Artikel Mindestbestellmwnge → wenn leer dann 0
- Order Multiple: Artikel Mindestbestellmwnge → wenn leer dann 0
- Group 1: Artikelkategorie

#### Datei: sales.csv

Verbrauch- und Verkaufs-Historie. Eingeschränkt auf alle Einträge ab dem Ersten des Vormonats. Beispiel: Aktuelles Datum 15.07. - angezeigt werden Daten ab dem 01.06.

Spalten der CSV-Datei und Beschreibung:

- Item Code: RE/GS-Position Artikelnummer
- Location: Übernommen aus den Modul-Einstellungen (Lager für Intern (Beistellungen))
- Customer Code: Kundenummer von RE/GS; Fallback adresse.kundenummer
- Order Date: Auftrag Datum; (Auftrag in Gutschrift über die Rechnung gejoint);Fallback RE/GS-Datum
- Invoice/Issue Date: RE/GS-Datum
- Sales Quantity: RE/GS-Position Menge
- Cost of Sales: RE/GS-Position Menge * RE/GS-Position Einkaufspreis
- Sales Value: RE/GS-Position.umsatz_netto_gesamt; Fallback Preis Menge und Rabatt der Position
- Issues Quantity: immer leer
- Transaction Type: 'S' für Rechnung, 'R' für Gutschrift

#### Datei: co.csv

Offene Kundenbestellungen. Enthält alle Lagerartikel oder Artikel die keine Lagerartikel sind aber Kopf-Artikel von 'Just in Time'-Stücklisten.Unterelemente von 'Just in Time'-Artikeln werden ausgeschlossen.

Spalten der CSV-Datei und Beschreibung:

- Item Code: Artikelnummer
- Location: Übernommen aus den Modul-Einstellungen (Lager für Intern (Beistellungen))
- Customer Code: Kundennummer aus AU; Fallback Kundennummer aus Adresse (über Adresse aus AU)
- Order Number: AU Belegnummer
- Line Number: Sortierung aus Position
- Order Date: AU-Datum
- Order Quantity: AU-Position Menge
- Requested Date: Lieferdatum aus Position; Fallback Liefersdatum aus AU; Fallback Datum aus AU
- Outstanding Quantity: AU-Position Menge - AU-Position Geliefert

#### Datei: po.csv

Enthält alle Positionen aller Produktionen deren Belegstatus nicht abgeschlossen, nicht storniert und nicht angelegt ist. Zusätzlich alle Bestellpositionen die nicht geliefert sind und deren Belegstatus nicht angelegt, nicht abgeschlossen und nicht storniert ist.

Spalten der CSV-Datei und Beschreibung:

- Item Code: Artikelnummer
- Location: Übernommen aus den Modul-Einstellungen (Lager für Intern (Beistellungen))
- Supplier Code: Lieferantennummer (bei Bestellungen: Lieferant der Bestellung, bei Produktionen: Standardlieferant des Artikels)
- Order Number: BE/PROD-Belegnummer
- Line Number: Sortierung aus Position
- Order Date: BE/PROD-Datum
- Order Quantity: Menge aus Position
- Expected Arrival Date: BE/PROD-Datum + Artikel-Lieferzeit
- Outstanding Quantity: BE/PROD-Menge aus Position - BE/PROD-Geliefert aus Position
- Order Type: 'P' für Bestellung, 'M' für Produktion
- Purchase Unit Cost: Wenn der Artikel ein Produktionsartikel ist dann Preis aus Position, ansonsten Kalkulierter EK

#### Datei: pohist.csv

Enthält alle Positionen aller Produktionen deren Belegstatus abgeschlossen ist. Und alle Bestellungspositionen die geliefert wurden aber auch alle Positonen die nicht geliefert wurden und deren Belegstatus abgeschlossen ist.

Spalten der CSV-Datei und Beschreibung:

- Item Code: Artikelnummer
- Location: Übernommen aus den Modul-Einstellungen (Lager für Intern (Beistellungen))
- Supplier Code: Lieferantennummer (gemappt über Lieferant aus BE oder PROD)
- Order Number: BE/PROD-Belegnummer
- Line Number: Sortierung aus Position
- Order Date: BE/PROD-Datum
- Order Quantity: Menge aus Position
- Expected Arrival Date: BE/PROD-Datum + Artikel-Lieferzeit
- Order Urgency: Derzeit immer leer; Definiert als entweder ST = Standardbestellung oder EM = Expressbestellung (Bestellung mit deutlich geringerer Lieferzeit)
- Quantity Received: Das Feld 'Geliefert' aus BE/PROD-Position
- Date of Receipt: BE/PROD-Lieferdatum
- Purchase Unit Cost: Kalkulierter EK des Artikels