Die GLN (Global Location Number) ist eine weltweit eindeutige Identifikationsnummer, die Unternehmen, Standorte oder Organisationseinheiten kennzeichnet. Sie wird von GS1 vergeben und dient als Basis für den automatisierten Datenaustausch zwischen Geschäftspartnern. Typische Einsatzgebiete sind:

- **Identifikation von Unternehmen**: Eindeutige Kennung für Rechnungsstellung, Lieferungen oder rechtliche Dokumente.
- **Standortkennzeichnung**: Zentrale, Filialen, Lager, Produktionsstätten oder Lieferadressen lassen sich präzise identifizieren.
- **EDI-Prozesse (Electronic Data Interchange)**: Vor allem im B2B-Bereich ist die GLN ein Standard für den automatisierten Austausch von Bestellungen, Lieferscheinen oder Rechnungen.

> **Tipp**
>
> Eine GLN ist 13-stellig und nach internationalem Standard strukturiert.

## Grundprinzip Verwendung GLN

Die **GLN (Global Location Number)** dient der eindeutigen Identifikation von Adressen (Unternehmen, Niederlassungen, Lager). Du solltest sie dann abdrucken, wenn dein Geschäftspartner sie ** fordert **oder wenn sie für die ** automatisierte Verarbeitung** notwendig ist.

### Typische Einsatzszenarien der GLN im B2B **Bestellungen**:

- Deine eigene GLN → zeigt dem Lieferanten, wer bestellt.
- Lieferadresse-GLN → wenn die Ware in ein Lager oder eine Filiale geht.

**Rechnungen / Gutschriften**:

- GLN der Rechnungsadresse (oft bei zentralen Buchhaltungen, Shared Service Centern)
- Teilweise Pflicht, wenn dein Partner EDI nutzt oder das Unternehmen GLNs als Standard eingeführt hat **Lieferscheine**:

- GLN der Lieferadresse, damit die Warenannahme die Lieferung korrekt zuordnen kann **Rahmenverträge & EDI**:

- Viele große Handelsunternehmen (z. B. im Lebensmittel- und Einzelhandel) bestehen auf GLNs, weil deren Systeme sonst keine automatische Verarbeitung erlauben.

## GLN in Xentral – Verwendung und Variablen

Xentral unterstützt die Verwaltung und den Druck von GLN auf Belegen wie Rechnungen, Aufträgen, Bestellungen, Lieferscheinen und Gutschriften. Dadurch können Geschäftspartner die Belege eindeutig zuordnen.

### Übersicht der GLN-relevanten Variablen in Xentral: GLN in Adress- und Belegdaten

In den **Adressdaten ** von Kunden und Lieferanten kann eine GLN gepflegt werden. Diese wird anschließend automatisch in Belegen genutzt. **Wichtige Variablen sind:**

-**{GLN}** – GLN aus den allgemeinen Adressdaten: GLN des Belegs (allgemeine Stammdaten)
- **{ADRESSE_GLN}** – GLN aus den Adress-Stammdaten
- **{LIEFERGLN}** – GLN aus der Lieferadresse
- **{ADRESSE_RECHNUNG_GLN}** – GLN aus der abweichenden Rechnungsadresse

> **Anmerkung**
>
> Wird eine GLN in den Stammdaten eingetragen, kann sie in Belegen automatisch verwendet werden.
>
> **Wo trage ich was ein?**
>
> - Adresse → Stammdaten: ADRESSE_GLN (Kunde/Lieferant allgemein)
> - Adresse → Lieferadresse: LIEFERGLN
> - Adresse → Abw. Rechnungsadresse: ADRESSE_RECHNUNG_GLN
> - Beleg (optional): GLN (falls projektspezifisch/abweichend je Beleg)

Praktische Umsetzung in Xentral

| Belegart | Empfohlene GLN-Variablen |
| --- | --- |
| Bestellung | {GLN} (eigene GLN), {LIEFERGLN} (Lieferadresse) |
| Rechnung | {ADRESSE_GLN} (Kunde/Rechnungsempfänger), {ADRESSE_RECHNUNG_GLN} (abweichende Rechnungsadresse), {LIEFERGLN} (optional Lieferadresse) |
| Lieferschein | {LIEFERGLN} (Lieferadresse) |
| Auftrag/Angebot | Meist nicht nötig, außer Partner fordert sie explizit |
| Gutschrift | Wie bei Rechnung – oft {ADRESSE_GLN} |

### GLN-Variablen im Beleg

Die GLN kann in verschiedenen Kontexten eingebunden werden. Beispiele:

**Rechnung **>** Anmerkung**
>
> **Hinweis**
>
> {IF}{ADRESSE_GLN}{THEN}GLN: {ADRESSE_GLN}{ELSE}{ENDIF}
>
> {IF}{LIEFERGLN}{THEN}Liefer-GLN: {LIEFERGLN}{ELSE}{ENDIF}

**Bestellung **>** Anmerkung**
>
> **Hinweis**
>
> Unsere GLN: {GLN}
>
> Ihre Lieferadresse (GLN): {LIEFERGLN}

**Lieferschein **>** Anmerkung**
>
> **Hinweis**
>
> {IF}{LIEFERGLN}{THEN}GLN der Lieferadresse: {LIEFERGLN}{ELSE}{ENDIF}

## Textvorlagen mit GLN

Die GLN kann wie jede andere Variable in den Textvorlagen von Xentral eingebunden werden. So kannst du sie automatisiert auf Dokumenten anzeigen lassen.

Beispiel: **Rechnungstext mit GLN **>** Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> vielen Dank für Ihren Auftrag.
>
> {IF}{TRANSAKTIONSNUMMER}{THEN}Transaktionsnummer: {TRANSAKTIONSNUMMER}{ELSE}{ENDIF}
>
> {IF}{LIEFERSCHEIN}{THEN}Lieferschein: {LIEFERSCHEIN}{ELSE}{ENDIF}
>
> {IF}{ADRESSE_GLN}{THEN}GLN (Rechnungsempfänger): {ADRESSE_GLN}{ELSE}{ENDIF}
>
> {IF}{LIEFERGLN}{THEN}GLN (Lieferadresse): {LIEFERGLN}{ELSE}{ENDIF}

Beispiel: **Bestellung mit GLN **>** Anmerkung**
>
> **Hinweis**
>
> Sehr geehrte Damen und Herren,
>
> wir bestellen hiermit:
>
> Unsere GLN: {GLN}
>
> Unsere Lieferadresse (GLN): {LIEFERGLN}
>
> Bitte liefern Sie bis zum: {GEWUENSCHTESLIEFERDATUM}

## Praxis-Tipps GLN

> **Tipp**
>
> - Pflege der Stammdaten: Stelle sicher, dass alle relevanten GLNs in den Kunden- und Lieferantendaten hinterlegt sind, damit diese automatisch in Belegen erscheinen.
> - IF-Bedingungen nutzen: Mit {IF}{GLN}{THEN}...{ELSE}{ENDIF} kannst du verhindern, dass leere GLN-Felder sichtbar werden.
> - GLN pro Adresse: Jede Rechnungs- oder Lieferadresse kann eine eigene GLN haben. So werden auch komplexe Lieferketten korrekt abgebildet.
> - B2B-Szenarien: Besonders im Handel mit großen Unternehmen und im internationalen Kontext ist die GLN Pflichtbestandteil für Rechnungen, Lieferscheine oder Bestellungen.

## FAQ - GLN

### Wie stelle ich sicher, dass meine GLN auf allen Belegen gedruckt wird?

**Antwort**: Lege die Variablen {GLN}, {LIEFERGLN} und {ADRESSE_RECHNUNG_GLN} in den jeweiligen Textvorlagen an. Nutze IF-Bedingungen, um leere Werte auszublenden.

### Kann ich mehrere GLNs für unterschiedliche Standorte pflegen?

**Antwort**: Ja, jede Adresse (Rechnung, Lieferung, abweichend) hat ihr eigenes GLN-Feld. So können unterschiedliche Standorte eindeutig abgebildet werden.

### Wann muss ich eine GLN nicht abdrucken?

**Antwort**: Im B2C-Bereich ist die GLN irrelevant. Privatkunden haben keine GLN, daher wird das Feld leer bleiben. Wenn dein Geschäftspartner keine GLN nutzt oder fordert, reicht meist die normale Adressangabe. Für interne Zwecke (z. B. Belegkopien) ist ein Abdruck nicht zwingend nötig.