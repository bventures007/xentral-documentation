### Voraussetzungen

Teste die Funktionalität deiner Schnittstelle vor Produktiv-Schaltung ausgiebig mit Hilfe der Funktionen im[Journal](https://help.xentral.com/hc/de/articles/14528034952476#UUID-0748de4e-37e4-85a3-21a3-6a2c51fcb42b), bei eingeschränkter[Artikelzuordnung](https://help.xentral.com/hc/de/articles/14528034786588#UUID-cfece960-9538-6fea-fdc4-64d9bbdfe08f).

### Achtung

Bevor du die Anbindung produktiv schaltest, stelle sicher, dass die Schnittstelle deine Testdaten richtig und wie erwartet übergibt.

Nach der Test-Phase erfolgt das Produktiv-Schalten in zwei Stufen:

1. Integrationsmodus je Feature aktivieren.
1. Produktivmodus der Schnittstelle aktivieren.

### Integrationsmodus je Feature aktivieren

Wenn du alle Einstellungen in der Artikelzuordnung und in den Workflows vorgenommen und getestet hast, kann es losgehen. Setze die Schaltfläche **Integrationsmodus ** bei allen Features, die du nutzen möchtest, nach rechts (Aktiv) und klicke auf**Speichern**.

![Shared_Workflows_Features_Integrationsmodus.png](https://help.xentral.com/hc/article_attachments/18670843163932)

Beim Umstellen der Schaltfläche erhälst du folgenden Hinweis:

![image-20240223-091306.png](https://help.xentral.com/hc/article_attachments/18670863785500)

> **Anmerkung**
>
> Falls Pflichtfelder (mit * gekennzeichnet) nicht ausgefüllt sind, erhälst du eine Fehlermeldung:
>
> Überprüfe in diesem Fall das betroffene Register auf nicht ausgefüllte Pflichtfelder und trage die entsprechenden Informationen ein:
>
> Klicke auf Speichern und wiederhole das Aktiv-Setzen der Schaltfläche **Integrationsmodus**.

Nachdem du alle gewünschten Features in den Integrationsmodus gesetzt hast, kannst du mit der Produktiv-Schaltung der Schnittstelle fortfahren.

### Produktivmodus der Schnittstelle aktivieren

Um die Schnittstelle in den Produktivmodus zu setzen, folge dem Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware6 Connector**. Wähle dann dasZahnrädchen.

![connect_modifysettings_overview.png](https://help.xentral.com/hc/article_attachments/18670863793564)

Setze dort die Schaltfläche **Produktivmodus aktivieren ** nach rechts (Aktiv) und klicke auf**Speichern**:

![Shared_Einstellungen_Produktivmodus.png](https://help.xentral.com/hc/article_attachments/18670863794972)

Anschließend werden die Prozesse zum Austausch der Daten gestartet und automatisch im Hintergrund ausgeführt.