## Überblick

Im Bereich Workflows kannst du nun die Details zu den gewählten Features konfigurieren und die Features einzeln aktiv schalten. Du erreichst die Workflows unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > [Marktplatzname] > Workflows**.

![Shared_Workflows_Ubersicht.png](https://help.xentral.com/hc/article_attachments/18670825450012)

## Allgemeine Funktionen

### Integrationsmodus

Die Schaltfläche “Aktivsteht dir in jedem Reiter zur Verfügung. Sie bezieht sich jeweils auf den Reiter, in dem du dich gerade befindest.

> **Anmerkung**
>
> Diese Schaltfläche benötigst du erst, nachdem du alle Einstellungen vorgenommen und getestet hast und alles bereit ist für den produktiven Einsatz deiner Schnittstelle.
>
> **Belasse den Schalter bis zum Abschluss deiner Tests auf links (inaktiv).**

![MiraklOtto_Workflows_Allgemein_Integrationsmodus.png](https://help.xentral.com/hc/article_attachments/18670825451676)

### Achtung

Erst nachdem deine Einrichtung und Tests abgeschlossen sind, kannst du die Schnittstelle produktiv schalten. Beachte dazu die Hinweise in diesem[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/18589768508828#UUID-94e6be55-89a9-e758-91fc-d82d54bd7940).

## Features-Reiter

Im Folgenden findest du zu jedem Feature detaillierte Konfigurationsmöglichkeiten.

### Reiter “Artikel”

#### Voraussetzungen

> **Anmerkung**
>
> Dieses Feature verwendest du, wenn du Stammdaten aus Xentral automatisch mit Mirakl abgleichen möchtest. Falls du Stammdaten lieber manuell in Mirakl pflegen möchtest, benötigst du diesen Reiter nicht.

Bevor du den Integrationsmodus aktiv schaltest, musst du

1. eine initiale Importdatei erstellen und anschließend
1. das Kategorienmapping auf Mirakl vornehmen.

Wie du die initiale Importdatei erstellst, erklären wir dir im nächsten Abschnitt. Wie du das Kategorienmapping vornimmst, findest du weiter unten.

> **Anmerkung**
>
> Nachdem du die Voraussetzungen geschaffen hast und die Übertragung mit einigen Testdaten geprüft hast, kannst du den Integrationsmodus aktivieren. Artikelstammdaten aus Xentral werden dann bei Neuanlage oder Änderungen an Mirakl übertragen.

#### Initiale Importdatei erstellen

Um das Kategorienmapping auf Mirakl vorzunehmen, benötigst du eine initiale Artikeldatei. Diese muss nicht alle Xentral Artikel enthalten, sondern nur so viele, dass alle Möglichkeiten an Kategorien, Attributen, Freifeldern etc. abgedeckt sind. Hast du also z. B. eine sehr einfache Artikelstruktur, bei der alle Artikel einer oder zwei Kategorien zugeordnet sind und wenige Freifelder verwendet werden, genügt es nur einige Artikel in die Importdatei zu übertragen. Ist der Artikelstamm sehr komplex mit vielen Kategorien und Freifeldern, kann es nötig sein, viele Artikel in die Datei zu schreiben, um sicherzustellen, dass alle Kombinationen abgedeckt werden.

> **Anmerkung**
>
> Die Importdatei musst du nur einmalig für das anschließende Mapping erzeugen. Nachdem das Mapping durchgeführt und das Feature aktiv geschaltet wurde, erfolgt der Austausch der Artikelstammdaten automatisch.

Um die initiale Artikeldatei zu erstellen, klicke auf **Initiale Datei erzeugen**.

![Workflows_Artikel_InitialeDatei.png](https://help.xentral.com/hc/article_attachments/18670825454108)

Wähle ein Limit abhängig von der Größe und Komplexität deines Artikelstamms aus.

![Workflows_Artikel_Datei_Limit.png](https://help.xentral.com/hc/article_attachments/18670851228188)

> **Anmerkung**
>
> Wie zuvor beschrieben, solltest du nur so viele Artikel wie nötig und so wenige wie möglich übertragen. Bei einem großen Limit dauert die Erzeugung und das Einlesen der Datei entsprechend lange.

### Reiter “Angebote”

Damit ein Artikel auf dem Marktplatz verkauft werden kann, muss ein sogenanntes Angebot angelegt werden. Ein Angebot besteht aus Beständen und Preisen, wobei beide getrennt voneinander aktiviert und deaktiviert werden können.

> **Anmerkung**
>
> Beispiel: Wenn du z. B. Preise manuell in Mirakl verwalten möchtest, kannst du die Bestände aktivieren, während du die Preise deaktiviert lässt. Diese werden dann nicht von Xentral übertragen.

#### Initiale Importdatei erstellen

Um Angebote einmalig auf Mirakl zu importieren, benötigst du eine initiale Angebotsdatei.

> **Anmerkung**
>
> Die Importdatei musst du nur einmalig für den initialen Import erzeugen. Nachdem das Feature aktiv geschaltet wurde, erfolgt der Austausch der Bestände und Preise automatisch.

Um die initiale Angebotsdatei zu erstellen, klicke auf **Initiale Datei erzeugen** und wähle als Limit “Alle”.

![Workflows_Angebote_InitialeDatei.png](https://help.xentral.com/hc/article_attachments/18670851229596)

#### Allgemein

![Workflows_Angebote_Allgemein.png](https://help.xentral.com/hc/article_attachments/18670825458076)

- Artikelzuordnung: Damit die Artikelzuordnung korrekt funktioniert, müssen die Felder richtig zugeordnet werden. Es stehen folgende Zuordnung zur Verfügung. Wähle:
  - “Marktplatz Artikelnummer”, um anhand der Xentral-Artikelnummer zuzuordnen oder
  - “GTIN”, um die Xentral EAN-Nummer aus dem Artikelstamm für die Zuordnung zu verwenden.
- Status für neue Angebote: Wähle den Status beim Erstellen von neuen Angeboten aus.

#### Bestand

![Workflows_Angebote_Bestand.png](https://help.xentral.com/hc/article_attachments/18670825459100)

- Auswahl Xentral Lager: Hake hier die Xentral-Lagerorte an, aus denen die Bestände (summiert) an den Marktplatz gemeldet werden.
- Reservierungen beachten: Setze den Schalter nach rechts, wenn die reservierte Menge vom Lagerbestand abgezogen werden soll.
- Offene Bestellungen beachten: Setze den Schalter nach rechts, wenn offene Auftragsmengen abgezogen werden sollen.
- Lagerkorrekturwert beachten: Setze den Schalter nach rechts, wenn der Lagerbestand um den im Artikel festgelegten Lagerkorrekturwert verändert werden soll. Das Feld “Lagerkorrekturwert” findest du unter Artikel → Details → Online-Shop Optionen, Bereich Lagerbestand.
- Pseudo Lagerzahl statt echten Lagerzahlen verwenden: Setze den Schalter nach rechts, wenn statt dem berechneten Lagerbestand eine im Artikelstamm festgelegte Pseudomenge übertragen werden soll. Das Feld “Pseudo Lagerzahl” findest du ebenfalls unter Artikel → Details → Online-Shop Optionen, Bereich Lagerbestand.

#### Preise

![Workflows_Angebote_Preise.png](https://help.xentral.com/hc/article_attachments/18670825463196)

- Kunde bzw. Kundengruppe: Falls du für deinen Marktplatz einen bestimmten Preis festlegen möchtest, kannst du in diesem Feld einen Kundennamen oder einen Kundengruppennamen eintragen. Möchtest du Standardpreise nutzen, lasse das Feld leer.
- Steuersatz (normal): Trage hier den Prozentwert (ohne Prozentzeichen) für normal besteuerte Artikel ein. (In Deutschland derzeit 19%)
- Steuersatz (ermäßigt): Trage hier den Prozentwert (ohne Prozentzeichen) für Artikel mit ermäßigtem Steuersatz ein. (In Deutschland derzeit 7%)

### Reiter “Aufträge”

Der Reiter Aufträge ist das Kernstück der Workflow-Konfiguration. Hier legst du unter anderem fest, ab welchem Zahlungsstatus Bestellungen aus demMarktplatzzu Xentral importiert werden und wie Zahlungen gehandhabt werden, wie Lieferbedingungen verknüpft werden, auf welche Artikelnummern Versandgebühren und Rabatte gebucht werden, wie mit Kommentaren verfahren werden soll und wie Kunden angelegt und zugeordnet werden.

#### Update Strategie

Grundsätzlich werden Aufträge erst dann importiert, wenn sie in Mirakl manuell akzeptiert wurden. Wenn du alle Aufträge automatisch zu Xentral importieren möchtest, ohne sie manuell in Mirakl auf akzeptiert zu setzen, aktiviere diese Schaltfläche:

![Workflows_Auftrage_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/18670825464604)

#### Projektzuordnung

![Workflows_Auftrage_Projektzuordnung.png](https://help.xentral.com/hc/article_attachments/18670851235612)

Wähle ein **Standardprojekt**, das standardmäßig in die importierten Aufträge eingefügt wird.

Sofern du unterschiedliche Vertriebskanäle in deinem Shop angelegt hast, kannst du sie unter **Sales Channel > Projekt Zuordnung** mit den dazugehörigen Xentral-Projekten verknüpfen

#### Zahlungsarten / Zahlungsweisen / Zahlungsbedingungen

![Mirakl_Workflows_Auftrage_Zahlungsarten.png](https://help.xentral.com/hc/article_attachments/21740287187740)

Hinterlege bei der **Standardzahlungsart** eine Zahlungsweise, die verwendet werden soll, falls keine Zahlungsweise vom Shop übergeben wird.

Wenn du den Schalter **Standardzahlungsart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Zahlungsart im Shop gezogen, sondern auch, wenn gar keine Zahlungsart zugeordnet ist.

Verknüpfe bei Bedarf weitere Zahlungsweisen, in dem du auf **+ Gruppe hinzufügen** klickst.

Du kannst außerdem Zahlungsarten auswählen, für die kein Autoversand gelten soll. Solche Aufträge werden importiert und können im weiteren Verlauf manuell in den Versand gegeben werden.

> **Anmerkung**
>
> Tippe die Zahlungsarten exakt so ein, wie sie im Marktplatz angelegt sind. Die Angabe findest du im Portal unter den Einstellungen.

#### Versandkosten

![TB_Workflows_Auftrage_Versandkosten.png](https://help.xentral.com/hc/article_attachments/20345584471068)

- Ordne unter **Artikelnummer für Versandkosten** den Porto-Artikel zu, auf den Versandgebühren geschrieben werden sollen.

#### Steuern

![Mirakl_Workflows_Auftrage_Steuern.png](https://help.xentral.com/hc/article_attachments/20345584472348)

- Trage den Standort des Versandlagers ein, damit Steuern korrekt berechnet werden können.
- Falls du eine USt-Identprüfung bereits im Shop abgedeckt hast, kannst du den Auswahlschalter **USt-IdNr. automatisch als geprüft kennzeichnen** nach rechts stellen, um eine Doppelprüfung zu vermeiden.

#### Rabatte

![TB_Workflows_Auftrage_WahrungRabatte.png](https://help.xentral.com/hc/article_attachments/20345584473756)

- Weise einen **Rabatt**

-Artikel zu, auf den Gutschriften und Rabatte gebucht werden sollen.

#### Kommentare

Lege hier fest, wie Kommentare aus dem Shop-Beleg in Xentral übernommen werden sollen.

![Shared_Workflows_Auftrage_Kommentare.png](https://help.xentral.com/hc/article_attachments/18670851239068)

Unter “Kommentar aus Bestellung verarbeiten” stehen dir folgende Möglichkeiten zur Verfügung:

- “nicht beachten”: Kommentare werden nicht übernommen
- “in Freitext schreiben”: Kommentare werden in das Freitextfeld des Auftrags importiert
- “in interne Bezeichnung schreiben”: Kommentare werden in das Interne Bezeichnung Feld des Auftrags importiert

Setze den Auswahlschieber bei **Autoversand bei Kommentar stoppen?** nach rechts, wenn du verhindern möchtest, dass Aufträge mit Kommentar automatisch im Auto-Versand fortgeführt werden.

#### Kundenzuordnung

In den folgenden Feldern legst du fest, wie Kunden zwischen deinem Shop und Xentral verknüpft werden sollen. Wir unterscheiden zwischen im Shop angelegten Kunden und Gastkunden, die kein Konto angelegt haben.

![Shared_Workflows_Auftrage_Kundenzuordnung.png](https://help.xentral.com/hc/article_attachments/18670825477148)

- Für Kunden sowie für Kunden ohne Kundenkonto (Gastkunden) hast du folgende Optionen:
- Hast du bei mind. einem der beiden vorhergehenden Felder die Option “Kunde aus Bestellung auf einen bestehenden Kunden zuordnen” gewählt, legst du im Feld **Kundenzuordnung** fest, anhand welcher Kriterien die Zuordnung erfolgt, wobei die Prüfreihenfolge “Kundennummer” vor “Mail-Adresse” vor “Name & Adresse” ist.

- Bestimme schließlich im Feld **Wenn kein Kunde gefunden wird, dann:** wie verfahren werden soll, falls kein Kunde zugeordnet werden kann:
- Setze den Auswahlschieber bei **Bestehende Kunden nur innerhalb des Projektes zuordnen?** nach rechts, wenn du die Suche nach Kunden auf das -spezifische Projekt in Xentral einschränken möchtest. Üblicherweise bleibt diese Schaltfläche deaktiviert.
- Hast du oben bei der Kundenanlage die Option “Jeden Kunden auf Default-Kunden schreiben” gewählt, trägst du schließlich im Feld “Default-Kunden auswählen” eine entsprechende Kundennummer ein.

#### Positionen

Setze den Auftragsschalter nach rechts, wenn du in den Belegen die Artikelbezeichnung aus dem XentralArtikelstamm andrucken möchtest. Dies ist beispielsweise sinnvoll, wenn du im Shop andere Bezeichnungen (z. B. für SEO-Zwecke) verwendest, als du in der Auftragsabwicklung nutzen möchtest. Du kannst außerdem wählen, ob bzw. welche Artikelbeschreibung in den Auftragspositionen angezeigt werden soll:

![Shared_Workflows_Auftrage_Positionen.png](https://help.xentral.com/hc/article_attachments/18670851247900)

### Reiter “Auftragsstatus & Tracking”

#### Update Strategie

![connect_workflows_auftragsstatus_update_otto.png](https://help.xentral.com/hc/article_attachments/18670851249948)

Setze den Schalter “Aufträge automatisch im Shop stornieren” nach rechts, wenn du Aufträge, die in Xentral storniert werden, auch im Marktplatz stornieren möchtest. Dies hat nur Auswirkungen auf noch nicht versendete Aufträge.

#### Versanddienstleister-Zuordnung

Klicke auf **+ Gruppe hinzufügen**, um die Versanddienstleister aus deinemMarktplatzmit den Versandarten in Xentral zu verknüpfen.

![MiraklShopify_Workflows_Auftragsstatus_Versanddienstleister.png](https://help.xentral.com/hc/article_attachments/18670851251484)

### Reiter "Belege"

In diesem Reiter kannst du einstellen, dass Belege aus Xentral als PDF an denMarktplatzexportiert werden. Um Rechnungs-Belege zu übertragen, aktiviere die Schaltfläche:

![Workflows_Belege.png](https://help.xentral.com/hc/article_attachments/18670851253148)

## Testphase und Produktivschaltung

### Testphase

Wenn du alle Einstellungen in den Workflows vorgenommen hast, solltest du die Anbindung ausgiebig testen.

Schränke die[Artikelzuordnung](https://help.xentral.com/hc/de/articles/18583246646684#UUID-9e1f9a28-77b4-16d1-be1a-bb9985f2090a)auf wenige Artikel ein.

Nutze einige Testdaten und führe die Tests mit Hilfe der Funktionen im[Journal](https://help.xentral.com/hc/de/articles/18583263358108#UUID-2c706abd-1741-7567-9171-df43c2e898f3)durch.

### Produktivschaltung

Sobald die Schnittstelle die Testdaten richtig und wie erwartet übergibt, kannst du mit der[Produktiv-Schaltung](https://help.xentral.com/hc/de/articles/18589768508828#UUID-94e6be55-89a9-e758-91fc-d82d54bd7940)fortfahren.

**Viel Spaß mit deiner neuen Schnittstelle!**