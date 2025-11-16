## Überblick

Mit der Artikelzuordnung legst du fest, welche Artikel zwischenShopund Xentral synchronisiert werden sollen. Du kannst einen Filter setzen, um die synchronisierten Artikel einzuschränken. Dies ist generell für die ersten Testläufe zu empfehlen, und im Produktivmodus dann, wenn in Xentral z.B. mehr Artikel enthalten sind, als du im Shop/Marktplatz anbieten willst.

> **Anmerkung**
>
> Wenn du keinen Filter definierst, werden alle Artikel synchronisiert.

Du erreichst die Artikelzuordnung unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze >Shopify Connector > Artikelzuordnung**.

![image-20240223-080827.png](https://help.xentral.com/hc/article_attachments/15365049034524)

## Erste Testläufe

Für die ersten Testläufe empfiehlt es sich, die Auswahl auf nur einen Artikel zu beschränken. Gib dazu als Filter z.B. **Artikel Nr. == NUMMER ** ein, wobei du für NUMMER eine Artikelnummer aus deinem Artikelstamm einsetzt. Klicke auf **Filter anwenden**…

![connect_assignproduct_testrun1.png](https://help.xentral.com/hc/article_attachments/15365049090588)

… und anschließend auf **Artikelliste aufbauen**:

![connect_assignproduct_testrun2.png](https://help.xentral.com/hc/article_attachments/15365049168796)

Der Status des Imports wird dir anschließend oben im Fenster angezeigt:

![connect_assignproduct_testrun3.png](https://help.xentral.com/hc/article_attachments/15365038931612)

## Produktivmodus

Für den Produktivmodus kannst du die synchronisierten Artikel bei Bedarf über die Filterfunktion einschränken, z. B. wenn dein Xentral mehr Artikel enthält als du im Shop/Marktplatz anbieten möchtest. Gib dazu die Filter deiner Wahl ein. Wie du die Filter korrekt nutzt, erklären wir im Abschnitt[Filternomenklatur](#UUID-6b6b31e2-79dc-2826-dd07-8cf4e4976109_UUID-cea99fc4-4ca0-d16b-7325-57c87180680c). Aktualisiere die Auswahl durch Klicken auf **Filter anwenden**...

![connect_assignitems_livemode1.png](https://help.xentral.com/hc/article_attachments/15365049334940)

… und anschließend auf **Artikelliste aufbauen**:

![connect_assignitems_livemode2.png](https://help.xentral.com/hc/article_attachments/15365017900188)

Der Status des Imports wird dir anschließend oben im Fenster angezeigt:

![connect_assignitems_livemode3.png](https://help.xentral.com/hc/article_attachments/15365033261852)

## Filternomenklatur

Zum Filtern stehen dir vielfältige Möglichkeiten zur Verfügung.

![connect_filternomenclature_numberedoverview.png](https://help.xentral.com/hc/article_attachments/18670826121244)

(1)**Filterfeld **, bestehend aus ** Feldname Operator Filterwert**

- Beim Feldnamen kannst du verschiedene Felder aus Xentral nutzen. Verwende z. B. “Artikel (DE)”, um nach dem Artikelnamen zu filtern.
- Als Operatoren kannst du nachstehende nutzen:

| == | ist gleich | Text, Zahl |
| --- | --- | --- |
|!= | ist nicht | Text, Zahl |
| > | größer als | Zahl |
| < | kleiner als | Zahl |
| IN | in einer Liste enthalten | Liste |
| NOT IN | nicht in einer Liste enthalten | Liste |
| **Operator **|** Funktion **|** Zu wählendes Format** |

- Als Filterkritierium gibst du schließlich den gewünschten Filterwert an.

(2) UND-**Verknüpfung** mehrerer Filter

(3)**Format** (z.B. Zahl, Text)

(4)**Zurücksetzen** eines Filterfelds

(5)**Löschen** einer Filterzeile

(6)**Anzeige****Filterbedingung ** (7)** Filter-Historie**: Hier siehst du, wieviele Artikel die Filterkriterien ab dem jeweiligen Aktivierungsdatum erfüllt haben.

> **Tipp**
>
> Um eine Auswahl aus mehreren Artikelnummern aufzuführen, kombiniere den Operator IN zusammen mit dem Format “Liste”:
>
> Artikel Nr. IN 100001,100005,100010

## Auf die Zielgerade!

Nur noch ein paar Schritte und du kannst deine Anbindung nutzen. Gehe nun in der Verwaltung auf[Workflows](https://help.xentral.com/hc/de/articles/13235060220444#UUID-55e1cf94-dd5f-eb68-4337-cabda5e7ee49), um Details zu den synchronisierten Features zu konfigurieren.

![image-20240223-082832.png](https://help.xentral.com/hc/article_attachments/15365054806300)

## Manuelle Anpassung der Artikelzuordnung für einzelne Artikel

Wenn du nachträglich einzelne Artikel manuell in die Artikelzuordnung hinzufügen möchtest, kannst du die Funktion **Filter für einzelne Artikel anwenden** nutzen. Dies ist zum Beispiel sinnvoll, wenn du Artikel angelegt hast, bei denen die Filter-Kriterien beim ersten Speichern noch nicht gesetzt waren und du nicht bis zum nächsten automatischen Lauf (über Nacht) warten möchtest.

Gehe dazu wie folgt vor:

1. Füge die Filter-Kriterien den jeweiligen Artikeln zu und speichere die Artikel.
1. Klicke auf die Funktion **Filter für einzelne Artikel anwenden**.
1. Trage die Artikelnummern der neu hinzuzufügenden Artikel kommagetrennt ein und klicke auf weiter.
1. Die Artikel werden nun manuell übertragen.

Durch den Einzelfilter erreichst du, dass betroffene Artikel manuell in die Artikelzuordnung aufgenommen werden, ohne nochmal die gesamte Filterliste durchlaufen lassen zu müssen und schonst damit die Performance deines Systems.

> **Warnung**
>
> Im umgekehrten Fall, wenn du einen Artikel aus dem Marktplatz entfernen möchtest, genügt es nicht, ihn nur aus der Artikelzuordnung herauszufiltern! Der Filter in der Artikelzuordnung hat nur Einfluss auf die Aktualisierung der Daten. Entfernst du also einen Artikel aus dem Filter, bleibt dieser Artikel zwar im Marktplatz aufgeführt, erhält aber keine aktuellen Daten mehr aus Xentral. Wenn du einen Artikel aus dem Marktplatz entfernen möchtest, öffne den Artikelstamm, gehe zum ReiterDetails > Online-Shop Optionenund setze dort den Haken beiArtikel inaktiv.