## Überblick

In diesem Artikel erfährst du, wie du Matrixprodukte und Varianten fehlerfrei von Xentral zu Shopify über die Connect-Schnittstelle überträgst. Dazu zeigen wir dir Schritt für Schritt:

- wie du Matrixprodukte und Varianten in Xentral anlegst,
- wie du die Synchronisation in der richtigen Reihenfolge durchführst und
- und was du tun kannst, wenn du Produkte oder Varianten später aus deinem Shopify-Angebot entfernen möchtest.

> **Anmerkung**
>
> Dieser Artikel setzt grundlegende Kenntnisse über die Xentral Connect Funktionen und eine vollständig eingerichtete Shopify-Schnittstelle voraus. Wenn du die Einrichtung noch nicht abgeschlossen hast, findest du dazu alle Informationen unterShopify Connector.

## Matrixprodukt und seine Varianten anlegen

Bevor du Artikel mit Shopify synchronisierst, müssen das Matrixprodukt und alle Varianten vollständig in Xentral angelegt sein. Wenn du hierzu nochmal mehr in die Tiefe gehen möchtest, besuche folgende Artikel:

- [Artikel manuell anlegen](https://help.xentral.com/hc/de/articles/5355868375324-Artikel-manuell-anlegen)
- [Matrixprodukt - Artikelvarianten erstellen](https://help.xentral.com/hc/de/articles/360016725120-Matrixprodukt-Artikelvarianten-erstellen)

> **Tipp**
>
> Wir empfehlen bei Matrixprodukten und Varianten zuerst die Grundtabelle, sozusagen das Matrixgerüst, anzulegen.

### Grundtabelle (Matrixgerüst) definieren

1. Um die Grundtabelle zu definieren, suche in der Smart Search nach Matrixprodukt.
1. Klicke auf + Neu Anlegen, um eine neue Variantengruppe anzulegen.
1. Vergib eine Bezeichnung für die Gruppe, z. B. Farbe und speichere.
1. Öffne die Variantengruppe mit Klick auf Optionen bearbeiten.
1. Klicke auf + Neuer Eintrag, um eine neue Option anzulegen.
1. Vergib einen Namen, z. B. grün. Optional kannst du bestimmen, dass Artikelnummern einen passenden Anhang erhalten, z. B. -gr. Wiederhole das Vorgehen für weitere Einträge.
1. Nun hast du das Matrixgerüst definiert und kannst mit der Artikelanlage fortfahren.

### Matrixprodukt anlegen

> **Anmerkung**
>
> Bevor du ein neues Matrixprodukt anlegst, stelle sicher, dass du ein passendes Matrixgerüst definiert hast.

1. Navigiere zum Artikelstamm (Verkaufen > Artikel) und klicke auf + Neu Anlegen, um einen neuen Artikel zu generieren.
1. Trage die Kopfdaten gemäß deinen Bedürfnissen ein.
1. Scrolle weiter nach unten, gibt einen Hersteller (für Shopify erforderlich) ein und hake Matrixprodukt an. Bestätige die Artikelanlage mit Speichern.
1. Öffne den Reiter Verkaufspreis und klicke auf +Neuer Verkaufspreis, um einen Verkaufspreis anzulegen.
1. Trage einen Standardpreis ein und speichere.

### Varianten anlegen

1. Öffne in deinem soeben angelegten Matrixprodukt den Reiter Matrixprodukt.
1. Klicke auf Neue Gruppe.
1. Wähle die zuvor angelegte Grundtabelle aus und hake die Optionen an, die für dieses Matrixprodukt zutreffen.
1. Um die Varianten zu erzeugen, aktiviere alle Artikel auswählen und klicke auf Fehlende Artikel erzeugen.
1. Stelle die für deine Bedürfnisse passenden Optionen ein und klicke auf Speichern. Im Beispiel nutzen wir den Artikelnummern-Anhang.
1. Nun sind alle Varianten anlegt:

#### Shopzuordnung und weitere Einstellungen vornehmen

1. Navigiere zum Reiter Details > Onlineshop Optionen.
1. Klicke auf Neuer Eintrag.
1. Wähle die Schnittstelle für die du eine Synchronisation einrichten möchtest und speichere.
1. Kehre zurück zum Reiter Matrixprodukt, um die Filterung für alle Varianten zu übernehmen.
1. Wähle alle Artikel aus und öffne die Massenbearbeitung.
1. Aktiviere Lagerartikel und Shopverknüpfungen und klicke auf Weiter.
1. Setze die Haken in allen Zeilen (am besten, indem du die Schnellfunktion in der Stapelverarbeitung ausführst), sowohl bei Lagerartikel als auch bei der Shop-Schnittstelle, die du in Punkt 3 für das Matrixprodukt gewählt hast und bestätige mit 2x Weiter.

Mit diesen Schritten hast du die Mindestanforderungen für die fehlerfreie Synchronisation von Matrixprodukten und Varianten an Shopify geschaffen. Natürlich kannst du weitere Artikeleinstellungen nach deinen Bedürfnissen ergänzen, z. B. Artikeltexte, Bilder oder den Artikelbaum.

## Erst-Übertragung zu Shopify schrittweise vornehmen

Bei der Erst-Übertragung der Artikel ist es wichtig, schrittweise und in der richtigen Reihenfolge vorzugehen, um eine korrekte Registrierung der Artikelstruktur in Shopify zu gewährleisten. Folge den nächsten Abschnitten Schritt für Schritt für ein reibungsloses Ergebnis.

> **Warnung**
>
> Beachte unbedingt, dass du bei der Erst-Übertragung schrittweise wie im Folgenden beschrieben vorgehst.

### Matrixprodukt und erste Variante in Artikelzuordnung aufnehmen

Mit der Artikelzuordnung legst du fest, welche Artikel zwischen Xentral und Shopify synchronisiert werden sollen.

1. Navigiere zu Einstellungen > Verkaufen > Shops/Marktplätze > Shopify.
1. Öffne die Artikelzuordnung derjenigen Shopify-Anbindung, für die du die Synchronisation einrichtest.
1. Wähle Filter für ausgewählte Artikel anwenden.
1. Trage die Artikelnummer des Matrixproduktes und einer Variante ein und klicke auf Weiter.
1. Bestätige mit Artikelliste aufbauen.

### Synchronisation für Matrixprodukt und erste Variante anstoßen

> **Anmerkung**
>
> Bevor du mit der Synchronisation startest, stelle sicher, dass
>
> - das Matrixprodukt und alle Varianten in Xentral wie oben konfiguriert sind,
> - das Matrixprodukt undeineVariante in der Artikelzuordnung aufgenommen sind und dass
> - derIntegrationsmodusfür Artikelaktivist (Einstellungen > Verkaufen > Shops/Marktplätze > Shopify > Workflows > Artikel)

Damit die Artikel in Shopify korrekt angelegt und miteinander verknüpft werden, ist es wichtig, zuerst das Matrixprodukt und anschließend die Variante zu übertragen.

1. Öffne das Journal derjenigen Shopify-Anbindung, für die du die Synchronisation einrichtest.
1. Suche im Reiter Artikel nach deinem Matrixprodukt.
1. Klicke in der Zeile des Matrixprodukts auf Artikel synchronisieren und warte bis die Artikel-Synchronisierung gestartet ist.
1. Klicke nun in der Zeile der Variante auf Artikel synchronisieren und warte bis die Artikel-Synchronisierung gestartet ist.

> **Tipp**
>
> Wenn du hier schrittweise und behutsam vorgehst, sorgst du dafür, dass das Matrixprodukt und die erste Variante geordnet an den Shop übergeben werden. Sobald beide Zeilen einen grünen Status anzeigen, kannst du mit den weiteren Varianten fortfahren.

### Artikelzuordnung auf alle Varianten erweitern

1. Öffne die Artikelzuordnung.
1. Erweitere deine Artikelliste. Dies tust du, indem du entweder erneut Filter für ausgewählte Artikel anwenden wählst und nun die Artikelnummern der weiteren Varianten einträgst oder indem du Filter für alle Artikel anwenden nutzt.

### Synchronisation für weitere Varianten anstoßen

1. Kehre zurück zum Journal und suche nach dem Artikel.
1. Hake die restlichen Varianten an und klicke auf die Sammelaktion Artikel synchronisieren.

## Produkt aus Angebot entfernen

Wenn du ein Produkt nicht mehr über den Shop/Marktplatz verkaufen möchtest, hast du grundsätzlich folgende Möglichkeiten:

- Artikel inaktiv setzen
- Lagerbestand auf Null setzen
- Artikel löschen

### Artikel inaktiv setzen

> **Anmerkung**
>
> Diese Methode eignet sich dann, wenn du die gesamte Gruppe, bestehend aus Matrixprodukt und allen Varianten, aus dem Angebot nehmen möchtest.

> **Tipp**
>
> Mit dieser Methode wird der Artikel im Shop/Marktplatz für Kunden nicht mehr angezeigt.

Um einen Artikel inaktiv zu setzen, gehe wie folgt vor:

1. Navigiere zu Verkaufen > Artikel und öffne ihn zum Bearbeiten.
1. Gehe zum Reiter Details > Online-Shop Optionen.
1. Setze den Haken bei Artikel inaktiv.
1. Klicke auf Speichern.

> **Anmerkung**
>
> Je nachdem, ob der Produktivmodus der Schnittstelle aktiviert ist oder nicht, wird die Änderung automatisch synchronisiert oder muss manuell übertragen werden:
>
> - Produktivmodus aktiv: Änderung wird automatisch an den Shop/Marktplatz übertragen.
> - Produktivmodus nicht aktiv: Stoße die Übertragung manuell über das Journal an: Systemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Journal > ReiterArtikel. Klicke in der Zeile des betreffenden Artikels aufArtikel synchronisieren.
>
> Um zu prüfen, ob der Produktivmodus aktiv ist, navigiere zuSystemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Zahnrad (Einstellungen).

### Lagerbestand auf Null setzen

> **Anmerkung**
>
> Diese Methode eignet sich insbesondere, wenn du einzelne Varianten nicht mehr anbieten möchtest.

> **Tipp**
>
> Diese Methode führt dazu, dass der Artikel im Shop/Marktplatz zwar angezeigt wird, aber nicht mehr bestellbar ist.

Folge diesen Schritten, um den Lagerbestand im Shop/Marktplatz auf Null zu setzen:

1. Navigiere zu Verkaufen > Artikel und öffne ihn zum Bearbeiten.
1. Gehe zum Reiter Details > Online-Shop Optionen.
1. Hake Restmenge (Abverkauf) an.
1. Trage in Pseudo Lagerzahl eine Null (0) ein.
1. Klicke auf Speichern.
1. Navigiere zu Systemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Workflows > Reiter Bestand.
1. Stelle sicher, dass Pseudo Lagerzahl statt echten Lagerzahlen verwenden im Abschnitt Lagerbestand berechnen aktiviert ist.
1. Navigiere zu Systemeinstellungen > Verkaufen > Shops/Marktplätze > [Shop-/Marktplatzname] > Journal > Reiter Artikel.
1. Klicke in der Zeile des betreffenden Artikels auf Bestand synchronisieren.

> **Anmerkung**
>
> Alternativ zur Nutzung der Pseudo Lagerzahl kannst du den echten Bestand natürlich komplett auslagern oder an ein Lager umbuchen, das nicht mit dem Shop/Marktplatz verknüpft ist. Stelle in diesen Fällen sicher, dassRestmenge (Abverkauf)in denOnline-Shop Optionendes Artikels angehakt ist.

### Artikel löschen

### Achtung

Das Löschen eines Artikels ist nur möglich, wenn er in keinen Belegen enthalten ist.

Wir empfehlen grundsätzlich, Artikel nicht zu löschen, da dadurch wichtige Informationen wie Artikel-Historie und Verknüpfungen verloren gehen. Diese Methode eignet sich daher nur, wenn du einen Artikel aus Versehen oder testweise angelegt hast und diesen wieder entfernen möchtest.

1. Um einen Artikel zu löschen, navigiere zu Verkaufen > Artikel.
1. Klicke in der Artikel-Übersicht auf X in der Zeile des zu löschenden Artikels.
1. Bestätige den Löschvorgang mit OK.

> **Warnung**
>
> **Bei Nutzung von Fremdnummern:**
>
> Falls du mit Fremdnummern arbeitest, beachte, dass Einträge aus der Fremdnummern-Tabelle entfernt werden, wenn ein Artikel in Xentral gelöscht wird. Deshalb werden Artikel im Shop/Marktplatz bei aktiver Fremdnummern-Verknüpfung nicht automatisch gelöscht, wenn sie in Xentral gelöscht werden. In diesem Fall musst du die Löschung im Shop manuell vornehmen.
>
> Weitere Informationen zu Fremdnummern findest du in diesem Artikel:Fremdnummern in Xentral

> **Warnung**
>
> Beachte bei dieser Methode unbedingt, dass du in Xentral sowohl Matrixprodukt als auch alle Varianten löschen musst, um die gesamte Gruppe aus Matrixprodukt und Varianten aus dem Shopangebot zu entfernen. Löschst du nur das Matrixprodukt, vergisst aber die Varianten, führt dies zu fehlerhaften Artikelübertragungen, da die verbleibenden Varianten shopseitig als neue Artikel interpretiert werden!
>
> Es ist jedoch problemlos möglich, einzelne Varianten zu löschen, solange das Matrixprodukt bestehen bleibt.