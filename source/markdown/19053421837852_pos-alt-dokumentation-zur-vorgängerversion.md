## Achtung

Das folgende alte Xentral Modul POS wird in Q2 durch das Redesign und weitere Funktionen ersetzt. (Stand: 17.03.2025). Du kannst die neue POS bereits im Beta Programm testen.

## Aktionen mit der Kasse

![POS1.png](https://help.xentral.com/hc/article_attachments/19055658908060)

Die Kasse ermöglicht folgende Aktionen:

- Zahlung Bar
- Zahlung EC
- Zahlung Kreditkarte
- Zahlung Überweisung
- Kein Beleg oder mit Rechnung bzw. Quittung
- Rabatt in EUR oder Prozent
- Trinkgeld
- Entnahme
- Einlage
- Storno Funktion
- Belege laden
- Lade öffnen
- Vorgang speichern

## Einrichtung POS

### Projekt anlegen

Legen Sie unter Stammdaten → Projekte ein eigenes Projekt für die Kasse an.

### Kassenbuch definieren

Für eine Kasse muss ein Kassenbuch hinterlegt werden, in welches die Umsätze der Kasse gebucht werden. Kassenbücher werden unter Administration → Einstellungen → Geschäftskonten angelegt. Dazu muss ein neues Geschäftskonto erstellt, und der Typ auf "Kasse" eingestellt werden.

Das so erstellte Kassenbuch wird dann unter Buchhaltung → Kassenbuch gelistet.

### Kundennummer für Laufkundschaft festlegen

Legen Sie in Stammdaten → Adressen eine Adresse an, die stellvertretend für alle anonyme Kunden verwendet wird. Ein geeigneter Name könnte z.B. "Laufkundschaft" o. ä. lauten. Diese Adresse wird später bei den Projekteinstellungen hinterlegt (siehe Screenshot bei POS Einstellungen).

### Kassierer anlegen

Die Bedienung der Kassenoberfläche kann nur durch ausgewiesene Kassierer erfolgen. Die Erstellung eines Kassierers im System, setzt voraus, dass dieser Kassierer bereits als Mitarbeiter in Stammdaten → Adressen vorhanden ist. Wichtig hierbei ist, dass der Mitarbeiter explizit die Rolle "Mitarbeiter des entsprechenden POS - Projektes ist", es reicht nicht wenn der Mitarbeiter nur die Rolle "Mitarbeiter von Projekt alle" besitzt.

Ist der Datensatz für den Mitarbeiter vorhanden, kann er unter App Center → POS (Konfiguration) → Übersicht als Kassierer hinzugefügt werden.

Legen Sie mit 'Neu' einen neuen Kassierer an.

![POS3.png](https://help.xentral.com/hc/article_attachments/19055687802524)

#### Rechtevergabe für Kassierer

Vergeben Sie mindestens folgende Rechte für Kassierer:

- POS
- WELCOME: login, logout, settings, start, startseite

Bitte überprüfen Sie direkt die fehlenden Rechte im Systemlog. Führen Sie den Workflow komplett durch und prüfen Sie im Systemlog. Vergeben Sie alle fehlenden Rechte.

### Artikel für Rabatt einrichten

Um an der Kasse einfach und schnell Rabatte an Kunden zu vergeben oder mit Gutscheinen zu arbeiten, legen Sie einen sog. Rabattartikel an, den Sie im weiteren Verlauf auch bei den Projekteinstellungen hinterlegen.

Da es sich hierbei nicht um einen prozentualen Rabatt handelt, ist der Artikel auch nicht als Rabattartikel durch ein Häkchen auszuzeichnen (siehe Screenshot). Vielmehr wird der Rabattabzug über einen negativen Verkaufspreis realisiert, der jedoch auch im Verkaufsprozess flexibel verändert werden kann.

Zusätzlich zu diesem "Standard-Rabatt-Artikel" können Sie auch beliebig viele weitere Rabattartikel dieser Art anlegen, um bspw. saisonale Gutscheine auszustellen und auf diesem Wege getätigte Umsätze anschließend auch auswerten zu können.

### POS Einstellungen

Sie müssen für die POS kein bestimmtes Kommissionierverfahren definieren. Alle Einstellungen nehmen Sie im Projekt unter Administration → Einstellungen → Verkauf → POS Einstellungen vor:

- Lagerprozess: Definiert, ob bei einem Verkauf eine Lagerbuchung stattfindet, und wenn ja, aus welchem Lager Ware für den Verkauf entnommen werden kann
- POS Lager für den Verkauf: Definiert das Lager für die POS, sofern bei Lagerprozess "Aus eingestelltem POS Lager entnehmen" ausgewählt wurde (Zusätzlich ist unter Lager & Logistik → Lagerverwaltung → Regale die Option "POS Lager" für jedes Regal zu aktivieren)
- Preisgruppe bevorzugt: es werden nur die Artikel-Verkaufspreise gezogen, die der hinterlegten Preisgruppe zugeordnet werden
- Kasse für Bar: Angabe des Kassenbuchs
- Laufkundschaft: Die für Laufkundschaft angelegte Adresse (siehe oben)
- Kunden aus fremden Nummernkreisen abwickeln: Die Kundenauswahl beim Verkauf ist damit auch aus anderen Projekten möglich
- Nur Artikel aus Projekt erlauben: Nur Artikel werden in POS angezeigt, die das selbe Projekt wie die POS besitzen.
- Lieferschein erstellen: Es wird zusätzlich ein Lieferschein erzeugt (Wichtig bei Nutzung von MHD und Chargen!)
- Kasse Beschriftung 1: Das Feld "Interne Bemerkung" kann hier in den Belegen umgenannt werden
- Kasse Beschriftung 2: Das Feld "Freitext" kann hier in den Belegen umbenannt werden
- Artikelbeschreibung in Belege übernehmen
- POS Anzeige in netto: Alle Preisangaben erfolgen in Netto
- Mehrere Aufträge pro Kassierer: Erfassung mehrerer Aufträge pro Kassierer möglich durch "Vorgänge Speichern" & "Laden"
- Automatisches Ausloggen: Hier können Vorgaben für einen automatischen Logout vorgenommen werden. Der Zeitraum für den Logout kann dabei sowohl je Abschluss eines Kassiervorgangs als auch allgemein festgelegt werden.

### Schaltflächen

Folgende Schaltflächen können in den POS Einstellungen für die Kasse aktiviert werden:

- Zahlweise Bar
- Wahlweise EC
- Zahlweise Kreditkarte
- Zahlweise Überweisung
- Beleg Rechnung
- Beleg Quittung
- Rabatt in %
- Rabatt in EUR
- Einlage
- Entnahme
- Trinkgeld
- Lade öffnen
- Belege laden
- Storno

Durch Betätigung der Rabatt-Schaltflächen können Sie einen Rabatt (in Euro oder Prozent) selektieren und unmittelbar auf alle Produkte im Warenkorb anwenden. Bei Auswahl des EUR Rabatts wird dabei die Artikelbezeichnung auf Ihrer Rechnung ausgewiesen, die Sie zuvor im Rabattartikel hinterlegt und in die Projekteinstellungen übertragen haben.

Außerdem kann die Annahme des Trinkgelds auf die Zahlweisen EC und Kreditkarte beschränkt werden. Dadurch steht der Schaltflächen bei anderen Zahlweisen nicht zur Verfügung (ausgegraut). Hintergrund hierfür ist, dass die Trinkgeldverwaltung nicht durch die Mitarbeiter selbst erlaubt sein soll, sondern diese nur über den Steuerberater möglich sein soll.

Beim Verkauf über die POS wird die Schaltfläche "Zahlung abbuchen" eingeblendet, wenn im POS-Projekt ein ZVT eingestellt ist.

### Weitere Einstellungen

Nehmen Sie hier die für Sie zutreffenden Konfigurationen vor:

- Zwangsauswahl Zahlweise
- Zwangsauswahl Zahlweise
- Vorauswahl Anrede

### Drucker Einstellungen

Konfigurieren Sie hier welche Dokumente bei einer Transaktion an der Kasse, wie oft, und auf welchem Drucker ausgegeben werden:

- Belege ausgeben nach Abschluss
- Drucker
- Anzahl Lieferschein
- Anzahl Rechnung
- Anzahl Lieferschein Doppel

## Einrichtung der dazugehörigen Hardware

Die einzelnen Hardwarekomponenten sollten, wie in folgender Grafik beschrieben, aufgebaut werden:

![POS4.png](https://help.xentral.com/hc/article_attachments/19055658911644)

Im Anschluss müssen Sie den POS noch in xentral einrichten, um die Kasse, wie in folgendem Video verwenden zu können:

### Bondrucker einrichten

Um zusätzlich zu den Rechnungsbelegen Bons zu drucken, können Sie einen Bondrucker einrichten.

> **Anmerkung**
>
> Ein Bondruck ist nur mit per Adapterbox angebundenem Hardware, also dem Bondrucker, möglich und nicht als Download verfügbar.

Zunächst müssen Sie die hierfür die Verbindung zur Adapterbox einrichten. Öffnen Sie in der Ansicht Administration → Einstellungen → System den Punkt Adapterbox.

> **Anmerkung**
>
> Wir empfehlen den Betrieb über ein Netzwerkkabel, da es so am besten und stabilsten läuft. Betrieb über WLAN ist prinzipiell möglich, wird aber von uns nicht supported, da dies eher fehleranfällig ist und die möglichen Probleme vor allem in Ihren Netzwerkeinstellungen zu finden sind.

Wählen Sie in der Adapterbox-Ansicht "+NEU". Danach werden Sie von xentral in 3 Schritten durch die Einrichtung geführt.

Zunächst können Sie, falls nötig, die Netzwerkeinstellungen manuell festlegen. Sollten Sie hier Änderungen vornehmen, speichern Sie diese mit der 'Speichern'-Schaltfläche. Um zum nächsten Schritt zu gelangen, klicken Sie auf 'weiter mit Schritt 2'.

Für diesen Schritt erhalten Sie von xentral eine Liste von durchzuführenden Aktionen. Arbeiten Sie diese Liste in der vorgegebenen Reihenfolge sorgfältig ab. Sie benötigen jetzt den FAT-formatierten USB-Stick.

Wenn Sie die Liste abgearbeitet haben, drücken Sie weiter mit Schritt 3 und geben Sie eine Drucker-Bezeichnung und die Seriennummer der Adapterbox an.

Im letzten Schritt kann die Einrichtung durch einen Testdruck überprüft werden. Nach erfolgreichem Testdruck können Sie den Bondrucker in den POS-Einstellungen anwählen und dem Projekt hinterlegen.

> **Wichtig**
>
> In der POS müssen Sie die Option "Beleg Quittung" auswählen, damit auch ein Bon bei Rechnungsdruck mitkommt.

![POS5.png](https://help.xentral.com/hc/article_attachments/19055658911900)

#### Freifeld auf Bon

Es gibt die Möglichkeit, pro Artikel-Position auf dem Bon einen Freifeldtext des Artikels auszugeben.

![POS6.png](https://help.xentral.com/hc/article_attachments/19055687803804)

Pro Zeile können 39 Zeichen dargestellt werden. Mit einem | im Freifeld-Text können Sie bei diesem Positionstext einen Umbruch erzeugen.

> **Anmerkung**
>
> Der Freifeld-Name erscheint auf dem Beleg auch, aber nur wenn er in den Freifeld-Einstellungen nicht leer ist.

### ZVT - Anbindung EC Terminal

Es ist möglich, ZVT-kompatible EC-Geräte anzubinden, indem man die IP-Adresse und den Port des Geräts dazu eingibt. Dadurch wird bei der Auswahl der Zahlungsweise "EC" der Betrag auf das Gerät übertragen.

Über die Schaltfläche "Zahlung abbuchen" im Verkaufendialog kann ein Trinkgeld bei Verkauf mit EC-Karte gebucht werden (siehe Schaltflächen).

> **Anmerkung**
>
> Es erfolgt nur eine Rückmeldung zum Kartenlese-Gerät, nicht wieder zurück nach xentral.

Felder:

- IP-Adresse: Die IP-Adresse des EC-Kartenlesers
- Port: Der Port an dem der EC-Kartenleser angeschlossen ist

> **Anmerkung**
>
> Diese Einstellungen finden Sie meist auf dem Gerät.

Bei ZVT muss man die IP-Adresse und den Port des EC-Kartenleser in xentral angeben. Hinweis: Meist ist es so das das EC-Kartenlesegerät im lokalen Netzwerk eingebunden ist und “nur” eine lokale IP Adresse hat. Betreibt man aber xentral in der Cloud oder auf einem externen Server kann xentral natürlich nicht auf die lokale IP Adresse des EC-Kartenlesers zugreifen. In diesem Fall muss man über den Router die lokale IP Adresse bzw. den Port nach außen verfügbar machen. Bitte wenden Sie sich an Ihre Administration - das kann nur diese für Sie machen. xentral hat keine Möglichkeit interne IP Adresse nach außen zu Veröffentlichen. Bitte stellen Sie ebenfalls die Sicherheit weiter sicher. D.h. es sollte mit Firewalls oder VPN-Techniken der Zugriff geschützt werden.

> **Anmerkung**
>
> xentral unterstützt die Ausgabe des EC-Kassenbons über den Kassendrucker zur Zeit noch nicht. Deshalb muss im EC-Gerät die Einstellung für den Bon Druck nicht deaktiviert werden.

## Entnahme/ Einlage Konten

Sie können in xentral bestimmte Konten für die Entnahme bzw. Einlage von Geldbeträgen in der POS mit den entsprechen Steuersätzen definieren.

Über die Schaltfläche "Neuer Eintrag" kann ein neues Konto definiert werden.

![POS7.png](https://help.xentral.com/hc/article_attachments/19055687806236)

Wenn in der POS die Schaltfläche "Einlage" oder "Entnahme" gedrückt wird, erscheint sobald man ein Konto definiert hat ein Grund, in dem man das Entnahme/ Einlage Konto auswählen kann.

Im Kassenbuch der POS erscheint der Grund auch als Eintrag.

![POS8.png](https://help.xentral.com/hc/article_attachments/19055658912668)

Außerdem erfolgt zusätzlich ein Bonausdruck bei jedem Entnahme- / Einlage-Vorgang.

## Arbeiten mit der Kassenoberfläche

### Anmelden an der POS

Die Anmeldung an der POS erfolgt unter Verkauf → POS mit der Kassierer-Nummer, die beim Anlegen des Kassierers vergeben wurde.

Wenn die Anmeldung erfolgreich war, wird die Kassenoberfläche entsperrt. Wenn Ware verkauft werden soll, wählen sie zunächst oben in der Mitte, entweder einen konkreten Kunden aus den Stammdaten aus, oder "Laufkundschaft" bei einem anonymen Vorgang. Falls ein neuer Kundendatensatz angelegt werden soll, wählen Sie hier "Neuer Kunde".

Fügen Sie unter Warenkorb die Artikel hinzu, die der Kunde erwerben möchte. Dazu können Sie die Artikel über das im Screenshot markierte Feld suchen (Leertaste = alle verfügbaren Artikel auflisten), oder Artikel mit dem Barcodescanner erfassen (der Cursor muss dazu in dem markierten blauen Textfeld stehen).

Negative Mengen werden in den POS Positionen verhindert, da diese nicht verarbeitet werden können und zu Fehlern im Lager führen würden.

Wenn alle zu verkaufenden Artikel erfasst wurden, wählen Sie über die entsprechenden Schaltflächen im rechten oberen Bildschirmbereich (siehe Screenshot) die Art der Transaktion und ggf. die Bezahlart aus. Wählen Sie dort auch aus, ob eine Rechnung gedruckt werden soll oder nicht.

![POS9.png](https://help.xentral.com/hc/article_attachments/19055658912796)

Schließen Sie die Transaktion mit Hilfe der "Verkaufen" Schaltfläche ab. Nach dem Abschließen werden die Belege zu dieser Transaktion gedruckt.

### Seriennummern in der POS

Es ist möglich, Seriennummern direkt in der POS-Oberfläche zu erfassen.

Im Artikel muss dafür folgende Option ausgewählt sein:

![POS10.png](https://help.xentral.com/hc/article_attachments/19055687807900)

Im POS-Projekt in den POS-Einstellungen muss Folgendes eingestellt sein:

- Feld "Lagerprozess" → Der Lagerprozess darf nicht “Keine Lagerbuchung erzeugen” sein
- Die Option "Lieferschein stellen" muss ausgewählt sein

In den System-Einstellungen (Administration → Einstellungen → System → Grundeinstellungen → System) folgende Option auswählen:

- Positionen mit Seriennummern

### MHD + Chargen in der POS

Chargen und -MHD Artikel werden nach FIFO-Prinzip (first in first out) ausgebucht.

Ähnliche Vorraussetzungen, wie bei Seriennummern (s.o.):

- In Artikel Einstellungen: Charge und MHD verwenden
- In POS Einstellungen: Lieferschein erstellen, Lagerbewegung aktiv
- In Systemeinstellungen: Charge + MHD auf Belegen einblenden

## Belege abkassieren & stornieren in POS

Aufträge / Rechnungen können in die POS-Oberfläche geladen werden um diese dort abzurechnen oder zu stornieren. Auf dem Kassenbon ist das Bezahldatum abgedruckt, an dem die Bezahlung an der POS vorgenommen wurde. Unabhängig davon enthält der PDF Rechnungsbeleg in xentral das Rechnungserstellungsdatum.

Dazu klickt man auf die Schaltfläche "Beleg laden" rechts unten.

Man erhält folgende Auswahl:

![POS11.png](https://help.xentral.com/hc/article_attachments/19055687808412)

> **Anmerkung**
>
> Wenn du über die Schaltfläche "Beleg laden" ein Teilstorno (Schaltfläche "Teilstorno") oder Komplettstorno (Schaltfläche "Komplettstorno") anlegst, dann musst du die Artikel manuell einlagern, da diese nicht automatisch eingelagert werden.

### Belege abrechnen

Wenn man eine Auftrags- oder Rechnungsnummer im Popup oben eingegeben hat und auf "Über Kasse abrechnen" klickt, wird der jeweilige Beleg in der Kassenoberfläche geladen.

Vom Beleg wird in der POS-Oberfläche folgendes übernommen:1. die Positionen des Belegs 2. die Adressdaten des Belegs

Danach können Sie diesen wie einen normalen POS-Vorgang weiter abwickeln.

### Belege teilstornieren

Die Schaltfläche "Teilstorno" lädt alle Positionen des Auftrags / Rechnung im Popup. Danach kann man die Menge der einzelnen Positionen eingeben, die storniert werden sollen.

Mit einem Klick auf die "Übernehmen"-Schaltfläche werden die angegebenen Positionen in die POS geladen.

### Belege komplett stornieren

Die Schaltfläche "Komplettstorno" lädt alle Positionen direkt in die POS Oberfläche. Mit einem Klick auf die rote Storno-Schaltfläche, kann daraufhin eine Gutschrift erstellt werden.

Im Kassenbuch wird der Betrag der Gutschrift ausgebucht und im Tagesabschluss der POS als Entnahme gekennzeichnet. Die in xentral erstellte Rechnung wird automatisch storniert und es wird ein Gutschriftsbeleg für den Vorgang erstellt.

### Mehrere Aufträge pro Kassierer

Sofern in den Einstellungen des Projekts "Mehrere Aufträge pro Kassierer" selektiert wurde, sind in der POS Oberfläche die zwei Schaltflächen "Vorgang Speichern" & "Laden" sichtbar.

Mit der Schaltfläche "Vorgang Speichern", kann man die bereits erfassten Artikel eines Vorgangs in einer Liste speichern (z.B. wenn der Kunde noch zusätzliche Artikel einkaufen möchte) und mit der Schaltfläche "Laden" können gespeicherte Vorgänge geladen und abkassiert werden.

## Kassenabschluss

Den Kassenabschluss finden Sie in der POS-Oberfläche unter dem Reiter 'Abschluss'.

### Tagesabschluss

Der Kassenabschluss wird am Anfang des Tages automatisch erstellt.

Alle Buchungen eines Tages über die POS fließen automatisch in diesen Tagesabschluss. Das bedeutet, dass dieser nicht manuell festgelegt werden muss. Nachdem Sie das Bargeld gezählt haben und "festgeschrieben" wurde, wird die Zählung auch in den Tagesabschluss übernommen.

Mit dem PDF Icon rechts können Sie sich diesen Abschluss anschauen / herunterladen. Dort werden folgende Positionen des Tages aufgelistet:

- Alle Einnahmen pro Zahlungsweise
- Stornierte Belege (Wenn eine aus der POS erstellte Rechnung storniert wird)
- Ein- und Entnahmen aus der Kasse
- Summe Einnahmen (Bar) in Brutto und Netto
- Kasse Anfangsbestand
- Kasse Endbestand
- Gezähltes Bargeld (aufgeteilt in Münzen und Scheine)

Hier ein Beispiel-PDF des Kassenabschlusses über mehrere Seiten:

![POS13.png](https://help.xentral.com/hc/article_attachments/19055687809180)

### Bargeld zählen

Hier können Sie alle Münzen und Scheine zählen und die Anzahl jeweils in das entsprechende Feld eingeben.

Die Schaltfläche 'Gezählte Werte jetzt festschreiben' lädt die Anzahl der Münzen & Scheine in den Tagesabschluss

Die Schaltfläche “Gezählte Werte speichern ohne Korrekturbuchung” erzeugt eine Korrekturbuchung im Kassenbuch.

### Monatsabschluss

Hier wird ein Sammel-PDF für alle Tagesabschlüsse eines Monats erstellt.

Hier bekommen Sie einen kumulierten Abschluss mit aufaddierten Werten aus allen Monatstagen übersichtlich und knapp dargestellt.

### Zahlungseingang

Im Bereich Buchhaltung → Zahlungseingang können die Buchungen der Kasse importiert werden. Hierzu die entsprechende Kasse über das Stift Icon auswählen, anschließend wird man in die Maske "Import" weitergeleitet. Über die Schaltfläche "Live-Import" können die Kassen-Buchungen abgerufen werden und durch betätigen des "Buchung fertigstellen" importiert werden. Sobald die Buchung importiert wurde, sind die Rechnungsbelege der Kasse auch entsprechend ausgeglichen.

Es wird geprüft, ob es mehrere Buchungen mit gleichem Grundbetrag und Datum an dem Tag gibt. Falls ja wird in einer Klammer die Nummer der Kassenbuchung dran gehängt:

### POS Berichte Einstellungen

Unter Stammdaten → Projekte → Einstellungen → POS Einstellungen kann man den Umfang der Monats- bzw. der Tagesabschlüsse einstellen.

Option "Monatsberichte ohne Einzelbuchung": hier wird ein zusammengefasster Bericht erzeugt, in dem die Einzelbuchungen nicht angezeigt werden

Option "Einzelbuchungen ausblenden": dadurch werden in den Tagesabschlüssen die einzelne Buchungen ausgeblendet und es stehen nur die Ein- und Ausgänge drin.

## Trinkgeld

Im POS Modul kannst du auch den Erhalt von Trinkgeld über verschiedene Zahlungsweisen wie Bar, EC oder Kreditkarte festhalten. Du musst nur ein paar wenige Einstellungen tätigen, bevor du Trinkgeld erhalten kannst.

### Konfiguration

Die Trinkgeld Option für EC & Kreditkarte wird zunächst nicht im POS Modul angezeigt, du musst diese zunächst in den Projekteinstellungen aktivieren (Stammdaten → Projekte → Einstellungen → POS Einstellungen).

Als Nächstes legst du eine Kostenstelle für das Trinkgeld im Modul Kostenstellen (Administration → Einstellungen → Buchhaltung → Kostenstellen) an.

Dann gehst du im Modul POS (Konfiguration) auf Entnahme / Einlage Konten und legst dort einen neuen Eintrag an. Dort gibst du einen Grund und die Nummer der zuvor angelegten Kostenstelle an. Je nach Zweck des Trinkgelds kannst du Arbeitgeber oder Arbeitnehmer auswählen.

Für die Verwendung des POS Moduls muss bereits im Modul Kassen ein Konto Typ "Kasse" erstellt und aktiviert sein. In den Projekteinstellungen musst du zudem das Kassenkonto und die Laufkundschaft eintragen haben.

### Workflow

Zur Nutzung der Trinkgeld Funktion gehst du wie gewohnt in das Modul POS.

### Barzahlung

Zunächst wählst du den Artikel aus und klickst auf "verkaufen". Bei Barzahlung gibt es im Dialogfenster nicht direkt die Möglichkeit Trinkgeld einzugeben. Hier gibst du den Betrag, den der Käufer gezahlt hat ein und das Rückgeld wird automatisch berechnet. Der Abschluss der Verkaufs wird durch ein Dialogfenster bestätigt.

Um Trinkgeld zu erfassen klickst du anschließend auf "Einlage", gibst im Dialogfenster den Betrag ein und bestätigst mit "Ok". Das Geld wird nun auf das Trinkgeldkonto gebucht.

Wenn ein Mitarbeiter Trinkgeld entnimmt, wird das über die Entnahme festgehalten und der Betrag wieder im Dialogfenster eingegeben.

### Zahlung mit EC oder Kreditkarte

Etwas anders läuft das Ganze bei der Zahlung mit EC oder Kreditkarte sowie der Überweisung. Hier wird das Trinkgeld direkt beim Verkauf der Artikels festgehalten.

Bei EC und Kreditkarte kann auch nach dem Verkauf noch über die Trinkgeld-Schaltfläche ein Trinkgeld gebucht werden.

Während bei der Bargeldmethode das Geld zunächst eingelagert und anschließend entnommen wird. Wird die Entnahme des Trinkgeld bei Zahlung mit EC, Kreditkarte oder per Überweisung direkt mit eingerechnet. Die Veränderung erscheint auch direkt im Kassenkonto.

![POS14.png](https://help.xentral.com/hc/article_attachments/19055687810076)