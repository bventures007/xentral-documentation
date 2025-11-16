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

Das Modul **Lagerstückliste ** ermöglicht es Stücklisten und Lager anzugeben, bei denen die Stückliste in Belegen explodieren soll. **Hintergrund**: Bei einer normalen Stückliste sieht man in den Beleg-Positionen lediglich den Hauptartikel. Mit dieser App kann man dies umgehen und alle Unterstücklistenartikel für die eingestellten Bedingungen anzeigen lassen.

## Übersicht

Mit dem **+NEU** Button kann man einen neuen Artikel zur Liste hinzufügen.

### Individueller Stücklistenartikel mit einzelnem Lager

Wenn man die Stücklistenartikel und entsprechende Lager einzeln angeben will, füllt man sowohl das Artikelfeld, als auch das Lagerfeld aus.

![InventoryBillOfMaterials1.png](https://help.xentral.com/hc/article_attachments/5080760596508)

Im Beispiel oben bedeutet das: Wenn ich im Auftrag als bevorzugtes Lager "Hauptlager" eingebe (und speichere) und danach die Stückliste 100003 einfüge, wird diese in den Positionen explodieren.

> **Anmerkung**
>
> Wenn der Haken **sofort im Auftrag explodieren** nicht gesetzt ist, explodiert die Stückliste nur im weitergeführten Lieferschein.

### Individueller Stücklistenartikel mit allen Lagern

Soll ein einzelner Stücklistenartikel immer explodieren, füllt man nur das Artikelfeld aus und lässt das Lagerfeld leer.

### Alle Stücklistenartikel mit individuellem Lager

Wenn alle Stücklistenartikel bei nur einem einzelnem Lager explodieren soll, füllt man nur das Lagerfeld aus und lässt das Artikelfeld leer.

### Bevorzugtes Lager im Auftrag

Das Feld **Bevorzugtes Lager ** befindet sich in der Auftragsmaske (**Verkauf > Auftrag**).

> **Anmerkung**
>
> Erst bevorzugtes Lager im Auftrag speichern, danach die Stücklisten einfügen.