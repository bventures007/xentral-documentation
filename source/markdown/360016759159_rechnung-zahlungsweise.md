Mit der Zahlungsweise Rechnung kannst du festlegen, wie Kunden in Xentral per Rechnung bezahlen. In den Einstellungen bestimmst du Bezeichnungen, Zahlungsbedingungen, optionale Skontoangaben sowie die Platzierung eines Girocodes für direkte Zahlungen.

In diesem Artikel:

- [Zahlungsweise **Rechnung** anlegen oder bearbeiten](#zahlungsweise-rechnung-anlegen-oder-bearbeiten)
- [Zahlungsbedingungen festlegen (Rechnung Einstellungen)](#zahlungsbedingungen-festlegen-(rechnung-einstellungen))
- [Skontotext und Variablen](#skontotext-und-variablen)
- [QR-Code für Überweisungen (Girocode) einfügen](#qr-code-fuer-ueberweisungen-(girocode)-einfuegen)
- [Übersetzung der Zahlungsweise auf Belegen](#uebersetzung-der-zahlungsweise-auf-belegen)

## Zahlungsweise Rechnung anlegen oder bearbeiten **Schritte: **

1. Gehe zu **Einstellungen > Buchhaltung > Zahlungen & Geschäftskonten > Zahlungsweisen**.
1. Wähle **Zahlungsweise hinzufügen ** oder öffne eine bestehende Zahlungsweise vom Typ **Rechnung**.
1. Klicke auf **Speichern**.

### Achtung

Wenn du nur die Texte bearbeiten möchtest, lege keine neue Zahlungsweise an, sondern bearbeite die bereits bestehenden Standard-Zahlungsweisen in Xentral.

Wenn du dennoch eine neue Zahlungsweise für Rechnung anlegst, beachte, dass diese parallel zur standardmäßig bereits vorhandenen Zahlungsweise Rechnung (Modul: Rechnung) existiert. Verwende keine identische Typ-Bezeichnung, sondern vergib für die neue Zahlungsweise, die sich wie Rechnung verhält und das Modul Rechnung erhält, eine eindeutige Typ-Bezeichnung – z. B. rechnung_b2b.

## Zahlungsbedingungen festlegen (Rechnung Einstellungen)

Im unteren Bereich kannst du die Texte für die Zahlungsbedingungen definieren. Xentral unterscheidet zwischen **sofort ** (0 Tage Zahlungsziel) und ** Zahlungsziel > 1 Tag**.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Satz in Rechnung: (sofort) (DE) | Text, der auf Rechnungen ohne Zahlungsziel erscheint (sofort fällig). Gib hier den Hinweistext ein, z. B. „Rechnung zahlbar sofort.“ |
| Satz in Rechnung: (>= 1 Tag) (DE) | Text, der auf Rechnungen mit Zahlungsziel erscheint. Du kannst Variablen wie {ZAHLUNGSZIELTAGE} und {ZAHLUNGBISDATUM} verwenden, z. B. „Rechnung zahlbar innerhalb {ZAHLUNGSZIELTAGE} Tage bis zum {ZAHLUNGBISDATUM}“. |
| Satz in Angebot/Auftrag: (sofort) (DE) | Text, der in Angeboten oder Aufträgen ohne Zahlungsziel erscheint. Lege hier den Hinweistext fest, der bei sofortiger Fälligkeit angezeigt wird. |
| Satz in Angebot/Auftrag: (>= 1 Tag) (DE) | Text, der in Angeboten oder Aufträgen mit Zahlungsziel erscheint. Du kannst Variablen wie {ZAHLUNGSZIELTAGE} und {ZAHLUNGBISDATUM} nutzen. |
| Eigener Skontotext | Individueller Text für Skonto-Hinweise. Trage hier einen eigenen Skonto-Text ein, wenn du nicht den Standardtext verwenden möchtest. |
| Satz in Angebot/Auftrag (DE) | Allgemeiner Zahlungshinweistext für Angebote oder Aufträge. |
| Satz in Rechnung (DE) | Allgemeiner Zahlungshinweistext für Rechnungen. |

> **Tipp**
>
> Du kannst auch Variablen aus den Adressstammdaten verwenden.
>
> Diese müssen immer mit dem Präfix **ADRESSE_** beginnen, z. B. ** ADRESSE_NAME **für den Kundennamen oder ** ADRESSE_BANK **und** ADRESSE_IBAN** für die Bankdaten.

## Skontotext und Variablen

Im Textfeld für Skontoeinstellungen kannst du zentral einen Skonto-Hinweis für Angebot/Auftrag und einen für die Rechnung hinterlegen.

Du kannst bestimmen, welche Texte auf deinen Belegen erscheinen. Je nach Einstellung werden diese Texte automatisch auf Angeboten, Aufträgen, Rechnungen und Gutschriften eingefügt. Dafür kannst du Variablen verwenden, die beim Erstellen des Belegs automatisch mit den passenden Informationen und Beträgen ersetzt werden.

| Variable | Beschreibung |
| --- | --- |
| {ZAHLUNGBISDATUM} | Datum, bis zu dem die Zahlung fällig ist. |
| {ZAHLUNGSZIELTAGE} | Anzahl der Tage, die der Kunde zur Zahlung hat. |
| {SOLL} | Gesamtbetrag der Rechnung (brutto). |
| {BELEGNR} | Belegnummer der Rechnung oder des Dokuments. |
| {NAME} | Name des Kunden bzw. Rechnungsempfängers. |
| {STEUERNORMAL} | Steuerbetrag mit normalem Steuersatz. |
| {GESAMTNETTONORMAL} | Nettobetrag mit normalem Steuersatz. |
| {STEUERERMAESSIGT} | Steuerbetrag mit ermäßigtem Steuersatz. |
| {GESAMTNETTOERMAESSIGT} | Nettobetrag mit ermäßigtem Steuersatz. |
| {WAEHRUNG} | Währung der Rechnung (z. B. EUR, USD). |

**Skontotext:**

Im Textfeld für Skontoeinstellungen kannst du zentral einen Skonto-Hinweis für Angebot/Auftrag und einen für die Rechnung hinterlegen.

> **Anmerkung**
>
> Diese Texte werden nur verwendet, wenn im Beleg ein Skonto **größer als 0 %** hinterlegt ist.

Um Skontoinformationen dynamisch im Text anzuzeigen, kannst du folgende Variablen in den Skonto-Text einfügen:

| Variable | Beschreibung |
| --- | --- |
| {ZAHLUNGSZIELSKONTO} | Prozentwert, wie viel Skonto gewährt wird. Dynamisch berechnet auf den Gesamtbetrag, wobei skontogesperrte Artikel gegengerechnet werden. |
| {ZAHLUNGSZIELSKONTOTOTAL} | Prozentwert, wie viel Skonto gewährt wird. Fester Wert im Beleg, ohne Berücksichtigung skontogesperrter Artikel. |
| {ZAHLUNGSZIELTAGESKONTO} | Anzahl der Tage, für die Skonto gewährt wird. |
| {ZAHLUNGSZIELSKONTODATUM} | Datum, bis zu dem Skonto gewährt wird. |
| {SOLLMITSKONTO} | Gesamtbetrag abzüglich Skonto. Skontogesperrte Artikel werden berücksichtigt. |
| {SKONTOBETRAG} | Betrag, um den sich die Zahlung durch Skonto reduziert. |
| {SKONTOFAEHIG} | Gesamtbetrag (Brutto) der Positionen, die für Skonto in Frage kommen, ohne skontogesperrte Artikel. |
| {SKONTOFAEHIGNETTO} | Gesamtbetrag (Netto) der Positionen, die für Skonto in Frage kommen, ohne skontogesperrte Artikel. |

> **Anmerkung**
>
> **Hinweis**
>
> **Skonto-Hinweise – Beispiele zur Verwendung**:
>
> Die folgenden Textbausteine sind exemplarische Formulierungen für Skonto-Hinweise in Angeboten, Aufträgen und Rechnungen. **Bitte stimme die konkrete Formulierung, Betragsdarstellung und steuerliche Behandlung immer mit deinem Steuerberater ab, bevor du sie in deinem Unternehmen einsetzt.**
>
> **Beispiel 1 – Klassisch & kurz:**
>
> Bei Zahlung innerhalb {ZAHLUNGSZIELTAGESKONTO} Tagen gewähren wir {ZAHLUNGSZIELSKONTO}% Skonto.
>
> Rechnungsbetrag mit Skonto: {SOLLMITSKONTO} EUR.
>
> Nach dem {ZAHLUNGSZIELSKONTODATUM} ist der volle Rechnungsbetrag fällig.
>
> **Beispiel 2 – Rechnungsbetrag & Skontobetrag sichtbar:**
>
> Zahlen Sie innerhalb von {ZAHLUNGSZIELTAGESKONTO} Tagen und sparen Sie {SKONTOBETRAG} EUR ({ZAHLUNGSZIELSKONTO}% Skonto).
>
> Rechnungsbetrag mit Skonto: {SOLLMITSKONTO} EUR.
>
> **Beispiel 3 – Für Angebote/Aufträge:**
>
> Bei Auftragserteilung mit Zahlungseingang innerhalb von {ZAHLUNGSZIELTAGESKONTO} Tagen erhalten Sie {ZAHLUNGSZIELSKONTO}% Skonto.
>
> Das entspricht einem Abzug von {SKONTOBETRAG} EUR auf skontofähige Positionen.
>
> **Beispiel 4 – Detaillierte B2B-Variante:**
>
> Skontofähiger Nettobetrag: {SKONTOFAEHIGNETTO} EUR
>
> Bei Zahlung bis {ZAHLUNGSZIELSKONTODATUM} gewähren wir {ZAHLUNGSZIELSKONTO}% Skonto (= {SKONTOBETRAG} EUR).
>
> Gesamtbetrag mit Skonto: {SOLLMITSKONTO} EUR.

## QR-Code für Überweisungen (Girocode) einfügen

Der GiroCode ist ein in Deutschland standardisierter QR-Code für SEPA-Überweisungen. Er enthält alle wichtigen Zahlungsdaten wie IBAN, BIC, Empfänger, Betrag und Verwendungszweck. Mit einer Banking-App in Deutschland oder anderen SEPA-Ländern kann man den Code einfach scannen – die Überweisungsmaske wird automatisch ausgefüllt. Das spart Zeit, reduziert Tippfehler und erhöht die Sicherheit. Typische Einsatzorte sind Rechnungen, Spendenaufrufe oder Online-Zahlungsbestätigungen.

**Schritte Girocode einfügen: **

1. Öffne in Xentral die **Einstellungen** der gewünschten Zahlungsweise (z. B. Rechnung).
1. Setze den Haken bei **QR aktivieren**.
1. Gib deine Bankverbindung in den Feldern **QR IBAN ** und **QR BIC** ein.
1. Passe bei Bedarf die Position des QR-Codes an:
1. Speichere die Einstellungen.
1. Erstelle eine Testrechnung, um den QR-Code zu prüfen.

![zahlungsweise_rechnung_qr-code_girocode_002.png](https://help.xentral.com/hc/article_attachments/21642323513756)

> **Anmerkung**
>
> **Hinweis**
>
> Beispiel für hinterlegte Kontodaten im QR-Code (Girocode):
>
> - Empfänger: **Musterfirma GmbH **> - IBAN: ** DE89 3704 0044 0532 0130 00 **> - BIC: ** COBADEFFXXX **> - Betrag: ** 123,45 EUR **> - Verwendungszweck: ** RE 402286**

**Felder Girocode:**

| Feldbezeichnung | Beschreibung |
| --- | --- |
| QR aktivieren | Aktiviere diese Option, um einen Girocode (QR-Code) für die Zahlung auf Rechnungen zu drucken. |
| QR IBAN | IBAN des Bankkontos, auf das der Kunde per Girocode überweisen soll. |
| QR BIC | BIC des Bankkontos, auf das der Kunde per Girocode überweisen soll. |
| Platzierung von links | Abstand des QR-Codes vom linken Rand in Millimetern. Wenn kein Wert eingetragen wird, verwendet Xentral den Standardwert von **160 mm**. |
| Platzierung von oben | Abstand des QR-Codes vom oberen Rand in Millimetern. Wenn kein Wert eingetragen wird, verwendet Xentral den Standardwert von **30 mm**. |

> **Anmerkung**
>
> In der Schweiz gibt es dafür ein eigenes System, den Swiss QR Code, der nicht mit dem deutschen GiroCode verwechselt werden sollte. Die Informationen wie du den Swiss QR Code einrichtest findest du im ArtikelQR Rechnung Schweiz - Swiss QR Code.

## Übersetzung der Zahlungsweise auf Belegen **Den Text auf Beleg für andere Belegsprachen übersetzen:**

Klicke auf die graue Weltkugel rechts neben dem Textfeld und füge einen neuen Eintrag mit der gewünschten Übersetzung hinzu.