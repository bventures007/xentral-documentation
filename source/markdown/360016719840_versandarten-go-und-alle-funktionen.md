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

In diesem Artikel findest du Informationen über die Anbindung der Schnittstelle des Versanddienstleisters GO! an xentral. Du kannst in xentral in dieser Versandart direkt Paketmarken anlegen und automatisch drucken. Zudem kannst du Aufträge auf diese Versandart buchen und über die Logistik abwickeln.

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du[hier](https://help.xentral.com/hc/articles/360016722580#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

## Features

Die Versandart GO! bietet dir folgende Features:

- Festlegung der Standard Abholzeit
- Festlegung der Standard Zustellzeit
- Angabe des Wunschzustelldatums
- Auswahl aus verschiedenen Servicearten

## Anbindung der Versandart

Um GO! an xentral anzubinden, brauchst du deine GO! Zugangsdaten. Diese erhältst du direkt bei deinem Geschäftskundenbetreuer bei GO! als "credentials.txt"-Dokument.

## Einstellungen in xentral

Um GO! in xentral als Versandart nutzen zu können, musst du zunächst eine neue Versandart anlegen. Dafür erstellst du unter **Administration > Einstellungen > Versandarten > Übersicht > +NEU > GO!** eine neue Versandart.

Nachdem du als Modul "GO!" aus dem Drop-Down Menü ausgewählt hast, erscheinen die relevanten Felder für GO!.

Befülle folgende Felder:

- **Bezeichnung:** Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag im Drop-Down Menü zur Auswahl angezeigt
- **Typ:** Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- **Modul:** Wähle "GO!" aus dem Drop-Down Menü aus
- **Projekt:** Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene GO! Versandart angelegt wird
- **Aktiv:** Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck:** Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke:** Wähle aus dem Drop-Down Menü den Standarddrucker, welcher die Paketmarken druckt, aus
- **Drucker Export:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail:** Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. Standardverhalten bedeutet, dass eine Standard-Trackingmail versendet wird, keine Versandmail bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und eigene Textvorlage bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Tracking übernehmen:** Durch Anhaken übernimmst du das Tracking, die Trackingnummer wird automatisch bei der Erstellung in xentral hinterlegt und muss dadurch nicht mehr abgescannt werden
- **API URL Prefix:** Gib die API URL Prefix, die du oben in der URL findest, ein: https://webservice.ax4.com/ws/4020/%% (ggf. ohne %%). Oftmals musst du die URL https://webservice.ax4.com/ws/4020/ nutzen, auch wenn von GO eine abweichende URL an den Kunden übermittelt wurde (z.B. www.ax4.com). Ob eine URL korrekt ist und mit xentral funktioniert kannst du überprüfen, indem die gesamte URL im Browser aufgerufen wird
- **API URL Postfix:** Gib die API URL Postfix, die du oben in der URL findest, ein: /Sendungsdaten
- **API URL User:** Gib die API URL User ein, die du oben in der URL findest: GOmeineFirma
- **Benutzername:** Gib deinen Benutzername ein: meineFirma. Diesen erhältst du im Kundenportal bzw. der GO! Außendienststelle
- **Passwort:** Gib dein Passwort ein. Du erhältst dieses im Kundenportal bzw. der GO! Außendienststelle
- **ax4nr:** Diese Information kannst du aus dem dir zugeschickten Dokumenten von GO! entnehmen bzw. diese erhältst du im Kundenportal oder der GO! Außendienststelle
- **Format:** Gib das Paketmarkenformat ein, z.B. "A4"
- **Ausgabe:** Gib "RouterlabelZebra" im Fall eines Zebra-Druckers an, sonst lasse das Feld leer
- **Absender Name 1:** Gib den Namen des Absenders ein. Dieser erscheint auf der Paketmarke
- **Absender Name 2:** Falls ein zusätzlicher zweiter Name des Absenders auf der Paketmarke erscheinen soll, gib diesen hier an
- **Absender Abteilung:** Gib an, welche Abteilung beim Absender mit der Sendung betraut ist
- **Absender Strasse 1:** Gib die Straße des Absenders ein, diese erscheint auf der Paketmarke
- **Absender Strasse 2:** Gib eine zweite, optionale Straße des Absenders ein, wenn es eine zusätzlich zu der aus "Absender Straße 1" gibt
- **Absender Hausnummer:** Gib die Hausnummer des Absenders an. Diese erscheint auf der Paketmarke
- **Absender PLZ:** Gib die Postleitzahl des Absenders ein. Diese erscheint auf der Paketmarke
- **Absender Ort:** Gib den Ort des Absenders ein. Dieser erscheint auf der Paketmarke
- **Absender Land:** Gib das Land des Absenders ein. Dieses erscheint auf der Paketmarke
- **Absender Standardgewicht:** Gib das Standardgewicht an, das künftig in der Paketmarke hinterlegt ist
- **Standard Kundenreferenz:** Nutze Variablen, um die Referenz auf dem Label zu gestalten. Folgende Variablen stehen dir zur Verfügung: {AUFTRAGSNUMMER}, {RECHNUNGSNUMMER}, {LIEFERSCHEINNUMMER}, {INTERNET}
- **Anzahl Differenz Tage Zustellung:** Gib das Wunschzustelldatum in n Tagen an, "1" bedeutet eine Zustellung morgen
- **Standard Abholzeit von:** Gib die Uhrzeit an, ab wann das Paket abgeholt werden kann
- **Standard Abholzeit bis:** Gib die Uhrzeit an, bis wann das Paket abgeholt werden kann
- **Standard Zustellzeit von:** Gib die Uhrzeit an, ab wann das Paket zugestellt werden kann
- **Standard Zustellzeit bis:** Gib die Uhrzeit an, bis wann das Paket zugestellt werden kann
- **Serviceart:** Wähle aus dem Drop-Down Menü einen zusätzlichen Service wie Overnight oder Worldwide aus
- **Pseudonym Artikelbezeichnungen:** Gib optional Pseudonyme für die Artikelbezeichnungen ein. Inhalte aus diesem Feld werden dann als Artikelbezeichnungen statt aus den Bezeichnungen aus den Artikeln übermittelt

Nachdem du alle Einstellungen vorgenommen hast, klicke auf **Speichern**.

## Paketmarkendruck

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Paketmarkendruck im **Versandzentrum ** oder auch in einem einzelnen **Lieferschein ** testen. Wähle dazu im Lieferschein im Reiter **Details ** im Bereich **Lieferschein ** die**Versandart **"GO!" aus dem Drop-Down Menü aus. Klicke auf ** Speichern**, bevor du in den Paketmarkendialog navigierst.

Klicke im Anschluss im Lieferschein auf den Reiter **Paketmarke ** und drucke über den Button**Paketmarke drucken** eine Paketmarke für die enthaltenen Artikel.

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss die Paketmarke im GO!-Geschäftskundenportal stornieren.