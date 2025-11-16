In den Systemeinstellungen findest du wichtige Xentral Einstellungen, die das gesamte System betreffen. In diesen Einstellungen kannst du zentrale Verhaltensweisen festlegen oder dein Geschäft individueller definieren z.B. Informationen, die in Belegtypen zentral angezeigt werden sollen, bis hin zu leistungsrelevanten System Einstellungsoptionen. Folgende Bereiche findest du in den Systemeinstellungen:

- **Standard Projektdefinition und Sprache**

- lege das zentralen Standardprojekt für die gesamte Firma fest und die bevorzugte Sprache
- **Artikel und Produkteinstellungen**

- Einstellungen für die zentrale Artikel Suche, Einheiten und Gewichtseinstellungen
- **Übergreifende Belegeinstellungen**

- z.B. Freigabe der Belege mit Zwischenabfrage, Informationsdichte und Anzeigen in Positionstabellen im Beleg, Individuelle Zusatzanzeigen z.B. Artikelbilder, Weiterführen der Belege und Workfloweinstellungen
- **Einstellungen der Xentral Tabellenansichten**

- Artikel- und Belegtabellen z.B. Auftrag, Rechnung
- **Auftragsampel**

- Individualisierung und Anzeige der Auftragsampelnzur Steuerung
- **Drucker**

- Standard Drucker als Voreinstellung für Arbeitsschritte für dein Team
- **Sonstiges**

- spezielle Moduleinstellungen, Systemweite bevorzugte Sprache
- **Weitere Moduleinstellungen**

- z.B. Wareneingang, Produktion, Zeiterfassung, E-Mail - spezielle systemweite Moduleinstellungen
- **DSGVO** Einstellungen, Sicherheitseinstellungen
- **System Beschleunigung und Limitierungen**

- individuell nach Performance und Volumenanforderungen

### Systemeinstellungen bearbeiten

Unter **Administration **>** Einstellungen **>** System **>** Grundeinstellungen **>** System** kannst du die Einstellungen vornehmen und speichern.

![systemeinstellungen_001.png](https://help.xentral.com/hc/article_attachments/12983719966748)

### Projekt (Systemeinstellungen)

Lege das zentralen Standardprojekt für die gesamte Firma fest.

| Feldbezeichnung | [en-us] Description |
| --- | --- |
| Hauptprojekt | Dieses Projekt wird immer im Standard geladen. Steuert die Projektvorschläge bei Neuanlage von Adressen und Artikeln sowie Geschäftsbriefvorlagen. |
| Projekt öffentlich setzen bei Anlage | Steuert die Sichtbarkeit des Projektes. Die Inhalte von öffentlichen Projekten sind für alle Mitarbeiter sichtbar. Übersteuert die Rollenzuweisung in den Adressstammdaten. |
| Projektrechte nur Mitarbeiterrolle auswerten | Es werden nur Projekte mit dem Recht Mitarbeiterrolle ausgewertet. |

### Artikel (Systemeinstellungen)

Einstellungen für die zentrale Artikel Suche, Einheiten und Gewichtseinstellungen.

| Feldbezeichnung | |
| --- | --- |
| Erweiterte Artikelsuche (Kurztext) | Ermöglicht in der Artikel-Übersicht nach Inhalten aus dem Artikel-Feld 'Kurztext DE' zu suchen. |
| Erweiterte Artikelsuche (Varianten) | Ermöglicht die Suche nach Varianten. Ist der Haken gesetzt, werden auch die Varianten zu einem gesuchten Artikel angezeigt. |
| Erweiterte Artikelsuche (Freifeld 1,2) | Ermöglicht in der Artikel-Übersicht nach Inhalten von Freifeld 1 und Freifeld 2 aus den Artikeln zu suchen. |
| Erweiterte Artikelsuche (Artikelnummern) | Ermöglicht die Suche nach den Artikelnummern von Kunden und Lieferanten in der Artikelübersicht, dem Adressstamm sowie in Belegpositionen. Die Artikelnummern von Lieferanten können beim Anlegen der Einkaufpreise angegeben werden, die Artikelnummern von Kunden beim Anlegen von Verkaufspreisen des Artikels. |
| Beschleunigte Artikelsuche | In der Suche in der Artikel-Übersicht wird nur nach Artikelnummer und Artikelbeschreibung DE gesucht. Diese Option überschreibt die Auswahl der oberen Haken zur Artikelsuche (z.B. Suche nach Freifeld / Kurztext). |
| Artikelbilder in Übersicht | Zeigt das Standard-Artikelbild in der Artikel-Listenansicht. Sollte kein Bild unter Artikel > Dateien hinterlegt sein, wird ein Musterbild eingeblendet. Hinweis: Diese Option verlangsamt den Aufbau der Artikel-Übersicht und sollte nur verwendet werden, wenn wenige Ergebnisse pro Seite angezeigt werden. |
| Artikelbaum in Übersicht | Zeigt den Artikelbaum links neben der Artikel-Liste in der Artikel-Übersicht. Es kann auf eine Kategorie geklickt werden um die Artikel-Liste nach dieser Kategorie zu filtern. |
| *Artikel Einheiten und Berechnungen* | |
| Gewicht aus JIT-Stückliste | Es wird bei Just-In-Time Stücklisten (= JIT-Stücklisten) nur das Gewicht aus dem Hauptartikel für das Auftragsprotokoll und den Paketmarkendruck verwendet. Ist die Option nicht aktiviert, so werden die Gewichte, sofern sie gepflegt sind, aus dem Hauptartikel und den Einzelpositionen der JIT-Stückliste aufaddiert. Dann könnte der Hauptartikel z.B. als Verpackungsteil o.Ä. dienen. Bei einer normalen Stückliste wird immer nur das Gewicht des Hauptartikels verwendet, wenn es gepflegt ist. Wurde kein Gewicht im Haupartikel gepflegt, so wird auch hier das Gewicht aller Einzelpositionen verwendet. |
| Standard Artikel Einheit | Wird als Einheit für alle Artikel eingeblendet, die keine individuelle Einheit im Artikel hinterlegt haben. |
| Gewichtseinheit | Einheit, in der das Gewicht systemweit dargestellt wird. Wenn nicht anderweitig gepflegt, ist die Standardgewichtseinheit kg. |
| Umrechnungsfaktor Gewicht | Der Umrechnungsfaktor zu Kilogramm. Beispiel: Für Tonne wäre es 0,001. Für Gramm wäre es 1000. |
| Standard Längeneinheit | Einheit in Zentimeter oder Inch: cm oder in. |

### Produktion (Systemeinstellungen)

Einstellungen zum Modul Produktion.

| Feldbezeichnung | |
| --- | --- |
| Verhalten Weiterführen Auftrag zur Produktion | Hier wird das Verhalten der zu produzierenden Stücklisten definiert, wenn diese aus einem Auftrag produziert werden sollen: - Unterstücklisten auflösen: Die Unterstücklisten einer Stückliste in der Produktion werden aufgelöst und angezeigt<br>- Unterstücklisten nicht auflösen: Die Unterstücklisten einer Stückliste in der Produktion werden nicht aufgelöst und angezeigt. Die Produktion beschränkt sich damit auf die oberste Stückliste<br>- Enthält eine zu produzierende Stückliste ebenfalls Stücklisten, die noch produziert werden sollen, so wird mit dieser Einstellung für jede Stückliste und Unter-Stückliste ein eigener Produktionsauftrag angelegt. Voraussetzung: Zu produzierende Stückliste ist als Produktionsartikel markiert (in den Stammdaten des Artikels einstellbar) Die Stückliste wurde aus einem Auftrag heraus in eine Produktion überführt. |
| Produktion nicht automatisch starten beim Weiterführen | Die Produktion wird beim Weiterführen aus dem Auftrag nicht automatisch gestartet. Der Start erfolgt über das Aktionsmenü in der jeweiligen Produktion. |
| Unterproduktionen mit Hauptproduktion abschließen | Unterproduktionen werden automatisch beim Abschliessen der Hauptproduktion mit geschlossen. Du solltest die Unterproduktionen in logischer Reihenfolge abarbeiten und zuletzt die Produktion als fertig bestätigen und abschliessen. |
| Produktionskorrektur nicht verwenden | Der Abschlussdialog mit der Produktionskorrektur wird nicht verwendet. |
| Für externe Produktionsartikel keine Produktionen anlegen | Für Artikel mit Einstellung "Externe Produktion" werden beim Weiterführen von Auftrag zu Produktion keine Produktionen angelegt. Ebenso nicht über die Produktion selbst "Unterproduktionen auflösen und anlegen". |

### Wareneingang (Systemeinstellungen)

Wareneingang - Art und Besonderheiten in der Warenannahme wie Artikeltyp, Erfassung mit Seriennummern, Großer oder schneller Wareneingang und Ansichten.

| Feldbezeichnung | |
| --- | --- |
| Große Paketannahme | Wareneingang in zwei Schritten Annahme + Distribution.Beim großen Wareneingang können z.B. auch eine Waage und Kamera verwendet werden, außerdem können die Nummern der Lieferantenrechnungen und Lieferantenlieferscheine erfasst werden.Eine Anleitung dazu finden Sie **hier**. |
| Nur Lagerartikel im Wareneingang | Im Wareneingang werden nur Artikel angezeigt, die als Lagerartikel definiert sind. |
| Annahme mit Kamera/Waage | Angebundene Kamera und Waage werden im Wareneingang genutzt. Funktioniert nur in Verbindung mit der Option 'Große Paketannahme'. |
| Wareneingang mit Zwischenlager | Internes Zwischenlager ist im Wareneingang vorausgewählt.Dadurch wird die Ware ins Zwischenlager eingelagert und kann über Lager > **Zwischenlager** an die echten Lagerplätze verteilt werden. |
| Aufträge zu Bestellungen im Wareneingang anzeigen | Nur für das Modul: Auftrag zu Bestellung. Ist der Haken gesetzt, kommt eine zusätzliche Spalte mit der Auftragsnummer im Wareneingang rein.Dies ist vor allem sinnvoll wenn man über einen Auftrag eine Bestellung anlegt. |
| Bildtyp beim Upload im Wareneingang | Standard Artikelbild (Shopbild) Standard Gruppenbild Etikettenbild Sonstiges Bild Datenblatt Druckbild (300dpi) Zertifikat Anhang (PDF) Sonstige Datei Deckblatt Anhang |
| Verhalten beim Scannen im Wareneingang | Nur Seriennummern erfassenErst Seriennummern dann Bemerkungen erfassen Erst Seriennummern dann Bemerkungen erfassen |

### Drucker (Systemeinstellungen)

Standard Drucker Vorauswahl für alle Mitarbeiter in deinem Team.

| Feldbezeichnung | |
| --- | --- |
| Standard Drucker | Voreinstellung für den Standard Dokumentendrucker, der für Druckvorgänge vorausgewählt ist. Kann pro Benutzer in den Benutzereinstellungen übersteuert werden. Wenn du keine physischen Drucker anbindest, bietet es sich an hier zunächst einen PDF Drucker einzustellen siehe **Anleitung**. |
| Standard Etikettendrucker | Voreinstellung für den Standard Etikettendrucker. Wenn du keinen Etiketten-Drucker anbindest, bietet es sich an hier zunächst einen PDF Drucker einzustellen - so können auch Etiketten als PDF Popup gedruckt werden. |
| Etikettendrucker Wareneingang | Voreinstellung für den Standard Etikettendrucker im Wareneingang (sofern dieser Wareneingangsprozess verwendet wird). |
| DMS Etiketten Wareneingang | Druck von Etiketten mit Barcode für Belege im Wareneingang an/aus. |
| Aufgaben Bondrucker | Auswahl eines angebundenen Bondruckers, auf dem die Aufgaben-Zettel ausgedruckt werden sollen. |

### Sonstiges (Systemeinstellungen)

Sonstige Systemeinstellungen.

| Feldbezeichnung | |
| --- | --- |
| Kleine Auflösung | Scrollbar bei kleinen Bildschirmen ausblenden. |
| Paketmarke mit Waage | Das Gewicht für die Paketmarke wird nicht über die im Artikel hinterlegten Gewichte bestimmt, sondern von einer angebundenen Waage. Voraussetzung: Anbindung einer Waage an der Versandstation. |
| Sprache bevorzugen | Deutsch, Englisch. |
| Export Button (CSV, PDF, Clipboard) unter Live-Tabelle | In vielen Live-Tabellen werden durch diese Option unterhalb Buttons für PDF, CSV, Excel Export eingeblendet. Hinweis: Es wird immer nur das exportiert, was in der Tabelle im Moment auf der Seite der Tabelle sichtbar ist - z.B. 10 von 1000 Einträge. Wenn mehr exportiert werden soll, kann die Anzahl der Elemente auf 1000 pro Seite gestellt werden. |
| Bestellvorschlag Menge | Wenn ein Artikel rechnerisch im Bestellvorschlag nicht nachbestellt werden muss und in keiner offenen Bestellung vorhanden ist, werden diese Artikel mit der Option im Bestellvorschlag ausgeblendet (Einkauf > Bestellvorschlag). |
| Mahnwesen mit Kontoabgleich | Der Zahlungsstatus von GS und RE werden automatisch geprüft und neu berechnet, sofern nicht manuell festgeschrieben in der Rechnung. Diese Prüfung wird gestartet wenn man das Mahnwesen aufruft, einen Zahlungseingang auf die RE/GS durchführt oder direkt in den Beleg klickt. |
| Anzahl Einträge Live-Tabelle | Hier können kann die Anzahl der angezeigten Listeneinträge in den Live-Tabellen (Artikelübersicht, Adressübersicht, Rechnungsübersicht usw.) festgelegt werden, z.B. 10, 25, 50, 200, oder 1000. Bei Wert 0 fällt Xentral auf den Standardwert von 10 zurück. Hinweis: Beim setzen der Einstellung (schneller Test verschiedener Werte, sind eventuell die Cookies im Browser zu löschen). |
| Erweiterte Adresssuche | In der Adress-Übersicht werden auch die Inhalte aus Freifeld 1 und Freifeld 2 aus der Adresse durchsucht. |
| Wiedervorlage - nur Mitarbeiter wählbar | Mit dieser Einstellung legst du fest, dass im Modul Wiedervorlagen nur Adressen mit der Rolle Mitarbeiter als der Bearbeiter einer Wiedervorlage eingetragen werden können. Wenn die Option deaktiviert ist, können alle Adressen, unabhängig von ihrer Rolle als Bearbeiter einer Wiedervorlage eingetragen werden. |
| Artikelbild im Versandzentrum anzeigen | Das Artikelbild wird auch in den Logistikprozessen am Packtisch angezeigt. |
| Gruppe für Bearbeiter | Zeigt in der Bearbeiter- / Innendienstauswahl in Belegen und dem großen Adressfilter nur die Adressen, die Mitglied dieser Gruppe sind.Falls leer, werden alle Adressen angezeigt. |
| Gruppe für Vertrieb | Zeigt in der Vertriebsmitarbeiterauswahl in Belegen und dem großen Adressfilter nur die Adressen, die Mitglied dieser Gruppe sind.Falls leer, werden alle Adressen angezeigt. |
| Auto. Proformarechnung bei Export "nur Lagerartikel" | Wenn man eine Proformarechnung im Versand automatisch erzeugen lässt oder weiterführen von Auftrag werden nur Lagerartikel mit in die Proformarechnung übernommen, keine Dienstleistungsartikel. |

### Belege (Systemeinstellungen)

Freigabe der Belege mit Zwischenabfrage, Informationsdichte und Anzeigen in Positionstabellen im Beleg, Individuelle Zusatzanzeigen z.B. Artikelbilder, Weiterführen der Belege und Workfloweinstellungen.

| Feldbezeichnung | |
| --- | --- |
| **Belege** | |
| Belege schnell anlegen ohne Zwischentabelle | Belege werden ohne Zwischenfrage nach vorhandenen Entwürfen direkt angelegt.Ohne diese Option gelangen Sie in eine Zwischenmaske um vorhandene Entwürfe weiter zu bearbeiten. |
| Belege schnell anlegen ohne manuelle Freigabe | Belege werden nach dem Anlegen automatisch freigegeben ohne, dass der Beleg in den Entwurfsmodus kommt und von dort freigegeben werden muss. Es wird direkt eine Belegnummer vergeben und der Status freigegeben gesetzt (aktuell in Angebot, Auftrag, Rechnung, Gutschrift, Lieferschein, Bestellung).Achtung: Sobald mehrere Projekte Anwendung finden, greift diese Option nicht mehr! |
| *Preise und Positionen* | - |
| Auswahl günstigster Verkaufspreise | Es wird in Belegen immer der günstigste Verkaufspreis vorgeschlagen.Ist der Haken nicht gesetzt, so muss der Verkaufspreis dem Einzelkunden explizit im Artikel zugeordnet werden.Ist das nicht der Fall, so nimmt das System weiterhin den niedrigsten Verkaufspreis. |
| Erweiterte Positionsansicht | Mit dieser Funktion lässt sich die Artikelbeschreibung in den Belegpositionen ein- oder ausblenden. Dadurch kann zwischen einer kompakten oder detaillierten Ansicht gewechselt werden. Die Beschreibung wird angezeigt in folgenden Belegen: Angebot, Auftrag, Rechnung, Gutschrift und Lieferschein. |
| Hersteller in Positionen anzeigen | Artikelbeschreibung ist in der Positionsansicht von Belegen sichtbar. Aktuell in Angebot, Auftrag, Rechnung, Gutschrift und Lieferschein. |
| Lagerbestand in Belegpositionen anzeigen | Der Lagerbestand, sowie die Anzahl der reservierten Artikel werden beim Einfügen von Positionen via Autocomplete im Tab Positionen im Auftrag und Lieferschein dargestellt. |
| Staffelpreise neu laden falls Menge geändert wird | Staffelpreis wird in die Position neu nachgeladen, wenn man die Positionsmenge ändert |
| Verkaufspreise auf VPE anpassen | Wenn der Artikel VPE Einheiten mit Verkaufs-Staffelpreisen hat, wird der Preis und die Menge je nach eingegebener Menge in den Positionen automatisch angepasst (aktuell in Aufträgen, Angeboten, Rechnungen, Gutschriften). Beispiel: VK: ab Menge 1 \| 10 Euro \| VPE 10 VK: ab Menge 10 \| 9 Euro \| VPE 10 Eingabe von 5: Menge ändert sich automatisch auf 10 und Einzelpreis 10 Eingabe von 13: Menge ändert sich automatisch auf 20 und Einzelpreis 9 Hinweis: Es muss eine VPE-Menge im Preis angegeben sein, damit die Funktion greift. |
| Einkaufspreise auf VPE anpassen | Wenn der Artikel VPE Einheiten mit Einkaufs-Staffelpreisen hat, wird der Preis und die Menge je nach eingegebener Menge in den Positionen automatisch angepasst (Bestellung). Beispiel: EK: ab Menge 1 \| 10 Euro \| VPE 10 EK: ab Menge 10 \| 9 Euro \| VPE 10 Eingabe von 5: Menge ändert sich automatisch auf 10 und Einzelpreis 10 Eingabe von 13: Menge ändert automatisch auf 20 und Einzelpreis 9 Hinweis: Es muss eine VPE-Menge im Preis angegeben sein, damit die Funktion greift. |
| Porto berechnen | Mit dieser Option können die Versandkosten eines Auftrags auf 0 gesetzt werden, sodass der Auftrag versandkostenfrei wird. Dazu muss eine Preisgruppe angelegt werden, zu der alle Kunden gehören, die versandkostenfrei einkaufen können sollen. In der Preisgruppe wird der Mindestbestellwert festgelegt (z.B. 50€), ab dem der Auftrag versandkostenfrei sein soll. |
| *Lieferschein Übernahme* | |
| Dienstleistungsartikel nicht zu Lieferschein übernehmen | Dienstleistungsartikel (Option in Artikel - Details) werden aus dem Auftrag nicht übernommen für den LS bei folgenden Aktionen: Manuelles Weiterführen des Auftrags zum Lieferschein Autoversand des Auftrags mit automatischer Lieferschein-Erstellung |
| Lieferschein Freitext / Interne Bemerkung | Der Freitext und die interne Bemerkung eines Lieferscheins tauchen als rote Meldung im Versandzentrum als Popup auf, das vom Mitarbeiter bestätigt werden muss. Funktioniert nur in Verbindung mit einem Logistikprozess (Projekt > Einstellungen > Logistik / Versand), der den Lieferschein in das Versandzentrum übergibt. |
| *Belegdaten* | |
| Abmessung im Dokument | Falls im Artikel Höhe/ Breite/ Länge hinerlegt wurde, wird dies in der Positionstabelle auf dem Beleg mit abgebildet. Beispiel: 'Abmessungen: 10,00 x 20,00 x 30,00' Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Bestellung, Gutschrift. |
| Adresse Typ im Dokument | Zeigt den Adress-Typ (Herr, Frau, Firma, eigenen Typ) in der ersten Zeile des Adressblocks auf dem Beleg an. Hinweis: Es wird der Typ der Adresse selbst angezeigt, nicht der Typ des Ansprechpartners. Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Gutschrift. |
| Artikel Einheit im Dokument | Blendet auf den Belegen eine Spalte für die Artikel-Einheit ein. Die Einheit kann in jedem Artikel individuell angegeben werden - wenn diese nicht gesetzt ist, wird die Standard-Artikeleinheit gezogen (siehe nächste Option). |
| Bearbeiter Telefon im Dokument | Die Telefonnummer des Bearbeiters wird auf dem Beleg in der Infobox dargestellt. Voraussetzung ist eine hinterlegte Telefonnummer im Feld 'Telefon' in der Adresse, die mit dem Benutzer verknüpft ist. Beispiel: 'Telefon: 01234/123123123' Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Gutschrift. |
| Bearbeiter E-Mail im Dokument | Die E-Mail des Bearbeiters wird auf dem Beleg in der Infobox dargestellt. Vorraussetzung ist eine hinterlegte E-Mail Adresse im Feld 'E-Mail' in der Adresse, die mit dem Benutzer verknüpft ist. Beispiel: 'E-Mail: maxmuster@test.de' Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Gutschrift. |
| Herstellernummer im Dokument | Falls eine Herstellernummer im Artikel hinterlegt ist, wird diese in der Positionstabelle auf dem Beleg mit abgebildet. Beispiel: 'Herstellernummer: 123456789' Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Bestellung, Gutschrift. |
| Projekt im Dokument | Falls die Projekt-Kennung vorhanden ist, wird sie auf dem Beleg in der Infobox dargestellt. Beispiel: 'Projekt: STANDARD' Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Bestellung, Gutschrift. |
| *Beleg weiterführen* | - |
| Dateien beim Weiterführen übernehmen | Wenn man Belege weiterführt, z.B. Auftrag zu Lieferschein, wird die Datei (unabhängig vom Dateityp) mit in den neuen Beleg übergeben. Es wird kein Duplikat der Datei erstellt. Die Datei wird nur im nächsten Beleg verknüpft. Funktion verfügbar für: Anfrage zu Angebot Angebot zu Auftrag Angebot zu Proformarechnung Auftrag zu Rechnung Auftrag zu Lieferschein Auftrag zu Produktion Auftrag zu Bestellung Bestellung zu Produktion Lieferschein zu Rechnung Rechnung zu Gutschrift |
| Original Beleg-PDF beim Versenden als Anhang einfügen | PDFs, die beim Abschicken-Dialog im Beleg mitgesendet werden, werden als Datei im Beleg gespeichert. Diese PDFs tauchen dann auch im Abschicken-Dialog als PDF Icon auf. |
| **Belegpositionen** | |
| Positionen mit Freifelder | Um sich Freifelder innerhalb von Beleg-Positionen anzeigen zu lassen, muss der Beleg ausgewählt werden, in dem das Freifeld angezeigt werden soll: Auszuwählen unter Administration > Einstellungen > Grundeinstellungen > Freifelder. Es wird der Name des Freifelds und der Inhalt in der Positionstabelle im Beleg dargestellt. Beispiel: 'Name von Freifeld 1: Inhalt von Freifeld 1' Funktion verfügbar in Angebot, Auftrag, Rechnung, Gutschrift, Kommissionierlauf, Lieferschein, Bestellung, Proformarechnung, Preisanfrage und Produktion. |
| Positionen mit EAN | Wenn im Artikelstamm eine EAN-Nummer hinterlegt ist, wird diese automatisch in der Positionstabelle des jeweiligen Belegs unter der Artikelbeschreibung angezeigt, z. B. im Format „EAN: 123456789“. Die Funktion ist ohne zusätzliche Aktivierung nutzbar und gilt für alle gängigen Belegarten wie Angebot, Auftrag, Rechnung, Lieferschein und Gutschrift. Voraussetzung ist lediglich, dass die EAN im Artikel gepflegt ist. |
| Positionen mit Zolltarifnummer | Haken gesetzt: Die Zolltarifnummer wird immer abgebildet in den Belegpositionen, wenn eine Zolltarifnummer vorhanden ist. Haken nicht gesetzt: Die Zolltarifnummer und Herkunftsland werden nur auf Rechnungen abgebildet, wenn diese auf Besteuerung Export stehen und eine Zolltarifnummer vorhanden ist. Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Gutschrift. |
| Positionen mit MHD | MHD eines Artikels wird falls vorhanden in der Positionstabelle auf Rechnung und Lieferschein dargestellt. Wichtig hierbei sind die Logistik-Einstellungen aus dem Projekt des Belegs zu MHD (Scannen im Versandzentrum / FIFO). Beispiel: 'MHD: 13.10.2020' Funktion verfügbar in Rechnung, Lieferschein. |
| Positionen mit Charge | Charge eines Artikels wird falls vorhanden in der Positionstabelle auf Rechnung und Lieferschein dargestellt. Wichtig hierbei sind die Logistik-Einstellungen aus dem Projekt des Belegs zu Chargen (Scannen im Versandzentrum / FIFO). Beispiel: 'Charge: 123456789 (2)' (In Klammern ist die Menge zu jeder Charge) Funktion verfügbar in Rechnung, Lieferschein. |
| Positionen mit Seriennummern | Wenn bei einem Artikel Seriennummern hinterlegt sind, werden diese automatisch in der Positionstabelle des Belegs angezeigt, z. B. im Format „S/N: 123456789“. Die Ausgabe erfolgt auf Rechnungen und Lieferscheinen. Ob Seriennummern dargestellt werden, hängt von den Logistik-Einstellungen im Projekt des jeweiligen Belegs ab (z. B. Scannen im Versandzentrum oder FIFO-Verfahren). Eine zusätzliche Aktivierung ist nicht notwendig – Voraussetzung ist lediglich, dass die Seriennummern für den Artikel gepflegt sind und im Beleg hinterlegt werden z.B. durch den Scanprozess am Packtisch oder manuell im Lieferschein eingetragen werden. |
| Herkunftsland immer ausblenden | Haken gesetzt: Das Herkunftsland wird nie angezeigt. Haken nicht gesetzt: Das Herkunftsland wird nur auf Rechnungen abgebildet, wenn diese auf Besteuerung Export stehen und eine Zolltarifnummer vorhanden ist. Funktion verfügbar in Angebot, Auftrag, Rechnung, Lieferschein, Gutschrift. |
| Lieferdatum in KW | Der Haken 'Kalenderwoche (KW)' als Lieferdatum ist standardmäßig in der Belegposition gesetzt für alle nach dem Aktivieren eingefügten Positionen. Funktion verfügbar in Angebot, Auftrag, Lieferschein, Rechnung, Gutschrift. |
| *Artikelbild Anzeige* | |
| Artikelbild in Auftrag PDF anzeigen | Artikelbild wird bei allen Aufträgen im PDF mit angezeigt. |
| Artikelbild in Lieferschein PDF anzeigen | Artikelbild wird bei allen Lieferscheinen im PDF mit angezeigt. |
| Artikelbild in Rechnung PDF anzeigen | Artikelbild wird bei allen Rechnungen im PDF mit angezeigt. |
| Artikelbild in Bestellung PDF anzeigen | Artikelbild wird bei allen Bestellungen im PDF mit angezeigt. |
| Artikelbild in Gutschrift PDF anzeigen | Artikelbild wird bei allen Gutschriften im PDF mit angezeigt. |
| Artikelbild in Angebot PDF anzeigen | Artikelbild wird bei allen Angeboten im PDF mit angezeigt. |
| *Dokumenten Beschriftungen* | |
| Dokumente Beschriftung Kundennummer | Die Bezeichnung für 'Kundennummer' in der Infobox auf Belegen kann hier umbenannt werden. Mit einem Klick auf das Weltkugel Icon können Übersetzungen für andere Sprachen dazu angelegt werden. |
| Dokumente Beschriftung Bestellnummer | Die Bezeichnung für 'Bestellnummer' in der Infobox auf Belegen kann hier umbenannt werden. Mit einem Klick auf das Weltkugel Icon können Übersetzungen für andere Sprachen dazu angelegt werden. |
| Dokumente Beschriftung Bearbeiter | Die Bezeichnung für 'Bearbeiter' in der Infobox auf Belegen kann hier umbenannt werden. Mit einem Klick auf das Weltkugel Icon können Übersetzungen für andere Sprachen dazu angelegt werden. |
| Dokumente Beschriftung Vertrieb | Die Bezeichnung für 'Vertrieb' in der Infobox auf Belegen kann hier umbenannt werden. Mit einem Klick auf das Weltkugel Icon können Übersetzungen für andere Sprachen dazu angelegt werden. |
| Bearbeiter und Vertrieb nicht füllen | Bei der Erstellung und Bearbeiten von Belegen, wird nicht automatisch das (leere) Bearbeiter- und Vertriebsfeld gefüllt, sondern muss manuell gefüllt werden. |
| Dokumente Bearbeiter ausblenden | Blendet den Bearbeiter im Infoblock des Beleges aus. |
| Dokumente Vertrieb ausblenden | Blendet den Vertriebsmitarbeiter im Infoblock des Beleges aus. |
| Beschriftung Internetnummer | Die Bezeichnung für 'Internetnummer' in der Infobox auf Belegen kann hier umbenannt werden. Mit einem Klick auf das Weltkugel Icon können Übersetzungen für andere Sprachen dazu angelegt werden. |
| Dokumente Beschriftung Internetnummer | Die Bezeichnung für 'Internetnummer' in der Infobox auf Belegen kann hier umbenannt werden. Mit einem Klick auf das Weltkugel Icon können Übersetzungen für andere Sprachen dazu angelegt werden. |
| Ansprechpartner in Rechnung, Gutschrift anzeigen | Der Ansprechpartner wird auf dem Beleg in der Rechnung und Gutschrift in der 2. Zeile im Adressblock ein-/ ausgeblendet. |
| Ansprechpartner in Angebot, Auftrag, Bestellung anzeigen | Der Ansprechpartner wird auf dem Beleg im Angebot, Auftrag und Bestellung in der 2. Zeile im Adressblock ein-/ ausgeblendet. |
| Bezeichnung Aktionscodes | Das Feld für die Eingabe der Aktionscodes im Auftrag, kann umbenannt werden. |
| Bezeichnung Kommissions-/Konsignationslager | Nur für das extra Modul 'Kommissions-/Konsignationslager'. Hier kann man das Feld im Auftrag für das Konsignationslager umbenennen. |
| *Dokumenten Typ-Beschriftungen* | |
| Beschriftung Abweichend Angebot | Im Angebot gibt es einen Haken um den Betreff des Angebot-Belegs umzubenennen. Mit der Option wird der Name der alternativen Dokumentenbezeichnung festgelegt. |
| als Standard | Mit dieser Option setzen Sie die alternative Bezeichnung im Angebot (Option drüber) als Standard. Dadurch ist der Haken beim Erstellen eines neuen Angebots immer gesetzt. |
| Beschriftung Abweichend Auftrag | Im Auftrag gibt es einen Haken um den Betreff des Auftrag-Belegs umzubenennen. Mit der Option wird der Name der alternativen Dokumentenbezeichnung festgelegt. |
| Beschriftung Abweichend Rechnung | In der Rechnung gibt es einen Haken um den Betreff des Rechnung-Belegs umzubenennen. Mit der Option wird der Name der alternativen Dokumentenbezeichnung festgelegt. |
| Beschriftung Abweichend Gutschrift | In der Gutschrift gibt es einen Haken um den Betreff des Gutschrift-Belegs z.B. in 'Stornorechnung' umzubenennen.Mit der Option wird der Name der alternativen Dokumentenbezeichnung festgelegt. Achtung: §14 UStG |
| Stornorechnung als Standard | Mit dieser Option setzen Sie die alternative Bezeichnung in der Gutschrift (Option drüber) als Standard. Dadurch ist der Haken beim Erstellen eines neuen Gutschrift immer gesetzt. |
| Beschriftung Abweichend Lieferschein | Im Lieferschein gibt es einen Haken um den Betreff des Lieferschein-Belegs umzubenennen.Mit der Option wird der Name der alternativen Dokumentenbezeichnung festgelegt. |
| Beschriftung Abweichend Bestellung | In der Bestellung gibt es einen Haken um den Betreff des Bestell-Belegs umzubenennen. Mit der Option wird der Name der alternativen Dokumentenbezeichnung festgelegt. |
| Beschriftung Abweichend Proformarechnung | In der Proformarechnung gibt es einen Haken um den Betreff der Proformarechnung-Belegs umzubenennen. Mit der Option wird der Name der alternativen Dokumentenbezeichnung festgelegt. |
| *Angebot Sales Einstellungen* | |
| Angebot Tage gültig bis | Hier wird die Anzahl an Tagen eingetragen, für die ein Angebot gültig sein soll. Das Enddatum wird dadurch automatisch gesetzt. Dieses kann über die Variable {GUELTIGBIS} ausgeben werden. |
| Angebot Tage Wiedervorlage | Nach Freigabe eines Angebots, wird automatisch eine Wiedervorlage angelegt, wenn die Tage > 0 sind. |
| Angebot Stage Wiedervorlage | 'Stage' der Wiedervorlage, die in einer automatischen Wiedervorlage aus dem Angebot für die Wiedervorlage übernommen werden soll. |
| Staffelpreise im Angebot bei Positionen anzeigen | Im Angebot in der Positionstabelle werden Staffelpreise eines Artikels untereinander dargestellt. Beispiel: ab 1 St. 10,00 EUR ab 5 St. 9,00 EUR ab 10 Str. 8,00 EUR Für 'St.'' wird die Artikeleinheit im Artikel selbst verwendet (z.B. Liter, etc.). Falls diese leer ist, wird die Standard Einheit in den Systemeinstellungen verwendet. Wenn diese auch leer ist, wird 'St.'' verwendet. |
| *Auftrag Einstellungen* | |
| Auftrag Barcodescanner Reiter einblenden | Im Auftrag erscheint ein neues Tab 'Barcodescanner'. Dort kann man bequem Artikel-Nr. / EANs abscannen und somit Artikel zu den Auftragspositionen hinzufügen. |
| Auftrag nicht abschließen beim Weiterführen zu Lieferschein und Rechnung | Wird der Auftrag manuell über das Aktionsmenü zu Lieferschein oder Rechnung weitergeführt, wird der Auftrag nicht auf den Status 'abgeschlossen' gesetzt. |
| Interne Bemerkungen im Auftrag-Minidetails editierbar | Die interne Bemerkung eines Auftrags lässt sich auch im Mini-Detail eines Auftrags in der Auftragsübersicht editieren. Dies funktioniert auch bei schreibgeschützten Aufträgen. |
| Markierung unbezahlte Aufträge | Unbezahlte Aufträge werden in der Auftragsübersicht rot markiert. Sobald ein Zahlungseingang auf den Auftrag oder dessen verknüpfte Rechnung einging bzw. die Rechnung auf manuell bezahlt gesetzt wird, ändert sich die Farbe von rot auf schwarz. |
| Unterstücklisten im Auftrag auflösen | Unterstücklisten die Just-In-Time Stücklisten sind, werden über alle ebenen aufgelöst. Funktionalität nur vorhanden, wenn die erste Ebene explodieren darf. Dazu Haken setzen bei: Projekteinstellungen > Just-In-Time Stücklisten auflösen/explodieren. |
| *Bestellung Einstellungen* | |
| Bestellung ohne Preise | Im Beleg Bestellung wird keine Bestellsumme ausgegeben. Die einzelnen Positionen sind mit dem Betrag 0 in der Positionstabelle dargestellt. |
| Bestellung mit Artikeltext | Die Artikelbeschreibung wird auf dem Beleg der Bestellung unterhalb des Artikelnamens in der Positionstabelle dargestellt. |
| Bestellung Eigene Artikelnummer erste Spalte | In der ersten Spalte der Positionstabelle der Bestellung wird die eigene Artikelnummer statt der Artikelnummer des Lieferanten (aus dem EK) gesetzt. |
| Bestellung Lange Artikelnummern | Im Beleg der Bestellung innerhalb der Positionstabelle werden der Artikelname und die Artikelbeschreibung um eine Zeile nach unten verschoben, so dass lange Artikelnummern nicht in den Namen oder in die Beschreibung hineinschreiben. Hinweis: Diese Option funktioniert nur für Artikelnummern des Lieferanten in der ersten Spalte. |
| Bestellung automatisch abschließen | Schliesst Bestellungen automatisch ab, sobald die gesamte Ware der Bestellung über den Wareneingang als geliefert markiert ist. Wenn man in die Bestellungsübersicht klickt, werden die offenen Bestellungen überprüft, ob diese mit der Option auf abgeschlossen gesetzt werden können. Außerdem gibt es einen Prozessstarter (bestellungabschliessen), der dies im Hintergrund ebenfalls überprüft. |

### Tabellen Zusatzspalten (Systemeinstellungen)

Einstellungen der Xentral Tabellenansichten - Artikel- und Belegtabellen z.B. Auftrag, Rechnung.

**Zusatzfelder Artikeltabelle**

| Feldbezeichnung | |
| --- | --- |
| VK netto | Anzeige Artikel Verkauspreis netto. Standardpreis. |
| VK brutto | Anzeige Artikel Verkauspreis brutto. Standardpreis, Preisgruppen Preise kannst du in der Gruppe einsehen. |
| EK netto | Anzeige Artikel Einkaufspreis netto. Standardpreis. |
| EK brutto | Anzeige Artikel Einkaufspreis brutto. Standardpreis. Wenn du einen Artikel bei mehreren Lieferanten beziehst, kannst du alle Preise im Artikel oder in der Preisübersicht für den speziellen Lieferanten in den Stammdaten einsehen. |
| Pseudo Preis / UVP | Anzeige der Preisangabe für die Unverbindliche Preisempfehlung (UVP). |
| Lager verfügbar | Berechnete Lagerverfügbarkeit. Diese Zahl findest du ebenfalls im Artikel in der Lagerinformation. Du siehst hier Lagerbestand, Reservierungen, offene Aufträge, berechneten Bestand, Verkaufbare Stück, berechneten Bestand mit offenen Bestellungen. |
| in Zulauf | Stückzahlen, die über deinen Lieferanten bereits im Zulauf sind. Mit beinberechnet werden abgeschickte und freigegebene Bestellungen. |
| im Sperrlager | Artikel Menge verbucht in das Sperrlager. |
| in Produktion | Artikel Menge in Produktion. Z.B. wenn du hunderter Charge für dein eigenes Sortiment vorproduzierst oder Kundenspezifische Produkte auf Abruf bereitstellst und mit deinen Kunden Rahmenverträge abgeschlossen hast. |
| Eigenschaften | Hinterlegte Eigenschaft und der dazugehörige Wert des Artikels. |
| EAN | Anzeige der EAN (= europäische Artikelnummerierung) des Artikels. |
| Hersteller | Anzeige des Herstellers des Artikels. |
| Hersteller Nr. | Anzeige der Herstellernummer des Artikels. |
| Zolltarifnummer | Anzeige der Zolltarifnummer des Artikels. |
| Freifeld 1-40 | Anzeige eines Freifeld Inhalts für deinen Artikel. |

**Zusatzfelder Adresstabelle**

| Telefon | Anzeige der Telefonnummer. |
| --- | --- |
| Fax | Anzeige der Faxnummer. |
| Mobil | Anzeige der Mobilfunknummer. |
| Ansprechpartner | Anzeige des Ansprechpartners der Adresse. |
| Abteilung | Anzeige der Abteilungsinformation. |
| Ust-ID | Anzeige der Ust-ID des Kunden. |
| Steuernummer | Anzeige der Steuernummer. |
| GLN | Anzeige der GLN. |
| Mitarbieternummer | Anzeige der Mitarbeiternummer dieser Adresse (sofern eine Mitarbeiternummer vorhanden ist). |
| Freifeld 1-20 | Anzeige eines Freifeld Inhalts für die Adresse. |
| Feldbezeichnung | |

**Zusatzfelder Auftragstabelle**

| Internet | Shop- oder Marktplatz ID. Diese ID wird beim Shopimport zu Xentral mit übernommen und ist in der Suche auch durchsuchbar. Die Nummer kann im Auftrag manuell gepflegt werden. |
| --- | --- |
| Wunsch Liefertermin | Wunsch Liefertermin des Kunden. |
| Auslieferung Lager | Dein Interner Auslieferungstermin. Z.B. zwei Tage vor Kunden Wunsch Liefertermin, so dass das Paket rechtzeitig ankommt. |
| Versandart | Versandart / Versanddienstleister. Wird im Auftrag über den Shopimport oder manuell oder über die Stammdaten vergeben. |
| Vertrieb | Mitarbeiter/In aus dem Vertrieb. Alternativ der Importkanal. |
| Bearbeiter | Interner Bearbeiter/In. |
| Betrag netto | Gesamtbetrag Auftragssumme netto. |
| Feldbezeichnung | |

**Zusatzfelder Rechnungstabelle**

| Internet | Shop- oder Marktplatz ID. Diese ID wird beim Shopimport zu Xentral mit übernommen und ist in der Suche auch durchsuchbar. Die Nummer wird aus dem Auftrag in die Rechnung übernommen. Sie ist im Auftrag bearbeitbar. |
| --- | --- |
| Versandart | Versandart / Versanddienstleister. Wird vom Auftrag in die Rechnung übernommen oder aus den Stammdaten gezogen. |
| Betrag (netto) | Gesamtbetrag Rechnungssumme netto. |
| Auftrag | Zugehörige Auftragsnummer. |
| Feldbezeichnung | |

**Zusatzfelder Lieferscheintabelle**

| Internet | Auftragsnummer bei der Übertragung aus einer Shop Plattform. |
| --- | --- |
| Feldbezeichnung | |

**Zusatzfelder Produktionstabelle**

| Auslieferung Lager | Datum an dem die produzierte Ware in das Lager übergeben wird. |
| --- | --- |
| Bereitstellung Start | Datum an dem die benötigten Artikel an die Arbeitsstation in der Produktion übergeben werden. |
| Produktion Start | Startdatum der Produktion. |
| Produktion Ende | Enddatum der Produktion. |
| Charge | Charge der Produktion. |
| MHD | Mindesthaltbarkeitsdatum der produzierten Artikel. |
| Artikelkategorie | Kategorie der produzierten Artikel. |
| Feldbezeichnung | |

**Zusatzfelder Bestellungstabelle**

| Bestätigtes Lieferdatum | Vom Lieferanten bestätigtes Lieferdatum. Bestellungen können als bestätigt gesetzt werden. Zusätzlich kannst du ein Datum eingeben, auf das sich der Lieferant festgelegt hat. |
| --- | --- |
| Wunschlieferdatum | Dein Wunschlieferdatum, das du beim Absenden der Bestellung gesetzt hast. |
| Feldbezeichnung | |

**Zusatzfelder Verbindlichkeitentabelle**

| Rechnungseingangsdatum | Datum, an dem die Lieferantenrechnung eingegangen ist. Desweiteren gibt es noch das Rechnungsdatum. Du kannst in der Buchhaltung einstellen, welches Datum für den Vorsteuerabzug verwendet werden soll. |
| --- | --- |
| Fälligkeitsdatum | Datum, zu dem die Verbindlichkeit zur Zahlung fällig ist. |
| Kontierungssumme | Summe deiner vorgenommen oder automatischen Kontierung. Hier kannst du überprüfen, ob der Verbindlichkeiten Betrag mit der Kontierung für diene Buchhaltung übereinstimmt und Null ergibt. |
| Feldbezeichnung | |

### Zeiterfassung (Systemeinstellungen)

Einstellungen für die Zeiterfassungs-Module.

| Feldbezeichnung | |
| --- | --- |
| Buchen auf anderen Mitarbeiter erlauben | Zeigt die Option 'für anderen Mitarbeiter Zeit buchen' in der 'Zeiterfassung buchen' Oberfläche an, mit der Sie Zeiten auch für Kollegen erfassen können. |
| Feld Interner Kommentar sichtbar | Zeigt ein zusätzliches Textfeld für interne Bemerkungen in der 'Zeiterfassung buchen' Oberfläche an. |
| Feld Ort sichtbar | Zeigt ein zusätzliches Textfeld für eine Ortsangabe in der 'Zeiterfassung buchen' Oberfläche an. |
| Erweiterte Zeitangabe | Zeigt folgende zusätzliche Optionen in der 'Zeiterfassung buchen' Oberfläche an: - Kunde<br>- Auftrag<br>- Auftragsposition<br>- Produktion (falls Modul vorhanden)<br>- Serviceauftrag (falls Modul vorhanden)<br>- Abrechnen Haken Setzt Zeit zum Abrechnen |
| abrechnen vorausgewählt | Der Haken für 'Abrechnen' wird in der 'Zeiterfassung buchen' Oberfläche standardmäßig gesetzt. |
| Zeiterfassung schließen | Wenn der Haken gesetzt ist, können Sie die Anzahl der Tage eingeben, wie viele Tage in der Vergangenheit eine gebuchte Zeit liegen darf.Wenn ein Mitarbeiter versucht eine ältere Buchung zu tätigen, bekommt er daraufhin eine Fehlermeldung.Um bestimmte Benutzer von dieser Regel auszunehmen können Sie dem Benutzer das Rechte 'bearbeitenerlauben' im Rechteblock 'Zeiterfassung' geben. |
| Zeiterfassungspflicht | Wenn der Haken gesetzt ist und keine Zeiten am letzten Werkstag gebucht wurden, wird der Mitarbeiter beim Login auf die Zeiterfassungsoberfläche geleitet. |

### Auftragsampeln ausblenden (Systemeinstellungen)

Auftragsampel - Individualisierung und Anzeige der Auftragsampeln zur Steuerung.

| Feldbezeichnung | |
| --- | --- |
| Lager | Anzeige welche Artikel lagernd sind und verfügbar für den Versand. |
| Porto | Anzeige, ob der Auftrag einen Versandartikel beinhaltet. Fehlen des Versandartikels (= fehlende Versandkostenberechnung) führt zu einer orangen Ampel. Versandkosten können auch mit Null Euro eingetragen werden. |
| UST | Innergemeinschaftlicher Erwerb. Ist die Vat ID (= Umsatzsteuernummer) des anderen Unternehmers geprüft. Die Steuerschuld liegt ansonsten bei dir. |
| Zahlung | Ist die Zahlung eingegangen oder der Auftrag als bezahlt markiert (kann auch eine automatische Markierung in der Zahlweise beim Auftragsimport von einem Shop sein). |
| Nachnahme | Prüfung Nachnahme Artikel plus Versandkostenartikel. |
| Autoversand | Freigabe für einen automatischen Losgistikprozess (= Versandprozess) z.B. den Autoversand. Je nach Einstellung werden die Aufträge stündlich oder z.B: um 8:00 Uhr übergeben. Wenn du einen komplett grünen Auftrag blockieren willst, kannst du das über die Autoversandfreigabe steuern. |
| Kundencheck | Wenn du einen Kundencheck pro Auftrag einstellen möchtest, kannst du das über diese Ampel steuern. Z.B. bei hohen Geldbeträge auf deinem B2B Projekt. |
| Liefertermin | Liefertermin ist erreicht bzw. die der Termin für Auslieferung Lager. Ist die Ampel grün, darf der Auftrag heute versendet werden. |
| Kreditlimit | Festlegung des Kreditlimits in den Kunden Stammdaten. Das Kreditlimit greift, wenn die Summe der aktuell offenen Rechnungen das eingetragene Limit übersteigen. |
| Liefersperre | Festlegung einer Liefersperre in den Kunden Stammdaten. Die Liefersperre kann gesetzt werden. Sobald ein neuer Auftrag auf diese Kundennummer eingetragen wird, wird die Ampel orange und blockiert die Weitergabe an die Logistik. Alternativ könntest du zusätzlich die Zahlungsweise auf Vorkasse stellen. Sofern die Bestellung von einem Shop eingeht kannst du hier ggf. nicht beeinflussen welche Zahlungsart gewählt wurde. |
| Produktion | Zu diesem Auftrag existiert eine abgeschlossene Produktion. Die Ware ist fertig konfektioniert/ produziert und eingelagert. |

### Adresse (Systemeinstellungen)

Adressbearbeitung Zwischenspeicher Funktion.

| Reihenfolge Zwischenspeicher | Bestimmt die Reihenfolge und die Daten, die Sie mit dem 'Adresse in Zwischenspeicher' Button direkt in der Adresse in den Zwischenspeicher nehmen können. Mit Ctrl/CMD + V können Sie den Inhalt dann wieder ausgeben. |
| --- | --- |
| Adresse Vorlage | Hier können Sie eine Adresse angeben, die als Vorlage für neu angelegte Adressen gilt (nicht über die Importzentrale). Es werden beim Neu-Anlegen einer Adresse die meisten Felder der Musteradresse unter Adresse > Details übernommen. |
| Feldbezeichnung | |

### Servereinstellungen (Systemeinstellungen)

Server Settings (Achtung: abgekündigt).

| Feldbezeichnung | |
| --- | --- |
| Server-URL | Achtung: nur für alte Systeme mit eigener Installtion vor 2021. Server URL und Port. (Legacy und abgekündigt). |

### LDAP Verzeichnis (Systemeinstellungen)

LDAP Settings (Achtung: abgekündigt)

| Feldbezeichnung | |
| --- | --- |
| LDAP URI | Die URI um Ihren LDAP-Client zu erreichen. |
| LDAP RDN | Hauptgruppe der Nutzer, die sich einloggen können. |
| LDAP Basis DN | Definiert, wo im Verzeichnisbaum abwärts die Suche nach bestimmten Objekten gestartet werden soll. |
| LDAP Filter | Innerhalb der Verzeichnisse kann nach hinterlegten Daten gefiltert werden. Z.B. kann man prüfen ob der Benutzer der passenden Gruppe angehört und ob es sich überhaupt um eine Person handelt. (Die Angabe des LDAP Filters ist Pflicht sonst klappt die Authentifzierung nicht). |

### DSGVO Einstellungen (Systemeinstellungen)

DSGVO

| Feldbezeichnung | |
| --- | --- |
| E-Mail nicht dem Versandunternehmen übergeben | Das Feld E-Mail wird nicht dem Versanddienstleister mitgegeben.Beim Erstellen einer Paketmarke wird das Feld mit der E-Mail Adresse ausgefüllt aber nicht übermittelt. |
| Telefon nicht dem Versandunternehmen übergeben | Das Feld Telefon wird nicht dem Versanddienstleister mitgegeben.Beim Erstellen einer Paketmarke wird das Feld mit der Telefonnummer ausgefüllt aber nicht übermittelt. |

### Sicherheit (Systemeinstellungen)

Sicherheitseinstellungen

| Feldbezeichnung | |
| --- | --- |
| Externe URL im Ticketsystem nicht laden | Im Ticketsystem werden keine externen URLs geladen um Angriffen vorzubeugen. |
| Zusätzliche CSP Header | Zusätzliche CSP Header um die Einbindung externer Inhalte zu erlauben. |

### System E-Mails (Systemeinstellungen)

E-Mail Log- und Statuseinstellungen.

| Feldbezeichnung | |
| --- | --- |
| System E-Mails abschalten | Systeminterne E-Mails zu Lagersync Statusmeldung, etc. werden nicht mehr ausgeführt. |
| System E-Mails Empfänger | E-Mail Adresse, an die die System E-Mails gehen sollen. Die Option drüber zum Abschalten der System-E-Mails darf natürlich nicht aktiviert sein. |

### Beschleunigung / Limitierungen (Systemeinstellungen)

Systemperformance und Prozessteuerung Einstellungen

| Feldbezeichnung | |
| --- | --- |
| Begrenzen Belegetabellen | Schaltet sich automatisch ein, wenn es mehr als 5000 Belege + 1 Sekunde Abfragedauer ODER mehr als 10000 Belege in einer Belegübersicht sind. Begrenzt auf doppelte Anzahl von Anzeige (Seite 10) - ist nur bei der Anzahl der gefunden Daten sowie Anzahl der Seiten unterhalb der Live-Tabelle wichtig Für die Performance bei großen Datenmengen ist es von Vorteil die Option zu aktivieren Es werden bei der Suche trotzdem alle Belege berücksichtigt - die Suche läuft nur gestaffelt ab. |
| Begrenzen Artikeltabelle | Schaltet sich automatisch ein, wenn es mehr als 5000 Artikel + 1 Sekunde Abfragedauer ODER mehr als 10000 Artikel sind Wenn man die Option einmal rausnimmt, dann wird die Option nicht mehr automatisch gesetzt. |
| Begrenzen Adressetabelle | Schaltet sich automatisch ein, wenn es mehr als 100 offene Aufträge sind, die für den Autoversand geprüft werden müssen. Nimmt die ältesten Aufträge, prüft die ersten ältesten 100 Aufträge (für Autoversand Plus). Wenn es deutlich mehr sind, sollte der Cronjob (autoversand_plus) öfters laufen. Standard sollte 100 eingetragen sein - 0 bedeutet keine Begrenzung. |
| Begrenzen Autoversand | Begrenzen Autoversand auf X Datensätze Anzahl der maximal zu prüfenden Aufträge beim Autoversand (0 bedeutet keine Begrenzung) - Schaltet sich automatisch ein, wenn es mehr als 100 offene Aufträge sind, die für den Autoversand gecheckt werden müssen<br>- Nimmt die ältesten Aufträge, prüft die ersten ältesten 100 Aufträge (für Autoversand Plus) ⇒ Wenn es deutlich mehr sind, sollte der Cronjob öfters laufen (autoversand_plus)<br>- Standard sollte 100 eingetragen sein - 0 ist keine Begrenzung |
| Versandmails und Rückmeldung an Shop per Prozessstarter | Anzahl X pro Durchlauf. Mails (0 bedeutet keine Begrenzung) - Sendet die Trackingnummer über einen Prozessstarter an den Shop. Dies ist sinnvoll wenn über einen Fulfiller mehrere Trackingnummern auf einmal geliefert werden und der Shop nicht so viele Requests verarbeiten kann. Bzw. wenn die Shop-API von sich aus langsam ist, muss beim Scannen der Paketmarke nicht lange gewartet werden, bis der Shop die Trackingnummer verarbeitet hat.<br>- Schaltet sich automatisch ein, wenn es mehr als 100 Aufträge sind, die zurückgemeldet werden müssen.<br>- Statusrückmeldung und Tracking an Shop<br>- Wenn deutlich mehr Trackingnummern zurückgemeldet werden müssen, dann sollte der Cronjob öfters laufen (shop_rueckmeldungen) |
| Schnellsuche aktivieren | Aktiviert sicht automatisch bei mehr als 5000 Artikel + 1 Sekunde Abfragedauer ODER mehr als 10000 Blendet im Artikel ein neues Suchfeld ein. In diesem Suchfeld muss mit Enter bestätigt werden für einen Suchbegriff, womit keine überflüssigen Such-Requests an die Datenbank geschickt werden und sich so keine Such-Requests anstauen, die die Suche verlangsamen. |
| Für Autoversand gesperrte Aufträge mitberechnen | Berechnet die Auftragsampeln gesperrter Aufträge mit. Achtung: eine große Menge nicht stornierter aber gesperrter Aufträge kann die Berechnung deutlich verlangsamen. Wenn du gesperrte Aufträge grundsätzlich nicht stornierst solltest du die Ampeln nicht mitberechnen. |
| Anzeige gefiltert von deaktivieren | Deaktiviert die Berechnung unterhalb der Übersichtstabellen, wie viele Ergebnisse von allen Artikel angezeigt werden. Diese Berechnung kann bei vielen Daten in der Tabelle zu erheblichen Ladezeiten führen und sollte deswegen bei mehreren Hundertausend Daten in einer Tabelle (z.B. Artikel) mit dem Haken deaktiviert werden. |
| Prozessstarter limitieren | Maximal Anzahl X (Standard 3) |
| Polling-Zeit erhöhen | Auf X Sekunden (Standard 5) |
| Report abfragen abbrechen | Nach X Sekunden (Standard 300) |

### Locale (Systemeinstellungen)

Lokalisation Zeit-, Datums- und Zahlenformate.

| Feldbezeichnung | |
| --- | --- |
| Zahlenformat | Einstellungen für die Lokalisierung z.B. Niederlassung in einem anderen Land. Einstellung des globalen Zahlenformats 1.234,56 oder 1,234.56. |
| Datumformat | Einstellungen für die Lokalisierung z.B. Niederlassung in einem anderen Land. Einstellung des globalen Datumformats: dd.mm.YYYY mm/dd/YYYY dd-mm-YYYY mm-dd-YYYY dd/mm/YYYY YYYY/MM/DD |
| Zeitformat | Einstellungen für die Lokalisierung z.B. Niederlassung in einem anderen Land. Einstellung für das Zeitformat: HH:mm:ss (13:00:99) hh:mm:ss am/pm (01:00:00 PM) |