## Voraussetzungen

Vergewissere dich mit Hilfe der[Checkliste](https://help.xentral.com/hc/de/articles/13235039238428#UUID-7b472917-dd79-f7ac-843a-cc4ef7e3c691_id_xentralConnect-ChecklisteShop-AnbindungChecklisteShopAnbindung), dass du alle Voraussetzungen geschaffen hast, die eine reibungslose Anbindung ermöglichen.

> **Tipp**
>
> Wenn du von einer klassischen Schnittstelle auf Connect wechselst, findest du in diesemArtikeleine Schritt-für-Schritt-Anleitung für die Migration.

> **Anmerkung**
>
> Für die nächsten Schritte benötigst du Zugriff auf beide Systeme. InShopware 6musst du als Administrator angemeldet sein. Wir empfehlen, die Shop-/Marktplatz-Verwaltung in einem und Xentral in einem anderen Browserfenster parallel zu öffnen.

## App in Xentral installieren (einmalig)

> **Anmerkung**
>
> Dieser Schritt ist nur für die allererste Anbindung erforderlich und entfällt bei weiteren Integrationen.

1. Klicke in deinem Xentral auf das Zahnrädchen oben rechts, um zu den Systemeinstellungen zu gelangen:
1. Folge dem Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware 6 Connector**.
1. Klicke jetzt auf **Install App** um das System vorzubereiten. Im Hintergrund wird ein Container für die Workflows angelegt.

Du kannst nun mit der Einrichtung der Anbindung fortfahren.

## Einrichtungswizard durchführen

### Starten

1. Öffne im Xentral-Fenster den Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware6 Connector ** und klicke auf **+ Neue Integration**, um den Einrichtungswizard zu starten:
1. Vergib bei den **Basisdaten** einen Namen deiner Wahl, um die Anbindung später identifizieren zu können.
1. Klicke auf **Weiter** und wechsele zur Shop-/Marktplatz-Verwaltung.

### API-Daten im Shop erzeugen

> **Warnung**
>
> Zugangs-ID und Sicherheitsschlüssel werden nur einmal zum Kopieren zur Verfügung gestellt. Stelle sicher, dass du die Einrichtung der Anbindung jetzt durchführen kannst. Alternativ halte einen Passwort-Safe bereit und sichere die Daten dort für später.

1. Navigiere im Shopware-Fenster auf **Einstellungen > System > Integrationen. **

1. Klicke auf **Integration hinzufügen. **

1. Gib einen Namen für die Integration ein, um sie identifizieren zu können und wähle **Administrator** aus.
1. Kopiere die Zugangs-ID.
1. Wechsele nun **zurück zum Xentral-Fenster** und fahre mit den Zugangsdaten fort.
1. Gib die URL deiner Shopware-Instanz ein und füge die **Zugangs-ID** aus der Zwischenablage ein.
1. Wechsele erneut **zum Shopware-Fenster ** und kopiere den **Sicherheitsschlüssel**. Füge ihn anschließend ebenfalls hier ein.
1. Klicke auf **Verbindung testen **, um die Zugangsdaten zu verifizieren und eine Verbindung aufzubauen. Sobald die Verbindung erfolgreich aufgebaut wurde, klicke auf ** Weiter**.

#### Features

Hier wählst du, welche Datentypen du grundsätzlich zwischen deinemShopund Xentral austauschen möchtest. Wir empfehlen, alle Features zu aktivieren. Du kannst sie später einzeln in den Integrations-Modus setzen und festlegen, welche genauen Daten eines Features zwischen den Systemen ausgetauscht werden.

> **Anmerkung**
>
> Beispiel: Du setzt hier **Artikel (exkl. Preise und Bestände) abgleichen (Xentral > Shop)** aktiv und bestimmst später in der Verwaltung, dass du zwar die Artikelnummer synchronisierst, aber nicht den Artikelnamen.

1. Wähle ein Feature, indem du den jeweiligen Schalter nach rechts stellst:
1. Klicke auf **Speichern**, um die Schnittstelle anzulegen. Dies dauert einen kurzen Moment.

## Nächste Schritte

Anschließend kannst du in der Verwaltung mitder[Artikelzuordnung](https://help.xentral.com/hc/de/articles/14528034786588#UUID-cfece960-9538-6fea-fdc4-64d9bbdfe08f)fortfahren.

![Shared_Artikelzuordnung_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19385107563804)

Falls du Artikeldaten aus deinem Shop übernehmen möchtest, findest du[hier](https://help.xentral.com/hc/de/articles/19385101720220#UUID-aa9bd09e-88ec-92c2-3b68-00a605cfc2c4)eine Anleitung zur Datenübernahme.