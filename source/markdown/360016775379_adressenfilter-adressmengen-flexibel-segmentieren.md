Der Adressenfilter ist kein tägliches Such-Tool, sondern ein Modul zur Segmentierung: Du bildest daraus Mengen und Teilmengen deiner Stammdaten – z. B. für Serienbriefe, Newsletterlisten, Kampagnen oder Datenexporte.

Menüpfad: **Verkauf > Adressen > Adressenfilter**

## So arbeitest du mit dem Modul Adressenfilter (Kurzüberblick)

1. **Filter hinzufügen** und Bedingungen definieren (z. B. Projekt, Gruppe, Adressfeld, Artikel im Beleg).
1. Bedingungen mit **UND/ODER** kombinieren, optional mit „ist nicht“ ausschließen.
1. **Als Vorlage speichern**, um die Selektion jederzeit wiederzuverwenden.
1. Unter **Aktion ** gewünschte **Export- oder Druckfunktion** starten.

## Funktionen (Modul Adressenfilter)

### Filter hinzufügen (Modul Adressenfilter)

Wähle **Filter hinzufügen** und entscheide dich für eine der folgenden Bedingungsarten:

| Filterfeld | Beschreibung |
| --- | --- |
| Gruppe | Filtert Adressen nach zuvor definierten **Adressgruppen** (z. B. Kunden, Lieferanten, VIP). Nutze Gruppen, um Zielgruppen organisatorisch zusammenzufassen. |
| Gruppe für Ansprechpartner | Selektiert **Ansprechpartner** anhand ihrer Gruppenzuordnung (z. B. Vertriebsleiter, Technik). Praktisch für Telefon- oder E-Mail-Listen bestimmter Rollen. |
| Projekt | Zeigt Adressen, die einem bestimmten **Projekt** zugeordnet sind (z. B. Messe 2024, Onboarding). Ideal für Kampagnen rund um Events oder Initiativen. |
| Adressfeld | Filtert konkrete **Stammdatenfelder** wie PLZ, Ort, Kundennummer oder Marketingsperre. Mit Operatoren fein steuerbar. |
| Artikel im Beleg | Sucht Adressen anhand von **Artikeln ** in **Belegen**: Angebot, Auftrag, Rechnung, Lieferschein oder Gutschrift. Perfekt für Nachfass- oder Cross-Selling-Kampagnen. |

### Operatoren (Modul Adressenfilter)

Neben dem Operator steht immer die Checkbox „ist nicht“ bereit – damit kehrst du jede Bedingung um (Ausschluss).

| Operator | Beschreibung & Beispiel |
| --- | --- |
| ist | Exakte Übereinstimmung. Beispiel: Projekt ist „STANDARD“ → nur Adressen im Projekt STANDARD. |
| enthält | Wert muss irgendwo im Feld vorkommen. Beispiel: Ort enthält „München“ → findet auch „München-Süd“. |
| beginnt mit | Wert muss am Anfang stehen. Beispiel: PLZ beginnt mit „80“ → alle Adressen mit 80xxx. |
| endet mit | Wert muss am Ende stehen. Beispiel: E-Mail endet mit „.de“ → alle Adressen mit deutscher Domain. |
| ist nicht (Checkbox) | Kehrt jede Bedingung um, schließt Treffer aus. Beispiel: Projekt ist nicht „POS“ → alle außer Projekt POS. |

**Kombinationslogik: **

-** UND** → alle Bedingungen müssen stimmen (präzise Teilmenge).
- **ODER **→ mindestens eine Bedingung reicht (breitere Menge). ** Beispiel**: Projekt STANDARD UND Projekt POS ist nicht → nur Adressen in STANDARD, aber nicht in POS.

### Vorlagen speichern & wiederverwenden (Modul Adressenfilter)

**Schritte: **

1. Bedingungen setzen →** Aktion **→** Als neue Vorlage speichern**.
1. **Bezeichnung** vergeben (z. B. „STANDARD ohne POS“) → OK.
1. Später im Bereich Vorlage **auswählen** und laden.
1. Vorlage **überschreiben** aktualisiert die bestehende Selektion.
1. Vorlage **löschen** entfernt sie dauerhaft.

Tipp: Lege dir für wiederkehrende Selektionen (Newsletter, Regionen, Projekte) eigene Vorlagen an.

### Aktionen & Exporte (Modul Adressenfilter)

Nachdem die Trefferliste steht, wählst du unter Aktion den nächsten Schritt.

**Die wichtigsten Aktionen:**

1. Serienbrief drucken – Serienbriefe für alle Treffer erzeugen.
1. Export E-Mails (Newsletter) – CSV für Newsletter-Tools.
1. Export Adressen (CSV) – vollständige Adressdatensätze als CSV.

Wichtig: Xentral verschickt keine Massenmails. Nutze die CSV z. B. für ein externes Mailing-Tool.

> **Anmerkung**
>
> **Hinweis**
>
> **Exportvarianten (Aktion)**:
>
> Im Bereich Aktion stehen dir folgende Exportmöglichkeiten zur Verfügung – jeweils auch in UTF-8-Variante:
>
> - Export E-Mails für Newsletter
> - Export E-Mails für Newsletter (UTF-8)
> - Export E-Mails inkl. aller Ansprechpartner für Newsletter
> - Export E-Mails inkl. aller Ansprechpartner für Newsletter (UTF-8)
> - Export Adressen als CSV
> - Export Adressen als CSV (UTF-8)
> - Export Adressen inkl. aller Ansprechpartner als CSV
> - Export Adressen inkl. aller Ansprechpartner als CSV (UTF-8)
>
> Tipp: Verwende UTF-8 für Exporte in externe Tools. Die Standard-CSV (Excel/ISO-8859-1) eignet sich vor allem für den direkten Import in Excel.

#### Felder im Export (Modul Adressenfilter)

Beim Export „Adressen als CSV“ werden folgende **Spalten** ausgegeben:

> **Anmerkung**
>
> **Hinweis**
>
> Kundennummer, Lieferantennummer, Firma/Name, Ansprechpartner, Abteilung, Unterabteilung, E-Mail, Telefonnummer, Fax, Mobil, Straße, PLZ, Ort, Land, Projekt, Typ, Anschreiben **Beispielauszug (CSV):**

```
Kundennummer,Lieferantennummer,Firma/Name,Ansprechpartner,Abteilung,Unterabteilung,E-Mail,Telefonnummer,Fax,Mobil,Straße,PLZ,Ort,Land,Projekt,Typ,Anschreiben
10001,,Muster GmbH,Max Mustermann,Vertrieb,,max@muster.de,089123456,,0176123456,Teststraße 1,80331,München,DE,STANDARD,Kunde,Sehr geehrter Herr Mustermann,
10001,,Muster GmbH,Anna Beispiel,Vertrieb,,anna@muster.de,089123456,,0176987654,Teststraße 1,80331,München,DE,STANDARD,Kunde,Sehr geehrte Frau Beispiel,
10002,20002,Beispiel AG,Peter Müller,Technik,Support,peter@beispiel.at,07201234,,0664556677,Hauptstraße 5,4020,Linz,AT,POS,Lieferant,Sehr geehrter Herr Müller,

```