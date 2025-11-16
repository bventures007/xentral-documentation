## Überblick

Mit der hier beschriebenen Funktion kannst du Verkaufspreise, die in einer CSV-Datei vorliegen, in deinen XentralArtikelstamm hinzufügen.

> **Warnung**
>
> Stelle sicher, dass die Artikel, zu denen du Verkaufspreise hochladen möchtest, bereits in Xentral angelegt sind. Falls du zunächst Artikel importieren möchtest, folgediesem Link, um zur Anleitung zu gelangen.

Du findest den CSV-Importer im Menü **Einstellungen > Administration > Datenaustausch > CSV-Importer**.

![CSV-Importer_Menupfad.png](https://help.xentral.com/hc/article_attachments/19857409184284)

Der Import von Verkaufspreisen über den CSV-Importer läuft nach folgendem Prozess ab:

![Preisimport_Workflow.png](https://help.xentral.com/hc/article_attachments/19857417862812)

## Voraussetzungen

### Pflichtfelder

Stelle sicher, dass deine CSV-Datei mindestens folgende **Pflichtfelder** enthält:

> **Anmerkung**
>
> Die Spaltenbenennungen können frei gewählt werden. Sie müssen nicht zwingend den hier aufgeführten Namen entsprechen, da sie im Rahmen das sog. Mappings den entsprechenden Xentral-Datenfeldern zugeordnet werden.

- Artikelnummer
- Preis Netto
- Währung
- Menge

> **Anmerkung**
>
> Beachte, dass die hier aufgeführten Felder eine Minimal-Konfiguration darstellen. Es ist möglich, dass zusätzliche Felder erforderlich werden, sobald du weitere Spalten einfügst, die eine Abhängigkeit zur Folge haben.
>
> Beispiel: Wenn du Verkaufsaufträge mit Versandkosten importieren möchtest, benötigst du nicht nur "Versandkosten (netto)", sondern auch das Feld "Versandkosten Artikelnummer".

### Formatierungsregeln

Halte dich an folgende **Formatierungsregeln**, um ein reibungsloses Mapping zu gewährleisten:

- Preise/Kosten: Nutze einen Punkt als Trennzeichen. Beispiel: Der Betrag "Zwei Euro und 59 Cent" wird in der CSV-Datei als "2.59" eingetragen.
- Datum: Nutze die Struktur JJJJ-MM-TT. Formatiere z. B. das Gültig ab Datum als 2025-05-01, wenn die Gültigkeit ab dem ersten Mai 2025 starten soll.

> **Anmerkung**
>
> Als Trennzeichnen, die du zwischen den einzelnen Datenfeldern in der CSV-Datei nutzt, kannst du z. B. Semikolon oder Komma verwenden. Sie werden beim Hochladen der Importdatei automatisch erkannt.
>
> Die Spaltenbenennungen können frei gewählt werden. Sie müssen nicht zwingend den oben aufgeführten Namen entsprechen, da sie im Rahmen das sog. Mappings den entsprechenden Xentral-Datenfeldern zugeordnet werden.

### Arbeiten mit IDs

Manchmal ist es notwendig oder sinnvoll, beim Import eine ID zu nutzen, wobei diese eine echte Referenz zur Datenbank darstellt und keine Nummer oder Bezeichnung ist. In diesem Abschnitt erklären wir dir, wie du eine ID ermitteln und beim Import verwenden kannst.

> **Anmerkung**
>
> Beachte, dass hier eine eindeutige Datenbank-ID gemeint ist, die nicht mit einer Nummer oder Bezeichnung verwechselt werden darf.

Um die ID eines Datensatzes zu ermitteln, benötigst du nur zwei Schritte:

1. Öffne den Datensatz, dessen ID du herausfinden möchtest.
1. Lies die ID in der URL ab.

#### Beispiel Projekt-ID

1. Öffne das Modul Projekte, um die jeweilige Projekt-ID zu ermitteln. Das geht am Schnellsten über die Smart Search:
1. In der Projektübersicht klickst du auf das Projekt, dessen Projekt-ID du herausfinden möchtest, um es zu öffnen. Lies anschließend die Projekt-ID in der URL ab:

#### Beispiel Kunden-/ Lieferanten-ID

1. Öffne das Modul Adressen.
1. Öffne eine Adresse zum Bearbeiten und lies die Kunden- bzw. Lieferanten-ID aus der URL ab:

#### Beispiel Artikel-ID

1. Öffne das Modul Artikel.
1. Öffne einen Artikel zum Bearbeiten und lies die Artikel-ID aus der URL ab:

#### Beispiel Artikelkategorie-ID

1. Öffne das Modul Artikelkategorien. Das geht am Schnellsten über die Smart Search.
1. Öffne eine Kategorie zum Bearbeiten und lies die ID aus der URL ab:

## CSV-Import erstellen

Klicke auf+ CSV-Import erstellen, um einen neuen Import anzulegen:

![CSV-Importer_NeuenImportErstellen__1_.png](https://help.xentral.com/hc/article_attachments/19857417864220)

> **Tipp**
>
> Sobald du Importe angelegt hast, kannst du sie an dieser Stelle wiederfinden, bearbeiten und erneut ausführen.

Lege die allgemeinen Daten deines Imports an, um ihn später wiederfinden zu können und lade die CSV-Datei hoch:

![Verkaufspreisimport_DateiHochladen.png](https://help.xentral.com/hc/article_attachments/19857417865372)

1. Trage einen **Namen** und
1. eine **Beschreibung** ein, die dir bei der Identifikation des Imports helfen.
1. Wähle den Datentyp, den du importieren möchtest.
1. Füge deine vorbereitete **CSV-Datei** ein.
1. Unter den **Erweiterten Einstellungen** kannst du bei Bedarf Anpassungen an den Trennzeichen und Sonderzeichen vornehmen, falls die Spalten der Importdatei auf der rechten Seite nicht korrekt angezeigt werden.
1. Wähle die Spalten aus, mit denen das System einen Datensatz eindeutig identifizieren kann (Datenbank-ID).

## Mapping durchführen

Sobald du auf **Mit dem Mapping starten** geklickt hast, werden die Daten in eine Vorschau geladen.

### Allgemeine Funktionen der Vorschau

In der Vorschauliste stehen dir folgende allgemeine Schaltflächen zur Verfügung:

![Verkaufspreisimport_Mapping_Vorschau_Schaltflachen.png](https://help.xentral.com/hc/article_attachments/19857417865756)

- **(1) Suchfeld**: Ermöglicht die Suche nach einer Artikelnummer
- **(2) Filter**: Hier kannst du die Vorschauliste nach einem oder mehreren Filterkriterien einschränken.
- **(3) Anleitung öffnen**: Hier bekommst du einen kurzen Überblick über die Importschritte.
- **(4) Schnellfilter**: Filtert die Daten nach Spalten, die nicht zugeordnet sind oder nach Zeilen, die invalide Daten enthalten.
- **(5) Neu laden**: Hiermit kannst du die Vorschau neu laden.
- **(6) Abschließen**: Führt eine Validierung durch und ermöglicht den anschließenden Datenimport.

### Spalten zuordnen (Mappen)

In der linken Spalte der Vorschau ist der Eindeutige Bezeichner aufgeführt, in unserem Beispieleine Kombination aus mehreren Kriterien, um sicherzustellen, dass alle Preiszeilen aufgeführt werden. Daneben werden alle Spalten geladen, die im XentralDatenstamm für den zu importierenden Datentyp zur Verfügung stehen. Rot hinterlegte Felder stellen Pflichtfelder dar und müssen im nächsten Schritt zugeordnet werden. Alle weißen Spalten sind optional. Für diese nimmst du eine Zuordnung vor, nur soweit du es möchtest.

Um eine Spaltenzuordnung zu konfigurieren, klicke auf die Schaltfläche neben dem Spaltentitel:

![Verkaufspreisimport_Mapping_Vorschau_Spaltenzuordnung.png](https://help.xentral.com/hc/article_attachments/19857409187612)

Im Feld **Ursprünglicher Feldname** werden dir die Spaltentitel aus der CSV-Datei angezeigt.

![Import_Spaltenkonfiguration_UrsprunglicherFeldname.png](https://help.xentral.com/hc/article_attachments/19857409190172)

Wähle den Feldnamen aus, der der ausgewähltenXentral-Spalte entspricht und klicke auf **Anwenden**. Die bereits erfolgte Zuordnung wird dir in der Vorschau angezeigt:

![Verkaufspreisimport_Mapping_ZuordnungErfolgt.png](https://help.xentral.com/hc/article_attachments/19857409192476)

Wiederhole das Vorgehen für allePflichtspalten und bei Bedarf weitere optionale Spalten.

> **Anmerkung**
>
> Die gelbe Kennzeichnung oben rechts zeigt dir an, dass noch Pflichtfelder zuzuordnen sind. Sobald alle verpflichtenden Spalten zugewiesen sind, verschwindet der Hinweis.

### Zuordnung von benutzerdefiniertem Text

Falls du einer Spalte Daten zuweisen möchtest, für die in der ursprünglichen CSV-Datei keine passende Spalte vorhanden ist, kannst du beim Mapping die Auswahl **Benutzerdefinierter Text** nutzen.

Klicke auf die Schaltfläche neben dem Spaltentitel, um die Zuordnung zu öffnen. Wähle im Feld **Ursprünglicher Feldname ** die Option**Benutzerdefinierter Text** aus und trage den zutreffenden Wert in das Feld daneben ein.

![Import_SpaltenzuordnungBenutzerdefinierterText.png](https://help.xentral.com/hc/article_attachments/19857417872028)

### Ändern der Spaltenzuordnung

Wenn du eine Zuordnung nochmal anpassen möchtest, klicke erneut auf die Schaltfläche neben dem Spaltentitel und anschließend auf **Startwert**:

![Import_SpaltenzuordnungAndern.png](https://help.xentral.com/hc/article_attachments/19857409194012)

Nachdem du eine andere Spalte ausgewählt hast, bestätige per Klick auf **Übernehmen**:

![Artikelimport_SpaltenzuordnungUbernehmen.png](https://help.xentral.com/hc/article_attachments/19857409194908)

## Daten transformieren

Mit Hilfe der so genannten Transformer-Funktionen kannst du Daten aus der CSV-Datei vor dem Importieren anpassen oder bereinigen.

Du kannst die Daten auf Basis einer selbst definierten Regel anpassen. Die Regel trägst du einmal je Spalte ein. Sie wirkt sich dann auf alle Datenzeilen aus, für die die Regel zutrifft.

Um eine Regel einzutragen, klicke erneut auf die Schaltfläche neben dem Spaltentitel und anschließend auf **Schritt hinzufügen**:

![Import_SpaltenzuordnungSchritthinzu.png](https://help.xentral.com/hc/article_attachments/19857417875228)

Wähle einen Konfigurationstypen aus, mit dem du die Daten anpassen möchtest und klicke auf **Übernehmen**:

![Import_SpaltenzuordnungKonfigurationstypwahlen.png](https://help.xentral.com/hc/article_attachments/19857417875996)

Folgende Konfigurationstypen stehen zur Verfügung:

- **HTML entfernen**: Hiermit entfernst HTML-Tags aus einem String.
- **Weißraum entfernen**: Diese Aktion entfernt Leerzeichen, die vor oder nach dem Inhalt stehen (jedoch keine Leerzeichen innerhalb der Zeichenkette).
- **Text ersetzen**: Hiermit kannst du eine beliebige Zeichenkette durch eine andere ersetzen. So kannst du z. B. auch Leerzeichen innerhalb einer Zeichenkette entfernen.
- **Feld anhängen**: Dies kannst du nutzen, um z. B. eine bestimmte Zeichenfolge an die im Feld vorhandenen Daten anzuhängen.
- **Wert festlegen**: So kannst du einen festen Wert in die Spalte eintragen.
- **Bedingung**: Auf diese Weise kannst du Daten vom System nach einer vorgegebenen Bedingung eintragen lassen.

Je nach Konfigurationstyp kannst du weitere Angaben machen.

> **Tipp**
>
> Die Funktion **Text ersetzen** kannst du z. B. nutzen, wenn du eine Währung durch eine andere ersetzen möchtest.

![Import_SpaltenzuordnungKonfigurationstypText.png](https://help.xentral.com/hc/article_attachments/19857417877276)

Bei Bedarf kannst du weitere Konfigurationstypen ergänzen, indem du erneut auf **Schritt hinzufügen** klickst und das Vorgehen mit einem anderen Konfigurationstypen wiederholst. So kannst du mehrere Änderungen / Ersetzungen kombinieren:

![Import_SpaltenzuordnungWeitererSchritt.png](https://help.xentral.com/hc/article_attachments/19857409198236)

Sobald du alle gewünschten Konfigurationstypen definiert hast, bestätige per Klick auf **Anwenden**:

![Import_SpaltenzuordnungTransformationAnwenden.png](https://help.xentral.com/hc/article_attachments/19857409199132)

Die Vorschau zeigt dir die angepassten Daten, wie sie in Xentralübernommen werden.

### Ändern der Transformations-Regeln

Falls du eine Transformation nochmal anpassen oder wieder entfernen möchtest, klicke erneut auf die Schaltfläche neben dem Spaltentitel, um zum Transformations-Workflow zu gelangen. Dort kannst du

- (1) Schritte wieder entfernen,
- (2) erneut zum Bearbeiten öffnen oder
- (3) neue Schritte hinzufügen.

Bestätige Änderungen per Klick auf **Anwenden**.

![Import_SpaltenkonfigurationAnpassen.png](https://help.xentral.com/hc/article_attachments/19857409199644)

## Daten überschreiben

Ergänzend zur regelbasierten Transformation kannst du einzelne Datensätze manuell füllen. Doppelklicke dazu einfach in ein anzupassendes Datenfeld, tippe den Zielwert ein und bestätige mit der Enter-Taste oder dem grünen Haken:

![Verkaufspreisimport_ManuelleTransformationBestatigen.png](https://help.xentral.com/hc/article_attachments/19857409200156)

Eine solche Änderung kannst du ganz einfach per Klick auf den Zurück-Pfeil zurücksetzen:

![Verkaufspreisimport_ManuelleTransformationZurucksetzen.png](https://help.xentral.com/hc/article_attachments/19857417881500)

## Daten importieren

Sobald alle Daten in der Vorschau so vorliegen, wie du es benötigst und keine invaliden Daten mehr angezeigt werden, kannst du mit dem Import starten. Klicke dazu zunächst auf **Abschließen**:

![Verkaufspreisimport_ImportStarten.png](https://help.xentral.com/hc/article_attachments/19857409201692)

Das System führt eine Datenvalidierung durch. Wenn keine invaliden Daten gefunden wurden, erhältst du eine grüne Erfolgsmeldung und kannst den **Import starten**:

![Import_DatenvalidierungGrun.png](https://help.xentral.com/hc/article_attachments/19857409202460)

> **Wichtig**
>
> Sollten einzelne Datenfelder noch nicht ausreichend zugeordnet worden sein, bekommst du eine rote Meldung. Brich in diesem Fall ab und korrigiere die genannten Datensätze.

Nachdem du auf **Import starten** geklickt hast, startet der Import im Hintergrund und du gelangst automatisch auf die Statusseite. Dort kannst du die Ansicht über die Filter oben einschränken und den Status über die Schaltfläche rechts aktualisieren:

![Artikelimport_ImportstatusNeuladen.png](https://help.xentral.com/hc/article_attachments/19857409208220)

Nach erfolgreichem Abschluss des Imports ist der Status für alle Datensätze grün:

![Artikelimport_ImportstatusVollstandig.png](https://help.xentral.com/hc/article_attachments/19857417889820)

> **Anmerkung**
>
> Nach dem Start des Imports kannst Du diese Seite jederzeit schließen. Der Import läuft im Hintergrund weiter, solange noch Datensätze übrig sind. Du kannst jederzeit über dieCSV-Importer Übersichtzum Reporting zurückkehren und den Status verfolgen.