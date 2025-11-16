Es gibt in xentral die Möglichkeit, ein Bankkonto per CSV-Import einzurichten. Dazu wird zunächst zum das Modul "Geschäftskonten" navigiert (Administration → Einstellungen → Buchhaltung → Geschäftskonten) und auf "Neu" → "Custom" geklickt.

## Felderklärungen

Im Folgenden findest du Felderklärungen zu den einzelnen Felder, die im Modul Bankkonto CSV vorhanden sind.

### Einstellungen

- **Bezeichnung**→ Interne Bezeichnung für das Konto. Diese Bezeichnung kann beliebig gewählt werden und wird an verschiedenen Stellen in der Oberfläche angezeigt
- **Typ**→ Typ des Kontos (Bankkonto: Konto (CSV-Import), PayPal-Konto, Kreditkartenanbieter, Kasse etc.)
- **aktiv**→ dieses Konto ist aktiv (in Verwendung) oder inaktiv (stillgelegt)
- **keine E-Mail**→ Der Kunde erhält keine automatische E-Mail-Benachrichtigung über den Eingang seiner Zahlung
- **Änderungen erlauben**→ Es dürfen Änderungen in den Kontoauszügen vorgenommen werden (nicht empfohlen, wird nur benötigt, wenn die Kontoauszüge von Hand eingegeben werden)

#### Bankverbindung (bei Typ Bank)

Bankdaten (werden für SEPA-Zahlungsverkehr und Lastschrift benötigt und sind hierfür Pflichtfelder)

- **Inhaber**→ Kontoinhaber für dieses Konto (keine Sonderzeichen, wenn der Sepa Zahlungsverkehr via XML verwendet wird)
- **BIC**→ BIC für dieses Konto (bei Bankkonten Pflichtangabe für Lastschrifteinzug und Sepa-Sammelüberweisung)
- **IBAN**→ IBAN für dieses Konto (bei Bankkonten Pflichtangabe für Lastschrifteinzug und Sepa-Sammelüberweisung)
- **BLZ**→ Bankleitzahl für dieses Konto
- **Konto**→ Kontonummer für dieses Konto
- **Gläubiger ID**→ Gläubiger ID für Bankkonten (bei Bankkonten Pflichtangabe für Lastschrifteinzug)
- **Lastschrift**→ Haken setzen um den Lastschrifteinzug zu aktivieren
- (HBCI → nur in alten Versionen noch vorhanden)
- (HBCI-Kennung → nur in alten Versionen noch vorhanden)

#### Konto (Buchhaltung)

- Kontenrahmen → Nummer des Kontenrahmens für das Bankkonto (für den Export der Auszüge); je nach Kontenrahmen z.B. 1800, 1700 etc.

#### CSV-Import

- **CSV-Import**→ Eingabemaske für den CSV-Import (Beispiel siehe CSV-Import-Einstellungen)
- **Erste Datenzeile**→ erste Zeilennummer in der echte Daten stehen (Bsp. für Daten ab Zeile 1: "1"). Sofern es eine Beschriftungszeile gibt, ist die erste richtige Datenzeile meist Zeile 2 (anzugeben dann "2")
- **Kodierung**→ Im Standard auf UTF8 Encode stellen, um die Umlaute korrekt zu übertragen
- **Trennzeichen**→ Strichpunkt oder Komma. Das Trennzeichen ist in der CSV Datei über einen Texteditor ersichtlich
- **Maskierung**→ Anführungszeichen oder keine Maskierung. Die Maskierung ist in der CSV Datei über einen Texteditor ersichtlich
- **Letzte Zeilen ignorieren**→ im Standard eine "0" eintragen, es sei denn der Kontoauszug enthält am Ende weitere Informationszeilen, die nicht mehr zu den Einzelbuchungen gehören. Hierzu als Zahl angeben, wie viele Zeilen am Ende ignoriert werden sollen
- **Datum**→ Spalte, in der das Datum steht.
- **Eingabeformat**→ Format, wie das Datum in Ihrer CSV-Datei angegeben ist (Meist Datum dd.mm.yyyy dann: %1.%2.%3)Beispiel für komplizierteres Format: 07.01.2020 10:07:18 GMT+00:00 => %1.%2.%3 %4:%5:%6 GMT+00:00
- **Ausgabeformat**→ Format, wie es für Xentral ausgegeben wird (Muss immer wie folgt ausgegeben werden: %3-%2-%1).
- -->>>> Bsp. für Eingabe und Ausgabe: 24.12.2016 in CSV entspricht Eingabeformat %1.%2.%3 und Ausgabeformat %3-%2-%1 (Ausgabe muss immer auf diese Format gebracht werden YYYY-MM-DD). Weiteres Beispiel: Ist das Eingabeformat folgendermaßen: 08/11/2016 11:12:45 wird dieses mit Variablen so dargestellt: %1/%2/%3 %4:%5:%6. Das Ausgabeformat bleibt %3-%2-%1 (die Uhrzeit wird in der Ausgabe abgeschnitten)
- **Betrag**→ Spalte, in der der Betrag steht (nur dieses Feld, wenn der Betrag in einer Spalte steht)
- **Extra Haben u. Soll**→ wird benötigt (Haken setzen und Spalte für Haben und Soll angeben), sofern der Betrag auf 2 Spalten aufgeteilt ist nach Haben und Soll
- **Haben**→ Spalte, in der der Betrag für HABEN steht (Voraussetzung: Haken bei "Extra Haben u. Soll" gesetzt)
- **Soll**→ Spalte, in der der Betrag für SOLL steht (Voraussetzung: Haken bei "Extra Haben u. Soll" gesetzt)
- **Buchungstext**→ Spalte(n), in der der Buchungstext steht. Besonderheit: für den Buchungstext können mehrere Spalten zusammengesetzt werden. Beispiel: 5+11+3+8+12+18+14. Bitte beachten: relevanteste Informationen für den Buchhaltungsexport nach vorne stellen, denn hier werden oft zu lange Texte abgeschnitten. Um möglichst viele relevante Informationen in eine separate Buchhaltungssoftware (z.B. Datev) zu importieren empfiehlt sich z.B. folgende Reihenfolge: Absender Name + Buchungstext + Referenznummer + Lastschriftinformationen + Sonstige Felder +... +...
- **Währung**→ Spalte, in der die Währung steht
- **Haben/Soll Kennung**→ Separate Spalte, die festlegt, ob der Betrag Haben oder Soll ist (z.B. eine extra Spalte, in der die Information "H" oder "S" zu finden ist)
- **Markierung Eingang**→ Zeichen für "Haben" z.B. "H" oder "+" (Voraussetzung: Spaltenangabe für "Haben/Soll Kennung")
- **Markierung Ausgang**→ Zeichen für "Soll" z.B. "S" oder "-" (Voraussetzung: Spaltenangabe für "Haben/Soll Kennung")

### Beispiel für ein Bankkonto mit CSV **Einstellungen (CSV Import)**:

![BankViaCSV1.png](https://help.xentral.com/hc/article_attachments/15492809910172)

**Aufruf Beispiel-Bankkonto**:

Soll das Bankkonto aufgerufen werden, so wird zu Buchhaltung → Zahlungseingang navigiert und das jeweilige Konto über den Editor-Button ausgewählt.

**Einstellungen Deutsche_Bank.csv (Stand 10/2019)**:

![BankViaCSV2.png](https://help.xentral.com/hc/article_attachments/15492809910172)

- Feld "Buchungstext": 4+5+8+9+10+6+7+3

> **Anmerkung**
>
> Bitte beachten, dass die Bank die Einstellungen ggf. von Zeit zu Zeit minimal ändert.

**Beispiel der CSV-Einstellungen und einer CSV-Datei:**

In diesem einfach gehaltenem Beispiel sehen Sie die CSV-Einstellungen des angelegten Geschäftskontos mit der dazugehörigen CSV-Datei.

![BankViaCSV3.png](https://help.xentral.com/hc/article_attachments/15492843307804)

**Beispieldatei**

![BankViaCSV4.png](https://help.xentral.com/hc/article_attachments/15492810450716)

Zu beachten beim CSV-Import ist, dass die Originaldatei der Bank oder des Zahlungsanbieters importiert wird und diese nicht über andere Systeme geöffnet und (automatisch) gespeichert wurde, da sonst die Originaldatei nicht mehr importfähig ist oder falsche Werte liefert. Bei Amazon Pay handelt es sich bei den "Kontonummern" um die entsprechende Kontonummer aus dem Kontorahmen.

### Kontenspezifische Einstellungen

Im Zahlungseingang doppelte Zahlungen als Importfehler anzeigen: In manchen Fällen sind Zahlungen sehr ähnlich und werden von Xentralfälschlicherweise als Duplikate angesehen. Ist hier ein Häkchen gesetzt, kannst du vermeintliche Duplikate manuell überprüfen und importieren. Duplikate werden dir als Importfehler angezeigt.

**Einzelbuchungen aktivieren **: Sammellastschriften können in Xentral im Modul ** Zahlungsverkehr **erstellt werden. Dabei werden mehrere Zahlungen zu einer gesammelten Zahlung zusammengefasst. Ist bei ** Einzelbuchungen aktivieren**ein Haken gesetzt, so können diese Zahlungen durch Xentral wieder in Einzelpositionen aufgelöst werden. Dies ist in den Kontoauszügen in Xentral sichtbar und erleichtert die Zuordnung der Zahlungen zu Aufträgen, Gutschriften und Rechnungen.

pain.001.001.03: Setze hier ein Häkchen, wenn du eine SEPA XML-Datei im Format pain.001.001.03 erstellen möchtest. Diese Datei kannst du manuell bei deiner Bank hochladen, um die Zahlung von Verbindlichkeiten und Gutschriften einzuleiten.