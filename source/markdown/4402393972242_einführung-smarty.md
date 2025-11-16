Hinter Smarty verbirgt sich eine Technik, die es dir ermöglicht, schnell und übersichtlich Daten zu konvertieren. Du kannst dabei alle textbasierten Formate konvertieren, gleich ob es sich um CSV-, XML, JSON- oder anders strukturierte Dateien handelt.

Smarty kannst du an verschiedenen Stellen in xentral nutzen:

- Smarty im Übertragen-Modul
- Smarty in Shop-Schnittstellen

Die verfügbaren Funktionen und dazugehörigen Modifier sind zum großen Teil identisch. Auf Besonderheiten weisen wir daher in den entsprechenden Abschnitten der Dokumentation hin. Smarty ist in xentral an den entsprechenden Stellen bereits enthalten. Das herunterladen von Libraries ist nicht notwendig.

## Vorgehensweise

Basis der Umwandlung ist immer das sog. Smarty Template. Darin wird das Format und die Struktur des ausgehenden Dokumentes definiert. Dazu kannst du einfach das Zielformat in Form einer Beispieldatei in den Template-Editor kopieren. Anschließend werden die Beispieldaten durch Variablen ersetzt und können dann vom System gefüllt werden.

Am Beispiel eines Auftrages als XML-Datei wird hier verdeutlicht, wie diese Umwandlung stattfinden kann.

Das folgende Format soll ausgegeben werden:

```
<?xml version="1.0" encoding="utf-8"?>
<auftrag>
  <belegnr>200259</belegnr>
  <kundennummer>100112</kundennummer>
  <name>Max Musterman</name>
  <strasse>Beispielstrasse 13</strasse>
  <plz>86150</plz>
  <ort>Augsburg</ort>
  <positionen>
<position>
<nummer>Art_001</nummer>
  <bezeichnung>Beispielartikel 1</bezeichnung>
  <menge>3</menge>
  <preis>7.96</preis>
</position>
<position>
<nummer>Art_002</nummer>
  <bezeichnung>Beispielartikel 2</bezeichnung>
  <menge>10</menge>
  <preis>399.99</preis>
</position>
  </positionen>
</auftrag>
```Diese Beispieldatei wird in den Template-Editor kopiert. Anschließend werden die Beispielwerte mit den zugehörigen Variablen ersetzt.```
<?xml version="1.0" encoding="utf-8"?>
<auftrag>
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
</auftrag>
```

Dabei wird je nach Bereich ein Basisobjekt verwendet, um auf die Werte zuzugreifen. Je nach Einsatzgebiet ist das ein anderes Objekt:

- **$beleg**→ Übertragen-Modul: Ausgehende Belegdaten verarbeiten
- **$artikelliste**→ Übertragen-Modul: Ausgehende Artikel oder Lagerbestände (Lagerzahlen) verarbeiten
- **$trackingliste**→ Übertragen-Modul: Ausgehende Trackinginformationen verarbeiten
- **$salesreportlist**→ Übertragen-Modul: Ausgehende Belegdaten verarbeiten
- **$object**→ Übertragen-Modul: Eingehende Daten verarbeiten
- **$cart** → Shop-Schnittstelle: Warenkorb verarbeiten

## Funktionen und Modifier

Die meisten der hier beschriebenen Beispiele stammen aus dem Standard-Umfang der verwendeten Template-Engine Smarty. Weitere Funktionen findest du daher in der offiziellen[Smarty-Dokumentation](https://www.smarty.net/docs/en/language.modifiers.tpl).

Grundsätzlich werden Funktionen oder Modifier nach dem Pipe-Zeichen ( |) in der Variable geschrieben, ggf. mit nachfolgenden Parametern, abgetrennt durch einen Doppelpunkt.

Template: { Wert oder $Variable | Modifier oder Funktion: Weitere Parameter}

### Beispiele

Das folgende Script zeigt dir beispielhaft die Verwendung von Smarty mit Konstanten, Wertzuweisungen, Variablen, Funktionen und Modifiern. Einige davon werden im Folgenden genauer beschrieben.

```
<xml>

{*0. Statisch*}
<auftragsdaten></auftragsdaten>
<transactions/>
<anrede>herr</anrede>

{*1. Wertzuweisung*}
<waehrung>{$cart->auftragsdaten->currency}</waehrung>

{*2. Rechnen*}
<gesamtsumme>{($cart->auftragsdaten->total_price - 5)}</gesamtsumme>

{*3. Variablenzuweisung*}
{assign var=data value=$cart->auftragsdaten}
<email>{$data->email}</email>

{*4. Funktionen*}
<bestelldatum>{$cart->auftragsdaten->processed_at|truncate:10:''}</bestelldatum>

{*5. Verzweigungen*}
{if $cart->auftragsdaten->total_tip_received > 0}
 <freitext>Danke für die Spende von {$cart->auftragsdaten->total_tip_received} {$cart->auftragsdaten->currency}!!!</freitext>
{else}
 <freitext>Geiz ist geil!</freitext>
{/if}

{*6. Schleifen*}
{foreach key=key item=item from=$cart->auftragsdaten->note_attributes}
  {if $item->name == "google-clientID"}
<internebemerkung>Google ClientID: {$item->value}</internebemerkung>
  {/if}
{/foreach}
</xml>
```

### Script-Funktionen

#### Assign / Variablen und Inhalte zuweisen

Durch den Befehl assign können Variablen erstellt und ihnen Werte zugewiesen werden. Dies kann zur Vereinfachung der Lesbarkeit im Template verwendet werden.

Template:

```{assign var=order value=$cart->auftragsdaten}```

Ergebnis: Der Wert von $cart->auftragsdaten->datum ist verkürzt erreichbar unter $order->datum.

Weitere Definitionen findest du in der Dokumentation der[Smarty Funktion assign](https://www.smarty.net/docs/en/language.function.assign.tpl).

### Zahlenbearbeitung

Hier erfährst du, wie du Zahlen bearbeiten kannst.

#### Nachkommastellen kürzen

Eine Zahl soll auf drei Nachkommastellen gekürzt werden. Anschließend soll der Punkt durch ein Komma ersetzt werden. Anstelle einer Zahl kann es natürlich auch eine Variable oder das Ergebnis einer Berechnung sein.

Template:

```{1.12345|string_format:"%1\$.3f"|replace:".":","}```

Ergebnis: 1,123

Weitere Definitionen findest du in der Dokumentation des[Smarty Modifiers string_format](https://www.smarty.net/docs/en/language.modifier.string.format.tpl).

#### Einfache Berechnungen

Neben komplexeren Berechnungen kannst du auch einfache Berechnungen direkt in der Ausgabe der Variablen vornehmen. Dazu musst du lediglich eine Klammer () um den Ausdruck setzen.

Template:

```{($cart->versandkostenbrutto-0.95)}```

Ergebnis: Ausgabe des Restwertes, z.B. bei 4,95 = 4

### Textbearbeitung

Hier erfährst du, wie du Texte bearbeiten kannst.

#### Textlänge begrenzen

Sollte beispielsweise im Warenkorb ein langer Textwert für den Namen (order => name =>) “Max Mustermann” importiert werden, könnte dieser auch mit Hilfe von Smarty auf eine feste Textlänge (in Zeichen) gekürzt werden.

Template:

```{$cart->order->name|truncate:3}```

Ergebnis: Max…

oder:

```{$cart->order->name|truncate:3,””}```

Ergebnis: Max

Weitere Definitionen findest du in der Dokumentation des[Smarty Modifiers truncate](https://www.smarty.net/docsv2/de/language.modifier.truncate.tpl).

Alternativ kannst du auch mit Hilfe der String-Formatierung arbeiten:

Template:

```{$cart->order->name|string_format:"%s{3}"}```

Weitere Definitionen findest du in der Dokumentation des[Smarty Modifiers string_format](https://www.smarty.net/docs/en/language.modifier.string.format.tpl)

#### Textenden bereinigen

Ersetzt mehrfache Leerzeichen, Zeilenumbrüche und Tabulatoren im Inhalt der Variable durch ein Leerzeichen oder eine alternative Zeichenkette (im zweiten Beispiel &nbsp;).

Template:

```{$cart->order->name|strip}```oder```{$cart->order->name|strip:&nbsp;}```

Weitere Definitionen findest du in der Dokumentation des[Smarty Modifiers strip](https://www.smarty.net/docsv2/de/language.modifier.strip.tpl).

#### Text suchen und ersetzen

Template:

```{$original|replace:“foo":“bar”|getxml assign=“newxml”}```

Ersetzt alle Strings foo zu bar und speichert / wandelt es in ein neues Objekt $newxml um.

#### Text mit Regular Expression suchen und ersetzen

Template:

```{$position->nummer|pregreplace:‘/[^0-9]/‘:’’}```

Führt eine reguläre Ersetzung auf dem Element aus.

Weitere Definitionen findest du in der Dokumentation des[Smarty Modifiers regex/replace](https://www.smarty.net/docsv2/de/language.modifier.regex.replace.tpl).

### Fehlerbearbeitung / Logging

Hier erfährst du, wie du Log-Einträge erstellst.

#### Logging im Übertragen-Modul

template:

```{“Der Auftrag enthält keine Positionen”|error}```

Gibt einen Fehler an Smarty aus, der geloggt und im Monitor des Übertragung-Moduls ausgegeben wird.

### Ausgabe von Daten

Template:

```{$orderData|@debug_print_var}```

Gibt die Daten des vorangestellten Elements im Output-Fenster aus.

## Bedingungen

Mit Hilfe von Bedingungen kann bereits im Template mit Logik gearbeitet werden, um kundenspezifische Entscheidungen bereits beim Ex- oder Import von Daten in verschiedene Ergebnisse zu überführen.

Im folgenden Beispiel wird beim Import eines Auftrages über eine Shop-Schnittstelle der englische Wert “mr” in die Anrede “herr” überführt, die in xentral für den Adresstyp und die Anrede “Herr” steht.

Beispiel Shopimporter:

```
<xml>
  <name>Max Mustermann</name>
  {if $cart->order->salutation == “mr”}
  <anrede>herr</anrede>
  {else}
  <anrede>frau</anrede>
  {/if}
</xml>
```Alternative Schreibweise (Shopimporter)```
<xml>
  <name>Max Mustermann</name>
  <anrede>
  {if $cart->order->Salutation == “mr”}
  herr{else}frau{/if}
  </anrede>
</xml>
```Weitere alternative Schreibweise zum Überschreiben eines Knotens (Shopimporter)```
<xml>
  <name>Max Mustermann</name>
  <anrede>frau</anrede>
  {if $cart->order->salutation == “mr”}
  <anrede>herr</anrede>
  {/if}
</xml>
```

In diesem Beispiel überschreibt der zweite gleichlautende Knoten (anrede) bei Zutreffen der Bedingung den vollständigen ersten Knoten inkl. Wert und ersetzt so den Inhalt.

Weitere Definitionen findest du in der Dokumentation[Smarty if/else](https://www.smarty.net/docs/en/language.function.if.tpl).

## Schleifen

Schleifen ermöglichen die Abarbeitung von Wertelisten (Arrays), z.B. Auftragspositionen, Steuersätze, o.ä. Ergebnis sind meist Key-Value-Pairs, die dann im zweiten Schritt ausgewertet werden können. Dazu werden diese Listen in einer Schleife durchlaufen und bearbeitet.

Im folgenden Beispiel wird für eine gegebene Struktur der Rechnungsadresse ein beliebiges Element herausgegriffen, um z.B. eine gesonderte Einstellung für das Land zu setzen.

Beispiel Shopimporter

Warenkorb:

```
...
billing => [
  0 => [name => country, value => DE],
  1 => [name => street, value => Musterweg],
  2 => [name => house_no, value => 2],
  3 => [name => phone, value => 123456789],
  4 => [name => first_name, value => Max],
...
```Template:```
<xml>
  {foreach key=billingKey item=billingData from=$cart->billing}
  {if $billingData->name == ”country”}
  <land>{$billingData->value}</land>
  {/if}
  {/foreach}
</xml>
```

Weitere Definitionen findest du in der[Dokumentation von Smarty zu Schleifen am Beispiel foreach](https://www.smarty.net/docs/en/language.function.foreach.tpl)

## Tipps und Tricks

Hier findest du einige Tipps und Tricks, die dir eventuell weiterhelfen können.

### Strings mit CDATA escapen

Viele Daten, die in Smarty übermittelt oder eingelesen werden können, beinhalten Zeichen, die durch die Weiterverarbeitung fehlinterpretiert werden können. Daher ist es wichtig, die übermittelten Inhalte von den strukturellen Daten zu unterscheiden. Dazu kannst du die Daten durch einem CDATA-Block umschließen und somit “escapen”.

Template:

```<![CDATA[{$orderData->total_price}]]>```

Weitere Informationen zu[CDATA und dessen Verwendung](https://en.wikipedia.org/wiki/CDATA).

### Letztes Element einer Schleife

Gerade bei der Ausgabe von JSON oder XML-Listen kann es wichtig sein, das Listenelement sauber abzuschließen. Um invalide Datenstrukturen zu erhalten, müssen alle Elemente mit einem Komma abgeschlossen werden, die nicht am Schluss der Liste stehen. Dazu kannst du die Syntax $item@last verwenden.

Beispiel

Ausgabe einer JSON-Datei mit dem Artikelbestand:

```
{"SELECT *... "|assignsql assign="stock"}
{
  "stock": [
  {foreach from=$stock key=keyrow item=st}
  {
  "materialId": "{$st->nummer}",
  "quantity": "{$st->menge}",
  "warehouse": "{$st->kurzbezeichnung}"
},

  {if $st@last}
  {
  "materialId": "{$st->nummer}",
  "quantity": "{$st->menge}",
  "warehouse": "{$st->kurzbezeichnung}"
}
  {/if}
  {/foreach}
]}
```