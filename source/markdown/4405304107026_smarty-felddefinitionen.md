In diesem Artikel findest du eine vollständige Auflistung der verfügbaren Felder inkl. einer Übersetzung der Feldnamen und einer Beschreibung der Inhalte in Englisch.

## Smarty im Übertragen-Modul

### Lieferschein

| XML Tag | XML Tag Translated | Required | Data type | Business description |
| --- | --- | --- | --- | --- |
| <?xml version="1.0" encoding="UTF-8"?> | | x | | |
| <response> | | x | | |
| <xml> | | x | | |
| <lieferschein_list> | delivery note list | x | | |
| <lieferschein> | delivery note | (x) | | |
| <id>68</id> | id | (x) | integer(11) | Internal ID |
| <datum>2020-10-22</datum> | date | | Date | Document date in format yyyy-mm-dd |
| <projekt>6</projekt> | project | | alphanumeric(222) | Internal ID of the project the document is assigned to. |
| <lieferscheinart/> | delivery note type | | alphanumeric(255) | Dispatch note type |
| <belegnr>300065</belegnr> | voucher number | | alphanumeric(255) | Document number |
| <bearbeiter>Firstname Lastname</bearbeiter> | processor | | alphanumeric(255) | Accountant |
| <auftrag>200063</auftrag> | order | | alphanumeric(255) | Order number |
| <auftragid>67</auftragid> | orderid | | integer(11) | Internal order number |
| <freitext/> | free text | | text | Free text field |
| <status>versendet</status> | status | | alphanumeric(64) | Status, possible values: versendet, freigegeben |
| <adresse>47</adresse> | address | | integer(11) | Referenced address ID |
| <name>Test Adresse</name> | name | | alphanumeric(255) | Recipient name |
| <abteilung/> | department | | alphanumeric(255) | Recipient department |
| <unterabteilung/> | sub department | | alphanumeric(255) | Recipient sub department |
| <strasse>Teststraße 11</strasse> | street | | alphanumeric(255) | Recipient street |
| <adresszusatz/> | address | | alphanumeric(255) | Recipient address amendment |
| <ansprechpartner/> | contact person | | alphanumeric(255) | Recipient contact person |
| <plz>86150</plz> | plz | | alphanumeric(255) | Recipient ZIP code |
| <ort>Augsburg</ort> | location | | alphanumeric(255) | Recipient city |
| <land>DE</land> | country | | alphanumeric(255) | Recipient country |
| <ustid/> | ustid | | alphanumeric(255) | Recipient VAT no. |
| <email>name@example.com</email> | email | | alphanumeric(255) | Recipient mail address |
| <telefon/> | phone | | alphanumeric(255) | Recipient phone number |
| <telefax/> | telefax | | alphanumeric(255) | Recipient fax number |
| <betreff/> | subject | | alphanumeric(255) | Recipient subject |
| <kundennummer>10032</kundennummer> | customer number | | alphanumeric(64) | Recipient customer number |
| <versandart>versandunternehmen</versandart> | shipping method | | alphanumeric(255) | Shipping method |
| <versand>Firstname Lastname</versand> | shipping | | alphanumeric(255) | Individual field |
| <firma>1</firma> | company | | integer(11) | Flag, if customer is a company |
| <versendet>1</versendet> | shipped | | int(1)/boolean | Flag, if document was sent via email/printed |
| <versendet_am>0000-00-00 00:00:00</versendet_am> | versendet am | | Datetime | Document delivery date in format yyyy-mm-dd hh24:MM:SS |
| <versendet_per/> | sent by | | alphanumeric(255) | Delivered with |
| <versendet_durch/> | sent by | | alphanumeric(255) | Delivered by |
| <inbearbeitung_user>0 </inbearbeitung_user> | editing user | | int(1)/boolean | Individual field |
| <logdatei>2020-10-27 14:56:39</logdatei> | logdatei | | timestamp | Date and time of log file in format yyyy-mm-dd HH24:MI:SS |
| <vertriebid>10</vertriebid> | salesid | | integer(11) | Internal sales ID |
| <vertrieb>Firstname Lastname</vertrieb> | sales | | alphanumeric(255) | Internal sales person |
| <ust_befreit>0</ust_befreit> | ust exempt | | int(1)/boolean | Flag, if customer is VAT-free |
| <ihrebestellnummer/> | your order number | | alphanumeric(255) | Order number of the customer |
| <anschreiben/> | letter | | alphanumeric(255) | title of the person, e.g. Dear Mr. Max Muster |
| <usereditid>1</usereditid> | useredit id | | integer(11) | User ID, who edited the document at last |
| <useredittimestamp>2020-10-27 14:56:39</useredittimestamp> | useredit timestamp | | timestamp | Timestamp of last of last user edit in format yyyy-mm-dd HH24:MI:SS |
| <lieferantenretoure>0</lieferantenretoure> | vendor return | | tinyint(1) | Flag, if it is a return delivery |
| <lieferantenretoureinfo/> | vendor return info | | text | Description of return delivery |
| <lieferant>0</lieferant> | vendor | | integer(11) | Internal distributor ID |
| <schreibschutz>1</schreibschutz> | writeprotect | | int(1)/boolean | Flag, if document is write protected |
| <pdfarchiviert>0</pdfarchiviert> | pdf archived | | int(1)/boolean | Flag, if document PDF has been archived |
| <pdfarchiviertversion>0 </pdfarchiviertversion> | pdf archived version | | integer(11) | Version number of archived Pdf |
| <typ>firma</typ> | type | | alphanumeric(255) | Type |
| <internebemerkung/> | internal note | | alphanumeric(255) | Internal remark |
| <ohne_briefpapier>0</ohne_briefpapier> | without stationery | | int(1)/boolean | Flag, if document is printed with/without letterhead |
| <lieferid>0</lieferid> | delivery id | | integer(11) | Internal delivery ID |
| <ansprechpartnerid>0</ansprechpartnerid> | contact id | | integer(11) | ID of the contact person |
| <projektfiliale>0</projektfiliale> | project branch | | integer(11) | Project branch |
| <projektfiliale_eingelagert>0 </projektfiliale_eingelagert> | project filial stored | | int(1)/boolean | In stock at project branch |
| <zuarchivieren>0</zuarchivieren> | to archive | | int(1)/boolean | Flag, if to be archived |
| <internebezeichnung/> | internal designation | | alphanumeric(255) | Internal name |
| <angelegtam/> | createdon | | datetime | Document issue date in format yyyy-mm-dd hh24:mi:ss |
| <kommissionierung>26</kommissionierung> | picking | | integer(11) | Commissioning |
| <sprache>deutsch</sprache> | language | | alphanumeric(32) | Language |
| <bundesland/> | state | | alphanumeric(64) | Federal province in Germany |
| <gln/> | gln | | alphanumeric(64) | Global Location Number |
| <rechnungid>30</rechnungid> | invoice id | | integer(11) | Internal invoice ID |
| <bearbeiterid>10</bearbeiterid> | agent id | | integer(11) | Internal accountant ID |
| <keinerechnung>0</keinerechnung> | no invoice | | int(1)/boolean | Invoice / no invoice-Flag |
| <ohne_artikeltext>0</ohne_artikeltext> | without itemtext | | int(1)/boolean | Flag, if product has a name or not |
| <abweichendebezeichnung>0 </abweichendebezeichnung> | different name | | int(1)/boolean | Flag, if product has a different name |
| <kostenstelle/> | cost center | | alphanumeric(10) | Cost center |
| <bodyzusatz/> | body addendum | | text | Amendment of the body |
| <lieferbedingung/> | delivery condition | | text | Delivery condition |
| <titel/> | title | | alphanumeric(64) | Title |
| <standardlager>0</standardlager> | standard warehouse | | int(1)/boolean | Default warehouse ID |
| <kommissionskonsignationslager>0 </kommissionskonsignationslager> | commission consignment warehouse | | int(1)/boolean | Consignment warehouse ID for commissioning |
| <bundesstaat/> | state | | alphanumeric(32) | Recipient federal state |
| <teillieferungvon>0</teillieferungvon> | part deliveryof | | integer(11) | Partial delivery |
| <teillieferungnummer>0</teillieferungnummer> | part deliverynumber | | integer(11) | Position number of partial delivery |
| <kiste>1</kiste> | box | | integer(11) | Box number |
| <id_ext/> | id ext | | alphanumeric | External ID |
| <anzahluebertragungen>1</anzahluebertragungen> | numberofdeliveries | | numeric | Number of transmissions |
| <tatsaechlicheslieferdatum/> | actual delivery date | | date | Effective delivery date in format yyyy-mm-dd |
| <lieferdatum/> | delivery date | | date | Delivery date in format yyyy-mm-dd |
| <lieferdatumkw>0</lieferdatumkw> | delivery datekw | | tinyint(1) | Calendar week of delivery date |
| <rechnung_name>HC Test Adresse</rechnung_name> | invoice name | | alphanumeric(255) | Invoice name |
| <auftrag_name>HC Test Adresse</auftrag_name> | order name | | alphanumeric(255) | Order name |
| <rechnung_anrede/> | invoice address | | alphanumeric(255) | Invoice salutation |
| <auftrag_anrede/> | order address | | alphanumeric(255) | Order salutation |
| <rechnung_strasse>Teststraße 11</rechnung_strasse> | invoice street | | alphanumeric(255) | Invoice street |
| <auftrag_strasse>Teststraße 11</auftrag_strasse> | order street | | alphanumeric(255) | Order street |
| <rechnung_adresszusatz/> | invoice address | | alphanumeric(255) | Invoice address amendment |
| <auftrag_adresszusatz/> | order address address | | alphanumeric(255) | Order address amendment |
| <rechnung_ansprechpartner/> | invoice address address | | alphanumeric(255) | Invoice contact person |
| <auftrag_ansprechpartner/> | order address address | | alphanumeric(255) | Order contact person |
| <rechnung_abteilung/> | invoice department | | alphanumeric(255) | Invoice department |
| <auftrag_abteilung/> | order department | | alphanumeric(255) | Order department |
| <rechnung_unterabteilung/> | invoice subdepartment | | alphanumeric(255) | Invoice sub department |
| <auftrag_unterabteilung/> | order subdepartment | | alphanumeric(255) | Order sub department |
| <rechnung_plz>86150</rechnung_plz> | invoice plz | | alphanumeric(255) | Invoice ZIP code |
| <auftrag_plz>86150</auftrag_plz> | invoice plz | | alphanumeric(255) | Order ZIP code |
| <rechnung_ort>Augsburg</rechnung_ort> | invoice location | | alphanumeric(255) | Invoice city |
| <auftrag_ort>Augsburg</auftrag_ort> | order place | | alphanumeric(255) | Order city |
| <rechnung_land>DE</rechnung_land> | invoice country | | alphanumeric(255) | Invoice country |
| <auftrag_land>DE</auftrag_land> | order country | | alphanumeric(255) | Order country |
| <rechnung_gln/> | invoice gln | | alphanumeric(64) | Invoice GLN |
| <auftrag_gln/> | order gln | | alphanumeric(64) | Order GLN |
| <internet/> | internet | | alphanumeric(255) | Internet ID, e.g. order no. of online shop |
| <shopextid/> | shopextid | | alphanumeric(1024) | External shop ID |
| <auftragextid/> | order xtid | | alphanumeric(255) | Reference of the connected order |
| <tracking>TESTDN-300065</tracking> | tracking | | alphanumeric(255) | Tracking ID of shipment |
| <lieferschein_position_list> | delivery note item list | (x) | - | - |
| <lieferschein_position> | delivery note item | (x) | - | - |
| <id>74</id> | id | (x) | integer(10) | Internal dispatch note position ID |
| <lieferschein>68</lieferschein> | delivery note | | integer(11) | Dispatch note ID |
| <artikel>17</artikel> | article | | integer(11) | Internal product number |
| <projekt>1</projekt> | project | | integer(11) | Internal ID of the project the document is assigned to. |
| <bezeichnung>MHD/Charge Test</bezeichnung> | article name | | alphanumeric(255) | Product name |
| <beschreibung/> | article description | | text | Description |
| <internerkommentar/> | internal comment | | text | Internal comment |
| <nummer>1000003</nummer> | nummer | | alphanumeric(255) | Product number within Xentral |
| <seriennummer/> | serial number | | alphanumeric(255) | Serial number |
| <menge>1.0000</menge> | quantity | | decimal(14) | Amount |
| <lieferdatum>0000-00-00</lieferdatum> | delivery date | | date | Delivery date in format: yyyy-mm-dd |
| <vpe>1</vpe> | vpe | | int(1)/boolean | Packing unit |
| <sort>1</sort> | sort | | integer(10) | Sorting number |
| <status>angelegt</status> | status | | alphanumeric(64) | Status: Possible values: |
| <bemerkung/> | note | | text | Remark |
| <geliefert>1.0000</geliefert> | delivered | | decimal(14) | Delivered amount |
| <abgerechnet>0</abgerechnet> | accounted | | int(1)/boolean | Billed-flag |
| <logdatei>2020-10-22 10:16:08</logdatei> | logdatei | | timestamp | Logfile datime |
| <explodiert_parent_artikel>0</explodiert_parent_artikel> | exploded parent item | | integer(11) | Flag if article is a part of a set-article |
| <einheit/> | unit | | alphanumeric(255) | Packaging unit |
| <zolltarifnummer/> | customs tariff number | | alphanumeric(128) | Customs tariff number |
| <herkunftsland/> | country of origin | | alphanumeric(128) | Country of origination |
| <artikelnummerkunde/> | article number customer | | alphanumeric(128) | Customer article number |
| <freifeld1>1</freifeld1> | freefield1 | | text | Free field 1 |
| <freifeld2>Tsubashi</freifeld2> | freefield2 | | text | Free field 2 |
| <freifeld3/> | freefield3 | | text | Free field 3 |
| <freifeld4/> | freefield4 | | text | Free field 4 |
| <freifeld5/> | freefield5 | | text | Free field 5 |
| <freifeld6/> | freefield6 | | text | Free field 6 |
| <freifeld7/> | freefield7 | | text | Free field 7 |
| <freifeld8/> | freefield8 | | text | Free field 8 |
| <freifeld9/> | freefield9 | | text | Free field 9 |
| <freifeld10/> | freefield10 | | text | Free field 10 |
| <lieferdatumkw>0</lieferdatumkw> | delivery date week | | tinyint(1) | Calendar week of delivery date |
| <auftrag_position_id>143</auftrag_position_id> | order item id | | integer(11) | Order position number |
| <kostenlos>0</kostenlos> | free | | tinyint(1) | Free of charge flag |
| <lagertext>PLANZER (1)</lagertext> | stock text | | alphanumeric(255) | Warehouse name |
| <teilprojekt>0</teilprojekt> | part project | | integer(11) | Internal sub project ID |
| <explodiert_parent>0</explodiert_parent> | exploded parent | | integer(11) | Flag if article is a part of a set-article |
| <freifeld11/> | freefield11 | | text | Free field 11 |
| <freifeld12/> | freefield12 | | text | Free field 12 |
| <freifeld13/> | freefield13 | | text | Free field 13 |
| <freifeld14/> | freefield14 | | text | Free field 14 |
| <freifeld15/> | freefield15 | | text | Free field 15 |
| <freifeld16/> | freefield16 | | text | Free field 16 |
| <freifeld17/> | freefield17 | | text | Free field 17 |
| <freifeld18/> | freefield18 | | text | Free field 18 |
| <freifeld19/> | freefield19 | | text | Free field 19 |
| <freifeld20/> | freefield20 | | text | Free field 20 |
| <freifeld21/> | freefield21 | | text | Free field 21 |
| <freifeld22/> | freefield22 | | text | Free field 22 |
| <freifeld23/> | freefield23 | | text | Free field 23 |
| <freifeld24/> | freefield24 | | text | Free field 24 |
| <freifeld25/> | freefield25 | | text | Free field 25 |
| <freifeld26/> | freefield26 | | text | Free field 26 |
| <freifeld27/> | freefield27 | | text | Free field 27 |
| <freifeld28/> | freefield28 | | text | Free field 28 |
| <freifeld29/> | freefield29 | | text | Free field 29 |
| <freifeld30/> | freefield30 | | text | Free field 30 |
| <freifeld31/> | freefield31 | | text | Free field 31 |
| <freifeld32/> | freefield32 | | text | Free field 32 |
| <freifeld33/> | freefield33 | | text | Free field 33 |
| <freifeld34/> | freefield34 | | text | Free field 34 |
| <freifeld35/> | freefield35 | | text | Free field 35 |
| <freifeld36/> | freefield36 | | text | Free field 36 |
| <freifeld37/> | freefield37 | | text | Free field 37 |
| <freifeld38/> | freefield38 | | text | Free field 38 |
| <freifeld39/> | freefield39 | | text | Free field 39 |
| <freifeld40/> | freefield40 | | text | Free field 40 |
| <zolleinzelwert>0.00000000</zolleinzelwert> | customs single value | | decimal(18) | Customs detail value |
| <zollgesamtwert>0.00000000</zollgesamtwert> | total customs value | | decimal(18) | Customs overall value |
| <zollwaehrung/> | customs currency | | alphanumeric(3) | Customs currency |
| <zolleinzelgewicht>0.00000000</zolleinzelgewicht> | customs weight | | decimal(18) | Customs detail weight |
| <zollgesamtgewicht>0.00000000</zollgesamtgewicht> | customs total weight | | decimal(18) | Customs overall weight |
| <nve/> | nve | | alphanumeric(255) | Globally unique Serial Shipping Container Code |
| <packstueck/> | package | | alphanumeric(255) | Packaging item |
| <vpemenge>0.0000</vpemenge> | vpe quantity | | decimal(14) | Amount of packaging units |
| <einzelstueckmenge>0.0000</einzelstueckmenge> | item quantity | | decimal(14) | Amount of individual items |
| <ausblenden_im_pdf>0</ausblenden_im_pdf> | hide in pdf | | tinyint1) | Flag to hide product in the PDF document |
| <id_ext/> | id ext | | alphanumeric | External ID |
| <ean/> | ean | | alphanumeric(1024) | EAN |
| <gewicht/> | weight | | alphanumeric(255) | Weight |
| <herstellernummer/> | manufacturer number | | alphanumeric(255) | Manufacturer number |
| <altersfreigabe/> | age rating | | alphanumeric(3) | Age restriction flag (0, 16, 18) |
| <lagerartikel>1</lagerartikel> | stock item | | int(1)/boolean | Flag if article is on stock |
| </lieferschein_position> | /delivery note item | (x) | | |
| </lieferschein_position_list> | /delivery note item list | (x) | | |
| </lieferschein> | /delivery note | (x) | | |
| </lieferschein_list> | /delivery note list | x | | |
| </xml> | | x | | |
| <status> | | x | | |
| <action>belege</action> | | x | alphanumeric | Static value |
| <message>OK</message> | | x | alphanumeric | Message text: Possible values: OK, |
| <messageCode>1</messageCode> | | x | numeric | Message Code |
| </status> | | x | | |
| </response> | | x | | |

> **Anmerkung**
>
> Unter **Übertragungsspezifische Einstellungen** steht für den Dateinamen nur {BELEGNR}.csv zur Verfügung.

### Tracking Rückmeldung

| XML Tag | XML Tag Translated | Required | Data type | Business description |
| --- | --- | --- | --- | --- |
| <?xml version="1.0" encoding="UTF-8"?> | | x | | |
| <response> | | x | | |
| <xml> | | x | | |
| <lieferschein_list> | delivery note list | x | | |
| <lieferschein> | delivery note | x | | |
| <belegnr>121212</belegnr> | document number | x | alphanumeric(255) | Document number |
| <tracking>1234567890</tracking> | tracking number | x | alphanumeric(255) | Tracking number of the actual carrier |
| <tracking_link>http://dhl.de/sendungsverfolgung?tracking=123456</tracking_link> | tracking link | | alphanumeric(255) | Tracking-Link |
| <tracking_sprache>english</tracking_sprache> | tracking language | | alphanumeric(255) | Language flag of the tracking(number) |
| <versandart>DPD</versandart> | carrier or shipment type | | alphanumeric(255) | Carrier name (Typ) that is used in Xentral |
| <lieferschein_position_list> | delivery note position list | (x) | | |
| <lieferschein_position> | delivery note position | (x) | | |
| <id>105</id> | id | (x) | numeric(10) | Database-ID of the products position within the document. Needed for pro |
| <geliefert>3</geliefert> | shipped | | decimal(14) | Amount/pieces |
| <serial>SN-123456</serial> | serial | (x) | alphanumeric(255) | Serial number, can be one or multiple lines |
| <mhd_charge_block> | block containing charge or lot | (x) | | Block containing charge or lot information, can be one or multiple lines |
| <mhd>2020-12-31</mhd> | bbd (best before date) | (x) | alphanumeric(255) | Best-Before-Date |
| <charge>ABC123</charge> | charge or lot | (x) | alphanumeric(255) | Batch number |
| <menge>2</menge> | quantity | | decimal(14) | Amount/pieces |
| </mhd_charge_block> | /block containing charge or lot | (x) | | End of block |
| </lieferschein_position> | /delivery note position | x | | |
| </lieferschein_position_list> | /delivery note position list | x | | |
| </lieferschein> | /delivery note | x | | |
| </lieferschein_list> | /delivery note list | x | | |
| </xml> | | x | | |
| </response> | | x | | |

### Lagerzahlen-Rückmeldung

| XML Tag | XML Tag Translated | Required | Data type | Business description |
| --- | --- | --- | --- | --- |
| <?xml version="1.0" encoding="UTF-8" standalone="yes"?> | | x | | |
| <response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> | | x | | |
| <xml> | | x | | |
| <artikel_list> | artikel list | x | | Product list tag open |
| <artikel> | artikel | x | | Product tag open |
| <nummer>1000012</nummer> | number | x | alphanumeric(255) | Xentral product number |
| <lagerzahl>3</lagerzahl> | stock inventory quantity | x | decimal(14) | Amount of products picked from the storage location |
| <lager_platz>Lagerplatz1</lager_platz> | stock inventory bin | (x) | alphanumeric(255) | Name of the storage location that is connected with the product |
| <mhd>30.10.2018</mhd> | bbd (best before date) | | alphanumeric(255) | Use-by date in format dd.mm.yyyy |
| <charge>TEST1</charge> | charge or lot | | alphanumeric(255) | Batch name |
| </artikel> | /article | x | | Product tag close |
| </artikel_list> | /article list | x | | Product list tag close |
| </xml> | | x | | |
| </response> | | x | | |

## Smarty im Shopimporter

### Headerdaten

| Field Name | Field Name Translated | Example Value | Required | Business Description |
| --- | --- | --- | --- | --- |
| zeitstempel | timestamp | 2020-10-10 12:00:00 | | For importers which use the „Ab Datum“ mode this field sets the exact value of the orders date. If the field is missing, the process uses the current date as the order date which may cause orders to be skipped |
| bestelldatum | order date | 2020-10-10 | | The actual date the order was made in the shop. This gets displayed in the Xentral orders as the “ordering date” |
| lieferdatum | delivery date | 2020-10-10 | | The (expected) delivery date of the order |
| auftrag | order | 100 | x | The technical ID (not the number) of the order. This information is relevant for order updates, e.g. by using the functions ImportDeleteAuftrag() or ImportUpdateAuftrag() |
| onlinebestellnummer | online order number | #UK12345 | x | The order number visible in the shop - occasionally it may be identical to the order ID |
| subshop | subshop | 1 | | The ID of the subshop this order originated from. On occasions it may be a string |
| useorderid | useorderid | 1 | | If this field is set and the import mode is set to “Ab Nummer” then the number which gets incremented after an import is not the value in the “auftrag” field but instead the value in the “onlinebestellnummer” field |
| onlinebestellnummerueberschreiben | overwrite online order number | 1 | | Gets used by the process “shopimport_auftragarchiv”. Has the same effect for it as the field “userorderid” for the regular import |
| benutzergruppe | user group | Powerseller | | If the address this order gets mapped to is supposed to be added to a certain group in Xentral this field holds the name of the target group |
| benutzergruppekuerzel | user group code | PS | | If the address this order gets mapped to is supposed to be added to a certain group in Xentral this field holds the shorthand of the target group |
| benutzergruppeanlegen | create user group | 1 | | If the group given in the above fields does not exist a value of 1 in this field will create it in Xentral and the cause the address to added to it, 0 otherwise |
| geburtstag | birthday | 2000-12-20 | | The buyers birthday |
| telefon | phone | 123456789 | | The phone number which is to be saved to the address |
| name | name | Max Power / Compuglobal | x | Name of the person who should receive the invoice. If the invoice goes out to a company, the company name gets saved in this field |
| anrede | salutation | firma / herr / frau | | Type of the address, whether it is a company, man, or woman. If more types are defined in the general settings those can be used as well |
| ansprechpartner | contact | Max Mustermann | | If the address is for a company, this field holds the information which person in the company is to receive the invoice. If the order is not for a company, this field can be left blank |
| strasse | street | Musterweg 3 | | The street for the invoice address |
| plz | zip code | 86111 | | Postal code for the invoice address |
| ort | city | Musterdorf | | City for the invoice address |
| land | country | DE | | Country for the invoice address |
| email | email | max@muster.mann | | Email |
| abteilung | department | Vertrieb | | Department of the address |
| unterabteilung | subdivision | Büroartikel | | Subdepartment of the address |
| adresszusatz | address addition | Postfach 17 | | Additional address information for the invoice address |
| bundesstaat | state | Bayern | | State for the invoice address |
| ustid | ustid | DE11001100 | | The VAT ID of the one receiving the invoice |
| projekt | project | 9 | | ID of the project |
| lieferung | Shipping method | dhlversenden | | type of shipping method |
| abweichende_lieferadresse | different delivery address | 1 | | If both invoice and delivery address are identical for the order this field can be omitted. If they differ this field needs to be filled with a 1 and the field for the delivery address data need to be filled, 0 otherwise |
| lieferadresse_name | delivery address name | Eva Musterfrau | | Name of the person or company receiving the delivery |
| lieferadresse_ansprechpartner | delivery address contact | | | If the receiver of the delivery is a company this field holds the name of the person in the company receiving it |
| lieferadresse_strasse | delivery address street | Andersstrasse 22b | | Street of the delivery address |
| lieferadresse_plz | delivery address plz | 74522 | | Zip code of the delivery address |
| lieferadresse_ort | delivery address location | Andersstadt | | City of the delivery address |
| lieferadresse_land | delivery address country | DE | | Country of the delivery address |
| lieferadresse_abteilung | delivery address department | Vertrieb | | Department of the delivery address |
| lieferadresse_unterabteilung | delivery address subdivision | Büroartikel | | Subdepartment of the delivery address |
| lieferadresse_adresszusatz | delivery address addition | Postfach 17 | | Additional address information of the delivery address |
| lieferadresse_bundesstaat | delivery address state | Bayern | | State of the delivery address |
| lieferadresse_ustid | delivery address ustide | DE11001101 | | The VAT ID of the delivery address |
| freitext | freetext | Beliebiger Text | | A free text which will be saved in the “Freitext” field of the order. Please do not set any preferences on what should happen to the Freitext in the Shop settings in xentral, otherwise this will override the Smarty template information |
| internebemerkung | internal remark | Beliebiger Text | | Free text which will be saved in the “Interne Bemerkung” field of the order. Please do not set any preferences on what should happen to the Freitext in the Shop settings in xentral, otherwise this will override the Smarty template information |
| internebezeichnung | internal name | Nur zu Sonderzwecken | | Adds additional information to the imported order. This information is also visible in "Versandübergabe" in Xentral |
| gesamtsumme | grand total | 250.15 | x | Gross sum of the order. Is used to countercheck with the total costs of all the positions in the original order. If the total cost of the order gets calculated to a different sum than provided in this field the order protocol will hold the message “Online-Shop Differenz erkannt“ and the autoversand option gets deactivated |
| waehrung | currency | EUR | | Currency the order is being submitted in |
| lieferung | delivery | dhl_express | x | The carrier chosen in the order. Must be mapped in the importer settings |
| zahlungsweise | method of payment | paypal | x | The payment type chosen in the order. Must be mapped in the importer settings |
| vorabbezahltmarkieren | prepaid mark | 1 | | Marks the order as already paid, 0 otherwise |
| transaktionsnummer | transaction number | 12 1254215 055421 | | Transaction number for payments made by PayPal |
| versandkostenbrutto | shipping cost gross | 11.9 | | Gross delivery cost |
| versandkostennetto | shipping cost net | 10.0 | | Net delivery cost. If possible, this field is to be preferred |
| portosteuersatz | postage rate | 19.0 | | If the delivery cost has a special tax rate this field holds the information |
| rabattbrutto | discount gross | 11.9 | | Gross discount |
| rabattnetto | discount net | 10.0 | | Net discount |
| rabattsteuer | discount tax | 19.0 | | If the discount has a special tax rate this field holds the information |
| nachnahmepreisnetto | cash on delivery net | 10.0 | | Gross cash on delivery value |
| nachnahmepreisbrutto | cash on delivery price gross | 19.0 | | Net cash on delivery value |
| steuerfrei | tax exempt | 1 | | Marks the order as tax free, otherwise 0 |
| ust_befreit | VAT exempt | 3 | | Marks the order with having a special tax exemption case: 1: tax free EU 2: tax free foreign country 3: tax free within country |
| steuersatz_normal | tax rate normal | 20.0 | | Sets the tax rate for “normal” tax rate products |
| steuersatz_ermaessigt | tax rate reduced | 10.0 | | Sets the tax rate for “reduced” tax rate products |
| autoversand | auto shipping | 0 | | Can actively activate or deactivate the autoversand option for orders |
| fastlane | fastlane | 1 | | Marks the order as prioritized (fast lane), 0 otherwise (e.g. for Prime delivery) |
| auftragsart | order type | lieferung | | Controls the way the order is to be processed: standardauftrag - Creates an invoice and delivery note rechnung: Creates an invoice only lieferung: Creates a delivery note only |
| lastschriftdatenueberschreiben | overwrite direct debit data | 1 | | This field enables the bank account information to be overwritten by the information in the following fields, 0 otherwise |
| bankverbindung->inhaber | bank connection->accountholder | Max Mustermann | | Name of the account holder |
| bankverbindung->bank | bank connection->bank | Sparkasse Zollernalb | | Name of the Bank |
| bankverbindung->iban | bank connection->iban | DE9715001254451 | | IBAN |
| bankverbindung->bic | bank connection->bic | SOLADESBAL1 | | BIC |
| bankverbindung->firmensepa | bank connection->company sepa | 1 | |? |
| bankverbindung->mandatsreferenzhinweis | bank connection->mandate reference text | Hinweis | | |
| bankverbindung->mandatsreferenzdatum | bank connection->mandate reference date | 2020-10-10 | | |
| bankverbindung->mandatsreferenz | bank connection->mandate reference | 123 | | |

### Artikelliste

| Field Name | Field Name Translated | Example Value | Required | Business Description |
| --- | --- | --- | --- | --- |
| articlelist | articlelist | [] | x | An array holding the items of the order |
| articleid | articleid | Schraube-100 | x | Despite the name the field does not hold the ID of the item but instead the SKU |
| price | price | 1.19 | (x) | Gross price of the item. Might be used instead of price net. |
| price_netto | price net | 1.0 | (x) | Net price of the item. Preferred field to use |
| name | name | Rote Schraube | x | Name of the line item |
| quantity | quantity | 1 | x | Quantity |
| umsatzsteuer | sales tax (VAT) | normal | | Describes which tax rate the product holds: normal, ermaessigt, befreit |
| steuersatz | tax rate | 19.0 | | Sets an explicit tax rate for the line item |
| fremdnummer | foreign number | ST-500-100 | | Alternative reference number for which the item is supposed to be searched in the foreign numbers. Mapping occurs for the according shop only using the shopid as reference |
| rabatt | discount (percentage) | 10.0 | | Discount in percent for this line |
| options | options | Schraube mit rotem Kopf und blauem Gewinde | | Description which can be shown in the order, will be interpreted as a single text and added to the PDF output in order and following documents |