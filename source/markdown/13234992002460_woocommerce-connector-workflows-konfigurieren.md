## Überblick

Im Bereich Workflows kannst du nun die Details zu den gewählten Features konfigurieren und die Features einzeln aktiv schalten. Du erreichst die Workflows unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > WooCommerce-Connector > Workflows**.

![Shared_Workflows_Ubersicht.png](https://help.xentral.com/hc/article_attachments/18670869393308)

## Allgemeine Funktionen

### Integrationsmodus

Die Schaltfläche “Aktivsteht dir in jedem Reiter zur Verfügung. Sie bezieht sich jeweils auf den Reiter, in dem du dich gerade befindest.

> **Anmerkung**
>
> Diese Schaltfläche benötigst du erst, nachdem du alle Einstellungen vorgenommen und getestet hast und alles bereit ist für den produktiven Einsatz deiner Schnittstelle.
>
> **Belasse den Schalter bis zum Abschluss deiner Tests auf links (inaktiv).**

![ShopifyShopwareWoo_Workflows_Allgemein_Integrationsmodus.png](https://help.xentral.com/hc/article_attachments/18670869395356)

### Achtung

Erst nachdem deine Einrichtung und Tests abgeschlossen sind, kannst du die Schnittstelle produktiv schalten. Beachte dazu die Hinweise in diesem[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/18589740730012#UUID-3482c0db-0cbb-26a5-6a44-9a82f4cfb81a).

## Features-Reiter

Im Folgenden findest du zu jedem Feature detaillierte Konfigurationsmöglichkeiten.

### Reiter “Artikel”

#### Datentypen

Lege fest, welche **Datentypen** zwischen den Systemen ausgetauscht werden sollen:

![Connect_datatype_WooCommerce.png](https://help.xentral.com/hc/article_attachments/15365043289372)

#### Meta Texte

Stelle sicher, dass du das Yoast Plugin implementiert hast.Setze den Schalter nach rechts, wenn du Metatexte an den Shop übertragen möchtest.

### Achtung

Für die Übertragung der Meta Texte benötigst du das Yoast Plugin.

![WooCommerce_Workflows_Artikel_Metatexte.png](https://help.xentral.com/hc/article_attachments/18670893945756)

#### Stammdaten

![Shared_Workflows_Artikel_Stammdaten.png](https://help.xentral.com/hc/article_attachments/18670893946268)

Um das Nettogewicht an den Shop zu übertragen, setze hier den Schalter nach rechts, andernfalls wird das Gewicht übertragen.

#### Update Strategie

Bestimme, wie Artikel von Xentral an den Shop übertragen werden sollen:

![Shared_Workflows_Artikel_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/18670869399324)

Bei der Update Strategie hast du folgende Möglichkeiten:

![Shared_Workflows_Artikel_UpdatestrategieDetails.png](https://help.xentral.com/hc/article_attachments/18670869401500)

Wenn Artikel, die du in Xentral löschst, automatisch im Shop gelöscht werden sollen, setze den Auswahlschalter “Produkte automatisch in Shop löschen?” nach rechts.

> **Anmerkung**
>
> Wird ein Matrixartikel gelöscht, werden alle zugehörigen Varianten im Shop gelöscht.

#### Steuern

Lege im folgenden Abschnitt die Steuereinstellungen fest:

![connect_taxes_woocommerce.png](https://help.xentral.com/hc/article_attachments/15365058940700)

- “Steuersatz (normal)”: Trage hier den Prozentwert (ohne Prozentzeichen) für normal besteuerte Artikel ein. (In Deutschland derzeit 19%)
- “Steuersatz (ermäßigt)”: Trage hier den Prozentwert (ohne Prozentzeichen) für Artikel mit ermäßigtem Steuersatz ein. (In Deutschland derzeit 7%)
- “Nettopreise übertragen”: Stelle den Schalter nach rechts, wenn du im Shop Nettopreise gepflegt hast, oder auf links für Bruttopreise.
- “Land des Firmensitzes”: Wähle hier das Land aus, in dem deine Firma sitzt.

#### Eigenschaften

Setze den Schalter nach rechts, wenn du Eigenschaften auf der Produktseite unter den zusätzlichen Informationen anzeigen lassen möchtest.

![connect_properties_woocommerce.png](https://help.xentral.com/hc/article_attachments/15365072715420)

### Reiter “Kategorie”

Setze die Schaltfläche nach rechts (aktiv), wenn du Kategorien, die du in Xentrallöschst, automatisch auch im Shop entfernt haben möchtest. Wird eine Kategorie mit Unterkategorien gelöscht, werden diese ebenfalls entfernt.

![Shared_Workflows_Kategorie_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/18670869403804)

Hier kannst du wählen, welche Artikelbaum-Kategorie standardmäßig zugeordnet werden soll:

![Shopware_Workflows_Kategorie_Kategoriezuordnung.png](https://help.xentral.com/hc/article_attachments/18670893956636)

> **Tipp**
>
> Wenn du eine neue Kategorie angelegt hast, die im Auswahlfeld noch nicht zur Verfügung steht, klicke auf **Optionen neu laden**, um die Auswahl zu aktualisieren.

### Reiter “Bestand”

#### Lager

“Auswahl Xentral Lager”: Hake hier die Xentral-Lagerorte an, aus denen die Bestände (summiert) an denShopgemeldet werden.

![OttoSW6Woo_Workflows_Bestand_Lagerzuordnung.png](https://help.xentral.com/hc/article_attachments/18670869406236)

> **Tipp**
>
> Wenn du einen neuen Lagerort angelegt hast, der im Auswahlfeld noch nicht zur Verfügung steht, klicke auf **Optionen neu laden**, um die Auswahl zu aktualisieren.

#### Lagerbestand berechnen

![Shared_Workflows_Bestand_Berechnen.png](https://help.xentral.com/hc/article_attachments/18670893962908)

Wähle folgende Optionen aus, um die an den Shop übertragene Bestandsmenge zu manipulieren:

- “Reservierungen beachten”: Setze den Schalter nach rechts, wenn die reservierte Menge vom Lagerbestand abgezogen werden soll.
- “Offene Bestellungen beachten”: Setze den Schalter nach rechts, wenn offene Auftragsmengen abgezogen werden sollen.
- “Lagerkorrekturwert beachten”: Setze den Schalter nach rechts, wenn der Lagerbestand um den im Artikel festgelegten Lagerkorrekturwert verändert werden soll. Das Feld “Lagerkorrekturwert” findest du unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.
- “Pseudo Lagerzahl statt echten Lagerzahlen verwenden”: Setze den Schalter nach rechts, wenn statt dem berechneten Lagerbestand eine im Artikelstamm festgelegte Pseudomenge übertragen werden soll. Das Feld **Pseudo Lagerzahl ** findest du ebenfalls unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.

### Reiter “Preise”

In diesem Reiter kannst du das Preisverhalten festlegen:

![connect_workflow_prices_woocommerce.png](https://help.xentral.com/hc/article_attachments/15365104517404)

“Kunde bzw. Kundengruppe”: Falls du für deinenShopeinen bestimmten Preis festlegen möchtest, kannst du in diesem Feld einen Kundennamen oder einen Kundengruppennamen eintragen. Möchtest du Standardpreise nutzen, lasse das Feld leer.

Um mögliche Rundungsdifferenzen zu vermeiden, kannst du den Schalter “Preise vor der Übertragung in den Shop vorrunden?” nach rechts setzen.

### Reiter “Aufträge”

Der Reiter Aufträge ist das Kernstück der Workflow-Konfiguration. Hier legst du unter anderem fest, ab welchem Zahlungsstatus Bestellungen aus demShopzu Xentral importiert werden und wie Zahlungen gehandhabt werden, wie Lieferbedingungen verknüpft werden, auf welche Artikelnummern Versandgebühren und Rabatte gebucht werden, wie mit Kommentaren verfahren werden soll und wie Kunden angelegt und zugeordnet werden.

#### Update Strategie

Bestimme, welche Zahlungsstatus als Auslöser für den Import aus dem Shop dienen sollen und (optional) welcher Name als Bearbeiter in die importierten Aufträge eingetragen werden soll. Beim Zahlungsstatus ist es möglich, neben den vordefinierten eigene Status anzulegen. Tippe dazu einfach einen eigenen Status (hier z. B. "checked") in das Feld ein und bestätige mit der Enter-Taste.

![WooCommerce_Workflows_Auftrage_Updatestrategie_EigeneEintippen.png](https://help.xentral.com/hc/article_attachments/18670893963548)

Du siehst dann die vordefinierten Status zur Auswahl und die eigenen daneben:

![WooCommerce_Workflows_Auftrage_Updatestrategie_Eigene.png](https://help.xentral.com/hc/article_attachments/18670869409820)

#### Zahlungsarten / Zahlungsweisen / Zahlungsbedingungen

![WooCommerce_Workflows_Auftrage_Zahlungsarten.png](https://help.xentral.com/hc/article_attachments/21740241987100)

Hinterlege bei der **Standardzahlungsart** eine Zahlungsweise, die verwendet werden soll, falls keine Zahlungsweise vom Shop übergeben wird.

Wenn du den Schalter **Standardzahlungsart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Zahlungsart im Shop gezogen, sondern auch, wenn gar keine Zahlungsart zugeordnet ist.

Verknüpfe bei Bedarf weitere Zahlungsweisen, in dem du auf **+ Gruppe hinzufügen** klickst.

Du kannst außerdem Zahlungsarten auswählen, für die kein Autoversand gelten soll. Solche Aufträge werden importiert und können im weiteren Verlauf manuell in den Versand gegeben werden.

#### Versandarten & Lieferbedingungen

![WooCommerce_Workflows_Auftrage_Versandarten.png](https://help.xentral.com/hc/article_attachments/21740241989020)

- Hinterlege bei **Welche Lieferbedingungen sollen für den Bestellimport für diesen Onlineshop gelten?** eine feste Lieferbedingung, die bei importierten Belegen eingetragen wird. Möchtest du keine Lieferbedingungen nutzen, kannst du das Feld leer lassen.
- Hinterlege bei der **Standardversandart** eine Versandart, die verwendet werden soll, falls keine Versandart vom Shop übergeben wird.
- Wenn du den Schalter **Standardversandart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Versandart im Shop gezogen, sondern auch, wenn gar keine Versandart zugeordnet ist.
- Verknüpfe bei Bedarf weitere Versandarten, in dem Du auf **+ Gruppe hinzufügen** klickst.
- **Fast-Lane Versandarten**: Falls du deinen Kunden Express-Versandarten anbieten möchtest, kannst du auf dieses Feld klicken und dort die zutreffenden Versandarten anhaken.
- **Belege im Autoversand erstellen **: Wähle hier, welche Belege im Autoversand erstellt werden sollen. Die Option ** Nur Rechnung** bietet sich z. B. an, wenn du einen Abholprozess abbilden möchtest.

#### Versandkosten

![TB_Workflows_Auftrage_Versandkosten.png](https://help.xentral.com/hc/article_attachments/20345585882908)

- Ordne unter **Artikelnummer für Versandkosten** den Porto-Artikel zu, auf den Versandgebühren geschrieben werden sollen.

#### Steuern

![WooCommerce_Workflows_Auftrage_Steuern.png](https://help.xentral.com/hc/article_attachments/20345585884188)

- Trage den Standort des Versandlagers ein, damit Steuern korrekt berechnet werden können.
- Falls du eine USt-Identprüfung bereits im Shop abgedeckt hast, kannst du den Auswahlschalter **USt-IdNr. automatisch als geprüft kennzeichnen** nach rechts stellen, um eine Doppelprüfung zu vermeiden.
- Falls deine Kunden im Shop Netto-Preise sehen, kannst du **Kalkulation auf Basis von Netto Preisen** aktivieren, um Rundungsdifferenzen zu vermeiden.
- Wenn dein jährlicher EU-weite Gesamtumsatz unter 10.000 EUR liegt, kannst du aktivieren, um die Mehrwertsteuer im Land des Lagerstandortes zu entrichten. **Besteuerung abhängig vom Lagerstandardort machen **

- Wenn du ** Gesamtbetrag festsetzen **aktivierst, übernimmt Xentral des Gesamtbetrag aus dem Verkaufskanal und berechnet ihn nicht als Summe aus den Einzelpreisen. So werden Rundungsdifferenzen vermieden. Aktivierst du diese Schaltfläche, kannst du im nächsten Feld die ** maximale Differenz** zwischen den Beträgen in Verkaufskanal und Xentral definieren. Überschreitet die Differenz eines Auftrags die von dir festgelegte Grenze, so wird der Autoversand für diesen Auftrag deaktiviert und du kannst die notwendigen Korrekturen vornehmen.

#### Rabatte

![TB_Workflows_Auftrage_WahrungRabatte.png](https://help.xentral.com/hc/article_attachments/20345616118940)

- Weise einen **Rabatt**

-Artikel zu, auf den Gutschriften und Rabatte gebucht werden sollen.

#### Zuschläge

![WooCommerce_Workflows_Auftrage_Zuschlage.png](https://help.xentral.com/hc/article_attachments/18670869417372)

- Trage eine Artikelnummer ein, auf die Zuschläge gebucht werden sollen. Wenn du z. B. unterhalb eines bestimmten Gesamtrechnungsbetrages einen Mindermengenzuschlag erheben möchtest, kannst du hierfür eine Artikelnummer anlegen (Artikel ist “Kein Lagerartikel”) und sie hier verknüpfen. Sobald ein Auftrag unterhalb des Mindestbetrags liegt, wird der entsprechende Mindermengenzuschlag auf diese Artikelnummer erfasst.

#### Kommentare

Lege hier fest, wie Kommentare aus dem Shop-Beleg in Xentral übernommen werden sollen.

![Shared_Workflows_Auftrage_Kommentare.png](https://help.xentral.com/hc/article_attachments/18670869417756)

Unter “Kommentar aus Bestellung verarbeiten” stehen dir folgende Möglichkeiten zur Verfügung:

- “nicht beachten”: Kommentare werden nicht übernommen
- “in Freitext schreiben”: Kommentare werden in das Freitextfeld des Auftrags importiert
- “in interne Bezeichnung schreiben”: Kommentare werden in das Interne Bezeichnung Feld des Auftrags importiert

Setze den Auswahlschieber bei **Autoversand bei Kommentar stoppen?** nach rechts, wenn du verhindern möchtest, dass Aufträge mit Kommentar automatisch im Auto-Versand fortgeführt werden.

#### Kundenzuordnung

In den folgenden Feldern legst du fest, wie Kunden zwischen deinem Shop und Xentral verknüpft werden sollen. Wir unterscheiden zwischen im Shop angelegten Kunden und Gastkunden, die kein Konto angelegt haben.

![Shared_Workflows_Auftrage_Kundenzuordnung.png](https://help.xentral.com/hc/article_attachments/18670893976092)

- Für Kunden sowie für Kunden ohne Kundenkonto (Gastkunden) hast du folgende Optionen:
- Hast du bei mind. einem der beiden vorhergehenden Felder die Option “Kunde aus Bestellung auf einen bestehenden Kunden zuordnen” gewählt, legst du im Feld **Kundenzuordnung** fest, anhand welcher Kriterien die Zuordnung erfolgt, wobei die Prüfreihenfolge “Kundennummer” vor “Mail-Adresse” vor “Name & Adresse” ist.

- Bestimme schließlich im Feld **Wenn kein Kunde gefunden wird, dann:** wie verfahren werden soll, falls kein Kunde zugeordnet werden kann:
- Setze den Auswahlschieber bei **Bestehende Kunden nur innerhalb des Projektes zuordnen?** nach rechts, wenn du die Suche nach Kunden auf das WooCommerce-spezifische Projekt in Xentral einschränken möchtest. Üblicherweise bleibt diese Schaltfläche deaktiviert.
- Hast du oben bei der Kundenanlage die Option “Jeden Kunden auf Default-Kunden schreiben” gewählt, trägst du schließlich im Feld “Default-Kunden auswählen” eine entsprechende Kundennummer ein.

#### Projekt

![connect_project_woocommerce.png](https://help.xentral.com/hc/article_attachments/15365578739996)

Wähle ein **Standardprojekt**, das standardmäßig in die importierten Aufträge eingefügt wird.

#### Positionen

Setze den Auftragsschalter nach rechts, wenn du in den Belegen die Artikelbezeichnung aus dem XentralArtikelstamm andrucken möchtest. Dies ist beispielsweise sinnvoll, wenn du im Shop andere Bezeichnungen (z. B. für SEO-Zwecke) verwendest, als du in der Auftragsabwicklung nutzen möchtest. Du kannst außerdem wählen, ob bzw. welche Artikelbeschreibung in den Auftragspositionen angezeigt werden soll:

![Shared_Workflows_Auftrage_Positionen.png](https://help.xentral.com/hc/article_attachments/18670893980572)

### Reiter “Auftragsstatus & Tracking”

#### Update Strategie

![WooCommerce_Workflows_Auftragsstatus_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/22662259274524)

Wenn du das WooCommerce PlugIn "Shipment Tracking" benutzt und Tracking Informationen direkt von Xentral an WooCommerce übertragen möchtest, aktiviere **Tracking Informationen zurückmelden **. Aktiviere ** Aufträge automatisch im Shop stornieren**, wenn du Aufträge, die in Xentral storniert werden, auch im Shop stornieren möchtest.

## Testphase und Produktivschaltung

### Testphase

Wenn du alle Einstellungen in den Workflows vorgenommen hast, solltest du die Anbindung ausgiebig testen.

Schränke die[Artikelzuordnung](https://help.xentral.com/hc/de/articles/13235023557532#UUID-2e1a76ae-2150-3aca-98cf-7f80d6c6f0b7)auf wenige Artikel ein.

Nutze einige Testdaten und führe die Tests mit Hilfe der Funktionen im[Journal](https://help.xentral.com/hc/de/articles/13921840987036#UUID-24f64971-99da-b968-5ba9-ff6a97dfabb5)durch.

### Produktivschaltung

Sobald die Schnittstelle die Testdaten richtig und wie erwartet übergibt, kannst du mit der[Produktiv-Schaltung](https://help.xentral.com/hc/de/articles/18589740730012#UUID-3482c0db-0cbb-26a5-6a44-9a82f4cfb81a)fortfahren.

**Viel Spaß mit deiner neuen Schnittstelle!**