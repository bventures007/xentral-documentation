## Überblick

Im Bereich Workflows kannst du nun die Details zu den gewählten Features konfigurieren und die Features einzeln aktiv schalten. Du erreichst die Workflows unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > OTTO > Workflows**.

![connect_artikelzuordnung_weiter-zu-workflows.png](https://help.xentral.com/hc/article_attachments/20880693772572)

## Allgemeine Funktionen

### Integrationsmodus

Die Schaltfläche “Aktivsteht dir in jedem Reiter zur Verfügung. Sie bezieht sich jeweils auf den Reiter, in dem du dich gerade befindest.

> **Anmerkung**
>
> Diese Schaltfläche benötigst du erst, nachdem du alle Einstellungen vorgenommen und getestet hast und alles bereit ist für den produktiven Einsatz deiner Schnittstelle.
>
> **Belasse den Schalter bis zum Abschluss deiner Tests auf links (inaktiv).**

![Otto__Workflows__Allgemein__Integrationsmodus__png.png](https://help.xentral.com/hc/article_attachments/20957207420828)

### Achtung

Erst nachdem deine Einrichtung und Tests abgeschlossen sind, kannst du die Schnittstelle produktiv schalten. Beachte dazu die Hinweise in diesem[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/18589740879132#UUID-76f3afac-0b29-56cb-47ca-10af39e437d6).

## Features-Reiter

Im Folgenden findest du zu jedem Feature detaillierte Konfigurationsmöglichkeiten.

### Reiter “Bestand”

#### Lager

“Auswahl Xentral Lager”: Hake hier die Xentral-Lagerorte an, aus denen die Bestände (summiert) an denMarktplatzgemeldet werden.

![OttoSW6Woo_Workflows_Bestand_Lagerzuordnung.png](https://help.xentral.com/hc/article_attachments/19113152314396)

> **Tipp**
>
> Wenn du einen neuen Lagerort angelegt hast, der im Auswahlfeld noch nicht zur Verfügung steht, klicke auf **Optionen neu laden**, um die Auswahl zu aktualisieren.

#### Lagerbestand berechnen

![Shared_Workflows_Bestand_Berechnen.png](https://help.xentral.com/hc/article_attachments/19113152315676)

Wähle folgende Optionen aus, um die an den Shop übertragene Bestandsmenge zu manipulieren:

- “Reservierungen beachten”: Setze den Schalter nach rechts, wenn die reservierte Menge vom Lagerbestand abgezogen werden soll.
- “Offene Bestellungen beachten”: Setze den Schalter nach rechts, wenn offene Auftragsmengen abgezogen werden sollen.
- “Lagerkorrekturwert beachten”: Setze den Schalter nach rechts, wenn der Lagerbestand um den im Artikel festgelegten Lagerkorrekturwert verändert werden soll. Das Feld “Lagerkorrekturwert” findest du unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.
- “Pseudo Lagerzahl statt echten Lagerzahlen verwenden”: Setze den Schalter nach rechts, wenn statt dem berechneten Lagerbestand eine im Artikelstamm festgelegte Pseudomenge übertragen werden soll. Das Feld **Pseudo Lagerzahl ** findest du ebenfalls unter **Artikel > Details > Online-Shop Optionen **, Bereich ** Lagerbestand**.

### Reiter “Aufträge”

Der Reiter Aufträge ist das Kernstück der Workflow-Konfiguration. Hier legst du unter anderem fest, wie Lieferbedingungen verknüpft werden, auf welche Artikelnummern Versandgebühren und Rabatte gebucht werden, wie mit Kommentaren verfahren werden soll und wie Kunden angelegt und zugeordnet werden.

#### Update Strategie

Trage ein, welcher Name als Bearbeiter in die importierten Aufträge eingetragen werden soll:

![Otto_Workflows_Auftrage_Updatestrategie.png](https://help.xentral.com/hc/article_attachments/19113137537692)

#### Versandkosten

![TB_Workflows_Auftrage_Versandkosten.png](https://help.xentral.com/hc/article_attachments/20345630245916)

- Ordne unter **Artikelnummer für Versandkosten** den Porto-Artikel zu, auf den Versandgebühren geschrieben werden sollen.

#### Steuern

![OTTO_Workflows_Auftrage_Steuern.png](https://help.xentral.com/hc/article_attachments/20345604358684)

- Falls du eine USt-Identprüfung bereits im Shop abgedeckt hast, kannst du den Auswahlschalter **USt-IdNr. automatisch als geprüft kennzeichnen** nach rechts stellen, um eine Doppelprüfung zu vermeiden.
- Wenn dein jährlicher EU-weite Gesamtumsatz unter 10.000 EUR liegt, kannst du aktivieren, um die Mehrwertsteuer im Land des Lagerstandortes zu entrichten. **Besteuerung abhängig vom Lagerstandardort machen **

- Wenn du ** Gesamtbetrag festsetzen **aktivierst, übernimmt Xentral des Gesamtbetrag aus dem Verkaufskanal und berechnet ihn nicht als Summe aus den Einzelpreisen. So werden Rundungsdifferenzen vermieden. Aktivierst du diese Schaltfläche, kannst du im nächsten Feld die ** maximale Differenz** zwischen den Beträgen in Verkaufskanal und Xentral definieren. Überschreitet die Differenz eines Auftrags die von dir festgelegte Grenze, so wird der Autoversand für diesen Auftrag deaktiviert und du kannst die notwendigen Korrekturen vornehmen.

#### Rabatte

![TB_Workflows_Auftrage_WahrungRabatte.png](https://help.xentral.com/hc/article_attachments/20345604359196)

- Weise einen **Rabatt**

-Artikel zu, auf den Gutschriften und Rabatte gebucht werden sollen.

#### Auftragspositionen

![Otto_Workflows_Auftrage_Auftragspositionen.png](https://help.xentral.com/hc/article_attachments/19113152322204)

- Standardmäßig wird eine Bestellzeile im Marktplatz, die mehr als 1 Stück eines Artikels enthält, in mehrere Auftragszeilen mit jeweils 1 Stück aufgeteilt. Um das zu vermeiden, empfehlen wir, diese Schaltfläche zu aktivieren. So wird nur eine Auftragszeile mit der gesamten Artikelmenge erstellt.

#### Zahlungsarten

- Hinterlege bei der “Standardzahlungsart” eine Zahlungsweise, die verwendet werden soll, falls keine Zahlungsweise vom Marktplatz übergeben wird.
- Hinterlege unter “Zahlungsarten Zuordnung” die Beziehung der OTTO-Zahlungsweisen zu Xentral-Zahlungsarten. Du kannst mehrere OTTO-Zahlungsweisen mit einer Xentral-Zahlungsart verknüpfen oder jeweils eigene Xentral-Zahlungsarten verwenden. Wichtig ist hierbei, dass du die Schreibweise von OTTO korrekt übernimmst. Folgende Zahlungsweisen stehen zur Verfügung:
- Du kannst außerdem Zahlungsarten auswählen, für die kein Autoversand gelten soll. Solche Aufträge werden importiert und können im weiteren Verlauf manuell in den Versand gegeben werden.

#### Versandarten und Lieferbedingungen

![Otto_Workflows_Auftrage_Versandarten.png](https://help.xentral.com/hc/article_attachments/21740257565468)

- Das Feld “Welche Lieferbedingungen sollen für den Auftragsimport für diesen Onlineshop gelten?” kannst du leer lassen, da das Feld bei OTTO nicht benutzt wird.
- Hinterlege bei der “Standardversandart” eine Versandart, die verwendet werden soll, falls keine Versandart vom Marktplatz übergeben wird.
- Hinterlege unter “Versandarten Zuordnung” die Beziehung der OTTO-Versandart zu Xentral-Versandarten. Du kannst mehrere OTTO-Versandarten mit einer Xentral-Versandart verknüpfen oder jeweils eigene Xentral-Versandarten verwenden. Wichtig ist hierbei, dass du die Schreibweise von OTTO korrekt übernimmst. Folgende Versandarten stehen bei OTTO zur Verfügung:
- “Fast-Lane Versandarten”: Falls du deinen Kunden Express-Versandarten anbieten möchtest, kannst du auf dieses Feld klicken und dort die zutreffenden Versandarten anhaken. Wird von OTTO eine dieser Versandweisen übergeben, wird das Fast-Lane-Flag im Auftrag automatisch gesetzt.
- “Belege im Autoversand erstellen”: Wähle hier, welche Belege im Autoversand erstellt werden sollen. Die Option “Nur Rechnung” bietet sich z. B. an, wenn du einen Abholprozess abbilden möchtest.

#### Projekt

![Otto_Workflows_Auftrage_Projekt.png](https://help.xentral.com/hc/article_attachments/19113137543580)

Wähle ein **Standardprojekt**, das standardmäßig in die importierten Aufträge eingefügt wird.

#### Kundenzuordnung

In den folgenden Feldern legst du fest, wie Kunden zwischen deinem Shop und Xentral verknüpft werden sollen. Wir unterscheiden zwischen im Shop angelegten Kunden und Gastkunden, die kein Konto angelegt haben.

![Shared_Workflows_Auftrage_Kundenzuordnung.png](https://help.xentral.com/hc/article_attachments/19113152330396)

- Für Kunden sowie für Kunden ohne Kundenkonto (Gastkunden) hast du folgende Optionen:
- Hast du bei mind. einem der beiden vorhergehenden Felder die Option “Kunde aus Bestellung auf einen bestehenden Kunden zuordnen” gewählt, legst du im Feld **Kundenzuordnung** fest, anhand welcher Kriterien die Zuordnung erfolgt, wobei die Prüfreihenfolge “Kundennummer” vor “Mail-Adresse” vor “Name & Adresse” ist.

- Bestimme schließlich im Feld **Wenn kein Kunde gefunden wird, dann:** wie verfahren werden soll, falls kein Kunde zugeordnet werden kann:
- Setze den Auswahlschieber bei **Bestehende Kunden nur innerhalb des Projektes zuordnen?** nach rechts, wenn du die Suche nach Kunden auf das -spezifische Projekt in Xentral einschränken möchtest. Üblicherweise bleibt diese Schaltfläche deaktiviert.
- Hast du oben bei der Kundenanlage die Option “Jeden Kunden auf Default-Kunden schreiben” gewählt, trägst du schließlich im Feld “Default-Kunden auswählen” eine entsprechende Kundennummer ein.

#### Positionen

Setze den Auftragsschalter nach rechts, wenn du in den Belegen die Artikelbezeichnung aus dem XentralArtikelstamm andrucken möchtest. Dies ist beispielsweise sinnvoll, wenn du im Shop andere Bezeichnungen (z. B. für SEO-Zwecke) verwendest, als du in der Auftragsabwicklung nutzen möchtest. Du kannst außerdem wählen, ob bzw. welche Artikelbeschreibung in den Auftragspositionen angezeigt werden soll:

![Shared_Workflows_Auftrage_Positionen.png](https://help.xentral.com/hc/article_attachments/19113137553692)

### Reiter “Auftragsstatus & Tracking”

#### Update Strategie

![connect_workflows_auftragsstatus_update_otto.png](https://help.xentral.com/hc/article_attachments/19113137554972)

Setze den Schalter “Aufträge automatisch im Shop stornieren” nach rechts, wenn du Aufträge, die in Xentral storniert werden, auch im Marktplatz stornieren möchtest. Dies hat nur Auswirkungen auf noch nicht versendete Aufträge.

#### Versanddienstleister-Zuordnung

![connect_workflow_versanddienstleister_otto.png](https://help.xentral.com/hc/article_attachments/19113152354972)

Hier weist du die Versandarten aus Xentral den Versanddienstleister-Codes von Otto zu, damit die Trackinginformationen korrekt an Otto zurück übermittelt werden können.

> **Anmerkung**
>
> Beachte die Vorgaben zurShopeinrichtung. Der Versand- und Retouren-Prozess für den Paketversand ist ausschließlich über DHL automatisiert. Solltest du einen anderen Versanddienstleister nutzen, denke daran, auch den Abschnitt "Retouren" weiter unten zu bearbeiten.

#### Lageradresse

![connect_workflows_lageradresse.png](https://help.xentral.com/hc/article_attachments/19113137558172)

Trage in den Feldern Postleitzahl, Stadt und Land die Daten des Versandlagers ein, aus dem du versendest. Dies ist wichtig, damit die Steuerberechnung korrekt erfolgen kann.

> **Anmerkung**
>
> Berücksichtige in diesem Zusammenhang auch die Lieferschwellen-Thematik. Nähere Informationen dazu findest duhier.

#### Retouren

> **Anmerkung**
>
> Falls du deinen Versand- und Retouren-Prozess an einen Fulfiller ausgelagert hast, oder deine Pakete mit einem anderen Dienstleister als DHL versendest, frage bei deinem Versanddienstleister einen Retourennummernpool an und trage ihn hier ein.

> **Anmerkung**
>
> Falls du nur den automatisierten Prozess über DHL-Paketversand nutzt, brauchst du an dieser Stelle nichts eintragen.

![connect_workflows_retouren.png](https://help.xentral.com/hc/article_attachments/19113152357788)

Trage den Retourennummernpool deines Versanddienstleisters ein. Die Angabe kann mit beliebigen Trennzeichen (z. B. Leerzeichen, Komma, Semikolon) erfolgen.

> **Wichtig**
>
> Die Connect-Schnittstelle verwendet automatisch die nächste freie Retourennummer des Pools und meldet diese bei der Statusmeldung einer Lieferung an den Marktplatz. Dies stellt sicher, dass die Lieferung als “fulfilled” im Marktplatz markiert wird. Wir empfehlen, den Retourennummernpool so groß zu wählen, dass das Sendungsvolumen von sechs Monaten abgedeckt ist, danach können Retourennummern wiederverwendet werden. Ein Ergänzen des Retourennummernpools ist jederzeit möglich.

## Testphase und Produktivschaltung

### Testphase

Wenn du alle Einstellungen in den Workflows vorgenommen hast, solltest du die Anbindung ausgiebig testen.

Schränke die[Artikelzuordnung](https://help.xentral.com/hc/de/articles/16510627621532#UUID-eecfb261-6503-5309-fcae-89ad123f65c3)auf wenige Artikel ein.

Nutze einige Testdaten und führe die Tests mit Hilfe der Funktionen im[Journal](https://help.xentral.com/hc/de/articles/16510622825756#UUID-cc81f147-fc32-992b-080c-a5e78d6107b5)durch.

### Produktivschaltung

Sobald die Schnittstelle die Testdaten richtig und wie erwartet übergibt, kannst du mit der[Produktiv-Schaltung](https://help.xentral.com/hc/de/articles/18589740879132#UUID-76f3afac-0b29-56cb-47ca-10af39e437d6)fortfahren.

**Viel Spaß mit deiner neuen Schnittstelle!**