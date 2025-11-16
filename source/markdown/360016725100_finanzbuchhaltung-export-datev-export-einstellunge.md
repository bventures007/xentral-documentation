Für den reibungslosen Datenaustausch mit externen Buchhaltungsprogrammen ist es möglich, verschiedene Dateitypen zu exportieren. Diese umfassen Rechnungen und Gutschriften, Verbindlichkeiten sowie Konten- und Adressdaten. Durch die Anpassung dieser Einstellungen kann der Datenaustausch effizient gestaltet werden, um die Buchhaltungsprozesse zu optimieren und den betrieblichen Anforderungen gerecht zu werden.

- Export von **Rechnungen ** und **Gutschriften** im [DATEV-Format](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_section-idm234605846815923) oder [XML Format (Unternehmen Online)](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_N1730823450593).
- Export von **Verbindlichkeiten** im [DATEV-Format](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_N1730823488592) oder [XML Format (Unternehmen Online)](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_N1730823450593).
- Export von **Bankkonten**

- Kontobuchungen mit Kontierungen und Belegzuordnungen [(Kostenkonto, Debitor, Kreditor) im DATEV Format](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_N1730823525659).
- Export von **Stammdaten** (= Kontenbeschriftungen) wie Adressdaten der [Debitoren und Kreditoren im DATEV Format](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_section-idm234605907502066).

> **Tipp**
>
> Die **Automatische ** XML-Übertragung zu Unternehmen Online mit dem**Rechnungsdatenservice1.0** findest du im ArtikelDATEV Rechnungsdatenservice 1.0 (zuvor DATEV connect online).

## Achtung

1. Bevor du mit dem Export beginnst, ist eine [initiale Einrichtung der Stammdaten](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_section-idm2346058023653) erforderlich. Dazu zählen die Eingabe von Beraternummer, Mandantennummer, Wirtschaftsjahr und die Festlegung der Sachkontenlänge. Diese Stammdaten sind entscheidend, da sie in die Exportdateien übernommen werden und eine korrekte Zuordnung der Buchhaltungsinformationen ermöglichen.
1. Stelle vor dem Export der Daten die Konfiguration für DATEV ein bzw. prüfe, ob der Standard für dich passend ist: [Einstellungen](#einstellungen)

## Einstellungen (DATEV Export Konfiguration)

Die Einstellungen zum Finanzbuchhaltung Export findest du im Hauptmenü unter **Buchhaltung > Buchhaltung Export ** oder über die Smart-Suche über**Finanzbuchhaltung Export **. Klicke für die Einstellungen (Initiale Stammdaten-Einrichtung) auf das Tab: ** Einstellungen **. Die Konfiguration und den Export findest du im Tab: ** Export**.

### Einstellungen (Initiale Stammdaten-Einrichtung)

Für die **initiale Einrichtung des DATEV-Datenaustauschs ** musst du wichtige **Stammdaten ** wie**Beraternummer **, ** Mandantennummer ** und das **Wirtschaftsjahr ** und **Sachkontenlänge ** in das System eintragen. Diese Daten werden anschließend in die Exportdateien übernommen und ermöglichen eine korrekte Zuordnung der Buchhaltungsinformationen. Je nach Bedarf kannst du diese Einstellungen global oder auch projektspezifisch vornehmen, um den Export an die Anforderungen deines Unternehmens anzupassen. ** Schritte:**

1. Klicke im Tab **Einstellungen ** auf **+Neuen Eintrag anlegen**.
1. Trage **Beraternummer ** und **Mandantennummer** ein (beide Nummern erhältst du von deinem Steuerberater).
1. Trage das **Wirtschaftsjahr ** im Format '**TTMM**' ein, für das du die Übertragung benötigst. Z.B. für Start des Wirtschaftsjahres am 01.01.2025 verwende 0101 für "erster Januar". Das Jahr wird automatisch über die Buchungsdaten und deine Datumseingrenzung für den Export mitgegeben.
1. Gib die **Sachkontenlänge** an z.B. '4' für SKR04 oder '6' für SKR03 (wenn du 6-stellig verwendest).

![datev_mandantennummer_beraternummer_eintragen_001.png](https://help.xentral.com/hc/article_attachments/16751320050716)

| Feldbezeichnung | Beschreibung |
| --- | --- |
| **Beraternummer **| Die ** Beraternummer** erhältst du von deinem Steuerbüro. Sie identifiziert die Kanzlei oder den Steuerberater eindeutig im DATEV-System und wird von der DATEV an Steuerberater, Wirtschaftsprüfer oder Kanzleien vergeben. |
| **Mandantennummer **| Die ** Mandantennummer** erhältst du von deinem Steuerbüro oder vergibst du in deiner lokalen DATEV Version (z.B. Rechnungswesen Einzelplatz). Diese Nummer ordnet einen Mandanten innerhalb der DATEV-Datenverwaltung eindeutig zu. Die Mandantennummer wird entweder von der Kanzlei selbst innerhalb der DATEV-Software vergeben oder kann durch den Steuerberater in Absprache mit dem Mandanten eingerichtet werden |
| Projekt (optional) | Optional: Nur zu verwenden, wenn du den Export projektweise durchführen möchtest und für jedes Projekt eine eigene Mandanten- und Beraternummer verwendet werden soll. |
| Zahlungsweise in Datev (optional) | Optional: Du kannst hier ein Freifeld in der Adresse definieren und die Zahlungsweise für Datev in den Kundenstammdaten eintragen. Z.B. einzutragen: "freifeld1" bezeichnet das Freifeld 1 bei der Kundenadresse unter "Sonstige Daten". Nur ausfüllen, wenn du die Zahlungsweise inklusive der Anzahl der Tage bis zur Fälligkeit und eventuell gewährten Skonto an Datev übergeben möchtest z.B. weil du das DATEV Mahnwesen nutzt. |
| **Wirtschaftsjahr **| Das ** Wirtschaftsjahr **gibt an, für welchen Zeitraum deine Buchungen und Abschlüsse gelten. DATEV liest diese Daten aus und ordnet sie dem entsprechenden Wirtschaftsjahr zu. Trage das Wirtschaftsjahr im Format ‘** TTMM**' ein z.B. '0101’ für 1. Januar oder '0104' für 1. April. |
| **Sachkontenlänge **| Die ** Sachkontenlänge** legt fest, wie viele Stellen deine Kontonummern haben, wobei der SKR03 normalerweise vierstellig ist, aber auf sechs Stellen erweitert werden kann, wenn du detailliertere Buchungen benötigst. Z.B. '4' für SKR04 oder '6' für SKR03. |

### Export & Einstellungen

Manuelle Datenexporte bieten eine flexible Lösung für die Übertragung betrieblicher Informationen in Buchhaltungssoftware. Sie ermöglichen den Export von Rechnungen, Gutschriften, Verbindlichkeiten und Bankkontobuchungen im DATEV- oder XML-Format direkt zu DATEV Unternehmen Online. Zusätzlich lassen sich Stammdaten wie Adressen von Debitoren und Kreditoren exportieren. Diese Exporte können durch verschiedene Einstellungen angepasst werden, beispielsweise durch das Hinzufügen von Transaktionsnummern aus Shopsystemen zu Belegfeldern in DATEV.

![buchhaltung_export.png](https://help.xentral.com/hc/article_attachments/16658129312028)

#### Export Rechnungen / Gutschriften (DATEV Format)

> **Tipp**
>
> Diese Daten erhältst du im DATEV Format als manuellen Export.

**Schritte: **

1. Wähle als Sortierung '** Rechnungsnummer **' aus und gruppiere nach '** Konten**'.
1. Wähle als **Datumsbereich** einen Monat aus z.B. 01.10.2024 bis 31.10.2024.
1. Klicke auf '**Export**' um die CSV Datei im DATEV Format zu erhalten.

![buchhaltungsesport_rechnungen_gutschriften_datev_format.png](https://help.xentral.com/hc/article_attachments/16656799810716)

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Sortiert nach: 'Datum' oder 'Rechnungsnummer' | Sortierung der Buchungen im Export des Stapels im von dir ausgewählten Zeitraum: - '**Datum **': Sortierung der Erlöse z.B. Rechnungsbuchungen oder Gutschriftenbuchungen nach Datum.<br>- '** Rechnungsnummer**': Sortierung der Erlöse z.B. Rechnungsbuchungen oder Gutschriftenbuchungen nach Belegnummer aufsteigend. |
| Gruppiert nach: 'Konten' oder 'Positionen' | Gruppiert die Inhalte der Erlöse nach Steuersätzen gebündelt oder auf Positionsebene: - '**Konten **': Aufteilung der Erlöse nach Steuern z.B. 7% und 19% in Belegen mit gemischten Steuersätzen. z.B. Beleg mit 19% Inland wird im SKR04 auf 4400 gebucht. z.B. Beleg mit 19% und 7% wird im SKR04 auf 4400 und 4300 gebucht.<br>- Optional: 'Positionen': Aufteilung nach den Konten auf Positionsebene (Artikelebene). 💬** Anmerkung:** Die Einstellungen für die Konten findest du in den Systemeinstellungen der Steuern. Die Einstellungen der Konten für Positionen (= Artikelebene) findest du im Artikel. |
| Projekt | Optional / Standardmäßig leer lassen: Das Projekt nur angeben, wenn du ausschliesslich einen Kanal exportieren möchtest. |
| von ‘TT.MM.JJJJ’ bis ‘TT.MM.JJJJ’ | Wähle einen Exportbereich aus, indem du ein Datum von ‘**TT.MM.JJJJ **’ bis ‘** TT.MM.JJJJ**' angibst. Exportiere für DATEV z.B. den Zeitraum eines Monats für den Monatsabschluss. |
| Bereits exportierte Dokumente ignorieren | Optional/ Besonderer Workflow: Ignoriert die bereits gezogenen Daten z.B. wenn du täglich exportierst kannst du die Daten von gestern ausschliessen. 💬 **Anmerkung:** Nur zu empfehlen bei hochpreisigen Produkten und wenig Durchsatz in Belegen. |

#### Export Verbindlichkeiten (DATEV Format)

> **Tipp**
>
> Diese Daten erhältst du im DATEV Format als manuellen Export.

**Schritte: **

1. Wähle als **Datumsbereich** einen Monat aus z.B. 01.10.2024 bis 31.10.2024.
1. Klicke auf '**Export**' um die CSV Datei im DATEV Format zu erhalten.

![buchhaltungsesport_verbindlichkeiten_datev_format.png](https://help.xentral.com/hc/article_attachments/16656823936284)

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Projekt | Optional / Standardmäßig leer lassen: Das Projekt nur angeben, wenn du ausschliesslich einen Kanal exportieren möchtest. |
| von ‘TT.MM.JJJJ’ bis ‘TT.MM.JJJJ’ | Wähle einen Exportbereich aus, indem du ein Datum von ‘**TT.MM.JJJJ **’ bis ‘** TT.MM.JJJJ**' angibst. Exportiere für DATEV z.B. den Zeitraum eines Monats für den Monatsabschluss. |
| Bereits exportierte Dokumente ignorieren | Optional/ Besonderer Workflow: Ignoriert die bereits gezogenen Daten z.B. wenn du täglich exportierst kannst du die Daten von gestern ausschliessen. 💬 **Anmerkung:** Nur zu empfehlen bei hochpreisigen Produkten und wenig Durchsatz in Belegen. |

#### Export Konten (DATEV Format)

> **Tipp**
>
> Diese Daten erhältst du im DATEV Format als manuellen Export.

**Schritte: **

1. Wähle '** alle Konten**' aus.
1. Wähle als **Datumsbereich** einen Monat aus z.B. 01.10.2024 bis 31.10.2024.
1. Klicke auf '**Export**' um die CSV Datei im DATEV Format zu erhalten.

![buchhaltungsesport_konten_datev_format.png](https://help.xentral.com/hc/article_attachments/16656807091996)

> **Anmerkung**
>
> Die Sortierung erfolgt nach Konten absteigend.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Konto | Auswahl alle Buchungen über alle Konten (= Bankkonten) als Stapel zu erhalten. Alternativ Export der in Xentral manuell angelegten Buchungen zur Kontrolle oder als separater Stapel. Alternativ Auswahl eines speziellen Kontos als separater Stapelexport z.B. Deutsche Bank. - **Alle Konten **: Export aller Konten in einer Datei.<br>-** Nur Manuelle Buchung **: Export der in Xentral manuell gebuchten Einträge.<br>-** Bankkonto CSV**: Auswahl spezielles Bankkonto oder der Konten einzeln als Stapel. |
| von ‘TT.MM.JJJJ’ bis ‘TT.MM.JJJJ’ | Wähle einen Exportbereich aus, indem du ein Datum von ‘**TT.MM.JJJJ **’ bis ‘** TT.MM.JJJJ**' angibst. Exportiere für DATEV z.B. den Zeitraum eines Monats für den Monatsabschluss. |

#### Export DATEV Unternehmen online

> **Tipp**
>
> Diese Daten erhältst du im DATEV-XML Format als manuellen Export.

**Schritte: **

1. Wähle Beleg '** Verbindlichkeiten**' aus.
1. Wähle als **Datumsbereich** einen Monat aus z.B. 01.10.2024 bis 31.10.2024.
1. Klicke auf '**Export**' um die XML Datei für 'DATEV Unternehmen Online' zu erhalten.

![buchhaltungsesport_unternehmen_online_xml_format.png](https://help.xentral.com/hc/article_attachments/16656824080412)

### Achtung

Bei der Nutzung von DATEV Unternehmen Online wird der Export von Daten im Hintergrund durchgeführt, um das System nicht unnötig zu belasten. Wenn du auf „Export“ klickst, zeigt das System zunächst „Exportiere…“ an. Je nach Anzahl der Belege kann das etwas dauern.

Danach bekommst du einen Link, über den du die Daten herunterladen kannst. Die ZIP-Dateien, die dabei erstellt werden, enthalten jeweils höchstens 100 Belege. Wenn also zum Beispiel 150 Belege exportiert werden, erhältst du zwei ZIP-Dateien: eine mit 100 und eine mit 50 Belegen.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| **Beleg** | Wähle die Belegart für den XML Export für 'DATEV Unternehmen Online' aus: - Rechnungen<br>- Gutschriften<br>- Verbindlichkeiten |
| Projekt | (Optional / Standardmäßig leer lassen) |
| von ‘TT.MM.JJJJ’ bis ‘TT.MM.JJJJ’ | Wähle einen Exportbereich aus, indem du ein Datum von ‘**TT.MM.JJJJ **’ bis ‘** TT.MM.JJJJ**' angibst. |
| Bereits exportierte Dokumente ignorieren | Optional/ Besonderer Workflow: Ignoriert die bereits gezogenen Daten z.B. wenn du täglich exportierst kannst du die Daten von gestern ausschliessen. 💬 **Anmerkung:** Nur zu empfehlen bei hochpreisigen Produkten und wenig Durchsatz in Belegen. |

### Export Stammdaten **Schritte: **

1. Wähle ein Datum von ‘** TT.MM.JJJJ **’ bis ‘** TT.MM.JJJJ**' aus.
1. Klicke auf den Button ‘**Kunden **’ oder ‘** Lieferanten**’.

> **Tipp**
>
> Im Beispiel siehst du einen Kundendaten Export ab einer speziellen Kundennummer und einen Lieferantendaten Export für einen Datumsbereich.

![datev_stammdaten_export_kunden_lieferanten.png](https://help.xentral.com/hc/article_attachments/16656817649692)

#### Export Kunden (DATEV Format)

**Export Kunden: ** Der Button ** Kunden** liefert ALLE Kundenbeschriftungen eines Datumsbereiches (Neu angelegte Kundennummern und z.B. Namensänderungen). Die Eingabe Kundennummer limitiert diese Liste, Export erfolgt aufsteigend ab dieser Nummer (= aufsteigend nach der System-ID dieser Kundennummer). Voraussetzung ist, dass du die Datumsfelder leer gesetzt hast.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Export ab Kd.-Nr. | Export erfolgt aufsteigend ab dieser Nummer (= aufsteigend nach der System-ID dieser Kundennummer). |
| Kunden ab Datum ‘TT.MM.JJJJ’ bis ‘TT.MM.JJJJ’ | Wähle einen Exportbereich aus, indem du ein Datum von ‘**TT.MM.JJJJ **’ bis ‘** TT.MM.JJJJ**' angibst. Exportiert werden Neu angelegte Kundennummern und z.B. Namensänderungen |

#### Export Lieferanten (DATEV Format)

**Export Lieferanten: ** Der Button ** Lieferanten** liefert ALLE Lieferantenbeschriftungen eines Datumsbereiches. (Neu angelegte Lieferantennummern und z.B. Namensänderungen). Die Eingabe der Lieferantennummer limitiert diese Liste, Export erfolgt aufsteigend ab dieser Nummer (= aufsteigend nach der System-ID dieser Lieferantennummer). Voraussetzung ist, dass du die Datumsfelder leer gesetzt hast.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Export ab Lf.-Nr. | Export erfolgt aufsteigend ab dieser Nummer (= aufsteigend nach der System-ID dieser Lieferantennummer). |
| Lieferanten ab Datum ‘TT.MM.JJJJ’ bis ‘TT.MM.JJJJ’ | Wähle einen Exportbereich aus, indem du ein Datum von ‘**TT.MM.JJJJ **’ bis ‘** TT.MM.JJJJ**' angibst. Exportiert werden Neu angelegte Lieferantennummern und z.B. Namensänderungen |

## Einstellungen

x

### Rechnungen / Gutschriften (Export Einstellungen)

![buchhaltungsexport_einstellungen_export_rechnungen_gutschriften.png](https://help.xentral.com/hc/article_attachments/18965495796124)

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Belegfeld1 bei Kontoauszugsexport mit Rechnungsnummer füllen wenn möglich | Ergänzt die Rechnungsnummer in 'Belegfeld 1' automatisch, z.B. wenn die Rechnung mit der Bankzahlung verknüpft ist. |
| Belegfeld1 bei Rechnungs- u. Gutschrift um Internet- und Transaktionsnummer erweitern | Ergänzt die Internet- und Transaktionsnummer in 'Belegfeld 1' sofern es die Zeichenmenge in DATEV erlaubt. |
| Belegfeld 2 bei Rechnung u. Gutschrift mit Fälligkeitsdatum füllen | |
| KOST1 mit Lieferland füllen anstelle Kostenstelle (Lieferschwelle) | Verwendet das DATEV Kostenstellenfeld für die Lieferschwelle um die Berechnung in DATEV für die Lieferschwelle zu steuern. Achtung: In diesem Fall ist das Feld KOST1 nicht mehr für die Kostenstelle genutzt sondern die Berechnung in DATEV angesteuert. |
| AmaInvoice-Belege ausschließen | Belege aus Amainvoice ausschliessen um den Amainvoice Export separat zu nutzen. |

### Verbindlichkeit (Export Einstellungen)

![buchhaltungsexport_einstellungen_export_verbindlichkeiten.png](https://help.xentral.com/hc/article_attachments/18965495797788)

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Verbindlichkeit Auswahl | Auswahl des Abgrenzungszeitraumes nach Eingangsdatum der Verbindlichkeit (= Lieferantenrechnung) oder nach Rechnungsdatum der Verbindlichkeit (= Lieferantenrechnung). Abhängig von dieser Einstellung werden die Belege in den von dir ausgewählten Exportzeitraum einbezogen oder ausgenommen. - Nach Eingangsdatum: Eingangsdatumsfeld im Modul Verbindlichkeiten (Eingangsdatum in der Belegeingabe)<br>- Nach Rechnungsdatum: Rechnungsdatumsfeld im Modul Verbindlichkeiten (Rechnungsdatum in der Belegeingabe) |

### Datev (Export Einstellungen)

![buchhaltungsexport_einstellungen_export_datev.png](https://help.xentral.com/hc/article_attachments/18965495798172)

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Belege mit Betrag = 0 EUR auch exportieren | Belege mit Gesamtsumme 0 EUR in den Export einschliessen. Z.B. wenn '0 Euro Rechnungen' mit zu DATEV übergeben werden sollen. 💬 **Anmerkung:** Beachte, dass 0 EUR Belege evtl. als Fehler erscheinen beim Import in Buchhaltungssysteme oder markiert werden z.B. DATEV. |
| Neues Datev Format (Testbuchung einfügen) | Fügt eine Markierungsbuchung ein, so dass der importierte Buchhungsstapel in DATEV importiert aber nicht festgeschrieben wird. Festgeschriebene Buchungsstapel können z.B. nur über dein Steuerbüro geöffnet oder falsche Importe evtl. nur durch Korrekturbuchungen korrigiert werden. |
| Erweiterte Buchungs-Codes erlauben | Erkennt in den Konten hinzugefügte Buchhungsschlüssel, die du deiner Standard Kontenlänge vorangestellt hast. Die Schlüssel werden in DATEV separat entsprechend dem DATEV Standard getrennt dargestellt. Z.B. kannst du für 4-stellige Kontenlänge folgende Nummern im [Kontenrahmen](https://help.xentral.com/hc/de/articles/360016775339#UUID-ea5b2535-11f1-4efa-8b41-f5ea33a91bf4) angeben: '4400' für Umsatzerlöse als DATEV Automatikkonto, für ein Kostenkonto z.B. Bürobedarf mit 19% Steuer das Konto '906815', für Innergemeinschafltiche Erwerbe 19% könnte es auch ein dreistelliger Schlüssel sein z.B. '9405900'. |
| CSV Validierung deaktivieren | Validerung der CSV für den DATEV Standard z.B. Anzeige einer Fehlermeldung bei Leerzeichen. |
| im XML für Datev Unternehmen Online ergänzen | Mit dieser Auswahl kannst du im DATEV XML für DATEV Unternehmen Online die Shopbestellnummer (= Internetnummer) oder die PayPal Transaktionsnummer (= Transaktionsnummer) oder beide hinzufügen lassen. - Internetnummer<br>- Transaktionsnummer<br>- Internetnummer und Transaktionsnummer<br>- Transaktionsnummer und Internetnumme |

## FAQ

Überschneidungen zum letzten exportierten Bereich vermeiden! Buchhaltungsprogramme erkennen in der Regel keine Überschneidungen → Doppelimport. Empfehlung: hier immer feste Zeitbereiche auswählen z.B. ganze Monate.

## Export für Datev

Für den Export zu Datev muss folgendes erledigt werden:

1. Beraternummer und Mandantennummer in Xentral angeben (wird in die Datei geschrieben und von Datev ausgewertet)
1. Export Haken einstellen und die Datei ziehen

Um in DATEV bereits einige Buchungen vorab automatisiert abzuschließen ist es notwendig, vor dem Einspielen der Daten aus DATEV Unternehmen Online diese auch als DATEV Connect Online hineinzuladen. DATEV Connect Online sind die Kontenbewegungen in DATEV. Sofern ihr den Zahlungseingang aktiv nutzt, könnt ihr diese Daten direkt aus Xentral herunterladen und zu DATEV Rechnungswesen importieren.

Dieser Schritt, ist trotz aktivem Matching im Zahlungseingang notwendig, da die Daten aus Unternehmen Online oder Connect Online lediglich Rechnungsdaten beeinhalten.

### 1. Berater Nummer / Mandanten Nummer

Für den neuen Datev Export (ab 2018) kann eine Berater- und Mandantennummer vergeben werden. Die Vergabe kann auch auf Projektebene stattfinden. Im angefügten Beispiel ist die Berater- und Mandantennummer global systemweit zu betrachten. Im Modul Finanzbuchhaltung Export ist unter dem Tab Einstellungen über den Button +Neuen Eintrag anlegen ein neuer Eintrag anzulegen.

Anschließend öffnet sich ein Dialogfeld, in dem die notwendigen Informationen eingetragen werden können. Diese sind:

- Beraternummer: Beraternummer eintragen. Diese wird dann mit in die Export-Datei generiert
- Mandantennummer: Mandantennummer eintragen. Diese wird dann mit in die Export-Datei generiert
- Projekt: Optional. Nur zu verwenden, wenn projektweise exportiert wird und für jedes Projekt eine eigenen Mandanten- und Beraternummer verwendet werden soll
- Zahlungsweise in Datev: Optional. freifeld1 bezeichnet bei Adresse des Kunden → Sonstige Daten das Freifeld 1. Nur zu verwenden, wenn bei den Kundenstammdaten die Zahlungsweise mit Anzahl der Tagen bis zur Fälligkeit und gegebenen Skonto an Datev übergeben werden soll
- Wirtschaftsjahr: Start des Wirtschaftsjahrs im Format TTMM - Beispiele: 0101 für 1. Januar oder 0104 für 1. April
- Sachkontenlänge: Gebe hier die Länge des Sachkontos an, die du benötigst (ggf. beim Steuerberater nachfragen). Diese wird dann mit in die Export-Datei generiert

Anschließend ist die Eingabe zu speichern. Beispiel für die Anzeige in Datev (Stand 02/2018):

- Beraternummer: 33333
- Mandantennummer: 10000

![buchhaltungexport_3.png](https://help.xentral.com/hc/article_attachments/5077565006364)

#### Länge von Nummernkreisen anpassen

Es ist auch möglich 6-stellige Sachkonten zu buchen oder mit 7-stelligen Kreditoren- bzw. Debitorennummern zu arbeiten. Hierzu können unter Administration > Einstellungen > System > Grundeinstellungen > Einstellungen im Tab Nummernkreise die Kunden- und Lieferanten-Nummernkreise entsprechend umgestellt werden. Dies kann auch pro Projekt durchgeführt werden.

Die Datev-Konten können dann beim Export eingestellt werden, sodass Datev diese Info im Dateiheader mitbekommt (Buchhaltung > Finanzbuchhaltung Export > Einstellungen).

Ansonsten können die Datev-Konten in Xentral direkt 6-stellig gepflegt werden (Administration > Einstellungen > Buchhaltung > Kontenrahmen).

Zu beachten ist, dass Konten beim Export nicht automatisch mit dem Steuerfeld mit einem Schlüssel vorkontiert werden. Der Steuerschlüssel wird in Xentral immer direkt vor die Kontierung eingetragen.

Hier besteht folgende Möglichkeit:

1. Den Steuerschlüssel vorne mit dazu nehmen/dazu tippen
1. Im Kontenrahmen die wichtigsten Verbindlichkeitskonten mit Steuerschlüssel zusätzlich anlegen und textuell bezeichnen

#### Verbindlichkeiten:

Bei der Kontierung der Verbindlichkeiten ist der Steuerschlüssel mit anzugeben. Das Feld für den Steuersatz wandelt sich nicht für Datev in den Steuerschlüssel um.

Beim Datev Export (CSV) kommt die Verbindlichkeit dann in 2 Splittbuchungen mit.

Unten bei Unternehmen Online erhält man dann hier bei dem Verbindlichkeiten Export in der XML jeweils die Kontierungen: einmal mit Steuerschlüssel, einmal ohne.

### 2. Export Haken einstellen und die Datei ziehen

Im TabExportim BereichEinstellungenkönnen auf der rechten Seite die benötigten Einstellungen für den Export getätigt werden.

Rechnungen/Gutschriften:

- Belegfeld1 bei Kontoauszugsexport mit Rechnungsnummer füllen wenn möglich (Datev findet die Pärchen und es erleichtert die Zuordnung für das Steuerbüro)
- Belegfeld1 bei Rechnung und Gutschrift um Internet- und Transaktionsnummer erweitern (nur wenn unbedingt gewünscht hier Haken setzen)

Verbindlichkeiten:

- Verbindlichkeit Auswahl nach Eingangsdatum oder Rechnungsdaten (für den eingegebenen Zeitraum werden nur die Verbindlichkeiten mit Eingangs- oder Rechnungsdatum, die in diesem Zeitraum liegen, exportiert)

Datev:

- Belege mit Betrag = 0 EUR auch exportieren (allgemeine Einstellung, bei gemischten Steuersätzen werden die Beträge der Rechnung einzeln zeilenweise exportiert)
- Datev Format auswählen: Neues Datev Format (ab 2018) oder Neues Datev Format Version 700
- Neues Datev Format (Testbuchung einfügen) (Wichtig → denn ansonsten wird in Datev sofort alles festgeschrieben beim Import)
- Erweiterte Buchungs-Codes (ermöglicht 3-4 stellige Buchungsschlüssel zu exportieren)
- Mit Anwählen der Option wird ein Splitten der Konten herbeigeführt. Anhand der Sachkontenlänge bzw. die Angabe der entsprechenden Konten, kommt es dann bei der Ausgabe zu einer neuen Spalte mit dem gesplitteten Teil. Z.B. Kontonummer 2250880, Sachkontenlänge → 4, Angabe "BU-Schlüssel" → 225
- Internet-,Transaktionsnummer im XML für Datev Unternehmen Online (übermittelt die Online-Shop oder Paypal Kennungen an Datev)

Zahlweisen/Steuersätze:

- Auswählen wenn diese Zusatzinformationen exportiert werden soll.

### Datev Unternehmen Online

Mit Datev Unternehmen Online können Rechnungen, Gutschriften und Verbindlichkeiten als PDF-Beleg an die Buchhaltung übergeben werden. Bei den Rechnungen werden die Belege verwendet, die von Xentral erzeugt wurden. Bei den Verbindlichkeiten werden diejenigen verwendet, die beim Modul Verbindlichkeiten hochgeladen wurden. Für die Einstellung DATEV Unternehmen Online muss die Vorkontierung der Verbindlichkeiten (im Tab Vorkontierung) vollständig abgeschlossen sein, bevor die Übertragung stattfinden kann. Im Tab Vorkontierung ist es ebenfalls möglich Konten zu splitten. Ein Sachkonto/Gegenkonto (Feld „Sachkonto“ im Verbindlichkeiten-Beleg, erster Tab) anzugeben, reicht hierfür nicht aus.

Es können alle Belege dieser Art exportiert werden, die sich in Xentral befinden, außer diese sind noch im Entwurfsmodus.Xentral bietet eine erweiterte Exportmöglichkeit für Datev Unternehmen Online an. Damit können Belege der Ausgangsrechnungen, Gutschriften und Eingangsrechnungen (Verbindlichkeiten) als ZIP-Datei exportieren werden.

> **Anmerkung**
>
> Wenn gewisse Zeiträume überschritten werden, werden die Daten stumpf weiter übertragen. D.h. die Daten werden doppelt ohne eine Überprüfung auf eine mögliche Dopplung übertragen.

- Beleg: Im Dropdown können Rechnungen, Gutschriften oder Verbindlichkeiten ausgewählt werden. Die Lieferantenrechnung muss bei der Verbindlichkeit hochgeladen werden, damit diese für den Export zur Verfügung stehen kann. Außerdem müssen bei den Verbindlichkeiten bei Vorkontierung ein Aufwandskonto eingegeben werden. Es muss zwingend das Feld "Währung" unter dem Modul "Verbindlichkeiten" ausgefüllt sein, da ansonsten das Datev-Tool die Daten nicht annimmt
- Projekt: Damit können Exportberichte nach Projekten sortiert ausgegeben werden. Über das Suchfeld kann das Projekt ausgewählt werden. Wird das Feld ist leer gelassen, werden alle Projekte exportiert.
- von / bis: Hier kann der Datumsbereich des Exports ausgewählt werden (Belegdatum).

Die ZIP-Dateien können mit dem Datev-Belegtransfer an das Datev-Rechenzentrum übertragen werden. (Die Software Belegtransfer kann von Datev kostenlos heruntergeladen werden).

![buchhaltungexport_6.png](https://help.xentral.com/hc/article_attachments/5077565021852)

- Verzeichnistyp: Bitte unbedingt im Belegtransfer beachten, dass der Verzeichnistyp nicht auf "Standard" ausgewählt ist, sondern "DATEV XML-Schnittstelle online"
- Belegtyp: Bei Belegtyp muss "ohne Belegtyp" ausgewählt seintype

> **Anmerkung**
>
> Es werden ausschließlich vorkontierte Buchungen in DATEV akzeptiert. Um zu prüfen, ob sämtliche Verbindlichkeiten über eine Vorkontierung besitzen, kann der Filter "fehlende Kontierung" in den Verbindlichkeiten aktiviert werden.

## Einstellung der Exportkonten

Die Einstellung der Exportkonten sind direkt über das TabExportim BereichEinstellungenvorzunehmen.

### Export Rechnungen / Gutschriften

Auf der linken Seite kann der Export der Dokumente Rechnungen und Gutschriften und den dazugehörigen Erlöskonten durchgeführt werden. Folgende Optionen stehen zur Verfügung:

- Sortiert nach: Datum oder Belegnummer
- Gruppiert nach: Konto oder Positionen
- Projekt: nicht ausfüllen (wird nur benötigt für Multimandanten oder getrennte Buchhaltung)
- von bis: Datumsbereich auswählen (Überschneidungen zum letzten exportierten Bereich vermeiden! Buchhaltungsprogramme erkenne in der Regel keine Überschneidungen → Doppelimport) Empfehlung: hier immer feste Zeitbereiche auswählen z.B. ganze Monate
- Export: Export der Rechnungen oder Gutschrift

### Export Verbindlichkeiten

Auch die Verbindlichkeiten können auf der linken Seite exportiert werden.

- Projekt: Optional und wird Standardmäßig leer gelassendefault
- von bis: Datumsbereich auswählen (Überschneidungen zum letzten exportierten Bereich vermeiden! Buchhaltungsprogramme erkenne in der Regel keine Überschneidungen → Doppelimport) Empfehlung: hier immer feste Zeitbereiche auswählen z.B. ganze Monate
- Export: Export der Rechnungen oder Gutschrift

Beschriftungsfelder

Folgende Felder stehen für den Export zur Verfügung: 1. Datum, 2. Betrag, 3. Konto/Lieferanten-Nr, 4. Belegfeld 1, 5. Buchungstext, 6. Land, 7. Ust-Id, 8. Gegenkonto, 9. Währung.

> **Anmerkung**
>
> Wird beim Erstellen einer Verbindlichkeit kein Rechnungs- und Eingangsdatum eingetragen, so werden die Felder automatisch mit dem aktuellen Datum gefüllt.

- Auch eine abweichende Rechnungsadresse wird exportiert.
- In Xentral stornierte Verbindlichkeiten werden nicht exportiert.