Die eBay App bietet viele verschiedene Features - von einer Übersicht aller Auktionen über diverse Einstellungen zu Rahmenbedingungen und Ähnlichem bis hin zu Lagerbestandsinformationen. Die eBay App findest du im App Center zusammen mit dem eBay Importer. Unter Umständen ist die App für die Verwendung des Importers erforderlich, in jeden Fall bietet sie aber nützliche Features für dessen Verwendung.

App Center > Shop Schnittstelle > Ebay App

## Der Reiter Listings

Um alle aktiven Artikel zu sehen, öffne den ReiterListings. Hier findest du alle laufenden Listings auf einen Blick. Du kannst Artikel manuell zuweisen, indem du auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/18590766452252)

klickst.

> **Wichtig**
>
> Die Lagersynchronisierung erfolgt nur für zugewiesene Artikel! Fehlt eine Zuweisung, erfolgt für diesen Artikel keine Lagersynchronisierung.

![eBay-App-2.png](https://help.xentral.com/hc/article_attachments/18590747180572)

## Der Reiter Übersicht

Im ReiterÜbersichtfindest du eine Übersicht aller Auktionsartikel, die Auflistung der Gebühren für die Artikel im Shop und Reservierungen.

### Auktionsübersicht

Hier wird die Auktionsübersicht angezeigt, das heißt eine Übersicht aller Artikel, die im Shop zur Auktion oder zum Verkauf stehen. Dabei werden auch bereits verkaufte und ausgelaufene Artikel mit Bestand angezeigt.

Du kannst die Filter verwenden, z.B.Nur abgelaufene Auktionen anzeigen, um die Anzeige der Auktionen einzugrenzen.

Mit einem Klick aufAnzeige aktualisierenlädst du den aktuellen Stand der Übersicht. Klicke auf der Seite unten aufAuktionen aktualisieren/ neu einstellen, um bereits ausgelaufene Artikel neu einzustellen.

![eBay-App-4.png](https://help.xentral.com/hc/article_attachments/18590747181724)

### Gebühren

Im untergeordneten ReiterGebührenwerden dir die Gebühren für die jeweils eingestellten Artikel angezeigt. Die wichtigsten Gebühren sind die Angebotsgebühr, die Verkaufsprovision, die Anzeigengebühr und die Gebühren für Zusatzoptionen.

![eBay-App-5.png](https://help.xentral.com/hc/article_attachments/18590766458652)

### Reservierungen

Käufer können bei eBay eine Bestellung abschließen, ohne dabei jedoch direkt zu bezahlen oder die Lieferadresse einzugeben. Der Kauf ist trotzdem getätigt und die Artikel sind für den Käufer reserviert. Solche Bestellungen werden im ReiterReservierungenin der eBay App angezeigt. Dabei wird die gekaufte Menge reserviert, damit es nicht zu Überverkäufen eines Artikels kommt.

## Der Reiter Einstellungen

Im ReiterEinstellungenkannst du Templates (d.h. Vorlagen) anlegen, Rahmenbedingungen sowie Zuordnungen definieren, Versanddienstleister zuweisen und Kategorien im eBay-Shop aktualisieren.

Verkaufst du über mehrere eBay-Shops, kannst du in allen untergeordneten Reitern des ReitersEinstellungen(mit Ausnahme des ReitersTemplates) über das Dropdown-MenüImporterschnittstelleden gewünschten Shop auswählen.

### Templates

Du kannst neue Vorlagen erstellen, indem du auf+Neues Template anlegenklickst. Das Anlageformular für Vorlagen wird angezeigt.

![eBay-App-7.png](https://help.xentral.com/hc/article_attachments/18590747187996)

Gib den HTML-Code der Vorlage in das Textfeld ein. Unten im Formular werden dir mögliche Wildcard-Felder angezeigt. Diese werden bei der Übertragung mit den entsprechenden Werten aus den Artikeldaten ersetzt. XX am Ende eines Wildcard-Feldes kann für die Initialisierung verwendet werden, z.B. kannst du das Länderkürzel (z.B. FR) statt XX einsetzen. Dadurch wird das entsprechende Wildcard-Feld auf Französisch übersetzt (Voraussetzung ist, dass der französische Wert hinterlegt ist). Alternativ kannst du das XX beibehalten, dann wird automatisch die Sprache genutzt, die im eBay-Listing eingestellt ist.

Du kannst folgende **Wildcards** verwenden:

{EAN}, {NUMMER}, {HERSTELLER}, {HERSTELLERNUMMER}, {HERKUNFTSLAND}, {ZOLLTARIFNUMMER}, {LISTINGID}, {PREIS}, {WAEHRUNG}, {LAENGE}, {BREITE}, {HOEHE}, {GEWICHT}, {EINHEIT}, {PSEUDOPREIS}, {ZUSTAND}, {FIRMA}, {EBAYUSERID}, {EIGENSCHAFT_Eigenschaftname_XX}, {ARTIKELNAME_XX}, {KURZTEXT_XX}, {ARTIKELBESCHREIBUNG_XX}, {ARTIKELSHOPTEXT_XX}, {METATITEL_XX}, {METADESCRIPTION_XX}, {METAKEYWORDS_XX}, {FREIFELD1_XX}... {FREIFELD40_XX}, {BILDURL1}... {BILDURL12};

#### Vorlagen mit Bedingungen

Vorlagen können {IF}-Verzweigungen enthalten, d.h. ein Inhalt wird nur dann dargestellt, wenn eine bestimmte Bedingung erfüllt ist.

In folgendem Beispiel soll der Hersteller eines Artikels angegeben werden. Ist im Artikel kein Hersteller gepflegt, sollen die Informationen aus dem Kurztext angezeigt werden. Ist auch hier nichts gepflegt, soll der Satz *Leider gibt es zu diesem Artikel keine weiteren Informationen* angezeigt werden.

Die Vorlage wird um eine entsprechende IF-Verzweigung ergänzt:

![eBay-App-9.png](https://help.xentral.com/hc/article_attachments/18590747196444)

Ist in einem Artikel kein Kurztext gepflegt, treffen die ersten beiden {IF}-Bedingungen nicht zu, d.h. die Vorlage wird den {ELSE}-Fall wählen und einen definierten Text anzeigen.

![eBay-App-10.png](https://help.xentral.com/hc/article_attachments/18590766464284)

> **Wichtig**
>
> Seit März 2018 werden Artikelbeschreibungen ohne HTTPS-Inhalte von eBay automatisch hinter einer Schaltfläche versteckt, welcher zur kompletten Artikelbeschreibung führt. Sollte dieses Verhalten auftreten, muss die Vorlage entsprechend angepasst werden.

#### Vorschau der eBay-Vorlagen im Artikel

Um die oben gezeigte Vorlage auf Korrektheit hin zu überprüfen, navigiere zu einem Artikel, den du mit eBay verknüpft hast (Stammdaten > Artikel). Öffne den ReiterOnline-Shop Optionenund prüfe, ob du bereits eBay als Shop hinterlegt hast. Weitere Informationen findest du[hier](https://help.xentral.com/hc/de/articles/5355868406428#UUID-1d1e8a13-6479-2b8d-d64e-2d5a4a044eb1).

Ist bereits ein eBay-Eintrag vorhanden, klicke auf![Gear_onlineshopoptions.png](https://help.xentral.com/hc/article_attachments/18590766465308)

für den Eintrag.

Es wird eine Übersicht angezeigt. Wähle im BereichTemplatesdeine zuvor angelegte Vorlage aus demVorlagen-Dropdown-Menü aus. Klicke aufZeige Vorschau, um deine Vorlage zu prüfen.

![eBay-App-12.png](https://help.xentral.com/hc/article_attachments/18590747201692)

In dem sich dann öffnenden Reiter im Browser kannst du alle Eingaben einsehen. Klicke aufSpeichern.

### Rahmenbedingungen

eBay empfiehlt die Nutzung von Rahmenbedingungen für Listings. Die Rahmenbedingungen sowie die Verwendung dieser definierst du in den Kontoeinstellungen von eBay. Rahmenbedingungen dienen dazu, Versand-, Zahlungs- und Rückgabedaten zu vereinheitlichen und vereinfachen. So müssen diese nicht mehr separat für jeden Artikel eingestellt werden, sondern können im Artikel aus einer Gruppe von Optionen ausgewählt werden.

Damit Rahmenbedingungen verwendet werden können, setze für eBay im ModulOnline-Shopsein Häkchen beiRahmenbedingungen verwenden.

![eBay-App-13.png](https://help.xentral.com/hc/article_attachments/18590766470044)

Du kannst die Rahmenbedingungen im untergeordneten ReiterRahmenbedingungenherunterladen. Wähle den gewünschten eBay-Shop imImporterschnittstelle-Dropdown-Menü. Sobald die Rahmenbedingungen heruntergeladen wurden, kannst du ihre Bezeichnungen ändern, um in den Artikeleinstellungen passende Bezeichnungen zur Verfügung zu haben. Eine Änderung des tatsächlichen Inhalts der Rahmenbedingung erfolgt derzeit noch direkt in eBay.

![eBay-App-14.png](https://help.xentral.com/hc/article_attachments/18590766471836)

Wenn es bei eBay Änderungen beim Versand, Zahlungen oder Rückgaben gibt, kannst du die Rahmenbedingungen mit einem Klick aufRahmenbedingungen aktualisierenaktualisieren.

![eBay-App-15.png](https://help.xentral.com/hc/article_attachments/18590747209500)

### Zuordnungen

Hast du eBay bereits vor der Nutzung des eBay-Importers verwendet, kannst du bereits bestehende Listings anzeigen lassen und so bestehende Produktbewertungen weiter verwenden. Voraussetzung für die Zuweisung der Artikel ist, dass die eindeutigen Identifikationsnummern bei den Artikeln als[Fremdnummern](https://help.xentral.com/hc/de/articles/18589763213980#UUID-3844967d-dff7-bcc8-f69a-f3d2a5bf4093)hinterlegt sind. Klicke im BereichAktionenaufArtikelliste aktualisieren, um den aktuellen Stand der Listings anzuzeigen.

Werden Artikel mit SKU übertragen, versucht Xentral eine automatische Zuordnung über die EAN. Alle gefunden, korrekten Zuordnungen werden angezeigt. Du kannst Zuweisungen ändern, indem du auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/18590766452252)

in der SpalteMenüklickst.

Sind alle Zuweisungen erfolgt, klicke im BereichAktionenaufArtikel automatisch zuordnen. Die Zuweisung wird in den Fremdnummern hinterlegt. Erst nach diesem Schritt ist die Zuordnung funktional.

### Versand

Im untergeordneten ReiterVersandkannst du Versanddienstleister den einzelnen Versandarten zuweisen.

Um die verfügbaren Versanddienstleister herunterzuladen, klicke im BereichAktionenaufShipping Carrier herunterladen.  Du kannst nun Zuweisungen herstellen, indem du auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/18590766452252)

klickst.

> **Anmerkung**
>
> Stelle sicher, dass alle erforderlichen Zuweisungen erfolgt sind, da sonst keine Trackingdaten übermittelt werden können.

Wichtig für die Rückmeldung von Trackingdaten: Für die Rückmeldung versucht Xentral zunächst, über die eingestellte Versandart an eBay zu melden. Sollte die Versandart keinem bekannten Dienstleister entsprechen, schlägt der Versand fehl. Die Versandart muss dann entsprechend angepasst werden. Es kann außerdem sein, dass der von eBay übermittelte Dienstleister nicht der angegebenen Beschreibung entspricht, wenn z.B. DHL als Dienstleister angegeben aber DPD in der Beschreibung erwähnt ist. In diesem Fall musst du den Dienstleister überschreiben, damit die Rückmeldung korrekt erfolgt.

### Storekategorien

Im untergeordneten ReiterStorekategorienkannst du eBay-Shopkategorien anzeigen und aktualisieren. Klicke dazu im BereichAktionenaufStorekategorien herunterladen.

> **Anmerkung**
>
> Änderungen in der Shopnavigation in eBay müssen auf in der eBay-App in Xentral aktualisiert werden.

## Der Reiter Stapelverarbeitung

### Jobs

Änderungen im Lagerbestand werden in regelmäßigen Abständen an eBay übertragen. Dies  kannst du im untergeordneten ReiterJobsnachverfolgen. Jobs sind Synchronisationen des Lagerbestands.

Der Prozessstarter fasst etwa alle 30 Minuten Änderungen/Requests als Job zusammen und überträgt diese an Ebay.

Für eine komplette Lagersynchronisierung brauchen wir jedoch zwei Zyklen des Jobs:

1. Im ersten Zyklus fordert Xentral eine Task-ID von eBay an. Diese ist für die Lagersynchronisierung erforderlich. eBay wird dann eine Task-ID zurückmelden.
1. Im zweiten Zyklus fügtXentral die Daten zur Task-ID hinzu und überträgt diese an eBay.

Die Lagersynchronisierung ist bereits erfolgt, wenn die Rückmeldung von eBay eingeht.

![eBay-App-22.png](https://help.xentral.com/hc/article_attachments/18590766477084)

### Requests

Im untergeordneten ReiterRequestswerden die einzelnen Lagerbestandsänderungen angezeigt.

![eBay-App-23.png](https://help.xentral.com/hc/article_attachments/18590747212572)

### Protokoll

Jedwede Kommunikation zwischen Xentral und eBay wird protokolliert. Die Protokolle findest du im untergeordneten ReiterProtokoll. Hier sind alle übertragenen Produkte mit ihren Job-IDs gelistet.

Du kannst den FilterNur Übertragungsfehlerverwenden, um fehlerhafte Übertragungen anzuzeigen.