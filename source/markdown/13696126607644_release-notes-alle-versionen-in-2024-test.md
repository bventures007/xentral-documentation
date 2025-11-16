## 25.35 Release notes

### Release version 25.35.3

*Veröffentlichungsdatum: 24. Oktober 2025 *#### Fehlerbehebungen **Api (CCI-2310)**

Autorisierungsfehler auf der ALTEN REST-API wurde behoben.

## 25.3 Release notes

### Release version 25.3.0

*Veröffentlichungsdatum: 14. Juli 2025*

## 25.2 Release notes

### Release version 25.2.4

*Veröffentlichungsdatum: 10. April 2025 *#### Fehlerbehebungen **E-Mail Accounts (TAN-4543)** Behoben Token-Probleme beim Verbinden ** Übertragungen (FFU-4528)** Fehlerhafte Abfrage im CSV-Import-Übertragungsmodul im Zusammenhang mit Sendungsnummern behoben. ** Übertragungen (FFU-4522)**

Fehlerhafte Abfrage im CSV-Import-Übertragungsmodul im Zusammenhang mit Sendungsnummern behoben.

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