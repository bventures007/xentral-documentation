> **Wichtig**
>
> Die in diesem Artikel beschriebene Funktionalität zur Inventur wurde durch die **Mobile Inventory App** ersetzt. Du kannst die neue App kostenlos auf dein MDE-Gerät oder Smartphone herunterladen und für die mobile Inventur in deinem Lager nutzen. Außerdem stehen dir für die Arbeit mit der Mobile Inventory App verschiedene Inventurberichte zur Verfügung, sodass du die Ergebnisse jederzeit transparent dokumentieren und auswerten kannst.
>
> Alle Informationen zur Mobile Inventory App findest du im ArtikelÜberblick: Inventur mit der Mobile Inventory App.
>
> Für die im Folgenden beschriebene Funktionalität veröffentlichen wir keine Fehlerbehebungen, Verbesserungen oder neue Features mehr. Möchtest du mehr zum Legacy-Status wissen? Dann schau dir den ArtikelWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?.

In diesem Artikel wird erklärt, wie die Abbildung und Durchführung der Inventur in Xentralmöglich ist und welche SpezialfunktionenXentral hierfür bietet.

## Übersicht

Eine Übersicht über alle dokumentierten Lager kannst du im Menü **Lager > Lagerverwaltung > Tab: Inventur ** einsehen. Mit einem Klick auf den**Pfeil **

-Button in der Menü-Spalte erscheint nachfolgend im Untertab ** Inventur**eine Übersicht über alle Artikel, die sich im ausgewählten Lager auf der ersten Lagerebene befinden. Dabei werden nur Stückzahlen größer als 0 dargestellt.

In dieser Inventurliste kannst du nun die tatsächlich vorhandenen Stückzahlen in das entsprechende Feld in der Spalte **Inventur** eingeben. Die eingegebenen Werte werden automatisch gespeichert, führen jedoch noch nicht zu einer Bestandsänderung. Es werden lediglich die Zwischenergebnisse in dieser Liste abgespeichert. Zwischenzeitliche Bestandsänderungen aufgrund von Anlieferung oder Versand werden hierbei in der Zwischenspeicherung nicht berücksichtigt. Daher ist es notwendig, den Betrieb für dieses Lager bis zum Abschluss der Inventur kurzzeitig auszusetzen. Änderungen können bei laufendem Betrieb eingetragen und wieder gespeichert werden.

> **Anmerkung**
>
> Eine Inventur kann nicht rückwirkend durchgeführt werden, sondern nur zum aktuellen Tagesdatum!

## Spezialfunktionen

Im Tab **Inventur ** kannst du im Untertab**Spezialfunktionen** verschiedene Spezialfunktionen nutzen.

Mit einem Klick auf den zuerst erscheinenden Button **Inventur für Lager jetzt aus Lagerbestand laden ** und anschließend einem Klick auf**Ok** im erscheinenden Feld werden weitere Spezialfunktionen sichtbar. Die folgenden Spezialfunktionen sind verfügbar:

- Inventur aus Lagerbestand laden
- Inventur komplett zurücksetzen

### Inventur aus Lagerbestand laden

Diese Spezialfunktion errechnet sich den aktuellen Soll-Lagerbestand für dieses Lager und kann verwendet werden, wenn nur wenige Änderungen zu erwarten sind bzw. vorgenommen werden müssen.

Diese Spezialfunktion bietet folgende Vorteile:

- kurze Inventurabstände
- sehr sauber gepflegte Lagerbestände

Klicke im Untertab **Spezialfunktionen ** auf den Button **Inventur jetzt aus Lagerbestand laden ** und im dann erscheinenden Feld auf**Ok**.

Dadurch fülltXentral automatisch die Inventur-Spalte im Untertab **Inventur** mit dem aktuellen Lagerbestand.

![WarehouseInventoryLoadInventoryFromStock.png](https://help.xentral.com/hc/article_attachments/13105146981276)

### Inventur komplett zurücksetzen

Diese Spezialfunktion setzt alle gespeicherten Werte wieder zurück. Somit werden alle eingegebenen Werte gelöscht. Dies kann in folgenden Fällen nützlich sein:

- Die Inventur soll komplett neu begonnen werden
- Der Zeitraum zwischen Beginn der Inventur und geplantem Abschluss ist zu groß geworden. Deshalb haben sich zu viele nachzutragende Bestandsänderungen ergeben

Um diese Funktion zu nutzen, klicke im Untertab **Spezialfunktionen ** auf **Inventur (komplett) zurücksetzen ** und anschließend auf**Ok** im dann erscheinenden Feld.

Danach wird die gesamte Inventurspalte im Untertab **Inventur** bereinigt.

## Inventur durchführen (Schritt für Schritt)

Im Folgenden erklären wir Schritt für Schritt, wie die Inventur in Xentral abläuft.

### Bestandsänderungen eingeben und speichern

Gib zunächst die Bestandsänderungen ein, die sich im Lager ergeben haben, einzugeben. Speichere anschließend deine Eingaben.

Gehe dazu wie folgt vor:

- Zähle die tatsächlichen Lagerbestände pro Regal und trage sie in die Spalte **Inventur ** im Untertab**Inventur** ein.
- Die farblichen Markierungen der einzelnen Artikel haben dabei unterschiedliche Bedeutungen:
  - **rot**: Dieser Artikel wurde noch nicht gezählt. Hier würde beim Abschluss der Inventur der aktuelle Bestand erhalten bleiben
  - **schwarz**: Der Artikel wurde gezählt. Der Ist-Bestand stimmt mit dem Soll-Bestand überein
  - **blau**: Der Artikel wurde gezählt, aber der Ist-Bestand weicht vom Soll-Bestand ab

![WarehouseInventoryColoredMarkings.png](https://help.xentral.com/hc/article_attachments/13105085503644)

### Inventur abschließen und Lagerbestände buchen (Bestandsänderung)

Nach der Eingabe der Bestandsänderung schließt du die Inventur ab und die aktuellen Lagerbestände zu buchen.

Dazu ist wie folgt vorzugehen:

1. Öffne das Untertab **Abschluss**.
1. Klicke auf **Hauptlager jetzt anpassen**.
1. Am oberen Rand wird eine Meldung angezeigt. Klicke auf **Ok**, um die Bestände mit dem Vermerk über Inventur und Datum anzupassen.

> **Warnung**
>
> Mit dem oben beschriebenen Schritt nimmst du Änderungen am Lagerbestand vor, die du später nicht mehr zurücksetzen kannst!

### Inventurdokument erstellen

Nachdem du die Inventur wie oben beschrieben abgeschlossen hast, kannst du Dokumente zur Inventur erstellen. Nach dem Abschluss der Inventur wechselt Xentral automatisch in die Dokumentenerzeugung. Alternativ kann auch wie folgt vorgegangen werden:

Die Inventurdokumente werden für jedes einzelne Lager bei der Inventur automatisch erzeugt. Diese Dokumente findest du im Menü **Lager > Lagerverwaltung > Inventur > Details > Inventur** aufgelistet.

Ein neu erzeugtes Dokument ist im Status **Bearbeitung** und noch nicht freigegeben. Das Dokument kann bei Bedarf gelöscht werden. Die vorgenommene Bestandsänderung der Artikelbestände wird damit allerdings nicht rückgängig gemacht.

- Falls du noch zusätzliche Informationen eingeben möchtest, kannst du diese einzutragen und das Dokument anschließend über den Button **Freigabe** freizugeben
- Die Aktion **Inventur abschließen** speichert das Dokument dauerhaft und friert es ein

### Beispiel-Inventureintrag

Hier wird ein Inventureintrag beispielhaft demonstriert.

Öffne zuerst das Menü **Stammdaten > Artikel > Stift-Icon bei jeweiligem Artikel > Lager**.

In der Tabelle **Lagerplatz Bewegungen ** kannst du die Buchungen, die durch die Inventur entstanden sind, einsehen. Dieser Eintrag wird automatisch beim Klick auf **Lagerbestände anpassen ** im Tab**Abschluss** erzeugt. Weitere Informationen dazu kannst du in den vorherigen Kapiteln nachlesen.

![WarehouseInventoryInventoryEntryExample.png](https://help.xentral.com/hc/article_attachments/13105101130908)

### Inventur ohne Preise

Wenn die Inventur ohne Preise im Beleg angezeigt werden soll, dann gibt es ab Version 19.3 eine zusätzliche Option dafür. Diese ist im Menü **Lager > Lagerverwaltung > Inventur ** zu finden. Aktiviere die Option**Preise ausblenden**.

Nachdem du die Option aktiviet und auf **Speichern ** geklickt hast, gestaltet sich das Inventurdokument, das im Untertab**Vorschau** eingesehen werden kann, folgendermaßen:

![WarehouseInventoryExampleDocument.png](https://help.xentral.com/hc/article_attachments/13105101161116)