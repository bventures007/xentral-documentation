> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Es ist nicht mehr möglich, DPD eSolutions in Xentral NextGeneinzurichten oder zu verwenden.
> - Wir nehmen keine Fehlerbehebungen mehr für dieses Produkt vor und entwickeln keine neuen Funktionen.

Die Anbindung von DPD an xentral ermöglicht dir den automatischen Paketmarkendruck und die Versandübergabe an den Paketdienst. Weitere Informationen zu DPD eSolutions findest du[hier](https://esolutions.dpd.com/entwickler.aspx).

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du.

## Features

DPD eSolutions bietet dir folgende Features:

- Auswahl des Produkts
- Angabe eines selbst gewählten Paketmarkenformats
- Angabe der Sprache auf Paketmarke

## Anbindung von DPD an xentral

DPD bietet verschiedene Lösungen an. Für xentral benötigst du die DPD Partnerlösung. Diese kann dir von deinem Kundenbetreuer freigeschaltet werden, xentral ist hier gelistet. Diese Information sollte dem Kundenbetreuer ausreichen.

Du findest das Modul unter DPD → eSolutions → Partnerlösungen → Plugins → xentral.

> **Anmerkung**
>
> Hierbei handelt es sich dann nicht um das normale myDPD pro und my DPD Business Portal, sondern die API-Anbindung.

## Einstellungen in xentral

Um DPD eSolutions vollumfänglich in xentral nutzen zu können, musst du DPD eSolutions zunächst als Versandart anlegen. Das machst du unter Administration → Einstellungen → Versandarten → "+NEU" → DPD eSolutions.

Anschließend erscheint eine Oberfläche, die du so konfigurieren kannst:

- Bezeichnung→ Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- Typ→ Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- Modul→ Wähle "Dpdesolutions" aus dem Drop-Down Menü aus
- Projekt→ Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene DPD Versandart angelegt wird
- Aktiv→ Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- Kein Portocheck→ Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- Drucker Paketmarke→ Wähle aus dem Drop-Down Menü den Standarddrucker, welcher die Paketmarken druckt, aus
- Drucker Export→ Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- Versandmail→ Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- Delis ID→ Gib deine DELIS-Benutzerkennung ein
- Passwort→ Gib dein DELIS-Passwort ein
- Versender Firma→ Gib den Namen der Versenderfirma ein
- Versender Strasse→ Gib die Straße der Versenderfirma ein
- Versender Hausnummer→ Gib die Hausnummer der Versenderfirma ein
- Versender PLZ→ Gib die PLZ der Versenderfirma ein
- Versender Ort→ Gib den Ort der Versenderfirma ein
- Versender Land→ Gib das Land der Versenderfirma als 2-stelligen ISO Code ein, verwende für Deutschland das Kürzel "DE", für Österreich "AT"
- Sprache→ Wähle aus dem Drop-Down Menü die Sprache aus, die auf der Paketmarke verwendet werden soll
- Referenz auf Label 1→ Gib hier den Text ein, der auf der Paketmarke bzw. dem DPD Etikett erscheint. Diesem kannst du optional Variablen hinzufügen. Folgende stehen dir dafür zur Verfügung: {LIEFERSCHEIN}, {AUFTRAG}, {PROJEKT}, {IHREBESTELLNUMMER} und {INTERNET}
- Referenz auf Label 2→ Gib hier den Text ein, der auf der Paketmarke bzw. dem DPD Etikett erscheint. Diesem kannst du optional Variablen hinzufügen. Folgende stehen dafür zur Verfügung: {LIEFERSCHEIN}, {AUFTRAG}, {PROJEKT}, {IHREBESTELLNUMMER} und {INTERNET}
- Product→ Wähle aus dem Drop-Down Menü das DPD Produkt aus, das diese Versandart darstellt
- Papierformat→ Wähle aus dem Drop-Down Menü das Papierformat der Paketmarke aus
- Tracking übernehmen→ Durch Anhaken wird die Trackingnummer in der Folgemaske des Versanddialogs angezeigt. Die Tracking Nummer wird automatisch beim Erstellen der Paketmarke in xentral übernommen, dadurch muss sie nicht mehr von der Paketmarke gescannt werden

Klicke abschließend auf "Speichern".

> **Anmerkung**
>
> Wenn du mehrere DPD-Produkte parallel verwendet willst, lege hierfür verschiedene Versandarten in xentral an und vergebe verschiedene, eindeutige Typ-Bezeichnungen, z.B. DPD_Express18, DPD_Express12.

Folgende Produkte sind bei DPD nach Absprache mit deinem Kundenbetreuer möglich:

- DPD CLASSIC
- DPD 8:30 (Express_830)
- DPD 10:00 (Express_10)
- DPD 12:00 (Express_12)
- DPD 18:00 (Express_18)
- DPD EXPRESS
- DPD PARCELLetter
- DPD PARCELLetterPlus
- DPD International Mail

## Paketmarkendruck

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Paketmarkendruck im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Wähle dazu im Lieferschein im Reiter "Details" die Versandart "DPD eSolutions" aus dem Dropdown-Menü unter Lieferschein aus.

Klicke im Anschluss im Lieferschein auf den Reiter "Paketmarke" und drucke über "Paketmarke drucken" eine Paketmarke für die enthaltenen Artikel.

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss die Paketmarke im DPD-Geschäftskundenportal stornieren.