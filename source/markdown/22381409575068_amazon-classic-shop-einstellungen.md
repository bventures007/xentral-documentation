In diesem Abschnitt werden dir die möglichen Einstellungen in der Shop-Schnittstelle erklärt.

### Schnittstelle

Wenn du die Einstellungen der Amazon Schnittstelle öffnest, landest du zunächst im TabDetails > Schnittstelle.

![Amazon-4.png](https://help.xentral.com/hc/article_attachments/22381468935324)

![Amazon-5.png](https://help.xentral.com/hc/article_attachments/22381431626524)

Einstellungen:

- **Bezeichnung:** Name frei wählbar für den Shop (wird z.B. im Artikel und im Import-Menü angezeigt)
- **Aktiv:** Haken setzen, damit die Schnittstelle aktiv ist. Nicht mehr benötigte Schnittstellen kannst du auf inaktiv setzen
- **Projekt:** Verknüpfung des Shops auf ein Projekt. Im Projekt kannst du die Logistikeinstellungen vornehmen
- **Abholmodus:** Bei Amazon kannst du hier ab einem bestimmten Datum abholen
- **Datum von:** Ab diesem Zeitpunkt werden Aufträge abgeholt, aktualisiert sich wenn du die Funktion Aufträge abholen benutzt
- **Start der Schnittstelle:** Es werden keine Aufträge vor diesem Datum abgeholt
- **Import-Modus:** Legt fest, ob die Aufträge aus dem Shop manuell (per Knopfdruck) oder automatisch importiert werden sollen
  - Demo (zum Testen): Der Auftragsstatus im Shop nicht umgestellt, keine Artikel oder Lagerzahlen übertragen
  - Manuell (mit Importzentrale): Die Aufträge werden erst abgeholt, wenn der Button Aufträge abholen geklickt wird
  - Automatisch (per Prozessstarter): Die Aufträge werden regelmäßig automatisch vom Shop abgeholt. Hierfür wird der Prozessstarter Shopimporter benötigt
- **Nur 1 Auftrag pro Anfrage:** Es wird nur 1 Auftrag pro Anfrage vom Shop übertragen
- **Aufträge in Zwischentabelle: ** Beim Abholen der Aufträge werden die Aufträge nicht direkt angelegt, sondern erstmal zum Durchschauen in einer Zwischentabelle gespeichert. Hier kannst du entscheiden, welche Aufträge angelegt und welche erst später importiert werden sollen ** Einstellungen für Shop oder Marktplatz: **

-** SellerId: ** SellerID aus Amazon Seller Central **Zugangsdaten: **

-** AWS Access Key Id:** Mit einem Entwickleraccount können statt dem MWS Auth Token ein Access Key und SecretKey für die Anbindung genutzt werden
- **AWS SecretKey:** Nur mit einem Entwickleraccount erhältlich
- **Zeitzone:** Zeitzone des Amazon Hauptshops
- **Währung:** Währung des Amazon Hauptshops
- **Wunschlieferdatum setzen:** Datum, bist wann die Lieferung erfolgen soll, wird von Amazon importiert. Falls das niedrigste Lieferdatum bei Amazon weniger als die eingetragene Anzahl an Tagen in der Zukunft liegt, wird ein neues Wunschlieferdatum im Auftrag gesetzt
- **Debug: ** Wenn du den Haken setzt, wird der Debugging-Modus aktiviert und die Aufrufe werden in Logs gespeichert ** FBA Einstellungen: **

-** FBA Aufträge abholen:** Haken setzen, wenn du FBA Aufträge abholen willst
- **Eigenes Projekt für FBA:** Hier kannst du ein Projekt für FBA Aufträge setzen
- **Rechnungsnummer von Amazon verwenden (nur bei Amazon Rechnungsservice):** Haken setzen, wenn die Rechnungsnummer von Amazon genutzt werden soll
- **Max. Tage für Reports:** Die maximale Anzahl an letzten Tagen, aus denen die Reports importiert werden (typischerweise 30)
- **Auftrag auf abgeschlossen setzen: ** Aufträge werden direkt mit dem grauen "Abgeschlossen"-Haken importiert ** FBM Einstellungen: **

-** FBM Aufträge abholen:** Haken setzen, wenn du FBM Aufträge abholen willst
- **Eigenes Projekt für FBM:** Hier kannst du ein Projekt für FBM Aufträge setzen
- **Geschenkverpackung: ** Hier musst du einen Portoartikel eintragen ** Invoice handling (Rechnungseinstellungen): **>** Anmerkung**
>
> Die korrekte Konfiguration für die Rechnungsabwicklung mit Amazon kann herausfordernd sein.Einstellungen für verschiedene Rechnungsszenarien (Amazon) (Classic)stellen wir sinnvolle Einstellungen für die verschiedenen Szenarien vor.

- **Gutschriften erzeugen:** Hier kannst du auswählen, ob eine Gutschrift erzeugt werden soll oder nicht
- **Rechnungsupload-Service verwenden:** Setze diesen Haken, damit die Rechnungen bei Versandmeldung an den Shop übertragen werden
- **Rechnungen spätestens x Tage nach Rechnungsdatum übertragen:** Nach der eingegebenen Anzahl an Tagen wird die Rechnung spätestens übertragen
- **Upload Startdatum:** Datum, ab dem die Rechnung hochgeladen wird
- **VAT übernehmen ab:** Datum, ab dem die Rechnungsnummern aus dem VAT Report übernommen werden
- **FBA: **

-** Rechnung erzeugen:** Hier kannst du einstellen, ob eine Rechnung für FBA Aufträge erstellt werden soll oder nicht
  - **Rechnung per E-Mail versenden:** Haken setzen, wenn die Rechnung per Mail an die Kunden versendet werden soll
  - **Gutschriften per E-Mail versenden:** Haken setzen, wenn die Gutschrift per Mail an die Kunden versendet werden soll
- **FBM: **

-** Rechnung erzeugen:** Hier kannst du einstellen, ob eine Rechnung für FBM Aufträge erstellt werden soll oder nicht
  - **Rechnung per E-Mail versenden: ** Haken setzen, wenn die Rechnung per Mail an die Kunden versendet werden soll ** Marktplätze: **

-**[Land] Checkbox:** Aktiviere einen Marktplatz, indem du den Haken beim jeweiligen Land setzt.
- **Preisgruppe:** Trage hier die Preisgruppe ein, die für den jeweiligen Marktplatz gilt.

Aktion:

- **Verbindung prüfen:** Hier kannst du die korrekte Verbindung zu Amazon prüfen
- **Aufträge abholen:** Holt die Aufträge aus deinem Shop ab. Das ist notwendig, wenn du den Importmodus der Schnittstelle auf manuell gestellt hast.

- **Shopimport Zwischentabelle:** Springt zur Zwischentabelle der Aufträge vom Shop. Die Zwischentabelle wird nur im manuellen Importmodus befüllt und wenn die Option 'Aufträge in Zwischentabelle' aktiviert ist.
  In der Zwischentabelle wählst du in der linken Spalte zwischen "Import", "Müll" und "Später" aus.

  - Import: Auftrag wird direkt importiert
  - Müll: Auftrag landet im Müll und kann kein zweites Mal importiert werden
  - Später: Auftrag kann zu einem späteren Zeitpunkt importiert werden
- **Zur Amazon App:** Leitet dich zur Amazon Seller App weiter
- **Alte Aufträge importieren:** Alte Aufträge werden in die Zwischentabelle geladen, wo du wieder entscheiden kannst ob die Aufträge importiert werden sollen. Wichtig ist, dass kein gleichzeitiger Betrieb möglich ist (d.h. aktuelle Aufträge und alte Aufträge können nicht gleichzeitig importiert werden)

### Einstellungen

Im Folgenden werden alle Einstellungen gezeigt, die du im ReiterEinstellungenvornehmen kannst.

#### Einstellungen für den Auftragsimport

Die Einstellungen im Bereich Auftrag Import regeln die Art der Übertragung und Synchronisation zwischen Xentral und Shop. Zu beachten ist, dass nicht jede Shop-Schnittstelle auch jede Funktion unterstützt. Welche Shop-Schnittstellen welchen Funktionsumfang abdecken, kannst du den Artikeln zu den einzelnen Schnittstellen entnehmen.

- **Zahlungweisen-Mapping verwenden**> Zahlungsweisen in Xentral sollen auf Zahlungsweisen im Shop verknüpft werden.
- **Versandarten-Mapping verwenden**> Versandarten in Xentral sollen auf Versandarten im Shop verknüpft werden.
- **Vorab als bezahlt markieren**> Aufträge aus dem Shop werden in Xentral vorab als bezahlt markiert. Diese Funktion markiert Aufträge mit besonderen Bezahlarten (spezielle Bezahlarten über Zahlungsanbieter, Geldinstitute) als "vorab bezahlt". Die Ampel wird für diese Bezahlarten immer auf grün
- **UTF8-Codierung**> Der Shopimporter verwendet die UTF8-Codierung (bitte aktiveren, um Anzeigefehler bei Sonderzeichen usw. zu vermeiden!)
- **Multiprojekt Shop**> In diesem Shop werden Artikel aus verschiedenen Projekten angeboten. Es handelt sich hierbei um eine Sonderfunktion.
  Diese Option benötigst du nur, wenn du in deinem Shop Artikel aus verschiedenen Projekten anbietest.

  Beispiel: In deinem Shop werden einige Artikel angeboten, die einen anderen Logistikprozess erfordern oder bei denen direkt nach der Bestellung eine spezielle Kundenprüfung (z.B. Handelsregisterauszug anfordern) notwendig ist. Diese Artikel können auf diese Weise gemeinsam gekauft werden. Nach dem Abholen der Aufträge nach Xentral werden jedoch verschiedene Prozesse angestoßen (z.B. andere E-Mail Vorlagen, Kundenprüfung ist erforderlich, anderen Logistikprozess, anderen Rechnungsversand, anderes Briefpapier etc.)

- **USt. geprüft + Freigabe für Versand**> Der Haken 'UST-ID geprüft' wird in alle Aufträgen aus dem Shop automatisch gesetzt, sodass die Umsatzsteuer-Prüfung die Aufträge für den Versand freigibt. Auf diese Weise kannst du die UST-ID Prüfung deaktivieren.
- **Porto**> Artikel aus Xentral, der die Versandkosten aus dem Shopauftrag als eigene Position abbildet
- **Porto ermäßigt**> Artikel aus Xentral, über den ermäßigte Versandkosten für Aufträge aus diesem Shop, abgebildet werden sollen
- **Portoartikel anlegen**> Falls kein Portoartikel hinterlegt ist, wird ein Portoartikel mit der Bezeichnung aus dem Shop angelegt und in den Auftrag in Xentral eingefügt, um das Porto abzubilden
- **Nachnahmegebühr als extra Position**> Bei Nachnahme-Aufträgen wird die Nachnahme-Gebühr als eigene Position im Auftrag eingefügt
- **Nachnahmegebühr**> Artikel in Xentral, der die Nachnahmegebühr als Auftragsposition abbildet
- **Auftragsstatus rückmelden**> Xentral darf den Status importierter Aufträge an den Shop zurückmelden
- **Automatische Rückmeldung deaktivieren**> Dadurch wird die automatische Rückmeldung an den Shop, für Aufträge ohne Trackingnummer, deaktiviert. Die Rückmeldung findet also nur noch nach Speichern der Trackingnummer statt oder durch das automatische Rückmelden ohne Trackingnummer im Übertragenmodul
- **Hole jeden Status**> Es werden unabhängig vom Status alle Aufträge vom Shop zu Xentral übertragen
- **Freitext aus Shopschnittstelle**> Durch diese Einstellung ist es dir möglich den Freitext (Kommentarfeld im Shop) entweder in den Freitext oder in die interne Bemerkung des Auftrags zu übernehmen. Stell hierzu die Einstellung auf:
  - in Feld Freitext laden
  - oder: in Feld interne Bemerkung laden
  Kundeninformationen/Kundenkommentare werden so mit in den Auftrag nach Xentral ins Feld 'Freitext' übernommen und werden somit auf den Dokumenten mit abgedruckt. Praxistipp: In der Logistik kannst du diese Info zusätzlich als rote Box in den Versandprozessen am Packtisch anzeigen lassen. Diese Information muss am Packtisch bestätigt werden. Die Einstellungen sind in den Systemeinstellungen (zentrale Einstellungen zu finden).

- **Angebote statt Aufträge anlegen**> Die Aufträge aus dem Shop werden in Xentral nicht als Aufträge, sondern als Angebote angelegt
- **Autoversand bei Kommentar in Warenkorb deaktivieren**> Hat der Kunde im Shop ein Kommentar beim Checkout im Shop hinterlassen, so wird der Autoversand für diesen Auftrag in Xentral deaktiviert (und erlaubt somit ein manuelles Prüfen der Aufträge durch den Mitarbeiter)
- **Stornierung rückmelden**> Wird ein Auftrag in Xentral storniert, wird die Stornierung an den Shop gemeldet, damit der Auftrag auch dort den Status 'storniert' bekommt (aktuell verfügbar für Shopify, Shopware und WooCommerce)
- **Besteuerung im Drittland abhängig von Lieferadresse machen**> Die Besteuerung bei Export-Aufträgen wird anhand der Lieferadresse statt an der Rechnungsadresse bestimmt
- **Gesamtbetrag festsetzen**> Der Gesamtbetrag der Aufträge wird aus dem Shop für Xentral übernommen und nicht in Xentral neu aus den Artikelpositionen berechnet
- **Maximale Differenz zur berechneten Summe**> Bereich, für den die Einstellung Gesamtbetrag festsetzen gelten soll. Nützlich z.B. wenn Auftragssummen auf 0,05 Währungseinheiten gerundet werden oder es zu Rundungsfehler bis zu 1 Cent kommt
- **Lastschriftdaten in Adresse überschreiben**> Die Lastschriftdaten einer Adresse im Adressstamm werden überschrieben, wenn sie bei einem Shopauftrag dieses Kunden abweichend waren

#### Einstellungen zum Artikelimport und -export

- **Lagerzahlen Übertragung erlauben**> Xentral darf die Lagerbestände der Artikel in den Shop exportieren
- **Lager Grundlage**> Lagerbestand des Artikels, der an den Shop gemeldet werden soll (Verkaufbare oder gesamter Lagerbestand minus Reservierungen)
- **Lagerkorrekturwert überschreiben**> Der hier eingetragene Lagerkorrekturwert wird für alle Artikel an den Shop gemeldet und muss somit nicht mehr pro Artikel im Artikelstamm gepflegt werden (anklicken, damit Lagerkorrekturwert eingetragen werden kann)
- **Pseudolager Regeln**> Meldet Lagerzahlen nach einem über Formeln einstellbaren Regelwerk an den Shop. Weitere Infos findest du im Helpcenter-Artikel [Pseudolagerzahlen Formeln](https://help.xentral.com/hc/de/articles/360016759379#UUID-791d5a33-b1e2-9dec-cc4e-05d3b88a25db)
- **Artikel Übertragung erlauben**> Xentral darf Artikel in den Shop exportieren
- **Alle geänderten Artikel automatisch übertragen**> Durch Anhaken werden alle geänderten Artikel automatisch von Xentral zum Shop übertragen. Dieses Feld hängt mit dem [artikeluebertragen](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a) Cronjob zusammen. Wenn der Cronjob läuft und keine Artikel für den Export vorhanden sind, sucht der Cronjob nach allen Produkten, die mit einem Shop verbunden sind und bei denen dieses Feld aktiv ist. Er überprüft dann bei jedem dieser Artikel, ob es seit dem letzten Export irgendwelche Änderungen gab. Falls das der Fall ist, wird der jeweilige Artikel zu der Liste der zu exportierenden Artikel hinzugefügt, welche nach der Überprüfung exportiert wird
- **Bilder übertragen**> Xentral darf Artikelbilder in den Shop exportieren
- **Eigenschaften übertragen**> Xentral darf Artikeleigenschaften in den Shop exportieren
- **Kategorien übertragen**> Xentral darf Artikelkategorien in den Shop exportieren
- **Crossselling übertragen**> Xentral darf die Crossselling-Verknüpfungen zwischen Artikeln in den Shop exportieren
- **Staffelpreise übertragen**> Xentral darf Staffelpreise der Artikel in den Shop exportieren
- **Gutscheine übertragen**→ Gutscheine aus Shopware 5 werden übertragen und können in Xentral verarbeitet werden. Weitere Infos sind [hier](https://help.xentral.com/document/preview/42597#UUID-c56fc7e3-4106-b7d0-cf23-d1d623d89b3c_id_360016725600_id_h_01F2VCJGTNEKGNA5M9DT3W8027) zu finden
- **Artikeltext Übertragung unterdrücken**> Der Export von Artikeltexten von Xentral zum Shop wird für die ganze Schnittstelle deaktiviert
- **Artikelliste abholen nur neue Artikel anlegen**> Bei der Aktion 'Artikelliste abholen' werden nur fehlende Artikel neu angelegt, aber bereits im Adressstamm von Xentral vorhandenen Artikel werden nicht aktualisiert
- **Artikelnummer beim Anlegen aus Shop übernehmen**> Die Artikelnummer aus dem Shop wird auch als Artikelnummer in Xentral angelegt, wenn der Artikel aus dem Shop importiert wird

#### Einstellungen zu den Rabatten

- **Rabatt**> Hier gibts du die Artikelnummer von dem Artikel aus Xentral ein, der Rabatte im Shopauftrag als eigene Position im Auftrag mit negativem Verkaufspreis abbildet
- **Steuersatz für Rabatt-Artikel**> MwSt.-Satz des verwendeten Rabatt-Artikels (normal oder ermäßigt). Für einen B2B-Shop mit Netto-Rechnung musst du hier den Wert 0 eintragen. Du kannst dieses Feld leer lassen, wenn du den Steuersatz aus dem Artikel verwenden möchtest.

#### Zugangsdaten für Xentral Import Plugin

- **URL**> Hier die URL zum Importer eingeben
- **ImportKey**> 32 Zeichen langes Sicherheitspasswort
- **ImportToken**> 6 Zeichen langes Sicherheitstoken

#### Einstellungen zu den Positionen im Auftrag

- **Fehlende Artikel anlegen**> Artikel, die im Shopauftrag enthalten sind, aber nicht im Artikelstamm gefunden werden, werden automatisch im Artikelstamm von Xentral angelegt
- **Rabatte Porto festschreiben**> Rabatte und Porto werden aus dem Shop übernommen und festgeschrieben
- **Beschreibungstexte aus Shop**> Texte aus dem Shop werden in den Artikelstamm von Xentral übernommen
- **Artikelnummern aus Nummernkreis**> Den Artikeln, die aus dem Shop kommen, werden Artikelnummern aus dem Nummernkreis von Xentral vergeben
- **einzeln**> Nur bei Artikeln mit der Option 'Online Shop Abgleich' im Artikelstamm findet die obige Einstellung Anwendung
- **Artikelnummern aus dem Shop**> Falls die Artikelnummern aus dem Shop sich von denen in xentral unterscheiden (gefunden über die Fremdnummern), werden die Artikelnummern vom Shop übernommen
- **Artikelbezeichnung aus xentral**> Es werden die Artikelbezeichnungen aus xentral in die Auftragspositionen übernommen
- **Artikelbeschreibungen aus xentral**> Es werden Artikelbeschreibungen aus Xentral in die Auftragspositionen übernommen
- **Artikelbeschreibungen aus dem Shop**> Falls der Shop die Artikelbeschreibungen überträgt, werden diese im Auftrag übernommen
- **Stücklisten ergänzen**> Bei 'Mix & Match'-Artikel (z.B. Bündelartikel bei Magento) werden die Stücklisten analog zum Shop ergänzt
- **Spezielle Steuersätze pro Positionen**> Die Steuersätze aus dem Shop werden auch bei Aufträgen mit gemischten Steuersätzen übernommen

#### Einstellungen zum Adressen Import

- **Bestehende Kunden nur aus Projekt verwenden**> Setze den Haken, wenn der Kunde pro Projekt mit einer neuen Adresse angelegt werden soll (die Kundenadresse existiert dann pro Projekt und z.B. pro Shop, also insgesamt mehrmals in xentral, sofern der Kunde über mehrere Shops bestellt)
- **Bestehende Adressen nicht überschreiben**> Die im Shop neu eingegebenen Daten überschreiben nicht die Kundenadresse in Xentral (keine Adressaktualisierung in den Stammdaten)
- **Manuelle Adressübertragung**

- Diese Funktion erlaubt das manuelle Übertragen von Adressdaten in den Shop.
  - Die Manuelle Adressübertragung fügt in Adresse (Stammdaten → Adressen → *Adresse auswählen*) eine Schaltfläche hinzu (Voraussetzung: die Adresse hat das gleiche Projekt wie der Shop), der - wenn du ihn betätigst - die Adresse im Shop anlegt. Automatisch wird aber nichts übertragen.
  Die manuelle Übertragung zeigt auch das Passwort an, welches die Kundennummer ist.

- **Vertrieb**> Hier kannst du den Vertriebsansprechpartner eintragen. Dieser wird aktuell nur in den Auftrag übernommen, nicht aber in die Adresse.

Eine abweichende Lieferadresse aus dem Shop wird beim Auftragsimport nicht in die Adresse übernommen.

#### Einstellungen zu den Extra Verkaufspreisen

Es gibt auch die Möglichkeit in den Shopeinstellungen eine Preisgruppe anzugeben, für die deren Verkaufspreis in den Shop übertragen werden soll.

Sobald du den Verkaufspreis auf diese Gruppe angelegt hast, überträgt xentral diesen Verkaufspreis in deinen Shop und nicht z.B. den Standardverkaufspreise.

#### Kommunikations-Einstellungen

Wenn du den Shopanbieter wechselst, kannst du hier auch das Modul im Shopimporter umstellen oder aktualisieren. Dazu gehört z.B. auch ein Wechsel von einem externen Importer auf einen neuen internen Importer.

Alle allgemeinen Einstellungen sowie alle Verknüpfungen zu Artikeln, Kategorien, Fremdnummern, Versand- und Zahlungsmappings sowie Subshops bleiben dann bestehen, es wird aber eine neue API angesprochen.

> **Wichtig**
>
> Alle shop-spezifischen Einstellungen gehen hierdurch verloren! Du musst die Zugangsdaten neu eingetragen und speichern.

### Zahlungsweisen Mapping

Im Tab **Zahlweisen ** kannst du die aus dem Shop übergebenen Parameter für die unterschiedlichen Zahlungsweisen auf die in Xentral angelegten Zahlungsweisen mappen. Dafür musst du unter**Einstellungen** die Option "Zahlungweisen-Mapping verwenden" aktiviert haben. Damit unbekannte Zahlungsweisen aus Online-Shops auf bekannte Zahlungsweisen in Xentral verknüpft werden können, werden die vom Shop übergebenen Parameter automatisch als leerer Eintrag in der Mapping-Tabelle angelegt.

![Online-Shops-6.png](https://help.xentral.com/hc/article_attachments/22381468936732)

Einstellungen

Mit einem Klick auf das Editiericon einer angelegten Zahlungsweise gelangst du in die Einstellungen. Pro Zahlungsweise kannst du Einstellungen vornehmen werden, wie Aufträge mit dieser Zahlungsweise zu behandeln sind.

![Online-Shops-7.png](https://help.xentral.com/hc/article_attachments/22381431627932)

- **Zahlweise Shop**> Bezeichnung der Zahlungsweise im Shop
- **Zahlweise xentral**> Zahlungsweise in Xentral
- **Vorab als bezahlt markieren**> Aufträge mit dieser Zahlungsweise vorab als bezahlt markieren
- **Autoversand aktiv**> Aufträge mit dieser Zahlungsweise werden für den Autoversand freigegeben
- **Keine Rechnung erstellen**> Es wird keine Rechnung für Aufträge mit dieser Rechnung erstellt
- **Fast-Lane**> Aufträge mit dieser Zahlungsweise automatisch in die Fast-Lane übergeben
- **Aktiv**> Zahlungsweise ist aktiv

### Versandarten

Wenn du auf **Verbindung prüfen (Details > Schnittstelle)** klickst, importiert die Schnittstelle alle Versanddienstleister (Carrier), die bei Amazon verfügbar sind. Neben dem Mapping mit Carriern verfügtXentral nun auch über ein Mapping für das Produkt. Es werden also die Versanddienstleister angezeigt und zusätzlich die jeweilige Produkt-ID.

Anschließend musst du die erstellten Versandarten den entsprechenden Versandarten auf der Registerkarte **Versandarten ** zuordnen. Diese Zuordnung musst du in**jeder** erstellten Amazon-Schnittstelle vornehmen. Es gibt ein neues Mapping-Feld namens "Produkt Ausgehend". Hier kannst du die entsprechende Produkt-ID für die Versandart für die Zuordnung eingeben.

![Amazon-8.png](https://help.xentral.com/hc/article_attachments/22381431628060)

Es ist notwendig, dass das Mapping in **jeder** Amazon-Schnittstelle durchgeführt wird, damit bei der Rückmeldung der Tracking-Nummer von versendeten Bestellungen auch eine Information an Amazon zurückgegeben werden kann, welcher Versanddienstleister verwendet wurde.

Ändern sich die Versandanbieterdaten seitens Amazon, kannst du die aktualisierten Daten jederzeit über die Schaltfläche **Verbindung prüfen** abrufen.

In der Protokolldatei der Shop-Schnittstelle sind alle Fehlermeldungen bezüglich der Zuordnung der Versandmethoden aufgeführt. Die Meldung "Carriers have not yet been retrieved from the store" wird ausgegeben, wenn du die Versandanbieter noch nicht über die Schaltfläche **Verbindung prüfen** hinzugefügt hast.

#### Versandarten-Mapping

Im Tab **Versandarten** kannst du die aus dem Shop übergebenen Parameter für die unterschiedlichen Versandarten auf die in Xentral angelegten[Versandarten](https://help.xentral.com/hc/de/articles/18567521362332#UUID-7d97af0c-3e39-6798-67c6-50f26028c174)mappen. Dafür musst du unter Einstellungen die Option "Versandarten-Mapping verwenden" aktivieren. Damit unbekannte Versandarten aus Online-Shops auf bekannte Versandarten in Xentral verknüpft werden können, werden die vom Shop übergebenen Parameter automatisch als leerer Eintrag in der Mapping-Tabelle angelegt.

![Online-Shops-8.png](https://help.xentral.com/hc/article_attachments/22381431628316)

**Einstellungen**

Mit einem Klick auf das Editier-Icon einer angelegten Versandart gelangst du in die Einstellungen. Pro Versandart kannst du Einstellungen vornehmen, wie Aufträge mit dieser Versandart zu behandeln sind.

![Online-Shops-9.png](https://help.xentral.com/hc/article_attachments/22381468938396)

- **Versandart Shop**> Bezeichnung der Versandart im Shop
- **Versandart xentral**> Versandart in Xentral
- **Versandart Ausgehend**> Nur für Amazon und Billbee relevant
- **Versandprodukt Ausgehend**> Nur für Amazon und Billbee relevant
- **Land** (mit Komma getrennt, zweistellig ISO) > Einschränkung, für welches Land Versandart verfügbar ist (leer = keine Einschränkung)
- **Fast-Lane**> Aufträge mit dieser Versandart automatisch in die Fast-Lane übergeben
- **Autoversand aktiv**> Aufträge mit dieser Versandart werden für den Autoversand freigegeben
  Aktiv > Versandart ist aktiv

Die textuelle Beschriftung der Versandart für die Software-Oberfläche und die Beschriftung auf den Dokumenten (abgedruckter Text auf Rechnung, Auftrag, etc.) erfolgt über das Mapping in den Versandarten (Administration → Einstellungen → Versandarten).

Dort wird der Typ (= Feldbezeichnung in Xentral, z.B. "selbstabholer") auf die textuelle Beschreibung wie z.B. "Selbstabholer" oder "Hofverkauf" verknüpft. Nähere Informationen zur Einstellung der Versandarten befinden sich[hier](https://help.xentral.com/hc/de/articles/18567521362332#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

### Freifelder

Freifelder sind für Amazon derzeit nicht verfügbar.

### Subshop

Mit dem Subshopmapping kannst du für jede Marketplace ID ein eigenes Projekt mit eigenem Logistikverfahren einstellen. Es ist auch möglich die Subshops nach FBA und FBM zu differenzieren.

Dazu kannst du unter in der Schnittstelle im Reiter Subshop die Subshops folgendermaßen anlegen: Marketplace (kleingeschrieben) + Unterstrich + FBA oder FBM, zum Beispiel:

- de_FBA für Marketplace Deutschland FBA
- it_FBM für Marketplace Italien FBM
- gb_FBM für Marketplace Großbritannien FBM

![Amazon-9.png](https://help.xentral.com/hc/article_attachments/22381431629084)

### Sprache/Lieferland

Im Tab **Sprache/Lieferland** kannst du verschiedene Sprachen für die Belege einstellen, indem du jeweils das Länderkürzel und die zugehörige Sprache eingibst und speicherst.

![Online-Shops-13.png](https://help.xentral.com/hc/article_attachments/22381431630364)

> **Anmerkung**
>
> Hierbei wird nur die Rechnungsadresse berücksichtigt, d.h. falls es eine abweichende Lieferadresse gibt, wird diese nicht berücksichtigt. Ist beispielsweise die Rechnungsadresse DE und die Lieferadresse GB, dann ist die Sprache des Auftrags deutsch.

Du kannst eine gespeicherte Sprache deaktivieren bzw. aktivieren, indem du auf das Editiersymbol klickst und den Haken bei "aktiv" entfernst oder hinzufügst.

![Online-Shops-14.png](https://help.xentral.com/hc/article_attachments/22381431631260)

Wenn du das Land leer lässt, gilt die Sprache für alle Länder außer diejenigen, für die du ebenfalls einen Eintrag angelegt hast. So kannst du zum Beispiel für die DACH-Region (D, AT, CH) jeweils Deutsch als Sprache hinterlegen. Als weiteren Eintrag Englisch ohne Land. Dann wird für alle Länder, die nicht aus der DACH-Region stammen, Englisch als Sprache hinterlegt.

### Gruppenmapping

Gruppenmapping ist für Amazon derzeit nicht verfügbar.

### Smarty

Über die Verwendung von Smarty erfährst du mehr in diesem Helpcenter-Artikel:[Smarty im Shopimporter](https://help.xentral.com/document/preview/13979#UUID-e55a4c1d-d861-ef5d-741d-94856c3b5b50).

### Artikel-Fremdnummern

Die ASIN ist nicht relevant bei Amazon - egal ob FBA oder FBM - relevant ist die zugehörige Seller SKU, welche bei Fremdnummern im Artikel hinterlegt sein müssen. Die ASIN ist bei Amazon nicht eindeutig, da diese unterschiedliche Zustände haben kann wie neu, gebraucht oder generalüberholt. In der Amazon Schnittstelle unter **Details -> Artikel-Fremdnummern** kannst du auch die Fremdnummern der von Amazon abgeholten FBA-Artikel verknüpfen, indem du die SKU zur Verknüpfung der Artikelnummer in Xentral verwendest oder indem du die SKU direkt als xentral-Artikelnummer verwendest.

Die Fremdnummern Tabelle wird aus der Tabelle Lagerbestände in der Amazon Seller App gefüllt. Dabei werden nur Artikel abgeholt, die in Amazon als FBA-Artikel eingestellt sind. Diese kannst du dann in der Amazon Seller App verwalten. Die Fremdnummern von FBM-Artikeln musst du direkt im Artikelstamm anlegen.

![Amazon-10.png](https://help.xentral.com/hc/article_attachments/22381468942364)

- Nicht zugeordnete Artikel anlegen: Amazon-Artikel, die nicht verknüpft wurden, werden neu in Xentral angelegt
- SKU als WaWi-Artikelnummer verwenden: Die SKU des Artikels wird in Xentral als Artikelnummer angelegt

Per Klick auf **Artikel updaten** speicherst du die eingetragenen Verknüpfungen.

### Report Status

![Amazon-11.png](https://help.xentral.com/hc/article_attachments/22381431632284)

### Feeds

In diesem Reiter werden die Abrechnungsberichte angezeigt, die Amazon erstellt, wenn du dir nach Verkäufen Geld auszahlen lässt. Außerdem hast du hier die Möglichkeit manuell Gutschriften zu erstellen.