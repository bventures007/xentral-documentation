Fremdnummern ermöglichen es, Artikel in Xentral eindeutig mit abweichenden Nummern aus Shops, Marktplätzen oder anderen Systemen zu verknüpfen – und sind damit ein zentrales Werkzeug für saubere Prozesse im Multi-Channel-Vertrieb, der Logistik und bei Systemmigrationen.

## Fremdnummern – Was ist das und wozu werden sie benötigt?

**Fremdnummern** sind alternative Artikelnummern, die du in Xentral einem bestehenden Artikel zuordnen kannst, um ihn in externen Systemen wie Online-Shops, Marktplätzen oder bei Kunden eindeutig zu identifizieren. Sie dienen als Bindeglied zwischen der internen Artikelstruktur in Xentral und der individuellen Nummernlogik externer Systeme.

In der Praxis kommen **Fremdnummern ** immer dann zum Einsatz, wenn ein Artikel in einem Fremdsystem unter einer anderen Nummer geführt wird – sei es eine**Amazon-SKU **, eine ** Shopify-Artikelnummer **, ein ** EAN-Code **oder die ** Kunden-Artikelnummer**eines Großkunden. Durch das Mapping dieser Fremdnummer auf den internen Artikel stellst du sicher, dass alle Prozesse – vom Import über den Lagerabgleich bis hin zur Kommissionierung – korrekt ablaufen.

## Wann ist der Einsatz von Fremdnummern sinnvoll?

Fremdnummern sind ein leistungsfähiges Werkzeug, sollten aber gezielt und mit klarer Strategie eingesetzt werden. Du solltest sie pflegen, wenn:

- du Artikel über **mehrere Kanäle ** verkaufst und **jeder Kanal eigene Nummern** verwendet (z. B. Shopify, WooCommerce, Amazon),
- du **Marktplätze wie Amazon oder eBay ** anbinden möchtest, bei denen eine **spezifische SKU** erforderlich ist,
- du **Großkunden ** hast, die bei Bestellungen **eigene Artikelnummern** verwenden,
- du in Logistikprozessen mit **wechselnden EANs oder Barcodes ** arbeitest, die sich von der Xentral-internen Nummer unterscheiden (**Hinweis**: eine eindeutige EAN kannst du im Artikel fest hinterlegen. In diesem Fall benötigst du keine Fremdnummer).

### Achtung **Nicht erforderlich sind Fremdnummern **, wenn du nur mit einem Shopsystem arbeitest und alle Artikelnummern zentral und konsistent verwaltest. In diesem Fall ist es besser, mit identischen Artikelnummern in allen Systemen zu arbeiten, um Pflegeaufwand zu vermeiden. ** Kurz:**

-** Du nutzt nur einen Shop und steuerst alles zentral**: Wenn du volle Kontrolle über alle Artikelnummern hast, reicht eine konsistente Nummer in allen Systemen.
- **Artikelnummern in Shop, Xentral und Logistik sind identisch**: Kein Mapping nötig → keine Fremdnummer erforderlich.

## Warum nicht überall dieselbe Artikelnummer verwenden?

Theoretisch wäre es wünschenswert, überall die gleiche Artikelnummer zu verwenden. In der Praxis scheitert das oft an folgenden Faktoren:

- **Technische Einschränkungen**: Shopsysteme wie Shopify oder Marktplätze wie Amazon erlauben nur bestimmte Formate, keine Leerzeichen oder Sonderzeichen.
- **Variantenlogik**: Variantenartikel werden in Xentral, Shops oder auf Amazon oft unterschiedlich abgebildet.
- **Externe Anforderungen**: Kunden oder Marktplätze bestehen auf eigenen SKUs oder Bezeichnungen.
- **EANs oder Barcodes**: Diese weichen als Produktbeschriftungen häufig von der Artikelnummer ab, sind aber relevant für die Logistikprozesse - um gescannt zu werden.

Die Lösung ist eine saubere Trennung: In Xentral führst du eine zentrale Artikelnummer, und je nach Bedarf hinterlegst du system- oder kundenspezifische Fremdnummern.

> **Anmerkung**
>
> Die korrekte Pflege von Fremdnummern ist entscheidend, um Überschneidungen, Verwechslungen oder fehlerhafte Bestandsbuchungen zu vermeiden. Besonders bei automatisierten Integrationen, wie der Anbindung an Amazon, ist eine fehlerfreie Fremdnummernpflege oft Voraussetzung für einen reibungslosen Betrieb und die fehlerfreie Verarbeitung von Bestellungen.

## Typische Anwendungsfälle für Fremdnummern

Fremdnummern helfen dir dabei, Artikel in Xentral korrekt zuzuordnen, auch wenn diese in anderen Systemen unter abweichenden Nummern geführt werden. Sie sind besonders dann sinnvoll, wenn du mit mehreren Vertriebskanälen, Lieferanten oder Länderstrukturen arbeitest.

1. **Shops und Marktplätze mit eigenen Nummern**: Viele Shopsysteme (z. B. Shopify, WooCommerce) und Marktplätze (z. B. Amazon, eBay) verwenden eigene Artikelnummern oder SKU-Formate. Damit Xentral Bestellungen oder Lagerabgleiche korrekt zuordnen kann, pflegst du diese Nummern als Fremdnummern.
1. **Vermeidung ständiger Umetikettierung bei wechselnden Nummern**: Wenn du Produkte vertreibst, bei denen sich die Kennzeichnung oder SKU regelmäßig ändert (z. B. bei Herstellerupdates, saisonalen Varianten oder durch externe Anforderungen), kannst du alle Nummern als Fremdnummern hinterlegen – so musst du nicht jedes Mal neu etikettieren.
1. **Wiederverkäufer mit Lieferantenetiketten**: Beziehst du Artikel von Herstellern oder Großhändlern, die ihre eigenen Nummern auf die Verpackung drucken, kannst du diese als Fremdnummern mit Lieferantenbezug hinterlegen. Das erspart dir das Umlabeln und ermöglicht trotzdem eine korrekte Zuordnung in Xentral – z. B. beim Scannen im Warenausgang.
1. **Vertrieb ins Ausland mit landesspezifischen Nummern**: Wenn du denselben Artikel in unterschiedlichen Ländern unter anderen Nummern vertreibst, kannst du die jeweiligen länderspezifischen Artikelnummern als Fremdnummern pflegen. So brauchst du nur einen Artikel im ERP, behältst aber die Flexibilität für regionale Anforderungen (z. B. Frankreich: andere SKU, andere Sprache, andere Verpackung).
1. Migration von einem Altsystem: Bei einem ERP-Wechsel kann es sinnvoll sein, die Artikelnummern aus dem vorherigen System als archivierte Fremdnummern zu erhalten. Lege z. B. ein Projekt oder einen Shop „Altsystem“ an und pflege dort alle alten Nummern als Fremdnummern weiter – für Nachvollziehbarkeit bei Retouren, Servicefällen oder Altbeständen.

## Fremdnummern im Shop

Im Shop erfolgt die Artikelzuordnung standardmäßig über die SKU. Wenn diese von der internen Artikelnummer in Xentral abweicht, wird die Zuordnung über die gepflegte Fremdnummer gesteuert.

- Die im Shop verwendete SKU stimmt nicht mit der internen Artikelnummer überein, dann sorgt die gepflegte Fremdnummer für die eindeutige Zuordnung.
- Dabei spielt die **Bezeichnung ** beim Anlegen der Fremdnummer eine **zentrale Rolle**, insbesondere in Kombination mit dem angebundenen Shop-Connector (Connect).

Die Fremdnummer wird im Modul „**Artikel Fremdnummern**“ gepflegt s.o.

- **Artikel**: Der in Xentral geführte Artikel, dem die Fremdnummer zugeordnet wird.
- **Fremdnummer**: Die externe Artikelnummer aus dem Shop oder Marktplatz (z. B. SKU).
- **Shop**: Die Shop-ID, über die die Fremdnummer dem richtigen Kanal zugewiesen wird.
- **Bezeichnung **: Ein frei wählbarer Kennzeichner, z. B. ** sku, ean, lieferantennr.**

Im Shop-Connector muss diese Bezeichnung explizit konfiguriert werden:

- Aktiviere im Connector die Option „**Fremdnummern verwenden**“.
- Trage unter „**Bezeichnung**“ exakt denselben Begriff ein, der in der Fremdnummer gepflegt wurde (Groß-/Kleinschreibung beachten).
- Nur wenn Bezeichnung und Fremdnummer übereinstimmen, erkennt Xentral beim **Bestellimport ** oder **Artikelabgleich** die richtige Zuordnung.

### Achtung

Der Einsatz der **Bezeichnung ** ist**nicht optional, sondern notwendig**, da:

- Du pro Artikel und Shop **mehrere Fremdnummern** pflegen kannst.
- Die **Bezeichnung ** als **technischer Selektor** dient, um zwischen verschiedenen Fremdnummernarten zu unterscheiden.
- Ohne diese Angabe keine eindeutige Auswahl möglich ist – selbst bei nur einer Fremdnummer.

Wichtig für die Praxis:

- Bezeichnungen wie **sku, ean, lieferant_sku** sind üblich – wähle einen Begriff, der dem Zweck der Nummer entspricht.
- Die Bezeichnung muss **identisch in Fremdnummer und Connector** gepflegt sein – sonst findet keine Verknüpfung statt.
- Nutze verschiedene Bezeichnungen, wenn du z. B. eine **SKU und zusätzlich eine EAN** pflegen möchtest.
- Die Bezeichnung ist unabhängig vom Shopnamen – sie ermöglicht zusätzliche Trennung **innerhalb eines Shops**.

So kannst du gezielt steuern, welche Fremdnummer in welchem Kontext gilt, und behältst gleichzeitig die Flexibilität, mehrere externe Nummern für denselben Artikel systematisch zu verwalten.

Mehr dazu findest du z.B. im Artikel[Shopware6 - Verarbeitung von Fremdnummern (Connect)](https://help.xentral.com/hc/de/articles/14528064061596-Shopware6-Connector-Einstellungen-anpassen#UUID-6d4dffad-8633-5d25-a378-9864446787dc_UUID-fbf54a42-e03c-1225-128c-5c20e00c366b).

## Fremdnummern in Xentral anlegen

Du kannst Fremdnummern auf zwei Arten in Xentral anlegen – manuell oder per Import. Beide Wege ermöglichen dir eine eindeutige Zuordnung.

> **Warnung**
>
> Verwende **jede Fremdnummer nur einmal** (pro Shop) – Doppelverwendungen oder fehlerhafte Zuordnungen führen zu Bestellimportfehlern und falscher Lagerbuchung.

### Anlage über das Modul: Artikel Fremdnummern

Diese Methode eignet sich, wenn du mehrere Fremdnummern schnell pflegen möchtest.

**Schritte: **

1. Navigiere über die Smart-Search zu '** Artikel Fremdnummern **' oder verwende alternativ den Pfad: ** Appstore > Stammdaten > Artikel Fremdnummern**.
1. Klicke auf **+NEU**.
1. Wähle den gewünschten **Artikel** über die Suche aus.
1. Gib die **Fremdnummer** ein (z. B. Amazon SKU, Kundennummer, EAN).
1. Wähle den zugehörigen Kanal/ **Shop** aus der Auswahlliste.
1. Optional: Aktiviere „**Barcodescanner **“, wenn die Nummer im Versand gescannt werden soll. Setze „** Aktiv**“, um die Nummer sofort zu nutzen.
1. Klicke auf **Speichern**. Die Fremdnummer ist nun im System verfügbar und kann in Prozessen wie Bestellung, Versand oder Import verwendet werden.

### Anlage im Artikel direkt

Diese Variante eignet sich, wenn du gezielt an einem bestimmten Artikel arbeitest.

**Schritte: **

1. Öffne:** Verkauf > Artikel > Artikel öffnen >** Tab: ** Fremdnummern **

1. Gib die **Bezeichnung** ein (z. B. SKU, EAN, Kunden-ID)
1. Trage die **Fremdnummer** ein.
1. Wähle den zugehörigen Kanal/ **Shop** aus der Auswahlliste.
1. Aktiviere bei Bedarf die **Barcodescanner**

-Option, wenn die Nummer im Versand gescannt werden soll.
1. Setze „**Aktiv**“, um die Nummer sofort zu nutzen.
1. Klicke auf **Speichern**. Die Fremdnummer ist nun im System verfügbar und kann in Prozessen wie Bestellung, Versand oder Import verwendet werden.

### Import von Fremdnummern (Massenpflege)

Für große Datenmengen steht dir ein Import zur Verfügung.

**Schritte: **

1. Gehe zu:** Stammdaten > Import/Export Zentrale > Stammdaten Import**.
1. Wähle die Vorlage **01 J - Shopzuordnung mit Fremdnummern**.
1. Lade deine vorbereitete CSV-Datei hoch: CSV-Datei auswählen und UTF-8 als Zeichencodierung verwenden. Klicke auf **CSV jetzt heraufladen**.
1. Stelle sicher, dass '**fremdnummerX_shopid**' korrekt befüllt ist.
1. Führe den Import aus: Prüfe **Vorschau ** und klicke auf **Importieren**.

> **Anmerkung**
>
> **Hinweis**
>
> **fremdnummerX_shopid** Fremdnummer für Shop mit ID shopid
>
> **fremdnummerbezeichnungX_shopid** Optionale Bezeichnung (z. B. SKU, EAN)

> **Anmerkung**
>
> Du kannst bis zu 40 Fremdnummern pro Artikel importieren, jeweils mit zugeordneter Shop-ID. Die Shop-IDs findest du in der Übersicht aller Online Shops.

> **Anmerkung**
>
> **Hinweis**
>
> Manuelle Einrichtung der Importvorlage: Shopzuordnung mit Fremdnummern:
>
> **Einstellungen:**
>
> Name: 01 J - Shopzuordnung mit Fremdnummern (nach Artikelnummer)
>
> Ziel: Artikel (min. Angabe: nummer oder name_de)
>
> CSV Daten ab Zeile: 2
>
> CSV Trennzeichen:;
>
> CSV Maskierung: " (Anführungszeichen)
>
> Auswahl Charset: UTF-8
>
> **CSV-Felder:**
>
> 1:nummer;
> 2:fremdnummer_1;
> 3:fremdnummerbezeichnung_1;
> 4:shop_1;
> 5:aktiv_1;
> 6:fremdnummer_2;
> 7:fremdnummerbezeichnung_2;
> 8:shop_2;
> 9:aktiv_2;
>
> **Hinweis**: Ersetze die Ziffern im Feldnamen (_1, _2) jeweils mit der Shop-ID, für die die Fremdnummer gelten soll (z. B. fremdnummer_4 für Shop-ID 4). Die Shop-IDs findest du unter Administration > Shop Schnittstelle > Übersicht.
>
> Damit lassen sich Fremdnummern für mehrere Shops gleichzeitig importieren – jeweils mit zugehöriger Bezeichnung und Aktiv-Status.

### Fremdnummern scanbar machen

Du kannst jede Fremdnummer so konfigurieren, **dass sie in Logistikprozessen gescannt werden kann**– z. B. im Versandzentrum beim Packen oder in der Wareneingangskontrolle.

Aktiviere dafür die Option „**Barcodescanner**“ in der Fremdnummer-Verwaltung. Xentral berücksichtigt dann diese Nummer beim Scannen automatisch – auch wenn sie von der internen Artikelnummer abweicht.

> **Anmerkung**
>
> **Hinweis**
>
> **Beispiel:**
>
> Ein Lieferantetikett zeigt die Nummer 'EAN-4001234567890', dein interner Artikel heißt 'TSHIRT001'. Wird die EAN als scanbare Fremdnummer hinterlegt, erkennt Xentral beim Scan im Versandprozess trotzdem den richtigen Artikel - auch wenn im Artikel eine weitere EAN gepflegt ist.

## Verwendung von Fremdnummern in der Praxis

Fremdnummern kommen in Xentral überall dort zum Einsatz, wo Artikel systemübergreifend erkannt und korrekt zugeordnet werden müssen – etwa beim Import, im Versand oder bei kundenspezifischen Bestellungen.

### Artikelimport aus Shops oder Marktplätzen (Fremdnummern)

Wenn Artikel aus einem Shop oder Marktplatz importiert werden, gleicht Xentral automatisch die Fremdnummern mit vorhandenen Artikeln ab. Stimmen die Nummern überein, wird der Artikel korrekt zugeordnet. Gibt es keine passende Fremdnummer, kann es zu fehlerhaften Zuordnungen oder Dubletten kommen.

### Logistik und Versand (Fremdnummern)

Im Versandzentrum können Mitarbeitende Artikel anhand der Fremdnummer scannen – z. B. per EAN oder Amazon SKU – wenn diese als „scannbar“ markiert ist. Dafür muss zusätzlich im Projekt die Option „**Shop-Fremdnummern scannen erlauben **“ aktiviert sein. ** Praxisnutzen**: Auch wenn das Etikett keine interne Xentral-Artikelnummer zeigt, wird der Artikel korrekt erkannt.

### Kundenindividuelle Artikelnummern (Fremdnummern)

Großkunden arbeiten häufig mit eigenen Artikelnummern. Wenn diese als Fremdnummer gepflegt sind, kannst du eingehende Bestellungen per API, EDI oder CSV verarbeiten und dennoch intern deine Standardartikelstruktur nutzen.

## Warum braucht Amazon eigene Fremdnummern?

Amazon ist ein eigenständiges System mit folgenden Besonderheiten:

- Du definierst deine SKU beim Hochladen eines Artikels ins Seller Central – diese SKU bleibt dauerhaft für diesen Artikel bestehen.
- Amazon-SKUs sind kanal- und lagerabhängig, d. h. für FBA und FBM brauchst du separate SKUs, auch wenn es sich um denselben physischen Artikel handelt.
- Amazon verwendet die SKU zur internen Steuerung, zur API-Kommunikation und zur Rückmeldung von Bestellungen.
- Die SKU darf nicht nachträglich geändert werden – bei Änderungen musst du den Artikel neu anlegen.

> **Anmerkung**
>
> Wann du mehrere Amazon-Fremdnummern brauchst, typische Szenarien:
>
> - Du verkaufst denselben Artikel als FBA und FBM → zwei Fremdnummern mit unterschiedlichen SKUs.
> - Du nutzt Pan-EU oder mehrere Amazon-Marktplätze → unterschiedliche SKUs pro Land empfohlen.
> - Du hast mehrere Listings für Varianten oder Bundles → jede Variante hat eigene SKU.

> **Tipp**
>
> So arbeitest du in Xentral damit:
>
> - Pflege die Amazon-SKUs im Artikel als Fremdnummern mit Shop-Zuweisung „Amazon“.
> - Verwende für FBA und FBM je eine eigene Fremdnummer.
> - Nutze die Importfunktion bei vielen Artikeln (Stammdaten Import Vorlage 01 J)
> - Aktiviere bei Bedarf die Barcodescanner-Funktion, wenn du Amazon-SKUs auch im Warenausgang verwendest (z. B. bei Amazon FBM mit eigenem Lager)

> **Anmerkung**
>
> Automatisierung über die Amazon-Schnittstelle:
>
> Wenn du die **Amazon-Schnittstelle von Xentral nutzt, können SKU-Zuordnungen automatisiert entstehen – insbesondere bei Bestellimporten**. Dennoch empfiehlt es sich, Fremdnummern proaktiv zu pflegen, um spätere Fehlerquellen und manuelle Nachbearbeitung zu vermeiden.

## Kann ich die Amazon SKU auch im Shop verwenden?

Technisch ja, strategisch meistens nein.

Amazon verwendet häufig sehr strukturierte, marktplatzbezogene SKUs (z. B. SKU_FBA_RED_XL). Diese machen im Shop wenig Sinn – vor allem wegen SEO, Benutzerfreundlichkeit und Konsistenz im Sortiment.

> **Tipp**
>
> Pflege die Amazon-SKU als Fremdnummer, aber verwende im Shop sprechende, markenkonforme Artikelnummern.

## Welche Nummern hat ein Shopify-Shop?

- Shopify SKU: Diese wird in Shopify gepflegt, ist aber nicht systemisch erforderlich – sie dient nur der Organisation.
- Handle / Slug / URL-Name: Der sichtbare Produktpfad ist oft eine andere ID.
- Produkt-ID: Interne Shopify-ID, nicht sichtbar, aber über API verfügbar.

> **Tipp**
>
> Die Shopify-SKU kann mit der Xentral-Artikelnummer identisch sein – muss aber nicht. Falls abweichend → als Fremdnummer pflegen.