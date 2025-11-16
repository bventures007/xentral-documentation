Template Scripts ermöglichen die weitergehende Anpassung von PDF-Belegen, E-Mail-Templates und anderen Ausgabeformaten aus xentral. Bereits im Standard stehen mit den Konfigurationsmöglichkeiten viele Einstellungsmöglichkeiten zur Verfügung. Dazu gehören die Anpassung der Schriftart und -größen, Positionierung von Elementen und einiges mehr. Sollen aber neue Daten hinzugefügt werden, Berechnungen stattfinden oder besondere Spracheinstellungen umgesetzt werden, kann durch Rendering Scripts jedes Detail angepasst werden.

## Briefpapier überladen

Ein Beispiel für die Anpassung von Templates in xentral ist die Überladung des Briefpapiers. Hier können weitere Informationen integriert werden, die im Standard-Briefpapier nicht zur Verfügung stehen, wie zum Beispiel zusätzlich bei einer Artikelposition zur Artikelbeschreibung das Gewicht oder die Höhe.

### Umsetzung

Die Datei die das Briefpapier überladen soll, muss class.briefpapier_custom.php heißen. Diese Datei muss im Ordner www/lib/dokumente liegen und ist dann für alle Belegarten (Rechnung, Auftragm Lieferschein, Gutschrift, etc.) gültig.

Im folgenden Beispiel soll zusätzlich das Gewicht sowie die Höhe, Breite, Länge und Ursprungsregion des Artikels zur Artikelbeschreibung einer Position hinzugefügt werden. Bisher gibt es noch kein Custom Briefpapier, weshalb das Briefpapier vorerst wie in den Standardeinstellungen festgelegt aussieht:

![Template1.png](https://help.xentral.com/hc/article_attachments/4996369650716)

Als Erstes ist die Datei class.briefpapier_custom.php zu erstellen. Das Grundgerüst für das Custom Briefpapier sieht wie folgt aus:

```
<?php

include_once "class.briefpapier.php";

class BriefpapierCustom extends Briefpapier {

  function __construct(&$app)
  {
  $this->app = $app;
  parent::__construct($app);
} 

} 
?>

```

Als nächstes ist die Datei class.briefpapier.php zu öffnen, die derzeit für das Layout des Briefpapiers zuständig ist und sucht die Funktion heraus, die überladen werden soll, kopiert diese und fügt diese unter der Funktion __construct ein. In diesem Fall ist die Funktion renderItems() zu kopieren, da diese für die Darstellung der Artikelpositionen verantwortlich ist.

Da die Funktion renderItems() recht umfangreich ist, wird hier jetzt nur angedeutet, wie der Code von class.briefpapier_custom.php im Anschluß aussehen könnte.

```
<?php

include_once "class.briefpapier.php";

class BriefpapierCustom extends Briefpapier {

  function __construct(&$app)
  {
  $this->app = $app;
  parent::__construct($app);
} 

  public function renderItems()
  {

  $posWidth = $this->app->erp->Firmendaten("breite_position");
  $amWidth = $this->app->erp->Firmendaten("breite_menge");
  $itemNoWidth = $this->app->erp->Firmendaten("breite_nummer");

...
...
...
  
}

} 
?>

```Unterhalb von```
if($item['ean']!="" && $item['ean']!="0"){
  if($item['desc']!=""){
  $item['desc']=$item['desc']."\r\n".$this->app->erp- >Beschriftung("dokument_ean").": ".$item['ean'];
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
  $item['desc']=$item['desc']."\r\n".$this->app->erp- >Beschriftung("dokument_ean").": ".$item['ean'];
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

![Template2.png](https://help.xentral.com/hc/article_attachments/4996369663900)

## Nur eine Belegart überladen

Desweiteren gibt es die Möglichkeit nur bestimmte Belege zu überladen. In folgendem Beispiel soll zur Artikelbeschreibung einer Position das nächste, also kleinste Mindesthaltbarkeitsdatum aus dem Lager für diesen Artikel auf einem Kommissionierschein angezeigt werden. Dazu muss der Lieferschein überladen werden, da der Kommissionierschein ebenfalls mit der class.lieferschein.php erstellt wird. Um die class.lieferschein.php Datei zu überladen, wird eine Datei namens class.lieferschein_custom.php erstellt und diese in den xentralsordner nach www/lib/dokumente abgelegt. Bisher gibt es keine class.lieferschein_custom.php Datei, somit sieht der Kommissionierschein so aus:

![Template3.png](https://help.xentral.com/hc/article_attachments/4996431681052)

Das Grundgerüst der Datei sieht wie folgt aus:

```
<?php
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

```Als nächstes wird die passende Funktion, die überladen werden soll, in der class.lieferschein.php gesucht. In diesem Fall ist es die Funktion GetLieferschein. Diese Funktion wird kopiert und unter dem Konstruktor __construct eingefügt. Da die Funktion GetLieferschein recht lang ist, wird hier nur angedeutet, wie die Datei derzeit aussieht:```
<?php
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

  function GetLieferschein($id,$info="",$extrafreitext="")
  {
  $this->doctypeid = $id;
  if(method_exists($this->app->erp,'LieferscheinSeriennummernberechnen'))$this- >app->erp->LieferscheinSeriennummernberechnen($id);
  $briefpapier_bearbeiter_ausblenden = $this->app->erp- >Firmendaten('briefpapier_bearbeiter_ausblenden');
  $briefpapier_vertrieb_ausblenden = $this->app->erp->Firmendaten('briefpapier_vertrieb_ausblenden');
  $adresse = $this->app->DB->Select("SELECT adresse FROM lieferschein WHERE id='$id' LIMIT 1");

...
...
...

}

}
?>

```Nun werden die Anpassungen im Code vorgenommen. Wenn diese nun einfach hinzugefügt werden würden, wären diese für Lieferscheine und Kommissionierscheine gültig. Allerdings sollen hier nur die Kommissionierscheine angepasst werden, weshalb mit einem if Statement vorher geprüft wird, ob es sich um einen Kommissionierschein handelt. Die Änderungen werden unter```
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
  $value['beschreibung'] = $value['beschreibung']."\r\n".$this->app->erp- >Beschriftung("dokument_charge").": ". $chargenliste;
}
}
*/

```hinzugefügt. Das Ganze sieht dann so aus:```
if($info == "kommissionierschein"){
  if($value['freifeld1']!= ""){
  //$value['beschreibung'].= "\r\n"."Bitte folgendes MHD wählen: ".$value['freifeld1'];
}else{
  $mhd = $this->app->DB->Select("SELECT MIN(mhddatum) FROM lager_mindesthaltbarkeitsdatum WHERE artikel= '".$value['artikel']."' AND mhddatum > CURDATE()");
  $value['beschreibung'].= "\r\n"."Kleinstes MHD im Lager: ".$mhd;
}
}

```

Endergebnis:

![Template4.png](https://help.xentral.com/hc/article_attachments/4996407788572)

## Kommissionierliste / Pickliste überladen

Die Überladung der Pickliste ist in xentral ebenfalls möglich.

### Umsetzung

Die Datei die das Briefpapier überladen soll, wird in /www/pages als kommissionierlauf_custom.php angelegt. In der Datei befindet sich die Funktion KommissionierlaufPDF diese kann dann angepasst werden kann.

Im folgenden ist die Standardfunktion gelistet, die dann den Vorstellungen nach angepasst werden kann.

```
 public function KommissionierlaufPDF($id = null)
  {
  if($id)
  {
  $kommissionierlaufid = $id;
  $intern = true;
}else{
  $intern = false;
  $kommissionierlaufid = (int)$this->app->Secure->GetGET('id');
}
  $commission = $this->app->DB->SelectRow(
  sprintf(
  'SELECT `abgeschlossen `, ` bezeichnung `FROM` kommissionierung `WHERE` id `= %d`',
  $kommissionierlaufid
)
);
  $bezeichnung = empty($commission)?'':$this->app->erp->ReadyForPDF(
  (String)$commission['bezeichnung']
);
  //$lieferscheinids = $this->app->DB->SelectArr("SELECT id FROM lieferschein WHERE kommissionierung = \"$kommissionierlaufid\"");
  $abgeschlossen =!empty($commission['abgeschlossen']);
  $artikelnummern = $this->getCommssionArticles($kommissionierlaufid, $abgeschlossen);
  $articleArr = $this->getStorageLocationsByArticleArr($artikelnummern);
  $storage = $this->getStorageByArticleArr($articleArr);
  $lieferscheinnr = $this->app->DB->SelectArr(
  sprintf(
  'SELECT DISTINCT l.belegnr, l.name
  FROM `lieferschein ` AS`l` 
  WHERE l.kommissionierung = %d 
  ORDER BY l.id',
  $kommissionierlaufid
)
);
  $kistenarray = array();
  $counter = 1;
  $mengenarray = array();
  $deliveryNoteNameByNumber = [];
  foreach($lieferscheinnr as $key => $value){
  $kistenarray[$value['belegnr']] = $counter;
  $deliveryNoteNameByNumber[$value['belegnr']] = $value['name'];
  $counter += 1;
}
  //Neue PDF Datei erstellen
  $pdf=new SuperFPDF('P','mm','A4',$this->app);
  $pdf->AddPage();
  $pdf->SetFont('Arial', 'B', 15);
  $pdf->Cell(
  100, 8,
  'Kommissionierlauf '.$kommissionierlaufid.($bezeichnung!== ''?' '.$bezeichnung:''),
  0, 0, 'L'
);
  $pdf->SetFont('Arial','',10);
  $pdf->Cell(0, 8, date('d.m.Y'), 0, 1, 'R');
  $pdf->Ln();
  $breitenummer = $this->app->erp->Firmendaten('breite_nummer');
  $pdf->SetFont('Arial','B',10);
  $pdf->Cell(15, 5, 'Pos', 0, 0, 'C');
  $pdf->Cell(25, 5, 'Lagerort', 0, 0, 'C');
  $pdf->Cell(50, 5, 'Artikelnr', 0, 0, 'L');
  $pdf->Cell(55, 5, 'Artikel', 0, 0, 'L');
  $pdf->Cell(20, 5, 'Menge', 0, 0,'C');
  $pdf->Cell(25, 5, 'Lagerbest.', 0, 1, 'C');
  $pdf->SetFont('Arial','',10);
  $pdf->Line($pdf->GetX(), $pdf->GetY(), $pdf->GetX()+190, $pdf->GetY());
  $position = 1;
  foreach($artikelnummern as $key=>$value){
  $artikelid = $value['id'];
  $fontsize = 10;
  if(isset($value['fontsize']) && (float)$value['fontsize'] > 1)
  {
  $fontsize = (float)$value['fontsize'];
}
  $pdf->Cell(15, 5, $position, 0, 0, 'C');
  $pdf->SetFont('Arial','B',10);
  $artikellagerort = $value['kurzbezeichnung'];
  if($artikellagerort == ''){
  $artikellagerort = '-';
}
  $pdf->Cell(25, 5, $artikellagerort, 0, 0, 'C');
  $pdf->SetFont('Arial','',10);
  $pdf->Cell(50, 5, $value['nummer'], 0, 0, 'L');
  $artikelname = $value['name_de'];
  $pdf->SetFont('Arial','B',$fontsize);
  $pdf->MultiCell(0, 5, $artikelname, 0, 'L');
  $pdf->SetFont('Arial','',$fontsize);
  $lieferscheindaten = $this->getDeliveryNoteDataByArticle(
  $kommissionierlaufid, $artikelid, $value['lager_platz'], $abgeschlossen
);
  $ean = $value['ean'];
  if($ean!= ''){
  $pdf->Cell(90, 5, '', 0, 0, 'L');
  $pdf->Cell(0, 5, '- EAN: '.$ean, 0, 1, 'L');
  $pdf->Cell(90, 5, "", 0, 0, 'L');
  $pdf->Cell(25, 5, $pdf->Code39($pdf->GetX(), $pdf->GetY(), $ean, 1, 5), 0, 1, 'L');
  $pdf->Cell(90, 5, "", 0, 1, 'L');
}
  foreach($lieferscheindaten as $artikel=>$daten){
  $pdf->Cell(90, 5, '', 0, 0, 'L');
  $pdf->Cell(
  0, 5,
  '- LS '.$daten['belegnr'].' / Kiste '.$kistenarray[$daten['belegnr']].' / '
.$this->app->erp->ReadyForPDF($daten['name']).' ('.(float)$daten['menge'].')',
  0, 1, 'L'
);
  $mengenarray[$daten['belegnr']] += $daten['menge'];
}
  $pdf->SetX($pdf->GetX()+145);
  $artikelmenge = $value['menge'];
  $pdf->SetFont('Arial','B',$fontsize);
  $pdf->Cell(20, 5, (float)$artikelmenge, 0, 0, "C");
  $pdf->SetFont('Arial','',$fontsize);
  if(empty($storage[(int)$artikelid])
  || empty($storage[(int)$artikelid][(int)$value['lager_platz']])) {
  $artikellagerbestand = $this->app->DB->SelectRow(
  sprintf(
  'SELECT IFNULL(SUM(`menge`),0) AS menge 
  FROM `lager_platz_inhalt ` WHERE`artikel `= %d AND` lager_platz` = %d 
  LIMIT 1',
  (int)$artikelid, (int)$value['lager_platz']
)
);
}
  else {
  $artikellagerbestand = ['menge'=>$storage[(int)$artikelid][(int)$value['lager_platz']]];
}
  if($artikellagerbestand['menge']!= ''){
  $artikellagerbestand['menge'] = (float)$artikellagerbestand['menge'];
}else{
  $artikellagerbestand['menge'] = 0;
}
  $pdf->Cell(25, 5, $artikellagerbestand['menge'], 0, 1, 'C');
  $pdf->Line($pdf->GetX(), $pdf->GetY(), $pdf->GetX()+190, $pdf->GetY());
  $position++;
} 
  //$pdf->AddPage();
  $pdf->Ln(20);
  $pdf->SetFont('Arial','B',10);
  $pdf->Cell(23, 5, 'Kisten-Nr', 0, 0, 'L');
  $pdf->Cell(27, 5, 'LS-Nr', 0, 0, 'L');
  $pdf->Cell(35, 5, 'Kundenname', 0, 0, 'L');
  $pdf->Cell(15, 5, 'Teile', 0, 0, 'L');
  $pdf->Cell(20, 5, 'Barcode LS', 0, 1, 'L');
  $pdf->SetFont('Arial','',10);
  $pdf->Line($pdf->GetX(), $pdf->GetY(), $pdf->GetX()+190, $pdf->GetY());
  $pdf->Ln(1);
  foreach($lieferscheinnr as $key => $value){
  $pdf->Cell(23, 5, 'Kiste '.$kistenarray[$value['belegnr']], 0, 0, 'L');
  $pdf->Cell(27, 5, $value['belegnr'], 0, 0, 'L');
  $kundenname =!empty($deliveryNoteNameByNumber[$value['belegnr']])
?$deliveryNoteNameByNumber[$value['belegnr']]
:$this->app->DB->Select(
  sprintf(
  "SELECT `name ` FROM`lieferschein ` WHERE`belegnr` = '%s' LIMIT 1",
  $this->app->DB->real_escape_string($value['belegnr'])
)
);
  if(strlen($kundenname) > 17){
  $kundenname = trim(substr($kundenname, 0, 17)).'...';
}
  $pdf->Cell(35, 5, $this->app->erp->ReadyForPDF($kundenname), 0, 0, 'L');
  $pdf->Cell(15, 5, $mengenarray[$value['belegnr']], 0, 0, 'L');
  $pdf->Cell(20, 5, $pdf->Code39($pdf->GetX(), $pdf->GetY(), $value['belegnr'], 1, 5), 0, 1, 'L');
  $pdf->Ln(18);
}
  if($intern)
  {
  $pdf->filename = $this->app->erp->Dateinamen(date('Ymd').'_'.$kommissionierlaufid.'_Pickliste.pdf');
  $pdf->Output($this->app->erp->GetTMP().$pdf->filename,'F');
  return $this->app->erp->GetTMP().$pdf->filename;
}
  $pdf->Output(date('Ymd').'_'.$kommissionierlaufid.'_Pickliste.pdf','D');
  $this->app->ExitXentral();
}

```

### Adressdatenstammblatt überladen

Ebenso wie das Briefpapier können auch andere Dokumente überladen werden, wie z.B. das Adressstammblatt. Die Definitionen dafür finden sich in der Klasse AdressstammblattPDF in der Datei class.adressstammblatt.php im Ordner www/lib/dokumente.

Zunächst wird die class.adressstammblatt_custom.php erstellt. Das Grundgerüst für das dafür sieht wie folgt aus:

```
<?php

include_once "class.adressstammblatt.php";

class AdressstammblattPDFCustom extends AdressstammblattPDF {

  function __construct($app,$projekt="")
  {
  $this->app=$app;
  $this->doctype="adresse";
  $this->doctypeOrig="Adressstammblatt";
  parent::__construct($this->app,$projekt);
} 
} 
?>

```

Anschließend können zusätzliche Daten im Stammdatenblatt ausgegeben werden. Dazu ist sich an der Klasse AdressstammblattPDF und den beiden darin enthaltenen Funktionen renderDocument() und GetAdressstammblatt() zu orientieren.