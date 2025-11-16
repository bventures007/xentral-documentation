## Überblick

Im Bereich Workflows kannst du nun die Details zu den gewählten Features konfigurieren und die Features einzeln aktiv schalten. Du erreichst die Workflows unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware6-Connector > Workflows**.

![Shared_Workflows_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19197941299100)

## Allgemeine Funktionen

### Integrationsmodus

Die Schaltfläche “Aktivsteht dir in jedem Reiter zur Verfügung. Sie bezieht sich jeweils auf den Reiter, in dem du dich gerade befindest.

> **Anmerkung**
>
> Diese Schaltfläche benötigst du erst, nachdem du alle Einstellungen vorgenommen und getestet hast und alles bereit ist für den produktiven Einsatz deiner Schnittstelle.
>
> **Belasse den Schalter bis zum Abschluss deiner Tests auf links (inaktiv).**

![ShopifyShopwareWoo_Workflows_Allgemein_Integrationsmodus.png](https://help.xentral.com/hc/article_attachments/19197928827420)

### Achtung

Erst nachdem deine Einrichtung und Tests abgeschlossen sind, kannst du die Schnittstelle produktiv schalten. Beachte dazu die Hinweise in diesem[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/18589763018012#UUID-51edb066-e697-e70b-6116-829fdd05e479).

## Features-Reiter

Im Folgenden findest du zu jedem Feature detaillierte Konfigurationsmöglichkeiten.

### Reiter “Artikel”

#### Datentypen

Lege fest, welche **Datentypen** zwischen den Systemen ausgetauscht werden sollen:

![SW6_Workflows_Artikel_Datentypen.png](https://help.xentral.com/hc/article_attachments/21714233253404)

##### Nutzung von Übersetzungen

MIt der Connect-Schnittstelle kannst du Übersetzungen und kanal-spezifische Sprachen an Shopware übertragen. Folgende Felder werden dabei berücksichtigt:

- Artikel
- Kurztext
- Artikelbeschreibung
- Meta-Title
- Meta-Description
- Meta-Keywords
- Feldfeld-Namen (Übertragung erfolgt nur einmalig bei Neuanlage des Freifeldes)
- Freifeld-Werte

Um eine reibungslose und wunschgemäße Übertragung zu erreichen, beachte, dass die Übersetzungen nach folgender Priorität berücksichtigt werden:

1. Zuerst werden Online-Shop Texte berücksichtigt, die unter Artikel > Texte mit einer spezifischen Shop-Auswahl angelegt wurden.
1. Es folgen die Einträge, die unter Artikel > Texte ohne spezifische Shop-Auswahl gemacht wurden.
1. Abschließend werden Texte einbezogen, die unter Artikel > Details > Texte und Beschreibungen eingegeben wurden. Hierbei wird das Feld Artikelbeschreibung im Bereich Online-Shop Texte zuerst berücksichtigt - nur wenn dieses Feld leer ist, wenn das gleichnamige Feld im Bereich Beschreibung verwendet.

Stelle bei den Freifeldern sicher, dass die[Freifeldzuordnung](#UUID-b0386169-a59f-1d8d-1375-62b9ba1825d5_N1755081332200)korrekt erfolgt ist, damit die Übertragung der Übersetzungen funktioniert.

#### Meta Texte

Setze den Schalter nach rechts, wenn du Metatexte an den Shop übertragen möchtest.

![WooCommerce_Workflows_Artikel_Metatexte.png](https://help.xentral.com/hc/article_attachments/19197941306396)

#### Stammdaten

![Shared_Workflows_Artikel_Stammdaten.png](https://help.xentral.com/hc/article_attachments/19197928835484)

Um das Nettogewicht an den Shop zu übertragen, setze hier den Schalter nach rechts, andernfalls wird das Gewicht übertragen.

#### Update Strategie

Bestimme, wie Artikel von Xentral an den Shop übertragen werden sollen:

![Shared_Workflows_Artikel_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/19197928838172)

Bei der Update Strategie hast du folgende Möglichkeiten:

![Shared_Workflows_Artikel_UpdatestrategieDetails.png](https://help.xentral.com/hc/article_attachments/19197928839964)

Wenn Artikel, die du in Xentral löschst, automatisch im Shop gelöscht werden sollen, setze den Auswahlschalter “Produkte automatisch in Shop löschen?” nach rechts.

> **Anmerkung**
>
> Wird ein Matrixartikel gelöscht, werden alle zugehörigen Varianten im Shop gelöscht.

#### Steuern

Lege im folgenden Abschnitt die Steuereinstellungen fest:

![connect_workflow_taxes_shopware6.png](https://help.xentral.com/hc/article_attachments/15365095812508)

- “Steuersatz (normal)”: Wähle hier den Steuersatz von Shopware aus, den du für den normalen Steuersatz vorgesehen hast.
- “Steuersatz (ermäßigt)”: Wähle hier den Steuersatz von Shopware aus, den du für einen ermäßigten Steuersatz vorgesehen hast.
- “Steuersatz (befreit)”: Wähle hier den Steuersatz von Shopware aus, den du für eine Steuerbefreiung vorgesehen hast.

#### Freifeldzuordnung

Bei den Freifeldern hast du die Möglichkeit, Xentral Freifelder an SW6 Freifelder oder Xentral FreiFelder in SW6 zu übertragen. Folgende Optionen stehen zur Wahl:

![41_SW6_WorkflowArtikelFreifelderDetails.png](https://help.xentral.com/hc/article_attachments/19197928842780)

Freifeld zu Freifeld:

- “Freifelder aus Xentral übernehmen”: Hiermit werden Freifelder aus Xentral mit SW6 Freifeldern verknüpft.
- “Manuelle Zuordnungstabelle”: Schreibe die gewünschten Feldverknüpfungen in die Tabelle “Freifeldzuordnung”

Freifeld zu Eigenschaft:

- “Freifelder aus Xentral automatische in verfügbare Eigenschaften schreiben”: Mit dieser Auswahl werden Freifelder aus Xentral mit SW6 Eigenschaften verknüpft.
- “Freifelder aus Xentral den im Shop verfügbaren Eigenschaften manuell zuordnen”: Hier kannst du die Feldverknüpfungen wie bei der manuellen Zuordnungstabelle eintragen. Beachte dabei, dass der Name der Xentral Eigenschaft mit dem Namen der SW6 Eigenschaft übereinstimmen muss.

> **Anmerkung**
>
> Es ist derzeit nicht möglich, Xentral Freifelder sowohl mit SW6 Freifeldern als auch SW6 Eigenschaften abzugleichen.

> **Anmerkung**
>
> **Feature-Hinweis: Freifelder von Xentral automatisch in Shopware 6-Eigenschaften übertragen**
>
> Bei der Schnittstelle zwischen Xentral und Shopware 6 ist es möglich, bestimmte Freifelder von Xentral direkt mit der jeweiligen Shopware 6-Eigenschaft zu verknüpfen. Die Verknüpfung (Mapping) erfolgt automatisch durch die Systeme, wenn es sich in Shopware 6 um ein Standardfeld handelt und die Bezeichnungen in beiden Systemen identisch gewählt werden.
>
> Standardmäßig können folgende Shopware 6-Eigenschaften aus Xentral-Freifeldern befüllt werden:
>
> - shopware6_max_purchase
> - shopware6_min_purchase
> - shopware6_purchase_steps
> - shopware6_reference_unit
> - shopware6_unit
> - shopware6_release_date
> - shopware6_pack_unit
> - shopware6_pack_unit_plural
> - shopware6_restock_time
> - shopware6_delivery_time *)
>
> Tipp*) Die Shopware 6-Eigenschaft shopware6_delivery_time kann wahlweise befüllt werden aus:
> - einem Xentral-Freifeld mit gleich lautender Bezeichnung,
> - einem Xentral-Freifeld mit der Bezeichnung "Lieferzeit",
> - dem Feld "Lieferzeittext manuell", das sich im Artikel unter Details > Online-Shop Optionen befindet.
>
> Damit die reibungslose automatische Übertragung funktioniert stelle folgendes sicher:
>
> - Voraussetzung: Die Übertragung von einem Freifeld erfolgt zu einem o. g. Shopware 6-Standardfeld.
> - Die Bezeichnung des Artikel Freifeldes unter Systemeinstellungen > Stammdaten > Freifelder ist identisch mit der jeweiligen Bezeichnung der Shopware 6-Eigenschaft. Bei Shopware 6-Dropdown-Feldern muss die Freifeld-Bezeichnung in Xentral mit der Dropdown-Option in Shopware 6 übereinstimmen.
> - Im Falle des Feldes shopware6_release_date wähle den Freifeld Typ "Datum" und blende das Feld in den Artikel > Details ein, um das Datum einpflegen zu können. Das Freifeld könnte in den Systemeinstellungen z. B. so konfiguriert werden:
>
> Für Eigenschaften, die in Shopware 6 keine direkten Standardfelder besitzen, wird ein Customizing benötigt. Hierbei wird die Freifeld-ID manuell an die entsprechende ID in Shopware angepasst.
>
> Wende dich in einem solchen Fall gerne an deinen Solution Consultant. Er unterstützt dich bei der kundenindividuellen Beratung und Anpassung oder kann dich an einen geeigneten Partner vermitteln. Wenn du noch keinen Solution Consultant hast, öffne ein Ticket bei unserem Support.

#### Sales Channels

Triff hier eine Auswahl, welchemShopware6-Vertriebskanal die Artikel zugeordnet werden sollen.

![connect_workflows_saleschannels_shopware6.png](https://help.xentral.com/hc/article_attachments/15365069261084)

#### Medien

Weise hier einen Ordner zu, in den Artikelbilder gespeichert werden und entscheide, ob Artikelbilder nur angelegt werden sollen, oder ob sie sowohl angelegt als auch gelöscht werden sollen.

![connect_workflow_media_shopware6.png](https://help.xentral.com/hc/article_attachments/15365080493724)

#### Artikelseite

Wähle hier optional eine Ansicht aus, wie die Artikelseite im Shop aussehen soll und wie Varianten in der Storefront dargestellt werden sollen:

![connect_workflow_productpage.png](https://help.xentral.com/hc/article_attachments/21740302672412)

### Reiter “Kategorie”

Setze die Schaltfläche nach rechts (aktiv), wenn du Kategorien, die du in Xentrallöschst, automatisch auch im Shop entfernt haben möchtest. Wird eine Kategorie mit Unterkategorien gelöscht, werden diese ebenfalls entfernt.

![Shared_Workflows_Kategorie_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/19197941319580)

Hier kannst du wählen, welche Artikelbaum-Kategorie verknüpft werden soll und ob diese selbst mit übertragen wird oder nur alle darunter befindlichen Kategorien:

![Shopware_Workflows_Kategorie_Kategoriezuordnung_2506.png](https://help.xentral.com/hc/article_attachments/20836826645532)

### Reiter “Bestand”

#### Lager

“Auswahl Xentral Lager”: Hake hier die Xentral-Lagerorte an, aus denen die Bestände (summiert) an denShopgemeldet werden.

![OttoSW6Woo_Workflows_Bestand_Lagerzuordnung.png](https://help.xentral.com/hc/article_attachments/19197941325596)

> **Tipp**
>
> Wenn du einen neuen Lagerort angelegt hast, der im Auswahlfeld noch nicht zur Verfügung steht, klicke auf **Optionen neu laden**, um die Auswahl zu aktualisieren.

#### Lagerbestand berechnen

![Shared_Workflows_Bestand_Berechnen.png](https://help.xentral.com/hc/article_attachments/19197941327644)

Wähle folgende Optionen aus, um die an den Shop übertragene Bestandsmenge zu manipulieren:

- “Reservierungen beachten”: Setze den Schalter nach rechts, wenn die reservierte Menge vom Lagerbestand abgezogen werden soll.
- “Offene Bestellungen beachten”: Setze den Schalter nach rechts, wenn offene Auftragsmengen abgezogen werden sollen.
- “Lagerkorrekturwert beachten”: Setze den Schalter nach rechts, wenn der Lagerbestand um den im Artikel festgelegten Lagerkorrekturwert verändert werden soll. Das Feld “Lagerkorrekturwert” findest du unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.
- “Pseudo Lagerzahl statt echten Lagerzahlen verwenden”: Setze den Schalter nach rechts, wenn statt dem berechneten Lagerbestand eine im Artikelstamm festgelegte Pseudomenge übertragen werden soll. Das Feld **Pseudo Lagerzahl ** findest du ebenfalls unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.

### Reiter “Preise”

#### Preisauswahl

Falls du für deinenShopeinen bestimmten Preis festlegen möchtest, kannst du in diesem Feld einen Kundennamen oder einen Kundengruppennamen eintragen. Möchtest du Standardpreise nutzen, lasse das Feld leer.

![image-20240311-095853.png](https://help.xentral.com/hc/article_attachments/14528207282844)

> **Anmerkung**
>
> Trage hier nur dieBezeichnungder Gruppe ein, nicht die Kennziffer. Entnimm die korrekte Bezeichnung aus der Tabelle im ModulGruppen.

#### Währungszuordnung

Verknüpfe in diesem Bereich die Währungen aus Shopware mit ihren Entsprechungen in Xentral.

![connect_workflow_prices_currency_shopware6.png](https://help.xentral.com/hc/article_attachments/15365096227484)

#### Erweiterte Preise

Wenn du Preisgruppen von Xentral in Shopware importieren möchtest, so aktiviere zunächst den Schalter “Erweiterte Preise importieren”. Anschließend kannst du in der Tabelle links die Bezeichnung der Kundengruppe aus Xentral eintippen und die dazugehörige Gruppe aus Shopware rechts auswählen.

![connect_workflow_prices_extendedprices_shopware6.png](https://help.xentral.com/hc/article_attachments/15365108031260)

Im Anschluss kannst du wählen, ob die Xentral-Kundengruppen den Shop-Kundengruppen oder den Shop-Preisgruppen zugeordnet werden sollen.

In der darunter stehenden Tabelle tippst du links die Bezeichnung der Xentral-Kundengruppe ein und wählst rechts die dazugehörige Gruppe des Shops aus.

### Reiter “Aufträge”

Der Reiter Aufträge ist das Kernstück der Workflow-Konfiguration. Hier legst du unter anderem fest, ab welchem Zahlungsstatus Bestellungen aus demShopzu Xentral importiert werden und wie Zahlungen gehandhabt werden, wie Lieferbedingungen verknüpft werden, auf welche Artikelnummern Versandgebühren und Rabatte gebucht werden, wie mit Kommentaren verfahren werden soll und wie Kunden angelegt und zugeordnet werden.

#### Update Strategie

Bestimme, welche Zahlungsstatus als Auslöser für den Import aus dem Shop dienen sollen und (optional) welcher Name als Bearbeiter in die importierten Aufträge eingetragen werden soll. Außerdem kannst du festlegen, aus welchen Shopware-Verkaufskanälen Aufträge importiert werden sollen. Bestimme desweiteren, ob beim Auftragsimport automatisch eine Status-e-Mail an den Kunden versendet werden soll:

![SW6_Workflows_Auftrage_UpdateStrategie.png](https://help.xentral.com/hc/article_attachments/20345585526940)

#### Projektzuordnung

![SW6_Workflows_Auftrage_Projektzuordnung.png](https://help.xentral.com/hc/article_attachments/21714211124636)

Wähle ein **Standardprojekt**, das standardmäßig in die importierten Aufträge eingefügt wird.

Sofern du unterschiedliche Vertriebskanäle in deinem Shop angelegt hast, kannst du sie unter **Sales Channel > Projekt Zuordnung** mit den dazugehörigen Xentral-Projekten verknüpfen

#### Zahlungsarten / Zahlungsweisen / Zahlungsbedingungen

![SW6_Workflows_Auftrage_Zahlungsarten.png](https://help.xentral.com/hc/article_attachments/21740319475228)

Hinterlege bei der **Standardzahlungsart** eine Zahlungsweise, die verwendet werden soll, falls keine Zahlungsweise vom Shop übergeben wird.

Wenn du den Schalter **Standardzahlungsart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Zahlungsart im Shop gezogen, sondern auch, wenn gar keine Zahlungsart zugeordnet ist.

Verknüpfe bei Bedarf weitere Zahlungsweisen, in dem du auf **+ Gruppe hinzufügen** klickst.

Du kannst außerdem Zahlungsarten auswählen, für die kein Autoversand gelten soll. Solche Aufträge werden importiert und können im weiteren Verlauf manuell in den Versand gegeben werden.

#### Versandarten & Lieferbedingungen

![SW6_Workflows_Auftrage_Versandarten.png](https://help.xentral.com/hc/article_attachments/21740302676636)

- Hinterlege bei **Welche Lieferbedingungen sollen für den Bestellimport für diesen Onlineshop gelten?** eine feste Lieferbedingung, die bei importierten Belegen eingetragen wird. Möchtest du keine Lieferbedingungen nutzen, kannst du das Feld leer lassen.
- Hinterlege bei der **Standardversandart** eine Versandart, die verwendet werden soll, falls keine Versandart vom Shop übergeben wird.
- Wenn du den Schalter **Standardversandart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Versandart im Shop gezogen, sondern auch, wenn gar keine Versandart zugeordnet ist.
- Verknüpfe bei Bedarf weitere Versandarten, in dem Du auf **+ Gruppe hinzufügen** klickst.
- **Fast-Lane Versandarten**: Falls du deinen Kunden Express-Versandarten anbieten möchtest, kannst du auf dieses Feld klicken und dort die zutreffenden Versandarten anhaken.
- **Belege im Autoversand erstellen **: Wähle hier, welche Belege im Autoversand erstellt werden sollen. Die Option ** Nur Rechnung** bietet sich z. B. an, wenn du einen Abholprozess abbilden möchtest.

#### Versandkosten

![TB_Workflows_Auftrage_Versandkosten.png](https://help.xentral.com/hc/article_attachments/20345615777052)

- Ordne unter **Artikelnummer für Versandkosten** den Porto-Artikel zu, auf den Versandgebühren geschrieben werden sollen.

#### Steuern

![SW6_Workflows_Auftrage_Steuern.png](https://help.xentral.com/hc/article_attachments/20345615778460)

- Trage den Standort des Versandlagers ein, damit Steuern korrekt berechnet werden können.
- Falls du eine USt-Identprüfung bereits im Shop abgedeckt hast, kannst du den Auswahlschalter **USt-IdNr. automatisch als geprüft kennzeichnen** nach rechts stellen, um eine Doppelprüfung zu vermeiden.
- Wenn dein jährlicher EU-weite Gesamtumsatz unter 10.000 EUR liegt, kannst du aktivieren, um die Mehrwertsteuer im Land des Lagerstandortes zu entrichten. **Besteuerung abhängig vom Lagerstandardort machen **

- Wenn du ** Gesamtbetrag festsetzen **aktivierst, übernimmt Xentral des Gesamtbetrag aus dem Verkaufskanal und berechnet ihn nicht als Summe aus den Einzelpreisen. So werden Rundungsdifferenzen vermieden. Aktivierst du diese Schaltfläche, kannst du im nächsten Feld die ** maximale Differenz** zwischen den Beträgen in Verkaufskanal und Xentral definieren. Überschreitet die Differenz eines Auftrags die von dir festgelegte Grenze, so wird der Autoversand für diesen Auftrag deaktiviert und du kannst die notwendigen Korrekturen vornehmen.

#### Rabatte

![TB_Workflows_Auftrage_WahrungRabatte.png](https://help.xentral.com/hc/article_attachments/20345561045916)

- Weise einen **Rabatt**

-Artikel zu, auf den Gutschriften und Rabatte gebucht werden sollen.

#### Kommentare

Lege hier fest, wie Kommentare aus dem Shop-Beleg in Xentral übernommen werden sollen.

![Shared_Workflows_Auftrage_Kommentare.png](https://help.xentral.com/hc/article_attachments/19197941340188)

Unter “Kommentar aus Bestellung verarbeiten” stehen dir folgende Möglichkeiten zur Verfügung:

- “nicht beachten”: Kommentare werden nicht übernommen
- “in Freitext schreiben”: Kommentare werden in das Freitextfeld des Auftrags importiert
- “in interne Bezeichnung schreiben”: Kommentare werden in das Interne Bezeichnung Feld des Auftrags importiert

Setze den Auswahlschieber bei **Autoversand bei Kommentar stoppen?** nach rechts, wenn du verhindern möchtest, dass Aufträge mit Kommentar automatisch im Auto-Versand fortgeführt werden.

#### Kundenzuordnung

In den folgenden Feldern legst du fest, wie Kunden zwischen deinem Shop und Xentral verknüpft werden sollen. Wir unterscheiden zwischen im Shop angelegten Kunden und Gastkunden, die kein Konto angelegt haben.

![Shared_Workflows_Auftrage_Kundenzuordnung.png](https://help.xentral.com/hc/article_attachments/19197941341596)

- Für Kunden sowie für Kunden ohne Kundenkonto (Gastkunden) hast du folgende Optionen:
- Hast du bei mind. einem der beiden vorhergehenden Felder die Option “Kunde aus Bestellung auf einen bestehenden Kunden zuordnen” gewählt, legst du im Feld **Kundenzuordnung** fest, anhand welcher Kriterien die Zuordnung erfolgt, wobei die Prüfreihenfolge “Kundennummer” vor “Mail-Adresse” vor “Name & Adresse” ist.

- Bestimme schließlich im Feld **Wenn kein Kunde gefunden wird, dann:** wie verfahren werden soll, falls kein Kunde zugeordnet werden kann:
- Setze den Auswahlschieber bei **Bestehende Kunden nur innerhalb des Projektes zuordnen?** nach rechts, wenn du die Suche nach Kunden auf das Shopware6-spezifische Projekt in Xentral einschränken möchtest. Üblicherweise bleibt diese Schaltfläche deaktiviert.
- Hast du oben bei der Kundenanlage die Option “Jeden Kunden auf Default-Kunden schreiben” gewählt, trägst du schließlich im Feld “Default-Kunden auswählen” eine entsprechende Kundennummer ein.

#### Länderzuordnung

Verknüpfe in diesem Bereich die in Shopware genutzen Länder mit ihren Entsprechungen in Xentral. Dies stellt sicher, dass bei Verkauf in mehrere Länder das richtige Land im Auftrag eingetragen wird.

![connect_workflows_assigncountry.png](https://help.xentral.com/hc/article_attachments/15365093058844)

#### Sprachenzuordnung

In diesem Abschnitt kannst du festlegen, in welcher Sprache Belege ausgegeben werden sollen. Du kannst die Sprache aus dem Shop übernehmen oder eine manuelle Zuordnung hinterlegen.

![Shopify_Workflows_Auftrage_Sprachenzuordnung__1_.png](https://help.xentral.com/hc/article_attachments/19197941345692)

> **Wichtig**
>
> Stelle sicher, dass die Sprachen, die du verwenden möchtest, in der Xentral-Sprachenliste angelegt sind. Weitere Hinweise dazu findest duhier.

#### Positionen

Setze den Auftragsschalter nach rechts, wenn du in den Belegen die Artikelbezeichnung aus dem XentralArtikelstamm andrucken möchtest. Dies ist beispielsweise sinnvoll, wenn du im Shop andere Bezeichnungen (z. B. für SEO-Zwecke) verwendest, als du in der Auftragsabwicklung nutzen möchtest. Du kannst außerdem wählen, ob bzw. welche Artikelbeschreibung in den Auftragspositionen angezeigt werden soll:

![Shared_Workflows_Auftrage_Positionen.png](https://help.xentral.com/hc/article_attachments/19197941346972)

### Reiter “Auftragsstatus & Tracking”

#### Update Strategie

![SW6_Workflows_Auftragsstatus_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/23118295604380)

Im Feld “Auftragsstatus für Auftragsstatus & Tracking Export” hast du folgende Wahlmöglichkeiten:

![SW6_Workflows_Auftragsstatus_Updatestrategie_Details.png](https://help.xentral.com/hc/article_attachments/23118295606812)

> **Tipp**
>
> Wenn du nur Auftragsstatus-, aber keine Tracking-Informationen übertragen möchtest, so wähle **Sobald der Auftrag oder Teilauftrag abgeschlossen ist ** unddeaktiviere**Tracking Informationen zurückmelden**.

Setze den Schalter “Aufträge automatisch im Shop stornieren” nach rechts, wenn du Aufträge, die in Xentral storniert werden, auch im Shop stornieren möchtest.

#### Benachrichtigungen

Setze den Schalter nach rechts, wennShopwareeine Versandbenachrichtigung per Mail an den Kunden senden soll.

![Shared_Workflows_Auftragsstatus_Benachrichtigungen.png](https://help.xentral.com/hc/article_attachments/19197941348764)

### Reiter "Belege"

> **Anmerkung**
>
> Funktionserweiterung 02/2025: Falls du die Schnittstelle schon länger nutzt, kann es sein, dass du diesen Reiter noch nicht sehen kannst. Um ihn zu aktivieren, folge in Xentral dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware6-Connector > Einstellungen (Zahnrädchen)** und aktiviere dort das Feature "Belege".

In diesem Reiter kannst du einstellen, dass Belege aus Xentral als PDF an denShopexportiert werden. Um Rechnungs-Belege zu übertragen, aktiviere die Schaltfläche **Rechnungsdokumente automatisch als PDF übertragen ** und bei Bedarf die Option**Beleg in Shopware als "gesendet" markieren**:

![SW6_Workflows_Belege_Rechnungen.png](https://help.xentral.com/hc/article_attachments/21740319477276)

## Testphase und Produktivschaltung

### Testphase

Wenn du alle Einstellungen in den Workflows vorgenommen hast, solltest du die Anbindung ausgiebig testen.

Schränke die[Artikelzuordnung](https://help.xentral.com/hc/de/articles/14528034786588#UUID-cfece960-9538-6fea-fdc4-64d9bbdfe08f)auf wenige Artikel ein.

Nutze einige Testdaten und führe die Tests mit Hilfe der Funktionen im[Journal](https://help.xentral.com/hc/de/articles/14528034952476#UUID-0748de4e-37e4-85a3-21a3-6a2c51fcb42b)durch.

### Produktivschaltung

Sobald die Schnittstelle die Testdaten richtig und wie erwartet übergibt, kannst du mit der[Produktiv-Schaltung](https://help.xentral.com/hc/de/articles/18589763018012#UUID-51edb066-e697-e70b-6116-829fdd05e479)fortfahren.

**Viel Spaß mit deiner neuen Schnittstelle!**