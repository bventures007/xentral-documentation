## Überblick

Mit der Artikelzuordnung legst du fest, welche Artikel zwischen Shop und Xentral synchronisiert werden. Du kannst einen Filter setzen, um die synchronisierten Artikel einzuschränken. Dies ist generell für die ersten Testläufe zu empfehlen, und im Livemodus dann, wenn in Xentral z. B. mehr Artikel enthalten sind, als du im Shop anbieten wirst.

[en-us]Du erreichst die Artikelzuordnung unter dem Pfad **Einstellungen > Verkaufen > Shopify Connector > Artikelzuordnung.**

![image-20240223-080827.png](https://help.xentral.com/hc/article_attachments/13054506939676)

## Erste Testläufe

Für die ersten Testläufe empfiehlt es sich, die Auswahl auf nur einen Artikel zu beschränken. Gib dazu als Filter z. B. **Artikel Nr. == NUMMER ** ein, wobei du für NUMMER eine Artikelnummer aus deinem Artikelstamm einsetzt. Aktualisiere die Auswahl durch Klicken auf **Neu laden**.

![image-20240223-080907.png](https://help.xentral.com/hc/article_attachments/13054521172892)

## Livemodus mit eingeschränkter Artikelauswahl

Für den Live-Modus kannst du die synchronisierten Artikel bei Bedarf über die Filterfunktion einschränken, z. B. wenn dein Xentral mehr Artikel enthält als du im Shop anbieten möchtest. Gib dazu die Filter deiner Wahl ein. Wie du die Filter korrekt nutzt, erklären wir im Abschnitt[Filternomenklatur](#UUID-6b8bcca3-4c4a-6238-ec33-6c996f16a655_UUID-cea99fc4-4ca0-d16b-7325-57c87180680c). Aktualisiere die Auswahl durch Klicken auf **Neu laden**.

![Artikelzuordnung_01a.png](https://help.xentral.com/hc/article_attachments/13054521237276)

## Filternomenklatur

Zum Filtern stehen dir vielfältige Möglichkeiten zur Verfügung.

![image-20240223-080935.png](https://help.xentral.com/hc/article_attachments/13054538238492)

(1)**Filterfeld **, bestehend aus ** Feldname Operator Filterwert**

- Beim Feldnamen kannst du verschiedene Felder aus Xentral nutzen. Verwende z. B. “Artikel (DE)”, um nach dem Artikelnamen zu filtern.
- Als Operatoren kannst du nachstehende nutzen.

| Operator | Funktion |
| --- | --- |
| == | ist gleich |
| > | größer als |
| >= | größer/gleich als |
| < | kleiner als |
| <= | kleiner/gleich als |
|!= | ist nicht |
| EXISTS | Wert ist ungleich ‘leer’ |

- Als Filterkritierium gibst du schließlich den gewünschten Filterwert an.

(2)**Verknüpfung** mehrerer Filter (UND / ODER)

(3) Hierarchisches **Verschachteln** von Filtern

(4)**Format** (z. B. Zahl, Text)

(5)**Zurücksetzen** eines Filterfelds

(6)**Löschen** einer Filterzeile

(7)**Anzeige****Filterbedingung**. Diesen Text kannst du kopieren und ihn als Filter in die Direkteingabe einfügen.

## Auf die Zielgerade!

Nur noch ein paar Schritte und du kannst deine Anbindung nutzen. Gehe nun in der Verwaltung auf[Workflows](https://xentral.atlassian.net/wiki/spaces/XM/pages/2741338277), um Details zu den synchronisierten Features zu konfigurieren.

![image-20240223-082832.png](https://help.xentral.com/hc/article_attachments/13054516093852)