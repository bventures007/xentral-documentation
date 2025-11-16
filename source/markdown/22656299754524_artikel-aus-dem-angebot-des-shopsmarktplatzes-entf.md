## Überblick

In diesem Know-How-Artikel erläutern wir dir, wie du vorgehen kannst, wenn ein Produkt nicht mehr im Shop/Marktplatz angeboten werden soll. Je nach Zielsetzung gibt es unterschiedliche Verfahren.

> **Anmerkung**
>
> Dieser Artikel baut auf den grundlegenden Kenntnissen über die Connect-Schnittstelle einschließlich deren Installation und Einrichtung auf. Falls du hierzu mehr Informationen benötigst, besuche die allgemeinen Artikel zur Schnittstellen-Einrichtung:
>
> - Shopify Connector
> - Shopware 6 Connector
> - Tradebyte Connector
> - WooCommerce Connector

Wenn du ein Produkt nicht mehr über den Shop/Marktplatz verkaufen möchtest, hast du grundsätzlich folgende Möglichkeiten:

- Artikel inaktiv setzen
- Lagerbestand auf Null setzen
- Artikel löschen

## Artikel inaktiv setzen

> **Tipp**
>
> Mit dieser Methode wird der Artikel im Shop/Marktplatz für Kunden nicht mehr angezeigt.

Um einen Artikel inaktiv zu setzen, gehe wie folgt vor:

1. Navigiere zu Verkaufen > Artikel und öffne ihn zum Bearbeiten.
1. Gehe zum Reiter Details > Online-Shop Optionen.
1. Setze den Haken bei Artikel inaktiv.
1. Klicke auf Speichern.

> **Anmerkung**
>
> Je nachdem, ob der Produktivmodus der Schnittstelle aktiviert ist oder nicht, wird die Änderung automatisch synchronisiert oder muss manuell übertragen werden:
>
> - Produktivmodus aktiv: Änderung wird automatisch an den Shop/Marktplatz übertragen.
> - Produktivmodus nicht aktiv: Stoße die Übertragung manuell über das Journal an: Systemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Journal > ReiterArtikel. Klicke in der Zeile des betreffenden Artikels aufArtikel synchronisieren.
>
> Um zu prüfen, ob der Produktivmodus aktiv ist, navigiere zuSystemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Zahnrad (Einstellungen).

## Lagerbestand auf Null setzen

> **Tipp**
>
> Diese Methode führt dazu, dass der Artikel im Shop/Marktplatz zwar angezeigt wird, aber nicht mehr bestellbar ist.

Folge diesen Schritten, um den Lagerbestand im Shop/Marktplatz auf Null zu setzen:

1. Navigiere zu Verkaufen > Artikel und öffne ihn zum Bearbeiten.
1. Gehe zum Reiter Details > Online-Shop Optionen.
1. Hake Restmenge (Abverkauf) an.
1. Trage in Pseudo Lagerzahl eine Null (0) ein.
1. Klicke auf Speichern.
1. Navigiere zu Systemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Workflows > Reiter Bestand.
1. Stelle sicher, dass Pseudo Lagerzahl statt echten Lagerzahlen verwenden im Abschnitt Lagerbestand berechnen aktiviert ist.
1. Navigiere zu Systemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Journal > Reiter Artikel.
1. Klicke in der Zeile des betreffenden Artikels auf Bestand synchronisieren.

> **Anmerkung**
>
> Alternativ zur Nutzung der Pseudo Lagerzahl kannst du den echten Bestand natürlich komplett auslagern oder an ein Lager umbuchen, das nicht mit dem Shop/Marktplatz verknüpft ist. Stelle in diesen Fällen sicher, dassRestmenge (Abverkauf)in denOnline-Shop Optionendes Artikels angehakt ist.

## Artikel löschen

### Achtung

Das Löschen eines Artikels ist nur möglich, wenn er in keinen Belegen enthalten ist.

Wir empfehlen grundsätzlich, Artikel nicht zu löschen, da dadurch wichtige Informationen wie Artikel-Historie und Verknüpfungen verloren gehen. Diese Methode eignet sich daher nur, wenn du einen Artikel aus Versehen oder testweise angelegt hast und diesen wieder entfernen möchtest.

1. Um einen Artikel zu löschen, navigiere zu Verkaufen > Artikel.
1. Klicke in der Artikel-Übersicht auf X in der Zeile des zu löschenden Artikels.
1. Bestätige den Löschvorgang mit OK.

> **Warnung**
>
> **Bei Nutzung von Fremdnummern:**
>
> Falls du mit Fremdnummern arbeitest, beachte, dass Einträge aus der Fremdnummern-Tabelle entfernt werden, wenn ein Artikel in Xentral gelöscht wird. Deshalb werden Artikel im Shop/Marktplatz bei aktiver Fremdnummern-Verknüpfung nicht automatisch gelöscht, wenn sie in Xentral gelöscht werden. In diesem Fall musst du die Löschung im Shop manuell vornehmen.
>
> Weitere Informationen zu Fremdnummern findest du in diesem Artikel:Fremdnummern in Xentral