Der Stammdaten Import ermöglicht es, Datenbestände aus anderen Systemen in die Datenbank von Xentral einzufügen. Dazu müssen die Daten aus den fremden Systemen als CSV-Datei (Textdateien, die sämtliche Informationen als kommaseparierte Listen enthalten) exportiert werden. Weitere Informationen stehen in der Dokumentation der entsprechenden Systeme zur Verfügung.

> **Tipp**
>
> Einen Leitfaden zum ersten Datenimport findest du in diesem Artikel **Stammdaten Import - Adressen, Artikel (Einrichtung)**.
>
> Der Artikel enthält eine Anleitung zum Stammdatenimport in Xentral. Du erfährst dort, wie du CSV-Dateien aus externen Systemen erstellst und welche Überlegungen du vor dem Import anstellen solltest. Wir erklären dir die Schritte für den manuellen Datenimport und geben dir Hinweise zur Vorbereitung und Durchführung eines erfolgreichen Datenimports, einschließlich der Bewertung der Datenqualität und der Auswahl relevanter Felder.

## Funktionsumfang des Stammdaten-Imports

Es können folgende Datensätze in Xentral hinzugefügt oder aktualisiert werden:

- [Adressen: Kunden, Lieferanten, Mitarbeiter, Ansprechpartner](#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574_id_360016758939_id_h_01F6SKFGKXQKBDSFMRSZGA3VTY)
- [Artikel: Einzelartikel und Stücklisten](#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574_id_360016758939_id_h_01F6SKJHAEBR6YE51M590DJQBF)
- [Erfasste Arbeitszeiten](#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574_id_360016758939_id_h_01F6SKQ218FCZ5F7TGVBNPTEZ0)
- [Wiedervorlagen auf Kunden](#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574_id_360016758939_id_h_01F6SKQKDJAV9ECWV27NXATTB9)
- [Kundennotizen](#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574_id_360016758939_id_h_01F6SKQRNCPDEXH8TTXK27523H)

## Stammdaten importieren

Der Import von Stammdaten wird in Xentral grundsätzlich über Import-Vorlagen durchgeführt. Diese Vorlagen können jederzeit wieder verwendet werden, sofern ein weiterer Import von Daten mit der gleichen Struktur notwendig ist.

Nutze zunächst die Smart Search, um das Modul **Import/Export Zentrale ** zu öffnen. Klicke dann auf**Stammdaten Import**.

Klicke oben rechts auf **+ NEU **, um eine neue Vorlage für den Import von Stammdaten anzulegen. Nimm dann die folgenden Einstellungen vor. Klicke am Ende auf ** Speichern**.

- **Bezeichnung**: Beliebiger Name für die Import-Vorlage
- **Ziel**: Auswahl der Art des Datenuploads (werden eingespielt: Adresse, Artikel, Einkaufspreise, Zeiterfassung, Wiedervorlagen, Notizen)
- **CSV-Daten ab Zeile**: Zeilennummer in der CSV-Datei, in der die Auflistung der eigentlichen Daten beginnt
- **CSV-Trennzeichen**: In der CSV-Datei verwendetes Trennzeichen, mit dem Daten von einander getrennt sind
- **CSV-Maskierung**: In der CSV-Datei verwendetes Maskierungszeichen (optional)
- **Auswahl Charset**: Codierung für die CSV-Datei. Bei CSVs aus Excel heraus auch ISO-8859-1 probieren
- **Charset **: Falls eine andere Codierung als im Dropdown-Menü ** Auswahl Charset** angegeben genutzt wird, kannst du diese hier eintragen. Lasse das Feld andernfalls leer.
- **CSV-Felder**: Trage hier die Spaltennummern in der CSV und die Importvariablen einzutragen. Format = SpaltenNrCSV:XentralVariable;
- **Interne Bemerkung**: Hier kann für die firmeninterne Kommunikation eine Bemerkung eingetragen werden

> **Wichtig**
>
> Ein sorgfältiger Umgang bei der Zuordnung der Datenfelder ist sehr wichtig, da ansonsten der Datenbestand durcheinander gerät. Teste deshalb vorab den Import, selbst wenn nur kleine Datenmengen verarbeitet werden.

Um die Daten in einer CSV-Datei zu importieren, öffnest du das Tab **Import starten: CSV Datei hochladen **. Klicke auf ** Datei auswählen **, um die gewünschte CSV-Datei auf deinem Computer auszuwählen und anschließend auf ** CSV hochladen**.

> **Anmerkung**
>
> Falls Schwierigkeiten bei der Darstellungsform auftreten, überprüfe die Trennzeichen vorliegende CSV-Datei.

**Hinweise für die CSV-Datei:**

- Die Daten werden beim Import nicht bereinigt. Stelle zuvor sicher, dass sich keine doppelten Daten in der CSV-Datei befinden
- Für die CSV-Datei empfiehlt es sich, als Feldtrenner ein Semikolon (;) und als Texttrenner ein Anführungszeichen ( ") zu verwenden

Falls eine Variable in der Importvorlage verwendet wird und kein Inhalt in der CSV-Datei vorhanden ist, überschreibtXentral einen möglicherweise vorhandenen Inhalt mit einem leeren Textfeld. Sobald die Datei vollständig übertragen wurde, erscheint eine Auflistung der enthaltenen Daten, die überprüfbar ist. Wichtig ist, dass in der Spalte **Aktion ** entweder **Neu ** oder **Update ** steht, da sonst ein Fehler in der Importvorlage vorliegt. Klicke auf**Importieren**, um den Import der Daten anzustoßen und zu warten, bis der Vorgang abgeschlossen ist. Wenn der Vorgang erfolgreich war, erscheinen die importierten Daten anschließend in Xentral. Die zuletzt vergebene Artikelnummer bzw. Adressnummer muss noch in die Nummernkreise eingetragen werden. Das verhindert, dass beim Inkrementieren um 1 eine bereits vergebene Nummer doppelt erstellt wird.

Weiterführende Informationen zu Nummernkreise findest du in diesem Artikel:[Nummernkreise verwenden](https://help.xentral.com/document/preview/54702#UUID-8477d892-3065-03ad-d893-9bbb3372737a).

### Workflow

Um Stammdaten in der Importzentrale hochzuladen, wird zunächst eine der Vorlagen ausgewählt.

In der Vorlage kann über den Reiter "Import starten: CSV Datei heraufladen" eine Datei für den Upload ausgewählt und hochgeladen werden.

Anschließend wird auf "importieren" geklickt und die Datei wandert in die Warteschlange. Es gibt 2 unterschiedliche Warteschlangen in der Importzentrale. Es gibt die Möglichkeit, sich die Dokumente in der Warteschlange für eine bestimmte Importvorlage anzusehen (*Importvorlage wählen* → Import starten: CSV Datei heraufladen → Warteschlange). Außerdem können alle wartenden Dokumente aller Importvorlagen anzeigt werden, indem direkt in der Importzentrale auf den Reiter Warteschlange geklickt wird.

> **Anmerkung**
>
> Falls Importaufträge dauerhaft in der Warteschlange verbleiben und der Fortschritt bei 0% stehen bleibt, kannst du versuchen, die Warteschlange zu löschen und den Import erneut durchzuführen. Beachte, dass der Import je nach Datenmenge etwas Zeit in Anspruch nehmen kann.

Der ganze Ablauf der Importvorlagen ist statusgetrieben. Der genau Statusablauf sieht folgendermaßen aus:

1. 'created' bzw. 'nicht freigegeben': Den Zustand hat ein Import, bevor die "importieren" Schaltfläche geklickt wurde. Ein Import in diesem Zustand kann freigegeben werden indem in der Übersicht auf den Pfeil nach rechts geklickt wird
1. 'in_queue' bzw. 'freigegeben': Diesen Zustand nimmt der Import ein wenn auf die Importieren-Schaltfläche, oder in der Übersicht auf den Pfeil nach rechts geklickt wird. Sobald ein Import freigegeben ist wird er vom Prozessstarter 'importvorlage' verarbeitet sobald er an der Reihe ist
1. 'canceled' bzw. 'abgebrochen': Der Import wurde vom Benutzer abgebrochen
1. 'in_progress' bzw. 'wird ausgeführt': Der Prozessstarter verarbeitet den Import aktuell
1. 'done' bzw. 'abgeschlossen': Der Import wurde vom Prozessstarter vollständig verarbeitet
1. 'complete' bzw. 'abgeschlossen': Ein Synonym für 'done'
1. 'error' bzw. 'Fehler': Bei einem Import in diesem Zustand ist während der Verarbeitung durch den Prozessstarter ein Fehler aufgetreten.

### Prozessstarter

Um auch große Dateien ohne Server-Timeout importieren zu können, wird nach dem Klick auf "Importieren" die Datei im Hintergrund bearbeitet und die Meldung "Import an Prozessstarter übergeben" erscheint.

Der Import findet somit erst statt, wenn der Prozessstarter neu angelaufen ist.

Unter "Administration → Einstellungen → System → Prozessstarter → Suche nach Importvorlage" kann das Intervall und der letzte Ausführungszeitpunkt überprüft werden:

Werden nur kleine Datenmengen importiert, kann der Prozessstarter auch deaktiviert werden, um den Import unmittelbar durchzuführen.

## xentral Praxistipps Import

Folgende Tipps sind hilfreich, um Dateien bei xentral richtig zu importieren.

### Tipps im Umgang mit Excel und CSV-Dateien

Es ist wichtig, die richtigen Einstellungen beim Exportieren, Bearbeiten und Speichern der CSV Datei zu beachten. Sonst kommt es zu Formatfehlern, wie z.B. "?" in den Werten statt Umlauten.

Vor dem Bearbeiten der Datei:

- Wenn die Daten aus dem Alt-System exportiert werden → Hier ist bereits die Kodierungs-Option → UTF-8 und als Trennzeichen eine Semikolon (;) auszuwählen
- Excel will oft Spalteninhalte "interpretieren" und ändert dafür das Format der Werte. Dies ist ein Grund, warum xentral für Importe Open Office verwendet
- Beim Öffnen der Datei in Open Office ist sicherzustellen, dass der Zeichensatz auf "Unicode (UTF-8)" steht
- Im selben Fenster ist auf das 1. Rechteck der Tabelle (siehe Screenshot unten) zu klicken, damit alles markiert wird. Danach ist im Drop-Down "Text" auszuwählen, um keine Formatveränderung zu bewirken

#### Beim Speichern der CSV Datei

Nachdem die Änderungen vorgenommen und als CSV Datei gespeichert wurden, ist im Popup unten die Option "Filtereinstellungen bearbeiten" zu wählen. Danach ist im nächsten Popup das Format beizubehalten und auf folgende Werte zu achten:

![importexport_2.png](https://help.xentral.com/hc/article_attachments/13755179534748)

#### Excel Datei in eine CSV speichern

Im Dropdown "Auswahl Charset" muss hier ISO-8859-1 ausgewählt werden. Falls die Umlaute immer noch nicht funktionieren, ist für UTF-8 unten ein Workaround beschrieben: Manchmal werden Excel-Dateien von der Struktur nur richtig in Excel angezeigt (in Open Office z.B. mit Zeilenumbrüchen). Will man aber direkt aus Excel diese Datei als CSV speichern, gibt es ohne einen Workaround oft Probleme mit den Umlauten.

Für den Workaround wird benötigt:

- Excel
- Open Office
- Einen guter Texteditor (z.B. Notepad++)
- Datei in Excel als Format "UTF-16 Unicode-Text (.txt)" Datei speichern
- Die Textdatei im Texteditor öffnen und dort als CSV Datei speichern (einfach.csv am Dateinamen anhängen)
- Die neue CSV Datei mit Open Office öffnen und folgenden Einstellungen tätigen:
- Die CSV in Open Office neu abspeichern
- Filtereinstellungen bearbeiten → Für die Bearbeitung ist der Haken zu setzen

Nun sollte die CSV Datei für den Import mit dem richtigen Format geeignet sein.

## Adressen Import

Adressen sollten immer vor den Artikeldaten importiert werden. Im Idealfall sind verschiedene CSV Dateien für Kunden und Lieferanten vorhanden. Mitarbeiter werden meist per Hand eingepflegt, könnten jedoch auf die gleiche Weise importiert werden.

### Kunden

Um Kunden in der CSV-Datei korrekt anzulegen, sind nachstehende Informationen zu beachten.

Checkliste für die CSV Datei:

- Pflichtfelder: name und kundennummer
- Pro Kunde nur eine Zeile
- Jede Kundennummer ist nur einmal vorhanden
- Alle Felder ohne Inhalt werden auf den Standard gestellt (z.B. Land, Sprache, etc.)

Beispiel für eine Importvorlage:

1:kundennummer; 2:name; 3:typ; 4:strasse; 5:plz; 6:ort; 7:telefon; 8:telefax; 9:ustid; 10:land;

Beispielinhalt für die CSV Datei:

| kundennummer | name | typ | strasse | plz | ort | telefon | telefax | ustid | land |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10001 | Anton Ansberger | Herr | Untere Talstr. 13 | 12345 | Augsburg | 555-555-5555 | 555-555-5556 | 123456789 | DE |

> **Anmerkung**
>
> Es ist möglich, die Kundennummer automatisch von xentral aus den hinterlegten Nummernkreisen vergeben zu lassen. In der CSV Datei ist in der Spalte für die Kundennummer als Inhalt für jeden Kunden das Wort "NEU" (ohne Anführungszeichen) zu schreiben.

![importexport_6.png](https://help.xentral.com/hc/article_attachments/13755158413340)

### Lieferanten

Hier ist analog zum Vorgang der Kunden vorzugehen, nur ist statt der Variable 'kundennummer' die Variable 'lieferantennummer' zu verwenden.

### Rolle vergeben beim Import

Soll die Kundennummer oder die Lieferantennummer mit der Rolle bei der Neuanlage von Adressen vergeben werden, werden mindestens folgende Informationen in der Importdatei benötigt:

![importexport_7.png](https://help.xentral.com/hc/article_attachments/13755158485660)

CSV-Datei, die für das Importbeispiel angelegt wurde:

![importexport_8.png](https://help.xentral.com/hc/article_attachments/13755190983964)

Du kannst dir eine Vorschau des Imports anzeigen lassen.

![importexport_9.png](https://help.xentral.com/hc/article_attachments/13755179968796)

Die Rolle wird in der Adresse wird über das entsprechende Auswahlmenü vergeben:

![importexport_10.png](https://help.xentral.com/hc/article_attachments/13755158672668)

> **Anmerkung**
>
> Für die Vergabe einer neuen Kundennummer aus dem Nummernkreis des Projektes wird das betreffende Projekt und "neu" als Kundennummer angegeben.

### Ansprechpartner

Es gibt auch die Möglichkeit, Ansprechpartner am Stück zu importieren. Hier werden die Ansprechpartner einem Kunden zugeordnet und in einer eigenen Zeile in der CSV-Datei dargestellt (siehe CSV-Beispielinhalt weiter unten).

> **Anmerkung**
>
> Dieser Import ist nur zum einmaligen Importieren der Ansprechpartner gedacht. Ein "Updaten" einzelner Ansprechpartner ist nicht vorgesehen und muss manuell über Stammdaten → Adresse → Edit → Ansprechpartner geschehen.

Checkliste für die CSV Datei:

- Pflichtfelder: name und lieferantennummer
- Pro Kunde nur eine Zeile
- Ansprechpartner müssen in der CSV Datei in der Spalte "Lieferantennummer" mit "ANSPRECHPARTNER:Lieferantennummer" gekennzeichnet werden, wobei die Lieferantennummer die in xentral hinterlegte Nummer für den Lieferanten ist

Alle Felder ohne Inhalt werden auf den Standard gestellt (z.B. Land, Sprache, etc.)

Beispiel für eine Importvorlage: 1:lieferantennummer; 2:name; 3:typ; 4:email; 5:telefon; 6:telefax; 7:mobil; 8:strasse; 9:plz; 10:ort; 11:abteilung; 12:anschreiben;

> **Anmerkung**
>
> Es ist zu beachten, dass die Ansprechpartner in der Spalte "Lieferantennummer" mit dem Inhalt "ANSPRECHPARTNER:Lieferantennummer" gekennzeichnet werden müssen **Beispielinhalt für die CSV Datei**: Hier werden 2 Kunden mit jeweils 2 Ansprechpartnern nach xentral importiert.

| Lieferantennummer | Name | Typ (firma, frau, herr) | E-Mail | Telefon | Telefax | Mobil |
| --- | --- | --- | --- | --- | --- | --- |
| 11223456 | Max Muster GmbH | firma | muster@email.de | 555-555-5555 | 555-555-5556 | 555-555-4444 |
| ANSPRECHPARTNER:11223456 | Alex Adler | herr | alexadler@email.de | 555-555-5555 | 555-555-5556 | 555-555-4433 |
| ANSPRECHPARTNER:11223456 | Berthold Bracht | herr | bertholdbracht@email.de | 555-555-5555 | 555-555-5556 | 555-555-4422 |
| 33445677 | Schrauben GmbH | firma | schraube@email.de | 444-444-4444 | 444-444-4445 | 444-444-3333 |
| ANSPRECHPARTNER:33445677 | Doris Dagobert | frau | dorisdagobert@email.de | 444-444-4444 | 444-444-4445 | 444-444-3322 |
| ANSPRECHPARTNER:33445677 | Emil Entlin | herr | emilentlin@email.de | 444-444-4444 | 444-444-4445 | 444-444-3311 |

Danach kann der Ansprechpartner unter der Adresse im Reiter "Ansprechpartner" eingesehen werden:

## Gruppen

Adressen können auch Gruppen über den Import zugeordnet werden.

Checkliste für die CSV Datei:

- Pflichtfelder: kundennummer oder lieferantennummer und gruppe1 - falls Adresse neu erstellt wird, wird zudem name und typ benötigt
- Alle Gruppen müssen vor dem Import schon in xentral unter Administration → Einstellungen → Buchhaltung → Gruppen angelegt sein **Beispiel für eine Importvorlage bei Adressupdate: ** 1:kundennummer; 2:gruppe1; 3:gruppe2;** Beispielinhalt für die CSV Datei:**

10001;Geschäftskunde;Elektronikbranche;

10002;Endkunde;Elektronikbranche;

10003;Geschäftskunde;Kommunikationsbranche;

> **Anmerkung**
>
> - Es können bis zu 5 Gruppen pro Adresse übergeben werden: Variablen → gruppe1, gruppe2, gruppe3, gruppe4, gruppe5
> - In der CSV Datei wird entweder der Gruppenname oder die Gruppenkennziffer erwartet
> - Falls keine Rolle (Kunde, Mitarbeiter, Lieferant) angelegt werden soll: Variable kundennummer verwenden aber die Spalte dafür in der CSV Datei leer lassen

### Lead Adressen

Adressen können auch als Lead über den Import angelegt werden.

Checkliste für die CSV Datei:

- Pflichtfelder: lead, name und typ **Beispiel für eine Importvorlage: ** 1:name; 2:lead; 3:ort;** Beispielinhalt für die CSV Datei:**

Anton Adler;1;Augsburg;

Berta Bussard;1;Berlin;

Catrin Cathlin;1;Cottbus;

## Vertrieb

### Zuordnung der Kunden zu einem Vertriebsmitarbeiter

Um allen Kunden aus einem Projekt X eine Vertriebsadresse bzw. einen Vertriebsmitarbeiter Y zuzuordnen, ist es ausreichend, eine CSV Datei im Stammdatenimport hochzuladen mit folgenden Spalten:

- Kundennummer
- AdressID der Vertriebsadresse

> **Anmerkung**
>
> Die AdressID unterscheidet sich von den im Nummernkreis vergebenen Nummern (Kunden-, Mitarbeiter-, Lieferantennummer). Bei der Auswahl eines Vertriebsmitarbeiters aus einer Liste befindet sich die ID auf der linken Seite vor dem Namen. Alternativ kann die Adresse des entsprechenden Mitarbeiters geöffnet und die ID aus der URL abgelesen werden.

Die Adressen können im ersten Schritt exportiert werden. Der Export der Liste aller Kundennummern eines Projektes ist[hier](https://help.xentral.com/hc/de/articles/360018921560#UUID-33498ffb-2f7f-2ef3-e568-702f17699b77)erklärt.

Im Anschluss wird diese Datei bearbeitet und wieder in einem Importformat hochgeladen. Relevant für den Import sind Spalte 1 und Spalte 3 (Spalte 2 kann ausgelassen werden, sofern die Kundennummer im System eindeutig vorliegt, ansonsten ist die SystemID die eindeutige Adress ID): kundennummersystemidvertrieb10000381000148100025810003781000498

Die Importvorlage sieht passend zu Spalte 1 und 3 folgendermassen aus:

![importexport_11.png](https://help.xentral.com/hc/article_attachments/13755180104732)

Der Upload der CSV Datei erfolgt über den Tab " Import starten: CSV Datei heraufladen".

> **Wichtig**
>
> Der Upload zeigt die gefundenen Daten an. Hier werden bei großen Datenmengen nur die ersten Seiten als Vorschau angezeigt. Über die Schaltfläche "Import" wird die Änderung in die Adressdaten geladen. Im Beispiel sind die erfolgreichen Daten (GRÜN) markiert. Die leeren Datensätze (nicht markiert) sollten in der Datei vollständig entfernt sein. Diese sind in der CSV Datei durch unvollständige Löschung und Bearbeitung der Datei entstanden. Die Datei ist ggf. nochmal nachzuarbeiten, korrekt zu speichern und neu hochzuladen.

> **Anmerkung**
>
> Für Importe, die eine Änderung des Adressstammes, relevanter Daten und großer Datenmengen nach sich ziehen, sollte der Import von Daten zuvor mit einer kleinen Datensatzmenge getätigt und genau kontrolliert werden.

![importexport_12.png](https://help.xentral.com/hc/article_attachments/13755152002716)

**Ergebnis:** Adresse Vertrieb: Die Vertriebsadresse ist bei den ausgewählten Kunden im Adresstamm hinterlegt:

![importexport_13.png](https://help.xentral.com/hc/article_attachments/13755158856092)

### Versandart

Allen Kunden ist eine Versandart Y zuzuordnen.

> **Anmerkung**
>
> Die Versandart muss nicht zwangsläufig der Kundenadresse zugewiesen werden. Die Standardversandart kann auch in den Systemeinstellungen unter Administration → Einstellungen → System → Grundeinstellungen → Steuer/Währung hinterlegt werden. Nur für abweichende Fälle wird dann die andere Versandart in der Kundenadresse direkt eingefügt.

![importexport_14.png](https://help.xentral.com/hc/article_attachments/13755165070364)

Bei der Versandart die Typbezeichnung unter "Administration → Einstellungen → Versandarten → Übersicht" verwenden:

![importexport_15.png](https://help.xentral.com/hc/article_attachments/13755152197404)

Beispieltabelle für die Versandart: kundennummerversandart10000express_dpd10001express_dpd10002express_dpd10003express_dpd10004express_dpd

Vor dem Import einer neuen Versandart in alle Kunden ist Folgendes zu prüfen: Wenn die Versandart A in allen Kunden gespeichert ist und diese firmenweit auf Versandart B geändert werden soll, kann direkt in der Versandart das "Modul" von Versandart A auf Versandart B umgestellt werden. Dies sollte jedoch nur vorgenommen werden, wenn Versandart A wirklich komplett eliminiert werden soll. In diesem Fall eines Modul-Wechsels wird die Versandart ID in der Adresse, im Projekt und in allen Einstellungen für die Logistik beibehalten und wechselt auf die neue Versandart B.

## Die wichtigsten Importvariablen für Adressen

Nachstehend sind die wichtigsten Importvariablen für Adressen zu sehen:

| Name in Xentral | Importvariable | Beispielinhalt CSV | Position in Xentral | Anmerkung |
| --- | --- | --- | --- | --- |
| Typ | typ | Firma | Adressen / Details / Adressdaten | Anrede, möglich: Herr, Frau, Firma, Mr, Mrs, Company |
| Sprache für Belege | sprache | deutsch | Adressen / Details / Adressdaten | möglich in CSV: deutsch, englisch |
| Name | name | Max Mustermann | Adressen / Details / Adressdaten | Pflichtfeld - Bei Firmen: Firmenname, bei Personen: Vor- und Nachname |
| Straße | strasse | Untere Talstr. 13 | Adressen / Details / Adressdaten | |
| Adresszusatz | adresszusatz | Apartment 1 | Adressen / Details / Adressdaten | Adresszusatz |
| Ort | ort | Augsburg | Adressen / Details / Adressdaten | |
| PLZ | plz | 10001 | Adressen / Details / Adressdaten | Postleitzahl |
| Land | land | DE | Adressen / Details / Adressdaten | Wichtig: Nur ISO-Code (DE, AT, NL, etc.) |
| Telefon | telefon | 0123456789 | Adressen / Details / Adressdaten | |
| Mobil | mobil | 0170123456 | Adressen / Details / Adressdaten | |
| Anschreiben | anschreiben | Sehr geehrter Herr Mustermann | Adressen / Details / Adressdaten | |
| E-Mail | email | max-mustermann@email.de | Adressen / Details / Adressdaten | |
| Internetseite | internetseite | [http://example.com](http://example.com/) | Adressen / Details / Adressdaten | |
| USt-ID | ustid | 12354567 | Adressen / Details / Zahlungskonditionen | |
| Kundennummer | kundennummer | 100001 | Adressen / Details / Zahlungskonditionen | Pflichtfeld (bei Kunden) - Nicht doppelt vergeben |
| Lieferantennummer | lieferantennummer | 200001 | Adressen / Details / Zahlungskonditionen | Pflichtfeld (bei Lieferanten) - Nicht doppelt vergeben |
| Mitarbeiternummer | mitarbeiternummer | 30001 | Adressen / Details / Zahlungskonditionen | Pflichtfeld (bei Mitarbeitern) - Nicht doppelt vergeben |
| Ansprechpartner | ansprechpartner | Hildegard Müller | Adressen / Details / Adressdaten | |
| Sonstiges | sonstiges | Ein sehr treuer Kunde | Adressen / Details / Adressdaten | |

Eine vollständige Liste der Importvariablen findet sich in xentral innerhalb der Importvorlage.

> **Anmerkung**
>
> Alle Felder in der CSV-Datei, für die es kein entsprechendes Feld in xentral gibt, können in sogenannte Freifelder geladen werden. Von diese sind bei einer Adresse 20 Stück, unter dem Tab "Sonstige Daten", vorhanden, die aufsteigend mit der Importvariable freifeld1, freifeld2, etc importiert werden können.

### Besteuerung

Für den Import der Besteuerung von Kunden kannst du mit der Variable ust_befreit arbeiten und folgende Werte nutzen:

- 0 (für Inland)
- 1 (für EU-Lieferung)
- 2 (für Export)
- 3 (für Steuerfrei Inland)

Sollte es sich bei der Adresse um einen Lieferanten handeln und sollte die Beteuerung Verbindlichkeiten rechts unter "Zahlungskonditionen beim Lieferant bei Bestellungen" importiert werden, heißt die Variable umsatzsteuer_lieferant und folgende Werte können genutzt werden:

- import
- eulieferung
- inland

## Artikel Import

Die Artikelnummer wird meistens als Index oder Schlüssel verwendet. Das Leerzeichen ist immer das Ende der Artikelnummer und wird von anderen Systemen auch so interpretiert. Weiterführende Systeme und andere interne Prozesse in xentral, z.B. Packtischprozesse, benötigen Artikelnummern ohne Sonderzeichen und Leerstellen für die Verarbeitung via Scanner, Barcodescanner oder Mobilen Devices. Leerzeichen sollten deshalb z.B. durch Minuszeichen oder Unterstriche ersetzt werden. Können die Artikelnummern auf Plattformen nicht geändert werden, kann die Plattformnummer via Fremdnummer in der xentral Artikelnummer hinterlegt werden.

### Artikel

Um Artikel korrekt zu importieren, sind folgende Punkte zu beachten:

- Checkliste für die CSV Datei:
- Pflichtfelder: name_de und nummer
- Pro Artikel nur eine Zeile → jede Artikelnummer ist nur einmal vorhanden
- Alle Felder ohne Inhalt werden auf den Standard gestellt (z.B. Währung auf Euro)

**Beispiel für eine Importvorlage:** 1:nummer; 2:name_de; 3:artikelbeschreibung_de; 4:kurztext_de; 5:internerkommentar; 6:ean; 7:gewicht; 8:lieferantennummer; 9:lieferanteinkaufnetto; 10:lieferanteinkaufmenge; 11:verkaufspreis1netto;

12:verkaufspreis1menge; 13:lagerartikel; 14:lager_platz; 15:lager_menge_total; 16:mindestlager;

> **Anmerkung**
>
> Mit der Variable “lager_platz” wird das Standardlager geändert, wenn kein Lagerbestand in der Importdatei vorhanden ist. Wenn ein Lagerbestand vorhanden ist, wird der Bestand geändert, nicht das Standardlager.

**Beispielinhalt für die CSV Datei:**

200001;Rennrad Cross X;Rennrad Cross X von Rennprofis empfohlen;Rennrad Cross X für Profis.;Unser Bestseller;1234567;3,5;300001;1300;1;1900;1;1;HL001A;3;2; 200002;Rahmen Rennrad Cross X;Rahmen für das Rennrad Cross X zum selber montieren.;Rahmen Cross X in grün.;Verkauft sich gut.;1231234;2;300001;500;1;700;1;1;HL001A;5;3; 200003;Reifen Rennrad Cross X;Reifen für das Rennrad Cross X zum selber montieren.;Reifen Cross X 28 Zoll.;;1231231;0,3;300003;10;1;30;1;1;HL001B;20;10; 200004;Sattel Rennrad Cross X;Sattel für das Rennrad Cross X zum selber montieren.;Sattel Cross X in schwarz.;;12312312;0,2;300003;15;1;25;1;1;HL001B;10;3;

### Stückliste

Um eine Stückliste zu erstellen, sind folgende Punkte zu beachten:

Checkliste für die CSV Datei:

- Pflichtfelder: nummer, stuecklistevonartikel und stuecklistemenge
- Alle Artikel in der Stückliste (auch der Hauptartikel) sind zuvor über den Artikelimport angelegt worden und haben die richtige Artikelnummer **Beispiel für eine Importvorlage:** 1:nummer; 2:stuecklistevonartikel; 3:stuecklistemenge;

Der Haken im Hauptartikel bei Stückliste wird durch den Import automatisch gesetzt.

**Beispielinhalt für die CSV Datei:**

| nummer | stuecklistevonartikel | stuecklistemenge |
| --- | --- | --- |
| 200002 | 200001 | 1 |
| 200003 | 200001 | 2 |
| 200004 | 200001 | 1 |

Bedeutet im vorliegenden Beispiel: Ein Rennrad (Art.Nr. 200001) setzt sich zusammen aus 1 x Rahmen (Art.Nr. 200002), 2 x Reifen (Art.Nr. 200003), 1 x Sattel (Art.Nr.200004) Alle Unterartikel einer Stückliste können auch separat verkauft werden.

### Fremdnummern

Wenn Fremdnummern für externe Verkaufsplattformen importieren werden sollen, kann dies mit Hilfe der internen Artikelnummer in xentral und der externen Nummer, z.B. Amazon SKU, vorgenommen werden. Via CSV-Import kann also die Beziehung zwischen interner und externer Nummer hergestellt werden.

Die Importvorlage würde wie folgt aussehen: 1:nummer; 2:fremdnummerX_shopid;

Anbei ein Beispiel für einen Fremdnummern Import:

- der Shop hat im Beispiel die ID=3 → für die Shop-ID in die Shopschnittstelle klicken (Administration → Einstellungen → Online-Shops → Shop anklicken und oben in der URL die ID ablesen)
- die Artikelnummer lautet: 1000004
- die Fremdnummer lautet: 1234567

Die.csv Datei mit der Fremdnummer wurde folgendermassen definiert, die Reihenfolge der Spalten kann, wie bei jedem Import, beliebig gewählt werden:

- Spalte 1 ist die Artikelnummer → 1000004
- Spalte 2 ist die Fremdnummer → 1234567

Die Importvorlage sieht folgendermaßen aus:

![importexport_17.png](https://help.xentral.com/hc/article_attachments/13755191728412)

> **Anmerkung**
>
> Die 3 bei der Fremdnummer ist die jeweilige Shop-ID, die 1 für die erste Fremdnummer, welche für diesen Artikel importiert wird.

Die Fremdnummer wird dann im Artikel gespeichert.

Shop-ID herausfinden:

Für die Shop-ID ist in die Shopschnittstelle klicken, unter Administration → Shop Schnittstelle → Übersicht ist der betreffende Shop anzuklicken.

![importexport_19.png](https://help.xentral.com/hc/article_attachments/13755191807132)

### Eigenschaften

Checkliste für die CSV Datei:

Pflichtfelder: nummer und eigenschaft1name / eigenschaftnameeindeutig1 und eigenschaft1wert / eigenschaftwerteindeutig1

Alle Artikel sind zuvor über den Artikelimport angelegt worden und haben die richtige Artikelnummer

Hier gibt es 2 Varianten für die Variablen.

**Variante1:** Eigenschaften nicht überschreiben eigenschaftname1 - eigenschaftname20

Eigenschaften mit demselben Namen werden nicht überschrieben. Bsp: Es können 2 Eigenschaften mit dem Name "Farbe" hinterlegt werden, z.B. Farbe = Grün und Farbe = Blau **Variante2:** Eigenschaften überschreiben eigenschaftnameeindeutig1 - eigenschaftnameeindeutig20

Eigenschaften mit demselben Namen werden überschrieben. Bsp: Wenn 2 x hintereinander Eigenschaften mit dem Name "Farbe" importiert werden, dann wird der erste Eigenschaftswert überschrieben.

- Eigenschaftnameeindeutig1: Nur eine Eigenschaft mit dem gleichen Namen ist zugelassen
- Eigenschaft1name: Mehrere Eigenschaften mit unterschiedlichen Werten können angelegt werden **Variante1**

**Beispiel für eine Importvorlage:**

1:nummer; 2:eigenschaftname1; 3:eigenschaftwert1; 4:eigenschaftname2; 5:eigenschaftwert2; 6:eigenschaftname3; 7:eigenschaftwert3;

Beispielinhalt für die CSV Datei:

| nummer | eigenschaftname1 | eigenschaftwert1 | eigenschaftname2 | eigenschaftwert2 | eigenschaftname3 | eigenschaftwert3 |
| --- | --- | --- | --- | --- | --- | --- |
| 200001 | Farbe | Grün | Farbe | Blau | Größe | M |
| 200002 | Farbe | Gelb | Farbe | Blau | Größe | S |
| 200003 | Farbe | Grün | Farbe | Rot | Größe | L |

In diesem Fall sind es nach dem Import 3 Eigenschaften. Z.B. gibt es bei Artikel 200001 die Eigenschaften Farbe: Grün, Farbe: Blau und Größe: M.

**Variante2**

**Beispiel für eine Importvorlage:**

1:nummer; 2:eigenschaftnameeindeutig1; 3:eigenschaftwert1; 4:eigenschaftnameeindeutig2; 5:eigenschaftwert2; 6:eigenschaftnameeindeutig3; 7:eigenschaftwert3;

Beispielinhalt für die CSV Datei:

| nummer | eigenschaftnameeindeutig1 | eigenschaftwert1 | eigenschaftnameeindeutig2 | eigenschaftwert2 | eigenschaftnameeindeutig3 | eigenschaftwert3 |
| --- | --- | --- | --- | --- | --- | --- |
| 200001 | Farbe | Grün | Farbe | Blau | Größe | M |
| 200002 | Farbe | Gelb | Farbe | Blau | Größe | S |
| 200003 | Farbe | Grün | Farbe | Rot | Größe | L |

In diesem Fall sind es nach dem Import nur 2 Eigenschaften. z.B. gibt es bei Artikel 200001 die Eigenschaften Farbe: Blau und Größe: M **Variante mit Übersetzungen**

**Beispiel für eine Importvorlage:**

1:nummer; 2:eigenschaftname1; 3:eigenschaftwert1; 4:eigenschaftname1_fr; 5:eigenschaftwert1_fr;

Beispielinhalt für die CSV-Datei:

| nummer | eigenschaft | wert | eigenschaft_fr | wert_fr |
| --- | --- | --- | --- | --- |
| 700001 | Farbe | Weiß | Couleur | Blanc |
| 700002 | Größe | L | Taille | L |
| 700003 | Material | Baumwolle | Matériau | Coton |

In diesem Fall wird für die Artikel jeweils die Eigenschaft mit der Übersetzung angelegt, z.B. hat der Artikel 700001 die Eigenschaft Farbe: Weiss und dazu die französische Übersetzung der Eigenschaft Couleur: Blanc.

**Eigenschaften**

In den Einstellungen können verschiedene Eigenschaften für den Export angegeben werden.

![importexport_20.png](https://help.xentral.com/hc/article_attachments/13755180599836)

## Charge und MHD

Checkliste für die CSV Datei:

- Pflichtfelder: nummer und lager_platz und lager_menge_addieren und lager_mhd / lager_charge
- Alle Artikel sind zuvor über den Artikelimport angelegt worden und haben die richtige Artikelnummer **Beispiel für eine Importvorlage:** 1:nummer; 2:lager_platz; 3:lager_menge_addieren; 4:lager_mhd; 5:lager_charge;

Beispielinhalt für die CSV Datei:

| nummer | lager_platz | lager_menge_addieren | lager_mhd | lager_charge |
| --- | --- | --- | --- | --- |
| 200001 | HL001A | 10 | 13.10.2020 | 123456 |
| 200002 | HL001A | 15 | 13.10.2020 | 123456 |
| 200003 | HL001A | 23 | 23.10.2020 | 456789 |

Das Resultat des Imports lautet:

- 10 x Artikel 200001 werden eingelagert mit MHD vom 13.10.2020 und Chargen Nr. 123456
- 15 x Artikel 200001 werden eingelagert mit MHD vom 13.10.2020 und Chargen Nr. 123456
- 23 x Artikel 200001 werden eingelagert mit MHD vom 23.10.2020 und Chargen Nr. 456789

> **Anmerkung**
>
> Der Import funktioniert nur mit der Variable lager_menge_addieren und nicht mit lager_menge_total. Mit der Variable “lager_platz” wird das Standardlager geändert, wenn kein Lagerbestand in der Importdatei vorhanden ist. Wenn ein Lagerbestand vorhanden ist, wird der Bestand geändert, nicht das Standardlager.

## Shop Verknüpfungen

Checkliste für die CSV Datei:

- Pflichtfelder: nummer und shop_x und aktiv_x
- Alle Artikel sind zuvor über den Artikelimport angelegt worden und haben die richtige Artikelnummer

Die Variablen shop_ und aktiv_ werden jeweils noch mit der ID des Shops ergänzt. Diese ist in der URL zu finden, wenn eine Shop-Schnittstelle unter Administration → Online-Shops editiert wird.

z.B.... index.php?module=onlineshops&action=edit&id=2

Wäre shop_2 und aktiv_2

Beispiel für eine Importvorlage: 1:nummer; "1":shop_2; "1":aktiv_2;

> **Anmerkung**
>
> "1" ist ein fester Inhalt, damit werden keine weiteren Spalten in der CSV Datei benötigt, um die Option zu aktivieren.

Beispielinhalt für die CSV Datei:

| nummer |
| --- |
| 200001 |
| 200002 |
| 200003 |

### Die wichtigsten Importvariablen für Artikel

| Name in Xentral | Importvariable | Beispielinhalt CSV | Position in Xentral | Anmerkung |
| --- | --- | --- | --- | --- |
| Name | name_de | Rennrad Cross X | Artikel / Details / Artikel | Pflichtfeld falls Artikel neu erstellt wird |
| Artikel Nr. | nummer | 200001 | Artikel / Details / Artikel | Pflichtfeld |
| Artikelbeschreibung (DE) | artikelbeschreibung_de | Rennrad Cross X von Rennprofis empfohlen. | Artikel / Details / Artikel | |
| Kurztext (DE) | kurztext_de | Rennrad Cross X für Profis. | Artikel / Details / Artikel | |
| Artikelkategorie | artikelkategorie_name | Rennräder | Artikel / Details / Artikel | Falls nicht vorhanden in den Einstellungen wird eine Neue angelegt. |
| Interner Kommentar | internerkommentar | Das ist unser Bestseller! | Artikel / Details / Artikel | |
| EAN Nr. | ean | 9783125171541 | Artikel / Details / Artikel | |
| Ermäßigte Umsatzsteuer | umsatzsteuer | ermaessigt | Artikel / Details / Artikel | Möglich in CSV: ermaessigt, normal |
| Gewicht (in kg) | gewicht | 3,1 | Artikel / Details / Artikel | |
| Von Artikel | variante_von | 200010 | Artikel / Details / Artikel | |

Lager

| Lagerartikel | lagerartikel | 1 | Artikel / Details / Artikel | Möglich in CSV: 0, 1 (1 entspricht Lagerartikel, 0 entspricht kein Lagerartikel) |
| --- | --- | --- | --- | --- |
| Lagerbestand | lager_menge_total | 7 | Artikel / Lager | Der Artikel muss ein Lagerartikel sein, s.o. lagerartikel = 1 |
| Min. Lagermenge | mindestlager | 5 | Artikel / Details / Artikel | |
| Standardlager | lager_platz | HL001A | Artikel / Details / Artikel | Hier ist explizit nach dem Regalnamen und nicht dem Lagernamen gefragt |

Stückliste

| In Stückliste | stuecklistevonartikel | 200020 | Artikel / In Stückliste | Gibt Hauptartikel von diesen Stücklistenartikel an |
| --- | --- | --- | --- | --- |
| Stücklistenartikel Menge | stuecklistemenge | 13 | Artikel / In Stückliste | |

Einkaufspreis

| Lieferant | lieferantennummer | 70001 | Artikel / Einkauf | Pflichtfeld für Einkaufspreis - Lieferant muss mit Lieferantennr. in Xentral angelegt sein |
| --- | --- | --- | --- | --- |
| Preis pro Stück | lieferanteinkaufnetto | 700 | Artikel / Einkauf | Pflichtfeld für Einkaufspreis |
| Ab Menge | lieferanteinkaufmenge | 1 | Artikel / Einkauf | Pflichtfeld für Einkaufspreis - Falls Standardpreis (kein Staffelpreis) → als Menge 1 angeben |
| Währung | lieferanteinkaufwaehrung | EUR | Artikel / Einkauf | Pflichtfeld für Einkaufspreis |

Verkaufspreis

| Preis | verkaufspreis1netto | 1100 | Artikel / Verkauf | Pflichfeld für Verkaufspreis |
| --- | --- | --- | --- | --- |
| Ab Menge | verkaufspreis1menge | 1 | Artikel / Verkauf | Pflichtfeld für Verkaufspreis - Falls Standardpreis (kein Staffelpreis) → als Menge 1 angeben |

Charge & MHD

| MHD | lager_mhd | 13.10.2020 | Artikel / Charge + MHD | Im Format: dd.mm.yyyy oder yyyy-mm-dd |
| --- | --- | --- | --- | --- |
| Charge | lager_charge | 123456 | Artikel / Charge + MHD | Erwartet die Chargen Nr. |

Eine vollständige Liste der Importvariablen ist in xentral innerhalb der Importvorlage zu finden.

> **Anmerkung**
>
> Auch bei den Artikeln können Informationen, für welche es kein Feld in xentral gibt, in Freifelder laden. Im Artikel gibt es dazu 40 Stück (Details → Parameter und Freifelder), die mit freifeld1 - freifeld40 importiert werden können. Um diese Felder anzuzeigen müssen diese noch unter Administration → Einstellungen → System → Grundeinstellungen → Freifelder ganz oben bei "Freifelder im Artikel einblenden" aktiviert werden.

### Einkaufspreise (über Herstellernummer)

Mit dem Import von Einkaufspreisen können Lieferantenlisten hinein geladen werden, die statt der Artikelnummer die Herstellernummer mitgegeben haben.

Checkliste für die CSV Datei:

- Pflichtfelder: herstellernummer und lieferantennummer
- Pro Einkaufspreis nur eine Zeile
- Die Lieferanten und Artikel sind davor schon in xentral gepflegt, mit Lieferantennummer und Herstellernummer **Beispiel für eine Importvorlage:** 1:herstellernummer; 2:lieferantennummer; 3:lieferanteinkaufnetto; 4:lieferanteinkaufmenge; 5:lieferanteinkaufwaehrung; 6:lieferanteinkaufnetto2; 7:lieferanteinkaufmenge2; 8:lieferanteinkaufwaehrung2;

Beispielinhalt für die CSV Datei:

| herstellernummer | lieferantennummer | lieferanteinkaufnetto | lieferanteinkaufmenge | lieferanteinkaufwaehrung | lieferanteinkaufnetto2 | lieferanteinkaufmenge2 | lieferanteinkaufwaehrung2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 123456 | 70000 | 10 | 1 | EUR | 8 | 10 | EUR |
| 234567 | 70000 | 11 | 1 | EUR | 9 | 10 | EUR |
| 345678 | 70000 | 14 | 1 | EUR | 10 | 100 | EUR |
| 456789 | 70000 | 15 | 1 | EUR | 10 | 13 | EUR |

## Artikelimport Beispiele

Hier finden sich Beispiele für einen Artikeldaten-Import. In der Praxis hat es sich bewährt, die Artikeldaten nacheinander in mehreren Tabellenlisten und Importformaten einzuspielen. Die Reihenfolge war hier z.B.:

- Import 1: Anlegen der Artikel mit Nummer und Bezeichnung
- Import 2: Einspielen der Verkaufspreise (ggf. Staffeln) auf die bestehenden Artikelnummern
- Import 3: Einspielen der Einkaufspreise mit Lieferantendaten
- Import 4: Nachimport von Artikeldaten → Optional, kann auch in Import 1 direkt mit angelegt werden oder am Ende, wenn alle Preisstrukturen stehen. Wenn zuvor eine Datenbank-Sicherung (Snapshot) gemacht wurde, kann der letze Artikeldaten-Nachimport am Schluss so oft eingespielt und zurückgesetzt werden (Snapshot), bis er endgültig passt.
- Import 5: Import von Gruppenpreisen, wenn dies benötigt wird

Bei Staffelpreisen und komplizierteren Strukturen empfiehlt sich folgender Ablauf:

- Importvorlage in xentral anlegen mit allen relevanten Feldern + speInfo: die Felder der Importvorlage als Text direkt, z.B. als Office Datei, abspeichern und die Einstellungen als Screenshot sichern
- Datenbanksnapshot anlegen. Dabei ist beim Download zu prüfen, ob dieser auch >0Byte ist. Nicht alle Webserver haben die Fähigkeit der Snapshotfunktion. Wenn dies der Fall ist, wird auf dem Server das Programm MySQLDump benötigt
- Import durchführen, jedoch nur im nicht produktiven System
- Wenn der Import nicht komplett passt, kann direkt der Snapshot (s.o.) zurück eingespielt werden. Wenn dieser nach dem Anlegen der Vorlage erstellt wurde, sind alle Daten noch vorhanden. Auf diese Weise können mehrere Iterationen im Import durchgeführt werden.

### Import 1: Artikel anlegen

Artikel können mit einem Schnellimport mit einer bestehenden Nummer oder einer neuen Nummer aus einem Nummernkreis angelegt werden. Sind Artikel von Hand selbst nach zu pflegen, reicht hier auch die Artikelnummer, die Artikelbezeichnung und ggf. das Setzen des Lagerhakens über Lagerartikel → Artikel, welcher im Lager auf Bestand liegt: Folgende Felder sind hier sinnvoll, je nachdem welche Artikelebenen zu bewältigen sind:

- Artikelnummer → Die bestehende Nummer ist in die Spalte eintragen oder aus zentralen Nummernkreis fortlaufend neu zu vergeben (Spalteninhalt: NEU)
- "Artikelnummer neu vergeben aus Artikelkategorie" setzt voraus, dass die Artikelkategorie angelegt wurde und hier eine nächste, zu vergebene Artikelnummer eingetragen wurde
- Projekt für Artikel vergeben → Projekt ID in einer Spalte mit aufnehmen
- Artikelkategorie vergeben → Artikelkategorie ID in einer Spalte mit aufnehmen
- Haken → Artikel ist Lagerartikel. 1=Artikel wird im Lager geführt. Leer bei Dienstleistungsartikeln
- Umsatzsteuersatz → Ohne Angabe werden die Artikel auf 19% gesetzt (Steuer Inland Standard), für den ermässigten Satz z.B. 7% hier in die Spalte "ermaessigt" angeben

Wenn es keine Artikelnummern gibt und diese neu fortlaufend vergeben werden sollen, kann in die Spalte der Artikelnummer "NEU" eingetragen werden. Alternativ kann auch direkt im Tabellenprogramm die erste Nummer angegeben und in der Spalte die fortlaufenden Nummern nach unten gezogen werden. Dadurch liegen diese für den Import in die Tabelle bereits vor.

![importexport_21.png](https://help.xentral.com/hc/article_attachments/13755159255964)

![importexport_22.png](https://help.xentral.com/hc/article_attachments/13755152694044)

Beispiel für eine Importvorlage: 1:nummer; 2:name_de; 3:projekt; 4:artikelkategorie; 5:lagerartikel;

### Import 2: Verkaufspreise

Verkaufspreise können in einem weiteren Import direkt auf bestehende Artikelnummern importiert werden. Die wichtigsten Felder sind folgende:

- Artikelnummer
- Verkaufspreis (netto)
- Menge (meist "1")

Für einen Artikel können auch Staffelpreise importiert werden (z.B. 1, 10, 100, 1000). Wenn du beim Import eines neuen Preises ein Gültigkeitsdatum vergeben möchtest, achte bitte darauf, dass das Datumsformat in der CSV-Datei yyyy-mm-dd sein muss. Da je nach Programm beim Erstellen der CSV-Datei dieses Format häufig automatisch überschrieben wird, solltest du die Formatierung umstellen auf "Text".

> **Anmerkung**
>
> Der Verkaufspreis wird als Standardpreis für alle Kunden importiert. Jede Menge darf hier für einen Artikel nur einmal vorhanden sein.

Beispiel für eine Importvorlage: 1:nummer; 2:verkaufspreis1netto; 3:verkaufspreis1menge; 4:verkaufspreis2netto; 5:verkaufspreis2menge; 6:verkaufspreis3netto; 7:verkaufspreis3menge; 8:verkaufspreis4netto; 9:verkaufspreis4menge;

> **Anmerkung**
>
> Wenn du einen Verkaufspreis aktualisieren willst, kannst du durch den CSV Import von einem geänderten Preis mit den ansonsten gleichen Parametern wie Menge, Gruppenzuordnung und Währung einen neuen Preis erzeugen. Der alte Preis mit den gleichen Parametern wird dadurch inaktiv gesetzt.

### Import 3: Einkaufspreis/ Lieferantendaten

Einkaufspreise können in einem weiteren Import ebenso auf bestehende Artikelnummern importiert werden. Die wichtigsten Felder sind folgende:

- Artikelnummer
- Lieferantennummer aus xentral
- Netto Einkaufspreis bei entsprechendem Lieferanten
- Menge (im Standard 1 Stck.)
- Artikel Bestellnummer bei entsprechendem Lieferanten

Beispiel für eine Importvorlage: 1:nummer; 2:lieferantennummer; 3:lieferanteinkaufnetto; 4:lieferanteinkaufmenge; 5:lieferantbestellnummer;

Soll ein Artikel bei allen Lieferanten einkaufbar sein, muss im Artikel der Haken "Einkauf bei allen Lieferanten" gesetzt werden. Ein Preis wird in diesem Fall nicht importiert.

#### Einkaufspreise mit neuen Preisen ersetzen

EK Preise können aktualisiert werden und der "alte" EK Preis erhält automatisch ein Gültigkeitsdatum, das bis zum gestrigen Datum eingetragen ist.

Dafür müssen aber folgende Daten vom alten und neuen EK übereinstimmen:

- Menge (ab)
- Währung
- Bezeichnung (falls vorhanden)
- Bestellnummer (falls vorhanden)

### Import 4: Nachimport Artikeldaten

Folgende Artikeldaten können z.B. auch in einem Nachimport später importiert werden, wobei ein sofortiger Import in Schritt 1 möglich wäre:

- Artikelbeschreibung, welche z.B. dann auch bei Dokumenten (Rechnung, Auftrag, etc.) angezeigt wird
- Kurztext → Ein optionaler, zusätzlicher Text kann eingegeben werden
- Interner Kommentar → Dieser ist optional, z.B. für die Suche durchsuchbar
- EAN → Die EAN Nummer des Artikels ist zu einzutragen
- Gewicht → Das Gewicht, das z.B. bei der Paketmarke mit ausgewertet werden kann, wie das Gesamtgewicht der Lieferung, ist anzugeben
- Lagerplatz → Der Lagerplatz, z.B. Standardlager und Lager für die Einlagerung, wie Lagerplatz Ebene 2, "Regal" in xentral, ist anzugeben
- Lagermenge → Die absolute Menge für die Einlagerung in ein Lager ist anzugeben
- Mindestlager → Die Mindestlagermenge, z.B. für den Bestellvorschlag, ist anzugeben

Grundsätzlich können alle Eigenschaften eines Artikels überschrieben werden, zu welchen Variablen in der Import-Zentrale vorhanden sind. Notwendig ist hierbei, dass die Nummer als Referenz angegeben wird. Andernfalls entsteht kein Update, sondern nur eine Artikelneuanlage.

Beispiel für eine Importvorlage: 1:nummer; 3:artikelbeschreibung_de; 4:kurztext_de; 5:internerkommentar; 6:ean; 7:gewicht; 14:lager_platz; 15:lager_menge_total; 16:mindestlager;

### Import 5: Gruppenpreise Beispiel

Im Folgenden ist ein Beispiel für Gruppenpreise aufgezeigt:

Beispiel für eine Importvorlage: 1:nummer; 2:verkaufspreis1netto; 3:verkaufspreis1menge; 4:verkaufspreis1gruppe; 5:verkaufspreis2netto; 6:verkaufspreis2menge; 7:verkaufspreis2gruppe; 8:verkaufspreis3netto; 9:verkaufspreis3menge; 10:verkaufspreis3gruppe;

## Artikel Lagermengen importieren

Für den Import von Artikelmengen wird die Artikelnummer, die Lagermenge, d.h. die absolute Bestandsmenge für diesen Platz oder die neu hinzukommende Menge, d.h. die additive Bestandsmenge für diesen Lagerplatz, und der Lagerplatz selbst benötigt. Für den Import der Lagermenge kann die EAN statt der Artikelnummer zur Zuordnung verwendet werden.

Beispiel für eine Importvorlage:

1:nummer;

2:lager_platz2;

3:lager_menge_total2;

4:lager_platz3;

5:lager_menge_total3;

6:lager_platz4;

7:lager_menge_total4;

Folgende Angaben sind zudem möglich:

- lager_menge_addieren2 → Bucht die Menge des Artikels auf die bestehende Menge in diesem Lagerplatz auf
- lager_menge_total2 → Bucht die Menge (total) des Artikels komplett neu ein

## Zeiterfassung

Mit dem Import für die Zeiterfassung, können Zeiten auf einen Kunden gebucht werden. Diese sind danach an 3 Stellen wiederzufinden:

- Im Zeitkonto Modul: Team → Zeitkonten → Zeitkonto → Zeiten abrechnen
- In den Stammdaten des Kunden: Stammdaten → Adressen → Kunden auswählen → Zeitkonto
- In der eigenen Zeiterfassung: Team → Zeiterfassung → Eigene Zeiterfassung Übersicht

Checkliste für die CSV Datei:

- Pflichtfelder: datum_von, zeit_von, datum_bis, zeit_bis, taetigkeit, kundennummer
- Der Kunde muss mit der entsprechenden Kundennummer in Xentral angelegt sein
- Falls auf Mitarbeiter gebucht wird muss der Mitarbeiter in Xentral angelegt sein

Beispiel für eine Importvorlage: 1:datum_von; 2:zeit_von; 3:datum_bis; 4:zeit_bis; 5:taetigkeit; 6:details; 7:kundennummer; 8:mitarbeiternummer;

Beispielinhalt für die CSV Datei:

20.09.2016;09:00;20.09.2016;18:00;Außentermin bei Kunden.;Neue Produkte vorgestellt.;10000;2500;

21.09.2016;09:00;21.09.2016;17:30;Präsentation erarbeitet.;Präsentation über neue Produktpalette XY.;10002;2500;

22.09.2016;09:30;22.09.2016;18:30;Workshop geben im Auftrag vom Kunden; Workshop zur besseren Einarbeitung der Mitarbeiter.;10003;2500;

### Eigene Zeiterfassung Übersicht

Die Übersicht der eigenen Zeiterfassung kann sich so gestalten:

![importexport_23.png](https://help.xentral.com/hc/article_attachments/13755165617180)

## Wiedervorlagen

Es können auch Wiedervorlagen nach xentral importiert werden.

Checkliste für die CSV Datei:

- Pflichtfelder: datum_faellig, kundennummer, mitarbeiternummer, betreff
- Der Kunde muss mit der entsprechenden Kundennummer in xentral angelegt sein
- Der Mitarbeiter muss mit der entsprechenden Mitarbeiternummer in xentral angelegt sein
- Das "Ziel" in der Importvorlage muss auf "Wiedervorlagen" stehen.

**Beispiel für eine Importvorlage:** 1:datum_faellig; 2:uhrzeit_faellig; 3:kundennummer; 4:mitarbeiternummer; 5:betreff; 6:text; 7:abgeschlossen;

Beispielinhalt für die CSV Datei:

25.01.2017;14:00;10000;90000;Kunden anrufen wegen Angebot;Nochmal nachfragen wegen des letzten Angebots;0;

13.01.2017;10:30;10001;90006;Bei der Entwicklung nachfragen;Status des neuen Features bei der Entwicklung nachfragen;1;

Nach dem Import können die Wiedervorlagen unter Stammdaten → Adressen → Korrespondenz → Wiedervorlage eingesehen werden:

![importexport_24.png](https://help.xentral.com/hc/article_attachments/13755165683868)

### Notizen

Notizen können ebenfalls nach xentral importiert werden.

Checkliste für die CSV Datei:

- Pflichtfelder: datum, kundennummer, mitarbeiternummer, betreff
- Der Kunde muss mit der entsprechenden Kundennummer in xentral angelegt sein
- Der Mitarbeiter muss mit der entsprechenden Mitarbeiternummer in xentral angelegt sein
- Das "Ziel" in der Importvorlage muss auf "Notiz" stehen.

**Beispiel für eine Importvorlage:** 1:datum; 2:uhrzeit; 3:kundennummer; 4:mitarbeiternummer; 5:betreff; 6:text;

Beispielinhalt für die CSV Datei:

25.01.2017;14:00;10000;90000;Kunden angerufen wegen Angebot;Nochmal nachgefragt wegen des letzten Angebots;

13.01.2017;10:30;10001;90006;

Bei der Entwicklung nachgefragt;Status des neuen Features bei der Entwicklung: Fertigstellung in KW2;

![importexport_25.png](https://help.xentral.com/hc/article_attachments/13755180864156)

Nach dem Import können die Wiedervorlagen unter Stammdaten → Adressen → Korrespondenz → Notizen eingesehen werden.

## Artikel-Provisionen

Über den Stammdatenimport können auch Provisionen auf einen bestehenden Artikel importiert werden.

Hinweis: Provisionsabrechnung ist ein extra Modul.

Checkliste für die CSV Datei:

- Pflichtfelder (nur Vertreter): artikel, vertreter_provision und vertreter_provisionsart
- Pflichtfelder (Vertreter & Vertriebsleiter): artikel, vertreter_provision, vertreter_provisionsart, vertriebsleiter_provision, vertriebsleiter_provisionsart
- Pro Artikel-Provision nur eine Zeile
- Jede Artikelnummer ist nur einmal vorhanden und bereits in xentral angelegt **Beispiel für eine Importvorlage (Vertreter und Vertriebsleiter):** 1:artikel; 2:vertreter; 3:vertreter_provision; 4:vertreter_provisionsart; 5:vertriebsleiter_provision; 6:vertriebsleiter_provisionsart; 7:gueltig_von; 8:gueltig_bis;

Beispielinhalt für die CSV Datei:

700010;6;6;vk;1;vk;01.01.2019;31.12.2019;

700007;6;6;vk;1;vk;01.01.2019;31.12.2019;

700002;4;5;ek;1;ek;01.01.2019;31.12.2019

Bedeutet im vorliegenden Beispiel: Unter Buchhaltung → Provisionen → Provisionen pro Artikel können die importierten Provisionen betrachtet werden:

![importexport_26.png](https://help.xentral.com/hc/article_attachments/13755192392092)

> **Anmerkung**
>
> Um zusätzlich die Provision des Vertriebsleiters anzugeben, sind die Importvariablen 'vertriebsleiter_provision' und 'vertriebsleiter_provisionsart' nötig. Zuvor muss der Vertriebsleiter einem Vertreter zugeordnet werden, dies kann auch über einen CSV Import erfolgen. Die Vertreter- und Vertriebsleiter Verknüpfung wird direkt im Modul "Provisionen" angelegt/importiert.

### Die wichtigsten Importvariablen für Artikel-Provisionen

Die nachstehenden Variablen sind die wichtigsten Importvariablen für Artikel-Provisionen:

| Name in Xentral | Importvariable | Beispielinhalt CSV | Position in Xentral | Anmerkung |
| --- | --- | --- | --- | --- |
| Name | name | Max Mustermann | Adressen / Details / Adressdaten | Pflichtfeld - Kann auch für Firma genommen werden |
| Anrede | typ | Herr | Adressen / Details / Adressdaten | Erwartet: Herr, Frau, Firma, Mr, Mrs, Company |
| Kundennummer | kundennummer | 100001 | Adressen / Details / Zahlungskonditionen/Besteuerung (16.3+) | Pflichtfeld (bei Kunden) - Nicht doppelt vergeben |
| Lieferantennummer | lieferantennummer | 200001 | Adressen / Details / Zahlungskonditionen/Besteuerung (16.3+) | Pflichtfeld (bei Lieferanten) - Nicht doppelt vergeben |
| Mitarbeiternummer | mitarbeiternummer | 30001 | Adressen / Details / Zahlungskonditionen/Besteuerung (16.3+) | Pflichtfeld (bei Mitarbeiter) - Nicht doppelt vergeben |
| Ansprechpartner | ansprechpartner | Hildegard Müller | Adressen / Details / Adressdaten | |
| Adresszusatz | adresszusatz | Apartment | Adressen / Details / Adressdaten | |
| Straße | strasse | Untere Talstr. 13 | Adressen / Details / Adressdaten | |
| Ort | ort | Augsburg | Adressen / Details / Adressdaten | |
| PLZ | plz | 86159 | Adressen / Details / Adressdaten | |
| Land | land | DE | Adressen / Details / Adressdaten | Wichtig: Nur ISO Code (DE, AT, NL, etc.) |
| Telefon | telefon | 0123456789 | Adressen / Details / Adressdaten | |
| Telefax | telefax | 0987654321 | Adressen / Details / Adressdaten | |
| Anschreiben | anschreiben | Sehr geehrter Herr Mustermann | Adressen / Details / Adressdaten | |
| E-Mail | email | max-mustermann@email.de | Adressen / Details / Adressdaten | |
| Mobil | mobil | 0170123456 | Adressen / Details / Adressdaten | |
| Internetseite | internetseite | [http://example.com](http://example.com/) | Adressen / Details / Adressdaten | |
| Ust-Id | ustid | 12354567 | Adressen / Details / Zahlungskonditionen/Besteuerung (16.3+) | |
| Sprache für Belege | sprache | deutsch | Adressen / Details / Adressdaten | Möglich in CSV: deutsch, englisch |
| Gruppen | gruppe1 | Geschäftskunde | Adressen / Gruppen | Die Gruppe muss zuvor in Xentral angelegt sein |
| Sonstiges | sonstiges | Ein sehr treuer Kunde | Adressen / Details / Adressdaten | |
| **Name in Xentral **|** Importvariable **|** Beispielinhalt CSV **|** Position in Xentral **|** Anmerkung** |

Hinweis: Sollten Änderungen an den Provisionen per Import erfolgen, ist es notwendig, alle bisherigen Provisionen zu löschen.

## Matrix Produkte

Alle Informationen zur Bedienung von Matrixprodukten sind unter[Matrixprodukt](https://help.xentral.com/hc/de/articles/360016725120#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29)zu finden. Zunächst ist ein Matrixprodukt als Artikel anzulegen, falls noch nicht vorhanden.

> **Anmerkung**
>
> Über die Importzentrale können maximal zwei Dimensionen importiert werden. Artikel mit mehr Dimensionen können direkt über die Oberfläche des Matrixprodukts erzeugt werden. Informationen dazu findest duhier.

Checkliste für die CSV Datei:

- Pflichtfelder: nummer, matrixprodukt, matrixproduktvon, matrixproduktgruppe1 und matrixproduktwert1
- Ein Hauptartikel (Matrixartikel) muss davor bereits in xentral angelegt sein und in der CSV in der Spalte matrixproduktvon stehen
- Es empfiehlt sich, die Unterartikel ebenfalls als normale Artikel schon in xentral angelegt zu haben, um mit dem Matrixartikel-Import nur noch die Artikel in ein Matrixprodukt zu verknüpfen. Andernfalls ist ein Namen anzugeben, da sonst alle Matrixunterprodukte gleich heißen.

Beispiel für eine Importvorlage:

1:nummer;

2:matrixprodukt;

3:name_de;

4:matrixproduktvon;

5:matrixproduktgruppe1;

6:matrixproduktwert1;

7:matrixproduktgruppe2;

8:matrixproduktwert2;

Beispielinhalt für die CSV-Datei:

| nummer | matrixprodukt | name_de | matrixproduktvon | matrixproduktgruppe1 | matrixproduktwert1 | matrixproduktgruppe2 | matrixproduktwert2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 201313-BS | 1 | T-Shirt Farbe: Blau - Größe: S | 201313 | Farbe | Blau | Größe | S |
| 201313-BM | 1 | T-Shirt Farbe: Blau - Größe: M | 201313 | Farbe | Blau | Größe | M |
| 201313-BL | 1 | T-Shirt Farbe: Blau - Größe: L | 201313 | Farbe | Blau | Größe | L |
| 201313-RS | 1 | T-Shirt Farbe: Rot - Größe: S | 201313 | Farbe | Rot | Größe | S |
| 201313-RM | 1 | T-Shirt Farbe: Rot - Größe: M | 201313 | Farbe | Rot | Größe | M |
| 201313-RL | 1 | T-Shirt Farbe: Rot - Größe: L | 201313 | Farbe | Rot | Größe | L |

Das bedeutet im vorliegenden Beispiel: Ein Matrixprodukt (201313) wird erstellt, die Unterartikel (201313-BS, 201313-BM, etc) als Artikel dieses Matrixprodukts markiert. Für diese Unterartikel werden 2 Matrixeigenschaften (Farbe, Größe) vergeben und verschiedene Werte mitgegeben. Wenn du bei der Variable Matrixprodukt 1 angibst, dann wird bei diesem Artikel der Haken bei Matrixprodukt gesetzt. Im Beispiel würden dann alle Varianten selbst auch als Matrixprodukt gekennzeichnet werden, nicht nur 201313.

![importexport_27.png](https://help.xentral.com/hc/article_attachments/13755166011548)

## Artikelkategorien im Artikelbaum mehreren Artikeln über die Importzentrale zuweisen

Du kannst gleichzeitig mehrere Kategorien im Artikelbaum mehreren Artikeln in deinen Stammdaten zuweisen, indem du die Importzentrale verwendest. Um die Kategorien korrekt zuzuweisen, müssen die folgenden Voraussetzungen erfüllt sein:

- Die Artikel sind bereits in den Stammdaten angelegt
- Die benötigten [Kategorien und Unterkategorien wurden im Artikelbaum](https://help.xentral.com/hc/de/articles/13755178574748#UUID-eb54ff2b-e31a-4c0a-9e21-47b7c87bc184_N1713367556954) angelegt.

Gehe wie folgt vor, um Kategorien mehreren Artikeln zuzuweisen:

1. Erstelle eine Tabelle in einem Tabellenkalkulationsprogramm deiner Wahl, welches die folgenden Spalten enthält:
  Auf dem folgenden Screen siehst du ein Beispiel, wie so eine Tabelle aussehen kann:

  - nummer: Gib deine Artikelnummern in dieser Spalte ein.
  - artikelkategorie_name: Gib den Namen der Root-Kategorie, die du bearbeiten möchtest, z.B. Handelsware oder Produktionsmaterial, in dieser Spalte an.
  - artikelbaum1: Gib den kompletten Pfad für die gewünschte Unterkategorie in dieser Spalte an. Die einzelnen Einträge im Pfad werden durch das Pipe-Zeichen | getrennt. Möchten wir, z.B. einen Artikel in der Kategorie Frauenkleidung einordnen, könnte der Pfad so aussehen: Handelsware|Kleidung|Damen.
  Um deinem ausgewählten Artikel eine zweite Kategorie zuzuweisen, musst du eine weitere Spalte mit dem Titel artikelbaum2 hinzufügen, für eine dritte Kategorie artikelbaum3, und so weiter. Du kannst auf diese Weise bis zu 20 Kategorien zuweisen.

1. Exportiere die Tabelle in eine CSV-Datei. Du kannst als Separatoren Kommas oder Semikolons nutzen.
1. Melde dich in Xentral an und öffne die Import / Export Zentrale über die Smart Search.
1. Klicke auf Stammdaten Import und dann auf + Neuer Eintrag
1. Erstelle eine Importvorlage:
1. Öffne den Reiter Import starten: CSV Datei heraufladen in der Importvorlage.
1. Klicke auf Browse und wähle die CSV-Datei von deinem Computer oder ziehe alternativ die CSV-Datei per Drag & Drop auf die Browse-Schaltfläche. In den meisten Fällen kannst du den Standardwert unter Kodierung belassen.
1. Klicke auf CSV jetzt heraufladen. Du bekommst eine Vorschau der importierten Daten und kannst sie vor dem Import noch einmal prüfen.
1. Klicke auf Importieren. Der Import wird in eine Warteschlange eingereiht und nach wenigen Minuten bearbeitet.

Nachdem der Import abgeschlossen ist, werden alle Kategorien auf die Artikel deiner CSV-Datei angewendet.

## Gambio Artikelimport Beispiel (Stand 04/2017 - Gambio Shop 3.1)

Die fett gedruckten Felder sind Pflichtfelder/ bzw. die relevanten Felder für die Zuordnung der Artikel.

Beispiel für einen Export aus Gambio:

Feldeinstellungen:

1: {products_model} → Artikelnummer des Produkts {p_model} → alternativ Artikelnummer des Produkts inkl. Eigenschaften

2: {products_name.de} → Produktname {p_name.de} → alternativ Produktname inkl. Eigenschaften

3: {p_description.de} → Produktbeschreibung

4: {p_short_description.de} → Produktkurzbeschreibung

5: {products_ean} → EAN{p_ean} → alternativ EAN mit Eigenschaften

6: {p_weight_comma} → Produktgewicht

7: {c_name.de} → Kategorie

8: {p_manufacturer_name} → Hersteller

Beispiel für einen Artikelimport in xentral:

1:nummer;

2:name_de;

3:artikelbeschreibung_de;

4:kurztext_de;

5:ean;

6:gewicht;

7:artikelkategorie_name;

8:hersteller;

9:lagerartikel;

10:umsatzsteuer;

Beispielinhalt für die CSV-Datei:

| nummer | name_de | artikelbeschreibung_de | kurztext_de | ean | gewicht | artikelkategorie_name | hersteller | lagerartikel | umsatzsteuer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100001 | Schraube M10x20 | Bavaria ipsum dolor sit amet boarischer Ewig und drei Dog Gidarn. A so a Schmarn Gamsbart oba Enzian Haferl di Vergeltsgott middn. | Bavaria ipsum dolor sit amet boarischer Ewig und drei Dog Gidarn. | 1234567891011 | 0,1 | Metallwaren | Bavaria ipsum | 1 (für ja, 0 für nein) | ermaessigt (falls der Artikel eine ermäßigte UST hat, beim normalen UST - Satz einfach das Feld leer lassen) |

## Hinzufügen von Shop-Texten

Ab der Version 20.1 können über eine Zeile auch mehrere Texte zu einem Shop hinzugefügt werden. Es kann pro Shop nur eine Übersetzung hinterlegt werden. Darüber hinaus werden alle neu hinzugefügten Texte standardmäßig als inaktiv angelegt, d.h. der Binärwert für "active" muss mitgegeben werden, wenn diese direkt auch aktiv geschaltet sein sollen.

**Beispiel Importvorlage**

![importexport_30.png](https://help.xentral.com/hc/article_attachments/13755166178204)

Beispiel für die CSV-Datei:

Artikelnummer;Name_FR;Kurztext_FR;Beschreibung_FR;Shop;Shop-

Text_FR;Name_IT;Kurztext_IT;Beschreibung_IT;Shop-Text_IT;Shop_IT; 700001;grenouille;Das ist ein

Kurztext(FR);Hier sehen wir eine Beschreibung;5;Online-Text für

Ebay(FR);rana;KurztextIT;BeschreibungIT;ShoptextIT;5;

## Formate

Wenn du in der **Import/Export Zentrale ** unter **Stammdaten Import ** einen neuen Eintrag anlegst, findest du im Reiter**Formate** eine große Auswahl an verfügbaren Variablen. Mehr zu den Variablen, die du in Xentral verwenden kannst, findest du im Artikel[Variablen](https://help.xentral.com/hc/de/articles/5091351567388#UUID-740920b3-8105-5183-b441-2c247de21390).