In Xentral ermöglichen **Freifelder** eine individuelle und flexible Erweiterung der Standarddaten in verschiedenen Modulen. Sie bieten dir die Möglichkeit, zusätzliche Informationen zu erfassen, die über die regulär verfügbaren Felder hinausgehen – beispielsweise produktspezifische Eigenschaften, interne Bemerkungen, kundenspezifische Klassifizierungen oder projektspezifische Informationen.

Freifelder sind vollständig konfigurierbar: Du kannst sie **aktivieren **, ** benennen **, einem bestimmten ** Typ zuweisen ** (z. B. einzeiliges Textfeld, Datum, Auswahlmenü), ihre ** Position innerhalb der Maske **oder im ** PDF-Dokument **bestimmen und festlegen, ** ob und wo** sie im System angezeigt werden sollen.

![Artikelfreifelder_konfiguration.png](https://help.xentral.com/hc/article_attachments/21878908399644)

## Wann Freifelder verwenden: Standardfeld oder Freifeld?

Standardfelder verwenden, wenn die Info für Xentral-Logik wichtig ist (Steuern, Zahlungen, Versand, Integrationen).

Freifelder nutzen für Zusatz- oder Individualdaten, die keine Xentral Kernprozesse beeinflussen bzw. die als Zusatzdaten für dein Businessmodell mit ausgewertet werden - aber keine ERP Xentral Standardfelder sind.

**Beispiele Standardfelder (immer nutzen): ** Typische Standardfelder sind etwa Zahlungskonditionen, die für Mahnwesen und Rechnungen relevant sind, die USt-ID, die für Steuerprüfung und innergemeinschaftliche Lieferungen benötigt wird, die Versandart bzw. der Carrier, die für Labelerzeugung und Versandautomation gebraucht werden, sowie Trackingnummern, die für Kundenbenachrichtigungen und Belege genutzt werden. Ebenso zählen Bankdaten wie IBAN oder BIC, die für SEPA-Zahlungsprozesse notwendig sind, und Adressstammdaten, die für Versand und Reporting eine zentrale Rolle spielen, zu den Standardfeldern.** Beispiele Freifelder (sinnvoll für):**

Freifelder machen hingegen dort Sinn, wo individuelle Zusatzinformationen benötigt werden, etwa bei Gravur- oder Wunschtexten für Produkte, bei technischen Zusatzdaten wie der Leistung eines Solarmoduls, bei internen Attributen wie einem VIP-Status oder Vertriebsgebiet, bei Formeleingaben wie Länge, Breite oder Preis pro Quadratmeter oder bei Zusatzinformationen aus Shops wie einem Geschenkverpackungstext.

> **Tipp**
>
> Praxisregel:
>
> - Alles, was Xentral Pflichtdaten oder Standard-Automationen betrifft → Standardfeld.
> - Alles, was individuell, kundenspezifisch oder rein intern ist → Freifeld.

## Freifelder in Stammdaten

Freifelder lassen sich in folgenden Stammdatenbereichen einsetzen:

- **Artikel**: bis zu 40 frei benennbare Felder, inklusive Übersetzungen und Shop-Integration
- **Adressen**: bis zu 20 Felder, davon zwei für die Adresssuche verwendbar
- **Projekte**: bis zu 10 Felder, individuell darstellbar in projektbezogenen Tabellen

Diese Felder eignen sich besonders zur strukturierten Erfassung zusätzlicher Daten und lassen sich in der Benutzeroberfläche an zentraler Stelle pflegen: **Einstellungen > Stammdaten > Freifelder**.

## Freifelder in Belegen

Darüber hinaus kannst du Freifelder in verschiedenen Belegarten einblenden lassen – zur Anzeige relevanter Informationen im operativen Ablauf sowie in gedruckten oder versendeten Dokumenten.

Die folgenden Belegtypen unterstützen die Verwendung von Freifeldern:

- Angebot, Auftrag,
- Rechnung, Gutschrift, Proforma-Rechnung (nur bei aktiviertem Modul),
- Lieferschein, Kommissionierschein,
- Bestellung,
- Preisanfrage und Produktion (nur bei aktiviertem Modul).

Die Anzeige in den Belegen wird über eine zentrale Einstellungs-Matrix gesteuert und kann bei Bedarf individuell für jedes Freifeld aktiviert oder deaktiviert werden. Auch eine Darstellung in PDFs ist konfigurierbar, sodass Freifelder z. B. im Angebots- oder Auftragsdokument sichtbar sind.

## Praxisbeispiele für Freifelder

Freifelder lassen sich in Xentral sehr vielseitig einsetzen – von der Abbildung kundenspezifischer Daten über die Erweiterung von Artikelinformationen bis hin zur Nutzung als Parameter für Berechnungen und individuelle Kalkulationen.

### Kundenspezifische Daten (Personalisierungen) in den Prozessfluss integrieren

Freifelder eignen sich ideal, um kundenspezifische Anpassungen direkt im ERP-System abzubilden. Ein typisches Beispiel sind Customizing-Artikel, wie etwa Produkte mit individueller Beschriftung, Namen oder Lasergravur.

- In den Artikelstammdaten legst du ein oder mehrere Freifelder an, z. B. Beschriftung, Gravurtext oder Kundenname.
- Diese Felder kannst du so konfigurieren, dass sie in Aufträgen und Rechnungen angezeigt werden oder nur intern genutzt werden.
- Über die API können solche Parameter auch direkt aus einem Webshop importiert werden, sodass kundenindividuelle Angaben automatisch in Xentral landen.
- Vorteil: Die Informationen begleiten den gesamten Prozess – von der Bestellung über die Produktion bis hin zum Lieferschein.

> **Anmerkung**
>
> **Hinweis**
>
> Kundenspezifische Daten (z. B. Gravurtext):
>
> **Konfiguration:**
>
> - Bereich: Artikel-Freifelder
> - Bezeichnung: Gravurtext
> - Typ: mehrzeilig
> - Spalte: 1
> - Anzeige im PDF: Auftrag, Rechnung
>
> **Einsatz:**
>
> - Gravurtext wird im Auftrag erfasst und im PDF angezeigt
> - Optionaler Import der Daten aus dem Shop via API

#### Erweiterte Artikelfelder

Mit Freifeldern lassen sich Produkte um zusätzliche technische oder inhaltliche Informationen erweitern, die im Standard nicht vorhanden sind.

Beispiele aus der Praxis:

- **Solartechnik**: Leistung in Watt-Peak, Wirkungsgrad oder Modulgröße.
- **Lebensmittel**: Nährwerte, Allergene oder Zutatenlisten.
- **Maschinenbau**: Spezifikationen wie Drehzahl, Leistungsaufnahme oder Maße.

Diese Freifelder können sowohl in der Artikelmaske gepflegt als auch in **Dokumenten oder Shops** sichtbar gemacht werden. So lassen sich detaillierte Produktinformationen zentral verwalten und überall nutzen.

> **Anmerkung**
>
> **Hinweis**
>
> Erweiterte Artikelfelder (z. B. Solarpanel-Leistung)
>
> **Konfiguration:**
>
> - Bereich: Artikel-Freifelder
> - Bezeichnung: Leistung (Wp)
> - Typ: einzeilig
> - Spalte: 2
> - Anzeige im PDF: Angebot, Auftrag, Rechnung
>
> **Einsatz:**
>
> - Technische Daten wie Leistung werden im Artikel gepflegt
> - Angaben erscheinen automatisch im Angebotsdokument

#### Freifelder für Formeln und Kalkulationen

Neben der reinen Datenerfassung können Freifelder auch als **Parameter für Berechnungen** dienen.

Dadurch kannst du **individuelle Kalkulationen** direkt im ERP-System abbilden.

> **Tipp**
>
> Weitere Informationen zum Thema **Formeln** findest du ausführlich im ArtikelFormeln.

Beispiele:

- **Zuschnitt und Maßanfertigungen**: Eingabe von Länge, Breite und Höhe in Freifeldern → automatische Berechnung des Preises oder Materialbedarfs.
- **Preisberechnungen**: Freifeld für Rohstoffpreis kombiniert mit Mengenangaben → automatisierte Kalkulation der Endkosten.
- **Kundenspezifische Konfigurationen**: Eingabe von Parametern wie Farbe, Größe oder Ausstattung → dynamische Preis- oder Produktionsanpassung.

So werden Freifelder zu einem wichtigen Werkzeug, um **maßgeschneiderte Produkte und Services** im System abzubilden.

> **Anmerkung**
>
> **Hinweis**
>
> Formeln und Kalkulationen (z. B. Zuschnitte)
>
> **Konfiguration:**
>
> - Bereich: Artikel-Freifelder
> - Bezeichnung: Länge → Typ: einzeilig
> - Bezeichnung: Breite → Typ: einzeilig
> - Bezeichnung: Preis/m² → Typ: einzeilig
> - Spalte: 1 oder 2 (je nach Platzierung)
> - Anzeige im PDF: Auftrag, Rechnung
>
> **Einsatz:**
>
> - Maße werden direkt im Auftrag eingegeben
> - Endpreis wird automatisch aus Länge × Breite × Preis/m² kalkuliert
> - Ideal für Maßanfertigungen oder Zuschnitte

## Einrichtung von Freifeldern **Schritte um Freifelder einzurichten: **

1. Gehe zu **Einstellungen > Stammdaten > Freifelder**.
1. Wähle den Bereich, in dem du Felder einrichten möchtest (Artikel, Adresse, Projekt).
1. **Aktiviere** das gewünschte Freifeld über die Checkbox.
1. Vergib eine **Bezeichnung** (z. B. „Material“ oder „Lieferbedingung“).
1. Wähle den passenden **Feldtyp** (Einzeilig, Mehrzeilig, Datum, Checkbox, Selectfeld).
1. Lege fest, wo das Feld angezeigt werden soll (Spalte 1,2 und Reihenfolge 1-n).
1. Klicke auf **Speichern**.

## Übersicht der Oberfläche zur Konfiguration von Freifeldern

Die Tabellen zeigen, welche Eingabefelder in Artikeln, Adressen und Projekten verfügbar sind, welche Funktion sie erfüllen und welche Optionen jeweils zur Auswahl stehen.

**Artikel-Freifelder:**

| Feld | Beschreibung |
| --- | --- |
| Aktiviert | Checkbox zum Ein- oder Ausschalten des Freifeldes. Nur aktivierte Felder können genutzt werden. |
| Bezeichnung | Freitextfeld für den Namen des Freifeldes (z. B. Material, Farbe, HS-Code). |
| Typ | Art der Eingabe: einzeilig, mehrzeilig, Datum, Checkbox oder Selectfeld. |
| Spalte | Position in der Artikelmaske: keine (Reiter „Parameter/Freifelder“), 1 (linke Seite im Tab „Artikel“), 2 (rechte Seite im Tab „Artikel“). |
| Reihenfolge | Zahl zur Festlegung der Anzeigereihenfolge (0, 1, 2 …). |
| Anzeige im PDF | Steuerung, in welchen Belegen das Freifeld angezeigt wird (z. B. Angebot, Auftrag, Rechnung, Lieferschein, Bestellung, Produktion). |

**Adress-Freifelder:**

| Feld | Beschreibung |
| --- | --- |
| Bezeichnung | Freitextfeld für den Namen des Freifeldes (z. B. Kundengruppe, Region). |
| Typ | Art der Eingabe: einzeilig, mehrzeilig, Datum, Checkbox oder Selectfeld. |
| Spalte | Position in der Adressmaske: keine, 1 (linke Seite), 2 (rechte Seite). |
| Reihenfolge | Zahl zur Festlegung der Reihenfolge der Anzeige (0, 1, 2 …). |

**Projekt-Freifelder:**

| Feld | Beschreibung |
| --- | --- |
| Bezeichnung | Freitextfeld für den Namen des Freifeldes (z. B. Projektart, Kostenstelle). |
| Typ | Art der Eingabe: einzeilig, mehrzeilig, Datum, Checkbox oder Selectfeld. |
| Spalte | Position in der Projektmaske: keine, 1 (linke Seite), 2 (rechte Seite). |
| Reihenfolge | Zahl zur Festlegung der Anzeigereihenfolge (0, 1, 2 …). |
| Tabelle | Gibt an, ob das Freifeld in der Projekt-Tabelle angezeigt wird. Werte: 0 = nein, >0 = ja. |
| Spaltenbreite in % | Legt die Breite in Projekt-Tabellen fest. Standardwert: 10 %, individuell anpassbar. |

**Beleg-Freifelder:**

| Feld | Beschreibung |
| --- | --- |
| Aktiviert | Checkbox zum Ein- oder Ausschalten der Nutzung von Freifeldern in Belegen. |
| Zuordnung | Über eine Haken-Matrix lässt sich festlegen, in welchen Belegarten das Freifeld sichtbar ist. Typische Belege sind Angebot, Auftrag, Rechnung, Gutschrift, Lieferschein, Bestellung, Produktion sowie optionale Belegarten wie Proforma oder Preisanfrage. |
| Anzeige im PDF | Wenn aktiviert, erscheint das Freifeld auch im generierten Beleg-PDF. |
| Bearbeitung im Beleg | Aktive Freifelder erscheinen im Bearbeitungsmodus des Belegs und können dort befüllt oder angepasst werden. Hinweis: Nur in nicht gesperrten Dokumenten verfügbar. |

## Freifelder in Artikeln

In Artikeln kannst du bis zu 40 Freifelder definieren. Diese können individuell beschriftet und in der Artikelmaske eingeblendet werden.

**Schritte: **

1. Gehe zu **Einstellungen > Stammdaten > Freifelder**.
1. Setze im Bereich **Artikel-Freifelder ** den Haken, um ein Feld zu **aktivieren**.
1. Trage eine **Bezeichnung** ein.
1. Wähle den Feldtyp:
1. Lege im Dropdown Spalte fest, wo das Feld angezeigt werden soll:
1. Klicke auf **Speichern**.

### Übersetzbare Freifelder in Artikeln

Im Artikel-Tab Freifelder kannst du Feldinhalte für verschiedene Sprachen hinterlegen.

- Standardmäßig ist Deutsch vorausgefüllt.
- Über **Fehlende Spracheinträge nachladen** werden weitere Sprachen automatisch ergänzt.
- Diese Übersetzungen können bei angebundenen Shops (z. B. Shopware) exportiert werden.

### Erweiterte Artikelsuche

Die Felder Freifeld 1 und Freifeld 2 können für die Artikelsuche aktiviert werden. **Einstellungen > Grundeinstellungen > System**.

## Freifelder in Adressen

Auch in den Adress-Stammdaten kannst du Freifelder definieren, um individuelle Zusatzinformationen zu Kunden, Lieferanten oder Ansprechpartnern zu speichern. Insgesamt stehen dir hier 20 Felder zur Verfügung.

**Schritte: **

1. Gehe zu **Einstellungen > Stammdaten > Freifelder**.
1. Setze im Bereich **Adress-Freifelder ** den Haken, um ein Feld zu **aktivieren**.
1. Gib eine **Bezeichnung** ein, die den Zweck klar beschreibt (z. B. „Kundengruppe“, „Region“, „Vertriebsgebiet“).
1. Wähle den passenden **Feldtyp**:
1. Lege die **Spalte** fest, in der das Feld erscheinen soll: keine, 1 (linke Seite), 2 (rechte Seite).
1. Bestimme die **Reihenfolge**, in der die Felder angezeigt werden sollen.
1. Klicke auf **Speichern**.

### Anzeige in der Adresse

- Aktivierte Freifelder kannst du in den Tab Weitere Felder der Adresse einblenden.
- Besonders wichtige Felder lassen sich ganz nach vorne verschieben, sodass sie sofort sichtbar sind.

### Adresssuche mit Freifeldern

- Über die **erweiterte Adresssuche ** kannst du **Freifeld 1 und 2** durchsuchbar machen.
- **Einstellungen > Gruneinstellungen > System > Sonstiges. **

- Besonderheit: Der Inhalt von ** Freifeld 1**wird in der Suchergebnisliste ** in Klammern hinter der Adresse angezeigt**.

## Freifelder in Projekten

Auch Projekte können zusätzliche Informationen über Freifelder speichern. Insgesamt stehen hier 10 Felder zur Verfügung.

**Schritte: **

1. Gehe zu **Einstellungen > Stammdaten > Freifelder**.
1. Setze im Bereich **Projekt-Freifelder ** den Haken, um ein Feld zu **aktivieren**.
1. Trage eine **Bezeichnung** ein (z. B. „Projektart“, „Abteilung“).
1. Wähle den **Feldtyp** (einzeilig, mehrzeilig, Datum, Checkbox oder Selectfeld).
1. Lege die **Spalte** fest, in der das Feld im Projekt angezeigt werden soll.
1. Definiere die **Reihenfolge**, wenn mehrere Felder aktiv sind.
1. Optional: Stelle ein, ob das Freifeld auch in der Projekt-Tabelle erscheinen soll.
1. Klicke auf **Speichern **. ** Besonderheiten bei Projekten**: Zusätzlich kannst du die Spaltenbreite in % bestimmen, wenn das Freifeld in einer Projektübersichtstabelle angezeigt wird. Standardmäßig ist die Breite auf 10 % eingestellt, kann aber flexibel angepasst werden, um längere Inhalte sichtbar zu machen.

## Freifelder in Belegen

Neben Stammdaten lassen sich Freifelder auch in **Belegen** verwenden, damit Zusatzinformationen direkt im operativen Geschäft (z. B. Angebot, Auftrag, Rechnung) erscheinen.

Unterstützte Belegarten:

- Angebot
- Auftrag
- Rechnung
- Gutschrift
- Lieferschein
- Kommissionierschein
- Bestellung
- Proforma-Rechnung (nur mit Modul)
- Preisanfrage
- Produktion **Schritte: **

1. Aktiviere unter **Einstellungen > Administration > Systemeinstellungen > Belege ** die Option **Positionen mit Freifelder**.
1. Öffne die Optionen-Matrix zur Zuordnung. **Einstellungen > Stammdaten > Freifelder**.
1. Setze die **Haken ** bei den **Belegarten**, in denen das jeweilige Freifeld sichtbar sein soll.
1. Klicke auf **Speichern**.

### Anzeige Freifelder in Belegen

- Aktivierte Freifelder werden im Beleg (z. B. Auftrag) unter den Artikelpositionen angezeigt.
- Im **Bearbeitungsmodus** kannst du die Inhalte der Felder direkt editieren.
- Im generierten **PDF-Dokument** erscheinen die Felder, wenn die Option „Anzeige im PDF“ aktiviert ist.
- Wichtig: Freifelder werden nur bei **nicht gesperrten Dokumenten** nachgeladen.

> **Anmerkung**
>
> **Hinweis**
>
> Praxisbeispiel:
>
> - Ein Artikel hat das Freifeld „Material“ mit dem Inhalt „925 Sterling Silber“.
> - Dieses Feld wurde für den Belegtyp **Auftrag** aktiviert.
> - Ergebnis: Das Feld erscheint sowohl im **Auftrags-PDF** als auch im Bearbeitungsmodus des Auftrags.