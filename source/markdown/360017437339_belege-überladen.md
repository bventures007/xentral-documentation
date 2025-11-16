## Briefpapier überladen

Falls für das Briefpapier weitere Informationen benötigt werden, wie zum Beispiel zusätzlich bei einer Artikelposition zur Artikelbeschreibung das Gewicht oder die Höhe, so kann ein eigenes Briefpapier zum Überladen angelegt werden.

Die Datei die das Briefpapier überladen soll, muss class.briefpapier_custom.php heißen. Diese Datei muss im Xentral ordner nach www/lib/dokumente hochgeladen werden und ist dann für alle Belege gültig.

> **Tipp**
>
> Den Quellcode kannst du dir aus der Datei aus der Open Source Version holen.

Im folgenden Beispiel soll zusätzlich das Gewicht sowie die Höhe, Breite, Länge und Ursprungsregion des Artikels zur Artikelbeschreibung einer Position hinzugefügt werden.

Bisher gibt es noch kein Custom Briefpapier, weshalb das Briefpapier vorerst wie in den Standardeinstellungen festgelegt aussieht:

![Briefpapier-1.png](https://help.xentral.com/hc/article_attachments/4996403325212)

Als Erstes ist die Datei class.briefpapier_custom.php zu erstellen. Das Grundgerüst für das Custom Briefpapier sieht wie folgt aus:

```
?php

include_once "class.briefpapier.php";

class BriefpapierCustom extends Briefpapier {

function __construct(&$app) { $this->app = $app; parent::__construct($app);} 

}?>
```Als Nächstes ist die Datei class.briefpapier.php zu öffnen, die derzeit für das Layout des Briefpapiers zuständig ist und sucht sich die Funktion heraus, die überladen werden soll, kopiert und fügt diese unter der Funktion "construct" ein. In diesem Fall ist die Funktion renderItems zu kopieren, da diese für die Darstellung der Artikelpositionen zuständig ist. Da die Funktion renderItems recht lang ist, wird hier im Bsp. nur angedeutet, wie der Code von class.briefpapier_custom.php dann aussieht.```
?php

include_once "class.briefpapier.php";

class BriefpapierCustom extends Briefpapier {

function __construct(&$app) { $this->app = $app; parent::__construct($app);}

public function renderItems() {

$posWidth = $this->app->erp->Firmendaten("breite_position");
$amWidth = $this->app->erp->Firmendaten("breite_menge");
$itemNoWidth = $this->app->erp->Firmendaten("breite_nummer");

...
...
...

}

}?>
```Unterhalb von```
if($item['ean']!="" && $item['ean']!="0"){
  if($item['desc']!=""){
  $item['desc']=$item['desc']."\r\n".$this->app->erp->Beschriftung("dokument_ean").": ".$item['ean'];
}else{
  $item['desc']=$this->app->erp->Beschriftung("dokument_ean").": ".$item['ean'];
}
}
```

wird nun die Größe, sowie die Höhe, Breite, Länge und Ursprungsregion des Artikels zur Variablen $item['desc'] hinzugefügt, da diese den Beschreibungstext beinhaltet und zu diesem die weiteren Werte hinzukommen sollen.

Der fertige Abschnitt sieht dann so aus:

```
if($item['ean']!="" && $item['ean']!="0"){
  if($item['desc']!=""){
  $item['desc']=$item['desc']."\r\n".$this->app->erp->Beschriftung("dokument_ean").": ".$item['ean'];
}else{
  $item['desc']=$this->app->erp->Beschriftung("dokument_ean").": ".$item['ean'];
}
}

$daten = $this->app->DB->SelectArr("SELECT gewicht, laenge, breite, hoehe, ursprungsregion FROM artikel WHERE id = '".$item['artikel']."'");
$daten = reset($daten);

if($item['desc']!= ""){
  if($daten['gewicht']!= "" AND $daten['gewicht'] > 0){
  $item['desc'] = $item['desc']."\r\n"."Gewicht: ".$daten['gewicht']." kg";
}
}else{
  if($daten['gewicht']!= "" AND $daten['gewicht'] > 0){
  $item['desc'] = $item['desc']."Gewicht: ".$daten['gewicht']." kg";
}
}

if($item['desc']!= ""){
  if($daten['laenge']!= "" AND $daten['laenge'] > 0){
  $item['desc'] = $item['desc']."\r\n"."Länge: ".$daten['laenge']." cm";
}
}else{
  if($daten['laenge']!= "" AND $daten['laenge'] > 0){
  $item['desc'] = $item['desc']."Länge: ".$daten['laenge']." cm";
}
}

if($item['desc']!= ""){
  if($daten['breite']!= "" AND $daten['breite'] > 0){
  $item['desc'] = $item['desc']."\r\n"."Breite: ".$daten['breite']." cm";
}
}else{
  if($daten['breite']!= "" AND $daten['breite'] > 0){
  $item['desc'] = $item['desc']."Breite: ".$daten['breite']." cm";
}
}

if($item['desc']!= ""){
  if($daten['hoehe']!= "" AND $daten['hoehe'] > 0){
  $item['desc'] = $item['desc']."\r\n"."Höhe: ".$daten['hoehe']." cm";
}
}else{
  if($daten['hoehe']!= "" AND $daten['hoehe' > 0]){
  $item['desc'] = $item['desc']."Höhe: ".$daten['hoehe']." cm";
}
}

$ursprungsregion = "";

switch($daten['ursprungsregion']){
  case "01":
  $ursprungsregion = "Schleswig-Holstein";
  break;
  case "02":
  $ursprungsregion = "Hamburg";
  break;
  case "03":
  $ursprungsregion = "Niedersachsen";
  break;
  case "04":
  $ursprungsregion = "Bremen";
  break;
  case "05":
  $ursprungsregion = "Nordrhein-Westfalen";
  break;
  case "06":
  $ursprungsregion = "Hessen";
  break;
  case "07":
  $ursprungsregion = "Rheinland-Pfalz";
  break;
  case "08":
  $ursprungsregion = "Baden-Württemberg";
  break;
  case "09":
  $ursprungsregion = "Bayern";
  break;
  case "10":
  $ursprungsregion = "Saarland";
  break;
  case "11":
  $ursprungsregion = "Berlin";
  break;
  case "12":
  $ursprungsregion = "Brandenburg";
  break;
  case "13":
  $ursprungsregion = "Mecklenburg-Vorpommern";
  break;
  case "14":
  $ursprungsregion = "Sachsen";
  break;
  case "15":
  $ursprungsregion = "Sachsen-Anhalt";
  break;
  case "16":
  $ursprungsregion = "Thüringen";
  break;
  case "99":
  $ursprungsregion = "ausländischer Ursprung";
  break;
}

if($item['desc']!= ""){
  if($ursprungsregion!= ""){
  $item['desc'] = $item['desc']."\r\n"."Ursprungsregion: ".$ursprungsregion;
}
}else{
  if($ursprungsregion!= ""){
  $item['desc'] = $item['desc']."Ursprungsregion: ".$ursprungsregion;
}
}
```

Das Ergebnis sieht nun so aus:

![Briefpapier-2.png](https://help.xentral.com/hc/article_attachments/4996448227228)

## Nur eine Belegart überladen

Des Weiteren gibt es die Möglichkeit nur bestimmte Belege zu überladen. In folgendem Beispiel soll zur Artikelbeschreibung einer Position das nächste, also kleinste, Mindesthaltbarkeitsdatum aus dem Lager für diesen Artikel auf einem Kommissionierschein angezeigt werden. Dazu muss der Lieferschein überladen werden, da der Kommissionierschein ebenfalls mit der class.lieferschein.php erstellt wird. Um die class.lieferschein.php Datei zu überladen, wird eine Datei namens class.lieferschein_custom.php erstellt und diese in den xentralsordner nach www/lib/dokumente abgelegt. Bisher gibt es keine class.lieferschein_custom.php Datei, somit sieht der Kommissionierschein so aus:

![Briefpapier-3.png](https://help.xentral.com/hc/article_attachments/4996403383324)

Das Grundgerüst der Datei sieht wie folgt aus:

```
?php 
if(!class_exists('BriefpapierCustom')) 
{ 
  class BriefpapierCustom extends Briefpapier 
  {

} 
}

class LieferscheinPDFCustom extends BriefpapierCustom {
  public $doctype;

  function __construct($app,$projekt="") 
  { 
  $this->app=&$app; 
  //parent::Briefpapier();
  $this->doctype="lieferschein";
  $this->doctypeOrig="Lieferschein";
  parent::__construct($this->app,$projekt);
}
} 
?>
```Als nächstes ist die passende Funktion zu suchen, die in der class.lieferschein.php überladen werden soll. In diesem Fall ist es die Funktion GetLieferschein. Diese Funktion wird kopiert und unter dem Konstruktor "construct" eingefügt. Da die Funktion GetLieferschein recht lang ist, wird hier nur angedeutet, wie die Datei derzeit aussieht:```
?php
if(!class_exists('BriefpapierCustom'))
{ 
  class BriefpapierCustom extends Briefpapier 
  {

} 
}

class LieferscheinPDFCustom extends BriefpapierCustom { 
  public $doctype;
  function __construct($app,$projekt="") 
  { $this->app=&$app;
  //parent::Briefpapier();
  $this->doctype="lieferschein";
  $this->doctypeOrig="Lieferschein";
  parent::__construct($this->app,$projekt);
}

  function GetLieferschein($id,$info="",$extrafreitext="")
  {
  $this->doctypeid = $id;
  if(method_exists($this->app->erp,'LieferscheinSeriennummernberechnen'))$this->app->erp->LieferscheinSeriennummernberechnen($id);
  $briefpapier_bearbeiter_ausblenden = $this->app->erp->Firmendaten('briefpapier_bearbeiter_ausblenden');
  $briefpapier_vertrieb_ausblenden = $this->app->erp->Firmendaten('briefpapier_vertrieb_ausblenden'); 
  $adresse = $this->app->DB->Select("SELECT adresse FROM lieferschein WHERE id='$id' LIMIT 1");
...
...
...
}
} 
?>
```Nun werden die Anpassungen im Code vorgenommen. Wenn diese nun einfach hinzugefügt werden würde, wären diese für Lieferscheine und Kommissionierscheine gültig. Allerdings sollen hier nur die Kommissionierscheine angepasst werden, weshalb mit einem if Statement vorher geprüft wird, ob es sich um einen Kommissionierschein handelt. Die Änderungen werden unter```
/*
  if(!empty($chargen)){
  foreach($chargen as $chargen=>$charge){
  $chargenliste = $chargenliste.$charge['charge'].";";
}
 
  $chargenliste=substr($chargenliste, 0, -1);
 
  $value['chargen'] = $this->app->DB->Select("SELECT chargenverwaltung FROM artikel WHERE id='".$value[artikel]."' LIMIT 1");
 
  if($value['chargen']=="0"){
  $value['beschreibung'] = $value['beschreibung'];
}else{
  $value['beschreibung'] = $value['beschreibung']."\r\n".$this->app->erp->Beschriftung("dokument_charge").": ". $chargenliste;
}
}
*/
```hinzugefügt. Das Ganze sieht dann so aus:```
if($info=="kommissionierschein"){
 if($value['freifeld1']!=""){
  //$value['beschreibung'].= "\r\n"."Bitte folgendes MHD wählen: ".$value['freifeld1'];
}else{
 $mhd=$this->app->DB->Select("SELECT MIN(mhddatum) FROM lager_mindesthaltbarkeitsdatum WHERE artikel= '".$value['artikel']."' AND mhddatum > CURDATE()");
 $value['beschreibung'].="\r\n"."Kleinstes MHD im Lager: ".$mhd;
}
}
```

Endergebnis:

![Briefpapier-4.png](https://help.xentral.com/hc/article_attachments/4996448282268)