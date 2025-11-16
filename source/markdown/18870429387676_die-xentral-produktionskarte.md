In diesem Artikel zeigen wir dir den grundsätzlichen Aufbau der Produktionskarte. Außerdem findest du detaillierte Erklärungen der Menüs und Funktionen, die dir dort zur Verfügung stehen.

Um das Produktionsmodul zu erreichen, folge dem PfadLager > Produktionoder suche über die Smart Search nach “Produktion”.

> **Tipp**
>
> Das Produktionsmodul wird in Xentral NextGen standardmäßig nicht in der Navigationsleiste auf der linken Seite angezeigt. Du kannst das Modul der Navigationsleiste für deinen Benutzer hinzufügen, indem du den Anweisungen im folgenden Artikel folgst:Individuelle Navigationsleiste einrichten.

Wenn du eine bestimmte Produktion öffnest, befindest du dich in der sog.Produktionskarteund kannst viele Details dieser Produktion bearbeiten. Je nach Status sind manche Reiter relevant oder nicht.

## Reiter Details

### Tab Produktion

Hier findest du die sog. Kopfdaten einer jeden Produktion. Daten, die du hier festlegst, gelten für den ganzen Produktionsvorgang.

![Produktionskarte_Produktion_Header.png](https://help.xentral.com/hc/article_attachments/19368069028124)

#### Monitor

Der Monitor in der Mitte zeigt dir den Status aller produktionsbezogenen Schritte an. Details zu den unterschiedlichen Status findest du im Artikel[Produktionsübersicht](https://help.xentral.com/hc/de/articles/18870429370140#UUID-20bfb91b-663a-e5ee-9dd1-e875d5b2cccb).

![Produktionskarte_Produktion_Header_Monitor.png](https://help.xentral.com/hc/article_attachments/19368105816220)

#### Aktionsmenü

Das Aktionsmenü befindet sich sowohl im Tab Produktion als auch im Tab Positionen oben rechts auf der Karte:

![Produktionskarte_Produktion_Aktionsmenu.png](https://help.xentral.com/hc/article_attachments/19368105816604)

Mit dem Aktionsmenü kannst folgende Maßnahmen durchführen:

![Produktionskarte_Produktion_Aktionsmenu_Optionen.png](https://help.xentral.com/hc/article_attachments/19368105816988)

- Produktion starten: Hiermit änderst du den Status der Produktion von FREIGEGEBEN auf GESTARTET. Voraussetzung ist, dass das notwendige Material in ausreichender Menge verfügbar ist.
- Produktion stornieren: Über diese Aktion kannst du die Produktion löschen (im Entwurfsstadium) oder stornieren (in allen anderen Stadien). Beachte den folgenden Hinweis!
- Produktion kopieren: Diese Aktion legt eine neue Produktion an und übernimmt allgemeine Daten, Einstellungen Produktion und Positionen. Das Angelegt-am-Datum, sowie Produktionsstart und -ende werden nicht übernommen.
- Produktion abschicken: Hierüber gelangst du zum Abschicken-Dialog, mit dem du ein PDF des Produktionsvorgangs versenden kannst.
- Produktion auslagern: Wenn du auf diese Aktion klickst, gelangst du zum “Artikel für Produktion”-Dialog. Dort kannst du Material für die Produktion auslagern.
- Produktion einlagern: Mit dieser Aktion lagerst du das hergestellte Erzeugnis einer Produktion ein.
- Produktion abschließen: Hiermit schließt du eine Produktion ab. Voraussetzung ist, dass das hergestellte Erzeugnis vorher eingelagert wurde.
- Teilproduktion erstellen: Diese Aktion ermöglicht es dir, Produktionen mit Produktionsmenge &gt; 1 in Teilproduktionen aufzuspalten. Dies ist z. B. hilfreich, wenn dein Material zwar nicht für die gesamte Produktionsmenge reicht, aber für Teilmengen, die du schon produzieren möchtest, bevor das gesamte Material an Lager ist. Voraussetzung für die Aufspaltung einer Produktion ist, dass noch kein Material ausgelagert wurde.
- Export als CSV: Hiermit kannst du die Daten der Produktion in eine CSV-Datei exportieren. Als Trennzeichen wird das Semikolon verwendet.
- PDF öffnen: Hier kannst du die Produktion als PDF-Datei öffnen. Die Datei enthält die allgemeinen Daten, die Fertigungsstückliste und die Arbeitsanweisung.
- Alle Positionen löschen: Mit dieser Funktion kannst du die Positionen mit einem Klick löschen. Die Kopfdaten der Produktion bleiben unverändert.

#### Allgemein

![Produktionskarte_Produktion_Header_Allgemein.png](https://help.xentral.com/hc/article_attachments/19368105818268)

In diesem Abschnitt stellst du einige allgemeine Daten für die Produktion ein. Folgende Felder kannst du nutzen:

- Kunde: Trage eine Kundennummer ein und bestätige die Auswahl mit übernehmen. Dieses Feld ist ein Pflichtfeld.
- Projekt: Wähle ein Projekt, dem die Produktion zugeordnet werden soll.
- Status: Dieses Feld zeigt den Status der Produktion an.
- Auftrag: Hier kannst du die Nummer eines Verkaufsauftrages eintragen, um eine Produktion und einen Verkaufsauftrag miteinander zu verknüpfen.
- Interne Bezeichnung: Dieses Feld kannst du nutzen, um die Produktion intern zu identifizieren oder um eigene kurze Notizen einzutragen. Die interne Bezeichnung wird in der Produktionsübersicht unterhalb der Produkt-Bezeichnung und im Produktions-PDF angezeigt.
- Angelegt am: Dieses Datum wird automatisch ausgefüllt. Bei Bedarf kannst du es überschreiben.
- Bevorzugtes Lager: Wenn du einschränken möchtest, dass Material nur von Lagerplätzen eines bestimmten Lagerortes verwendet werden soll, kannst du hier den entsprechenden Lagerort eintragen.
- Schreibschutz: Setze diesen Haken, sobald du keine Änderungen an den Daten mehr vornehmen möchtest.

#### Aktionen

![Produktionskarte_Produktion_Header_Aktionen.png](https://help.xentral.com/hc/article_attachments/19368105819164)

Folgende Aktionen stehen hier für dich bereit:

- Produktionsanweisungen als PDF: Hier kannst du die Produktion mit Stückliste und Arbeitsschritten als PDF ausgeben.
- Datenblätter als ZIP: Hier kannst du alle angehängten Dateien in einem zip-Archiv herunterladen.
- Etikettensets für alle Produkte: Diese Schaltfläche erzeugt Etikettensets für alle in der Produktion enthaltenen Erzeugnisse und sendet sie an den Spooler. Voraussetzung ist, dass Etiketten im gleichnamigen Reiter hinzugefügt wurden.
- Seriennummern-Etiketten für alle Produkte: Hiermit generierst du Seriennummern-Etiketten für alle seriennummerngeführten Erzeugnisse und sendest sie an den Spooler. Voraussetzungen sind, dass Seriennummern zugewiesen und dass Etiketten im gleichnamigen Reiter hinzugefügt wurden.
- Stückliste als Etiketten drucken

Die folgenden Schaltflächen stehen nur bei Produktionen mit StatusGESTARTETzur Verfügung:

- Zum Produktionszentrum: Mit dieser Schaltfläche wechselst du zum Produktionszentrum. Weitere Details zum Produktionszentrum findest du auf dieser [Seite](https://help.xentral.com/hc/de/articles/18870420757404#UUID-68222470-282c-fb58-d100-d91148e6f837).
- Seriennummer generieren: Hier kannst du ein Menü öffnen, mit dem du eine Seriennummer für das Erzeugnis generieren kannst:
- Charge erzeugen: Hierüber gelangst du in das Menü zur Erzeugung von Chargennummern:

#### Einstellung Produktion

![Produktionskarte_Produktion_Header_EinstellungProduktion.png](https://help.xentral.com/hc/article_attachments/19368069043356)

Folgende Einstellungen kannst du für eine Produktion vornehmen:

> **Anmerkung**
>
> Die vier Datumsfelder “Auslieferung Datum”, “Bereitstellung Start”, “Produktion Start” und “Produktion Ende” sind rein informativ und können nach deinen eigenen betrieblichen Bedürfnissen genutzt werden. Die Felder werden in anderen Modulen nicht zur Berechnung herangezogen.

- Reservierung Material: Hier legst du den Zeitpunkt fest, zu dem das Material für die Produktion reserviert werden soll:
- Entnahme im Lager: Du kannst entscheiden, wie die Materialentnahme gebucht werden soll:
- Unterstücklisten auflösen:
  - Wenn du möchtest, dass für jede enthaltene Unterstückliste ein eigener Produktionsvorgang angelegt und mit dieser Produktion verknüpft wird, setze keinen Haken. Anschließend kannst du die Schaltfläche “Unterstücklisten als eigene Produktion anlegen” nutzen, um die Unterproduktionen anzulegen. Dabei werden bereits vorproduzierte Unterstücklisten ausgenommen, indem du den Haken “Lagerbestand und Min. Bestellmenge betrachten” setzt.
  - Ist der Haken gesetzt, werden alle Bauteile in der vorliegenden Produktion “in einer Ebene” eingefügt, unabhängig davon, ob sie unmittelbar aus der Stückliste des Erzeugnisses oder einer Unterstückliste stammen. In diesem Fall werden keine gesonderten Unterproduktionen angelegt.
- Funktionstest: Mit diesem Haken kannst du steuern, ob bei dieser Produktion ein Funktionstest durchgeführt und aufgezeichnet werden soll (Haken gesetzt) oder nicht (Haken nicht gesetzt). Setzt du den Haken nicht, wird dir dies in einem Banner angezeigt. In diesem Fall kann der Werker den Funktionstest im Produktionszentrum nicht starten und aufzeichnen.
- Beschreibungen von Arbeitsschritten anzeigen: Du kannst wählen, ob im Produktionsdokument die ausführliche Arbeitsanweisung einschließlich der Beschreibung (Haken gesetzt) oder nur die Titel der Arbeitsschritte (Haken nicht gesetzt) angedruckt werden soll.
- Seriennummer anlegen: Mit diesem Haken kannst du steuern, ob bei dieser Produktion Seriennummern für das Erzeugnis automatisch erzeugt werden (Haken gesetzt) oder manuell vergeben werden sollen (Haken nicht gesetzt). Setzt du den Haken nicht, wird dir dies in einem Banner angezeigt. In diesem Fall musst du im weiteren Verlauf Seriennummern manuell vergeben.
- Unterseriennummer erfassen: Mit diesem Haken kannst du steuern, ob bei dieser Produktion Seriennummern von verbauten Materialien erfasst werden sollen (Haken gesetzt) oder nicht (Haken nicht gesetzt). Setzt du den Haken nicht, wird dir dies in einem Banner angezeigt. In diesem Fall können keine verbauten Seriennummern zugeordnet werden.
- Auslieferung Lager: Unter diesem Datum wird der Warenausgangstermin verstanden, an dem die fertige Ware an den Kunden geliefert werden soll.
- Bereitstellung Start: An diesem Datum soll das Material vom Lager an die Produktion bereitgestellt werden.
- Produktion Start: Hier soll die Produktion beginnen…
- Produktion Ende: … und hier abgeschlossen sein.

#### Freitext und Interne Bemerkung

![Produktionskarte_Produktion_Header_FreitextBemerkung.png](https://help.xentral.com/hc/article_attachments/19368105824412)

In diesen beiden Feldern kannst du beliebige Informationen hinterlegen und nach Wunsch formatieren.

> **Tipp**
>
> Das Vorhandensein eines Freitextes ist in der Produktionsübersicht mit einem schwarzen, das einer Internen Bemerkung mit einem roten Sternchen gekennzeichnet.

- Freitext: Dieser Text wird auf dem Produktionsbeleg angedruckt.
- Interne Bemerkung: Dieser Text ist ausschließlich in diesem Feld sichtbar und dient für interne / vertrauliche Zwecke.

### Tab Positionen

In diesem Tab kannst du das zu produzierende Erzeugnis eintragen und verwalten.

![Produktionskarte_Positionen.png](https://help.xentral.com/hc/article_attachments/19368105825820)

#### Monitor und Aktionsmenü

Diese beiden Funktionen oben links und oben rechts hast du bereits im[Tab Produktion](#UUID-e0c9e80f-6be5-7a76-ac8d-996f628409e1_section-idm234819921159949)kennengelernt.

![Produktionskarte_Positionen_MonitorAktionsmenu.png](https://help.xentral.com/hc/article_attachments/19368105829020)

#### Produktionszeilen

Hier findest du die Produktionszeilen. Tippe die Artikelnummer des zu produzierenden Erzeugnisses in die Spalte “Artikel”. Wenn du mehr als ein Stück in dieser Produktion herstellen möchtest, passe die Menge an, ansonsten belasse sie auf 1. Bestätige mit einem Klick aufeinfügen.

![Produktionskarte_Positionen_ProduktEinfugen.png](https://help.xentral.com/hc/article_attachments/19368105830300)

Sobald du ein Erzeugnis eingefügt hast, wird die Stückliste aus den Stammdaten in die vorliegende Produktion kopiert. Es entfaltet sich die sog. Produktionsstückliste:

![Produktionskarte_Positionen_Produktionsstuckliste.png](https://help.xentral.com/hc/article_attachments/19368069061148)

> **Anmerkung**
>
> Wenn Erzeugnis mehrere Unterebenen hat, wird nur die erste Ebene oder alle Unterebenen aufgeklappt - je nachdem, ob du im Reiter Produktion den Haken “Unterstücklisten auflösen” gesetzt hast oder nicht.

Die Produktionsstückliste ist eine Kopie der Stammdaten und kann individuell für einen Vorgang angepasst werden. Eine Änderung greift nur in diesem einen Vorgang. Die ursprüngliche Stückliste im Artikel und andere Produktionen sind von einer Anpassung nicht betroffen.

Du hast somit die Möglichkeit, zusätzliche Bauteile einzufügen und andere aus der Produktionsstückliste zu entfernen:

![Produktionskarte_Positionen_Produktionsstuckliste_Individualisieren.png](https://help.xentral.com/hc/article_attachments/19368105834140)

(1) Füge weitere Bauteile in die Produktionsstückliste ein, indem du einen Artikel eintippst und mit einfügen bestätigst.

(2) Öffne eine Zeile für weitere Detailbeschreibungen, kopiere oder lösche sie oder ändere die Reihenfolge von Zeilen über die Aktionen am rechten Rand jeder Zeile.

(3) Nutze die Sammelbearbeitung um ausgewählte / alle Zeilen zu löschen.

Über die Schaltfläche Artikel manuell suchen / neu anlegen öffnest du eine Suchmaske, über die du nach Artikeln suchen oder neue Artikel anlegen kannst:

![Produktionskarte_Positionen_ArtikelSuchen.png](https://help.xentral.com/hc/article_attachments/19368069062940)

### Tab Vorschau

In diesem Tab kannst du die Produktion als Druckvorschau betrachten. Generell findest du auf der ersten Seite des Ausdrucks die Kopfdaten und die Produktionsstückliste und auf der/n Folgeseite/n die Arbeitsanweisung.

![Produktionskarte_Vorschau.png](https://help.xentral.com/hc/article_attachments/19368105837212)

### Tab Protokoll

Nutze das Protokoll, wenn du dir einen genaueren Überblick über eine Produktion verschaffen willst, insbesondere, wenn es um die erfolgten Aktivitäten, Stückliste und Arbeitsanweisungen sowie die erfassten Zeiten geht. Außerdem kannst du von dort auf dasAktionsmenüund dieAktionenzugreifen.

![Produktionskarte_Protokoll.png](https://help.xentral.com/hc/article_attachments/19368069064732)

## Reiter Dateien

Um neue Dateien an die Produktion anzuhängen, klicke aufNeue Datei anlegen(1). Bei aktivierter Schaltfläche (2), kannst du die Sortierung von Dokumenten über die Pfeiltasten ändern.

![Produktionskarte_Dateien.png](https://help.xentral.com/hc/article_attachments/19368105840540)

Alle gesammelten Dokumente können als zip-Archiv heruntergeladen werden (unter der Stapelverarbeitung oder im ReiterDetailsunterAktionen > Datenblätter als ZIP).

## Reiter Arbeitsanweisung

Sofern du im Artikel des Erzeugnisses eine Arbeitsanweisung angelegt hast, wird sie hieran geladen. Du erhälst so einen Überblick über alle geplanten Arbeitsschritte dieser Produktion und deren Status. Mit (1) kannst du die Reihenfolge der Schritte ändern, unter (2) kannst du weitere Details bearbeiten mit (3) und (4) kannst du Schritte löschen bzw. neue hinzufügen.

![Produktionskarte_Arbeitsanweisung_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19368069067164)

In der Detail-Ansicht (2) kannst du die einzelnen Schritte präzisieren: Du kannst z. B. einen Mitarbeiter für die Tätigkeit wählen und den Status eintragen, sobald du eine entsprechende Rückmeldung erhälst:

![Produktionskarte_Arbeitsanweisung_Details.png](https://help.xentral.com/hc/article_attachments/19368069067676)

## Reiter Funktionsprotokoll

Sofern du im Artikel des Erzeugnisses ein Funktionsprotokoll angelegt hast, wird es hieran geladen. Du erhälst so einen Überblick über alle geplanten Prüfschritte dieser Produktion und deren Status. Mit (1) kannst du die Reihenfolge der Schritte ändern, unter (2) kannst du weitere Details bearbeiten mit (3) und (4) kannst du Schritte löschen bzw. neue hinzufügen.

![Produktionskarte_Funktionsprotokoll_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19368069069596)

In der Detail-Ansicht (2) kannst du die einzelnen Schritte präzisieren: Du kannst z. B. den Test-Typ bestimmen, eigene Textfelder definieren oder Güteklassen eintragen, sobald du eine entsprechende Rückmeldung erhälst:

![Produktionskarte_Funktionsprotokoll_Details.png](https://help.xentral.com/hc/article_attachments/19368105847836)

## Reiter Etiketten

Sofern du im Artikel des Erzeugnisses Etiketten ausgewählt hast, werden sie hier angezeigt. Du kannst auch neue Etiketten hinzufügen:

![Produktionskarte_Etiketten.png](https://help.xentral.com/hc/article_attachments/19368105849372)

## Reiter Seriennummern

Hier bekommst du einen Überblick über die zu der Produktion gehörigen Seriennummern - sowohl der Erzeugnisse (1), als auch der Komponenten (2). Über den Stift (3) gelangst du zum ReiterEinzelproduktionen erfassen.

![Produktionssteuerung_ReiterSeriennummern.png](https://help.xentral.com/hc/article_attachments/19368069073820)

## Reiter Chargen

Hier erhälst du einen Überblick über die in der Produktion eingesetzten und produzierten Chargen bzw. Mindesthaltbarkeitsdaten.

Unter dem TabEingesetzte Chargensind alle chargengeführten Bauteile oder Bauteile mit Mindesthaltbarkeitsdatum aufgelistet mit der Angabe, in welcher Produktion sie verwendet wurden. Über das X am rechten Rand kannst du eine Zuweisung entfernen.

![Produktionsubersicht_Chargen.png](https://help.xentral.com/hc/article_attachments/19368069074972)

Unter dem TabProduzierte Chargenfindest du alle erzeugten Chargen bzw. Mindesthaltbarkeitsdaten der von dir produzierten Artikel. Über die Produktionsnummer kannst du zu einer betreffenden Produktion wechseln.

## Reiter Abschluss

Eine ausführliche Beschreibung dieses Reiters und zu dem generellen Vorgehen beim Produktionsabschluss findest du[hier](https://help.xentral.com/hc/de/articles/18870451160988#UUID-29284617-b0fc-fc6e-2df7-284c68337605).