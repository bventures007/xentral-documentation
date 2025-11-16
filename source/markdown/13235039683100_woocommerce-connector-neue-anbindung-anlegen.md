## Voraussetzungen

Vergewissere dich mit Hilfe der[Checkliste](https://help.xentral.com/hc/de/articles/13235039238428#UUID-7b472917-dd79-f7ac-843a-cc4ef7e3c691_id_xentralConnect-ChecklisteShop-AnbindungChecklisteShopAnbindung), dass du alle Voraussetzungen geschaffen hast, die eine reibungslose Anbindung ermöglichen.

> **Tipp**
>
> Wenn du von einer klassischen Schnittstelle auf Connect wechselst, findest du in diesemArtikeleine Schritt-für-Schritt-Anleitung für die Migration.

> **Anmerkung**
>
> Für die nächsten Schritte benötigst du Zugriff auf beide Systeme. InWooCommercemusst du als Administrator angemeldet sein. Wir empfehlen, die Shop-/Marktplatz-Verwaltung in einem und Xentral in einem anderen Browserfenster parallel zu öffnen.

## App in Xentral installieren (einmalig)

> **Anmerkung**
>
> Dieser Schritt ist nur für die allererste Anbindung erforderlich und entfällt bei weiteren Integrationen.

1. Klicke in deinem Xentral auf das Zahnrädchen oben rechts, um zu den Systemeinstellungen zu gelangen:
1. Folge dem Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > WooCommerce Connector**.
1. Klicke jetzt auf **Install App** um das System vorzubereiten. Im Hintergrund wird ein Container für die Workflows angelegt.

Du kannst nun mit der Einrichtung der Anbindung fortfahren.

## Einrichtungswizard durchführen

### Starten

1. Öffne im Xentral-Fenster den Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > WooCommerce Connector ** und klicke auf **+ Neue Integration**, um den Einrichtungswizard zu starten:
1. Vergib bei den **Basisdaten** einen Namen deiner Wahl, um die Anbindung später identifizieren zu können.
1. Klicke auf **Weiter** und wechsele zur Shop-/Marktplatz-Verwaltung.

### Consumer Key & Consumer Secret im Shop generieren

> **Warnung**
>
> Consumer Key und Consumer Secret werden im Shop nur solange zum Kopieren zur Verfügung gestellt, bis die Seite verlassen wird. Stelle sicher, dass du die Einrichtung der Anbindung jetzt durchführen kannst. Alternativ halte einen Passwort-Safe bereit und sichere die Zugangsdaten dort für später.

1. Klicke im WooCommerce-Fenster auf Einstellungen, Erweitert und dort auf “REST-API”, um die Zugangsdaten anzuzeigen.
1. Klicke auf Schlüssel hinzufügen.
1. Wähle im Feld “Berechtigungen” Schreiben/Lesen aus.
1. Kopiere den Consumer-Key.
1. Wechsele nun zurück zum Xentral-Fenster und fahre mit den Zugangsdaten fort.
1. Gib die URL deiner WooCommerce-Instanz ein und füge den Consumer-Key aus der Zwischenablage ein:
1. Wechsle erneut zum WooCommerce-Fenster und kopiere das Consumer Secret. Füge es anschließend ebenfalls hier ein.
1. Klicke auf Verbindung testen, um die Zugangsdaten zu verifizieren und eine Verbindung aufzubauen. Sobald die Verbindung erfolgreich aufgebaut wurde, klicke auf Weiter.

### Features

Hier wählst du, welche Datentypen du grundsätzlich zwischen deinemShopund Xentral austauschen möchtest. Wir empfehlen, alle Features zu aktivieren. Du kannst sie später einzeln in den Integrations-Modus setzen und festlegen, welche genauen Daten eines Features zwischen den Systemen ausgetauscht werden.

> **Anmerkung**
>
> Beispiel: Du setzt hier **Artikel (exkl. Preise und Bestände) abgleichen (Xentral > Shop)** aktiv und bestimmst später in der Verwaltung, dass du zwar die Artikelnummer synchronisierst, aber nicht den Artikelnamen.

1. Wähle ein Feature, indem du den jeweiligen Schalter nach rechts stellst:
1. Klicke auf **Speichern**, um die Schnittstelle anzulegen. Dies dauert einen kurzen Moment.

## Nächste Schritte

Anschließend kannst du in der Verwaltung mitder[Artikelzuordnung](https://help.xentral.com/hc/de/articles/13235023557532#UUID-2e1a76ae-2150-3aca-98cf-7f80d6c6f0b7)fortfahren.

![Shared_Artikelzuordnung_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19129562824092)

Falls du Artikeldaten aus deinem Shop übernehmen möchtest, findest du[hier](https://help.xentral.com/hc/de/articles/13235023523228#UUID-e7601775-eed8-d291-fa9f-32518eb82b8a)eine Anleitung zur Datenübernahme.