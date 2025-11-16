Im Unternehmensalltag werden Zahlungen über verschiedene Wege abgewickelt – z. B. per Überweisung, Lastschrift oder über Bezahldienste wie PayPal oder Stripe. Diese Zahlungsvorgänge müssen in der Buchhaltung nachvollziehbar dokumentiert und den passenden Belegen zugeordnet werden. Xentral bietet dafür ein eigenes Modul, mit dem du Kontoauszüge importieren und Buchungen verarbeiten kannst – unabhängig vom verwendeten Zahlungskanal. So stellst du sicher, dass Zahlungsein- und -ausgänge korrekt erfasst und für den weiteren Buchhaltungsprozess bereitstehen.

Die Verwaltung von Zahlungseingängen ist ein zentraler Bestandteil der Buchhaltung. In Xentral kannst du Kontoauszüge aus verschiedenen Quellen wie[Bankkonten](https://help.xentral.com/hc/de/articles/6380930667548#UUID-aa9fdcf6-d617-bcfe-7bdf-0c6af1ce7a16),[PayPal](https://help.xentral.com/hc/de/articles/360016721920#UUID-5b7950ea-43de-e5a2-45a6-d9e4455abe51)oder Stripe importieren – entweder manuell als CSV-Datei oder automatisiert über die PSD2-Schnittstelle. Die Buchungen lassen sich dabei direkt mit den passenden Belegen wie Rechnungen, Aufträgen oder Gutschriften verknüpfen. So behältst du den Überblick über offene Posten, vermeidest doppelte Zahlungen und bereitest deine Daten sauber für den Buchhaltungsexport vor. In diesem Artikel erfährst du Schritt für Schritt, wie der Import funktioniert, wie du Zahlungen zuordnest und welche Möglichkeiten dir bei Sonderfällen wie Rücklastschriften oder Teilzahlungen zur Verfügung stehen.

> **Anmerkung**
>
> **Hinweis**
>
> Neben dem Standardprozess für den Import und die Verknüpfung von Zahlungen bietet Xentral weitere Funktionen, die dich bei der Nachbearbeitung, Auswertung und Organisation deiner Buchungsdaten unterstützen.
>
> - **Importmöglichkeiten von Kontoauszügen**: Kontoauszüge können in Xentral entweder manuell per CSV-Datei oder automatisiert über die PSD2-Schnittstelle (Live-Import) eingebunden werden. Die meisten Banken und Zahlungsdienstleister wie PayPal oder Stripe werden unterstützt.
> - **Voraussetzung für den Import**: Für jedes genutzte Konto muss in Xentral ein Geschäftskonto angelegt sein. Erst dann ist ein Import möglich.
> - **Verknüpfung mit Belegen**: Eingehende Zahlungen können mit Rechnungen, Gutschriften, Aufträgen oder Verbindlichkeiten verknüpft werden. Automatisch erkannte Buchungen werden grün markiert; manuelle Zuordnungen sind ebenfalls möglich.
> - **Kennzeichnung der Buchungen**: Farbmarkierungen in der Übersicht zeigen den Verbuchungsvorschlag einer Buchung an (z. B. grün = korrekt gefunden, grau = noch offen, rot = Ausgabe). Eine Übersicht aller Farben findest du im Artikel.
> - **Zahlungen splitten oder aufteilen**: Eine Buchung kann auf mehrere Belege verteilt oder als Teilzahlung erfasst werden. Auch Rücklastschriften lassen sich erneut auf eine Rechnung buchen.
> - **Verbindlichkeiten**: Zahlungen können auch auf offene Verbindlichkeiten gebucht werden. Dabei wird der Status automatisch auf "bezahlt" gesetzt – ein Rücksetzen ist manuell nicht vorgesehen.
> - **Klärfälle**: Nicht zuordenbare Buchungen können als Klärfall markiert und separat ausgewertet werden.
> - **Manuelle Anpassung**: Buchungen lassen sich im Detail bearbeiten und bei Bedarf aufteilen oder neu zuordnen.
> - **Verknüpfungen auflösen**: Bestehende Buchungszuordnungen können zurückgesetzt und neu verarbeitet werden.
> - **Zusätzliche Optionen**: Übersicht über Soll, Haben und Salden je Konto und Zeitraum Volltextsuche in Kontoauszügen Manuelle Erfassung von Zahlungseingängen (für Offline-Konten, Beta) Buchung regelmäßiger Gebühren über automatische Verbindlichkeiten Kontenblatt zur Durchsuchung von Kontobeziehungen und Gegenkonten.

## Import und Erkennung von Kontoauszügen

Wenn du mit der Finanzbuchhaltung in Xentral arbeitest, ist die Konten-Übersicht deine zentrale Anlaufstelle für die Verwaltung aller Bankkonten, Kassen und sonstiger Finanzkonten. In dieser Ansicht kannst du bestehende Konten prüfen, neue Konten hinzufügen und auf einen Blick erkennen, auf welchen Konten noch offene Buchungen vorhanden sind.

### Zahlungseingang Kontenübersicht

Die Übersicht deiner aktiv geschalteten Geschäftskonten findest du unter **Buchhaltung > Zahlungseingang.**

Standardspalten in der Tabelle:

- **Bezeichnung**: Der Name des Kontos, meist mit Kontonummer (z. B. 1700_Postbank).
- **Konto-Art**: Gibt an, ob es sich um ein Bankkonto, ein Kassenkonto, PayPal oder eine andere Kontoart handelt (z. B. konto, kasse, paypal, finapi).
- **IBAN / BIC**: Bankverbindung, sofern vorhanden.
- **Saldo**: Zeigt den aktuellen Kontostand an, wenn dieser z. B. durch finAPI oder einen CSV-Import bereitgestellt wurde.
- **Projekt**: Wenn das Konto einem bestimmten Projekt zugeordnet ist
- **Menü**: Kontextmenü für Aktionen (z. B. Konto bearbeiten, Kontoauszüge einsehen)

![zahlungseingang_bankkonten_uebersicht_001.png](https://help.xentral.com/hc/article_attachments/20764230607900)

> **Tipp**
>
> **Offene Buchungen erkennen**:
>
> In der Kontenübersicht kannst du sehen, auf welchen Konten offene Buchungen vorhanden sind. Konten mit offenen Buchungen sind durch eine Markierung oder einen Hinweis im Menü-Feld oder direkt im zugehörigen Kontenblatt gekennzeichnet.
>
> Diese Informationen helfen dir, schnell zu identifizieren, wo noch Zuordnungen oder Bearbeitungen notwendig sind.
>
> **Filterfunktionen in der Kontenliste:**
>
> Um die Ansicht zu filtern oder gezielt nach Konten zu suchen, stehen dir folgende Funktionen zur Verfügung:
>
> - **auch inaktive**: Aktiviert die Anzeige inaktiver Konten
> - **Suche**: Volltextsuche über alle Konten
> - **Spaltensuche**: Separate Eingabefelder pro Spalte (Bezeichnung, Konto-Art, IBAN, BIC, Saldo, Projekt)

### Konto Import

In Xentral stehen dir zwei Möglichkeiten zur Verfügung, um Kontoauszugsdaten in ein Bankkonto zu importieren:

> **Warnung**
>
> **Verwende nur eine Importvariante pro Bankkonto!**
>
> Bitte entscheide dich je Bankkonto **entweder für den Live-Import oder den CSV-Import **. Die gleichzeitige Nutzung beider Varianten kann zu ** doppelten oder abweichenden Buchungen führen**, da:
>
> - der Live-Import teilweise andere Felder liefert als dein individuelles CSV-Format.
> - Buchungen doppelt eingelesen werden können, wenn sie aus beiden Quellen stammen.
>
> **Ausnahme: Konten mit kombinierter Importfunktion**
>
> Einige Konten wie z. B. PayPal sind in Xentral standardmäßig für beide Methoden freigegeben. Hier kannst du zusätzlich zum Live-Import auch CSV-Dateien einspielen – z. B. dann, wenn du bei Auftragsspitzen mehr Daten benötigst, als der automatische Abruf rechtzeitig liefern kann.

#### Live-Bankanbindung (z. B. via finAPI, PayPal)

Wenn du ein Bankkonto über eine Live-Schnittstelle angebunden hast, kannst du Kontoauszüge entweder:

- **manuell per Button** abrufen, oder
- **automatisch im Hintergrund ** im festgelegten **Zeitintervall** abrufen lassen (Einstellung im Konto).

Diese Methode ist für alle gängigen Bankkonten vorgesehen, die über finAPI unterstützt werden und Zahlungsanbieter wie PayPal. Die Buchungen werden dabei standardisiert importiert und enthalten strukturierte Zusatzinformationen (z. B. Gegenkonto, Buchungstext, Verwendungszweck aufgeschlüsselt in Felder).

#### Manueller CSV-Import

Alternativ kannst du Kontoauszüge manuell per CSV-Datei in ein Konto importieren. Die Upload-Funktion findest du direkt im jeweiligen Bankkonto unter dem Menüpunkt CSV Import. Diese Methode eignet sich z. B. für:

- Banken, die nicht via finAPI angebunden werden können
- Spezialformate oder angepasste Kontodaten
- Fälle, in denen du gezielt Daten korrigieren oder nachtragen möchtest

> **Anmerkung**
>
> **Best Practices:**
>
> - Wenn du **CSV-Import** nutzt, definiere ein klares internes Format und passe es ggf. an das Xentral-Importschema an.
> - Wenn du **Live-Import** nutzt, stelle sicher, dass das Konto korrekt angebunden ist und der Abruf funktioniert (Statusanzeige im Konto prüfen).
> - Prüfe regelmäßig, ob doppelte Buchungen vorhanden sind – insbesondere nach einem Importwechsel.

### Konto Buchungserkennung und - zuordnung

Beim Import von Kontoauszügen – egal ob über eine Live-Bankverbindung oder per CSV – erkennt Xentral automatisch, ob es sich um Einnahmen oder Ausgaben handelt und versucht, Zahlungen mit vorhandenen Belegen (z. B. Rechnungen, Aufträgen, Gutschriften oder Verbindlichkeiten) zu verknüpfen.

![zahlungseingang_buchungen_bankkonto_ausgaben_kundenzahlungen.png](https://help.xentral.com/hc/article_attachments/20764246638236)

**Schritte:**

1. Klicke in das betreffende Bankkonto im Zahlungseingang.
1. Wähle in der Infobox für den **automatischen Abgleich ** den Button **Starten**.
1. Der **Automatische Abgleich ** startet und **ermittelt die Buchungsvorschläge **. Bei kleineren Buchungsmengen erhältst du das Ergebnis innerhalb einer Minute. Bei größeren Datenmengen wird dir der ** Fortschritt in der Infomeldung angezeigt** und aktualisiert.
1. Die Eingangs- und Ausgangszahlungen kannst du über **Buchungen fertigstellen ** oder **Alle automatisch abgeglichenen Transaktionen abschliessen** verbuchen.

> **Anmerkung**
>
> Die Berechnungsmenge kannst du über den Zeitraum in den Einstellungen steuern s.u:Einstellungen Abgleichszeitraum.

#### Farbkennzeichnung von Buchungen

Xentral nutzt eine Farbmarkierung, um dir auf einen Blick den Status und Typ jeder Buchung anzuzeigen:

| Farbe | Bedeutung |
| --- | --- |
| Grün | Einnahme wurde automatisch erkannt und erfolgreich mit einem passenden Auftrag oder einer Rechnung verknüpft (Buchungsvorschlag) |
| Grau | Einnahme, die noch nicht automatisch zugeordnet wurde |
| Rot | Ausgabe, die nicht automatisch zugeordnet wurde |
| Lila | Ausgabe, die erfolgreich mit einer Verbindlichkeit verknüpft wurde |
| Orange | Zahlung wurde einem stornierten Beleg, einem bereits bezahlten Beleg oder einer unsicheren Übereinstimmung zugeordnet (z. B. korrekte Rechnungsnummer, aber nicht eindeutig) |

## Zahlungseingang Übersichtsfunktionen und manuelle Buchungen

In diesem Abschnitt erhältst du einen kompakten Überblick über die wichtigsten Tabs im Bereich der Finanzübersicht. Jeder Reiter erfüllt eine spezifische Funktion – von der Anzeige einzelner Kontoauszüge bis hin zur Auswertung von Salden oder der Konfiguration individueller Kontenansichten.

Im Folgenden werden die Tabs **Übersicht **, ** Alle Kontoauszüge **, ** Kontenblatt **, ** Summen und Salden ** sowie **Einstellungen** im Detail erklärt.

### Übersicht

> **Anmerkung**
>
> **Hinweis**
>
> In der Übersicht werden dir die Konten inkl. der offenen Buchungen angezeigt s.o.:Zahlungseingang Kontenübersicht

### Alle Kontoauszüge

Im Tab **Alle Kontoauszüge ** findest du eine tabellarische Übersicht aller importierten Bankbewegungen. Die Tabelle bildet den zentralen Arbeitsbereich für die Prüfung, Nachbearbeitung und Klärung von Zahlungsein- und -ausgängen. Jede Zeile entspricht einem einzelnen Buchungsvorgang. **Filterfunktionen (oberhalb der Tabelle):**

Zur gezielten Eingrenzung der angezeigten Daten stehen dir mehrere Filter zur Verfügung:

- **Klärfälle** – zeigt nur Buchungen mit ungeklärtem Status
- **Importfehler** – listet fehlerhafte oder unvollständige Importzeilen
- **Ohne Importfehler** – zeigt nur technisch einwandfreie Buchungen
- **Status prüfen** – zeigt Buchungen, die manuell überprüft werden müssen
- **Buchungstext statt Kontoauszugstext**

- zeigt Buchungen, die einen Buchungstext eingegeben und aktiviert haben
- **Soll / HABEN** – schränkt die Anzeige auf Ein- oder Auszahlungen ein
- **Von / Bis (Datum)**– grenzt den Zeitraum der Buchungen ein ** Tabellenspalten und Suchfelder:**

Jede Spalte der Tabelle verfügt über ein eigenes Suchfeld, mit dem du gezielt nach Inhalten filtern kannst. Die verfügbaren Spalten sind:

- **Vom** (Buchungsdatum)
- **Konto** (zugeordnetes Bankkonto)
- **Nr** (laufende Nummer der Buchung)
- **Vorgang/Buchungstext** (Name, Vorgangsnummer, Buchungstext)
- **Gegenkonto** (automatisch oder manuell zugeordnetes Konto)
- **Kostenstelle **

-** Soll** (Ausgangsbetrag)
- **HABEN** (Eingangsbetrag)
- **Gebühr** (Bankkosten, falls vorhanden)
- **Status** (z. B. offen, gebucht, prüfen)
- **Menü** (Aktionen wie Zuweisung, Bearbeiten, Löschen)

![zahlungseingang_alle_kontoauszuege.png](https://help.xentral.com/hc/article_attachments/20764246644636)

### Kontenblatt & manuelle Buchungen

Das Kontenblatt zeigt alle Buchungen eines bestimmten Kontos in chronologischer Reihenfolge. Diese Ansicht dient der gezielten Nachverfolgung und Analyse von Buchungen innerhalb eines Kontos, z. B. für Abstimmungen, Prüfungen oder zur Vorbereitung des Jahresabschlusses.

Im Bereich Kontenblatt kannst du Kontoauszüge gezielt nach bestimmten Konten filtern und durchsuchen. Grundlage dafür sind die im System hinterlegten Konten aus dem Kontenrahmen.

Im Kontenblatt werden folgende Daten ausgewertet:

1. Sachkonten aus dem Modul [Kontenrahmen](https://help.xentral.com/hc/de/articles/360016775339#UUID-92298972-2029-3a2c-00ce-a5bdd614203c).
1. Gegenkonten aus den Kontoauszügen – geprüft wird dabei, ob das Gegenkonto einer Kunden- oder Lieferantennummer zugeordnet werden kann.
1. [Geschäftskonten](#UUID-52941a15-b42a-09c5-ac22-b8f72d671c79), die als DATEV-relevant gekennzeichnet sind (Feld DATEV im Geschäftskonto ist ungleich „0“).

**Filter oberhalb der Tabelle:**

Mit den Filterfeldern kannst du die Anzeige auf bestimmte Buchungen eingrenzen:

- **Gegenkonto** – Filtert nach zugeordnetem Gegenkonto
- **Von / Bis (Datum)**– Eingrenzung des Buchungszeitraums ** Statusinfoanzeige (über der Tabelle):**

Diese Anzeige gibt dir eine schnelle Übersicht über den aktuellen Zustand des gewählten Kontos:

- **Haben**: Gesamtbetrag aller Haben-Buchungen
- **Soll**: Gesamtbetrag aller Soll-Buchungen
- **Saldo**: Differenz aus Haben und Soll
- **Anzahl Buchungen **: Gesamtanzahl der Buchungszeilen ** Spaltensuche unterhalb der Tabellenüberschriften:**

Jede Spalte besitzt ein eigenes Suchfeld, über das du gezielt nach Werten filtern kannst. Die verfügbaren Spalten sind:

- **Datum **

-** Konto **

-** Gegenkonto **

-** Kostenstelle **

-** Buchungstext **

-** Belegefeld1 **

-** Soll **

-** Haben **

-** Währung **![zahlungseingang_kontenblatt.png](https://help.xentral.com/hc/article_attachments/20764246645788)** Manuelle Buchung:**

Xentral bietet dir die Möglichkeit, Zahlungseingänge auch manuell zu erfassen – insbesondere dann, wenn es sich um Geschäftskonten ohne Online-Banking-Anbindung handelt oder kein Kontoimport vorgesehen ist.

Für die Erfassung wählst du zunächst das entsprechende Bankkonto aus. Dieses ist Teil des Sachkontenrahmens und wird als Bilanzkonto geführt. Weitere Voreinstellungen sind für eine manuelle Buchung nicht erforderlich.

Bei der Buchung kannst du festlegen, ob sie einem **Debitor **, ** Kreditor **, einem ** Sachkonto**oder einer Kategorie aus Bilanz bzw. GuV zugeordnet werden soll. So bleibt die Buchführung auch bei manuellen Vorgängen strukturiert und nachvollziehbar.

> **Anmerkung**
>
> Das Feld **Gegenkonto ** ist optional. Wenn du die Buchung ohne Gegenkonto speicherst, kannst du die Zuordnung später im Modul Zahlungseingang vornehmen. **Erfassbare Felder:**

-** Währung** (z. B. EUR)
- **Soll (S)**

-** Haben (H)**

- Gegenkonto (optional)
- Kostenstelle (optional)
- Belegfeld 1 (optional)
- **Datum **

-** Konto **

-** Buchungstext**

![zahlungseingang_kontoblatt_manuelle_buchung.png](https://help.xentral.com/hc/article_attachments/20764230617500)

### Summen und Salden

Im Tab Summen und Salden erhältst du eine Übersicht der Soll-, Haben- und Saldenwerte pro Konto für einen wählbaren Zeitraum. Den Zeitraum legst du über die Filterfelder **Datum von ** und**Datum bis** fest.

- **Haben**: Summe aller positiven Beträge (Einnahmen) aus den Kontoauszügen
- **Soll**: Summe aller negativen Beträge (Ausgaben)
- **Saldo**: Differenz zwischen Haben und Soll
- **Startsaldo**: Kontostand zu Beginn des gewählten Zeitraums

Zusätzlich werden die Kontonummer, die Bezeichnung und die Anzahl der Buchungen je Konto angezeigt. In der letzten Zeile findest du die Gesamtsummen über alle Konten hinweg für den ausgewählten Zeitraum.

![zahlungseingang_summen_und_salden.png](https://help.xentral.com/hc/article_attachments/20764230618908)

> **Anmerkung**
>
> In diesem Bereich werden nur Konten mit Buchungen angezeigt.

## Einstellungen Toleranz

Legt fest, in welchem Umfang der Zahlungseingang vom erwarteten Betrag abweichen darf.

**Bedeutung**: Bei aktivierter Toleranz werden geringe Differenzen – z. B. Rundungsabweichungen von 1 Cent – bei der automatischen Zuordnung zu Aufträgen oder Rechnungen akzeptiert. Die Zahlung wird trotz der Abweichung korrekt mit dem zugehörigen Beleg verknüpft.

## Einstellungen Abgleichszeitraum

In den Systemeinstellungen kannst du festlegen, welcher Zeitraum beim Zahlungsabgleich berücksichtigt wird. Dabei wird bestimmt, welche offenen Buchungen in die automatische Zuordnung einbezogen werden sollen – zum Beispiel die letzten 3 Monate, 6 Monate, das letzte Jahr, die letzten 2 Jahre oder ohne zeitliche Begrenzung.

> **Tipp**
>
> Bei einer großen Anzahl an Transaktionen empfiehlt es sich, den Abgleichszeitraum auf die letzten 3 Monate zu begrenzen. So wird die Berechnung nur auf einen aktuellen und relevanten Teil der offenen Buchungen angewendet, was die Performance deutlich verbessert – insbesondere dann, wenn du ältere offene Buchungen erst zum Jahresabschluss bearbeitest oder nicht alle Zahlungen vollständig verbuchst.

![zahlungseingang_settings_beschleunigungsoptionen_001.png](https://help.xentral.com/hc/article_attachments/20764246649372)

## Zahlungseingang - Import von Kontoauszügen

Heute bieten Banken ihren Kunden die Möglichkeit, alle Kontobewegungen jederzeit über ein Webportal als CSV-Datei zu exportieren. Diese CSV Dateien können in Xentral importiert werden, um Zahlungsein- und abgänge im System zu registrieren, und mit den entsprechenden Vorgängen zu verknüpfen. Die meisten Banken bieten zudem die Möglichkeiten eines automatisierten oder automatischen Live Imports via der PSD2-API.

Weitere Informationen dazu, wie du Kontoauszüge importierst, findest du[hier](https://help.xentral.com/hc/de/articles/6380930667548#UUID-aa9fdcf6-d617-bcfe-7bdf-0c6af1ce7a16).

Um die Kontobewegungen importieren zu können, muss in Xentralfür jedes der Konten ein[Geschäftskonto](https://help.xentral.com/hc/de/articles/360016722680#UUID-7723b7cc-cc0e-d54d-24cb-3815c4ae2a94)definiert werden.

InXentralkönnen die Buchungen deiner Geschäftskonten importiert werden. Dazu zählen nicht nur Bankkonten, sondern auch PayPal, Stripe und viele weitere.

Unter **Buchhaltung**> Zahlungseingang kannst Du für jedes Deiner angebunden Geschäftskonten einen Zahlungsimport durchführen, um alle Buchungen dieses Kontos in Xentral hinterlegt zu haben. Das ermöglicht die Verknüpfung aller Buchungen auf ihre zugehörigen Belege, also Rechnungen, Gutschriften und Verbindlichkeiten. Diese Verknüpfung kann mit einem Klick für alle Buchungen durchgeführt werden, die einem Beleg anhand von Betrag und Verwendungszweck eindeutig zuzuordnen sind. Erkennbar ist das an den grün hinterlegten Zeilen. Übrige Buchungen können mit wenigen weiteren Klicks manuell verknüpft werden. Die Markierung der Belege als "bezahlt" erfolgt dadurch automatisch. Für jede Buchung wird in Xentral ein Kontoauszug erstellt. Über diesen ist bei Korrekturbedarf auch eine Auflösung einer Verknüpfung möglich.

Im Bereich Kontenblatt können Sie Kontoauszüge nach den Konten aus dem Kontenrahmen gefiltert durchsuchen. Dort werden die Konten aus dem Modul Kontorahmen durchsucht, die Gegenkonten aus den Kontoauszügen herausgesucht und dort geprüft, ob das Gegenkonto einer Kunden- oder Lieferantennummer entspricht. Ebenso werden die die Geschäftskonten durchsucht, die DATEV-Konten sind. Das ist der Fall, wenn im Geschäftskonto das Feld "DATEV" anders gefüllt ist als mit "0".

## Übersicht Zahlungseingang

### Import der Kontoauszugs-Dateien

Die aktuellen Kontoauszüge der Geschäftskonten kannst du importieren, um Zahlungseingänge mit offenen Aufträgen zu verknüpfen und damit für den Buchhaltungsexport vor zu kontieren.

Wähle dazu das Stift-Icon in der Menü-Spalte in der Übersicht (Buchhaltung → Zahlungseingang) an.

> **Anmerkung**
>
> Wenn du denLive-Importim jeweiligen Geschäftskonto aktiviert hast, geht das über den Button Live-Import. CSV-Dateien kannst du über *Durchsuchen* und *Importieren* einspielen.

Wenn du das Stift-Icon ausgewählt hast, gelangst du in diese Maske:

![ReceiptOfPayment1.png](https://help.xentral.com/hc/article_attachments/5033340473628)

- Einnahmen sind grau markiert
- Ausgaben sind rot markiert
- Gefundene Aufträge/ Rechnungen sind grün markiert

Xentral erkennt beim Kontoimport automatisch, ob eine Buchung zu einem früheren Zeitpunkt bereits importiert wurde. In diesem Fall wird die Buchung nicht erneut importiert.

Mit dem Button "Alle automatisch erkannten Buchungen fertigstellen" werden alle erkannten Buchungen sofort auf einmal verbucht, unabhängig davon, ob diese sich auf anderen Seiten befinden.

### Verknüpfen der Zahlungen (Auftrag, Rechnung, Gutschrift, Verbindlichkeit)

Wenn der Betreff einer Überweisung Hinweise auf eine(n) Rechnung/Auftrag enthält und der Überweisungsbetrag mit dem Auftragswert übereinstimmt, schlägtXentral die passende Verknüpfung automatisch vor (grüne hinterlegte Zeilen im Screenshot). Dabei werden Zahlungen bei Vorkasse-Bezahlarten (z.B. PayPal, Kreditkarte, Vorkasse) mit Aufträgen und bei anderen Bezahlarten mit Rechnungen verknüpft (z.B. Zahlung auf Rechnung, Barzahlung, Nachnahme).

Nicht automatisch erkannte Zahlungseingänge bleiben grau hinterlegt, und können manuell mit den passenden Aufträgen/ Rechnungen/ Gutschriften verknüpft werden. Zahlungsabgänge werden in der Import-Ansicht rot hinterlegt.

In der Übersicht der Zahlungseingänge gibt es eine direkte PDF-Vorschau für die Belege, die verknüpft werden können (Verbindlichkeiten, Rechnungen, Gutschriften und Aufträge).

Um welche Art der Buchung es sich handelt, ist an der Farbe der Zeile erkenntlich:

- Grün = Zahlungseingang, der erfolgreich auf eine Rechnung oder einen Auftrag verknüpft werden konnte
- Grau = Nicht erkannte Einnahme bzw. positive Buchung
- Rot = Ausgabe bzw. negative Buchung, die nicht zugeordnet werden konnte
- Lila = Negative Buchung, die einer Verbindlichkeit zugeordnet werden konnte
- Orange = Erkannte Buchung
  - auf stornierten Auftrag/ Rechnung
  - auf Auftrag/ Rechnung mit bereits verknüpfter Zahlung
  - auf eine Rechnung/ POS-Rechnung, die durchs System automatisch als bezahlt markiert wurde (aber ohne direkt darauf gebuchten Zahlungseingang)
  - mit passender Nummer, bei der sich Xentral jedoch nicht komplett sicher ist, ob sie stimmt

### Klärfall

Ein schnelles Erstellen von Klärfällen ist direkt in der Übersicht Zahlungseingang möglich. Über das!-Icon erscheint das Dialogfenster, um die Buchung als Klärfall zu markieren und einen Grund zu hinterlegen.

Nach Klärfällen kann im Reiter Kontoauszüge gefiltert werden. Diese Markierung kann zum Beispiel der Kommunikation zwischen dem Mitarbeiter, der den Zahlungseingang bearbeitet und der Buchhaltung dienen.

> **Anmerkung**
>
> Der Grund des Klärfalls wird im Buchhaltungsexport für das DATEV-Format nicht mit exportiert. Allerdings kann die Liste aller Klärfälle über einen Datumsbereich im Tab "Alle Kontoauszüge" gezogen werden.

### Automatische Zuordnung von Zahlungen zu Verbindlichkeiten in Xentral

Wenn eine Zahlung deines Unternehmens dein Bankkonto verlässt, erkennt Xentral diese automatisch und ordnet sie der richtigen Verbindlichkeit zu – sofern eine wichtige Bedingung erfüllt ist:

- **Bedingung **: Die Buchung auf dem Kontoauszug muss die ** Xentral-Verbindlichkeitsnummer **enthalten. Diese Nummer stammt aus dem ** fortlaufenden Nummernkreis für Verbindlichkeiten **in Xentral. ** Warum ist das wichtig?**

- Die Xentral-Verbindlichkeitsnummer ist ** eindeutig**.
- Im Gegensatz dazu kann die **Lieferantenrechnungsnummer ** mehrfach bei verschiedenen Lieferanten vorkommen – sie ist **nicht eindeutig**.

So funktioniert's bei Nutzung des Xentral-Zahlungsverkehrs:

- Wenn du den Zahlungsverkehr **über Xentral abwickelst** (z. B. via SEPA-XML), wird die Verbindlichkeitsnummer automatisch in der Zahlungsdatei mitgegeben.
- Dadurch wird beim späteren Zahlungsausgang auf dem Bankkonto ein **zuverlässiges Matching** zur zugehörigen Verbindlichkeit ermöglicht.

> **Tipp**
>
> Achte darauf, dass deine Bankbuchung (z. B. im Verwendungszweck) die Xentral-Verbindlichkeitsnummer enthält – insbesondere, wenn du außerhalb von Xentral überweist.

Es ist möglich, auch Verbindlichkeiten im Zahlungseingang zu verknüpfen. Dabei wird der Status der Verbindlichkeit auf "bezahlt" gesetzt. Sollte der Zahlungsimport rückgängig gemacht werden, wird der Status der Verbindlichkeit nicht zurückgesetzt. Dieser bleibt auf "bezahlt". Damit sollen mehrfache Auszahlungen verhindert werden.

> **Anmerkung**
>
> Im Autocomplete Feld werden alle Verbindlichkeiten angezeigt, die nicht direkt über den Zahlungseingang auf bezahlt gesetzt wurden. Manuell auf bezahlt gesetzte Verbindlichkeiten werden immer noch angezeigt.

#### Skonto auf Verbindlichkeiten

Wird ein Skonto auf der Verbindlichkeit automatisch im Zahlungseingang erkannt, analog zum Zahlungseingang auf eine Kundenrechnung mit Skonto.

> **Anmerkung**
>
> Wenn die Rechnungssumme abzüglich Skonto beglichen wurde, kannst du die Rechnung als bezahlt markieren, indem du in der Rechnung unter Details → Rechnung in der Oberfläche "Mahnwesen" einen Betrag als Skonto im Feld "Skonto gegeben" eintragen. Weitere Informationen dazu findest duhier.

### Eine Zahlung auf mehrere Belege/Verbindlichkeiten buchen

Zahlungen können auch auf mehrere Belege (egal ob Auftrag, Rechnung oder Gutschrift) gebucht werden:

- Aktion: "Auftragsguthaben" auswählen (analog für Rechnung oder Gutschrift)
- Feld: "Auftrag" → Hier werden die Auftragsnummern mit Komma getrennt eingegeben (keine Leerzeichen verwenden!)

Für Verbindlichkeiten ist die Vorgehensweise wie folgt:

1. Klicke bei der jeweiligen Buchung auf das **Stift**

-Symbol
1. Klicke im Popup-Fenster auf den Reiter **Verbindlichkeiten **

1. Wähle eine Verbindlichkeit mit dem **Pfeil **

-Symbol aus und klicke auf ** Speichern**

1. Der Betrag wird aufgeteilt und der Restbetrag kann erneut mit einer Verbindlichkeit verknüpft werden (siehe Schritt 1)

Ist die Summe des Zahlungsbetrags kleiner als der Wert beider Belege/ Verbindlichkeiten, wird auf die zuletzt gebuchte Belegnummer der vorhandene "Restbetrag" gebucht. Dieser Beleg wird nicht als bezahlt markiert, da zu wenig Geld verknüpft ist.

> **Anmerkung**
>
> Skonto wird beim Verknüpfen mehrerer Aufträge, Rechnungen oder Gutschriften nicht verarbeitet.

### Rücklastschriften auf eine Rechnung verbuchen

Rücklastschriften können erneut auf eine Rechnung verbucht werden. Die Rechnung wird dann wieder auf "offen" umgestellt und der Lastschriftbetrag wird inkl. der Gebühr angezeigt.

Die Rechnung wird ganz normal im Mahnwesen angezeigt. Sobald der Kunde überwiesen hat, kann die neue Zahlung wieder auf die Rechnung gebucht werden. Die Restsumme (Gebühr) kann entweder als Skonto gegeben werden oder der Kunde überweist diese nach.

Wenn eine Rücklastschrift mehreren Rechnungen zugeordnet werden soll, nutze den folgenden Workflow:

1. **Rechnungen auf offen setzen: ** Damit die Rechnungen in der Übersicht auftauchen, musst du den Zahlungsstatus auf offen setzen (** Buchhaltung > Rechnung > Details > Rechnung**).
1. **Rechnungen zuordnen: ** Navigiere zu ** Buchhaltung > Zahlungseingang > Import** und klicke auf das Pfeil-Symbol bei der Rücklastschrift, die du bearbeiten möchtest. Es erscheint eine Übersicht, in welcher du die einzelnen Rechnungen über das Pfeil-Symbol auswählen kannst. Wähle die erste Rechnung über das Pfeil-Symbol aus und trage den Wert bei SOLL ein. Nun entsteht eine Splitbuchung über den restlichen Betrag. Das Ganze muss für die anderen Rechnungen wiederholt werden.
1. Das Ergebnis findest du in der Übersicht unter **Buchhaltung > Zahlungseingang > Import **. ** Beispiel mit zwei Rechnungen:** Wenn es zwei Rechnungen gibt, die per Rücklastschrift eingebucht werden müssen, kann die Zuordnung folgendermaßen vorgenommen werden: Damit die Position aufgesplittet wird, ist über den Stift zu gehen und dort den "SOLL" Betrag auf einen Rechnungswert inkl. der Rücklastgebühr zu reduzieren.

Im Beispiel unten geht die Rechnung über 19,04 Euro und die Rücklast beträgt 33 Euro.

![ReceiptOfPayment3.png](https://help.xentral.com/hc/article_attachments/13026572238620)

Nach den Eintragungen wird gespeichert, dadurch wird die Buchung aufgesplittet und die Positionen können jeweils auf die Rechnung gebucht werden.

### Zahlungsein- und ausgänge splitten

Kontoauszugsbuchungen können auch gesplittet werden, wenn z.B. zwei Rechnungen in einer Summe bezahlt wurden oder eine Überzahlung stattgefunden hat.

Beispiel:

- Rechnungsbetrag: 8,12
- Gutschrift: 3,70
- Kunde bezahlt: 4,42 (RE-GS)

Im Zahlungseingang ist bei einer solchen Buchung auf das Editier-Icon zu klicken.

Danach kann nach der Belegnummer (RE) gesucht und über den Pfeil die Angaben des Belegs übernommen werden.

![ReceiptOfPayment4.png](https://help.xentral.com/hc/article_attachments/5033343994140)

Mit einem Klick auf die Schaltfläche Speichern, wird die Buchung abgeschlossen und erscheint als neue Zeile. Die ursprüngliche Zeile wird türkis markiert und besteht aus dem restlichen Betrag. Diese Zeile kann jetzt mit der Gutschrift verknüpft und auf "Buchungen fertigstellen" geklickt werden:

Analog können auch für Zahlungsausgänge bzw. Verbindlichkeiten gesplittet werden.

Das Stiftsymbol rechts neben einer Buchung ist auszuwählen und im Dialogfenster die fehlenden Daten einzutragen.

#### Teilzahlungen verknüpfen

Sollten Sie Teilbezahlungen auf eine Rechnung bekommen, können Sie wie oben beschrieben vorgehen und ebenfalls auf das Edit-Icon in der Zahlungszeile klicken. Nach dem Übernehmen der Rechnungsdaten, müssen Sie aber nochmal den Betrag händisch an die Teilsumme anpassen:

Beispiel: Gesamtbetrag: 185,05 Euro Teilzahlung: 100 Euro + 85,05 Euro

Die Restzahlung wird dann genauso verbucht, nur dass Xentral hier bereits die Differenz beim Zuweisen erkennt und diese so verbucht werden kann:

### Verknüpfen der Kosten

Ausgaben und Einnahmen, die nicht Kundenkonten (Aufträge, Rechnungen, Gutschriften) betreffen, können direkt auf Konten des hinterlegten Kontenrahmens gebucht werden.

### Erstellen von Verbindlichkeiten

Zudem ist es möglich, Verbindlichkeiten direkt aus Zahlungseingängen heraus zu erstellen und zu verknüpfen.

Im Dialogfenster kann die Verbindlichkeit angelegt werden. Stimmen der Betrag der Verbindlichkeit und der des Zahlungseingangs überein, wird der Status automatisch umgestellt.

### Übersicht über alle Kontoauszüge

Es erscheint ein neues Tab um alle Kontoauszüge über alle Geschäftskonten hinweg zu sehen. Natürlich werden hier immer noch die Projektzuordnungen des Mitarbeiters beachtet, damit man nicht zu viel sieht.

In dieser Oberfläche bestehen die gleichen Filter-Möglichkeiten, wie in den Buchungsübersichten der einzelnen Konten.

### Auflösen von Verknüpfungen

Verknüpfungen von Dokument und Kontoauszugsbuchung können wieder aufgelöst werden. Zu beachten ist, dass hierbei keine neue Buchung (für die Buchhaltung) erzeugt wird. Die ursprüngliche Buchung wird gelöscht und die neue Buchung erzeugt. Datum der Buchung ist weiterhin das Datum der Bankbuchung.

Buchhaltung → Zahlungseingang →![RoPgreenFence1.png](https://help.xentral.com/hc/article_attachments/13026566029724)

![RoPgreenFence1.png](https://help.xentral.com/hc/article_attachments/13026566029724)

- Verknüpfte Kontobuchungen erhalten den Status "abgeschlossen"
- Noch nicht verknüpfte Kontobuchungen den Status "prüfen"
- Als "Importfehler" verbuchte Kontobuchungen werden durchgestrichen dargestellt

Abgeschlossene Verknüpfungen können mit der Aktion![RoPredcross.png](https://help.xentral.com/hc/article_attachments/5033282608028)

wieder aufgelöst werden.

![RoPredcross.png](https://help.xentral.com/hc/article_attachments/5033282608028)

Diese Buchung wird geöffnet und ist bei den Kontoauszügen nun wieder erneut zu verbuchen.

### Markieren als Importfehler oder Abgeschlossen

Es ist möglich, mit einem Klick auf das Edit Icon noch zusätzliche Eigenschaften festzulegen.

- Importfehler → Markiert diese Buchung als Importfehler und verhindert somit, dass diese Buchung im FiBu Export erscheint.
- Abgeschlossen → Markiert diese Buchung als abgeschlossen und verhindert, dass diese Buchung wieder im Zahlungseingang aufgeführt wird.

#### Digitale Suche in Buchungen

Das Suchfeld ermöglicht eine Suche nach Inhalten in Kontoauszugsbuchungen. Z.B. die Umsatzsteuerabbuchungen des Finanzamtes im letzten Jahr für das Steuerbüro. Hier kann blitzschnell nach Namen, Behörden oder anderen Texten gesucht werden. Das Suchergebnis kann als Liste per Knopfdruck exportiert werden.

### Manuelle Bearbeitung der Verknüpfungen (Expertenmodus)

Buchhaltung → Zahlungseingang →![RoPgreenFence1.png](https://help.xentral.com/hc/article_attachments/13026566029724)

. Die Verknüpfung eines Zahlungsbetrags mit einer Bestellung oder einer Rechnung kann auch manuell bearbeitet oder geändert werden (z. B. Änderung der Aufteilung eines Betrags auf mehrere Rechnungen). Die Verknüpfung eines Kontoauszugs mit einer oder mehreren Rechnungen ist direkt in den Kontoauszügen ersichtlich. Öffnen Sie dazu die Zahlung vorne mit dem blauen Pfeil.

![RoPgreenFence1.png](https://help.xentral.com/hc/article_attachments/13026566029724)

Um diese Buchungen zu ändern ist auf die Auftragsnummer zu klicken. Dann gelangst du in den Auftrag, im Reiter Positionen findest du die Zahlungen und öffnest diese mit einem Klick auf **zur Buchung**.

![ReceiptOfPayment5.png](https://help.xentral.com/hc/article_attachments/13026566204700)

Nun erscheint die Ansicht einer einzelnen Bankbuchung. Im unteren Bereich ist die Verknüpfung zu einer oder mehreren Rechnungen zu sehen, die bearbeitet werden können.

Es kann auf die einzelne Buchung geklickt und der Betrag bearbeitet werden, indem ein neuer Betrag eingegeben (z.B 10 EUR werden mit Trennzeichen "Punkt" eingegeben: 10.00) und auf "ok" geklickt wird.

In diesem Expertenmodus ist zu berücksichtigen, dass die geänderten Beträge zusammenaddiert die Summe der Kontobuchung ergeben.

Die Buchung für eine einzelne Rechnung ist im Protokoll des Dokumentes zu sehen.

## Summen und Salden

Das Tab Summen und Salden zeigt eine Übersicht über die Haben, Soll und Saldo der einzelnen Konten innerhalb eines bestimmten Zeitraums. Der Zeitraum kann über den Filter mit "Datum von:" und "Datum bis:" definiert werden.

Die Haben-Beträge errechnen sich aus allen positiven Werten der Kontoauszüge und die Soll Beträge aus den Ausgaben. Das Saldo ist jeweils die Differenz von Haben und Soll. Das Startsaldo bezieht sich immer auf das Saldo am Tag zum Start des ausgewählten Zeitraums. Zusätzlich werden jeweils die Kontonummer & Bezeichnung sowie die Anzahl an Buchungen angezeigt. In der untersten Zeile finden sich die Gesamtsummen aller Konto für den ausgewählten Zeitraum.

## Löschen eines Kontoimports

Ein Datenimport einer Kontoauszugsdatei kann auch wieder rückgängig gemacht werden. Es kann immer nur der letzte Import rückgängig gemacht werden. Dabei werden Verknüpfungen wieder gelöst - mit Ausnahme von Verbindlichkeiten.

## Kontenblatt

Im Bereich "Kontenblatt" können Kontoauszüge nach den Konten aus dem Kontenrahmen gefiltert durchsucht werden.

Im Kontenblatt werden:

1.) die Konten aus dem Modul Kontenrahmen (Administration → Einstellungen → Buchhaltung → Kontenrahmen) durchsucht

2.) die Gegenkonten aus den Kontoauszügen herausgesucht und dort geprüft, ob das Gegenkonto einer Kunden- oder Lieferantennummer entspricht

3.) die Geschäftskonten durchsucht, die DATEV-Konten sind (also wenn im Geschäftskonto das Feld "DATEV" anders gefüllt ist als mit 0)

## Einfache manuelle Erfassung des Zahlungseingangs (Beta)

Zusätzlich bietet dir Xentral die Möglichkeit, Zahlungseingänge manuell zu erfassen. Diese Option kannst du nutzen, wenn dir Konten vorliegen, die keinen Online-Zugriff haben und auch keinen erhalten werden.

Um die richtige Erfassung sicherzustellen, gib bei "Konto" das gewünschte Bankkonto an. Dieses ist zwar nur ein Bilanzkonto, das ist hier aber irrelevant. Das Konto ist Teil des Sachkontenrahmens und beide Konten sind im Kontenrahmen enthalten.

Du entscheidest dann, ob

- auf Debitor/ Kreditor/ Sachkonto oder
- Bilanz oder GuV gebucht wird.

> **Anmerkung**
>
> "Gegenkonto" ist kein Pflichtfeld! Wenn du ohne Gegenkonto buchst, erfolgt das Mapping im Zahlungseingang.

> **Anmerkung**
>
> Diese Option befindet sich noch in der Beta-Phase.

## Verbuchung von Gebühren über regelmäßige Verbindlichkeiten

Für Gebühren o.ä. gibt es auch einen Workaround, um diese fest dem korrekten Konto zuzuordnen und eine automatische Buchung zu initiieren.

Dazu legst du eine[regelmäßige Verbindlichkeit](#)an (Administration → Einstellungen → Buchhaltung → Verbindlichkeiten → Regelmäßige Verbindlichkeiten → *+ Neuen Eintrag anlegen*).

Wichtig ist es, dass du als Art "Kontenrahmen" auswählst. Bei konstanten Beträgen für Haben und Soll kannst du hier auch einen Wert eingeben.

## Warum werden manche Verbindlichkeiten beim Kontoabgleich nicht automatisch erkannt, obwohl alles korrekt scheint?

Xentral ordnet Zahlungen beim Einlesen des Kontoauszugs nicht über die Rechnungsnummer, sondern über die **eindeutige Verbindlichkeitsnummer** zu. Diese Nummer wird beim Anlegen der Verbindlichkeit in Xentral vergeben (z. B. 100123) und ist notwendig für eine automatische Zuordnung. Wird eine Zahlung manuell oder außerhalb von Xentral durchgeführt und enthält der Verwendungszweck diese Verbindlichkeitsnummer nicht, kann Xentral die Zahlung nicht eindeutig einer Verbindlichkeit zuordnen – auch dann nicht, wenn Betrag, Rechnungsnummer und Status korrekt sind.

Wenn der Zahlungsverkehr direkt über Xentral ausgeführt wird, wird die Verbindlichkeitsnummer automatisch in der Zahlungsdatei (z. B. SEPA-XML) mitgegeben, sodass die Zuordnung beim Bankabgleich zuverlässig funktioniert. Bei manuellen Überweisungen sollte die Verbindlichkeitsnummer immer im Verwendungszweck angegeben werden.