Im Folgenden wird erklärt, wie eine CSV-Datei per Kommandozeile eingelesen werden kann.

Sowohl das PHP Script als auch die CSV-Datei liegen in diesem Beispiel im Ordner Importer des xentral Ordners.

## Kopf des Scripts

Damit das Script auf die eigenen Funktionen von xentral zugreifen kann, müssen ein paar Klassen eingebunden und Objekte erstellt werden. Dies geschieht mit folgendem Code:

```
<?php
// Report simple errors only

error_reporting(E_ERROR | E_WARNING | E_PARSE);

include_once("../conf/main.conf.php");
include_once("../phpwf/plugins/class.mysql.php");
include_once("../phpwf/plugins/class.string.php");
include_once("../phpwf/plugins/class.user.php");
include_once("../www/lib/class.erpapi.php");

class app_t {
 var $DB;
 var $String;
 var $User;
}

$app = new app_t();
$app->User = new User($app);
$conf = new Config();
$app->DB = new DB($conf->WFdbhost,$conf->WFdbname,$conf->WFdbuser,$conf->WFdbpass);
$app->string = new string();
$erp = new erpAPI($app);
$app->erp = $erp;
```

## Parameter übergeben

Wird in der Konsole ein Script aufgerufen mit

```php script.php file```werden die Parameter in das Array $argv gespeichert. Es ist sinnvoll zu prüfen, ob überhaupt ein Parameter gegeben ist und ob die im Aufruf angegebene Datei existiert:```
if(!isset($argv[1]))
{
  the("No file specified for import");
}
if(!file_exists($argv[1]))
{
  the("file ".$argv[1]." does not exist");
}
if(!is_file($argv[1]))
{
  the($argv[1]." is not a file");
}
```

## Einlesen der Datei

Hier wird gezeigt, wie die Datei eingelesen werden kann:

```
$csvimport = new CSVImport($app, $argv[1]);

class CSVImport
{
 var $app;
 var $file;

 function __construct(&$app, $file)
 {
  $this->app = $app;
  $this->file = $file;

}

 function read()
 {
  if($this->file && file_exists($this->file) && is_file($this->file))
  {
  if (($handle = fopen($this->file, "r"))!== FALSE) {
  $row = 0;
  while (($csv = fgetcsv($handle, 0, ";"))!== FALSE) {
  //$line = iconv("ISO-8859-1", "UTF-8", $line); //If script is stored in UTF-8 and CSVin ANSI the string will be converted
  foreach($csv as $k => $el)$csv[$k] = iconv("ISO-8859-1","UTF-8", $el);
  $row++;
  //$csv = str_getcsv($line,"\t","\""); //When CSVis tab delimited and individual elements are enclosed with ".
  //$csv = str_getcsv($line, ";",""); //separated with;.
  if($row < 5) { //If the header of the file has 4 lines this can be used for debugging e.g. 

} else {
  //From here on the actual data will be processed

  $this->process($csv);

}
}
}
} else {
  return false;
}
}
 function process(&$csv)
 {
  //Process the individual data

...
}
}
```

## Verarbeiten der Daten mit Wawifunktionen

Die erpAPI-Klasse bietet viele Funktionen zum Import bzw. zum Verarbeiten der Daten. Im vorliegenden Beispiel wird der Import von Artikeln erklärt:

```
function process(&$csv){//Process the individual data
if($csv[30]){$data['number']=$csv[2];//If article number is 3rd column$data['name_en']=$csv[0];//If article name is in first column$data['short_text_en']=$csv[22];/*$data['description_en'] =....
  $data['manufacturer'] =...
  $data['manufacturer_link'] =...*/$data['weight']=$csv[48];if($scv[32]=='D1')$data['sales-tax']='ermaessigt';//data will be saved with the erpAPI
$artikelid=true;$artikelid=$this->app->erp->InsertUpdateArticle($data);//Now the sales prices
$pricegross=$csv[30];$nettoprice=$pricegross/(1+($scv[32]=='D1'?7:19)/100);//print_r($data);//echo $netprice;
$this->app->erp->AddSellPrice($artikelid,1,0,$nettoprice);}if($csv[31]){//downloadarticle$data2['number']=$csv[2].'D';//If item number is 3rd column$data2['name_en']=$csv[0].' Download';//If article name in first column is$data2['short_text_en']=$csv[22];/*$data['description_en'] =....
  $data['manufacturer'] =...
  $data['manufacturer_link'] =...*/if($scv[32]=='D1')$data2['sales_tax']='reduced';if(isset($articleid)){$data2['variante']=1;$data2['variant_of']=$artikelid;}$artikelid2=$this->app->erp->InsertUpdateArticle($data2);$pricegross=$csv[31];$nettoprice=$pricegross/(1+($scv[32]=='D1'?7:19)/100);//print_r($data2);//echo $netprice;
$this->app->erp->AddSellPrice($artikelid2,1,0,$nettoprice);
} 
}
```

## Gesamte Datei

Die gesamte Datei gestaltet sich wie folgt:

```
<?php
// Report simple errors only

error_reporting(E_ERROR | E_WARNING | E_PARSE);

include_once("../conf/main.conf.php");
include_once("../phpwf/plugins/class.mysql.php");
include_once("../phpwf/plugins/class.string.php");
include_once("../phpwf/plugins/class.user.php");
include_once("../www/lib/class.erpapi.php");

class app_t {
 var $DB;
 var $String;
 var $User;
}

$app = new app_t();
$app->User = new User($app);
$conf = new Config();
$app->DB = new DB($conf->WFdbhost,$conf->WFdbname,$conf->WFdbuser,$conf->WFdbpass);
$app->string = new string();
$erp = new erpAPI($app);
$app->erp = $erp;

if(!isset($argv[1]))
{
  the("No file specified for import");
}
if(!file_exists($argv[1]))
{
  the("File ".$argv[1]." does not exist");
}
if(!is_file($argv[1]))
{
  the($argv[1]." is not a file");
}

$csvimport = new CSVImport($app, $argv[1]);
$csvimport->read();

class CSVImport
{
 var $app;
 var $file;

 function __construct(&$app, $file)
 {
  $this->app = $app;
  $this->file = $file;

}

 function read()
 {
  if($this->file && file_exists($this->file) && is_file($this->file))
  {
  if (($handle = fopen($this->file, "r"))!== FALSE) {
  $row = 0;
  while (($csv = fgetcsv($handle, 0, ";"))!== FALSE) {
  //$line = iconv("ISO-8859-1", "UTF-8", $line); //If script is stored in UTF-8 and CSVin ANSI the string will be converted
  foreach($csv as $k => $el)$csv[$k] = iconv("ISO-8859-1","UTF-8", $el);
  $row++;
  //$csv = str_getcsv($line,"\t","\""); //When CSVis tab delimited and individual elements are enclosed with ".
  //$csv = str_getcsv($line, ";",""); //separated with;.
  if($row < 5) { //If the header of the file has 4 lines this can be used for debugging e.g. 

} else {
  //From here on the actual data will be processed

  $this->process($csv);

}
}
  return true;
} else the("Could not open file ".$this->file."! \r\n");
} else {
  echo $this->file." not found\r\n";
  return false;
}
}
 function process(&$csv)
 {

  //Process the individual data

  if($csv[30])
  {

  $data['number'] = $csv[2]; //If article number is 3rd column
  $data['name_en'] = $csv[0]; //If article name is in first column
  $data['short_text_en'] = $csv[22];
  /*$data['description_en'] =....
  $data['manufacturer'] =...
  $data['manufacturer_link'] =...*/
  $data['weight'] = $csv[48];
  if($scv[32] == 'D1')$data['sales-tax'] = 'ermaessigt';

  //data will be saved with the erpAPI

  $artikelid = true;
  $artikelid = $this->app->erp->InsertUpdateArticle($data);

  //Now the sales prices

  $pricegross = $csv[30];
  $nettoprice = $pricegross / (1+($scv[32]=='D1'?7:19)/100);
  //print_r($data);
  //echo $netprice;

  $this->app->erp->AddSellPrice($artikelid,1,0,$nettoprice);
}
  if($csv[31])
  {
  //downloadarticle
  $data2['number'] = $csv[2].'D'; //If item number is 3rd column
  $data2['name_en'] = $csv[0].' Download'; //If article name in first column is
  $data2['short_text_en'] = $csv[22];
  /*$data['description_en'] =....
  $data['manufacturer'] =...
  $data['manufacturer_link'] =...*/
  if($scv[32] == 'D1')$data2['sales_tax'] = 'reduced';
  if(isset($articleid))
  {
  $data2['variante'] = 1;
  $data2['variant_of'] = $artikelid;
}
  $artikelid2 = $this->app->erp->InsertUpdateArticle($data2);
  $pricegross = $csv[31];
  $netprice = $pricegross / (1+($scv[32]=='D1'?7:19)/100);
  //print_r($data2);
  //echo $netprice;

  $this->app->erp->AddSellPrice($artikelid2,1,0,$nettoprice);
}

}
}
```

## Import Datei einmalig ausführen

Die Datei, welche die CSV Datei verarbeitet (.php Datei), muss im xentral Ordner in den Ordner importer gespeichert sein. Hier werden auch die benötigten CSV Dateien zum Verarbeiten abgelegt. In diesem Beispiel ist die PHP Datei beispielimporter.php und die CSV Datei beispieldaten.csv.

Im Anschluss wird die Konsole aufgerufen und in den importer Ordner gewechselt, z.B. mit

```cd /var/www/html/wawision/importer```

Der Pfad kann, je nachdem wie die Verzeichnisstruktur aufgebaut ist, abweichen.

Mit

```php exampleimporter.php exampledata.csv```

wird die PHP Datei aufgerufen und der Code darin ausgeführt.

Die Dateinamen müssen durch die jeweiligen Dateinamen ersetzt werden.

Es kann sein, dass ein Typ angegeben werden muss, hier wird die Konsole jedoch darauf aufmerksam machen und die möglichen Typen nennen. Dann erfolgt der Aufruf mit

```php exampleimporter.php exampletype exampledata.csv```

Je nach Dateigröße der CSV Datei, kann der Ablauf mehrere Minuten in Anspruch nehmen. Der Code wurde komplett ausgeführt, wenn in der Kommandozeile wieder der Benutzernamen und Pfad in einer neuen Zeile erscheint.

## Import Datei mehrmals manuell ausführen

Die Datei, welche die CSV Datei verarbeitet (.php Datei), muss im xentral Ordner in den Ordner importer abgelegt werden. Hier werden auch die benötigten CSV Dateien zum Verarbeiten abgelegt. In diesem Beispiel ist die PHP Datei beispielimporter.php und die CSV Datei beispieldaten.csv.

Im Anschluss wird die Konsole aufgerufen und in den importer Ordner gewechselt, z.B. mit

```cd /var/www/html/wawision/importer```

Der Pfad kann je nachdem wie die Verzeichnisstruktur aufgebaut ist abweichen.

Mit

```php exampleimporter.php```

wird die PHP Datei aufgerufen und der Code darin ausgeführt. Der Dateinamen muss durch den jeweiligen Dateinamen ersetzt werden. Je nach Dateigröße der CSV Datei, kann der Ablauf mehrere Minuten in Anspruch nehmen. Der Code wurde komplett ausgeführt, wenn in der Kommandozeile wieder der Benutzernamen und Pfad in einer neuen Zeile erscheint.