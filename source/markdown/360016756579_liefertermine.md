Mit dem extra Modul **Liefertermine ** sind in der Schnellvorschau, d.h. über das Mini-Detail des Auftrags, berechnete, potentielle Liefertermine einzusehen. Diese basieren auf den aktuellen Aufträgen, dem Lagerbestand und platzierten Bestellungen. Dadurch lässt sich auf einen Blick abschätzen, wann ein Auftrag, anhand von den Lieferterminen der versendeten Bestellungen, bedient werden kann. **Verkauf > Auftrag > Protokoll / Mini-Detail**

## Liefertermine im Auftrag

Im Mini-Detail in der Auftrags-Übersicht und im Protokoll innerhalb eines Auftrags werden die potentiellen Liefertermine angezeigt:

![deliverydates_1.png](https://help.xentral.com/hc/article_attachments/13075187209500)

### Erklärung der Liste

In der Spalte für potentielles Lieferdatum können drei Optionen auftauchen: **Verfügbar **, ** keine Bestellung verschickt ** oder ein konkreter Liefertermin **Verfügbar ** Wenn die Ware auf Lager ist und auch der verkäufliche Bestand für den Auftrag ausreichend ist, d.h. es gibt keine weiteren offenen Aufträge, die den Lagerbestand aufbrauchen würden, dann steht **verfügbar ** in der Auflistung. ** Keine Bestellung verschickt ** Die Ware ist nicht auf Lager und es gibt entweder keine Bestellungen dafür oder es gibt eine offene Bestellung, die aber noch nicht versendet wurde. Für die Versendung der Bestellung ist im einzelnen Auftrag im Drop-Down Menü des Aktionsmenüs **als Bestellung weiterführen ** auszuwählen. ** Konkreter Liefertermin**

Ein Liefertermin erscheint in der Auflistung im Auftrag, sobald Folgendes gewährleistet ist:

- Es ist nicht genug Ware auf Lager um den Auftrag zu bedienen und
- Es gibt eine versendete Bestellung, die den Bedarf des Auftrags bedienen kann
- Es gibt keine weiteren Aufträge, die von der Bestellung davor bedient werden müssen (FIFO Prinzip), oder falls doch kann die Bestellung alle offenen Aufträge auf einmal bedienen

## Reihenfolge der Liefertermine

Die Reihenfolge, nach der xentral die Liefertermine bestimmt, ist wie folgt:

1. Die Lieferschein-Positionen, die im Modul **Bestellung ** Reiter **Details ** Unterreiter**Positionen** eingesehen werden können, sind der erste ausschlaggebende Wert:
1. Das bestätigte Lieferdatum der Bestellung ist der zweite Punkt in der Reihenfolge.
1. Sind Punkt 1 und 2 nicht befüllt, wird der Wunschliefertermin der Bestellung herangezogen: