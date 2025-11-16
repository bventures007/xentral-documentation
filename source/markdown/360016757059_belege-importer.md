Mit dem **Belegeimporter ** kannst du **Belege ** aus externen Quellen oder anderen Systemen per**CSV-Datei** direkt in Xentral importieren. Das eignet sich z. B. für den Datentransfer aus einer anderen ERP- oder Buchhaltungssoftware, von Dienstleistern oder externen Abrechnungssystemen – etwa für Aufträge, Lieferscheine, Rechnungen oder Gutschriften. Der Import wird über einen Prozessstarter ausgeführt, sodass die Belege nach dem Hochladen automatisch im ERP weiterverarbeitet werden können.

> **Tipp**
>
> Wenn du **Stammdaten** importieren möchtest (z. B. Artikel, Adressen), verwende denCSV-Importer (Connect).
>
> Für **Shopbestellungen ** nutze dieStandardisierten Connect-Shop-Schnittstellen mit No-Code-Import, um**Aufträge direkt und automatisiert** zu übernehmen.

## Belegeimporter Funktionsumfang

Der Belege Importer unterstützt den Import folgender Belegarten: **Angebote **, ** Aufträge **, ** Lieferscheine **, ** Rechnungen **, ** Gutschriften **, Preisanfragen, ** Bestellungen **, ** Produktionen**, Proforma-Rechnungen, Adressen (dafür ist die Importzentrale besser geeignet).

> **Anmerkung**
>
> Du kannst mehrere Belege in einer CSV-Datei hochladen – jede Zeile entspricht dabei einer Belegposition.

- **Vielfältige Belegarten importieren**: Aufträge, Angebote, Bestellungen, Rechnungen, Gutschriften, Proforma-Rechnungen u. v. m.
- **Direkte Kundenzuordnung**: Kundennummern oder Lieferantennummern direkt im Import festlegen.
- **Abweichende Lieferadressen automatisch übernehmen**: inkl. Name, Abteilung, Straße, Ort, Postleitzahl und Land.
- **Komplette Beleg- und Zahlungsdetails importieren**: Belegnummern, Wunsch- oder Auslieferungsdatum, Zahlungsweise, Zahlungsziel und Skonto.
- **Versand- und Lieferbedingungen setzen**: Versandart, Lieferbedingung und Belegstatus individuell vorgeben.
- **Belegverknüpfungen herstellen**: z. B. Rechnungen mit Aufträgen oder Lieferscheinen verknüpfen.
- **Detaillierte Artikelpositionen importieren**: Artikelnummer, Bezeichnung, Menge, Preis, Rabatt, Währung, Steuersatz, Herkunftsland, Zolltarifnummer u. v. m.
- **Flexible Belegstruktur**: Gruppierung von Positionen zu einem Beleg per PARENT- und NEW-Logik.
- **Individuelle Texte einfügen**: Freitexte und Kopftexte direkt in den Beleg übernehmen.
- **Adressdaten komplett anlegen**: inkl. Ansprechpartner, Abteilungen, Telefonnummer, E-Mail, USt-IdNr. und Anrede.

## Bedienung und Workflow

Die folgenden Schritte zeigen dir den genauen Ablauf von der CSV-Auswahl bis zur Übertragung der Daten ins System.

**Schritte im Belegeimporter: **

1.** Datei auswählen** – Wähle deine vorbereitete CSV-Datei aus.
1. **Belegart festlegen** – Bestimme, ob du z. B. Aufträge, Rechnungen oder Gutschriften importierst.
1. **Status zuweisen** – Lege fest, welchen Status die Belege nach dem Import haben sollen (z. B. angelegt, freigegeben).
1. **Upload starten**– Starte den Importprozess. * Optional*: Zwischenspeicher leeren – Falls du den Import abbrechen oder Änderungen vornehmen möchtest.

> **Anmerkung**
>
> Im Reiter **Formate** findest du eine Liste aller möglichen Feldnamen. Die erste Zeile deiner CSV muss exakt diese Spaltenüberschriften enthalten, und es gilt: eine Position = eine Zeile.

## Wichtige Felder im Belegeimporter

Die folgende Tabelle listet alle unterstützten Feldbezeichnungen des Belegeimporters mit ihrer jeweiligen Bedeutung auf. Sie dient als Referenz, um deine CSV-Datei korrekt zu strukturieren und sicherzustellen, dass alle Daten den richtigen Feldern im System zugeordnet werden.

> **Anmerkung**
>
> In der **ersten Zeile ** der hochzuladenden CSV-Datei müssen die **Spaltenüberschriften gemäß den Felddefinitionen in Xentral ** stehen. Die Datei muss als CSV mit**Semikolon-separierten Werten** (;) vorliegen.
>
> - **Kundennummer fehlt**: Xentral legt automatisch eine neue Adresse und einen neuen Kundendatensatz an.
> - **Artikelnummer fehlt**: Xentral legt automatisch einen neuen Artikel an.
> - **Steuersatz in Prozent**: Entspricht dem Feld Individueller Steuersatz in Xentral.

> **Tipp**
>
> Der Import verändert keine bestehenden Stammdaten. Abweichungen zu gespeicherten Adress- oder Artikeldaten werden nur für den importierten Beleg übernommen.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| art | Beleg-Typ (z. B. Auftrag, Angebot, Bestellung, Rechnung, Adresse etc.) |
| **beleg_belegnr** | Manuell vergebene Belegnummer |
| beleg_datum | Manuell vergebenes Belegdatum |
| beleg_lieferdatum | Manuell vergebenes Wunschlieferdatum |
| beleg_tatsaechlicheslieferdatum | Manuelle Auslieferung Lager im Auftrag |
| beleg_versandart | Manuell vergebene Versandart |
| beleg_status | Manuell vergebener Belegstatus. Ersetzt den beim Dateiupload ausgewählten Status |
| beleg_hauptbelegnr | Haupt-Belegnummer, falls Teilauftrag |
| **beleg_kundennummer **/** adresse_kundennummer** | Kundennummer |
| **beleg_lieferantennummer** | Lieferantennummer |
| beleg_name / adresse_name | Name des Kunden |
| beleg_abteilung / adresse_abteilung | Abteilung des Kunden |
| beleg_unterabteilung / adresse_unterabteilung | Unterabteilung des Kunden |
| beleg_adresszusatz / adresse_adresszusatz | Adresszusatz des Kunden |
| beleg_ansprechpartner / adresse_ansprechpartner | Ansprechpartner beim Kunden |
| beleg_telefon / adresse_telefon | Telefonnummer des Kunden |
| beleg_email / adresse_email | E-Mail-Adresse des Kunden |
| beleg_land / adresse_land | Land des Kunden (ISO-3166, z. B. DE, AT, FR) |
| beleg_strasse / adresse_strasse | Straße inkl. Hausnummer des Kunden |
| beleg_plz / adresse_plz | Postleitzahl des Kunden |
| beleg_ort / adresse_ort | Ort des Kunden |
| beleg_projekt / adresse_projekt | Abkürzung aus Xentral |
| beleg_ihrebestellnummer | Bestellnummer / Kommission aus Xentral |
| beleg_aktion | Aktionscode aus Xentral |
| beleg_internebemerkung | Interne Bemerkung aus Xentral |
| beleg_internebezeichnung | Interne Bezeichnung aus Xentral |
| beleg_zahlungsweise | Zahlungsweise (Bitte die Spalte "Typ" verwenden) |
| beleg_zahlungszieltage | Beleg-Zahlungsziel |
| beleg_zahlungszieltageskonto | Beleg-Zahlungsziel Skonto |
| beleg_zahlungszielskonto | Beleg-Skonto |
| beleg_freitext | Freitext aus Xentral |
| beleg_bodyzusatz | Kopftext aus Xentral |
| beleg_lieferbedingung | Lieferbedingung aus Xentral |
| beleg_art | Belege im Auto-Versand erstellen (Standardauftrag, Lieferung, Rechnung) |
| beleg_auftragsnummer | Verknüpfung von Rechnungen und Lieferscheinen mit dem Auftrag |
| beleg_rechnungsnumer | Verknüpfung von Aufträgen, Lieferscheinen und Gutschriften mit der Rechnung |
| beleg_bearbeiter | Bearbeiter des Beleges |
| beleg_sprache | Sprache des Belegs |
| beleg_liefername | Abweichende Lieferadresse – Name |
| beleg_lieferabteilung | Abweichende Lieferadresse – Abteilung |
| beleg_lieferunterabteilung | Abweichende Lieferadresse – Unterabteilung |
| beleg_lieferland | Abweichende Lieferadresse – Land |
| beleg_lieferstrasse | Abweichende Lieferadresse – Straße |
| beleg_lieferort | Abweichende Lieferadresse – Ort |
| beleg_lieferplz | Abweichende Lieferadresse – Postleitzahl |
| beleg_lieferadresszusatz | Abweichende Lieferadresse – Adresszusatz |
| beleg_lieferansprechpartner | Abweichende Lieferadresse – Ansprechpartner |
| beleg_abschlagauftrag | Zur Abschlagsrechnung zugehörige Auftragsnummer |
| beleg_abschlagauftragbezeichnung | Bezeichnung der Abschlagsrechnung |
| beleg_waehrung | Währung (z. B. EUR, USD) |
| beleg_bundesstaat | Bundesland / Bundesstaat (ISO-codiert, z. B. BY für Bayern) |
| beleg_internet | Shopbestellnummer oder Fremdnummer |
| **artikel_nummer** | Artikelnummer für Position |
| artikel_bezeichnung | Bezeichnung für Position |
| artikel_beschreibung | Beschreibung für Position |
| **artikel_menge** | Mengenangabe für Position |
| artikel_preis | Einzelpreis (netto) für Position |
| artikel_preisfuermenge | Preis bezieht sich auf folgende Menge (leer = 1) |
| artikel_waehrung | Währung für Position |
| artikel_lieferdatum | Lieferdatum für Position |
| artikel_sort | Reihenfolge in Positionstabelle |
| artikel_umsatzsteuer | Umsatzsteuer (leer = normal, sonst "ermaessigt") |
| artikel_steuersatz | Steuersatz |
| artikel_einheit | Einheit für Position |
| artikel_rabatt | Rabatt für Position (in %) |
| artikel_zolltarifnummer | Zolltarifnummer für Position |
| artikel_herkunftsland | Herkunftsland für Position |
| artikel_artikelnummerkunde | Artikelnummer beim Kunden |
| artikel_freifeld1 – artikel_freifeld10 | Freifelder 1 bis 10 |
| adresse_typ | Anrede des Kunden (firma, herr, frau) |
| adresse_ustid | USt-IdNr. des Kunden |
| adresse_anschreiben | Anschreiben bei Kunde |
| adresse_freifeld1 – adresse_freifeld20 | Freifelder 1 bis 20 |

## Schlüsselworte für dynamische Belegnummern (Belegeimporter)

Der Belegeimporter kennt zwei besondere Steuerworte:

- **NEW **– Erstellt eine neue Belegnummer auf Basis der Belegart. Beispiel: Jede Zeile mit ** NEW** erzeugt einen neuen Beleg.
- **PARENT** – Nutzt die Belegnummer der vorherigen Zeile, um mehrere Positionen zu einem Beleg zu gruppieren.

## Beispielstruktur (Belegeimporter)

**Beispiel:**

```
beleg_belegnr;beleg_kundennummer;artikel_bezeichnung;artikel_nummer;artikel_preis;artikel_menge
203567;10456;Artikel A;A_100001;19.90;1
PARENT;10456;Artikel B;A_100002;29.90;2
NEW;10456;Artikel C;A_100003;15.50;1
```

- **203567** = erste Belegnummer (z.B. Rechnung oder Auftrag).
- **PARENT** = Artikel B wird dem vorherigen Beleg zugeordnet (gleiche Belegnummer wie Artikel A).
- **NEW** = erstellt einen neuen Beleg für Artikel C.
- **10456** = Kundennummer.
- **A_100001 **/** A_100002 **= Artikelnummern aus deinem Beispiel. ** Die erzeugte Belegstruktur basierend auf dem CSV-Beispiel:**

```
Beleg 203567
  - Artikel A (A_100001, 19.90 €, Menge 1)
  - Artikel B (A_100002, 29.90 €, Menge 2)

Beleg 30001 (neu erstellt durch NEW)
  - Artikel C (A_100003, 15.50 €, Menge 1)
```

So funktioniert’s:

- Der erste Artikel bestimmt den Startbeleg (**203567**).
- **PARENT** hängt den nächsten Artikel an denselben Beleg an.
- **NEW ** startet einen komplett neuen Beleg mit einer automatisch vergebenen Nummer (hier z. B. **30001**).

> **Anmerkung**
>
> **Hinweis**
>
> **Hinweis zu NEW **: Nach der ersten Zeile mit ** NEW **dürfen ** keine statischen Belegnummern**mehr folgen – sonst landen Positionen auf falschen Belegen.
>
> **Status 'angelegt'**: Wenn der Zielstatus '** angelegt **' ist, wird jede Belegnummer ≠ PARENT als NEW behandelt; die temporären ** ENTWURF_X_**

-Nummern dienen nur der Zuordnung und werden beim finalen Import verworfen.
>
> **PARENT in der ersten Zeile**: Wird wie NEW behandelt (es wird eine neue Belegnummer erzeugt).
>
> **CSV-Struktur**: Eine Position = eine Zeile; die erste Zeile enthält exakt die Feldnamen (aus dem Reiter Formate).
>
> **Voransicht & Freigabe**: Nach Upload Zuweisungen prüfen und erst dann auf „Belege jetzt importieren“ klicken..
>
> **Stammdaten bleiben unverändert**: Abweichungen zu Artikel-/Adress-Stammdaten werden rot angezeigt und gelten nur für den importierten Beleg.
>
> **Prozessstarter**: Der Import wird über einen Prozessstarter ausgeführt – dieser muss aktiv laufen, sonst werden die hochgeladenen Belege nicht verarbeitet.

## Best Practices für den Import (Belegeimporter)

- Vorher CSV in **Excel oder LibreOffice prüfen**, um Formatfehler zu vermeiden.
- Immer die offiziellen Feldnamen aus dem Reiter **Formate** verwenden.
- Bei vielen Belegen den Import zunächst mit einer **kleinen Testdatei** durchführen.
- **Prozessstarter** beim Import regelmäßig überwachen - checken, um sicherzustellen, dass der Import läuft.

### Achtung **Technischer Hinweis zu großen Datenmengen:**

Für sehr hohe Beleg- und Positionsvolumina empfiehlt sich die Verarbeitung über die[Xentral API](https://help.xentral.com/hc/de/articles/6618896113820#UUID-111b6679-d25f-f139-f468-9380f9e785b1), die[Shop-Importer](https://help.xentral.com/hc/de/articles/13235039238428-Xentral-Connect-%C3%9Cbersicht)oder das[Übertragungsmodul (3PL)](https://help.xentral.com/hc/de/articles/16164850902428#UUID-8975f07c-756b-3cdf-6500-9cd416962345). Der Belegeimporter ist nicht für High-Volume-Datenimporte optimiert.