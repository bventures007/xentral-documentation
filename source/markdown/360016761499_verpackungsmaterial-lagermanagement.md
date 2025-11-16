Mit der App **Verpackungsmaterial Lagermanagement** können Sie für eine bestimmte Menge an Positionen im Lieferschein Regeln definieren, wieviel Verpackungsmaterial jeweils automatisch mit aus dem Lager ausgebucht werden soll. Wenn Sie einen Überblick über die Verfügbarkeit Ihres Verpackungsmaterials behalten wollen, ohne diese in Stücklisten unterbringen zu müssen, ist dieses Modul eine gute Möglichkeit trotzdem einen Lagerabzug der Verpackungen zu gewährleisten.

## Übersicht

In der Livetabelle sehen Sie die bereits erstellten Regeln in einer **Übersicht** und können diese editieren oder neue Regeln anlegen.

Es können auch mehrere Verpackungsartikel für einen Lagerartikel ausgelagert werden. Für jeden Verpackungsartikel braucht man eine Verpackungsregel.

![packagingmaterialwarehouse_1.png](https://help.xentral.com/hc/article_attachments/13075231374236)

In diesem Beispiel würden die ersten beiden Einträge festlegen, dass je 6 Einheiten vom Artikel "Gehäuse", ein Faltkarton und pro 3 Einheiten nochmal ein Gummiband ausgebucht werden soll.

Der letzte Eintrag würde zudem festlegen, dass für jeden anderen Artikel (außer "Gehäuse") der ausgelagert wird, pro 10 Einheiten ebenfalls ein Gummiband ausgelagert werden soll. Die Ausbuchung des Verpackungsmaterials kann auf das eingestellte Projekt verknüpft werden.

## Verpackungs-Regeln hinzufügen/editieren

Mit der Schaltfläche **+NEU** können Sie neue Regeln hinzufügen. Im darauf erscheinenden Fenster sind folgende Felder auszufüllen:

- **Aktiv:** Nur aktive Regeln werden für den Lagerauszug ausgewertet
- **Projekt aus Lieferschein:** Das Projekt aus dem Lieferschein wird auch bei der Ausbuchung des Verpackungsartikels referenziert
- **Anzahl Teile von:** Ab dieser Menge des Hauptartikels (einzupackenden Artikels) gilt diese Regel - Mindestanzahl
- **Anzahl Teile bis:** Bis zu dieser Menge des Hauptartikels gilt diese Regel - Maximalanzahl
- **Für Artikel (optional):** Hauptartikel, für den die Verpackung mit ausgelagert werden soll (wird nichts angegeben, so wird die Verpackung für die Anzahl Teile jedes Artikels mit ausgelagert)
- **Artikel für Verpackung:** Der Verpackungsartikel, der mit ausgelagert werden soll
- **Menge Verpackungsmaterial:** Anzahl des Verpackungsartikels, welche ausgelagert werden soll
- **Bevorzugtes Verpackungslager:** Wenn Verpackungsmaterial auf mehreren Lägern liegt, wird zuerst aus diesem Lager ausgebucht
- **Projekt:** Beschränkung auf Projekt möglich - hier wird das Projekt aus dem Beleg ausgewertet

Mit den Schaltflächen **Editieren ** und**Löschen** können Sie die angelegten Verpackungsregeln ändern oder löschen.

## Beispiele für Verpackungsregeln

Menge an Positionen im Lieferschein: 1 - 10- Lagere 1 Karton mit den Maßen 20 x 40 aus (Artikelnummer 10000)

- Lagere 1 Transportfolie mit den Maßen 30 x 50 aus (Artikelnummer 10010)

Menge an Positionen im Lieferschein: 11 - 20- Lagere 1 Karton mit den Maßen 50 x 90 aus (Artikelnummer 10001)

- Lagere 2 Transportfolien mit den Maßen 30 x 50 aus (Artikelnummer 10010)

Menge an Positionen im Lieferschein: 21-30- Lagere 1 Karton mit den Maßen 50 x 90 aus (Artikelnummer 10001)

- Lagere 3 Transportfolien mit den Maßen 30 x 50 aus (Artikelnummer 10010)

...und so weiter.