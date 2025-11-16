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
> GLS (CSV) ist für Cloud-Kunden nicht verfügbar.

## Einrichtung von GLS (CSV) in xentral

Um GLS in xentral als Versandart nutzen zu können, musst du zunächst eine neue Versandart anlegen. Dafür erstellst du unter Administration → Einstellungen → Versandarten → "+NEU"→ GLS (CSV) eine neue Versandart.

Nachdem du als Modul "GLS CSV" aus dem Drop-Down Menü ausgewählt hast, erscheinen die relevanten Felder für GLS. Die Befüllung der Felder könnte z.B. so aussehen:

![GLS-CSV-1.png](https://help.xentral.com/hc/article_attachments/5009694350236)

Befülle folgende Felder:

- **Bezeichnung**→ Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ**→ Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du Voreinstellung bei
- **Modul**→ Wähle "GLS CSV" aus dem Drop-Down Menü aus
- **Projekt**→ Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene GLS Versandart angelegt wird
- **Aktiv**→ Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck**→ Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke**→ Wähle aus dem Drop-Down Menü den Standarddrucker, welcher die Paketmarken druckt, aus
- **Drucker Export**→ Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail**→ Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. Standardverhalten bedeutetet, dass eine Standard-Trackingmail versendet wird, keine Versandmail bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und eigene Textvorlage bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Standardgewicht**→ Gib das Standardgewicht deiner Sendungen an. Dieses wird dann im Versanddialog automatisch ausgefüllt
- **Export als Einzeldatei**→ Durch Anhaken druckst du Exportdokumente als eigenen Ausdruck (default: Exportdokumente auf selbem Dokument wie Paketmarke)
- **Trackingnummer Startposition**→ Gib den Barcode der internen Startposition an. Alles vor dieser Position wird von der Trackingnummer abgeschnitten (z.B. Startposition 3, Trackingnummer "abcdef" => "def")
- **Trackingnummer Länge**→ Gib die Länge der Trackingnummer ab Startposition ein
- **Trackingnummer GLS Kennung entfernen**→ Durch Anhaken wird die GLS Kennung aus der Trackingnummer entfernt
- **Pfad**→ Gib das Verzeichnis an, in welchem die zu druckenden Dokumente abgelegt werden
- **testen**→ Über die "testen"-Schaltfläche kannst du eine Testdatei anlegen. Speichere vorher aber deine eingetragenen Daten über die "Speichern"-Schaltfläche ab
- **userdata** →
- **Dateiendung**→ Dateiendung des erzeugten Dokuments (z.B. csv,...)
- **Format**→ Dir stehen verschiedene Werte als Variablen zur Auswahl, mit welchen du das Format bestimmen kannst. Diese sind: {NAME}, {NAME2}, {NAME3}, {STRASSE}, {HAUSNUMMER}, {PLZ}, {ORT}, {LAND}, {GEWICHT}, {VERFAHREN}, {PRODUKT}, {SERVICE}, {BETRAG}, {NACHNAHMETEXT}, {LIEFERSCHEINNUMMER}, {KUNDENNUMMER}, {INTERNETNUMMER}, {DATUMHEUTE}, {INTERNET}