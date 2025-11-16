ZusammenfassungOptimiere deinen Shopify-Connector in Xentral: Konfiguriere Workflows für Artikel, Bestände, Preise und Aufträge. Aktiviere Funktionen individuell für effiziente Prozesse.

## Überblick

Im Bereich Workflows kannst du nun die Details zu den gewählten Features konfigurieren und die Features einzeln aktiv schalten. Du erreichst die Workflows unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopify-Connector > Workflows**.

![Shared_Workflows_Ubersicht.png](https://help.xentral.com/hc/article_attachments/18723405793820)

## Allgemeine Funktionen

### Integrationsmodus

Die Schaltfläche “Aktivsteht dir in jedem Reiter zur Verfügung. Sie bezieht sich jeweils auf den Reiter, in dem du dich gerade befindest.

> **Anmerkung**
>
> Diese Schaltfläche benötigst du erst, nachdem du alle Einstellungen vorgenommen und getestet hast und alles bereit ist für den produktiven Einsatz deiner Schnittstelle.
>
> **Belasse den Schalter bis zum Abschluss deiner Tests auf links (inaktiv).**

![ShopifyShopwareWoo_Workflows_Allgemein_Integrationsmodus.png](https://help.xentral.com/hc/article_attachments/18723449193116)

### Achtung

Erst nachdem deine Einrichtung und Tests abgeschlossen sind, kannst du die Schnittstelle produktiv schalten. Beachte dazu die Hinweise in diesem[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/18589752911516#UUID-e51cce39-191a-dec1-8f90-44b0af01a9f4).

## Features-Reiter

Im Folgenden findest du zu jedem Feature detaillierte Konfigurationsmöglichkeiten.

### Reiter “Artikel”

#### Datentypen

Lege fest, welche **Datentypen** zwischen den Systemen ausgetauscht werden sollen:

![Shopify_Workflows_Artikel_Datentypen.png](https://help.xentral.com/hc/article_attachments/21714227021468)

##### Nutzung von Übersetzungen

> **Anmerkung**
>
> Damit du die Übersetzungs-Funktion für Texte nutzen kannst, benötigst du die Shopify AppTranslate & Adapt (Lokalize), die du kostenlos im Shopify Appstore erhälst. Weitere Infos dazu findest duhier.

MIt der Connect-Schnittstelle kannst du Übersetzungen und kanal-spezifische Sprachen an Shopify übertragen. Folgende Felder werden dabei berücksichtigt:

- Artikel
- Kurztext
- Artikelbeschreibung
- Meta-Title
- Meta-Description
- Meta-Keywords

Um eine reibungslose und wunschgemäße Übertragung zu erreichen, beachte, dass die Übersetzungen nach folgender Priorität berücksichtigt werden:

1. Zuerst werden Online-Shop Texte berücksichtigt, die unter Artikel > Texte mit einer spezifischen Shop-Auswahl angelegt wurden.
1. Es folgen die Einträge, die unter Artikel > Texte ohne spezifische Shop-Auswahl gemacht wurden.
1. Abschließend werden Texte einbezogen, die unter Artikel > Details > Texte und Beschreibungen eingegeben wurden. Hierbei wird das Feld Artikelbeschreibung im Bereich Online-Shop Texte zuerst berücksichtigt - nur wenn dieses Feld leer ist, wenn das gleichnamige Feld im Bereich Beschreibung verwendet.

#### Meta Texte

Setze den Schalter nach rechts, wenn du Metatexte an den Shop übertragen möchtest.

![WooCommerce_Workflows_Artikel_Metatexte.png](https://help.xentral.com/hc/article_attachments/18723449194908)

#### Stammdaten

![Shared_Workflows_Artikel_Stammdaten.png](https://help.xentral.com/hc/article_attachments/18723405801884)

Um das Nettogewicht an den Shop zu übertragen, setze hier den Schalter nach rechts, andernfalls wird das Gewicht übertragen.

#### Update Strategie

Bestimme, wie Artikel von Xentral an den Shop übertragen werden sollen:

![Shared_Workflows_Artikel_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/18723449196828)

Bei der Update Strategie hast du folgende Möglichkeiten:

![Shared_Workflows_Artikel_UpdatestrategieDetails.png](https://help.xentral.com/hc/article_attachments/18723449201180)

Wenn Artikel, die du in Xentral löschst, automatisch im Shop gelöscht werden sollen, setze den Auswahlschalter “Produkte automatisch in Shop löschen?” nach rechts.

> **Anmerkung**
>
> Wird ein Matrixartikel gelöscht, werden alle zugehörigen Varianten im Shop gelöscht.

#### Steuern

Lege im folgenden Abschnitt die Steuereinstellungen fest:

![image-20240312-153334.png](https://help.xentral.com/hc/article_attachments/13235058458652)

- “Collection für reduzierten Steuersatz”: Falls es in deinem Shop Artikel gibt, für die ein reduzierter Steuersatz gilt, wähle hier die entsprechende Kollektion aus Shopify aus, um die richtige Steuerberechnung sicherzustellen.
- “Collection für befreiten Steuersatz”: Falls es in deinem Shop Artikel gibt, für die eine Steuerbefreiung gilt, wähle hier die entsprechende Kollektion aus Shopify aus, um die richtige Steuerberechnung sicherzustellen.
- “Steuersatz (normal)”: Trage hier den Prozentwert (ohne Prozentzeichen) für normal besteuerte Artikel ein. (In Deutschland derzeit 19%)
- “Steuersatz (ermäßigt)”: Trage hier den Prozentwert (ohne Prozentzeichen) für Artikel mit ermäßigtem Steuersatz ein. (In Deutschland derzeit 7%)
- “Nettopreise übertragen”: Stelle den Schalter nach rechts, wenn du im Shop Nettopreise gepflegt hast, oder auf links für Bruttopreise.
- “Land des Firmensitzes”: Wähle hier das Land aus, in dem deine Firma sitzt.

#### Freifeldzuordnung

Bei den Freifeldern hast du die Möglichkeit, Xentral Freifelder oder Xentral Eigenschaften an Metafelder in Shopify zu übertragen. Folgende Optionen stehen zur Wahl:

![connect_workflow_freefields.png](https://help.xentral.com/hc/article_attachments/15365033924380)

Freifeld zu Metafeld:

- “Freifelder aus Xentral übernehmen”: Freifelder aus Xentral werden automatisch in gleich lautende Metafelder geschrieben.
- “Manuelle Zuordnungstabelle”: Freifelder aus Xentral werden den Metafeldern manuell zugeordnet.

Eigenschaft zu Metafeld:

- “Eigenschaften aus Xentral automatisch in verfügbare Freifelder schreiben”: Eigenschaften aus Xentral werden automatisch in gleich lautende Metafelder geschrieben.
- “Eigenschaften aus Xentral den Shop verfügbaren Freifeldern manuell zuordnen”: Eigenschaften aus Xentral werden den Metafeldern manuell zugeordnet.

Bei der “Manuellen Zuordnungstabelle” und bei “Eigenschaften aus Xentral den Shop verfügbaren Freifeldern manuell zuordnen” erscheint eine Tabelle, in der du die Zuordnung eintragen kannst:

![image-20240223-085130.png](https://help.xentral.com/hc/article_attachments/15365050023836)

#### Sales Channels

Triff hier eine Auswahl, welchemShopify-Vertriebskanal die Artikel zugeordnet werden sollen.

![image-20240223-085310.png](https://help.xentral.com/hc/article_attachments/15365039893020)

#### Medien

Entscheide, ob Artikelbilder nur angelegt werden sollen, oder ob sie sowohl angelegt als auch gelöscht werden sollen.

![connect_media.png](https://help.xentral.com/hc/article_attachments/13921859495324)

### Reiter “Kategorie”

Hier legst du fest, welche Kategorien aus dem Xentral Artikelbaum in die Kategorien der Shopify Produkttaxonomie übertragen werden werden.

> **Anmerkung**
>
> Es erfolgtkeinedirekte Verknüpfung “Artikelkategorie zu Kollektion”. Wir verknüpfen Xentral Artikel-Tags mit Shopify Produkttags und den Xentral Artikelbaum mit der Shopify Produkttaxonomie. Wenn du Kollektionen auf Basis von Tags anlegen möchtest, erfolgt dies innerhalb Shopify mit automatisierten Anlage.

Für die erste Gruppe klicke auf **+ Gruppe hinzufügen** und ordne eine (Unter-)Kategorie des Xentral-Artikelbaums einer Shopify-Kategorie zu. Optional kannst du weitere Kategorien verknüpfen.

![connect_categorytab_shopify.png](https://help.xentral.com/hc/article_attachments/15371580665116)

Setze den Schalter **Warengruppe in Produkttyp übertragen?** nach rechts, wenn du die Xentral Artikelkategorie in den Shopify Produkttyp übertragen möchtest.

### Reiter “Bestand”

#### Lager

“Lager Zuordnung”: Verknüpfe hier die Lagerorte aus Xentral mit den entsprechenden Standorten des Shops. Du kannst mehrere Lagerorte verknüpfen:

![Shopify_Workflows_Bestand_Lagerzuordnung.png](https://help.xentral.com/hc/article_attachments/18723449202076)

> **Tipp**
>
> Wenn du einen neuen Lagerort angelegt hast, der im Auswahlfeld noch nicht zur Verfügung steht, klicke auf **Optionen neu laden**, um die Auswahl zu aktualisieren.

#### Lagerbestand berechnen

![Shared_Workflows_Bestand_Berechnen.png](https://help.xentral.com/hc/article_attachments/18723405805340)

Wähle folgende Optionen aus, um die an den Shop übertragene Bestandsmenge zu manipulieren:

- “Reservierungen beachten”: Setze den Schalter nach rechts, wenn die reservierte Menge vom Lagerbestand abgezogen werden soll.
- “Offene Bestellungen beachten”: Setze den Schalter nach rechts, wenn offene Auftragsmengen abgezogen werden sollen.
- “Lagerkorrekturwert beachten”: Setze den Schalter nach rechts, wenn der Lagerbestand um den im Artikel festgelegten Lagerkorrekturwert verändert werden soll. Das Feld “Lagerkorrekturwert” findest du unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.
- “Pseudo Lagerzahl statt echten Lagerzahlen verwenden”: Setze den Schalter nach rechts, wenn statt dem berechneten Lagerbestand eine im Artikelstamm festgelegte Pseudomenge übertragen werden soll. Das Feld **Pseudo Lagerzahl ** findest du ebenfalls unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.

### Reiter “Preise”

#### Preisauswahl

Falls du für deinenShopeinen bestimmten Preis festlegen möchtest, kannst du in diesem Feld einen Kundennamen oder einen Kundengruppennamen eintragen. Möchtest du Standardpreise nutzen, lasse das Feld leer.

![image-20240311-095853.png](https://help.xentral.com/hc/article_attachments/18723405807900)

> **Anmerkung**
>
> Trage hier nur dieBezeichnungder Gruppe ein, nicht die Kennziffer. Entnimm die korrekte Bezeichnung aus der Tabelle im ModulGruppen.

#### Erweiterte Preise

Wenn du Preisgruppen von Xentral in Shopify importieren möchtest, so aktiviere zunächst den Schalter “Erweiterte Preise importieren”. Anschließend kannst du diejenigen Xentral Kundengruppen auswählen, die für Shopify-B2B-Kataloge berücksichtigt werden sollen.

![Shopify_Workflows_Preise_ErweitertePreise.png](https://help.xentral.com/hc/article_attachments/20345615373340)

> **Anmerkung**
>
> Beachte, dass du die Kundengruppen in Shopify als Katalog anlegen musst und die Bezeichnungen in beiden Systemen gleich sein müssen.

### Reiter “Aufträge”

Der Reiter Aufträge ist das Kernstück der Workflow-Konfiguration. Hier legst du unter anderem fest, ab welchem Zahlungsstatus Bestellungen aus dem Shop zu Xentral importiert werden und wie Zahlungen gehandhabt werden, wie Vertriebskanäle zugeordnet und Lieferbedingungen verknüpft werden, auf welche Artikelnummern Versandgebühren und Rabatte gebucht werden, wie mit Kommentaren verfahren werden soll und wie Kunden angelegt und zugeordnet werden.

#### Update Strategie

Bestimme, welche Zahlungsstatus als Auslöser für den Import aus dem Shop dienen sollen und (optional) welcher Name als Bearbeiter in die importierten Aufträge eingetragen werden soll:

![Shared_Workflow_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/18723405811356)

#### Projektzuordnung

![image-20240223-095944.png](https://help.xentral.com/hc/article_attachments/15365546754972)

Wähle ein **Standardprojekt**, das standardmäßig in die importierten Aufträge eingefügt wird.

Sofern du unterschiedliche Vertriebskanäle in deinem Shop angelegt hast, kannst du sie unter **Sales Channel > Projekt Zuordnung** mit den dazugehörigen Xentral-Projekten verknüpfen

Außerdem kannst Du bestimmte **Tags** aus Shopify-Bestellungen einem Xentral-Projekt zuordnen. Beachte, dass diese Einstellung eine eventuelle Zuordnung über den Sales-Channel überschreibt.

#### Zahlungsarten / Zahlungsweisen / Zahlungsbedingungen

![Shopify_Workflows_Auftrage_Zahlungsarten.png](https://help.xentral.com/hc/article_attachments/21740257610140)

Hinterlege bei der **Standardzahlungsart** eine Zahlungsweise, die verwendet werden soll, falls keine Zahlungsweise vom Shop übergeben wird.

Wenn du den Schalter **Standardzahlungsart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Zahlungsart im Shop gezogen, sondern auch, wenn gar keine Zahlungsart zugeordnet ist.

Verknüpfe bei Bedarf weitere Zahlungsweisen, in dem du auf **+ Gruppe hinzufügen** klickst.

Du kannst außerdem Zahlungsarten auswählen, für die kein Autoversand gelten soll. Solche Aufträge werden importiert und können im weiteren Verlauf manuell in den Versand gegeben werden.

#### Versandarten & Lieferbedingungen

![Shopify_Workflows_Auftrage_Versandarten.png](https://help.xentral.com/hc/article_attachments/21740257610908)

- Hinterlege bei **Welche Lieferbedingungen sollen für den Bestellimport für diesen Onlineshop gelten?** eine feste Lieferbedingung, die bei importierten Belegen eingetragen wird. Möchtest du keine Lieferbedingungen nutzen, kannst du das Feld leer lassen.
- Hinterlege bei der **Standardversandart** eine Versandart, die verwendet werden soll, falls keine Versandart vom Shop übergeben wird.
- Wenn du den Schalter **Standardversandart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Versandart im Shop gezogen, sondern auch, wenn gar keine Versandart zugeordnet ist.
- Verknüpfe bei Bedarf weitere Versandarten, in dem Du auf **+ Gruppe hinzufügen** klickst.
- **Fast-Lane Versandarten**: Falls du deinen Kunden Express-Versandarten anbieten möchtest, kannst du auf dieses Feld klicken und dort die zutreffenden Versandarten anhaken.
- **Belege im Autoversand erstellen **: Wähle hier, welche Belege im Autoversand erstellt werden sollen. Die Option ** Nur Rechnung** bietet sich z. B. an, wenn du einen Abholprozess abbilden möchtest.

#### Versandkosten

![TB_Workflows_Auftrage_Versandkosten.png](https://help.xentral.com/hc/article_attachments/20345585100700)

- Ordne unter **Artikelnummer für Versandkosten** den Porto-Artikel zu, auf den Versandgebühren geschrieben werden sollen.

#### Steuern

![Shopify_Workflows_Auftrage_Steuern.png](https://help.xentral.com/hc/article_attachments/20345615377564)

- Belässt du den Auswahlschalter **Befreiten Steuersatz bei fehlender Steuerinformation übertragen** links (Standardeinstellung), erscheint beim Auftragsimport eine Fehlermeldung, für den Fall dass Steuerinformationen in den Auftragspositionen fehlen. Setze den Auswahlschalter nach rechts, falls du Steuerinformationen bewusst nicht übertragen möchtest. So unterbindest du an dieser Stelle ungewollte Fehlermeldungen.
- Trage den Standort des Versandlagers ein, damit Steuern korrekt berechnet werden können.
- Falls du eine USt-Identprüfung bereits im Shop abgedeckt hast, kannst du den Auswahlschalter **USt-IdNr. automatisch als geprüft kennzeichnen** nach rechts stellen, um eine Doppelprüfung zu vermeiden.
- Wenn dein jährlicher EU-weite Gesamtumsatz unter 10.000 EUR liegt, kannst du aktivieren, um die Mehrwertsteuer im Land des Lagerstandortes zu entrichten. **Besteuerung abhängig vom Lagerstandardort machen **

- Wenn du ** Gesamtbetrag festsetzen **aktivierst, übernimmt Xentral des Gesamtbetrag aus dem Verkaufskanal und berechnet ihn nicht als Summe aus den Einzelpreisen. So werden Rundungsdifferenzen vermieden. Aktivierst du diese Schaltfläche, kannst du im nächsten Feld die ** maximale Differenz** zwischen den Beträgen in Verkaufskanal und Xentral definieren. Überschreitet die Differenz eines Auftrags die von dir festgelegte Grenze, so wird der Autoversand für diesen Auftrag deaktiviert und du kannst die notwendigen Korrekturen vornehmen.

#### Rabatte

![TB_Workflows_Auftrage_WahrungRabatte.png](https://help.xentral.com/hc/article_attachments/20345615378716)

- Weise einen **Rabatt**

-Artikel zu, auf den Gutschriften und Rabatte gebucht werden sollen.

#### Kommentare

Lege hier fest, wie Kommentare aus dem Shop-Beleg in Xentral übernommen werden sollen.

![Shared_Workflows_Auftrage_Kommentare.png](https://help.xentral.com/hc/article_attachments/18723449217564)

Unter “Kommentar aus Bestellung verarbeiten” stehen dir folgende Möglichkeiten zur Verfügung:

- “nicht beachten”: Kommentare werden nicht übernommen
- “in Freitext schreiben”: Kommentare werden in das Freitextfeld des Auftrags importiert
- “in interne Bezeichnung schreiben”: Kommentare werden in das Interne Bezeichnung Feld des Auftrags importiert

Setze den Auswahlschieber bei **Autoversand bei Kommentar stoppen?** nach rechts, wenn du verhindern möchtest, dass Aufträge mit Kommentar automatisch im Auto-Versand fortgeführt werden.

#### Kundenzuordnung

In den folgenden Feldern legst du fest, wie Kunden zwischen deinem Shop und Xentral verknüpft werden sollen. Wir unterscheiden zwischen im Shop angelegten Kunden und Gastkunden, die kein Konto angelegt haben.

![Shared_Workflows_Auftrage_Kundenzuordnung.png](https://help.xentral.com/hc/article_attachments/18723449219612)

- Für Kunden sowie für Kunden ohne Kundenkonto (Gastkunden) hast du folgende Optionen:
- Hast du bei mind. einem der beiden vorhergehenden Felder die Option “Kunde aus Bestellung auf einen bestehenden Kunden zuordnen” gewählt, legst du im Feld **Kundenzuordnung** fest, anhand welcher Kriterien die Zuordnung erfolgt, wobei die Prüfreihenfolge “Kundennummer” vor “Mail-Adresse” vor “Name & Adresse” ist.

- Bestimme schließlich im Feld **Wenn kein Kunde gefunden wird, dann:** wie verfahren werden soll, falls kein Kunde zugeordnet werden kann:
- Setze den Auswahlschieber bei **Bestehende Kunden nur innerhalb des Projektes zuordnen?** nach rechts, wenn du die Suche nach Kunden auf das Shopify-spezifische Projekt in Xentral einschränken möchtest. Üblicherweise bleibt diese Schaltfläche deaktiviert.
- Hast du oben bei der Kundenanlage die Option “Jeden Kunden auf Default-Kunden schreiben” gewählt, trägst du schließlich im Feld “Default-Kunden auswählen” eine entsprechende Kundennummer ein.

#### POS Kunden

Wenn du POS-Kunden hast, wähle im Auswahlfeld “Ja” und gib im nächsten Feld die gewünschte allgemeine Kundennummer an.

![Workflows_Bestellungen08.png](https://help.xentral.com/hc/article_attachments/15365040691484)

> **Anmerkung**
>
> Dies ist nur zutreffend, falls du deinen Shop für Kunden nutzt, die vor Ort im Laden kaufen und von denen dir nicht alle Daten vorliegen, um ein einzelnes Kundenkonto anzulegen.

> **Tipp**
>
> Wenn du sowohl POS- als auch Online-Kunden hast, kannst du über dieSaleschannel-Zuordnungfür jeden Vertriebskanal unterschiedliche Projekte zuordnen, um die Prozesse unterschiedlich steuern und auswerten zu können.

#### Sprachenzuordnung

In diesem Abschnitt kannst du festlegen, in welcher Sprache Belege ausgegeben werden sollen. Du kannst die Sprache aus dem Shop übernehmen oder eine manuelle Zuordnung hinterlegen.

![Shopify_Workflows_Auftrage_Sprachenzuordnung__1_.png](https://help.xentral.com/hc/article_attachments/18723449227420)

> **Wichtig**
>
> Stelle sicher, dass die Sprachen, die du verwenden möchtest, in der Xentral-Sprachenliste angelegt sind. Weitere Hinweise dazu findest duhier.

#### Positionen

Setze den Auftragsschalter nach rechts, wenn du in den Belegen die Artikelbezeichnung aus dem XentralArtikelstamm andrucken möchtest. Dies ist beispielsweise sinnvoll, wenn du im Shop andere Bezeichnungen (z. B. für SEO-Zwecke) verwendest, als du in der Auftragsabwicklung nutzen möchtest. Du kannst außerdem wählen, ob bzw. welche Artikelbeschreibung in den Auftragspositionen angezeigt werden soll:

![Shared_Workflows_Auftrage_Positionen.png](https://help.xentral.com/hc/article_attachments/18723405840412)

### Reiter “Auftragsstatus & Tracking”

#### Update Strategie

![connect_workflows_update_shopify.png](https://help.xentral.com/hc/article_attachments/15365069973532)

Im Feld “Auftragsstatus für Auftragsstatus & Tracking Export” hast du folgende Wahlmöglichkeiten:

![image-20240223-090617.png](https://help.xentral.com/hc/article_attachments/15365034995228)

Setze den Schalter “Aufträge automatisch im Shop stornieren” nach rechts, wenn du Aufträge, die in Xentral storniert werden, auch im Shop stornieren möchtest.

Wenn in Xentral erstellte Retouren an den Shop übertragen werden sollen, setze den Schalter im entsprechenden Feld nach rechts.

#### Versanddienstleister-Zuordnung

Klicke auf **+ Gruppe hinzufügen**, um die Versanddienstleister aus deinemShopmit den Versandarten in Xentral zu verknüpfen.

![MiraklShopify_Workflows_Auftragsstatus_Versanddienstleister.png](https://help.xentral.com/hc/article_attachments/18723405843100)

#### Benachrichtigungen

Setze den Schalter nach rechts, wennShopifyeine Versandbenachrichtigung per Mail an den Kunden senden soll.

![Shared_Workflows_Auftragsstatus_Benachrichtigungen.png](https://help.xentral.com/hc/article_attachments/18723405847708)

### Reiter "Rückzahlungen" (Shopify Refund)

> **Anmerkung**
>
> Dies ist eine neue Funktionserweiterung. Falls du die Schnittstelle schon länger nutzt, kann es sein, dass du diesen Reiter noch nicht sehen kannst. Um ihn zu aktivieren, folge in Xentral dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopify-Connector > Einstellungen (Zahnrädchen)** und aktiviere dort das Feature "Rückzahlungen".

#### Funktionalität

Die Funktion "Rückzahlungen" ermöglicht, dass Gutschriften nach Freigabe automatisch als Rückzahlung an Shopify Pay übergeben und dem Kunden ausgezahlt werden.

##### Ablauf einer einzelnen Rückzahlung:

1. Auftrag als Retoure weiterführen. Details dazu findest du unter [Deine Retouren verwalten (Retouren Belege)](https://help.xentral.com/hc/de/articles/360016764099#UUID-7d6e48fa-434c-01df-f6fe-f1f4589f2f89).
1. Retoure als Gutschrift oder Stornorechnung weiterführen. Wenn du mehr dazu wissen möchtest, lies in o. g. Artikel weiter: [Deine Retouren verwalten (Retouren Belege)](https://help.xentral.com/hc/de/articles/360016764099#UUID-7d6e48fa-434c-01df-f6fe-f1f4589f2f89).
1. Gutschrift freigeben. Dadurch erscheint die Gutschrift in der Tabelle **Zahlungsverkehr**.
1. Tabelle **Zahlungsverkehr** öffnen.
1. Register "Offen": Vorgang markieren --> **Shopify Pay ** als Konto wählen -->**Zahlung zuordnen und freigeben**.
1. Register "Shopify Pay": Vorgang markieren --> **Zahlung ausführen**. Dadurch wird der Vorgang an Shopify Pay übergeben und die Zahlung an den Kunden veranlasst.

#### Aktivierung

Um die o. g. Funktionalität zu nutzen, stelle sicher, dass das Feature in den Einstellungen aktiviert ist und gehe dann in den Workflows zum Reiter "Rückzahlungen".

Setze dort die Schaltfläche Integrationsmodus nach rechts (aktiv):

![Shopify_Workflows_Ruckzahlungen.png](https://help.xentral.com/hc/article_attachments/18723449234844)

Es ist keine weitere Konfiguration notwendig.

## Testphase und Produktivschaltung

### Testphase

Wenn du alle Einstellungen in den Workflows vorgenommen hast, solltest du die Anbindung ausgiebig testen.

Schränke die[Artikelzuordnung](https://help.xentral.com/hc/de/articles/13235060173596#UUID-6b6b31e2-79dc-2826-dd07-8cf4e4976109)auf wenige Artikel ein.

Nutze einige Testdaten und führe die Tests mit Hilfe der Funktionen im[Journal](https://help.xentral.com/hc/de/articles/13921857699612#UUID-d8ed9992-afac-447b-5f28-2e5f96fd98ac)durch.

### Produktivschaltung

Sobald die Schnittstelle die Testdaten richtig und wie erwartet übergibt, kannst du mit der[Produktiv-Schaltung](https://help.xentral.com/hc/de/articles/18589752911516#UUID-e51cce39-191a-dec1-8f90-44b0af01a9f4)fortfahren.

**Viel Spaß mit deiner neuen Schnittstelle!**