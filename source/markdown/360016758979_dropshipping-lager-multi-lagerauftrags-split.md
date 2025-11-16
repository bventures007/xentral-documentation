## Wann nutzt du die Funktion?

Die Funktion **Dropshipping Lager** hilft dir immer dann, wenn du Ware von mehreren Lagerstandorten verschicken willst. Dabei spielt es keine Rolle, ob sich die Standorte innerhalb deines Unternehmens befinden oder ob du die Logistik von einem Drittanbieter erledigen lässt. Das Modul teilt einen Auftrag automatisch auf, wenn die Artikel in verschiedenen Lagerorten liegen. Man bezeichnet diese Funktion auch als Order-Split oder Multi-Warehouse Management.

![DropshippingLager_Workflow.png](https://help.xentral.com/hc/article_attachments/20225615339292)

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in das Modul Dropshipping Lager**
>
> Möchtest du dir innerhalb weniger Minuten einen Überblick über die Funktionen und die Nutzung des Moduls **Dropshipping Lager** in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/z8MOl3hYJbM)**

### Features

- Regeln und Prioritäten für die Aufteilung von Aufträgen in Teilaufträge festlegen
- Teilaufträge in Teillieferungen überführen
- Teilrechnungen oder Sammelrechnungen vorbereiten
- Befüllen der Felder **Projekt ** und/oder **Bevorzugtes Lager** im Auftrag nach vorgegebenen Regeln
- Verschiedene Möglichkeiten, die Funktion auszulösen (manuelle Auftragsbearbeitung, Prozessstarter, Auto-Versand, Shopimport)

> **Anmerkung**
>
> Nicht enthaltene Funktionalitäten:
>
> - Erstellung von Lieferantenbestellungen. Nutze hierfür das ModulDropshipping Lieferant.
> - Senden von Lieferscheinen an die Lagerorte. Nutze für die Automatisierung dieses Prozesses das ModulÜbertragungen.

## Wie konfigurierst du deine Dropshipping Lager?

### Voraussetzungen

Bevor du dein **Dropshipping Lager** einrichten kannst, müssen Lagerorte in Deiner Lagerverwaltung angelegt sein. Falls du noch keine Lagerorte eingerichtet hast, hole dies im Modul Lagerverwaltung (Lager > Lagerverwaltung > +NEU) nach.

### Einrichtung

Sobald du deine grundsätzliche Lagerstruktur eingerichtet hast, kannst du die Lagerorte, für die die Funktion **Dropshipping Lager** greifen soll, als solche Lager konfigurieren.

Suche hierzu über dieSmart Searchnach **Dropshipping Lager** und öffne das Modul.

#### Übersicht

Hier siehst du alle Lager, für eine Dropshipping-Konfiguration angelegt ist. Bei der erstmaligen Einrichtung ist die Liste leer. Per Klick auf+ Neu anlegenlegst du eine neue Konfiguration an.

![DropshippingLager_Ubersicht.png](https://help.xentral.com/hc/article_attachments/20225556657436)

##### Neue Konfiguration anlegen

![DropshippingLager_NeueKonfiguration.png](https://help.xentral.com/hc/article_attachments/20225615342236)

- Lager: Wähle hier ein Lager aus, das beim Dropshipping genutzt werden soll.
- Projekt Filter: Wenn du hier ein Projekt einträgst, prüft die Funktion bei der Ausführung, ob das Projekt im Auftrag mit diesem Projekt übereinstimmt. Wenn ja, greift Dropshipping. Ist hier kein Projekt eingetragen, greift die Funktion immer.
- Ziel-Projekt: Wenn die abgesplitteten Teilaufträge ein eigenes Projekt erhalten sollen, das nicht dem des Ursprungsauftrags entspricht, kannst du hier ein entsprechendes Ziel-Projekt eintragen. Hiermit kannst du z. B. erreichen, dass ein bestimmtes Ziel-Projekt mit einem projektspezifischen Logistikprozess arbeitet. Lässt du das Feld leer, wird das Projekt vom Ursprungsauftrag übernommen.
- Prio: Hiermit gibst du vor, in welcher Reihenfolge die Prüfsequenz über die verschiedenen Dropshipping-Lager abarbeitet. Die niedrigste Zahl wird dabei zuerst geprüft.
- Auftrag splitten: Xentral prüft für jede Prio, wie mit einem zu splittenden Auftrag vorgegangen werden soll.
  - Auftrag immer aufsplitten: Die Artikel, die lagernd auf diesem Lagerort sind, werden auf jeden Fall vom Auftrag in einen Teilauftrag weg gesplittet, ungeachtet, ob nur Teilmengen erfüllt werden können oder nicht. Wenn nach dem Split noch Restmengen / Restpositionen übrig bleiben, setzt das System seine Prüfung beim Lager mit der nächst höheren Priorität fort.
  - Erlaube aufsplitten: Das System durchläuft die Prüfsequenz zunächst vollständig und prüft, ob der gesamte Auftrag von einem der Lager vollständig ausgeführt werden kann. Wenn ja, wird der Auftrag diesem Lager zugewiesen. Falls nein, erfolgt in der nächsten Prüfrunde eine Verteilung auf verschiedene Lager/Teilaufträge.
  - Niemals aufsplitten: Hiermit gibst du vor, dass Aufträge niemals aufgesplittet, sondern nur in Gänze einem Lagerort zugewiesen werden. Kann der Auftrag nicht in Gänze erfüllt werden, bleibt die Auftragsampel rot und du kannst manuell entscheiden, wie weiterverfahren werden soll. Diese Funktion kannst du auch nutzen, um die Felder “Projekt” und/oder “Bevorzugtes Lager” im Auftrag gezielt zu befüllen.
- Just-In-Time Stücklisten aufsplitten:
  - Erlaube aufsplitten: Komponenten einer Just-In-Time Stückliste dürfen auf unterschiedliche Aufträge verteilt werden. Hierbei wird der Titel der Just-In-Time Stückliste in alle Teilaufträge kopiert, der Gesamtpreis verbleibt als Position im Ursprungsauftrag.
  - Niemals aufsplitten: Alle Positionen einer Just-In-Time Stückliste werden in jedem Fall als Block in einem Auftrag zusammengehalten.
- Positionen splitten:
  - Erlaube aufsplitten: Ist die Gesamtmenge einer Position nicht von einem einzelnen Lagerort erfüllbar, dürfen Teilmengen auf unterschiedliche Teilaufträge verteilt werden.
  - Niemals aufsplitten: Eine Position wird in jedem Fall gesamt von einem Teilauftrag / Lagerort bedient.
- Aktiv: An- oder Ausschalten der Regel

#### Einstellungen

In diesem Tab nimmst du allgemeine Einstellungen vor.

![DropshippingLager_Einstellungen.png](https://help.xentral.com/hc/article_attachments/20225615345564)

- Autoversand ausführen:
  - Ist diese Option **aktiviert**, wird der Auto-Versand automatisch im Anschluss an das Aufsplitten angestoßen.
  - Ist diese Option **deaktiviert** (empfohlen), startet der Auto-Versand nur über den regulären Prozessstarter.
- Rechnung erstellen, falls nicht angelegt:
  - Ist diese Option **aktiviert**, erzeugt das System eine Gesamtrechnung über alle Teilaufträge. Die Rechnungspositionen entsprechen damit dem Zustand von vor der Splittung in mehrere Aufträge. Achtung: Diese Funktion solltest du aus steuerrechtlichen Gründen nur dann aktivieren, wenn sichergestellt ist, dass alle Teillieferungen zeitgleich mit der Gesamtrechnung versendet werden können.
  - Ist diese Option **deaktiviert** (empfohlen), werden Einzelrechnungen für jede Teillieferung im Rahmen des Versandprozesses erzeugt.
- Anzahl gleichzeitiges Abarbeiten von Aufträgen im Prozessstarter: Die Zahl bestimmt die Anzahl der offenen Aufträge, die pro Prozessstarter-Aufruf geprüft werden sollen. Bei großer Auftragsmenge empfehlen wir, hier eine Begrenzung einzusetzen und dafür eher den Prozessstarter in geringerem Zeitabstand aufzurufen. Bei kleinerer Auftragsmenge kannst du auf die Begrenzung verzichten, indem du 0 einträgst.

## Wie startest du die Funktion?

Sobald du die Einrichtung deines Dropshipping-Lagers abgeschlossen hast, kannst du die Funktion wie folgt anstoßen:

### Möglichkeit 1: Start per Prozesstarter

Zur automatischen Prüfung aller offenen Aufträge auf Artikel, die auf einem Dropshipping Lager verfügbar sind, kannst du den Prozessstarter nutzen. Öffne dazu das Modul **Prozessstarter ** und aktiviere den Parameter**dropshippinglager**. Bei jedem Durchlauf des Prozessstarters werden passende Aufträge in Teilaufträge gesplittet.

![DropshippingLager_Prozessstarter.png](https://help.xentral.com/hc/article_attachments/20225615346716)

### Möglichkeit 2: Manueller Start

Alternativ kannst du ohne den Prozessstarter arbeiten. Bei allen Aufträgen, für die die Dropshipping-Regeln erfüllt werden, erscheint nach der Freigabe des Auftrags eine Schaltfläche zur Ausführung der Dropshipping-Funktion:

![DropshippingLager_ManuellStarten.png](https://help.xentral.com/hc/article_attachments/20225556673948)

## FAQ

Im Folgenden haben wir häufige Fragen und Antworten zum Thema Dropshipping Lager für dich gesammelt.

### Ich möchte einzelne Aufträge ohne Dropshipping ausführen, obwohl die eingerichteten Regeln im Auftrag zutreffen würden. Wie kann ich das umsetzen?

Das erreichst du ganz bequem und einfach, indem du in dem entsprechenden Auftrag das Feld **Bevorzugtes Lager ** nicht leer lässt, sondern mit einem Lager deiner Wahl befüllst. Das Feld**Bevorzugtes Lager** übersteuert die Dropshipping-Funktion.

### Ich habe unterschiedlich geartete Just-In-Time Stücklisten und möchte, dass manche aufgesplittet werden und andere unbedingt zusammengehalten werden. Wie kann ich das erreichen?

Wir empfehlen, dass du hierfür mit dem Projektfilter arbeitest und damit erzwingst, dass die Artikel auf verschiedene Projekte zugeordnet werden.

### Meine Aufträge werden nicht gesplittet, obwohl alles richtig eingerichtet ist und die Regeln aus den Dropshipping-Lagern erfüllt sind. Warum?

Stelle sicher, dass das Feld **Bevorzugtes Lager** im Auftrag leer ist, denn dieses Feld übersteuert die Dropshipping-Funktion.