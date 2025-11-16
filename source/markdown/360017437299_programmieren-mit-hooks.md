Durch Hooks ist es möglich, bestimmte Funktionen aufzurufen, ohne das aufrufende Modul zu ändern. Der Ablauf folgt dabei diesem Schema:

![Hooks-1.png](https://help.xentral.com/hc/article_attachments/4996391893020)

## RegisterHook

Um einen Hook zu registrieren, wird folgende Funktion in der Install Funktion des zugrundeliegenden Moduls aufgerufen:

$this->app->erp->RegisterHook('hookname_1', 'modulname', 'FunktionsName');

Vereinfach gesagt: Wenn der Hook mit dem Namen 'hookname_1' durch die Funktion 'RunHook' ausgeführt wird, dann ist im Modul 'modulname' die Funktion 'FunktionsName' aufzurufen. Sollte ein registrierter Hook nicht mehr benötigt werden, kann er deaktiviert werden, indem der Funktion "RegisterHook" als vierter Parameter eine 0 übergeben wird:

$this->app->erp->RegisterHook('hookname_1', 'modulname', 'FunktionsName',0); Durch diesen Aufruf wird die Registrierung deaktiviert.

## RunHook

Über die Funktion "RunHook" ist es auch möglich, neue Hooks zu setzen:

$this->app->erp->RunHook('hookname_1', 0);

Sobald die Funktion aufgerufen wird, werden alle auf "hookname_1" registrierten Hooks der Reihe nach ausgeführt.

## Parameter

Es ist möglich, den Funktionen, die über Hooks ausgeführt werden, Parameter zu übergeben. Dabei legt der zweite Parameter der Funktion 'Runhook' fest, wie viele Parameter übergeben werden.

$this->app->erp->RunHook('hookname_1', 1, $x);

Bei diesem Hook wird allen registrierten Funktionen die Variable $x als Parameter übergeben.

## Hooks wieder entfernen

Um nicht mehr benötigte Hooks wieder aus dem System zu entfernen, kann die Funktion 'RemoveHooks()' verwendet werden:

$this->app->erp->RemoveHook('hookname_1');

Dabei wird nicht nur der Hook 'hookname_1' entfernt, sondern auch alle Registrierungsverweise auf diesen.

## Vorhandene Hooks

Im System werden bereits an diversen Stellen Hooks ausgeführt, an die sich durch "RegisterHook" angehängt werden kann. Zur Zeit der Erstellung dieses Artikels waren dies:

Modul: Hookname cronjobs/amazon.php: 'amazon_cronjob' cronjobs/versandmailsundrueckmeldung.php: 'versanderzeugen_frankieren_hook1' phpwf/plugins/class.yui.php: 'AARLGEditable' phpwf/plugins/class.yui.php: 'AARLGPositionen_aktion' phpwf/plugins/class.yui.php: 'AARLGPositionenPreis' phpwf/plugins/class.yui.php: 'AARLGPositionenSprache' phpwf/plugins/class.yui.php: 'auftraege_tablesearch' (x2) phpwf/plugins/class.yui.php: 'yui_sortlistadd_draw' phpwf/plugins/class.yui.php: 'yui_sortlistadd_ende' phpwf/widgets/easytable.php: 'EasyTableDisplayEditable' (x2) phpwf/widgets/easytable.php: 'EasyTableDisplayEditableClick' www/eproosystem.php: 'eproosystem_ende' www/lib/class.erpapi.php: 'ANABREGSNeuberechnen_1' www/lib/class.erpapi.php: 'ANABREGSNeuberechnenEnde' www/lib/class.erpapi.php: 'artikelnummerscan' www/lib/class.erpapi.php: 'auftragcheck' www/lib/class.erpapi.php: 'BerechneDeckungsbeitragEnde' www/lib/class.erpapi.php: 'chargenlog_bestand' www/lib/class.erpapi.php: 'dokument_absenden_email' www/lib/class.erpapi.php: 'DokumentAbschickenMeldungAngelegt' www/lib/class.erpapi.php: 'DokumentMask' www/lib/class.erpapi.php: 'DokumentMaskVersendet' www/lib/class.erpapi.php: 'dokumentsend_email' www/lib/class.erpapi.php: 'erpapi_lieferschein_auslagern' www/lib/class.erpapi.php: 'erpapi_loadauftragstandardwerte' www/lib/class.erpapi.php: 'erpapi_loadlieferscheinstandardwerte' www/lib/class.erpapi.php: 'ImportAuftrag' www/lib/class.erpapi.php: 'mhdlog_bestand' www/lib/class.erpapi.php: 'paketmarke_abschluss' www/lib/class.erpapi.php: 'parseuservars' www/lib/class.erpapi.php: 'produktion_explodieren' www/lib/class.erpapi.php: 'rechnungsmail' www/lib/class.erpapi.php: 'versanderzeugen_frankieren_hook1' (x3) www/lib/class.erpapi.php: 'versandmail' www/lib/class.erpapi.php: 'WeiterfuehrenAuftragZuLieferschein' www/lib/class.erpapi.php: 'ZahlungsweisetextZahlungsdatum' www/lib/dokumente/class.auftrag.php: 'BreifpapierGetAuftragArtikel' www/lib/dokumente/class.auftrag.php: 'BreifpapierGetAuftragEnde' www/lib/dokumente/class.briefpapier.php: 'briefpapier_render_document_hook1' www/lib/dokumente/class.briefpapier.php: 'briefpapier_render_document_hook2' www/lib/dokumente/class.briefpapier.php: 'briefpapier_render_footer_hook1' www/lib/dokumente/class.briefpapier.php: 'briefpapier_render_footer_hook2' www/lib/versandarten/dpd.php: 'versanderzeugen_frankieren_hook1' (x2) www/lib/versandarten/intraship.php: 'versanderzeugen_frankieren_hook1' (x2) www/lib/versandarten/logoix.php: 'versanderzeugen_frankieren_hook1' www/lib/versandarten/sonstiges.php: 'versanderzeugen_frankieren_hook1' www/lib/versandarten/spedition.php: 'paketmarke_abschluss' www/lib/versandarten/ups.php: 'versanderzeugen_frankieren_hook1' www/pages/ajax.php: 'ajax_filter_hook1' www/pages/amazon.php: 'lieferschein_auslagern' www/pages/artikel.php: 'artikel_ajaxwerte' www/pages/artikel.php: 'artikel_minidetail_hook1' www/pages/artikel.php: 'artikel_shopbutton' (x4) www/pages/auftrag.php: 'auftrag_edit_hook1' www/pages/auftrag.php: 'auftraguebersicht_filter' www/pages/bestellung_einlagern.php: 'bestellung_einlagern' www/pages/bestellvorschlagapp.php: 'bestellvorschlagapp_berechnen' www/pages/bestellvorschlagapp.php: 'bestellvorschlagapp_select' www/pages/kommissionskonsignationslager.php: 'kommissionskonsignationslager_artikel_tablesearch' www/pages/kommissionskonsignationslager.php: 'KommissionskonsignationslagerArtikel' www/pages/lager.php: 'lager_buchenauslagern_display1' www/pages/lager.php: 'lager_buchenauslagern_mhdlagerbewegung' (x2) www/pages/lagermobil.php: 'lager_buchenauslagern_mhdlagerbewegung' www/pages/lieferschein.php: 'lieferschein_auslagern' www/pages/onlineshops.php: 'shopexport_create' (x3) www/pages/produktion.php: 'produktion_edit' www/pages/produktion.php: 'produktion_minidetail' www/pages/produktionszentrum.php: 'produktionszentrum_abschluss_hook1' www/pages/shopimport.php: 'Shopimport' www/pages/shopimport.php: 'Shopimportwarenkorb' www/pages/shopimporter_amazon.php: 'amazon_einstellungenstruktur' www/pages/shopimporter_amazon.php: 'shopimporter_amazon_getKonfig' www/pages/shopimporter_amazon.php: 'shopimporter_amazon_tabs' www/pages/steuerregeln.php: 'steuerregeln_berechneerloessteuer_setzen' www/pages/steuerregeln.php: 'steuerregeln_berechneerloessteuer_uebergeordnet' www/pages/steuerregeln.php: 'steuerregeln_edit_hook1' www/pages/versanderzeugen.php: 'versanderzeugen_einzel_komplett' www/pages/versanderzeugen.php: 'versanderzeugen_frankieren' www/pages/versanderzeugen.php: 'versanderzeugen_frankieren_hook1' www/pages/versanderzeugen.php: 'versanderzeugen_lieferschein_drucken' www/pages/versanderzeugen.php: 'versanderzeugen_wechsel' www/pages/wareneingang.php: 'wareneingang_display_hook_rma1' (x3) www/pages/wareneingang.php: 'wareneingang_lager_submit' www/pages/wareneingang.php: 'wareneingang_mitarbeiter_submit' www/pages/wareneingang.php: 'wareneingang_rma_submit' www/pages/zahlungseingang.php: 'zahlungseingang_checkbuchung' www/pages/zahlungsweisen.php: 'zahlungsweisen_edit_show' (x2) www/pages/zeiterfassung.php: 'zeiterfassung_create_guihook1' (x4) www/widgets/widget.auftrag.php: 'auftrageditdetail' (x2) www/widgets/widget.bestellung_position.php: 'widget_bestellung_position1' (x2) www/widgets/widget.shopexport.php: 'shopexport_show' www/widgets/widget.shopexport.php: 'shopexport_speichern'

## TableSearch Hook

Als Hook ist hierbei zu verwenden:

tablesearch_after mit den Parametern $name und $hookfelder.

$hookfelder ist ein array der From array('sql'=>"SELECT...", 'heading'=>array('ueberschrift1','foobar'))

Um sich am Hook in Install oder List Methode zu registrieren, gilt Folgendes:

$this->app->erp->RegisterHook('tablesearch_after', 'adresse', 'AdresseTableSearch');

Die entsprechende Methode ist so zu wählen:

function AdresseTableSearch(&$name,&$hookfelder) { $name = "adressetabelle"; $hookfelder = array('heading'=>array('bla','foobar');}

## Navigation

> **Anmerkung**
>
> Hooks für die Navigation stehen ab XentralVersion 22.1 nicht mehr zur Verfügung. Anstelle der Menüanpassung durch Hooks kannst du ein Lesezeichen auf der Startseite einfügen.

Zudem ist es möglich, durch die Verwendung von Hooks das Menü anzupassen. Bei der Verwendung von Navigationshooks darf nicht von einer Custom Datei aus auf das Modulmenü der vererbenden Klassen verwiesen werden. Sonst entsteht eine Endlossschleife bei der Verarbeitung und die Anzeige bricht mit einer leeren Seite ab.

### RegisterNavigationHook

Im Folgenden wird der Einbau in Install() des Moduls Bsp aufgezeigt:

$this->app->erp->RegisterNavigationHook('auftragscockpit', 'auftraglist', 'Verkauf', 'Auftragscockpit', 'Auftrag');

Das entspricht:

$this->app->erp->RegisterNavigationHook('modul', 'action', 'Hauptpunkt', 'Neuer Navigations Titel', 'Titel bestehender Navigationspunkt');

Dadurch wird "index.php?module=auftragscockpit&action=auftraglist" mit dem Namen "Auftragscockpit" im Menüpunkt "Verkauf" unter dem Feld "Auftrag" (optionaler Parameter) an das Menü angehängt.

### Hooks wieder entfernen

Sollte ein Navigationshook nicht mehr benötigt bzw. eine andere zugrundeliegende Funktion verwendet werden, muss der alte Navigationshook entfernt werden. Das ist zum einen über die Datenbank möglich, indem der entsprechende Eintrag aus der Tabelle "hook_navigation" entfernt wird. Zum anderen kann es auch programmatisch durchgeführt werden:

$this->app->erp->RemoveNavigationHook('modulname', 'aktionname');

Der zweite Parameter ist optional. Wenn er nicht angegeben wird, werden alle dem Modul zugeordneten Hooks entfernt.