Berichte geben dir die Möglichkeit, deine Daten in Xentral auszuwerten. Ob datengetriebenes Management deiner Artikel und Verkaufskanäle, ein schneller Überblick über deine Kundenumsätze oder die Optimierung deiner Lager-Performance - Berichte sind der perfekte Startpunkt, um Potenziale und Problemfelder in deinem Geschäft aufzudecken.

Für Einsteiger in die Datenanalyse erleichtert die intuitive No-Code-Oberfläche und die Auswahl an vordefinierten Berichtsvorlagen den Start. Diese Vorlagen, entwickelt aus der Praxis der wichtigsten Geschäftsmodelle und der Erfahrung von Experten, bieten sofort einsatzbereite Einblicke. Erfahrene Nutzer können die erweiterten Funktionen des SQL-Editors nutzen und von der modernen Datenbanktechnologie AWS Redshift profitieren, die schnelle und zeitnahe Datenaktualisierungen ermöglicht.

Die Berichte zu Bruttoumsatz (Auftragswert) ermöglichen dir, die generierten Umsätze vor Abzügen zu analysieren und die Performance deiner Verkaufskanäle und Artikel zu bewerten. Mit der Lagerperformance erhältst du Einblicke in Bestandswerte und Lagerumschläge, um die Effizienz deines Lagers zu optimieren. Die Reports zu Nettoumsatz & Rohertrag helfen dir, die Rentabilität nach Abzug von Retouren und Rabatten zu ermitteln. Retouren-, Storno- und Rabattquoten geben dir Aufschluss über potenzielle Schwachstellen in deinen Verkaufsprozessen. Zusätzlich sorgt die Stammdatenpflege für eine hohe Datenqualität und unterstützt wichtige operative Prozesse.

![berichte_neu_001.png](https://help.xentral.com/hc/article_attachments/15365243779868)

## Allgemeines zu den Berichten

Die Berichte-Plattform basiert auf modernster Datenbank-Technologie und ermöglicht dadurch schnelle, stabile und zuverlässige Auswertungen. Das zugrunde liegende Datenmodell ist vollständig dokumentiert und bietet detaillierte Informationen zu allen Tabellen und Spalten. Alle Bezeichner und Inhalte sind konsistent ins Englische übersetzt, sodass ein einheitlicher Zugriff und eine klare Orientierung gewährleistet sind. Das Modell wird fortlaufend erweitert und optimiert, beispielsweise durch intelligente Tabellen, die Rechnungen, Gutschriften und deren Positionen strukturiert zusammenfassen.

> **Anmerkung**
>
> **Details zur Datenbank:** Wir nutzen AWS Redshift, das für hohe Geschwindigkeit und Effizienz bei großen Datenmengen optimiert ist. Im Gegensatz zu MySQL, das zeilenbasiert arbeitet, verwendet Redshift eine spaltenbasierte Speicherung. Dies ermöglicht schnellere Abfragen und Analysen, ideal für datenintensive Aufgaben und schnelles Reporting. Bitte beachte, dass der Redshift Dialekt zwar dem von MySQL sehr ähnlich ist, hier und da jedoch Unterschiede in der Syntax aufweist.

### Wichtige Hinweise zur Datenaktualisierung

> **Anmerkung**
>
> Standardmäßig werden die Daten **einmal pro Nacht** aktualisiert. Dies ist sowohl aus Kostengründen als auch aufgrund unserer Nutzungsanalyse sinnvoll, da über 90 % der Kunden ihre Berichte nicht mehrmals täglich abfragen. Solltest du eine höhere Aktualisierungsfrequenz benötigen (z.B. alle 3 Stunden oder sogar in nahezu Echtzeit), kannst du dies über einen individuellen Vertrag für deine Instanz beantragen. Kontaktiere hierfür bitte unser Customer Development Team unteraccountmanagement@xentral.com.

## Berichte verwenden

Berichte können sensible Informationen enthalten. Aus diesem Grund sind Berichte standardmäßig nur für Admins freigeschaltet. Sofern der Benutzer keine Admin-Rechte hat, braucht er die Berechtigung **Benutzer > Analytics_platform > all**.

Für einen unbeschwerten Start ohne technische Kenntnisse, empfiehlt es sich, mit vordefinierten Berichtsvorlagen zu starten. Diese Vorlagen decken bereits viele generelle Analysen ab, von[Management](#UUID-0c282c1c-34bb-ff63-e4f5-88fc343e49a2_id_reportNEW-HandbookDraft-XentralBerichtswesen-Berichteneu-BerichtsvorlagenfrdasManagementdeinesGeschfts)bis[Stammdatenpflege](#UUID-0c282c1c-34bb-ff63-e4f5-88fc343e49a2_id_reportNEW-HandbookDraft-XentralBerichtswesen-Berichteneu-BerichtsvorlagenzurPflegevonStammdatenundUntersttzungoperativerProzesse).

Für individuelle Fragestellungen, die über den Inhalt von Berichtsvorlagen hinausgehen, kannst du hingegen eigene Berichte anlegen. Je nach technischem Kenntnisstand und Komplexität bieten wir dir hierzu einen einfachen, klick-basierten[No-Code Editor](#UUID-0c282c1c-34bb-ff63-e4f5-88fc343e49a2_id_reportNEW-HandbookDraft-XentralBerichtswesen-Berichteneu-No-CodeEditorErstellenvonBerichtenleichtgemacht)sowie einen deutlich flexibleren[SQL Editor](#UUID-0c282c1c-34bb-ff63-e4f5-88fc343e49a2_id_reportNEW-HandbookDraft-XentralBerichtswesen-Berichteneu-SQL-EditorFrkomplexereAbfragen).

### Benutzerrechte und Berichte Freigaben

Das Freigabesystem für Berichte ermöglicht es dir, einzelnen Mitarbeitern Lesezugriff auf  ausgewählte Berichte einzurichten. Mitarbeiter mit reinem Lesezugriff können nur freigegebene Berichte sehen und abrufen. Das Schreiben oder Verändern von Berichten bleibt gesperrt.

Als Xentral Admin hast du unter **Benutzer > Rechte ** die Option, einem Xentral Nutzer vollen Schreib- und Lesezugriff auf das Berichtswesen (“**all **”) oder lediglich beschränkten Lesezugriff (“** restricted**”) einzurichten.

![berichtswesen_rechte_benutzer_einstellen.png](https://help.xentral.com/hc/article_attachments/18748066788764)

Der beschränkte Lesezugriff wird grundsätzlich im Berichtswesen unter dem Menüpunkt **Berichte (neu) > Freigabe ** erteilt und konfiguriert. Du musst dies nicht vorab unter**Benutzer > Rechte** zuteilen (dies passiert automatisch mit der ersten Berichtsfreigabe). Nach Freigabe kann der Nutzer freigegebene Berichte sehen, abrufen und exportieren. Das Erstellen oder Verändern von SQL statements / No-Code Konfigurationen ist hingegen nicht möglich. Nicht freigegebene Berichte werden dem Nutzer nicht angezeigt.

> **Anmerkung**
>
> Hat ein Benutzer mehrere Freigabe-Niveaus, gewinnt das höchste (Xentral Admin → “all” → “restricted”). Willst du sicherstellen, dass ein Benutzer nicht bereits Vollzugriff (“all”) hat, macht der Umweg über die Benutzerrechte Sinn, um die Rechte von “all” auf “restricted” zu ändern.

#### Berichte Freigaben für einzelne Nutzer erteilen **Schritte: **

1. Erstelle ein **neues Freigabeprofil**. Ein Freigabeprofil bündelt den Zugriff auf einen oder mehrere Berichte, z.B. alle Sales oder Logistik Berichte.
1. Wähle die **Berichte ** oder **Berichts-Sammlungen** aus, für die du eine Lese-Freigabe erteilen möchtest.
1. Unter “**Nutzerfreigabe **” kannst du dieses Profil anschließend beliebig vielen ** Mitarbeitern zuordnen **, um ihnen den ** Zugriff** auf die ausgewählten Berichte zu ermöglichen.

> **Anmerkung**
>
> **Hinweis**
>
> Beispielsweise könntest du ein Freigabeprofil “**Controlling **” für Auswertungen von Nettoumsatz und Deckungsbeitrag anlegen, während ein anderes Profil namens “** Lagerauswertung**” Zugriff auf Berichte zur Lagerperformance gewährt.

### Unterschiede zwischen Basis und Premium Version im Berichtswesen

In der Basis Version (im Standard für alle Pläne freigeschaltet) kannst du grundsätzlich alle Berichtsvorlagen ansehen, Inhalte prüfen und eigene Berichte konfigurieren. Das Abrufvolumen ist unbegrenzt, sollte jedoch einen gewöhnlichen Umfang nicht regelmäßig überschreiten. Die einzige Limitation besteht bei der Ansicht der Ergebnisse - hier ist der Toggle auf “Vorschau” festgesetzt und lässt sich nicht auf “Vollansicht” umstellen. Dies hat zur Folge, dass a) nur 5 Zeilen des Ergebnisses angezeigt werden und b) die Exportfunktionen deaktiviert sind.

Eine Ausnahme bilden Berichte in der Sammlung “Stammdatenpflege und Unterstützung operativer Prozesse”. Diese dienen nicht dem klassischen Reporting und stehen dir daher vollständig zur Verfügung, inkl. Download von CSV Dateien. Sollten hier deiner Meinung nach wichtige Berichte fehlen, kannst du uns dies gerne per Ticket melden. Wir prüfen anschließend, ob dein Berichtswunsch nachträglich hinzugefügt werden kann.

In der Premium Version erhältst du hingegen den vollen Umfang des Add-ons und kannst von einer Vollansicht der Ergebnisse sowie[erweiterten Exportfunktionen](#UUID-0c282c1c-34bb-ff63-e4f5-88fc343e49a2_id_reportNEW-HandbookDraft-XentralBerichtswesen-Berichteneu-ExportierenvonDaten)Gebrauch machen. Der Vorschau-Modus steht dir weiterhin zum kostenfreien Entwickeln und Testen von Berichten zur Verfügung.

Beachte, dass der Toggle in der Premium Version auf dem Vorschau-Modus beginnt und mit dem ersten Wechsel auf Vollansicht auch nach dem Wiederholten Öffnen von Berichten in der Vollansicht verbleibt, bis du den Toggle wieder auf Vorschau zurückstellst.

![vs_1_berichte_neu_003.png](https://help.xentral.com/hc/article_attachments/15368378316316)

### Vorgefertigte Berichtsvorlagen

#### Berichtsvorlagen zur Pflege von Stammdaten und Unterstützung operativer Prozesse

Gut gepflegte Stammdaten sind essenziell für eine sinnvolle Datenanalyse und ein datengetriebenes Management. Da noch nicht alle Xentral-Module eine ideale Stammdatenpflege unterstützen, bieten wir kostenfreie Möglichkeiten, Probleme in den Stammdaten zu identifizieren und zu beheben. Ein Beispiel hierfür ist das Auffinden und Nachhalten von Artikeln ohne EAN-Codes.

Darüber hinaus können unsere Berichte operative Prozesse unterstützen, die noch nicht optimal durch bestehende Xentral-Module abgedeckt sind. Wir haben die gängigsten individuellen Berichte gescannt und in generischer Form bereitgestellt. Diese Sammlung dient als Erweiterung der aktuellen Exportzentrale, z.B. für das Exportieren von Lagerbeständen für eigene Pick & Pack Prozesse.

Xentral-Berichte zur Pflege von Stammdaten und zur Unterstützung operativer Prozesse sind bei üblicher Nutzung (mehrmals täglich, jedoch nicht im Minutentakt) kostenfrei.

#### Berichtsvorlagen für das Management deines Geschäfts

| | |
| Bruttoumsatz | Analysiere deinen Bruttoumsatz basierend auf Aufträgen (exkl. angelegte Aufträge) vor Retouren, Stornos und Rabatten. Diese Berichte helfen dir, den Bestelleingang zu verstehen und die Performance einzelner Hebel zu identifizieren. Schneide deinen Bruttoumsatz nach Dimensionen wie Zeit, Artikel, Kunde, Verkaufskanal und mehr. |
| Nettoumsatz & Rohertrag | Bewerte deinen Nettoumsatz basierend auf Rechnungen und Gutschriften (exkl. angelegte) nach Retouren, Stornos und Rabatten. Diese Berichte unterstützen dich bei der Analyse deines Umsatzes und Rohertrags und helfen dir, Optimierungspotenziale zu identifizieren. |
| Retouren-/Rabatt-/Stornoquoten | Analysiere die Quoten für Retouren, Rabatte und Stornos, um mögliche Schwachstellen in deinem Prozess zu identifizieren. Dir stehen die gleichen Dimensionen zur Verfügung, wie in der Analyse von Brutto- und Nettoumsatz. |
| Lagerbestand und Performance | Überwache deinen Lagerbestand und die Performance, um potenzielle Engpässe oder Überbestände frühzeitig zu erkennen. In dieser Sammlung findest du beispielsweise Berichte zu Lagerbestand und -wert, Penner/Renner-Analyse, Lagerumschlag und Abverkaufsquoten. |

### Individuelle Berichte erstellen

Manchmal reichen die vordefinierten Analysen nicht aus und es bedarf einer individuellen Lösung. Genau dafür kannst du dir individuelle Berichte erstellen und in einer Sammlung abspeichern.

#### Sammlungen zum Ablegen von Berichten

Berichtssammlungen funktionieren ähnlich wie Ordner und helfen dir, den Überblick zu behalten, indem du Berichte logisch gruppierst. So findest du schnell relevante Berichte zu Finanzen, Verkauf oder Lager. Auch das Erstellen einer Archiv-Sammlung für alte, überholte Berichte kann sinnvoll sein.

**Sammlung bearbeiten und löschen **: Deine selbst erstellten Sammlungen kannst du über das 3-Punkte-Menü rechts neben dem Sammlungstitel bearbeiten oder löschen. Die von Xentral erstellten Sammlungen sind schreibgeschützt und lassen sich nicht bearbeiten. ** Einen neuen Bericht anlegen**: Du kannst einen neuen Bericht entweder über den Button in einer leeren Sammlung oder über den Button "Bericht erstellen" in der rechten oberen Ecke anlegen. Bestehende Berichte lassen sich ebenfalls über das 3-Punkte-Menü rechts neben ihrem Titel löschen.

> **Tipp**
>
> Direkt neben dem Editor findest du unsere interaktive Dokumentation. Sie ermöglicht dir die Suche nach spezifischen Inhalten in Deutsch und Englisch und bietet dir durch neue Kurzbeschreibungen für Tabellen / Spalten genauere Einblicke in die Datenpunkte. Zur besseren Orientierung wird zusätzlich die alte Bezeichnung der Quell-Daten für jede Tabelle und Spalte angezeigt.

#### No-Code Editor: Erstellen von Berichten leicht gemacht

Der No-Code Editor führt dich Schritt für Schritt durch die Erstellung deiner Abfrage, ohne dass tiefgehende Programmierkenntnisse erforderlich sind. Eine gründliche Auseinandersetzung mit dem englischen Datenmodell sowie dem Zusammenführen von Tabellen (join) wird sich jedoch schnell in der Bearbeitungseffizienz und dem Ergebnis wiederspiegeln.

![berichte_neu_004.png](https://help.xentral.com/hc/article_attachments/15365460656924)

##### Schritt 1: Datensatz auswählen

Zu Beginn wählst du den Datensatz aus, der am besten zu deiner Frage passt. Zum Beispiel wählst du Aufträge (sales orders), wenn es um Bestelleingänge geht. Bei Fragen zu Nettoumsatz oder Rohertrag startest du mit Rechnungen (invoices).

Über das Drop-Down Icon neben deinem gewählten Datensatz kannst du die Spalten auswählen, die deine Ergebnistabelle enthalten soll.

##### Schritt 2: Weitere Datensätze hinzufügen

Du kannst zusätzliche Datensätze hinzufügen, um deine Abfrage zu erweitern. Dabei wählst du zwischen zwei Optionen:

> **Anmerkung**
>
> **Hinweis**
>
> - **Left Join**: Erweiterung des bestehenden Datensatzes (häufig der beste Startpunkt).
> - **Inner Join**: Ergänzung und Einschränkung des bestehenden Datensatzes.

Wähle die Tabelle aus, die du hinzufügen möchtest, und spezifiziere den Parameter, auf den sie hinzugefügt werden soll. Meist sind dies ID-Felder mit ähnlichem Namen wie die zuerst gewählte Tabelle, auch bekannt als Primary und Foreign Keys.

Falls dir diese Begriffe noch zu kryptisch erscheinen, findest du nachfolgend ein anschauliches Beispiel als Hilfestellung.

##### Beispiele für LEFT JOIN und INNER JOIN

*Stell dir vor, du hast zwei Excel-Tabellen: eine mit den Namen aller Familienmitglieder und eine mit den Geburtstagsgeschenken. *>**Anmerkung**
>
> **Hinweis**
>
> LEFT JOIN
>
> *Ein SQL LEFT JOIN kombiniert beide Tabellen, sodass du siehst, welches Familienmitglied ein Geschenk bekommen hat und wer nicht. Dabei werden alle Familienmitglieder angezeigt, auch wenn sie kein Geschenk erhalten haben.*
>
> *In Excel würdest du die SVERWEIS-Funktion (VLOOKUP) verwenden, um in der Geschenkliste nachzusehen, welches Geschenk jedes Familienmitglied erhalten hat. Der LEFT JOIN funktioniert ähnlich, aber mit einem entscheidenden Unterschied: Er zeigt auch diejenigen Familienmitglieder an, die kein Geschenk bekommen haben. Der "ON"-Parameter im LEFT JOIN entspricht dem Suchkriterium in SVERWEIS (VLOOKUP) und verbindet die Listen anhand eines gemeinsamen Merkmals, wie dem Namen.*

*Beispiel: *-* Tabelle 1 (Familienmitglieder): Namen *-* Tabelle 2 (Geschenke): Namen und Geschenk*

*Der LEFT JOIN verbindet die Tabellen "ON" (basierend auf) dem gemeinsamen Namen, sodass du siehst, wer ein Geschenk bekommen hat und wer nicht.*

*Ergebnis des LEFT JOIN: *-* Kind A hat ein Auto *-* Kind B hat eine Puppe *-* Kind B hat einen Ball *-* Kind C hat kein Geschenk *>**Anmerkung**
>
> **Hinweis**
>
> INNER JOIN
>
> *Ein INNER JOIN funktioniert ebenfalls wie ein SVERWEIS (VLOOKUP) in Excel, zeigt jedoch nur die Familienmitglieder an, die tatsächlich ein Geschenk erhalten haben.*

*Beispiel: *-* Tabelle 1 (Familienmitglieder): Namen *-* Tabelle 2 (Geschenke): Namen und Geschenk*

*Beim INNER JOIN werden nur die Namen der Familienmitglieder angezeigt, die auch in der Geschenkliste stehen. Das heißt, du siehst nur die Familienmitglieder, die ein Geschenk bekommen haben. Der "ON"-Parameter im INNER JOIN sagt, dass die Listen basierend auf einem gemeinsamen Merkmal, wie dem Namen, verbunden werden sollen.*

*Ergebnis des INNER JOIN: *-* Wenn Kind A ein Geschenk hat, wird es angezeigt. *-* Wenn Kind B ein Geschenk hat, wird es angezeigt. *-* Wenn Kind C kein Geschenk hat, wird es nicht angezeigt.*

*Nur diejenigen, die ein Geschenk bekommen haben, sind im Ergebnis sichtbar. *>**Tipp**
>
> *Diese Erklärungen helfen dir, die Unterschiede zwischen LEFT JOIN und INNER JOIN zu verstehen und wie sie in SQL-Abfragen verwendet werden.*

##### Schritt 3: Datensatz filtern

Nachdem du deinen Datensatz erstellt hast, kannst du ihn über Regeln filtern:

Wähle eine Spalte aus und setze Vergleichsparameter, z.B.:

- **Textfelder**: enthält/nicht enthält bestimmten Wert.
- **Zahlenwerte**: größer/kleiner als eine bestimmte Zahl.
- **Datumsfelder:** vor/nach/zu einem bestimmten Datum.
- **Boolean-Felder**: wahr/falsch.

Kombiniere beliebig viele Regeln mit UND/ODER, und lösche sie bei Bedarf mit dem X. Beachte, dass nur Felder gefiltert werden können, die du im ersten Schritt ausgewählt hast.

##### Schritt 4: Spalten aggregieren

Fasse bestimmte Spalten zusammen, indem du Funktionen wie Summe, Durchschnitt, Minimum, Maximum oder Anzahl verwendest. Der Editor lässt nur gültige Operationen basierend auf dem Spaltentyp zu. Beispielsweise kannst du keine Summe über eine Textspalte wie “Stadt” bilden.

##### Schritt 5: Ergebnisse sortieren und begrenzen

Sortiere deine Ergebnisse nach einer bestimmten Spalte, auf- oder absteigend. Begrenze die Anzahl der angezeigten Zeilen über den Limit-Parameter, um z.B. nur die ersten 100 Ergebnisse zu sehen.

##### Schritt 6: Vorschau und Speichern

Überprüfe die Vollständigkeit deiner Auswahl im Editor. Wenn die Auswahl gültig ist, klicke auf den Vorschau-Button, um deine Abfrage zu testen. Die Gültigkeitsanzeige neben dem Titel zeigt dir zu jeder Zeit an, ob sich dein Bericht bereits ausführen lässt.

![vs_1_berichte_neu_005.png](https://help.xentral.com/hc/article_attachments/15368402786716)

![vs_1_berichte_neu_006.png](https://help.xentral.com/hc/article_attachments/15368391266588)

Speichere den Bericht, indem du auf den Speichern-Button in der rechten oberen Ecke klickst. Achte darauf, Änderungen zu speichern, bevor du die Seite verlässt, um Datenverlust zu vermeiden.

#### SQL-Editor: Für komplexere Abfragen

Zusätzlich zum No-Code Editor bietet Xentral einen SQL-Editor für fortgeschrittene Benutzer.

![berichte_neu_007.png](https://help.xentral.com/hc/article_attachments/15365489842332)

Dieser Editor unterstützt:

- **Auto-Complete**: Vorschläge während des Tippens.
- **Syntax-Highlighting**: Farbige Hervorhebung von Schlüsselwörtern.
- **Fehleranzeige**: Zeigt Fehlermeldungen im Ergebnisfeld an.

Erweitere das Editor-Eingabefeld bei Bedarf über die sechs Punkte unterhalb des Eingabefelds und rufe die Dokumentation über das Fragezeichen neben dem Editor auf. Klappe den Editor bei Bedarf über die zwei gegeneinander gerichteten Pfeile ein oder aus. Speichere deine Änderungen, um Datenverlust zu vermeiden.

Bearbeite den Titel deines Berichts und die ausgewählte Kollektion direkt im Editor über das Stift-Symbol in der rechten oberen Ecke.

**Dynamische Parameter / Filter einfügen**

Filter dynamisieren deinen Bericht und verleihen deinen Nutzern die Möglichkeit, ohne Programmierkenntnisse Ergebnisse zu verändern. Du erstellt Filter ganz einfach über Parameter in deinem SQL Statement. Konfigurieren kannst du Parameter über den Button {x} rechts neben dem Eingabefeld.

![berichte_neu_008.png](https://help.xentral.com/hc/article_attachments/15365506589596)

In der Seitenleiste kannst du nun einen neuen Parameter anlegen. Der Parameter wird beim Ausführen einer Abfrage automatisch mit dem gesetzten Filterwert ersetzt.

Ein Parameter hat folgende Eigenschaften:

- **Wert**: Der Wert ist das, was du in deinem SQL Statement in geschweiften Klammern einsetzt. Zum Beispiel *{name_filter}*-**Label**: Das Label beschreibt den Namen, unter dem dein neuer Filter für Nutzer angezeigt wird. Zum Beispiel * Name Filter.* In der aktuellen Implementierung wird das Label automatisch erzeugt, indem der Bindestrich in ein Leerzeichen umgewandelt wird.
- **Typ**: Der Datentyp des Parameters. Du kannst wählen zwischen Text, Nummer, Datum und SQL Statement. Beachte, dass du Werte beim Typ “SQL Statement” in einzelne Anführungszeichen wrappen musst (’yxz’). Dies ermöglicht dir komplexere Filterausdrücke, wie z.B. WHERE product_name LIKE {{VAR}} mit Filter ’
- **Standardwert**: Damit dein SQL Statement auch ohne das Setzen von Filterwerten funktioniert, musst du einen Standardwert vorgeben. Dein Parameter wird dann beim Ausführen der Abfrage automatisch mit dem Standardwert ersetzt, sollte kein Filterwert vorgegeben sein.

![berichte_neu_009.png](https://help.xentral.com/hc/article_attachments/15365460982044)

#### Exportieren von Daten

Daten können auf verschiedene Wege aus dem Berichte Modul exportiert werden:

- **Permanent-Link (URL):**
  Die URL ist ein permanenter Link, über den du durch Aufrufen im Browser oder ein Drittanbieter-Tool den Download einer.csv Datei mit deinen Berichtsergebnissen auslöst. Du erstellst und verwaltest deine individuelle Berichts-URL im Tab Exporteinstellungen → Permalink.

- **E-Mail:**
  Beim Einrichten des E-Mail Versands kannst du sowohl angeben, in welchem Zeitintervall die Mail versendet wird, als auch in welchem Dateiformat der Bericht gespeichert wird. Du erhältst dann zur entsprechenden Zeit eine E-Mail mit Download-Link.

- **FTP/SFTP/FTPS:**
  Mit dem neuen Berichte-Modul erhaltet ihr auch einen vollständig überarbeiteten FTP Service. Dieser basiert auf der neuen Connect Technologie und lässt sich in zwei Schritten einrichten.

  - Zuerst konfigurierst du deinen Server (FTP/SFTP/..) unter Einstellungen → Administration → Datenaustausch → FTP
  - Im zweiten Schritt kannst du für jeden Bericht eine FTP Konfiguration auswählen sowie ein Zeitintervall definieren, indem du im Bericht auf das Tab “Exporteinstellungen” klickst und den FTP Export aufklappst.

- **File download:**
  Über den Export Button rechts oben kannst du deinen aktuellen, gespeicherten (!) Bericht als.csv file herunterladen. Die Erstellung deines Reports geschieht asynchron im Hintergrund und kann ggf. ein paar Sekunden dauern. Du findest den Download Link zur Datei unter dem Tab Exporte auf jeder Berichtsansicht.

- **Reporting API:**
  Wir entwickeln aktiv an neuen API Endpunkten zum programmatischen Abrufen und Bearbeiten von Berichten und Konfigurationen. Die Dokumentation dazu findest du in unseren OpenAPI specs. Folgende Endpunkte stehen dir derzeit zur Verfügung:

  - **Query endpoint** to create, execute and list the history of executed SQL queries
  [https://developer.xentral.com/reference/analyticsquery](https://developer.xentral.com/v24.31/reference/analyticsquery)

  - **Report endpoint** to create, alter, delete reports, retrieve / change export configurations
  [https://developer.xentral.com/reference/analyticsreportlist](https://developer.xentral.com/v24.31/reference/analyticsreportlist)

**Report usage endpoint** to show the history of chargeable requests made within the given timeframe

[https://developer.xentral.com/reference/analyticsreportusageget](https://developer.xentral.com/v24.31/reference/analyticsreportusageget)

> **Tipp**
>
> Um die Ergebnisse (und nicht nur die Konfiguration) von Berichten über die API abzurufen, gibt es mehrere Wege. Du kannst z.B. das SQL Statement eines angelegten Berichts via GET /report/{id} abfragen und es dann in einem zweiten Schritt über /query ausführen. Alternativ erzeugst du ein CSV file über POST /report/{id}/export und fragst das Ergebnis über GET /report/{id}/export ab. Wurde das file erfolgreich erstellt, liefert GET neben dem Status auch das file zurück.
>
> Die Report ID findest du in der URL, z.B. 1362 für *...xentral.biz/app/analytics-platform?activeReport=1362&editorModeActive=false&tab=report*-**GSheet Integration: **

- Schritt 1) Downloade die Code Datei zum Upload in Google Scripts (Status:** In Arbeit**)
  - Schritt 2) Folge [dieser Anleitung](https://drive.google.com/file/d/1yq3ys5mh_TvoeKVzI9jCGdHNmipMFXDJ/view?usp=drive_link), um deine Verbindung zu Xentral zu konfigurieren (Status: **Vorläufig**)
- **Excel Integration: **

- Schritt 1) Downloade die Code Datei zum Upload in Google Scripts (Status:** In Arbeit**)
  - Schritt 2) Folge dieser Anleitung, um deine Verbindung zu Xentral zu konfigurieren (Status: **In Arbeit**)

### Weitere Informationen

- [Xentral Berichtswesen - Übersicht](https://docs.google.com/document/d/1-gSzD_dQ_fhZmwp4_c6beyfmckiohpVsQfnX8fjx8_k/edit)
- [Xentral Berichtswesen - Datenmodell](https://docs.google.com/document/d/17UoqFdqPbQMgvwAMuwoqTIlxL3bG_HCHZ-4Cgg1c510/edit?usp=sharing)
- [Xentral Berichtswesen - Berichtsvorlagen (neu)](https://docs.google.com/document/d/1yc63I8VDichHVm2bH0A1_58gxJAQy4f_rLmG3sAMfjA/edit)
- [Xentral Berichtswesen - Q&A + known issues](https://docs.google.com/document/d/1CjUtNv1qPd6MEm88tbbmms4JU63J6XlsWtcgzQYh9II/edit)