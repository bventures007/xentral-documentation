Shop-Schnittstellen (sog. "Importer") können kundenspezifisch erstellt oder überladen werden. Dabei können bereits im Import-Prozess Daten verändert oder angereichert werden, auch die komplexere Umwandlung von Datenstrukturen ist möglich.

## Einleitung

Ein großes Thema bei xentral ist die Anbindung und automatische Verarbeitung von Bestellungen in Online-Shops. Obwohl viele Online-Shops bereits einen hohen Automatisierungsgrad besitzen, stellen neue Shopsysteme und deren Anbindung uns immer wieder vor Herausforderungen. Zwar besitzt fast jeder Shop eine Schnittstelle, häufig stellt sich dann aber doch heraus, dass die anzubindenden Schnittstellen nicht kompatibel sind.

Der Importer tritt dabei als sogenannte Middleware auf und übersetzt die Daten der Bestellungen aus dem Shop in ein Format, aus dem xentral dann wiederum Aufträge erstellen kann. Umgekehrt ist der Importer auch dafür zuständig den Bestellstatus, also die Information, ob der Auftrag abgearbeitet und versendet wurde, sowie Artikeldaten und Lagerzahlen an den Shop zu übertragen – ein kompaktes Multitalent sozusagen.

## Der Ablauf innerhalb des Shop-Importers

Der Ablauf innerhalb des Importers folgt immer einem festen Schema. Wenn beispielsweise Aufträge aus dem Shop abgeholt werden sollen, wird zunächst geprüft ob eine Verbindung zur Shop-Schnittstelle besteht. Anschließend wird ermittelt ob, beziehungsweise wie viele, Aufträge im Shop abgeholt werden sollen. Wenn es Aufträge abzuholen gibt, werden diese importiert und anschließend im Shop als „In Bearbeitung“ markiert. Wenn Artikel aus dem Shop importiert oder in den Shop exportiert werden sieht das Schema ähnlich aus. Zunächst erfolgt eine Prüfung, ob eine Verbindung zwischen xentral und dem Shop besteht. Anschließend werden die Daten übertragen.

![ShopImporterScript-1.png](https://help.xentral.com/hc/article_attachments/4996450950428)

## Grundlagen

Um einen eigenen Importer zu schreiben benötigt man keine Expertenkenntnisse. Grundlegende PHP-Kenntnisse reichen aus, wenn man sich an die vorgegebene Struktur hält. Im Vorfeld sind jedoch einige Dinge zu klären:

1. Name Der Name des Importers spielt eigentlich keine große Rolle. Per Konvention ist es aber so, dass der Klassenname aus „Shopimporter_XXX“ zusammengesetzt wird. In diesem Beispiel werden wir einen speziellen Importer für Shopware entwickeln, weswegen die Klasse auch den Namen Shopimporter_Shopwarespecial trägt. Die Datei selbst heißt wie der Klassenname in Kleinbuchstaben und wird im www/pages/ Verzeichnis der Xentral-Installation abgelegt, also beispielsweise
1. Datenbankeintrag Wird ein neuer Importer über die Oberfläche zum System hinzugefügt wird in der Datenbank in der Tabelle „Shopexport“ ein neuer Eintrag angelegt. Da dieser Importer jedoch eine Spezialanfertigung ist, muss in diesem Fall der Namen des Importer kurzerhand selbst in diese Tabelle eingetragen werden. Wichtig ist dabei, dass der Modulname dem Namen der PHP-Datei entspricht.
1. ShopimporterBase Allen internen Importern liegt die Klasse „ShopimporterBase“ zugrunde. Die Klasse beinhaltet systemrelevante Funktionen, welche die Ausführung des Importers gewährleisten. Prinzipiell sollte jeder Importer von der Basisklasse ShopimporterBase abgeleitet sein, damit sichergestellt werden kann, dass diese Funktionen auch wirklich vorhanden sind:
1. Boilerplate Zwei Variablen sind für die Verwendung der Importer relevant. $app beinhaltet die Applikation xentrals selbst und wird im Konstruktor übergeben. Dadurch kann der Importer die Kernfunktionalität von xentral nutzen, ohne dass dafür zusätzlich noch etwas getan werden muss. Die Variable $intern gibt nicht an, ob es sich um einen internen Importer handelt, sondern ob die Actionhandler für das Objekt initialisiert werden müssen. Dadurch ist es möglich, das Objekt anderweitig zu instanziieren und zu verwenden, ohne dass es zu einem Konflikt kommt.
1. Konstruktor Im Konstruktor werden zwei Parameter übergeben, $app und $intern werden direkt im Objekt hinterlegt, um später bei Bedarf angesprochen zu werden. Dann findet die erste Logik im Modul statt: Es wird geprüft ob für das Modul Actionhandler registriert werden sollen. Es gibt einige Actionhandler, die registiert werden können – für dieses Beispiel orientieren wir uns aber an den grundlegenden Funktionen die eigentlich jeder Shopimporter mitbringen sollte. Es ist empfiehlt sich die Funktionsnamen wie vorgegeben zu übernehmen um die Kompatibilität zu gewährleisten. Eine Auflistung der Funktionen sowie die Rolle, die im Importer übernommen wird, folgt weiter unten im Detail.
1. EinstellungenStruktur Da eigentlich jede Shop-Schnittstelle ihre ganz eigenen Einstellungsmöglichkeiten hat, ist es notwendig dem Importer genau diese Einstellungsmöglichkeiten mit auf den Weg zu geben. Das passiert in der Funktion EinstellungenStruktur(). Hier übergebene Felder werden im Oberflächen-Formular des Importers angezeigt. Bei Bedarf können natürlich auch weitere Felder angelegt werden - für dieses Beispiel sollen aber die für die Anmeldung benötigten Daten ausreichen.
1. getKonfig Die letzte Funktion bevor es richtig los geht ist getKonfig(). In dieser Funktion werden die Daten aus den Einstellungen sowie die ID des Shopimporters an das Objekt übergeben. Der Parameter $data ist ein Überbleibsel aus der Zeit der externen Importer. In diesem Parameter werden Anweisungen für die einzelnen Funktionen parat gehalten. Diese Funktion wird vom System bei der Initialisierung des Objekts aufgerufen.

Nachdem die Grundlagen für den Importer erledigt sind, kommt es jetzt zur eigentlichen Verbindung zu Shopware. Natürlich ist es möglich, die komplette Kommunikation in eine eigene Klasse auszulagern oder, im Falle von Shopware, die Klasse aus der Dokumentation zu kopieren. Der Einfachheit halber reicht für dieses Beispiel aber eine kurze Funktion welche die Antwort der API zurückgibt:

```
protected function call($endpoint, $method, $data=array(),$params=array()){ $queryString = ''; if (!empty($params)) { $queryString = '?'.http_build_query($params);} $url = $this->apiUrl.$endpoint.$queryString; $dataString = json_encode($data);

$curl = curl_init(); curl_setopt($curl, CURLOPT_RETURNTRANSFER, true); curl_setopt($curl, CURLOPT_FOLLOWLOCATION, false); curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC); curl_setopt($curl, CURLOPT_USERPWD, $this->apiUser. ':'. $this->apiKey); curl_setopt($curl, CURLOPT_HTTPHEADER, ['Content-Type: application/json; charset=utf-8']); curl_setopt($curl, CURLOPT_URL, $url); curl_setopt($curl, CURLOPT_CUSTOMREQUEST, $method); curl_setopt($curl, CURLOPT_POSTFIELDS, $dataString); return curl_exec($curl);}
```

## Funktion ImportAuth

Nachdem alle Voraussetzungen für die Funktion des Importers erfüllt sind, kann er mit Leben gefüllt werden. Die erste Schritt in diese Richtung ist die Funktion ImportAuth(). In externen Importer ist diese Funktion für die Authentifizierung von xentral zum Importer notwendig, in internen Importern prüft die Funktion den Verbindungsaufruf zur API. Da diese Funktion jedes Mal aufgerufen wird wenn der Importer in Aktion treten soll, steckt hier für gewöhnlich eine Anfrage oder ein Mechanismus zum Erstellen eines Tokens. Wichtig ist dabei die Rückgabe von success, um mitzuteilen, dass der Importer bereit ist, um Anweisungen entgegenzunehmen und an die Shop API weiterzuleiten.

```
public function ImportAuth() { $params = ['limit' => 1]; $responseJson =$this->call('articles','GET',null, $params); $response = json_decode($responseJson,true);

if($response['success']){ return 'success';}

return '';}
```

## Funktion ImportSendListLager

Als nächstes wird die Funktion ImportSendListLager() hinzugefügt. Wenn die Option für das Übertragen von Lagerzahlen in den Importeinstellungen aktiviert ist sorgt die Funktion dafür, dass die Bestände im Shop mit dem Beständen in xentral synchronisiert werden. In diesem Beispiel geschieht das über die Artikelnummer. Zu beachten ist, dass für diese Funktion im data-Parameter des Importer-Objekts die Daten für den zu aktualisierenden Artikel vorhanden sind.

```public function ImportSendListLager() { $updatedArticles = 0; $tmp = $this->CatchRemoteCommand('data'); foreach ($tmp as $article){ $nummer = $article['nummer']; $lageranzahl = $article['anzahl_lager'];```

```
$updateInStock = [
  'mainDetail' => [
  'inStock' => $lageranzahl
]
];

$params = [
  'useNumberAsId'=>true
];

$result = $this->call('articles/'.$nummer, 'PUT',$updateInStock, $params);
if($result['success']){
  $updatedArticles++;
}

```

```} return $updatedArticles;}```

## Funktion ImportSendlList

Die Funktion ImportSendList() ist im Grunde genommen eine aufgebohrte Version von ImportSendListLager(). Die Funktion überträgt Artikel an den Shop - beziehungsweise aktualisiert deren Daten. Welche Daten und vor allem wie diese übertragen werden können, hängt von der jeweiligen Shop-Schnittstelle ab. So können Artikeleigenschaften oder auch Bilder an den Shop übertragen werden. Dabei sollte man auf die Trennung der beiden Funktionen achten, da ImportSendList nur in zwei Fällen aufgerufen wird:

1. Manueller Export des Artikels
1. Export des Artikels über die Artikel-Übertragung im Importer

```$articleData = [ 'name' => $name, 'lastStock' => $laststock, 'tax' => $tax, // alternativ 'taxId' => 1, 'supplier' => $supplier, // alternativ 'supplierId' => 2, 'description' => $description, 'descriptionLong' => $description_long, 'keywords' => $keywords, 'metaTitle' => $metatitle, 'highlight' => $topseller, 'mainDetail' => [ 'number' => $articleNumber, 'active' => $active, 'ean' => $ean, 'weight' => $weight, 'width' => $width, 'len' => $length, 'height' => $height, 'supplierNumber' => $supplierNumber, 'inStock' => $lageranzahl, 'prices' => $prices]];```

## Funktion ImportGetAuftraegeAnzahl

In dieser Funktion wird ermittelt, wie viele offene Bestellungen im Shop vorhanden sind und abgeholt werden müssen. Denkbar ist das Abholen über den Status, ab einer bestimmten Bestellnummer oder aber auch über das Bestelldatum. Abhängig von der Shopschnittstelle sind nicht alle Optionen realisierbar.

```
public function ImportGetAuftraegeAnzahl() { $result = $this->getOrders($this->data);

return count($result['data']);}
```

## Funktion ImportGetAuftrag

Die wichtigste Grundfunktion aller Importer ist das Abholen und Übersetzen der Bestellungen aus dem Shop in das Warenkorbformat von xentral. Nachdem die nächste Bestellung von der Shop API abgeholt wurde, werden im ersten Schritt die Adressdaten des Kunden an den Warenkorb übergeben:

```$cart['anrede'] = 'herr'; $cart['strasse'] = $order['data']['billing']['street']; $cart['plz'] = $order['data']['billing']['zipCode']; $cart['ort'] = $order['data']['billing']['city']; $cart['land'] = $order['data']['billing']['country']['iso']; $cart['email'] = $order['data']['customer']['email']; $cart['name'] = $order['data']['billing']['firstName']. ' '. $order['data']['billing']['lastName'];```Falls eine abweichende Lieferadresse vorliegt, muss diese logischerweise enebfalls übergeben werden. Ausserdem muss dann das Feld abweichendeliferadresse mit true befüllt werden damit der Auftrag dann auch beim richtigen Empfänger ankommt. Anschließend gibt es eine ganze Reihe wichtiger Daten, die für die weitere Verarbeitung von Bedeutung sind.```$cart['auftrag'] = $orderFromCollection['id']; $cart['gesamtsumme'] = $orderFromCollection['invoiceAmount']; $cart['transaktionsnummer'] = $orderFromCollection['transactionId']; $cart['onlinebestellnummer'] = $orderFromCollection['number'];... $cart['zahlungsweise'] = $order['data']['payment']['name']; $cart['lieferung'] = $order['data']['dispatch']['name']; $cart['bestelldatum'] = substr($order['data']['orderTime'],0,10); $cart['versandkostennetto'] = $order['data']['invoiceShippingNet'];```

- **Gesamtsumme:** Die Gesamtsumme des Auftrags dient als Absicherung gegen einen falsch zusammengesetzten Warenkorb. Falls Artikeldaten nicht richtig übergeben wurden oder es ein Problem mit der Besteuerung gibt weicht die Gesamtsumme des Auftrags von der Gesamtsumme des Warenkorbs ab und für die Bestellung wird die Auto-Versandoption deaktiviert. Dadurch wird sichergestellt, dass keine Lieferung das Lager verlässt, die nicht mit der Bestellung übereinstimmt.
- **Transaktionsnummer:** Die Transaktionsnummer ist für die Automatisierung des Rechnungswesens relevant und hilft dabei bezahlte Bestellungen zuzuordnen.
- **Auftrag:** In diesem Feld wird die eindeutige Kennzeichnung des Auftrags für den Shop übergeben. Nicht jede Shop-Schnittstelle erlaubt es den Versandstatus einer Bestellung über die Bestellnummer zu ändern. Gelegentlich wird eine interne ID benötigt, die an dieser Stelle übergeben werden kann. Auf den hier übergebenen Wert wird später Bezug genommen, wenn eine Änderung des Bestellstatus aus dem Shop übermittelt wird.
- **Onlinebestellnummer:** In diesem Feld steht die Bestellnummer, die auch der Kunde sieht. Das erleichtert die Zuordnung und im Falle einer Rückfrage kann dadurch eine Bestellung aus dem Shop direkt einem Auftrag in xentral zugeordnet werden.
- **Zahlungsweise:** Das Übertragen der Zahlungsweise erlaubt es, Einstellungen wie Autoversand, Fast-Lane oder das Anlegen von Rechnungen spezifisch für bestimmte Zahlungsweisen in xentral zu aktivieren oder zu deaktivieren.
- **Lieferung:** Ähnlich wie bei der Zahlungsweise kann bei übergebener Lieferweise ein Matching in xentral vorgenommen werden.
- **Versandkostenbrutto:** Prinzipiell können bei einer Bestellung die Versandkosten wie ein Artikel im Warenkorb mit übergeben werden. Durch die Verwendung dieses Spezialfelds werden die Versandkosten allerdings gleich auf den im Importer eingestellten Portoartikel gebucht und in den Auftrag übernommen.
- **Bestelldatum:** Das Bestelldatum zeigt das Datum an, an dem die Bestellung eingegangen ist.

```
foreach ($order['data']['details'] as $article) { $articlearray[] = [ 'articleid' => $article['articleNumber'], 'name' => $article['articleName'], 'price' => $article['price'], 'quantity' => $article['quantity']];}

...

$orderData =[ 'id' => $cart['auftrag'], 'warenkorb' => base64_encode(serialize($cart)), 'warenkorbjson' => base64_encode(json_encode($cart))];
```Wenn die benötigten Grunddaten der Bestellung an den Warenkorb übergeben wurden, ist es an der Zeit die einzelnen Positionen zum Warenkorb hinzuzufügen. Im Feld articleid wird die Artikelnummer übergeben. In den anderen Feldern steht ihr jeweiliges Äquivalent aus der Bestellposition. Nachdem der Warenkorb mit allen Daten befüllt wurde die aus der Bestellung übergeben werden sollen, gibt die Funktion die Daten zurück. Funktionen ImportDeleteAuftrag / ImportUpdateAuftrag Die aus historischen Gründen ungünstig benannte Funktion ImportDeleteAuftrag wird nicht etwa dazu verwendet um Aufträge aus dem Shop zu löschen. Sie ist stattdessen dafür zuständig eine offene Bestellung als „In Bearbeitung“ zu kennzeichnen. Die Partnerfunktion ImportUpdateAuftrag kennzeichnet die Bestellung als „Versendet“.```
public function ImportDeleteAuftrag() { $orderId = $this->data['auftrag']; $update = [ 'orderStatusId' => 1];

$this->call('orders/'.$orderId, 'PUT',$update);

return true;}
```