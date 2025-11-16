ImXentral NextGenDesign:Buchhaltung > Zahlungsverkehr.

Im Classic Design:Buchhaltung > Zahlungsverkehr.

Der Zahlungsverkehr umfasst alle Übertragungen von Zahlungsmitteln.

In xentral können in diesem Modul Beträge sowohl beglichen, als auch eingezogen werden. Es ist auch möglich eine Verbindlichkeit direkt in diesem Modul anzulegen. Voraussetzungen für die Nutzung dieses Moduls sind:

- dass der SEPA-Zahlungsverkehr in xentral eingerichtet ist
- dass eine SEPA-Gläubiger-Identifikationsnummer vorhanden ist

Besonders relevant ist dieses Modul, wenn der Zahlungsverkehr über xentral abgewickelt wird.

In der App Zahlungsverkehr könnt ihr Überweisungen von euren Bankkonten veranlassen, indem ihr im Modul eine XML-Datei erzeugt und diese in eurer Online-Banking-Software hochlädt. Zu diesem Zweck können Verbindlichkeiten und Gutschriften direkt hereingeladen werden, um die Auszahlung zu veranlassen und die erstellte Buchung direkt auf den korrekten Beleg zu verknüpfen – und diesen als bezahlt zu markieren. Diese Belege könnt ihr nach Offenen, Fehlgeschlagenen, Ausgeführten, etc. filtern, um stets den benötigten Überblick zu erhalten.

Über die Aktion Zahlungen zuordnen und freigeben werden die vorgeschlagenen Buchungen vorbereitet. Anschließend kann oben auf den Reiter des gewünschten Kontos navigiert werden und mit der Aktion Zahlung ausführen die Überweisungen ausgelöst werden.

## Voraussetzungen

### SEPA-Zahlungsverkehr einrichten

Der SEPA-Zahlungsverkehr kann unter Administration → Einstellungen → Buchhaltung → Geschäftskonten für jedes Konto aktiviert werden. Folgende Daten müssen vorab im Geschäftskonto eingetragen werden:

- Inhaber
- BIC
- IBAN
- BLZ (optional)
- Konto (optional)
- Gläubiger ID
- Lastschrift: aktiviert durch Setzen eines Hakens

### SEPA-Gläubiger-Identifikationsnummer

Für das Lastschriftverfahren wird für die eigene Firma eine SEPA-Gläubiger-Identifikationsnummer benötigt. Diese muss z.B. für Deutschland bei der Deutschen Bundesbank mit dem „Formular zur Beantragung Ihrer Gläubiger-Identifikationsnummer“ beantragt werden.

Mit dieser Nummer kann man sich bei der Hausbank freischalten lassen. Für die einzelnen Kunden muss bei jedem Lastschrifteinzug die Mandatsreferenz übermittelt werden. Diese Daten werden beim Einzug jedes Mal für jeden Kunden von xentral aus mit übergeben.

Diese Nummer wird direkt bei den Firmendaten eingetragen: Administration → Einstellungen → System → Grundeinstellungen → Firmenanschrift.

## Zahlungen

### Offen

In der Übersicht sind alle offenen Lastschriften aufgelistet. Diese können nach bestimmten Kriterien gefiltert werden. Außerdem ist es möglich im Bereich "Aktion" direkt hier eine neue Überweisung anzulegen sowie Gutschriften und Verbindlichkeiten zu laden.

### Filter

- **nur Offene** → zeigt ausschließlich die Verbindlichkeiten und Gutschriften an, die noch offen sind und noch keinem Zahlungskonto zugeordnet wurden. Dieser Filter sollte standardmäßig gesetzt werden
- **nur Fehlgeschlagene** → zeigt ausschließlich die Verbindlichkeiten und Gutschriften an, die fehlgeschlagen sind
- **nur Ausgeführte** → zeigt ausschließlich bereits ausgeführte Verbindlichkeiten und Gutschriften an
- **nur Verbindlichkeiten** → zeigt ausschließlich Verbindlichkeiten an
- **nur Gutschriften** → zeigt ausschließlich Gutschriften an
- **Skonto-Datum verwenden** → Verwendet das Skonto-Datum zur Sortierung

### Neue Überweisung

Über die Schaltfläche "Neue Überweisung" kann eine Überweisung direkt hier neu angelegt werden.

In der Eingabemaske können die notwendigen Informationen hinterlegt werden. Über die Edit-Schaltfläche bei bestehenden Überweisungen erscheint ebenfalls diese Maske, wobei die Informationen dann noch einmal angepasst werden können, z.B. wenn für diese eine Überweisung eine andere IBAN verwendet werden soll, als die, die in den Stammdaten hinterlegt ist.

### Offene Zahlungen

Hier können Gutschriften und Verbindlichkeiten geladen werden. Im ersten Schritt werden die Überweisungen händisch angehakt oder über den Haken "alle markieren" ausgewählt. Dann ist das Konto auszuwählen, zu welchem die Überweisung zugeordnet werden soll. Als letztes ist die Auswahl mit der Schaltfläche "Zahlungen zuordnen und freigeben" abzuschließen.

### Konten

Neben dem Tab "offen" erscheinen alle angelegten Konten, die für den Zahlungsverkehr freigegeben wurden. In unseren Bsp. sind dies "Bankkonto CSV (Beispiel:Deutsche Bank)", "Barkasse", "Konto: AmazonPay (API)". Hier werden die Überweisungen angezeigt, die diesem Konto zugeordnet wurden.

![PaymentTransactions1.png](https://help.xentral.com/hc/article_attachments/13026760349468)

### Filter

Auch hier ist es möglich über Filter nach bestimmten Kriterien zu filtern.

- **nur Fehlgeschlagene** → zeigt ausschließlich die Verbindlichkeiten und Gutschriften an, die fehlgeschlagen sind
- **nur Ausgeführte** → zeigt ausschließlich bereits ausgeführte Verbindlichkeiten und Gutschriften an
- **nur Verbindlichkeiten** → zeigt ausschließlich Verbindlichkeiten an
- **nur Gutschriften** → zeigt ausschließlich Gutschriften an
- **Skonto-Datum verwenden** → Verwendet das Skonto-Datum zur Sortierung

### Transaktionsmonitor

Hier liegt eine Auflistung aller ausgeführten Zahlungen für dieses Konto.

### Zahlungsausführung

Nachdem die Zahlung ausgeführt wurde, erscheint im Transaktionsmonitor die XML-Datei zum Download. Nach dem Download kann diese wiederum bei der jeweiligen Bank hochgeladen werden. Dieser Ablauf ist immer der gleiche, außer bei[Paypal](https://help.xentral.com/hc/de/articles/360017416839#UUID-d95f79b2-836e-9f04-5bfc-ecd171d4550d)und[Amazon Pay](https://help.xentral.com/document/preview/24279#UUID-917f32e3-64d6-2860-9ca2-9f0de43a94a9). Dort erfolgt die Rückzahlung direkt über die API.

### SEPA Sammelüberweisung

Dieser Tab wird nicht mehr verwendet. Alle Aktionen erfolgen nun über die Konten Tabs.

## Lastschriften

### offene Rechnungen

In diesem Tab werden alle offenen Rechnungen aufgelistet. Es kann danach gefiltert werden, dass nur Rechnungen angezeigt werden, die in mindestens 10 Tagen fällig sind. Im Bereich "Übersicht" wird die Gesamtsumme dargestellt. Mit der Stapelverarbeitung kann ein Konto und optional ein Präfix vor dem Buchungstext ausgewählt werden, um dann eine Sammellastschrift anzulegen.

### offene Gutschriften

In diesem Tab werden alle offenen Gutschriften aufgelistet. Im Bereich Übersicht wird die Gesamtsumme dargestellt.

### Abgebuchte Rechnungen

Wurden Rechnungen verbucht, erscheinen diese in diesem Tab. Die Rechnungen können hier noch einmal bearbeitet oder als PDF ausgegeben werden.

### Zahlungsavis

Mit einem Zahlungsavis werden ausstehende Rechnungen angekündigt. In diesem Tab liegt eine Auflistung aller bestehenden Avis. Das Avis Dokument ist via PDF Icon abrufbar. Über die Stapelverarbeitung können die Avis über einen Prozessstarter versendet oder gedruckt und versendet werden. Stand Juni 2021 kann das Zahlungsavis nur in deutscher Sprache verschickt werden.

Wenn es einen Lastschrifteinzug für einen Kunden mit mehreren Rechnungen gleichzeitig in einem SEPA-Sammellauf gibt, werden die Rechnungen zu einer Summe zusammengefasst und anstelle der Rechnungsnummern wird dann die Nummer der Avis mit in den Überweisungstext verwendet. Z.B. bei 10 Rechnungen als Sammeleinzug sind zu viele Zeichen im Buchungstext, wenn jede Rechnung einzeln mit Nummer aufgelistet wird.

> **Anmerkung**
>
> Die Zahlungsavis wird standardmäßig an die in den Adressstammdaten hinterlegte E-Mail-Adresse gesendet. Falls unter **Adresse > Details > Dokumente Versandoptionen > Rechnung** eine abweichende E-Mail-Adresse hinterlegt ist, wird der Zahlungsavis stattdessen an diese gesendet.

### Zahlungsavis per Prozessstarter versenden

Zahlungsavise können gesammelt in großer Menge versendet werden. Zu versendende Avise können in der Übersicht ausgewählt und dann als Alternative zum Druck zu einer internen Liste hinzugefügt werden, von der aus diese der Prozessstarter "zahlungsavis_mailausgang" verschickt. Für die Mail wird die Geschäftsbriefvorlage "LastschriftenZahlungsavis" verwendet. Wenn die Geschäftsbriefvorlage nicht vorhanden ist, oder Text bzw. Betreff leer sind, dann wird keine Mail versendet.

### SEPA Sammellastschriften

In diesem Tab liegt eine Übersicht über alle SEPA Sammellastschriften. Diese können hier mit dem "x" entfernt oder über den Pfeil heruntergeladen werden. Durch das entfernen werden die einzelnen Rechnungen wieder in den Bereich der offenen Lastschriften verschoben, falls bspw. Änderungen an den Bankdaten des Kunden vorgenommen werden sollen, bevor die XML Datei erzeugt wird. Sind in einem Lastschrift Lauf Erstlastschriften und Folgelastschriften vorhanden, werden hier zwei Dateien für die Bank angelegt.

> **Anmerkung**
>
> Beim 'Präfix vor Buchungstext' ist darauf zu achten, dass der ausgewählte Text nicht zu lang ist. Ansonsten könnte die Banksoftware die Rechnungsnummer in 2 Zeilen trennen, was zur Folge hat, dass im xentral Zahlungseingang die Rechnungsnummer nicht mehr automatisch erkannt werden kann. Die Rechnungsnummer muss zusammenhängend in der Zahlungszeile beim Zahlungsimport vorhanden sein. Wird kein Präfix eingegeben, setzt sich der Buchungstext aus der Rechnungsnummer, der Kundennummer sowie des vollständigen Kundennamens zusammen.

In der Minidetail Ansicht können zudem weitere Details eingesehen werden und die Buchungsübersicht kann hier ausgedruckt werden. Kunden mit mehreren Rechnungen werden als Avis zusammengefasst und in einer Buchung angezeigt. Der Einzug via XML erfolgt dann auch in einer Sammelbuchung für diesen Kunden und wird später auf dem Bankkonto auch so verbucht. Die Aufsplittung der Einzelbuchungen kann dann im Zahlungseingang mit der Splitfunktion erfolgen. Um die Auflösung in Einzelpositionen von Sammellastschriften durch xentral zu gewährleisten, muss die Einstellung "Einzelbuchungen aktivieren" im Geschäftskonto aktiviert werden.

## Einstellungen

Im ReiterEinstellungenkann festgelegt werden, mit wie vielen Tagen das Skonto überzogen werden darf. Standardmäßig ist hier 0 eingestellt.

### Einzugsdatum einstellen

Das Einzugsdatum für Lastschriften wird in der Rechnung im BereichEinzugsermächtigungeingestellt. Das Einzugsdatum hat einen Einfluss auf die offenen Lastschriften unterZahlungsverkehr > Reiter Lastschriften > Unterreiter Offene Rechnungen. Hier wird die Rechnung automatisch für eine Sammellastschrift markiert, sobald das Einzugsdatum (z.B. der 15.06.2023 im folgenden Screenshot) erreicht ist. Alle Rechnungen ohne Einzugsdatum werden ebenfalls automatisch markiert.

![paymenttransaction_directdebit.png](https://help.xentral.com/hc/article_attachments/11351053692444)

Wenn du eine Rechnung manuell für eine Sammellastschrift auswählst, bevor ihr Einzugsdatum erreicht ist, wird das Einzugsdatum ignoriert und das Geld vorzeitig eingezogen.

### Rechnungsbetrag nochmals einziehen

Um einen Rechnungsbetrag noch einmal einzuziehen ist in eine Rechnung zu klicken und dort den Schreibschutz zu entfernen. Danach ist die Schaltfläche "nochmals einziehen" auszuwählen. Die Rechnung wird nun nochmals in den Lastschriftenlauf (Liste aller fälligen) aufgenommen.

### Rechnung mit Gutschrift verrechnen

Gutschriften können mit Rechnungen gemeinsam verrechnet werden. Hierzu muss der Rechnungsbetrag größer als der Gutschriftsbetrag sein. Andernfalls wäre es eine Rücküberweisung. Der Gutschriftsbetrag wird vom Rechnungsbetrag abgezogen. Folgende Rechnung soll als Lastschrift eingezogen werden:

![PaymentTransactions2.png](https://help.xentral.com/hc/article_attachments/13026768608028)

Zu dieser Rechnung wurde eine Gutschrift erstellt (Rechnung weiterführen als Gutschrift, Zahlungsweise "Lastschrift"). Diese Gutschrift erscheint bei den "Offene Gutschriften".

Bei der Erstellung der XML-Datei wird die Gutschrift mit der Rechnung verrechnet, sofern die Gutschrift einen Betrag kleiner / gleich der Rechnung hat.