Unter Converter Scripts werden in xentral alle Erweiterungen zusammengefasst, die zur Konvertierung von Daten verwendet werden. Darin enthalten sind u.a.:

- Dateiimport und -export
- Datentransfer über das Übertragen-Modul in vielen Formaten (CSV, XML, PDF, EDI)
- Datenaustausch über Shopschnittstellen
- Belegimport und Datenmigration

xentral bietet bereits viele Connectoren zu externen Diensten. Diese sind meistens über eine proprietäre API-Schnittstelle umgesetzt und daher nicht veränderbar. Daten können aber an verschiedenen Stellen in xentral aus dem System heraus exportiert und anderen Diensten zur Verfügung gestellt werden. Dabei sind die Möglichkeiten für Ausgabeformate beinahe unbegrenzt, eingehende Nachrichten sind jedoch meist von korrekter Interpretation der Datenstrukturen abhängig und daher nur bedingt anpassbar.

## Modul Übertragungen (CSV/XML/EDI/PDF)

Ein Tool zur Verarbeitung aus- und eingehender Daten ist das[Modul Übertragungen (CSV/XML/EDI/PDF)](https://help.xentral.com/hc/articles/360016738020#UUID-88dc60e8-820c-bd05-95e8-2d31e5ff7ec9). Dort stehen diverse Ein- und Ausgabeformate zur Verfügung, es lassen sich aber eigene Formate definieren. Die flexibelste Lösung zum Datentransfer von Listen bietet das CSV-Format. Da die Spalten durch die Spaltenbeschriftung eindeutig zuordenbar sind, kann dieses Format auch flexibel auf eingehende Daten reagieren.

### Ausgehende Daten manipulieren

Mit Hilfe der integrierten[Template-Engine Smarty](https://www.smarty.net/)können flexibel zeichenbasierte Ausgabestrukturen von Datenformaten wie CSV, XML oder JSON an die Bedürfnisse des Kunden angepasst werden. Es muss lediglich das vorhandene Zielformat in eine Textdatei kopiert und mit den entsprechenden Variablen gefüllt werden. Diese können dabei noch umformatiert werden.

Belegdaten befinden sich z.B. in der Smarty-Variable $beleg und werden in gewohnter PHP-Objektschreibweise angesprochen, z.B. $beleg->kundennummer oder $beleg->belegnr. Die Namensgebung gleicht der Benennung von Datenbank-Spaltennamen. Auch ein Zugriff auf komplexere Strukturen ist je nach Beleg möglich. So kann im Lieferschein auf den zugrundeliegenden Auftrag zugegriffen werden: $beleg->auftrag->lieferdatum.

**Verkürztes Beispiel mit fiktivem Format**

```
<?xml version="1.0" encoding="utf-8"?>
<lieferschein>

  {*Beleg-Stammdaten --------------------------------*} 
  <status>{$beleg->status}</status>
  <datum>{$beleg->datum|date_format:'%d.%m.%Y'}</datum>
  <belegnummer>{$beleg->belegnr}</belegnr>
  <kundennummer>{$beleg->kundennummer}</kundennummer>
  <kundenname>{$beleg->name}</kundenname>

  {*Zugriff auf Daten des zugrundeliegenden Auftrages*} 
  <lieferdatum>{$beleg->auftrag->lieferdatum}</lieferdatum>
  {*Weitere Felder entfernt*} 

  {*Positionen - Beginn ------------------------------*} 
  <positionen>

  {*Schleife durchläuft alle verfügbaren Positionen*} 
  {foreach from=$beleg->positionen key=keypos item=position}
  <position>
  <artikelnummer>{$position->nummer}</artikelnummer>
  <artikelbezeichnung>{$position->bezeichnung}</artikelbezeichnung>
  <artikelbeschreibung>{$position->beschreibung}</artikelbeschreibung>
  <menge>{$position->menge}</menge>
  <preis>{$position->preis}</preis>
  <ean>{$position->articledata->ean}</ean>
  {*Weitere Felder entfernt*} 
  </position>
  {/foreach}

  </positionen>
  {*Positionen - Ende --------------------------------*} 
</lieferschein>

```

### Zusatzdaten aus den Stammdaten

Über die übermittelten Daten hinaus, kann auch auf zusätzliche Daten, z.B. aus den Artikelstammdaten, zugegriffen werden. Diese sind über das Objekt articledata referenzierbar, wie im obigen Beispiel durch die EAN dargestellt. Alle Spalten der Artikeltabelle sind über diese Notation ansprechbar, also z.B. auch die Freifelder des Artikels, die im Auftrag selbst ggf. mit anderen Werten belegt sein können.

### Formatumwandlung

#### Datumswerte

Datumswerte können nach Anforderung ausgegeben werden:

- Int. Datumsformat (ISO 8601):
- Deutsches Datumsformat (DIN 5008):

#### Zahlen

Zahlen können nach Bedarf formatiert werden. Hier am Beispiel der Spalte "Menge":

- Ausgabe ohne Nachkommastellen (als Ganzzahl):
- Ausgabe mit einer Nachkommastelle:
- Ausgabe mit zwei Nachkommastellen:

#### Texte

Bei einigen Ausgabeformaten sind die Textlängen für ausgegebene Texte zu formatieren. Dazu eignet sich die

- Ausgabe fester Länge mit führenden Leerzeichen:
- Ausgabe fester Länge mit führenden Nullen:

Grundsätzlich können alle Formate ausgegeben werden, die durch die[Funktion sprintf](https://www.php.net/manual/de/function.sprintf.php)in PHP verfügbar sind.

### Beispiele

Im Folgenden sind einige Beispiele zusammengefasst, die die Ausgabe verschiedener Lieferscheinformate in den Formaten EDI, CSV und XML ermöglichen. Dabei sind die Spaltenbeschriftungen (CSV), Tagnamen (XML) und EDI-Spezifikationen zu prüfen. Weitere Ausgabeformate wie z.B. JSON sind denkbar.

#### Beispiel Lieferschein CSV (ausführlich)

Im Folgenden wird ein ausführliches Beispiel für den Export eines Lieferscheines in verschiedenen Formaten aufgelistet.

Format EDI

```- wird ergänzt -```**Format CSV**`"tracking";"beleg_status";"beleg_datum";"beleg_lieferdatum";"beleg_tatsaechlicheslieferdatum";"beleg_versandart";"beleg_zahlungsweise";"beleg_belegnr";"beleg_hauptbelegnr";"beleg_kundennummer";"beleg_name";"beleg_abteilung";"beleg_unterabteilung";"beleg_adresszusatz";"beleg_ansprechpartner";"beleg_telefon";"beleg_email";"beleg_land";"beleg_strasse";"beleg_plz";"beleg_ort";"beleg_projekt";"beleg_aktion";"beleg_internebemerkung";"beleg_internebezeichnung";"beleg_freitext";"beleg_ihrebestellnummer";"beleg_lieferbedingung";"beleg_art";"artikel_nummer";"artikel_bezeichnung";"artikel_beschreibung";"artikel_menge";"artikel_preis";"artikel_rabatt";"artikel_waehrung";"artikel_lieferdatum";"artikel_sort";"artikel_umsatzsteuer";"artikel_einheit";"artikel_zolltarifnummer";"artikel_herkunftsland";"artikel_artikelnummerkunde";"wunschlieferdatum";"artikel_freifeld1";"artikel_freifeld2";"artikel_freifeld3";"artikel_freifeld40"`

```
{foreach from=$beleg->positionen key=keyrow item=position}{*Positionen*}\
"{$position->tracking}";\
"{$beleg->status}";\
"{$beleg->datum|date_format:'%d.%m.%Y'}";\
"{$beleg->lieferdatum}";\
"{$beleg->tatsaechlicheslieferdatum}";\
"{$beleg->versandart}";\
"{$beleg->zahlungsweise}";\
"{$beleg->belegnr}";\
"{$beleg->hauptbelegnr}";\
"{$beleg->kundennummer}";\
"{$beleg->name}";\
"{$beleg->abteilung}";\
"{$beleg->unterabteilung}";\
"{$beleg->adresszusatz}";\
"{$beleg->ansprechpartner}";\
"{$beleg->telefon}";\
"{$beleg->email}";\
"{$beleg->land}";\
"{$beleg->strasse}";\
"{$beleg->plz}";\
"{$beleg->ort}";\
"{$beleg->projekt}";\
"{$beleg->aktion}";\
"{$beleg->internebemerkung}";\
"{$beleg->internebezeichnung}";\
"{$beleg->freitext}";\
"{$beleg->ihrebestellnummer}";\
"{$beleg->lieferbedingung}";\
"{$beleg->art}";\
"{$position->nummer}";\
"{$position->bezeichnung}";\
"{$position->beschreibung}";\
"{$position->menge|string_format:'%.2f'}";\
"{$position->preis}";\
"{$position->rabatt}";\
"{$position->waehrung}";\
"{$position->lieferdatum}";\
"{$position->sort}";\
"{$position->umsatzsteuer}";\
"{$position->einheit}";\
"{$position->zolltarifnummer}";\
"{$position->herkunftsland}";\
"{$position->artikelnummerkunde}";\
"{$beleg->auftrag->lieferdatum}";\
"{$position->freifeld1}";\
"{$position->freifeld2}";\
"{$position->freifeld3}";\
{*Ggf. weitere Freifelder*}";\
"{$position->freifeld40}";\

{/foreach}

```**Format XML**```
<?xml version="1.0" encoding="utf-8"?>
<lieferschein>

  <status>{$beleg->status}</status>
  <datum>{$beleg->datum|date_format:'%d.%m.%Y'}</datum>
  <lieferdatum>{$beleg->lieferdatum}</lieferdatum>
  <tatsaechlicheslieferdatum>{$beleg->tatsaechlicheslieferdatum}</tatsaechlicheslieferdatum>
  <versandart>{$beleg->versandart}</versandart>
  <zahlungsweise>{$beleg->zahlungsweise}</zahlungsweise>
  <belegnr>{$beleg->belegnr}</belegnr>
  <hauptbelegnr>{$beleg->hauptbelegnr}</hauptbelegnr>
  <kundennummer>{$beleg->kundennummer}</kundennummer>
  <name>{$beleg->name}</name>
  <abteilung>{$beleg->abteilung}</abteilung>
  <unterabteilung>{$beleg->unterabteilung}</unterabteilung>
  <adresszusatz>{$beleg->adresszusatz}</adresszusatz>
  <ansprechpartner>{$beleg->ansprechpartner}</ansprechpartner>
  <telefon>{$beleg->telefon}</telefon>
  <email>{$beleg->email}</email>
  <land>{$beleg->land}</land>
  <strasse>{$beleg->strasse}</strasse>
  <plz>{$beleg->plz}</plz>
  <ort>{$beleg->ort}</ort>
  <projekt>{$beleg->projekt}</projekt>
  <aktion>{$beleg->aktion}</aktion>
  <internebemerkung>{$beleg->internebemerkung}</internebemerkung>
  <internebezeichnung>{$beleg->internebezeichnung}</internebezeichnung>
  <freitext>{$beleg->freitext}</freitext>
  <ihrebestellnummer>{$beleg->ihrebestellnummer}</ihrebestellnummer>
  <lieferbedingung>{$beleg->lieferbedingung}</lieferbedingung>
  <art>{$beleg->art}</art>
  <positionen>

  {foreach from=$beleg->positionen key=keypos item=position}
  <position>
  <nummer>{$position->nummer}</nummer>
  <bezeichnung>{$position->bezeichnung}</bezeichnung>
  <beschreibung>{$position->beschreibung}</beschreibung>
  <menge>{$position->menge}</menge>
  <preis>{$position->preis}</preis>
  <rabatt>{$position->rabatt}</rabatt>
  <waehrung>{$position->waehrung}</waehrung>
  <lieferdatum>{$position->lieferdatum}</lieferdatum>
  <sort>{$position->sort}</sort>
  <umsatzsteuer>{$position->umsatzsteuer}</umsatzsteuer>
  <einheit>{$position->einheit}</einheit>
  <zolltarifnummer>{$position->zolltarifnummer}</zolltarifnummer>
  <herkunftsland>{$position->herkunftsland}</herkunftsland>
  <artikelnummerkunde>{$position->artikelnummerkunde}</artikelnummerkunde>
  <freifeld1>{$position->freifeld1}</freifeld1>
  <freifeld2>{$position->freifeld2}</freifeld2>
  <freifeld3>{$position->freifeld3}</freifeld3>
  {*Ggf. weitere Freifelder*} 
  <freifeld40>{$position->freifeld40}</freifeld40>
  </position>
 {/foreach}

  </positionen>
  {if $beleg->versand}
{foreach from=$beleg->versand key=keyversand item=tracking} {*Versand*}
  <tracking>{$tracking->tracking}</tracking>
{/foreach}
{/if}
</lieferschein>

```

#### Beispiel Lieferschein mit MHD

Im Folgenden werden Beispiele als Ergänzung zu obigen Code-Beispielen gezeigt, die nur Besonderheiten in Bezug auf MHDs in einer Position berücksichtigen.

**Format CSV **```- wird ergänzt -```** Format XML**```- wird ergänzt -```

#### Beispiel Lieferschein mit Charge

Nachstehend werden Beispiele als Ergänzung zu obigen Code-Beispielen angegeben, die nur die Besonderheiten in Bezug auf Chargen in einer Position berücksichtigen.

**Format CSV **```- wird ergänzt -```** Format XML**```- wird ergänzt -```

#### Beispiel Lieferschein mit Charge und MHD

Im Folgenden werden Beispiele als Ergänzung zu obigen Code-Beispielen gezeigt, die nur die Besonderheiten in Bezug auf MHDs und Chargen in einer Position berücksichtigen.

**Format CSV **```- wird ergänzt -```** Format XML**```- wird ergänzt -```

#### Beispiel Auftrag

Die Option ist nur bei direktem Fulfillment ohne Autoversand anwendbar. Diese sollte genau geprüft werden, meist ist die Übertragung von Lieferscheinen der optimale Weg.

**Format EDI **```- wird ergänzt -```** Format CSV **```- wird ergänzt -```** Format XML**```- wird ergänzt -```

## Shop Importer Script

Shop-Schnittstellen (sog. "Importer") können kundenspezifisch erstellt oder überladen werden. Bereits im Import-Prozess können Daten verändert oder angereichert werden, auch die komplexere Umwandlung von Datenstrukturen ist möglich.

### Einleitung

Bei xentral wird großer Wert auf die Anbindung sowie die automatische Verarbeitung von Bestellungen in Online-Shops gelegt. Daher bietet xentral Schnittstellen zu diversen Shops an. Obwohl fast jeder Shop eine Schnittstelle besitzt, treten manchmal Probleme mit der Kompatibilität der anzubindenden Schnittstellen auf. Ein Importer, der als Adapter zwischen xentral und der Online-Shops-Schnittstelle dient, kann entwickelt werden. Dieser tritt als Middleware auf und übersetzt die Daten der Bestellungen aus dem Shop in ein Format, aus dem xentral wiederum Aufträge erstellen kann. Umgekehrt ist der Importer auch dafür zuständig, den Bestellstatus, Artikeldaten und Lagerzahlen an den Shop zu übertragen.

### Der Ablauf innerhalb des Shop-Importers

Der Ablauf innerhalb des Importers folgt immer einem festen Schema. Wenn bspw. Aufträge aus dem Shop abzuholen sind, wird zunächst geprüft, ob eine Verbindung zur Shop-Schnittstelle besteht. Anschließend wird ermittelt ob bzw. wie viele Aufträge im Shop abgeholt werden sollen. Wenn es Aufträge zur Abholung vorhanden sind, werden diese importiert und anschließend im Shop als „In Bearbeitung“ markiert. Wenn Artikel aus dem Shop importiert oder in den Shop exportiert werden, gilt ein ähnliches Schema. Zunächst erfolgt die Prüfung, ob eine Verbindung zwischen xentral und dem Shop besteht, anschließend werden die Daten übertragen.

![ShopImporterScript-1.png](https://help.xentral.com/hc/article_attachments/4996448869916)

### Grundlagen

Es ist die vorgegebene Struktur einzuhalten, wenn ein Importer geschrieben wird. Einige Punkte sind im Vorfeld festzulegen:

1. Name
  Per Konvention wird der Klassenname aus „Shopimporter_XXX“ zusammengesetzt. In diesem Beispiel wird ein spezieller Importer für Shopware entwickelt, weshalb die Klasse auch den Namen Shopimporter_Shopwarespecial trägt. Die Datei selbst entspricht dem Klassenname in Kleinbuchstaben und wird im www/pages/ Verzeichnis der xentral-Installation abgelegt, also beispielsweise /var/home/www/html/xentral/www/pages/shopimporter_shopwarespecial.php.

1. Datenbankeintrag
  Wird ein neuer Importer über die Oberfläche zum System hinzugefügt, wird in der Datenbank in der Tabelle „Shopexport“ ein neuer Eintrag angelegt. Da dieser Importer jedoch eine Spezialanfertigung ist, muss in diesem Fall der Name des Importers selbst in diese Tabelle eingetragen werden. Wichtig ist dabei, dass der Modulname dem Namen der PHP-Datei entspricht.

1. ShopimporterBase
  Allen internen Importern liegt die Klasse „ShopimporterBase“ zugrunde. Die Klasse beinhaltet systemrelevante Funktionen, welche die Ausführung des Importers gewährleisten. Prinzipiell sollte jeder Importer von der Basisklasse ShopimporterBase abgeleitet sein, um sicherzustellen, dass diese Funktionen auch tatsächlich vorhanden sind:

1. Boilerplate
  Zwei Variablen sind für die Verwendung der Importer relevant:

  - $app beinhaltet die Applikation xentrals selbst und wird im Konstruktor übergeben. Der Importer kann, ohne zusätzliche Aktionen, die Kernfunktionalität von xentral nutzen.
  - $intern gibt an, ob die Actionhandler für das Objekt initialisiert werden müssen. Dadurch ist es möglich, das Objekt anderweitig zu instanziieren und zu verwenden
  /** *@var bool*/ public $intern = false;

  /** *@var Application*/ public $app;

1. Konstruktor
  Im Konstruktor werden zwei Parameter übergeben; $app und $intern werden direkt im Objekt hinterlegt, um später bei Bedarf angesprochen zu werden. Als erste Logik im Modul wird geprüft, ob für das Modul Actionhandler registriert werden sollen.

  Es gibt einige Actionhandler, die registiert werden können – in diesem Beispiel findet eine Orientierung an den grundlegenden Funktionen statt, die jeder Shopimporter beinhalten sollte. Es empfiehlt sich, die Funktionsnamen wie vorgegeben zu übernehmen, um die Kompatibilität zu gewährleisten. Eine Auflistung der Funktionen sowie die Rolle, die sie im Importer übernehmen, folgt im weiteren Verlauf.

1. EinstellungenStruktur
  Da jede Shop-Schnittstelle eigene Einstellungsmöglichkeiten hat, ist es notwendig, dem Importer diese Einstellungsmöglichkeiten über die Funktion EinstellungenStruktur() zu geben. Hier übergebene Felder werden im Oberflächen-Formular des Importers angezeigt. Bei Bedarf können auch weitere Felder angelegt werden.

1. getKonfig
  Die letzte Funktion ist getKonfig(). Diese übergibt die Daten aus den Einstellungen sowie die ID des Shopimporters an das Objekt. Im Parameter $data sind Anweisungen für die einzelnen Funktionen vorhanden. Diese Funktion wird vom System bei der Initialisierung des Objekts aufgerufen.

  Nachdem die Grundlagen für den Importer vorhanden sind, kommt es zur eigentlichen Verbindung zu Shopware. Es ist möglich, die komplette Kommunikation in eine eigene Klasse auszulagern oder, im Falle von Shopware, die Klasse aus der Dokumentation zu kopieren. Zur Vereinfachung ist für dieses Beispiel aber eine kurze Funktion ausreichend, welche die Antwort der API zurückgibt:

### Funktion ImportAuth

Es sind alle Voraussetzungen zu erfüllen: Zunächst ist die Funktion ImportAuth() zu verwenden. Im externen Importer ist diese Funktion für die Authentifizierung von xentral zum Importer notwendig, in internen Importern prüft die Funktion den Verbindungsaufruf zur API. Da diese Funktion jedes Mal aufgerufen wird, wenn der Importer in Aktion treten soll, liegt hier eine Anfrage oder ein Mechanismus zum Erstellen eines Tokens zugrunde. Wichtig ist dabei die Rückgabe von success, um mitzuteilen, dass der Importer bereit ist, Anweisungen entgegenzunehmen und an die Shop API weiterzuleiten.

```
public function ImportAuth()
{
  $params = ['limit' => 1];
  $responseJson =$this->call('articles','GET',null, $params);
  $response = json_decode($responseJson,true);

  if($response['success']){
  return 'success';
}

  return '';
}

```

### Funktion ImportSendListLager

Die Funktion ImportSendListLager() wird zusätzlich hinzugefügt. Wenn die Option für das Übertragen von Lagerzahlen in den Importeinstellungen aktiviert ist, führt diese Funktion zu einer Synchronisation der Bestände im Shop mit den Beständen in xentral. In diesem Beispiel geschieht das über die Artikelnummer. Es ist zu beachten, dass für diese Funktion im data-Parameter des Importer-Objekts die Daten für den zu aktualisierenden Artikel vorhanden sind.

```
public function ImportSendListLager()
{
  $updatedArticles = 0;
  $tmp = $this->CatchRemoteCommand('data');
  foreach ($tmp as $article){
  $nummer = $article['nummer'];
  $lageranzahl = $article['anzahl_lager'];

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
}
  return $updatedArticles;
}

```

### Funktion ImportSendList

Die Funktion ImportSendList() ist eine Version von ImportSendListLager(). Diese Funktion überträgt Artikel an den Shop bzw. aktualisiert deren Daten. So können Artikeleigenschaften oder Bilder an den Shop übertragen werden. Von der jeweiligen Shop-Schnittstelle hängt ab, wie und welche Daten übertragen werden können.

Es sollte auf die Trennung der beiden Funktionen geachtet werden, da ImportSendList nur in zwei Fällen aufgerufen wird:

1. Manueller Export des Artikels
1. Export des Artikels über die Artikel-Übertragung im Importer

### Funktion ImportGetAuftraegeAnzahl

In der Funktion ImportGetAuftraegeAnzahl wird ermittelt, wie viele offene Bestellungen im Shop vorhanden sind und abgeholt werden müssen. Denkbar ist das Abholen über den Status, ab einer bestimmten Bestellnummer oder aber auch über das Bestelldatum. Je nach Shopschnittstelle sind nicht alle Optionen realisierbar.

```
public function ImportGetAuftraegeAnzahl()
{
  $result = $this->getOrders($this->data);

  return count($result['data']);
}

```

### Funktion ImportGetAuftrag

Die wichtigste Grundfunktion aller Importer ist das Abholen und Übersetzen der Bestellungen aus dem Shop in das Warenkorbformat von xentral. Nachdem die Bestellung von der Shop API abgeholt wurde, werden im ersten Schritt die Adressdaten des Kunden an den Warenkorb übergeben:

```
$cart['anrede'] = 'herr';
$cart['strasse'] = $order['data']['billing']['street'];
$cart['plz'] = $order['data']['billing']['zipCode'];
$cart['ort'] = $order['data']['billing']['city'];
$cart['land'] = $order['data']['billing']['country']['iso'];
$cart['email'] = $order['data']['customer']['email'];
$cart['name'] = $order['data']['billing']['firstName']. ' '. $order['data']['billing']['lastName'];

```Falls eine abweichende Lieferadresse vorliegt, muss diese ebenfalls übergeben werden und das Feld abweichendelieferadresse ist mit true zu befüllen, um zu gewährleisten, dass der Auftrag beim richtigen Empfänger ankommt. Zudem gibt es wichtige Daten, die für die weitere Verarbeitung von Bedeutung sind.```
$cart['auftrag'] = $orderFromCollection['id'];
$cart['gesamtsumme'] = $orderFromCollection['invoiceAmount'];
$cart['transaktionsnummer'] = $orderFromCollection['transactionId'];
$cart['onlinebestellnummer'] = $orderFromCollection['number'];
...
$cart['zahlungsweise'] = $order['data']['payment']['name'];
$cart['lieferung'] = $order['data']['dispatch']['name'];
$cart['bestelldatum'] = substr($order['data']['orderTime'],0,10);
$cart['versandkostennetto'] = $order['data']['invoiceShippingNet'];

```**Gesamtsumme: ** Die Gesamtsumme des Auftrags dient als Absicherung gegen einen falsch zusammengesetzten Warenkorb. Falls Artikeldaten nicht richtig übergeben wurden oder ein Problem mit der Besteuerung auftritt, weicht die Gesamtsumme des Auftrags von der Gesamtsumme des Warenkorbs ab und die Auto-Versandoption wird für die Bestellung deaktiviert. Dadurch wird sichergestellt, dass keine Lieferung das Lager verlässt, die nicht mit der Bestellung übereinstimmt.** Transaktionsnummer: ** Die Transaktionsnummer ist für die Automatisierung des Rechnungswesens relevant und hilft, bezahlte Bestellungen zuzuordnen.** Auftrag: ** In diesem Feld wird die eindeutige Kennzeichnung des Auftrags für den Shop übergeben. Nicht jede Shop-Schnittstelle erlaubt, den Versandstatus einer Bestellung über die Bestellnummer zu ändern. Gelegentlich wird eine interne ID benötigt, die an dieser Stelle übergeben werden kann. Auf den hier übergebenen Wert wird später Bezug genommen, wenn eine Änderung des Bestellstatus aus dem Shop übermittelt wird.** Onlinebestellnummer: ** In diesem Feld ist die Bestellnummer einzupflegen. Diese erleichtert die Zuordnung und bei Rückfragen kann eine Bestellung aus dem Shop direkt einem Auftrag in xentral zugeordnet werden.** Zahlungsweise: ** Das Übertragen der Zahlungsweise erlaubt es, Einstellungen wie Autoversand, Fast-Lane oder das Anlegen von Rechnungen spezifisch für bestimmte Zahlungsweisen in xentral zu aktivieren oder zu deaktivieren.** Lieferung: ** Bei übergebener Lieferweise kann ein Matching in xentral vorgenommen werden, ähnlich wie bei der Zahlungsweise.** Versandkostenbrutto: ** Bei einer Bestellung können die Versandkosten wie ein Artikel im Warenkorb übergeben werden. Durch dieses Spezialfeld werden die Versandkosten allerdings auf den, im Importer eingestellten, Portoartikel gebucht und in den Auftrag übernommen.** Bestelldatum:** Das Bestelldatum zeigt das Datum des Bestellungseingangs an.```
foreach ($order['data']['details'] as $article)
{
  $articlearray[] = [
  'articleid' => $article['articleNumber'],
  'name' => $article['articleName'],
  'price' => $article['price'],
  'quantity' => $article['quantity']
];
}

...

$orderData =[
  'id' => $cart['auftrag'],
  'warenkorb' => base64_encode(serialize($cart)),
  'warenkorbjson' => base64_encode(json_encode($cart))
];

```

Wenn die benötigten Grunddaten der Bestellung an den Warenkorb übergeben wurden, sind die einzelnen Positionen zum Warenkorb hinzuzufügen. Im Feld articleid wird die Artikelnummer übergeben. In den anderen Feldern steht ihr jeweiliges Äquivalent aus der Bestellposition.

Nachdem der Warenkorb mit allen Daten aus der Bestellung befüllt wurde, gibt die Funktion die Daten zurück.

### Funktionen ImportDeleteAuftrag / ImportUpdateAuftrag

Die Funktion ImportDeleteAuftrag ist dafür zuständig, eine offene Bestellung als „In Bearbeitung“ zu kennzeichnen. Die Partnerfunktion ImportUpdateAuftrag kennzeichnet die Bestellung als „Versendet“.

```
public function ImportDeleteAuftrag()
{
  $orderId = $this->data['auftrag'];
  $update = [
  'orderStatusId' => 1
];

  $this->call('orders/'.$orderId, 'PUT',$update);

  return true;
}

```

## Code des Beispiels

Im Folgenden ist der gesamte Code des beschriebenen Beispiels zur eigenen Verwendung gelistet. Dieser dient als Startpunkt für die Entwicklung - ohne Gewähr für Fehlerfreiheit oder erwartete Funktionalität.

```
<?php

class Shopimporter_Shopwarespecial extends ShopimporterBase
{
  /** *@var bool*/
  public $intern = false;

  /** *@var Application*/
  public $app;

  /**@var string*/
  public $apiUrl;

  /**@var string*/
  public $apiKey;

  /**@var string*/
  public $apiUser;

  /**@var int*/
  public $shopid;

  /**@var mixed*/
  public $data;

  /** * Shopimporter_Shopwarespecial constructor. * *@param $app *@param bool $intern*/
  public function __construct($app, $intern = false)
  {
  $this->app=$app;
  $this->intern = true;
  if($intern)
  {
  return;
}
  $this->app->ActionHandlerInit($this);

  $this->app->ActionHandler('auth','ImportAuth');
  $this->app->ActionHandler('sendlist','ImportSendList');
  $this->app->ActionHandler('sendlistlager','ImportSendListLager');
  $this->app->ActionHandler('getauftraegeanzahl','ImportGetAuftraegeAnzahl');
  $this->app->ActionHandler('getauftrag','ImportGetAuftrag');
  $this->app->ActionHandler('deleteauftrag','ImportDeleteAuftrag');
  $this->app->ActionHandler('updateauftrag','ImportUpdateAuftrag');

  $this->app->DefaultActionHandler('list');
  $this->app->ActionHandlerListen($app);
}

/** *@return array*/
public function EinstellungenStruktur()
{
  return
  array(
  'felder'=>array(
  'APIUser'=>array('typ'=>'text','bezeichnung'=>'{|API User:','size'=>40),
  'APIKey'=>array('typ'=>'text','bezeichnung'=>'{|API Key|}:','size'=>40),
  'APIUrl'=>array('typ'=>'text','bezeichnung'=>'{|API Url|}:','size'=>40),
));
}

/** *@param $shopid *@param $data*/
public function getKonfig($shopid, $data)
{
  $this->shopid = $shopid;
  $this->data = $data;
  $einstellungen = $this->app->DB->Select("SELECT einstellungen_json FROM shopexport WHERE id = '$shopid' LIMIT 1");
  if($einstellungen){
  $einstellungen = json_decode($einstellungen,true);
  $this->apiUser = $einstellungen['felder']['APIUser'];
  $this->apiKey = $einstellungen['felder']['APIKey'];
  $this->apiUrl = $einstellungen['felder']['APIUrl'];
}
}

/** *@param $endpoint *@param $method*@param array $data *@param array $params* *@return bool|string*/
protected function call($endpoint, $method, $data=array(),$params=array()){
  $queryString = '';
  if (!empty($params)) {
  $queryString = '?'.http_build_query($params);
}
  $url = $this->apiUrl.$endpoint.$queryString;
  $dataString = json_encode($data);

  $curl = curl_init();
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_FOLLOWLOCATION, false);
  curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
  curl_setopt($curl, CURLOPT_USERPWD, $this->apiUser. ':'. $this->apiKey);
  curl_setopt($curl, CURLOPT_HTTPHEADER, ['Content-Type: application/json; charset=utf-8']);
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_CUSTOMREQUEST, $method);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $dataString);
  return curl_exec($curl);
}

/** *@return int*/
public function ImportSendListLager()
{
  $updatedArticles = 0;
  $tmp = $this->CatchRemoteCommand('data');
  foreach ($tmp as $article){
  $nummer = $article['nummer'];
  $lageranzahl = $article['anzahl_lager'];

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
}
  return $updatedArticles;
}

/** *@return int|string*/
public function ImportSendList()
{
  $tmp = $this->CatchRemoteCommand('data');
  $successCount = 0;

  foreach ($tmp as $article){
  $name = $article['name_de'];
  $articleNumber = $article['nummer'];
  $active =!$article['inaktiv'];
  $length = $article['laenge'];
  $width = $article['breite'];
  $height = $article['hoehe'];
  $weight = $article['gewicht'];
  $tax = $article['steuersatz'];
  $ean = $article['ean'];

  $lageranzahl = $article['anzahl_lager'];
  $laststock = $article['restmenge'];
  $supplier = $article['hersteller'];
  $supplierNumber = $article['herstellernummer'];
  $description = $article['metadescription_de'];
  $description_long = htmlspecialchars_decode($article['uebersicht_de']);
  $keywords = $article['metakeywords_de'];
  $metatitle = $article['metatitle_de'];

  $preis = $article['bruttopreis'];

  $topseller=0;
  if($article['topseller'])
  {
  $topseller=1;
}

  $prices[] = [
  'customerGroupKey' => 'EK',
  'price' => $preis
];

  $articleData = [
  'name' => $name,
  'lastStock' => $laststock,
  'tax' => $tax, // alternativ 'taxId' => 1,
  'supplier' => $supplier, // alternativ 'supplierId' => 2,
  'description' => $description,
  'descriptionLong' => $description_long,
  'keywords' => $keywords,
  'metaTitle' => $metatitle,
  'highlight' => $topseller,
  'mainDetail' => [
  'number' => $articleNumber,
  'active' => $active,
  'ean' => $ean,
  'weight' => $weight,
  'width' => $width,
  'len' => $length,
  'height' => $height,
  'supplierNumber' => $supplierNumber,
  'inStock' => $lageranzahl,
  'prices' => $prices
]
];

  $params = [
  'useNumberAsId' => true
];
  $responseJson = $this->call('articles/'.$articleNumber, 'GET',null,$params);
  $response = json_decode($responseJson,true);

  if(empty($response['data']['id'])){
  $responseJson = $this->call('articles', 'POST',$articleData);
}else{
  $responseJson = $this->call('articles/'.$articleNumber, 'PUT',$articleData,$params);
}

  $response = json_decode($responseJson,true);
  if($response['success']){
  $successCount++;
}else{
  return 'error: '.print_r($response,true);
}
}

 return $successCount;
}

 /** *@return int*/
 public function ImportGetAuftraegeAnzahl()
 {
  $result = $this->getOrders($this->data);

  return count($result['data']);
}

 /** *@return bool*/
 public function ImportUpdateAuftrag()
 {
  $orderId = $this->data['auftrag'];
  $update = [
  'orderStatusId' => 2
];

  $this->call('orders/'.$orderId, 'PUT',$update);

  return true;
}

 /** *@return bool*/
 public function ImportDeleteAuftrag()
 {
  $orderId = $this->data['auftrag'];
  $update = [
  'orderStatusId' => 1
];

  $this->call('orders/'.$orderId, 'PUT',$update);

  return true;
}

 /** *@param $data * *@return array*/
 protected function getOrders($data){
  $toNumber = $data['bis_nummer'];

  if(empty($toNumber)){
  $filter[] = [
  'property' => 'status',
  'value' => 0,
];
}else{
  $filter[] = [
  'property' => 'number',
  'expression' => '<=',
  'value' => $toNumber,
];
}

  $params = [
  'filter' => $filter
];
  $resultJson = $this->call('orders', 'GET', null, $params);
  return json_decode($resultJson,true);
}

 /** *@return array*/
 public function ImportGetAuftrag()
 {
  $result = $this->getOrders($this->data);

  $allOrders = [];
  foreach ($result['data'] as $orderFromCollection){
  $cart = [];
  $cart['auftrag'] = $orderFromCollection['id'];
  $cart['gesamtsumme'] = $orderFromCollection['invoiceAmount'];
  $cart['transaktionsnummer'] = $orderFromCollection['transactionId'];
  $cart['onlinebestellnummer'] = $orderFromCollection['number'];
  $orderJson = $this->call('orders/'.$orderFromCollection['id'],'GET');
  $order = json_decode($orderJson,true);

  $cart['anrede'] = 'herr';
  $cart['strasse'] = $order['data']['billing']['street'];
  $cart['plz'] = $order['data']['billing']['zipCode'];
  $cart['ort'] = $order['data']['billing']['city'];
  $cart['land'] = $order['data']['billing']['country']['iso'];
  $cart['email'] = $order['data']['customer']['email'];
  $cart['name'] = $order['data']['billing']['firstName']. ' '. $order['data']['billing']['lastName'];

  $cart['zahlungsweise'] = $order['data']['payment']['name'];
  $cart['lieferung'] = $order['data']['dispatch']['name'];
  $cart['bestelldatum'] = substr($order['data']['orderTime'],0,10);
  $cart['versandkostennetto'] = $order['data']['invoiceShippingNet'];

  $articlearray = [];

  foreach ($order['data']['details'] as $article)
  {
  $articlearray[] = [
  'articleid' => $article['articleNumber'],
  'name' => $article['articleName'],
  'price' => $article['price'],
  'quantity' => $article['quantity']
];
}

  $cart['articlelist']=$articlearray;

  $orderData =[
  'id' => $cart['auftrag'],
  'warenkorb' => base64_encode(serialize($cart)),
  'warenkorbjson' => base64_encode(json_encode($cart))
];

  $allOrders[] = $orderData;
}

return $allOrders;
}

 /** *@return string*/
 public function ImportAuth()
 {
  $params = ['limit' => 1];
  $responseJson =$this->call('articles','GET',null, $params);
  $response = json_decode($responseJson,true);

  if($response['success']){
  return 'success';
}

  return '';
}
}

```

## EDI-Verbindung

EDI Messages sind in Codezeilen unterteilt, in welchen genau definierte Daten übermittelt werden.

### UNB: Kommunikationspartner

Die UNB Zeile definiert unter anderem den Empfänger und Absender. Hier ist ein eindeutiges Kennzeichen für den Kommunikationspartner einzutragen. Dafür existieren verschiedene Möglichkeiten:

- Quasi-Standard ist hier eine GLN (Global Location Number, früher auch ILN) aus dem GS1 System (vormals EAN System), die in Deutschland von der GS1.de verwaltet wird. Diese GLN UNB ID Typ "14" ist jedoch nur eine von vielen Möglichkeiten.
- Für einen schnellen Start und wenn die Schnittstellte selbst entwickelt wird, kann als UNB-ID auch der Typ "9" gewählt werden. Dort wird die DUNS Nummer (auch D-U-N-S, kurz für Data Universal Numbering System) erwartet, die unter https://www.upik.de/upik_suche.cgi abgefragt werden kann. Alle Kapitalgesellschaften bekommen nach Anmeldung bei den entsprechenden Behörden automatisch eine DUNS-Nummer zugewiesen.
- Die Telefonnummer mit internationaler Vorwahl kann als UNB-ID Typ "12" verwendet werden.

### Übertragungsstandard EDI / EDIFACT

Bei EDI/EDIFACT wird nahezu alles mit Codelisten übertragen. Dafür existieren einige Quellen, die das Format erläutern und den Umgang damit aufzeigen:

- Einen guten Einstieg ist unter https://www.stylusstudio.com/edifact/ zu bekommen.
- Eine etwas kompliziertere, aber dafür sehr umfangreiche Einleitung ist unter https://service.unece.org/trade/untdid/d96a/trmd/orders_t.htm zu finden.

Die Datenübertragung erfolgt z.B. mit SFTP ausschließlich per keyfile (ssh pub-key), alternativ wird AS2 verwendet. Bei Bedarf stellt xentral einen AS2-Server bereit, hierfür ist der Vertrieb oder der Partner-Betreuer bei xentral zu kontaktieren.

Die EDI-Datei ist eine reine Textdatei, idealerweise codiert in UTF8; dies ist aber nicht zwingend im Standard vorgeschrieben. Wird eine Datei mit nur einer Zeile gesendet, kann das EDI Satzendzeichen ' (einfaches Anführungszeichen, wird im UNA Segment definiert) durch ein LF bzw. CR/LF ersetzen.

Bestimmte Segmente können in EDI mehrfach vorkommen und haben dann evtl. eine unterschiedliche Bedeutung, z.B. Daten im Kopf (Header) und auf Positions-Ebene.

### Beispiel ORDER

Es wurden einige Segmente in einer ORDER zusammengefasst um zu zeigen, wie eine ORDER zu parsen wäre.

```
BGM+220+4HQ7EBLG+9' --> Bestellung mit PO Nummer 4HQ7EBLG, 
  --> die 9 am Schluss bedeutet es werden die EAN/GS1 Codelisten verwendet
DTM+137:20190107:102' --> Belegdatum im Format 102
DTM+63:20190111:102' --> Lieferdatum spätestens im format 102
DTM+64:20190107:102' --> Lieferdatum frühstens im Format 102
Benötigt wird das GLN Verzeichnis aus dem Vendor-Central, damit die Lieferadressen zugeordnet werden können.
NAD+BY+5450534000017::9' --> Käufer, GLN Codiert
NAD+SU+4016428000009::9' --> Lieferant, hier wird die eigene UNB-ID wieder angegeben
NAD+DP+5450534002325::9+++++++DE' --> Lieferadresse mit Land
NAD+IV+5450534005838::9++AMAZON EU SARL:NIEDERLASSUNG DEUTSCHLAND+MARCEL-BREUER-STR. 12+MUENCHEN++80807+DE' 
  --> Rechnungsadresse als GLN und Klartext muss in der INVOICE Message auch komplett 
  --> im Klartext übertragen werden.

```

Im Folgenden (ab LIN) beginnen die Positionen. Zwischen NAD und LIN sind weitere Zeilen möglich, zb. RFF (Referenz jeweils zum aktuellen Element) oder CUX (hier wird die Währung definiert).

Jedes LIN definiert den Beginn einer neuen Position(LIN+1, LIN+2, LIN+3 usw.):

```
LIN+1++4016428352115:EN' --> Artikel Pos 1 mit Artikel EAN, EN=Datenherkunft EAN, könnte evtl. auch SA sein
QTY+21:52' --> Pos Menge in Stück
PRI+AAA:55.9' --> Preis pro Stück netto

```

Im Anschluss folgen Rahmendaten, die vor allem der Validierung dienen: Mit UMS+S beginnt der Summenblock, der mithilfe verschiedener Summen eine Validierung ermöglicht.

Sollten mehrere Belege einer UNB Übertragung enthalten sein, folgen diese nun durch ein UNH bzw. BGM, mit dem Belegkopf getrennt.