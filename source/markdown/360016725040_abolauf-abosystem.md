Das in Xentral integrierte Abo-System ermöglicht es regelmäßige Leistungen automatisiert bei Kunden abzurechnen. Das Abosystem senkt den Aufwand der regelmäßigen Abrechnung für Serviceverträge, Vermietungen, Dienstleistungsverhältnisse, Abonnements und ähnliches auf ein Minimum. Dieses Modul ist somit für alle relevant, die regelmäßige Leistungen beim Kunden abrechnen.

## Neues Abo anlegen

Abos werden direkt in der Adresse im Tab **Abos** neu angelegt. Hier können Artikel eingefügt werden, die der Kunde gebucht hat. Zusätzlich zu wiederkehrenden Gebühren können auch einmalige Artikel (z.B. Waren) mit abgerechnet werden.

Klicke auf **+Neue Position einfügen**, um einen neuen Artikel zum Abo hinzuzufügen. Sobald ein neuer Artikel eingefügt wurde, erscheint dieser in der Übersicht.

### Einstellungen für die Abrechnung

In der Ansicht **Allgemein** kannst du folgende Eingaben machen:

- Artikel→ Zeigt den Artikel, der vom Kunden abonniert wird. Dieser kann über das Lupensymbol gesucht werden
- Bezeichnung → Bezeichnung des Aboartikels im Beleg (kann bei Bedarf verändert werden)
- Beschreibung → Beschreibung des Aboartikels im Beleg (kann bei Bedarf verändert werden)
- Menge → Menge des abonnierten Artikels
- Preis (netto) → Nettopreis pro Stück. Rechts daneben kann ausgewählt werden, ob das Abo monatlich, monatlich für x Monate, jährlich, wöchentlich, 30-tägig oder einmalig ist
- Automatisch anlegen als → Auswahl zwischen Auftrag oder Rechnung. Zudem kann hier eine Gruppe und eine Reihenfolge angegeben werden, wobei die zwei letztgenannten Punkte optional sind
- Erstes Startdatum → Datum, an dem der Abolauf startet. Sobald die ersten Aboläufe gestartet sind, darf das Feld nicht mehr verändert werden
- Zahlzyklus → Angabe des Rhythmus zu dem der Abolauf ausgeführt werden soll
- Enddatum → Das Enddatum bestimmt nur das Ende des Zyklus. Es wird nicht taggenau abgerechnet, sondern nur geprüft ob das Enddatum erreicht ist oder nicht. Ist es nicht erreicht wird der Zyklus vollständig abgerechnet, erst nach Ablauf des Enddatums verschwindet der Artikel im Abo. Soll vor dem Zyklus beendet werden, müsste die Differenz manuell nach dem Erstellen der Rechnung abgezogen bzw. eine Gutschrift angelegt werden
- Expertenmodus → Auswahl des Expertenmodus. Wird dieser ausgewählt, können zusätzliche Einstellungen wie das Datum bis welches bereits abgerechnet wurde eingestellt und eine interne Bemerkung hinzugefügt werden

## Abo-Gruppen verwenden

Mit Abo-Gruppen können Artikel in den Aborechnungen zu sogenannten Abo-Gruppen zusammengefasst werden. Diese erscheinen dann gruppiert auf der Rechnung. Es können auch einzelne Rechnungen pro Abo-Gruppe erstellt werden.

> **Anmerkung**
>
> Damit Abo-Gruppen ausgewertet werden, muss unter Buchhaltung → Abolauf → Einstellungen ein Haken bei "Abo-Gruppen verwenden" gesetzt sein.

### Abo-Gruppe erstellen

Damit eine Abo-Gruppe zugeordnet werden kann, muss diese zuvor unter "Gruppen" angelegt werden. Hier kann auch die Einstellung getätigt werden, ob eine gemeinsame Rechnung, eine eigene Rechnung oder eine Sammelrechnung erstellt werden soll. Diese Abo-Gruppen werden global erstellt und sind für alle Adressen gültig.

Über "+Neuen Eintrag anlegen" kann eine neue Abo-Gruppe erstellt werden.

Trage dafür folgendes ein:

- Bezeichnung → Name der Gruppe (dies erscheint auf der Rechnung)
- Beschreibung → Beschreibung der Gruppe (dies erscheint auf der Rechnung)
- Rabatt → optional kann hier ein Rabatt in % angegeben werden
- Rechnung → Auswahl wie die Gruppe in die Rechnung kommen soll:
  - Gemeinsame Rechnung → Die Gruppen werden untereinander in einer gemeinsamen Rechnung gelistet
  - Eigene Rechnung → Für jede Gruppe wird eine eigene Rechnung erstellt
  - Sammelrechnung → Mehrere Gruppen können zu einer Sammelrechnung zusammengefasst werden. Nach der Auswahl im Dropdown erscheint ein Suchfeld für eine Sammelrechnung, die unter Adresse → Abo → Sammelrechnung angelegt wurde
- Abweichender Ansprechpartner → Wird für das Ansprechpartner-Feld in der Rechnung übernommen
- Ziel-Projekt → Die erstellte Rechnung läuft auf dieses Projekt
- Reihenfolge → Wenn mehrere Gruppen in einer Rechnung vorkommen, kann die Reihenfolge der Gruppen damit angepasst werden (ab Version 18.3)
- Gruppensumme → Nach jeder Auflistung der Artikel einer Gruppe, wird eine Gruppensumme auf dem Beleg ausgegeben

Eine zweite Möglichkeit eine Abo-Gruppe zu erstellen besteht darin, diese direkt unter Adresse → Abo → Gruppe anzulegen. Hierbei ist zu beachten, dass diese Abo-Gruppe nur für diese Adresse gültig ist und bei anderen Adressen nicht ausgewählt werden kann.

### Übersicht

Unter dem Reiter "Gruppen" befindet sich eine Auflistung aller angelegten Abo-Gruppen. Unter Adresse → Abo → Gruppen befindet sich eine Übersicht aller Gruppen, die für diese Adresse in Verwendung sind.

### Abo-Gruppen einem Abo-Artikel zuweisen

Nach dem Erstellen einer Abo-Gruppe kann unter Adresse → Abo → Artikel die Gruppe im Artikel angegeben werden.

![rechnungslauf_3475.png](https://help.xentral.com/hc/article_attachments/5077618160540)

### Abo-Gruppen in Belegen

Unter Buchhaltung → Abolauf können die Belege für den Abolauf erstellt werden. Hier werden die Gruppen hinten in Klammern angezeigt:

![rechnungslauf_3476.png](https://help.xentral.com/hc/article_attachments/5077571762588)

Auf der erstellten Rechnung wird die Gruppe dann so dargestellt:

![rechnungslauf_3477.png](https://help.xentral.com/hc/article_attachments/5077618268956)

## Abo Sammelrechnungen

Der zusätzliche Reiter unter Adresse → Abo → Sammelrechnung dient dazu, einzelne Abo-Gruppen zu einer Sammelrechnung zusammenzuführen.

### Übersicht

In der Übersicht werden alle angelegten Sammelrechnungen angezeigt.

### Sammelrechnung hinzufügen

Mit der Schaltfläche 'Neuen Eintrag anlegen' kann eine neue Sammelrechnung für die Abo-Gruppen erstellt werden.

Befülle folgende Felder:

- Bezeichnung → Name der Sammelrechnung, wird nur gebraucht zur Auswahl in den Abo-Gruppen
- Rabatt → optional kann hier ein Rabatt in % angegeben werden
- Abweichende Rechnungsadresse → Wird als Rechnungsadresse in der erstellen Abo Rechnung genommen
- Ziel-Projekt → Optional, bestimmt das Rechnungs-Projekt der Sammelrechnung

### Auswahl der Sammelrechnung in den Abo-Gruppen

Sobald unter Adresse → Abo → Gruppen: Rechnung Dropdown "Sammelrechnung" ausgewählt wurde, erscheint ein zusätzliches Feld, um die Sammelrechnung auszuwählen.

## Abrechnung über das Abosystem

### Übersicht der fälligen Beträge

Über den Abolauf können Rechnungen oder Aufträge automatisch erstellt werden. Die "Übersicht" zeigt die abzurechnenden Kunden und Artikel mit den Abrechnungszeiträumen an.

### Gebuchte Abos

Der Reiter "gebuchte Abos" bietet eine allgemeine Übersicht über alle aktuellen Abos.

Hier kann durchsucht werden nach:

- Kunde
- Kundennummer
- Bezeichnung
- Nummer
- Abgerechnet bis
- Enddatum
- Preis
- Menge
- Art
- Zahlperiode
- Dokument

Über den Filter kann zudem nach abgeschlossenen Projekten sowie nach einem Zeitraum gefiltert werden.

### Vorschau der Rechnungspositionen

Die Vorschau der Positionen, die für den Kunden berechnet werden, wird über "Details" in der letzten Spalte aufgerufen. Diese Übersicht zeigt die Zeiträume und die Positionen, die für den Kunden eingetragen wurden und aktuell berechnet werden sollen.

Wird auf Details geklickt, öffnet sich ein neues Browserfenster mit der Vorschau der Rechnungspositionen.

![rechnungslauf_3484.png](https://help.xentral.com/hc/article_attachments/5077618321308)

### Abrechnung starten

Die abzurechnenden Kunden können in der ersten Spalte gesammelt an- oder abgewählt werden. Nur für angewählte Kunden wird eine Abrechnung erstellt.

#### Abrechnungsart auswählen

Über das Dropdown-Menü (über "Abrechnung starten") kann die Abrechnungsart ausgewählt werden.

Folgende Abrechnungsarten stehen zur Verfügung:

- Rechnungen generieren - kein Versand der Rechnung → Die Rechnung wird generiert, der Status der Rechnung ist "freigegeben". Die Rechnung muss noch manuell über das System versendet werden.
- Rechnungen generieren - Rechnung per Mail versenden (wenn E-Mail vorhanden) → Die Rechnung wird generiert, der Status der Rechnung ist "versendet". Eine E-Mail wird versendet, sofern der Kunde eine E-Mail Adresse hinterlegt hat.
- Rechnungen generieren - Alle Rechnungen drucken (auch wenn E-Mail vorhanden) → Die Rechnung wird generiert, der Status der Rechnung ist "versendet". Die Rechnung wird an dem Drucker ausgedruckt, der ausgewählt wurde.
- Rechnung generieren - Rechnung drucken oder Mail Versand (wenn E-Mail vorhanden) → Die Rechnung wird generiert, der Status der Rechnung ist versendet. Die Rechnung wird gedruckt oder per Mail versendet.
- Rechnung generieren - Rechnungen drucken und Mail Versand (wenn E-Mail vorhanden) → Die Rechnung wird generiert, der Status der Rechnung ist "versendet". Die Rechnung wird per E-Mail versendet, sofern bei den Kundendaten eine E-Mail Adresse hinterlegt ist. Ansonsten wird die Rechnung an dem Drucker ausgedruckt, der ausgewählt wurde.

Die Abrechnungsart ist analog zu betrachten für den Reiter "Aufträge".

#### Drucker auswählen

Bei Abrechnungsarten, die eine Druckeranbindung benötigen, muss mindestens ein Drucker an Xentral angebunden sein. Sind mehrere Drucker angebunden, kann der gewünschte Drucker für den Abrechnungslauf aus dem Dropdown-Menü (links neben "Abrechnung starten") ausgewählt werden.

### Abrechnung via Prozessstarter

Die Abrechnung muss nicht zwingend manuell stattfinden, sondern kann auch via Prozessstarter automatisch laufen. Der entsprechende Prozessstarter heißt "rechnungslauf" und muss dafür aktiviert werden.

![subscription1.png](https://help.xentral.com/hc/article_attachments/5077630258332)

Darüber hinaus gibt es den Prozessstarter "Abolauf Manuell", der im Standard bereits aktiviert ist. Dieser Prozessstarter arbeitet die ausgelösten Rechnungsläufe schrittweise ab, so ähnlich wie der Prozessstarter "Autoversand manuell". Im Standardprozess landen die Aboläufe zunächst in der Warteschlange und werden nach und nach von diesem Prozessstarter abgewickelt. Ist die Anzahl der Aboläufe gering, kann dieser Prozessstarter auch deaktiviert werden, um den Prozess zu beschleunigen.

### Rückwirkende Abrechnung

#### Abrechnung wurde im letzten Monat vergessen

Falls die Abrechnung im letzten Monat vergessen wurde, die Artikel aber nicht für zwei Abrechnungszeiträume summiert auf der Rechnung stehen dürfen, gibt es hier die Möglichkeit, den vergessenen Monat nochmals abzurechnen.

1. Öffne Abolauf → Einstellungen

2. Setze einen Haken bei "Vergangenes Datum für Abrechnungserstellung"

3. Datum auswählen (= Datum, an dem die Abrechnung erledigt werden sollte z.B. ein paar Tage zurück am Ende des letzten Monats)

4. Sperchern

5. Klicke auf Übersicht und wähle den Reiter "Rechnungen" oder "Aufträge" (je nach dem, welches Dokument erstellt werden soll)

6. Wähle die gewünschten Kunden und drücke "Abrechnung starten"

7. Bei Einstellungen den Haken wieder entfernen, das Datum löschen und speichern

> **Wichtig**
>
> Die Einstellungen unbedingt wieder komplett zurücksetzen und speichern!

Abrechnung mit Leistungsdatum erstellen - Abos im Leistungszeitraum anstelle vor dem Leistungszeitraum abrechnen → berechnet einen Monat später; Rechnung bzw. Auftrag wird in dem Intervall bzw. Monat erstellt in dem das Abo gebucht ist (z.B. Abrechnung im Juni für Leistungszeitraum Mai). Somit muss das Datum für die Abrechnung nicht mehr jeden Monat manuell gesetzt werden. Der Abolauf wird somit im Standard um einen Monat/Intervall verschoben.

> **Anmerkung**
>
> Sollte der Abrechnungszeitraum vergessen worden sein oder doch manuell einmal geändert werden, kann mit den Datumseinstellungen der Zeitraum auch trotzdem weiterhin speziell temporär verschoben werden.

#### Einstellung der Zahlungsweise für den Kunden

Die Zahlungsweise für den Kunden wird in der Adresse eingestellt. Stammdaten → Adressen → Details → Zahlungskonditionen.

### Rabatte im Abolauf

#### Abrechnen mit EUR Rabatten

In die Abrechnung können sowohl einmalige als auch wiederkehrende Rabatte eingefügt werden.

- Artikel mit negativem Verkaufspreis anlegen
- Artikel dem Abo eines Kunden hinzufügen
- Abrechnung: "Einmalig" bzw. Monatspreis, wenn eine mehrmalige Abrechnung gewünscht wird
- Es ist zu beachten, dass bei Aboabrechnungen nicht mit prozentualen Preisnachlässen, sondern fixen Beträgen zu arbeiten ist

Der Betrag wird in der Abrechnung, für die dieser voreingestellt ist mit abgezogen:

![rechnungslauf_3491.png](https://help.xentral.com/hc/article_attachments/5077609845404)

#### Rabatte in Prozent hinzufügen

Es ist möglich Rabatte auch in Prozent hinzuzufügen.

Über das Edit-Icon unter Adresse → Abo können die Abo-Artikel überarbeitet werden. Hier kann für diese Abo-Position ein Rabatt hinzugefügt werden.

Dieser Rabatt wird auch in der Spalte angezeigt:

![rechnungslauf_3492.png](https://help.xentral.com/hc/article_attachments/5077630333084)

### Abos mit zukünftigem Startzeitpunkt

Sollen Abos angelegt werden, bevor diese starten und daher für die Abrechnung zu berücksichtigen sind, z.B. weil gerade auf Xentral umgestiegen wird oder die Abos bereits eingetragen sind, ist in der entsprechenden Adresse zu dem Abo zu navigieren und auf das Stift-Icon zum Bearbeiten zu klicken.

In diesem Spezialfall ist der Haken für den Expertenmodus zu aktivieren. Anschließend ist als Datum "Abgerechnet bis" der letzte Tag des Monats, der in der Abrechnung nicht mehr berücksichtigt werden soll, auszuwählen.

## Automatische Abos verwenden

- Automatische Abos werden anhand der gefundenen Artikel in einem Auftrag automatisch erstellt
- Preis, Rabatt und Menge werden aus dem Auftrag verwendet
- Wenn ein Projekt ausgewählt wird, wird nur dann ein automatisches Abo aus einem Auftrag erzeugt, wenn der Auftrag und das Abo das selbe Projekt haben
- Als Preisart stehen Monats- oder Jahrespreis zur Verfügung
- Es kann ausgewählt werden, ob eine Rechnung oder ein Auftrag beim Abolauf angelegt wird
- Auswählbar ist auch die Abo Gruppe, die dann dem automatischen Abo zugeordnet wird
- Die Position gibt an, an welcher Stelle im erzeugten Beleg der Abo-Artikel stehen soll
- Beim ersten Startdatum stehen drei Optionen zur Verfügung: das Auftragsdatum, der nächstmögliche 15. oder der 1. des nächsten Monats
- Es gibt die Möglichkeit in dem Auftrag, in dem der automatische Abo Artikel gefunden wurde, den Autoversand zu blockieren.
- Wenn die automatische E-Mail Bestätigung aktiv ist, kann mit der voreingestellten Geschäftsbriefvorlage eine Mail versendet werden. In dieser Geschäftsbriefvorlage steht eine weitere Variable {ABOARTIKEL} zur Verfügung in der alle Artikel samt Nummer aufgeführt werden, die in auslösenden Aufträgen für ein automatisches Abo in Frage kommen
- An diese Mail kann ein PDF des Belegs angehängt werden