Im Folgenden wird die Datenstruktur für den Warenkorb im Shopskeleton gezeigt.

## Rechnungsadresse

Hier können Angaben zu der Rechnungsadresse gemacht werden:

- $warenkorb[name] = "Musterfirma AG"; /*Bei Privatperson direkt Name der Person - Ansprechpartner bleibt dann leer*/
- $warenkorb[anrede]="firma"; /*herr, frau oder firma*/
- $warenkorb[ansprechpartner] = "Max Mustermann";
- $warenkorb[abteilung] = "Abteilung Entwicklung;
- $warenkorb[abteilung] = "Abteilung Entwicklung;
- $warenkorb[plz] = "12345";
- $warenkorb[ort] = "Musterdorf;
- $warenkorb[land] = "DE"; /*2-stellig ISO*/
- $warenkorb[email] = "email@email.de";

## Auftragsinformationen

Hier können Angaben zu den Auftragsinformationen gemacht werden:

- $warenkorb[bestelldatum] = "2012-12-01"; /*Datum der Bestellung*/
- $warenkorb[gesamtsumme] = 10.99; /*Endsumme die gezahlt wird*/
- $warenkorb[transaktionsnummer] = 192939; /*z.B. Paypal, iPayment oder Billsafe Transaktionsnummer*/
- $warenkorb[onlinebestellnummer] = 123456; /*Interne Shop Bestellnummer (Wichtig z.B. bei Vorkassen)*/
- $warenkorb[versandkostennetto] = "3.31";
- $warenkorb[versandkostenbrutto] = "3.95";
- $warenkorb[freitext] = "Freitext auf Belegen wie Auftrag, Rechnung und Lieferschein";

## Steuer Informationen

Hier können Angaben zu den Steuerinformationen gemacht werden:

- $warenkorb[steuerfrei] = 0; /*oder 1 wenn steuerfrei*/
- $warenkorb['vorabbezahltmarkieren']=1; /*Falls kein Zahlungseingang von Xentral aus gemacht wird*/

## Lieferung

Hier können Angaben zu der Lieferung gemacht werden:

- $warenkorb['lieferdatum']="2012-12-24"; /*Wunsch Lieferdatum des Kunden*/
- $warenkorb[lieferung] = "versandunternehmen"; /*bzw. selbstabholer oder gezielt dpd oder dhl*/

## Abweichende Lieferadresse

Diese Angaben sind auszufüllen, wenn eine andere Lieferadresse vorhanden ist.

- $warenkorb2[lieferadresse_name] = "";
- $warenkorb2[lieferadresse_ansprechpartner] = "";
- $warenkorb2[lieferadresse_strasse] = "";
- $warenkorb2[lieferadresse_plz] = "";
- $warenkorb2[lieferadresse_ort] = "";
- $warenkorb2[lieferadresse_land] = "";
- $warenkorb2[lieferadresse_abteilung] = "";

## Artikel Liste

Hier können eliebig viele Positionen gebucht werden:

$articlearray[] = array( 'articleid'=>'12345', /*Artikelnummer aus Xentral / 'name'=>'Name des Artikels', / Name des Artikels der im Auftrag, Rechnung und Lieferschein auftaucht. / 'price'=>'41.97', / Netto Preis des Artikels / 'quantity'=>1 / Menge des Artikels*/);

Das Array ist am Schluss zuzuweisen:

$warenkorb[articlelist]=$articlearray;

## Zahlungsweisen

Die jeweiligen Zahlungsweisen müssen korrekt gemapped werden:

$warenkorb[zahlungsweise] = "bar"; $warenkorb[zahlungsweise] = "rechnung"; $warenkorb[zahlungsweise] = "vorkasse"; $warenkorb[zahlungsweise] = "kreditkarte"; $warenkorb[zahlungsweise] = "lastschrift"; $warenkorb[zahlungsweise] = "paypal"; $warenkorb[zahlungsweise] = "nachnahme"; $warenkorb[zahlungsweise] = "Amazoncba"; $warenkorb[zahlungsweise] = "sofortueberweisung"; $warenkorb[zahlungsweise] = "billsafe"; $warenkorb[zahlungsweise] = "unbekannt";

## Funktionen

====Artikel übertragen====

===Staffelpreise===

[1] => Array ( [ab_menge] => 10.0000 [preis] => 1.00000000 [bruttopreis] => 1.19 [waehrung] => EUR))