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

In xentral hast du die Möglichkeit, eine Anbindung zum Versanddienstleister Hermes vorzunehmen. Zudem kannst du verschiedene Hermes Adressen anlegen und verwalten. Dieser Artikel beschreibt die einzelnen Einrichtungspunkte für eine erfolgreiche Anbindung.

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du[hier](https://help.xentral.com/hc/de/articles/18567521362332#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

## Features

Hermes bietet dir folgende Features:

- Auswahl des Produkts
- Druck eines Demo-Labels

## Anbindung von Hermes an xentral

Die Zugangsdaten bzw. deine Oauth Resource Owner Username und Oauth Resource Password erfährst du bei deinem Geschäftskundenbetreuer bei Hermes.

Hermes wird über die API an xentral angebunden. Seit dem 26. April 2021 gibt der Versanddienstleister nun vor, dass alle Requests an die Hermes Shipping Interface (HSI) API mit der Version 1.2 des Verschlüsselungsprotokolls TLS erfolgen. Requests mit den TLS-Versionen 1.0 und 1.1 sind nicht mehr möglich. Um zu überprüfen, ob TLS v1.2 auf deinem bzw. eurem Server bereits aktiviert ist, navigiere zu dem Modul[System Health](https://help.xentral.com/hc/de/articles/360016725020#UUID-7c21ff2b-2ee6-8bf0-a7cf-f6faf8638ffe). Dieses erreichst du entweder über App Center → System Health oder über das Menü rechts oben:

![Hermes-1.png](https://help.xentral.com/hc/article_attachments/5009693383196)

In der System Health-Übersicht findest du im Bereich “Server” den Check für TLS v1.2:

![TLS_1.2_in_System_Health.png](https://help.xentral.com/hc/article_attachments/5009693410204)

Wenn du eine On-Premise Installation verwendest, dann hilft dir das Icon zu erkennen, ob TLS v1.2 installiert ist. Sollte das nicht der Fall sein, bitte deinen Serveradministrator oder -hoster, die aktuellste Version von OpenSSL zu installieren, damit du TLS v1.2 verwenden kannst.

Wenn du die xentral Cloud verwendest, dann ist TLS 1.2 bereits aktiv. Die xentral-Schnittstelle zu Hermes selbst forciert bei allen Requests bereits TLS v1.2, d.h. sobald du die aktuelle Version auf dem Server installiert hast, hast du alle Voraussetzungen zur Nutzung erfüllt.

## Einstellungen in xentral

Unter Administration → Einstellungen → Versandarten → Übersicht legst du mit "+NEU" eine neue Versandart an und wählst dann das Modul Hermes aus.

Im Anschluss kannst du deine Zugangsdaten eintragen und andere Informationen einpflegen:

![hermes1.png](https://help.xentral.com/hc/article_attachments/5009693439004)

- **Bezeichnung**→ Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ**→ Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- **Modul**→ Wähle "Hermes" aus dem Drop-Down Menü aus
- **Projekt**→ Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene Hermes Versandart angelegt wird
- **Aktiv**→ Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck**→ Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke**→ Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Paketmarken druckt
- **Drucker Export**→ Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail**→ Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Versender Firma**→ Gib die Firmendaten des Versenders ein
- **Versender Ansprechpartner**→ Gib den Ansprechpartner bei der Versenderfirma an, diesen benötigst du z.B. für Export Sendungen
- **Versender Telefon**→ Gib die Telefonnummer des Versenders an
- **Versender E-Mail**→ Gib die E-Mail Adresse des Versenders an
- **Versender Strasse**→ Gib die Straße des Versenders an
- **Versender Ort**→ Gib den Ort des Versenders an
- **Versender PLZ**→ Gib die PLZ des Versenders an
- **Versender Land**→ Gib den zweistelligen ISO-Code für das Versenderland an, für Deutschland ist dieser "DE", für Österreich "AT"
- **Oauth Resource Owner Username**→ Gib den Oauth-Benutzernamen an, diesen findest du im Hermes-Geschäftskundenportal oder im Profipaketservice
- **Oauth Resource Owner Password**→ Gib das Oauth-Passwort an, dieses findest du im Hermes-Geschäftskundenportal oder im Profipaketservice
- **Produkt**→ Wähle aus dem Drop-Down Menü das Produkt aus. Du kannst zwischen XS, S, M, L und XL wählen
- **Standardgewicht**→ Gib das Standardgewicht für Pakete in kg an. Dieses wird im Paketmarkendruck gezogen und vorab ausgefüllt
- **Länge**→ Gib optional die Standardlänge des Pakets in cm an. Diese wird immer verwendet, falls du sie angegeben und nicht im Paketmarkendialog verändert hast
- **Breite**→ Gib optional die Standardbreite des Pakets in cm an. Diese wird immer verwendet, falls du sie angegeben und nicht im Paketmarkendialog verändert hast
- **Höhe**→ Gib die Standardhöhe des Pakets in cm an. Diese wird immer verwendet, falls du sie angegeben und nicht im Paketmarkendialog verändert hast
- **Demo-Label drucken**→ Durch Anhaken druckst du eine Demo-Paketmarke, die nicht berechnet wird
- **Tracking übernehmen**→ Durch Anhaken wird die Trackingnummer nach dem Erstellen der Paketmarke automatisch in das Feld eingefügt und muss nicht mehr von der Paketmarke gescannt werden

## Paketmarkendruck

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Paketmarkendruck im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Wähle dazu im Lieferschein im Reiter "Lieferschein" die Versandart "Hermes" aus dem Drop-Down Menü aus:

![hermes3.png](https://help.xentral.com/hc/article_attachments/5009694591132)

Klicke auf die "Speichern"-Schaltfläche, bevor du in den Paketmarkendialog navigierst.

Klicke im Anschluss im Lieferschein auf den Reiter "Paketmarke" und drucke über "Paketmarke drucken" eine Paketmarke für die enthaltenen Artikel:

![hermes4.png](https://help.xentral.com/hc/article_attachments/5009723159580)

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss die Paketmarke im Hermes-Geschäftskundenportal stornieren.