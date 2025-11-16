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

> **Anmerkung**
>
> Der Paketmarkendruck via CSV war nur bei On-Premise-Instanzen möglich!

Zusätzlich zu der herkömmlichen Art des Paketmarkendrucks über Lieferschein und Paketmarkenformat, kannst du den Paketmarkendruck auch mit CSV-Dateien durchführen. In diesem Artikel findest du Informationen zu Herangehensweise und die Spezialfälle DPD (CSV) und GLS (CSV).

## Anbindung einer externen Software zur Übertragung von Paketmarkeninformationen

Oftmals liegt Software vom Paketdienstleister vor, die eine CSV-Datei in einem lokalen Verzeichnis erwartet. In diesem Fall läuft xentral auf einem Webserver in einem entfernten Netz. Dann musst du die Dateien bzw. das Verzeichnis lokal einbinden. Viele Hoster, z.B. All-inkl., bieten einfache Freigaben per Netzlaufwerk an. So kann eine Datei von xentral erstellt und über das Netzlaufwerk lokal angebunden werden. Alternativ kannst du mit einem FTP Programm arbeiten, das ein FTP Verzeichnis zyklisch kopiert, z.B. http://www.watchftp.com/.

### Verzeichnis anlegen

Um ein Verzeichnis anzulegen, gehe wie folgt vor:

1. Lege auf deinem xentral-Server ein Verzeichnis an (im Webspace, auf dem xentral installiert ist). Aus diesem Verzeichnis kann eine Versandsoftware, z.B. die.csv, Informationen zur Erzeugung von Paketmarken abholen.
1. Die Abholung kann z.B. über eine Ordnerfreigabe, z.B. per Windows-Freigabe veröffentlichen, oder via FTP erfolgen.

## DPD (CSV) - DELISprint

Der Paketmarkendruck in xentral beim Versanddienstleister DPD funktioniert auf zwei Arten: Entweder verwendest du die herkömmliche Versandart[DPD](https://help.xentral.com/hc/de/articles/360016721940#UUID-9f736703-cbf7-5fd4-5177-d56fe9fb78a0)oder du führst den Paketmarkendruck mit CSV wie hier beschrieben durch.

### Einrichtung von DPD (CSV) in xentral

Lege unter **Administration > Einstellungen > Versandarten > Übersicht > +NEU > DPD (CSV)** eine neue Versandart an.

Fülle dazu folgende Felder aus:

- **Bezeichnung:** Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ:** Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- **Modul: ** Wähle ** DPD CSV** aus dem Drop-Down Menü aus
- **Projekt:** Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene DPD(CSV)-Versandart angelegt wird
- **Aktiv:** Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck:** Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Paketmarken druckt
- **Drucker Export:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail:** Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutetet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Standardgewicht:** Gib das Standardgewichts eines Pakets in kg an
- **Export als Einzeldatei:** Durch Anhaken wird pro Paket eine eigene Datei verschickt
- **Trackingnummer Startposition:** Gib den Barcode der internen Startposition ein
- **Trackingnummer Länge:** Gib die gewünschte Länge der Trackingnummer ein. Gibst du "0" ein, wird alles bzw. die gesamte Trackingnummer verwendet
- **Trackingnummer DPD Kennung entfernen:** Durch Anhaken entfernst du die DPD Kennung aus der Trackingnummer
- **DPD Kennung:** Gib die DPD Kennung ein
- **DPD Pfad:** Gib das DPD-Verzeichnis an, in welchem die zu druckenden Dokumente abgelegt werden. Die Dateien werden lokal am Server abgelegt
- **testen: ** Über die Schaltfläche ** Testdatei anlegen **kannst du eine CSV-Testdatei anlegen. Klicke vorher aber auf die ** Speichern**

-Schaltfläche, um alle Daten zu sichern
- **userdata:** Hier steht dein xentral userdata-Pfad
- **DPD Dateiendung:** Gib die Dateiendung für DPD ein
- **DPD Format:** Bestimme das DPD Format. Folgende Variablen stehen dir zur Verfügung: {NAME}, {NAME2}, {NAME3}, {STRASSE}, {HAUSNUMMER}, {PLZ}, {ORT}, {LAND}, {GEWICHT}, {VERFAHREN}, {PRODUKT}, {SERVICE}, {BETRAG}, {NACHNAHMETEXT}, {LIEFERSCHEINNUMMER}, {KUNDENNUMMER}, {INTERNETNUMMER}, {DATUMHEUTE} und {INTERNET}

Klicke abschließend auf die **Speichern**

-Schaltfläche.

## GLS (CSV)

Der Paketmarkendruck ist in xentral nicht nur über DPD (CSV) DELISprint, sondern auch über GLS (CSV) möglich.

### Einrichtung von GLS (CSV) in xentral

Um GLS in xentral als Versandart nutzen zu können, musst du zunächst eine neue Versandart anlegen. Dafür erstellst du unter **Administration > Einstellungen > Versandarten > Übersicht > +NEU > GLS (CSV)** eine neue Versandart.

Nachdem du als Modul **GLS CSV** aus dem Drop-Down Menü ausgewählt hast, erscheinen die relevanten Felder für GLS.

Befülle folgende Felder:

- **Bezeichnung:** Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ:** Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- **Modul: ** Wähle ** GLS CSV** aus dem Drop-Down Menü aus
- **Projekt:** Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene GLS-Versandart angelegt wird
- **Aktiv:** Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck:** Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Paketmarken druckt
- **Drucker Export:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail:** Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Standardgewicht:** Gib das Standardgewicht deiner Sendungen in kg an. Dieses wird dann im Versanddialog automatisch ausgefüllt
- **Export als Einzeldatei:** Durch Anhaken wird pro Paket eine eigene Exportdatei verschickt, default: Exportdokumente auf selbem Dokument wie Paketmarke
- **Trackingnummer Startposition:** Gib den Barcode der internen Startposition an. Alles vor dieser Position wird von der Trackingnummer abgeschnitten (z.B. Startposition 3, Trackingnummer "abcdef" > "def")
- **Trackingnummer Länge:** Gib die Länge der Trackingnummer ab der Startposition ein
- **Trackingnummer GLS Kennung entfernen:** Durch Anhaken wird die GLS Kennung aus der Trackingnummer entfernt
- **Pfad:** Gib das Verzeichnis an, in welchem die zu druckenden Dokumente abgelegt werden. Die Dateien werden lokal am Server abgelegt
- **testen: ** Über die ** testen **

-Schaltfläche kannst du eine Testdatei anlegen. Speichere vorher aber deine eingetragenen Daten über die ** Speichern**

-Schaltfläche ab
- **userdata:** Hier steht dein userdata-Pfad bei xentral
- **Dateiendung:** Trage die Dateiendung des erzeugten Dokuments ein, z.B..csv
- **Format:** Dir stehen verschiedene Werte als Variablen zur Auswahl, mit welchen du das Format bestimmen kannst. Diese sind: {NAME}, {NAME2}, {NAME3}, {STRASSE}, {HAUSNUMMER}, {PLZ}, {ORT}, {LAND}, {GEWICHT}, {VERFAHREN}, {PRODUKT}, {SERVICE}, {BETRAG}, {NACHNAHMETEXT}, {LIEFERSCHEINNUMMER}, {KUNDENNUMMER}, {INTERNETNUMMER}, {DATUMHEUTE}, {INTERNET}

Klicke abschließend auf die **Speichern**

-Schaltfläche.

## Testdatei

Sowohl in der Oberfläche für DPD als auch in der für GLS hast du die Möglichkeit, deine Angaben über eine Testdatei anzulegen und zu testen. Speichere aber in jedem Fall vorher deine eingetragenen Informationen über den **Speichern**

-Button unten rechts auf der Seite ab.

Voraussetzung für die Nutzung der Testdatei ist, dass du zuvor im Feld **Pfad** einen gültigen und erreichbaren Speicherort für die Dokumente eingetragen hast.