### Achtung **Wichtige Mitteilung: Nutzung der neuesten API empfohlen***(letzte Aktualisierung dieser Information: 01/2025)* Bitte beachte, dass die beiden älteren API-Versionen (REST-API und die zuvor eingeführte API) abgekündigt sind und sich im Wartungsmodus befinden.Wir empfehlen Ihnen dringend, die **neueste API-Generation ** zu verwenden, da diese aktiv weiterentwickelt wird, neue Funktionen bietet und Sicherheitsstandards erfüllt. **Vorteile der neuesten API:**

- Erweiterte Funktionalitäten
- Verbesserte Leistung und Stabilität
- Zukunftssichere Entwicklung

Weitere Informationen zur neuen API und zur Migration findest du in der[API-Dokumentation](https://developer.xentral.com/reference/intro), allgemeine Informationen im Helpcenter-Artikel[API Dokumentation und Ressourcen (Neue Xentral API)](https://help.xentral.com/hc/de/articles/6618896113820#UUID-03a6d5d2-0c6b-65c8-6753-4bc5ad5bb509). Für Fragen oder Unterstützung bei der Migration steht unser Support-Team gerne zur Verfügung.

Dieser Artikel behandelt die Legacy-API von Xentral. Wir empfehlen jedoch die Nutzung der neuesten Generation der XentralAPI, da diese kontinuierlich weiterentwickelt wird und modernste Funktionalitäten bietet.

In Xentral stehen derzeit zwei Legacy-APIs zur Verfügung:

- **REST-API (Legacy)**: Die REST-API-Dokumentation für die abgekündigte Version ist weiterhin verfügbar und enthält alle relevanten Informationen zur Nutzung dieser API, einschließlich der Erstellung eines API-Accounts, der Gestaltung von Anfragen sowie der Liste der verfügbaren Endpunkte. Die Dokumentation kann unter www/api/docs.html oder online abgerufen werden: [REST-API-Dokumentation (Legacy)](https://update.xentral.biz/apidoc/docs211.html). Bitte beachte, dass diese API-Version sich im Wartungsmodus befindet und keine neuen Funktionen oder Updates erhält.
- **Standard-API (Legacy)**: Die folgende Dokumentation beschreibt eine ältere, vor der REST-API eingeführte API-Version, die für die Anbindung externer Systeme genutzt werden kann. Sie unterstützt grundlegende Funktionen wie das Anlegen und Bearbeiten von Adressen, Aufträgen und Benutzern, Single Sign-On sowie Event-Handler für Rückmeldungen an Fremdsysteme. Diese API wird nicht weiterentwickelt und ist ausschließlich für bestehende Integrationen vorgesehen.

## REST API (Legacy)

> **Wichtig**
>
> Wir empfehlen nicht mehr die Anbindung der Standard-API über die Hash-Authentifizierung vorzunehmen. Stattdessen ist unsere Empfehlung die REST-API, mit der auch die Funktionsaufrufe der Standard-API (dieser API) vorgenommen werden können.

Ab Version 18.3 gibt es in der xentral ERP-Software zusätzlich eine REST-API, die künftig weiter ausgebaut wird und später die alten API-Aufrufe ablösen soll. Spezifische Infos zur xentral-API findest du hier.

Die Dokumentation zur REST-API befinden sich in der Installation unter www/api/docs.html. Dort wird erklärt, wie ein API-Account angelegt werden kann, wie Anfragen an API-Ressourcen aussehen müssen, welche API-Endpunkte existieren, usw.

Die API-Dokumentation wird mit xentral ausgeliefert und kann in jeder xentral-Instanz unter instanzname/www/api/docs.html im Browser aufgerufen werden. Oft wird das /www/ jedoch nicht benötigt.

Alternativ ist die API-Dokumentation, nach Versionen gegliedert, auch online zu finden:[https://update.xentral.biz/apidoc/docs224.html](https://update.xentral.biz/apidoc/docs224.html)

Prinzipiell kann die Version im Pfadname angegeben werden, Die Version 22.4 findet sich beispielsweise im Pfad docs224.html.

### Weitere Informationen zu Rest-APIs

Bei der Bereitstellung von Tracking-Nummern über die API ist keine weitere Übertragung vorgesehen, um diese Informationen an die Shops zu übermitteln.

Diese Aufgabe kann durch den Cronjob (shop_rueckmeldung) erledigt werden. Dies funktioniert jedoch nur für die folgenden logistischen Modi:

![API-Documentation.png](https://help.xentral.com/hc/article_attachments/10178120500124)

> **Anmerkung**
>
> Mit der neuen Versionen (ab 22.1.x) ist die Authentifizierung per Hash nicht mehr notwendig/möglich. Wir setzen auf DIGEST in Zusammenhang mit unseren REST-API.

## Standard-API (Legacy)

Die folgende API Dokumentation bezieht sich NICHT auf die REST-API (siehe oben). Für die Anbindung externer Systeme bietet xentral eine API an, die im Folgenden beschrieben wird.

### Achtung

Ab Version 22.1.x wird die Hash-Authentifizierung nicht mehr unterstützt, daher musst du über die REST-API auf DIGEST Auth umstellen.

### Funktionsumfang

Funktionen der API:

- Anlegen und Bearbeitung von Adressen
- Anlegen und Bearbeitung von Aufträgen
- Anlegen und Bearbeitung von Benutzern
- Single Sign On / Externes starten und beenden der Session aus einem zentralen Login
- Rückmeldung bei Änderungen in xentral in das Fremdsystem (Event-Handler)

### Abkürzungsverzeichnis

- Fremdsystem (z.B. das eigene Webbackend aus einem eigenen Portal)
- xentral (Zentrale Installation von xentral)
- Hash (Authentifizierungs-Token für API)
- Methode (Aufruf der Methode / Ist in URL der Parameter action='Name der Methode bzw. Request')

### Zugriff

Um mit der API kommunizieren zu können, wird ein Hash benötigt. Um einen Hash zu erstellen, ist unter Administration → Einstellungen → Grundeinstellungen → API's zu gehen. Der Haken "API aktiviert" muss gesetzt sein. Unter "Initkey" muss eine beliebig lange und aus beliebigen Buchstaben und Zahlen zusammengesetzte Zeichenkette stehen, die keine Satz-, Sonderzeichen oder Umlaute beinhaltet. Unter "Remote Domain" ebenfalls eine beliebige Kennung z.B: die Domain, von der aus die API genutzt wird (www.meinedomain.de). Wichtig ist, dass diese auch auf der anderen Seite im Client Quelltext angegeben ist. Am Ende darf kein / stehen. Außerdem muss der "UTF8 Clean" Haken gesetzt bleiben. Zum Abschluss ist auf die "Speichern"-Schaltfläche zu klicken.

Nach dem Speichern wird bei "Aktueller Key" der Hash erstellt.

Prinzipiell gibt es zwei Möglichkeiten für die Kommunikation

- Standard Request (Standard POST Request vom Fremdsystem) um z.B. Aufruf einer Methode um einen neuen Auftrag, Adresse oder Benutzer über die API anzulegen bzw. zu bearbeiten
- Event Handler (Standard POST Request von xentral): xentral ruft eine hinterlegte URL auf, wenn ein Auftrag, Adresse, Benutzer o.ä. erstellt oder geändert wird

Der POST Request wird an die URL

index.php?module=api&action='Request'&hash=XXXXXXXXXXXXXXXX gesendet.

Als POST Variablen müssen immer dabei sein:

- xml (optional wenn Datenstrukturen notwendig sind)

In der Variable xml muss das Format wie folgt aussehen:

```
  <?xml version="1.0" encoding="UTF-8"?>
<request>
  <status>
  <function>ArtikelCreate</function>
  </status>
  <xml>
  <name_de>Saft Bene</name_de>
  <nummer>1616161</nummer>
  <einkaufspreise>
  <staffelpreis>
  <ab_menge>1</ab_menge>
  <preis>728.22</preis>
  <lieferantennummer>70000</lieferantennummer>
  </staffelpreis>
  </einkaufspreise>
  <verkaufspreise>
  <staffelpreis>
  <ab_menge>1</ab_menge>
  <preis>718,22</preis>
  </staffelpreis>
  <staffelpreis>
  <ab_menge>1</ab_menge>
  <preis>618,22</preis>
  <kundennummer>10006</kundennummer>
  <projekt>VM001</projekt>
  </staffelpreis>
  </verkaufspreise>
  </xml>
</request>
</nowiki>

  
```Sendet die Methode Request eine Antwort, erfolgt diese als XML Struktur:```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>Aufgerufene Methode</action>
  <message>Statusnachricht</message>
  <messageCode>Statuscode (Bei Erfolg: 1, siehe unten)</messageCode>
  </status>
  <md5sum></md5sum>
  <xml></xml>
</response>

  
```

### Statuscodes

Folgende Statuscodes sind möglich:

- 1: Erfolg, alles OK (OK)
- 2: Hash falsch (Wrong Hash)
- 3: Zu wenige GET Parameter (Wrong number of GET parameters)
- 4: Falsche XML Daten (Wrong XML data structure for method)
- 5: Falscher Schlüssel (id) (Invalid key (id))
- 6: Falsche MD5-Summe (Wrong md5sum)
- 7: Username existiert bereits (Username exists already)
- 8: Daten nicht gefunden (Data not found)
- Sonst: (Unkown message code)

### API Hash für Authentifizierung

Für den Zugriff auf die API wird ein Token benötigt. Es wird empfohlen, per https auf die API zuzugreifen.

```
  function generateHash()
{
  
  $initKey = 'EXsl4ywgDR5mR3sTGwws9Ikl2ocSKZlvhxoFTv8Au3MaV5UqrEIJORVF5PmFNy';
  $appName = 'NameDerApp';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $appName. $date);
  
  return $hash;
}

  
```

### Standard Request an xentral senden

Ist das API Modul vorhanden, kann wie folgt darauf zugegriffen werden:

index.php?module=api&action='Request'&hash='Hash'

Per URL wird die Methode bzw. der Request definiert. Optionale Daten werden als POST an die API übertragen.

Zur einfachen Kommunikation können diese Funktionen verwendet werden:

```
  function SendRequest($methodname,$xml,$hash)
{
  $url = 'http://server.com/index.php?module=api&action='.$methodname.'&hash='.$hash;
  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

  
```Als Antwort für den Request folgt eine XML Nachricht:```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>Aufgerufene Methode</action>
  <message>Statusnachricht</message>
  <messageCode>Statuscode</messageCode>
  </status>
  <md5sum></md5sum>
  <xml></xml>
</response>

  
```

### Event Handler Aufruf entgegennehmen

Zum Empfang und Auswerten von Events von xentral an das Fremdsystem werden folgende Variablen per POST übertragen.

per URL:?action=YYYYY&hash=XXXXXXXXX

```
  <?php

$action = $_GET['action'];
$hash = $_GET['hash'];
$xml = $_POST['xml'];
$md5sum = $_POST['md5sum'];

?>

  
```

### Liste mit Standard Requests

Im Folgenden werden die Standard Requests tabellarisch aufgezeigt:

| Request (Parameter action) | Beschreibung | GET Parameter | XML Daten | XML Rückgabe im Erfolg | Beschreibung Rückgabe im Erfolg |
| --- | --- | --- | --- | --- | --- |
| AdresseCreate | Anlegen einer neuen Adresse | - | XML Adresse per POST in Feld xml (kundennummer=`new` wenn eine vergeben werden soll) | <id>34</id><kundennummer></kundennummer> | Neue ID der Adresse bzw. Kundennummer |
| AdresseEdit | Änderung einer bestehenden Adresse | `id ` oder`kundennummer ` und optional`projekt` | XML Adresse per POST in Feld xml | - | - |
| AdresseGet | Abfragen einer bestehenden Adresse | `id ` oder`kundennummer ` und optional`projekt`. | - | XML Adresse | Datenstruktur der angefragten Adresse |
| AuftragCreate | Anlegen eines neuen Auftrags | - | XML Auftrag per POST in Feld xml (belegnr=`new ` wenn eine vergeben werden soll) (**Hinweis:** Feld kundennummer ist ein Pflichtfeld bzw. kann mit dem Wert`new` ein neuer Datensatz angelegt werden) Daten wie Zahlungsweisen, Versandarten usw. werden aus den Zusatzdaten des Kundenstamm gezogen, sofern diese nicht explizit übergeben werden | <id>34</id><belegnr></belegnr> | Neue ID des Auftrags bzw. Belegnummer |
| AuftragEdit | Änderung eines bestehenden Auftrags | `id ` oder`belegnr ` und optional`projekt` | - | - | - |
| AuftragGet | Abfragen eines bestehenden Auftrags | `id ` oder`belegnr ` und optional`projekt` | - | XML Auftrag | Datensatz des Auftrags |
| AuftragAbschliessen | Abschluss eines Auftrags | - | XML per POST, enthält ID des Auftrags | XML Antwort Code | 1-OK, 5-falsche ID oder Auftrag bereits abgeschlossen |
| WeiterfuehrenAuftragZuRechnung | Weiterführung eines Auftrag zur Rechnung | - | XML per POST, enthält ID des Auftrags | XML ID | Gibt die ID der erzeugten Rechnung zurück |
| WeiterfuehrenRechnungZuGutschrift | Weiterführen einer Rechnung zur Gutschrift | - | XML per POST, enthält ID der Rechnung | XML ID | Gibt die ID der erzeugten Gutschrift zurück |
| ArtikelCreate | Anlegen eines neuen Artikels | - | XML Artikel | - | Neue ID des Artikels bzw. Artikelnummer |
| ArtikelEdit | Änderung eines bestehenden Artikels | `id ` oder`nummer ` und optional`projekt` | XML Artikel | - | - |
| ArtikelGet | Abfragen eines bestehenden Artikels | `id ` oder`kundennummer ` und optional`projekt` | - | XML Artikel | Datenstruktur des Artikels |
| BenutzerCreate | Anlegen eines neuen Benutzers | - | - | - | Neue ID des Benutzers |
| BenutzerEdit | Änderung eines bestehenden Benutzers | `id` des Benutzers | - | - | - |
| BenutzerList | Abfragen der Liste von Benutzern | - | - | XML Benutzerliste | Vereinfachte Liste von Benutzern |
| BenutzerGet | Abfragen eines bestehenden Benutzers | `id` des Benutzers | - | - | Datenstruktur des Benutzers |
| BenutzerGetRFID | Abfragen eines bestehenden Benutzers anhand der RFID | - | XML `rfid` des Benutzers | XML Benutzer | Datenstruktur des Benutzers |
| AdresseKontaktCreate | Anlegen einer weiteren Kontaktmöglichkeit | - | XML Adresse Kontakt | - | Neue ID der Kontaktinformation |
| AdresseKontaktEdit | Änderung einer Kontaktmöglichkeit | `id ` oder`kundennummer ` und optional`projekt` | XML Adresse Kontakt | - | - |
| AdresseKontaktGet | Abfragen einer Kontaktmöglichkeit | `id` | - | XML Adresse Kontakt | - |
| GruppeCreate | Anlegen einer weiteren Gruppe | - | - | - | Neue ID der Gruppe |
| GruppeEdit | Änderung einer bestehenden Gruppe | `id` der Gruppe | - | - | - |
| GruppeGet | Abfragen einer bestehenden Gruppe | `id` der Gruppe | - | - | Datenstruktur der Gruppe |
| BelegeList | Abfragen bestehender Belege | - | - | XML Belege | Datenstruktur von Belegen |
| PreiseEdit | Änderung vieler Preise | - | - | XML Preise | - |
| DateiList | Abfragen vorhandener Dateien | - | - | - | Datenstruktur von Dateien |
| ExportVorlageGet | Abfragen verschiedener Daten | `id ` und optional`von `, ` bis `, ` projekt` | - | XML Daten | Datenstruktur der gewählten Exportvorlage |
| BerichteGet | Abfragen von Berichtsdaten | `id` | - | XML Bericht | Datenstruktur von Berichten |
| ArtikelList | Abfragen von Artikeldaten | - | XML Daten, mit deren Inhalt gefiltert werden soll | XML Artikel | Datenstruktur der Artikel |
| AccountCreate | Anlegen eines Accounts innerhalb einer Adresse | - | XML Daten per POST die für den Account verwendet werden sollen | Account ID | Gibt bei Erfolg die ID des Accounts innerhalb der Adresse zurück |
| AccountEdit | Bearbeiten eines Accounts innerhalb einer Adresse | `id` des Accounts | XML Daten per POST die für den Account verwendet werden sollen | - | - |
| RechnungAlsBezahltMarkieren | Markiert eine Rechnung als bezahlt | `id` der Rechnung | (Optional) XML/JSON Daten, die die ID der Rechnung enthalten | Rechnung ID | Gibt die ID der Rechnung zurück, die geändert wurde |
| AngebotFreigabe | Freigabe eines Angebots | - | XML Daten, die die ID des Anbebotsentwurfs enthalten | XML id und belegnr | Gibt die ID und die erzeugte Belegnummer zurück. |
| AuftragFreigabe | Freigabe eines Auftrags | - | XML Daten, die die ID des Auftragsentwurfs enthalten | XML id und belegnr | Gibt die ID und die erzeugte Belegnummer zurück. |
| RechnungFreigabe | Freigabe einer Rechnung | - | XML Daten, die die ID des Rechnungsentwurfs enthalten | XML id und belegnr | Gibt die ID und die erzeugte Belegnummer zurück. |
| LieferscheinFreigabe | Freigabe eines Lieferscheins | - | XML Daten, die die ID des Lieferscheinentwurfs enthalten | XML id und belegnr | Gibt die ID und die erzeugte Belegnummer zurück. |
| BestellungFreigabe | Freigabe einer Bestellung | - | XML Daten, die die ID des Bestellungsentwurfs enthalten | XML id und belegnr | Gibt die ID und die erzeugte Belegnummer zurück. |
| GutschriftFreigabe | Freigabe einer Gutschrift | - | XML Daten, die die ID des Gutschriftentwurfs enthalten | XML id und belegnr | Gibt die ID und die erzeugte Belegnummer zurück. |
| AngebotVersenden | Versendet ein Angebot | - | XML Daten: ID = id des Angebots, versandart = 'email' oder 'brief', optional: drucker = id des Druckers der verwendet werden soll | XML id | Gibt die ID des versendeten Angebots zurück |
| AuftragVersenden | Versendet eine Auftragsbestätigung | - | XML Daten: ID = id des Auftrags, versandart = 'email' oder 'brief', optional: drucker = id des Druckers der verwendet werden soll | XML id | Gibt die ID des versendeten Auftrags zurück |
| RechnungVersenden | Versendet eine Rechnung | - | XML Daten: ID = id der Rechnung, versandart = 'email' oder 'brief', optional: drucker = id des Druckers der verwendet werden soll | XML id | Gibt die ID der versendeten Rechnung zurück |
| LieferscheinVersenden | Versendet einen Lieferschein | - | XML Daten: ID = id des Lieferscheins, versandart = 'email' oder 'brief', optional: drucker = id des Druckers der verwendet werden soll | XML id | Gibt die ID des versendeten Lieferscheins zurück |
| GutschriftVersenden | Versendet eine Gutschrift | - | XML Daten: ID = id der Gutschrift, versandart = 'email' oder 'brief', optional: drucker = id des Druckers der verwendet werden soll | XML id | Gibt die ID der versendeten Gutschrift zurück |
| AngebotArchivieren | Archiviert ein Angebot | - | XML Daten: ID = id des Angebots | XML id | Gibt die ID des archivierten Angebots zurück |
| AuftragArchivieren | Archiviert einen Auftrag | - | XML Daten: ID = id des Auftrags | XML id | Gibt die ID des archivierten Auftrags zurück |
| RechnungArchivieren | Archiviert eine Rechnung | - | XML Daten: ID = id der Rechnung | XML id | Gibt die ID der archivierten Rechnung zurück |
| LieferscheinArchivieren | Archiviert einen Lieferschein | - | XML Daten: ID = id des Lieferscheins | XML id | Gibt die ID des archivierten Lieferscheins zurück |
| GutschriftArchivieren | Archiviert eine Gutschrift | - | XML Daten: ID = id der Gutschrift | XML id | Gibt die ID der archivierten Gutschrift zurück |
| ServerTimeGet | Holt die aktuelle Serverzeit ab | - | - | - | Serverzeit als Timestamp |
| StechuhrStatusGet | Abfrage Stechuhrstatus eines Mitarbeiters | - | `id ` ID der Stechuhr, `adresse` ID des Mitarbeiters | XML Stechuhrstatus | Aktueller Status und Dauer |
| StechuhrStatusSet | Ändert den Stechuhrstaus eines Mitarbeiters | - | `cmd ` neuer Status (mögliche Werte: 'kommen', 'gehen', 'pausestart', 'pausestop'), `adresse ` ID des Mitarbeiters oder`user` ID des Benutzers | - | - |
| StechuhrSummary | Abfrage einer Zusammenfassung der Zeiterfassung eines Mitarbeiters | - | `adresse ` ID des Mitarbeiters oder`user` ID des Benutzers | XML Stempelzeiten | Zusammenfassung der Stempelzeiten des Mitarbeiters |

### Liste mit Event Handler

Bei Änderungen in xentral wird ein Event (Aufruf einer einstellbaren URL) geworfen. Der Event erhält direkt die Informationen für die Änderungen. Z.B. die Daten eines Auftrags, einer Adresse oder eines Benutzers.

| Request (Parameter action) | Beschreibung | GET Parameter | XML-Daten |
| --- | --- | --- | --- |
| EventAdresseCreate | Eine neue Adresse wurde angelegt | - | - |
| EventAdresseEdit | Es gab eine Änderung an einer bestehenden Adresse | - | - |
| EventAuftragCreate | Ein neuer Auftrag wurde angelegt | - | - |
| EventAuftragEdit | Es gab eine Änderung eines bestehenden Auftrags | - | - |
| EventArtikelCreate | Ein neuer Artikel wurde angelegt | - | - |
| EventArtikelEdit | Es gab eine Änderung an einem bestehenden Artikel | - | - |
| EventBenutzerCreate | Ein neuer Benutzer wurde angelegt | - | - |
| EventBenutzerEdit | Es gab eine Änderung an einem bestehenden Benutzer | - | - |
| EventSessionClose | Wenn Benutzer abmelden geklickt hat (siehe Session Management) | - | - |

| Request (Parameter Action) | Beschreibung | GET Parameter | XML-Daten |
| --- | --- | --- | --- |
| SessionStart | Session eines Benutzers starten | - | - |
| SessionClose | Session eines Benutzers beenden | - | - |

| Request (Parameter Action) | Beschreibung | GET Parameter | XML-Daten |
| --- | --- | --- | --- |
| EventSessionClose | Wenn Benutzer abmelden geklickt hat | - | - |

### Beschreibung der API Funktionen

#### Verwalten von Adressen: AdresseCreate, AdresseEdit, AdresseGet

Im Prinzip kann jede Spalte der Datenbank aus der Tabelle "adresse" bearbeitet oder abgefragt werden. Hierfür ist die Spaltenbezeichnung der Tabelle anzugeben, wie z.B.. Selbiges gilt beim Anlegen einer Adresse.

Um eine neue Adresse anzulegen, kann die Funktion AdresseCreate verwendet werden. Grundlegende Parameter, die beim Anlegen einer Adresse nicht fehlen sollten, um eine sinnvolle Adresse zu erhalten, sind:

- <name> Name der Adresse (Falls Adresse eine Firma ist, hier den Namen des Ansprechpartners eintragen)
- <strasse> Die Straße kann auch in Kombination mit der Hausnummer im Tag verwendet werden
- <hausnummer> Die Hausnummer kann auch in Kombination mit der Straße im Tag <strasse_hausnummer> verwendet werden
- <plz> Postleitzahl der Adresse
- <ort> Ort der Adresse
- <email> E-Mail Adresse der Adresse
- <anrede> Anrede, bei einer Firma ist die Anrede "firma"
- <firma> Firmenname. Wenn befüllt ist, wird automatisch auf "firma" gesetzt
- <vorname> Wenn <firma>, <vorname> und <name> und befüllt sind, wird der Ansprechpartner zusammengesetzt aus <vorname> und <name>. Ist <vorname> leer, wird nur <name> als Ansprechpartner verwendet. Ist <firma> nicht befüllt, wird <name> zusammengesetzt aus <vorname> und <name>
- <projekt> Abkürzung des Projektes. Ist <projekt> leer, wird das Standardprojekt gewählt
- <kundennummer> Kundennummer der Adresse. Falls eine neue Kundennummer vergeben werden soll, muss NEW eingetragen werden.
- <lieferantennummer> Lieferantennummer der Adresse. Falls eine neue Lieferantennummer vergeben werden soll, muss NEW eingetragen werden.

Bei einer abweichenden Lieferadresse können folgende Parameter angegeben werden:

- <liefername> Name der Adresse, zu der geliefert wird. Falls es sich um eine Firma handelt, hier den Namen der Firma
- <liefervorname> Vorname der Adresse, zu der geliefert wird
- <lieferstrasse> Straße, zu der geliefert wird
- <lieferhausnummer> Hausnummer, zu der geliefert wird
- <lieferplz> Postleitzahl der Adresse, zu der geliefert wird
- <lieferort> Ort der Adresse, zu der geliefert wird
- <lieferfirma> Firmenname der zu beliefernden Adresse. Ist dieses Feld befüllt, wird der Adresszusatz zusammengesetzt aus <liefervorname> und <liefername>
- <lieferabteilung> Abteilung der Adresse, zu der geliefert wird
- <lieferland> Land der Adresse, zu der geliefert wird

Des Weiteren kann man beim Anlegen und Bearbeiten einer Adresse, dieser eine Gruppe zuweisen. Hierfür kann das Tag <verband> mit der id der Gruppe verwendet werden (z.B. <verband>34</verband>).

Soll eine Adresse bearbeitet (AdresseEdit) oder nur Daten der Adresse abgefragt werden (AdresseGet), muss die ID oder die Kundennummer angegeben werden. Optional kann das Projekt über die URL übergeben werden.

##### Beispiel Anfrage AdresseCreate mit Funktionen

```
  <?php
$hash = generateHash();
 
$xml = "<name>Emilia Gruber</name>
  <strasse>Musterstrasse</strasse>
  <hausnummer>21</hausnummer>
  <plz>11111</plz>
  <ort>Musterort</ort>
  <email>emiliagruber@musterort.de</email>
  <kundennummer>NEW</kundennummer>";
 
$output_xml = SendRequest("AdresseCreate",$xml,$hash); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```##### Beispiel Antwort AdresseCreate```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AdresseCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>13</id>
  <kundennummer>23243</kundennummer>
  </xml>
</response>

  
```##### Beispiel Anfrage AdresseEdit mit Funktionen```
  <?php
$hash = generateHash();
 
$xml = "<name>Emilia Gruber</name>
  <strasse>Musterweg</strasse>
  <hausnummer>67</hausnummer>
  <plz>22222</plz>
  <ort>Musterhausen</ort>
  <email>emiliagruber@musterhausen.de</email>";

$id = "13";
 
$output_xml = SendRequest("AdresseEdit",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```##### Beispiel Antwort AdresseEdit```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AdresseEdit</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status> 
</response>

  
```##### Beispiel Anfrage AdresseGet mit Funktionen```
  <?php
$hash = generateHash();

$xml = "";

$id = "12";

$output_xml = SendRequest("AdresseGet",$xml,$hash,$id); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash,$id)
{

  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```##### Beispielrückgabe einer Adressabfrage```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AdresseGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>37</id>
  <typ>herr,frau,firma</typ>
  <marketingsperre />
  <trackingsperre>1=keine Mail senden, 0=Mail senden</trackingsperre>
  <rechnungsadresse>0=keine gesonderte, 1 = gesonderte Rechnungsadresse</rechnungsadresse>
  <sprache>deutsch,englisch</sprache>
  <name>Max Muster 2</name>
  <abteilung />
  <unterabteilung />
  <ansprechpartner />
  <land />
  <strasse>Muster strasse 888</strasse>
  <ort />
  <plz />
  <telefon />
  <telefax />
  <mobil />
  <email />
  <ustid />
  <ust_befreit>0</ust_befreit>
  <passwort_gesendet>0</passwort_gesendet>
  <sonstiges />
  <adresszusatz />
  <kundenfreigabe>0</kundenfreigabe>
  <steuer />
  <logdatei>2014-06-01 16:01:08</logdatei>
  <kundennummer />
  <lieferantennummer>70002</lieferantennummer>
  <mitarbeiternummer />
  <konto />
  <blz />
  <bank />
  <inhaber />
  <swift />
  <iban />
  <waehrung />
  <paypal />
  <paypalinhaber />
  <paypalwaehrung />
  <projekt>1</projekt>
  <partner>0</partner>
  <zahlungsweise />
  <zahlungszieltage />
  <zahlungszieltageskonto />
  <zahlungszielskonto />
  <versandart />
  <kundennummerlieferant />
  <zahlungsweiselieferant />
  <zahlungszieltagelieferant />
  <zahlungszieltageskontolieferant />
  <zahlungszielskontolieferant />
  <versandartlieferant />
  <geloescht>0</geloescht>
  <firma>1</firma>
  <webid />
  <internetseite />
  <vorname />
  <kalender_aufgaben />
  <titel />
  <anschreiben />
  <logfile />
  <mlmaktiv />
  <mlmvertragsbeginn />
  <geburtstag />
  <liefersperre />
  <mlmpositionierung />
  <steuernummer />
  <steuerbefreit />
  <mlmmitmwst />
  <mlmabrechnung />
  <sponsor />
  <geworbenvon />
  <liefersperregrund />
  <verrechnungskontoreisekosten>0</verrechnungskontoreisekosten>
  <rolledatum />
  <mlmwaehrungauszahlung />
  <mlmfestsetzen>0</mlmfestsetzen>
  <mlmmindestpunkte>0</mlmmindestpunkte>
  <mlmwartekonto>0.00</mlmwartekonto>
  <abweichende_rechnungsadresse>0</abweichende_rechnungsadresse>
  <rechnung_vorname />
  <rechnung_name />
  <rechnung_titel />
  <rechnung_typ />
  <rechnung_strasse />
  <rechnung_ort />
  <rechnung_land />
  <rechnung_abteilung />
  <rechnung_unterabteilung />
  <rechnung_adresszusatz />
  <rechnung_telefon />
  <rechnung_telefax />
  <rechnung_anschreiben />
  <rechnung_email />
  <rechnung_plz />
  <rechnung_ansprechpartner />
  <kennung />
  <zahlungskonditionen_festschreiben />
  <rabatte_festschreiben />
  <rabattinformation />
  <portofreiab />
  <portofrei_aktiv />
  <provision />
  <porto_preis />
  <porto_artikelid />
  <freifeld1 />
  <freifeld2 />
  <freifeld3 />
  <rechnung_periode />
  <rechnung_anzahlpapier />
  <rechnung_permail />
  <rechnung_email />
  
  </xml>
</response>

  
```

### Verwalten von Aufträgen: AuftragCreate, AuftragEdit, AuftragGet

Hier können Aufträge komplett verwaltet werden, d.h. neue anlegen (AuftragCreate), bestehende bearbeiten (AuftragEdit) oder bestehende abholen (AuftragGet) um diese in einem anderen System übertragen.

Bei AuftragCreate können folgende Parameter angegeben werden:

- <kundennummer> Hier kann NEW für einen neuen Kunden oder die bisherige Kundennummer eines Kunden verwendet werden.

Daten wie Zahlungsart, Versandart müssen nicht übergeben werden. Diese werden grundsätzlich aus den Kundenstammdaten geholt, außer diese werden an die API übergeben.

Bei AuftragEdit und AuftragGet muss die id oder orderid (Belegnr) und optional das Projekt als URL übergeben werden. Möchtest du mit AuftragEdit einen Auftrag ändern, in dem schon Positionen enthalten sind, musst du weiterhin alle Positionen des Auftrags komplett mit angeben.

#### Beispiel Anfrage AuftragCreate mit Funktionen

```
  <?php
$hash = generateHash();

$xml = "<kundennummer>23243</kundennummer>
<artikelliste>
  <position>
  <nummer>700001</nummer>
  <preis>9.99</preis>
  <menge>2</menge>
  <waehrung>EUR</waehrung>
  </position>
  <position>
  <nummer>700002</nummer>
  <preis>3.99</preis>
  <menge>1</menge>
  <waehrung>EUR</waehrung>
  </position>
</artikelliste>";

$output_xml = SendRequest("AuftragCreate",$xml,$hash); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort AuftragCreate```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AuftragCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>16</id>
  <customernumber>200003</customernumber>
  </xml>
</response>

  
```#### Beispiel Anfrage AuftragGet mit Funktionen```
  <?php

$hash = generateHash();

$xml = "";

$id = "14";

$output_xml = SendRequest("AuftragGet",$xml,$hash,$id); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash,$id)
{

  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;

$xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel Antwort AuftragGet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AuftragGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>14</id>
  <datum>2017-03-16</datum>
  <art/>
  <projekt>0</projekt>
  <belegnr>200002</belegnr>
  <internet/>
  <bearbeiter>Mitarbeiter</bearbeiter>
  <angebot/>
  <freitext/>
  <internebemerkung/>
  <status>freigegeben</status>
  <adresse>11</adresse>
  <name>Mustersupermarkt</name>
  <abteilung/>
  <unterabteilung/>
  <strasse>Supermarktstraße 1</strasse>
  <adresszusatz/>
  <ansprechpartner>Herr Supermarktleiter</ansprechpartner>
  <plz>12345</plz>
  <ort>Supermarktstadt</ort>
  <land>DE</land>
  <ustid/>
  <ust_befreit>0</ust_befreit>
  <ust_inner>0</ust_inner>
  <email/>
  <telefon/>
  <telefax/>
  <betreff/>
  <kundennummer>23241</kundennummer>
  <versandart>versandunternehmen</versandart>
  <vertrieb>Testfirma GmbH</vertrieb>
  <zahlungsweise>rechnung</zahlungsweise>
  <zahlungszieltage>14</zahlungszieltage>
  <zahlungszieltageskonto>10</zahlungszieltageskonto>
  <zahlungszielskonto>2.00</zahlungszielskonto>
  <bank_inhaber/>
  <bank_institut/>
  <bank_blz/>
  <bank_konto/>
  <kreditkarte_typ/>
  <kreditkarte_inhaber/>
  <kreditkarte_nummer/>
  <kreditkarte_pruefnummer/>
  <kreditkarte_monat/>
  <kreditkarte_jahr/>
  <firma>1</firma>
  <versendet>0</versendet>
  <versendet_am>0000-00-00 00:00:00</versendet_am>
  <versendet_per/>
  <versendet_durch/>
  <autoversand>1</autoversand>
  <keinporto>0</keinporto>
  <keinestornomail>0</keinestornomail>
  <abweichendelieferadresse>0</abweichendelieferadresse>
  <liefername/>
  <lieferabteilung/>
  <lieferunterabteilung/>
  <lieferland/>
  <lieferstrasse/>
  <lieferort/>
  <lieferplz/>
  <lieferadresszusatz/>
  <lieferansprechpartner/>
  <packstation_inhaber/>
  <packstation_station/>
  <packstation_ident/>
  <packstation_plz/>
  <packstation_ort/>
  <autofreigabe>0</autofreigabe>
  <freigabe>0</freigabe>
  <nachbesserung>0</nachbesserung>
  <gesamtsumme>171.36</gesamtsumme>
  <inbearbeitung>0</inbearbeitung>
  <abgeschlossen>0</abgeschlossen>
  <nachlieferung>0</nachlieferung>
  <lager_ok>1</lager_ok>
  <porto_ok>1</porto_ok>
  <ust_ok>1</ust_ok>
  <check_ok>1</check_ok>
  <vorkasse_ok>1</vorkasse_ok>
  <nachnahme_ok>1</nachnahme_ok>
  <reserviert_ok>0</reserviert_ok>
  <partnerid>0</partnerid>
  <folgebestaetigung>0000-00-00</folgebestaetigung>
  <zahlungsmail>0000-00-00</zahlungsmail>
  <stornogrund/>
  <stornosonstiges/>
  <stornorueckzahlung/>
  <stornobetrag>0.00</stornobetrag>
  <stornobankinhaber/>
  <stornobankkonto/>
  <stornobankblz/>
  <stornobankbank/>
  <stornogutschrift>0</stornogutschrift>
  <stornogutschriftbeleg/>
  <stornowareerhalten>0</stornowareerhalten>
  <stornomanuellebearbeitung/>
  <stornokommentar/>
  <stornobezahlt/>
  <stornobezahltam>0000-00-00</stornobezahltam>
  <stornobezahltvon/>
  <stornoabgeschlossen/>0</stornoabgeschlossen>
  <stornorueckzahlungper/>
  <stornowareerhaltenretour>0</stornowareerhaltenretour>
  <partnerausgezahlt>0</partnerausgezahlt>
  <partnerausgezahltam>0000-00-00</partnerausgezahltam>
  <kennen/>
  <logdatei>2017-03-17 10:30:05</logdatei>
  <keinetrackingmail/>
  <zahlungsmailcounter/>
  <rma>0</rma>
  <transaktionsnummer/>
  <vorabbezahltmarkieren>0</vorabbezahltmarkieren>
  <deckungsbeitragcalc>1</deckungsbeitragcalc>
  <deckungsbeitrag>100.00</deckungsbeitrag>
  <erloes_netto>144.00</erloes_netto>
  <umsatz_netto>144.00</umsatz_netto>
  <lieferdatum/>
  <tatsaechlicheslieferdatum/>
  <liefertermin_ok>1</liefertermin_ok>
  <teillieferung_moeglich>0</teillieferung_moeglich>
  <kreditlimit_ok>1</kreditlimit_ok>
  <kreditlimit_freigabe>0</kreditlimit_freigabe>
  <liefersperre_ok>1</liefersperre_ok>
  <teillieferungvon>0</teillieferungvon>
  <teillieferungnummer>0</teillieferungnummer>
  <vertriebid>0</vertriebid>
  <aktion/>
  <provision>0.00</provision>
  <provision_summe/>
  <anfrageid>0</anfrageid>
  <gruppe>0</gruppe>
  <shopextid/>
  <shopextstatus/>
  <ihrebestellnummer/>
  <anschreiben/>
  <usereditid>1</usereditid>
  <useredittimestamp>2017-03-17 10:30:05</useredittimestamp>
  <realrabatt>0.00</realrabatt>
  <rabatt>0.00</rabatt>
  <einzugsdatum/>
  <rabatt1>0.00</rabatt1>
  <rabatt2>0.00</rabatt2>
  <rabatt3>0.00</rabatt3>
  <rabatt4>0.00</rabatt4>
  <rabatt5>0.00</rabatt5>
  <shop>0</shop>
  <steuersatz_normal>19.00</steuersatz_normal>
  <steuersatz_zwischen>7.00</steuersatz_zwischen>
  <steuersatz_ermaessigt>7.00</steuersatz_ermaessigt>
  <steuersatz_starkermaessigt>7.00</steuersatz_starkermaessigt>
  <steuersatz_dienstleistung>7.00</steuersatz_dienstleistung>
  <waehrung>EUR</waehrung>
  <keinsteuersatz/>
  <angebotid/>
  <schreibschutz>0</schreibschutz>
  <pdfarchiviert>0</pdfarchiviert>
  <pdfarchiviertversion>0</pdfarchiviertversion>
  <typ>firma</typ>
  <ohne_briefpapier>0</ohne_briefpapier>
  <auftragseingangper/>
  <lieferid>0</lieferid>
  <ansprechpartnerid>0</ansprechpartnerid>
  <systemfreitext/>
  <projektfiliale>0</projektfiliale>
  <lieferungtrotzsperre>0</lieferungtrotzsperre>
  <zuarchivieren>0</zuarchivieren>
  <internebezeichnung/>
  <angelegtam/>
  <saldo>-171.36</saldo>
  <saldogeprueft>2017-03-17 10:29:59</saldogeprueft>
  <lieferantenauftrag>0</lieferantenauftrag>
  <lieferant>0</lieferant>
  <lieferdatumkw>0</lieferdatumkw>
  <abweichendebezeichnung>0</abweichendebezeichnung>
  <rabatteportofestschreiben>0</rabatteportofestschreiben>
  <sprache>deutsch</sprache>
  <bodyzusatz/>
  <bundesland/>
  <artikelliste>
  <position>
  <id>51</id>
  <auftrag>14</auftrag>
  <artikel>385815</artikel>
  <projekt>0</projekt>
  <bezeichnung>Kirschjoghurt klein</bezeichnung>
  <beschreibung>Ein leckerer kleiner Kirschjogurt.</beschreibung>
  <internerkommentar/>
  <nummer>115491</nummer>
  <menge>50</menge>
  <preis>0.30000000</preis>
  <waehrung>EUR</waehrung>
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe>1</vpe>
  <sort>1</sort>
  <status>angelegt</status>
  <umsatzsteuer/>
  <bemerkung/>
  <geliefert>0</geliefert>
  <geliefert_menge>0</geliefert_menge>
  <explodiert>0</explodiert>
  <explodiert_parent>0</explodiert_parent>
  <logdatei>2017-03-17 10:29:59</logdatei>
  <punkte>0.00</punkte>
  <bonuspunkte>0.00</bonuspunkte>
  <mlmdirektpraemie>0.00</mlmdirektpraemie>
  <keinrabatterlaubt>0</keinrabatterlaubt>
  <grundrabatt>0.00</grundrabatt>
  <rabattsync>1</rabattsync>
  <rabatt1>0.00</rabatt1>
  <rabatt2>0.00</rabatt2>
  <rabatt3>0.00</rabatt3>
  <rabatt4>0.00</rabatt4>
  <rabatt5>0.00</rabatt5>
  <einheit/>
  <webid/>
  <rabatt>0.00</rabatt>
  <nachbestelltexternereinkauf/>
  <zolltarifnummer/>
  <herkunftsland>DE</herkunftsland>
  <artikelnummerkunde/>
  <freifeld1/>
  <freifeld2/>
  <freifeld3/>
  <freifeld4/>
  <freifeld5/>
  <freifeld6/>
  <freifeld7/>
  <freifeld8/>
  <freifeld9/>
  <freifeld10/>
  <lieferdatumkw>0</lieferdatumkw>
  <teilprojekt>0</teilprojekt>
  </position>
  </artikelliste>
  </xml>
</response>

  
```

### Verwalten von Artikeln: ArtikelCreate, ArtikelEdit, ArtikelGet

Es können mit der API neue Artikel angelegt (ArtikelCreate), Artikel bearbeitet (ArtikelEdit) und Artikelinformationen abgerufen (ArtikelGet) werden. Bei ArtikelGet und ArtikelEdit ist zu beachten, dass die ID des Artikels in der URL über GET mittels &id= mitgegeben werden muss. Beim Anlegen und Bearbeiten der Artikel können alle Tags verwendet werden, die als Spalte in der Tabelle "artikel" vorliegen. Um jedoch sinnvolle Artikel zu erhalten, sollten beim Erstellen einige Tags mindestens gesetzt werden:

- <name_de> Name des Artikels
- <anabregs_text> Beschreibungstext des Artikels
- <projekt> Abkürzung des Projektes. Falls nicht gesetzt, wird das Standardprojekt gewählt
- <nummer> Artikelnummer des Artikels. Soll eine neue Artikelnummer vergeben werden, muss NEW eingetragen werden
- <aktiv> 1 oder 0, für einen aktiven bzw. inaktiven Artikel
- <variante_von_nummer> Nummer des Artikels, von dem der neue Artikel eine Variante ist

#### Beispiel Anfrage ArtikelCreate mit Funktionen

```
  <?php

$hash = generateHash();

$xml = "<name_de>Kirschjoghurt</name_de>
  <anabregs_text>Ein leckerer Kirschjoghurt</anabregs_text>
  <nummer>NEW</nummer>
  <aktiv>1</aktiv>";

$output_xml = SendRequest("ArtikelCreate",$xml,$hash); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash)
{

  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel Antwort ArtikelCreate```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>ArtikelCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>149</id>
  <nummer>115491</nummer>
  </xml>
  </response>

  
```#### Beispiel Anfrage ArtikelEdit mit Funktionen```
  <?php

$hash = generateHash();

$xml = "<nummer>115491</nummer>
  <name_de>Kirschjoghurt klein</name_de>
  <anabregs_text>Ein leckerer kleiner Kirschjogurt.</anabregs_text>
  ";

$id = "149";

$output_xml = SendRequest("ArtikelEdit",$xml,$hash,$id); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash,$id)
{

  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;

$xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel Antwort ArtikelEdit```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>ArtikelEdit</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
</response>
  
```#### Beispiel Lagerbestandsveränderung mit ArtikelEdit```
  <xml>
  <nummer>1000001</nummer>
  <lager_platz>HL001B</lager_platz>
  <lager_menge>5020</lager_menge>
</xml>
  
```#### Beispiel Anfrage ArtikelGet mit Funktionen```
  <?php

$hash = generateHash();

$xml = "";
$id = 149;

$output_xml = SendRequest("ArtikelGet",$xml,$hash,$id); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash,$id)
{

  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);

?>

  
```#### Beispiel Antwort ArtikelGet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>ArtikelGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>385815</id>
  <typ/>
  <nummer>115491</nummer>
  <checksum/>
  <projekt>0</projekt>
  <inaktiv>0</inaktiv>
  <ausverkauft>0</ausverkauft>
  <warengruppe/>
  <name_de>Kirschjoghurt klein</name_de>
  <name_en/>
  <kurztext_de/>
  <kurztext_en/>
  <beschreibung_de/>
  <beschreibung_en/>
  <uebersicht_de/>
  <uebersicht_en/>
  <links_de/>
  <links_en/>
  <startseite_de/>
  <startseite_en/>
  <standardbild/>
  <herstellerlink/>
  <hersteller/>
  <teilbar/>
  <nteile/>
  <seriennummern/>
  <lager_platz/>
  <lieferzeit/>
  <lieferzeitmanuell/>
  <sonstiges/>
  <gewicht/>
  <endmontage/>
  <funktionstest/>
  <artikelcheckliste/>
  <stueckliste/>
  <juststueckliste/>
  <barcode/>
  <hinzugefuegt/>
  <pcbdecal/>
  <lagerartikel>0</lagerartikel>
  <porto>0</porto>
  <chargenverwaltung>0</chargenverwaltung>
  <provisionsartikel>0</provisionsartikel>
  <gesperrt>0</gesperrt>
  <sperrgrund/>
  <geloescht>0</geloescht>
  <gueltigbis>0000-00-00</gueltigbis>
  <umsatzsteuer/>
  <klasse/>
  <adresse>0</artikel>
  <shopartikel>0</shopartikel>
  <unishopartikel>0</unishopartikel>
  <journalshopartikel>0</journalshopartikel>
  <shop>0</shop>
  <katalog>0</katalog>
  <katalogtext_de/>
  <katalogtext_en/>
  <katalogbezeichnung_de/>
  <katalogbezeichnung_en/>
  <neu>0</neu>
  <topseller>0</topseller>
  <startseite>0</startseite>
  <wichtig>0</wichtig>
  <mindestlager>0</mindestlager>
  <mindestbestellung>0</mindestbestellung>
  <partnerprogramm_sperre>0</partnerprogramm_sperre>
  <internerkommentar/>
  <intern_gesperrt>0</intern_gesperrt>
  <intern_gesperrtuser>0</intern_gesperrtuser>
  <intern_gesperrtgrund/>
  <inbearbeitung>0</inbearbeitung>
  <inbearbeitunguser>0</inbearbeitunguser>
  <cache_lagerplatzinhaltmenge>-999</cache_lagerplatzinhaltmenge>
  <internkommentar/>
  <firma>1</firma>
  <logdatei>2017-03-24 06:53:10</logdatei>
  <anabregs_text>Ein leckerer kleiner Kirschjogurt.</anabregs_text>
  <autobestellung>0</autobestellung>
  <produktion/>
  <herstellernummer/>
  <restmenge/>
  <mlmdirektpraemie/>
  <keineeinzelartikelanzeigen>0</keineeinzelartikelanzeigen>
  <mindesthaltbarkeitsdatum>0</mindesthaltbarkeitsdatum>
  <letzteseriennummer/>
  <individualartikel>0</individualartikel>
  <keinrabatterlaubt/>
  <rabatt>0</rabatt>
  <rabatt_prozent/>
  <geraet>0</geraet>
  <serviceartikel>0</serviceartikel>
  <autoabgleicherlaubt>0</autoabgleicherlaubt>
  <pseudopreis/>
  <freigabenotwendig>0</freigabenotwendig>
  <freigaberegel/>
  <nachbestellt/>
  <ean/>
  <mlmpunkte>0.00</mlmpunkte>
  <mlmbonuspunkte>0.00</mlmbonuspunkte>
  <mlmkeinepunkteeigenkauf/>
  <shop2/>
  <shop3/>
  <usereditid>1</usereditid>
  <useredittimestamp>2017-03-24 06:53:10</useredittimestamp>
  <freifeld1/>
  <freifeld2/>
  <freifeld3/>
  <freifeld4/>
  <freifeld5/>
  <freifeld6/>
  <einheit/>
  <webid/>
  <lieferzeitmanuell_en/>
  <variante/>
  <variante_von/>
  <produktioninfo/>
  <sonderaktion/>
  <sonderaktion_en/>
  <autolagerlampe>0</autolagerlampe>
  <leerfeld/>
  <zolltarifnummer/>
  <herkunftsland>DE</herkunftsland>
  <laenge>0.00</laenge>
  <breite>0.00</breite>
  <hoehe>0.00</hoehe>
  <gebuehr>0</gebuehr>
  <pseudolager/>
  <matrixprodukt>0</matrixprodukt>
  <anabregs_text_en>
  <externeproduktion>0</externeproduktion>
  <bildvorschau/>
  <inventursperre>0</inventursperre>
  <variante_kopie>0</variante_kopie>
  <unikat>0</unikat>
  <downloadartikel>0</downloadartikel>
  <generierenummerbeioption>0</generierenummerbeioption>
  <allelieferanten>0</allelieferanten>
  <tagespreise>0</tagespreise>
  <rohstoffe>0</rohstoffe>
  <steuer_erloese_inland_normal/>
  <steuer_aufwendung_inland_normal/>
  <steuer_erloese_inland_ermaessigt/>
  <steuer_aufwendung_inland_ermaessigt/>
  <steuer_erloese_inland_steuerfrei/>
  <steuer_aufwendung_inland_steuerfrei/>
  <steuer_erloese_inland_innergemeinschaftlich/>
  <steuer_aufwendung_inland_innergemeinschaftlich/>
  <steuer_erloese_inland_eunormal/>
  <steuer_erloese_inland_nichtsteuerbar/>
  <steuer_erloese_inland_euermaessigt/>
  <steuer_aufwendung_inland_nichtsteuerbar/>
  <steuer_aufwendung_inland_eunormal/>
  <steuer_aufwendung_inland_euermaessigt/>
  <steuer_erloese_inland_export/>
  <steuer_aufwendung_inland_import/>
  <steuer_art_produkt>1</steuer_art_produkt>
  <steuer_art_produkt_download>1</steuer_art_produkt_download>
  <metadescription_de/>
  <metadescription_en/>
  <metakeywords_de/>
  <metakeywords_en/>
  <vkmeldungunterdruecken>0</vkmeldungunterdruecken>
  <freifeld7/>
  <freifeld8/>
  <freifeld9/>
  <freifeld10/>
  <ursprungsregion/>
  <altersfreigabe/>
  <provisionssperre/>
  <inventurekaktiv>0</inventureaktiv>
  <inventurek/>
  <verkaufspreise>
  <staffelpreis>
  <ab_menge>1</ab_menge>
  <preis>0.30000000</preis>
  <vpe/>
  <waehrung>EUR</waehrung>
  </staffelpreis>
  </verkaufspreise>
  </xml>
</response>

  
```

### Verwalten von Benutzer: BenutzerCreate, BenutzerEdit, BenutzerGet

Mit BenutzerCreate kann ein neuer Benutzer angelegt werden. Soll ein Benutzer bearbeitet werden, geschieht dies mit BenutzerEdit. BenutzerGet liefert Informationen eines Benutzers zurück. Bei BenutzerEdit und BenutzerGet muss die ID des Benutzers als GET Parameter übergeben werden.

Beim Anlegen bzw. Bearbeiten eines Benutzers sind einige Dinge zu beachten:

- <active> Muss auf 1 gesetzt sein, da sich sonst der Benutzer nicht anmelden kann
- <startseite> Die URL der Startseite (z.B. index.php?module=welcome&action=pinwand) muss base54 kodiert sein
- <passwordmd5> Das Passwort des Benutzers muss hier md5 kodiert angegeben werden, nicht <password>. <password> stammt aus älteren Versionen, wird nicht mehr verwendet und dient nur noch historischen Zwecken

Tags, um einen Benutzer anzulegen oder zu bearbeiten:

- <adresse> Beinhaltet die ID der Adresse
- <username> Darf nicht bereits existieren
- <type> Art des Benutzers, z.B. admin oder standard
- <aktiv> Auf 1 setzen
- <startseite> Muss base54 kodiert sein
- <passwordmd5> Muss md5 kodiert sein

#### Beispiel Anfrage BenutzerCreate mit Funktionen

```
  <?php
$hash = generateHash();

$xml = "<adresse>12</adresse>
  <username>Musterbenutzer</username>
  <type>admin</type>
  <activ>1</activ>
  <passwordmd5>e22a63fb76874c99488435f26b117e37</passwordmd5>
  <externlogin>1</externlogin>";

$output_xml = SendRequest("BenutzerCreate",$xml,$hash); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>
Beispiel Antwort BenutzerCreate
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>BenutzerCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>10</id>
  </xml>
</response>

  
```#### Beispiel Antwort BenutzerCreate```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>BenutzerCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>10</id>
  </xml>
</response>
  
```Beispiel Anfrage BenutzerEdit mit Funktionen```
  <?php
$hash = generateHash();

$xml = "<type>standard</type>
  <activ>1</activ>
  <passwordmd5>dafe3d37f46376f08f8e92b15e308239</passwordmd5>
  <externlogin>0</externlogin>";

$id = 10;

$output_xml = SendRequest("BenutzerEdit",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort BenutzerEdit```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>BenutzerEdit</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status> 
</response>

  
```#### Beispiel Anfrage BenutzerGet mit Funktionen```
  <?php

$hash = generateHash();

$xml = "";

$id = "1";

$output_xml = SendRequest("BenutzerGet",$xml,$hash,$id); 

function generateHash()
{
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash,$id)
{

  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel Antwort BenutzerGet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>BenutzerGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>1</id>
  <username>admin</username>
  <password>MAiwwHrOSf9kg</password>
  <repassword>0</repassword>
  <description />
  <settings>a:2:{s:18:"lohnabrechnung_von";s:0:"";s:18:"lohnabrechnung_bis";s:0:"";}</settings>
  <parentuser />
  <activ>1</activ>
  <type>admin</type>
  <adresse>1</adresse>
  <fehllogins>0</fehllogins>
  <standarddrucker>0</standarddrucker>
  <firma>1</firma>
  <logdatei>2014-05-26 11:12:28</logdatei>
  <startseite>aW5kZXgucGhwP21vZHVsZT13ZWxjb21lJmFjdGlvbj1waW53YW5k</startseite>
  <hwtoken>0</hwtoken>
  <hwkey />
  <hwcounter>0</hwcounter>
  <motppin />
  <motpsecret />
  <externlogin>1</externlogin>
  <hwdatablock />
  <passwordmd5 />
  <internebezeichnung />
  <gpsstechuhr>0</gpsstechuhr>
  <kalender_passwort />
  <kalender_aktiv />
  </xml>
</response>

  
```#### Beispiel Anfrage BenutzerGetRFID```
  <?php

$xml = '<rfid>1234</rfid>';

$output_xml = SendRequest('BenutzerGetRFID', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```#### Beispiel Antwort BenutzerGetRFID```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>BenutzerGetRFID</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>3</id>
  <username>demomitarbeiter</username>
  <password>pllIX0pw7JU9c</password>
  <repassword>0</repassword>
  <description></description>
  <settings>a:6: 
{s:16:&quot;pos_list_projekt&quot;;s:1:&quot;0&quot;;s:18:&quot;pos_list_kassierer&quot;;s:1:&quot;0&quot;;s:22:&quot;pos_list_kassierername&quot;;s:1:&quot;0&quot;;s:18:&quot;pos_list_lkadresse&quot;;s:1:&quot;0&quot;;s:18:&quot;lohnabrechnung_von&quot;;s:0:&quot;&quot;;s:18:&quot;lohnabrechnung_bis&quot;;s:0:&quot;&quot;;}
  </settings>
  <parentuser>0</parentuser>
  <activ>1</activ>
  <type>standard</type>
  <adresse>6</adresse>
  <fehllogins>0</fehllogins>
  <standarddrucker>0</standarddrucker>
  <firma>1</firma>
  <logdatei>2019-11-22 16:54:00</logdatei>
  <startseite></startseite>
  <hwtoken>0</hwtoken>
  <hwkey></hwkey>
  <hwcounter>0</hwcounter>
  <motppin></motppin>
  <motpsecret></motpsecret>
  <passwordmd5>2ad71933e4b074c4671425c8e6b48021</passwordmd5>
  <externlogin>0</externlogin>
  <projekt_bevorzugen>0</projekt_bevorzugen>
  <email_bevorzugen>1</email_bevorzugen>
  <projekt>0</projekt>
  <rfidtag>1234</rfidtag>
  <vorlage></vorlage>
  <kalender_passwort></kalender_passwort>
  <kalender_ausblenden>0</kalender_ausblenden>
  <kalender_aktiv>0</kalender_aktiv>
  <gpsstechuhr>0</gpsstechuhr>
  <standardetikett>0</standardetikett>
  <standardfax>0</standardfax>
  <internebezeichnung></internebezeichnung>
  <hwdatablock></hwdatablock>
  <standardversanddrucker>0</standardversanddrucker>
  <passwordsha512></passwordsha512>
  <salt></salt>
  <paketmarkendrucker>0</paketmarkendrucker>
  <sprachebevorzugen>deutsch</sprachebevorzugen>
  <vergessencode></vergessencode>
  <vergessenzeit></vergessenzeit>
  <chat_popup>1</chat_popup>
  <defaultcolor>false</defaultcolor>
  <passwordhash></passwordhash>
  <docscan_aktiv>0</docscan_aktiv>
  <docscan_passwort></docscan_passwort>
  <callcenter_notification>1</callcenter_notification>
  <stechuhrdevice></stechuhrdevice>
  </xml>
</response>

  
```

### Verwalten von Gruppen: GruppeCreate, GruppeEdit, GruppeGet

Mit dem Befehl GruppeCreate kann eine neue Gruppe angelegt werden. Zum Bearbeiten einer Gruppe wird GruppeEdit verwendet. Sollen jedoch nur die Daten einer Gruppe abgefragt werden, geschieht dies mit GruppeGet. Bei GruppeEdit und GruppeCreate muss die ID der Gruppe als GET Parameter übergeben werden.

Tags, um eine Gruppe anzulegen oder zu bearbeiten: Es können als Tag die Spaltenbezeichnungen der Tabelle gruppen aus der Datenbank gewählt werden, z.B.:

- <name> Beinhaltet den Namen der Gruppe
- <art> Hier sollte gruppe eingetragen werden
- <kennziffer> Beliebige Kennziffer zum Erkennen der Gruppe

#### Beispiel Anfrage GruppeCreate mit Funktionen

```
  <?php
$hash = generateHash();

$xml = "<name>Messe 2017</name>
  <art>Gruppe</art>
  <kennziffer>2017</kennziffer>";

$output_xml = SendRequest("GruppeCreate",$xml,$hash); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort GruppeCreate```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>GruppeCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>8</id>
  </xml>
</response>

  
```#### Beispiel Anfrage GruppeEdit mit Funktionen```
  <?php
$hash = generateHash();

$xml = "<name>Messe 2016</name>
  <kennziffer>2016</kennziffer>";

$id = 8;

$output_xml = SendRequest("GruppeEdit",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort GruppeEdit```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>GruppeEdit</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
</response>

  
```#### Beispiel Anfrage GruppeGet mit Funktionen```
  <?php
$hash = generateHash();

$xml = "";
$id = 2;

$output_xml = SendRequest("GruppeGet",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort GruppeGet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>GruppeGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>2</id>
  <name>Händler</name>
  <art>gruppe</art>
  <kennziffer>1</kennziffer>
  <internebemerkung/>
  <grundrabatt>0.00</grundrabatt>
  <rabatt1>0.00</rabatt1>
  <rabatt2>0.00</rabatt2>
  <rabatt3>0.00</rabatt3>
  <rabatt4>0.00</rabatt4>
  <rabatt5>0.00</rabatt5>
  <sonderrabatt_skonto>0.00</sonderrabatt_skonto>
  <provision>0.00</provision>
  <kundennummer/>
  <partnerid/>
  <dta_aktiv>0</dta_aktiv>
  <dta_periode>1</dta_periode>
  <dta_dateiname/>
  <dta_mail/>
  <dta_mail_betreff/>
  <dta_mail_text/>
  <dtavariablen/>
  <dta_variante>1</dta_variante>
  <bonus1>0.00</bonus1>
  <bonus1_ab>0.00</bonus1_ab>
  <bonus2>0.00</bonus2>
  <bonus2_ab>0.00</bonus2_ab>
  <bonus3>0.00</bonus3>
  <bonus3_ab>0.00</bonus3_ab>
  <bonus4>0.00</bonus4>
  <bonus4_ab>0.00</bonus4_ab>
  <bonus5>0.00</bonus5>
  <bonus5_a>0.00</bonus5_ab>
  <bonus6>0.00</bonus6>
  <bonus6_ab>0.00</bonus6_ab>
  <bonus7>0.00</bonus7>
  <bonus7_ab>0.00</bonus7_ab>
  <bonus8>0.00</bonus8>
  <bonus8_ab>0.00</bonus8_ab>
  <bonus9>0.00</bonus9>
  <bonus9_ab>0.00</bonus9_ab>
  <bonus10>0.00</bonus10>
  <bonus10_ab>0.00</bonus10_ab>
  <zahlungszieltage>0</zahlungszieltage>
  <zahlungszielskonto>0.00</zahlungszielskonto>
  <zahlungszieltageskonto>0</zahlungszieltageskonto>
  <portoartikel>0</portoartikel>
  <portofreiab>0.00</portofreiab>
  <erweiterteoptionen>0</erweiterteoptionen>
  <zentralerechnung>0</zentralerechnung>
  <zentralregulierung>0</zentralregulierung>
  <gruppe>0</gruppe>
  <preisgruppe>0</preisgruppe>
  <verbandsgruppe>0</verbandsgruppe>
  <rechnung_name/>
  <rechnung_strasse/>
  <rechnung_ort/>
  <rechnung_plz/>
  <rechnung_abteilung/>
  <rechnung_land/>
  <rechnung_email/>
  <rechnung_periode>1</rechnung_periode>
  <rechnung_anzahlpapier>0</rechnung_anzahlpapier>
  <rechnung_permail>0</rechnung_permail>
  <webid/>
  <portofrei_aktiv>0.00</portofrei_aktiv>
  <projekt>0</projekt>
  <objektname/>
  <objekttyp/>
  <parameter/>
  <objektname2/>
  <objekttyp2/>
  <parameter2/>
  <objektname3/>
  <objekttyp3/>
  <parameter3/>
  <kategorie>1</kategorie>
  </xml>
</response>

  
```

### Anlegen und Bearbeiten von Preisen eines Artikels: PreiseEdit

Mit PreiseEdit besteht die Möglichkeit neue Einkaufs- und Verkaufspreise anzulegen, sowie bestehende Einkaufs- und Verkaufspreise zu bearbeiten. Für den genauen Aufbau der XML Struktur, ist der Beispielaufruf der Funktion PreiseEdit weiter unten anzusehen.

Grundlegender Aufbau der XML Daten:

```
  <artikel>
  <id/>
  <nummer/>
  <verkaufspreise>
  <staffelpreis/>
  </verkaufspreise>
  <einkaufspreise>
  <staffelpreis/>
  </einkaufspreise>
</artikel>

  
```

Das Tag <artikel> umschließt alle anderen Tags. Um die Preise zuzuordnen, muss die ID des Artikels angegeben werden. Ab der Version 17.3 kann die Artikelnummer, statt der ID verwendet werden. Anschließend kommt das Tag <verkaufspreise> / <einkaufspreise>, das dann das Tag <staffelpreis> beinhaltet. Innerhalb von <staffelpreis> stehen weitere Parameter wie im nächsten Absatz gelistet. Für jeden Preis, muss jeweils ein neues Tag <staffelpreis> innerhalb <verkaufspreise> / <einkaufspreise> geöffnet werden.

Folgende Parameter stehen zur Verfügung:

Verkaufspreise:

- <kundennummer> falls Preis für alle gilt und nicht kundenspezifisch, dann <kundennummer> leer lassen
- <gruppe> ID der Gruppe aus Xentral, falls Preis für bestimmte Gruppen gilt. Ansonsten <gruppe> leer lassen
- <ab_menge> Gibt die Menge an, ab der der Preis gültig sein soll. Wenn <ab_menge> leer ist, wird 1 als Menge genommen. Kommazahlen mit Punkt angeben, z.B. 2.50
- <preis> Verkaufspreis, muss mit Punkt angegeben werden, z.B. 29.99

Einkaufspreise:

- <lieferantennummer> muss befüllt sein, sonst wird der Einkaufspreis nicht angelegt / bearbeitet
- <ab_menge> Gibt die Menge an, ab der der Preis gültig sein soll. Wenn <ab_menge> leer ist, wird 1 als Menge genommen. Kommazahlen mit Punkt angeben, z.B. 2.50
- <bestellnummer> Bestellnummer des Artikels beim Lieferanten
- <bezeichnunglieferant> Bezeichnung des Artikels beim Lieferanten
- <preis> Einkaufspreis, muss mit Punkt angegeben werden, z.B. 29.99
- <waehrung> Währung des Preises, falls leer ist, wird EUR als Währung genommen

#### Beispiel Anfrage PreiseEdit mit Funktionen

```
  <?php

$hash = generateHash();

$xml = "<artikel> 
  <id>7</id>
  <verkaufspreise> 
  <staffelpreis>
  <kundennummer>100030</kundennummer>
  <gruppe/>
  <ab_menge>1</ab_menge>
  <preis>2.80</preis>
  </staffelpreis> 
  <staffelpreis>
  <kundennummer/>
  <gruppe/>
  <ab_menge/>
  <preis>2.40</preis>
  </staffelpreis>
  </verkaufspreise>
  <einkaufspreise>
  <staffelpreis>
  <lieferantennummer>70003</lieferantennummer>
  <ab_menge/>
  <bestellnummer>123456789</bestellnummer>
  <bezeichnunglieferant>Artikel 54367B</bezeichnunglieferant>
  <preis>1.20</preis>
  <waehrung/>
  </staffelpreis>
  </einkaufspreise>
  </artikel>
  ";

$output_xml = SendRequest("PreiseEdit",$xml,$hash); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash)
{

  $url = 'http://192.168.0.28/wawision/17.4/www/index.php?module=api&action='.$methodname.'&hash='.$hash;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel Antwort PreiseEdit```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>PreiseEdit</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
</response>

  
```

### Verwalten von weiteren Kontaktinformationen einer Adresse: AdresseKontaktCreate, AdresseKontaktEdit, AdresseKontaktGet

Mit AdresseKontaktCreate können weitere Kontaktinformationen bei einer Adresse hinterlegt werden. Bearbeitet werden diese mit AdresseKontaktEdit. Soll eine Kontaktinformation zurückkommen, geschieht dies mit AdresseKontaktGet.

Mögliche Parameter zum Anlegen und Bearbeiten einer Adressinformation:

- <addresse> ID der Adresse für die Kontaktinformation
- <bezeichnung> Bezeichnung der Kontaktinformation, z.B. Telefon privat
- <kontakt> Inhalt der Kontaktinformation, z.B. eine Telefonnummer

#### Beispiel Anfrage AdresseKontaktCreate mit Funktionen

```
  <?php
$hash = generateHash();

$xml = "<adresse>13</adresse>
  <bezeichnung>Telefon privat</bezeichnung>
  <kontakt>01234567890</kontakt>";

$output_xml = SendRequest("AdresseKontaktCreate",$xml,$hash); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort AdresseKontaktCreate```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AdresseKontaktCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>2</id>
  </xml>
</response>

  
```#### Beispiel Anfrage AdresseKontaktEdit mit Funktionen```
  <?php
$hash = generateHash();

$xml = "<bezeichnung>Mobil privat</bezeichnung>
  <kontakt>01232222222</kontakt>";

$id = 2;

$output_xml = SendRequest("AdresseKontaktEdit",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort AdresseKontaktEdit```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AdresseKontaktEdit</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status> 
</response>
<?xml version="1.0" encoding="UTF-8"?>
  <response>
  <status>
  <action>AdresseKontaktGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <adresse>41</adresse>
  <bezeichnung>Skype Account</bezeichnung>
  <kontakt>123456789</kontakt>
  </xml>
  </response>

  
```

### Anfragen von Belegen (Angebot bis Lieferschein: BelegeList)

Um Informationen aus Belegen zu holen, kann die Funktion BelegeList verwendet werden. Tags die für eine Anfrage innerhalb von <order> verwendet werden können: Nur 1 innerhalb von möglich. Erlaubte Sortierkriterien: anabregs_text, anabregs_text_en, artikelkategorie, belegnr, betrag, bezeichnung, datum, land, letztes_datum, menge, name, name_de, name_en, nummer, ort, plz, preis, status, strasse, telefax, telefon

<desc> 1 oder 0 möglich, um die Sortierung aufsteigend oder absteigend zu gestalten

Tags die für eine Anfrage unterhalb von <order> verwendet werden können, um die Suche nach bestimmten Elementen einzugrenzen:

- <beleg> Folgende Belege sind möglich: auftrag, rechnung, angebot, lieferschein, gutschrift, retoure
- <addresse> ID der gewünschten Adresse, von der Belege angezeigt werden soll
- <datum_von> Datum, ab dem die Belege gewählt werden sollen
- <datum_bis> Datum, bis die Belege gewählt werden sollen
- <groupbyartikel> 1 oder 0, um nach Artikel zu gruppieren oder nicht
- <groupbyadresse> 1 oder 0, um nach Adressen zu gruppieren oder nicht
- <groupbyposition> 1 oder 0, um nach Positionen zu gruppieren oder nicht
- <kategorie> ID der Artikelkategorie
- <kategoriename> Name der Artikelkategorie
- <limit> Zahl angeben, um die Ausgabe der Belege zu limitieren, z.B. <limit>10</limit> zeigt nur die ersten 10 Belege an
- <offset> Zeigt ab der angegeben Zahl die Belege an, z.B. <offset>10</offset>, zeigt ab dem 10. Beleg die Belege an
- Status von gewünschten Belegen angeben, wie z.B. freigegeben oder versendet

#### Beispiel Anfrage mit Funktionen 1

```
  <?php

$hash = generateHash();
$xml = "<order>
  <field>name_de</field>
  <desc>1</desc>
  </order>
  <beleg>rechnung</beleg>
  <groupbyartikel>1</groupbyartikel>
  <limit>10</limit>
  <offset>0</offset>";

$output_xml = SendRequest("BelegeList",$xml,$hash); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash)
{
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

?>

  
```#### Beispiel Antwort nach Anfrage 1```
  <response>
  <status>
  <action>BelegeList</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  
  <xml>
  <artikel_list>
  <artikel>
  <id>
  <value>1</value>
  </id>
  <nummer>
  <value>700001</value>
  </nummer>
  <name_de>
  <value>Apfelmus</value>
  </name_de>
  <menge>
  <value>3</value>
  </menge>
  <betrag>
  <value>2,50</value>
  </betrag>
  <artikelkategorie>
  <value>produkt</value>
  </artikelkategorie>
  <letztes_datum>
  <value>2016-10-19</value>
  </letztes_datum>
  <artikelkategoriebezeichnung>
  <value />
  </artikelkategoriebezeichnung>
  </artikel>
  
  <anz_gesamt>1</anz_gesamt>
  <anz_result>1</anz_result>
  </artikel_list>
  </xml>
  </response>

  
```#### Beispiel Belege Anfrage nach Artikel Eingabe 2```
  <order>
  <field>name_de</field>
  <desc>1</desc>
</order>
<beleg>rechnung</beleg>
<groupbyartikel>1</groupbyartikel>
<limit>10</limit>
<offset>0</offset>
  
```#### Antwort auf Anfrage 2```
  <response>
  <status>
  <action>BelegeList</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <artikel_list>
  <artikel>
  <id>
  <value>29549</value>
  </id>
  <nummer>
  <value>6450823</value>
  </nummer>
  <name_de>
  <value>Testartoleö</value>
  </name_de>
  <menge>
  <value>1</value>
  </menge>
  <betrag>
  <value>0</value>
  </betrag>
  <artikelkategorie>
  <value>1289_kat</value>
  </artikelkategorie>
  <letztes_datum>
  <value>2016-04-26</value>
  </letztes_datum>
  <artikelkategoriebezeichnung>
  <value>Testkategorie</value>
  </artikelkategoriebezeichnung>
  </artikel>
  <artikel>
  <id>
  <value>1388</value>
  </id>
  <nummer>
  <value>123456</value>
  </nummer>
  <name_de>
  <value>Akkuschrauber</value>
  </name_de>
  <menge>
  <value>1</value>
  </menge>
  <betrag>
  <value>94.0252</value>
  </betrag>
  <artikelkategorie>
  <value>produkt</value>
  </artikelkategorie>
  <letztes_datum>
  <value>2016-10-25</value>
  </letztes_datum>
  <artikelkategoriebezeichnung>
  <value/>
  </artikelkategoriebezeichnung>
  </artikel>
  <artikel>
..
  </artikel>
  <anz_gesamt>365</anz_gesamt>
  <anz_result>30</anz_result>
  </artikel_list>
  </xml>
</response>
  
```#### Beispiel: Positionen für einen Lieferschein anhand der Belegnr```
  $input_xml = '<beleg>lieferschein</beleg>
<search>
<field>belegnr</field>
<suche>'.base64_encode(300080).'</suche>
<exakt>1</exakt>
</search>';
$xml = SendRequest($url,"BelegeList",$input_xml,$hash,"", $api_id);
  
```#### Antwort```
  <response>
  <status>
  <action>BelegeList</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <beleg_list>
  <lieferschein>
  <belegid>
  <value>125</value>
  </belegid>
  <datum>
  <value>2016-10-27</value>
  </datum>
  <belegnr>
  <value>300080</value>
  </belegnr>
  <status>
  <value>versendet</value>
  </status>
  <adresse>
  <value>655</value>
  </adresse>
  <name>
  <value>TEST KUNDE</value>
  </name>
  <position>
  <beleg>
  <value>lieferschein</value>
  </beleg>
  <adresse>
  <value>655</value>
  </adresse>
  <name>
  <value>TEST KUNDE</value>
  </name>
  <datum>
  <value>2016-10-27</value>
  </datum>
  <belegnr>
  <value>300080</value>
  </belegnr>
  <belegid>
  <value>125</value>
  </belegid>
  <id>
  <value>178</value>
  </id>
  <lieferschein>
  <value>125</value>
  </lieferschein>
  <artikel>
  <value>36370</value>
  </artikel>
  <projekt>
  <value>1</value>
  </projekt>
  <bezeichnung>
  <value>Artikelname</value>
  </bezeichnung>
  <beschreibung>
  <value>foobar</value>
  </beschreibung>
  <internerkommentar>
  <value/>
  </internerkommentar>
  <nummer>
  <value>A123</value>
  </nummer>
  <seriennummer>
  <value>100002</value>
  </seriennummer>
  <menge>
  <value>2</value>
  </menge>
  <lieferdatum>
  <value>0000-00-00</value>
  </lieferdatum>
  <vpe>
  <value>1</value>
  </vpe>
  <sort>
  <value>1</value>
  </sort>
  <status>
  <value>versendet</value>
  </status>
  <bemerkung>
  <value/>
  </bemerkung>
  <geliefert>
  <value>2</value>
  </geliefert>
  <abgerechnet>
  <value>0</value>
  </abgerechnet>
  <logdatei>
  <value>2016-10-27 09:23:59</value>
  </logdatei>
  <explodiert_parent_artikel>
  <value>0</value>
  </explodiert_parent_artikel>
  <einheit>
  <value/>
  </einheit>
  <zolltarifnummer>
  <value/>
  </zolltarifnummer>
  <herkunftsland>
  <value>DE</value>
  </herkunftsland>
  <artikelnummerkunde>
  <value/>
  </artikelnummerkunde>
  <lieferdatumkw>
  <value>0</value>
  </lieferdatumkw>
  <auftrag_position_id>
  <value>1734</value>
  </auftrag_position_id>
  <lagertext>
  <value/>
  </lagertext>
  <kostenlos>
  <value>0</value>
  </kostenlos>
  <teilprojekt>
  <value>0</value>
  </teilprojekt>
  <freifeld1>
  <value/>
  </freifeld1>
  <freifeld2>
  <value/>
  </freifeld2>
  <freifeld3>
  <value/>
  </freifeld3>
  <freifeld4>
  <value/>
  </freifeld4>
  <freifeld5>
  <value/>
  </freifeld5>
  <freifeld6>
  <value/>
  </freifeld6>
  <freifeld7>
  <value/>
  </freifeld7>
  <freifeld8>
  <value/>
  </freifeld8>
  <freifeld9>
  <value/>
  </freifeld9>
  <freifeld10>
  <value/>
  </freifeld10>
  <explodiert_parent>
  <value>0</value>
  </explodiert_parent>
  <artikelkategorie>
  <value>1331_kat</value>
  </artikelkategorie>
  <preis>
  <value>0</value>
  </preis>
  </position>
  </lieferschein>
  <anz_gesamt>1</anz_gesamt>
  <anz_result>1</anz_result>
  </beleg_list>
  </xml>
</response>
  
```

### Abfrage von Umsätzen: AdresseListeGet

Mit AdresseListeGet können Kunden ausgegeben werden, die z.B. innerhalb eines bestimmten Zeitraums eine bestimmte Menge Umsatz erzeugt haben.

Die Abfrage der Kunden können mit einigen Parametern eingegrenzt werden:

- <order> beinhaltet das Tag <field>. Dadurch wird Ihr Ergebnis nach dem Feld in <field> sortiert
- <field> steht innerhalb von <order> und kann verschiedene Filter beinhalten, wie z.B. <field>name</field>. Möglich sind: gruppenname, kennziffer, name, plz, ort, telefon, telefax, ansprechpartner, typ, strasse, land, email, kundennummer, lieferantennummer
- <desc> steht innerhalb von <order>. Wird eine 1 gesetzt, wird Ihr Ergebnis absteigend nach Ihrer Angabe von <field> sortiert. Bei einer 0 das selbe aufsteigend
- <limit> limitiert das Ergebnis Ihrer Abfrage auf Ihre festgelegte Zahl, z.B. <limit>10</limit> zeigt nur die ersten 10 Belege an
- <offset> zeigt ab der angegeben Zahl die Belege an, z.B. <offset>10</offset>, zeigt ab dem 10. Beleg die Belege an
- <kategorie> Hier muss die Kategorien-ID angegeben werden. Wenn ein Beleg einen Artikel aus dieser Artikelkategorie enthält wird der Gesamtumsatz angezeigt
- <vertrieb> Hier muss die ID des Vertriebsmitarbeiters angegeben werden. Die Umsätze dieser Belege mit diesem Vertriebsmitarbeiter werden summiert
- <summierung> beinhaltet die verschiedenen Tags der Belegarten, deren Umsätze summiert werden sollen. Möglich sind:
  - <rechnung>
  - <gutschrift>
  - <bestellung>
  - <auftrag>
  - <angebot>
- <umsatzvon> gibt den Mindestumsatz an der vorhanden sein muss
- <status> Hier kann der Status angegeben werden, die die Belege erfüllen müssen. Wird kein <status> angegeben, werden stornierte und angelegte Belege nicht mit einbezogen
- <datumvon> Ab diesem Datum werden die Belege berücksichtigt
- <datumbis> Bis zu diesem Datum werden die Belege berücksichtigt
- <searchmode> Hier kann AND oder OR angegeben werden, um die einzelnen Bedingungen zu verknüpfen. Wird nichts angegeben, wird AND verwendet
- <exakt> Hier muss 1 oder 0 angegeben werden, ob die Bedingungen bei LIKE von % umschlossen werden sollen oder nicht. 1 bedeutet mit % (z.B. LIKE %Bedingung%), 0 bedeutet ohne (z.B. LIKE Bedingung)
- <search> beinhaltet die Tags <suche> und <field>. In <suche> muss mit base64_encode() der Wert übergeben werden, nachdem gesucht werden soll, wie z.B. einem spezifischen Kundennamen (<suche>.base64_encode('Testname').</suche>). Mit <field> wird dann das Datenbankfeld aus der Adresstabelle genannt, in dem der Begriff aus <suche> gesucht werden soll (<field>name</field>)
- <id> Mit Angabe der Adress-ID kann die Abfrage auf diese Adresse beschränkt werden

#### Beispiel 1 Anfrage AdresseListeGet mit Funktionen

```
  $input_xml = "
<order>
  <field>name</field><desc>0</desc>
</order>
<limit>10</limit>
<offset>0</offset>
<summierung> 
  <beleg>rechnung</beleg>
  <beleg>gutschrift</beleg>
</summierung>
<umsatzvon>100</umsatzvon>
<datumbis>2016-09-08</datumbis>
<datumvon>2015-03-08</datumvon>
";
$xml = SendRequest($url,"AdresseListeGet",$input_xml,$hash,"", $api_id);

  
```#### Beispiel 1 Antwort AdresseListeGet```
  <response>
  <status>
  <action>AdresseListeGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <adressen>
  <adresse>
  <id>
  <value>1085</value>
  </id>
  <typ/>
  <marketingsperre/>
  <trackingsperre>
  <value>0</value>
  </trackingsperre>
  <rechnungsadresse>
  <value>0</value>
  </rechnungsadresse>
  <sprache/>
  <name>
  <value>Testkunde</value>
  </name>
  <abteilung/>
  <unterabteilung/>
  <ansprechpartner/>
  <land>
  <value>DE</value>
  </land>
  <strasse>
  <value>Musterstr. 1</value>
  </strasse>
  <ort>
  <value>Musterstadt</value>
  </ort>
  <plz>
  <value>12345</value>
  </plz>
  <telefon/>
  <telefax/>
  <mobil/>
  <email>
  <value>email@example.com</value>
  </email>
  <ustid/>
  <ust_befreit>
  <value>0</value>
  </ust_befreit>
  <passwort_gesendet>
  <value>0</value>
  </passwort_gesendet>
  <sonstiges/>
  <adresszusatz/>
  <kundenfreigabe>
  <value>0</value>
  </kundenfreigabe>
  <steuer/>
  <logdatei>
  <value>2016-09-23 12:01:26</value>
  </logdatei>
  <kundennummer>
  <value>10476</value>
  </kundennummer>
  <lieferantennummer/>
  <mitarbeiternummer/>
  <konto/>
  <blz/>
  <bank/>
  <inhaber/>
  <swift/>
  <iban/>
  <waehrung/>
  <paypal/>
  <paypalinhaber/>
  <paypalwaehrung/>
  <projekt>
  <value>1</value>
  </projekt>
  <partner>
  <value>0</value>
  </partner>
  <zahlungsweise/>
  <zahlungszieltage/>
  <zahlungszieltageskonto/>
  <zahlungszielskonto/>
  <versandart/>
  <kundennummerlieferant/>
  <zahlungsweiselieferant/>
  <zahlungszieltagelieferant/>
  <zahlungszieltageskontolieferant/>
  <zahlungszielskontolieferant/>
  <versandartlieferant/>
  <geloescht>
  <value>0</value>
  </geloescht>
  <firma>
  <value>1</value>
  </firma>
  <webid/>
  <vorname/>
  <kennung/>
  <sachkonto/>
  <freifeld1/>
  <freifeld2/>
  <freifeld3/>
  <filiale/>
  <vertrieb/>
  <innendienst/>
  <verbandsnummer/>
  <abweichendeemailab/>
  <portofrei_aktiv/>
  <portofreiab>
  <value>0.00</value>
  </portofreiab>
  <infoauftragserfassung/>
  <mandatsreferenz/>
  <mandatsreferenzdatum/>
  <mandatsreferenzaenderung>
  <value>0</value>
  </mandatsreferenzaenderung>
  <glaeubigeridentnr/>
  <kreditlimit>
  <value>0.00</value>
  </kreditlimit>
  <tour>
  <value>0</value>
  </tour>
  <zahlungskonditionen_festschreiben/>
  <rabatte_festschreiben/>
  <mlmaktiv/>
  <mlmvertragsbeginn/>
  <mlmlizenzgebuehrbis/>
  <mlmfestsetzenbis/>
  <mlmfestsetzen>
  <value>0</value>
  </mlmfestsetzen>
  <mlmmindestpunkte>
  <value>0</value>
  </mlmmindestpunkte>
  <mlmwartekonto>
  <value>0.00</value>
  </mlmwartekonto>
  <abweichende_rechnungsadresse>
  <value>0</value>
  </abweichende_rechnungsadresse>
  <rechnung_vorname/>
  <rechnung_name/>
  <rechnung_titel/>
  <rechnung_typ/>
  <rechnung_strasse/>
  <rechnung_ort/>
  <rechnung_plz/>
  <rechnung_ansprechpartner/>
  <rechnung_land/>
  <rechnung_abteilung/>
  <rechnung_unterabteilung/>
  <rechnung_adresszusatz/>
  <rechnung_telefon/>
  <rechnung_telefax/>
  <rechnung_anschreiben/>
  <rechnung_email/>
  <geburtstag/>
  <rolledatum/>
  <liefersperre/>
  <liefersperregrund/>
  <mlmpositionierung/>
  <steuernummer/>
  <steuerbefreit/>
  <mlmmitmwst/>
  <mlmabrechnung/>
  <mlmwaehrungauszahlung/>
  <mlmauszahlungprojekt>
  <value>0</value>
  </mlmauszahlungprojekt>
  <sponsor/>
  <geworbenvon/>
  <logfile/>
  <kalender_aufgaben/>
  <verrechnungskontoreisekosten>
  <value>0</value>
  </verrechnungskontoreisekosten>
  <usereditid/>
  <useredittimestamp>
  <value>0000-00-00 00:00:00</value>
  </useredittimestamp>
  <rabatt/>
  <provision/>
  <rabattinformation/>
  <rabatt1/>
  <rabatt2/>
  <rabatt3/>
  <rabatt4/>
  <rabatt5/>
  <internetseite/>
  <bonus1/>
  <bonus1_ab/>
  <bonus2/>
  <bonus2_ab/>
  <bonus3/>
  <bonus3_ab/>
  <bonus4/>
  <bonus4_ab/>
  <bonus5/>
  <bonus5_ab/>
  <bonus6/>
  <bonus6_ab/>
  <bonus7/>
  <bonus7_ab/>
  <bonus8/>
  <bonus8_ab/>
  <bonus9/>
  <bonus9_ab/>
  <bonus10/>
  <bonus10_ab/>
  <rechnung_periode/>
  <rechnung_anzahlpapier/>
  <rechnung_permail/>
  <titel/>
  <anschreiben/>
  <nachname/>
  <arbeitszeitprowoche>
  <value>0.00</value>
  </arbeitszeitprowoche>
  <folgebestaetigungsperre>
  <value>0</value>
  </folgebestaetigungsperre>
  <verein_mitglied_seit/>
  <verein_mitglied_bis/>
  <verein_mitglied_aktiv/>
  <verein_spendenbescheinigung>
  <value>0</value>
  </verein_spendenbescheinigung>
  <freifeld4/>
  <freifeld5/>
  <freifeld6/>
  <freifeld7/>
  <freifeld8/>
  <freifeld9/>
  <freifeld10/>
  <rechnung_papier>
  <value>0</value>
  </rechnung_papier>
  <angebot_cc/>
  <auftrag_cc/>
  <rechnung_cc/>
  <gutschrift_cc/>
  <lieferschein_cc/>
  <bestellung_cc/>
  <angebot_fax_cc/>
  <auftrag_fax_cc/>
  <rechnung_fax_cc/>
  <gutschrift_fax_cc/>
  <lieferschein_fax_cc/>
  <bestellung_fax_cc/>
  <abperfax>
  <value>0</value>
  </abperfax>
  <abpermail/>
  <kassiereraktiv>
  <value>0</value>
  </kassiereraktiv>
  <kassierernummer/>
  <kassiererprojekt>
  <value>0</value>
  </kassiererprojekt>
  <portofreilieferant_aktiv>
  <value>0</value>
  </portofreilieferant_aktiv>
  <portofreiablieferant>
  <value>0.00</value>
  </portofreiablieferant>
  <mandatsreferenzart/>
  <mandatsreferenzwdhart/>
  <serienbrief>
  <value>0</value>
  </serienbrief>
  <lieferantennummerbeikunde/>
  <lead>
  <value>0</value>
  </lead>
  <geburtstagkalender>
  <value>0</value>
  </geburtstagkalender>
  <zahlungsweiseabo/>
  <bundesland/>
  <liefersperredatum/>
  <mandatsreferenzhinweis/>
  <geburtstagskarte>
  <value>0</value>
  </geburtstagskarte>
  <kundennummer_buchhaltung/>
  <lieferantennummer_buchhaltung/>
  <mlmintranetgesamtestruktur>
  <value>0</value>
  </mlmintranetgesamtestruktur>
  <rechnung_umsatz_netto>
  <value>1219.24</value>
  </rechnung_umsatz_netto>
  <gutschrift_umsatz_netto/>
  </adresse>
  <adresse>
...
  </adresse>
  <anz_gesamt>6771</anz_gesamt>
  <anz_result>10</anz_result>
  </adressen>
  </xml>
</response>

  
```#### Beispiel 2 Anfrage AdresseListeGet mit Funktionen```
  <?php

$hash = generateHash();

$xml = "<order>
  <field>name</field>
  <desc>0</desc>
  </order>
  <limit>10</limit>
  <offset>0</offset>
  <summierung> 
  <beleg>rechnung</beleg>
  </summierung>
  <umsatzvon>2800</umsatzvon>
  <search>
  <suche>".base64_encode('86150')."</suche>
  <field>plz</field>
  </search> 
  ";

$output_xml = SendRequest("AdresseListeGet",$xml,$hash); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash)
{

  $url = 'http://192.168.0.28/wawision/17.4/www/index.php?module=api&action='.$methodname.'&hash='.$hash;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel 2 Antwort AdresseListeGet```
  <response>
  <status>
  <action>AdresseListeGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <adressen>
  <adresse>
  <id>
  <value>1085</value>
  </id>
  <typ/>
  <marketingsperre/>
  <trackingsperre>
  <value>0</value>
  </trackingsperre>
  <rechnungsadresse>
  <value>0</value>
  </rechnungsadresse>
  <sprache/>
  <name>
  <value>Testkunde</value>
  </name>
  <abteilung/>
  <unterabteilung/>
  <ansprechpartner/>
  <land>
  <value>DE</value>
  </land>
  <strasse>
  <value>Musterstr. 1</value>
  </strasse>
  <ort>
  <value>Musterstadt</value>
  </ort>
  <plz>
  <value>86150</value>
  </plz>
  <telefon/>
  <telefax/>
  <mobil/>
  <email>
  <value>email@example.com</value>
  </email>
  <ustid/>
  <ust_befreit>
  <value>0</value>
  </ust_befreit>
  <passwort_gesendet>
  <value>0</value>
  </passwort_gesendet>
  <sonstiges/>
  <adresszusatz/>
  <kundenfreigabe>
  <value>0</value>
  </kundenfreigabe>
  <steuer/>
  <logdatei>
  <value>2016-09-23 12:01:26</value>
  </logdatei>
  <kundennummer>
  <value>10476</value>
  </kundennummer>
  <lieferantennummer/>
  <mitarbeiternummer/>
  <konto/>
  <blz/>
  <bank/>
  <inhaber/>
  <swift/>
  <iban/>
  <waehrung/>
  <paypal/>
  <paypalinhaber/>
  <paypalwaehrung/>
  <projekt>
  <value>1</value>
  </projekt>
  <partner>
  <value>0</value>
  </partner>
  <zahlungsweise/>
  <zahlungszieltage/>
  <zahlungszieltageskonto/>
  <zahlungszielskonto/>
  <versandart/>
  <kundennummerlieferant/>
  <zahlungsweiselieferant/>
  <zahlungszieltagelieferant/>
  <zahlungszieltageskontolieferant/>
  <zahlungszielskontolieferant/>
  <versandartlieferant/>
  <geloescht>
  <value>0</value>
  </geloescht>
  <firma>
  <value>1</value>
  </firma>
  <webid/>
  <vorname/>
  <kennung/>
  <sachkonto/>
  <freifeld1/>
  <freifeld2/>
  <freifeld3/>
  <filiale/>
  <vertrieb/>
  <innendienst/>
  <verbandsnummer/>
  <abweichendeemailab/>
  <portofrei_aktiv/>
  <portofreiab>
  <value>0.00</value>
  </portofreiab>
  <infoauftragserfassung/>
  <mandatsreferenz/>
  <mandatsreferenzdatum/>
  <mandatsreferenzaenderung>
  <value>0</value>
  </mandatsreferenzaenderung>
  <glaeubigeridentnr/>
  <kreditlimit>
  <value>0.00</value>
  </kreditlimit>
  <tour>
  <value>0</value>
  </tour>
  <zahlungskonditionen_festschreiben/>
  <rabatte_festschreiben/>
  <mlmaktiv/>
  <mlmvertragsbeginn/>
  <mlmlizenzgebuehrbis/>
  <mlmfestsetzenbis/>
  <mlmfestsetzen>
  <value>0</value>
  </mlmfestsetzen>
  <mlmmindestpunkte>
  <value>0</value>
  </mlmmindestpunkte>
  <mlmwartekonto>
  <value>0.00</value>
  </mlmwartekonto>
  <abweichende_rechnungsadresse>
  <value>0</value>
  </abweichende_rechnungsadresse>
  <rechnung_vorname/>
  <rechnung_name/>
  <rechnung_titel/>
  <rechnung_typ/>
  <rechnung_strasse/>
  <rechnung_ort/>
  <rechnung_plz/>
  <rechnung_ansprechpartner/>
  <rechnung_land/>
  <rechnung_abteilung/>
  <rechnung_unterabteilung/>
  <rechnung_adresszusatz/>
  <rechnung_telefon/>
  <rechnung_telefax/>
  <rechnung_anschreiben/>
  <rechnung_email/>
  <geburtstag/>
  <rolledatum/>
  <liefersperre/>
  <liefersperregrund/>
  <mlmpositionierung/>
  <steuernummer/>
  <steuerbefreit/>
  <mlmmitmwst/>
  <mlmabrechnung/>
  <mlmwaehrungauszahlung/>
  <mlmauszahlungprojekt>
  <value>0</value>
  </mlmauszahlungprojekt>
  <sponsor/>
  <geworbenvon/>
  <logfile/>
  <kalender_aufgaben/>
  <verrechnungskontoreisekosten>
  <value>0</value>
  </verrechnungskontoreisekosten>
  <usereditid/>
  <useredittimestamp>
  <value>0000-00-00 00:00:00</value>
  </useredittimestamp>
  <rabatt/>
  <provision/>
  <rabattinformation/>
  <rabatt1/>
  <rabatt2/>
  <rabatt3/>
  <rabatt4/>
  <rabatt5/>
  <internetseite/>
  <bonus1/>
  <bonus1_ab/>
  <bonus2/>
  <bonus2_ab/>
  <bonus3/>
  <bonus3_ab/>
  <bonus4/>
  <bonus4_ab/>
  <bonus5/>
  <bonus5_ab/>
  <bonus6/>
  <bonus6_ab/>
  <bonus7/>
  <bonus7_ab/>
  <bonus8/>
  <bonus8_ab/>
  <bonus9/>
  <bonus9_ab/>
  <bonus10/>
  <bonus10_ab/>
  <rechnung_periode/>
  <rechnung_anzahlpapier/>
  <rechnung_permail/>
  <titel/>
  <anschreiben/>
  <nachname/>
  <arbeitszeitprowoche>
  <value>0.00</value>
  </arbeitszeitprowoche>
  <folgebestaetigungsperre>
  <value>0</value>
  </folgebestaetigungsperre>
  <verein_mitglied_seit/>
  <verein_mitglied_bis/>
  <verein_mitglied_aktiv/>
  <verein_spendenbescheinigung>
  <value>0</value>
  </verein_spendenbescheinigung>
  <freifeld4/>
  <freifeld5/>
  <freifeld6/>
  <freifeld7/>
  <freifeld8/>
  <freifeld9/>
  <freifeld10/>
  <rechnung_papier>
  <value>0</value>
  </rechnung_papier>
  <angebot_cc/>
  <auftrag_cc/>
  <rechnung_cc/>
  <gutschrift_cc/>
  <lieferschein_cc/>
  <bestellung_cc/>
  <angebot_fax_cc/>
  <auftrag_fax_cc/>
  <rechnung_fax_cc/>
  <gutschrift_fax_cc/>
  <lieferschein_fax_cc/>
  <bestellung_fax_cc/>
  <abperfax>
  <value>0</value>
  </abperfax>
  <abpermail/>
  <kassiereraktiv>
  <value>0</value>
  </kassiereraktiv>
  <kassierernummer/>
  <kassiererprojekt>
  <value>0</value>
  </kassiererprojekt>
  <portofreilieferant_aktiv>
  <value>0</value>
  </portofreilieferant_aktiv>
  <portofreiablieferant>
  <value>0.00</value>
  </portofreiablieferant>
  <mandatsreferenzart/>
  <mandatsreferenzwdhart/>
  <serienbrief>
  <value>0</value>
  </serienbrief>
  <lieferantennummerbeikunde/>
  <lead>
  <value>0</value>
  </lead>
  <geburtstagkalender>
  <value>0</value>
  </geburtstagkalender>
  <zahlungsweiseabo/>
  <bundesland/>
  <liefersperredatum/>
  <mandatsreferenzhinweis/>
  <geburtstagskarte>
  <value>0</value>
  </geburtstagskarte>
  <kundennummer_buchhaltung/>
  <lieferantennummer_buchhaltung/>
  <mlmintranetgesamtestruktur>
  <value>0</value>
  </mlmintranetgesamtestruktur>
  <rechnung_umsatz_netto>
  <value>3400.87</value>
  </rechnung_umsatz_netto>
  </adresse>
  <anz_gesamt>1</anz_gesamt>
  <anz_result>1</anz_result>
  </adressen>
  </xml>
</response>

  
```

### Verwalten von Dateien: DateiList, DateiHeader, DateiDownload

Mit DateiList können Dateien die sich in xentral befinden angezeigt werden. Zur Auswahl stehen hierbei zwei Parameter:

- <parameter> Entspricht hier der ID des jeweiligen Objekts
- <objekt> Hier muss angegeben werden, von welchem Objekt die Dateien kommen, wie z.B. adressen, auftrag oder rechnung. Sollen bereits hochgeladene Dateien wieder heruntergeladen werden, kann dies in Kombination von DateiHeader und DateiDownload umgesetzt werden.

#### Beispiel Anfrage DateiList mit Funktionen

```
  <?php
$hash = generateHash();

$xml = "<parameter>1</parameter>
  <objekt>Adressen</objekt>";

$output_xml = SendRequest("DateiList",$xml,$hash);

 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash)
{
 
  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort DateiList```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>DateiList</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <Datei>
  <titel>Arbeitsnachweis Testfirma GmbH von 2017-02-23 bis 2017-02-23</titel>
  <subjekt>anhang</subjekt>
  <version>1</version>
  <ersteller>Testfirma GmbH</ersteller>
  <bemerkung>Initiale Version</Bemerkung>
  <datum>2017-03-23</datum>
  <id>16</id>
  </Datei>
  <Datei>
  <titel>Arbeitsnachweis Testfirma GmbH von 2017-02-22 bis 2017-02-22</titel>
  <subjekt>anhang</subjekt>
  <version>1</version>
  <ersteller>Testfirma GmbH</ersteller>
  <bemerkung>Initiale Version</bemerkung>
  <datum>2017-03-22</datum>
  <id>17</id>
  </Datei> 
  </xml>
</response>

  
```#### Beispiel Anfrage DateiHeader + DateiDownload mit Funktionen```
  <?php
$hash = generateHash();

$xml = "";

$id = 20;

$headera = explode("\n",file_get_contents('http://192.168.0.28/wawision/16.3/www/index.php?module=api&action=DateiHeader&hash='.$hash.'&id='.$id));

foreach($headera as $head){
  header($head);
}
echo file_get_contents('http://192.168.0.28/wawision/16.3/www/index.php?module=api&action=DateiDownload&hash='.$hash.'&id='.$id);

exit;

 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}

  
```

#### Beispiel Antwort DateiHeader + DateiDownload

Das typische Fenster zum Öffnen oder Speichern von Dateien öffnet sich.

### Verwalten von Dateien: BelegPDFHeader, BelegPDF

Mit DateiList können sich Dateien, die sich in xentral befinden, anzeigen lassen. Zur Auswahl stehen hierbei zwei Parameter:

- <parameter> Entspricht hier der ID des jeweiligen Objekts.
- <objekt> Hier müssen Sie angeben, von welchem Objekt Sie die Dateien möchten, wie z.B. adressen, auftrag oder rechnung

Sollen bereits hochgeladene Dateien wieder heruntergeladen werden, kann dies in Kombination von DateiHeader und DateiDownload umgesetzt werden.

#### Beispiel Anfrage BelegPDFHeader + BelegPDF mit Funktionen

```
  <?php
$hash = generateHash();

$xml = "";

$id = 20;
$beleg='rechnung';

$headera = explode("\n",file_get_contents('http://192.168.0.28/wawision/18.3/www/index.php?module=api&action=BelegPDFHeader&hash='.$hash.'&id='.$id.'&beleg='.$beleg));

foreach($headera as $head){
  header($head);
}
echo file_get_contents('http://192.168.0.28/wawision/18.3/www/index.php?module=api&action=BelegPDF&hash='.$hash.'&id='.$id.'&beleg='.$beleg);

exit;

 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}

  
```

#### Beispiel Antwort BelegPDFHeader + BelegPDF

Das typische Fenster zum Öffnen oder Speichern von Dateien öffnet sich.

### Sonderfunktionen von Spezialmodulen

#### XML Artikelkontingente

Zum Abfragen der Kontingente gibt es zwei Möglichkeiten: Mit und ohne die Parameter sowie von und bis. Ohne die beiden Parameter erscheint die Artikelkontingent Liste ab dem heutigen Datum. Mit den Parametern erscheint eine Liste mit den gebuchten Artikeln in dem Zeitbereich von Aufträgen, die den Status "freigegeben" haben.

##### Beispiel Anfrage ArtikelkontingenteGet

```
  <?php
 include("../api.php");
 include("../config.php");
 global $remotedomain,$initkey,$url;

 $hash = generateHash($initkey,$remotedomain);

 $nummer = "700245";

 $von = "2015-07-01";
 $bis = "2015-07-20";

 header('Content-Type: application/xml; charset=utf-8');
 echo SendRequest($url,"ArtikelkontingenteGet","",$hash,"&nummer=".$nummer."&von=".$von."&bis=".$bis);

  
```##### Beispiel Antwort ArtikelkontingenteGet```<?xml version="1.0" encoding="UTF-8"?><response><status><action>ArtikelkontingenteGet</action><message>OK</message><messageCode>1</messageCode></status><xml><artikelkontingente><kontingent><gebucht>103</gebucht><menge>11.00</menge><datum>2015-07-13</datum></kontingent><kontingent><gebucht>5</gebucht><menge>5.00</menge><datum>2015-07-17</datum></kontingent></artikelkontingente></xml>```

#### Anfrage von Daten aus Export Vorlagen: ExportVorlageGet

Um Daten aus Export Vorlagen abfragen zu können, muss bereits eine Export Vorlage angelegt sein (Anleitung zu Export Vorlagen). Verfügbare Daten die abgefragt werden können:

- Adressen
- Angebote
- Aufträge
- Ansprechpartner
- Artikel
- Gutschriften
- Rechnungen
- Lieferscheine
- Bestellungen
- Angebotspositionen
- Auftragspositionen
- Gutschriftpositionen
- Rechnungspositionen
- Lieferscheinpositionen
- Bestellungspositionen

Damit die Daten über die API abrufbar sind, muss im Bearbeitungsmodus der gewünschten Export Vorlage der Haken API Freigabe aktiviert sein.

Ebenfalls im Bearbeitungsmodus der Export Vorlage muss der Haken CSV Beschriftung aktiviert werden, damit die Spaltennamen als XML Tagnamen verwendet werden, denn sonst funktioniert die Ausgabe als XML nicht.

Zur Abfrage der Daten stehen hierbei verschiedene GET Parameter zur Auswahl:

- id → Entspricht hier der ID der jeweiligen Export Vorlage (Pflichtfeld)
- von → Datumsangabe (im Format dd.mm.yy), ab wann die gewünschten Daten abgefragt werden sollen (optional). Verfügbar bei Angeboten, Aufträgen, Gutschriften, Rechnungen, Lieferscheine, Bestellungen und deren Positionen
- bis → Datumsangabe (im Format dd.mm.yy), bis wann die gewünschten Daten abgefragt werden sollen (optional). Verfügbar bei Angeboten, Aufträgen, Gutschriften, Rechnungen, Lieferscheine, Bestellungen und deren Positionen
- projekt → Gibt nur die Daten zum passenden Projekt zurück (optional). Verfügbar bei Adressen, Angeboten, Aufträgen, Artikel, Gutschriften, Rechnungen, Lieferscheine, Bestellungen und deren dazugehörige Belegpositionen.

Welche Werte der Export Vorlage zurückgeliefert werden, hängt von den festgelegten CSV Feldern in der Export Vorlage ab.

##### Beispiel Anfrage ExportVorlageGet mit Funktionen

```
  <?php

$hash = generateHash();

$xml = "";

$id = "1";
$projekt = "";
$von = "";
$bis = "";

$output_xml = SendRequest("ExportVorlageGet",$xml,$hash,$id,$projekt,$von,$bis); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash,$id,$projekt,$von,$bis)
{

  $url = 'http://192.168.0.28/wawision/16.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id.'&projekt='.$projekt.'&von='.$von.'&bis='.$bis;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```##### Beispiel Antwort ExportVorlageGet für Artikel```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>ExportVorlageGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <items>
  <item>
  <nummer>1000001</nummer>
  <name_de>Tastatur</name_de>
  <name_en/>
  <beschreibung_de/>
  <beschreibung_en/>
  <kurztext_de/>
  <kurztext_en/>
  <internerkommentar/>
  <hersteller/>
  <herstellernummer/>
  <herstellerlink/>
  <ean/>
  <systemid>1</systemid>
  </item>
  <item>
  <nummer>1000002</nummer>
  <name_de>Tasten</name_de>
  <name_en/>
  <beschreibung_de/>
  <beschreibung_en/>
  <kurztext_de/>
  <kurztext_en/>
  <internerkommentar/>
  <hersteller/>
  <herstellernummer/>
  <herstellerlink/>
  <ean/>
  <systemid>2</systemid>
  </item>
  <item>
  <nummer>1000003</nummer>
  <name_de>USB Maus</name_de>
  <name_en/>
  <beschreibung_de/>
  <beschreibung_en/>
  <kurztext_de/>
  <kurztext_en/>
  <internerkommentar/>
  <hersteller/>
  <herstellernummer/>
  <herstellerlink/>
  <ean/>
  <systemid>3</systemid>
  </item>
  </items>
  </xml>
</response>

  
```

### Anfrage von Daten aus Berichten: BerichteGet

BerichteGet liefert das Ergebnis der SQL Abfrage aus dem Strukturfeld eines Berichts zurück.

BerichteGet liefert das Ergebnis der SQL Abfrage aus dem Strukturfeld eines Berichts zurück. Hierzu muss die ID des Berichts als GET Parameter übergeben werden.

#### Beispiel Anfrage BerichteGet mit Funktionen

```
  <?php

$hash = generateHash();

$xml = "";

$id = "1";

$output_xml = SendRequest("BerichteGet",$xml,$hash,$id); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash,$id)
{

  $url = 'http://192.168.0.28/wawision/17.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel Antwort BerichteGet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>BerichteGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <items>
  <item>
  <name>Kunde 1</name>
  <kundennummer>10000</kundennummer>
  </item>
  <item>
  <name>Kunde 2</name>
  <kundennummer>10001</kundennummer>
  </item>
  </items>
  </xml>
</response>

  
```

### Anfrage von Daten aus Artikeln mit Hilfe von Filtern: ArtikelList

ArtikelList liefert als Ergebnis alle Artikelinformationen zu den Artikeln, die auf Ihre Suchkriterien zutreffen.

Folgende Parameter stehen Ihnen zur Verfügung:

- Innerhalb des <order> Tags können Sie das Tag <field> angeben. Innerhalb von <field> steht die Spaltenbezeichnung aus der Artikeltabelle der Datenbank, mit der das Ergebnis sortiert werden kann
- Hierzu kann ebenfalls innerhalb des Tags <order> das Tag <desc> angegeben werden. Bei 1 wird absteigend sortiert, bei 0 aufsteigend. Wird <desc> nicht angegeben, wird standardmäßig aufsteigend nach dem Feld sortiert, dass in <field> angegeben wurde
- Mit dem Tag <limit> kann die Auflistung der Ergebnisse auf eine bestimmte Anzahl beschränkt werden
- Das Tag <offset> kann nur in Kombination mit <limit> verwendet werden, um Ihre Auflistung der Ergebnisse auf eine bestimmte Anzahl zu beschränken. Z.B. zeigt <limit>10</limit> und <offset>0</offset> alle Einträge von 0 bis 10.
- Neben den oben genannten Tags kann als Tag jede Spaltenbezeichnung aus der Artikeltabelle der Datenbank verwenden werden, um die Suche weiter einzuschränken, z.B. sucht <name_de>Schraube</name_de> nach den Artikeln, die im Namen Schraube beinhalten.

#### Beispiel Anfrage ArtikelList mit Funktionen

```
  <?php

$hash = generateHash();

$xml = "<order> 
  <field>name_de</field>
  <desc>1</desc> 
  </order> 
  <limit>10</limit> 
  <offset>0</offset>
  <name_de>Apfel</name_de>
  ";

$id = "";

$output_xml = SendRequest("ArtikelList",$xml,$hash); 

function generateHash()
{
  
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";

  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
  
  return $hash;
}

function SendRequest($methodname,$xml,$hash)
{

  $url = 'http://192.168.0.28/wawision/17.4/www/index.php?module=api&action='.$methodname.'&hash='.$hash;

  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';

  $data = array('xml' => $xml, 'md5sum' => md5($xml));

  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}

$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";

?>

  
```#### Beispiel Antwort ArtikelList```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>ArtikelList</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <items>
  <item>
  <id>7</id>
  <typ>produkt</typ>
  <nummer>1000006</nummer>
  <checksum/>
  <projekt>1</projekt>
  <inaktiv/>
  <ausverkauft>0</ausverkauft>
  <warengruppe/>
  <name_de>Apfelkuchen</name_de>
  <name_en/>
  <kurztext_de/>
  <kurztext_en/>
  <beschreibung_de/>
  <beschreibung_en/>
  <uebersicht_de/>
  <uebersicht_en/>
  <links_de/>
  <links_en/>
  <startseite_de/>
  <startseite_en/>
  <standardbild/>
  <herstellerlink/>
  <hersteller/>
  <teilbar/>
  <nteile/>
  <seriennummern>keine</seriennummern>
  <lager_platz>1</lager_platz>
  <lieferzeit/>
  <lieferzeitmanuell/>
  <sonstiges/>
  <gewicht/>
  <endmontage/>
  <funktionstest/>
  <artikelcheckliste/>
  <stueckliste>1</stueckliste>
  <juststueckliste>0</stueckliste>
  <barcode/>
  <hinzugefuegt/>
  <pcbdecal/>
  <lagerartikel>1</lagerartikel>
  <porto>0</porto>
  <chargenverwaltung>0</chargenverwaltung>
  <provisionsartikel>0</provisionsartikel>
  <gesperrt>0</gesperrt>
  <sperrgrund/>
  <geloescht>0</geloescht>
  <gueltigbis>0000-00-00</gueltigbis>
  <umsatzsteuer>normal</normal>
  <klasse/>
  <adresse>0</adresse>
  <shopartikel>0</shopartikel>
  <unishopartikel>0</unishopartikel>
  <journalshopartikel>0</journalshopartikel>
  <shop>0</shop>
  <katalog>0</katalog>
  <katalogtext_de/>
  <katalogtext_en/>
  <katalogbezeichnung_de/>
  <katalogbezeichnung_en/>
  <neu>0</neu>
  <topseller>0</topseller>
  <startseite>0</startseite>
  <wichtig>0</wichtig>
  <mindestlager>0</mindestlager>
  <mindestbestellung>0</mindestbestellung>
  <partnerprogramm_sperre>0</partnerprogramm_sperre>
  <internerkommentar/>
  <intern_gesperrt>0</intern_gesperrt>
  <intern_gesperrtuser>0</intern_gesperrtuser>
  <intern_gesperrtgrund/>
  <inbearbeitung>0</inbearbeitung>
  <inbearbeitunguser>0</inbearbeitunguser>
  <cache_lagerplatzinhaltmenge>0</cache_lagerplatzinhaltmenge>
  <internkommentar/>
  <firma>1</firma>
  <logdatei>2017-10-18 08:27:17</logdatei>
  <anabregs_text>Ein Apfelkuchen</anabregs_text>
  <autobestellung>0</autobestellung>
  <produktion>0</produktion>
  <herstellernummer>A232</herstellernummer>
  <restmenge>0</restmenge>
  <mlmdirektpraemie>0.00</mlmdirektpraemie>
  <keineeinzelartikelanzeigen>0</keineeinzelartikelanzeigen>
  <mindesthaltbarkeitsdatum>0</mindesthaltbarkeitsdatum>
  <letzteseriennummer/>
  <individualartikel>0</individualartikel>
  <keinrabatterlaubt>0</keinrabatterlaubt>
  <rabatt>0</rabatt>
  <rabatt_prozent>0.00</rabatt_prozent>
  <geraet>0</geraet>
  <serviceartikel>0</serviceartikel>
  <autoabgleicherlaubt>0</autoabgleicherlaubt>
  <pseudopreis>0.00</pseudopreis>
  <freigabenotwendig>0</freigabenotwendig>
  <freigaberegel/>
  <nachbestellt>0</nachbestellt>
  <ean/>
  <mlmpunkte>0.00</mlmpunkte>
  <mlmbonuspunkte>0.00</mlmbonuspunkte>
  <mlmkeinepunkteeigenkauf>0</mlmkeinepunkteeigenkauf>
  <shop2>0</shop2>
  <shop3>0</shop3>
  <usereditid>1</usereditid>
  <useredittimestamp>2017-10-18 08:27:17</useredittimestamp>
  <freifeld1/>
  <freifeld2/>
  <freifeld3/>
  <freifeld4/>
  <freifeld5/>
  <freifeld6/>
  <einheit/>
  <webid/>
  <lieferzeitmanuell_en/>
  <variante>0</variante>
  <variante_von>0</variante_von>
  <produktioninfo/>
  <sonderaktion/>
  <sonderaktion_en>
  <autolagerlampe>0</autolagerlampe>
  <leerfeld/>
  <zolltarifnummer/>
  <herkunftsland/>
  <laenge>0.00</laenge>
  <breite>0.00</breite>
  <hoehe>0.00</hoehe>
  <gebuehr>0</gebuehr>
  <pseudolager/>
  <downloadartikel>0</downloadartikel>
  <matrixprodukt>0</matrixprodukt>
  <steuer_erloese_inland_normal/>
  <steuer_aufwendung_inland_normal/>
  <steuer_erloese_inland_ermaessigt/>
  <steuer_aufwendung_inland_ermaessigt/>
  <steuer_erloese_inland_steuerfrei/>
  <steuer_aufwendung_inland_steuerfrei/>
  <steuer_erloese_inland_innergemeinschaftlich/>
  <steuer_aufwendung_inland_innergemeinschaftlich/>
  <steuer_erloese_inland_eunormal/>
  <steuer_erloese_inland_nichtsteuerbar/>
  <steuer_erloese_inland_euermaessigt/>
  <steuer_aufwendung_inland_nichtsteuerbar/>
  <steuer_aufwendung_inland_eunormal/>
  <steuer_aufwendung_inland_euermaessigt/>
  <steuer_erloese_inland_export/>
  <steuer_aufwendung_inland_import/>
  <steuer_art_produkt>0</steuer_art_produkt>
  <steuer_art_produkt_download>0</steuer_art_produkt_download>
  <metadescription_de/>
  <metadescription_en/>
  <metakeywords_de/>
  <metakeywords_en/>
  <anabregs_text_en/>
  <externeproduktion>0</externeproduktion>
  <bildvorschau/>
  <inventursperre>0</inventursperre>
  <variante_kopie>0</variante_kopie>
  <unikat>0</unikat>
  <generierenummerbeioption>0</generierenummerbeioption>
  <allelieferanten>0</allelieferanten>
  <tagespreise>0</tagespreise>
  <rohstoffe>0</rohstoffe>
  <provisionssperre>0</provisionssperre>
  <dienstleistung>0</dienstleistung>
  <inventurekaktiv>0</inventurekaktiv>
  <inventurek>0.00000000</inventurek>
  <hinweis_einfuegen/>
  <steuertext_innergemeinschaftlich/> 
  <steuertext_export/> 
  <formelmenge/> 
  <formelpreis/> 
  <freifeld7/> 
  <freifeld8/> 
  <freifeld9/> 
  <freifeld10/> 
  <freifeld11/> 
  <freifeld12/> 
  <freifeld13/> 
  <freifeld14/>
  <freifeld15/> 
  <freifeld16/>
  <freifeld17/>
  <freifeld18/> 
  <freifeld19/>
  <freifeld20/>
  <ursprungsregion/>
  <bestandalternativartikel>0</bestandalternativartikel>
  <metatitle_de/>
  <metatitle_en/>
  <vkmeldungunterdruecken>0</vkmeldungunterdruecken>
  <altersfreigabe/>
  <unikatbeikopie>0</unikatbeikopie>
  <steuergruppe>0</steuergruppe>
  <keinskonto>0</keinskonto>
  <berechneterek>0.0000</berechneterek>
  <verwendeberechneterek>0</verwendeberechneterek>
  <berechneterekwaehrung/>
  </item>
  </items>
  </xml>
</response>

  
```

### Verwalten von Accounts: AccountCreate (ab Version 18.3), AccountEdit (ab Version 18.3), AdresseAccountsGet

Mit AccountCreate kann ein neuer Account innerhalb einer Adresse angelegt werden, welcher mit AccountEdit auch bearbeitet werden kann.

Als Parameter stehen alle Datenbankfelder aus der Tabelle adresse_accounts zur Verfügung:

- <aktiv> gibt an, ob ein Account momentan aktiv (1) oder inaktiv (0) ist
- <adresse> ist die Adress-ID der Adresse, zu der dieser Account gehört
- <bezeichnung> ist die Bezeichnung für diesen Account, z.B. Login Account
- <art> ist die Art eines Accounts, z.B. Datenbank, SSH
- <url> ist die URL zum jeweiligen Account, falls vorhanden
- <benutzername> ist der Benutzername für diesen Account
- <passwort> ist das Passwort für diesen Account
- <gueltig_ab> gibt an, ab wann dieser Account gültig ist
- <gueltig_bis> gibt an, bis wann dieser Account gültig ist
- <email> hier kann die passende E-Mail Adresse eingetragen werden
- <notiz> hier können Notizen eingetragen werden

Pflichtfelder, um einen Account mit AccountCreate anzulegen sind <adresse> und <bezeichnung>.

Um AccountEdit zu verwenden, muss als Get-Parameter die ID des Accounts angegeben werden.

AdresseAccountsGet liefert alle aktiven Accounts einer bestimmten Adresse zurück. Hierfür muss die Adress-ID und optional die Art des Accounts als Get-Parameter übergeben werden.

#### Beispiel Anfrage AccountCreate mit Funktionen

```
  <?php
$hash = generateHash();
 
$xml = "<adresse>3</adresse>
  <bezeichnung>Datenbank Login</bezeichnung>
  <aktiv>1</aktiv>
  <art>db</art>
  <url>http://192.168.0.28/meinedatenbank</url>
  <benutzername>mustermannmax</benutzername>
  <passwort>123456</passwort>
  <gueltig_ab>20.08.2018</gueltig_ab>
  <gueltig_bis>20.08.2019</gueltig_bis>
  <email>maxmustermann@maxmustermann.de</email>
  <notiz>Datenbank Login zu Testsystem</notiz>";
 
$output_xml = SendRequest("AccountCreate",$xml,$hash); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash)
{
 
  $url = 'http://192.168.0.28/wawision/18.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort AccountCreate```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AccountCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>2</id>
  </xml>
</response>

  
```#### Beispiel Anfrage AccountEdit mit Funktionen```
  <?php
$hash = generateHash();
 
$xml = "<bezeichnung>Datenbank Login MySQL</bezeichnung>
  <aktiv>0</aktiv>
  <art>db mysql</art>
  <url>http://192.168.0.28/meinedatenbank</url>
  <benutzername>mustermannmaxsql</benutzername>
  <passwort>123456sql</passwort>
  <gueltig_ab>26.09.2018</gueltig_ab>
  <gueltig_bis>31.12.2019</gueltig_bis>
  <email>maxmustermann@maxmustermann.de</email>
  <notiz>Datenbank Login zu MySQL DB</notiz>";
 
$id = "2";

$output_xml = SendRequest("AccountEdit",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/18.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort AccountEdit```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AccountEdit</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status> 
</response>

  
```#### Beispiel Anfrage AdresseAccountsGet mit Funktionen```
  <?php
$hash = generateHash();
 
$xml = "";

$id = 3; 

$output_xml = SendRequest("AdresseAccountsGet",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/18.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```#### Beispiel Antwort AdresseAccountsGet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>AdresseAccountsGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <adresse_accounts>
  <account>
  <id>2</id>
  <aktiv>1</aktiv>
  <adresse>3</adresse>
  <bezeichnung>Datenbank Login</bezeichnung>
  <art>db</art>
  <url>http://192.168.0.28/meinedatenbank</url>
  <benutzername>mustermannmax</benutzername>
  <passwort>123456</passwort>
  <webid>0</webid>
  <gueltig_ab>2018-08-20</gueltig_ab>
  <gueltig_bis>2019-08-20</gueltig_bis>
  <email>maxmustermann@maxmustermann.de</email>
  <notiz>Datenbank Login zu Testsystem</notiz>
  </account>
  </adresse_accounts>
  </xml>
</response>

  
```

### Weitere Möglichkeiten zur Nutzung der API

#### Zeiterfassung einem Mitarbeiter zuordnen

Ab Version 19.2 gibt es die Möglichkeit, über die API eine Zeiterfassung zu erstellen:

adresse

Wenn die ID der Adresse bekannt ist, für die die Zeiterfassung erstellt werden soll, kann diese im Feld adresse_abrechnung übergeben werden

##### Beispiel Anfrage ZeiterfassungCreate mit Adresse

```
  <?php
$hash = generateHash();
 
$xml = "<adresse>1</adresse>
<adresse_abrechnung>1</adresse_abrechnung>
<von>2017-01-01 12:00:00</von>
<bis>2017-01-01 14:15:00</bis>
<aufgabe>Hallo</aufgabe>";
 
$id = "2";

$output_xml = SendRequest("ZeiterfassungCreate",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/18.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```##### Beispiel Antwort ZeiterfassungCreate mit Adresse```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>ZeiterfassungCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
</response>

  
```

mitarbeiternummer

Ab Version 19.3 gibt es Möglichkeiten, über die API eine Zeiterfassung für eine bestimmte Mitarbeiternummer zu erstellen.

##### Beispiel Anfrage ZeiterfassungCreate mit Mitarbeiternummer

```
  <?php
$hash = generateHash();
 
$xml = "<mitarbeiternummer>90002</mitarbeiternummer>
<von>2017-01-01 12:00:00</von>
<bis>2017-01-01 14:15:00</bis>
<aufgabe>Hallo</aufgabe>";
 
$id = "2";

$output_xml = SendRequest("ZeiterfassungCreate",$xml,$hash,$id); 
 
function generateHash()
{
 
  $initKey = 'neijfj38734hujfie';
  $remoteDomain = 'http://192.168.0.28';
  $date = gmdate('dmY');
  $hash = "";
 
  for($i = 0; $i <= 200; $i++) 
  $hash = sha1($hash. $initKey. $remoteDomain. $date);
 
  return $hash;
}
 
function SendRequest($methodname,$xml,$hash,$id)
{
 
  $url = 'http://192.168.0.28/wawision/18.3/www/index.php?module=api&action='.$methodname.'&hash='.$hash.'&id='.$id;
 
  $xml = '<?xml version="1.0" encoding="UTF-8"?>
  <request>
  <status>
  <function>'.$methodname.'</function>
  </status>
  <xml>'.$xml.'</xml>
  </request>';
 
  $data = array('xml' => $xml, 'md5sum' => md5($xml));
 
  // use key 'http' even if you send the request to https://...
  $options = array(
  'http' => array(
  'header' => "Content-type: application/x-www-form-urlencoded\r\n",
  'method' => 'POST',
  'content' => http_build_query($data),
),
);
 
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  return $result;
}
 
$obj = simplexml_load_string($output_xml);
echo "<pre>";
print_r($obj);
echo "</pre>";
 
?>

  
```##### Beispiel Antwort ZeiterfassungCreate mit Mitarbeiternummer```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>ZeiterfassungCreate</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
</response>

  
```

#### Rechnung als bezahlt markieren

Ab Version 20.1 gibt es die Möglichkeit, über die API Rechnungen als bezahlt zu markieren.

##### Beispiel Anfrage RechnungAlsBezahltMarkieren

```
  <?php

$xml = '<id>6</id>';

$output_xml = SendRequest('RechnungAlsBezahltMarkieren', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort RechnungAlsBezahltMarkieren```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action></action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>6</id>
  </xml>
</response>

  
```

#### Auftrag abschließen

Ab Version 20.1 kann ein Auftrag über die API abgeschlossen werden.

##### Beispiel Anfrage AuftragAbschliessen

```
  <?php

$xml = '<id>2</id>';

$output_xml = SendRequest('AuftragAbschliessen', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort AuftragAbschliessen```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action></action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>2</id>
  </xml>
</response>

  
```

#### Belege freigeben

Ab Version 20.1 gibt es die Möglichkeit, Belege über die API freizugeben. Das gilt für die Belegarten Angebot, Auftrag, Rechnung, Lieferschein, Bestellung und Gutschrift. Der Aufruf ist für alle Belegarten gleich, es ändert sich nur der Funktionsname.

##### Beispiel anhand eines Auftrags

```
  <?php

$xml = '<id>2</id>';

$output_xml = SendRequest('AuftragFreigabe', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort AuftragAbschliessen```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action></action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>8</id>
  <belegnr>200007</belegnr>
  </xml>
</response>

  
```

#### Belege Abschicken

Ab Version 20.1 gibt es die Möglichkeit, Belege über die API zu versenden. Das gilt für Angebot, Auftragsbestätigung, Rechnung, Lieferschein und Gutschrift. Der Aufruf ist für alle Belegarten gleich, es ändert sich nur der Funktionsname.

##### Beispiel Anfrage AuftragVersenden

```
  <?php

$xml = '<id>8</id>
  <versandart>email</versandart>
  <drucker>1</drucker>';

$output_xml = SendRequest('AuftragVersenden', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort AuftragVersenden```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action></action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>8</id>
  </xml>
</response>

  
```

#### Auftrag als Rechnung weiterführen

Ab Version 20.1 gibt es die Möglichkeit, Aufträge über die API als Rechnung weiterzuführen.

##### Beispiel Anfrage WeiterfuehrenAuftragZuRechnung

```
  <?php

$xml = '<id>10</id>';

$output_xml = SendRequest('WeiterfuehrenAuftragZuRechnung', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort WeiterfuehrenAuftragZuRechnung```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action></action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>18</id>
  </xml>
</response>

  
```

#### Rechnung als Gutschrift weiterführen

Ab Version 20.1 gibt es die Möglichkeit, Rechnungen über die API als Gutschrift weiterzuführen.

##### Beispiel Anfrage WeiterfuehrenRechnungZuGutschrift

```
  <?php

$xml = '<id>1</id>';

$output_xml = SendRequest('WeiterfuehrenRechnungZuGutschrift', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort WeiterfuehrenRechnungZuGutschrift```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action></action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>4</id>
  </xml>
</response>

  
```

#### Stechuhrstatus abfragen

Der aktuelle Status eines Mitarbeiters an der Stechuhr kann mit der ID der Stechuhr und der AdressID des Mitarbeiters abgerufen werden.

##### Beispiel Anfrage StechuhrStatusGet

```
  <?php

$xml = '<id>1</id>
  <adresse>6</adresse>';

$output_xml = SendRequest('StechuhrstatusGet', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort StechuhrStatusGet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>StechuhrStatusGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <status>pausestart</status>
  <seit>0.08</seit>
  <dd>0</dd>
  <kommen>0</kommen>
  </xml>
</response>

  
```

#### Stechuhrstatus ändern

Der aktuelle Status eines Mitarbeiters an der Stechuhr kann mit dem neuen Status und der ID des Benutzers oder der Adresse des Mitarbeiters gesetzt werden. Welcher Status gesetzt werden kann, ist vom aktuellen Status abhängig:

- Wenn aktueller Status = 'gehen': Nur Status 'kommen' kann gesetzt werden
- Wenn aktueller Status = 'kommen': Nur Status 'gehen' oder 'pausestart' kann gesetzt werden
- Wenn aktueller Status = 'pausestart': Nur Status 'pausestop' kann gesetzt werden

##### Beispiel Anfrage StechuhrStatusSet

```
  <?php

$xml = '<cmd>pausestop</cmd>
  <adresse>6</adresse>';

$output_xml = SendRequest('StechuhrstatusSet', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort StechuhrStatusSet```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>StechuhrStatusSet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
</response>

  
```##### Beispiel Anfrage StechuhrSummary```
  <?php

$xml = '<adresse>6</adresse>';

$output_xml = SendRequest('StechuhrSummary', $xml);

echo "<pre>";
var_dump($output_xml);
echo "</pre>";

function SendRequest($methodname,$xml)
{
  $url = 'http://localhost/xentral/20.1/www/api/'.$methodname;

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_USERPWD, "apitest:password1234");
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, '<xml>'.$xml.'</xml>');
  curl_setopt($ch, CURLOPT_HTTPHEADER, ['content-type: application/xml']);
  $response = curl_exec($ch);
  curl_close($ch);

  return $response;
}

?>

  
```##### Beispiel Antwort StechuhrSummary```
  <?xml version="1.0" encoding="UTF-8"?>
<response>
  <status>
  <action>StechuhrStatusSet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <mitarbeiter_adresse type="documentary">6</mitarbeiter_adresse>
  <ZeitRequest>2019-11-25T10:17:01+01:00</ZeitRequest>
  <UrlaubSoll>0</UrlaubSoll>
  <UrlaubIst>0</UrlaubIst>
  <UeberstundenMonat>0.00</UeberstundenMonat>
  <UeberstundenGesamt>0.00</UeberstundenGesamt>
  <KW>1</KW>
  <Einzelauflistung>
  <Kalenderwoche>
  <KW>48</KW>
  <Arbeitstag>
  <Datum>25.11.2019</Datum>
  <ArbeitszeitSoll>0</ArbeitszeitSoll>
  <ArbeitszeitIst>0.25</ArbeitszeitIst>
  <ArbeitsEvents>
  <Event>
  <typ>kommen</typ>
  <zeit>08:00</zeit>
  </Event>
  <Event>
  <typ>pausestart</typ>
  <zeit>12:30</zeit>
  </Event>
  <Event>
  <typ>pausestop</typ>
  <zeit>13:30</zeit>
  </Event>
  <Event>
  <typ>gehen</typ>
  <zeit>17:00</zeit>
  </Event>
  </ArbeitsEvents>
  </Arbeitstag>
  <Arbeitstag>
  <Datum>26.11.2019</Datum>
  <ArbeitszeitSoll>0</ArbeitszeitSoll>
  <ArbeitszeitIst>0</ArbeitszeitIst>
  <ArbeitsEvents/>
  </Arbeitstag>
  [...]
  </Kalenderwoche>
  </Einzelauflistung>
  </xml>
</response>

  
```

### Aktueller Hinweis: Neue API Accounts ab Version 20.3

Ab Version 20.3 muss **jeder ** API Account auch mit Permissions versehen sein. Diese müssen**immer** eingestellt werden. Beim Update von Version 20.2 auf Version 20.3 ist der API Account aus den Grundeinstellungen in die API Accounts App übernommen worden.

Die API Accounts aus den Grundeinstellungen in das Modul API Accounts migriert. Hier benötigen Sie keine weiteren Anpassungen des Aufrufs.

Sollten Sie bereits einen API Account aus dem Modul API Account nutzen und den Aufruf ohne den Parameter der API-ID verwenden, nehmen Sie bitte folgende Anpassung vor:

Für diesen Aufruf (/www/index.php?module=api&action=AdresseGet&hash={hash}&id={address-id}) wird noch zusätzlich der Parameter &api_id={api_id} benötigt. Dabei ist "id" mit der ID der zu verwendenden API zu ersetzen, also z.B. "api_id=1" oder "api_id=2".

#### Umstellung des API-Aufrufs via Hash

##### Hintergrund

Es gibt verschiedene Möglichkeiten, die xentral-API anzusprechen. In der ersten Variante wurde folgender Aufruf verwendet:

URL.de/index.php?module=api&action=BenutzerList&hash=

Diese war auf den API-Account aus den Grundeinstellungen zugeschnitten, der nicht weiter über IDs oder Ähnliches unterschieden werden konnte.

Mit der Version 20.1 wurde dann das eigene Modul für API-Accounts implementiert und zusätzlich auch ein neuer Parameter “api_id” hinzugefügt, welcher in Kombination mit dem Hash sicherstellt, dass die Anfragen auch über den korrekten API-Account aufgerufen/abgehandelt werden. Wie der Parametername schon vermuten lässt, handelt es sich hier dann um die ID des API-Accounts.

Dieser Parameter wird seit der Version 20.3 als Pflichtangabe benötigt. Ohne diesen werden die Aufrufe mit der Fehlermeldung "wrong hash" begleitet.

#### Wie verwende ich diesen Parameter korrekt?

Hier ist die ID API-Account des Accounts mit zu übergeben. Derzeit kann die ID des Parameters nicht in der Oberfläche herausgelesen werden. Eine Änderung wird derzeit durch die Entwicklung vorbereitet.

#### Wie kann die ID des API-Accounts abgefragt werden?

##### Datenbank Ansicht

Modul "Datenbank Ansicht" öffnen via Supersearch oder über den Appstore. Tabelle "api_account" anwählen. In der Spalte “Bezeichnung” nach dem Namen/Bezeichnung des API-Accounts suchen. Links davon befindet sich die ID.

> **Anmerkung**
>
> Bei mehreren Einträgen kann es sein, dass die Ansicht nicht nur langsam oder nicht geöffnet wird. Hier dann auf Variante 2 umsteigen.

##### Bericht

Öffne Controlling → Berichte.

1. Neuen Bericht erstellen
1. Folgendes SQL angeben
  select id, bezeichnung from api_account where bezeichnung like '%Migration%' // Der Name hängt hier natürlich von der verwendeten Bezeichnung ab. Spalten erzeugen lassen

1. Unter "Ansicht" sich die entsprechende ID anzeigen lassen **Neues Beispiel anhand des Parameters:**

IhreURL/20.3/www/index.php?module=api&action=BenutzerListhash=b7a41dfcc80257710d799a7576f685f12f096624&api_id=26

Die Reihenfolge der Parameter spielt keine Rolle.

#### Alternative zum Hash-Aufruf

Nachdem der Hash-Aufruf auch nur für die API-Funktionen der Standard-API verwendet werden kann, besteht auch die Option über den Wrapper der REST-API zu gehen.

Die Umleitung wird hier beschrieben:[https://update.xentral.biz/apidoc/docs203.html#standard_api_aufrufe](https://update.xentral.biz/apidoc/docs203.html#standard_api_aufrufe)

Zusätzlich ändert sich dadurch aber auch die Methode zur Authentifizierung.[https://update.xentral.biz/apidoc/docs203.html#authentifizierung](https://update.xentral.biz/apidoc/docs203.html#authentifizierung)