## Anwendungsbereich

> **Anmerkung**
>
> Der Datenimport dient der einmaligen Übertragung von Artikeln von Shopware5 an Xentral, um den Umstieg auf Shopware 6 zu unterstützen.

### Achtung

Falls du eine Bereinigung der Daten vornehmen möchtest, so musst du dies vor dem Import durchführen. Die Importfunktion ermöglicht nur eine Anzeige der zu importierenden Daten, jedoch keine Manipulation vor dem Import.

## Konfiguration

Zum Starten der Migration klicke in deiner gewünschten Anbindung aufEinstellungen > Verkaufen >Shopware5Connector. Wähle dann dasZahnrädchen.

Setze die Schaltfläche nach rechts (aktiv)...

![Shared_Einstellungen_Migrationsmodus.png](https://help.xentral.com/hc/article_attachments/20345604778524)

... und bestätige die Meldung, um die Schnittstelle in den Migrationsmodus zu setzen.

![Shared_Einstellungen_MigrationsmodusBestatigen.png](https://help.xentral.com/hc/article_attachments/20345630679836)

Klicke auf Speichern und kehre zurück zur Übersicht. Nun kannst du in deiner Anbindung den initialen Datenimport starten:

![2811986143.png](https://help.xentral.com/hc/article_attachments/15365067608604)

### Reiter “Einstellungen”

![connect_datamigration_shopware5.png](https://help.xentral.com/hc/article_attachments/14528200800796)

- **Projekt:** Wir empfehlen für jede Shop-Integration ein eigenes Projekt in Xentral anzulegen. Hier trägst du das Projekt für die jeweilige Anbindung ein.
- **Steuersatz (normal):** Trage hier den Prozentwert (ohne Prozentzeichen) für normal besteuerte Artikel ein. (In Deutschland derzeit 19%)
- **Steuersatz (ermäßigt):** Trage hier den Prozentwert (ohne Prozentzeichen) für Artikel mit ermäßigtem Steuersatz ein. (In Deutschland derzeit 7%)
- **Preise inkl. Steuern (Brutto):** Stelle den Schalter auf rechts, wenn du im Shop Bruttopreise gepflegt hast und auf links für Nettopreise.

Klicke oben rechts aufSpeichern, um deine Einstellungen zu speichern und wechsele zum nächsten Reiter:

### Reiter “Artikel in Verkaufskanal identifizieren”

In diesem Reiter lädst du Artikel aus deinem Shop in eine Import-Vorschlagsliste.

> **Anmerkung**
>
> Falls du mehrere Anbindungen parallel laufen hast, werden dir Shop-Artikel von allen Anbindungen angezeigt.

1. Klicke auf (1a) Für Alle Artikel starten bzw. auf (1b) Für einzelnen Artikel starten und gib ggf. eine Shopware5-Artikelnummer ein. Aktualisiere die Anzeige mit Neu Laden (2):
1. Nach dem Neu Laden siehst du nach und nach die zum Import vorgeschlagenen Daten und deren Status.
1. Prüfe die Daten auf Vollständigkeit und ihre Struktur.

> **Anmerkung**
>
> Überprüfe hier die Daten im Hinblick auf ihre Struktur. Sind die Artikel vollständig? Falls dir an dieser Stelle auffällt, dass Daten nicht in Ordnung sind, oder nicht alle Artikel angezeigt werden, solltest du sie vor dem Import korrigieren.

Sobald du sichergestellt hast, dass die zu importierenden Daten korrekt sind, kannst du zum nächsten Reiter wechseln.

### Reiter “Artikel zu Xentral importieren”

In diesem Reiter startest du schließlich den Import zu Xentral.

> **Anmerkung**
>
> Falls du mehrere Anbindungen parallel laufen hast, werden dir Shop-Artikel von allen Anbindungen angezeigt.

### Achtung

Der Import beginnt unmittelbar durch Klicken aufFür Alle Artikel starten. Stelle vorher sicher, dass die Datenqualität stimmt.

1. Um Artikel zu importieren, klicke auf (1a) Für Alle Artikel starten bzw. auf (1b) Für einzelnen Artikel starten und gib ggf. eine Shopware5-Artikelnummer ein. Aktualisiere die Anzeige mit Neu Laden (2). Sobald der Import startet, wird die Schaltfläche Migration beenden bis zum Abschluss der Migration ausgegraut.
1. Über Neu Laden kannst du den Import-Status aktualisieren. Hier kannst du bei jedem Artikel sehen, ob er schon importiert wurde oder noch zum Import ansteht.

> **Anmerkung**
>
> Eine genaue Einschätzung der Migrationsdauer ist nicht möglich, da sie sowohl von der Artikelanzahl, als auch von der Komplexität, Dateigröße der Bilder und anderen Faktoren abhängt. Bei einem Umfang von zwei- bis dreitausend Artikeln mit normaler Bildqualität kannst du mit etwa drei Stunden kalkulieren. Größere oder komplexere Datenbestände können durchaus einen ganzen Tag benötigen.

- Du kannst die Migration beenden, wenn die Schaltfläche wieder aktiv ist. Solange du diese Schaltfläche noch nicht geklickt hast, kannst du auch später nochmal zurückkehren und ggf. weitere Artikel importieren.

> **Anmerkung**
>
> Falls du später weitere Daten importieren möchtest, kannst du, auch nach Produktiv-Schaltung, den Produktivmodus deaktivieren und den Migrationsmodus aktivieren. So kannst du den Import erneut starten.

## Nächste Schritte

Deine Artikel wurden nun von Shopware5 in Xentral importiert und du kannst mit der Umstellung auf Shopware6 fortfahren.