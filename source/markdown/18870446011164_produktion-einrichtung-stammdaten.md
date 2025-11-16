In diesem Artikel geben wir dir einen Überblick, welche generelle Systemeinstellungen für die Produktion vorgenommen werden sollten und wie die Stammdaten für die Produktion aufgebaut werden können.

## Einrichtung

### Produktion

Klicke in deinem Xentral auf das Zahnrädchen oben rechts, um zu den Systemeinstellungen zu gelangen, und dort auf Administration > System:

![Produktion_Einrichtung_Pfad.png](https://help.xentral.com/hc/article_attachments/19368076634652)

Navigiere zum Abschnitt **Produktion**. Dort kannst du die unten stehenden Optionen einstellen.

![Produktion_Einrichtung_Produktion.png](https://help.xentral.com/hc/article_attachments/19368076637212)

(1) Verhalten Weiterführen Auftrag zu Produktion:

![Produktion_Einrichtung_Produktion_WeiterfuhrungAuftrag.png](https://help.xentral.com/hc/article_attachments/19368045402012)

> **Anmerkung**
>
> Diese Auswahl greift nur dann, wenn du Verkaufsaufträge in Produktionen weiterführen möchtest und du mit Unterstücklisten arbeitest, d. h. dass ein übergeordnetes Hauptprodukt ein oder mehrere Untererzeugnisse mit eigenen Stücklisten enthält. Möchtest du diese Funktionalitäten nicht nutzen, brauchst du keine Änderung vorzunehmen.

Folgende Optionen stehen zur Wahl:

- Unterstücklisten auflösen: Alle Komponenten, die in der Stückliste und deren Unterstücklisten enthalten sind, werden in die aus dem Verkaufsauftrag angelegte Produktion übernommen. Es befinden sich dann alle Komponenten in einer Produktionsstückliste derselben Ebene, die Struktur der Stückliste entfällt bei der Weiterführung.
- Unterstücklisten nicht auflösen: Aus dem Auftrag wird ausschließlich das Produkt, das auf der obersten Stücklistenebene steht, in die Produktion weitergeführt. Enthält dieses Produkt ein oder mehrere Unterstücklisten, so werden diese nicht in die Produktion übernommen und müssen bei Bedarf manuell geplant werden.
- Unterproduktionen anlegen: Bei der Weiterführung eines Verkaufsauftrags in die Produktion werden sowohl das Produkt der obersten Stücklistenebene, als auch enthaltene Untererzeugnisse als eigene Produktionen angelegt.

(2) Produktion nicht automatisch starten beim Weiterführen:

> **Anmerkung**
>
> Auch diese Auswahl ist nur relevant, wenn du Verkaufsaufträge in Produktionen weiterführen möchtest.

- Setzt du den Haken, stehen Produktionen nach der Weiterführung aus dem Auftrag im Status ANGELEGT. Die jeweilige Produktion findest du dann in der Produktionsübersicht im Reiter “In Bearbeitung” und muss noch manuell gestartet und freigegeben werden.
- Setzt du den Haken nicht, erhalten solche Produktionen sofort den Status FREIGEGEBEN und befinden sich im Reiter “Produktionssuche”.

(3) Unterproduktionen mit Hauptproduktion abschließen:

> **Anmerkung**
>
> Diese Wahl ist zu treffen, wenn du übergeordnete Hauptprodukte mit ein oder mehreren Untererzeugnissen hast und du für die Untererzeugnisse eigene Produktionen anlegst.

- Setzt du den Haken, werden die Produktionen der Untererzeugnisse automatisch abgeschlossen, sobald die Hauptproduktion abgeschlossen wird.
- Setzt du den Haken nicht, musst du die Unterproduktionen manuell abschließen.

(4) Mit der Produktionskorrektur kannst du beim Abschließen der Produktion individuelle Einstellungen vornehmen, z. B. wenn mehr oder weniger Komponenten als planmäßig gedacht verwendet wurden. Setze den Haken nur, wenn du diese Möglichkeit nicht aktivieren möchtest.

> **Anmerkung**
>
> Wir empfehlen, den Haken bei Nutzung der externen Produktion nicht zu setzen.

(5) Für externe Produktionsartikel keine Produktionen anlegen: Wenn du den Haken setzt, werden für Produktionsschritte, die durch einen externen Dienstleister durchgeführt werden sollen, keine Produktionen aus dem Verkaufsauftrag oder als Unterstücklisten-Vorgang angelegt. Dies ist z. B. dann sinnvoll, wenn du die externe Produktion auftragsunabhängig steuern möchtest. Zum Thema externe Produktion findest du[hier](https://help.xentral.com/hc/de/articles/18870429541788#UUID-46a11200-782c-e248-c999-2ec59fc42c17)weitere Informationen.

### Zusatzfelder Produktion

Im Abschnitt **Zusatzfelder Produktion** weiter unten auf der Einstellungen-Seite hast die Möglichkeit, bis zu fünf zusätzliche Spalten in der Produktionsübersicht anzeigen zu lassen. Du kannst bestimmte Felder als Spaltenbelegung auswählen:

![Produktion_Einrichtung_Systemeinstellungen_ZusatzfelderProduktion.png](https://help.xentral.com/hc/article_attachments/19368076641052)

## Stammdaten

### Artikel

Zur Nutzung der Produktionsfunktionalität benötigst du bei den Artikeln folgende Ausprägungen:

- Komponenten (Bauteile)
- Stücklisten (Produkte)

Zur Veranschaulichung betrachten wir im Folgenden ein sehr einfaches Beispiel, das uns durch die Produktion begleiten wird: Das Produkt “Fidgetspinner”, das aus zwei verschiedenen Bauteilen bestehen soll, wobei je Fidgetspinner ein Gehäuse und drei Kugellager benötigt werden:

![Produktion_Stammdaten_BspArtikel_Fertigerzeugnis_Bild.png](https://help.xentral.com/hc/article_attachments/19368045403932)

#### Allgemein

Sowohl die Komponenten als auch das Produkt mit Stückliste werden im gleichen Formular als Artikel angelegt. Wie du Artikel generell anlegst und verwaltest, ist in diesem Artikel beschrieben. Hier gehen wir nur auf die produktionsspezifischen Besonderheiten ein.

Klicke in der Artikelübersicht auf **Artikel hinzufügen ** oder in der Formularansicht**+NEU **, um einen neuen Artikel anzulegen. Das Formular ** Artikel**öffnet sich.

> **Tipp**
>
> Lege zuerst die Komponenten an, damit du sie anschließend gleich in deine Stückliste einfügen kannst.

#### Komponenten-Artikel anlegen

Gib einen Namen und weitere allgemeine Angaben für deinen Bauteil-Artikel oben im Reiter ein:

![Produktion_Stammdaten_BspArtikel_Komponente.png](https://help.xentral.com/hc/article_attachments/19368045404572)

Aktiviere weiter unten im Abschnitt **Artikel Optionen** die Lagerführung für den Artikel:

![Produktion_Stammdaten_BspArtikel_Komponente_Artikeloptionen.png](https://help.xentral.com/hc/article_attachments/19368076643228)

Optional kannst du im Abschnitt **Sonstige Einstellungen** die

- Chargenführung aktivieren, falls du verfolgen möchtest, welche Komponenten mit welcher Charge in deiner Produktion verbaut/verbraucht werden:
- oder die Seriennummernführung aktivieren, falls du verfolgen möchtest, welche Komponenten-Seriennummern in deiner Produktion verbaut werden. Wähle dafür **Originale einlagern und nutzen**:
- Außerdem kannst du den Haken bei Mindesthaltbarkeitsdatum setzen, wenn du dieses Datum mit dem Einlagern des Artikels mitführen möchtest:

Alle anderen Artikel-Einstellungen handhabst du einfach je nach deinem individuellen Bedarf wie im entsprechenden[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/360016809699#UUID-aa696cfe-b602-15d0-fffe-44fa01f44cda)beschrieben.

#### Stücklisten-Artikel anlegen

Nachdem du alle Komponenten angelegt hast, kannst du mit dem Erzeugnis fortfahren. Zunächst nimmst du wieder einige generelle Einstellungen vor:

Gib einen Namen und weitere allgemeine Angaben für deinen Artikel oben im Reiter ein:

![Produktion_Stammdaten_BspArtikel_Fertigerzeugnis.png](https://help.xentral.com/hc/article_attachments/19368045411356)

Aktiviere im Abschnitt **Artikel Optionen** die Lagerführung für den Artikel:

![Produktion_Stammdaten_BspArtikel_Fertigerzeugnis_Artikeloptionen.png](https://help.xentral.com/hc/article_attachments/19368076651420)

Setze den Haken neben “Stückliste” im Abschnitt **Sonstige Einstellungen**:

![Produktion_Stammdaten_BspArtikel_Fertigerzeugnis_SonstigeEinstellungen.png](https://help.xentral.com/hc/article_attachments/19368076652700)

> **Anmerkung**
>
> Sobald du auf Speichern klickst, wird der Reiter Stückliste hinzugefügt, in welchem du mit der Stückliste fortfahren kannst.

*Optional* kannst du im gleichen Abschnitt die

![Produktion_Stammdaten_BspArtikel_Komponente_SonstigeEinstellungen_CN.png](https://help.xentral.com/hc/article_attachments/19368045405852)

- Chargenführung aktivieren, falls du für dein Produkt eine Chargennummer anlegen möchtest:
- oder die Seriennummernführung aktivieren, falls du für dein erzeugtes Produkt in der Produktion eine Seriennummer anlegen möchtest. Wähle dafür Originale einlagern und nutzen:
- Außerdem kannst du den Haken bei Mindesthaltbarkeitsdatum setzen, wenn du dieses Datum mit dem Einlagern des Artikels mitführen möchtest:

Darüber hinaus kannst du den Haken neben “Produktionsartikel” setzen, falls du ermöglichen möchtest, das Produkt aus einem Verkaufsauftrag direkt in eine Produktion weiterzuführen.

> **Anmerkung**
>
> Die Felder “Just-In-Time Stückliste”, “Einzelpos. ausblenden” und “Vorproduzierte Stückliste” gehören nicht zur Produktion und bleiben in unserem Fall leer. Besuche die entsprechenden Links, um Details zu den Feldern “Externe Produktion” und “Rohstoffliste” zu erfahren.

Alle anderen Artikel-Einstellungen handhabst du einfach je nach deinem individuellen Bedarf wie im entsprechenden[Handbuchabschnitt](https://help.xentral.com/document/preview/6012#UUID-f85ed282-d224-2419-081e-c39a5a14a443)beschrieben.

#### Stückliste manuell anlegen oder importieren

Nachdem du den Haken neben “Stückliste” gesetzt und den Artikel gespeichert hast, steht dir im Artikel des Fertigerzeugnisses der **Reiter Stückliste** zur Verfügung. Du kannst nun deine Komponenten in deine Stückliste einfügen und so die Verknüpfung der Komponenten zum Produkt herstellen. Zum Anlegen der Stückliste stehen dir zwei Methoden zur Verfügung:

- Komponenten manuell anlegen
- Stückliste importieren

##### Komponenten manuell anlegen

Klicke im Reiter Stückliste auf **+ Neue Position** um eine neue Position hinzuzufügen:

![Produktion_Stammdaten_BspArtikel_Fertigerzeugnis_Stuckliste_NeuePosition.png](https://help.xentral.com/hc/article_attachments/19368076654364)

Wähle im Fenster die Artikelnummer der Komponente aus, trage die benötigte Menge für ein Produkt ein und speichere:

![Produktion_Stammdaten_BspArtikel_Fertigerzeugnis_Stuckliste_Teilemenge.png](https://help.xentral.com/hc/article_attachments/19368076656028)

> **Anmerkung**
>
> Die anderen Einstellungen in diesem Fenster sind Sonderfunktionen, die hier näher beschrieben werden.

Wiederhole das Vorgehen mit allen weiteren Komponenten.

##### Stückliste importieren

Möglicherweise hast du im Unternehmen eine Datenquelle, z. B. ein CAD-, SPICE- oder Produktdaten-Management-Programm, aus dem du Stücklistendaten entnehmen kannst. Dann ist ein Import natürlich - insbesondere bei langen Stücklisten - noch komfortabler als das manuelle Anlegen.

![Produktion_Stammdaten_Excelstuckliste.png](https://help.xentral.com/hc/article_attachments/19368045416348)

1. Datenvorbereitung: Die Daten werden in Listenform benötigt, wobei die Komponenten-Artikelnummer in einer Spalte und die Menge in einer zweiten Spalte aufgeführt ist. Speichere sie in.CSV-Format ab. Eventuell kann das Quellprogramm die Daten direkt in dem gefordertem Format bereitstellen.
1. Gehe im Reiter Stückliste auf **Stückliste importieren**:
1. Wenn in der.CSV-Datei eine Überschrift enthalten war, kannst du durch Wahl des Optionskästchens festlegen, dass die übernommenen Daten erst einer späteren Zeile beginnen (hier: Zeile 2). Du kannst außerdem die Spalteninhalte zuweisen. Eine Spalte mit anderen Daten als Artikelnummer oder Menge ordnest du einfach keinem Feld zu (hier: Spalte “Zeichnung”). Sobald die Datenstruktur stimmt, klicke auf **Jetzt importieren**.

> **Anmerkung**
>
> Die Anzeige dient nur der Kontrolle der Datenstruktur und ist auf zehn Zeilen begrenzt. Sollte deine.CSV-Datei mehr als zehn Positionen beinhalten, werden alle Positionen beim Klick auf “Jetzt importieren” übernommen.

#### Stückliste verwalten

Nachdem du die Stückliste angelegt oder importiert hast, kannst du dir jederzeit im Reiter Stückliste einen schnellen Überblick über die benötigten Teile, deren Lagerbestand (über alle Lagerorte) und deren Struktur verschaffen:

![Produktion_Stammdaten_BspArtikel_Fertigerzeugnis_Stuckliste.png](https://help.xentral.com/hc/article_attachments/19368076663836)

Im Artikelformular einer Komponente kannst du wiederum im Reiter “In Stückliste” die `Teileverwendung` sehen, also in welchen Produkten ein Bauteil in welcher Menge benötigt wird:

![Produktion_Stammdaten_BspArtikel_Komponente_Teileverwendung.png](https://help.xentral.com/hc/article_attachments/19368045432348)

### Optional: Lagerplätze

Du kannst einschränken, dass Produktionsvorgänge nur auf sog. **Bevorzugte Lager** zugreifen können. Wenn du diese Option einrichten möchtest, gehe zur Lagerverwaltung und setze bei allen Lagerplätzen, die für die Produktion zur Verfügung stehen sollen, den folgenden Haken:

![Produktion_Stammdaten_Lager_Produktionslager.png](https://help.xentral.com/hc/article_attachments/19368076666908)

Es werden dann nur noch Lagerplätze in der Produktion als Bevorzugtes Lager angezeigt, die diesen Haken aktiviert haben. Alle Lager ohne diese Einstellung werden nicht mehr vorgeschlagen.

![Produktion_BevorzugtesLager.png](https://help.xentral.com/hc/article_attachments/19368045434908)

> **Tipp**
>
> Ist der Haken bei keinem Lagerplatz gesetzt, stehen hier alle Lager zur Auswahl.

### Optional: Projekte

Bestimmte Einstellungen für die Produktion kannst du projektspezifisch vornehmen. Gehe hierzu in die[Projektverwaltung](https://help.xentral.com/hc/de/articles/360016723620#UUID-a5ebd026-5507-1c92-7a7f-41bcefd1d0af), öffne ein Projekt zur Bearbeitung und navigiere zum Reiter Einstellungen → Logistik / Versand.

Im Bereich **Optionen ** hast du die Möglichkeit, ein**Bevorzugtes Lager** einzutragen. Dieses wird dann in allen Produktionen automatisch eingetragen, die diesem Projekt zugeordnet werden.

![Produktion_Stammdaten_Projekte_Optionen.png](https://help.xentral.com/hc/article_attachments/19368076673692)

### Optional: Arbeitsplatzgruppen

Arbeitsplatzgruppen kannst in Arbeitsanweisungen verwenden und dadurch bestimmte zusätzliche Informationen hinzufügen:

- Kosten pro Stunde
- Teile pro Stunde
- Anzahl Mitarbeiter pro Arbeitsplatzgruppe

Um zu den Arbeitsplatzgruppen zu gelangen, gib den Begriff in der Smart Search ein. Du gelangst dann zu folgender Übersicht:

![Produktion_Stammdaten_Arbeitsplatzgruppen_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19368076675356)

Eine neue Arbeitsplatzgruppe legst du einfach ein, indem du die entsprechenden Daten in diese Zeile eingibst und mit Anlegen bestätigst:

![Produktion_Stammdaten_Arbeitsplatzgruppen_Anlegen.png](https://help.xentral.com/hc/article_attachments/19368045444252)

Unter (1) kannst du eine Arbeitsplatzgruppe ändern, mit (2) löschst du sie:

![Produktion_Stammdaten_Arbeitsplatzgruppen_Menu.png](https://help.xentral.com/hc/article_attachments/19368076679196)

### Optional: Artikel Arbeitsanweisung Vorlagen

Wenn du mit Arbeitsanweisungen arbeiten möchtest, kannst optional Vorlagen dafür anlegen, die später in den (Stücklisten-)Artikel geladen werden können. So brauchst du Arbeitsschritt-Abfolgen, die bei mehreren Artikeln durchlaufen werden, nicht jedes Mal einzeln in die Artikel eingeben.

Suche in der Smart Search nachArtikel Arbeitsanweisung Vorlagen.

Um eine neue Vorlage anzulegen, gib eine Bezeichnung (1) in diese Zeile ein und klicke aufSpeichern. Damit die Vorlage in Artikel geladen werden kann, vergiss nicht den Haken bei aktiv zu setzen. Klicke auf den Pfeil (2), um die Vorlage zum Bearbeiten zu öffnen.

![Produktion_Stammdaten_ArbeitsanweisungVorlagen.png](https://help.xentral.com/hc/article_attachments/19368045446556)

1. Klicke auf Neuen Schritt hinzufügen.
1. Gib Details zu jedem Arbeitsschritt ein und speichere. Du kannst z. B. eine Beschreibung der Arbeitsschritte einfügen, die später die Mitarbeiter der Produktion als Vorgabe bekommen, eine Zeitvorgabe (pro Stück) und die Arbeitsplatzgruppe. Außerdem ist es möglich, ein Bild zu hinterlegen.
1. Wiederhole diesen Vorgang für alle zu durchlaufenden Arbeitsschritte.
1. Gehe in den Artikel, in den du eine Arbeitsanweisung einfügen möchtest und dort auf den Reiter Arbeitsanweisung. Wähle die Vorlage und klicke auf Laden. Wiederhole diese Schritte bei allen Artikeln, für die die Arbeitsanweisung gilt. Alternativ kannst du Schritte manuell, also ohne Vorlage hinzufügen.

### Optional: Artikel Funktionsprotokoll Vorlagen

Wenn du mit Funktionsprotokollen arbeiten möchtest, kannst optional Vorlagen dafür anlegen, die später in den (Stücklisten-)Artikel geladen werden können. So brauchst du Prüfschritt-Abfolgen, die bei mehreren Artikeln durchlaufen werden, nicht jedes Mal einzeln in die Artikel eingeben.

Suche in der Smart Search nachArtikel Funktionsprotokoll Vorlagen.

Um eine neue Vorlage anzulegen, gib eine Bezeichnung (1) in diese Zeile ein und klicke aufSpeichern. Damit die Vorlage in Artikel geladen werden kann, vergiss nicht den Haken bei aktiv zu setzen. Klicke auf den Pfeil (2), um die Vorlage zum Bearbeiten zu öffnen.

![Produktion_Stammdaten_FunktionsprotokollVorlagen.png](https://help.xentral.com/hc/article_attachments/19368076689180)

1. Klicke auf Neuen Schritt hinzufügen.
1. Gib Details zu jedem Prüfschritt ein und speichere. Du kannst z. B. eine Beschreibung der Prüfschritte einfügen, die später die Mitarbeiter der Produktion als Vorgabe bekommen, sowie ein Bild und die Angabe, ob der Prozess bei einem Fehler fortgesetzt werden soll.
1. Wiederhole diesen Vorgang für alle zu durchlaufenden Prüfschritte.
1. Gehe in den Artikel, in den du ein Funktionsprotokoll einfügen möchtest und dort auf den Reiter Funktionsprotokoll. Wähle die Vorlage und klicke auf Laden. Wiederhole diese Schritte bei allen Artikeln, für die das Funktionsprotokoll gilt. Alternativ kannst du Schritte manuell, also ohne Vorlage hinzufügen.