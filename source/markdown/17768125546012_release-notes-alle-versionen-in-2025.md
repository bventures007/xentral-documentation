## 25.43 Release notes

### Release version 25.43.5

*Veröffentlichungsdatum: 13. November 2025 *#### Fehlerbehebungen **Adressen (PF-4414)**

Ein Problem mit der Standardeinstellung der Sprache bei der Erstellung eines neuen Kontakts wurde behoben.

### Release version 25.43.4

*Veröffentlichungsdatum: 11. November 2025 *#### Verbesserungen **(FFU-6117)**

Die Telemetriefunktionen wurden verbessert.

#### Fehlerbehebungen **Finanzbuchhaltung Export (FAC-5100)**

Ein Problem wurde behoben, bei dem im Buchhaltungsexport die Buchungsschlüssel (BU-Schlüssel) in der exportierten Datei fehlten.

### Release version 25.43.3

*Veröffentlichungsdatum: 11. November 2025 *#### Neue Funktionen **Iam (PF-4393)**

Projektbereichsindikator wurde zu Bereichskategorien hinzugefügt.

#### Verbesserungen **Systemupdate (PF-4378, PIM-2100)** Der Informationsbereich des Beta-Programms wurde aktualisiert. ** Vorlage (PF-2882)** Standardtext für Aufträge in Textvorlagen wurde angepasst. ** Geschäftskonten (FAC-3311)**

Die Fidor Bank hat seit Juli 2023 ihren Betrieb eingestellt und wird nicht mehr unterstützt. Alle Verweise auf die Fidor-Integration wurden entfernt. Bestehende Fidor-Verbindungen mit Transaktionen werden jetzt auf CSV-Import standardisiert. Bestehende Verbindungen ohne Transaktionen werden entfernt.

#### Fehlerbehebungen **Exportbelegepositionen (FAC-5091, PF-4381)** Ein Fehler, der das Herunterladen von Dokumentpositionen im Exportbelegepositionen-Modul verhinderte, wurde behoben. Positionen sind jetzt wie erwartet herunterladbar. ** Geschäftsbrief Vorlagen (FAC-5073, PF-4380)**

Ein Fehler, der eine falsche Datumsanzeige im ZahlungOk-Geschäftsbriefvorlage verursachte, wurde behoben. Das Datum wird jetzt korrekt angezeigt.

## 25.42 Release notes

### Release version 25.42.4

*Veröffentlichungsdatum: 06. November 2025 *#### Verbesserungen **Amazon (FAC-5187)**

Ein Feature-Flag verbessert die Konsistenz des Auftragimports während Zeiten hoher Durchsatzrate, wenn es aktiviert ist.

### Release version 25.42.3

*Veröffentlichungsdatum: 06. November 2025 *#### Fehlerbehebungen **Reporting (XIN-2618)**

Es wurde ein Problem behoben, bei dem der Datumsauswahler für Berichtsvariablen im SQL-Editor des Berichtsmoduls nicht korrekt sichtbar war.

### Release version 25.42.1

*Veröffentlichungsdatum: 06. November 2025 *#### Neue Funktionen **Reporting (XIN-2583)** Eine neue Trennzeichenoption (Tab) wurde zu den CSV-Exporten im Reporting-Modul hinzugefügt. ** Adressen (PF-2941)**

Eine API zum Aktualisieren von Kundenkontaktpersonen wurde hinzugefügt.

#### Fehlerbehebungen **Drucker (PF-4389)** Ein Problem mit veralteter Benachrichtigung des NextGen-Polls für Printer-Downloads wurde behoben. ** Auftrag (FFU-3602)** Es wurde ein Problem behoben, bei dem die Suche nicht richtig funktionierte. ** N/a (FE-819)** Ein Problem wurde behoben, bei dem das Datumswähler-Dropdown in einigen Fällen nicht sichtbar war. ** N/a (FAC-5071, IMPAPI-821)**

Ein Fehler, der gelegentlich das Herunterladen von Finanzberichten verhinderte, wurde behoben.

## 25.41 Release notes

### Release version 25.41.6

*Veröffentlichungsdatum: 28. Oktober 2025 *#### Fehlerbehebungen **Artikel (PIM-3208, FFU2-760)**

Sortierprobleme bei Artikelbildern in der Listenansicht wurden behoben.

### Release version 25.41.5

*Veröffentlichungsdatum: 29. Oktober 2025 *#### Neue Funktionen **SalesOrder API (PF-4325)**

Ein Fallback-Mechanismus wurde eingeführt, der das Standardsprachen-Alias verwendet, wenn beim Import eines Auftrags kein Alias für den angegebenen Sprach-ISO-Code vorhanden ist.

#### Verbesserungen **Zahlungseingang (FAC-5052)** Der generische Gutschriftenabgleichsservice schließt jetzt Amazon-Geschäftskonten aus, um Konflikte mit deren spezifischer Abgleichslogik zu vermeiden. ** Email Service (PF-3490)** Benutzer mit der Berechtigung email:logs können jetzt die Liste der E-Mail-Protokolle anzeigen. ** N/a (FE-805)** Datenspalten in NextGen-Tabellen werden jetzt im Format TT.JJ.MMMM angezeigt. ** E-invoice (FAC-4931)** Die Exportlogik für Schlussrechnungen im kommerziellen Bereich wurde angepasst, um den EN16931/XRechnung-Standards zu entsprechen. Negative Preise auf Positionsebene werden durch Verweise auf zuvor in Rechnung gestellte Teilbeträge und das TotalPrepaidAmount-Feld ersetzt. Alle Kopf- und Gesamtfelder sind jetzt vollständig und mathematisch konsistent, um den Geschäftsregeln BR-27 und BR-28 zu entsprechen, für eine nahtlose Erstellung und den Austausch von Schlussrechnungen innerhalb der PEPPOL-Umgebung. ** POS (FAC-4611)**

Die Formatierung bleibt beim Bearbeiten eines Artikels im POS erhalten.

#### Fehlerbehebungen **N/a (CE-274, FFU2-786)** Ein Problem im Lagerbestandmodul wurde behoben, bei dem das Mindesthaltbarkeitsdatum falsch gesetzt wurde. ** New Pos (FAC-5002)** Das POS verhindert jetzt das Erstellen von Anzahlungsrechnungen, wenn kein Anzahlungsartikel für das ausgewählte Projekt definiert ist. Die Schaltfläche ist deaktiviert und ein Tooltip führt die Benutzer zu den richtigen POS-Einstellungen, um falsche Rechnungen zu vermeiden und die Konsistenz des Projekts sicherzustellen. ** New Pos (FAC-4994)** Teilzahlungen im POS erzeugen jetzt korrekt partielle Rechnungen, die mit dem ursprünglichen Auftrag verknüpft sind. Der Auftrag bleibt für zusätzliche Zahlungen offen und wird erst mit einer Schlussrechnung abgeschlossen. Ein Anzahlungsartikel muss in den Projekteinstellungen definiert sein. ** Email Service (FAC-4983)**

Ein seltener Fall wurde behoben, bei dem E-Mails mit leeren Anhängen versendet wurden.

## 25.40 Release notes

### Release version 25.40.3

*Veröffentlichungsdatum: 22. Oktober 2025 *#### Verbesserungen **Shopexporter (ECOM-5174)**

Der API-Endpunkt der Vertriebskanäle wurde verbessert, um Konfigurationen für das Frontend zu ermöglichen.

#### Fehlerbehebungen **Taxdoo Schnittstelle (FAC-5030)**

Zuvor wurde nur eine Rabattzeile pro Auftrag an Taxdoo übertragen, selbst wenn mehr vorhanden waren. Dieses Problem wurde behoben — alle Rabattpositionen sind nun korrekt in die Datenübertragung einbezogen.

### Release version 25.40.2

*Veröffentlichungsdatum: 22. Oktober 2025 *#### Verbesserungen **Zahlungseingang (FAC-4980)** Zahlen werden nun richtig mit dem entsprechenden Dezimalpunkt angezeigt, und das System erlaubt jetzt die Verwendung von Kommas bei der Suche und Filterung im Zahlungseingangsmodul. ** Rechnung (FAC-4963)** Schweizer QR-Codes nutzen jetzt strukturierte Adressdaten gemäß der Spezifikation 2.3 zur Sicherstellung der Compliance nach dem 21.11.2025. Dies beinhaltet eine automatische Trennung von Straße und Hausnummer durch eine Parsing-Funktion für das neue Schweizer QR-Format. ** Amainvoice (FAC-4720)**

Die Leistung der Datentabellen in der AMA-Rechnung wurde verbessert.

#### Fehlerbehebungen **Auftrag (FFU-5870)** Die Ampelberechnung für Auto-Ship erlaubt ist für Teilaufträge und verschachtelte Stücklistenartikel behoben. ** Zahlungseingang (FAC-4977)** Das Löschen einer geteilten Zahlung beeinflusst nicht mehr die Werte der ursprünglichen Zahlung. Das Löschen aller geteilten Transaktionen stellt die Transaktion auf ihren ursprünglichen Betrag wieder her. ** Zahlungseingang (FAC-4060)**

Die Anzeige von Beträgen bei Import von Zahlungseingängen, die nicht für Skonto berechtigt waren, wurde behoben.

## 25.39 Release notes

### Release version 25.39.6

*Veröffentlichungsdatum: 22. Oktober 2025 *#### Verbesserungen **Shopexporter (ECOM-5174)**

Der API-Endpunkt für Verkaufskanäle wurde verbessert, um Konfigurationsmöglichkeiten für das Frontend zu unterstützen.

#### Fehlerbehebungen **Taxdoo Schnittstelle (FAC-5030)**

Der Datentransfer zu Taxdoo umfasst jetzt alle Rabattpositionen korrekt, wodurch die vorherige Einschränkung behoben wurde, bei der nur eine einzige Rabattzeile pro Auftrag übertragen wurde.

### Release version 25.39.5

*Veröffentlichungsdatum: 16. Oktober 2025 *#### Verbesserungen **(FFU-6026)**

Die Telemetrie wurde verbessert.

#### Fehlerbehebungen **Berichtswesen (XIN-2565)**

Ein Fehler im Berichtswesen-Modul wurde behoben, der Benutzer mit eingeschränktem Zugriff daran hinderte, zulässige Berichte herunterzuladen.

### Release version 25.39.4

*Veröffentlichungsdatum: 14. Oktober 2025 *#### Fehlerbehebungen **Abschlagsrechnung (FAC-4967)**

Das Problem, das die Erstellung der Schlussrechnung verhinderte, wurde behoben.

### Release version 25.39.3

*Veröffentlichungsdatum: 14. Oktober 2025 *#### Neue Funktionen **Benutzer (PF-3663)**

Die Benutzerverwaltungsansicht ist jetzt in NextGen implementiert.

#### Verbesserungen **Iam (PF-4330)**

Der globale MFA-Schalter befindet sich jetzt in der Kopfzeile der Benutzertabelle.

#### Fehlerbehebungen **N/a (FE-803)** Ein Problem mit nicht gespeicherten NextGen-Tabellen wurde behoben. ** Zahlungseingang (FAC-4948)**

Das Bearbeiten und Speichern einer Transaktion im Zahlungseingangsmodul entfernt nicht mehr die zuvor automatisierte Zuordnung von der Transaktion.

## 25.38 Release notes

### Release version 25.38.5

*Veröffentlichungsdatum: 13. Oktober 2025 *#### Neue Funktionen **Batches / Picklisten Profile (FFU-6032)** Erweiterte Überwachung mit zusätzlichen Einblicken in den Batch-Prozess. ** Api (PF-4283)** Neue Daten wurden den Kunden-API-Endpunkten hinzugefügt. ** E-invoice (FAC-4501)**

Support für strukturierte Artikelidentifikatoren (EAN/GTIN/BARCODE) in elektronischen Rechnungsformaten wurde hinzugefügt.

#### Verbesserungen **Iam (PF-4328)** Der Projektabschnitt in der PAT-Erstellungsansicht ist jetzt hinter einem Feature-Flag verborgen. ** Einvoice (FAC-4866)** Rechnungen mit kartengestützten Zahlungen wie PayPal entsprechen nun der XRechnung 3.0 Struktur. IBAN und BIC werden weggelassen, wenn Zahlungstyp 48 ausgewählt ist, und die erforderlichen Kartenzahlungsinformationen werden hinzugefügt, um die Konformität mit EN 16931 sicherzustellen und Validierungsfehler während der Einreichung zu vermeiden. ** Getmyinvoice (FAC-4865)** Das GetMyInvoices-Modul wurde entfernt und durch die allgemeine API-Kontoerstellung ersetzt. ** Verbindlichkeiten (FAC-1880)**

Für Verbindlichkeiten erstellte Bankzahlungen verwenden bevorzugt den Namen des Bankkontoinhabers in den Adresseneinstellungen. Wenn das Feld Bankkontoinhaber nicht ausgefüllt ist, wird der allgemeine Adressname als Fallback verwendet.

#### Fehlerbehebungen **Belege Importer (PF-4341)** Ein Problem wurde behoben, das dazu führte, dass der Belegeimport fehlschlug, wenn das Update-Set leer war. ** N/a (FAC-4916)** Ein Problem wurde behoben, das das Drucken von Rechnungen verhinderte. ** Pinnwand (PF-4336)**

Ein Problem mit redundanten Benachrichtigungen in NextGen-Umfragen wurde behoben.

## 25.36 Release notes

### Release version 25.36.11

*Veröffentlichungsdatum: 01. Oktober 2025 *#### Fehlerbehebungen **Email Service (FAC-4918)**

Ein seltener Randfall wurde behoben, bei dem E-Mails mit leeren Anhängen gesendet wurden.

### Release version 25.36.10

*Veröffentlichungsdatum: 29. September 2025 *#### Verbesserungen **N/a (SRE-2929)**

Bedeutende Leistungsverbesserungen wurden für den 'SuperSearch Index Diff'-Cronjob eingeführt.

### Release version 25.36.9

*Veröffentlichungsdatum: 26. September 2025 *#### Neue Funktionen **Versandart DHL (aka DHL 3.0) (FFU2-701)**

Der PDDP-Service wurde aufgrund neuer Zollbedingungen für den Versand in die USA hinzugefügt.

### Release version 25.36.8

*Veröffentlichungsdatum: 25. September 2025 *#### Verbesserungen **Tages-Auto-Versand (FFU-6001)**

Die Berechnung der Lagerampeln umfasst jetzt Aufträge mit dem Status 'Versendet'.

#### Fehlerbehebungen **Rechnung (FAC-4906)**

Ein Fehler, der das Drucken von Rechnungen verhinderte, wurde behoben.

### Release version 25.36.7

*Veröffentlichungsdatum: 24. September 2025 *#### Fehlerbehebungen **Auftragsampel (FFU-5992)**

Ein Problem mit der Auftragsampelfunktion bei aktivierten Chargen, Mindesthaltbarkeitsdaten und/oder Seriennummern wurde behoben.

### Release version 25.36.6

*Veröffentlichungsdatum: 24. September 2025 *#### Verbesserungen **App Mobilepicking (FFU-5749)** Picklisten werden beim Verlassen des Picklisten-Kontextes im Dispatch Center in ihren nicht abgeschlossenen Status zurückgesetzt. ** Iam (PF-4273)** Die PAT-Liste in den Kontoeinstellungen ist auf den angemeldeten Benutzer beschränkt. ** Verbindlichkeiten (FAC-4749)**

Wiederkehrende Zahlungen werden jetzt beim automatisierten Abgleich von eingehenden und ausgehenden Zahlungen berücksichtigt.

#### Fehlerbehebungen **Api (API-217, IMPAPI-539)**

Ein Fehler, bei dem der v1-Rechnungsstatus-Endpunkt anders als der übliche Workflow verhielt, wenn eine Rechnung auf 'bezahlt' gesetzt wurde, wurde behoben.

## 25.35 Release notes

### Release version 25.35.6

*Veröffentlichungsdatum: 22. September 2025 *#### Neue Funktionen **Artikel (PIM-3167)**

Eine Funktionserkennungsprüfung wurde im Versandzentrum hinzugefügt, um die Verwendung der Thumbnail-URL anstelle eines API-Aufrufs zum Abrufen des Artikel-Thumbnails zu ermöglichen.

#### Verbesserungen **Amainvoice (ECOM-5149)**

Die Leistung von Amainvoice wurde unter bestimmten Bedingungen verbessert.

#### Fehlerbehebungen **Auftrag (FFU-5965)**

Ein Problem mit der Ampelberechnung für Autoship wurde behoben.

### Release version 25.35.5

*Veröffentlichungsdatum: 22. September 2025 *#### Neue Funktionen **Iam (PF-4255)** Die PAT-Sperrfunktion wurde implementiert. ** N/a (PF-4163)** X1-Poll-Benachrichtigungen wurden in NextGen implementiert. ** Versand Aufsplitten (FAC-4631)**

Eine Option wurde hinzugefügt, um Artikel von Rabatt oder Versandaufteilungen auszuschließen.

#### Verbesserungen **N/a (SRE-2922)** Die Veröffentlichung optimiert die Geschwindigkeit der nächtlichen Supersearch Indexing Prozesse. ** Api (PF-4240)** API-Endpunkt erweitert, um mehr Informationen zur Dokumentenbereitstellung für Kunden zu umfassen. ** Api (PF-4238)** API-Endpunkt erweitert, um Bankinformationen für Kunden einzubeziehen. ** Api (PF-4237)** API-Endpunkt erweitert, um Aktualisierungen der Bankdaten eines Kunden zu ermöglichen. ** Api (PF-4236)** API-Endpunkt erweitert, um Finanzinformationen für Kunden einzubeziehen. ** Api (PF-4235)** API-Endpunkt erweitert, um Aktualisierungen der Finanzinformationen eines Kunden zu ermöglichen. ** Api (PF-4076)** API-Endpunkt erweitert, um Kunden mit Bankinformationen zu erstellen. ** E-invoice (FAC-4681)** Die Brutto-Preiskalkulation wurde verbessert, um Warnungen in einigen Validierern zu verhindern, wenn Rabatte pro Zeile angewendet werden. ** E-invoice (FAC-4677)**

Die Brutto-Preiskalkulation wurde verbessert, um Warnungen in einigen Validierern zu vermeiden.

#### Fehlerbehebungen **Bossapp (FAC-4814)** Verbindung zu xentral ist wiederhergestellt. ** Api (CCI-2310)** Fix für Autorisierungsfehler bei der LEGACY REST-API. ** Api (CCI-2309)** Die alte Implementierung von HTTP-Anfragen wurde aktualisiert. URL-Routen werden nicht mehr normalisiert, was frühere ältere APIs obsolet macht. ** N/a (XIN-2481)** Ein Problem wurde behoben, bei dem die KPI-Kacheln auf dem Startbildschirm nicht korrekt ins Deutsche übersetzt wurden. ** Wiedervorlage (PF-4096)** Ein Problem wurde behoben, bei dem Gmail-E-Mails den konfigurierten Anzeigenamen des E-Mail-Kontos nicht angezeigt haben. ** Zahlungseingang (FAC-4713)**

Ein Randfall wurde behoben, bei dem die Buchhaltungsbeschreibung für eine neue eingehende Zahlung nicht gespeichert wurde.

## 25.34 Release notes

### Release version 25.34.4

*Veröffentlichungsdatum: 17. September 2025 *#### Neue Funktionen **New Pos (FAC-4804)**

Es wurde ein Protokollierungssystem hinzugefügt, um die Sendung von Terminalanfragen zu verfolgen.

### Release version 25.34.3

*Veröffentlichungsdatum: 10. September 2025 *#### Neue Funktionen **Api (PF-4227, IMPAPI-766)** Ein API-Endpunkt zur Erstellung von Lagern wurde hinzugefügt. ** Iam (PF-4213)**

Die PAT-Log-Seite wurde in das Einstellungszentrum aufgenommen.

#### Verbesserungen **N/a (XIN-2423)** Im Modul für Erlösanalyse lädt die 'Projekte'-Eingabe in den Seiteneinstellungen nun automatisch die verfügbaren Projekte. ** Iam (PF-4203)** Die Produktankaufpreis-API ist jetzt durch Token-Scopes geschützt. ** Iam (PF-4200)** Scopes wurden für die Lager- und Lagerplatz-APIs implementiert. ** Api (PF-4068)** Der API-Endpunkt wurde erweitert, um Kunden mit Finanzinformationen zu erstellen. ** E-invoice (FAC-4500)**

BT-49 ist jetzt Teil der E-Rechnung. Wenn verfügbar, werden Leitweg-ID, GLN oder Kunden-E-Mail-Adresse verwendet.

#### Fehlerbehebungen **Iam (PF-4250)** Ein Problem beim Erstellen von PATs ohne ausgewähltes Projekt wurde behoben. ** Wiedervorlage (PF-4165)** Die Funktionalität zum Versenden von Erinnerungsemails im Wiedervorlage-Modul wurde repariert. ** Konten Mollie (FAC-4070)**

[Mollie] Die Handhabung der Ausschlussoption für PayPal bei leeren mollie_api_date_range-Einstellungen wurde korrigiert.

## 25.33 Release notes

### Release version 25.33.4

*Veröffentlichungsdatum: 05. September 2025 *#### Fehlerbehebungen **N/a (CE-150, FFU-5911)**

Das Protokollierungsniveau bestimmter Altdatenbankprotokolle wurde angepasst, um die Gesamtleistung zu verbessern.

### Release version 25.33.3

*Veröffentlichungsdatum: 04. September 2025 *#### Fehlerbehebungen **New Pos (FAC-4727)** Terminalereignisse im POS wurden unter bestimmten Bedingungen nicht ausgelöst. ** Shopify (ECOM-5150)**

Die automatische Zahlungsabstimmung für PayPal über den Shopify-Legacy-Importer wurde nach Änderungen in der Shopify-API wiederhergestellt.

### Release version 25.33.2

*Veröffentlichungsdatum: 04. September 2025 *#### Neue Funktionen **Iam (PF-4208)** Weitere API-Endpunkte für verbesserte Integrationsfähigkeiten bereitgestellt. ** Lagerverwaltung (PF-4229, IMPAPI-768)** Ein Endpoint zum Löschen von Lagern wurde hinzugefügt. ** Lagerverwaltung (PF-4228, IMPAPI-767)** Ein Endpoint zum Aktualisieren von Lagern wurde hinzugefügt. ** Iam (PF-4205)** Scopes wurden für die Kontaktperson-API implementiert. ** Iam (PF-4204)** Scopes wurden für die Artikelverkaufspreis-API implementiert. ** Iam (PF-4201)** Scopes wurden für die Warengruppen-API implementiert. ** Iam (PF-4199)**

Scopes wurden für die Lagerartikel-API implementiert.

#### Verbesserungen **N/a (PF-4224)** Der EU-spezifische 'XI' ISO-Ländercode wurde Nordirland zugeordnet. ** Länderliste (PF-4158)**

Die Liste der Länderteilungen wurde mit den entsprechenden ISO 3166-Codes aktualisiert.

#### Fehlerbehebungen **Iam (PF-4191)** Ein Fehler wurde behoben, bei dem Tokens in der Liste der 'persönlichen Zugangstokens' angezeigt wurden, obwohl sie gelöscht waren. ** Bestellung (FFU-5810)** Die Fehlermeldung 'Weiter als Produktion' wurde behoben, wenn keine Produktionsartikel vorhanden sind. ** Auftrag (FFU-5625)**

Ein Problem wurde behoben, bei dem das gleichzeitige Öffnen mehrerer Geschäftsdokumentprotokolle (Rechnung, Auftrag, Lieferschein) dazu führte, dass der Sendendialoge fehlerhafte Kundendaten anzeigte.

## 25.32 Release notes

### Release version 25.32.2

*Veröffentlichungsdatum: 28. August 2025 *#### Verbesserungen **Zahlungseingang (FAC-4718)**

Die Option zur eigenständigen Aktivierung der Verbesserungen beim Zahlungseingang-Import wurde entfernt.

### Release version 25.32.1

*Veröffentlichungsdatum: 28. August 2025 *#### Neue Funktionen **E-invoice (FAC-4519)**

Die GLN für die Versandadresse ist jetzt in XRechnung und ZUGFeRD enthalten.

#### Verbesserungen **Hubspot (PF-4188)** Eine Benachrichtigung wird jetzt an Kunden gesendet, wenn sie aufgrund der Einschränkungen ihres kostenlosen Tarifs keine weiteren Kontakte in HubSpot erstellen können. ** Einvoice (FAC-4455)**

Die Auftragsnummer ist jetzt in der XML enthalten, und das Zahlungsdatum wird mit Hilfe von Zieltagen berechnet und in die XML eingefügt.

#### Fehlerbehebungen **App Mobilepicking (PF-4217, FFU-5800)** Ein Problem wurde behoben, bei dem die Schaltfläche 'Erstellen' auf eine falsche Seite in den mobilen Kommissionierprofilen weiterleitete. ** Geschäftsbrief Vorlagen (PF-4081)** Der Erstellungsprozess für E-Mail-Vorlagenanhänge wurde behoben. ** Tickets (PF-4070)**

Ein Fehler im Zusammenhang mit der Verwendung von Umlauten und Sonderzeichen wurde behoben.

## 25.31 Release notes

### Release version 25.31.7

*Veröffentlichungsdatum: 21. August 2025 *#### Fehlerbehebungen **Versandzentrum (FFU-5844)**

Die Unterstützung für XML-Objekte und andere Datentypen in der Datenbank-Escaping wurde implementiert, um Abstürze im Transfermodul und Integrationsprobleme mit dem Post CH-Carrier bei der Verarbeitung von SimpleXMLElement-Daten zu beheben.

### Release version 25.31.6

*Veröffentlichungsdatum: 19. August 2025 *#### Neue Funktionen **Function (PF-4132)** Das lange veraltete Modul "chat" wurde entfernt. ** Iam (PF-4114)** Scopes wurden zur Rückgabe-API hinzugefügt. ** E-invoice (FAC-4573)** Unterstützung für XRechnung Version 3.0.2 für E-Rechnungen wurde hinzugefügt. ** E-invoice (FAC-4499)** Zusätzliche Daten einschließlich Kontaktinformationen und Bankverbindungen wurden zum ZUGFeRD-Plugin hinzugefügt. ** E-invoice (FAC-4498)**

Xentral-Users GLN ist nun in X-Rechnung und ZUGFeRD enthalten.

#### Verbesserungen **Email Backup (PF-4187)** Es werden nun entsprechende Fehlermeldungen angezeigt, wenn das Senden von E-Mails über Gmail aufgrund geänderter Google-Kontodaten nicht möglich ist. ** N/a (PF-4148)** Die Leistung von NextGen wurde durch Behebung von speicherbezogenen Lecks in Übersetzungen verbessert. ** E-invoice (FAC-4502)** Die Versandadresse wurde in X-Rechnung und ZUGFeRD-Rechnungen hinzugefügt. ** N/a (FAC-4491)**

Leistungsverbesserungen für Zahlungsimporte können nun aktiviert werden.

#### Fehlerbehebungen **DPD (API) (FFU-5797)** Der Fehler, der bei der Erstellung des DPD-Labels auftrat, wurde behoben. ** Email Service (PF-4186)** Ein Problem mit unbegrenzt erscheinenden Erfolgsmeldungen beim Verbinden eines E-Mail-Kontos wurde behoben. ** Auftrag (PF-4130)** Änderungen wurden zurückgenommen, um Schriftgrößen in PDFs korrekt darzustellen. ** Lagerverwaltung (FFU-5255)**

Ein Problem wurde behoben, bei dem der CSV-Import von Lagerorten das Kontrollkästchen "Erste Zeile als Kopfzeile" ignorierte. Die erste Zeile wird nun korrekt als Kopfzeile behandelt, wenn ausgewählt.

## 25.30 Release notes

### Release version 25.30.6

*Veröffentlichungsdatum: 18. August 2025 *#### Fehlerbehebungen **Finanzbuchhaltung Export (FAC-4643)**

Ein Problem mit der Exportfunktion für Rechnungen und Gutschriften mit Fremdwährung wurde behoben.

### Release version 25.30.5

*Veröffentlichungsdatum: 12. August 2025 *#### Fehlerbehebungen **DHL Retoure (FFU-5776)**

Ein Fehler wurde behoben, der das Speichern von Tracking-Links in Retouren verhinderte.

### Release version 25.30.4

*Veröffentlichungsdatum: 12. August 2025 *#### Fehlerbehebungen **Finanzbuchhaltung Export (FAC-4635)**

Fehlerbehebung im Haftungsexportprozess, um die korrekte Verarbeitung sicherzustellen, wenn die erste oder zweite Dezimalstelle null ist.

### Release version 25.30.3

*Veröffentlichungsdatum: 12. August 2025 *#### Neue Funktionen **Iam (PF-4118)** Scopes wurden zur Rechnungs-API hinzugefügt. ** Iam (PF-4103)** Scopes wurden zur Artikel-API hinzugefügt. ** Iam (PF-4014)**

Eine Option zur Bereichseingrenzung von Personal Access Tokens nach Projekten wurde aktiviert.

#### Verbesserungen **N/a (PF-4033, PIM-2980)**

Die Leistung wurde durch die Behebung von Speicherlecks im Zusammenhang mit X1 Userlane, NextGen-Modul, mantine und getrennten Elementen verbessert.

#### Fehlerbehebungen **New Pos (FAC-4626)**

Eine Anzahlungsrechnung konnte unter bestimmten Bedingungen dazu führen, dass der Gesamtbetrag der Buchung erneut erfasst wurde. Dieses Problem wurde behoben.

## 25.29 Release notes

### Release version 25.29.6

*Veröffentlichungsdatum: 11. August 2025 *#### Fehlerbehebungen **Tages-Auto-Versand (FFU-5726)**

Ein Auftrag mit nicht auseinandergelegten JIT-Positionen wird jetzt ordnungsgemäß blockiert, um reibungslosere Abläufe im System zu gewährleisten.

### Release version 25.29.5

*Veröffentlichungsdatum: 08. August 2025 *#### Fehlerbehebungen **New Pos (FAC-4579)**

Ein Problem wurde behoben, bei dem eine Anzahlungsrechnung unter bestimmten Bedingungen fälschlicherweise dazu führen konnte, dass der Gesamtbetrag der Buchung erneut gebucht wurde.

### Release version 25.29.4

*Veröffentlichungsdatum: 07. August 2025 *#### Fehlerbehebungen **Api (FFU-5704)**

Ein Fehler, der zum Überverkauf von Lagerbeständen führte, wurde behoben. Dieses Problem stand im Zusammenhang mit der kürzlichen Restrukturierung im Dropshipping-Lagermodul, die die Berechnung der Lagerampel beeinflusste.

### Release version 25.29.2

*Veröffentlichungsdatum: 05. August 2025 *#### Neue Funktionen **Settings Center (PF-4124)** Der PATCH-Endpunkt für persönliche Zugriffstoken unterstützt jetzt den Parameter 'expiresAt' (gesteuert durch Feature-Flag). ** Iam (PF-4117)** Scopes wurden zur Gutschriften-API hinzugefügt. ** Iam (PF-4101)** Scopes wurden zur Produktions-API hinzugefügt. ** Iam (PF-4100)** Scopes wurden zur Bestellung-API hinzugefügt. ** Iam (PF-4099)**

Scopes wurden zur Rückgabe-API hinzugefügt.

#### Verbesserungen **Reporting (XIN-2083)**

Im Berichte-Modul kann nun das Dateiformat für den Export von Berichten festgelegt werden.

#### Fehlerbehebungen **Reporting (XIN-2364)** Ein Problem mit dem Ladezustand von Excel-Exporten im Reporting-Modul wurde behoben. ** Settings Center (PF-4036)** Ein Problem mit der Zurück-Schaltfläche in den E-Mail-Konten wurde behoben. ** Generic (PF-4159)**

Problem mit dem Ablauf des persönlichen Zugriffstokens wurde behoben.

## 25.28 Release notes

### Release version 25.28.1

*Veröffentlichungsdatum: 29. Juli 2025 *#### Neue Funktionen **Iam (PF-4060)** Es wurden Scopes zu den Webhooks-APIs hinzugefügt. ** System-status (PF-4059)** Es wurden Scopes zu den Systemstatus-APIs hinzugefügt. ** Iam (PF-4057)** Es wurden Scopes zur API für Personal Access Tokens hinzugefügt. ** Drucker (PF-3736)** Eine neue Benutzerberechtigung "printer:download" wurde eingeführt, die es Benutzern ermöglicht, alle Druckaufträge als PDFs herunterzuladen. Die Berechtigung ist standardmäßig für neue Benutzer deaktiviert und für aktuelle Benutzer aktiviert, um Unterbrechungen zu vermeiden. Aufgrund von DSGVO-Gründen wird empfohlen, dass Administratoren diese Berechtigung sorgfältig vergeben. ** Versandart DHL (aka DHL 3.0) (FFU-5528)**

Der DHL-Identitätsprüfungsdienst wurde implementiert.

#### Verbesserungen **Konten Shopify (FAC-4360)** Das Shopify-Geschäftskonto ist nicht mehr mit dem Shop-Importer verknüpft. Es setzt jetzt auf eine eigene Authentifizierung. ** Auftrag (FAC-4200)**

Mahn-E-Mails werden jetzt für alle Konten unterstützt, die mit `vorkasse` beginnen.

#### Fehlerbehebungen **Auftrag (FFU-5527)**

Falls ein Auftrag eine nicht aufgeschlüsselte JIT-Position enthält, wird die Anzeige [Auto-ship erlauben] rot und blockiert die weitere Auftragsbearbeitung.

## 25.27 Release notes

### Release version 25.27.5

*Veröffentlichungsdatum: 25. Juli 2025 *#### Neue Funktionen **Zahlungseingang (FAC-4445)**

Logging hinzugefügt, um den Ausfall von Warteschlangenjobs beim Abgleich eingehender Zahlungstransaktionen zu verfolgen.

#### Fehlerbehebungen **Appstore (PF-4090)**

Das Problem im Automatisierungsfluss wurde behoben.

### Release version 25.27.3

*Veröffentlichungsdatum: 22. Juli 2025 *#### Neue Funktionen **Iam (PF-4027)** Die Endpunkte für Kunden-, Benutzer- und E-Mail-Konten-APIs enthalten nun Scopes. ** Finanzbuchhaltung Export (FAC-4022)**

Unterstützung für Leistungsdatum zu DATEV-Exporten hinzugefügt.

#### Verbesserungen **Adressen (PF-3990)**

Während des Imports einer CSV wurden die Ereignisse CustomerCreated und CustomerUpdated ausgelöst.

#### Fehlerbehebungen **License (PF-4037)** Behoben: Das Problem, bei dem der Abschnitt zum Beta-Programm auf der Systemaktualisierung-Admin-Seite nicht sichtbar war. ** N/a (FFU-5585)**

Das Problem, das sich auf Bestandsbewegungen mit nicht-ganzzahligen Mengen über API-Endpunkte auswirkte, wurde behoben.

## 25.26 Release notes

### Release version 25.26.5

*Veröffentlichungsdatum: 18. Juli 2025 *#### Fehlerbehebungen **Lieferschwelle (FAC-4416)**

Das Modul für die Versandsteuersplit setzte den Portosteueranteil fälschlicherweise auf 0, was zu inkorrekten Preisen für Schweizer Aufträge führte, aufgrund eines Konflikts mit der Lieferschwellenbesteuerung. Dieses Problem wurde behoben.

### Release version 25.26.4

*Veröffentlichungsdatum: 15. Juli 2025 *#### Neue Funktionen **N/a (PF-4039)** Abschnitt Automatisierung und Modul Flows wurden eingeführt. ** Email Backup (PF-3956)**

Ein 'HTML-Quelle'-Button wurde dem Email-Signatur-WYSIWYG-Editor hinzugefügt, um HTML-Signaturen zu ermöglichen.

#### Verbesserungen **Iam (PF-4019)** Die Benutzererfahrung in den neuen PAT-Übersichts- und Erstellungsseiten wurde verbessert. ** Adressen (PF-3988)** API-Endpunkte für Kunden (V1/V2) versenden nun Ereignisse bei Erstellen-, Aktualisieren- und Löschanfragen. ** N/a (FE-353)** Die Datumswähler-Eingabe wurde verbessert. ** Auftrag (FAC-4340)**

Eine neue Option zur Preisberechnung aus eingehenden Dokumenten über die API wurde in den Liefergrenzwerten eingeführt, selbst ohne definierten Liefergrenzwertartikel.

#### Fehlerbehebungen **Api (PF-4066)** Vorbeugende Maßnahmen gegen unerwartete Löschung ungenutzter persönlicher Zugriffstoken implementiert. ** N/a (PF-4034)** Ein Problem mit leeren Login-Callback-Seiten wurde behoben. ** Auftrag (FFU-5598)**

Ein Fehler wurde behoben, der verhinderte, dass Aufträge durch den Batch-Cronjob verarbeitet wurden.

## 25.25 Release notes

### Release version 25.25.9

*Veröffentlichungsdatum: 15. Juli 2025 *#### Fehlerbehebungen **Adressen (PF-4072)**

Die Standardeinstellung der Sprache für neue Kontakte wurde korrigiert.

### Release version 25.25.8

*Veröffentlichungsdatum: 11. Juli 2025 *#### Fehlerbehebungen **Tickets (PF-4024)**

Sonderzeichen im Absender- und Empfängernamen der E-Mails wurden korrigiert.

### Release version 25.25.7

*Veröffentlichungsdatum: 10. Juli 2025 *#### Fehlerbehebungen **Frontend (FE-779)**

Beheben Sie, dass in einigen Browsern Menüsymbole nicht angezeigt wurden.

### Release version 25.25.5

*Veröffentlichungsdatum: 09. Juli 2025 *#### Neue Funktionen **Drucker (PF-4012, IMPAPI-125)** Ein neuer API-Endpunkt POST /api/v1/printJobs wurde implementiert, um das direkte Drucken von PDF-Dokumenten zu unterstützen. ** Iam (PF-3943)** Eine neue Seite zur Erstellung von PAT wurde hinzugefügt. ** Service & Support (PF-3908)**

Es wurde eine Möglichkeit eingeführt, Serviceaufträge aus einem Ticketsystem zu erstellen. Diese Funktion ist standardmäßig inaktiv und wird schrittweise eingeführt.

#### Verbesserungen **Dateien (PF-3742)**

Änderung der Entfernung von Anhängen aus der Geschäftsvorlagenbrief-Vorlage entfernt nun nur die Originaldatei.

#### Fehlerbehebungen **Adressen (PF-4044)** Das Problem, das dazu führte, dass die CRM-Registerkarte in Kontakten nicht geladen wurde, wurde behoben. ** Sendcloud (FFU-5593, FFU-5567, FE-773)** Korrekturen an der Auswahl von Versandartikeln in Sendcloud mit Just-In-Time (JIT) Artikeln wurden vorgenommen. ** N/a (PF-4018)**

Ein Problem wurde behoben, bei dem das Quick-Filter-Dropdown im NextGen-Datentabelle abgeschnitten war.

## 25.24 Release notes

### Release version 25.24.10

*Veröffentlichungsdatum: 03. Juli 2025 *#### Fehlerbehebungen **Versandarten (PIM-3016)**

Ein Problem wurde gelöst, bei dem nicht alle Drucker in der Carrier Integration Service Versandmethode erkannt wurden.

### Release version 25.24.9

*Veröffentlichungsdatum: 02. Juli 2025 *#### Verbesserungen **Sendcloud (FFU-5570)**

SKU ist jetzt für Sendcloud DHL 2 Mann Handling Artikel verfügbar.

#### Fehlerbehebungen **E-invoice (FAC-4423)**

Die USt-IdNr. des Debitors wird nun für die E-Rechnung berücksichtigt. Eine Inkonsistenz bei den Netto-Preisen wurde behoben.

### Release version 25.24.8

*Veröffentlichungsdatum: 01. Juli 2025 *#### Neue Funktionen **Api (PF-3962)** In der Customer API ist jetzt die Option enthalten, Werte für konfigurierte benutzerdefinierte Felder festzulegen. ** POS (FAC-4373)**

Die neue POS-Funktionalität umfasst jetzt die Möglichkeit, eine Positionsbeschreibung hinzuzufügen.

#### Verbesserungen **POS (FAC-4348)** Das Ereignis wurde umbenannt, um die Klarheit zu verbessern. ** Api (PF-3964)** Die Customer API zeigt jetzt auch Werte für konfigurierte benutzerdefinierte Felder in der Kundenansicht an. ** Email Service (PF-3881)** Im Geschäftsbrief wird jetzt der für ein E-Mail-Konto konfigurierte Absendername verwendet. ** Tickets (PF-3767)** Die Funktion zum Importieren von Tickets arbeitet jetzt mit der IMAP-Objekt-UID. ** Verbindlichkeiten (FAC-4288)**

Die Lieferantenermittlung für Verbindlichkeiten und E-Rechnungen priorisiert jetzt explizitere Übereinstimmungen wie die Umsatzsteuer-Identifikationsnummer gegenüber dem Stadtnamen. Eine Meldung informiert, wenn der Lieferant automatisch geändert wird.

#### Fehlerbehebungen **Auftrag (PF-4035, FFU-5576)** Englische Übersetzungen für Dokumente wurden korrigiert. ** Wiedervorlage (PF-3756)**

Ein Fehler in den Datentabellen, wenn Spalten als sichtbar/unsichtbar konfiguriert wurden, wurde behoben.

## 25.23 Release notes

### Release version 25.23.9

*Veröffentlichungsdatum: 27. Juni 2025 *#### Neue Funktionen **Verbindlichkeiten (FAC-4432)**

Ein neuer OCR-Dienst wurde zum Modul Verbindlichkeiten hinzugefügt.

### Release version 25.23.8

*Veröffentlichungsdatum: 27. Juni 2025 *#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (FFU-5561)**

Der Berechnungsfehler bei der Handhabung mehrerer JIT-Teilstücklisten wurde behoben.

### Release version 25.23.7

*Veröffentlichungsdatum: 26. Juni 2025 *#### Verbesserungen **Lagerverwaltung (FFU-3590)**

Die Lagerbewertung verwendet jetzt den aktuellen Lagerwert, wenn 'live mit aktuellem Wert' ausgewählt ist.

#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (FFU-5552)**

Ein Fehler wurde behoben, der die JIT-Gewichtsberechnungen bei DHL störte, wenn der JIT-Kopf kein Gewicht gesetzt hatte.

### Release version 25.23.6

*Veröffentlichungsdatum: 25. Juni 2025 *#### Fehlerbehebungen **Sendcloud (FFU-5554)**

Das Problem mit der Aktivierung des Sendcloud-Paketscheinformulars aus dem Versandzentrum wurde behoben.

### Release version 25.23.5

*Veröffentlichungsdatum: 24. Juni 2025 *#### Neue Funktionen **Api (PF-3945)** Personenbezogene Zugriffstoken (PAT) können nun Beschreibungen haben. ** N/a (PF-3942)**

Eine neue PAT-Übersichtsseite wurde hinzugefügt.

#### Verbesserungen **Reporting (XIN-2179)** Spalten mit dem Namen 'tags' im Berichte-Modul führen nicht mehr zu Problemen. ** Api (PF-3932, IMPAPI-631)** Customer-API wurde um zusätzliche E-Mail-Daten erweitert. ** Systemupdate (PF-3513, PIM-2100)** Der Infobereich des Beta-Programms wurde aktualisiert. ** Multi-Order Picking (FFU-5385)** Verbesserte Validierung beim Scannen von Chargen und Mindesthaltbarkeitsdaten im Multiauftragkommissionieren. ** Rechnung (FAC-3298)**

Die Anzeige des Teilerstattungsstatus im Rechnungszusammenhang wurde vereinheitlicht.

#### Fehlerbehebungen **Retouren Belege (FFU-5524)** Die fehlerhafte Berechnung des Return Label JIT Gewichts wurde behoben. Das Gewicht wird nun korrekt nur aus dem Kopfstück gemäß den Einstellungen entnommen. ** New Pos (FAC-4398)** Probleme beim Abschluss eines Verkaufs über das neue POS, die zur Erstellung eines neuen Kunden mit derselben Adresse führten, wurden behoben. ** New Pos (FAC-4374)** Ein Problem wurde behoben, bei dem das Laden einer Rechnung und die Bezahlung über das POS zu einer neuen Rechnung führte, anstatt die vorhandene Rechnung zu aktualisieren. ** Import/Export Zentrale (PF-3944)** Ein Fehler mit dem unendlichen Ladeindikator nach dem Herunterladen einer Datei wurde behoben. ** Adressen (FAC-4309)** Ein Fehler, der das Löschen von Abonnements verhinderte, wurde behoben. ** E-invoice (FAC-4298)**

Die Unterstützung für Zahlungsanweisungen bei E-Rechnungen wurde korrigiert.

## 25.22 Release notes

### Release version 25.22.7

*Veröffentlichungsdatum: 17. Juni 2025 *#### Neue Funktionen **Gesamtüberblick (XIN-1519)** Berichte können jetzt im Berichte-Modul kopiert werden. ** Api (PF-3914)** Ein API-Endpunkt wurde hinzugefügt, um Textvorlagen für Geschäftsschreiben zu konfigurieren. ** System-status (PF-3883)** Ein neuer Wurzelabschnitt für 'Automatisierung' wurde eingeführt. ** Api (FAC-4336)**

Unterstützung für den 'greaterThanOrEquals' Filter-Operand im Listen-Rechnungs-API-Endpunkt wurde hinzugefügt.

#### Verbesserungen **Adressen (PF-3829)** Die Kontaktliste-API ist jetzt nach Adresstyp, Straße, Postleitzahl, Stadt und Bundesland durchsuchbar. ** Drucker (PF-3666)** Wenn die Einstellung 'Druck ohne Hintergrund' im Drucker gewählt wird, hat sie jetzt Vorrang vor anderen Einstellungen, die das Drucken mit Hintergrund ermöglichen. ** Versandzentrum (FFU-5285)** Optimierungen wurden bei den Fehlermeldungen und Übersetzungen des Versandzentrums vorgenommen. ** Kassenbuch (FAC-4358)** Die Formulierung im POS-Aktivierungsdialog wurde für eine bessere Verständlichkeit angepasst. ** Einvoice (FAC-4285)** Die Vertragsreferenz (BT-12) wird nun bei E-Rechnungen berücksichtigt. ** Zahlungseingang (FAC-4372)** Die neuen Zahlungsleistungsverbesserungen wurden für Nicht-Admin-Benutzer aktiviert. ** N/a (FFU-5526)** Die FeatureFlag-Konfiguration wurde aktualisiert, um Konsistenz mit den unternehmensweiten Formatstandards zu gewährleisten. ** N/a (FFU-5288)**

Der Explosionsprozess für JIT-Stücklisten während des Imports/UI wurde mit maximal 5 Versuchen verbessert.

#### Fehlerbehebungen **N/a (PF-3939)** Ein Problem wurde behoben, das verhinderte, dass Benutzer Module im Sidebar/Launchpad ausblenden konnten. ** Settings Center (PF-3923)** Ein Problem, das die Neuanordnung von Modulgruppen verhinderte, wurde behoben. ** Projekte (PF-3586)** Die Neuanordnungslogik für Teilprojekte wurde angepasst, um Kreisreferenzen zu vermeiden. ** Versandart DHL (aka DHL 3.0) (FFU-5446)** Ein Problem mit negativen Versandkosten, die Fehler in der DHL-API verursachten, wurde behoben. Negative Werte werden jetzt in 0.0 umgewandelt. ** Versandart DHL (aka DHL 3.0) (FFU-5406)** Ein Problem mit JIT-Komponenten auf CN23-Formularen, das für DHL nicht funktionierte, wurde behoben. Die korrekte Konfiguration übernimmt jetzt korrekt den HS-Code und das Gewicht der Komponenten. ** Inventur (FFU-5354)** Es wurde eine Korrektur vorgenommen, um die erneute Übermittlung von Anfragen zum Abschluss des Inventur-Laufs zu blockieren. ** Adapterbox (FAC-4355)** Das Quittungsdruck für POS funktioniert wieder. ** Versandart DHL (aka DHL 3.0) (PIM-3001)** Ein Problem wurde behoben, bei dem die Verwendung englischer Variablen, wie {DELIVERY_NOTE}, in Bezugsnummern die DHL-Versandmethode störte. ** Lieferschein (FFU-5488)** Ein Fehler wurde behoben, bei dem DHLExpress und PostAT eine Nachricht anzeigten, die darauf hinwies, dass die Versandmethode für internationale Paketsendungen nicht verfügbar war. ** Versandart DHL (aka DHL 3.0) (FFU-5491)** Die Gewichtskalkulation für JIT wurde korrigiert. ** Versandart DHL (aka DHL 3.0) (FFU-5493)** Ein Fehler, der dazu führte, dass Telefonnummern auf DHL Versandetiketten fehlten, wurde behoben. ** Versandart DHL (aka DHL 3.0) (FFU-5482)** Das Verhalten von Nachnahme bei DHL wurde korrigiert. ** Lieferschein (FFU-5499)** Die Gewichtberechnung für JIT-Artikel ist jetzt korrigiert, wenn die Einstellung 'Gewicht aus JIT-Stückliste' aktiviert ist. ** Reporting (XIN-2246)** Ein Fehler wurde behoben, bei dem das Öffnen und Schließen der Akkordeons im Berichte-Modul "Zugriffsrechte"-Tab einen Fehler verursachte. ** Versandart DHL (aka DHL 3.0) (PIM-3012)**

Einige deutsche Übersetzungen für die Versandart DHL wurden korrigiert.

## 25.21 Release notes

### Release version 25.21.11

*Veröffentlichungsdatum: 13. Juni 2025 *#### Fehlerbehebungen **Lieferschein (FFU-5499)**

Die Gewichtskalkulation für JIT-Artikel wurde korrigiert, wenn die Einstellung 'Gewicht aus JIT-Teileliste' aktiviert ist.

### Release version 25.21.10

*Veröffentlichungsdatum: 12. Juni 2025 *#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (FFU-5493)** Ein Problem wurde behoben, bei dem die Telefonnummer auf den DHL-Versandetiketten fehlte. ** Versandart DHL (aka DHL 3.0) (FFU-5482)**

Das Verhalten der Nachnahme bei DHL wurde korrigiert.

### Release version 25.21.9

*Veröffentlichungsdatum: 12. Juni 2025 *#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (FFU-5491)**

Die Gewichtskalkulation für JIT wurde korrigiert.

### Release version 25.21.8

*Veröffentlichungsdatum: 11. Juni 2025 *#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (PIM-3001)** Ein Problem wurde behoben, bei dem die Verwendung von englischen Variablen wie {DELIVERY_NOTE} in Referenznummern die DHL Versandmethode störte. ** Lieferschein (FFU-5488)**

Ein Fehler wurde behoben, bei dem DHLExpress und PostAT angezeigt haben, dass die Versandmethode für internationalen Paketsendungen nicht verfügbar war.

### Release version 25.21.7

*Veröffentlichungsdatum: 10. Juni 2025 *#### Neue Funktionen **Drucker (PF-3903)** Ein CalendarPicker für Datums- und Zeitfilter im NextGen-Datentisch wurde eingeführt. ** POS (FAC-4250)**

Die Aktivierung der neuen POS-Funktionalität über eine Benachrichtigung wurde ermöglicht.

#### Verbesserungen **Kassenbuch (FAC-4358)** Die Formulierung des POS-Aktivierungsmodals wurde angepasst, um die Verständlichkeit zu verbessern. ** Settings Center (PF-3930)** Die Benutzererfahrung im Einstellungszentrum wurde verbessert. ** Angebot (PF-3926)** Das Sendeformular v2 für alle Mini-Details von Geschäftsdokumenten in der Aktionsliste wurde aktiviert. ** Settings Center (PF-3885)**

Die Benutzererfahrung auf der Unternehmensdatenseite wurde verbessert.

#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (FFU-5406)** Ein Problem wurde behoben, bei dem JIT-Komponenten auf CN23-Formularen für DHL nicht funktionierten. Bei korrekter Konfiguration von DHL werden jetzt der HS-Code und das Gewicht der Komponenten korrekt übernommen. ** SalesOrder API (IMPAPI-567)** Ein Problem im API-Endpunkt zum Aktualisieren von Verkaufsaufträgen wurde behoben, bei dem customerOrderNumber und customerNumber unbeabsichtigt überschrieben wurden. ** Reports (XIN-2177)** Ein Problem mit dem E-Mail-Export im neuen Berichtsmodul wurde behoben, bei dem Download-Links manchmal zu schnell abliefen. ** Drucker (PF-3927)** Ein Problem wurde behoben, bei dem das Aktions-Dropdown im NextGen-Datentisch nicht korrekt angezeigt wurde. ** N/a (PF-3907)** Ein Problem mit dem nie verschwindenden Download-Ladeanzeiger wurde behoben. ** Tickets (PF-3905)** Probleme beim Abrufen von Sonderzeichen aus dem Betreff im Ticketimport wurden behoben. ** Adressen (PF-3887)** Mehrere Fehler und kleine Inkonsistenzen in der Kunden-API wurden behoben. ** Drucker (PF-3884)** Probleme mit dem erneuten Drucken mit dem Download-Drucker aus dem Versandzentrum wurden behoben. ** Inventur (FFU-5354)**

Ein Problem wurde behoben, das das erneute Einreichen des Antrags zum Abschluss des Inventurablaufs verhinderte.

## 25.20 Release notes

### Release version 25.20.6

*Veröffentlichungsdatum: 06. Juni 2025 *#### Fehlerbehebungen **Adapterbox (FAC-4355)**

Das Drucken von Belegen im POS funktioniert wieder korrekt.

### Release version 25.20.4

*Veröffentlichungsdatum: 03. Juni 2025 *#### Neue Funktionen **Reports (XIN-2081)**

Im Modul Reports können geplante E-Mail-Exporte nun an eine spezifizierte Liste von E-Mail-Adressen gesendet werden.

#### Verbesserungen **Spedition (PF-3857)** Send-Formular v.2.0.0 ist jetzt für Send Spedition aktiviert. ** Preisanfrage (PF-3852)** Send-Formular v.2.0.0 ist jetzt für Preisanfragen aktiviert. ** Layoutvorlagen Anhang (PF-3835)**

Die Erstellung von Auftragsanhängen (während der Vorbereitung der Bearbeitungsseite) wurde stabilisiert.

#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (FFU-5446)** Ein Problem wurde behoben, bei dem negative Versandkosten dazu führten, dass die DHL-API einen Fehler auslöste. Negative Werte werden jetzt in 0,0 umgewandelt. ** Reports (XIN-2062)** Ungültige Spalten werden in der Umsatzauswertungstabelle im Modul Revenue Analysis nicht mehr angezeigt. ** Amazon Seller App (PF-3917)** Ein Problem, das die Amazon Seller App zum Neuladen veranlasste, wurde behoben. ** Drucker (PF-3902)**

Ein Fehler in der Druckaufgabentabelle wurde behoben, bei dem das erneute Ausführen eines Druckauftrags das Statuslabel in der Benutzeroberfläche nicht aktualisierte.

## 25.19 Release notes

### Release version 25.19.5

*Veröffentlichungsdatum: 30. Mai 2025 *#### Neue Funktionen **Versandart DHL (aka DHL 3.0) (PIM-2998)**

Die Fähigkeit, vorläufige Rücksendeetiketten im selben Format und Druckauftrag wie ein Versandetikett für DHL zu erstellen, wurde hinzugefügt.

### Release version 25.19.4

*Veröffentlichungsdatum: 28. Mai 2025 *#### Verbesserungen **Versandart DHL (aka DHL 3.0) (PIM-2990)**

DHL kann jetzt Pakete mit einer einheitlichen Versandart an National, Euro und International senden.

#### Fehlerbehebungen **Versandart DHL (aka DHL 3.0) (PIM-2997)** Es wurde ein Problem behoben, bei dem die Packstation-Nummer für DHL nicht im korrekten Namensfeld (Name3) gesetzt wurde. ** Tages-Auto-Versand (FFU-5410)**

Ein Problem wurde behoben, bei dem Pakete bei der Nutzung von Autoversand Plus nicht mit DHL versichert wurden.

### Release version 25.19.3

*Veröffentlichungsdatum: 28. Mai 2025 *#### Verbesserungen **E-invoice (FAC-4320)**

Die Leitweg-ID Konfiguration befindet sich jetzt in Adress-Freitextfeld 20, vorher war sie in den Plugin-Einstellungen zu finden.

### Release version 25.19.2

*Veröffentlichungsdatum: 27. Mai 2025 *#### Neue Funktionen **Versandart DHL (aka DHL 3.0) (PIM-2966)** Die Funktion 'Sofort abschließen' wurde zur DHL-Versandart hinzugefügt. ** Versandart DHL (aka DHL 3.0) (FFU-1555)** Ein Rücksendeetikett (Retoure beigelegt) wurde für DHL 3.0 hinzugefügt. ** Versandart DHL (aka DHL 3.0) (FFU-811)** Nachnahme ist jetzt mit DHL 3.0 möglich. ** Produktion (PF-3853)** Version 2.0.0 des Send-Formulars ist jetzt für die Produktion aktiviert. ** Lieferschein (PF-3851)** Version 2.0.0 des Send-Formulars ist jetzt für Lieferscheine aktiviert. ** Email Service (PF-3791)** Es wurde eine neue Option hinzugefügt, um E-Mail-Antworten auf ein Maximum von einem pro Ticket zu begrenzen. ** Produktion (PF-3853)** Das Send-Formular v.2.0.0 ist jetzt für die Produktion aktiviert. ** Lieferschein (PF-3851)** Das Send-Formular v.2.0.0 ist jetzt für den Lieferschein aktiviert. ** Email Service (PF-3791)**

Eine neue Option ermöglicht das Festlegen einer maximalen E-Mail-Antwort pro Ticket.

#### Verbesserungen **Versandart DHL (aka DHL 3.0) (FFU-5259)** Beim Vorbereiten von Exportdaten für DHL wird der Warenwert aus einem Auftrag entnommen, wenn keine Rechnung verfügbar ist. ** N/a (PIM-2962)** Die Datenbank-Komponente speichert die Tisch-Einstellungen standardmäßig nicht mehr. Benutzer können sich für die Speicherung der Einstellungen entscheiden. ** Kommissionierlauf (PIM-2912)** Die Abfrageoptimierung hat die Geschwindigkeit des Zugriffs auf die Liste der Kommissionierläufe verbessert. ** Adressen (PF-3844)** Die PATCH-Kunden-API erlaubt jetzt die Aktualisierung von Kontaktgruppen. ** Tickets (PF-3755)** Sonderzeichen und Emojis werden jetzt in Ticketantworten unterstützt. ** N/a (PIM-2962)** Die Daten-Tabellen-Komponente speichert jetzt standardmäßig keine Tabelleneinstellungen. Verbraucher können sich für die Persistenz der Einstellungen entscheiden. ** Kommissionierlauf (PIM-2912)** Die Optimierung von Abfragen hat die Geschwindigkeit der Abholung der Kommissionierläufe verbessert. ** Adressen (PF-3844)** Kontaktgruppen können jetzt mithilfe der PATCH Kunden-API aktualisiert werden. ** Tickets (PF-3755)**

Tickets unterstützen jetzt Antworten mit Sonderzeichen und Emojis.

#### Fehlerbehebungen **N/a (PF-3882)** Das Problem, bei dem das X1-Modalfenster den gesamten Bildschirm nicht abdeckte, wurde gelöst. ** N/a (PF-3840)** Das Problem, dass die benutzerdefinierte Navigationsreihenfolge nicht eingehalten wurde, wurde korrigiert. ** Amazon (ECOM-5105)** Das Problem der doppelten Rechnungen bei Amazon IDU-Bestellimporten aus der Schweiz wurde gelöst. ** Amazon (ECOM-5103)** Ein Problem bei der VCS-Konfigurationsverwaltung, das zu einer Deaktivierung bei einigen Kunden führte, wurde behoben. Der VCS-Mechanismus funktioniert jetzt wie erwartet. ** N/a (PF-3882)** Ein Problem wurde behoben, bei dem der X1-Modalfond nicht die gesamte Seite abdeckte. ** N/a (PF-3840)** Ein Problem wurde behoben, bei dem die benutzerdefinierte Navigationsreihenfolge nicht eingehalten wurde. ** Amazon (ECOM-5105)** Die Nutzung von Amazon IDU sollte nicht mehr zu doppelten Rechnungen führen, wenn Bestellungen aus der Schweiz importiert werden. ** Amazon (ECOM-5103)**

Ein Problem wurde behoben, bei dem die VCS-Konfiguration für einige Kunden deaktiviert war. Der VCS-Mechanismus funktioniert jetzt wie vorgesehen.

## 25.18 Release notes

### Release version 25.18.7

*Veröffentlichungsdatum: 21. Mai 2025 *#### Neue Funktionen **Angebot (PF-3847)**

Version 2.0.0 des Versandformulars ist jetzt für das Versenden von Angeboten aktiviert.

#### Verbesserungen **Einvoice (FAC-4183)** Die Funktion für elektronische Rechnungen zeigt jetzt bis zu 150 Projekte zur Auswahl an. ** Bestellung (PF-3859)** Das Bestellung Versandformular unterstützt jetzt mehrere Kanäle wie Download und E-Mail. ** Shopware 5 (ECOM-4144)**

Sonderzeichen in Artikelbeschreibungen werden nicht mehr maskiert angezeigt.

#### Fehlerbehebungen **N/a (PF-3894)** Ein Problem wurde behoben, bei dem die Sortierung bestimmter Spalten in den NextGen-Datenbanken fehlschlug. ** Amazon Seller App (PF-3875)** Ein Problem wurde behoben, bei dem die Amazon Seller App nicht zugänglich war. ** Api (XIN-2151)** Das Problem mit dem AnalyticsClient wurde behoben. ** Kassenbuch (FAC-3742)**

Eine Race Condition, die zu doppelten IDs im Kassenbuch führte, wurde beseitigt.

## 25.17 Release notes

### Release version 25.17.8

*Veröffentlichungsdatum: 19. Mai 2025 *#### Fehlerbehebungen **Chargen (FFU-5316)**

Ein Problem wurde behoben, bei dem die Umlagerung oder Entnahme von Bestand nicht abgeschlossen werden konnte, wenn mehrere Chargen mit Mindesthaltbarkeitsdatum verwendet wurden.

### Release version 25.17.7

*Veröffentlichungsdatum: 16. Mai 2025 *#### Fehlerbehebungen **Grundeinstellungen (SRE-2813)** Das Problem, dass PDF-Hintergründe beim Speichern der Grundeinstellungen deaktiviert wurden, wurde behoben. ** Sendcloud (FFU-5320)**

Ein Problem wurde behoben, bei dem SendCloud-Versendungen für nationale Sendungen scheiterten, wenn in Sendcloud keine EORI-Nummer eingegeben wurde.

### Release version 25.17.6

*Veröffentlichungsdatum: 13. Mai 2025 *#### Fehlerbehebungen **N/a (PF-3880)**

Ein Link wurde korrigiert, um das erneute Anzeigen des Auffüllmoduls zu ermöglichen.

### Release version 25.17.4

*Veröffentlichungsdatum: 13. Mai 2025 *#### Verbesserungen **Artikel Kalkulation (PIM-2956, FFU-5207)** Der Prozessstarter für die automatische Preiskalkulation des BOM ist jetzt so konfiguriert, dass er jede Nacht um 03:00 Uhr läuft. ** Projekte (PF-3809)** Der Dashboard-Tab des Projektmoduls wurde für schnellere Modalfunktionalitäten optimiert, mit verbesserter Dashboard-Logik. ** Lagerverwaltung (FFU-4989)**

Die Leistung der Lagerbestandslistenansicht im Modul Lager wurde für schnellere Datenladezeiten optimiert.

#### Fehlerbehebungen **Deposit (FFU-5101)**

Ein Problem wurde behoben, bei dem die Menge an Einlagenteil-Listenartikeln nicht korrekt aktualisiert wurde.

## 25.16 Release notes

### Release version 25.16.6

*Veröffentlichungsdatum: 09. Mai 2025 *#### Fehlerbehebungen **Artikel (FFU-5262)**

Ein Problem wurde behoben, bei dem der Prozessstarter in bestimmten Szenarien mit zahlreichen Artikelbestandsänderungen stoppte.

### Release version 25.16.5

*Veröffentlichungsdatum: 08. Mai 2025 *#### Neue Funktionen **Abolauf / Abosystem / Subscription module (FAC-4178)**

In einem Auftrag ist nun die Möglichkeit sichtbar, automatische Abonnements zu erstellen, wenn ein abonnierbarer Artikel enthalten ist, unabhängig vom bestehenden Abonnementstatus des Kunden für diesen Artikel.

### Release version 25.16.4

*Veröffentlichungsdatum: 08. Mai 2025 *#### Verbesserungen **Batches / Picklisten Profile (FFU-5261)**

Ein Fallback-Mechanismus für den `batches` Cronjob wurde bereitgestellt, der es ermöglicht, dessen Ausführung im Falle eines Problems zurückzusetzen.

### Release version 25.16.3

*Veröffentlichungsdatum: 07. Mai 2025 *#### Fehlerbehebungen **Lieferschein (FFU-5260)** Ein Problem wurde behoben, bei dem das Gewichtsfeld im DHL-Versandetikettenformular auf kleineren Bildschirmen nicht anklickbar war. ** POS (FAC-4240)**

Die Summe pro Zahlungsmethode ist im Tagesbericht wieder verfügbar.

### Release version 25.16.2

*Veröffentlichungsdatum: 06. Mai 2025 *#### Neue Funktionen **Settings Center (PF-3830)** Die Integration mit dem Mirakl-Marktplatz ist jetzt aktiviert. ** Adressen (PF-3225)** Es ist jetzt möglich, die Standardkontaktperson von Kunden zu verwalten. ** SalesOrder API (FFU-5195, FAC-4176)** Die Sales Order API unterstützt jetzt vier zusätzliche Währungen: ARS (Argentinischer Peso), CLP (Chilenischer Peso), SAR (Saudi-Riyal) und AED (VAE-Dirham). ** Versandarten (FFU-1914)** Der Versandartikel Europaket wurde zu DHL hinzugefügt, mit der Möglichkeit, die Frankiermethode für Europaket (DAP, DDU, DXV, DDX) auszuwählen. ** Abolauf / Abosystem / Subscription module (FAC-4178)**

In einem Auftrag sehen Benutzer jetzt die Möglichkeit, automatische Abonnements zu erstellen, wenn ein abonnierbarer Artikel enthalten ist, unabhängig davon, ob der Kunde bereits ein Abonnement für diesen Artikel hat oder nicht.

#### Verbesserungen **N/a (XIN-2091)** Die Seitengröße in der Tabelle Druckaufträge kann jetzt auf bis zu 200 eingestellt werden. ** Versandzentrum (PF-3827, FFU-5188)** Die Leistung des Versandzentrums wurde für die Handhabung zahlreicher Artikelbilder verbessert. ** Email Backup (PF-3777)** Die Fehlermanagementprozesse beim Senden von E-Mails wurden verbessert. ** Artikel (PIM-2910)** Die Aktivierung der Schnellsuche in den Systemeinstellungen verbessert nun die Suchleistung in den Modulen Liefernotizen, Aufträge, Rechnungen und Artikel. ** Pdf (PF-3798, CCI-2269)** Die Leistung der PDF-Erstellung wurde durch Korrektur des Schriftarten-Caching-Verhaltens verbessert. ** Api (PF-3751)** API-Routen für Kundenkontaktpersonen wurden angepasst, um demselben Schema zu folgen. ** Lagerverwaltung (FFU-5141)** Die Leistung beim Laden der Bewertung der Lagerwertseite wurde verbessert. ** Chargen (FFU-3934)**

Die Leistung der Chargenverlauf-Datentabelle wurde optimiert.

#### Fehlerbehebungen **POS (FAC-4241)** Rechnungen, die aus Kunden mit bestimmten Preisgruppen erstellt wurden, enthalten jetzt korrekte Werte. ** Reports (XIN-2084)** Ein Fehler im Reports-Modul wurde behoben. Exportpläne mit monatlicher Frequenz können jetzt problemlos in den Exportkonfigurationen erstellt werden. ** Reports (XIN-2063)** Ein Fehler im Reports-Modul, bei dem Exporte als "abgelaufen" angezeigt wurden, obwohl sie noch gültig waren, wurde behoben. Nur gültige Exporte werden jetzt angezeigt. ** Reports (XIN-2014)** Ein Problem in der NextGen-Datentabelle, bei dem Sortierungsregeln entfernt wurden, nachdem eine Filterregel angewendet wurde, wurde behoben. ** Versandart DHL (aka DHL 3.0) (PIM-2955)** DHL wirft keine Validierungsfehler mehr, wenn Zolltarifnummern mit Punkten angegeben sind (z.B. 1234.12.12). ** Adressen (PF-3799)** Die Berechtigungsprüfungen der Customer API wurden angepasst, um Admin-Benutzern den Zugriff auf alle Endpunkte zu ermöglichen. ** Provisionen (PF-3792)**

Zugriffsprobleme in den Modulen Provisionen und Vertreterabrechnungen wurden behoben.

## 25.15 Release notes

### Release version 25.15.4

*Veröffentlichungsdatum: 29. April 2025 *#### Neue Funktionen **POS (FAC-4163)**

Ein neuer API-Endpunkt wurde eingeführt, der QR-Codes für POS bereitstellt.

#### Verbesserungen **Zahlungseingang (FAC-3974)** Die Leistung bei der Verarbeitung von Zahlungseingängen wurde verbessert. ** Tillhub (ECOM-5062)**

Die Tillhub-Shopverbindung unterstützt nun die Autorisierung über den Organisationsnamen.

#### Fehlerbehebungen **POS (FAC-4221)** Die Funktionalität zum Laden von Dokumenten mit nicht-numerischen Kundennummern im POS-Modul wurde wiederhergestellt. ** Benutzer (PF-3815)** Ein Problem mit der fehlerhaften Berechtigungsüberprüfung für die Modul-Erstellung-Schaltfläche wurde behoben. ** Verbindlichkeiten (FAC-4215)** Die Berechnung der Steuer über Summenwerte funktioniert wieder korrekt. ** Reports (XIN-2061)** Der No-Code-Editor im Modul Reports passt nun die Filter für Spalten vom Typ Datum nach dem Speichern des Berichts korrekt an. ** Versandart DHL (aka DHL 3.0) (PIM-2951)** Ein Problem beim Generieren eines Versandetiketts mit DHL bei Verwendung von Autoversand mit vorab generierten Versandetiketten wurde behoben. ** Reports (PF-3805)** Fehlerhafte Pfade in X1-Modulen bei aktivierter FF-Funktion wurden behoben. ** Getmyinvoice (FAC-4148)**

Der veraltete API-Endpunkt /v1/docscan führt nun bei Bereitstellung des optionalen Feldes meta.invoice_date nicht mehr zu Fehlern.

## 25.14 Release notes

### Release version 25.14.4

*Veröffentlichungsdatum: 25. April 2025 *#### Verbesserungen **Versand Aufsplitten (FAC-4202)**

Die Rabattaufteilung wird nun korrekt auf Aufträge mit unterschiedlichen Steuersätzen angewendet.

#### Fehlerbehebungen **Drucker (PF-3814)**

Ein Problem mit der PrintJobs-Tabelle, das die Anzeige von mehr als 50 Einträgen verhinderte, wurde behoben.

### Release version 25.14.3

*Veröffentlichungsdatum: 23. April 2025 *#### Neue Funktionen **Reports (XIN-1518)** SQL-Berichte können jetzt aus bestehenden No-Code-Berichten im Modul Berichte erstellt werden. ** Adressen (PF-3688, IMPAPI-198)**

API v2 ermöglicht die Zuweisung eines Kunden zu Kundengruppen durch Angabe einer Liste ihrer IDs.

#### Verbesserungen **Kassenbuch (FAC-4195)** Artikelbeschreibungen werden nun konsequent in Dokumente aufgenommen, wenn sie in den Projekteinstellungen aktiviert sind. ** Pdf (PF-3754)**

Die Leistung der PDF-Erstellung wurde beim Einsatz von benutzerdefinierten Schriftarten optimiert.

#### Fehlerbehebungen **Reports (XIN-2066)** Ein Problem im Reports-Modul wurde behoben, bei dem einige Berichte nicht geöffnet werden konnten. Alle Berichte sind nun zugänglich. ** Auftrag (FFU-5140)** Ein Fehler wurde behoben, der beim Umgang mit mehreren Rechnungen pro Auftrag während der Ampelberechnungen auftrat. ** Email Service (PF-3775)** Ein Problem wurde behoben, bei dem die Seite E-Mail-Konten nach dem erfolgreichen Verbinden von Google- oder Microsoft-Konten nicht sichtbar war. ** N/a (PF-3774)** Ein Problem mit der falschen Darstellung der Numerierung-Details-Seite wurde behoben. ** Seriennummern (FFU-5148)** Die Listenansicht im Modul Seriennummern wird nun mit Inhalten geladen. ** Verbindlichkeiten (FAC-4152)**

Daten im Bereich der Vorbuchhaltung wurden vorübergehend in der falschen Rubrik angezeigt, dies wurde korrigiert.

## 25.13 Release notes

### Release version 25.13.8

*Veröffentlichungsdatum: 16. April 2025 *#### Fehlerbehebungen **Finanzbuchhaltung Export (FAC-4169)**

PDF-Dateien mit Großbuchstaben im Dateinamen werden nun korrekt im DATEV-Export berücksichtigt.

### Release version 25.13.7

*Veröffentlichungsdatum: 15. April 2025 *#### Neue Funktionen **Adressen (PF-3624)** E-Mail-Validierung in den Modulen Dokumentensendung, Ticket-Erstellung und Kontakte hinzugefügt. ** Wiedervorlage (PF-3183)**

Möglichkeiten hinzugefügt, Nachverfolgungstickets per E-Mail über Kontakt -> CRM-Tab zu erstellen.

#### Verbesserungen **Reports (XIN-1304)** Bei der Ausführung von Berichten im Reports-Modul zeigt die Ergebnistabelle jetzt einen Summenwert für numerische Spalten an. ** N/a (PF-3634)** Die Sicherheit wurde durch die Implementierung einer strengeren CORS-Konfiguration erhöht. ** UPS (OAuth) (FFU-4406)**

Die Versandmethode UPS (OAuth) unterstützt nun Nachnahme.

#### Fehlerbehebungen **Angebot (PIM-2944)** Die Reihenfolge der Dateien, die zur Auswahl eines Artikelbildes für Dokumente verwendet wird, wurde korrigiert. ** Versandarten (FFU-5135)** Ein Problem wurde behoben, bei dem eine Versandpositionsbestellung mit ProductId = 0 eine Ausnahme verursachte. ** Produktion (FFU-5061)** Ein Fehler beim Herunterladen von Datenblättern als.zip-Archiv wurde behoben. ** Reports (XIN-2023)** Ein Problem mit den Tabellenfiltern im Reports-Modul wurde behoben. Numerische Filter werden nun konsequent im englischen Format verarbeitet. ** N/a (PF-3764)** Das Problem, dass Logos nicht korrekt in mehrseitige PDF-Dokumente eingebettet werden, wurde behoben. ** N/a (PF-3762)** Ein Problem mit der Seitengröße von NextGen-Tabellen wurde behoben. ** Benutzer Vorlage (PF-3761)** Die Benutzer-API wurde behoben, um eine Filterung nach E-Mail zu ermöglichen. ** Einvoice (FAC-4104)** Fehlende Details zur empfangenden Partei im generierten XML für E-Rechnungen wurden hinzugefügt. ** Auftrag (FAC-3990)**

Bei Aufträgen mit teilweise stornierten Positionen werden die Rechnungen nun korrekt als teilweise storniert markiert.

## 25.12 Release notes

### Release version 25.12.5

*Veröffentlichungsdatum: 10. April 2025 *#### Fehlerbehebungen **Login (PF-3789)**

Das Problem mit Benachrichtigungs-Logout-Popups, insbesondere auf MacOS und Safari, wurde behoben.

### Release version 25.12.4

*Veröffentlichungsdatum: 08. April 2025 *#### Verbesserungen **Shopify (ECOM-5080)**

Der veraltete API-Aufruf zur Bestimmung von Steuersätzen beim Artikelimport wurde ersetzt.

#### Fehlerbehebungen **(FAC-4149)** Der Fiskaly-Kassen-POS-Abschlussprozess für neue Kunden wurde behoben. ** Datev-connect-online (ECOM-5078)**

Ein Problem, bei dem das Setzen eines Logos als Dokumentenhintergrund in den Haupteinstellungen unter bestimmten Umständen fehlschlagen konnte, wurde behoben.

### Release version 25.12.3

*Veröffentlichungsdatum: 08. April 2025 *#### Neue Funktionen **Versandart DHL (aka DHL 3.0) (FFU-2260)**

Die auf dem Versandlabel gedruckte Referenznummer ist nun konfigurierbar.

#### Verbesserungen **Pdf (PF-3660, FFU-4820)** Die Geschwindigkeit der PDF-Erstellung wurde bei Verwendung benutzerdefinierter Schriftarten verbessert. ** Iam (PF-3377)** Das Aktualisieren der Benutzersitzung über Tabs hinweg wurde optimiert, um die Benutzererfahrung zu verbessern und erzwungene Abmeldungen von allen Tabs zu verhindern. ** Post.AT (FFU-4885)** Die Versandart 'Post AT' ermöglicht nun das Speichern der Sendungsverfolgungsnummer nach dem Drucken des Versandlabels. ** Lagerverwaltung (FFU-4825)** Verbesserungen bei der Lagerverlagerung in der EN-Version verhindern nun doppelte Umlagerungen für dieselbe Verlagerungsanforderung. ** E-invoice (FAC-4101)** Für X-Rechnung wird das `BuyerReference` mit dem Wert aus Frei-Feld 20 im Kontakt gefüllt, wenn vorhanden; andernfalls enthält es die Adress-ID. ** Finanzbuchhaltung Export (FAC-3885)** Die Feldlänge des Erlöskontos wurde von 8 auf 15 Zeichen erweitert. ** Amazon (ECOM-4949)** Der Amazon Legacy Shopimporter wurde durch das Entfernen zweier kaum genutzter Beta-Funktionen - angehängte Angebote und Erstellen neuer Artikel - gestrafft. ** Amazon (ECOM-4874)**

Für Aufträge, die in die Schweiz, Liechtenstein oder Büsingen versandt werden, wird nun das VCS anstelle von IDU für die Rechnungsbearbeitung verwendet.

#### Fehlerbehebungen **Berichte (XIN-1973)** Die Tabelle in der Exportübersicht des Berichte-Moduls zeigt nun die Spalte 'Angeforderte Zeit' korrekt an. ** Kommissionierlauf (FFU-4736)** Links auf der Kommissionierliste-Seite wurden korrigiert. ** Produktion (FFU-4448)**

Das Sendeformular in der Produktion funktioniert nun korrekt bei Verwendung benutzerdefinierter PDFs.

## 25.11 Release notes

### Release version 25.11.8

*Veröffentlichungsdatum: 03. April 2025 *#### Verbesserungen **UPS (OAuth) (FFU-5045)**

UPS unterstützt nun USt-Ids, was eine Voraussetzung für papierlose Rechnungen für Mexiko ist.

#### Fehlerbehebungen **Berichte (XIN-2010)** Ein Fehler in der Benutzerzugriffssteuerung innerhalb des neuen Berichtmoduls wurde behoben. Benutzer mit eingeschränktem Zugriff auf bestimmte Berichte können die Ergebnisse nun korrekt herunterladen. ** DATEVconnect online (FAC-4129)**

[Datev Rechnungsservice] Der Export einer größeren Anzahl von Dokumenten überträgt nun die Dokument-PDFs korrekt.

### Release version 25.11.5

*Veröffentlichungsdatum: 01. April 2025 *#### Neue Funktionen **Reports (XIN-1955)** Ein Export-Permalink für einen Bericht kann nun im Berichtsmodul ohne begrenzte Gültigkeitsdauer erstellt werden. ** Übersetzungen (FAC-4066)** Benutzer können jetzt Zahlungsavisdokumente über das Übersetzungsmodul übersetzen. ** Zahlungsweisen (FAC-4042)**

Das Etikett unterhalb des QR-Codes auf einer Rechnung kann nun mit dem Übersetzungsmodul bearbeitet werden.

#### Verbesserungen **Grundeinstellungen (PF-3655)** Die Leistung der Unternehmensdaten-Seite wurde verbessert. ** Drucker (PF-3518)** Ein Druckauftragselement, das ein PNG enthält, kann jetzt als PDF heruntergeladen werden. ** Api (FFU-4973)** Die Geschwindigkeit des GET /api/returns-Endpunktes wurde verbessert. ** App Mobilepicking (FFU-4845)** In der Mobile Picking App (geschlossene Beta), das Berechtigungssystem wurde aktualisiert. Benutzer können jetzt granulare Berechtigungen zugewiesen bekommen und müssen keinen Admin-Zugriff mehr haben. ** Verbindlichkeiten (FAC-3991)**

Die Leistung beim Importieren von Daten von e-Rechnungen zu Verbindlichkeiten wurde verbessert.

#### Fehlerbehebungen **Auftrag (FFU-5002)** Die Hervorhebung nicht verfügbarer Artikel im Autovervollständigen wurde behoben und ist nun in allen Sprachversionen verfügbar. ** Tickets (PF-3730)** Veraltete Meldungen auf der Ticket-Seite wurden behoben. ** N/a (SRE-2735)** Internes Problem beim Umgang mit Dateien während der Dokumentenarchivierung behoben. ** Drucker (PF-3712)** Ein Problem mit Print Jobs-Filtern, die nach dem Neuladen der Seite nicht bestehen blieben, wurde behoben. ** N/a (PF-3707)** Es wurde ein Problem mit der Spaltenausrichtung in NextGen DataTables behoben. ** System-status (PF-3703)** Ein Problem wurde behoben, bei dem Vorfallmeldungen im Systemstatus-Incident-Bericht nicht angezeigt wurden. ** N/a (PF-3693)**

Ein Problem wurde behoben, bei dem NextGen DataTable Höhenbeschränkungen nicht respektierte.

## 25.10 Release notes

### Release version 25.10.10

*Veröffentlichungsdatum: 28. März 2025 *#### Verbesserungen **Autoversand Plus (FFU-5040)**

Ein Befehl zur Sperrbereinigung wurde hinzugefügt, um alle blockierten Sperren freizugeben, die verhindern, dass Batches und Autoversand-Plus-Jobs Aufträge bearbeiten.

#### Fehlerbehebungen **Tickets (PF-3743)**

Kompatibilitätsprobleme beim Ticketimport wurden behoben.

### Release version 25.10.8

*Veröffentlichungsdatum: 27. März 2025 *#### Verbesserungen **Rechnung (FAC-4110)**

Redundante Einträge in der pdfarchiv Tabelle, die zu Leistungsproblemen beim Öffnen von Rechnungen oder Abrufen von Dateien für den DATEV-Export führen könnten, wurden entfernt.

#### Fehlerbehebungen **Email Service (PF-3694)** Die Auswahl der Absende-E-Mail-Adresse wurde korrigiert, wenn mehrere Adressen vorhanden sind. Das System ruft nun die erste gültige E-Mail-Adresse ab. ** Adressen (PF-3684, FFU-4421)**

Ein Problem wurde behoben, das verhinderte, dass das 'Kommissionskonsignationslager' aufgrund einer ungültigen HTML-Struktur gespeichert werden konnte.

### Release version 25.10.6

*Veröffentlichungsdatum: 26. März 2025 *#### Neue Funktionen **Iam (PF-3625)** Ein Bestätigungsfenster wurde dem globalen MFA-Schalter hinzugefügt. ** POS (FAC-3401)**

EC-Zahlung ist jetzt verfügbar, wenn der Beleg ins POS geladen wird.

#### Verbesserungen **Projekte (PF-3503)**

Leistungsoptimierung wurde für das Projekt-Dashboard implementiert.

#### Fehlerbehebungen **Tickets (PF-2764)**

E-Mail-Inhalte werden jetzt korrekt auf der Ticket-Detailseite angezeigt.

## 25.9 Release notes

### Release version 25.9.9

*Veröffentlichungsdatum: 24. März 2025 *#### Verbesserungen **Artikel (PIM-2899)**

Das Suchverhalten ist jetzt für Kunden mit dem neuen Suchmodus konsistent. Sowohl Spalten- als auch globale Suchen verhalten sich gleich, wenn kein Platzhalter am Anfang verwendet wird (z. B. 'Schraube').

### Release version 25.9.8

*Veröffentlichungsdatum: 20. März 2025 *#### Fehlerbehebungen **Api (FFU-4932)**

Ein Fehler wurde behoben, der das Erstellen von Aufträgen durch die Legacy-Auftrag-API aufgrund von Systemfehlern verhinderte.

### Release version 25.9.7

*Veröffentlichungsdatum: 20. März 2025 *#### Verbesserungen **Artikel (PIM-2893)**

Die Geschwindigkeit der Such-Cache-Tabellenabfragen wurde für eine bessere Leistung verbessert.

### Release version 25.9.6

*Veröffentlichungsdatum: 19. März 2025 *#### Fehlerbehebungen **Tickets (PF-3690)**

Es wurde ein Problem behoben, bei dem E-Mails von Office365-Konten nicht in das Ticketsystem importiert werden konnten.

### Release version 25.9.5

*Veröffentlichungsdatum: 18. März 2025 *#### Fehlerbehebungen **Api (PIM-2865)**

Ein Problem wurde behoben, bei dem die Anfrage von ArtikelMedien über die API fehlschlug.

### Release version 25.9.4

*Veröffentlichungsdatum: 18. März 2025 *#### Neue Funktionen **Einvoice (FAC-4020)**

Eine zusätzliche Option zum Umgang mit der E-Rechnung als Anhang wurde hinzugefügt.

#### Verbesserungen **N/a (PF-3676)** Der Lizenzname wird jetzt in der Navigationskonfiguration angezeigt. ** Settings Center (PF-3662)** Die Seitenleiste ist jetzt immer eingeklappt, wenn sich der Benutzer im Einstellungszentrum befindet. ** Tickets (PF-3522)** E-Mails, die nicht standardmäßige MIME-Nachrichten enthalten, können jetzt importiert werden, mit einer Warnung für potenziell fehlerhafte Inhalte. ** Amazon (ECOM-4961)**

Der Amazon-Auftragsimport berücksichtigt jetzt die Einstellung "Beginn der Schnittstelle" und verwirft Aufträge, die älter als dieses Datum sind.

#### Fehlerbehebungen **Auftrag (FFU-4943)** Die Leistung der Versandzentrum-Datentabelle wurde verbessert, insbesondere bei aktivierter mobiler Kommissionierstapel-Funktionalität. ** Import/Export Zentrale (SRE-2677)** Für Windows-Benutzer wurde ein Problem behoben, bei dem das Importieren von CSV-Dateien einen Validierungsfehler während des Datei-Uploads auslösen konnte. ** POS (PF-3653)** Die Bearbeitungsaktion im POS-Pro-Projekt-Modul führt jetzt zur korrekten Seite. ** Verbindlichkeiten (FAC-4008)**

Im Modul Verbindlichkeiten funktioniert die Filterung nach Buchungstext in regulären Verpflichtungen wieder mit dem Prozentzeichen-Wildcard.

## 25.8 Release notes

### Release version 25.8.11

*Veröffentlichungsdatum: 14. März 2025 *#### Verbesserungen **Tickets (PF-3591)**

Die Fehlerbehandlung wurde während der Initialisierung des IMAP-Clients verbessert.

#### Fehlerbehebungen **Tickets (PF-3686)**

Ein Problem wurde behoben, bei dem der Tickets Importeur ein E-Mail-Konto aufgrund eines temporären Verbindungsproblems mit dem Mail-Client nicht aussetzte.

### Release version 25.8.10

*Veröffentlichungsdatum: 12. März 2025 *#### Verbesserungen **Artikel (PIM-2888)**

Die Geschwindigkeit der Such-Cache-Tabellenabfragen wurde verbessert.

### Release version 25.8.9

*Veröffentlichungsdatum: 12. März 2025 *#### Fehlerbehebungen **Api (FFU-4932)**

Ein Fehler wurde behoben, der verhinderte, dass die Legacy-Verkaufsauftrags-API aufgrund von Systemfehlern Aufträge erstellt.

### Release version 25.8.8

*Veröffentlichungsdatum: 12. März 2025 *#### Verbesserungen **Tages-Auto-Versand (FFU-4898)**

Die Vorbereitung für die Einführung kommender Leistungsverbesserungen wurde durch die Feinabstimmung der Indizes neu eingeführter Cache-Tabellen erreicht.

### Release version 25.8.4

*Veröffentlichungsdatum: 11. März 2025 *#### Neue Funktionen **Email Backup (PF-3648)** Benachrichtigung für Instanzadministratoren hinzugefügt, sich erneut mit Gmail zu verbinden, wenn ihr Zugriffstoken nicht geladen werden konnte. ** Einvoice (FAC-4013)**

E-Rechnungen können jetzt nach Bedarf erstellt werden.

#### Verbesserungen **Api (PIM-2792)** Alle Freifelder sind jetzt in der Artikel v2 API-Ansicht und Listenendpunkte enthalten, auch wenn das Freifeld leer ist. ** Settings Center (PF-3628)** Die MFA wurde in den Abschnitt Benutzermanagement im Settings Center verschoben. ** Email Backup (PF-3599)** E-Mails mit multipart/* Content-Type können jetzt importiert werden. **Email Backup (PF-3590)** Der Import von E-Mails wird bei permanenten Problemen mit dem Mail-Client ausgesetzt. ** Settings Center (PF-3558)** Die Zurück-Taste im Settings Center führt Nutzer jetzt zu ihrem zuvor besuchten Ort. ** Settings Center (PF-2871)** Nutzer können jetzt die vollständige Liste der Projekte im Settings Center einsehen. ** Konten Shopify (FAC-3549)** Rückerstattungen werden jetzt auch im Modul für eingehende Zahlungen mit Gutschriften abgeglichen. ** Gutschrift / Stornorechnung (FAC-3495)**

Gutschriften werden jetzt als gesendet markiert, wenn die Sammelfunktion genutzt wird.

#### Fehlerbehebungen **Reports (XIN-1893)** Ein Fehler im Berichtsmodul wurde behoben. Das Auswahlfeld im Zugriffsrechte-Tab filtert nun die Optionen korrekt basierend auf den Benutzereingaben, wenn Zugriffsrechte hinzugefügt werden. ** Netstock CSV Export (FFU-4877)** Die Netstock-Exportfunktion wurde korrigiert, um leere Ergebnisse effektiv zu verarbeiten. ** Artikel (PIM-2734)** Ein Fehler wurde behoben, bei dem das Feedback für die manuelle Exportierung eines Artikels in den Shop nicht angezeigt wurde. ** System-status (PF-3661)** Ein Fehler wurde behoben, der verhinderte, dass Nachrichten in Störungsberichten angezeigt wurden. ** Verbindlichkeiten (FAC-3331)**

Ein Unterschied im Vorbuchhaltungsabschnitt im Modul Verbindlichkeiten wurde behoben, wenn der Unterschied kleiner als 1 ist.

## 25.7 Release notes

### Release version 25.7.9

*Veröffentlichungsdatum: 07. März 2025 *#### Fehlerbehebungen **Tages-Auto-Versand (PF-3670, FFU-4884)**

Das Problem bei der PDF-Erstellung mit JPEG-Bildern wurde behoben.

### Release version 25.7.7

*Veröffentlichungsdatum: 05. März 2025 *#### Fehlerbehebungen **(FAC-4062)**

Die Datumsvalidierung bei eingehenden Zahlungen wurde korrigiert.

### Release version 25.7.5

*Veröffentlichungsdatum: 05. März 2025 *#### Fehlerbehebungen **Artikel (PF-3642, PIM-2864)**

Artikelbilder in PDF-Dokumenten werden nun korrekt angezeigt.

### Release version 25.7.4

*Veröffentlichungsdatum: 04. März 2025 *#### Neue Funktionen **Adressen (PF-3217)**

Kunden-API-Funktion zum Löschen einer Kundenadresse hinzugefügt.

#### Verbesserungen **Mailausgang Log (PF-3629)** Tracking-Parameter in URLs werden jetzt in E-Mails ordnungsgemäß kodiert, was die Genauigkeit der E-Mail-Verfolgung verbessert. ** Email Backup (PF-3621)** Benachrichtigung für Benutzer hinzugefügt, wenn der Versuch, eine E-Mail an eine falsch formatierte Adresse zu senden, fehlschlägt. ** Email Backup (PF-3568)** Fähigkeit hinzugefügt, um das falsch formatierte E-Mail-Datum zu analysieren. ** Settings Center (PF-3533)** Die Schaltfläche 'Zurück' auf der Nummernbereich-Bearbeitungsseite führt nun zurück zur Listenansicht. ** Adressen (PF-3216)** Kunden-API-Funktion verbessert, um eine Kundenadresse zu aktualisieren. ** Zahlungseingang (FAC-4002)** Transaktionen ohne übergeordnete Transaktion können im Zahlungseingang-Modul wieder gelöscht werden. ** Abschlagsrechnung (FAC-3902)** Das Verhalten von Texten und Zusammenfassungen in Rechnungen wurde geändert. ** Shopexporter (ECOM-4965)**

Der veraltete Tab, der die Upload-Funktionalität für benutzerdefinierte Shop-Importeure bereitstellte, wurde entfernt.

#### Fehlerbehebungen **Drucker (FFU-4834)** Ein Problem wurde behoben, bei dem das Drucken von Etiketten beim Verwenden bestimmter Spooler-Versionen verzögert sein konnte. ** Api (SRE-2682)** Ein Problem wurde behoben, das dazu führte, dass einige API-Anfragen fälschlicherweise abgelehnt wurden, was zu einem 429-Statuscode (Zu viele Anfragen) führte. ** Reports (XIN-1771)** Im Berichte-Modul wurde ein Fehler behoben, bei dem das Tippen im SQL-Editor den Cursor manchmal auf die erste Zeile des Editors bewegte. ** Email Service (PF-3587)** Ein Problem beim Import von E-Mails durch Überspringen der Absender-Header wurde behoben. ** Retouren Belege (FFU-4459)**

Ein Fehler wurde behoben, bei dem kostenlose Ersatzlieferungen mit einer anderen Währung als der ursprünglichen Auftrag erstellt wurden.

## 25.6 Release notes

### Release version 25.6.2

*Veröffentlichungsdatum: 28. Februar 2025 *#### Fehlerbehebungen **Presta (ECOM-5017)**

Eine Änderung der internen Mechanik führte zu unzuverlässigen Aktualisierungen der Aufträge. Dieses Problem wurde behoben, sodass Aufträge jetzt wie erwartet eingehen.

### Release version 25.6.1

*Veröffentlichungsdatum: 25. Februar 2025 *#### Neue Funktionen **Adressen (PF-3213)**

Ein API-Endpunkt wurde hinzugefügt, um die Adressen eines Kunden aufzulisten.

#### Verbesserungen **Artikel (PF-3610, PF-3606, PIM-2856)** PDF-Dateien sind jetzt wieder mit dem Adobe PDF-Reader kompatibel. ** Email Backup (PF-3609)** Tags für gesperrte E-Mails werden jetzt in der E-Mail-Kontoliste angezeigt. ** Email Backup (PF-3607)** Der Systemstatus wird aktualisiert, wenn die Gmail-Authentifizierung beim E-Mail-Versand fehlschlägt. ** Settings Center (PF-3559)** Benutzer können jetzt Bearbeitungsseiten im Settings Center neu laden. ** Übertragungen (CSV/XML/EDI/PDF) (FFU-4565)** Die TransferEdi-Komponente wurde für die Migration auf S3-Storage vorbereitet. ** Konten Mollie (FAC-3981)**

Die Rückerstattungsregeln von Mollie erfordern keine Shop-Verbindung mehr.

#### Fehlerbehebungen **Verbindlichkeiten (FAC-4039)** Ein Problem in der Verbindlichkeitenansicht wurde behoben, das dazu führte, dass PDF-Vorschauen unter bestimmten Bedingungen nicht korrekt funktionierten. ** Reports (XIN-1650)** Im Modul 'Reports' wurde ein Problem behoben, bei dem die Einstellungen zur Exportanzeige nach einer Änderung nicht korrekt aktualisiert angezeigt wurden. ** Artikel (PIM-2855)** Das Problem, bei dem das Vorschaubild beim Duplizieren eines Artikels falsch kopiert wurde, wurde behoben. Das Vorschaubild wird nun nicht mehr kopiert. ** Iam (PF-3611)** Verbessertes Handling von Zuständen in der MFA-Benutzertabelle. ** Vorlage (PF-3565)** Ein Problem wurde behoben, bei dem die Speicheraktion in E-Mail-Vorlagen nicht zurück zur Listenansicht führte. ** Verbindlichkeiten (FAC-4000)** Das Filtern nach Rechnungsnummer funktioniert nun korrekt, wenn zusätzliche Spalten ausgewählt und der Archiv-Filter aktiv sind. ** Zahlungsverkehr (FAC-3979)** Ein Fehler, bei dem der Skonto/Rabatt im Transaktionsmonitor des Zahlungsmoduls nicht korrekt angezeigt wurde, wurde behoben. ** POS (FAC-3385)** Das Problem, dass POS-Belege keine Mengenangaben enthielten, wenn die Menge kleiner als null war, wurde behoben. ** N/a (ECOM-4959)**

Fehler, die bei Artikelübertragungen auftraten, insbesondere wenn viele Updates nicht an den Vertriebskanal gesendet wurden, wurden behoben.

## 25.5 Release notes

### Release version 25.5.2

*Veröffentlichungsdatum: 18. Februar 2025 *#### Neue Funktionen **E-invoice (FAC-3993)**

'Gültig von' und 'Gültig bis' Daten wurden für die E-Rechnungs-Einstellungsseite eingeführt.

#### Verbesserungen **DATEVconnect online (FAC-3300)**

XML-Validierungsfehler werden jetzt in einer herunterladbaren CSV-Datei für den DATEV Rechnungsdatenservice 1.0 und Datev Unternehmen Online gesammelt.

#### Fehlerbehebungen **Batches / Picklisten Profile (FFU-4708)** Ein Fehler beim Ausführen des Batches-Cronjobs wurde behoben. ** Geschäftsbrief Vorlagen (PF-3545)** Die Verarbeitung von Tracking-Nummer-URLs in Geschäftsbriefen wurde korrigiert. ** Inventur (FFU-4650)** Der Fehler im Inventurergebnis bei Verwendung eines Betrags von 0 wurde behoben, um genaue Inventurdokumente sicherzustellen. ** N/a (FE-520)** Ein Problem mit der Modul-Lizenzvalidierung in der Navigationskonfiguration wurde behoben. ** Grundeinstellungen (FE-439)** Ein Problem wurde behoben, das Benutzer daran hinderte, das Übersetzungspopup in den Grundeinstellungen zu öffnen. ** Mahnwesen (FAC-3821)**

Ein Problem, bei dem Rabatte und Salden auf Rechnungen nicht korrekt angezeigt wurden, wenn sie über das Mahnsystem hinzugefügt wurden, wurde behoben.

## 25.4 Release notes

### Release version 25.4.6

*Veröffentlichungsdatum: 11. Februar 2025 *#### Fehlerbehebungen **Api (PIM-2853)**

Der API-Aufruf zur Abfrage von Artikeln mit einer Filterung nach externen Referenzen in Version 2 wurde korrigiert.

### Release version 25.4.5

*Veröffentlichungsdatum: 11. Februar 2025 *#### Neue Funktionen **N/a (PIM-2622)** Die automatische Berechnung von Einkaufspreisen für Stücklisten wurde implementiert. ** Adressen (PF-3196)** Eine neue API-Version zum Erstellen eines Kunden wurde hinzugefügt. ** Adressen (PF-3186)**

Version 2 der Get Customer by Id API ist jetzt verfügbar.

#### Verbesserungen **Zahlungseingang (FAC-3890)** Transaktionen mit einem größeren Betrag als die zugehörigen Transaktionen können nun wieder zugewiesen werden. Transaktionen, die mit anderen Transaktionen verknüpft sind, können nicht mehr gelöscht werden. ** Amainvoice (FAC-3716)** Gutschriften von Amainvoice sind jetzt länger als 3 Monate rückwirkend verfügbar. ** Magento 2 (ECOM-4880)**

Von Magento2 importierte Aufträge enthalten nun die USt-IdNr. der Versandadresse, falls vorhanden.

#### Fehlerbehebungen **Iam (PF-3577)** Ein Problem mit veralteten Daten in der MFA-Nutzertabelle wurde behoben. ** Lagerverwaltung (FFU-4668)** Das Verhalten der "Barcode drucken"-Schaltflächen wurde korrigiert. ** Umlagern mit neuem Datum (PF-3550, FE-716)** Ein Problem wurde behoben, bei dem Benutzer keine freien Tage bearbeiten konnten. ** Geschäftsbrief Vorlagen (PF-3549, FE-478)** Ein Problem mit doppelten Optionen im Sprachselektor der E-Mail-Vorlagen wurde behoben. ** Tickets (PF-3526)** Ein Fehler wurde behoben, der beim Import von E-Mails mit Datumsheadern, die Zeitzonen in Klammern enthalten, auftrat. ** Ticket Vorlagen (PF-3495)** Ein Problem wurde behoben, bei dem Benutzer Ticketvorlagen nicht bearbeiten konnten. ** Tickets (PF-3018)** Ein Fehler wurde behoben, der beim E-Mail-Import ohne Content-Transfer-Encoding-Kopfzeile auftrat. ** App Mobilepicking (FFU-4549)** Ein Problem mit der Erfassung von mobilen Picks Wannen im Versandzentrum wurde behoben. ** Retouren Belege (FFU-4416)** Ein Problem, das den Rückkehrfortschrittswert betraf, wurde behoben. ** Produktion (FFU-4143)** Der Druck von Etiketten in der Produktion wurde korrigiert. ** Drucker (FE-533)** Ein Problem mit unzugänglicher Paginierung auf den Seiten des Einstellungszentrums wurde behoben. ** Rechnung (FAC-3923)** Das Rendering-Problem des QR-Codes in Rechnungs-PDFs wurde behoben, wenn eine benutzerdefinierte Schriftart mit der Schweizer QR-Code-Funktion verwendet wurde. ** Bossapp (FAC-3868, FAC-3866, DATA-2664)** Ein Problem mit dem Wochenbericht in der Boss App wurde behoben. ** Amainvoice (FAC-3660)** Ein Problem wurde behoben, bei dem Amainvoice-Gutschriften falsch importiert wurden, wenn ein Rabattartikel oder Versandartikel enthalten war. ** Billbee (ECOM-4868)**

Probleme bei der Zuordnung von Versanddienstleistern in Billbee wurden behoben. Die Zuordnung ist jetzt nicht mehr von der Groß- und Kleinschreibung abhängig.

## 25.3 Release notes

### Release version 25.3.8

*Veröffentlichungsdatum: 10. Februar 2025 *#### Verbesserungen **N/a (PIM-2825)**

Bilder für neu erstellte Artikel sind jetzt in Dokumenten sichtbar.

#### Fehlerbehebungen **N/a (PF-3573, FFU-4662)**

Ein Leistungsproblem im Zusammenhang mit der PDF-Erzeugung wurde behoben.

### Release version 25.3.4

*Veröffentlichungsdatum: 10. Februar 2025 *#### Neue Funktionen **Reports (XIN-1712)**

Der KI-Copilot im Reporting-Modul unterstützt nun die Erstellung von Berichten mit Parametern.

#### Verbesserungen **Dropshipping Lieferant (FFU-4544)** Optimierung der Geschwindigkeit des Assistenten in Dropshipping-Prozessen. ** Lagerverwaltung (FFU-3983)** Die Bestandsanzeige in der Lagerverwaltung sortiert Artikel jetzt nach dem Lagerregal. ** System-status (PF-3268)** Dashboard-Warnungen für Datenübertragungen werden jetzt im SystemStatus-Dashboard angezeigt. ** System-status (PF-3119)** SystemHealth-Ereignisse werden absteigend nach Datum sortiert. ** Provisionen (FAC-3911)** Eine Einzigartigkeitsprüfung nach Projekt wurde im Provisionsmodul implementiert. ** Api (FAC-3457)**

Die Rechnungs-API ist jetzt flexibler und erlaubt Teil-Payloads, um nur die erforderlichen Daten zu aktualisieren.

#### Fehlerbehebungen **Shopexporter (ECOM-4897)** Ein Problem, das den automatisierten Artikel-Export daran hinderte, korrekte Metrikdaten zu erzeugen, wurde behoben. ** Tickets (PF-3505)** Ein Problem wurde behoben, bei dem ein aus einem Ticket erstellter Folgeauftrag einen Link zum falschen Ticket enthielt. ** Exportvorlage (PF-3241)** Ein Navigationsproblem im Import/Export Center wurde korrigiert. ** Inventur (FFU-4444)** Ein Problem wurde behoben, bei dem die 'alte' Bestandsfunktionalität mehrfach Bestandsbuchungen anlegte, wodurch Bestände für erfasste Mengen fälschlicherweise verdoppelt wurden. ** Drucker (FE-543)** Die Navigation von der Druckerdetailseite zu den Druckerverbindungen wurde behoben. ** N/a (FE-507)** Breadcrumb-Navigationsprobleme im Einstellungscenter wurden gelöst. ** Gutschrift / Stornorechnung (FAC-3907)**

Ein Problem wurde behoben, bei dem Gutschrift-PDFs nicht aus dem Archiv abgerufen wurden und aktualisierte Daten trotz Schreibschutz angezeigt wurden.

## 25.2 Release notes

### Release version 25.2.5

*Veröffentlichungsdatum: 29. Januar 2025 *#### Fehlerbehebungen **N/a (FFU-4615)**

Ein datenbezogenes Problem im Korrekturprozess der Lagerbewegung wurde behoben.

### Release version 25.2.4

*Veröffentlichungsdatum: 29. Januar 2025 *#### Verbesserungen **Artikel (PIM-2834, CCI-2245)** Die SQL-Abfrage bezüglich Thumbnail-Einstellungen in der Artikel Tabelle wurde entfernt. ** Shopexporter (ECOM-4904)** Der Exportmechanismus für Artikel wird überarbeitet, um die Leistung zu verbessern. Die zugehörigen Schaltflächen in den Verkaufskanaleinstellungen werden nach der Aktivierung der Funktion obsolet. ** Shopify (ECOM-4902)**

Eine Benachrichtigung wird angezeigt, wenn ein Artikelbild die maximal zulässige Größe für Shopify überschreitet.

### Release version 25.2.3

*Veröffentlichungsdatum: 29. Januar 2025 *#### Neue Funktionen **System-status (PF-3476)**

Systemstatusberichte für das FTP-Backup-Modul wurden eingeführt.

#### Verbesserungen **Adressen (PF-2966)**

Benutzer können jetzt Rücksendungen im Bereich Belege im Kundenprofil einsehen. Außerdem ist die Filterung nur für Rücksendungen verfügbar.

#### Fehlerbehebungen **Übertragungen (CSV/XML/EDI/PDF) (FFU-4529)** Das Problem der Übertragungsdatei, bei dem CSV-Dateien keine Spaltenüberschriften enthielten, wurde behoben. ** Übertragungen (CSV/XML/EDI/PDF) (FFU-4522)** Ein ungültiger Abfragefehler im CSV-Import des Übertragungsmoduls im Zusammenhang mit Sendungsverfolgungsnummern wurde behoben. ** Adressen (PF-2881)** Fehlerhafte Telefonanrufsymbole in der Liste der Kontaktpersonen wurden behoben. ** Zahlungseingang (FAC-3875)** Der Import-Zahlung-Cronjob läuft jetzt korrekt, auch wenn keine vorherigen Importe vorgenommen wurden. ** Rechnung (FAC-3856)** Die Anzeige von Rechnungsbeträgen in der Listenansicht wurde korrigiert. ** Zahlungsverkehr (FAC-3765)** Ein Problem, bei dem Änderungen an Zahlungstransaktionen nicht gespeichert wurden, wenn sie einem Konto zugewiesen wurden, wurde behoben. ** Zahlungseingang (FAC-3587)**

Die Anzeige von Beträgen, wenn Zahlungseingänge nicht für Skonto berechtigt waren, wurde behoben.

## 25.1 Release notes

### Release version 25.1.7

*Veröffentlichungsdatum: 28. Januar 2025 *#### Verbesserungen **Artikel (PIM-2834, CCI-2245)**

SQL-Abfrage entfernt, wenn ein Vorschaubild in der Artikeltabelle zugewiesen wird.

### Release version 25.1.6

*Veröffentlichungsdatum: 23. Januar 2025 *#### Fehlerbehebungen **Übertragungen (CSV/XML/EDI/PDF) (FFU-4508)**

Die ungültige Abfrage im CSV-Import des Übertragungsmoduls im Zusammenhang mit Trackingnummern wurde behoben.

### Release version 25.1.5

*Veröffentlichungsdatum: 23. Januar 2025 *#### Neue Funktionen **Shipcloud (FFU-3616)**

Das Shipcloud-Modul beinhaltet jetzt ein Abholdatum-Feld zur Unterstützung des GO-Transportdienstes.

### Release version 25.1.4

*Veröffentlichungsdatum: 21. Januar 2025 *#### Fehlerbehebungen **Einvoice (FAC-3889)** Das Problem wird behoben, bei dem eingehende E-Rechnungen in Verbindlichkeiten nicht korrekt geparst wurden. ** Einvoice (FAC-3848)**

Das Problem beim Hochladen einer E-Rechnung in Verbindlichkeiten aus dem Dateireiter wird behoben.

### Release version 25.1.3

*Veröffentlichungsdatum: 21. Januar 2025 *#### Verbesserungen **Verbindlichkeiten (FAC-3854)** Die Schaltfläche 'Datei auswählen' wurde wieder hinzugefügt. ** Benutzer (PF-3415)** Ein Datentabellen-Element/Zeile kann entfernt werden, wodurch eine Weiterleitung zu einer Detailseite verhindert wird. ** System-status (PF-3272)** Alte Systemgesundheit wurde aus NextGen entfernt. ** Mahnwesen (FAC-3760)**

Wenn eine Rechnung mit der Option 'nicht in Mahnwesen anzeigen' zu einer Gutschrift verschoben wird, wird der Soll/Haben nun synchronisiert. Vorher war die Gutschrift nicht entsprechend gesetzt.

#### Fehlerbehebungen **Verbindlichkeiten (FAC-3859)** Ein Problem wurde behoben, bei dem das Klicken auf eine beliebige Schaltfläche innerhalb der Listenansicht des Verbindlichkeiten-Moduls anstelle der Ausführung der beabsichtigten Aktion in den Bearbeitungsmodus wechselte. ** Einvoice (FAC-3848)** Ein Problem wurde behoben, das beim Hochladen von E-Rechnungen im Verbindlichkeiten-Modul über die Datei-Registerkarte auftrat. ** Verbindlichkeiten (FAC-3794)** Das Problem, bei dem regelmäßige Verpflichtungen im Verbindlichkeiten-Modul nicht mehr funktionierten, wenn Daten mit dem "%"-Zeichen abgefragt wurden, wurde behoben. ** Wareneingang Paket Annahme (FFU-4190)** Korrektur bei der Etikettendruckfunktion im Wareneingangsbildschirm, wo 'MHD' und 'MHD3' Variablen nicht korrekt ersetzt wurden. ** Finanzbuchhaltung Export (FAC-3715)**

Der Wechselkurs im XML-Export von Rechnung/Gutschrift/Verbindlichkeit für Datev Online wurde angepasst. Vorher war ein inverser/umgekehrter Wechselkurs vorhanden; jetzt wird der reguläre verwendet.

## 25.0 Release notes

### Release version 25.0.5

*Veröffentlichungsdatum: 15. Januar 2025 *#### Neue Funktionen **Versandart DHL (aka DHL 3.0) (FFU-2615)**

Die Unterstützung für MRN (Master Reference Number) wurde für DHL-Sendungen implementiert.

### Release version 25.0.4

*Veröffentlichungsdatum: 14. Januar 2025 *#### Fehlerbehebungen **Bestellvorschlag (alt) (FFU-4457)**

Das Problem bei der Berechnung des Lieferzeitraums mit Einkaufspreisen wurde behoben.

### Release version 25.0.3

*Veröffentlichungsdatum: 14. Januar 2025 *#### Verbesserungen **Reports (XIN-1696)** In dem Reports Modul werden Berichtsexportkonfigurationen jetzt für Benutzer mit eingeschränktem Zugriff auf das Modul ausgeblendet. ** System-status (PF-3469)** Die Systemstatusmeldungen wurden für Situationen verbessert, in denen keine Standardnachricht vorhanden ist. ** Shopexporter (ECOM-4842)** Probleme mit Smarty-Templates führen nicht mehr dazu, dass der Auftragimport vollständig fehlschlägt. Eine Fehlermeldung wird ebenfalls angezeigt, um den Benutzer zu informieren. ** System-status (PF-3469)** Das Systemstatus-Messaging wurde für Fälle verbessert, in denen keine Standardnachricht vorhanden ist. ** Shopexporter (ECOM-4842)**

Probleme mit Smarty-Vorlagen führen nicht mehr zu einer vollständigen Unterbrechung des Bestellimportprozesses. Zusätzlich wird eine Fehlermeldung angezeigt, um den Benutzer zu informieren.

#### Fehlerbehebungen **POS (FAC-3857)** Die Funktion zum Öffnen der Kassenschublade wurde behoben. ** Paketmarke (PIM-2789)** Ein Problem wurde behoben, bei dem das 'Sofort Abschliessen' Kontrollkästchen nach der Gewichtsänderung in DHLVersenden nicht abgewählt wurde. ** System-status (PF-3233)** Ein Problem wurde behoben, bei dem Benutzer nicht alle Ereignisse im Abonnementmanagement laden konnten. ** Paketmarke (PIM-2789)** Ein Fehler wurde behoben, bei dem das `Sofort Abschliessen` Kontrollkästchen nicht deaktiviert wurde, nachdem das Gewicht in DHLVersenden geändert wurde. ** System-status (PF-3233)**

Ein Problem wurde behoben, bei dem Benutzer nicht alle Ereignisse im Abonnementmanagement laden konnten.

## 24.50 Release notes

### Release version 24.50.7

*Veröffentlichungsdatum: 08. Januar 2025 *#### Verbesserungen **SuperSearch (SRE-2598)**

Die Leistung der Smart-Suche wurde verbessert.

### Release version 24.50.5

*Veröffentlichungsdatum: 07. Januar 2025 *#### Verbesserungen **Etikettendrucker (PF-3429)** Ein Problem wurde behoben, bei dem heruntergeladene Dokumente zum Drucken keinen Inhalt enthielten. ** Hood (ECOM-4837)** Ein Fehler, der den Auftrag Import mit einem einzelnen Artikel ohne Auktions-ID verhinderte, wurde behoben. ** Ebay (ECOM-4833)** Das Problem mit falsch formatierten eBay-Kategoriedaten wurde behoben. ** Dateien (PF-3446)** Der Fehler, der verhinderte, dass an Kunden gesendete Dokumente in Xentral-Instanzen gespeichert wurden, wurde behoben. ** Mobile Inventory App (Flutter) (FFU-4407)** Ein Konflikt mit der Seriennummer während eines Inventurlaufs wurde behoben. ** Ebay (ECOM-4869)** Ein Fehler wurde behoben, der das Erstellen von eBay-Listings verhinderte. ** Shopify (ECOM-4867)** Fehler in den DPD-Tracking-Links aufgrund von URL-Escaping wurden behoben. ** E-Rechnung (FAC-3825)**

Ein Problem wurde behoben, das zu falschen Benachrichtigungen im Zusammenhang mit E-Rechnungen führte.