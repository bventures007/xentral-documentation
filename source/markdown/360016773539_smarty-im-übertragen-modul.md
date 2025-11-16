Das **Übertragen-Modul ** ermöglicht es dir, eine Vielzahl von Belegen oder Daten aus xentral zu exportieren. Dabei werden dir neben verschiedenen Ausgabeformaten und Ausgabekanälen auch verschiedene Trigger zum Export angeboten (z.B. der Belegstatus, Label, ID oder Datum eines Beleges, etc.). Dazu verwendest du das**Smarty Transfer-Modul**.

Mit Hilfe von Smarty kannst du nun das Zielformat der ausgegebenen Daten selbst definieren und mit Hilfe von

- Funktionen (wie z.B. truncate) bearbeiten,
- mit SQL-Abfragen anreichern
- und durch die Anwendung von Schleifen, Bedingungen o.ä. mit Logik verändern.

Im Übertragen-Modul steht dir Smarty bei eingehenden und ausgehenden Nachrichten zur Verfügung. Dabei bestimmt das Template

- bei ausgehenden Nachrichten das von der Gegenstelle erwartete Zielformat
- bei eingehenden Nachrichten das xentral interne Format zur Verarbeitung (in den meisten Fällen xentral XML).

## Belegarten und Daten

Hier erfährst du, welche Belegarten und Daten du exportieren bzw. importieren kannst.

### Ausgehende Übertragungen und Daten

Im Übertragen-Modul kannst du per Smarty die folgenden Belegtypen exportieren:

- Auftrag
- Lieferschein
- Rechnung
- Gutschrift
- Angebot
- Bestellung
- Retoure

Darüber hinaus kannst du die folgenden Daten mit Hilfe von Smarty Templates exportieren:

- Artikel
- Lagerzahlen
  - Lagerbestände
  - Lagerplätze

### Eingehende Übertragungen und Daten

Im Übertragen-Modul kannst du per Smarty die folgenden Belegtypen **importieren**:

- Auftrag: techn. Bezeichnung 'auftrag' (XML, CSV)
- Bestellung: techn. Bezeichnung 'bestellung' (XML, CSV)
- Produktion: techn. Bezeichnung 'produktion' (XML, CSV)
- Retoure: techn. Bezeichnung 'retoure' (XML, CSV)

Darüberhinaus kannst du die folgenden Daten importieren (einlesen):

- Lagerzahlen
- Artikeldaten
- Tracking-Informationen

Um alle Belegtypen zu importieren, musst du das Übertragungsformat **smarty ** auswählen und**speichern **. Dann erscheint unter ** Beleg empfangen **eine neue Checkbox, die ** alle Belegtypen importieren**heißt.

Fehler beim Auslesen kannst du teilweise aus dem Monitor bzw. der Logfile lesen.

## Smarty Ausgehend (outbound oder Export)

Daten aus xentral zu versenden (auch “outbound” genannt) ermöglicht es dir die Daten von xentral

1. in ein Zielformat zu konvertieren und anschließend
1. in ein Fremdsystem zu exportieren

Eine Template-Datei könnte dabei z.B. folgendermaßen aussehen:

```
<?xml version="1.0" encoding="utf-8"?>
<auftrag>
  <status>{$beleg->status}</status>
  <datum>{$beleg->datum|date_format:'%d.%m.%Y'}</datum>
  <lieferdatum>{$beleg->lieferdatum}</lieferdatum>
  <versandart>{$beleg->versandart}</versandart>
  <zahlungsweise>{$beleg->zahlungsweise}</zahlungsweise>
  <belegnr>{$beleg->belegnr}</belegnr>
  <kundennummer>{$beleg->kundennummer}</kundennummer>
  <name>{$beleg->name}</name>
  <strasse>{$beleg->strasse}</strasse>
  <plz>{$beleg->plz}</plz>
  <ort>{$beleg->ort}</ort>
  <positionen>
  {foreach from=$beleg->positionen key=keyrow item=position}{*Positionen*}
  <position>
<nummer>{$position->nummer}</nummer>
  <bezeichnung>{$position->bezeichnung}</bezeichnung>
  <beschreibung>{$position->beschreibung}</beschreibung>
  <menge>{$position->menge}</menge>
  <preis>{$position->preis}</preis>
  <einheit>{$position->einheit}</einheit>
</position>
  {/foreach}
  </positionen>
  {if $beleg->versand}
  <tracking>
  {foreach from=$beleg->versand key=keyversand item=tracking}{*Versand*}
<tracking>{$tracking->tracking}</tracking>
  {/foreach}
  </tracking>
{/if}
</auftrag>
```

## Smarty Eingehend (inbound oder Import)

Daten in xentral einzulesen (auch “inbound” genannt) ermöglicht es dir die Daten

1. aus einem anderen System zu importieren,
1. zu interpretieren, dann
1. in ein xentral Zielformat zu konvertieren und anschließend
1. in xentral zu importieren.

> **Anmerkung**
>
> Alle Inhalte, die im Eingangskonverter eingegeben werden, orientieren sich an den Standard-Templates aus dem Übertragen-Modul. Diese stellen gleichzeitig auch das Maximum an zu verarbeitenden Informationen dar. Informationen, welche darüber hinaus geliefert werden, bleiben unbeachtet.

Standardmäßig werden die meisten Inhalte korrekt über das $object-Array geparst. Wenn die Darstellung nicht passen sollte, kannst du mit alternativen Arrays arbeiten.

### Alternative smarty-objects

- **$csv:** ein Array aus Objekten mit dem Headerspalten als Keys
- **$csvwithoutheader:** ein Array aus Objekten ohne Headerspalten; Aufruf der Spalten in der Notation col0, col1, usw.
- **$xml:** ein Object das aus einem Xml gaparst wurde
- **$object:** ist ein $xml falls Ursprungsdaten ein gültiges xml waren
- **$original:** ist der Original-String des Eingangs

### Operationen

- {"Der Auftrag enthält keine Positionen"|error}
  gibt einen Fehler an Smarty aus, der in den Übertragungsmonitor geloggt wird

- {"SELECT nummer FROM artikel"|assignsql assign="artikelnummern"}
  speichert das Ergebnis der SQL-Abfrage in die Variable $artikelnummern

- {$original|replace:"1.0":"2.0"|getxml assign="neuesxml"}
  ersetzt alle Strings 1.0 zu 2.0 und speichert wandelt es in ein neues Objekt $neuesxml um

- {$position->nummer|pregreplace:'/[^0-9]/':''}
  führt eine reguläre Ersetzung auf das eine Objekt aus

### Beispiele

Nachfolgend zeigen wir dir Beispiele zur eingehenden Datenkonvertierung.

#### Beispiel 1: Umwandlung CSV-Datei in xml zur Auftragserstellung

```
<?xml version="1.0" encoding="UTF-8"?>
<response>
<xml>
{assign var="letztebestellnummer" value=0}{assign var="ersterbeleg" value=1}

<auftrag_list>{foreach from=$object key=keyrow item=position}{if $letztebestellnummer <> $position->beleg_belegnr and $ersterbeleg == 0}
</auftrag_position_list>
</auftrag>
{/if}

{if $letztebestellnummer <> $position->beleg_belegnr or $ersterbeleg == 1}
<auftrag>
{$ersterbeleg = 0}{$letztebestellnummer= $position->beleg_belegnr}
<datum>{$position->beleg_datum|date_format:"%d.%m.%Y"}</datum>
<versandart>{$position->beleg_versandart}</versandart>
<status>{$position->beleg_status}</status>
<projekt>{$position->beleg_projekt}</projekt>
<name>{$position->beleg_name_firma|escape:"html"}</name>
<adresszusatz>{$position->beleg_name_nachname|escape:"html"} {$position->beleg_name_vorname|escape:"html"}</adresszusatz>
<strasse>{$position->beleg_adresse_strasse} {$position->beleg_adresse_hausnummer|escape:"html"}</strasse>
<plz>{$position->beleg_plz}</plz>
<ort>{$position->beleg_ort}</ort>
<ihrebestellnummer>{$position->beleg_belegnr}</ihrebestellnummer>
<internebezeichnung>{$position->POSNR|string_format:"%.0f"}</internebezeichnung>
<email>{$position->beleg_email}</email>
<telefon>{$position->beleg_telefon}</telefon>
<lieferunterabteilung>
</lieferunterabteilung>
<internebemerkung>
</internebemerkung>
<auftrag_position_list>{/if}
<auftrag_position>
<name>{$position->artikel_bezeichnung|escape:"html"}</name>
<menge>{$position->artikel_menge}</menge>
<nummer>{$position->artikel_nummer}</nummer>
</auftrag_position>
{/foreach}
</auftrag_position_list>
</auftrag>
</auftrag_list>
</xml>
</response>
```

### Beispiel 2: Falllprüfung für Lagerzahlen inklusive SQL-Verwendung

Hintergrund: Lagerzahlen wurden von Fulfiller teilweise ohne MHD/Chargen-Infos übertragen. Via SQL wird geprüft, ob der Artikel MHD/Chargenpflichtig ist. Wenn ja, dann wird das template um statische Informationen erweitert.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<xml>
<artikel_list>
{assign var="counter" value = 0}
{foreach from=$object->xml->artikel_list->artikel key=key item=item}
{assign var="Nummer" value=$object->xml->artikel_list->artikel[$counter++]->nummer}
{"SELECT nummer, mindesthaltbarkeitsdatum, chargenverwaltung FROM artikel WHERE nummer = '$Nummer' and lagerartikel = 1 and geloescht<>1 "|assignsql assign="artikel"}
<artikel>
<nummer>{$item->nummer}</nummer>
<lagerzahl>{$item->lagerzahl}</lagerzahl>
{if!($item->lager_platz)}
<lager_platz>Hauptlager</lager_platz>{else} <lager_platz>{$item->lager_platz}</lager_platz> {/if}
{if $artikel[0]->nummer == $item->nummer && $artikel[0]->mindesthaltbarkeitsdatum == 1 && $artikel[0]->chargenverwaltung == 2}
<mhd>31.12.9999</mhd>
<charge>DUMMY</charge>
{elseif $artikel[0]->nummer == $item->nummer && $artikel[0]->chargenverwaltung == 2}
<charge>DUMMY</charge>
{/if}
</artikel>
{/foreach}
</artikel_list>
</xml>
</response>
```

#### Beispiel 3: Einlesen von CSV-Dateien ohne Kopfzeile

> **Anmerkung**
>
> Array von $csvwithoutheader wird nicht über den Bildschirm von $object ausgegeben. Den Inhalt aus $csvwithoutheader kannst du auch bspw. mit {$csvwithoutheader|@debug_print_var} ausgeben. Der Spaltenaufruf erfolgt über die Notation col0-n.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <xml>
  <artikel_list>
 {foreach from=$csvwithoutheader key=keyrow item=Ab}
  <artikel>
  <nummer>{$Ab->col0}</nummer>
  <lagerzahl>{$Ab->col1}</lagerzahl>
</artikel>
{/foreach}
  </artikel_list>
  </xml>
</response>
```

## Übertragung mit Typ API

API steht als technische Übertragungsart im Standard zur Verfügung. Weitere verfügbare Übertragungsarten sind FTP, FTPS (Benutzername und Passwort, keine Zertifikate), SFTP, E-Mail und die lokale Speicherung auf dem Server.

Der Umgang mit Smarty erfolgt hier nach derselben Weise, wie wenn eine andere Übertragungsart verwendet wird. Allerdings können hier api-spezifische Anforderungen wie Authentifizierung, Header oder application-type zu beachten sein. Wenn du mit einer Authentifizierung arbeitest, die ein Passwort benötigt, werden im Tab **Dateien** werden keine Enträge angezeigt. Erfolgreiche Übertragungen können zum aktuellen Zeitpunkt nur im Übertragen-Monitor nachvollzogen werden, wenn zum entsprechenden Beleg bzw. der entsprechenden Aktion “hochgeladen” in einer grünen Erfolgsmeldung steht. Möglicherweise werden nur unzureichende Fehlermeldungen bei der Übertragung zurückgemeldet, weshalb du hier auf ein ausführliches error-logging vom Zielsystem angewiesen bist.

## Besonderheiten im Übertragen-Modul

Hier zeigen wir dir Besonderheiten von Smarty im Übertragen-Modul.

### Verknüpfte Belege

In allen Belegen kannst du mit Hilfe von Smarty auf verknüpfte Belege zugreifen. Wenn z.B. zu einem Auftrag ein Lieferschein existiert, existiert auch ein Array $beleg->lieferschein[], in dem dann die entsprechenden Informationen des referenzierten Lieferscheines zur Verfügung stehen. Auf diese Art kannst du schnell auf ergänzende Belegnummern, Lieferdaten, Chargen oder Seriennummern zurückgreifen - auch bei der Erstellung eines Auftrages. Die Lieferscheinnummer z.B. erreichst du direkt über $beleg->lieferschein[0]->belegnr

Die Folgenden Daten stehen dir in den jeweiligen Belegen zur Verfügung, sofern ein entsprechender Beleg im System existiert.

Im Auftrag:

- $beleg->bestellung[]
- $beleg->angebot[]
- $beleg->lieferschein[]
- $beleg->rechnung[]
- $beleg->retoure[]
- $beleg->gutschrift[]

Im Lieferschein:

- $beleg->bestellung[]
- $beleg->rechnung[]

Beispiele:

Für die folgenden Beispiele benötigst du SQL. Die allgemeine Syntax für SQL-Abfragen im Übertragungen-Modul findest du im Abschnitt[SQL-Abfragen](#UUID-7173bf6b-953d-0500-1285-3235d3cfce20_id_360016773539_id_h_01FDS6QHPZXY5NR99QCXDVX912)dieses Artikels.

**Seriennummer **: Die Seriennummer eines Lieferscheins ist in der Tabelle ** belege_chargesnmhd**gespeichert. Du kannst über den folgenden SQL-Code auf den Wert zugreifen:

```
{foreach from=$beleg->positionen key=keyrow item=position}{*Positionen*}
  <position>
(...)
  {"SELECT wert FROM beleg_chargesnmhd WHERE doctype = 'lieferschein' AND type = 'sn' AND pos = '{$position->id}' "|assignsql assign="sn"}
  <seriennummer>{$sn[0]->wert}</seriennummer>
```**Internetnummer**: Um auf die Internetnummer eines mit dem Lieferschein verknüpften Auftrags zuzugreifen, kannst du den folgenden SQL-Code nutzen:```
<lieferschein>
(...)
  {"SELECT internet FROM auftrag WHERE id = '{$beleg->auftragid}' "|assignsql assign="internet"}
  <internet>{$internet[0]->internet}</internet>
```

In der Rechnung:

- $beleg->bestellung[]
- $beleg->lieferschein[]

#### ArtikelStammdaten aus Positionen ansprechen

Über die Belegpositionen kannst du auch "darunterliegende" Strukturen abrufen, die nicht direkt im Beleg gespeichert sind. Ein Beispiel dafür ist das Gewicht eines Artikels. Dieses kannst du über {$position->articledata->gewicht} abrufen. So kannst du z.B. durch eine Multiplikation mit der Menge der Position und dem Aufaddieren aller Gewichte auch das Gesamtgewicht aller Artikel eines Beleges berechnen und übertragen. Über $position->articledata kannst du alle Spalten aus der Tabelle artikel ansprechen. Dabei solltest du immer beachten, ob Informationen aus den Artikel-Stammdaten evtl. in der Auftragsposition bereits verändert worden sein könnten. Im Zweifelsfall solltest du den Wert aus dem Beleg verwenden.

### SQL-Abfragen

Im Übertragen-Modul kannst du zur Anreicherung von Daten auch allgemeine SQL-Anfragen erstellen und in den ausgegebenen Templates ausgeben. Dazu verwendest du folgende Syntax:

```{"SELECT gln, rechnung_gln FROM adresse where lieferantennummer = '{$beleg->lieferantennummer}' "|assignsql assign="adressdata"}```Auf das Ergebnis kannst du dann über das zugewiesene Array adressdata zugreifen:```{$adressdata[0]->gln} // for the targeted call of the array```

### Datenmanipulation und Formatumwandlung

Datumswerte können nach Anforderung ausgegeben werden:

- Int. Datumsformat (ISO 8601): {$beleg->datum|date_format:'%Y-%m-%d'}
- Deutsches Datumsformat (DIN 5008): {$beleg->datum|date_format:'%d.%m.%Y'}

Zahlen können nach Bedarf umformatiert werden. Hier am Beispiel der Spalte "Menge":

- Ausgabe ohne Nachkommastellen (als Ganzzahl): {$position->menge|string_format:'%d'}
- Ausgabe mit einer Nachkommastelle: {$position->menge|string_format:'%.1f'}
- Ausgabe mit zwei Nachkommastellen: {$position->menge|string_format:'%.2f'}

Grundsätzlich können alle Formate ausgegeben werden, die durch die Funktion sprintf in PHP verfügbar sind.

## Felddefinitionen

Hier findest du eine Auflistung der verschiedenen Felddefinitionen. Eine vollständige Auflistung der verfügbaren Felder inkl. einer Übersetzung der Feldnamen und einer Beschreibung der Inhalte in Englisch ist jeweils unterhalb des Screenshots verlinkt.

### Lieferschein

![smarty_delivery_note.png](https://help.xentral.com/hc/article_attachments/10728995013660)

Weitere Felddefinitionen findest du[hier](https://help.xentral.com/hc/de/articles/4405304107026#UUID-c256ae4c-84cd-1a0b-fb33-b5210d57d6da).

### Tracking Rückmeldung

![smarty_tracking.png](https://help.xentral.com/hc/article_attachments/10729009114524)

Weitere Felddefinitionen findest du[hier](https://help.xentral.com/hc/de/articles/4405304107026#UUID-c256ae4c-84cd-1a0b-fb33-b5210d57d6da).

### Lagerzahlen-Rückmeldung

![smarty_stock_figures.png](https://help.xentral.com/hc/article_attachments/10729029800860)

Weitere Felddefinitionen findest du[hier](https://help.xentral.com/hc/de/articles/4405304107026#UUID-c256ae4c-84cd-1a0b-fb33-b5210d57d6da).

## Features

Mit Hilfe der integrierten Template-Engine Smarty können einfach und flexibel zeichenbasierte Ausgabestrukturen von Datenformaten wie CSV, XML oder JSON an die Bedürfnisse des Kunden angepasst werden. Im Grunde muss lediglich das vorhandene Zielformat in eine Textdatei kopiert und mit den entsprechenden Variablen gefüllt werden. Diese können dabei noch umformatiert werden.

Belegdaten finden sich z.B. in der Smarty-Variable $beleg und werden in gewohnter PHP-Objektschreibweise angesprochen, z.B. $beleg->kundennummer oder $beleg->belegnr. Die Namensgebung gleicht der Benennung von Datenbank-Spaltennamen.

Auch ein Zugriff auf komplexere Strukturen ist möglich (je nach Beleg). So kann im Lieferschein auf den zu Grunde liegenden Auftrag zugegriffen werden: $beleg->auftrag->lieferdatum. Verkürztes Beispiel mit fiktivem Format:

```
{*Beleg-Stammdaten --------------------------------*}
 {$beleg->status}
 {$beleg->datum|date_format:'%d.%m.%Y'}
 {$beleg->belegnr}
 {$beleg->kundennummer}
 {$beleg->name} 
{*Access to data of the underlying order*} 
{$beleg->auftrag->lieferdatum} 
{*Other fields removed*}
```

```
{*Positionen - Beginn ------------------------------*}
 {*loop through all available items*}
 {foreach from=$beleg->positionen key=keypos item=position}
 {$position->nummer}
 {$position->name}
 {$position->beschreibung}
 {$position->menge}
 {$position->preis}
 {*Other fields removed*}
 {/foreach}
{*Positionen - Ende --------------------------------*}
```

## Beispiele

Im Folgenden haben wir dir einige Beispiele zusammengefasst, die dir die Ausgabe verschiedener Lieferscheinformate in den Formaten EDI, CSV und XML ermöglichen. Bitte prüfe bei eigener Anwendung die Spaltenbeschriftungen (CSV), Tagnamen (XML) und EDI-Spezifikationen. Natürlich sind auch weitere Ausgabeformate (wie z.B. JSON) denkbar.

### Beispiel Lieferschein CSV (ausführlich)

Das folgende Beispiel listet ein ausführliches Beispiel für einen Export eines Lieferscheines in verschiedenen Formaten.

#### Format EDI

- wird ergänzt -

#### Format CSV

```"tracking"; "document_status"; "document_date"; "document_delivery_date"; "document_actual_delivery_date"; "document_shipping_method"; "document_payment_method"; "document_document_nr"; "document_main_document_nr"; "document_customer_number"; "document_name"; "document_department"; "document_subdepartment"; "document_address_addition"; "voucher_contact_person"; "voucher_phone"; "voucher_email"; "voucher_country"; "voucher_street"; "voucher_plz"; "voucher_location"; "voucher_project"; "voucher_action"; "voucher_internal_note"; "voucher_internal_name"; "voucher_free_text"; "voucher_your_order_number"; "voucher_delivery_condition"; "voucher_type"; "item_number"; "item_designation"; "item_description"; "item_quantity"; "item_price"; "item_discount"; "item_currency"; "item_delivery_date"; "item_sort"; "item_tax"; "item_unit"; "item_tariff_number"; "item_country_of_origin"; "item_article_number_customer"; "desired_delivery_date"; "item_free_field1"; "item_free_field2"; "item_free_field3"; "item_free_field40"{foreach from=$voucher->items key=keyrow item=item}{*items *}\"{$item->tracking}";\"{$voucher->status}";\"{$voucher->date|date_format: '%d. %m. %Y'}";\"{$voucher->delivery date}";\"{$voucher->actual delivery date}";\"{$voucher->shipping method}";\"{$voucher->payment method}";\"{$voucher->voucher_number}";\"{$voucher->main_voucher_number}"; \"{$voucher->name}";\"{$voucher->department}";\"{$voucher->subdepartment}";\"{$voucher->address}";\"{$voucher->contact person}";\"{$voucher->phone}";\"{$voucher->email}";\"{$voucher->country}"; \"{$voucher->street}";\"{$voucher->plz}";\"{$voucher->location}";\"{$voucher->project}";\"{$voucher->action}";\"{$voucher->internal remark}";\"{$voucher->internal name}";\"{$voucher->free text}"; \"{$document->your order number}";\"{$document->delivery condition}";\"{$document->type}";\"{$item->number}";\"{$item->designation}";\"{$item->description}";\"{$item->quantity|string_format: '%. 2f'}";\"{$item->price}";\"{$item->discount}";\"{$item->currency}";\"{$item->delivery date}";\"{$item->location}";\"{$item->sales tax}";\"{$item->unit}";\"{$item->tariff number}"; \"{$item->country of origin}";\"{$item->part number customer}";\"{$voucher->order->date of delivery}";\"{$item->free field1}";\"{$item->free field2}";\"{$item->free field3}";\{* If applicable. other free fields *}";\"{$position->freefield40}";\ {/foreach}```#### Format XML```{$voucher->status} {$voucher->date|date_format:'%d.%m.%Y'} {$voucher->delivery date} {$voucher->actual delivery date} {$voucher->shipping method} {$voucher->payment method} {$voucher->document number} {$voucher->main document number} {$voucher->customer number} {$voucher->name} {$voucher->department} {$voucher->subdepartment} {$voucher->address supplement} {$document->contact person} {$document->phone} {$document->email} {$document->country} {$document->street} {$documents->plz} {$voucher->location} {$voucher->project} {$voucher->action} {$voucher->internal remark} {$voucher->internal description} {$voucher->free text} {$voucher->your order number} {$voucher->delivery condition} {$voucher->type} {foreach from=$voucher->items key=keypos item=item} {$item->number} {$item- >name} {$item->description} {$item->quantity} {$item->price} {$item->discount} {$item->currency} {$item->delivery date} {$item->location} {$item->tax} {$item->unit} {$item->tariff number} {$item->country of origin} {$item->article number customer} {$item->freefield1} {$item->freefield2} {$item->freefield3} {* Other free fields if necessary *} {$item->freefield40} {/foreach} {if $bill->shipping} {foreach from=$bill->shipping key=keyshipping item=tracking} {* shipping*} {$tracking->tracking} {/foreach} {/if}```

### Beispiel Lieferschein mit MHD

Im Folgenden werden Beispiele als Ergänzung zu obigen Code-Beispielen gezeigt, die nur die Besonderheiten in Bezug auf MHDs in einer Position berücksichtigen.

#### Format CSV

- wird ergänzt -

#### Format XML

- wird ergänzt -

### Beispiel Lieferschein mit Charge

Im Folgenden werden Beispiele als Ergänzung zu obigen Code-Beispielen gezeigt, die nur die Besonderheiten in Bezug auf Chargen in einer Position berücksichtigen.

#### Format CSV

- wird ergänzt -

#### Format XML

- wird ergänzt -

### Beispiel Lieferschein mit Charge und MHD

Im Folgenden werden Beispiele als Ergänzung zu obigen Code-Beispielen gezeigt, die nur die Besonderheiten in Bezug auf MHDs und Chargen in einer Position berücksichtigen.

#### Format CSV

- wird ergänzt -

#### Format XML

- wird ergänzt -

### Beispiel Auftrag

Anwendbar nur bei direktem Fulfillment ohne Autoversand. Diese Option sollte genau geprüft werden, meistens ist die Übertragung von Lieferscheinen der optimale Weg.

#### Format EDI

- wird ergänzt -

#### Format CSV

- wird ergänzt -

#### Format XML

- wird ergänzt -