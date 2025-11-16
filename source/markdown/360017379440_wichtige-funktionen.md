## Secure: Kommunikation über GET und POST

### Zugriff per GetPOST()

Holt den Value über POST aus einem Formular. Innerhalb () den Namen des Formularelementes angeben z.B.

$name = $this->app->Secure->GetPOST('name');

### Zugriff per GetGET()

Holt den Value über GET aus der URL. Innerhalb () den Namen der Variable aus der URL angeben z.B.

$id = $this->app->Secure->GetGET('id');

## DB: Zugriff auf die Datenbank

Wird verwendet um mit den Daten aus der Datenbank zu arbeiten. Für Module in Xentral sollten nur diese Funktionen verwendet werden.

### Zugriff per Update()

Innerhalb der Klammern das SQL Update-Statement zur Ausführung angeben z.B.

$id = $this->app->Secure->GetGET('id'); $this->app->DB->Update("UPDATE adresse SET name ='Mayer Antonia' WHERE id = "$id"");

### Ergebnis mit einem Wert mit Select()

Innerhalb der Klammern das SQL Abfrage-Statement zur Ausführung angeben z.B.

$id = 4; $name = $this->app->DB->Select("SELECT name FROM adresse WHERE id = "$id"");

### Ergebnis mit mehreren Werten mit SelectArr()

Wird verwendet, wenn man Werte aus mehreren Spalten der Datenbank möchte. Die Rückgabe wird in einem Array mit assoziativen Indizes gespeichert z.B.

$personendaten = $this->app->DB->SelectArr("SELECT name, strasse, ort, plz, land FROM adresse WHERE id = 5");

### Einfügen per Insert()

Innerhalb der Klammern das SQL Einfügen-Statement zur Ausführung angeben z.B.

$this->app->DB->Insert("INSERT INTO adresse (name, strasse, ort, plz, land) VALUES ('Klein Christian', 'Musterstrasse 10', 'Musterort', '12345', 'DE')");

### Löschen per Delete()

Innerhalb der Klammern das SQL Lösch-Statement zur Ausführung angeben z.B.

$this->app->DB->Delete("DELETE FROM adresse WHERE id = 10");

### Zuletzt vergebene ID per GetInsertID()

Gibt die zuletzt in die Datenbank eingefügte ID zurück, z.B.

$adressid = $this->app->DB->GetInsertID();

## Tpl: Das Templatesystem

Wird verwendet um mit dem Template zu arbeiten.

### Werte einfügen / ersetzen mit Set()

Fügt dem Templatefeldbereich einen neuen String hinzu. Achtung: Set() überschreibt den Inhalt des bisherigen Templatefeldbereichs. Der erste Parameter steht für den beliebig benennbaren Templatefeldbereich (immer großgeschrieben!) und der zweite Parameter ist der String der diesen Templatefeldbereich überschreiben soll. Beispiel:

$this->app->Tpl->Set("VORNAME", "Marie");

### Werte einfügen mit Add()

Fügt dem Templatefeldbereich einen neuen String hinzu. Erster Parameter ist der beliebig benennbare Feldbereich des Templates, zweiter Parameter der String der eingefügt werden soll, wie z.B.

$this->app->Tpl->Add("TABELLE", "VornameNachname");

### Template Datei auswählen mit Parse()

Sorgt dafür, dass die in () angegebene Template Datei zur Darstellung des HTML Codes verwendet wird. Beispiel:

$this->app->Tpl->Parse("PAGE","beispielmodul_list.tpl");

## erp: Die Kernbibliothek für ERP Funktionen

Diese Funktionen sind in der Datei class.erpapi.php zu finden.

### Neuen Menüpunkt hinzufügen

Fügt einen neuen Menüpunkt der Navigation hinzu. Der erste Parameter ist der Link des Moduls in dem der neue Menüpunkt hinzugefügt werden soll. Parameter 2 ist die Beschriftung des Menüpunktes. Beispiel:

$this->app->erp->MenuEintrag("index.php?module=modulname&action=list","Übersicht");

### Tabellen vorhanden / anlegen mit CheckTable()

Prüft, ob die Tabelle in der Datenbank vorhanden ist. Wenn sie nicht vorhanden ist, wird sie neu angelegt. Beispiel: $this->app->erp->CheckTable("adresse");

### Spalten vorhanden / anlegen mit CheckColumn()

Prüft, ob in der angegebenen Tabelle die Spalte vorhanden ist. Wenn sie nicht vorhanden ist, wird sie neu angelegt. Bedeutung der Parameter CheckColumn(Spaltenname, Datentyp, Tabellenname, Default Wert). Beispiel: $this->app->erp->CheckColumn("id", "int(10)", "adresse", "NOT NULL AUTO_INCREMENT");

### Einkaufspreis hinzufügen mit AddEinkaufspreis()

Fügt dem angegebenen Artikel einen neuen Einkaufspreis hinzu. Bedeutung der Parameter AddEinkaufspreis(ArtikelID, AbMenge, IDLieferant, Bestellnr, NameLieferant, Einkaufspreis). Beispiel: $this->app->erp->AddEinkaufspreis(23, 1, 57, "14456", "Joghurt und Eis GmbH", 1.80);

### Verkaufspreis hinzufügen mit AddVerkaufspreis()

Fügt dem angegebenen Artikel einen neuen Verkaufspreis hinzu. Bedeutung der Parameter AddVerkaufspreis(ArtikelID, AbMenge, AdressID für welche Gruppe der Preis gilt, Verkaufspreis). 0 als dritter Parameter bedeutet, dass dieser Verkaufspreis für alle gilt, also für keine bestimmte Gruppe. Beispiel: $this->app->erp->AddVerkaufspreis(23, 1, 0, 2.00);

### Artikel anlegen / aktualisieren mit InsertUpdateArtikel()

Fügt einen neuen Artikel hinzu, bzw. aktualisiert einen bestehenden Artikel. Parameter muss ein Array sein. Falls der Artikel aktualisiert werden soll, muss die ID übergeben werden, sonst wird der Artikel neu erstellt. Die Indizes des Arrays müssen wie die Spalten der Tabelle artikel heißen. Beispiel: $artikeldaten = array(); $artikeldaten['name_de'] = "Apfel"; $artikeldaten['anabregs_text'] = "Ein roter Apfel"; $artikeldaten['hersteller'] = "Apfelfarm";

$this->app->erp->InsertUpdateArtikel($artikeldaten);

### Adresse anlegen / aktualisieren mit InsertUpdateAdresse()

Fügt eine neue Adresse hinzu, bzw. aktualisiert eine bestehende Adresse. Parameter muss ein Array sein. Falls die Adresse aktualisiert werden soll, muss die ID und - je nachdem welche Rolle die Adresse hat - die Mitarbeiter-, oder Kunden-, oder Lieferantennummer angegeben werden, sonst wird die Adresse neu erstellt. Die Indizes des Arrays müssen wie die Spalten der Tabelle adresse heißen. Beispiel: $adressdaten = array(); $adressdaten['name'] = "Max Mustermann"; $adressdaten['strasse'] = "Musterstraße 1"; $adressdaten['plz'] = "00000"; $adressdaten['ort'] = "Musterort"; $adressdaten['land'] = "DE";

$this->app->erp->InsertUpdateAdresse($adressdaten);

### Rollen vergeben mit AddRolleZuAdresse()

Fügt eine Rolle zu einer bereits vorhandenen Adresse hinzu. Es gibt die Rollen Mitarbeiter, Kunde und Lieferant. Die Rollen kann man bestimmten Objekten zuordnen, wie zum Beispiel "Projekt" oder "Gruppe". Bedeutung der Parameter AddRolleZuAdresse(AdressID, Rolle, optional Prädikat, optional Objekt, optional ParameterID). Soll die Rolle allgemein gültig sein, können nur die ersten beiden Parameter verwendet werden, falls Sie bestimmten Objekten zugeordnet werden sollen, muss der letzte Parameter mit der jeweiligen Projekt- oder GruppenID befüllt werden. In folgendem Beispiel wird einer Adresse die Rolle Kunde für ein bestimmtes Projekt hinzugefügt. Beispiel: $this->app->erp->AddRolleZuAdresse(145, "Kunde", "von", "Projekt", 2);

### Freie Artikelnummer ermitteln mit GetNextArtikelnummer()

Gibt die nächste freie Artikelnummer aus dem Nummernkreis zurück. Beispiel: $freieartikelnr = $this->app->erp->GetNextArtikelnummer();

### Freie Kundennummer ermitteln mit GetNextKundennummer()

Gibt die nächste freie Kundennummer aus dem Nummernkreis zurück. Beispiel: $freiekundennr = $this->app->erp->GetNextKundennummer();

### Freie Lieferantennummer ermitteln mit GetNextLieferantennummer()

Gibt die nächste freie Lieferantennummer aus dem Nummernkreis zurück. Beispiel: $freielieferantennr = $this->app->erp->GetNextLieferantennummer();

### Freie Mitarbeiternummer ermitteln mit GetNextMitarbeiternummer()

Gibt die nächste freie Mitarbeiternummer aus dem Nummernkreis zurück. Beispiel: $freiemitarbeiternr = $this->app->erp->GetNextMitarbeiternummer();

### Angebot anlegen mit CreateAngebot()

Erstellt ein neues Angebot für die in () angegebene AdressID. Gibt die ID vom erstellten Angebot zurück. Beispiel: $angebotid = $this->app->erp->CreateAngebot(22);

### Auftrag anlegen mit CreateAuftrag()

Erstellt einen neuen Auftrag für die in () angegebene AdressID. Gibt die ID vom erstellten Auftrag zurück. Beispiel: $auftragid = $this->app->erp->CreateAuftrag(34);

### Lieferschein anlegen mit CreateLieferschein()

Erstellt einen neuen Lieferschein für die in () angegebene AdressID. Gibt die ID vom erstellten Lieferschein zurück. Beispiel: $lieferscheinid = $this->app->erp->CreateLieferschein(12);

### Rechnung anlegen mit CreateRechnung()

Erstellt eine neue Rechnung für die in () angegebene AdressID. Gibt die ID von der erstellten Rechnung zurück. Beispiel: $rechnungid = $this->app->erp->CreateRechnung(23);

### Ländernamen mit ISO erhalten per GetSelectLaenderliste()

Gibt ein Array gefüllt mit Ländernamen und deren zweistelligen ISO-Code zurück. Ist der Parameter auf true, ist der Key vom Array die Landesbezeichnung und der Value der ISO-Code. Bei false ist es genau andersherum. Beispiel: $laender = $this->app->erp->GetSelectLaenderliste(true);

### Englische Ländernamen mit ISO erhalten per GetSelectLaenderlisteEN()

Gibt ein Array gefüllt mit englischen Ländernamen und deren zweistelligen ISO-Code zurück. Ist der Parameter auf true, ist der Key vom Array die englische Landesbezeichnung und der Value der ISO-Code. Bei false ist es genau andersherum. Beispiel: $laenderEN = $this->app->erp->GetSelectLaenderlisteEN(false);

## YUI: Für jQuery und Javascript Widgets

Diese Funktionen sind in der Datei class.yui.php zu finden.

### LiveTabelle wählen mit TableSearch()

Bestimmt, welches Template zur Darstellung der LiveTabelle verwendet wird. Der erste Parameter gibt an, in welchem Templatefeldbereich die LiveTabelle angezeigt werden soll. Der zweite Parameter gibt an, welche LiveTabelle verwendet werden soll. Beispiel: $this->app->YUI->TableSearch('TAB1','beispielmodul_list', "show","","",basename(FILE), CLASS);

### Vorauswahl für Textfelder per AutoComplete()

Erzeugt während dem Tippen eine Vorauswahl passender Einträge. Bereits vorhandene Vorauswahlen sind in der Datei ajax.php in der Funktion AjaxFilter() zu finden. Bedeutung der Parameter AutoComplete(TextfeldID, Filter, Nur_Nummer). Nur_Nummer kann weggelassen werden oder auf 1 stehen. Ist der Parameter auf 1 gesetzt, wird nur die Nummer ins Textfeld eingefügt, statt Nummer und Bezeichnung. Beispiel: $this->app->YUI->AutoComplete("auswahlartikel", "artikelnummer", 1);

### DatePicker erstellen mit DatePicker()

Erzeugt bei Klick in das in () angegebene Textfeld einen kleinen Kalender bei dem man das gewünschte Datum anklicken kann. Die grafische Oberfläche können Sie hier unter Widgets sehen. Beispiel: $this->app->YUI->DatePicker("datum_von");

### TimePicker erstellen mit TimePicker()

Erzeugt bei Klick in das in () angegebene Textfeld ein Fenster mit zwei Schiebern zur Zeitauswahl. Die grafische Oberfläche können Sie hier unter Widgets sehen. Beispiel: $this->app->YUI->TimePicker("zeit_von");

### Erweiterte Textarea mit CkEditor()

Fügt einer normalen HTML Textarea einige Formatierungsmöglichkeiten über Buttons hinzu. Als erster Parameter muss die Id des Textarea eingetragen werden. Der zweite Parameter ist die Art der Formatierungsmöglichkeiten, wie basic, belege oder all. Die verschiedenen grafischen Oberflächen können Sie hier unter Widgets sehen. Beispiel: $this->app->YUI->CkEditor("textarea", "basic");

## Benachrichtigungen

$this->app->erp->InternesEvent($this->app->User->GetID(),"text","typ",1);

1. Parameter ist die BenutzerID, muss vorhanden sein
1. Parameter ist der Text den man ausgeben möchte
1. Parameter ist der Typ der Nachricht (siehe Auflistung unten)
1. Parameter ob die Benachrichtigung mit Sound oder ohne Sound erscheinen soll

### Gültige Typen für die Nachricht

- default
- notice
- success
- warning
- error
- push

## Eigene Quelltexte / Änderungen in Update-Server hinterlegen

Viele PHP Dateien können mit eigenen Dateien überladen werden. Dazu kopiert man den Rumpf einer originalen Datei z.B. class.rechnung.php und nennt diese class.rechnung_custom.php. In dieser Datei muss es die Klasse mit dem Anhang Custom geben. z.B. Class RechnungCustom Extends Rechnung Jetzt können die Methoden in der Datei einzeln überladen werden. Die neue Datei class.rechnung_custom.php wird vom Update-Server nicht überschrieben. Sie können auf Anfrage einen FTP Account für den Update-Server erhalten, so werden zu den normalen Updates die eigenen Anpassungen automatisch mit übertragen. Dateien, die mit der Open Source-Version identisch sind, werden unverschlüsselt ausgeliefert.

### Überladbare Dateien

- Module aus www/pages
- Dokumente aus lib/dokumente
- class.erpapi.php → class.erpapi_custom.php
- class.printer.php → class.printer_custom.php

### Quelltext Dateien

Den allgemeinen Quelltext finden Sie in der.src.php Datei Beispiel class.erpapi_custom.php

### Beispiel class.remote_custom.php

## Bilderimport

Informationen zum Bilderimport findest du[in diesem Artikel](https://help.xentral.com/hc/articles/360017437599#UUID-aa9aeb9e-d458-f09b-7ea0-3917fc547eb7).