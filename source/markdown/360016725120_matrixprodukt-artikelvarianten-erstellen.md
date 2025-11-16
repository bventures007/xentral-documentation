Das Modul **Matrixprodukt** in Xentral erlaubt dir, innerhalb kurzer Zeit zahlreiche Varianten eines Artikels zu erstellen. Diese Varianten unterscheiden sich in bestimmten Eigenschaften wie z.B. Farbe oder Größe.

Die Matrix ist die Kombination dieser Eigenschaften in einer Tabelle. Beim Verkauf eines T-Shirts in zwei Größen und drei Farben entstehen somit sechs mögliche Varianten. In folgendem Beispiel werden T-Shirts der Größe S nur in rot verkauft, die der Größe M in allen verfügbaren Farben.

| Größe | Farbe |
| --- | --- |
| rot | blau | grün |
| S | x | | |
| M | x | x | x |

Haben deine Artikel oft ähnliche Eigenschaften, solltest du eine[Grundtabelle anlegen](#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29_N1657635501298). Sind deine Artikel sehr unterschiedlich oder benötigst du nur einen Matrixartikel, kannst du auch direkt zum Abschnitt[Matrixartikel anlegen](#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29_N1657635521146)springen.

> **Anmerkung**
>
> Eigenschaften werden in Xentral in diesem Zusammenhang als **Gruppe ** bezeichnet. Die Ausprägung der Eigenschaft bzw. Gruppe wird**Option** genannt.

## Grundtabelle für Artikeleigenschaften erstellen

Eine Grundtabelle erlaubt dir, immer wieder verwendbare Artikeleigenschaften (Gruppen) für deine Matrixprodukte zu erstellen. So kannst du z.B. die Gruppe **Größe** nicht nur für ein T-Shirt, sondern auch für eine Hose verwenden. Eine Grundtabelle legst du wie folgt an:

1. Nutze die Smart Search, um das Modul **Matrixprodukt** zu öffnen.
1. Klicke auf + NEU.
1. Gib im Feld Name die gewünschte Gruppe (z.B Größe) ein. Achte darauf, dass bei Aktiv ein Haken gesetzt ist.
1. **Optional**: Du kannst diese Gruppe auch nur für ein bestimmtes Projekt aktivieren. Bleibt das Feld leer, gibt es keine Einschränkungen.
1. Klicke auf Speichern.

Nun musst du definieren, wie diese Gruppe ausgeprägt sein kann. InXentral wird diese Ausprägung **Option** genannt. Ein T-Shirt mit der Gruppe Größe kann z.B. die Optionen S, M und L haben.

Die Optionen legst du wie folgt an:

1. Klicke im Modul Matrixprodukt bei der gewünschten Gruppe (z.B. Größe) auf das Pfeil-Symbol.
1. Klicke auf + Neuer Eintrag.
1. Gib im Feld Name die gewünschte Option (z.B. L) ein. Achte darauf, dass bei Aktiv ein Haken gesetzt ist.
1. **Optional**: Du kannst unter Anhang an Artikelnummer eine Zeichenfolge festlegen, die zur Artikelnummer der Variante hinzugefügt werden kann. Weiterhin kannst du über die Einstellung Sortierung festlegen, in welcher Reihenfolge die Optionen in der Tabelle erscheinen.
1. Klicke auf Speichern.

Du hast nun eine Grundtabelle erstellt und kannst diese auf einen Artikel anwenden.

## Matrixartikel anlegen

Gehe wie folgt vor, um einen Matrixartikel anzulegen:

1. Lege einen neuen Artikel an oder öffne einen bestehenden Artikel.
1. Öffne das Tab Details.
1. Aktiviere im Bereich **Varianten** die Option Matrixprodukt.
1. Klicke auf Speichern.

In der Artikelansicht erscheint das neue TabMatrixprodukt.

Dieser Artikel ist der Eltern-Artikel. Die durch das Matrixprodukt erschaffenen Kinder-Varianten erben ihre Daten und Einstellungen wieArtikelbezeichnungundHerstellervon diesem Artikel. Auch dieArtikelnummerkann automatisch basierend auf diesem Eltern-Artikel vergeben werden.

> **Tipp**
>
> Du kannst dir viel Arbeit ersparen, wenn du den Eltern-Artikel ausführlich bearbeitest. Durch die Vererbung der Daten brauchst du in den Kinder-Artikeln nur noch wenige Anpassungen durchzuführen.

> **Wichtig**
>
> Wir empfehlen, dass der Eltern-Artikel ein Platzhalter oder ein Konzept ist, wie z.B. ein allgemeines T-Shirt ohne weitere Angaben. Aus diesem Artikel leiten sich dann die konkreten Artikel ab. Diese Art der Datenstruktur wird von vielen Online-Shops erwartet.

> **Warnung**
>
> Der Eltern-Artikel darf in den Artikelstammdaten **nicht** als Lagerartikel markiert werden, da es andernfalls zu Problemen beim Lagerabgleich der zugehörigen Varianten kommt.

## Varianten erzeugen

Aus dem Matrixartikel können zahlreiche Varianten erzeugt werden. Hierfür stehen dir zwei Möglichkeiten zur Verfügung: Die Standard- und die Listenansicht.

Die jeweiligen Besonderheiten sind in folgender Tabelle zusammengefasst:

| Standardansicht | Listenansicht |
| --- | --- |
| Schnell und komfortabel durch grafische Oberfläche | Höhere Übersicht bei vielen Artikelvarianten durch tabellarische Listenform |
| Wiederverwendung von Gruppen durch Anwendung der Grundtabelle | Keine Verwendung der Grundtabelle, Gruppen und Optionen müssen immer manuell angelegt werden |
| Bis zu vier Gruppen können verwendet werden | Beliebig viele Gruppen können verwendet werden |

> **Anmerkung**
>
> Shopify erlaubt pro Artikel maximal 100 Varianten. Behalte diese Einschränkung beim Erzeugen der Varianten im Hinterkopf, falls du Shopify nutzt.

## Varianten in der Standardansicht erzeugen

Gehe in der Standardansicht zur Erstellung der Matrix wie folgt vor:

1. Klicke in deinem Matrixartikel auf das Tab Matrixprodukt.
1. Klicke auf neue Gruppe.
1. Wähle die gewünschte Gruppe (z.B. Größe) in der Grundtabelle und die gewünschten Optionen. Es besteht die Möglichkeit weniger Optionen zu nutzen, als in der Grundtabelle verfügbar sind.
1. **Alternativ**: Lege eine neue Gruppe an und füge dieser manuell Optionen hinzu. Diese Gruppe ist nur in diesem Artikel verfügbar.
1. Klicke auf Speichern.
1. Du kannst weitere Gruppen (z.B. Farbe) auf dieselbe Weise hinzufügen.

Du erhältst eine Matrix, bei der du alle möglichen Kombinationen deiner Optionen sehen kannst.

![Matrix_Product_Create_Variants.png](https://help.xentral.com/hc/article_attachments/5355868786460)

Aus dieser Matrix kannst du nun die Varianten erstellen:

1. Wähle die Artikel aus, die du erstellen möchtest. Du kannst hierbei einzelne Felder, ganze Zeilen und Spalten oder alle Artikel auswählen.
1. Erzeuge die ausgewählten Varianten über die Schaltfläche Fehlende Artikel erzeugen.

Es erscheint ein neues Fenster, in dem du die[Artikelnummer](#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29_N1657636332857)und die[Artikelbezeichnung](#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29_N1657636353376)zuweisen kannst.

In der Standardansicht kannst du denExpertenmodus für die Optionenöffnen. In diesem Modus werden deine Optionen in Listenform dargestellt. Außerdem kannst du hier einen Anhang an die Artikelnummer definieren. Diesen kannst du nach Erstellung der Varianten an die Artikelnummer anhängen (siehe Abschnitt[Artikelnummer zuweisen](#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29_N1657636332857)).

> **Tipp**
>
> Du kannst die Matrix frei nach deinen Bedürfnissen anpassen. Du kannst neue Gruppen und Optionen hinzufügen, bestehende bearbeiten und die Sortierung anpassen. Diese Änderungen beziehen sich nur auf diesen Artikel.

## Varianten in der Listenansicht erzeugen

Als Alternative zur Standardansicht, kannst du die Matrixvarianten auch in der Listenansicht erzeugen.

Um Varianten in der Listenansicht zu erzeugen, gehe wie folgt vor:

1. Klicke in deinem Matrixartikel auf das Tab Matrixprodukt.
1. Klicke auf Zu Listenansicht wechseln.
1. Klicke auf Neue Gruppe und wähle eine Bezeichnung.
1. Erstelle auf diese Weise weitere Gruppen, bis du alle deine benötigten Gruppen erstellt hast.
1. Klicke auf Neue Option.
1. Wähle die zugehörige Gruppe aus der Auswahlliste und wähle eine Bezeichnung für deine Option.
1. Erstelle auf diese Weise weitere Optionen, bis du alle deine benötigten Optionen erstellt hast.
1. Wähle die Artikel aus, die du erstellen möchtest. Setze dazu auf der linken Seite der Tabelle einen Haken in der entsprechenden Artikelvariante. Du kannst auch alle Artikel gleichzeitig markieren.
1. Erzeuge die ausgewählten Varianten über die Schaltfläche Fehlende Artikel erzeugen.

Es erscheint ein neues Fenster, in dem du die[Artikelnummer](#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29_N1657636332857)und die[Artikelbezeichnung](#UUID-f80260c3-d35f-b5e9-4195-c84c1694ee29_N1657636353376)zuweisen kannst.

## Artikelnummer zuweisen

Das Zuweisen einer Artikelnummer ist nur bei der Erstellung des Artikels möglich. Dazu stehen dir mehrere Möglichkeiten zur Auswahl. Diese sind:

- Artikelnummern aus Nummernkreis von Hauptkategorie verwenden: Der Nummernkreis wird vom Eltern-Artikel übernommen und weitere Nummern werden in dieser Kategorie fortlaufend erzeugt (z.B 1000028, 1000029, usw.).
- Artikelnummer aus Optionen an Hauptnummer anfügen: Die Artikelnummer des Eltern-Artikels wird mit den gewählten Optionen kombiniert (z.B. 1000027-L-ROT). Sollte in einer Option ein Umlaut oder Sonderzeichen vorhanden sein, so wird dieser nicht angezeigt (aus grün wird GRN).
- Artikelnummern aus Hauptnummer und Anhang an Artikelnummern bilden: Die Artikelnummer des Eltern-Artikels wird mit dem in der Grundtabelle definierten Anhang kombiniert. Dieser kann aus einer beliebigen Zeichenfolge bestehen. Dabei werden keine Trennzeichen genutzt (z.B 1000027BEISPIEL1).
- Artikelnummern von Hauptartikel mit Suffix: Die Artikelnummer des Eltern-Artikels wird mit einem Trennzeichen und einer Nummer kombiniert. Diese sind frei wählbar. Auch die Anzahl der Stellen kann selbst gewählt werden (z.B 1000027-001).

## Artikelbezeichnung zuweisen

Die erzeugten Varianten werden automatisch in den Artikel-Stammdaten als Variante des Eltern-Artikels gekennzeichnet. Das Zuweisen einer zusätzlichen Artikelbezeichnung ist nur bei der Erstellung des Artikels möglich. Dafür stehen zwei Optionen zur Auswahl. Diese sind:

- Optionen an Artikelbezeichnung der Unterartikel hängen: Die Eigenschaften und Optionen werden in der Artikelbezeichnung der Variante genannt (z.B. T-Shirt Größe: L Farbe: Rot).
- Zusatzbezeichnung als Lieferantenbezeichnung im Einkaufspreis anlegen: Der an die Artikelbezeichnung angehängte Zusatz (z.B. Größe: L Farbe: rot) wird auch als Artikelbezeichnung beim Lieferanten angelegt, sofern der Matrixartikel bereits einen Einkaufspreis besitzt.

## Mehrere Matrixvarianten auf einmal bearbeiten

Die Massenbearbeitung der Varianten ist jederzeit im Eltern-Artikel im TabMatrixproduktmöglich. Gehe dazu wie folgt vor:

1. Wähle die zu bearbeitenden Kind-Artikel in der Matrix aus.
1. Klicke auf Massenbearbeitung öffnen.
1. Wähle die zu bearbeitenden Parameter aus z.B. Einkaufs- und Verkaufspreise.
1. Klicke auf Weiter.
1. Bearbeite die gewünschten Parameter.
1. Klicke auf **Weiter**.

> **Tipp**
>
> Wird der Haken über der Spalte gesetzt, reicht es, die erste Zeile auszufüllen und dann im BereichStapelverarbeitungWerte mit Markierung aus Zeile 1 für alle Artikel übernehmenzu wählen. Klicke aufausführen. Dieser Eintrag wird dann auf alle folgenden Artikel übertragen.

Du erhältst die NachrichtArtikel wurden gespeichert!. Du hast die ausgewählten Artikel somit alle erfolgreich bearbeitet.

> **Wichtig**
>
> Manche Felder können über die Massenbearbeitung bearbeitet, jedoch nicht geleert bzw. gelöscht werden. Wird ein Feld in der Massenbearbeitung leer gelassen, belässtXentral den bisherigen Eintrag im Feld. Manche Textfelder können durch ein “-” ersetzt werden, wenn sie nicht für Belege oder Ähnliches benötigt werden.

## Matrix mit mehr als zwei Gruppen anlegen

Gibt es zu einem Artikel mehr als zwei Gruppen, reicht eine einfache Tabelle nicht mehr aus. Die weitere Gruppe muss mit allen bisherigen Varianten kombiniert werden können. Dies wird möglich, indem die neue Gruppe der bestehenden Tabelle vorangestellt wird. Die bestehende Tabelle muss also für jede Option der neuen Gruppe ein Mal kopiert werden (siehe Screenshot).

![Matrix_Product_Multiple_Groups.png](https://help.xentral.com/hc/article_attachments/5355893162268)

Auf diese Weise können in der Standardansicht bis zu vier Gruppen zum Matrixartikel hinzugefügt werden. Um mehr als vier Gruppen hinzuzufügen, musst du in die Listenansicht wechseln. Hier kannst du beliebig viele Gruppen hinzufügen, kannst aber bei mehr als vier Gruppen nicht mehr in die Standardansicht wechseln.

Die Handhabung und Verwendungsweise der Matrix mit mehreren Gruppen ist identisch zur Matrix mit zwei Gruppen.

> **Wichtig**
>
> Falls sehr viele Variantenartikel erzeugt werden, kann das Anlegen der Artikel einige Zeit dauern. In dieser Zeit darf das Tab nicht geschlossen werden.

## Standard-Import von Matrixprodukten

Den Standard-Import von Matrixprodukten mit einer Importvorlage findest du hier:[Import von Matrixprodukten](https://help.xentral.com/hc/de/articles/360016758939#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574).

> **Anmerkung**
>
> Über die Importzentrale können maximal Matrizen mit zwei Gruppen importiert werden. Artikel mit mehr als zwei Gruppen müssen direkt über die Oberfläche des Matrixprodukts erzeugt werden.