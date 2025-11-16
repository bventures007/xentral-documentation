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

Seven Senders ist ein Anbieter von internationalen bzw. ausländischen Versanddienstleistern. In diesem Artikel erfährst du, wie du diesen an xentral anbinden und individuelle Einstellungen vornehmen kannst. Weitere Informationen zum Versanddienstleister erhältst du unter[https://sevensenders.com/de/](https://sevensenders.com/de/).

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du[hier](https://help.xentral.com/hc/articles/360016722580#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

## Features

Seven Senders bietet dir folgende Features:

- Angabe einer Empfänger E-Mail Adresse, wenn diese im Lieferschein fehlt
- Aktivierung der Nachnahme
- Überspringen des Scandialogs

## Anbindung von Seven Senders an xentral

Um Seven Senders an xentral anzubinden, benötigst du den Seven Senders API Key. Diesen erhältst du bei deinem Seven Senders Kundenbetreuer. Wenn du dich für die Integration über den xentral Adapter entscheidest, benötigst du ebenfalls deinen kundenspezifischen API Key, den du von Seven Senders mitgeteilt bekommst.

## Einstellungen in xentral

Um Seven Senders in xentral als Versandart nutzen zu können, musst du zunächst eine neue Versandart anlegen. Diese erstellst du unter **Administration > Einstellungen > Versandarten > Übersicht > +NEU > Sevensenders**.

Nachdem du als Modul **Sevensenders** aus dem Drop-Down Menü ausgewählt hast, erscheinen die relevanten Felder für Seven Senders.

Befülle folgende Felder:

- **Bezeichnung:** Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ:** Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- **Modul: ** Wähle ** Sevensenders** aus dem Drop-Down Menü aus
- **Projekt:** Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene Seven Senders Versandart angelegt wird
- **Aktiv:** Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck:** Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Paketmarken druckt
- **Drucker Export:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail:** Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Sevensenders Api Key:** Gib den Seven Senders API Key ein
- **Versender Firma:** Gib die Versenderfirma ein
- **Versender Vorname:** Gib den Vornamen des Versenders ein
- **Versender Nachname:** Gib den Nachnamen des Versenders ein
- **Versender Telefon:** Gib die Telefonnummer des Versenders ein
- **Versender E-Mail:** Gib die E-Mail Adresse des Versenders ein
- **Versender Strasse:** Gib die Straße inkl. Hausnummer des Versenders ein
- **Versender Ort:** Gib den Ort des Versenders ein
- **Versender PLZ:** Gib die PLZ des Versenders ein
- **Versender Land:** Gib das Land des Versenders ein. Verwende dabei den zweistelligen ISO-Code, bspw. für Deutschland "DE", für Österreich "AT"
- **Empfängermail bei Fehlen in Lieferschein:** Gib die E-Mail Adresse des Empfängers ein. Dieser erhält dann eine E-Mail, wenn der Lieferschein in der Sendung fehlt
- **Versandfirma:** Gib die Versandfirma an
- **Standardgewicht:** Gib das Standardgewicht einer Sendung in kg an
- **Tracking übernehmen:** Durch Anhaken aktivierst du das Tracking. Die Trackingnummer wird nach dem Erstellen der Paketmarke automatisch in das Feld eingefügt und muss später nicht mehr von der Paketmarke gescannt werden
- **Scandialog überspringen:** Durch Anhaken wird der Trackingscandialog übersprungen und erst dann ein Versandeintrag angelegt, wenn dir die Daten von Seven Senders zur Verfügung stehen

Klicke abschließend auf **Speichern**.

## Paketmarkendruck

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Paketmarkendruck im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Wähle dazu im Lieferschein im Reiter **Lieferschein ** die**Versandart** Seven Senders aus dem Drop-Down Menü aus:

![sevensenders2.png](https://help.xentral.com/hc/article_attachments/5009710152988)

Klicke auf die **Speichern**

-Schaltfläche, bevor du in den Paketmarkendialog navigierst.

Klicke im Anschluss im Lieferschein auf den Reiter **Paketmarke ** und drucke über**Paketmarke drucken** eine Paketmarke für die enthaltenen Artikel:

![sevensenders3.png](https://help.xentral.com/hc/article_attachments/5009710971932)

Hier kannst du zusätzlich noch die Nachnahme aktivieren, indem du unter Service das Feld **Nachnahme** anhakst.

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss die Paketmarke im Seven Senders-Geschäftskundenportal stornieren.