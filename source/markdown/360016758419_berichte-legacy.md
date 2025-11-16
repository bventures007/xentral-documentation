In xentral können eigene Berichte mit Hilfe von SQL Statements angelegt und als PDF/CSV exportiert oder per FTP und E-Mail versendet werden.

Über App Center → Berichte (Legacy) können Berichte bearbeitet werden.

> **Anmerkung**
>
> Es handelt sich um ein Legacy-Modul, das nicht mehr von Xentral supportet oder weiterentwickelt wird. Um unseren Kunden die Arbeit mit der vorhandenen Funktionsweise weiterhin zu ermöglichen, ist es noch immer im Xentral App Store verfügbar.

## Einstellungen

Im Reiter "Einstellung" werden die benötigten Informationen für den Bericht eingetragen.

In den Feldern ist dabei Folgendes einzugeben:

- Name→ Der Name des Berichts, kann frei gewählt werden
- Projekt→ Projekt des Berichts kann optional angegeben werden
- Beschreibung→ Optionale Beschreibung zur Anzeige des Berichts
- Variablen→ Optionale Definition von Variablen, die dann im SQL-Statement dementsprechend ersetzt werden
- Struktur→ SQL-Statement, welches die Struktur des Berichts festlegtreport
- Spaltenname→ Bezeichnung der Spalten, in denen die Daten auftauchen (z.B. Datum, Kunde, Betrag)
- Spaltenbreite→ Optional kann die Spaltenbreite in Millimetern angegeben werden, die Gesamtbreite beträgt 190mm190mm
- Spaltenausrichtung→ Die Ausrichtung des Textes kann in allen Feldern der Spalte, R (rechtsbündig), L (linksbündig), oder C (zentriert), optional angegeben werdenoptionally
- Interne Bemerkung→ Eine interne Anmerkung kann optional erstellt werden, diese ist im Bericht nicht einzusehen

## Variablen

Es ist möglich, Variablen in Berichten zu deklarieren und diese im SQL-Statement zu nutzen.

Die entsprechende Syntax sieht dann so aus, das Semikolon muss am Ende eingefügt werden: {DATUMVON} = 2018-10-01; Im Bericht werden die Variablen folgendermaßen eingefügt:

![berichte_20.png](https://help.xentral.com/hc/article_attachments/5041750824092)

## FTP-Übertragung und E-Mail

Erstellte Berichte können über FTP übertragen sowie in regelmäßigen Abständen und zu bestimmten Zeitpunkten per E-Mail versendet werden.

Die Funktion muss aktiviert und alle Felder gefüllt werden:

- E-Mail Empfänger→ E-Mail-Adresse, an die der Bericht versendet werden soll
- E-Mail Betreffzeile→ Betreff, den die E-Mail haben soll
- Uhrzeit→ Uhrzeit, zu der die E-Mail verschickt werden soll
- Dateiname→ Name der Datei, die der Bericht ausgeben soll. Dabei muss die Endung des entsprechenden Dateityps angefügt werden, z.B..csv oder.txt

Damit das Verschicken der E-Mails funktioniert, muss der Prozessstarter "Berichte FTP Übertragungen" aktiv und korrekt konfiguriert sein. Die Einstellungen könnten folgendermaßen aussehen:

- Bezeichnung→ Als Bezeichnung ist "Berichte FTP Übertragung" einzugeben
- Art→ Aus dem Drop-Down-Menü ist als Art "periodisch" auszuwählen
- Wochentag→ Aus dem Drop-Down-Menü ist "Jeden Tag" auszuwählen
- Startzeit→ Es ist die vorgegebene Startzeit zu belassen
- Letzte Ausführung→ Es ist die vorgegebene Endzeit zu belassen
- Periode→ Als Periode ist 1 in min. anzugeben
- Typ→ Als Typ ist "Cronjob" aus dem Drop-Down-Menü auszuwählen
- Parameter→ Als Parameter ist "berichte_ftp_uebertragen" einzugeben
- Aktiv→ Durch Anhaken wird der Prozessstarter aktiviert

## Beispielberichte

### ZM

`SELECT belegnr, datum, name, kundennummer, land, ustid, SUM(soll) as sollFROM rechnungWHERE land!= '{LAND}' AND land IN ({EULAENDER}) AND status!= 'angelegt' AND ustid!= <em> AND datum >= '{DATUMVON}' AND datum <= '{DATUMBIS}'GROUP BY ustid</em>` Variablen: `{LAND} = DE;{DATUMVON} = 2019-01-01;{DATUMBIS} = 2019-12-31;{EULAENDER} = 'AT','BE','BG','CY','CZ','DE','DK','EE','ES','FI','FR','GB','GR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK';`

Spaltenname: Rechnung;Datum;Kunden;Kdnr;Land;USTID;Betrag

Spaltenbreite: 20;25;65;15;10;30;25

Spaltenausrichtung: L;L;L;L;L;L;L

> **Anmerkung**
>
> Soll bei Zahlen statt einem Punkt ein Komma stehen (bsp: 13,10 statt 13.10), muss die Struktur entsprechend geändert werden: FORMAT(soll,2,'de_DE'

### Verkaufte Artikel (Gerät) ins Ausland

SELECT lieferschein_position.nummer,lieferschein_position.bezeichnung,lieferschein.land,round(auftrag_position.preis,2),(auftrag_position.preis * lieferschein_position.menge),lieferschein.auftrag,DATE_FORMAT(lieferschein.datum,'%d.%m.%Y'),artikel.geraet,lieferschein_position.mengeFROM lieferschein_positionLEFT JOIN lieferschein ON lieferschein.id=lieferschein_position.lieferscheinLEFT JOIN artikel ON artikel.id=lieferschein_position.artikelLEFT JOIN auftrag_position ON auftrag_position.id=lieferschein_position.auftrag_position_idWHERE artikel.geraet=1 AND lieferschein.land!='DE'AND lieferschein.datum &gt;='2016-01-01' AND lieferschein.datum &lt; '2016-07-31'

Spaltennamen: Artikelnummer;Artikelbezeichnung;Land;AB Preis;AB;Datum;Gerät;Menge

Spaltenbreite: 20;50;10;20;20;20;20;20

Spaltenausrichtung: L;L;L;L;L;L;L;L

### Lieferschein mit Lieferadresse und Produkt

Über das SQL-Statement werden nachstehende Informationen aus dem Lieferschein gezogen:

- Lieferadresse des Kunden
- Alle Kunden, die ein bestimmtes Produkt bestellt haben (Artikel ID)
- Lieferscheine über einen bestimmten Datumsbereich

SELECT l.belegnr,l.datum,l.name,l.ansprechpartner,l.abteilung,l.unterabteilung,l.adresszusatz,l.land,l.strasse,l.plz,l.ort, a.name_de,a.nummer FROM lieferschein l LEFT JOIN lieferschein_position lp ON lp.lieferschein=l.id LEFT JOIN artikel a ON a.id=lp.artikel WHERE lp.artikel=212 AND l.datum&gt;='2017-08-01' AND l.datum &lt;='2017-12-31' ANDl.status='versendet'

### Lagerbestand frei verfügbare Artikel

SELECT a.nummer,a.name_de,TRIM(IFNULL((SELECT SUM(lpi.menge) FROM lager_platz_inhalt lpi WHERE lpi.artikel=a.id),0)-IFNULL((SELECT SUM(ap.menge) FROM auftrag_position ap LEFT JOIN auftrag auf ON auf.id=ap.auftrag WHERE ap.artikel=a.id AND (auf.status='freigegeben' OR auf.status='versendet')),0))+0 FROM artikel a WHERE a.geloescht!=1

### Alle Artikel mit Fremdnummern

`SELECT artikel.nummer, artikel.name_de, artikelnummer_fremdnummern.nummer as fremdnummer, artikelnummer_fremdnummern.bezeichnung FROM artikelnummer_fremdnummern LEFT JOIN artikel ON artikel.id=artikelnummer_fremdnummern.artikel`

### Alle Kunden mit letztem Bestelldatum

SELECT MAX(datum), name, kundennummer FROM auftrag WHERE status!='angelegt' AND datum &gt;='2018-01-01' AND datum&lt;'2018-04-01' GROUP by adresse

### Mit Ausgabe Projekt und Projekt

IDSELECT MAX(a.datum), a.name, a.kundennummer, p.abkuerzung FROM auftrag a LEFT JOIN projekt p ON p.id=a.projekt WHERE a.status!='angelegt' AND a.datum &gt;='2018-01-01' AND a.projekt='1' AND a.datum&lt;'2018-04-01' GROUP by a.adresse

### Rechnung mit manueller Zahlungsfestsetzung

Folgende Angaben sind zu verwenden:

- Info: liefert alle Rechnungen als Bericht, die den Haken "Alle Einstellungen manuell festsetzen" gesetzt haben.
- "als.csv anzeigen" verwenden

Struktur: SELECT r.belegnr,r.datum,r.name FROM rechnung r WHERE r.mahnwesenfestsetzen='1'