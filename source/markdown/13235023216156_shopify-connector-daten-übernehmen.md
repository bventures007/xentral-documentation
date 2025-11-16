## Überblick

Mit dem initialen Datenimport kannst du im Shop vorhandene Daten an Xentral übertragen, bevor du mit deiner Anbindung loslegst.

## Voraussetzungen

Falls es in deinem Shop Artikel gibt, für die ein reduzierter Steuersatz gilt, müssen diese in Shopify einer sog. Kollektion zugewiesen worden sein.

## Vorüberlegungen

Bevor du mit dem Datenimport startest, solltest du grundsätzlich abwägen, in welchem System welche Daten vorhanden sind und ob du Daten vom Shop zu Xentral importieren möchtest. Dies bietet sich dann an, wenn du bereits viele gut gepflegte Artikeldaten im Shop vorliegen und dein Xentral gleichzeitig noch keine oder nur wenige Artikel beinhaltet. Bedenke, dass z. B. Einkaufsdaten wie Lieferanten und Staffel-Einkaufspreise in der Regel nicht im Shop gepflegt sind und daher anderweitig in Xentral nachgetragen werden müssen (z. B. über die[Importzentrale](https://help.xentral.com/hc/de/articles/360016758939#UUID-f547c6d9-743a-a701-602b-449b7a4acb24)oder manuell).

> **Warnung**
>
> Falls du eine Bereinigung der Daten vornehmen möchtest, so musst du dies vor dem initialen Datenimport durchführen. Die vorliegende Funktion ermöglicht nur eine Anzeige der zu importierenden Daten, jedoch keine Manipulation vor dem Import.

> **Anmerkung**
>
> Du kannst den initialen Datenimport dazu nutzen, zum Projektstart eine Datensicherung der Shop-Artikeldaten durchzuführen.

Im Fall, dass du mit deinem Shop frisch startest, oder wenn du einfach keine Artikel aus dem Shop in Xentral importieren möchtest, kannst du direkt mit der[Artikelzuordnung](https://help.xentral.com/hc/de/articles/13235060173596#UUID-6b6b31e2-79dc-2826-dd07-8cf4e4976109)fortfahren.

## Konfiguration

Zum Starten der Migration klicke in deiner gewünschten Anbindung aufEinstellungen > Verkaufen >ShopifyConnector. Wähle dann dasZahnrädchen.

Setze die Schaltfläche nach rechts (aktiv)...

![Shared_Einstellungen_Migrationsmodus.png](https://help.xentral.com/hc/article_attachments/18670852978204)

... und bestätige die Meldung, um die Schnittstelle in den Migrationsmodus zu setzen.

![Shared_Einstellungen_MigrationsmodusBestatigen.png](https://help.xentral.com/hc/article_attachments/18670809040412)

Klicke auf Speichern und kehre zurück zur Übersicht. Nun kannst du in deiner Anbindung den initialen Datenimport starten:

![Shared_Datenimport_Ubersicht.png](https://help.xentral.com/hc/article_attachments/18670852981020)

### Reiter “Einstellungen”

![image-20240312-155230.png](https://help.xentral.com/hc/article_attachments/13235041643164)

- **Projekt:** Wir empfehlen für jede Shop-Integration ein eigenes Projekt in Xentral anzulegen. Hier trägst du das Projekt für die jeweilige Anbindung ein.
- **Collection für reduzierte Steuersätze:** Falls es in deinem Shop Artikel gibt, für die ein reduzierter Steuersatz gilt, trage hier die entsprechende Kollektion aus Shopify ein, um die richtige Steuerberechnung sicherzustellen.
- **Steuersatz (normal):** Trage hier den Prozentwert (ohne Prozentzeichen) für normal besteuerte Artikel ein. (In Deutschland derzeit 19%)
- **Steuersatz (ermäßigt):** Trage hier den Prozentwert (ohne Prozentzeichen) für Artikel mit ermäßigtem Steuersatz ein. (In Deutschland derzeit 7%)
- **Preise inkl. Steuern (Brutto):** Stelle den Schalter auf rechts, wenn du im Shop Bruttopreise gepflegt hast und auf links für Nettopreise.

Klicke oben rechts aufSpeichern, um deine Einstellungen zu speichern und wechsele zum nächsten Reiter:

### Reiter “Artikel in Verkaufskanal identifizieren”

In diesem Reiter lädst du Artikel aus deinem Shop in eine Import-Vorschlagsliste.

> **Anmerkung**
>
> Falls du mehrere Anbindungen parallel laufen hast, werden dir Shop-Artikel von allen Anbindungen angezeigt.

1. Klicke auf (1a) Für Alle Artikel starten bzw. auf (1b) Für einzelnen Artikel starten und gib ggf. eine Shopify-SKU ein. Aktualisiere die Anzeige mit Neu Laden (2):
1. Nach dem Neu Laden siehst du nach und nach die zum Import vorgeschlagenen Daten und deren Status.
1. Prüfe die Daten auf Vollständigkeit und ihre Struktur.

> **Anmerkung**
>
> Überprüfe hier die Daten im Hinblick auf ihre Struktur.Stimmt die Artikelebene, also Container vs. Variante?Sind die Artikel vollständig? Falls dir an dieser Stelle auffällt, dass Daten nicht in Ordnung sind, oder nicht alle Artikel angezeigt werden, solltest du sie vor dem Import korrigieren.

Sobald du sichergestellt hast, dass die zu importierenden Daten korrekt sind, kannst du zum nächsten Reiter wechseln.

### Reiter “Artikel zu Xentral importieren”

In diesem Reiter startest du schließlich den Import zu Xentral.

> **Anmerkung**
>
> Falls du mehrere Anbindungen parallel laufen hast, werden dir Shop-Artikel von allen Anbindungen angezeigt.

1. Um Artikel zu importieren, klicke auf (1a) Für Alle Artikel starten bzw. auf (1b) Für einzelnen Artikel starten und gib ggf. eine Shopify-SKU ein. Aktualisiere die Anzeige mit Neu Laden (2). Sobald der Import startet, wird die Schaltfläche Migration beenden bis zum Abschluss der Migration ausgegraut.
1. Über Neu Laden kannst du den Import-Status aktualisieren. Hier kannst du bei jedem Artikel sehen, ob er schon importiert wurde oder noch zum Import ansteht.

> **Anmerkung**
>
> Eine genaue Einschätzung der Migrationsdauer ist nicht möglich, da sie sowohl von der Artikelanzahl, als auch von der Komplexität, Dateigröße der Bilder und anderen Faktoren abhängt. Bei einem Umfang von zwei- bis dreitausend Artikeln mit normaler Bildqualität kannst du mit etwa drei Stunden kalkulieren. Größere oder komplexere Datenbestände können durchaus einen ganzen Tag benötigen.

- Du kannst die Migration beenden, wenn die Schaltfläche wieder aktiv ist. Solange du diese Schaltfläche noch nicht geklickt hast, kannst du auch später nochmal zurückkehren und ggf. weitere Artikel importieren.

> **Anmerkung**
>
> Falls du später weitere Daten importieren möchtest, kannst du, auch nach Produktiv-Schaltung, den Produktivmodus deaktivieren und den Migrationsmodus aktivieren. So kannst du den Import erneut starten.

## Nächste Schritte

Anschließend kannst du in der Verwaltung mit der[Artikelzuordnung](https://help.xentral.com/hc/de/articles/13235060173596#UUID-6b6b31e2-79dc-2826-dd07-8cf4e4976109)fortfahren.

![Shared_Artikelzuordnung_Ubersicht.png](https://help.xentral.com/hc/article_attachments/18670852984988)