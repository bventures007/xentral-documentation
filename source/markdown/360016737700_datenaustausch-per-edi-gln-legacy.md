> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

In diesem Artikel findest du Informationen zum Übertragungsmodul EDI und zu GLN.

## Informationen für EDI

Die Adresse direkt in der Rechnungsstruktur ist immer der Empfänger. In der Rechnung entsprechend der Rechnungsempfänger, im Lieferschein der Sendungsempfänger. Das Feld "Soll" der Rechnung hat den Bruttobetrag.

- Umsatz_Netto = Nettobetrag über alle Umsätze
- steuersatz_normal = Normaler Steuersatz
- steuersatz_ ermaessigt = ermäßigte Umsatzsteuer
- gln_empfaenger= Die GLN-Nummer des Empfängers
- ust = Gesamtsumme der Steuern
- ust_ermaessigt = Gesamtsumme der ermäßigten Steuern
- ust_normal = Gesamtsumme der normalen Umsatzsteuern

Die Adresse und GLN vom Absender findet man im Bereich "sender".

xentral stellt diese XML Dateien per FTP oder E-Mail einem EDI Gateways zur Verfügung.

- Pro Beleg muss ein Übertrager in xentral aktiviert werden
- Es muss immer das XML für den Sender hinzugefügt werden
- Einmalig muss ein Freifeld als GLN Nummer definiert werden (für Empfänger bzw. Hauptadressen)
- Bei abweichenden Lieferadressen kann die GLN bei dieser gepflegt werden

## ORDERS (Bestellung)

Bestellungen werden in xentral in eingehend (von Kunden) und ausgehend (von dir aus) unterschieden.

### Richtung: Eingehend

Wenn bei Bestellungen die Rechnungen die Richtung "eingehend" haben, stellen sie Bestellungen von Kunden dar. Diese heißen in xentral Auftrag:

```
<?xml version="1.0" encoding="UTF-8"?>
<response> 
  <status>
  <action>AuftragGet</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  <xml>
  <id>2</id> 
  <datum>2017-05-15</datum>
  <art />
  <projekt>1</projekt>
  <belegnr>200005</belegnr>
  <internet />
  <bearbeiter>Administrator</bearbeiter>
  <angebot>100003</angebot> 
  <freitext /> 
  <internebemerkung />
  <status>freigegeben</status> 
  <adresse>4</adresse> 
  <name>Müller IT Services GmbH</name>
  <abteilung /> 
  <unterabteilung /> 
  <strasse>Am Tal 5</strasse> 
  <adresszusatz /> 
  <ansprechpartner>Sophie Müller</ansprechpartner> 
  <plz>46236</plz> 
  <ort>Bottrop</ort> 
  <land>DE</land> 
  <ustid /> 
  <ust_befreit>0</ust_befreit> 
  <ust_inner>0</ust_inner>
  <email /> 
  <telefon />
  <telefax /> 
  <betreff />
  <kundennummer>10005</kundennummer>
  <versandart>versandunternehmen</versandart>
  <vertrieb>Administrator</vertrieb> 
  <zahlungsweise>rechnung</zahlungsweise>
  <zahlungszieltage>14</zahlungszieltage> 
  <zahlungszieltageskonto>10</zahlungszieltageskonto> 
  <zahlungszielskonto>2.00</zahlungszielskonto> 
  <bank_inhaber /> 
  <bank_institut /> 
  <bank_blz /> 
  <bank_konto /> 
  <kreditkarte_typ /> 
  <kreditkarte_inhaber /> 
  <kreditkarte_nummer />
  <kreditkarte_pruefnummer /> 
  <kreditkarte_monat /> 
  <kreditkarte_jahr /> 
  <firma>1</firma> 
  <versendet>0</versendet> 
  <versendet_am>0000-00-00 00:00:00</versendet_am> 
  <versendet_per />
  <versendet_durch /> 
  <autoversand>0</autoversand> 
  <keinporto>0</keinporto> 
  <keinestornomail>0</keinestornomail> 
  <abweichendelieferadresse>1</abweichendelieferadresse> 
  <liefername>Sophie Müller</liefername> 
  <lieferabteilung />
  <lieferunterabteilung /> 
  <lieferland>DE</lieferland> 
  <lieferstrasse>Mainzer Straße 78</lieferstrasse> 
  <lieferort>Bottrop</lieferort> 
  <lieferplz>46242</lieferplz> 
  <lieferadresszusatz /> 
  <lieferansprechpartner /> 
  <packstation_inhaber /> 
  <packstation_station /> 
  <packstation_ident /> 
  <packstation_plz /> 
  <packstation_ort />
  <autofreigabe>0</autofreigabe> 
  <freigabe>0</freigabe> 
  <nachbesserung>0</nachbesserung> 
  <gesamtsumme>67.69</gesamtsumme> 
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
  <stornogrund /> 
  <stornosonstiges />
  <stornorueckzahlung /> 
  <stornobetrag>0.00</stornobetrag>
  <stornobankinhaber /> 
  <stornobankkonto /> 
  <stornobankblz />
  <stornobankbank /> 
  <stornogutschrift>0</stornogutschrift> 
  <stornogutschriftbeleg /> 
  <stornowareerhalten>0</stornowareerhalten> 
  <stornomanuellebearbeitung /> 
  <stornokommentar /> 
  <stornobezahlt /> 
  <stornobezahltam>0000-00-00</stornobezahltam> 
  <stornobezahltvon /> 
  <stornoabgeschlossen>0</stornoabgeschlossen> 
  <stornorueckzahlungper /> 
  <stornowareerhaltenretour>0</stornowareerhaltenretour>
  <partnerausgezahlt>0</partnerausgezahlt> 
  <partnerausgezahltam>0000-00-00</partnerausgezahltam>
  <kennen />
  <logdatei>2017-05-15 16:39:18</logdatei> 
  <keinetrackingmail /> 
  <zahlungsmailcounter /> 
  <rma>0</rma>
  <transaktionsnummer /> 
  <vorabbezahltmarkieren>0</vorabbezahltmarkieren> 
  <deckungsbeitragcalc>1</deckungsbeitragcalc> 
  <deckungsbeitrag>100.00</deckungsbeitrag> 
  <erloes_netto>56.88</erloes_netto> 
  <umsatz_netto>56.88</umsatz_netto> 
  <lieferdatum>0000-00-00</lieferdatum>
  <tatsaechlicheslieferdatum />
  <liefertermin_ok>1</liefertermin_ok> 
  <teillieferung_moeglich>0</teillieferung_moeglich>
  <kreditlimit_ok>1</kreditlimit_ok>
  <kreditlimit_freigabe>0</kreditlimit_freigabe> 
  <liefersperre_ok>1</liefersperre_ok>
  <teillieferungvon>0</teillieferungvon>
  <teillieferungnummer>0</teillieferungnummer> 
  <vertriebid>1</vertriebid> 
  <aktion /> 
  <provision>0.00</provision>
  <provision_summe>0.00</provision_summe> 
  <anfrageid>0</anfrageid> 
  <gruppe>0</gruppe> 
  <shopextid />
  <shopextstatus /> 
  <ihrebestellnummer />
  <anschreiben />
  <usereditid>1</usereditid>
  <useredittimestamp>2017-05-15 16:39:18</useredittimestamp>
  <realrabatt>0.00</realrabatt>
  <rabatt>0.00</rabatt> 
  <einzugsdatum /> 
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
  <keinsteuersatz>0</keinsteuersatz> 
  <angebotid>5</angebotid>
  <schreibschutz>0</schreibschutz> 
  <pdfarchiviert>0</pdfarchiviert>
  <pdfarchiviertversion>0</pdfarchiviertversion> 
  <typ>firma</typ> 
  <ohne_briefpapier /> 
  <auftragseingangper /> 
  <lieferid>0</lieferid> 
  <ansprechpartnerid>0</ansprechpartnerid> 
  <systemfreitext /> 
  <projektfiliale>0</projektfiliale>
  <lieferungtrotzsperre>0</lieferungtrotzsperre>
  <zuarchivieren>0</zuarchivieren>
  <internebezeichnung />
  <angelegtam />
  <saldo>-67.69</saldo>
  <saldogeprueft>2017-05-15 10:19:35</saldogeprueft>
  <lieferantenauftrag>0</lieferantenauftrag>
  <lieferant>0</lieferant>
  <lieferdatumkw>0</lieferdatumkw> 
  <abweichendebezeichnung>0</abweichendebezeichnung> 
  <rabatteportofestschreiben>0</rabatteportofestschreiben> 
  <sprache /> <bundesland /> 
  <gln>5578124659227</gln>
  <liefergln>6654811237869</liefergln> 
  <bearbeiterid>0</bearbeiterid> 
  <cronjobkommissionierung>0</cronjobkommissionierung>
  <bodyzusatz />
  <lieferbedingung /> 
  <titel />
  <liefertitel />
  <standardlager>0</standardlager>
  <rechnungid>0</rechnungid>
  <artikelliste>
  <position>
  <id>2</id> 
  <auftrag>2</auftrag> 
  <artikel>3</artikel>
  <projekt>1</projekt>
  <bezeichnung>HDMI Kabel</bezeichnung>
  <beschreibung />
  <internerkommentar />
  <nummer>1000003</nummer> 
  <menge>8.0000</menge> 
  <preis>3.36000000</preis> 
  <waehrung>EUR</waehrung> 
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe>1</vpe>
  <sort>1</sort> 
  <status>angelegt</status>
  <umsatzsteuer /> 
  <bemerkung />
  <geliefert>0</geliefert>
  <geliefert_menge>0.0000</geliefert_menge>
  <explodiert>0</explodiert>
  <explodiert_parent>0</explodiert_parent>
  <logdatei>2017-05-15 10:19:34</logdatei>
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
  <einheit />
  <webid />
  <rabatt>0.00</rabatt>
  <nachbestelltexternereinkauf />
  <zolltarifnummer />
  <herkunftsland>DE</herkunftsland>
  <artikelnummerkunde />
  <freifeld1 /> 
  <freifeld2 /> 
  <freifeld3 /> 
  <freifeld4 />
  <freifeld5 /> 
  <freifeld6 />
  <freifeld7 />
  <freifeld8 />
  <freifeld9 /> 
  <freifeld10 />
  <lieferdatumkw>0</lieferdatumkw>
  <teilprojekt>0</teilprojekt>
  <steuersatz /> 
  <steuertext /> 
  <erloese />
  <einkaufspreiswaehrung />
  <einkaufspreis>0.00000000</einkaufspreis>
  <einkaufspreisurspruenglich>3.36000000</einkaufspreisurspruenglich>
  <einkaufspreisid>0</einkaufspreisid> 
  <ekwaehrung>EUR</ekwaehrung>
  <deckungsbeitrag>1.00000000</deckungsbeitrag>
  <freifeld11 /> 
  <freifeld12 /> 
  <freifeld13 /> 
  <freifeld14 /> 
  <freifeld15 /> 
  <freifeld16 /> 
  <freifeld17 /> 
  <freifeld18 />
  <freifeld19 /> 
  <freifeld20 /> 
  <formelmenge /> 
  <formelpreis /> 
  <ean>9548114374576</ean>
  </position>
  <position>
  <id>3</id> 
  <auftrag>2</auftrag> 
  <artikel>4</artikel>
  <projekt>1</projekt>
  <bezeichnung>USB Maus</bezeichnung>
  <beschreibung />
  <internerkommentar /> 
  <nummer>1000004</nummer>
  <menge>3.0000</menge>
  <preis>10.00000000</preis> 
  <waehrung>EUR</waehrung> 
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe>1</vpe>
  <sort>2</sort>
  <status>angelegt</status>
  <umsatzsteuer /> 
  <bemerkung />
  <geliefert>0</geliefert>
  <geliefert_menge>0.0000</geliefert_menge>
  <explodiert>0</explodiert>
  <explodiert_parent>0</explodiert_parent>
  <logdatei>2017-05-15 09:49:19</logdatei>
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
  <einheit /> 
  <webid />
  <rabatt>0.00</rabatt> 
  <nachbestelltexternereinkauf /> 
  <zolltarifnummer /> 
  <herkunftsland>DE</herkunftsland> 
  <artikelnummerkunde />
  <freifeld1 />
  <freifeld2 />
  <freifeld3 />
  <freifeld4 />
  <freifeld5 />
  <freifeld6 /> 
  <freifeld7 /> 
  <freifeld8 /> 
  <freifeld9 />
  <freifeld10 />
  <lieferdatumkw>0</lieferdatumkw> 
  <teilprojekt>0</teilprojekt>
  <steuersatz />
  <steuertext />
  <erloese />
  <einkaufspreiswaehrung /> 
  <einkaufspreis>0.00000000</einkaufspreis> 
  <einkaufspreisurspruenglich>10.00000000</einkaufspreisurspruenglich>
  <einkaufspreisid>0</einkaufspreisid>
  <ekwaehrung>EUR</ekwaehrung> 
  <deckungsbeitrag>1.00000000</deckungsbeitrag> 
  <freifeld11 /> 
  <freifeld12 /> 
  <freifeld13 />
  <freifeld14 /> 
  <freifeld15 />
  <freifeld16 /> 
  <freifeld17 /> 
  <freifeld18 />
  <freifeld19 />
  <freifeld20 /> 
  <formelmenge /> 
  <formelpreis /> 
  <ean>7458424177423</ean>
  </position> 
  </artikelliste>
  </xml> 
</response>
```

## INVOIC (Rechnung)

Im Folgenden wird die ausgehende Rechnung an die Kunden dargestellt.

### Richtung: Ausgehend

xentral stellt die Rechnung für den Kunden zur Verfügung.

```
<?xml version="1.0" encoding="UTF-8"?>
<response> 
  <xml> 
  <rechnung_list> 
  <rechnung>
  <id>142</id> 
  <datum>2016-10-06</datum> 
  <aborechnung>0</aborechnung>
  <projekt>19</projekt> 
  <anlegeart /> 
  <belegnr>400112</belegnr> 
  <auftrag>200167</auftrag>
  <auftragid>224</auftragid> 
  <bearbeiter>Cashier</bearbeiter>
  <freitext>Datum / Uhrzeit des Verkaufs: 06.10.2016 15:49:00</freitext> 
  <internebemerkung />
  <status>versendet</status>
  <adresse>15</adresse>
  <name>Laufkundschaft</name> 
  <abteilung /> 
  <unterabteilung />
  <strasse />
  <adresszusatz />
  <ansprechpartner />
  <plz />
  <ort /> 
  <land />
  <ustid /> 
  <ust_befreit>0</ust_befreit>
  <ustbrief>0</ustbrief> 
  <ustbrief_eingang>0</ustbrief_eingang> 
  <ustbrief_eingang_am>0000-00-00</ustbrief_eingang_am>
  <email /> 
  <telefon /> 
  <telefax /> 
  <betreff />
  <kundennummer>10006</kundennummer> 
  <lieferschein>0</lieferschein>
  <versandart>selbstabholer</versandart>
  <lieferdatum>0000-00-00</lieferdatum> 
  <buchhaltung>Max</buchhaltung> 
  <zahlungsweise>bar</zahlungsweise> 
  <zahlungsstatus>offen</zahlungsstatus>
  <ist>0.00</ist> 
  <soll>421.20</soll> 
  <skonto_gegeben>0.00</skonto_gegeben> 
  <zahlungszieltage>0</zahlungszieltage> 
  <zahlungszieltageskonto>0</zahlungszieltageskonto> 
  <zahlungszielskonto>0.00</zahlungszielskonto>
  <firma>1</firma>
  <versendet>0</versendet>
  <versendet_am>0000-00-00 00:00:00</versendet_am>
  <versendet_per /> 
  <versendet_durch />
  <versendet_mahnwesen>0</versendet_mahnwesen> 
  <mahnwesen /> 
  <mahnwesen_datum>0000-00-00</mahnwesen_datum> 
  <mahnwesen_gesperrt>0</mahnwesen_gesperrt>
  <mahnwesen_internebemerkung />
  <inbearbeitung>0</inbearbeitung>
  <datev_abgeschlossen>0</datev_abgeschlossen> 
  <logdatei>2016-10-07 08:41:38</logdatei> 
  <doppel /> 
  <autodruck_rz>0</autodruck_rz> 
  <autodruck_periode>1</autodruck_periode>
  <autodruck_done>0</autodruck_done> 
  <autodruck_anzahlverband>0</autodruck_anzahlverband> 
  <autodruck_anzahlkunde>0</autodruck_anzahlkunde> 
  <autodruck_mailverband>0</autodruck_mailverband>
  <autodruck_mailkunde>0</autodruck_mailkunde> 
  <dta_datei_verband>0</dta_datei_verband> 
  <dta_datei>0</dta_datei> 
  <deckungsbeitragcalc>1</deckungsbeitragcalc> 
  <deckungsbeitrag>-1.37</deckungsbeitrag>
  <umsatz_netto>353.95</umsatz_netto> 
  <erloes_netto>-4.85</erloes_netto> 
  <mahnwesenfestsetzen>0</mahnwesenfestsetzen> 
  <vertriebid>11</vertriebid> 
  <aktion /> 
  <vertrieb>Cashier</vertrieb>
  <provision>0.00</provision> 
  <provision_summe>0.00</provision_summe>
  <gruppe>0</gruppe>
  <punkte /> 
  <bonuspunkte />
  <provdatum />
  <ihrebestellnummer /> 
  <anschreiben /> 
  <usereditid />
  <useredittimestamp>0000-00-00 00:00:00</useredittimestamp>
  <realrabatt /> 
  <rabatt>0</rabatt> 
  <einzugsdatum>0000-00-00</einzugsdatum>
  <rabatt1>0.00</rabatt1>
  <rabatt2>0.00</rabatt2>
  <rabatt3>0.00</rabatt3> 
  <rabatt4>0.00</rabatt4>
  <rabatt5>0.00</rabatt5> 
  <forderungsverlust_datum />
  <forderungsverlust_betrag />
  <steuersatz_normal>19.00</steuersatz_normal>
  <steuersatz_zwischen>7.00</steuersatz_zwischen> 
  <steuersatz_ermaessigt>7.00</steuersatz_ermaessigt>
  <steuersatz_starkermaessigt>7.00</steuersatz_starkermaessigt>
  <steuersatz_dienstleistung>7.00</steuersatz_dienstleistung>
  <waehrung>EUR</waehrung> 
  <keinsteuersatz>0</keinsteuersatz>
  <schreibschutz>1</schreibschutz> 
  <pdfarchiviert>0</pdfarchiviert>
  <pdfarchiviertversion>0</pdfarchiviertversion> 
  <typ>firma</typ>
  <ohne_briefpapier /> 
  <lieferid>0</lieferid>
  <ansprechpartnerid>0</ansprechpartnerid>
  <systemfreitext />
  <projektfiliale>0</projektfiliale>
  <zuarchivieren>0</zuarchivieren>
  <internebezeichnung />
  <angelegtam>2016-10-06 15:49:00</angelegtam> 
  <abweichendebezeichnung>1</abweichendebezeichnung> 
  <bezahlt_am />
  <sprache />
  <bodyzusatz />
  <id_ext />
  <gln_empfaenger>12345699</gln_empfaenger> 
  <liefername>Laufkundschaft</liefername>
  <lieferstrasse />
  <lieferadresszusatz /> 
  <lieferansprechpartner />
  <lieferabteilung /> 
  <lieferunterabteilung />
  <lieferplz /> 
  <lieferort /> 
  <lieferland />
  <gebuehr>0</gebuehr>
  <ust>67.25</ust>
  <ust_ermaessigt>0</ust_ermaessigt> 
  <ust_normal>67.25</ust_normal> 
  <rechnung_position_list> 
  <rechnung_position> 
  <id>208</id>
  <rechnung>142</rechnung> 
  <artikel>123</artikel> 
  <projekt>19</projekt>
  <bezeichnung>Test-Artikel Serial</bezeichnung>
  <beschreibung /> 
  <internerkommentar />
  <nummer>100040</nummer> 
  <menge>120</menge> 
  <preis>2.94957983</preis> 
  <waehrung>EUR</waehrung>
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe />
  <sort>1</sort> 
  <status>angelegt</status>
  <umsatzsteuer>normal</umsatzsteuer> 
  <bemerkung /> 
  <logdatei>2016-10-06 15:49:00</logdatei>
  <explodiert_parent_artikel>0</explodiert_parent_artikel>
  <punkte>0.00</punkte> 
  <bonuspunkte>0.00</bonuspunkte> 
  <mlmdirektpraemie>0.00</mlmdirektpraemie>
  <mlm_abgerechnet />
  <keinrabatterlaubt>0</keinrabatterlaubt> 
  <grundrabatt>0.00</grundrabatt> 
  <rabattsync>1</rabattsync> 
  <rabatt1>0.00</rabatt1> 
  <rabatt2>0.00</rabatt2> 
  <rabatt3>0.00</rabatt3>
  <rabatt4>0.00</rabatt4> 
  <rabatt5>0.00</rabatt5> 
  <einheit /> 
  <rabatt>0.00</rabatt> 
  <zolltarifnummer>0</zolltarifnummer> 
  <herkunftsland>0</herkunftsland>
  <artikelnummerkunde />
  <freifeld1 /> 
  <freifeld2 />
  <freifeld3 />
  <freifeld4 />
  <freifeld5 />
  <freifeld6 />
  <freifeld7 />
  <freifeld8 />
  <freifeld9 /> 
  <freifeld10 />
  <lieferdatumkw>0</lieferdatumkw> 
  <auftrag_position_id>406</auftrag_position_id>
  <teilprojekt>0</teilprojekt> 
  <id_ext /> 
  <ean /> 
  <gewicht /> 
  <herstellernummer /> 
  </rechnung_position> 
  </rechnung_position_list>
  </rechnung>
  </rechnung_list> 
  <sender> 
  <gln>12345</gln> 
  <name>Musterfirma</name> 
  <strasse>Musterfirma</strasse> 
  <adresszusatz /> 
  <ansprechpartner /> 
  <abteilung /> 
  <unterabteilung />
  <plz>12344</plz> 
  <ort>Musterdorf</ort>
  <land>DE</land> 
  </sender> 
  </xml> 
  <status> 
  <action>belege</action>
  <message>OK</message> 
  <messageCode>1</messageCode> 
  </status>
</response>

```

In den Übertragungen Einstellungen können im Feld XML-Zusatz feste XML-Elemente hinzugefügt werden: Zum Beispiel EDI-Senderinformationen. GLN-Felder für Adressen werden in Freifeldern gespeichert und in der Übertragung-Einstellung zugeordnet.

Beispiel für Sender Adresse (diese muss fest so hier angegeben werden):

```
<sender>
<gln>12345</gln>
<name>Musterfirma</name>
<strasse>Musterfirma</strasse>
<adresszusatz/>
<ansprechpartner/>
<abteilung/>
<unterabteilung/>
<plz>12344</plz>
<ort>Musterdorf</ort>
<land>DE</land>
</sender>
```

## DESADV (Lieferschein)

### Richtung: Ausgehend

xentral stellt den Lieferschein für den Kunden zur Verfügung.

```
<?xml version="1.0" encoding="UTF-8"?> 
<response> 
  <xml> 
  <lieferschein_list> 
  <lieferschein>
  <id>86</id>
  <datum>2016-10-07</datum> 
  <projekt>20</projekt>
  <lieferscheinart /> 
  <belegnr>30002</belegnr>
  <bearbeiter>Max</bearbeiter> 
  <auftrag>20002</auftrag>
  <auftragid>225</auftragid> 
  <freitext /> 
  <status>versendet</status>
  <adresse>3</adresse> 
  <name>Max Muster</name>
  <abteilung /> 
  <unterabteilung /> 
  <strasse>Musterstrasse 6</strasse> 
  <adresszusatz />
  <ansprechpartner />
  <plz>12345</plz>
  <ort>Musterdorf</ort>
  <land>DE</land>
  <ustid />
  <email>info@maxmuellermuster.de</email>
  <telefon>0821123456789</telefon> 
  <telefax>0821123456790</telefax>
  <betreff />
  <kundennummer>10000</kundennummer> 
  <versandart>versandunternehmen</versandart>
  <versand>Max</versand>
  <firma>1</firma> 
  <versendet>1</versendet> 
  <versendet_am>0000-00-00 00:00:00</versendet_am> 
  <versendet_per />
  <versendet_durch /> 
  <inbearbeitung_user>0</inbearbeitung_user> 
  <logdatei>2016-10-07 10:06:43</logdatei> 
  <vertriebid>0</vertriebid> <vertrieb>Max</vertrieb>
  <ust_befreit>0</ust_befreit>
  <ihrebestellnummer />
  <anschreiben>Sehr geehrter Herr Muster</anschreiben>
  <usereditid />
  <useredittimestamp>0000-00-00 00:00:00</useredittimestamp> 
  <lieferantenretoure>0</lieferantenretoure> 
  <lieferantenretoureinfo /> <lieferant>0</lieferant> 
  <schreibschutz>1</schreibschutz> <pdfarchiviert>0</pdfarchiviert> 
  <pdfarchiviertversion>0</pdfarchiviertversion> 
  <typ>firma</typ>
  <internebemerkung /> 
  <ohne_briefpapier />
  <lieferid>0</lieferid>
  <ansprechpartnerid>0</ansprechpartnerid>
  <projektfiliale>0</projektfiliale>
  <projektfiliale_eingelagert>0</projektfiliale_eingelagert> 
  <zuarchivieren>0</zuarchivieren>
  <internebezeichnung />
  <angelegtam /> 
  <kommissionierung>0</kommissionierung>
  <sprache /> 
  <bodyzusatz />
  <id_ext />
  <gln_empfaenger />
  <rechnung_name>Max Muster</rechnung_name>
  <rechnung_anrede />
  <rechnung_strasse>Musterstrasse 6</rechnung_strasse> 
  <rechnung_adresszusatz /> 
  <rechnung_ansprechpartner /> 
  <rechnung_abteilung /> 
  <rechnung_unterabteilung /> 
  <rechnung_plz>12345</rechnung_plz> 
  <rechnung_ort>Musterdorf</rechnung_ort>
  <rechnung_land>DE</rechnung_land>
  <lieferschein_position_list> 
  <lieferschein_position>
  <id>121</id> 
  <lieferschein>86</lieferschein>
  <artikel>124</artikel>
  <projekt>20</projekt>
  <bezeichnung>TestNummernkreis</bezeichnung> 
  <beschreibung /> 
  <internerkommentar /> 
  <nummer>100041</nummer>
  <seriennummer />
  <menge>1</menge> 
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe>1</vpe>
  <sort>1</sort>
  <status>angelegt</status>
  <bemerkung />
  <geliefert>0</geliefert>
  <abgerechnet>0</abgerechnet>
  <logdatei>2016-10-07 10:05:53</logdatei> 
  <explodiert_parent_artikel>0</explodiert_parent_artikel> 
  <einheit />
  <zolltarifnummer />
  <herkunftsland>DE</herkunftsland>
  <artikelnummerkunde /> 
  <freifeld1 /> 
  <freifeld2 />
  <freifeld3 />
  <freifeld4 /> 
  <freifeld5 /> 
  <freifeld6 />
  <freifeld7 /> 
  <freifeld8 />
  <freifeld9 />
  <freifeld10 />
  <lieferdatumkw>0</lieferdatumkw>
  <auftrag_position_id>407</auftrag_position_id>
  <kostenlos>0</kostenlos> 
  <lagertext />
  <teilprojekt>0</teilprojekt> 
  <explodiert_parent>0</explodiert_parent> 
  <id_ext /> 
  <ean />
  <gewicht />
  <herstellernummer /> 
  </lieferschein_position> 
  </lieferschein_position_list>
  </lieferschein>
  </lieferschein_list> 
  </xml> 
  <status> 
  <action>belege</action> 
  <message>OK</message> 
  <messageCode>1</messageCode> 
  </status>
</response>
```

## PRICAT (Artikelkatalog)

### Richtung: Ausgehend

xentral stellt den Artikelkatalog für den Kunden zur Verfügung:

```
<?xml version="1.0" encoding="UTF-8"?> 
<response> 
  <xml> 
  <artikel_list> 
  <artikel>
  <id>36327</id>
  <typ>1170_kat</typ>
  <nummer>200000</nummer> 
  <checksum/> 
  <projekt>0</projekt>
  <inaktiv/>
  <ausverkauft>0</ausverkauft>
  <warengruppe/> 
  <name_de>Testartikel</name_de>
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
  <hersteller>Mustermann GmbH</hersteller> 
  <teilbar/> 
  <nteile/> 
  <seriennummern>keine</seriennummern> 
  <lager_platz/>
  <lieferzeit/>
  <lieferzeitmanuell/>
  <sonstiges/>
  <gewicht>1</gewicht> 
  <endmontage/>
  <funktionstest/>
  <artikelcheckliste/>
  <stueckliste>0</stueckliste> 
  <juststueckliste>0</juststueckliste> 
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
  <umsatzsteuer/>
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
  <logdatei>2016-08-31 14:41:54</logdatei>
  <anabregs_text>Artikelbeschreibung<br /></anabregs_text>
  <autobestellung>0</autobestellung>
  <produktion>0</produktion> 
  <herstellernummer/> 
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
  <useredittimestamp>2016-08-31 14:41:54</useredittimestamp> 
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
  <sonderaktion_en/>
  <autolagerlampe>0</autolagerlampe> 
  <leerfeld/> 
  <zolltarifnummer/>
  <herkunftsland>DE</herkunftsland>
  <laenge>20.00</laenge>
  <breite>20.00</breite>
  <hoehe>10.00</hoehe>
  <gebuehr>0</gebuehr>
  <pseudolager/> 
  <anabregs_text_en/>
  <matrixprodukt>0</matrixprodukt>
  <downloadartikel>0</downloadartikel> 
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
  <generierenummerbeioption>0</generierenummerbeioption> 
  <allelieferanten>0</allelieferanten> 
  <variante_kopie>0</variante_kopie>
  <bildvorschau/> 
  <inventursperre>0</inventursperre> 
  <unikat>0</unikat> 
  <tagespreise>0</tagespreise> 
  <rohstoffe>0</rohstoffe>
  <externeproduktion>0</externeproduktion>
  <vkmeldungunterdruecken>0</vkmeldungunterdruecken>
  <id_ext/>
  </artikel>
  </artikel_list> 
  </xml>
  <status>
  <action>artikel_list</action>
  <message>OK</message> 
  <messageCode>1</messageCode>
  </status> 
</response>
```

## Sonstige Informationen für GLN

### Variablen

Die GLN kann als Variable in Dokumente übernommen werden:

- {GLN} → GLN aus der Stammdatenadresse (diese wird im Dokument im Feld "GLN" bei der Stammdatenadresse abgespeichert)
- {LIEFERGLN} → GLN aus der Lieferadresse (diese wird im Dokument in der blauen Box bei der Lieferadresse abgespeichert)

#### GLN

![TransferEdi_2.png](https://help.xentral.com/hc/article_attachments/16611906550172)

#### Liefer-GLN

![TransferEdi_3.png](https://help.xentral.com/hc/article_attachments/16611943870748)

#### Einstellungen in den Textvorlagen

![TransferEdi_4.png](https://help.xentral.com/hc/article_attachments/16611906561436)