> **Tipp**
>
> Dies ist ein separater Artikel, um Release Notes für Kunden aufzulisten, die imBeta Programmsind.
>
> Falls du kein Teil des Beta-Programms bist, findest du die aktuellen Release Notes für dich hier:Release Notes (alle Versionen in 2025).

## 25.35 Release notes

### Release version 25.35.3

*Veröffentlichungsdatum: 15. September 2025 *#### Fehlerbehebungen **Api (CCI-2310)**

Autorisierungsfehler auf der ALTEN REST-API wurde behoben.

## 25.3 Release notes

### Release version 25.3.0

*Release date: 22-August-2024 *#### New Features **SuperSearch (PIM-2147)**

Resources with dashes and underscores can now be found through SuperSearch.

#### Improvements **Addresses (TAN-4405)** Increased the performance of the list endpoint with larger amounts of data in the system. ** Article properties translation (PIM-2192)** Missing English translations added for shipping method configuration ** Import/Export Central (PIM-2157)**`hinweis_einfuegen` variable can be used both in an initial import of products and in updates. ** Appstore (PF-2402)** Remove the US taxes module. ** Transfers (CSV/XML/EDI/PDF) (FFU-3183)** It is now possible to convert ISO-8859-1 files with special chars in TransferSmarty-account **Car Shipping Plus (FFU-3054)** Allow auto-ship sales-order if split to partially sales-orders **Financial accounting export (FAC-3108)** All of the available export formats for Xentral Invoices (DATEV CSV, DATEV XML, Rechnungsdatenservice 1.0) will now contain the invoice Due Date. ** Subscription run / subscription system / subscription module (FAC-3081)** A mechanism to prevent double execution of subscription-runs implemented **Amazon (ECOM-4289)** Changed some tooltips in amazon settings UI **Amazon (ECOM-4254)**

Amazon settings have been rearranged:

#### Bug Fixes **Templates (TAN-4539)** Icon of dashboard tile changed ** Api (TAN-4514)** Fixed: customer project is always default project after creation ** Article properties translation (PIM-2170)** Fixed an issue where part of the interface would show in German and part of the interface would show in English after leaving the app idle for multiple hours. ** Commissions (FAC-3181)** Correct commision will be selected for credit-notes if rule with product-category exits ** Amazon (ECOM-4554, CCI-2127)** Fixed automatic shopimport ** Amazon (ECOM-3808)**

Amazon order import will no longer create orders which have the street name copied into the department.

## 25.2 Release notes

### Release version 25.2.4

*Veröffentlichungsdatum: 09. Juli 2024 *#### Fehlerbehebungen **E-Mail Accounts (TAN-4543)**

Behoben Token-Probleme beim Verbinden

### Release version 25.2.2

*Veröffentlichungsdatum: 21. Februar 2025 *#### Fehlerbehebungen **Übertragungen (FFU-4528)** Fehlerhafte Abfrage im CSV-Import-Übertragungsmodul im Zusammenhang mit Sendungsnummern behoben. ** Übertragungen (FFU-4522)**

Fehlerhafte Abfrage im CSV-Import-Übertragungsmodul im Zusammenhang mit Sendungsnummern behoben.

### Release version 25.2.1

*Veröffentlichungsdatum: 22. Januar 2025 *#### Fehlerbehebungen **Einvoice (FAC-3889)** Das Problem wurde behoben, bei dem eingehende E-Rechnungen nicht korrekt in Verbindlichkeiten geparst wurden. ** Einvoice (FAC-3848)**

Das Problem beim Hochladen von E-Rechnungen in Verbindlichkeiten über die Registerkarte 'Dateien' wurde behoben.

### Release version 25.2.0

*Veröffentlichungsdatum: 21. Februar 2025 *#### Neue Funktionen **Versandart DHL (aka DHL 3.0) (FFU-2615)**

MRN (Master Reference Number) für DHL.

#### Verbesserungen **Adressen (PF-2966)** Der Benutzer kann jetzt Rücksendungen im Rahmen des Belegabschnitts im Kundenprofil sehen. Der Benutzer kann auch nur nach Rücksendungen filtern. ** Rechnung (FAC-3856)**

Beheben der Anzeige von Rechnungssummen in der Listenansicht.

#### Fehlerbehebungen **System-status (PF-3476)** Die Berichterstattung der Systemstatus für das FTP-Backup-Modul beginnt. ** Adressen (PF-2881)** Beheben von fehlerhaften Telefonanrufsymbolen in der Kontaktlistenansicht. ** Bestellvorschlag (alt) (FFU-4457)** Die Berechnung des Lieferzeitraums aus den Einkaufspreisen wurde behoben. ** Zahlungseingang (FAC-3875)** Beheben der Bedingung für den Ausführungszeitpunkt des Importzahlungs-Cronjobs - er sollte auch ausgeführt werden, wenn keine vorherigen Imports durchgeführt wurden. ** Verbindlichkeiten (FAC-3859)** Beheben eines Problems, bei dem ein Klick auf einen beliebigen Button innerhalb der Listenansichtsreihe des Verbindlichkeitsmoduls in den Bearbeitungsmodus wechselt, anstatt die beabsichtigte Aktion auszuführen. ** Verbindlichkeiten (FAC-3794)** Beheben eines Problems, bei dem regelmäßige Verpflichtungen im Verbindlichkeitsmodul nicht mehr funktionierten, wenn Daten mit dem "%"-Zeichen abgefragt wurden. ** Zahlungsverkehr (FAC-3765)** Beheben eines Problems, bei dem Änderungen an Zahlungstransaktionen nicht gespeichert wurden, wenn sie einem Konto zugeordnet wurden. ** Zahlungseingang (FAC-3587)**

Eingehender Zahlungseingang-Import: Anzeige des Betrags korrigiert, wenn die Zahlung nicht für den Frühzahlungsrabatt berechtigt war.

## 25.1 Release notes

### Release version 25.1.3

*Veröffentlichungsdatum: 20. Januar 2025 *#### Verbesserungen **Verbindlichkeiten (FAC-3854)**

Die Schaltfläche 'Datei auswählen' wurde wieder hinzugefügt.

#### Fehlerbehebungen **Verbindlichkeiten (FAC-3859)** Ein Problem wurde behoben, bei dem das Klicken auf eine beliebige Schaltfläche innerhalb der Listenansicht des Verbindlichkeiten-Moduls anstelle der Ausführung der beabsichtigten Aktion in den Bearbeitungsmodus wechselte. ** Einvoice (FAC-3848)** Ein Problem wurde behoben, das beim Hochladen von E-Rechnungen im Verbindlichkeiten-Modul über die Datei-Registerkarte auftrat. ** Verbindlichkeiten (FAC-3794)**

Das Problem, bei dem regelmäßige Verpflichtungen im Verbindlichkeiten-Modul nicht mehr funktionierten, wenn Daten mit dem "%"-Zeichen abgefragt wurden, wurde behoben.

### Release version 25.1.2

*Veröffentlichungsdatum: 15. Januar 2025 *#### Neue Funktionen **Versandart DHL (aka DHL 3.0) (FFU-2615)**

Die Funktion der Master-Referenznummer (MRN) für DHL wurde implementiert.

### Release version 25.1.1

*Veröffentlichungsdatum: 14. Januar 2025 *#### Fehlerbehebungen **Bestellvorschlag (alt) (FFU-4457)**

Korrektur der Berechnung des Lieferzeitraums auf Basis der Einkaufspreise.

### Release version 25.1.0

*Veröffentlichungsdatum: 14. Januar 2025 *#### Verbesserungen **Reports (XIN-1696)** Exportkonfigurationen für Berichte sind jetzt für Benutzer mit eingeschränktem Zugang im Reports-Modul ausgeblendet. ** SuperSearch (SRE-2598)** Die Leistung der Smart-Suche wurde verbessert. ** System-status (PF-3469)** Die Systemstatus-Meldungen wurden verbessert, wenn keine Standardmeldung vorhanden ist. ** Benutzer (PF-3415)** Ein Datentabellen-Element/Zeile kann entfernt werden, wodurch eine Weiterleitung zu einer Detailseite verhindert wird. ** System-status (PF-3272)** Alte Systemgesundheit wurde aus NextGen entfernt. ** Mahnwesen (FAC-3760)**

Wenn eine Rechnung mit der Option 'nicht in Mahnwesen anzeigen' zu einer Gutschrift verschoben wird, wird der Soll/Haben nun synchronisiert. Vorher war die Gutschrift nicht entsprechend gesetzt.

#### Fehlerbehebungen **Paketmarke (PIM-2789)** Problem behoben, bei dem das 'Sofort Abschliessen'-Checkbox nicht deselektiert wurde, nachdem das Gewicht in DHLVersenden geändert wurde. ** System-status (PF-3233)** Problem behoben, bei dem Benutzer alle Ereignisse im Abonnementmanagement nicht laden konnten. ** Wareneingang Paket Annahme (FFU-4190)** Korrektur bei der Etikettendruckfunktion im Wareneingangsbildschirm, wo 'MHD' und 'MHD3' Variablen nicht korrekt ersetzt wurden. ** POS (FAC-3857)** Korrektur zum Öffnen der Kassenschublade. ** Finanzbuchhaltung Export (FAC-3715)** Der Wechselkurs im XML-Export von Rechnung/Gutschrift/Verbindlichkeit für Datev Online wurde angepasst. Vorher war ein inverser/umgekehrter Wechselkurs vorhanden; jetzt wird der reguläre verwendet. ** Shopexporter (ECOM-4842)**

Probleme mit Smarty-Templates führen nicht mehr zum vollständigen Abbruch des Auftragsimports. Jetzt wird eine Fehlermeldung angezeigt, die den Benutzer über das Problem informiert.

## 25.0 Release notes

### Release version 25.0.3

*Veröffentlichungsdatum: 13. Januar 2025 *#### Fehlerbehebungen **POS (FAC-3857)**

Die Funktion zum Öffnen der Kassenschublade wurde behoben.

### Release version 25.0.1

*Veröffentlichungsdatum: 09. Januar 2025 *#### Verbesserungen **Reports (XIN-1696)** In dem Reports Modul werden Berichtsexportkonfigurationen jetzt für Benutzer mit eingeschränktem Zugriff auf das Modul ausgeblendet. ** SuperSearch (SRE-2598)** Die Leistung der Smart-Suche wurde verbessert. ** System-status (PF-3469)** Die Systemstatusmeldungen wurden für Situationen verbessert, in denen keine Standardnachricht vorhanden ist. ** Shopexporter (ECOM-4842)**

Probleme mit Smarty-Templates führen nicht mehr dazu, dass der Auftragimport vollständig fehlschlägt. Eine Fehlermeldung wird ebenfalls angezeigt, um den Benutzer zu informieren.

#### Fehlerbehebungen **Paketmarke (PIM-2789)** Ein Problem wurde behoben, bei dem das 'Sofort Abschliessen' Kontrollkästchen nach der Gewichtsänderung in DHLVersenden nicht abgewählt wurde. ** System-status (PF-3233)**

Ein Problem wurde behoben, bei dem Benutzer nicht alle Ereignisse im Abonnementmanagement laden konnten.

### Release version 25.0.0

*Veröffentlichungsdatum: 08. Januar 2025 *#### Verbesserungen **System-status (PF-3469)** Das Systemstatus-Messaging wurde für Fälle verbessert, in denen keine Standardnachricht vorhanden ist. ** Shopexporter (ECOM-4842)**

Probleme mit Smarty-Vorlagen führen nicht mehr zu einer vollständigen Unterbrechung des Bestellimportprozesses. Zusätzlich wird eine Fehlermeldung angezeigt, um den Benutzer zu informieren.

#### Fehlerbehebungen **Paketmarke (PIM-2789)** Ein Fehler wurde behoben, bei dem das `Sofort Abschliessen` Kontrollkästchen nicht deaktiviert wurde, nachdem das Gewicht in DHLVersenden geändert wurde. ** System-status (PF-3233)**

Ein Problem wurde behoben, bei dem Benutzer nicht alle Ereignisse im Abonnementmanagement laden konnten.

## 24.50 Release notes

### Release version 24.50.5

*Veröffentlichungsdatum: 06. Januar 2025 *#### Fehlerbehebungen **Ebay (ECOM-4869)** Ein Fehler wurde behoben, der das Erstellen von eBay-Listings verhinderte. ** Shopify (ECOM-4867)**

Fehler in den DPD-Tracking-Links aufgrund von URL-Escaping wurden behoben.

### Release version 24.50.4

*Veröffentlichungsdatum: 06. Januar 2025 *#### Fehlerbehebungen **E-Rechnung (FAC-3825)**

Ein Problem wurde behoben, das zu falschen Benachrichtigungen im Zusammenhang mit E-Rechnungen führte.