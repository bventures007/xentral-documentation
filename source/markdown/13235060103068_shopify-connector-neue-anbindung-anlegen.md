## Voraussetzungen

Vergewissere dich mit Hilfe der[Checkliste](https://help.xentral.com/hc/de/articles/13235039238428#UUID-7b472917-dd79-f7ac-843a-cc4ef7e3c691_id_xentralConnect-ChecklisteShop-AnbindungChecklisteShopAnbindung), dass du alle Voraussetzungen geschaffen hast, die eine reibungslose Anbindung ermöglichen.

> **Tipp**
>
> Wenn du von einer klassischen Schnittstelle auf Connect wechselst, findest du in diesemArtikeleine Schritt-für-Schritt-Anleitung für die Migration.

## App in Xentral installieren (einmalig)

> **Anmerkung**
>
> Dieser Schritt ist nur für die allererste Anbindung erforderlich und entfällt bei weiteren Integrationen.

1. Klicke in deinem Xentral auf das Zahnrädchen oben rechts, um zu den Systemeinstellungen zu gelangen:
1. Folge dem Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopify Connector**.
1. Klicke jetzt auf **Install App** um das System vorzubereiten. Im Hintergrund wird ein Container für die Workflows angelegt.

Du kannst nun mit der Einrichtung der Anbindung fortfahren.

## Einrichtungswizard durchführen

### Starten

1. Öffne im Xentral-Fenster den Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopify Connector ** und klicke auf **+ Neue Integration**, um den Einrichtungswizard zu starten:
1. Vergib bei den **Basisdaten** einen Namen deiner Wahl, um die Anbindung später identifizieren zu können.
1. Klicke auf **Weiter.**

### Empfohlen: Über die Shopify Public App verbinden

> **Anmerkung**
>
> Wir empfehlen, die Shop-Schnittstelle über die Public App anzubinden. So stellst du eine problemlose Authentifizierung sicher.

1. Um die Anbindung über die Public App aufzusetzen, belasse den Schalter aktiv (rechts) und klicke auf **Meinen Verkaufskanal verbinden**.
1. Markiere deinen Shopify-Account in der Liste und warte einen Moment:
1. Im Hintergrund werden nun die Shopify-App installiert und alle benötigten Rechte automatisch gesetzt. Sobald die Anbindung erfolgreich abgeschlossen ist, erhälst du eine Bestätigung auf deinem Bildschirm:

### Alternativ: Über eine Shopify Custom App verbinden

> **Warnung**
>
> Wir empfehlen, die Shop-Schnittstelle über die Public App (siehe oben) zu verbinden. So sparst du dir das manuelle Setzen von Berechtigungen. Falls du die Verbindung dennoch über eine Custom App aufsetzen möchtest, stelle sicher, dass du die Berechtigungen so gesetzt hast, wie unterOptional: Berechtigungen setzenbeschrieben.

> **Warnung**
>
> Der Token wird nur einmal zum Kopieren zur Verfügung gestellt. Stelle sicher, dass du die Einrichtung der Anbindung jetzt durchführen kannst. Alternativ halte einen Passwort-Safe bereit und sichere den Token dort für später.

1. Um die Anbindung über eine Custom App aufzusetzen, deaktiviere die Schaltfläche (links).
1. Wechsele zum Shopify-Fenster und klicke dort auf **API-Anmeldedaten**, um den API-Zugriffstoken anzuzeigen.
1. Klicke auf **Token einmalig einblenden** und kopiere ihn in die Zwischenablage.
1. Wechsele nun **zurück zum Xentral-Fenster** und fahre mit den Zugangsdaten fort.
1. Füge den **Token ** aus der Zwischenablage ein und tippe die **URL** deiner Shopify-Instanz ein:
1. Klicke auf **Verbindung testen **, um die Zugangsdaten zu verifizieren und eine Verbindung aufzubauen. Sobald die Verbindung erfolgreich aufgebaut wurde, klicke auf ** Weiter**.

### Features

Hier wählst du, welche Datentypen du grundsätzlich zwischen deinemShopund Xentral austauschen möchtest. Wir empfehlen, alle Features zu aktivieren. Du kannst sie später einzeln in den Integrations-Modus setzen und festlegen, welche genauen Daten eines Features zwischen den Systemen ausgetauscht werden.

> **Anmerkung**
>
> Beispiel: Du setzt hier **Artikel (exkl. Preise und Bestände) abgleichen (Xentral > Shop)** aktiv und bestimmst später in der Verwaltung, dass du zwar die Artikelnummer synchronisierst, aber nicht den Artikelnamen.

1. Wähle ein Feature, indem du den jeweiligen Schalter nach rechts stellst:
1. Klicke auf **Speichern**, um die Schnittstelle anzulegen. Dies dauert einen kurzen Moment.

## Nächste Schritte

Anschließend kannst du in der Verwaltung mitder[Artikelzuordnung](https://help.xentral.com/hc/de/articles/13235060173596#UUID-6b6b31e2-79dc-2826-dd07-8cf4e4976109)fortfahren.

![Shared_Artikelzuordnung_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19129557269532)

Falls du Artikeldaten aus deinem Shop übernehmen möchtest, findest du[hier](https://help.xentral.com/hc/de/articles/13235023216156#UUID-e411fce4-0b3a-6983-0e8d-e8686b8f38ad)eine Anleitung zur Datenübernahme.