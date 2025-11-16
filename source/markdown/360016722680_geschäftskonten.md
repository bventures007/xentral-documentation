InXentral kannst du verschiedene Konten anlegen. Hierbei ist es unerheblich, ob das Konto ein Bankkonto ist oder z.B. auch ein Kreditkartenkonto, dessen Bewegungen nur als CSV-Datei vorliegen. So kannst du beispielsweise auch den Kontoauszug von Amazon Payments einspielen und verbuchen. Je nach Anforderungen kannst du z.B. nur das Hauptbankkonto verbuchen und die anderen Konten über das Steuerbüro laufen lassen. Für die Zahlungsweise Kreditkarte kannst du z.B. die Rechnung automatisch auf bezahlt setzen, wenn der Online-Shop ausschließlich abgeschlossene und bezahlte Kundenbestellungen an Xentralübermittelt. Für diesen Fall ist ein Abgleich des Kreditkartenkontos nicht für den Versand der Ware, sondern nur für die Buchhaltung relevant.

## Konten in Xentral verwenden

Die Konten und der Import der Kontoauszüge sind für dich in folgenden Bereichen relevant:

- Schalten der Auftragsampel (automatisches auf "bezahlt"-setzen der Aufträge)
- OPOS-Liste im Mahnwesen (automatischer "bezahlt"-Abgleich)
- SEPA-Überweisungen, Lastschrifteinzug (XML-Datei Export in Banksoftware)
- Buchhaltungsexport in Buchhaltungsprogramme (z.B.[DATEV](https://help.xentral.com/hc/de/articles/360016725100#UUID-ab78107e-071f-f5f8-0eec-571c0ab86efe),[BMD](https://help.xentral.com/hc/de/articles/360016724680#UUID-e5a1b74b-f0c3-57e5-1f08-15809e4ff1cc),[Sage](https://help.xentral.com/hc/de/articles/360016757919#UUID-bd47ad79-541a-2772-71d0-d53928e114e7))
- Digitales Archiv der Kontoauszugszeilen inkl. Suchfunktion über alle Buchungen

### Kontodaten importieren (Kontoauszüge)

Der Zahlungseingang setzt für erfolgreich verbuchte Zahlungen (Betrag komplett) die Auftragsampel auf grün = "bezahlt" (automatisches auf "bezahlt"-setzen der Aufträge). Hat der Kunde z.B. eine Rechnung bezahlt, wird diese über das Verbuchen der Kontoauszugszeile auf "bezahlt" gesetzt. Die Rechnung wird aus dem Mahnwesen ausgebucht (OPOS Liste).

### Kontodaten exportieren

Den Export der Kontoauszüge für die Buchhaltung kannst du im Artikel[Finanzbuchhaltung Export](#)nachlesen.

### Archiv und Suche

Die Kontoauszüge kannst du später digital durchsuchen. So lassen sich z.B. schnell Abbuchungen des Finanzamtes auflisten bzw. finden. Der Aufruf jedes Kontos erfolgt über:

**Buchhaltung > Zahlungseingang > Bearbeiten**

### SEPA Zahlungsverkehr

Analog zum Kontoimport kannst du auch Überweisungen und Lastschrifteinzüge überXentral vornehmen, Informationen zur Einrichtung des SEPA Zahlungsverkehrs befindet sich[hier](https://help.xentral.com/hc/de/articles/360016724700#UUID-bae89b09-9c58-1b7e-ba11-012d734aa381).

### Konto CSV Import

Beachte, dass die Originaldatei der Bank oder des Zahlungsanbieters importiert wird und diese nicht über andere Systeme geöffnet und (automatisch) gespeichert wurde. Sonst ist die Originaldatei nicht mehr importfähig oder liefert falsche Werte. Bei Amazon Pay handelt es sich bei den "Kontonummern" um die entsprechende Kontonummer aus dem Kontorahmen. Weitere Informationen gibt es im Artikel[Konto: Bank per CSV-Import](https://help.xentral.com/hc/de/articles/360020073639#UUID-5f6d6683-98a0-d026-f695-8a17ae8b143c).

## Funktionen eines Kontos

Im Folgenden kannst du die Funktionen eines Kontos nachlesen.

### Live-Import

Der Live-Import kann erfolgen, wenn ein Geschäftskonto die Einstellung Live-Import aktiv besitzt und die Zugangsdaten zur Schnittstelle der Bank korrekt eingetragen sind. Wie die Zugangsdaten bei den einzelnen Kontentypen aussehen müssen, ist in den Artikeln der jeweiligen Geschäftskonto-Module nachzulesen. Diese Kontentypen stehen zur Auswahl und sind in den jeweiligen Kontotypen genauer zu finden unter:

- [Konto: Bank per CSV-Import](https://help.xentral.com/hc/de/articles/360020073639#UUID-5f6d6683-98a0-d026-f695-8a17ae8b143c)
- [Konto: Paypal (API)](https://help.xentral.com/hc/de/articles/360016721920#UUID-5b7950ea-43de-e5a2-45a6-d9e4455abe51)
- [Konto: Stripe (API)](https://help.xentral.com/hc/de/articles/360016761459#UUID-4869205f-8168-2f09-4a2d-b77c662d5f71)
- [Konto: Shopify (API)](https://help.xentral.com/hc/de/articles/360016728160#UUID-a9a70e1b-1629-93ed-bfc2-9e336aa68454)
- [Konto: Klarna](https://help.xentral.com/hc/de/articles/360016721160#UUID-cdbbd77b-9f3c-5b8c-c2fe-7b68e0449bcb)
- [Konto: Amazon Zahlungsberichte](https://help.xentral.com/hc/de/articles/360017421159#UUID-ea6fa560-1491-ecf6-62ee-be6502477890)
- [Konto: AmazonPay (API)](https://help.xentral.com/hc/de/articles/360017324559#UUID-32787e16-b216-3d06-3ab8-d98509ec6498)
- [Konto: Ebay Payment (API)](https://help.xentral.com/hc/de/articles/360020793079#UUID-41b5d896-edec-d26c-3421-a79fee13e322)
- [Kasse](https://help.xentral.com/hc/de/articles/360016760739#UUID-31965de0-71ed-7cd0-ab79-14c3c5a0ffe2)
- Sonstige Verbindlichkeiten Firma
- Verrechnungskonto
- Custom

Hierbei gibt es die Option, maximal zurückliegende Kontoauszüge anzugeben, um so Fehlermeldungen von der Bank zu vermeiden, da es sein kann, dass wen die Kontoauszüge zu lang zurückliegen, bei jeder Abfrage eine TAN eingegeben werden muss. Die Variable hierfür lautet: API_MAX_DAYS_BEFORE.

Mit der Einstellung **Zeitraum ** wird festgelegt, wie oft der Import erfolgen soll und mit der Schaltfläche**zu Zeiten** wird die Uhrzeit festgelegt, zu dem der Import erfolgen soll.

- **Live Import**: Diese Option aktiviert den Live-Import.
- **Zeitraum**: Festlegung der Häufigkeit, mit der der Import erfolgen soll.
- **zu Zeiten**: Festlegung der Uhrzeit, zu der der Import erfolgt.
- **Zugangsdaten**: Eintragung der Zugangsdaten zur Schnittstelle der Bank.
- **Passwort Tresor**: Angabe eines Passworts.

> **Anmerkung**
>
> Ein Wechsel zwischen Live-Import und CSV führt ggf. zu doppelten Buchungen.Xentral filtert nur komplett identische Buchungen aus. Bei einer Formatänderung der Bank oder des Importkanals kommt es meist zu Abweichungen der Buchungsinformationen, sodass die Buchungen nicht als doppelt erkannt werden. In diesem Fall sollte der Importzeitraum möglichst ohne Überschneidung gewählt werden. Doppelte Buchungen können auf **Importfehler** gebucht werden.

#### Zahlungen automatisch im Hintergrund verbuchen

Die Einstellung **Zahlungseingänge automatisch verbuchen ** ist auf**aktiv** zu setzen, sodass die Zahlungseingänge automatisch verbucht werden. Alle Buchungen, die grün hinterlegt sind, also eindeutig zugeordnet werden können, werden dann automatisch auf Auftrag/Rechnung/etc. verbucht.

Für diese Funktion muss der Prozessstarter "Zahlungseingang" aktiviert sein und laufen.

## Neues Konto anlegen

Ein neues Geschäftskonto legst du im Menü **Buchhaltung > Geschäftskonten ** an, indem du oben rechts auf**+ NEU** klickst.

Befülle folgende Felder:

- **Bezeichnung**: Vergib eine eindeutige Kontobezeichnung pro Konto (z.B. Sparkasse Musterstadt, PayPal, PayPal Plus, Amazon Payments Transaktionen etc.). Diese Bezeichnung erscheint beim Aufruf der Konten in der Buchhaltung
- **Typ**: Wähle den Typ, wie zB CSV Import, Live Import (sofern es das Konto unterstützt), aus dem Drop-Down Menü aus
- **Projekt**: Ordne das Konto optional einem Projekt zu. Trage dieses händisch ein oder wähle es über das "Lupe"-Icon aus der Liste aus. Die Zuordnung dient der Einschränkung der Sichtbarkeit. Nur Benutzer, die das Projekt des Geschäftskonto als Rolle besitzen, können es auch sehen und damit arbeiten
- **Aktiv**: Um das Konto zu aktivieren, setze hier den Haken
- **Keine E-Mail**: Normalerweise wird beim Zahlungseingang eine Mail an den Kunden gesendet. Soll dies unterdrückt werden, musst du diese Option anhaken.
- **Änderungen erlauben **: Durch Anhaken erlaubst du die nachträgliche Veränderung vonKontobuchungen ** Bankverbindung (bei Typ Bank)**

-** Inhaber**: Trage den Inhaber des Bankkontos ein
- **BIC**: Trage die BIC des Bankkontos ein
- **IBAN**: Trage die IBAN des Bankkontos ein
- **BLZ**: Trage die BLZ des Bankkontos ein
- **Konto**: Trage die Kontonummer für dieses Bankkonto ein
- **Gläubiger ID**: Trage die Gläubiger ID des Bankkontos ein. Dieses Feld ist verpflichtend bei bei einem Lastschrifteinzug
- **Lastschrift **: Durch Anhaken aktivierst du den Lastschrifteinzug bei diesem Konto ** DATEV **

-** Konto**: Trage die Nummer des Kontenrahmens für das Bankkonto ein, je nach Kontenrahmen 1000, 1700 usw.. Benötigt wird dieses Feld für den Export von Kontoauszügen

Klicke abschließend auf **Speichern**.

Die weiteren Einstellungen werden je nach Kontotyp individuell vorgenommen.

**Hinweis zum Versenden der E-Mail im Feld "Keine E-Mail"**: Soll die Mail beim Zahlungseingang versendet werden, ist zunächst die Option ** Keine-Email **nicht zu aktivieren. Zudem ist folgende, zusätzliche Einstellung unter ** Stammdaten > Projekte **nötig. Editiere den zum Konto dazugehörigen Eintrag über das ** Stift **

-Icon, navigiere zu ** Einstellungen > Grundeinstellungen **und hake ** Zahlungsmail **an. Klicke abschließend auf ** Speichern**.

## FAQ

### Woran liegt es, dass das Saldo meines Bankkontos bzw. meines PayPal-Kontos in Xentral nicht mit dem tatsächlichen Kontostand übereinstimmen?

Folgende Gründe kommen in Frage:

- Der **Anfangsbestand** des Kontos wurde nicht richtig eingetragen. Dann stimmt das Saldo trotz vollständiger Importe nicht.
- **Import-Zeitpunkt**: Wenn Zahlungen vom vorherigen Tag am darauffolgenden Tag rückwirkend importiert werden, kann es dazu kommen, dass das Ergebnis "verfälscht" wird. Am besten holst du hier alle Buchungen bis zu einem Stichtag komplett rein, verbuchst sie und setzt dann noch einmal den Kontostand im Geschäftskonto in Xentral neu.
- Beachte bei **PayPal** zusätzlich Folgendes:
  - **Gebühren **: Gebühren werden beim Zahlungseingang von PayPal in Xentral nicht berücksichtigt. Diese kannst du aber am Monatsende im Tab ** Kontoblatt** manuell eingeben.
  - **Währungsumrechnung**: Bei PayPal musst du oftmals Währungsumrechnungen als Importfehler buchen. Alternativ kannst du ggf. auch beide Seiten als Umrechnungstransit buchen. Bei einer Ausgabe von 120 US-Dollar werden z.B. erst 120 US-Dollar abgebucht, dann 120 US-Dollar zurückerstattet und eine Abbuchungen von 100 Euro getätigt (bei einem Kurs von 1,2 USD = 1 EUR)

### Beim.csv Import von Kontoauszügen gibt es manchmal Buchungen ohne Betrag / 0 EUR Buchungen. Ist das richtig?

In der Regel sollten beim Import keine 0 EUR Buchungen auftauchen. Meistens handelt es sich hier um einen Fehler bei der Vergabe der Felder in Xentral. Prüfe hier nochmal die Einstellungen der Bankkonten im MenüBuchhaltung > Geschäftskonten.

Eventuell enthält die Datei der Bank noch Leerzeilen oder Informationszeilen nach der letzten Bankbuchung. Diese können manuell abgeschnitten werden. Öffne die entsprechende Bankverbindung und schreibe im Bereich CSV-Import in das Feld **Letzte Zeilen ignorieren** die Anzahl der Zeilen die abgeschnitten werden sollen.

Es gibt aber auch Banken, die ab und an eine eigene Buchung mit 0 EUR z.B. am Monatsende auf dem Kontoauszug haben. Diese kannst du z.B. als Importfehler buchen, wenn das nachfolgende Buchhaltungsprogramm keine Null-Werte einlesen kann. Dann wird diese Zeile beim Export aus Xentral nicht mitgenommen, sondern "ausgeschnitten".