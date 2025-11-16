## Inhaltsverzeichnis

Die Artikelübersicht listet Lieferanten, für die ein Bestellvorschlag vorliegt, fehlende Artikel und nachbestellte Artikel auf.

### Lieferanten

Diese Übersicht basiert auf den Mengen in den Positionen von Aufträgen und Bestellungen.

Dargestellt sind alle Lieferanten, bei denen:

- Bestellungen aufgegeben werden sollen.Schwarze Ziffer= Anzahl der Artikel, bei denen die Bestandsmindestmenge unterschritten wurde.
- Bestellungen müssen aufgegeben werden.Rote Ziffer= Anzahl der Artikel, bei denen nicht genügend Einheiten auf Lager sind, um die offenen Bestellungen zu bedienen

Die Aktion "Bestellvorschlag" liefert direkt eine Bestellvorschlagsliste mit den Standardeinstellungen. Die Berechnungsgrundlage ist hier 3 Monate und zeigt nur offene Bestellungen an.

### Fehlende Artikel

Diese Registerkarte zeigt alle fehlenden Artikel in einer individuellen Auflistung, die:

- Nachbestellt werden sollten.Blaue Artikelbezeichnung= Bestandsmindestmenge des Artikels unterschritten
- Nachbestellt werden muss.Rote Artikelbezeichnung= Nicht genügend Einheiten des Artikels auf Lager, um offene Bestellungen zu bedienen

> **Wichtig**
>
> Beachte zwingend folgende Einschränkung: Die in den Artikelstammdaten gespeicherte Lieferzeit wird zwar in der Übersicht fehlender Artikel angezeigt, jedoch nicht für die Bedarfsplanung berücksichtigt. Das bedeutet, dass die Lieferzeit des Artikels keinen Einfluss auf die angezeigten Informationen hat. Achte daher besonders auf Artikel, die lange Lieferzeiten bei deinem Lieferanten haben, um Engpässe zu vermeiden und die Bestellung frühzeitig auszulösen.

![bestellvorschlag_3039.png](https://help.xentral.com/hc/article_attachments/5037945007004)

### Nachbestellte Artikel

In diesem Bereich werden alle nachbestellten Artikel in einem individuellen Angebot angezeigt, die derzeit auf Lager sind.

## Schnellproduktion Bestellvorschlag

Neben der Übersicht befindet sich die OptionSchnellproduktion Bestellvorschlag. Hier kannst du einen beliebigen Lieferanten für einen Bestellvorschlag auswählen und den Bestellvorschlag starten.

> **Tipp**
>
> Voraussetzung ist, dass die gewählte Adresse eine Lieferantennummer hat (Rolle in Adresse) und es Artikel gibt, die einen Einkaufspreis für diesen Lieferanten hinterlegt haben. Der Artikel muss ein Lagerartikel sein. Wenn ein Artikel zwar den selben Hauptlieferanten hat, aber kein Einkaufspreis hinterlegt ist, wird eine Warnung eingeblendet.

- Lieferant→ Lieferant auswählen
- Berechnungsbasis Anzahl der letzten Monate→ Zeitraum der Berechnungsbasis wählen. Daraus wird die durchschnittliche Menge der Artikel ermittelt, die Sie in dem betrachteten Zeitraum verkauft haben
- Monate→ Wählen Sie den Bereich der Bestellmenge. Entweder wird die Menge an Artikeln ermittelt, mit der die aktuell offenen Aufträge oder Produktionen bedient werden können, oder es wird auf Basis der Berechnungsgrundlage prognostiziert, wie viele Artikel Sie für den Bedarf der nächsten x Monate bestellen müssten

Der Bestellvorschlag wird unter Berücksichtigung von eventuellen Mindestbestell- oder Lagermengen berechnet.

### Informationen zur Artikelmenge

- Artikel→ Bezeichnung des Artikels
- Nummer→ Artikelnummer
- Im Lager / Mit Sperrlager→ Anzahl der Artikel auf Lager / Anzahl der Artikel auf Lager, inklusive Bestand auf Sperrlagern
- Mindestbestellmengen (Artikel)→ Falls bei einem Artikel eine Mindesbestellmenge hinterlegt wurde, wird diese hier angezeigt
- Mindestlager (Artikel)→ Mindestlagermenge (wird im Artikelstamm eingestellt)
- Pro Monat→ Verbrauch pro Monat
- Im Auftrag→ Anzahl der Einheiten des Artikels, gebucht in offenen Aufträgen
- In Bestellung→ Artikel in Bestellungen bei Lieferanten (violett → bestellt, rot → in angelegten Bestellungen)
- Verkauf Gesamt→ Gesamte Verkaufszahl des Artikels
- Preis→ Einkaufspreis des Artikels. Staffelpreise werden ebenfalls angezeigt
- Nachbestellen→ Vorschlag nachzubestellende Menge (orange → muss nachbestellt werden, da offene Kundenaufträge bedient werden müssen)

Bei der Berechnung gilt es folgendes zu beachten:

- Der Bestellvorschlag berücksichtigt alle offenen Kundenaufträge und Reservierungen. Kundenaufträge, die einige Zeit zurück liegen, werden also in die Berechnung mit einbezogen.
- Ebenso werden alle freigegebenen Bestellungen bei diesem Lieferanten beachtet.
- Nicht mehr benötigte Aufträge und Bestellungen sollten daher am Besten regelmäßig im System storniert werden.
- Die Bestellungen "In Bearbeitung" haben noch keine Bestellnummer und können deshalb jederzeit gelöscht werden.
- Ware auf einem Sperrlager wird nicht in der Berechnung der Spalte "Nachbestellen" berücksichtigt.