Über individuelle Berichte können Datenexporte und auch der regelmäßige Transfer der Daten in andere Systeme oder per E-Mail realisiert werden. SQL-Berichte ermöglichen die Auswertung sämtlicher verfügbarer Daten in jeder erdenklichen Form und sind ein mächtiges Werkzeug zur Analyse und Bereitstellung von Daten zur weiteren Analyse in Business Intelligence Tools (BI-Systeme).

Beginnend mit der Version 20.1 werden viele zusätzliche Report Scripts zur Verfügung stehen und das Modul weitere Funktionen beinhalten, die das Erstellen und Nutzen von Report Scripts zu einer einfachen Aufgabe werden lassen.

Berichte lassen sich auf vielfältige Weise teilen:

- Einfache Freigabe für andere Benutzer im Berichte-Dashboard
- Integration in der Software als Tabelle in einem zusätzlichen Tab (Register)
- Integration in den Aktionsmenüs der Belege als Download
- Regelmäßiger Versand per E-Mail
- Regelmäßiges Übertragen per FTP
- Bereitstellen per URL, auch für einen eingeschränkten Zeitraum
- Freigabe zum Zugriff per API

xentral bringt ab der Version 20.1 bereits eine große Zahl von Berichten mit und diese werden weiter ausgebaut. So werden zukünftig mit den meisten Modulen bereits einige Auswertungen mitgeliefert, die leicht durch eigene Reports ergänzt werden können. Der Austausch von Report Scripts ist durch Berichtsvorlagen möglich - Dateien in denen die Definitionen für Berichte schnell gespeichert und an anderer Stelle geladen werden können.

## Datenbank-Struktur

Die Datenbanktabellen sind hauptsächlich in deutscher Sprache benannt. Die Benennung folgt üblichen Standards und bietet daher einen schnellen Einstieg.

### Kurzer Blick auf die Tabellen

Den schnellsten Weg zur Orientierung in der Datenbank befindet sich in der xentral Custom Suite im Register SQL Viewer. Dort kann eine rascher Blick auf alle Tabellen des Systems geworfen werden. Aus Performance-Gründen sind manche Tabellen in der Sicht auf Spalten oder Zeilen eingeschränkt. Alle Details befinden sich im Artikel zur XCS (Xentral Customizing Suite).

![Report-Script-1.png](https://help.xentral.com/hc/article_attachments/4996407578524)

Die Abbildung zeigt einen Screenshot aus der xentral Customizing Suite mit der Tabelle adresse_rolle.

### Gesamtübersicht

Unabhängig von der xentral-Installation kann die eigene Datenbank jederzeit über das Backup-Tool als Datenbank-Snapshot heruntergeladen und auf einem lokalen Rechner angesehen werden. So können auch SQL-Statements für Reports Scripts (Berichte) erstellt und getestet werden. Dazu empfiehlt sich folgende Vorgehensweise: Das Backup der xentral Datenbank ist auf den lokalen Rechner zu laden. Dazu ist die Funktion "DB-Snapshot erstellen" zu verwenden und den Punkten 1. und 2. der Seite Datenbank Backup Erstellen zu folgen. Die heruntergeladene Datei kann dann z.B. in einer XAMPP-Umgebung in den dort vorhandene Datenbankserver geladen und SQL-Statements ausprobiert werden. XAMPP ist eine vollständig kostenlose, leicht zu installierende Apache-Distribution, die MariaDB, PHP und Perl enthält. Das XAMPP Open-Source-Paket wurde für eine extrem einfache Installation und Nutzung eingerichtet. XAMPP ist für Windows, Linus und MacOS in 15 Sprachen verfügbar und bietet eine einfache Komplettinstallation eines lauffähigen Webservers mit Datenbankserver und den notwendigsten Tools (wie z.B. PHP und phpMyAdmin). Darüber hinaus sind zu XAMP viele Anleitungen und Community Support online verfügbar.

### Datenbank-Tabellen

#### Belege

- auftrag
- auftrag_position
- rechnung
- rechnung_position
- lieferschein
- lieferschein_position
- gutschrift
- gutschrift_position

#### Adressen

- adresse
- ansprechpartner
- lieferadressen

#### Artikel

- artikel
- einkaufspreise
- verkaufspreise

#### Lager

- lager
- lager_platz
- lager_platz_inhalt

### DB-Diagramm

![Report-Script-2.png](https://help.xentral.com/hc/article_attachments/4996407627420)

Die wichtigsten Tabellen aus dem xentral Datenbank-Schema befindet sich unter[DB-Diagram.io](https://dbdiagram.io/embed/5da80fb302e6e93440f25074). Diese Struktur wird zukünftig auf alle Datenbanktabellen erweitert.

## Beispiele

### ZM (Zusammenfassende Meldung)

#### Variablen

{LAND} = DE; {DATUMVON} = 2019-01-01; {DATUMBIS} = 2019-12-31; {EULAENDER} = 'AT','BE','BG','CY','CZ','DE','DK','EE','ES','FI','FR','GB','GR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK';

#### SQL Statement

SELECT belegnr, datum, name, kundennummer, land, ustid, SUM(soll) as soll FROM rechnung WHERE land!= '{LAND}' AND land IN ({EULAENDER}) AND status!= 'angelegt' AND ustid!= '' AND datum >= '{DATUMVON}' AND datum <= '{DATUMBIS}' GROUP BY ustid

#### Spalten

Spaltennamen: Rechnung;Datum;Kdnr;Kunden;Land;USTID;Betrag Spaltenbreiten: 20;25;65;10;15;30;25 Spaltenausrichtung: L;L;L;L;L;L;R Hinweis: Sollen bei den Zahlen statt einem Punkt eher ein Komma verwendet werden (bsp: 13,10 statt 13.10), dann müsste die Struktur entsprechend geändert werden und in Zeile 1 des SQL-Statements das Wort "soll" z.B. ersetzt werden durch: FORMAT(soll,2,'de_DE') AS betrag

### Umsatz-Statistik

#### Variablen

{DATUMVON} = 2019-01-01; {DATUMBIS} = 2019-12-31; {PROJEKT} = STANDARD;

#### SQL Statement

SELECT p.abkuerzung, ap.bezeichnung, COUNT(ap.auftrag), FORMAT(SUM(ap.umsatz_netto_gesamt),2,'de_DE'), FORMAT(SUM(ap.umsatz_brutto_gesamt),2,'de_DE') FROM auftrag_position ap LEFT JOIN projekt p ON ap.projekt = p.id LEFT JOIN auftrag au ON ap.auftrag = au.id WHERE au.datum >= '{DATUMVON}' AND au.datum <= '{DATUMBIS}' AND p.abkuerzung = '{PROJEKT}' GROUP BY ap.projekt, ap.artikel

#### Spalten

Spaltennamen: Projekt;Artikel;Anzahl Kunden/Aufträge;Umsatz netto;Umsatz brutto Spaltenbreiten: 20;30;15;15;15 Spaltenausrichtung: L;L;R;R;R

## Helpful: SQL- / Felddefinitionen

### Eingangskanal für Aufträge

Um die Herkunft von Aufträgen in SQL-Statements einzugrenzen kann das Feld shop ausgewertet werden. Es beinhaltet die id aus der Tabelle shopexport.

- shop = 0 bedeutet: Der Auftrag wurde manuell angelegt oder über Belegimporter, API oder das Übertragungsmodul in das System importiert
- shop > 0 gibt die Shop Id (den Kanal) an aus der Tabelle shopexport an Alle importierten Aufträge werden mitgeloggt in der Tabelle shopimport_auftraege.

## Weitere Beispiele

Weitere Beispiele befinden sich unter DB-Berichte im Anwender-Handbuch. Beginnend mit der Version 20.1 finden sich im Berichte-Modul viele Vorlagen für Berichte, die einfach verwendet oder durch kopieren auch rasch an die persönlichen Vorstellungen angepasst werden können.