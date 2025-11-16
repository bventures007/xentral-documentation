> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Mit dem extra ModulBestellvorschlag Tagkann über die Auftragsmenge ein Bestellvorschlag für einen bestimmten Tag erzeugt werden. Dabei werden alle Aufträge, die noch nicht von diesem Bestellvorschlag erfasst wurden, addiert und der Bedarf für die Produktion/Bestellung ausgerechnet.

## Übersicht

In derÜbersichtkann der Bestellvorschlag über Auswahlfelder durchgeführt und zurückgesetzt werden.

### Filter

In der Filteransicht können folgende Filter gesetzt werden:

- nur markierte Artikel anzeigen: Zeigt nur diejenigen Artikel an, die aus dem Bestellvorschlag generiert wurden. Diese Artikel sind automatisch angehakt
- **alle Artikel anzeigen:** Zeigt alle Artikel an, auch die, die nicht Teil des Bestellvorschlags sind

## Tagesbestellung Vorschlag

- **Lieferant**: Die Auswahl kann, falls gewünscht, auf einen einzelnen Lieferanten beschränkt werden,
- **Tag**: Berücksichtigt alle Aufträge (Auftragsdatum) bis zu dem ausgewählten Tag
- **Starten**: Button führt den Bestellvorschlag mit getroffener Auswahl durch

### Zurücksetzen

- **Bestellvorschlag zurücksetzen**: Der Button setzt den letzten Bestellvorschlag zurück. Dabei bleiben die Aufträge, für die bereits Bestellungen erzeugt wurden, trotzdem gespeichert, werden jedoch nicht mehr für diesen Bestellvorschlag verwendet

### Berechnung des Bedarfs

Aus den Aufträgen, die bisher noch nicht in Bestellungen umgewandelt wurden, wird der Bedarf des Bestellvorschlags errechnet. Dabei ist der Bedarf unabhängig vom Auftragsstatus.

### Bestellung(en) erzeugen

Über den ButtonBestellung(en) erzeugenwerden alle Artikel mit gefüllten Bedarfsfeldern in eine oder mehrere Bestellungen übernommen. Dabei wird pro Lieferant eine Bestellung aufgegeben.

## Einstellungen

In den Einstellungen kann eingerichtet werden, dass nur Aufträge ab einer bestimmten ID berücksichtigt werden. Wird das Feld nicht ausgefüllt, werden alle Aufträge, unabhängig von der ID, berücksichtigt.