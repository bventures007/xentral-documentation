## Überblick

> **Anmerkung**
>
> Die hier beschriebene Funktion ist ausschließlich für Kunden relevant, die derzeit eine klassische Shop-Anbindung nutzen und auf die Xentral Connect Schnittstelle umstellen möchten.

In dieser Anleitung erfährst du, wie du in wenigen Schritten eine bestehende klassische Shop-Schnittstelle (Shopimporter) in die neue Xentral Connect-Schnittstelle migrieren kannst. Die Übernahme der Einstellungen aus der alten Schnittstelle in die Connect-Schnittstelle durchläuft folgende Schritte, die wir in den nächsten Abschnitten im Detail erläutern:

1. [Connect App in Xentral installieren](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-1AppinXentralinstallieren)
1. [Übernahmewizard starten](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-2bernahmewizarddurchfhren)
1. [Übernommene Einstellungen prüfen und testen](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-3bernommeneEinstellungenprfenundtesten)
  1. [Artikelzuordnung prüfen oder neu anlegen](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-aArtikelzuordnungprfenoderneuanlegen)
  1. [Workflow-Einstellungen prüfen](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-bWorkflow-Einstellungenprfen)
  1. [Workflows testen](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-cWorkflowstesten)
1. [Alten Shopimporter deaktivieren](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-4AltenShopimporterdeaktivieren)
1. [Connect-Schnittstelle testen und produktiv schalten](#UUID-6de2ece7-a6ef-36e4-311c-cda7397cfb63_id_MigrationeinerklassischenShop-AnbindungineineXentralConnectSchnittstelle-5ConnectSchnittstelleliveschalten)

## Voraussetzungen

Um eine reibungslose Übernahme und Funktionalität der Schnittstelle zu gewährleisten, ist es wichtig, zunächst einige allgemeine Einstellungen in Xentral durchzuführen. Beachte dazu diesen[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62). Prüfe deine Einstellungen insbesondere dann, wenn deine bisherige Shop-Schnittstelle individuell angepasst war, z. B. über Smarty.

Die Connect-Schnittstelle bietet eine hohe Standardisierung, was die Wartbarkeit und die Upgradefähigkeit deines Systems erhöht. Viele Funktionen, die in der klassischen Schnittstelle nur über einer individuelle Anpassung möglich waren, sind in Connect im Standard bereits enthalten. Bei der Übernahme einer individuell angepassten klassischen Schnittstelle musst du die Einstellungen jedoch sorgsam vornehmen und auf das korrekte Verknüpfen von Datenfeldern (sog. Mapping) achten. Nimm im Zweifel vorher Kontakt zu deinem Solution Consultant auf.

## 1. Connect App in Xentral installieren

> **Anmerkung**
>
> Dieser Schritt ist nur für die erste Anbindung eines Shops erforderlich und entfällt bei weiteren Integrationen desselben Shop-Anbieters.

> **Anmerkung**
>
> Wir schalten die Funktion schrittweise frei, um eine maximale Stabilität und die reibungslose Migration zu gewährleisten. Du bekommst von uns aktiv in der Software Bescheid, sobald die Xentral Connect-Schnittstelle für Dich zur Verfügung steht. Möchtest du vorzeitig Zugriff haben, wende dich gerne an deinen Solution Consultant.

![Shared_NeueAnbindung_Pfad.png](https://help.xentral.com/hc/article_attachments/18680610398620)

1. Klicke in deinem Xentral auf das Zahnrädchen oben rechts, um zu den Systemeinstellungen zu gelangen:
1. Folge dem Menüpfad **Einstellungen > Verkaufen > […] Connector** (hier als Beispiel: WooCommerce Connector)
1. Klicke jetzt auf **Install App** um das System vorzubereiten:

Sobald die Connect-Schnittstelle angelegt wurde, kannst du mit dem Übernahmewizard fortfahren.

## 2. Übernahmewizard durchführen

### Für Shopify-Anbindungen

1. Klicke auf **Integration übernehmen**, um den Wizard zu starten:
1. Wähle die bestehende Shop-Anbindung, aus der du die Einstellungen zu Xentral Connect übernehmen möchtest und klicke auf **Weiter**.
1. Du kannst die Anbindung ganz bequem über die Shopify Public App aufsetzen und sparst dir so das manuelle Setzen von so keine Berechtigungen. Alternativ kannst du einen bestehenden API Token oder eine Custom App mit neuem Token verwenden:
  1. Um die Anbindung über die Public App aufzusetzen, belasse die ersten beiden Schaltflächen deaktiviert (links):
  1. Wenn deine vorhandene App alle Berechtigungen gesetzt hat und du diese weiter nutzen möchtest, kannst du den bestehenden API Token weiter verwenden. Setze dazu die erste Schaltfläche nach rechts:
  1. Wenn du eine Custom App mit neuem Token nutzen möchtest, lasse die erste Schaltfläche deaktiviert (links) und setze die zweite Schaltfläche nach rechts. Du kannst dann im nächsten Feld den Token einfügen:
1. Falls es in deinem Shop Artikel gibt, für die ein reduzierter Steuersatz und/oder eine Steuerbefreiung gilt, wähle in den nächsten beiden Feldern die entsprechende Kollektion aus Shopify aus, um die richtige Steuerberechnung sicherzustellen:
1. Wähle anschließend die Art der Artikelzuordnung. Du kannst…
  1. … die Artikelzuordnung von deiner bestehenden Anbindung übernehmen oder
  1. … eine neue Artikelzuordnung anhand selbst gewählter Kriterien einrichten. Wenn du diese Option wählst, kannst du die Filterkriterien für die Artikelzuordnung nach Abschluss des Wizards eintragen.
1. Belasse den Schalter **Bilderübertragung** auf links, wenn Bilder aus dem Onlineshop weiter verwendet werden sollen. Du kannst die Synchronisierung von Bilddateien zwischen Xentral und Shop später in den Workflows aktivieren. (Nur falls du sichergestellt hast, dass die Artikelbilder in Xentral vollständig und aktuell sind, kannst du den Schalter nach rechts setzen. In diesem Fall werden alle im Shop vorhandenen Bilder von den Bildern in Xentral ersetzt.)
1. Bestätige die Übernahme der Schnittstellen-Konfiguration und beachte die Hinweise:
1. Markiere deinen Shopify-Account in der Liste und warte einen Moment:
1. Im Hintergrund werden nun die Shopify-App installiert und alle benötigten Rechte automatisch gesetzt. Sobald die Anbindung erfolgreich abgeschlossen ist, erhälst du eine Bestätigung auf deinem Bildschirm:

### Für Shopware 6-Anbindungen

![SW6_Migrationswizard_IntegrationUbernehmen.png](https://help.xentral.com/hc/article_attachments/18680627201052)

1. Klicke auf **Integration übernehmen**, um den Wizard zu starten:
1. Wähle die bestehende Shop-Anbindung, aus der du die Einstellungen zu Xentral Connect übernehmen möchtest und klicke auf **Weiter**.
1. Gib anschließend deine Shopware 6-Zugangsdaten ein (bestätige die Daten im sich öffnenden Shopware 6-Fenster, sobald du dazu aufgefordert wirst)...
1.... und wähle die Art der Artikelzuordnung. Du kannst…
  1. … die Artikelzuordnung von deiner bestehenden Anbindung übernehmen oder
  1. … eine neue Artikelzuordnung anhand selbst gewählter Kriterien einrichten. Wenn du diese Option wählst, kannst du die Filterkriterien für die Artikelzuordnung nach Abschluss des Wizards eintragen.
1. Belasse den Schalter **Bilderübertragung** auf links, wenn Bilder aus dem Onlineshop weiter verwendet werden sollen. Du kannst die Synchronisierung von Bilddateien zwischen Xentral und Shop später in den Workflows aktivieren. (Nur falls du sichergestellt hast, dass die Artikelbilder in Xentral vollständig und aktuell sind, kannst du den Schalter nach rechts setzen. In diesem Fall werden alle im Shop vorhandenen Bilder von den Bildern in Xentral ersetzt.)
1. Bestätige die Übernahme der Schnittstellen-Konfiguration und beachte die Hinweise:
1. Die Integration wird angelegt:
1. Nach Abschluss erhälst du eine Erfolgsmeldung:

### Für WooCommerce-Anbindungen

![Shared_Migrationswizard_WichtigeHinweise.png](https://help.xentral.com/hc/article_attachments/18680627213084)

1. Klicke auf **Integration übernehmen**, um den Wizard zu starten:
1. Wähle die bestehende Shop-Anbindung, aus der du die Einstellungen zu Xentral Connect übernehmen möchtest und klicke auf **Weiter**.
1. Wähle anschließend die Art der Artikelzuordnung. Du kannst…
  1. … die Artikelzuordnung von deiner bestehenden Anbindung übernehmen oder
  1. … eine neue Artikelzuordnung anhand selbst gewählter Kriterien einrichten. Wenn du diese Option wählst, kannst du die Filterkriterien für die Artikelzuordnung nach Abschluss des Wizards eintragen.
1. Belasse den Schalter **Bilderübertragung** auf links, wenn Bilder aus dem Onlineshop weiter verwendet werden sollen. Du kannst die Synchronisierung von Bilddateien zwischen Xentral und Shop später in den Workflows aktivieren. (Nur falls du sichergestellt hast, dass die Artikelbilder in Xentral vollständig und aktuell sind, kannst du den Schalter nach rechts setzen. In diesem Fall werden alle im Shop vorhandenen Bilder von den Bildern in Xentral ersetzt.)
1. Bestätige die Übernahme der Schnittstellen-Konfiguration und beachte die Hinweise:
1. Die Integration wird angelegt:
1. Nach Abschluss erhälst du eine Erfolgsmeldung:

## 3. Übernommene Einstellungen prüfen und testen

Bevor du die Liveschaltung aktivierst, solltest du alle übernommenen Einstellungen gründlich überprüfen. Dazu gehören die Artikelzuordnung und die Workflow-Konfiguration.

### a. Artikelzuordnung prüfen oder neu anlegen

Um die Artikelzuordnung zu prüfen oder neu anzulegen, klicke auf diese Schaltfläche:

![Migration_Shopimporter8.png](https://help.xentral.com/hc/article_attachments/15467586979228)

#### Artikelzuordnung prüfen

> **Anmerkung**
>
> Dieser Abschnitt ist relevant, falls du im Wizard **Artikelzuordnung aus der bestehenden Integration übernehmen** gewählt hast.

Die vorhandene Zuordnung ist hier bereits eingetragen. Stelle sicher, dass die gefundene Anzahl der Artikel korrekt ist. Falls sie nicht deinen Erwartungen entspricht, überprüfe die **Online-Shop Optionen** in den Artikeln oder lege deine Artikelzuordnung neu an, wie im nächsten Abschnitt beschrieben.

![Migration_Shopimporter10.png](https://help.xentral.com/hc/article_attachments/15467556320284)

#### Artikelzuordnung neu anlegen

> **Anmerkung**
>
> Dieser Abschnitt ist relevant, falls du im Wizard **Artikel anhand einer definierten Regel (z. B. Projekt, Freifeld etc. zuordnen** gewählt hast oder dich später entscheidest, eine neue Artikelzuordnung zu definieren.

Richte dir die Filterkriterien nach deinem Bedarf ein. Schaue dir dazu den Handbuchabschnitt[Artikel zuordnen](https://help.xentral.com/hc/de/articles/13235023557532#UUID-2e1a76ae-2150-3aca-98cf-7f80d6c6f0b7)an.

> **Anmerkung**
>
> Der Link hier verweist beispielhaft auf WooCommerce. Die Artikelzuordnung erfolgt in allen Shop-Schnittstellen gleich.

### b. Workflow-Einstellungen prüfen

Um die Workflows zu prüfen oder anzupassen, klicke auf diese Schaltfläche:

![Migration_Shopimporter9.png](https://help.xentral.com/hc/article_attachments/15467578596252)

Überprüfe in allen Reitern, ob die übernommenen Einstellungen deiner Erwartung entsprechen, falls nicht, nehme Änderungen vor und speichere sie. Detaillierte Anleitungen zu den Workflows findest du in den einzelnen Shop-Handbüchern:

[Shopify: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/13235060220444#UUID-55e1cf94-dd5f-eb68-4337-cabda5e7ee49)

[Woo-Commerce: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/13234992002460#UUID-2da1fca7-0bf6-4ed1-5caa-064075c28cd0)

[Shopware6: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/14528034840732#UUID-b0386169-a59f-1d8d-1375-62b9ba1825d5)

Falls du die Bilderübertragung beim Übernahmewizard deaktiviert hattest und Bilder zwischen Xentral und Shop synchronisieren möchtest, aktiviere die entsprechende Schaltfläche. Du findest sie in den **Workflows > Reiter Artikel > Datentypen**:

![Migration_Shopimporter14.png](https://help.xentral.com/hc/article_attachments/15467587160732)

### c. Workflows testen

Mit Hilfe des Journals kannst du einzelne Testdaten anstoßen und deren korrekte Übertragung testen. Um zum Journal zu gelangen, klicke auf diese Schaltfläche:

![Migration_Shopimporter16.png](https://help.xentral.com/hc/article_attachments/15467578702108)

Stoße für jeden Datentyp, den du nutzen möchtest - also z. B. Artikel und Aufträge - einzelne Datensätze zur Synchronisierung an, indem du beispielsweise bei einem Artikel auf **Artikel synchronisieren ** oder bei den Aufträgen auf **Workflow starten ** klickst und eine Auftragsnummer eingibst. Anschließend aktualisierst du den Status durch die**Neu laden**

-Schaltfläche und prüfst, ob die Datenübertragung funktioniert. Falls nicht, orientiere dich an den Fehlerhinweisen im Journal und nimm Korrekturen vor. Nähere Informationen zur Nutzung des Journals findest du in den einzelnen Shop-Handbüchern:

[Shopify: Journal](https://help.xentral.com/hc/de/articles/13921857699612#UUID-d8ed9992-afac-447b-5f28-2e5f96fd98ac)

Die Schnittstelle synchronisiert nach der Produktiv-Schaltung - je nach Feature Artikel, Bestände, Preise, Aufträge und Auftragsstatus - automatisch zwischen Xentral und deinem Shop. Der Prozessstarter ist dafür nicht mehr erforderlich.

[WooCommerce: Journal](https://help.xentral.com/hc/de/articles/13921840987036#UUID-24f64971-99da-b968-5ba9-ff6a97dfabb5)

[Shopware6: Journal](https://help.xentral.com/hc/de/articles/14528034952476#UUID-0748de4e-37e4-85a3-21a3-6a2c51fcb42b)

## 4. Alten Shopimporter deaktivieren

Nachdem du alle Einstellungen erfolgreich geprüft hast, ist deine neue Xentral Connect Schnittstelle grundsätzlich bereit zur Liveschaltung.

> **Warnung**
>
> Stelle sicher, dass du den Livemodus der alten Shop-Anbindung **deaktivierst**, bevor du die Connect-Schnittstelle live schaltest, um Konflikte und doppelte Auftragsimporte zu vermeiden!
>
> **Die alte Shop-Integration ** muss weiterhin im System verbleiben und **darf nicht gelöscht werden**!

Um die alte Shop-Anbindung zu deaktivieren, führe folgendes aus:

1. Navigiere zur Übersicht der Shops & Marktplätze: **Systemeinstellungen (Zahnrädchen) > Verkaufen > Shops & Marktplätze Übersicht**. Öffne die zu deaktivierende Schnittstelle:
1. Entferne den Haken **Aktiv **, entferne die Einträge in den Feldern ** URL **, ** API-Key **, ** Passwort **, ** Token ** und klicke unten auf der Seite auf **Speichern**:
1. Stelle in der Übersicht sicher, dass die alte Schnittstelle deaktiviert ist:

## 5. Connect-Schnittstelle testen und produktiv schalten

Mehr Informationen zur Xentral Connect-Schnittstelle und ihrer Konfiguration, findest du in den Handbuch-Artikel des jeweiligen Shop-Systems. Hier ist auch beschrieben, wie du die Schnittstelle vor der Produktiv-Schaltung testen kannst:

[Shopify Connector: Überblick](https://help.xentral.com/hc/de/articles/13235060016796#UUID-ececee00-f23a-e3d2-f4be-6a460247b779)

[Shopware6-Connector: Überblick](https://help.xentral.com/hc/de/articles/14528018649244#UUID-9a01cf3b-a21b-b87d-fef7-25e98b30175a)

[WooCommerce Connector: Überblick](https://help.xentral.com/hc/de/articles/13235023397404#UUID-37643e86-d675-5eb3-89cb-8885a658df23)

> **Warnung**
>
> Stelle sicher, dass die alte Schnittstelle wie im vorherigen Abschnitt beschrieben **deaktiviert** ist, bevor du die Connect-Schnittstelle produktiv schaltest, um Konflikte und doppelte Auftragsimporte zu vermeiden!
>
> **Die alte Shop-Integration ** muss jedoch weiterhin im System verbleiben und **darf nicht gelöscht werden**!

Nach Überprüfung der Konfiguration kannst du den Produktiv-Modus aktivieren. Wie du dabei vorgehst, erfährst du in diesen Artikeln:

[Shopify Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589752911516#UUID-e51cce39-191a-dec1-8f90-44b0af01a9f4)

[Shopware6-Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589763018012#UUID-51edb066-e697-e70b-6116-829fdd05e479)

[WooCommerce Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589740730012#UUID-3482c0db-0cbb-26a5-6a44-9a82f4cfb81a)