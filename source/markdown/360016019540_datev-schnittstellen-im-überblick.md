Xentral bietet drei Exportmöglichkeiten für die Buchhaltung: Über den **Finanzbuchhaltung Export ** können Rechnungen, Gutschriften und Verbindlichkeiten als **CSV-Dateien ** mit vollständigen Kontierungen ausgegeben werden. Diese Daten basieren auf projektbezogenen oder globalen Steuereinstellungen und lassen sich flexibel anpassen. Zusätzlich gibt es die Möglichkeit, speziell für **DATEV Unternehmen Online ** formatierte Dateien zu exportieren, während eine dritte Option einen **vollständig digitalen Belegtransfer ** ohne lokale Speicherung ermöglicht, abgesichert über den**DATEV SmartLogin**.

Für die Anbindung an DATEV hast du diese Optionen:

- **Manueller Export **: Buchhaltungsdaten als CSV (** DATEV Format **) oder ** XML** exportieren und in DATEV hochladen.
- **Automatischer Export **: Über den ** DATEV Rechnungsdatenservice 1.0** werden die Daten direkt an DATEV übertragen, ohne zusätzlichen Aufwand.

Diese Optionen ermöglichen es dir, Zeit zu sparen und sicherzustellen, dass dein Steuerberater auf die aktuellen Daten zugreifen kann.

| Produkt | Beschreibung | Exportmethode | Datenformat |
| --- | --- | --- | --- |
| [DATEV Rechnungswesen Einzelplatz](#UUID-8983ff8b-79f9-5156-6c9e-8f282e6d4857_section-idm234547172619313) | Lokale Installation für eigenständige Buchhaltung. | Manueller Export von Buchungsstapeln. | **DATEV-Format** (CSV) |
| [DATEV Unternehmen online](#UUID-8983ff8b-79f9-5156-6c9e-8f282e6d4857_section-idm234547172983486) (manueller Export) | Cloudbasierter Dienst für die Zusammenarbeit mit Steuerberatern. | Manuelle Übertragung der Daten zu DATEV Unternehmen online. | **XML ** und **PDF** |
| [DATEV Unternehmen online](#UUID-8983ff8b-79f9-5156-6c9e-8f282e6d4857_section-idm234547172983486) (**Rechnungsdatenservice 1.0 **) | Automatisierte Schnittstelle für den direkten Belegtransfer. | Direkte Übertragung der Daten via Schnittstelle. |** XML** (automatisiert) |

> **Anmerkung**
>
> **Hinweis**
>
> Weitere Themen:
>
> - Auf dieser Seite:Schnellstart: Anbindung von DATEV - Xentral
> - Einstellungen für den DATEV Export(Konfigurationsmöglichkeiten)
> - Kontierung undKontenrahmen:Verbindlichkeiten, Artikeleinstellungen
> - Debitoren- und Kreditoren Stammdaten Export, eigene Debitoren-/Kreditoren Nummer, Sammeldebitoren.
> - Nummernkreise passend für DATEVfür Belege (Rechnung, Gutschrift, Verbindlichkeit), Nummernkreise für Kunden-/Lieferanten
> - Einrichtungsleitfaden:Buchhaltung und Reporting (Einrichtung)

> **Tipp**
>
> Die Xentral - DATEV informationen findest du parallel auch auf demDATEV Marktplatz.

## DATEV Rechnungswesen Einzelplatz

![DATEV_FORMAT_Workflow_kurzueberblick.png](https://help.xentral.com/hc/article_attachments/17296943893020)

DATEV Rechnungswesen Einzelplatz ist eine Softwarelösung für Unternehmen, die ihre Buchhaltung selbstständig im Haus abwickeln möchten. Sie ermöglicht deinem Buchhaltungsteam, alle Geschäftsvorfälle wie Rechnungen und Verbindlichkeiten zu erfassen, Bilanzen und Gewinn- und Verlustrechnungen zu erstellen sowie Zahlungen zu überwachen. Alle Daten werden lokal verwaltet und lassen sich bei Bedarf als DATEV-Format (CSV) exportieren, um sie an ein Steuerbüro zu übermitteln. Diese Lösung bietet dir volle Kontrolle über deine Buchhaltung, während du gleichzeitig flexibel mit deinem Steuerberater zusammenarbeiten kannst.

> **Anmerkung**
>
> **Hinweis**
>
> Wie du den manuellen Export im DATEV Format erstellen kannst findest du hier:Finanzbuchhaltung Export (DATEV Export Einstellungen)

## DATEV Unternehmen online

![DATEV_unternehmenonline_xml_Workflow_kurzueberblick.png](https://help.xentral.com/hc/article_attachments/17296943893660)

DATEV Unternehmen online ist eine cloudbasierte Lösung, die dir und deinem Buchhaltungsteam ermöglicht, alle Belege und Buchungen digital zu verwalten. Du kannst Belege direkt in der Cloud speichern und hast jederzeit Zugriff auf aktuelle Daten, was die Zusammenarbeit mit deinem Steuerberater vereinfacht. Dein Steuerberater kann auf die Buchhaltungsdaten in Echtzeit zugreifen und Aufgaben wie den Jahresabschluss direkt bearbeiten, ohne dass Daten manuell übertragen werden müssen. Dies macht den gesamten Buchhaltungsprozess effizienter und flexibler.

> **Anmerkung**
>
> **Hinweis**
>
> Wie du Unternehmen online an Xentral anbindest findest du hier:DATEV Unternehmen Online - XML Format

## Schnellstart: Anbindung von DATEV - Xentral

### (1) Initiale Stammdaten-Einrichtung für den DATEV-Export

Für die initiale Einrichtung des DATEV-Datenaustauschs musst du wichtige Stammdaten wie **Beraternummer **, ** Mandantennummer ** und das **Wirtschaftsjahr ** in das System eintragen. Diese Daten werden anschließend in die Exportdateien übernommen und ermöglichen eine korrekte Zuordnung der Buchhaltungsinformationen. Je nach Bedarf kannst du diese Einstellungen **global ** oder auch **projektspezifisch** vornehmen, um den Export an die Anforderungen deines Unternehmens anzupassen.

> **Anmerkung**
>
> **Hinweis**
>
> Wie du die Stammdaten (Mandanten-, Beraternummer und Wirtschaftsjahr) für Datev einträgst findest du hier:Einstellungen (Initiale Stammdaten-Einrichtung)

### (2) Automatisierter Export über die DATEV-Schnittstelle

In diesem Schritt wählst du den Export für eine automatische Übertragung über den DATEV Rechnungsdatenservice 1.0 aus. Diese Lösung ermöglicht es, Buchhaltungsdaten wie Rechnungen und Verbindlichkeiten ohne manuelles Eingreifen direkt an DATEV zu übermitteln. Hierfür muss die Schnittstelle einmalig konfiguriert werden, sodass zukünftige Exporte automatisch im Hintergrund erfolgen.

> **Anmerkung**
>
> **Hinweis**
>
> Wie du den automatischen Export zu DATEV Unternehmen Online nutzt findest du hier:DATEV Rechnungsdatenservice 1.0 (Unternehmen Online)

### (3) Manueller Export über die Benutzeroberfläche

Alternativ kannst du den Export manuell über eine grafische Benutzeroberfläche durchführen. Über einen Button in den Buchhaltungs-Einstellungen kannst du Einstellungen wie die Kontierung und den Exportzeitraum festlegen. Der Export erfolgt dann als CSV- oder XML-Datei, die anschließend manuell in das Buchhaltungssystem hochgeladen wird.

> **Anmerkung**
>
> **Hinweis**
>
> Wie du den CSV and XML Download nutzt findest du hier:Finanzbuchhaltung Export (DATEV Export Einstellungen)

## Einstellungen DATEV Export

Einstellungen für das[Datev Format](https://help.xentral.com/hc/de/articles/360016725100#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e),[DATEV Unternehmen Online - XML Format](https://help.xentral.com/hc/de/articles/16853858443292#UUID-ae91f160-799c-77e4-fb15-76cb4c8e70a2),[DATEV Rechnungsdatenservice 1.0 (Unternehmen Online)](https://help.xentral.com/hc/de/articles/16853851788572#UUID-a0703471-aeb2-3876-7f6a-6b407c12941d).