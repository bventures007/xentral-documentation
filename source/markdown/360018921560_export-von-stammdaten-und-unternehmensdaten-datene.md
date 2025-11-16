## Eine neue Exportvorlage anlegen

Diese Artikel zeigt, wie eine neue Exportvorlage anzulegen ist. Für weitere Informationen steht der Artikel[Import/Export](https://help.xentral.com/hc/de/articles/360016758939#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574)zu Verfügung.

Über folgenden Pfad kann eine Exportvorlage erstellt werden: **Stammdaten > Import-/Exportzentrale > Stammdaten Export > "+NEU"**.

Um eine neue Exportvorlage anzulegen, ist folgendermaßen vorzugehen:

![exportmastercompanydata_1.png](https://help.xentral.com/hc/article_attachments/5091283955612)

Folgende Angaben können allgemein gemacht werden:

- **Bezeichnung:** Beliebiger Name für die Export-Vorlage ist anzugeben
- **Quelle:** Die Auswahl der Art des Datendownloads ist hier möglich. Aus dem Dropdown-Menü kann ausgewählt werden: Adresse, Angebot, Auftrag, Ansprechpartner, Artikel, Gutschrift, Rechnung, Lieferschein, Bestellung, Angebot Positionen, Auftrag Positionen, Rechnung Positionen, Gutschrift Positionen, Lieferschein Positionen, Bestellung Positionen
- **CSV Beschriftung:** Durch Anhaken wird die erste Zeile der CSV-Datei als Beschriftung verwendet
- **CSV Trennzeichen:** In der CSV-Datei verwendetes Trennzeichen, mit dem Daten von einander getrennt sind
- **CSV Maskierung:** In der CSV-Datei verwendetes Maskierungszeichen ist optional auszuwählen
- **Filter Datum:** Durch Anhaken wird bei der Ausgabe nach Datum gefiltert
- **Filter Projekt:** Durch Anhaken wird bei der Ausgabe nach Projekt gefiltert
- **API Freigabe:** Durch Anhaken wird das Abfragen über API möglich
- **CSV-Felder:** Hier sind die Exportvariablen einzutragen
- **Filter: ** Hier können Filter für den Download gesetzt werden.** Hinweis:** Die Operationen sind AND-Operationen und keine OR-Operationen. Es wird nach Einträgen gesucht, die „alle Bedingungen“ erfüllen und nicht „mindestens eine davon“

> **Anmerkung**
>
> Es kann in der Exportvorlage nur nach Spalten gefiltert werden, die auch in der entsprechenden Tabelle vorhanden sind.

### Export Rechnungen mit bestimmter Zahlungsweise

Um Rechnungen mit bestimmter Zahlungsweise exportieren zu können, sind folgende Angaben zu machen:

![exportmastercompanydata_2.png](https://help.xentral.com/hc/article_attachments/13439940953116)

### Export Erlöse mit Vertrieb

Es ist möglich, Daten aus einer CSV-Datei herunterzuladen. Diese könnte z.B. so aussehen:

![exportmastercompanydata_3.png](https://help.xentral.com/hc/article_attachments/13439924646172)

Um die Erlöse, die durch den Vertrieb entstanden sind, zu exportieren, ist folgende Exportvorlage anzulegen:

![exportmastercompanydata_4.png](https://help.xentral.com/hc/article_attachments/13439942906524)

### Belegdaten Export

Diverse Belegdaten können ebenfalls exportiert werden.

#### Export der Positionen einer Bestellung

Wie Positionen aus einer Bestellung exportiert werden können, ist nachstehend nachzulesen.

![exportmastercompanydata_5.png](https://help.xentral.com/hc/article_attachments/13439913516572)

Folgende Felder können aus einer CSV-Datei exportiert werden:

- beleg_name
- beleg_belegnr
- beleg_datum
- beleg_status
- bp.sort: Sortierreihenfolge der Positionen
- bp.bestellnummer: Bestellnummer beim Lieferanten
- bp.bezeichnunglieferant: Bezeichnung beim Lieferanten
- bp.preis: Hier ist der Einzelpreis als Belegposition eingetragen
- bp.menge: Hier ist die Menge die Belegposition eingetragen
- bp.nummer: Hier ist die Artikelnummer als Belegposition einzutragen

Mit diesen Felder können Einstellungen im Tab Details vorgenommen werden.

![exportmastercompanydata_6.png](https://help.xentral.com/hc/article_attachments/13439930932124)

### Artikel Export

Im Folgenden ist ein Beispiel für eine mögliche Exportvorlage einzusehen, welche verwendet wird, um Artikeldaten aus dem System zu ziehen.

![exportmastercompanydata_7.png](https://help.xentral.com/hc/article_attachments/13439913613596)

> **Anmerkung**
>
> Es können gelöschte Artikel aus den Export-Dateien gefiltert werden, indem in das Feld "Filter" "nummer not like 'DEL';" eingetragen wird.

### Adressen Export

Für den Export von Adressdaten können verschiedene Felder ausgegeben werden. Anbei sind einige Beispiele aufgeführt.

**Kundennummer und Projekt ** Eine Liste aller Kunden/Lieferanten eines Projekts wird oftmals benötigt, um den anschließenden Nachimport, die Änderung einer Einstelloption oder eines Feldes in dem Adresssatz vornehmen zu können. **Export der Liste aller Kundennummern eines Projekts**

Um alle Kundennummern eines Projekts als Liste zu exportieren, ist folgende Exportvorlage anzulegen:

![exportmastercompanydata_8.png](https://help.xentral.com/hc/article_attachments/13439931048348)

Verwende hierfür folgende Exporteinstellungen:

- **Quelle:** Wähle "Adresse" aus dem Dropdown-Menü
- **Filter Projekt:** Durch Anhaken kann bei der Ausgabe ein Projekt ausgewählt werden
- **CSV Felder:** Trage "kundennummer" ein, um die Kundennummer in der ersten Spalte zu exportieren
- **Filter:** Trage "kundennummer!='';" ein, um die Bedingung zu setzen, dass alle Kunden bzw. alle Adressen, bei denen die Kundennummer nicht leer ist, gefiltert werden.

> **Anmerkung**
>
> Der Download der CSV Datei erfolgt über den Tab Export starten: CSV Datei herunterladen.

![exportmastercompanydata_9.png](https://help.xentral.com/hc/article_attachments/13439925096220)

Projektauswahl

Wähle im Tab **Export starten: CSV Datei** herunterladen in der Übersicht das Projekt "STANDARD" aus, wenn nach diesem gefiltert werden soll.

![exportmastercompanydata_10.png](https://help.xentral.com/hc/article_attachments/13439941543068)

**CSV-Liste ** Folgende Export-Liste erscheint als Ergebnis nachdem du auf **Download** klickst.

![exportmastercompanydata_11.png](https://help.xentral.com/hc/article_attachments/13439941605020)

Diese Export-Liste kann überarbeitet und erweitert werden, um für Bestandskunden neue Nachimports durchzuführen. Sofern die Kundennummern eindeutig sind, können diese normal verwendet werden. Die System-ID kann beim Import als Spalte einfach weggelassen werden.

> **Anmerkung**
>
> Statt der Kundennummer für den Adresssatz kann die SystemID für den Import verwendet werden. Wird die ID nicht benötigt, kann sie in der bearbeiteten Datei als Spalte bestehen bleiben und ein Import dieser Spalte ausgelassen werden.

#### Adresse mit Liefersperre

Es ist zudem möglich, alle Adressen mit einer Liefersperre zu exportieren. Falls eine Kundennummer vorhanden ist, wird diese in der ersten Spalte ausgegeben.

![exportmastercompanydata_12.png](https://help.xentral.com/hc/article_attachments/13439931303964)

#### Adresse mit Postleitzahlenbereich und Telefonnummer

Für den Vertrieb können Listen der Kundenadressen über einen bestimmten Postleitzahlenbereich ausgegeben werden:

![exportmastercompanydata_13.png](https://help.xentral.com/hc/article_attachments/13439931378332)

Wird nur ein Postleitzahlenbereich als Ausgabe gewünscht, kann zusätzlich im Bereich **Filter** eine Eingrenzung vorgenommen werden. In diesem Beispiel sind die Postleitzahlen zwischen 80000 und 90000 gewünscht. Die Eingabe lautet daher: plz > 80000 AND plz < 90000;

Im Filter kannst du zusätzliche Bedingungen angeben:

- lieferantennummer!='': Alle Lieferanten, deren Lieferantennummer nicht leer ist, werden gefiltert
- land='GB': Es wird der Filter für das Land Großbritannien (GB) gesetzt
- lagerartikel='0': Falls keine Lagerartikel angezeigt werden sollen, ist dieser Filter zu setzen
- stueckliste='0': Falls keine Stücklisten-Hauptartikel angezeigt werden sollen, ist dieser Filter zu setzen
- nummer!='DEL': Falls keine gelöschten Artikel anzeigt werden sollen, ist dieser Filter zu setzen
- intern_gesperrt='0': Falls keine gesperrten Artikel angezeigt werden sollen, ist dieser Filter zu setzen **Lieferscheinadressen mit Bedingung**

SELECT l.belegnr,l.datum,l.name,l.abteilung,l.adresszusatz,l.unterabteilung,l.land,l.strasse,l.ort

FROM lieferschein l LEFT JOIN lieferschein_position lp ON lp.lieferschein=l.id

WHERE lp.artikel=4 AND l.datum>='2017-12-01' AND l.datum ⇐'2017-12-31'