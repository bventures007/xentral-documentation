ZusammenfassungOptimiere deinen Tradebyte-Connector in Xentral: Konfiguriere Workflows für Artikel, Bestände, Preise und Aufträge. Aktiviere Funktionen individuell für effiziente Prozesse.

## Überblick

Im Bereich Workflows kannst du nun die Details zu den gewählten Features konfigurieren und die Features einzeln aktiv schalten. Du erreichst die Workflows unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > Tradebyte > Workflows**.

![Shared_Workflows_Ubersicht.png](https://help.xentral.com/hc/article_attachments/20346775225756)

## Allgemeine Funktionen

### Integrationsmodus

Die Schaltfläche “Aktivsteht dir in jedem Reiter zur Verfügung. Sie bezieht sich jeweils auf den Reiter, in dem du dich gerade befindest.

> **Anmerkung**
>
> Diese Schaltfläche benötigst du erst, nachdem du alle Einstellungen vorgenommen und getestet hast und alles bereit ist für den produktiven Einsatz deiner Schnittstelle.
>
> **Belasse den Schalter bis zum Abschluss deiner Tests auf links (inaktiv).**

![TB_Workflows_AllgemeinSchaltflachen.png](https://help.xentral.com/hc/article_attachments/20346752347292)

### Achtung

Erst nachdem deine Einrichtung und Tests abgeschlossen sind, kannst du die Schnittstelle produktiv schalten. Beachte dazu die Hinweise in diesem[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/20346726922524#UUID-da47e695-24d4-715a-88a1-24755f9f7500).

## Features-Reiter

Im Folgenden findest du zu jedem Feature detaillierte Konfigurationsmöglichkeiten.

### Reiter “Artikel”

#### Datentypen

Lege fest, welche **Datentypen** zwischen den Systemen ausgetauscht werden sollen:

![TB_Workflows_Artikel_Datentypen.png](https://help.xentral.com/hc/article_attachments/20430355244188)

#### Stammdaten

![TB_Workflows_Artikel_Stammdaten.png](https://help.xentral.com/hc/article_attachments/21740241919388)

Um das Nettogewicht an den Shop zu übertragen, setze hier den Schalter nach rechts, andernfalls wird das Gewicht übertragen.

Wähle, ob die Artikel ID oder die Artikel Nr. als product number verwendet werden soll.

#### Steuern

Lege im folgenden Abschnitt die Steuereinstellungen fest:

![TB_Workflows_Artikel_Steuern.png](https://help.xentral.com/hc/article_attachments/20430366412572)

- “Steuersatz (normal)”: Trage hier den Prozentwert (ohne Prozentzeichen) für normal besteuerte Artikel ein. (In Deutschland derzeit 19%)
- “Steuersatz (ermäßigt)”: Trage hier den Prozentwert (ohne Prozentzeichen) für Artikel mit ermäßigtem Steuersatz ein. (In Deutschland derzeit 7%)
- “Land des Firmensitzes”: Wähle hier das Land aus, in dem deine Firma sitzt.

#### Keyword

Trage das Trennzeichen, durch das Keyword-Einträge separiert werden hier ein:

![TB_Workflows_Artikel_Keyword.png](https://help.xentral.com/hc/article_attachments/20430355246620)

### Reiter “Bestand”

#### Lager

“Auswahl Xentral Lager”: Hake hier die Xentral-Lagerorte an, aus denen die Bestände (summiert) an denMarktplatzgemeldet werden.

![OttoSW6Woo_Workflows_Bestand_Lagerzuordnung.png](https://help.xentral.com/hc/article_attachments/20346752348828)

> **Tipp**
>
> Wenn du einen neuen Lagerort angelegt hast, der im Auswahlfeld noch nicht zur Verfügung steht, klicke auf **Optionen neu laden**, um die Auswahl zu aktualisieren.

#### Lagerbestand berechnen

![Shared_Workflows_Bestand_Berechnen.png](https://help.xentral.com/hc/article_attachments/20346752350364)

Wähle folgende Optionen aus, um die an den Shop übertragene Bestandsmenge zu manipulieren:

- “Reservierungen beachten”: Setze den Schalter nach rechts, wenn die reservierte Menge vom Lagerbestand abgezogen werden soll.
- “Offene Bestellungen beachten”: Setze den Schalter nach rechts, wenn offene Auftragsmengen abgezogen werden sollen.
- “Lagerkorrekturwert beachten”: Setze den Schalter nach rechts, wenn der Lagerbestand um den im Artikel festgelegten Lagerkorrekturwert verändert werden soll. Das Feld “Lagerkorrekturwert” findest du unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.
- “Pseudo Lagerzahl statt echten Lagerzahlen verwenden”: Setze den Schalter nach rechts, wenn statt dem berechneten Lagerbestand eine im Artikelstamm festgelegte Pseudomenge übertragen werden soll. Das Feld **Pseudo Lagerzahl ** findest du ebenfalls unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.

### Reiter “Preise”

In diesem Reiter kannst du das Preisverhalten festlegen:

![connect_workflow_prices_woocommerce.png](https://help.xentral.com/hc/article_attachments/21740257701020)

“Kunde bzw. Kundengruppe”: Falls du für deinenMarktplatzeinen bestimmten Preis festlegen möchtest, kannst du in diesem Feld einen Kundennamen oder einen Kundengruppennamen eintragen. Möchtest du Standardpreise nutzen, lasse das Feld leer.

Um mögliche Rundungsdifferenzen zu vermeiden, kannst du den Schalter “Preise vor der Übertragung in den Shop vorrunden?” nach rechts setzen.

### Reiter “Aufträge”

Der Reiter Aufträge ist das Kernstück der Workflow-Konfiguration. Hier legst du unter anderem fest, ab welchem Zahlungsstatus Bestellungen aus demMarktplatzzu Xentral importiert werden und wie Zahlungen gehandhabt werden, wie Lieferbedingungen verknüpft werden, auf welche Artikelnummern Versandgebühren und Rabatte gebucht werden, wie mit Kommentaren verfahren werden soll und wie Kunden angelegt und zugeordnet werden.

#### Update Strategie

Trage ein, welcher Name als Bearbeiter in die importierten Aufträge eingetragen werden soll:

#### Zahlungsarten / Zahlungsweisen / Zahlungsbedingungen

![TB_Workflows_Auftrage_Zahlungsarten.png](https://help.xentral.com/hc/article_attachments/21740241926556)

Hinterlege bei der **Standardzahlungsart** eine Zahlungsweise, die verwendet werden soll, falls keine Zahlungsweise vom Shop übergeben wird.

Wenn du den Schalter **Standardzahlungsart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Zahlungsart im Shop gezogen, sondern auch, wenn gar keine Zahlungsart zugeordnet ist.

Verknüpfe bei Bedarf weitere Zahlungsweisen, in dem du auf **+ Gruppe hinzufügen** klickst.

Du kannst außerdem Zahlungsarten auswählen, für die kein Autoversand gelten soll. Solche Aufträge werden importiert und können im weiteren Verlauf manuell in den Versand gegeben werden.

> **Anmerkung**
>
> Tippe die Zahlungsarten exakt so ein, wie sie im Marktplatz angelegt sind. Die Angabe findest du im Portal unter den Einstellungen.

#### Versandarten & Lieferbedingungen

![TB_Workflows_Auftrage_Versandarten.png](https://help.xentral.com/hc/article_attachments/21740257707036)

- Hinterlege bei **Welche Lieferbedingungen sollen für den Bestellimport für diesen Onlineshop gelten?** eine feste Lieferbedingung, die bei importierten Belegen eingetragen wird. Möchtest du keine Lieferbedingungen nutzen, kannst du das Feld leer lassen.
- Hinterlege bei der **Standardversandart** eine Versandart, die verwendet werden soll, falls keine Versandart vom Shop übergeben wird.
- Wenn du den Schalter **Standardversandart auch bei fehlender Zuordnung verwenden** aktivierst, wird diese nicht nur bei fehlenden Informationen zur Versandart im Shop gezogen, sondern auch, wenn gar keine Versandart zugeordnet ist.
- Verknüpfe bei Bedarf weitere Versandarten, in dem Du auf **+ Gruppe hinzufügen** klickst.
- **Fast-Lane Versandarten**: Falls du deinen Kunden Express-Versandarten anbieten möchtest, kannst du auf dieses Feld klicken und dort die zutreffenden Versandarten anhaken.
- **Belege im Autoversand erstellen **: Wähle hier, welche Belege im Autoversand erstellt werden sollen. Die Option ** Nur Rechnung** bietet sich z. B. an, wenn du einen Abholprozess abbilden möchtest.

#### Versandkosten

![TB_Workflows_Auftrage_Versandkosten.png](https://help.xentral.com/hc/article_attachments/20346775233436)

- Ordne unter **Artikelnummer für Versandkosten** den Porto-Artikel zu, auf den Versandgebühren geschrieben werden sollen.

#### Steuern

![TB_Workflows_Auftrage_Steuern.png](https://help.xentral.com/hc/article_attachments/20346775234204)

- Trage den Standort des Versandlagers ein, damit Steuern korrekt berechnet werden können.
- Wähle unter **Umsatzsteuerberechnung für Nebenleistungen** die Option, die du in deiner TB.One Plattform unter Admin > Systemeinstellungen > Auftragsabwicklung hinsichtlich der Handhabung der Umsatzsteuer auf Nebenleistungen eingestellt hast.
- Falls du eine USt-Identprüfung bereits im Shop abgedeckt hast, kannst du den Auswahlschalter **USt-IdNr. automatisch als geprüft kennzeichnen** nach rechts stellen, um eine Doppelprüfung zu vermeiden.
- Wenn dein jährlicher EU-weite Gesamtumsatz unter 10.000 EUR liegt, kannst du aktivieren, um die Mehrwertsteuer im Land des Lagerstandortes zu entrichten. **Besteuerung abhängig vom Lagerstandardort machen **

- Wenn du ** Gesamtbetrag festsetzen **aktivierst, übernimmt Xentral des Gesamtbetrag aus dem Verkaufskanal und berechnet ihn nicht als Summe aus den Einzelpreisen. So werden Rundungsdifferenzen vermieden. Aktivierst du diese Schaltfläche, kannst du im nächsten Feld die ** maximale Differenz** zwischen den Beträgen in Verkaufskanal und Xentral definieren. Überschreitet die Differenz eines Auftrags die von dir festgelegte Grenze, so wird der Autoversand für diesen Auftrag deaktiviert und du kannst die notwendigen Korrekturen vornehmen.

#### Währung und Rabatte

![TB_Workflows_Auftrage_WahrungRabatte.png](https://help.xentral.com/hc/article_attachments/20346775234844)

- Träge deine Standard-**Währung** ein.
- Weise einen **Rabatt**

-Artikel zu, auf den Gutschriften und Rabatte gebucht werden sollen.

#### Zuschläge

![WooCommerce_Workflows_Auftrage_Zuschlage.png](https://help.xentral.com/hc/article_attachments/20346775235356)

- Trage eine Artikelnummer ein, auf die Zuschläge gebucht werden sollen. Wenn du z. B. unterhalb eines bestimmten Gesamtrechnungsbetrages einen Mindermengenzuschlag erheben möchtest, kannst du hierfür eine Artikelnummer anlegen (Artikel ist “Kein Lagerartikel”) und sie hier verknüpfen. Sobald ein Auftrag unterhalb des Mindestbetrags liegt, wird der entsprechende Mindermengenzuschlag auf diese Artikelnummer erfasst.

#### Projektzuordnung

![TB_Workflows_Auftrage_Projektzuordnung.png](https://help.xentral.com/hc/article_attachments/20346752355740)

Wähle ein **Standardprojekt**, das standardmäßig in die importierten Aufträge eingefügt wird.

Sofern du unterschiedliche Vertriebskanäle in deinem Shop angelegt hast, kannst du sie unter **Sales Channel > Projekt Zuordnung** mit den dazugehörigen Xentral-Projekten verknüpfen

#### Kommentare

Lege hier fest, wie Kommentare aus dem Shop-Beleg in Xentral übernommen werden sollen.

![Shared_Workflows_Auftrage_Kommentare.png](https://help.xentral.com/hc/article_attachments/20346775235996)

Unter “Kommentar aus Bestellung verarbeiten” stehen dir folgende Möglichkeiten zur Verfügung:

- “nicht beachten”: Kommentare werden nicht übernommen
- “in Freitext schreiben”: Kommentare werden in das Freitextfeld des Auftrags importiert
- “in interne Bezeichnung schreiben”: Kommentare werden in das Interne Bezeichnung Feld des Auftrags importiert

Setze den Auswahlschieber bei **Autoversand bei Kommentar stoppen?** nach rechts, wenn du verhindern möchtest, dass Aufträge mit Kommentar automatisch im Auto-Versand fortgeführt werden.

#### Kundenzuordnung

In den folgenden Feldern legst du fest, wie Kunden zwischen deinem Shop und Xentral verknüpft werden sollen. Wir unterscheiden zwischen im Shop angelegten Kunden und Gastkunden, die kein Konto angelegt haben.

![Shared_Workflows_Auftrage_Kundenzuordnung.png](https://help.xentral.com/hc/article_attachments/20346752356124)

- Für Kunden sowie für Kunden ohne Kundenkonto (Gastkunden) hast du folgende Optionen:
- Hast du bei mind. einem der beiden vorhergehenden Felder die Option “Kunde aus Bestellung auf einen bestehenden Kunden zuordnen” gewählt, legst du im Feld **Kundenzuordnung** fest, anhand welcher Kriterien die Zuordnung erfolgt, wobei die Prüfreihenfolge “Kundennummer” vor “Mail-Adresse” vor “Name & Adresse” ist.

- Bestimme schließlich im Feld **Wenn kein Kunde gefunden wird, dann:** wie verfahren werden soll, falls kein Kunde zugeordnet werden kann:
- Setze den Auswahlschieber bei **Bestehende Kunden nur innerhalb des Projektes zuordnen?** nach rechts, wenn du die Suche nach Kunden auf das -spezifische Projekt in Xentral einschränken möchtest. Üblicherweise bleibt diese Schaltfläche deaktiviert.
- Hast du oben bei der Kundenanlage die Option “Jeden Kunden auf Default-Kunden schreiben” gewählt, trägst du schließlich im Feld “Default-Kunden auswählen” eine entsprechende Kundennummer ein.

#### Positionen

Setze den Auftragsschalter nach rechts, wenn du in den Belegen die Artikelbezeichnung aus dem XentralArtikelstamm andrucken möchtest. Dies ist beispielsweise sinnvoll, wenn du im Shop andere Bezeichnungen (z. B. für SEO-Zwecke) verwendest, als du in der Auftragsabwicklung nutzen möchtest. Du kannst außerdem wählen, ob bzw. welche Artikelbeschreibung in den Auftragspositionen angezeigt werden soll:

![Shared_Workflows_Auftrage_Positionen.png](https://help.xentral.com/hc/article_attachments/20346752357660)

### Reiter “Auftragsstatus & Tracking”

#### Update Strategie

![connect_workflows_auftragsstatus_update_otto.png](https://help.xentral.com/hc/article_attachments/20346775241116)

Setze den Schalter “Aufträge automatisch im Shop stornieren” nach rechts, wenn du Aufträge, die in Xentral storniert werden, auch im Marktplatz stornieren möchtest. Dies hat nur Auswirkungen auf noch nicht versendete Aufträge.

#### Versanddienstleister-Zuordnung

Klicke auf **+ Gruppe hinzufügen**, um die Pakettypen von Tradebyte mit den Versandarten in Xentral zu verknüpfen.

![TB_Workflows_Auftragsstatus_Versanddienstleister.png](https://help.xentral.com/hc/article_attachments/21740241933084)

## Testphase und Produktivschaltung

### Testphase

Wenn du alle Einstellungen in den Workflows vorgenommen hast, solltest du die Anbindung ausgiebig testen.

Schränke die[Artikelzuordnung](https://help.xentral.com/hc/de/articles/20346718496156#UUID-71d16cd8-aed2-e377-65d6-acb76c1171c2)auf wenige Artikel ein.

Nutze einige Testdaten und führe die Tests mit Hilfe der Funktionen im[Journal](https://help.xentral.com/hc/de/articles/20346726988060#UUID-6bb90a04-de32-e4b8-4290-85677e0c9b29)durch.

### Produktivschaltung

Sobald die Schnittstelle die Testdaten richtig und wie erwartet übergibt, kannst du mit der[Produktiv-Schaltung](https://help.xentral.com/hc/de/articles/20346726922524#UUID-da47e695-24d4-715a-88a1-24755f9f7500)fortfahren.

**Viel Spaß mit deiner neuen Schnittstelle!**