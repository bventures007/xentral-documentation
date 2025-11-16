Bist du im E-Commerce tätig, bietest du deine Ware in einem Online-Shop, einem Markplatz oder in beiden an. Die beiden Vertriebsarten unterscheiden sich wie folgt:

Ein Online-Shop besteht aus deiner eigenen Webseite, die du nach deinen Bedürfnissen individualisieren kannst. Dies erlaubt dir das Kundenerlebnis besser zu steuern und dich von der Masse abzuheben. Im Hintergrund arbeitet ein Shopsystem wie Shopify oder Shopware, das deine Aufträge entgegennimmt und an Xentral weiterleitet.

Ein Marktplatz ist eine bestehende Plattform wie Amazon oder eBay, auf der du deine Artikel einstellen kannst. Aufgrund der hohen Nutzerzahlen dieser Plattformen, profitierst du von einer hohe Reichweite. Andererseits bist du von den Entscheidungen der Plattform abhängig und kannst deine Artikel nicht individuell präsentieren. Dies spart Zeit, macht es aber schwieriger deine eigene Marke zu etablieren.

[Online-Shops und Marktplätze](https://help.xentral.com/hc/articles/360016756799#UUID-9f183a72-7906-0ad5-3f24-f4eeabc42c07)sind über Schnittstellen mit Xentral verbunden. Diese können z.B. Aufträge importieren, die Lagerzahlen über alle Shops/ Marktplätze abgleichen und die Trackingnummer an den Shop zurückmelden.

> **Anmerkung**
>
> Die klassischen Shop-Schnittstellen in Xentral werden nach und nach durch neue Schnittstellen ersetzt. Du kannst die neuen Schnittstellen am Wort “Connector” erkennen, z.B. Shopify-Connector. Diese sind leichter anzubinden und bieten erweiterte Funktionalitäten. Hast du deinen Shop bereits über eine klassische Schnittstelle angebunden, kannst du diese leicht auf die neue Schnittstelle migrieren.

## Online-Shops und Marktplätze anbinden (klassisch)

Einen Shop oder Marktplatz bindest du über die klassische Schnittstelle folgendermaßen an:

1. Navigiere zu **Einstellungen > Verkaufen > Shops/ Marktplätze **. Klicke auf ** Verbindung hinzufügen**.
1. Wähle den Shop/ Marktplatz aus, den du anbinden möchtest.
1. Gib die Zugangsdaten deines Shops oder Marktplatzes an. Dieser Schritt unterscheidet sich je nachdem, was du anbinden möchtest. Du wirst zu den Einstellungen der Schnittstelle weitergeleitet.
1. Klicke auf **Verbindung prüfen**, um die korrekte Anbindung zu überprüfen. Hierbei werden keine Daten des Shops oder von Xentral übertragen, sondern nur geprüft, ob eine Verbindung möglich ist.
  War die Verbindung erfolgreich, dann fahre bitte mit der Anbindung fort. Tritt ein Fehler auf, dann prüfe bitte deine Zugangsdaten.

1. Wähle den Importmodus. Dieser bestimmt wie Aufträge von Xentral importiert werden:
  1. **Demo (zum Testen)**: Standardmäßig eingestellt. Wir empfehlen dir die Schnittstelle ausgiebig zu testen, bevor du in den Live-Betrieb wechselst. In diesem Modus wird der Auftragsstatus im Shop nicht verändert und keine Artikel und Lagerzahlen übertragen.
  1. **Manuell (mit Importzentrale)**: Importiert Aufträge nur, wenn du in deiner Schnittstelle auf der rechten Seite im ** Aktion **

-Menü auf ** Aufträge abholen** klickst. Der manuelle Import bietet dir die Möglichkeit deine Aufträge vor der Freigabe zu überprüfen. Dies ist besonders im B2B-Bereich wichtig, wenn du nur wenige, aber sehr wichtige Aufträge hast.
  1. **Automatisch (per Prozessstarter)**: Importiert deine Aufträge in regelmäßigen Intervallen automatisch. Den Intervall legst du im [Prozessstarter](https://help.xentral.com/hc/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a)** Shopimporter** fest. Dies ist der typische Modus für ein E-Commerce-Unternehmen im B2C-Bereich.

Die Rückmeldung der Trackingnummer an den Shop ist standardmäßig voreingestellt. Du findest die Option unter **Reiter Details > Unterreiter Einstellungen ** im Feld**Auftragsstatus rückmelden**.

Die Synchronisierung der Lagerzahlen findet statt, wenn die folgenden Voraussetzungen erfüllt sind:

- Der Prozessstarter Lagerzahlen (Shops) mit dem Parameter lagerzahlen ist aktiv.
- Im **Reiter Details > Unterreiter Online-Shop Optionen** eines Artikels sind die folgenden zwei Voraussetzungen erfüllt:
  - Die Option **Lagerzahlen Sync** ist aktiviert.
  - Der Artikel ist mit der Shop-Schnittstelle verknüpft. Klicke hierfür im Bereich **Online-Shops ** auf **Neuer Eintrag**.

> **Anmerkung**
>
> Bei einer neuen Schnittstelle kannst du die benötigten Features, wie die Synchronisierung der Lagerzahlen und Tracking direkt in der Schnittstelle steuern.

### Artikel aus Shop in Xentral zuordnen - Artikel Fremdnummern (klassisch)

[Fremdnummern](https://help.xentral.com/hc/articles/360016758199#UUID-be6a2725-3071-98cf-ad2e-1a9016c503cc)dienen bei der klassischen Schnittstelle dazu eine Verbindung zwischen einem Shop oder Markplatz und Xentral herzustellen. Es gibt drei Möglichkeiten deine Fremdnummern anzupassen:

- Im entsprechenden Artikel im Reiter **Fremdnummern** für einen einzelnen Artikel
- In der **Artikel Fremdnummern** App für die manuelle Bearbeitung aller Artikel
- In der Importzentrale für mehrere Artikel gleichzeitig über eine CSV-Datei

Bei der Zuordnung einer Fremdnummer sind drei Informationen wichtig: die Artikelnummer in Xentral, die Bezeichnung und die Fremdnummer (Artikelnummer im Shop). Die Bezeichnung unterscheidet sich je nach Shop:

| Shop/ Marktplatz | Art des Artikels | Bezeichnung |
| --- | --- | --- |
| Shopify | Artikel | shopifyproductid |
| Shopify | Variante | shopifyvariantid |
| WooCommerce | Artikel | SKU |
| Amazon | Artikel (Fulfillment by Amazon) | SKU_FBA |
| Amazon | Artikel (Fulfillment by Merchant) | SKU_FBM |
| eBay | Artikel | eBayListing |
| eBay | Variante | SKU, alternativ: Bestandseinheit |
| Kaufland | Artikel | apiunitid |

> **Anmerkung**
>
> Für Shopware werden keine Fremdnummern im Artikel benötigt. Die Artikelnummern/ SKUs in Xentral müssen jedoch identisch zu den Artikelnummern in Shopware sein.

## Online-Shops und Marktplätze anbinden (neue Schnittstelle)

Eine[neue Schnittstelle](https://help.xentral.com/document/preview/77557#UUID-01f05285-a5d1-500d-fad2-4521da1df80c)(z.B. Shopify oder WooCommerce) kannst du wie folgt anbinden:

1. Navigiere zu **Einstellungen > Verkaufen ** und wähle eine der neuen Schnittstellen aus, z.B. **Shopify Connector**.
1. Klicke auf **Install App**. Dieser Schritt ist nur bei der ersten Anbindung notwendig.
1. Klicke auf **+ Neue Integration**.
1. Gib der Schnittstelle einen Namen und lasse den Schalter unter **Livemodus aktivieren ** links (inaktiv). Dies erlaubt dir die Schnittstelle vor dem Go-live ausführlich zu testen. Klicke auf **Weiter**.
1. Erzeuge in deinem externen Shop ein Zugangstoken und gib anschließend die Zugangsdaten deines Shops in Xentral ein.
1. Klicke auf **Verbindung testen **, um die korrekte Anbindung zu überprüfen. Hierbei werden keine Daten des Shops oder von Xentral übertragen, sondern nur geprüft, ob eine Verbindung möglich ist. Klicke auf ** Weiter**.
1. Wähle aus, welche Daten zwischen Xentral und deinem Shop ausgetauscht werden sollen. Du kannst hier unter anderem entscheiden, ob du Lagerzahlen, Preise und Tracking synchronisieren möchtest. Klicke anschließend auf **Speichern**.

Die Schnittstelle wird nun angelegt. Dies dauert einen kurzen Moment. Im Anschluss kannst du über die Verwaltungsoberfläche **Daten migrieren **, ** Artikel zuordnen ** sowie die Details zum Datenaustausch unter **Workflows einstellen **. Test und Liveschaltung der Schnittstelle erfolgen ebenfalls unter ** Workflows**.