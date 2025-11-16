> **Wichtig**
>
> Dieser Artikel setzt voraus, dass du bereits mit dem Modul **Übertragungen ** in Xentral vertraut bist und über das notwendige Wissen zu den einzelnen Datenformaten und Logistik-Workflows verfügst. Falls du dir nicht sicher bist, ob du bereit für die technischen Details des Datenaustausches bist, schau dir die weiteren Informationen und besonders den ArtikelÜbersicht: Fulfillment-Dienstleister (3PL) anbindenim Themenbereich**Fulfillment** an.

## Unterstützte Kryptoalgorithmen für SFTP-Server

Wenn Probleme bei der Herstellung einer SFTP-Verbindung mit deinem Server auftreten oder eine Fehlermeldung angezeigt wird, informiere bitte deinen Fulfillment-Dienstleister oder (falls zutreffend) deinen Systemadministrator. Diese Personen prüfen dann, ob dein SFTP-Server die unten genannten Kryptoalgorithmen unterstützt.

Unterstützt dein Server diese Kryptoalgorithmen nicht, wechsle auf einen SFTP-Server, der die Kryptoalgorithmen unterstützt oder bitte die zuständigen Personen, die benötigten Kryptoalgorithmen in der Serverkonfiguration zu erlauben.

Derzeit unterstütztXentral bei SFTP-Verbindungen die folgenden Kryptoalgorithmen:

| Unterstützte Key Exchange KEX-Methoden | Unterstützte Hostkey-Methoden |
| --- | --- |
| curve25519-sha256 | ssh-ed25519 |
| [curve25519-sha256@libssh.org](mailto:curve25519-sha256@libssh.org) | ecdsa-sha2-nistp256 |
| ecdh-sha2-nistp256 | ecdsa-sha2-nistp384 |
| ecdh-sha2-nistp384 | ecdsa-sha2-nistp521 |
| ecdh-sha2-nistp521 | rsa-sha2-256 |
| diffie-hellman-group-exchange-sha256 | rsa-sha2-512 |
| diffie-hellman-group-exchange-sha1 | ssh-rsa |
| diffie-hellman-group14-sha256 | ssh-dss |
| diffie-hellman-group14-sha1 | |
| diffie-hellman-group15-sha512 | |
| diffie-hellman-group16-sha512 | |
| diffie-hellman-group17-sha512 | |
| diffie-hellman-group18-sha512 | |
| diffie-hellman-group1-sha1 | |

## Beispielhafte CSV- und XML-Dateien

Wie du bereits weißt, findet der Datenaustausch zwischen Xentral und dem Fremdsystem des Fulfillment-Dienstleisters häufig über Dateien in den Formaten CSV oder XML statt.

Bei der Einrichtung von Übertragungen werden im Hintergrund Standard-Dateistrukturen verwendet, die in vielen Fällen bereits ausreichen, um alle notwendigen Daten zwischen Xentral und dem Fremdsystem auszutauschen. Falls notwendig oder gewünscht, kannst du aus- oder eingehende CSV- und XML-Strukturen anpassen, soweit du über das notwendige technische Fachwissen verfügst. Für diese Anpassungen benötigst du Smarty, also eine Template Engine, mit der sich diese Dateistrukturen beeinflussen lassen.

> **Tipp**
>
> Schau dir folgende Artikel an, um mehr über über die Verwendung von Smarty zu lernen:
>
> - Einführung Smarty
> - Smarty Felddefinitionen
> - Smarty im Übertragungen Modul

Damit du Dateien korrekt aufbauen und somit Fehler vermeiden kannst, enthält dieser Artikel einige Beispiel-Dateien für die häufigsten Anwendungsfälle. Beachte jedoch, dass es sich lediglich um Musterdateien handelt, die du für deinen produktiven Einsatz erst anpassen musst.

### CSV-Dateien

In den folgenden Unterkapiteln stellen wir dir den beispielhaften Aufbau der jeweiligen CSV-Datei pro Anwendungsfall zur Verfügung. Neben einer kurzen Beschreibung des Anwendungsfalls findest du hier auch wichtige Zusatzinformationen.

#### Lieferscheine übertragen

Nutze die folgende CSV-Struktur, um Lieferscheine an deinen Fulfillment-Dienstleister zu übertragen.

```
adresse;artikel;beleg_projekt;art;beleg_status;beleg_datum;
beleg_versandart;beleg_belegnr;beleg_kundennummer;beleg_name;
beleg_abteilung;beleg_unterabteilung;beleg_adresszusatz;
beleg_ansprechpartner;beleg_telefon;beleg_email;beleg_land;
beleg_strasse;beleg_plz;beleg_ort;beleg_internebemerkung;
beleg_internebezeichnung;beleg_freitext;beleg_lieferbedingung;
artikel_nummer;artikel_bezeichnung;artikel_beschreibung;
artikel_menge;artikel_lieferdatum;artikel_sort;artikel_einheit;
artikel_zolltarifnummer;artikel_herkunftsland;
artikel_artikelnummerkunde;artikel_freifeld1;
artikel_freifeld2;artikel_freifeld3;artikel_freifeld4;
artikel_freifeld5;artikel_freifeld6;artikel_freifeld7;
artikel_freifeld8;artikel_freifeld9;artikel_freifeld10;
artikel_freifeld11;artikel_freifeld12;artikel_freifeld13;
artikel_freifeld14;artikel_freifeld15;artikel_freifeld16;
artikel_freifeld17;artikel_freifeld18;artikel_freifeld19;
artikel_freifeld20;artikel_freifeld21;artikel_freifeld22;
artikel_freifeld23;artikel_freifeld24;artikel_freifeld25;
artikel_freifeld26;artikel_freifeld27;artikel_freifeld28;
artikel_freifeld29;artikel_freifeld30;artikel_freifeld31;
artikel_freifeld32;artikel_freifeld33;artikel_freifeld34;
artikel_freifeld35;artikel_freifeld36;artikel_freifeld37;
artikel_freifeld38;artikel_freifeld39;artikel_freifeld40;
artikel_ean;artikel_preisfuermenge; 
```

#### Aufträge übertragen

Nutze die folgende CSV-Struktur, um Aufträge an deinen Fulfillment-Dienstleister zu übertragen.

> **Wichtig**
>
> Nutzt du Freifelder im Auftrag, deren Inhalt mit übertragen werden soll? Dann stelle sicher, dass du im Menü **Einstellungen > Stammdaten > Freifelder ** die Option**Anzeige im PDF** für den betreffenden Belegtyp (hier: Auftrag) aktiviert ist, bevor du mit der Übertragung startest.

```
beleg_projekt;art;beleg_status;beleg_datum;
beleg_tatsaechlicheslieferdatum;beleg_versandart;
beleg_zahlungsweise; beleg_belegnr;beleg_kundennummer;
beleg_name;beleg_abteilung;beleg_unterabteilung;
beleg_adresszusatz;beleg_ansprechpartner;beleg_telefon;
beleg_email;beleg_land;beleg_strasse;beleg_plz;
beleg_ort;beleg_aktion;beleg_internebemerkung;
beleg_internebezeichnung;beleg_freitext;
beleg_ihrebestellnummer;beleg_lieferbedingung;
beleg_art;artikel_nummer;artikel_bezeichnung;
artikel_beschreibung;artikel_menge;artikel_preis;
artikel_rabatt;artikel_waehrung;artikel_lieferdatum;
artikel_sort;artikel_umsatzsteuer;artikel_einheit;
artikel_zolltarifnummer;artikel_herkunftsland;
artikel_artikelnummerkunde;artikel_freifeld1;
artikel_freifeld2;artikel_freifeld3;artikel_freifeld4;
artikel_freifeld5;artikel_freifeld6;artikel_freifeld7;
artikel_freifeld8;artikel_freifeld9;artikel_freifeld10;
artikel_freifeld11;artikel_freifeld12;artikel_freifeld13;
artikel_freifeld14;artikel_freifeld15;artikel_freifeld16;
artikel_freifeld17;artikel_freifeld18;artikel_freifeld19;
artikel_freifeld20
  
  
```

#### Tracking-URLs empfangen

Nutze die folgende CSV-Struktur, um Tracking-URLs zu importieren, die von deinem Fulfillment-Dienstleister an dich zurückgemeldet werden.

> **Wichtig**
>
> Möchtest du zusätzlich zu den Tracking-URLs auch Informationen zu Mindesthaltbarkeitsdaten, Chargen oder Seriennummern importieren? Dieser Anwendungsfall ist mit der Übertragung per CSV nicht möglich. Nutze stattdessen XML-Dateien für die Übertragung.

### Achtung

Stelle beim Import von Tracking-URLs per CSV sicher, dass die Spalte **versandart** in der Struktur enthalten ist. Hierbei handelt es sich um eine Pflichtangabe.

```
belegnr;tracking;tracking_link;versandart

2300111;1234567890;https://example.com/?tracking=1234567890;dhl
```

#### Bestandsinformationen zu Lagerartikeln empfangen

Nutze die folgende CSV-Struktur, um Lagerzahlen zu importieren, die von deinem Fulfillment-Dienstleister an dich zurückgemeldet werden.

```
nummer;lagerzahl;lager_platz

1000012;5;Dropregal1
```

#### Informationen zu MHD und Chargen empfangen

Nutze die folgende CSV-Struktur, um Informationen zu MHD und Chargen zu importieren, die von deinem Fulfillment-Dienstleister an dich zurückgemeldet werden.

```
nummer;lagerzahl;lager_platz;mhd;charge

1000003;6;Lagerplatz11;2022-01-01;TX500

```

### XML-Dateien

In den folgenden Unterkapiteln stellen wir dir den beispielhaften Aufbau der jeweiligen XML-Datei pro Anwendungsfall zur Verfügung. Neben einer kurzen Beschreibung des Anwendungsfalls findest du hier auch wichtige Zusatzinformationen.

> **Wichtig**
>
> Wenn du das Element **<versandart>** innerhalb einer XML-Struktur verwendest, stelle sicher, dass du die Versandart mit genau der Bezeichnung verwendest, die in der Spalte ** Typ **im Menü ** Versandarten** angezeigt werden. Beachte vor allem die korrekte Groß- und Kleinschreibung, da die Informationen der Versandart ansonsten nicht korrekt übertragen werden.

#### Lieferscheine übertragen

Nutze die folgende XML-Struktur, um Lieferscheine an deinen Fulfillment-Dienstleister zu übertragen.

```
<?xmlversion="1.0"encoding="UTF-8"?>
<response>
  <xml>
  <lieferschein_list>
  <lieferschein>
  <datum>2016-11-10</datum>
  <projekt>1</projekt>
  <lieferscheinart />
  <belegnr>13256</belegnr>
  <bearbeiter>Sachbearbeiter1</bearbeiter>
  <auftrag>AH200019</auftrag>
  <auftragid>15</auftragid>
  <freitext />
  <status>versendet</status>
  <adresse>26</adresse>
  <name>Musterfirma GmbH</name>
  <abteilung />
  <unterabteilung />
  <strasse>Müsterstraße 12</strasse>
  <adresszusatz />
  <ansprechpartner />
  <plz>12345</plz>
  <ort>Musterhausen</ort>
  <land>DE</land>
  <ustid />
  <email>musterfirma@waw.de</email>
  <telefon />
  <telefax />
  <betreff />
  <kundennummer>12000</kundennummer>
  <versandart>DHL</versandart>
  <versand />
  <firma>1</firma>
  <versendet>1</versendet>
  <versendet_am>2016-11-10 12:05:35</versendet_am>
  <versendet_per>sonstiges</versendet_per>
  <versendet_durch>VersandMA1</versendet_durch>
  <inbearbeitung_user>0</inbearbeitung_user>
  <logdatei>2016-11-10 12:06:59</logdatei>
  <vertriebid>0</vertriebid>
  <vertrieb>Johannes Schmid</vertrieb>
  <ust_befreit>0</ust_befreit>
  <ihrebestellnummer />
  <anschreiben />
  <usereditid>1</usereditid>
  <useredittimestamp>2016-11-10 12:06:59</useredittimestamp>
  <lieferantenretoure>0</lieferantenretoure>
  <lieferantenretoureinfo />
  <lieferant>0</lieferant>
  <schreibschutz>1</schreibschutz>
  <pdfarchiviert>0</pdfarchiviert>
  <pdfarchiviertversion>0</pdfarchiviertversion>
  <typ>firma</typ>
  <internebemerkung />
  <ohne_briefpapier>0</ohne_briefpapier>
  <lieferid>0</lieferid>
  <ansprechpartnerid>0</ansprechpartnerid>
  <projektfiliale>0</projektfiliale>
  <projektfiliale_eingelagert>0</projektfiliale_eingelagert>
  <zuarchivieren>0</zuarchivieren>
  <internebezeichnung />
  <angelegtam>0000-00-00 00:00:00</angelegtam>
  <kommissionierung>0</kommissionierung>
  <sprache />
  <bodyzusatz />
  <id_ext />
  <rechnung_name>Musterfirma GmbH</rechnung_name>
  <rechnung_anrede />
  <rechnung_strasse>Musterstrasse 12</rechnung_strasse>
  <rechnung_adresszusatz />
  <rechnung_ansprechpartner>Mustermann</rechnung_ansprechpartner>
  <rechnung_abteilung />
  <rechnung_unterabteilung />
  <rechnung_plz>12345</rechnung_plz>
  <rechnung_ort>Musterhausen</rechnung_ort>
  <rechnung_land>CN</rechnung_land>
  <anzahluebertragungen>1</anzahluebertragungen>
  <lieferschein_position_list>
  <lieferschein_position>
  <lieferschein>10</lieferschein>
  <projekt>1</projekt>
  <bezeichnung>Musterartikel</bezeichnung>
  <beschreibung />
  <internerkommentar />
  <nummer>AI-100-2</nummer>
  <seriennummer />
  <menge>3</menge>
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe />
  <sort>1</sort>
  <status>angelegt</status>
  <bemerkung />
  <geliefert>0</geliefert>
  <abgerechnet>0</abgerechnet>
  <logdatei>2016-11-10 11:59:02</logdatei>
  <explodiert_parent_artikel>0</explodiert_parent_artikel>
  <einheit />
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
  <auftrag_position_id>30</auftrag_position_id>
  <kostenlos>0</kostenlos>
  <lagertext />
  <teilprojekt>0</teilprojekt>
  <explodiert_parent>0</explodiert_parent>
  <id_ext />
  <ean />
  <gewicht />
  <herstellernummer />
  <lagerartikel>1</lagerartikel>
  </lieferschein_position>
  </lieferschein_position_list>
  </lieferschein>
  </lieferschein_list>
  
</response>
<xml>
```

#### Lieferscheine mit Stücklisten übertragen

Nutze die folgende XML-Struktur, um Lieferscheine, die Stücklisten enthalten, an deinen Fulfillment-Dienstleister zu übertragen.

```
<?xmlversion="1.0"encoding="UTF-8"?>
<response>
  <xml>
  <lieferschein_list>
  <lieferschein>
  <id>87</id>
  <datum>2017-11-02</datum>
  <projekt>1</projekt>
  <lieferscheinart />
  <belegnr>171102-10</belegnr>
  <bearbeiter>Administrator</bearbeiter>
  <auftrag>200091</auftrag>
  <auftragid>122</auftragid>
  <freitext />
  <status>versendet</status>
  <adresse>2</adresse>
  <name>Beispielkunde</name>
  <abteilung>Wareneingang</abteilung>
  <unterabteilung>Elektronik</unterabteilung>
  <strasse>Rue de bellvue</strasse>
  <adresszusatz />
  <ansprechpartner>Testkontakt</ansprechpartner>
  <plz>1620</plz>
  <ort>Brüssel</ort>
  <land>BE</land>
  <ustid>4545446656446</ustid>
  <email />
  <telefon />
  <telefax />
  <betreff />
  <kundennummer>10003</kundennummer>
  <versandart>DPD</versandart>
  <versand>Administrator</versand>
  <firma>1</firma>
  <versendet>1</versendet>
  <versendet_am>0000-00-00 00:00:00</versendet_am>
  <versendet_per />
  <versendet_durch />
  <inbearbeitung_user>0</inbearbeitung_user>
  <logdatei>2017-11-02 08:55:17</logdatei>
  <vertriebid>1</vertriebid>
  <vertrieb>Administrator</vertrieb>
  <ust_befreit>3</ust_befreit>
  <ihrebestellnummer />
  <anschreiben />
  <usereditid />
  <useredittimestamp>0000-00-00 00:00:00</useredittimestamp>
  <lieferantenretoure>0</lieferantenretoure>
  <lieferantenretoureinfo />
  <lieferant>0</lieferant>
  <schreibschutz>1</schreibschutz>
  <pdfarchiviert>0</pdfarchiviert>
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
  <kommissionierung>65</kommissionierung>
  <sprache />
  <bundesland />
  <gln />
  <rechnungid>53</rechnungid>
  <bearbeiterid />
  <bodyzusatz />
  <lieferbedingung />
  <titel />
  <standardlager>0</standardlager>
  <kommissionskonsignationslager>0</kommissionskonsignationslager>
  <abweichendebezeichnung>0</abweichendebezeichnung>
  <id_ext />
  <anzahluebertragungen>1</anzahluebertragungen>
  <rechnung_name>Testkunde</rechnung_name>
  <rechnung_anrede />
  <rechnung_strasse>Musterstrasse 7</rechnung_strasse>
  <rechnung_adresszusatz>Anlieferbereich C</rechnung_adresszusatz>
  <rechnung_ansprechpartner>Testansprechpartner</rechnung_ansprechpartner>
  <rechnung_abteilung>Einkauf</rechnung_abteilung>
  <rechnung_unterabteilung>Technik</rechnung_unterabteilung>
  <rechnung_plz>848415</rechnung_plz>
  <rechnung_ort>Musterhausen</rechnung_ort>
  <rechnung_land>DE</rechnung_land>
  <internet />
  <shopextid />
  <lieferschein_position_list>
  <lieferschein_position>
  <id>127</id>
  <lieferschein>87</lieferschein>
  <artikel>1</artikel>
  <projekt>1</projekt>
  <bezeichnung>Muster</bezeichnung>
  <beschreibung />
  <internerkommentar />
  <nummer>1000001</nummer>
  <seriennummer />
  <menge>5.0000</menge>
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe>1</vpe>
  <sort>1</sort>
  <status>angelegt</status>
  <bemerkung />
  <geliefert>0.0000</geliefert>
  <abgerechnet>0</abgerechnet>
  <logdatei>2017-11-02 08:55:17</logdatei>
  <explodiert_parent_artikel>0</explodiert_parent_artikel>
  <einheit />
  <zolltarifnummer />
  <herkunftsland />
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
  <auftrag_position_id>226</auftrag_position_id>
  <kostenlos>0</kostenlos>
  <lagertext />
  <teilprojekt>0</teilprojekt>
  <explodiert_parent>0</explodiert_parent>
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
  <id_ext />
  <ean>4001222601064</ean>
  <gewicht />
  <herstellernummer />
  <altersfreigabe />
  <lagerartikel>0</lagerartikel>
  </lieferschein_position>
  <lieferschein_position>
  <id>128</id>
  <lieferschein>87</lieferschein>
  <artikel>3</artikel>
  <projekt>1</projekt>
  <bezeichnung>*** Einbauteil A</bezeichnung>
  <beschreibung>Lager: HL001(5)</beschreibung>
  <internerkommentar />
  <nummer>1000002</nummer>
  <seriennummer />
  <menge>5.0000</menge>
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe />
  <sort>2</sort>
  <status>angelegt</status>
  <bemerkung />
  <geliefert>0.0000</geliefert>
  <abgerechnet>0</abgerechnet>
  <logdatei>2017-11-02 08:55:17</logdatei>
  <explodiert_parent_artikel>1</explodiert_parent_artikel>
  <einheit />
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
  <auftrag_position_id>227</auftrag_position_id>
  <kostenlos>0</kostenlos>
  <lagertext>HL001 (5)</lagertext>
  <teilprojekt>0</teilprojekt>
  <explodiert_parent>127</explodiert_parent>
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
  <id_ext />
  <ean />
  <gewicht />
  <herstellernummer />
  <altersfreigabe />
  <lagerartikel>1</lagerartikel>
  </lieferschein_position>
  <lieferschein_position>
  <id>129</id>
  <lieferschein>87</lieferschein>
  <artikel>4</artikel>
  <projekt>1</projekt>
  <bezeichnung>*** Einbaukosten/Stk.</bezeichnung>
  <beschreibung />
  <internerkommentar />
  <nummer>1000004</nummer>
  <seriennummer />
  <menge>5.0000</menge>
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe />
  <sort>3</sort>
  <status>angelegt</status>
  <bemerkung />
  <geliefert>0.0000</geliefert>
  <abgerechnet>0</abgerechnet>
  <logdatei>2017-11-02 08:55:17</logdatei>
  <explodiert_parent_artikel>1</explodiert_parent_artikel>
  <einheit />
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
  <auftrag_position_id>228</auftrag_position_id>
  <kostenlos>0</kostenlos>
  <lagertext />
  <teilprojekt>0</teilprojekt>
  <explodiert_parent>127</explodiert_parent>
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
  <id_ext />
  <ean />
  <gewicht />
  <herstellernummer />
  <altersfreigabe />
  <lagerartikel>0</lagerartikel>
  </lieferschein_position>
  <lieferschein_position>
  <id>130</id>
  <lieferschein>87</lieferschein>
  <artikel>17</artikel>
  <projekt>1</projekt>
  <bezeichnung>*** Einbauteil B</bezeichnung>
  <beschreibung>Lager: HL001(10)</beschreibung>
  <internerkommentar />
  <nummer>1000008</nummer>
  <seriennummer />
  <menge>10.0000</menge>
  <lieferdatum>0000-00-00</lieferdatum>
  <vpe />
  <sort>4</sort>
  <status>angelegt</status>
  <bemerkung />
  <geliefert>0.0000</geliefert>
  <abgerechnet>0</abgerechnet>
  <logdatei>2017-11-02 08:55:17</logdatei>
  <explodiert_parent_artikel>1</explodiert_parent_artikel>
  <einheit />
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
  <auftrag_position_id>229</auftrag_position_id>
  <kostenlos>0</kostenlos>
  <lagertext>HL001 (10)</lagertext>
  <teilprojekt>0</teilprojekt>
  <explodiert_parent>127</explodiert_parent>
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
  <id_ext />
  <ean />
  <gewicht />
  <herstellernummer />
  <altersfreigabe />
  <lagerartikel>1</lagerartikel>
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
<xml>
```

#### Lagerbestände empfangen

> **Wichtig**
>
> Beachte bei diesem Übertragungsformat die Pflichtfelder *nummer* und *lagerzahl*.

Nutze die folgende XML-Struktur, um Lagerbestände von deinem Fulfillment-Dienstleister **ohne MHD- und Chargeninformationen** zu empfangen.

```
<?xmlversion="1.0"encoding="UTF-8"?>
<response>
  <xml>
  <artikel_list>
  <artikel>
  <nummer>123456</nummer>
  <lagerzahl>7</lagerzahl>
  <lager_platz>HL001</lager_platz>
  </artikel>
  </artikel_list>
  
</response>
<xml>
```Wenn du Lagerbestände **mit MHD- und Chargeninformationen** von deinem Fulfillment-Dienstleister empfangen möchtest, orientiere dich an folgender XML-Struktur. Beachte, dass in diesem Beispiel zwei unterschiedliche Mindesthaltbarkeitsdaten und Chargennummern für denselben Artikel dargestellt werden.```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response>
  <xml>
  <artikel_list>
  <artikel>
  <nummer>1650007</nummer>
  <lagerzahl>3</lagerzahl>
  <lager_platz>KR-HR-11</lager_platz>
  <mhd>30.10.2018</mhd>
  </artikel>
  <artikel>
  <nummer>1650007</nummer>
  <lagerzahl>3</lagerzahl>
  <lager_platz>KR-HR-12</lager_platz>
  <mhd>15.02.2019</mhd>
  </artikel>
  </artikel_list>
  
</response>
<xml>
```

#### Aufträge empfangen

Nutze die folgende XML-Struktur, um Aufträge von deinem Fulfillment-Dienstleister zu empfangen. Beachte, dass die Beispieldatei einen Einblick in die geforderte Struktur geben soll und recht umfangreich ist, da sie alle theoretisch möglichen Felder enthält, über die verschiedenste Auftragsinformationen übermittelt werden können.

```
  
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <xml>
  <auftrag_list>
  <auftrag>
  <datum>2021-05-03</datum>
  <art>standardauftrag</art>
  <projekt>1</projekt>
  <internet>OnlineBestellNummer</internet>
  <bearbeiter>Administrator</bearbeiter>
  <freitext>Freitext</freitext>
  <internebemerkung>Interne Bemerkung</internebemerkung>
  <status>freigegeben</status>
  <firma>0</firma>
  <titel>Dr.</titel>
  <name>Eva Müller</name>
  <abteilung>Abteilung</abteilung>
  <unterabteilung>Unterabteilung</unterabteilung>
  <strasse>Musterweg 12a</strasse>
  <adresszusatz>Adresszusatz</adresszusatz>
  <ansprechpartner>ASP</ansprechpartner>
  <plz>12345</plz>
  <ort>Musterdorf</ort>
  <land>DE</land>
  <ustid>DE11125205</ustid>
  <ust_befreit>3</ust_befreit>
  <email>testmail@xentral.com</email>
  <telefon>089123456789</telefon>
  <telefax>089123456790</telefax>
  <kundennummer>10001</kundennummer>
  <versandart>versandunternehmen</versandart>
  <vertrieb>Administrator</vertrieb>
  <zahlungsweise>rechnung</zahlungsweise>
  <zahlungszieltageskonto>11</zahlungszieltageskonto>
  <abweichendelieferadresse>1</abweichendelieferadresse>
  <liefername>Abweichender Name</liefername>
  <lieferabteilung>Abweichende Abteilung</lieferabteilung>
  <lieferunterabteilung>Abweichende Unterabteilung</lieferunterabteilung>
  <lieferland>DE</lieferland>
  <lieferstrasse>Abweichende Straße</lieferstrasse>
  <lieferort>Augsburg</lieferort>
  <lieferplz>86150</lieferplz>
  <lieferadresszusatz>Lieferzusatz</lieferadresszusatz>
  <lieferansprechpartner>Lieferansprechpartner</lieferansprechpartner>
  <transaktionsnummer>TRANSACTION-100</transaktionsnummer>
  <lieferdatum>2022-05-06</lieferdatum>
  <tatsaechlicheslieferdatum>2022-07-05</tatsaechlicheslieferdatum>
  <ihrebestellnummer>23234324</ihrebestellnummer>
  <anschreiben>1</anschreiben>
  <internebezeichnung>11</internebezeichnung>
  <lieferdatumkw>15</lieferdatumkw>
  <bundesland/>
  <gln></gln>
  <liefergln/>
  <lieferemail/>
  <bundesstaat/>
  <lieferbundesstaat/>
  <auftrag_position_list>
  <auftrag_position>
  <bezeichnung>Schraube Deluxe</bezeichnung>
  <beschreibung>&lt;ul&gt;&lt;li&gt;1 &lt;strong&gt;Fett&lt;/strong&gt; geschrieben.&lt;/li&gt;&lt;li&gt;2&lt;/li&gt;&lt;li&gt;3&lt;/li&gt;&lt;li&gt;4&lt;/li&gt;&lt;/ul&gt;</beschreibung>
  <internerkommentar/>
  <nummer>700001</nummer>
  <menge>3.0000</menge>
  <preis>0.55328000</preis>
  <lieferdatum>2022-05-05</lieferdatum>
  <freifeld1>Freifeld1</freifeld1>
  <freifeld2>Freifeld2</freifeld2>
  <freifeld3>Freifeld3</freifeld3>
  <freifeld4>Freifeld4</freifeld4>
  <freifeld5>Freifeld5</freifeld5>
  <freifeld6>Freifeld6</freifeld6>
  <freifeld7>Freifeld7</freifeld7>
  <freifeld8>Freifeld8</freifeld8>
  <freifeld9>Freifeld9</freifeld9>
  <freifeld10>Freifeld10</freifeld10>
  <freifeld11>Freifeld11</freifeld11>
  <freifeld12>Freifeld12</freifeld12>
  <freifeld13>Freifeld13</freifeld13>
  <freifeld14>Freifeld14</freifeld14>
  <freifeld15>Freifeld15</freifeld15>
  <freifeld16>Freifeld16</freifeld16>
  <freifeld17>Freifeld17</freifeld17>
  <freifeld18>Freifeld18</freifeld18>
  <freifeld19>Freifeld19</freifeld19>
  <freifeld20>Freifeld20</freifeld20>
  <freifeld21>Freifeld21</freifeld21>
  <freifeld22>Freifeld22</freifeld22>
  <freifeld23>Freifeld23</freifeld23>
  <freifeld24>Freifeld24</freifeld24>
  <freifeld25>Freifeld25</freifeld25>
  <freifeld26>Freifeld26</freifeld26>
  <freifeld27>Freifeld27</freifeld27>
  <freifeld28>Freifeld28</freifeld28>
  <freifeld29>Freifeld29</freifeld29>
  <freifeld30>Freifeld30</freifeld30>
  <freifeld31>Freifeld31</freifeld31>
  <freifeld32>Freifeld32</freifeld32>
  <freifeld33>Freifeld33</freifeld33>
  <freifeld34>Freifeld34</freifeld34>
  <freifeld35>Freifeld35</freifeld35>
  <freifeld36>Freifeld36</freifeld36>
  <freifeld37>Freifeld37</freifeld37>
  <freifeld38>Freifeld38</freifeld38>
  <freifeld39>Freifeld39</freifeld39>
  <freifeld40>Freifeld40</freifeld40>
  <ean/>
  </auftrag_position>
  </auftrag_position_list>
  </auftrag>
  </auftrag_list>
  <status>
  <action>belege</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
  </response>
<xml>
```

#### Bestellung empfangen

Nutze die folgende XML-Struktur, um Bestellungen von deinem Fulfillment-Dienstleister zu empfangen.

```
<?xmlversion="1.0"encoding="UTF-8"?>
<response>
  <xml>
  <bestellung_list>
  <bestellung>
  <id>30</id>
  <datum>2017-11-02</datum>
  <projekt>1</projekt>
  <bestellungsart />
  <belegnr>100023</belegnr>
  <bearbeiter>Administrator</bearbeiter>
  <angebot />
  <freitext>Bitte aufs Sperrlager einlagern</freitext>
  <internebemerkung />
  <status>versendet</status>
  <adresse>6</adresse>
  <name>Meine Firma</name>
  <vorname />
  <abteilung>Entwicklung/Produktion</abteilung>
  <unterabteilung />
  <strasse>Musterstrasse 6</strasse>
  <adresszusatz>Eingang C</adresszusatz>
  <plz>49646</plz>
  <ort>Musterhausen</ort>
  <land>DE</land>
  <abweichendelieferadresse>1</abweichendelieferadresse>
  <liefername>Testempfänger</liefername>
  <lieferabteilung>Logistik</lieferabteilung>
  <lieferunterabteilung />
  <lieferland>DE</lieferland>
  <lieferstrasse>Musterstrasse 7</lieferstrasse>
  <lieferort>Musterhausen</lieferort>
  <lieferplz>85344</lieferplz>
  <lieferadresszusatz>Tor 3</lieferadresszusatz>
  <lieferansprechpartner>Ansprechpartner Lieferadresse</lieferansprechpartner>
  <ustid>4648448649848</ustid>
  <ust_befreit>0</ust_befreit>
  <email>testmail@web.de</email>
  <telefon>082126841041</telefon>
  <telefax>081664644565</telefax>
  <betreff />
  <kundennummer />
  <lieferantennummer>70004</lieferantennummer>
  <versandart />
  <lieferdatum>0000-00-00</lieferdatum>
  <einkaeufer />
  <keineartikelnummern>0</keineartikelnummern>
  <zahlungsweise>rechnung</zahlungsweise>
  <zahlungsstatus />
  <zahlungszieltage>0</zahlungszieltage>
  <zahlungszieltageskonto>0</zahlungszieltageskonto>
  <zahlungszielskonto>0.00</zahlungszielskonto>
  <gesamtsumme>1.1900</gesamtsumme>
  <bank_inhaber />
  <bank_institut />
  <bank_blz>0</bank_blz>
  <bank_konto>0</bank_konto>
  <paypalaccount />
  <bestellbestaetigung>0</bestellbestaetigung>
  <firma>1</firma>
  <versendet>1</versendet>
  <versendet_am>2017-11-02 07:34:26</versendet_am>
  <versendet_per>sonstiges</versendet_per>
  <versendet_durch>Administrator</versendet_durch>
  <logdatei>2017-11-02 07:35:54</logdatei>
  <artikelnummerninfotext>0</artikelnummerninfotext>
  <ansprechpartner>Testansprechpartner</ansprechpartner>
  <anschreiben />
  <usereditid>1</usereditid>
  <useredittimestamp>2017-11-02 07:35:54</useredittimestamp>
  <steuersatz_normal>19.00</steuersatz_normal>
  <steuersatz_zwischen>7.00</steuersatz_zwischen>
  <steuersatz_ermaessigt>7.00</steuersatz_ermaessigt>
  <steuersatz_starkermaessigt>7.00</steuersatz_starkermaessigt>
  <steuersatz_dienstleistung>7.00</steuersatz_dienstleistung>
  <waehrung>EUR</waehrung>
  <bestellungohnepreis>0</bestellungohnepreis>
  <schreibschutz>1</schreibschutz>
  <pdfarchiviert>0</pdfarchiviert>
  <pdfarchiviertversion>0</pdfarchiviertversion>
  <typ>firma</typ>
  <verbindlichkeiteninfo />
  <ohne_briefpapier>0</ohne_briefpapier>
  <projektfiliale>0</projektfiliale>
  <bestellung_bestaetigt>0</bestellung_bestaetigt>
  <bestaetigteslieferdatum>0000-00-00</bestaetigteslieferdatum>
  <bestellungbestaetigtper>internet</bestellungbestaetigtper>
  <bestellungbestaetigtabnummer />
  <gewuenschteslieferdatum>0000-00-00</gewuenschteslieferdatum>
  <zuarchivieren>0</zuarchivieren>
  <internebezeichnung />
  <angelegtam>0000-00-00 00:00:00</angelegtam>
  <preisanfrageid>0</preisanfrageid>
  <sprache>deutsch</sprache>
  <kundennummerlieferant />
  <bodyzusatz />
  <lieferbedingung />
  <titel />
  <liefertitel />
  <skontobetrag>0.0000</skontobetrag>
  <langeartikelnummern>0</langeartikelnummern>
  <skontoberechnet>0</skontoberechnet>
  <id_ext />
  <anzahluebertragungen>1</anzahluebertragungen>
  <rabatt>0</rabatt>
  <gebuehr>0</gebuehr>
  <ust>0</ust>
  <bestellung_position_list>
  <bestellung_position>
  <id>31</id>
  <bestellung>30</bestellung>
  <artikel>10</artikel>
  <projekt>1</projekt>
  <bezeichnunglieferant>Steckverbindung c10</bezeichnunglieferant>
  <bestellnummer>Seriennummernartikel XY</bestellnummer>
  <beschreibung />
  <menge>2.0000</menge>
  <preis>0.50000000</preis>
  <waehrung>EUR</waehrung>
  <lieferdatum>2017-11-30</lieferdatum>
  <vpe>24</vpe>
  <sort>1</sort>
  <status>angelegt</status>
  <umsatzsteuer />
  <bemerkung />
  <geliefert>0.0000</geliefert>
  <mengemanuellgeliefertaktiviert>0</mengemanuellgeliefertaktiviert>
  <manuellgeliefertbearbeiter />
  <abgerechnet>0</abgerechnet>
  <logdatei>2017-11-02 07:29:13</logdatei>
  <abgeschlossen>0</abgeschlossen>
  <einheit />
  <zolltarifnummer>0</zolltarifnummer>
  <herkunftsland>0</herkunftsland>
  <artikelnummerkunde />
  <auftrag_position_id>0</auftrag_position_id>
  <preisanfrage_position_id>0</preisanfrage_position_id>
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
  <auswahlmenge>0.0000</auswahlmenge>
  <auswahletiketten>0</auswahletiketten>
  <auswahllagerplatz>0</auswahllagerplatz>
  <teilprojekt>0</teilprojekt>
  <steuersatz>-1.00</steuersatz>
  <steuertext />
  <erloese />
  <erloesefestschreiben>0</erloesefestschreiben>
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
  <skontobetrag>0.0000</skontobetrag>
  <id_ext />
  <ean />
  <gewicht />
  <herstellernummer />
  <altersfreigabe />
  <lagerartikel>1</lagerartikel>
  </bestellung_position>
  </bestellung_position_list>
  </bestellung>
  </bestellung_list>
  </xml>
  <status>
  <action>belege</action>
  <message>OK</message>
  <messageCode>1</messageCode>
  </status>
</response>
<xml>
```

#### Tracking-Informationen empfangen

Nutze die folgende XML-Struktur, um Sendungsnummern und Tracking-Links zu versendeten Aufträgen von deinem Fulfillment-Dienstleister zu empfangen. Bei dieser Beispielstruktur werden die Tracking-Informationen gesammelt an dein XentralSystem zurück übertragen.

```
<?xmlversion="1.0"encoding="UTF-8"?>
<response>
  <xml>
  <lieferschein_list>
  <lieferschein>
  <belegnr>200001</belegnr>
  <tracking>12345678901231</tracking>
  <tracking_link>https://nolp.dhl.de/nextt-online-public/de/search?piececode=12345678901231</tracking_link>
  <tracking_sprache>german</tracking_sprache>
  <lieferschein_position_list>
  <lieferschein_position>
  <id>1</id>
  <geliefert>12</geliefert>
  </lieferschein_position>
  <lieferschein_position>
  <id>2</id>
  <geliefert>2</geliefert>
  </lieferschein_position>
  </lieferschein_position_list>
  </lieferschein>
  <lieferschein>
  <belegnr>200001</belegnr>
  <tracking>12345678901232</tracking>
  <tracking_link>https://nolp.dhl.de/nextt-online-public/de/search?piececode=12345678901232</tracking_link>
  <tracking_sprache>german</tracking_sprache>
  <lieferschein_position_list>
  <lieferschein_position>
  <id>3</id>
  <geliefert>4</geliefert>
  </lieferschein_position>
  </lieferschein_position_list>
  </lieferschein>
  </lieferschein_list>
  
</response>
<xml>
```

#### Daten zu Mindesthaltbarkeit und Chargen empfangen

Nutze die folgende XML-Struktur, um Informationen zu MHD und Chargen zu importieren, die von deinem Fulfillment-Dienstleister an dich zurückgemeldet werden. Entscheide vorab, ob MHD- und Chargeninformationen einzeln oder gemeinsam in einem Block zusammengefasst werden sollen. Der Block kann bei mehrfachen Chargen / MHD-Kombinationen auch mehrfach mit den entsprechenden Teilmengen integriert werden. Die jeweilige Menge muss dazu jeweils innerhalb des Blocks angegeben werden. Wird im Block keine Menge angegeben und es ist nur ein Block vorhanden wird automatisch die Gesamtmenge der Positon zugeschrieben. Wenn mehrere Blöcke ohne Mengenangabe für eine Position vorhanden sind, werden die Angaben auf Grund der Nicht-Eindeutigkeit ignoriert.

> **Tipp**
>
> Möchtest du entnommenen Mindesthaltbarkeitsdaten, Chargen und Seriennummern in deinem PDF-Dokument aufführen, aktiviere im Menü **Grundeinstellungen > Tab: System > Bereich: Belege ** die Optionen**Positionen mit MHD **, ** Positionen mit Charge ** und **Positionen mit Seriennummern**.

> **Wichtig**
>
> Beachte bei diesem Übertragungsformat die Pflichtfelder *tracking* und *belegnr*. Sie müssen zwingend in der XML-Struktur enthalten sein.

##### Beispiel für die Rückmeldung von MHD und Charge innerhalb eines Blocks:

```
<?xmlversion="1.0"encoding="UTF-8"?>
<response>
  <xml>
  <lieferschein_list>
  <lieferschein>
  <belegnr>121212</belegnr>
  <tracking>1234567890</tracking>
  <tracking_link>http://dhl.de/sendungsverfolgung?tracking=123456</tracking_link>
  <tracking_sprache>english</tracking_sprache>
  <versandart>DPD</versandart>
  <lieferschein_position_list>
  <lieferschein_position>
  <id>105</id>
  <geliefert>3</geliefert>
  <serial>SN-123456</serial>
  <serial>SN-654321</serial>
  <serial>SN-456789</serial>
  <mhd_charge_block>
  <mhd>2020-12-31</mhd>
  <charge>ABC123</charge>
  <menge>2</menge>
  </mhd_charge_block>
  <mhd_charge_block>
  <mhd>2022-12-31</mhd>
  <charge>DEF456</charge>
  <menge>1</menge>
  </mhd_charge_block>
  </lieferschein_position>
  </lieferschein_position_list>
  </lieferschein>
  </lieferschein_list>
  
</response>
<xml>
```##### Beispiel für die Rückmeldung von MHD und Charge für jeden einzelnen Auftrag:```
<?xmlversion="1.0"encoding="UTF-8"?>
<response>
  <xml>
  <lieferschein_list>
  <lieferschein>
  <auftragextid>78787878</auftragextid>
  <tracking>1234567890</tracking>
  <tracking_link>http://dhl.de/sendungsverfolgung?tracking=123456</tracking_link>
  <tracking_sprache>english</tracking_sprache> 
  </lieferschein>
  </lieferschein_list>
  
</response>
<xml>
```

## Verfügbare Datenfelder für den XML-Import von Belegen

Wenn du eingehende Daten von deinem Fulfillment-Dienstleister per XML erhältst, ist es wichtig zu wissen, welche Datenfelder pro Beleg gefüllt werden können. Je nach Belegtyp gibt es Limitierungen bezüglich der verfügbaren Datenfelder für die Übertragung. Die folgende Tabelle zeigt dir übersichtlich auf, welche Datenfelder du pro Beleg nutzen kannst. Nutze diese Informationen, um die XML-Strukturen für deine Übertragungen entsprechend aufzubauen und Fehler bei der Datenübertragung zu vermeiden.

| Datenfeld | Auftrag | Angebot | Retoure | Bestellung | Produktion |
| --- | --- | --- | --- | --- | --- |
| auftrag | | | | | | |
| |
| auftragid | | | | | | |
| |
| lieferschein | | | | | | |
| |
| lieferscheinid | | | | | | |
| |
| fastlane | | | | | | |
| |
| shopextid | | | | | | | |
| |
| |
| kostenstelle | | | | | | | | |
| |
| |
| |
| belegnr | | | | | | | | |
| |
| |
| |
| name | | | | | | | | | | |
| |
| |
| |
| |
| |
| abteilung | | | | | | | | | | |
| |
| |
| |
| |
| |
| unterabteilung | | | | | | | | | | |
| |
| |
| |
| |
| |
| ansprechpartner | | | | | | | | | | |
| |
| |
| |
| |
| |
| strasse | | | | | | | | | | |
| |
| |
| |
| |
| |
| bundesstaat | | | | | | | | | | |
| |
| |
| |
| |
| |
| land | | | | | | | | | | |
| |
| |
| |
| |
| |
| plz | | | | | | | | | | |
| |
| |
| |
| |
| |
| ort | | | | | | | | | | |
| |
| |
| |
| |
| |
| email | | | | | | | | | | |
| |
| |
| |
| |
| |
| telefon | | | | | | | | | | |
| |
| |
| |
| |
| |
| telefax | | | | | | | | | | |
| |
| |
| |
| |
| |
| abweichendelieferadresse | | | | | | | | | | |
| |
| |
| |
| |
| |
| art | | | | | | | | |
| |
| |
| |
| bearbeiter | | | | | | | | | | |
| |
| |
| |
| |
| |
| datum | | | | | | | | | | |
| |
| |
| |
| |
| |
| lieferdatum | | | | | | | | |
| |
| |
| |
| tatsaechlicheslieferdatum | | | | | | | |
| |
| |
| ustid | | | | | | | | | | |
| |
| |
| |
| |
| |
| ust_befreit | | | | | | | | | |
| |
| |
| |
| |
| internet | | | | | | | |
| |
| |
| transaktionsnummer | | | | | | | |
| |
| |
| versandart | | | | | | | | | |
| |
| |
| |
| |
| vertrieb | | | | | | | | |
| |
| |
| |
| zahlungsweise | | | | | | | | |
| |
| |
| |
| freitext | | | | | | | | | | |
| |
| |
| |
| |
| |
| vorabbezahltmarkieren | | | | | | |
| |
| liefername | | | | | | | | | | |
| |
| |
| |
| |
| |
| liefergln | | | | | | | |
| |
| |
| ihrebestellnummer | | | | | | |
| |
| internebemerkung | | | | | | | | |
| |
| |
| |
| internebezeichnung | | | | | | | | |
| |
| |
| |
| projekt | | | | | | | | |
| |
| |
| |
| gesamtsumme | | | | | | | |
| |
| |
| bestellungsart | | | | | | |
| |
| unterlistenexplodieren | | | | | | |
| |

## Häufige Fehlermeldungen und Verbindungsprobleme

Im Folgenden haben wir einige Empfehlungen und Hinweise auf häufige Fehlerursachen gesammelt, die du beachten solltest, um Fehler beim Datenaustausch zu verhindern.

### Fehlermeldung “Invalid Server Configuration”

Diese Meldung wird im[Monitor](https://help.xentral.com/hc/de/articles/16164850902428#UUID-2e4e5ae1-18e2-8825-e29e-b9ecc181152a_id_ArbeitenmitdembertragungenModul-bertragungenmitdemMonitorberwachen)im Feld **Status** einer Übertragung angezeigt und kann mehrere Ursachen im Bereich der Netzwerkkonfiguration haben. Überprüfe folgende Punkte und nimm gegebenenfalls Anpassungen vor, um die Ursache des Fehlers zu beheben.

- **Geänderte IP-Adresse**: Hat sich die IP-Adresse deines Xentral Systems geändert? Wir empfehlen, die Vergabe einer so genannten statischen IP-Adresse zu beantragen. Frage diese bei unserem Xentral Support an, damit sie für dein System dauerhaft vergeben wird. Sende außerdem deinem Fulfillment-Dienstleister deine statische IP-Adresse, damit er diese bei Bedarf in die Whitelist seiner Serverkonfiguration aufnehmen und somit die Verbindung erlauben kann.
- **Firewall-Einstellungen**: Bei ausgehenden sowie eingehenden Übertragungen kann es zu Fehlern kommen, wenn die Verbindungen durch eine Firewall blockiert werden. Überprüfe bei fehlerhaften eingehenden Übertragungen deine eigenen Firewall-Einstellungen und passe diese an.

### Fehlermeldung “Server / Dateisystem nicht erreichbar”

Diese Meldung wird im[Monitor](https://help.xentral.com/hc/de/articles/16164850902428#UUID-2e4e5ae1-18e2-8825-e29e-b9ecc181152a_id_ArbeitenmitdembertragungenModul-bertragungenmitdemMonitorberwachen)im Feld **Status ** einer Übertragung angezeigt und deutet auf Fehler bei der Kommunikation mit dem gemeinsam genutzten Server für den Datenaustausch hin. In einigen Fällen kommt es ohne Fehlermeldung dazu, dass keine Übertragungen mehr stattfinden. Ein ungewöhnlich lang zurückliegender Zeitpunkt im Feld**Letzte Übertragung** des Monitors deutet darauf hin. Folgendes solltest du überprüfen:

- **Zu viele Dateien im Antwort-Speicherort **: Bei eingehenden Übertragungen kann es vorkommen, dass der Ordner, in dem die zurückgemeldeten Dateien vom Fulfillment-Dienstleister abgelegt werden, zu viele Dateien enthält. Meist tritt der Fehler bei einigen Tausend Dateien auf. Du kannst das Problem verhindern, indem du im Tab ** Details **jeder eingehenden Übertragung die Option ** Löschen vom Server nach Download** aktivierst. So kann es gar nicht erst dazu kommen, dass sich zu große Datenmengen ansammeln.
- **Fehlerhafte Zugangsdaten **: Es ist möglich, dass sich die Zugangsdaten zum gemeinsam genutzten Server zwischenzeitlich geändert haben und die neuen Daten noch nicht in Xentral eingetragen wurden. Öffne das Tab ** Details **der betroffenen Übertragung und prüfe die Einträge in den Feldern ** Username **und ** Passwort**. Tools wie [Cyberduck](https://cyberduck.io/) oder [Filezilla](https://filezilla-project.org/) ermöglichen dir, schnell und einfach die Zugangsdaten zu prüfen. Sprich dich zudem mit deinem Fulfillment-Dienstleister ab, um sicherzustellen, dass du die korrekten Anmeldedaten verwendest.
- **Fehlerhafte Pfadangabe **: Wenn der Speicherort für ein- oder ausgehende Übertragungen nicht korrekt eingegeben wurde, können übermittelte Dateien nicht korrekt erkannt werden. Es kommt zu oben genannten Fehlermeldung oder die Übertragungen bleiben komplett aus. Überprüfe bei eingehenden Übertragungen das Feld ** Antwort-Speicherort (Eingang)**und bei ausgehenden Übertragungen das Feld ** Speicherort (Ausgang)**. Stelle außerdem sicher, dass der Pfad nicht versehentlich im Feld ** Server** angegeben wurde.