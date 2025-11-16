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

In diesem Artikel findest du Informationen über die Anbindung von Fedex an xentral. In xentral kannst du in dieser Versandart direkt Paketmarken anlegen und automatisch drucken. Zudem kannst du Aufträge auf diese Versandart buchen und über die Logistik abwickeln. Trackinginformationen werden in xentral gespeichert und direkt über FedEx an die Kunden weitergeleitet.

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du[hier](https://help.xentral.com/hc/articles/360016722580#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

## Features

Folgende Features bietet dir die Versandart FedEx:

- Drucken eines Demo-Labels
- Angabe der Maße deiner Pakete
- Angabe des Paketmarkenformats in Zoll

## Anbindung von FedEx an xentral

Wie die Anbindung von FedEx an xentral funktioniert, kannst du in diesem Abschnitt nachlesen.

Die Kommunikation mit dem FedEx Server funktioniert über die FedEx API, welche du im Entwicklerbereich von FedEx findest. Dafür musst du dich unter[https://www.fedex.com/en-us/developer.html](https://www.fedex.com/en-us/developer.html)registrieren und einen Account anlegen. Dort erhältst du dann

- Fedex Key
- Fedex Passwort
- Fedex Account number
- Fedex Meter number

Weitere Informationen findest du[hier](http://www.fedex.com/ca_english/businesstools/webservices/Web_Services_Guide_ENG.pdf).

> **Wichtig**
>
> Achte bei der Verwendung der API unbedingt darauf, dass es <PaymentType>RECIPIENT</PaymentType> in der API heißt, auf keinen Fall <PaymentType>SENDER</PaymentType>.

> **Anmerkung**
>
> Der Entwicklerbereich von FedEx ist etwas anderes als dein eigentlicher Account, den du unterhttps://www.fedex.com/en-us/home.htmlaufrufst.

## Einrichtung der Versandart in xentral

Unter **Administration > Einstellungen > Versandarten > Übersicht > +NEU > Fedex ** fügst du eine neue Versandart hinzu. Wähle die Versandart**FedEx API** aus der angebotenen Liste der Module aus und konfiguriere die Versandart.

Befülle folgende Felder:

- **Bezeichnung:** Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ:** Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- **Modul: ** Wähle ** Fedex API** aus dem Drop-Down Menü aus
- **Projekt:** Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene Fedex Versandart angelegt wird
- **Aktiv:** Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck:** Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke:** Wähle aus dem Drop-Down Menü den Standarddrucker, welcher die Paketmarken druckt, aus
- **Drucker Export:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail:** Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutetet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Sender Name:** Gib den Namen des Senders ein
- **Sender Ansprechpartner:** Gib den Ansprechpartner beim Sender an
- **Sender Strasse:** Gib die Straße des Senders ein
- **Sender PLZ:** Gib die PLZ des Senders ein
- **Sender Ort:** Gib den Ort des Senders ein
- **Sender Land:** Gib das zweistellige ISO-Länderkürzel des Senders ein, bspw. DE für Deutschland und AT für Österreich
- **Sender E-Mail:** Gib die E-Mail Adresse des Senders ein
- **Sender Telefon:** Gib die Telefonnummer des Senders an
- **Tracking übernehmen:** Durch Anhaken wird die Trackingnr. nach dem Erstellen der Paketmarke in das Feld eingefügt und muss nicht mehr von der Paketmarke gescannt werden
- **Fedex Key:** Gib deinen Fedex Authentification Key ein
- **Fedex Passwort:** Gib dein Fedex Account Passwort ein. Dieses sollte dir zuvor per E-Mail zugeschickt worden sein
- **Fedex Account number:** Gib deine Fedex Shipping Accountnummer ein
- **Fedex Meter number:** Gib deine Fedex Web Services Meternummer ein
- **Demo Label drucken:** Durch Anhaken kannst du ein Fedex Demo Label drucken
- **Standardhöhe:** Gib die Standardhöhe deiner Pakete in cm an
- **Standardbreite:** Gib die Standardbreite deiner Pakete in cm an
- **Standardlänge:** Gib die Standardlänge deiner Pakete in cm an
- **label_stock_type:** Wähle aus dem Drop-Down Menü den Label Stocktyp aus, der das Format der Paketmarke in Zoll angibt

## Paketmarkendruck

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Paketmarkendruck im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Wähle dazu im Lieferschein im Reiter **Lieferschein ** die Versandart**Fedex** aus dem Drop-Down Menü aus:

![fedex2.png](https://help.xentral.com/hc/article_attachments/5009709278236)

Klicke auf die **Speichern**

-Schaltfläche, bevor du in den Paketmarkendialog navigierst.

Klicke im Anschluss im Lieferschein auf den Reiter **Paketmarke ** und drucke über**Paketmarke drucken** eine Paketmarke für die enthaltenen Artikel:

![fedex3.png](https://help.xentral.com/hc/article_attachments/5009709311772)

> **Anmerkung**
>
> Hier kannst du nochmal den Service-Typ zusätzlich auswählen, der die Lieferung der Pakete beeinflusst. Wähle INTERNATIONAL_ECONOMY oder INTERNATIONAL_PRIORITY aus dem Drop-Down Menü aus.

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss die Paketmarke im FedEx-Geschäftskundenportal stornieren.