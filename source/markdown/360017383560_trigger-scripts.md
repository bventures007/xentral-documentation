Als Trigger Scripts werden Skripte bezeichnet, die sich an bestimmten Stellen der Software in die Geschehnisse "einklinken" und nach individuellen Gesichtspunkten Entscheidungen treffen können, die z.B. Eigenschaften eines Auftrags anpassen oder den weiteren Weg durch die Prozesse der Firma verändern.

## Arten von Triggern

Trigger Scripts existieren in zwei Formen:

- Event Trigger (Ereignis-Trigger)
- Timed Trigger (Zeitgesteuerte Trigger oder Prozessstarter)

### Event Trigger

Die Ereignis-Trigger werden an bestimmte Ereignisse gehängt, wie in den folgenden Beispielen ersichtlich wird:

- OnDocumentChange → Wenn z.B. bei einem Auftrag oder einer Rechnung eine Änderung vorgenommen wird
- OnDocumentOfferPositionChange → Wenn in einer Rechnung die Positionen der Artikel verändert werden
- OnDocumentAddressChange → Wenn in einem Beleg die Adresse verändert wird
- OnDeliverynoteStockSwapOut → Wenn ein Lieferschein ausgelagert wird
- AfterAdressCreate → Nach dem Anlegen einer neuen Adresse
- OnProductLabelPrint → Beim Ausdruck eines Artikel-Etiketts

#### Anwendungsbeispiele für Event Trigger

- Dynamische Anpassung der Versandart nach Artikelanzahl in einem Auftrag und der PLZ der Lieferadresse → OnDocumentChange triggert ein Scripts, welches die Artikelzahl, die PLZ und den günstigsten Versanddienstleister untersucht
- Gewährung eines Aktionsrabatts bei Erreichen eines Gesamtbestellwerts von € 100,- → OnDocumentOfferPositionChange wird aufgerufen, sobald die Positionen eines Auftrages verändert werden. Bei Erreichen der Schwelle für den Gesamtrabatt kann auf alle Positionen und Artikel zugegriffen werden, die Gesamtsumme berechnet sowie ein Rabattartikel hinzugefügt werden. Unter Beispiel Gesamtrabatt ist ein Beispiel dafür zu finden
- Automatische Vergabe der Rolle "Kunde" beim Anlegen einer neuen Adresse durch einen Vertriebsinnendienstmitarbeiter und der Rolle "Lieferant" bei Mitarbeitern aus dem Einkauf → AfterAdressCreate ergänzt zusätzlich zur neuen Adresse eine Rolle, je nach aktivem Benutzer des Systems (Vertrieb oder Einkauf)

So können beispielsweise Versandeinstellungen nach den Artikeln eines Auftrags oder der Lieferadresse verändert, Artikel eines Auftrages bei Vorreservierung abgespalten oder die Sonderrabatte bei der Auftragserstellung oder dem -import berechnet werden.

Trigger existieren an allen Stellen von xentral und Trigger Scripts ermöglichen die einfache Anpassung fast aller Prozesse, wie beispielsweise OnDocumentChange.

**Arbeiten mit Belegen (Documents)**

- BeforeDocumentChange, AfterDocumentChange
- OnDocumentPositionChange
- OnDocumentAddressChange
- OnDocumentAttributeChange
- OnDocumentStateChange / OnDocumentStatusChange **Arbeiten mit Stammdaten**

- BeforeProductCreate, BeforeProductChange, BeforeProductDelete, AfterProductCreate, AfterProductChange, AfterProductDelete
- BeforeAdressCreate, BeforeAdressChange, BeforeAdressDelete, AfterAdressCreate, AfterAdressChange, AfterAdressDelete
- zukünftig: BeforeUserCreate, BeforeUserChange, BeforeUserDelete, AfterUserCreate, AfterUserChange, AfterUserDelete **Arbeiten mit Produktionen**

- BeforeProductionCreate, BeforeProductionEdit, BeforeProductionDelete, AfterProductionCreate, AfterProductionEdit, AfterProductionDelete
- OnProductionStart, OnProductionFinish
- OnProductionStockSwapOut, OnProductionStockSwapIn **Prozess-Trigger**

- Versandzentrum: OnShipment, OnAutoShipmentManuelStart, OnAutoShipmentPlusStart
- Frankierung: BeforeStampCreate, AfterStampCreate
- Scan der Trackingnummer: BeforeTrackingScan, AfterTrackingScan,
- Lager: OnStockChange, OnStockSwapOut, OnStockSwapIn, OnDeliverynoteStockSwapOut
- Drucken: OnPrint, OnLabelPrint, OnDocumentPrint, OnDocumentDeliveryNotePrint, OnDocumentInvoicePrint, OnDocumentOfferPrint, OnDocumentOrderPrint
- E-Mail-Versand: OnEmailSend, OnDocumentEmailSend, OnDocumentDeliveryNoteEmailSend, OnDocumentInvoiceEmailSend, OnDocumentOfferEmailSend, OnDocumentOrderEmailSend
- Benutzeraktionen: (zukünftig) OnUserAction
- Benutzer-Session: (zukünftig) OnSessionStart, OnSessionEnd / OnSessionClose
- Wareneingang: OnIncomingGoodsDocumentStart, OnIncomingGoodsDocumentEnd, OnIncomingGoodsArticleStart, OnIncomingGoodsArticleEnd

### Timed Trigger

Timed Trigger (auch Prozessstarter) ermöglichen es, zeitgesteuerte Aktionen durchzuführen. Diese können periodisch (z.B. alle 15 Minuten, jede Stunde, alle 3 Tage) oder zu bestimmten Zeiten (z.B. sonntags, 8:30 Uhr) ausgeführt werden.

#### Anwendungsbeispiele für Timed Trigger

- Jede Nacht wird eine Liste von Adressen erstellt, die weder als Kunde noch als Lieferant markiert sind, und eine Aufgabe, z.B. Prüfung und Bearbeitung der Fälle, für die Verwaltung angelegt.
- Einmal pro Woche wird eine Liste erstellt, die alle Aufträge anzeigt, die noch nicht vollständig abgerechnet sind. Diese Liste wird als E-Mail gesendet.

## Arbeiten mit Belegen (Event Trigger)

Mithilfe von Trigger Scripts können alle Daten eines Belegs (z.B. eines Auftrags) verändert werden. Dazu gehören z.B. die Veränderung von Positionen, Preisen, Beschreibungen, Rabatten und Versand- oder Zahlungsoptionen.

Basis in diesem Beispiel ist das Event OnDocumentPositionChange. Hierbei werden die Daten angepasst und anschließend die normale Funktionalität der Funktion ausgeführt, um das Standardverhalten von xentral für die nicht veränderten Abläufe zu nutzen.

Vorgehensweise vor Version 20.1: Überschreiben der Funktion ANABREGSNeuberechnen()) in der Klasse ERPApi, die hierfür überladen werden kann.

### Ausführungszeitpunkt

Diese Funktion wird aufgerufen, wenn das Dokument nicht schreibgeschützt ist und verändert wird. Das gilt u.a. wenn:

- Ein Beleg angelegt wird, auch beim Import aus einer Shop-Schnittstelle oder über EDI / Übertragen-Modul
- Ein API-Aufruf den Beleg verändert
- Positionen des Belegs verändert werden
- Stammdaten des Belegs geändert werden

### Belegarten

Die Funktion erhält zwei Parameter:

- $art: Die Art des Belegs → Angebote (angebot), Auftrag (auftrag), Rechnung (rechnung), Gutschrift (gutschrift)
- $id: Die Datenbank-ID des Belegs

Auf allen Werten des Belegs kann frei gearbeitet werden und alle Daten in dieser Methode manipuliert werden. Dazu sollten vorzugsweise die ERP-eigenen Funktionen verwendet werden (siehe Fragen zur Programmierung). Das direkte Arbeiten auf der Datenbank ist aber ebenfalls möglich.

> **Anmerkung**
>
> Die Methode dient der Anpassung des entsprechenden Belegs und sollte daher auch nur für diesen Zweck verwendet werden, um unerwartetes Verhalten der Software zu vermeiden. So ist es z.B. für einen Benutzer nicht nachvollziehbar, wenn sich durch die Arbeit an einem Auftrag die Stammdaten der Kundenadresse ändern würden. Bei Belegdaten sollte sich auf die DB-Tabellen beschränkt werden, vor allem bzgl. der Schreibzugriffe. Die entsprechenden Tabellen lauten:
>
> - auftrag
> - auftrag_positionen
> - rechnung
> - rechnung_positionen
> - lieferschein
> - lieferschein_positionen
> - gutschrift
> - gutschrift_positionen

Eine Übersicht der wichtigsten DB-Tabellen aus diesem Bereich ist unter Datenbank-Diagramm Belege4 und wichtigste Relationen zu finden.

### Vorgehensweise & Beispiel ''class.erpapi_custom.php''

Um die Funktion zu überladen, muss lediglich eine Datei class.erpapi_custom.php erzeugt und im Verzeichnis www/lib/ neben der Datei class.erpapi.php abgelegt werden.

Diese Information benötigst du nur bei selbständigem Hosten. Für Cloud Kunden hinterlegt Xentral die Datei auf dem Server.

Dafür brauchst du die PHP des Skriptes, den Ort, wo es abgelegt werden soll, und die gültige Lizenz der Instanz.

### Beispiel: Gesamtrabatt

Das folgende Beispiel zeigt eine einfache Anwendung: Ab einer Gesamtsumme von EUR 100,- ($threshold, Wert netto) soll automatisch ein Rabattartikel ($rebateId) eingefügt werden. Dieser kann nur wieder gelöscht werden, wenn die Summe unter EUR 100,- sinkt, andernfalls wird er bei jeder Berechnung neu erzeugt. Der Rabatt soll dabei nicht in die Gesamtsumme eingerechnet werden, diese kann also auch unter EUR 100,- fallen.

Das Beispiel zeigt die Überladung der Funktion ANABREGSNeuberechnen()

- die Einschränkung auf Belegarten (siehe Sample 1),
- die Verwendung der Artikelpositionen mit Artikel und Preis,
- die Verwendung von Datenbank (siehe Sample 2),
- die Verwendung von ERP-Funktionen (siehe Sample 3 und Sample 4)
  Zum Debugging können verschiedene Methoden angewendet werden, siehe Debugging bei der Entwicklung in xentral.

#### Code

```
  <?php

class erpAPICustom extends erpAPI
{
  public function __construct(&$app)
  {
  $this->app = $app;
  parent::__construct($app);
} // end of constructor

  public function ANABREGSNeuberechnen($id, $art, $bool = false)
  {
  /*Choose the documents you want to manipulate - Sample 1*/
  if($art === 'auftrag') {

  /*Custom definitions here*/
  $rebateId = 15; /*Set rebate article ID %*/
  $threshold = 100; /*Activate rebate for orders above EUR 100,-*/
  $rebateExists = false; /*Assume rebate article not yet added*/

  /*Get some information about positions from database - Sample 2*/
  $positionenSQL = sprintf('SELECT ap.* FROM %s_position ap WHERE %s = %s', $art, $art, $id);
  $positionen = $this->app->DB->SelectArr($positionenSQL);

  /*Walk through positions and compute the price*/
  $sum = 0;
  foreach ($positionen as $p) {
  $artikelId = $p['artikel'];
  $menge = $p['menge'];

  if ((int)$artikelId!== $rebateId) {
  $sum += $this->app->erp->GetVerkaufspreis($artikelId, $menge) *$menge; /* Sample 3*/
} else {
  $rebateExists = true;
}
} // end of foreach

  if ($sum >= $threshold &&!$rebateExists) {
  /*Sample 4*/
  $this->app->erp->AddAuftragPositionManuell($id, $rebateId, 0, 1, 'Rabatt ab € '.$this->app->erp->formatMoney($threshold, 'EUR'));
} // end of if - add rebate if not exists
} // end of if - Document type: Offer / Auftrag

  /*Call the main routine from parent class erpAPI and return*/
  return parent::ANABREGSNeuberechnen($id, $art);
} // end of function

} // end of class

  
```

#### Ergebnis

Im Ergebnis passt sich dann die Positionstabelle folgendermaßen an:

![TriggerScript-1.png](https://help.xentral.com/hc/article_attachments/4996392886556)

Und der Beleg hat entsprechend ebenfalls ein anderes Erscheinungsbild:

![Trigger2.png](https://help.xentral.com/hc/article_attachments/4996407862044)

#### Beispiel: Schweizer Rappen-Rundung

In der Schweiz sind 1 und 2 Rappenmünzen nicht mehr im Umlauf. Daher runden Einzelhändler auf 5 oder 10 Rappen auf oder ab, wobei mathematische Rundungsgereln gelten. Dabei bezieht sich die Rundung im Normalfall auf den Gesamtbetrag.

Mit Hilfe der Funktion ANABREGSNeuberechnen() kann diese Rundung umgesetzt werden. Dazu muss der Gesamtbetrag in zwei Feldern gespeichert werden:

- extsoll
- gesamtsumme **Weitere Ideen für Projekte:**

- Besonderer Preis oder Rabatt ab einer definierten Gesamtmenge
- Kombination verschiedener Artikel oder ganzer Artikelkategorien in einer Rabattstaffelung
- "Zahle x bekomme y"
- Gesamt-Rabatt ab x Euro (siehe Beispiel oben)
- Versandkostenfrei ab x Euro
- Verwendung besonderer Erlöskonten nach bestimmten Kriterien
- Anpassung der Versandart oder -kosten nach Zielgebiet, Positionen, Gesamtgewicht o.ä.
- Besondere Rundungen (siehe Beispiel Schweizer Rappen-Rundung)

#### Beispiel: Lieferschein auslagern

Mit der Methode LieferscheinAuslagern wird der Lagerbestand angepasst. Den Algorithmus kann dafür selbst entwickelt werden. Die ID des Lieferscheins erscheint primär als Parameter. Es können dann die Positionen aus der Datenbank abgefragt werden (ArtikelID und Menge), um im Lager in der Tabelle lager_platz_inhalt die korrekten Mengen zu entnehmen.

##### Code

```function LieferscheinAuslagern($lieferschein,$anzeige_lagerplaetze_in_lieferschein=false, $standardlager = 0, $belegtyp = 'lieferschein', $chargenmhdnachprojekt = 0, $forceseriennummerngeliefertsetzen = false,$nurrestmenge = false, $lager_platz_vpe = 0, $lpiid = 0)```

Die Funktion bekommt Werte aus dem System übergeben, die bei der Einrichtung vom Einrichter oder dem xentral Onboarding-Team festgelegt wurden. Diese übergebenen Werte können innerhalb der Funktion ausgewertet werden:

- $lieferschein: ID des Lieferscheins
- $anzeige_lagerplaetze_in_lieferschein: Anzeige der Lagerplätze im Lieferschein (System-Einstellung)
- $standardlager: Standardlager (System-Einstellung), Defaultwert ist 0
- $belegtyp - Typ des Beleges, Default ist 'lieferschein'
- $chargenmhdnachprojekt: Nur zur Verwendung durch xentral (System-Einstellung)
- $forceseriennummerngeliefertsetzen: Nur zur Verwendung durch xentral (System-Einstellung)
- $nurrestmenge: Nur zur Verwendung durch xentral (System-Einstellung)
- $lager_platz_vpe: Nur zur Verwendung durch xentral (System-Einstellung)
- $lpiid: Nur zur Verwendung durch xentral (System-Einstellung)

Nun werden die eigentlichen Entnahmen aus dem Lager vorgenommen, mithilfe der Funktion LagerAuslagernRegal.

Aufruf:

```function LagerAuslagernRegal($artikel,$regal,$menge,$projekt,$grund,$importer="", $doctype = "", $doctypeid = 0, $lager_platz_vpe = 0, $lpiid = 0)```

Beschreibung der Parameter:

- $artikel: Artikel ID
- $regal: Lagerplatz ID, aus welchem entnommen wird
- $menge: Menge, welche entnommenen wird
- $projekt: Projekt für Lagerbewegung
- $grund: Bemerkung für Lagerbewegungstabelle
- $importer: Aktuelle Wert aus Prozess wird übergeben - aktuell leer lassen, Default ist Leerstring
- $doctype: Optionale Angabe für welchen Beleg entlagert wird, Defaultwert ist Leerstring
- $doctypeid: Optionale Angabe für welchen Beleg (ID des Beleges) entlagert wird, Defaultwert ist 0
- $lager_platz_vpe: Optional Angabe, welche VPE ausgelagert wird, Defaultwert ist 0. Diese Angabe wird aktuell nur für Amazon verwendet
- $lpiid: Optional: Aktueller Wert aus Prozess wird hier übergeben - aktuell wird 0 übergeben. Defaultwert ist 0

## Timed Trigger

Timed Trigger bezeichnen individuelle Prozessstarter, die integriert werden können, um Datenanalysen, Datenmanipulationen oder andere datenbankbasierte Aktionen auszuführen. Dabei kann sowohl direkt in die Datenbank geschrieben als auch externe Funktionen (wie z.B. API-Calls) aufgerufen werden.

### Allgemein

Alle Timed Trigger (Prozessstarter) liegen in dem Verzeichnis../xentral/cronjobs.

Der Hauptprozess (starter2.php) wird jede Minute vom Heartbeat-Cronjob (system cronjob) aufgerufen. Die starter2.php prüft alle Einträge der Datenbanktabelle prozessstarter und führt die Prozesse aus, die laut ihrer Zeitpunkts- bzw. Periodeneinstellung an der Reihe sind (siehe[Handbuch Prozessstarter](#)).

### Timed Trigger anlegen

1. Die PHP Datei für den Prozessstarter Code im Ordner../xentral/cronjobs ist zu erstellen
1. Für den Dateinamen sind nur ASCII Zeichen zu verwenden, Leerzeichen sind zu vermeiden
1. Folgende Navigation ist in der xentral Oberfläche vorzunehmen: Administration → Einstellungen → Prozessstarter. Ein neuer Eintrag ist zu erzeugen, dabei die Zeitpunkt- / Periodeneinstellung für den Prozess sinnvoll festzulegen
1. In das Feld "Parameter" ist der Name der PHP Datei ohne Dateiendung einzutragen. Anhand dieses Parameters wird die starter2.php die auszuführende PHP Datei im cronjob Ordner suchen und ausführen

### Timed Trigger manuell ausführen

Während der Entwicklung muss der Prozessstarter normalerweise mehrmals zu Testzwecken manuell gestartet werden.

Folgende Vorgehensweise hat sich dabei bewährt:

- Keine Arbeit im Live-System, andernfalls haben die weiteren Punkte ggf. negative Auswirkungen
- Es ist sicher zu stellen, dass für das Entwicklungssystem kein Heartbeat-Cronjob registriert ist
- Alle Prozessstarter sind auf inaktiv zu schalten, bis auf denjenigen, der bearbeitet wird
- Folgende Einstellungen sind für den zu bearbeitenden Prozessstarter zu setzen:
  - Art: periodisch
  - Periode: 0
- Die starter2.php im cronjob Ordner sind über eine Kommandozeile zu starten, z.B. über das Kommando php starter2.php

### Code schreiben

#### Beispiel: BMEcat-Export zum Update veränderter Artikel

Das folgende Beispiel erstellt zeitgesteuert einen Export der Produktdaten im BMEcat-Format, einem standardisierten Austauschformat für Katalogdaten im Katalogmanagement (siehe auch[BMEcat auf Wikipedia)](https://de.wikipedia.org/wiki/BMEcat). Dabei werden gezielt veränderte Artikel im Update-Format exportiert und nur Artikel gewählt, die seit dem letzten Ausführen des CRON-Jobs verändert wurden. In diesem Beispiel werden dafür nur Veränderungen an den Stammdaten der Artikel berücksichtigt, nicht aber z.B. veränderte Verkaufspreise.

```
  <?php

use Xentral\Components\Database\Exception\QueryFailureException;
use Xentral\Components\Filesystem\Filesystem;
use Xentral\Components\Filesystem\FilesystemFactory;
use Xentral\Components\Util\StringUtil;

//predefined variables:

/**@var Application $app * access to services and functions(e.g. Database, erpAPI, PHPMail...)*/

/**@var array $task * information about all current executed cronjobs*/

/**@var int $task_index * index of current cronjob in $task array*/

//information about the current running cronjob
$jobInfo = $task[$task_index];

//get the time of the last execution of this cronjob
$lastExec = $jobInfo['letzteausfuerhung'];

//it makes sense to keep some settings flexible (e.g. for test environment)
$outputDir = '';

$exportObject = new BmecatExportCronjob($app, $lastExec, $outputDir);
$exportObject->execute();

final class BmecatExportCronjob
{
  /**@var erpooSystem $app*/
  private $app;

  /**@var array $data*/
  private $data;

  /**@var string $lastExecution*/
  private $lastExecution;

  /**@var SimpleXMLElement $xml*/
  private $xml;

  /**@var string $outputDirectory*/
  private $outputDirectory;

  /**@var bool $debugMode*/
  private $debugMode = true; //set to false for production usage

  /** *@param erpooSystem $app *@param string $lastExecution*@param string $outputDirectory*/
  public function __construct($app, $lastExecution, $outputDirectory = '')
  {
  $this->app = $app;
  $this->lastExecution = $lastExecution;
  if ($outputDirectory!== '') {
  $this->outputDirectory = $outputDirectory;
} else {
  //get the userdata directory of Xentral as default value for output directory
  $this->outputDirectory = $app->Conf->WFuserdata;
}
}

  /** * Collects data for the BMECAT export and writes the result to a file * *@throws Exception * *@return void*/
  public function execute()
  {
  $this->app->erp->LogFile('BMECAT_export started', __FILE__);

  //collect data for the export
  $this->data['header'] = $this->getHeader();
  $articles = $this->getArticles();

  //if there are no changed articles we leave a hint in the logfile and exit cleanly
  if (empty($articles)) {
  $this->app->erp->LogFile('BMECAT_export: No changed articles since last execution.');

  return;
}

  $this->data['t_update_products']['_attr_prev_version'] = '0';
  $this->data['t_update_products']['article'] = $articles;

  //render the XML string according to BMECAT specs
  $this->xml = $this->toXml();

  //It is good practice to use filenames with timestamps for output to avoid colliding results
  $date = new DateTime('now');
  $filename = sprintf('bmecat_export_%s.xml', $date->format('Y-m-d_H_i_s'));

  //write the XML content to a file
  $this->writeXmlFile($this->xml, $filename);

  $this->app->erp->LogFile('BMECAT_export completed');
}

  /** * Write the xml string to a file in the userdata directory * * uses Xentral FileSystem class to write the file. * *@param string $xml *@param string $filename*/
  private function writeXmlFile($xml, $filename)
  {
  $path = sprintf('%s/%s', $this->outputDirectory, $filename);
  $this->debug('BMECAT_export write xml file', $path);

  //we do not want to overwrite old export files
  if (file_exists($path)) {
  throw new RuntimeException(sprintf('BMECAT_export Cannot overwrite file %s', $path));
}

  /**@var FilesystemFactory $factory*/
  $factory = $this->app->Container->get('FilesystemFactory');
  /**@var Filesystem $fileSystem*/
  $fileSystem = $factory->createLocal('/');
  $fileSystem->write($path, $xml);
}

  /** * transforms the data to xml string * *@return string*/
  private function toXml()
  {
  $xml = new SimpleXMLElement('<BMECAT/>');
  $xml->addAttribute('version', '1.2');
  $this->appendXmlRecursive($xml, $this->data);

  return $xml->asXML();
}

  /** * walks through the data recursively and buidls the data structure for bmecat * *@param SimpleXMLElement $startnode *@param array $data*@param string $parentName*/
  private function appendXmlRecursive(SimpleXMLElement $startnode, $data, $parentName = '')
  {
  foreach ($data as $name => $value) {
  if ($parentName!== '') {
  $name = $parentName;
}
  if (is_array($value)) {
  if (count(array_filter(array_keys($value), 'is_string')) === 0) {
  $this->appendXmlRecursive($startnode, $value, $name);
} else {
  $child = $startnode->addChild(mb_strtoupper($name), '');
  $this->appendXmlRecursive($child, $value);
}
} else {
  if (StringUtil::startsWith($name, '_attr_')) {
  $startnode->addAttribute(substr($name, 6), $value);
} else {
  $startnode->addChild(mb_strtoupper($name), $value);
}
}
}
}

  /** * collects necessary data for the bmecat header * *@throws Exception * *@return array*/
  private function getHeader()
  {
  $header = [];
  $header['generator_info'] = 'Xentral custom cronjob';
  $date = new DateTime('now');
  $header['catalog'] = [
  'language' => 'deu',
  'catalog_id' => 'standard_endkunden_katalog',
  'catalog_version' => '001.001',
  'datetime' => [
  '_attr_type' => 'generation_date',
  'date' => $date->format('Y-m-d'),
  'time' => $date->format('H:i:s'),
],
];
  $header['supplier'] = ['suppliername' => $this->app->erp- >Firmendaten('footer_0_1')];

  return $header;
}

  /** * collects data about changed articles * *@return array*/
  private function getArticles()
  {
  $data = [];
  //this query gets all articles that were edited since the cronjob's last execution
  $sql = sprintf(
  "SELECT a.id, a.typ, a.nummer, a.ean, a.name_de, a.katalogbezeichnung_de, a.katalogtext_de, 
  a.hersteller, a.herstellernummer
  FROM artikel AS a 
  WHERE a.useredittimestamp > '%s' AND a.katalog = 1",
  $this->lastExecution
);

  $articles = $this->app->DB->SelectArr($sql);

  $dbError = $this->app->DB->error();
  if (!empty($dbError)) {
  //this is a critical error, the cronjob can not continue
  //so log the error message and quit the cronjob with an error by throwing an exception
  $this->app->erp->LogFile('BMECAT_export article query failed', $this->app->DB->real_escape_string($sql));
  $this->app->erp->LogFile('BMECAT_export DB error', $this->app->DB->real_escape_string($dbError));

  throw new QueryFailureException('database query failed');
}

  if (empty($articles)) {
  return [];
}

  $this->debug(sprintf('BMECAT_export %s changed articles found', count($articles)));

  foreach ($articles as $article) {
  $item = [];
  $item['_attr_mode'] = 'update';
  $item['supplier_aid'] = $article['nummer'];
  $item['article_details']['description_short'] = $article['katalogbezeichnung_de'];
  $item['article_details']['description_long'] = $article['katalogtext_de'];
  if ($article['ean']!== '') {
  $item['article_details']['ean'] = $article['ean'];
}
  if ($article['herstellernummer']!== '') {
  $item['article_details']['manufacturer_aid'] = $article['herstellernummer'];
}
  if ($article['hersteller']!== '') {
  $item['article_details']['manufacturer_name'] = $article['hersteller'];
}
  $prices = $this->getPrices((int)$article['id']);
  foreach ($prices as $price) {
  $item['article_price_details']['article_price'][] = [
  'price_amount' => $price['preis'],
  'price_currency' => $price['waehrung'],
];
}
  $data[] = $item;
}

  return $data;
}

  /** * Gets currently active prices of one article * *@param int $articleId * *@return array*/
  private function getPrices($articleId)
  {
  $this->debug('get prices for article', $articleId);
  //this query gets all prices of the specified article that are active on the current date
  $sql = sprintf(
  "SELECT p.preis, p.waehrung, p.ab_menge
  FROM verkaufspreise AS p
  WHERE p.art = 'kunde' AND p.adresse = 0 AND p.geloescht = 0
  AND (p.gueltig_bis = '0000-00-00' OR curdate() <= p.gueltig_bis OR isnull(gueltig_bis))
  AND (p.gueltig_ab = '0000-00-00' OR curdate() >= p.gueltig_ab OR isnull(gueltig_ab))
  AND p.artikel = %s
  ORDER BY p.ab_menge",
  $articleId
);

  $prices = $this->app->DB->SelectArr($sql);

  $dbError = $this->app->DB->error();
  if (!empty($dbError)) {
  //this is a noncritical error, the cronjob can still continue, just log the error message
  $this->app->erp->LogFile('BMECAT_export price query failed', $this->app->DB->real_escape_string($sql));
  $this->app->erp->LogFile('BMECAT_export DB error', $this->app->DB->real_escape_string($dbError));
}

  if (empty($prices)) {
  return [];
}

  return $prices;
}

  /** * Prints log message to logfile table * (only if debug mode is enabled)* *@param string $message *@param mixed|null $dump*/
  private function debug($message, $dump = null)
  {
  if ($this->debugMode === true) {
  $this->app->erp->LogFile($message, $dump);
}
}
}

  
```

#### Beispiel: BMEcat-Export zum Update veränderter Artikel

Das folgende Beispiel zeigt die Erstellung eines Dateianhangs an einen Beleg. Dieses Code-Beispiel registriert sich auf den Trigger bei Änderung eines Beleges und erstellt eine Datei, die dann als Anhang den Beleg erweitern kann. In xentral existieren dazu z.B. zusätzliche Einzahlungsscheine bei Rechnungserstellung oder Gefahrgutdeklarationen, die nach diesem Muster im Systen verankert wurden. Denkbar ist aber jede Art von Dateianhang. Solange die Datei als **Typ Anhang** hinterlegt wird, kann diese durch eine geeignete Konfiguration in den Projekteinstellungen automatisch mit der Rechnung gesendet oder beim Rechnungsdruck zusätzlich ausgedruckt werden.

### Integration in Xentral

1. Die Datei ist im Ordner www/pages zu speichern
1. Der Dateiname muss aus Kleinbuchstaben bestehen
1. Der Klassenname muss mit einem Großbuchstaben beginnen, der Rest sind Kleinbuchstaben
1. Wenn die Datei am Zielort liegt, muss diese einmal aufgerufen werden, damit der Hook registriert wird - im vorliegenden Fall also: index.php?module=beispiel
1. Auf der Seite selbst hat xentral im Beispiel noch eine Checkbox eingebaut, mit der man die hinterlegte Logik an- und ausschalten kann. Beim ersten Aufruf ist einmalig der Haken zu setzen. Dieser wird automatisch gespeichert - daher ist kein Speichern-Button nötig.

### Beispiel-Code

```
  <?php

// TODO Wichtig! Nur der erste Buchstabe gross, kein CamelCase; 
// Der Name der Datei selbst muss klein geschrieben sein, also hier beispiel.php
class Beispiel
{

  /**@var erpooSystem $app*/
  public $app;

  /** *@param erpooSystem $app *@param bool $intern*/
  public function __construct($app, $intern = false)
  {
  $this->app = $app;
  if($intern){
  return;
}

  $this->app->ActionHandlerInit($this);
  $this->app->ActionHandler('list','Liste');
  $this->app->DefaultActionHandler('list');
  $this->app->ActionHandlerListen($app);
}

  public function Liste()
  {
  $this->Install();
  $this->app->YUI->AutoSaveKonfiguration('belegeanhangerzeugen', 'belegeanhangerzeugen');

  $belegeanhangerzeugen = $this->app->erp->GetKonfiguration('belegeanhangerzeugen');

  $checked = '';
  if(!empty($belegeanhangerzeugen)){
  $checked = 'checked=""';
}
  $this->app->Tpl->Set('TAB1','Automatisch eine Anhangsdatei für Belege erzeugen:
 <input type="checkbox" name="belegeanhangerzeugen" id="belegeanhangerzeugen" '.$checked.'>');

  $this->app->Tpl->Parse('PAGE','tabview.tpl');
}

  public function Install()
  {
  $modulName = 'beispiel'; // TODO frei vergebbar, sollte nach dem ersten Mal aber nicht mehr verändert werden; z.b. Klassenname mit Kleinbuchstaben
  $this->app->erp->RegisterHook('ANABREGSNeuberechnenEnde', $modulName, 'createDocument');
}

  public function createFile($tmpPath,$documentId, $documentType)
  {
  $belegId = (int)$documentId;
  $beleg = $this->app->DB->SelectRow(
  "SELECT *
  FROM {$documentType} AS r
  WHERE r.id = '{$belegId}'"
);
  if (empty($beleg)) {
  return;
}

  // TODO
  /* * Hier wird die eigentliche Datei im z.b. temp-Verzeichnis erzeugt * */
}

  public function createDocument($documentId, $documentType)
  {
  if(
  $documentType == 'auftrag' ||
  empty($documentId) ||
  $this->app->erp->GetKonfiguration('belegeanhangerzeugen')!=='on'
){
  return;
}

  $tmpPath = ''; // TODO z.b. tempnam(sys_get_temp_dir(), 'beleg'). '.csv'
  $this->createFile($tmpPath,$documentId, $documentType); // TODO
  $fileTitle = ''; // TODO
  $fileDesc = ''; // TODO
  $fileName = ''; // TODO
  $fileHash = ''; // TODO z.b. md5(serialize($belegDatenObjekt));
  $bearbeiter = $this->app->User->GetName();

  // Prüfen ob vorher schon mal eine Datei zu Beleg generiert wurde
  $dateiCheck = $this->app->DB->SelectArr(sprintf(
  "SELECT d.id AS datei_id, dv.bemerkung AS datei_hash
  FROM datei AS d
  INNER JOIN datei_stichwoerter AS ds ON d.id = ds.datei
  INNER JOIN datei_version AS dv ON d.id = dv.datei
  WHERE ds.subjekt = 'anhang' AND ds.objekt = '%s'
  AND d.titel = '%s' AND ds.parameter = '%s'
  AND d.geloescht = 0
  ORDER BY dv.id DESC
  LIMIT 1",
  $documentType, $fileTitle, $documentId
));
  $dateiId = (int)$dateiCheck[0]['datei_id'];
  $dateiHash = $dateiCheck[0]['datei_hash'];

  if($dateiId > 0){
  // Beleg ist vorhanden > Prüfen ob sich der Inhalt geändert hat
  if($dateiHash!== $fileHash){
  // Hash in Bemerkungsfeld hat sich geändert > Neue Datei-Version hinterlegen
  // Hash stellt sicher dass Inhalte identisch sind.
  $this->app->erp->AddDateiVersion($dateiId, $bearbeiter, $fileName, $fileHash, $tmpPath);
}
}
  else{
  // Datei nicht vorhanden > Datei als Anhang zum Beleg anlegen
  $dateiId = $this->app->erp->CreateDatei($fileName, $fileTitle, $fileDesc, '', $tmpPath, $bearbeiter);
  $this->app->erp->AddDateiStichwort($dateiId, 'anhang', $documentType, $documentId);
}
}
}

  
```

### Variablen

Innerhalb des Prozesses sind einige Variablen gesetzt, die nützliche Informationen und Funktionen liefern:

- $app: Zugang zu verschiedenen Services
  - $app->DB Klasse DB: Zugriffe auf die xentral Datenbank
  - $app->Conf Klasse Config: Zugriff auf Datenbankverbindungsdaten und userdata Verzeichnis (z.B. um Ergebnisdateien dort zu speichern)
  - $app->Container Klasse ServiceContainer: Zugriff auf weitere Services, z.B. FileSystem)
  - $app->erp Klasse erpAPI: Zugriff auf alle funktionen der erpAPI. Hier sind vorgefertigte Datenbankabfragen und Hilfsfunktionen zu finden.
  - $app->mail Klasse PHPMailer: Zugriff auf E-Mail Funktionen, um z.B. nach erfolgreicher Ausführung eine Benachrichtigung per E-Mail an den Administrator zu schicken

### Best Practice, Tipps, Tricks

- Eine Klasse für die Programmlogik des Prozessstarters ist zu erstellen und der prozedurale Code so klein wie möglich zu halten
- Mit der Funktion $app->erp->LogFile() werden Lognachrichten in der Tabelle Logfile erzeugt.
- Eine Variable ist zu setzen, mit welcher die Ausgabe detaillierter Lognachrichten an- und ausgeschaltet werden kann, um im Live-Betrieb Ressourcen zu schonen
- Wird eine Exception geworfen, die der Prozessstarter nicht selbst behandelt, so wird der Prozessstarter in der Übersicht als fehlerhaft markiert und in der Tabelle logfile ist die Fehlermeldung einzusehen. Beispiel Fehler im Logfile: Prozessstarter Fehler bei Aufruf des Moduls bmecatexportarticles: Cant write XML file
- Diese Mechanik kann ausgenutzt und eigene Exceptions geworfen werden, wenn z.B. wichtige Bedingungen für den Prozess nicht erfüllt sind oder ein kritischer Fehler auftritt.

### Weitere Links:

- [Übersicht Handbuch Anpassungen](https://help.xentral.com/hc/articles/360017383080#UUID-bb6076c2-8277-a8ea-502e-0c1c3dff9adf)

Wir freuen uns auch auf Ideen, Anregungen und Code-Beispiele in unserer Community:

[https://xentral.community](https://xentral.community)