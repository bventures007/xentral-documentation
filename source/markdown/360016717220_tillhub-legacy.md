Mit dieser Schnittstelle kannst du xentral mit dem Online-Kassensystem Tillhub verbinden, um Verkäufe (Aufträge) in xentral zu importieren. Die Schnittstelle funktioniert wie ein Shopimporter.

## Features der Schnittstelle

Die Schnittstelle bietet dir folgende Features:

- Aufträge importieren
- Artikel von xentral zu Tillhub übertragen

Welche Funktionen im Einzelnen möglich sind, kannst du unter **Administration > Shop Schnittstelle > Übersicht > Shopfunktionen** überprüfen.

## Installation in xentral

Unter **Administration > Shop Schnittstelle > Übersicht > NEU ** kannst du nach**Tillhub** suchen:

## Details

Im Reiter **Details** kannst du Informationen zur Schnittstelle eintragen, Einstellungen sowie Zahlungsweisen anpassen, Versandarten angaben oder auch ein Gruppenmapping durchführen.

### Schnittstelle

Nachdem du Tillhub ausgewählt hast, kannst du im nächsten Schritt die nötigen Daten für die Verbindung der beiden Systeme eintragen:

#### Einstellungen

Befülle folgende allgemeine Felder:

- **Bezeichnung:** Trage die Bezeichnung des Shops ein
- **Aktiv:** Durch Anhaken aktivierst du den Shop
- **Projekt:** Trage optional ein Projekt ein oder wähle über das "Lupe"-Icon eines aus der Liste aus
- **Abholmodus:** Wähle den Abholmodus aus dem Drop-Down Menü aus
- **Datum von:** Trage das Startdatums des Abholmodus "ab Datum "ein"
- **Zeit:** Trage die Startzeit ein
- **Import-Modus:** Wähle aus dem Drop-Down Menü den Importmodus für Aufträge aus
- **Nur 1 Auftrag pro Anfrage:** Durch Anhaken wird nur ein Auftrag pro Anfrage abgeholt
- **Aufträge in Zwischentabelle: ** Durch Anhaken werden die Aufträge in einer Zwischentabelle gespeichert. Die Freigabe musst du dann manuell vornehmen ** Einstellungen für Shop oder Marktplatz**

-** Protokollierung im Logfile:** Durch Anhaken findet eine Protokollierung im Logfile statt
- **E-Mail:** Trage die E-Mail-Adresse ein, mit der du dich im Tillhub-Backend anmeldest
- **Passwort:** Trage das Passwort ein, mit dem du dich im Tillhub-Backend anmeldest
- **Standardadresse:** Trage die Kundenadresse aus den Stammdaten in xentral ein, die die Laufkundschaft abbildet
- **Aufträge Laufkundschaft direkt abschließen:** Durch Anhaken erstellst du keinen Lieferschein, daher kann keine Lagerbuchung stattfinden

Klicke abschließend auf **Speichern**.

Für die Laufkundschaft könnte z.B. eine eigene Adresse angelegt werden. Sie dient bei allen anonymen Verkäufen über die Kasse als Kunde.

## Verbindungsdaten prüfen

Sobald die Daten eingetragen wurden, kannst du die Verbindung zwischen beiden System über die Schaltfläche **Verbindung prüfen** prüfen.

Sobald die Verbindung erfolgreich war, erhältst du die Meldung **success**. Sollte die Verbindung nicht erfolgreich hergestellt werden, wird dir in einer Meldung eine Ursache mitgeteilt.

## Einstellungen in der Schnittstelle

Da der Tillhub-Importer genau wie ein Shopimporter funktioniert, kannst du die gleichen Einstellungen vornehmen wie in einer Shopschnittstelle. Informationen zu den Einstellungen findest du im Artikel[Online-Shops](#).

> **Anmerkung**
>
> Bitte beachte, dass der Artikeltransfer einschließlich der Bestandsabgleich-Funktion für Varianten nicht verfügbar ist. Du kannst daher keine Matrixprodukte übertragen oder abgleichen.