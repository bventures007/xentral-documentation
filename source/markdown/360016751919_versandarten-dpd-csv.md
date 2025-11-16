## Inhaltsverzeichnis

- Anbindung einer externen Software, um Paketmarkeninformationen zu übertragen
  - Verzeichnis anlegen
  - DPD CSV (DELISprint)

Dieses Modul ermöglicht die Anbindung von Paketmarken-Software über ein Verzeichnis.

# Anbindung einer externen Software zur Übertragung von Paketmarkeninformationen

Oftmals liegt Software vom Paketdienstleister vor, die eine CSV Datei in einem lokalen Verzeichnis erwartet. In diesem Fall ist es aber meist so, dass xentral auf einem Webserver in einem entfernten Netz läuft. Dann musst du die Dateien bzw. das Verzeichnis lokal einbinden. Viele Hoster, z.B. All-inkl. bieten einfache Freigaben per Netzlaufwerk an. So kann eine Datei von xentral erstellt werden und über das Netzlaufwerk lokal angebunden werden. Alternativ kannst du mit einem FTP Programm arbeiten, dass ein FTP Verzeichnis zyklisch kopiert, z.B.[http://www.watchftp.com/](http://www.watchftp.com/).

## Verzeichnis anlegen

Um ein Verzeichnis anzulegen, gehe wie folgt vor:

Lege hierzu auf deinem xentral-Server ein Verzeichnis an (im Webspace, auf dem xentral installiert ist). Aus diesem Verzeichnis kann eine Versandsoftware, z.B. die.csv, Informationen zur Erzeugung von Paketmarken abholen.

Diese Abholung kann z.B. über eine Ordnerfreigabe (z.B. per Windows-Freigabe veröffentlichen) oder via FTP erfolgen.

## DPD CSV (DELISprint)

Lege unter Versandarten → "+NEU" → DPD (CSV) eine neue Versandart an:

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/versandarten_dpd_1.png)

![dpd_csv1.png](https://help.xentral.com/hc/article_attachments/360025234099/dpd_csv1.png)

Fülle dazu folgende Felder aus:

- Bezeichnung → Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- Typ → Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du Voreinstellung bei
- Modul → Wähle "DHL Versenden" aus dem Drop-Down Menü aus
- Projekt → Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene DHL Versandart angelegt wird
- Aktiv → Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- Kein Portocheck → Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- Drucker Paketmarke → Wähle aus dem Drop-Down Menü den Standarddrucker, welcher die Paketmarken druckt, aus
- Drucker Export → Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- Versandmail → Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. Standardverhalten bedeutetet, dass eine Standard-Trackingmail versendet wird, keine Versandmail bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und eigene Textvorlage bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- Standardgewicht → Gib das Standardgewichts eines Pakets an
- Export als Einzeldatei → Durch Anhaken wird pro Paket eine eigene Datei verschickt
- Trackingnummer Startposition → Gib den Barcode der internen Startposition ein
- Trackingnummer Länge → Gib die gewünschte Länge der Trackingnummer ein. Gibst du "0" ein, wird alles bzw. die gesamte Trackingnummer verwendet
- Trackingnummer DPD Kennung entfernen → Durch Anhaken entfernst du die DPD Kennung aus der Trackingnummer
- DPD Kennung → Gib die DPD Kennung ein
- DPD Pfad → Gib den DPD Pfad an
- testen → Über die Schaltfläche "Testdatei anlegen" kannst du eine CSV-Testdatei anlegen. Klicke vorher aber auf die "Speichern"-Schaltfläche, um alle Daten zu sichern
- userdata →
- DPD Dateiendung → Gib die Dateiendung für DPD ein
- DPD Format → Bestimme das DPD Format. Folgende Variablen stehen dir zur Verfügung: {NAME}, {NAME2}, {NAME3}, {STRASSE}, {HAUSNUMMER}, {PLZ}, {ORT}, {LAND}, {GEWICHT}, {VERFAHREN}, {PRODUKT}, {SERVICE}, {BETRAG}, {NACHNAHMETEXT}, {LIEFERSCHEINNUMMER}, {KUNDENNUMMER}, {INTERNETNUMMER}, {DATUMHEUTE}, {INTERNET}

Klicke abschließend auf die "Speichern"-Schaltfläche.