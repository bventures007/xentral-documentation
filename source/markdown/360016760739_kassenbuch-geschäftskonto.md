Es ist möglich, auch direkt in xentral ein Kassenbuch zu pflegen, um Bar-Transaktionen revisionssicher für die Buchhaltung abzubilden. Außerdem kannst du über das Modul Kassenbuch laufende Buchungen sowie die regelmäßigen Kassenabschlüsse jederzeit schnell tätigen.

Dieses Modul ist besonders relevant, wenn ein Kassenbuch in xentral gepflegt wird oder werden soll.

## Kassenbuch anlegen

Hierzu wird zunächst unter **Administration > Einstellungen > Buchhaltung > Geschäftskonten ** das neue Konto mit einer beliebigen Bezeichnung angelegt und als aktiv markiert. Hierbei muss der Typ **Kasse ** ausgewählt und durch das entsprechende Häkchen verhindert werden, dass Kunden unnötige E-Mails erhalten. Außerdem besteht die Möglichkeit das neue Konto einem Projekt zuzuordnen. Ist zudem bekannt, welcher Kontenrahmen verwendet wird, kann das korrekte Konto in das Feld**DATEV** eingetragen werden, um der Buchhaltung bzw. der Steuerkanzlei dadurch künftig die Arbeit zu erleichtern.

![cashbook_settings.png](https://help.xentral.com/hc/article_attachments/15492895917596)

### Anfangsbestand anlegen

Wenn das Kassenbuch angelegt wurde und das erste mal in das Kassenbuch reingegangen wird, kann ein Kassenanfangsbestand gebucht werden. Es erscheint die Meldung: "Es gibt noch keinen Anfangsbestand in der Kasse! Bevor eine Buchung gemacht wird, kann jetzt ein Anfangsbestand definiert werden."

![cashbook_openingbalance1.png](https://help.xentral.com/hc/article_attachments/15492895954844)

Durch klicken auf die Schaltfläche **Anfangsbestand eintragen **, kann der Anfangsbestand der Kasse angegeben werden. Über die Editor-Schaltfläche kann fortan eine Auflistung aller aktuell gebuchten Transaktionen angezeigt werden. Über die Schaltfläche**+NEU** können über das folgende Menü Buchungen manuell erfasst werden.

![cashbook_openingbalance2.png](https://help.xentral.com/hc/article_attachments/15492862564380)

Die Feldnamen mit einem Sternchen geben Aufschluss darüber, welche Mindestangaben verpflichtend vorgenommen werden müssen, damit das System die Buchung akzeptiert. Neben dem Buchungsdatum und dem Belegfeld ist hier der Buchungsbetrag anzugeben, welcher sich aus drei Einzelfeldern zusammensetzt:

- **Buchungshöhe**: Hier ist in jedem Fall eine positive Zahl einzutragen, welche die Höhe der Buchung widerspiegelt
- **Buchungstyp**: Über das Dropdown Menü wird angegeben, ob es sich bei der Buchung um eine Einnahme oder Ausgabe handelt
- **Steuersatz**: In Abhängigkeit der Voreinstellungen kann zudem ausgewählt werden, mit welchem Steuersatz die Buchung zu besteuern ist, wobei auch die Angabe von 0% zulässig ist. Sofern Buchungspositionen mit unterschiedlicher Besteuerung erfasst werden soll, sind diese als separate Buchungen zu erfassen

Zu beachten ist, dass ein negatives Vorzeichen im Belegfeld grundsätzlich ignoriert wird, da der Buchungstyp gesondert auszuweisen ist. Ein negativer Betrag mit dem Typ Einnahme wird demnach vom System als "echte" und damit positive Einnahme gehandhabt. Im Belegfeld ist eine eindeutige Kennung einzugeben, anhand derer Rückschlüsse auf den zugrunde liegenden Geschäftsvorfall gezogen werden kann.

Zusätzlich zu diesen Pflichtangaben können einige weitere Einträge vorgenommen werden, wodurch in höherem Umfang von der Anwendung profitiert werden kann. Steht die Buchung in Zusammenhang mit einem Kunden des Unternehmens, so kann dies aus den Stammdaten direkt in das Adressfeld übernommen werden. Bei bekanntem DATEV Konto kann auch dieses angegeben sowie angelegte Projekte verknüpft und Bemerkungen (in der Buchungsübersicht sichtbare oder rein interne) eingefügt werden.

Da die Buchungsnummern fortlaufend vergeben werden, empfiehlt es sich, möglichst von Beginn an auf eine korrekte Erfassungsreihenfolge zu achten, um den nachträglichen Arbeitsaufwand zu minimieren. Solange jedoch noch kein Kassenabschluss durchgeführt wurde, ist es jederzeit möglich, Buchungen auch für ein zurückliegendes Datum vorzunehmen.

![CashBook1.png](https://help.xentral.com/hc/article_attachments/15492875125404)

Wie in dem Screenshot ersichtlich ist, wurde hier eine Buchung auf ein zurückliegendes Datum vorgenommen, wodurch die Reihenfolge des Kassenbuches korrigiert werden muss. Dies lässt sich am einfachsten in der Übersicht des Kassenbuchs ändern. Über die Pfeiltasten hoch bzw. runter im rechten Menübereich können einzelne Buchungen verschoben werden. Während die Buchung mithilfe der Schaltflächen an die gewünschte Position verschoben wird, wird die entsprechende Buchungsnummer automatisch korrigiert. Sollten einmal eine Buchung auf ein falsches Datum vorgenommen worden sein, kann auch dies problemlos mithilfe der Pfeiltasten korrigiert werden. Soll eine Buchung zurückdatiert werden, bewirkt ein Klick auf den Pfeil nach unten in dem entsprechenden Eintrag, dass die Buchung unter die unmittelbar vorhergehende gerückt wird.

![cashbook_openingbalance3.png](https://help.xentral.com/hc/article_attachments/15492830434460)

Ein Kassenabschluss kann durch einen Klick auf **Kassenabschluss durchführen** veranlasst werden. Es folgt eine Aufforderung, in der die letzte Buchung auszuwählen ist, die im Rahmen des Abschlusses noch berücksichtigt werden soll.

![cashbook_openingbalance4.png](https://help.xentral.com/hc/article_attachments/15492830497436)

> **Wichtig**
>
> Nach Kassenabschluss kann das Kassenbuch nicht mehr bearbeitet werden! Es gibt keine Möglichkeit den Schreibschutz aufzuheben und Buchungen nachträglich zu ändern. Wird das Kassenbuch mit einer zukünftigen Zahlung abgeschlossen, so können keine weiteren Buchungen abgeschlossen werden, die sich vor diesem Datum befinden.

Sollte der Saldo des Kassenbuchs zu einem beliebigen Zeitpunkt innerhalb des ausgewählten Festschreibungszeitpunkts einen negativen Saldo aufweisen, wird das System mit einer Fehlermeldung reagieren und keinen Kassenabschluss für den fraglichen Zeitraum durchführen, solange der Fehler nicht berichtigt worden ist. Auf diese Weise wird vor nachgelagerten Schwierigkeiten geschützt, da das Finanzamt Minusbestände in der Barkasse als schwerwiegenden Mangel wertet und als Indiz dahingehend interpretiert, dass das Kassenbuch insgesamt nicht ordnungsgemäß geführt worden sein kann.

Wurden alle Einträge korrigiert und der Kassenabschluss erfolgreich durchgeführt, befinden sich die festgeschriebenen Einträge fortan unter dem Reiter **Archiv**. Je nach Bedarf kann in dieser Ansicht sowohl nach Einnahmen, Ausgaben und Bemerkungen gefiltert, gezielt nach Begriffen gesucht oder mit einem Klick auf das Stiftsymbol sämtliche Details einer spezifischen Einzelbuchung angesehen werden.

![cashbook_openingbalance5.png](https://help.xentral.com/hc/article_attachments/15492879603996)

## Kassenbuch exportieren

Soll das Kassenbuch exportiert werden, kann dies über den Reiter **Export** veranlasst werden.

![cashbook_export1.png](https://help.xentral.com/hc/article_attachments/15492846750364)

Hier kann zunächst der Datumsbereich ausgewählt werden, der exportiert werden soll, bevor eine entsprechende CSV-Datei erzeugt wird. Zu beachten ist, dass hierbei nur die Buchungen exportiert werden können, nachdem für diese bereits ein Kassenabschluss durchgeführt wurde.

![cashbook_export2.png](https://help.xentral.com/hc/article_attachments/15492830597660)

Die exportierte CSV-Datei enthält dann neben der Überschrift "Kasse" folgende Angaben:

- Erste Zeile → Anfangsbestand
- Erste Spalte → Fortlaufend vergebene Buchungsnummer
- Zweite Spalte → Buchungsdatum
- Dritte Spalte → Verwendungszweck (bei Buchungen aus der POS bildet dies der Kundenname in Verbindung mit der Rechnungsnummer
- Vierte Spalte → Art der Buchung (Einnahme oder Ausgabe)
- Fünfte Spalte → Betrag
- Sechste Spalte → Währung
- Siebte Spalte → Kassenbestand

## Kassenbuch im "neuen Datev-Format" exportieren

> **Anmerkung**
>
> Du kannst Dateien, wie Kassenbelege, in den Kassenbuchungen hinterlegen. Sie werden jedoch nicht per DATEV übermittelt. Falls du eine Übermittlung per DATEV wünschst, musst du eine Verbindlichkeit im Zahlungseingang anlegen.

Es ist möglich, das Kassenbuch auch im neuen Datev-Format zu exportieren. Dazu müssen folgende drei Schritte getätigt werden:

1. **Kassenabschluss für den Exportbereich durchführen ** Durch Drücken der Schaltfläche **Kassenabschluss durchführen **, muss angegeben werden, bis zu welcher Buchung der Kassenabschluss durchgeführt werden soll. Danach verschwinden die Buchungen aus dem Reiter ** Aktuelle Buchungen **und erscheinen nun im ** Archiv**.

1. **Zahlungseingang für das Kassenbuch durchführen ** Als nächstes ist im Zahlungseingang (**Buchhaltung > Zahlungseingang > Kassenbuch auswählen **) die Schaltfläche ** Live-Import**auszuwählen, damit alle Buchungen geladen werden, bis zu denen ein Kassenabschluss durchgeführt wurde.

  Nach dem "Live-Import" kann nochmals der "Buchungstext, Konto" etc. editiert werden.

  Mit der Schaltfläche **Buchung fertigstellen** werden alle Buchungen die auf der Seite verbucht wurden fertiggestellt.

1. **Export der Daten im neuen Datev-Format ** Danach kann in den Finanzbuchhaltungsexport (**Buchhaltung > Finanzbuchhaltung Export > Buchhaltung Konten**) gewechselt werden. Hier lässt sich das entsprechende Kassenbuch nun als Konto auswählen und für den verbuchten Bereich exportieren.