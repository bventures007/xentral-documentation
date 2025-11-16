## Inhaltsverzeichnis

- Passwort zurücksetzen
- SQL Statements
  - Artikel Update
- Daten löschen / zurücksetzen
  - Stammdaten
  - Belege
  - Buchhaltung
  - Lager & Logistik
  - Produktion
  - Alle offenen Einträge im Versandzentrum löschen
  - Allen Adressen eine fortlaufende Kundennummer vergeben und Rolle von Projekt ID=1 setzen
  - Bei Kundennummern die letzten 4 Nullen abschneiden
  - Aufträge stornieren (Statusumstellung)
  - Reservierungen löschen, wenn Auftrag nicht mehr in Datenbank

# Passwort zurücksetzen **Kurz:** UPDATE user SET passwordmd5=MD5('passwort'),passwordhash='',activ=1,fehllogins=0,password='',salt='',passwordsha512='' WHERE username='admin2';

Bzw. manuell:

1. Es ist sich in die Datenbank einzuloggen
1. In der Tabelle ist auf "USER" zu gehen
1. Der Benutzer ist anzuklicken, das neue Passwort in das Feld "passwordmd5" zu setzen und das Select Feld auf "MD5" einzustellen
1. Der Inhalt aus den Feldern 'passwordsha512' und 'salt' ist herauszulöschen
1. Die Fehllogins "fehllogins" sind auf 0 zu setzten
1. Speichern

# SQL Statements

## Artikel Update

Das Updatestatement ist über alle Artikel auszuführen und dort den Haken "Lagersync" im Artikel zu setzen:

- für alle Artikel, die einem oder mehreren Online-Shops zugeordnet sind
  Update artikel SET autolagerlampe=1 WHERE shop>0 OR shop2 > 0 OR shop3 > 0

# Daten löschen / zurücksetzen

Nach dem Testlauf oder einem Datenimport können Daten und Verknüpfungen über die Datenbank wieder gelöscht werden:

## Stammdaten **Artikel:** delete FROM `artikel` WHERE 1; delete FROM einkaufspreise; delete FROM verkaufspreise; delete FROM lager_platz_inhalt; delete FROM stueckliste;

## Belege **Angebot: ** delete FROM angebot; delete FROM angebot_position; delete FROM angebot_protokoll;** Auftrag: ** delete FROM auftrag; delete FROM auftrag_position; delete FROM auftrag_protokoll;** Lieferschein: ** delete FROM lieferschein; delete FROM lieferschein_position; delete FROM lieferschein_protokoll;** Rechnung: ** delete FROM rechnung; delete FROM rechnung_position; delete FROM rechnung_protokoll;** Bestellung:** delete FROM bestellung; delete FROM bestellung_position; delete FROM bestellung_protokoll;

## Buchhaltung **Geschäftskonten: ** delete FROM konten;** Kontoauszüge / Zahlungseingang:** delete FROM kontoauszuege; delete FROM kontoauszuege_zahlungseingang; delete FROM kontoauszuege_zahlungsausgang;

## Lager & Logistik **Lager: ** delete FROM lager_platz_inhalt; delete FROM lager_bewegung; delete fROM lager_charge;** Versandzentrum: ** delete FROM versand;** Inventur:** delete FROM inventur; delete FROM inventur_position; delete FROM inventur_protokoll;

## Produktion

delete FROM produktion; delete FROM produktionkorrektur; delete FROM produktionslager; delete FROM produktion_arbeitsanweisung; delete FROM produktion_arbeitsanweisung_batch; delete FROM produktion_baugruppen; delete FROM produktion_baugruppen_charge; delete FROM produktion_charge; delete FROM produktion_etiketten; delete FROM produktion_funktionsprotokoll; delete FROM produktion_funktionsprotokoll_position; delete FROM produktion_position; delete FROM produktion_protokoll; delete FROM produktion_unterseriennummern;

### Alle offenen Einträge im Versandzentrum löschen

DELETE v FROM versand AS v LEFT JOIN lieferschein AS l ON v.lieferschein=l.id LEFT JOIN kommissionierung AS k ON l.kommissionierung = k.id LEFT JOIN projekt AS p ON p.id=v.projekt WHERE v.abgeschlossen!='1' AND (tracking <> '' OR weitererlieferschein <> 1) AND v.cronjob = 0

AND l.status!='storniert' AND tracking = ''

AND (IFNULL(p.multiorderpicking,0) = 0 OR IFNULL(k.abgeschlossen,0) = 1)

### Allen Adressen eine fortlaufende Kundennummer vergeben und Rolle von Projekt ID=1 setzen

- Die 400000 bitte ersetzen durch die nächste zu vergebende Kundennummer
- Die Rolle "Kunde" wird auf das Projekt ID=1 vergeben (wäre z.B. Projekt "STANDARD")

(Vorher ist eine Sicherung der aktuellen DB machen)

Alle Adressen erhalten eine Kundennummer und eine Zuweisung der Rolle "Kunde" auf das Projekt mit ID "1". SET @zaehler:= 400000;

UPDATE adresse SET kundennummer = @zaehler:= @zaehler + 1 WHERE kundennummer = '' OR isnull(kundennummer);

INSERT INTO adresse_rolle (objekt,adresse, subjekt, praedikat, projekt, parameter, von, bis) SELECT 'Projekt' as objekt, a.id as adresse, 'Kunde' as subjekt, 'von' as praedikat,'1' as projekt,'1' as parameter, curdate() as von, '0000-00-00' as bis FROM adresse a LEFT JOIN `adresse_rolle` ar ON ar.adresse = a.id AND ar.subjekt LIKE 'Kunde' WHERE isnull(ar.id) AND a.kundennummer <> '';

insert into objekt_protokoll ( objektid,objekt, action_long, meldung, bearbeiter, zeitstempel) Select a.id as objektid,'adresse' as objekt, 'adresse_next_kundennummer', concat('Kundennummer erhalten: ',a.kundennummer) as meldung,'' as bearbeiter,now() as zeitstempel FROM adresse a LEFT JOIN objekt_protokoll op ON op.objektid = a.id AND op.objekt = 'adresse' AND op.action_long = 'adresse_next_kundennummer' WHERE a.kundennummer <> '' AND isnull(op.id);

- Im Anschluss ist in den Grundeinstellungen im Reiter "Nummernkreis" die nächste zu vergebende Kundennummer einzutragen und zu speichern

### Bei Kundennummern die letzten 4 Nullen abschneiden

- alle 10-stelligen (Kunden- und Lieferantennummern)
- die an den letzten 4 Stellen eine Null haben
- diese (Kunden- und Lieferantennummern) auf 6 Stellen kürzen

UPDATE adresse SET kundennummer=LEFT(kundennummer,6) WHERE kundennummer IS LIKE '%0000' AND LENGTH(kundennummer)=10; UPDATE adresse SET lieferantennummer=LEFT(lieferantennummer,6) WHERE lieferantennummer IS LIKE '%0000' AND LENGTH(kundennummer)=10;

### Aufträge stornieren (Statusumstellung)

UPDATE auftrag SET status='storniert' WHERE belegnr >=200077 AND belegnr<=200099 AND status='freigegeben'

### Reservierungen löschen, wenn Auftrag nicht mehr in Datenbank

DELETE l FROM lager_reservierung l LEFT JOIN auftrag a ON l.parameter = a.id AND l.objekt = 'auftrag' WHERE ISNULL(a.id) AND l.objekt = 'auftrag'