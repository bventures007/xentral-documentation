Mithilfe des ModulsErweiterter Bestellvorschlagkannst du den tatsächlichen Nachschubbedarf deiner Artikel ermitteln. Dieses Modul verfügt also über einen größeren Funktionsumfang als der[reguläre Bestellvorschlag](https://help.xentral.com/hc/de/articles/360016757859#UUID-b36d5a57-67bd-5185-edda-fd68cadb28a5). InXentral kannst du grundsätzlich zwei Beschaffungswege planen:

- Welche Teile über **Bestellungen** eingekauft werden müssen: Das erfährst du in diesem Artikel!
- Welche Teile selbst **produziert** werden müssen: Dies wird im [Artikel zum Thema Poduktionsplanung](https://help.xentral.com/hc/de/articles/18870446128284#UUID-4cda6245-518a-cd3d-3575-15139b36f57a) detailliert erläutert.

## Bestellbedarf ermitteln

Um deinen Bestellbedarf zu ermitteln, kannst du zwischen verschiedenen Berechnungsgrundlagen wählen - dies sind Bedarfe aus Mindestmengen, Aufträgen oder Produktionen.

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in den erweiterten Bestellvorschlag**
>
> Möchtest du dir innerhalb weniger Minuten einen Überblick über die Funktionen und die Nutzung des erweiterten Bestellvorschlags in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/yueMRRLnOkU)**

## Artikel für den erweiterten Bestellvorschlag auswählen

Öffne das Menü **Einkauf > Erweiterter Bestellvorschlag**, um die Bedarfe für deine Artikel zu berechnen. Im ersten Schritt kannst du auswählen, für welche Artikel du den Bedarf ermitteln möchtest.

> **Wichtig**
>
> Damit dein Bestellvorschlag berechnet werden kann, müssen in den Artikelstammdaten Einkaufspreise für den jeweiligen Lieferanten hinterlegt sein. Weitere Informationen dazu findest du im ArtikelArtikelstammdaten pflegen.

Im oberen Bereich des Menüs **Einkauf > Erweiterter Bestellvorschlag** hast du die Möglichkeit, Kriterien für die Erstellung des Bestellvorschlags pro Artikel auszuwählen.

![erweiterter-bestellvorschlag-optionen-de.png](https://help.xentral.com/hc/article_attachments/23598326720668)

- Aktiviere die Option **alle Artikel aus Stammdaten**, um einen Gesamtüberblick über sämtliche in Xentral gepflegten Artikel zu erhalten.
- Aktiviere alternativ die Option **nur durch Bestellvorschlag hinzugefügte Artikel anzeigen** um nur die Artikel anzuzeigen, für die aktuell ein Bedarf vorliegt - so schaffst du dir eine gezielte Übersicht über die Artikel, die nachbestellt werden müssen.

Zusätzlich kannst du weitere Filter setzen, zum Beispiel, wenn du nur Produktionen planen oder nur Bestellungen anlegen möchtest. Diese Filteroptionen werden in der folgenden Tabelle erläutert.

| Filteroption | Erläuterung |
| --- | --- |
| **Nur Produktionsartikel **| Zeigt nur Artikel, die nicht zugekauft, sondern durch eine Produktion erzeugt werden. Sie sind durch das Kennzeichen ** Produktionsartikel** markiert. Du benötigst diese Option für die [Produktionsplanung](https://help.xentral.com/hc/de/articles/18870446128284#UUID-4cda6245-518a-cd3d-3575-15139b36f57a). |
| **Nur Material / ohne Produktionsartikel **| Hier kannst du auf Einzelkomponenten filtern, also Artikel, bei denen das Kennzeichen ** Produktionsartikel** nicht aktiviert ist, weil sie zugekauft werden. Aktiviere diese Option, wenn du nur Bestellungen anlegen möchtest. |
| **Ohne Aufträge mit Bestellung** | Es gibt Kundenaufträge, die direkt mit einer zugehörigen Bestellung verknüpft sind. Aktiviere diese Option, wenn sie hier nicht angezeigt werden sollen. |

Die mithilfe der oben beschriebenen ausgewählten Artikel werden dann wie folgt in der Übersicht des Menüs **Einkauf > Erweiterter Bestellvorschlag** aufgelistet.

![erweiterter_bestellvorschlag-2-de.png](https://help.xentral.com/hc/article_attachments/23598372208156)

> **Wichtig**
>
> Die angezeigten Artikel sind zunächst nur eine leere Vorlage und dienen als Ausgangspunkt. Die eigentliche Bedarfsberechnung wird erst im nächsten Schritt durchgeführt!

## Bedarfe berechnen

Es gibt verschiedene Berechnungsgrundlagen ( auch als **Berechnungsläufe ** bezeichnet), die du einzeln oder nacheinander ausführen kannst. Du findest sie im Feld **Basis ** des Menüs**Einkauf > Erweiterter Bestellvorschlag**. Wie genau die einzelnen Berechnungslogiken funktionieren, erklären wir im Kapitel[Bedarfe berechnen](#UUID-56dcdac9-2d89-d96a-863c-0dc39eb2804a_section-id235260578263084). Zunächst möchten wir dir aber in der folgenden Tabelle noch weitere Filtermöglichkeiten für die Bedarfsberechnung zeigen.

| Filteroption | Erklärung |
| --- | --- |
| **Lieferant **| Wenn du den Bedarf für einen bestimmten Lieferanten ermitteln möchtest, kannst du den Filter im Feld ** Lieferant** setzen. Es werden dir alle Produkte angezeigt, für die bei diesem Lieferanten ein Einkaufspreis gepflegt ist. |
| **Tage einbeziehen von bis **| Wenn du als Basis Aufträge oder Produktionen verwendest, dann kannst du hier den Zeitraum über das Belegdatum eingrenzen. Für die Basis ** Mindestmengen **brauchst du diesen Belegfilter nicht. Dieser Zeitfilter wirkt sich nur auf die Berechnung der vorgeschlagenen Bestellmenge aus. Er hat keine Auswirkung auf die Anzeige in den Spalten ** Bedarf letzte X Tage **und ** Bedarf nächste X Tage**. |
| Suchfeld neben dem Feld **Basis **| Wenn du als Basis Aufträge oder Produktionen verwendest, dann kannst du hier einzelne Belege auswählen. Es wird dann nur der Bedarf berechnet, der aus diesem Beleg resultiert. Für die Basis ** Mindestmengen** brauchst du diesen Filter nicht und er wird dementsprechend auch nicht angezeigt. |

> **Wichtig**
>
> Wenn du mehrere Berechnungsläufe durchführst, ist die Einhaltung der Reihenfolge entscheidend für die Ausgabe eines korrekten Ergebnisses!

Grundsätzlich empfehlen wir dir, als erstes den Bedarf aus Produktionen zu ermitteln. Du verwendest keine Produktionen? Dann beginn damit,[Mindestmengen aufzufüllen](#UUID-56dcdac9-2d89-d96a-863c-0dc39eb2804a_section-id235260801922037).

### Berechnungsbasis: Nur offene Produktionen verwenden

Mit Auswahl der Option **Nur offene Produktionen verwenden ** aus dem Dropdown-Menü**Basis** ermittelt der Bestellvorschlag die Bedarfe, die sich aus offenen Produktionsaufträge ergeben. Es handelt sich also um Komponenten, die bestellt werden müssen, damit deine Produktionen durchgeführt werden können.

Über die Filter **Tage einbeziehen von ** und**Bis** im oberen Abschnitt kannst du eingrenzen, welche Produktionen in der Bedarfsermittlung berücksichtigt werden sollen.

Dabei werden dir folgende Informationen angezeigt:

- Falls es selbst ein Produktionsartikel ist: Menge, die aktuell in Fertigung ist
- Falls der Artikel in Produktionen benötigt wird: in Klammern **()** die Menge, die für aktuell geplante Produktionen benötigt wird ** Anwendungsbeispiel**:

Du handelst mit Nüssen und planst den Bedarf für deinen Produktionsartikel “Nuss-Mix”. Der Nuss-Mix wird gerade 2x produziert, so dass nach Abschluss der Fertigung ein Bestand von 2 Stück Nuss-Mix eingelagert werden kann. Es sind also 2 Stück im Zulauf. Diese Menge wird dir in der Spalte **in Produktion** angezeigt.

Weiterhin ist der Nuss-Mix Teil deines Geschenksets, das du ebenfalls anbietest. Es ist eine Produktion angelegt, die ein Geschenkset produzieren soll. Es gibt also 1 Stück, das für eine weitere Produktion benötigt wird. Der Bedarf aus offenen Produktionen ist also 1 und wird dir in der Spalte **in Produktion** in Klammern angezeigt.

![erweiterter-bestellvorschlag-produktion-de.png](https://help.xentral.com/hc/article_attachments/23598357551516)

### Berechnungsbasis: Mindestmengen

Wähle im Dropdown-Menü **Basis ** die Option **Mindestmengen ** aus und klicke auf**Starten**.

Xentral prüft, nun welche Menge beschafft werden muss, um den am Artikel hinterlegten Mindestbestand zu erreichen. Dabei wird folgende Berechnung durchgeführt:

- Mindestlagermenge = Gewünschter Lagerpuffer (z.B. 100 Stück)
- Lagerbestand = Aktuell vorhandene Menge im Lager (z.B. 0 Stück)
- Offene Bestellungen = Bereits bestellte, aber noch nicht gelieferte Menge (z.B. 5 Stück)
- Bedarf = Menge, die noch bestellt werden muss

```Bedarf = Mindestlagermenge - (Lagerbestand + offene Bestellungen)```

```Bedarf = 100 - (0 + 5) = 95```

Um nachzuvollziehen, wie das konkret in Xentral aussieht, schauen wir uns das Beispiel konkreter an.

Im Tab **Details ** der Artikelstammdaten findest du im Bereich **Lager/Abmessungen ** das Feld**Min. Lagermenge**. Hier trägst du die Lagermindestmenge ein.

![erweiterter-bestellvorschlag-lagermindestmenge-de.png](https://help.xentral.com/hc/article_attachments/23598334329756)

Im Tab **Lager** sehen wir die aktuelle Bestandssituation. Es befinden sich keine Artikel mehr auf Lager, aber 5 Stück wurden schon nachbestellt und warten auf Lieferung.

![bestellvorschlag-zahlenbeispiel-de.png](https://help.xentral.com/hc/article_attachments/23598357699100)

Führen wir nun die Berechnung auf Basis der Mindestmengen durch, erhalten wir im Bestellvorschlag die Vorschlagsmenge von 95 aus der Beispielrechnung.

![erweiterter-bestellvorschlag-mindestmenge-de.png](https://help.xentral.com/hc/article_attachments/23598319232540)

In unserem Beispiel fügen wir im nächsten Schritt noch die Bedarfe auf offenen Aufträgen hinzu.[Im folgenden Kapitel](#UUID-56dcdac9-2d89-d96a-863c-0dc39eb2804a_section-id235260843241303)erfährst du, wie das funktioniert.

### Berechnungsbasis: Nur offene Aufträge verwenden

Wir fügen nun noch die Bedarfe, die sich aus offenen Kundenaufträgen ergeben, hinzu. Wähle dafür im Dropdown-Menü **Basis ** die Option **Nur offene Aufträge verwenden ** aus. Als Nächstes definierst du einen einen Zeithorizont über die Felder **Tage einbeziehen von ** und**Bis**.

![erweiterter-bestellvorschlag-nur-offene-auftraege-de.png](https://help.xentral.com/hc/article_attachments/23598334498716)

Es werden in der Berechnung also nur die Aufträge berücksichtigt, deren **Auftragsdatum** im gefilterten Zeitraum liegt und die noch nicht abgeschlossen sind.

Für unseren Beispielartikel liegt ein Auftrag über 2 Stück vor, der noch offen ist. Dieser offene Bedarf wird im Tab **Lager ** in den Artikelstammdaten dargestellt. Im Artikel selbst haben wir im Tab**Details** eine Mindestbestellmenge von 10 Stück festgelegt.

Unserem Bestellvorschlag wird nun - zusätzlich zur vorherigen Berechnung - noch eine Bedarfsmenge von 10 Stück hinzugefügt, die sich aus den offenen Aufträgen (2 Stück) und der Mindestbestellmenge (10 Stück) ergeben. Zusätzlich zu den vorher berechneten 95 Stück ergibt sich nun eine kumulierte Vorschlagsmenge von 105 Stück.

![erweiterter-bestellvortag-alle-offenen-auftraege-de.png](https://help.xentral.com/hc/article_attachments/23598327146012)

Scrolle nach unten und klicke auf **Bestellung(en) erzeugen**, um die Bestellung direkt anzulegen.

### Berechnungsbasis: Nur offene Aufträge verwenden (Wunschlieferdatum, Liefertermin verwenden)

Du hast Aufträge mit längeren Lieferzeiten oder mit unterschiedlichen Lieferzeiten der einzelnen Positionen? Dann wähle im Dropdown-Menü **Basis ** die Option**Nur offene Aufträge verwenden (Wunschlieferdatum, Liefertermin verwenden)** aus. Die Berechnungslogik ist dieselbe wie bei der Option ** Nur offene Aufträge verwenden**: Es werden die Bedarfe aus offenen Aufträgen berücksichtigt. Der Unterschied liegt darin, dass der Zeitraum nicht nach dem Auftrags-, sondern nach dem jeweiligen Lieferdatum gefiltert wird.

Bei dieser Berechnungsbasis wird immer das bestmögliche Datum berücksichtigt – je nachdem, welche Informationen im Auftrag hinterlegt sind. Die Reihenfolge dabei ist:

1. **Lieferdatum ** aus der Auftragsposition: Diese Information findest du im Auftrag unter **Details > Positionen > Spalte: Lieferdatum**.
1. **Wunsch Liefertermin ** des gesamten Auftrags: Diese Information findest du im Auftrag unter **Details > Allgemein**.
1. **Auftragsdatum ** (falls kein Lieferdatum gepflegt ist): Diese Information findest du im Auftrag unter ** Details > Allgemein**.

### Berechnungsbasis: Alte Aufträge

Es werden alle Artikel vorgeschlagen, die sich in bereits abgeschlossenen Aufträgen befinden.

Das ist praktisch, um Artikel nachzubestellen, die sich bewährt haben oder regelmäßig verkauft wurden, auch wenn gerade keine offenen Aufträge vorliegen. Oder wenn du ein saisonales Geschäft hast und das diesjährige Weihnachtsgeschäft auf Basis des Vorjahres planen möchtest.

## Ergebnistabelle: Den Bestellvorschlag verstehen

Am Ende der Berechnung wird dir der Bestellvorschlag in einer Tabelle angezeigt. Hier siehst du alle wichtigen Informationen, die das System auf Basis deiner Einstellungen ermittelt hat. In den folgenden Abschnitten erklären wir dir, was die einzelnen Spalten bedeuten und wie das Ergebnis zustande kommt.

| Spaltenname | Erläuterung |
| --- | --- |
| **Artikel-Nr.** | Die Artikelnummer des Produkts in Xentral. |
| **Artikel** | Die Artikelbezeichnung des Produkts in Xentral. |
| **Lager** | Anzahl der Artikel, die aktuell auf Lager sind (inklusive Bestand auf Sperrlagerplätzen) |
| **Min. Lager** | Falls du in den Artikelstammdaten eine Mindestlagermenge festgelegt hast, wird diese Information hier angezeigt. |
| **Min. Bestellung** | Falls du in den Artikelstammdaten eine Mindestbestellmenge festgelegt hast, wird diese Information hier angezeigt. |
| **Im Auftrag** | Anzahl der Artikeleinheiten, die aktuell in offenen Aufträgen enthalten sind. |
| **In Produktion **| Anzahl der Artikel, die sich aktuell in Produktion befinden. Wird der Artikel als Komponente in einer anderen Produktion benötigt, so wird dieser Bedarf in Klammern** ()** angezeigt. |
| **In Bestellung (nicht vers.)**| Anzahl der Artikel, die bereits in laufenden Nachbestellungen enthalten sind. Wenn es Bestellungen gibt, die zwar angelegt, aber noch nicht versendet wurden, dann erscheint ein entsprechender Hinweis und die Menge wird in Klammern ** ()** angezeigt. |
| **Bedarf **| Der Bedarf ergibt sich aus dem aktuellen Lagerbestand (Spalte ** Lager **) minus der Mindestmenge (Spalte ** Min. Lager **) und abzüglich der Mengen, die bereits bestellt wurden. In der Spalte ** Bedarf** siehst du also auf einen Blick, wie viele Einheiten Xentral noch zur Bestellung vorschlägt. Der hier angezeigte Wert wird also aufgrund folgender Formel berechnet: Bedarf = Lager – Min. Lager + In Bestellung (nicht vers.) |
| **Bedarf letzte X Tage **| Menge der Artikel, die bereits in Aufträgen erfasst sind und deren Liefertermin in dem betrachteten Zeitraum (X Tage) lag. Wenn kein Lieferdatum für die Position hinterlegt ist, wird das Lieferdatum des Auftrags verwendet – und falls auch das fehlt, das Auftragsdatum. Für den Zeitraum zählt allein, was in der Spaltenüberschrift steht, Bedarf 30 Tage zeigt dir also alle Bedarfe aus den letzten 30 Tagen. Die Filter ** Tage einbeziehen von **und ** Bis** haben hier keine Auswirkung. |
| **Bedarf nächste X Tage **| Menge der Artikel, die bereits in Aufträgen erfasst sind und deren Liefertermin in der Zukunft (X Tage) liegt. Wenn kein Lieferdatum für die Position hinterlegt ist, wird das Lieferdatum des Auftrags verwendet – und falls auch das fehlt, das Auftragsdatum. Für den Zeitraum zählt allein, was in der Spaltenüberschrift steht, Bedarf 30 Tage zeigt dir also alle Bedarfe aus den nächsten 30 Tagen. Die Filter ** Tage einbeziehen von **und ** Bis** haben hier keine Auswirkung. |
| **Staffel** | Hier wird die Preisstaffel angezeigt, sofern du eine Preisstaffel in den Stammdaten des entsprechenden Lieferanten festgelegt hast. Im editierbaren Feld siehst du die Menge, die Xentral dir als Bestellmenge vorschlägt. Du kannst sie bei Bedarf manuell überschreiben. |
| **VK** | Der Verkaufspreis des Artikels aus den Artikelstammdaten. Staffelpreise werden hier ebenfalls angezeigt. |
| **Menü **| Im Tab ** Einstellungen **des Menüs ** Einkauf > Erweiterter Bestellvorschlag** kannst du festlegen, dass hier hier ein Link angezeigt werden soll, der dich beispielsweise direkt zu den Artikelstammdaten führt. Wenn du einen Link definiert hast, wird er dir hier mit einem Pfeil angezeigt. |

> **Wichtig**
>
> **Beachte bei der Verwendung der oben beschriebenen Staffeln zwingend folgende Einschränkung**:
>
> Die in den Artikelstammdaten gespeicherte Lieferzeit wird hier zwar angezeigt, jedoch nicht für die Bedarfsplanung berücksichtigt. Das bedeutet, dass die Lieferzeit des Artikels keinen Einfluss auf die angezeigten Informationen hat. Achte daher besonders auf Artikel, die lange Lieferzeiten bei deinem Lieferanten haben, um Engpässe zu vermeiden und die Bestellung frühzeitig auszulösen.

## Berechnung zurücksetzen

Du willst deine Berechnung nochmal komplett neu starten oder einzelne Berechnungsschritte rückgängig machen?

Per Klick auf Bestellvorschlag zurücksetzen oben rechts kannst du bei Bedarf alle zuvor in den Bestellvorschlag geladenen Artikel wieder aus der Liste löschen. Damit wird die Auswahl jeglicher Produkte zurückgesetzt, also die Checkboxen links in der Produkttabelle deaktiviert.

Du willst nur eine Berechnung löschen, zum Beispiel den Bedarf aus offenen Aufträgen?

Im oberen Bereich wird angezeigt, welche Berechnungsläufe durchgeführt wurden - in diesem Fall die Mindestmengen und die offenen Aufträge. Über Mengen entfernen kannst du den jeweiligen Berechnungslauf jederzeit wieder rückgängig machen.

![erweiterter-bestellvorschlag-zurzecksetzen-de.png](https://help.xentral.com/hc/article_attachments/23598372798492)

## Bestellung anlegen

Unterhalb der Filter und Hinweise befindet sich eine Übersicht über die Anzahl der unterschiedlichen Artikel und Lieferanten sowie der kumulierte Betrag für alle markierten Artikel. Dieser Betrag berechnet sich aus den Mengen in der Spalte **Bedarf** multipliziert mit dem Einkaufspreis des Artikels.

Passt alles? Dann klicke auf **Bestellung anlegen**, um eine Bestellung anzulegen. Dir wird im nächsten Schritt noch eine Zusammenfassung gezeigt, welche Positionen in die Bestellung übernommen werde, bevor sie final angelegt wird. Pro Lieferant wird daraufhin eine Bestellung erzeugt.

![bestellvorschlag-bestellung-erzeugen-de.png](https://help.xentral.com/hc/article_attachments/23598319650972)

> **Anmerkung**
>
> Der angezeigte kumulierte Betrag deines Bestellvorschlags kann von dem finalen Betrag der auf Basis des Bestellvorschlags erstellten Bestellungen abweichen. Grund dafür ist, dass sich dein Bedarf nicht mit der erforderlichen Mindestbestellmenge des Lieferanten deckt. Ist die Mindestbestellmenge deines Lieferanten höher als dein Bedarf, wird die Bestellung mit der Mindestbestellmenge angelegt.

## Weitere Einstellungen für erweiterte Bestellvorschläge

Öffne im Menü **Einkauf > Erweiterter Bestellvorschlag ** das Tab**Einstellungen**, um bei Bedarf weitere Einstellungen für das Modul vorzunehmen.

So kannst zu beispielsweise Zeitstaffeln definieren, für die der künftige Artikelbedarf auf Basis der freigegebenen Aufträge in Xentral angezeigt werden kann.

![erweiterter_bestellvorschlag_3-de.png](https://help.xentral.com/hc/article_attachments/18937452349340)

Die von dir erstellten Staffeln werden dann wie folgt als zusätzliche Spalten im Tab **Übersicht** angezeigt:

![erweiterter_bestellvorschlag_4-de.png](https://help.xentral.com/hc/article_attachments/18937414580252)

Die SpalteBedarf letzte x Tageerrechnet sich dabei aus den Artikeleinheiten, die in offenen Aufträgen enthalten sind und deren Lieferdatum in diesem Zeitraum liegt. Wurde für die einzelne Position eines Auftrags kein eigenes Lieferdatum definiert, so wird das Lieferdatum des Auftrags herangezogen. Ist diese Information ebenfalls nicht gepflegt, wird das Auftragsdatum verwendet.

Die SpalteBedarf nächste x Tageerrechnet sich aus der Menge an Artikeleinheiten, die sich in bereits angelegten Aufträgen befinden und deren Lieferdatum in diesem zukünftigem Zeitraum liegt. Auch hier wird, falls kein Lieferdatum für den einzelnen Artikel definiert ist, das Lieferdatum des Auftrags herangezogen. Wenn diese Information ebenfalls nicht gepflegt ist, wird das Auftragsdatum verwendet.

> **Wichtig**
>
> **Beachte bei der Verwendung der oben beschriebenen Staffeln zwingend folgende Einschränkung**:
>
> Die in den Artikelstammdaten gespeicherte Lieferzeit wird hier zwar angezeigt, jedoch nicht für die Bedarfsplanung berücksichtigt. Das bedeutet, dass die Lieferzeit des Artikels keinen Einfluss auf die angezeigten Informationen hat. Achte daher besonders auf Artikel, die lange Lieferzeiten bei deinem Lieferanten haben, um Engpässe zu vermeiden und die Bestellung frühzeitig auszulösen.

Bei Bedarf kannst du dir auch das Hauptartikelbild des jeweiligen Artikels innerhalb des Bestellvorschlags anzeigen lassen. Aktiviere dazu im Tab **Einstellungen ** die Option**Artikelbilder anzeigen**.

### Dynamische Berechnung von Lagermindestmengen

Die im System gepflegten Angaben zu den Lagermindestmengen der Artikel sind wesentliche Informationen, die in Xentral bei der Erstellung von Bestellvorschlägen berücksichtigt werden. Umso wichtiger ist es, dass die Lagermindestmengen deiner Artikel nicht nur ordnungsgemäß in den Artikelstammdaten gepflegt sind, sondern Änderungen an den Lagermindestmengen direkt für die Berechnung des Bestellvorschlags zur Verfügung stehen.

Damit du stets Zugriff auf aktuelle und korrekte Bestellvorschläge hast, kannst du eine separate Einstellung vornehmen. Diese Einstellung sorgt einmal täglich (über Nacht) für eine dynamische Berechnung der Lagermindestmengen deiner Artikel, sodass du dich bei der Verwaltung deiner Bestände stets auf den Bestellvorschlag verlassen kannst.

Gehe wie folgt vor, um die dynamische Berechnung von Lagermindestmengen zu aktivieren.

1. Öffne das Menü **Einkauf > Erweiterter Bestellvorschlag**.
1. Klicke auf das Tab **Einstellungen**.
1. Aktiviere die Option **Dynamische Lagermindestmengenberechnung aktivieren**.
1. Wähle aus dem Dropdown-Menü **Dynamische Berechnung speichern in Freifeld** das Freifeld in den Artikelstammdaten aus, in dem Xentral das Ergebnis der Lagermindestmengenberechnung automatisch speichern soll.
1. Klicke auf **Speichern **. Anschließend wird die Berechnung 1x täglich durch den Prozessstarter ** Bestellvorschlag **ausgeführt. Bei Bedarf kannst du den Zeitpunkt der Ausführung im Menü ** Einstellungen > Administration > Prozessstarter** anpassen. Wir empfehlen dir jedoch, die Standardeinstellung bei 01:30 Uhr zu belassen.

## Dynamische Lagermindestmengen

Xentral bietet die Möglichkeit, Lagermindestmengen dynamisch zu berechnen – basierend auf den vergangenen Bedarfen eines Artikels. So kann das System automatisch ermitteln, welche Mindestmenge sinnvoll ist, um rechtzeitig Nachbestellungen auszulösen. In den folgenden Kapiteln zeigen wir dir, wie du die dynamische Berechnung von Lagermindestmengen aktivierst.

### Dynamische Berechnung der Lagermindestmengen einrichten

Gehe wie folgt vor, um die dynamische Berechnung von Lagermindestmengen zu aktivieren.

1. Nutze die Smart Search, um das Modul **Freifelder** zu öffnen.
1. Definiere ein Feld.
1. Aktiviere die Option **Freifelder im Artikel einblenden**.
1. Klicke auf **Speichern**.
1. Öffne das Menü **Einkauf > Erweiterter Bestellvorschlag**.
1. Klicke auf das Tab **Einstellungen**.
1. Aktiviere die Option **Dynamische Lagermindestmengenberechnung aktivieren**.
1. Wähle aus dem Dropdown-Menü **Dynamische Berechnung speichern in Freifeld** das Freifeld in den Artikelstammdaten aus, das du zuvor in Schritt 2 definiert hast. Hier wird das Ergebnis der Berechnung dann angezeigt.
1. Klicke auf **Speichern**.

Sobald du die Option aktivierst, findet einmal täglich (über Nacht) folgende Berechnung statt:

```Mindestlagermenge = (Bedarfsstaffel letzte X Tage / Anzahl Tage) x (Lieferzeit Standard)```

Gehen wir die Berechnung einmal am Beispiel durch:

Die **Bedarfsstaffel letzte X Tage ** bestimmst du ebenfalls selbst in den Einstellungen des Moduls**Erweiterter Bestellvorschlag**. Hast du mehrere Bedarfsstaffeln definiert, so wird immer der erste Eintrag für die dynamische Berechnung verwendet. In unserem Beispiel sind es 10 Tage.

In unserem Beispiel wurden in den letzten 10 Tagen 90 Stück (50+20+20) verkauft, wie wir im Tab **Belege** der Artikelstammdaten nachvollziehen können.

Die Lieferzeit legst du selbst im gleichnamigen Feld am hinterlegten Einkaufspreis des Artikels unter **Artikel > Einkauf ** fest. Wenn es im Feld**Lieferzeit** aktuell einen Eintrag gibt, dann rechnet das System mit dieser Zeit, ansonsten mit der Standardzeit.

In unserem Beispiel ist eine **Lieferzeit aktuell ** von 2 Wochen, eine**Lieferzeit Standard** von 3 Wochen hinterlegt. Es wird also mit 14 Tagen kalkuliert.

![erweiterter-bestellvorschlag-artikel-lieferzeiten-de.png](https://help.xentral.com/hc/article_attachments/23598358221852)

Es ergibt sich also folgende Berechnung:

```Mindestlagermenge = (Bedarfsstaffel letzte 10 Tage / 10) x (Lieferzeit aktuell 14 Tage)```

```126 = (90 Stück Bedarf / 10 Tage) * 14 Tage Lieferzeit aktuell```

Dieses Ergebnis wird nach Durchlaufen des Prozessstarters **Bestellvorschlag ** im Freifeld am Artikel angezeigt (**Artikel > Tab: Details > Bereich: Weitere Felder**).

![erweiterter-bestellvorschlag-dynmenge-freifeld-de.png](https://help.xentral.com/hc/article_attachments/23598319736604)

> **Warnung**
>
> Damit die dynamische Berechnung funktioniert, muss in den Artikelstammdaten ein Lieferant mit einem Einkaufspreis hinterlegt sein und die Option **Standardlieferant** aktiviert sein.

Wenn im Tab **Einstellungen ** des Moduls **Erweiterter Bestellvorschlag ** die Option **Dynamische Lagermindestmengenberechnung aktivieren ** aktiviert ist, dann wird in der Berechnung des Bestellvorschlags der dynamische ermittelte Wert in der Spalte**Min. Lager** angezeigt. Dieser wird auch beim editierbaren Vorschlagswert berücksichtigt.

![erweiterter-bestellvorschlag-min-lager-uebersicht-de.png](https://help.xentral.com/hc/article_attachments/23598327598364)

Ist die Option **Dynamische Lagermindestmengenberechnung aktivieren ** nicht aktviert, dann wird der Wert angezeigt und für die Berechnung weiterverwendet, der im Feld**Min. Lagermenge** in den Artikelstammdaten hinterlegt ist.

In diesem Beispiel sind am Artikel 90 Stück als Mindestlagermenge definiert.

![erweiterter-bestellvorschlag-min-lagermenge-artikel-de.png](https://help.xentral.com/hc/article_attachments/23598373076508)

Dieser Wert wird dann auch im erweiterten Bestellvorschlag in der Spalte **Min. Lager** angezeigt und fließt in den berechneten Vorschlag ein, der dann übernommen oder nochmal manuell überschrieben werden kann.

> **Anmerkung**
>
> Im Bestellvorschlag wird in der Ergebnisspalte immer die Standardlieferzeit angezeigt, auch, wenn eine aktuelle Lieferzeit eingetragen ist. Aufgrund eines Darstellungsfehlers wird die Lieferzeit aktuell in “Wochen” angezeigt, die Berechnung ist aber korrekt.