In den **Textvorlagen** kannst du Textbausteine und Inhalte für Belege festlegen Je Belegart kannst du die Textbausteine oder Inhalte auf Dokumenten abdrucken lassen. Beim Erstellen eines neuen Belegs werden diese Informationen automatisch abgedruckt.

Du kannst z.B. explizit ausführlicher auf deine AGB hinweisen, eine Kundeninformation auf einen Lieferschein abdrucken, Bausteine wie Rechnungsadresse, abweichende Rechnungsadresse oder Lieferadresse auf bestimmten Belegen anzeigen lassen. Auch Umsatzsteuer-ID des Kunden, das Lieferdatum, die Kalenderwoche oder Transaktionsnummern aus Online Shops kannst du andrucken lassen.

> **Tipp**
>
> In der Standardlauslieferung von Xentral steht dir automatisch ein Set an Mustervorlagen zur Verfügung, so dass du sofort ohne viel Einstellung loslegen kannst.
>
> Die wichtigsten Tips und fertige Textbausteine findest du in deiner Xentral Version und in diesem Artikel.

> **Anmerkung**
>
> Die Textbausteine und Variablen werden **vor ** und **nach ** der Artikeltabelle auf dem Beleg angezeigt. **Für individuelle einfache Anpassungen deiner Belege stehen dir folgende Möglichkeiten zur Verfügung:**

- Anpassung der Texte je Beleg ** über der Artikeltabelle **und ** nach der Artikeltabelle ** (am Ende des Belegs, nach dem Freitext) und Einfügen von ** Variablen** z.B. Liefertermin, Vertriebskanal (= Projekt), Wunschliefertermin, Kalenderwoche, Kostenstelle u.v.m.
- Möglichkeit der Text Anpassung für die gängigen Belege **Angebot **, ** Auftrag **, ** Rechnung **, ** Lieferschein **, ** Gutschrift **, ** Bestellung**, Proformarechnung u.a..
- Textbaustein für **EU Lieferung ** (B2B Innergemeinschaftlicher Erwerb) und Textbaustein für ** Export Drittland **. ** Für erweiterte Anpassungen mit Variablen, Bedingungen und Übersetzung stehen dir folgende Möglichkeiten zur Verfügung:**

- Textbausteine mit ** Bedingungen** hinterlegen z.B. pro Vertriebskanal, zusätzliche Ausgabe von 7% und 19% Steuer, Text nur anzeigen, falls eine Bedingung zutrifft.
- **Formatierung** der Texte.
- **Übersetzung** der Bausteine in andere Sprachen.
- Möglichkeit Briefpapier und Logo auszublenden (für den Druck auf Firmeninternes Briefpapier).
- Erweiterte Sortiermöglichkeit: Reihenfolge der Textblöcke.
- Zahlreiche **Variablen** aus Adressdaten und Belegdaten.

> **Anmerkung**
>
> **Beispiel:** Du möchtest z.B. die Kalenderwoche nicht anzeigen lassen, dann entferne die Variable {LIEFERWOCHE}.
>
> **Info **: Im Beispiel sind zusätzlich zur Variable auch Bedingungen verwendet worden. Mit Bedingungen kannst du Beschriftungen ausblenden, wenn keine Information abgedruckt wird. Du findest Vorlagen und Beispiele im Bereich ** Bedingungen**in diesem Artikel.

![2885091357.png](https://help.xentral.com/hc/article_attachments/14212165063580)

![2885091363.png](https://help.xentral.com/hc/article_attachments/14212149546268)

## Einfügen von Textbausteinen, Variablen und Bedingungen

Um deine wichtigen Informationen für deine Kunden auf Belegen abzudrucken, kannst du feste Texte einfügen, Platzhalter (= Variablen) automatisch füllen lassen oder Bedingungen einfügen, wann bestimmte Texte angezeigt werden sollen.

Menü: Gehe im Hauptmenü auf **Einstellungen **>** Dein System einrichten **> Untermenüpunkt ** Textvorlagen.**

### Textbausteine - feste Texte einfügen

Du kannst Texte wie z.B. weiterführende Informationen zu deinen AGB, eine persönliche Anrede sowie Vertragsinformationen, die beim Kauf immer gelten auf Belege fest einfügen z.B. dein Angebot.

**Schritte: **

1. Klicke in den **Textvorlagen ** auf die entsprechende Textbox z.B. ** Auftrag Text vor Artikeltabelle**

1. Füge einen Text ein z.B.
1. Klicke auf **Speichern**.
1. Ergebnis: Der Text wird auf jedem neuen Auftrag vor der Artikeltabelle abgedruckt.

![2885091369.png](https://help.xentral.com/hc/article_attachments/14212165206428)

![2885091375.png](https://help.xentral.com/hc/article_attachments/14212117973148)

### Variablen - Platzhalter automatisch füllen lassen

Du kannst mit Variablen automatisch Daten aus dem jeweiligen Beleg oder der Adresse abdrucken lassen. Z.B. das Lieferdatum, die Kalenderwoche, Shop-Bestellnummer, Transaktionsnummer, erweiterte Lieferadresse.

- Lieferdaten und -bedingungen und Versandinformationen.
- Rechnungsdaten und Zahlungsinformationen.
- Adressinformationen und Kunden-/ Lieferantendaten.
- Produktinformationen.

**Schritte: **

1. Klicke in den **Textvorlagen ** auf die entsprechende Textbox z.B. ** Auftrag Text vor Artikeltabelle**

1. Füge eine Variable ein z.B.
1. Klicke auf **Speichern**.
1. Ergebnis: Für einen neuen Auftrag wird die Variable {ANREDE} aus den Kundenstammdaten gefüllt. Hier kannst du den Text individuell pro Kunde personalisiert eingeben.

### Bedingungen - für die Anzeige eines bestimmten Textes

Mit Bedingungen kannst du Texte anzeigen lassen, wenn bestimmte Voraussetzungen erfüllt wurde. Wenn du beispielsweise auf einem Angebot eine Liste an Variablen hast, kannst du nur diese anzeigen lassen, die für den Kunden oder das Projekt oder den Kanal (z.B. B2B) zutreffen. Andere Kunden erhalten diese Beschriftungen nicht, da du die Felder für sie auch nicht ausgefüllt hast. Du kannst z.B.:

- **Beschriftungen ausblenden**: Wenn ein Wert vorhanden ist, dann auch die Beschriftung mit auf dem Beleg anzeigen. Wenn kein Wert vorhanden ist, die Beschriftung nicht anzeigen.
- **Texte für ein Projekt einblenden**: Wenn das Projekt ONLINESHOP im Beleg ausgewählt ist den Text für die Onlineshop-Kundeninformation anzeigen. Bei anderen Projekten keinen Text anzeigen.
- **Texte für ein Land abdrucken**: z.B. Abweichende Information für Schweiz (CH).

#### Verwendung von Bedingungen **Schritte: **

1. Klicke in den **Textvorlagen ** auf die entsprechende Textbox z.B. ** Auftrag Text vor Artikeltabelle**

1. Füge eine Bedingung ein z.B.
1. Klicke auf **Speichern**.
1. Ergebnis: Für einen neuen Auftrag wird der Wunschliefertermin und die Lieferwoche angezeigt, wenn du das Feld dafür im Auftrag gefüllt hast. Hat der Auftrag kein Datum und keine Kalenderwoche, wird auf dem Auftrag nichts ausgegeben.

> **Tipp**
>
> Wenn du die Bedingungsvariablen **{IF}**{LIEFERWOCHE}**{THEN}** Lieferwoche:{LIEFERWOCHE}**{ELSE}{ENDIF}** entfernst, wird die Beschriftung “Lieferwoche:” immer angezeigt, auch wenn der Wert auf dem Beleg nicht gefüllt ist. Verwende also keine Bedingungen, wenn du die Beschriftung in jedem Fall auf deinem Beleg für dich sehen willst.
>
> Beispiel:
>
> - **{IF}{USTID}{THEN}Ihre UmsatzsteuerID: {USTID} {ELSE}{ENDIF}**. Dieser Ausdruck liefert auf dem Beleg "Ihre UmsatzsteuerID: XXXXXXXX", wenn die Nummer XXXXXXXX angegeben wurde. Wenn keine Umsatzsteuernummer im Beleg vorhanden ist, wird nichts ausgegeben, auch nicht die Beschriftung "Ihre UmsatzsteuerID:" Die Beschriftung ist also nicht sichtbar und erzeugt keine Kundennachfragen vor allem im B2C Business.
> - **Ihre UmsatzsteuerID: {USTID}**. Dieser Ausdruck liefert auf dem Beleg "Ihre UmsatzsteuerID: XXXXXXXX", wenn die Nummer XXXXXXXX angegeben wurde. Wenn keine Umsatzsteuernummer im Beleg vorhanden ist, wird die Beschriftung "Ihre UmsatzsteuerID:" ausgegeben. Die Beschriftung ist also weiterhin sichtbar und erleichtert die Kontrolle der internen Belege vor allem im B2B Business.

### Standard Variablen und Beispiele

Anbei finden Sie einige Beispiele für die Verwendung von Variablen. Die Variablen beziehen sich meist auf das jeweilige Dokument, für das Sie den individuellen Text einpflegen. Soll sich eine Variable auf die Kundenadresse beziehen, so können Sie der Variable aus dem Dokument das Präfix „ADRESSE_“ voranstellen. Dann erhalten Sie dieselbe Variable aber mit Bezug auf die Kunden-/Lieferanten-Adresse. Anbei ein Beispiel: {NAME} bezieht sich auf das Namensfeld im Dokument, {ADRESSE_NAME} bezieht sich auf das Namensfeld in der Adresse.

#### Angebot - Beispiel Textbausteine

Angebot Text vor Artikeltabelle

> **Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> hiermit bieten wir Ihnen an:

Angebot Text am Ende (nach Freitext)

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{GUELTIGBIS}{THEN}Das Angebot ist gültig bis zum: {GUELTIGBIS}{ELSE}{ENDIF}
>
> {IF}{LIEFERADRESSELANG}{THEN}Ihre Lieferadresse: {LIEFERADRESSELANG}{ELSE}{ENDIF}
>
> Dieses Formular wurde maschinell erstellt und ist ohne Unterschrift gültig.

#### Auftrag - Beispiel Textbausteine

Auftrag Text vor Artikeltabelle

> **Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> vielen Dank für Ihren Auftrag.
>
> {IF}{LIEFERTERMIN}{THEN}Ihr Wunschliefertermin: {LIEFERTERMIN}{ELSE}{ENDIF} / {IF}{LIEFERWOCHE}{THEN}Lieferwoche: {LIEFERWOCHE}{ELSE}{ENDIF}

Auftrag Text am Ende (nach Freitext)

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{LIEFERADRESSE}{THEN}Lieferadresse: {LIEFERADRESSE}{ELSE}{ENDIF}
>
> {IF}{ABWEICHENDE_RECHNUNGSADRESSE}{THEN}Abweichende Rechnungsadresse: {ABWEICHENDE_RECHNUNGSADRESSE}{ELSE}{ENDIF}
>
> Dieses Formular wurde maschinell erstellt und ist ohne Unterschrift gültig.

#### Rechnung - Beispiel Textbausteine

Rechnung Text vor Artikeltabelle

> **Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> anbei Ihre Rechnung.
>
> {IF}{INTERNET}{THEN}Bestellnummer:{INTERNET} {ELSE}{ENDIF} {IF}{TRANSAKTIONSNUMMER}{THEN}Transaktionsnummer:{TRANSAKTIONSNUMMER}{ELSE}{ENDIF} {IF}{USTID}{THEN}Ihre USt-ID:{USTID}{ELSE}{ENDIF}

Rechnung Text am Ende (nach Freitext)

> **Anmerkung**
>
> **Hinweis**
>
> Dieses Formular wurde maschinell erstellt und ist ohne Unterschrift gültig.

#### Lieferschein - Beispiel Textbausteine

Lieferschein Text vor Artikeltabelle

> **Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> hiermit liefern wir Ihnen:
>
> {IF}{TRACKINGNUMMER}{THEN}Trackingnummer/n:{TRACKINGNUMMER}{ELSE}{ENDIF}

Lieferschein Text am Ende (nach Freitext)

> **Anmerkung**
>
> **Hinweis**
>
> Dieses Formular wurde maschinell erstellt und ist ohne Unterschrift gültig.

#### Gutschrift - Beispiel Textbausteine

Gutschrift Text vor Artikeltabelle

> **Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> anbei Ihre {ART}:

Gutschrift Text am Ende (nach Freitext)

> **Anmerkung**
>
> **Hinweis**
>
> Dieses Formular wurde maschinell erstellt und ist ohne Unterschrift gültig.

#### Bestellung - Beispiel Textbausteine

Bestellung Text vor Artikeltabelle

> **Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> wir bestellen hiermit:
>
> Unsere Auftragsnummer: {BESTELLUNGBESTAETIGTABNUMMER} Lieferadresse: {LIEFERADRESSELANG}
>
> Bitte liefern Sie bis zum: {GEWUENSCHTESLIEFERDATUM}

Bestellung Text am Ende (nach Freitext)

> **Anmerkung**
>
> **Hinweis**
>
> Dieses Formular wurde maschinell erstellt und ist ohne Unterschrift gültig.

## Spezielle Textbausteine

### Textbaustein für EU Lieferung und Export Drittland

Den Standardtext für EU-Lieferung (Innergemeinschaftliche Lieferung) und Export (Drittland) gibst du in die entsprechenden Felder ein.

> **Anmerkung**
>
> Bevor du mit der Erstellung von Belegen - insbesondere Rechnungen und Gutschriften - beginnst, stelle sicher, welche Steuerrechtlichen Vorgaben für dein Geschäft gelten, indem du dich an dein lokales Steuerbüro oder das Finanzamt/Steuerbehörde wendest.

**EU-Lieferung Vermerk** (Beispiel):

> **Anmerkung**
>
> **Hinweis**
>
> EU-Lieferung Vermerk: Steuerfrei nach § 4 Nr. 1b i.V.m. § 6 a UStG.Ihre USt-IdNr. {USTID} Land: {LAND}

**Export-Lieferung Vermerk** (Beispiel):

> **Anmerkung**
>
> **Hinweis**
>
> Export-Lieferung Vermerk: Steuerfrei (Drittland) gem. §4 Nr. 1a UStG **Export-Lieferung Vermerk**

(Beispiel mit Bedingung: Steuertext Schweiz abweichend von Steuertext anderer Drittländer):

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{LAND}="CH"{THEN}Steuertext für CH{ELSE}Steuertext für alle anderen Drittländer{ENDIF}

![2885091381.png](https://help.xentral.com/hc/article_attachments/14212133209500)

> **Anmerkung**
>
> Der Text wird in Belegen bei entsprechender Einstellung der Steuer angedruckt. Z.B. **Land ** in Rechnungs- und Lieferadresse und die Einstellung der Besteuerung **EU-Lieferung ** oder**Export** im Beleg.

### Besteuerung 7% und 19% gemischt

Gemischte Besteuerung und getrennter Ausweis der MWST bei gemischten Rechnungen. Achte auf die korrekten Angaben auf deinen Belegen.

> **Anmerkung**
>
> Bevor du mit der Erstellung von Belegen - insbesondere Rechnungen und Gutschriften - beginnst, stelle sicher, welche Steuerrechtlichen Vorgaben für dein Geschäft gelten, indem du dich an dein lokales Steuerbüro oder das Finanzamt/Steuerbehörde wendest.

Beispiel für die Angabe der Netto und Bruttobeträge auf deinen Belegen:

> **Anmerkung**
>
> **Hinweis**
>
> Der Gesamtbetrag setzt sich zusammen aus {STEUERNORMAL}% {GESAMTNETTONORMAL} {WAEHRUNG} und {STEUERERMAESSIGT}% {GESAMTNETTOERMAESSIGT} {WAEHRUNG}.

![2885091387.png](https://help.xentral.com/hc/article_attachments/14212149846684)

## Reihenfolge in den Textvorlagen

Du kannst für die Inhaltsblöcke der Textvorlagen auch die Reihenfolge festlegen, in der einzelne Textelemente im jeweiligen Beleg aufgelistet werden sollen.

| | |
| **{FOOTERFREITEXT}** | Freitext, der im Dokument selbst beim Anlegen z.B. eines Auftrags eingegeben werden kann |
| **{FOOTERTEXTVORLAGEANGEBOT}** | Textblock hier in den Textvorlagen: „Angebot Text am Ende (nach Freitext)„ |
| **{FOOTERSTEUER}** | Textblock hier in den Textvorlagen: „EU-Lieferung Vermerk“ oder „Export-Lieferung Vermerk“ (je nach Einstellung im Beleg wird einer gezogen) |
| **{FOOTERZAHLUNGSWEISETEXT}** | Standardtext bei „Zahlungsweisen“ |
| **{FOOTERSYSTEMFREITEXT}** | wird z.B. für PaypalPlus, Secupay, Billpay usw. genutzt, wenn von externen Modulen Inhalte auf den Belegen angezeigt werden müssen (Voraussetzung ist das Modul der jeweiligen Zahlungsart/Forderungsmanagement) |
| **{FOOTERVERSANDINFO}** | wenn vorhanden wird folgendes abgedruckt: „Versandart: Trackingnummer“ (der Name Versandart (entspricht der Versandart) gefolgt von der Trackingnummer) |
| **{FOOTERTEXTVORLAGELIEFERSCHEIN}** | Textblock hier in den Textvorlagen: „Lieferschein Text am Ende (nach Freitext)„ |
| **{FOOTERTEXTVORLAGEBESTELLUNG}** | Textblock hier in den Textvorlagen: „Bestellung Text am Ende (nach Freitext)„ |
| **{FOOTERTEXTVORLAGERECHNUNG}** | Textblock hier in den Textvorlagen: „Rechnung Text am Ende (nach Freitext)„ |

Die verwendbaren Variablen stehen dabei direkt bei der Checkbox mit dabei. Für die Auftragsbestätigung könnte die Reihenfolge zum Beispiel wie folgt verändert werden.

![Grundeinstellung-37-Footerfreitext.png](https://help.xentral.com/hc/article_attachments/14212118174108)

Dies würde sich dann wie folgt auf die Ansicht der Auftragsbestätigung auswirken.

![Grundeinstellung-38-Vorschau-Footer.png](https://help.xentral.com/hc/article_attachments/14212123250460)

## Variablen und Beispiele

> **Anmerkung**
>
> **Legende**:
>
> AN = Angebot
>
> AB = Auftragsbestätigung
>
> BE = Bestellung
>
> LS = Lieferschein
>
> RE = Rechnung
>
> GS = Gutschrift
>
> PF = Proformarechnung
>
> PA = Preisanfrage
>
> RT = Retoure

### Beispiel: Bestellung

> **Anmerkung**
>
> **Hinweis**
>
> Sehr geehrte Damen und Herren,
>
> wir bestellen hiermit:
>
> Unsere Kundennummer: {ADRESSE_KUNDENNUMMERLIEFERANT}
>
> Unsere Auftragsnummer von Ihnen: {BESTELLUNGBESTAETIGTABNUMMER}
>
> Unsere Angebotsnummer von Ihnen: {ANGEBOT}
>
> Bitte liefern Sie bis zum: {GEWUENSCHTESLIEFERDATUM}
>
> Lieferadresse: {LIEFERADRESSELANG}

![textvorlagen_001.png](https://help.xentral.com/hc/article_attachments/14322916462492)

### Beispiel: Rechnung, Gutschrift, GLN

> **Anmerkung**
>
> **Hinweis**
>
> {ANSCHREIBEN},
>
> vielen Dank für Ihren Auftrag.
>
> Folgende Positionen stellen wir Ihnen in Rechnung/schreiben wir Ihnen gut.
>
> {IF}{TRANSAKTIONSNUMMER}{THEN}Transaktionsnummer: {TRANSAKTIONSNUMMER}{ELSE}{ENDIF}
>
> {IF}{LIEFERSCHEIN}{THEN}Lieferschein: {LIEFERSCHEIN}{ELSE}{ENDIF}
>
> {IF}{ART}{THEN}Art des Beleges: {ART}{ELSE}{ENDIF}
>
> {IF}{INTERNET}{THEN}Shopbestellnummer: {INTERNET}{ELSE}{ENDIF}
>
> {IF}{AUFTRAGSDATUM}{THEN}Auftragsdatum: {AUFTRAGSDATUM}{ELSE}{ENDIF}
>
> {IF}{VERSANDARTBEZEICHNUNG}{THEN}Versandart: {VERSANDARTBEZEICHNUNG}{ELSE}{ENDIF}
>
> {IF}{ADRESSE_GLN}{THEN}GLN: {ADRESSE_GLN}{ELSE}{ENDIF}
>
> {IF}{LIEFERGLN}{THEN}GLN: {LIEFERGLN}{ELSE}{ENDIF}
>
> {IF}{LIEFERADRESSE}{THEN}Lieferadresse: {LIEFERADRESSE}{ELSE}{ENDIF}

### Beispiel: Liefertermin / Lieferwoche

Liefertermin und die Lieferwoche können auch kombiniert verwendet werden z.B. {LIEFERTERMIN} / {LIEFERWOCHE}

> **Anmerkung**
>
> **Hinweis**
>
> Sehr geehrte Damen und Herren,
>
> vielen Dank für Ihren Auftrag.
>
> Lieferadresse: {LIEFERADRESSELANG}
>
> {IF}{LIEFERTERMIN}{THEN}Ihr Wunsch-Liefertermin: {LIEFERTERMIN}{ELSE}{ENDIF} / {IF}{LIEFERWOCHE}{THEN}Lieferwoche: {LIEFERWOCHE}{ELSE}{ENDIF}

### Beispiel: Abweichende Lieferadresse

Die abweichende Lieferadresse kann als Variable z.B. auf Angebot, Auftrag, Rechnung genommen werden. Angezeigt werden kann die Lieferadresse in Kurz- oder Langform. Normalerweise wird die Lieferadresse als Block unter der Artikeltabelle angeordnet.

{LIEFERADRESSE} → Lieferadresse (nur wenn Lieferadresse als abweichend angegeben)

{LIEFERADRESSELANG} → Lieferadresse mit mehr Angaben

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{LIEFERADRESSE}{THEN}Lieferadresse:{LIEFERADRESSE}{ELSE}{ENDIF}
>
> {IF}{ABWEICHENDE_RECHNUNGSADRESSE}{THEN}Abweichende Rechnungsadresse: {ABWEICHENDE_RECHNUNGSADRESSE}{ELSE}{ENDIF}

### Beispiel: Lieferantennummer / Kundennummer

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{LIEFERANTENNUMMER}{THEN}Ihre Lieferantennummer:{LIEFERANTENNUMMER}{ELSE}{ENDIF}

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{KUNDENNUMMER}{THEN}Ihre Kundennummer:{KUNDENNUMMER}{ELSE}{ENDIF}

### Beispiel: Lieferantennummer bei Kunde / Kundennummer bei Lieferant

{ADRESSE_LIEFERANTENNUMMERBEIKUNDE} Lieferantennummer bei Kunde → deine Lieferantennummer, die dir dein Kunde in seiner Warenwirtschaft gegeben hat. Diese Nummer kann als Variable nur bei ausgehenden Dokumenten an deine Kunden verwendet werden. Einzutragen in der Adresse.

{ADRESSE_KUNDENNUMMERLIEFERANT} Kundennummer bei Lieferant → deine Kundennummer, die dir dein Lieferant in seiner Warenwirtschaft gegeben hat. Diese Nummer kann als Variable nur bei ausgehenden Dokumenten an deinen Lieferanten verwendet werden. Einzutragen in der Adresse.

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{ADRESSE_LIEFERANTENNUMMERBEIKUNDE}{THEN}Unsere Lieferantennummer: {ADRESSE_LIEFERANTENNUMMERBEIKUNDE}{ELSE}{ENDIF}

> **Anmerkung**
>
> **Hinweis**
>
> {IF}{ADRESSE_KUNDENNUMMERLIEFERANT}{THEN}Unsere Kundennummer: {ADRESSE_KUNDENNUMMERLIEFERANT}{ELSE}{ENDIF}

### Adresse Variablen (Basics)

| | |
| **{ANSCHREIBEN}** | Adress-Anschreiben Feld |
| {FREIFELD1} | Adress-Freifeld 1 |
| {FREIFELD2} | Adress-Freifeld 2 |
| {FREIFELD3} | Adress-Freifeld 3 |
| **{KUNDENNUMMER}** | Kundennummer des Kunden |
| **{LAND}** | ISO Länderkürzel |
| **{LIEFERADRESSE}** | Lieferadresse: Nur wenn Lieferadresse als abweichend angegeben, sonst erscheint „Entspricht Rechnungsadresse“ |
| **{USTID}** | Umsatzsteuernummer des Kunden |
| {GLN} | Adress-GLN |
| {LIEFERGLN} | GLN aus der Lieferadresse |
| {ADRESSE_RECHNUNG_GLN} | GLN aus der abweichenden Rechnungsadresse |

### Belege Variablen (Basics)

| | |
| *Belege-Details* | |
| **{BELEGNUMMER}** | Belegnummer des aktuellen Dokumentes |
| **{IHREBESTELLNUMMER}** | Ihre Bestellnummer / Kommission |
| **{INTERNET}** | Zeigt die im Auftrag hinterlegte Internetnummer (= Shop-Bestellnummer) auf dem Beleg z.B. Lieferschein an. Beispiel: Verwende die Variable {INTERNET} in der Textvorlage des Lieferscheins – der Platzhalter wird beim Erstellen automatisch durch die gespeicherte Internetnummer ersetzt (z. B. aus einem Webshop-Import) |
| {LIEFERBEDINGUNG} | Lieferbedingungen z.B. Frei Haus |
| {LIEFERTERMIN} | Feld Wunschliefertermin |
| **{TRACKINGNUMMER}** | Trackingnummer falls Paketmarke erzeugt und Tracking bestätigt |
| **{VERSANDARTBEZEICHNUNG}** | Bezeichnung der Versandart |
| {ABWEICHENDEBEZEICHNUNG} | Haken für abweichende Bezeichnung gesetzt - wichtig für anderen Text bei abweichender Belegbezeichnung via IF-Blöcke |
| *Belege-Positionen* | |
| **{ANZAHLTEILE}** | Gesamtmenge aller Positionen |
| **{NETTOGEWICHT}** | Gesamtgewicht aller Positionen |

> **Anmerkung**
>
> Die Belgeg-Variablen werden aus dem Beleg selber genommen.
>
> Wenn die Felder im Beleg manuell angepasst wurden, können diese Variablen somit vom Inhalt der verknüpften Adresse abweichen.

### Häufig genutzte Variablen: Belege und Adressen

#### Belege

| | |
| {ADRESSE} | „Kunde“ Feld im Beleg. Gibt die Adress-ID aus (AN,) |
| {PROJEKT} | „Projekt“ Feld im Beleg. Gibt die Projekt-Kennung aus (AN,) |
| {AKTION} | Aktionscode“ Feld im Beleg (AN,) |
| {STATUS} | „Status“ Feld im Beleg (AN,) |
| {ANFRAGE} | „Ihre Anfrage“ Feld im Beleg (AN,) |
| {INTERNEBEZEICHNUNG} | „Interne Bezeichnung“ Feld im Beleg (AN,) |
| {DATUM} | „Datum“ Feld im Beleg. Format ist TT.MM.JJJJ (AN,) |
| {LIEFERDATUM} | „Lieferdatum“ Feld im Beleg. Format ist TT.MM.JJJJ oder MM/JJJJ falls KW angehakt (AN,) |
| {LIEFERDATUMKW} | „KW“ Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |
| {GUELTIGBIS} | „Angebot gültig bis“ Feld im Beleg. Format ist TT.MM.JJJJ (AN,) |
| {PLANEDORDERDATE} | „gepl. Auftragsdatum“ Feld im Beleg. Format ist JJJJ-MM-TT (AN,) |
| {SCHREIBSCHUTZ} | „Schreibschutz“ Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |
| {ABWEICHENDEBEZEICHNUNG} | „Abweichende Bezeichnung“ Feld im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |

#### Abweichende Lieferadresse

| | |
| {ABWEICHENDELIEFERADRESSE} | „Abweichende Lieferadresse“ Lieferadresse Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |
| {LIEFERNAME} | „Name“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERTITEL} | „Titel“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERANSPRECHPARTNER} | „Ansprechpartner“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERABTEILUNG} | „Abteilung“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERUNTERABTEILUNG} | „Unterabteilung“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERADRESSZUSATZ} | „Adresszusatz“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERSTRASSE} | „Straße“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERPLZ} | „PLZ“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERORT} | „Ort“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFERBUNDESSTAAT} | „Bundesstaat“ Lieferadresse Feld im Beleg. Inhalt dargestellt in Kürzel 2-stellig (AN,) |
| {LIEFERLAND} | „Land“ Lieferadresse Feld im Beleg. Inhalt dargestellt in ISO-Länderkürzel 2-stellig (AN,) |
| {LIEFERGLN} | „GLN“ Lieferadresse Feld im Beleg (AN,) |
| {LIEFEREMAIL} | „E-Mail“ Lieferadresse Feld im Beleg (AN,) |

#### Stammdaten

| | |
| **{TYP}**| „Typ“ Feld des Adresse-Typs in der Adresse (standardmäßig frau, herr, firma kleingeschrieben). Änderbar unter * Administration → AppStore → Adresse Typ*. **Hinweis:** Wird der Typ geändert (z.B. von frau zu Frau), müssen alle bestehenden Adressen nochmal zugewiesen werden (AN,) |
| **{NAME}** | „Name“ Feld im Beleg (AN,) |
| **{TITEL}** | „Titel“ Feld im Beleg (AN,) |
| **{ANSPRECHPARTNER}** | „Ansprechpartner“ Feld im Beleg (AN,) |
| **{ABTEILUNG}** | „Abteilung“ Feld im Beleg (AN,) |
| **{UNTERABTEILUNG}** | „Unterabteilung“ Feld im Beleg (AN,) |
| **{ADRESSZUSATZ}** | „Adresszusatz“ Feld im Beleg (AN,) |
| **{STRASSE}** | „Straße“ Feld im Beleg (AN,) |
| **{PLZ}** | „PLZ“ Feld im Beleg (AN,) |
| **{ORT}** | „Ort“ Feld im Beleg (AN,) |
| **{BUNDESSTAAT}** | „Bundesstaat“ Feld im Beleg. Inhalt dargestellt in Kürzel 2-stellig (AN,) |
| **{LAND}** | „Land“ Feld im Beleg. Inhalt dargestellt in ISO-Länderkürzel 2-stellig (AN,) |
| **{TELEFON}** | „Telefon“ Feld im Beleg (AN,) |
| **{TELEFAX}** | „Telefax“ Feld im Beleg (AN,) |
| **{EMAIL}** | „E-Mail“ Feld im Beleg (AN,) |
| **{ANSCHREIBEN}** | „Anschreiben“ Feld im Beleg (AN,) |
| | |

#### Info für Angebots- und Auftragserfassung

| | |
| **{ADRESSE_INFOAUFTRAGSERFASSUNG}** | „Info für Angebots- und Auftragserfassung“ Feld im Beleg (AN,) |

#### Beleg Freitext und Kopftext

| | |
| **{FREITEXT}** | „Freitext“ Feld im Beleg (AN,) |
| **{BODYZUSATZ}** | „Kopftext“ Feld im Beleg (AN,) |

#### Belegart (Angebot, Auftrag, etc.)

| | |
| **{ZAHLUNGSWEISE}**| „Zahlungsweise“ Feld im Beleg. Der Inhalt ist der Typ der Zahlungsweise unter * Administration → Einstellungen → Zahlungsweisen* (AN,) |
| **{VERSANDART}**| „Versandart“ Feld im Beleg. Inhalt des Typs der Versandart unter * Administration → Einstellungen ⇒ Versandarten* (AN,) |
| **{LIEFERBEDINGUNG}** | „Lieferbedingung“ Feld im Beleg (AN,) |
| **{VERTRIEB}** | “Vertrieb“ Feld im Beleg. Zeigt den Namen der verknüpften Adresse des hinterlegten Benutzers an (AN,) |
| **{BEARBEITER}** | „Bearbeiter“ Feld im Beleg. Zeigt den Namen der verknüpften Adresse des hinterlegten Benutzers an (AN,) |
| **{KEINPORTO}** | „Kein Porto“ Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |
| **{OHNE_BRIEFPAPIER}** | „Kein Briefpapier und Logo“ Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |
| **{GESAMTSUMMEAUSBLENDEN}** | „Gesamtsumme ausblenden“ Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |
| **{OHNE_ARTIKELTEXT}** | „Artikeltexte ausblenden“ Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |

#### GLN (B2B)

| | |
| **{GLN}** | „GLN“ Feld im Beleg (AN,) |

#### Zahlungsweise - Rechnung

| | |
| **{ZAHLUNGSZIELTAGE}** | „Zahlungsziel (in Tagen)“ Feld im Beleg (AN,) |
| **{ZAHLUNGSZIELTAGESKONTO}** | „Skonto (in Tagen)“ Feld im Beleg (AN,) |

#### Skonto

| | |
| **{ZAHLUNGSZIELSKONTO}** | „Skonto“ Feld im Beleg. Inhalt mit Punkt und 2-stelligen Nachkommastellen (AN,) |

#### Interne Bemerkung

| | |
| **{INTERNEBEMERKUNG}** | „Interne Bemerkung“ Feld im Beleg (AN,) |

#### UST-Prüfung

| | |
| **{USTID}** | „UST ID“ Feld im Beleg (AN,) |
| **{UST_BEFREIT}** | „Besteuerung“ Feld im Beleg. Inhalt „0“ für Inland, „1“ für EU-Lieferung, „2“ für Export„ und „3“ für Steuerfrei Inland (AN,) |
| **{KEINSTEUERSATZ}** | „ohne Hinweis bei EU oder Export“ Haken im Beleg. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt (AN,) |

#### Einstellung im Beleg

| | |
| **{ANZEIGESTEUER}** | „Anzeige Steuer“ Feld im Beleg. Inhalt „0“ für automatisch, „3“ für netto, „4“ für brutto (AN,) |
| **{WAEHRUNG}** | „Währung“ Feld im Beleg. 3-stellige Währung, z.B: EUR, CAD, USD (AN,) |
| **{SPRACHE}** | „Sprache“ Feld im Beleg. Gibt den „Value“ der Option wieder ohne Umlaute (z.B. „franzoesisch“) (AN,) |
| **{KURS}** | „Wechselkurs“ Feld im Beleg. Inhalt mit Punkt und 9-stelligen Nachkommastellen (AN,) |
| **{KOSTENSTELLE}** | „Kostenstelle“ Feld im Beleg. Gibt die Nummer der Kostenstelle an (AN,) |

#### Weitere Beleg Variablen

| | |
| **{ANSPRECHPARTNER}** | Ansprechpartner bei Adresse (Verfügbar in allen Belegen) |
| **{LIEFERWOCHE}** | Kunden Wunschliefertermin Angezeigt als Lieferwoche (Kalenderwoche: KW) |
| **{GUELTIGBIS}** | Datumsangabe: „Angebot gültig bis“ (Verfügbar in allen Belegen) |
| **{GUELTIGBISWOCHE}** | Kalenderwoche → Angebot gültig bis Kalenderwoche XY (Verfügbar in allen Belegen) |
| **{LIEFERADRESSE}** | Lieferadresse (nur wenn Lieferadresse als abweichend angegeben; Verfügbar in allen Belegen) |
| **{LIEFERADRESSE_HINWEIS}** | Lieferhinweis Bemerkung (nur wenn Lieferadresse als abweichend angegeben; Verfügbar in AN, AB, LS) |
| **{LIEFERADRESSELANG}** | Lieferadresse (wird in einer Zeile angezeigt und nicht als mehrzeiliger Block; Verfügbar in allen Belegen) |
| **{ANZAHLTEILEALLE}** | Zeigt alle Teile (Verfügbar in AN, AB, BE, LS, RE, GS, PF, PA, RT) |
| **{AUFTRAG}** | Auftragsnummer (Verfügbar in AB) |
| **{AUFTRAGSDATUM}** | Datum des vorausgegangenen Auftrags (Verfügbar in LS, RE, RT aus dazugehöriger AB) |
| **{PROJEKT}**/**{PROJEKTNUMMER}** | Projekt, auf das das aktuelle Dokument läuft (Verfügbar in allen Belegen) |
| **{ART}**/**{BELEGART}** | Art des Beleges, also z.B. Gutschrift, Stornorechnung, Rechnung, Angebot, Auftrag, etc. (Verfügbar in allen Belegen) |
| **{TRANSAKTIONSNUMMER}** | Bezahlungs Transaktionsnummer, z.B PayPal Transaktionsnummer (Feld im Auftrag → wird beim Shopimport automatisch gefüllt; Verfügbar in AB sowie LS, GS, RE, RT aus vorausgegangener AB) |
| **{USTID}** | Umsatzsteuernummer des Kunden (muss in Adresse gepflegt sein) z.B. zu verwenden für die Angabe der USTID beim innergemeinschaftlichen Erwerb |
| **{BEARBEITER}** | Bearbeiter des Dokumentes |
| **{VERSANDART}** | Typ der Versandart des Dokumentes z.B. dhl560, Selbstabholer, dpd, Spedition (Lieferbedingungen sind extra) |
| **{LIEFERADRESSE_HINWEIS}** | Hinweis aus Lieferadresse für Belege: Angebot, Auftrag oder Lieferfschein (Lieferhinweis Textbox aus „Adresse → Stammdaten → Lieferadresse“) |
| **{ADRESSE_FREIFELD1}** | Freifelder aus Adresse |
| **{INTERNEBEZEICHNUNG}** | |
| **{VERBANDSNUMMER}** | |
| **{VERBAND}** | |
| **{ADRESSE_MANDATSREFERENZ}** | Mandatsreferenz aus den Kundenstammdaten |
| **{BESTELLUNGBESTAETIGTABNUMMER}** | Bestellung: AB Nummer von Lieferant → Die Auftragsnummer, die Sie von Ihrem Lieferanten erhalten haben. |
| **{ANGEBOT}** | Bestellung: Ihr Angebot → Die Angebotsnummer, die Sie von Ihrem Lieferanten erhalten haben |
| **{GEWUENSCHTESLIEFERDATUM}** | Bestellung: Wunsch Liefertermin → Ihr Wunschliefertermin, den Sie angeben können |
| **{ABWEICHENDE_RECHNUNGSADRESSE}** | Abweichende Rechnungsadresse (weitere Adresse aus den Adressdaten → abweichende Rechnungsadresse; Verfügbar in allen Belegen) |
| **{ABWEICHENDE_RECHNUNGSADRESSELANG}** | Abweichende Rechnungsadresse (weitere Adresse aus den Adressdaten → abweichende Rechnungsadresse) - diese wird in eine Zeile geschrieben, statt untereinander. (Verfügbar in allen Belegen) |
| **{BEZAHLT_AM}** | Nur für Rechnungsdokumente → Datumsfeld, wann die Rechnung auf bezahlt gesetzt wurde |
| **{KOSTENSTELLE}** | im Beleg unter Details hinterlegte Kostenstelle (AN, AB, BE, LS, RE, GS) |
| **{LABELS}** | Labels, die dem Beleg zugeweisen waren, werden kommagetrennt als Text ausgegeben. |

### Weitere Adress-Variablen

> **Anmerkung**
>
> Die Adress-Variablen werden direkt aus der im Beleg verknüpften Adresse geladen.
>
> Somit können die Inhalte vom Beleg abweichen, wenn dieser manuell geändert wurde.

#### Adresse → Details → Adressdaten → Stammdaten

| | |
| **{ADRESSE_TYP}**| „Typ“ Feld des Adresse-Typs in der Adresse (standardmäßig frau, herr, firma kleingeschrieben). Änderbar unter * Administration → AppStore → Adresse Typ*. **Hinweis:** Wird der Typ geändert (z.B. von frau zu Frau), müssen alle bestehenden Adressen nochmal zugewiesen werden. |
| **{ADRESSE_NAME}** | „Name“ Feld in der Adresse |
| **{ADRESSE_TITEL}** | „Titel“ Feld in der Adresse |
| **{ADRESSE_ANSPRECHPARTNER}** | „Ansprechpartner“ Feld in der Adresse |
| **{ADRESSE_ABTEILUNG}** | „Abteilung“ Feld in der Adresse |
| **{ADRESSE_UNTERABTEILUNG}** | „Unterabteilung“ Feld in der Adresse |
| **{ADRESSE_ADRESSZUSATZ}** | „Adresszusatz“ Feld in der Adresse |
| **{ADRESSE_STRASSE}** | „Straße“ Feld in der Adresse |
| **{ADRESSE_PLZ}** | „PLZ“ Feld in der Adresse |
| **{ADRESSE_ORT}** | „Ort“ Feld in der Adresse |
| **{ADRESSE_BUNDESSTAAT}** | „Bundesstaat“ Feld in der Adresse. Inhalt dargestellt in Kürzel 2-stellig (z.B. BY) |
| **{ADRESSE_LAND}** | „Land“ Feld in der Adresse. Inhalt dargestellt in ISO-Länderkürzel 2-stellig (z.B. AT) |
| **{ADRESSE_LIEFERBEDINGUNG}** | „Lieferbedingung“ Feld in der Adresse |
| **{ADRESSE_GLN}** | „GLN“ Feld in der Adresse |
| **{ADRESSE_ABWEICHENDE_RECHNUNGSADRESSE}** | „Abw. Rechnungsadresse“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt. Eher wichtig für anderen Text bei abweichender Belegbezeichnung via IF-Blöcke. |

#### Adresse → Details → Adressdaten → Kontaktdaten

| | |
| **{ADRESSE_TELEFON}** | „Telefon“ Feld in der Adresse |
| **{ADRESSE_TELEFAX}** | „Telefax“ Feld in der Adresse |
| **{ADRESSE_MOBIL}** | „Mobil“ Feld in der Adresse |
| **{ADRESSE_ANSCHREIBEN}** | „Anschreiben“ Feld in der Adresse |
| **{ADRESSE_EMAIL}** | „E-Mail“ Feld in der Adresse |
| **{ADRESSE_INTERNETSEITE}** | „Internetseite“ Feld in der Adresse |

#### Adresse → Details → Adressdaten → Zuordnung

| | |
| **{ADRESSE_VERTRIEB}** | ID der Vertriebs-Adresse im „Vertrieb“ Feld in der Adresse |
| **{ADRESSE_INNENDIENST}** | ID der Innendienst-Adresse im „Innendienst“ Feld in der Adresse |
| **{ADRESSE_PROJEKT}** | ID des Projekts im „Hauptprojekt“ Feld in der Adresse |
| **{ADRESSE_FROMSHOP}** | ID des Shops im „Herkunftskanal (Shop)“ Feld in der Adresse |

#### Adresse → Details → Adressdaten → Einstellungen

| | |
| **{ADRESSE_LIEFERSPERRE}** | „Liefersperre“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt. |
| **{ADRESSE_LIEFERSPERREDATUM}** | Datum der Liefersperre im „Datum“ Feld in der Adresse. Wird im Format JJJJ-MM-TT dargestellt. |
| **{ADRESSE_LIEFERSPERREGRUND}** | „Liefersperre Grund“ Feld in der Adresse |
| **{ADRESSE_SPRACHE}** | „Sprache für Belege“ Feld in der Adresse. Gibt den „Value“ der Option wieder ohne Umlaute (z.B. „franzoesisch“) |
| **{ADRESSE_KUNDENFREIGABE}** | „Kundenfreigabe“ Feld in der Adresse. Inhalt dargestellt in „1“ für ja, oder „0“ für nein. |
| **{ADRESSE_FOLGEBESTAETIGUNGSPERRE}** | „Folgebestätigungsperre“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt. |
| **{ADRESSE_TRACKINGSPERRE}** | “Trackingmailsperre“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt. |
| **{ADRESSE_MARKETINGSPERRE}** | „Marketingsperre“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt. |
| **{ADRESSE_LEAD}** | „Lead“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt. |

#### Adresse → Details → Adressdaten → Einstellungen

| | |
| **{ADRESSE_RECHNUNG_TYP}** | „Typ“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_NAME}** | „Name“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_TITEL}** | „Titel“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_ANSPRECHPARTNER}** | „Ansprechpartner“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_ABTEILUNG}** | „Abteilung“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_UNTERABTEILUNG}** | „Unterabteilung“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_ADRESSZUSATZ}** | „Adresszusatz“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_STRASSE}** | „Straße“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_PLZ}** | „PLZ“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_ORT}** | „Ort“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_BUNDESSTAAT}** | „Bundesstaat“ Feld in der Abweichenden Rechnungsadresse der Adresse. Inhalt dargestellt in Kürzel 2-stellig (z.B. BY) |
| **{ADRESSE_RECHNUNG_LAND}** | „Land“ Feld in der Abweichenden Rechnungsadresse der Adresse. Inhalt dargestellt in ISO-Länderkürzel 2-stellig (z.B. AT) |
| **{ADRESSE_RECHNUNG_GLN}** | „GLN“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_TELEFON}** | „Telefon“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_TELEFAX}** | „Telefax“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_ANSCHREIBEN}** | „Anschreiben“ Feld in der Abweichenden Rechnungsadresse der Adresse |
| **{ADRESSE_RECHNUNG_EMAIL}** | „E-Mail“ Feld in der Abweichenden Rechnungsadresse der Adresse |

#### Adresse → Details → Adressdaten → Sonstiges

| | |
| **{ADRESSE_INFOAUFTRAGSERFASSUNG}** | „Info für Auftragserfassung“ Feld in der Adresse |
| **{ADRESSE_SONSTIGES}** | „Sonstiges“ Feld in der Adresse |

#### Adresse → Details → Zahlungskonditionen / Besteuerung → Zahlungskonditionen des Kunden für Rechnungen

| | |
| **{ADRESSE_ZAHLUNGSKONDITIONEN_FESTSCHREIBEN}** | „Zahlungskonditionen festschreiben“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken angehakt, oder „0“ für nicht angehakt. |
| **{ADRESSE_ZAHLUNGSWEISE}**| „Zahlungsweise“ Feld in der Adresse. Der Inhalt ist der Typ der Zahlungsweise unter * Administration → Einstellungen → Zahlungsweisen* |
| **{ADRESSE_ZAHLUNGSZIELTAGE}** | „Zahlungsziel (bei Rechnung)“ Feld in der Adresse |
| **{ADRESSE_ZAHLUNGSZIELTAGESKONTO}** | „Zahlungsziel Skonto (bei Rechnung)“ Feld in der Adresse |
| **{ADRESSE_ZAHLUNGSZIELSKONTO}** | „Skonto (bei Rechnung)“ Feld in der Adresse. Inhalt mit Punkt und 2-stelligen Nachkommastellen. |
| **{ADRESSE_LIEFERANTENNUMMERBEIKUNDE}** | „Lieferantennummer bei Kunde“ Feld in der Adresse |
| **{ADRESSE_ZAHLUNGSWEISEABO}** | „Zahlungsweise Abo“ Feld in der Adresse. Inhalt „Standard aus Stammdaten“, „rechnung“ oder „lastschrift“ |
| **{ADRESSE_ART}** | „Belege im Auto-Versand erstellen“ Feld in der Adresse. Inhalt „standardauftrag“, „lieferung“ oder „rechnung“ |
| **{ADRESSE_KOMMISSIONSKONSIGNATIONSLAGER}** | Id des Lagerplatzes im „Kommissions-/Konsignationslager“ Feld in der Adresse |

#### Adresse → Details → Zahlungskonditionen / Besteuerung → Zahlungskonditionen beim Lieferant bei Bestellungen

| | |
| **{ADRESSE_ZAHLUNGSWEISELIEFERANT}**| „Zahlungsweise“ Lieferant Feld in der Adresse. Der Inhalt ist der Typ der Zahlungsweise unter * Administration → Einstellungen → Zahlungsweisen* |
| **{ADRESSE_ZAHLUNGSZIELTAGELIEFERANT}** | „Zahlungsziel (in Tagen)“ Lieferant Feld in der Adresse |
| **{ADRESSE_ZAHLUNGSZIELTAGESKONTOLIEFERANT}** | „Zahlungsziel Skonto (in Tagen)“ Lieferant Feld in der Adresse |
| **{ADRESSE_ZAHLUNGSZIELSKONTOLIEFERANT}** | „Skonto“ Lieferant Feld in der Adresse. Inhalt mit Punkt und 2-stelligen Nachkommastellen. |
| **{ADRESSE_VERSANDARTLIEFERANT}** | „Lieferart“ Feld in der Adresse |
| **{ADRESSE_KUNDENNUMMERLIEFERANT}** | „Kundennummer bei Lieferant“ Feld in der Adresse |
| **{ADRESSE_UMSATZSTEUER_LIEFERANT}** | „Besteuerung Verbindlichkeiten“ Feld in der Adresse. Inhalt „inland“, „eulieferung“, „import“ |
| **{ADRESSE_HINWEISTEXTLIEFERANT}** | „Lieferant Hinweis-Text“ Feld in der Adresse |

#### Adresse → Details → Zahlungskonditionen / Besteuerung → Steuer / Währung / Zoll

| | |
| **{ADRESSE_USTID}** | „USt-ID“ Feld in der Adresse |
| **{ADRESSE_STEUERNUMMER}** | „Steuernummer“ Feld in der Adresse |
| **{ADRESSE_UST_BEFREIT}** | „Besteuerung“ Feld in der Adresse. Inhalt „0“ für Inland, „1“ für EU-Lieferung, „2“ für Export“ und „3“ für Steuerfrei Inland |
| **{ADRESSE_WAEHRUNG}** | „Währung“ Feld in der Adresse. 3-stellige Währung, z.B: EUR, CAD, USD |
| **{ADRESSE_LIEFERSCHWELLENICHTANWENDEN}** | „Lieferschwelle nicht anwenden“ Feld in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |
| **{ADRESSE_ANZEIGESTEUERBELEGE}** | „Anzeige Steuer auf Belege“ Feld in der Adresse. Inhalt „0“ für automatisch, „1“ für immer netto und „2“ für immer brutto |
| **{ADRESSE_ZOLLINFORMATIONEN}** | „Zollinformationen“ Feld in der Adresse |
| | |

#### Adresse → Details → Zahlungskonditionen / Besteuerung → Kunde/Lieferant

| | |
| **{ADRESSE_KUNDENNUMMER}** | „Kunden Nr.“ Feld in der Adresse |
| **{ADRESSE_KUNDENNUMMER_BUCHHALTUNG}** | „Abw. Debitoren Nr.“ Feld in der Adresse |
| **{ADRESSE_LIEFERANTENNUMMER}** | „Lieferanten Nr.“ Feld in der Adresse |
| **{ADRESSE_LIEFERANTENNUMMER_BUCHHALTUNG}** | „Abw. Kreditoren Nr.“ Feld in der Adresse |
| **{ADRESSE_MITARBEITERNUMMER}** | „Mitarbeiter Nr.“ Feld in der Adresse |

#### Adresse → Details → Bankverbindung → Bankverbindung

| | |
| **{ADRESSE_INHABER}** | „Inhaber“ Feld in der Adresse |
| **{ADRESSE_SWIFT}** | „BIC“ Feld in der Adresse |
| **{ADRESSE_MANDATSREFERENZ}** | „Mandatsreferenz“ Feld in der Adresse |
| **{ADRESSE_MANDATSREFERENZDATUM}** | „Mandatsreferenz Datum“ Feld in der Adresse. Inhalt mit Format JJJJ-MM-TT |
| **{ADRESSE_BANK}** | „Bank“ Feld in der Adresse |
| **{ADRESSE_IBAN}** | „IBAN“ Feld in der Adresse |
| **{ADRESSE_MANDATSREFERENZART}** | „Lastschrift Art“ Feld in der Adresse. Inhalt „einmalig“ und „wdh“ |
| **{ADRESSE_MANDATSREFERENZWDHART}** | „Lastschrift Art“ Feld in der Adresse. Inhalt „erste“ und „folge“ |
| **{ADRESSE_MANDATSREFERENZAENDERUNG}** | „Mandatsreferenz Änderung“ Feld in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |
| **{ADRESSE_FIRMENSEPA}** | „Firmen-SEPA“ Feld in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |
| **{ADRESSE_MANDATSREFERENZHINWEIS}** | „Bemerkung“ Feld in der Adresse |

#### Adresse → Details → Bankverbindung → Paypal (bei Zahlungen)

| | |
| **{ADRESSE_PAYPALINHABER}** | „Inhaber“ Paypal Feld in der Adresse |
| **{ADRESSE_PAYPALWAEHRUNG}** | „Währung“ Paypal Feld in der Adresse |
| **{ADRESSE_PAYPAL}** | „Paypal-Account“ Feld in der Adresse |

#### Adresse → Details → Dokumente Versandoption → Allgemeine Versandoptionen

| | |
| **{ADRESSE_RECHNUNG_PAPIER}** | „Immer Papier Rechnung“ Feld in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |
| **{ADRESSE_RECHNUNG_ANZAHLPAPIER}** | „Anzahl Ausdrucke Rechnung“ Feld in der Adresse |

#### Adresse → Details → Dokumente Versandoption → E-Mail Empfänger

| | |
| **{ADRESSE_ANGEBOT_EMAIL}** | „Angebot“ E-Mail-Adresse Feld in der Adresse |
| **{ADRESSE_AUFTRAG_EMAIL}** | „Auftrag“ E-Mail-Adresse Feld in der Adresse |
| **{ADRESSE_RECHNUNGS_EMAIL}** | „Rechnung“ E-Mail-Adresse Feld in der Adresse |
| **{ADRESSE_GUTSCHRIFT_EMAIL}** | „Gutschrift“ E-Mail-Adresse Feld in der Adresse |
| **{ADRESSE_LIEFERSCHEIN_EMAIL}** | „Lieferschein“ E-Mail-Adresse Feld in der Adresse |
| **{ADRESSE_BESTELLUNG_EMAIL}** | „Bestellung“ E-Mail-Adresse Feld in der Adresse |

#### Adresse → Details → Dokumente Versandoption → E-Mail Kopie Empfänger

| | |
| **{ADRESSE_ANGEBOT_CC}** | „Angebot“ E-Mail-Adresse Kopie Feld in der Adresse |
| **{ADRESSE_AUFTRAG_CC}** | „Auftrag“ E-Mail-Adresse Kopie Feld in der Adresse |
| **{ADRESSE_RECHNUNG_CC}** | „Rechnung“ E-Mail-Adresse Kopie Feld in der Adresse |
| **{ADRESSE_GUTSCHRIFT_CC}** | „Gutschrift“ E-Mail-Adresse Kopie Feld in der Adresse |
| **{ADRESSE_LIEFERSCHEIN_CC}** | „Lieferschein“ E-Mail-Adresse Kopie Feld in der Adresse |
| **{ADRESSE_BESTELLUNG_CC}** | „Bestellung“ E-Mail-Adresse Kopie Feld in der Adresse |

#### Adresse → Details → Dokumente Versandoption → Fax Kopie Empfänger

| | |
| **{ADRESSE_ABPERFAX}** | „AB per Fax bevorzugt“ Feld in der Adresse |

#### Adresse → Details → Sonstige Daten → Vertrieb / Innendienst

| | |
| **{ADRESSE_PROVISION}** | „Provision“ Feld in der Adresse. Darstellung mit. und 2 Nachkommastellen |

#### Adresse → Details → Sonstige Daten → Porto / Versandart

| | |
| **{ADRESSE_PORTOFREI_AKTIV}** | „Porto frei aktiv“ Haken in der Adresse. Inhalt dargestellt in „1.00“ für Haken gesetzt und „0.00“ für nicht gesetzt |
| **{ADRESSE_PORTOFREIAB}** | „Porto frei aktiv“ Feld in der Adresse |
| **{ADRESSE_VERSANDART}**| „Versandart“ Feld in der Adresse. Inhalt des Typs der Versandart unter * Administration → Einstellungen ⇒ Versandarten* |
| **{ADRESSE_KEINEALTERSABFRAGE}** | „Keine Altersprüfung notwendig“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |

#### Adresse → Details → Sonstige Daten → Porto bei Lieferant

| | |
| **{ADRESSE_PORTOFREILIEFERANT_AKTIV}** | „Porto frei aktiv“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |
| **{ADRESSE_PORTOFREIABLIEFERANT}** | „Porto frei aktiv“ Feld in der Adresse |

#### Adresse → Details → Sonstige Daten → Sonstiges

| | |
| **{ADRESSE_GEBURTSTAG}** | „Geburtstag“ Feld in der Adresse. Datum Format JJJJ-MM-TT |
| **{ADRESSE_GEBURTSTAGKALENDER}** | „im Kalender anzeigen“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |
| **{ADRESSE_GEBURTSTAGSKARTE}** | „Geburtstagskarte“ Haken in der Adresse. Inhalt dargestellt in „1“ für Haken gesetzt und „0“ für nicht gesetzt |

#### Adresse → Details → Sonstige Daten → Finanzbuchhaltung

| | |
| **{ADRESSE_VERRECHNUNGSKONTOREISEKOSTEN}** | „Reisekosten“ Feld in der Adresse. Inhalt „0“ für Standardeinstellung |
| **{ADRESSE_KREDITLIMIT}** | „Kredit Limit“ Feld in der Adresse |

#### Adresse → Details → Sonstige Daten → Personalwesen Einstellungen

| | |
| **{ADRESSE_ARBEITSZEITPROWOCHE}** | „Arbeitszeit pro Woche:“ Feld in der Adresse. Inhalt mit. und 2 Nachkommastellen |

#### Adresse → Details → Sonstige Daten → Freifelder

| | |
| **{ADRESSE_FREIFELD1} - {ADRESSE_FREIFELD20}** | „Freifeld 1 - Freifeld 20“ Feld in der Adresse |

#### Adresse → Details → Sonstige Daten → Geodaten

| | |
| **{ADRESSE_LAT}** | „Breitengrad“ Feld in der Adresse. Inhalt mit. und 12 Nachkommastellen |
| **{ADRESSE_LNG}** | „Längengrad“ Feld in der Adresse. Inhalt mit. und 12 Nachkommastellen |

#### Adresse → Details → Sonstige Daten → Kennung

| | |
| **{ADRESSE_KENNUNG}** | „Eindeutige Kennung“ Feld in der Adresse |
| **{ADRESSE_LIEFERANTENNUMMERBEIKUNDE}** | Lieferantennummer, die Sie bei Ihrem Kunden erhalten haben (in seiner Warenwirtschaft), wenn Sie ihn beliefern. |
| **{ADRESSE_KUNDENNUMMERLIEFERANT}** | Kundennummer, die Sie von Ihrem Lieferanten erhalten haben (in seiner Warenwirtschaft), wenn Sie dort bestellen. |

### FAQs **Frage: Wie kann man das Gewicht des Warenauftrages auf dem Dokument anzeigen lassen?**

**Antwort:** Das Gewicht der Ware kann für das gesamte Dokument mit der Variable {NETTOGEWICHT} gezogen werden. Fügen Sie hierzu z.B. folgenden Text bei den Textvorlagen (Administration → Einstellungen → Grundeinstellungen → Textvorlagen) ein:

- Gewicht: {NETTOGEWICHT}

**Praxistipp **: Das Gewicht kann direkt im Artikel hinterlegt werden. ** Suchbegriffe:** Auftragsgewicht, Warenauftrag Gewicht, Gewichtangabe **Frage: Wie bekomme ich den Liefertermin auf die Auftragsbestätigung und andere Dokumente?**

**Antwort:** Es gibt Liefertermin und Lieferwoche als Variablen:

- {LIEFERTERMIN} → Kunden Wunschliefertermin aus dem Auftrag
- {LIEFERWOCHE} → Kunden Wunschliefertermin als KW (Kalenderwoche) aus dem Auftrag

Diese können Sie auf Ihre Geschäftsdokumente mit aufnehmen: Administration → Einstellungen → Grundeinstellungen → Textvorlagen **Hinweis: ** Im Auftrag gibt es zwei Felder: „Wunschliefertermin“ und „Auslieferung Lager“. „Auslieferung Lager“ zeigt Ihnen nur intern an (Schaltet die Ampel „Liefertermin“ auf grün, sobald der Tag erreicht ist), wann Sie packen müssen, damit der Kunde die Ware noch rechtzeitig zu seinem Wunschliefertermin bekommt. Der Wunschliefertermin kann für den Kunden als Information auf dem Briefpapier abgedruckt werden.** Praxistipp: ** Wenn Sie sich nur auf die KW (Kalenderwoche) festlegen können, dann verwenden Sie am besten nur die Variable für die Kalenderwoche.** Suchbegriffe: ** Liefertermin auf Dokument, Liefertermin auf Auftragsbestätigung ** Frage: Wie kann ich für einen Kunden einen speziellen Text auf einem Beleg anzeigen lassen?**

**Antwort:** Spezielle Texte können folgendermaßen aufgedruckt werden:

- Zahlungsweise → spezielle Zahlungsweise für einen Kunden
- Versandart → spezielle Versandart für einen Kunden
- Lieferbedingungen → spezielle Lieferbedingung für einen Kunden
- Lieferhinweis Bemerkung → z.B. Anlieferungshinweise, nur wenn Lieferadresse als abweichend angegeben, Variable {LIEFERADRESSE_HINWEIS}
- Freifeld → Sonstige Daten, die für einen Kunden auf allen Dokumenten unten mit abgedruckt werden müssen und unabhängig von den oben genannten Punkten laufen können als Freifeld in der Adresse gepflegt und nach Bedarf mit Variablen auf das Briefpapier eingefügt werden.

Wird nur die Variable eingefügt (also ohne textuelle Beschriftung), ist bei Kunden, die diesen Text nicht haben nichts sichtbar. Beispiel:

- **{ADRESSE_FREIFELD4}**→ druckt nur Text ab, wenn beim Kunden in Freifeld 4 etwas eingepflegt ist. ** Praxistipp:** Beschriften Sie die Freifelder mit eindeutigen textuellen Bezeichnungen, dann weiß jeder in Ihrer Firma, was sich genau hinter dem Freifeld in der Adresse verbirgt. Für Sonderfälle, die nur einen Kunden betreffen, empfiehlt es sich, die Freifelder gar nicht nach vorne zu ziehen. Dann wird auch nicht versehentlich in diese Felder falscher Text eingepflegt, da Sie „versteckt“ im letzten Reiter der Adresse bleiben. ** Suchbegriffe:** Kundenspezifischer Text, Rahmen- und Konditionsvereinbarungen textuell einfügen, Kundenspezifischer Dokumententext, Freifeldtext auf Dokumente abdrucken **Frage: Die Textvorlagen können nicht gespeichert werden. Wenn ich in der Datenbank den Text direkt eingebe, kommt ein SQL Fehler?**

**Antwort:** Das liegt an den Datenbank Einstellungen. Es müssen einige Einstellungen geändert werden:

Folgendes in my.cnf File ändern.

[mysqld] innodb_file_per_table=1 innodb_file_format = Barracuda innodb_log_file_size = 256M

Danach in der Datenbank folgendes eingeben:

ALTER TABLE firmendaten

ENGINE=InnoDB

ROW_FORMAT=COMPRESSED

KEY_BLOCK_SIZE=8;

Mögliche Fehlermeldung in SQL um es zu erkennen:

Row size too large (> 8126). Changing some columns to TEXT or BLOB or using ROW_FORMAT=DYNAMIC or ROW_FORMAT=COMPRESSED may help. In current row format, BLOB prefix of 768 bytes is stored inline.

**Suchbegriffe: ** Datenbankfehler, Textvorlagen speichern ** Frage: Die eingetragenen Vorlagen lassen sich nicht abspeichern. Woran kann dies liegen?**

**Antwort: **

- Dies kann an dem Standardsystem von MySQL liegen. Hier wurde bislang MyISAM als Standard verwendet. Dieses ist jedoch veraltet und es muss der InnoDB Storage Engine verwendet werden, damit die in Xentral eingetragenen Werte in der DB abgespeichert werden können.** Suchbegriffe: ** Abspeichern, Texte verschwinden, Vorlage kann nicht gespeichert werden **Frage: Ist es möglich auf allen Belegen die „Lieferantennummer bei Kunde“ oder „Kundennummer bei Lieferant“ anzeigen zu lassen?**

**Antwort:** Das sind folgende Variablen:

- {ADRESSE_LIEFERANTENNUMMERBEIKUNDE} → Lieferantennummer, die Sie bei Ihrem Kunden erhalten haben (in seiner Warenwirtschaft), wenn Sie ihn beliefern
- {ADRESSE_KUNDENNUMMERLIEFERANT} → Kundennummer, die Sie von Ihrem Lieferanten erhalten haben (in seiner Warenwirtschaft), wenn Sie dort bestellen **Suchbegriffe:** Variable Lieferantennummer bei Kunde oder Kundennummer bei Lieferant

Lieferantennummer bei Kunde **Frage: Wie kann ich Textvorlagen mit einer Wenn - Dann Bedingung anlegen? Kann ich IF ELSE Blöcke verwenden?**

**Antwort:** Eine IF ELSE Bedingung ist möglich in den Textvorlagen.

Hier finden Sie eine Beschreibung dazu:[IF & ELSE Variablen in Textvorlagen](#)

**Suchbegriffe: ** IF ELSE Textvorlagen, Bedingung Textvorlagen ** Frage: Der Steuertext wird auf der Rechnung nicht gezogen, auf anderen Dokumenten schon. Was kann das sein?**

**Antwort:** Prüfen Sie folgende Stellen:

- passt die Einstellung für die Steuer im Beleg?
- wurde im Briefpapier die Reihenfolge der Footer umgesltellt und fehlt die Variable {FOOTERSTEUER}
- ist der Text in den Vorlagen gar nicht vorhanden?
- fehlt die englische Übersetzung (wenn hier nichts angezeigt wird ein einer Sparche, sonst schon)

**Suchbegriffe: ** EU Text fehlt, Export Text fehlt, Steuertext fehlt ** Frage: Wir haben bei unseren Lieferscheinen ein Formatproblem. Warum erscheint der Text so groß?**

**Antwort:** Wenn Sie im Textfeld die Schriftgröße „default“ einstellen wird der Standard gezogen. Wenn z.B. hier Größe „12“ eingestellt ist, erscheint der Text viel zu groß auf dem Lieferschein.

Bitte den ganzen Text mit „STRG+A“ markieren und dann wieder auf „default“ umstellen. Dann speichern und es wird die korrekte Größe gezogen.

Sie können den Text auch auf was kleineres als Größe „12“ fest einstellen, z.B. Größe „8“.

**Suchbegriffe: ** Textbaustein Schriftgröße, Schrift zu groß ** Frage: Wie bekomme ich auf dem Rechnungsbeleg, der an eine abweichende Rechnungsadresse (Zentralverrechner) gestellt wird, den Hinweis zum Auftraggeber/ Kunden?**

**Antwort: ** Bei einer abweichende Rechnungsadresse, zusätzlich auf der Rechnung noch den tatsächlichen Kundennamen anzugeben, kann mit der Variable **{ADRESSE_NAME}** erfolgen. Das wäre am besten mit ** IF Blöcken** in den Textvorlagen lösbar, dann taucht das nur auf wenn es eine abweichende Rechnungs-Adresse gibt.

{IF}{ABWEICHENDE_RECHNUNGSADRESSE}{THEN}Kunde: {ADRESSE_NAME}, *{ADRESSE_STRASSE}, {ADRESSE_PLZ} {ADRESSE_ORT}*{ELSE}{ENDIF}

Falls der Kundenname allein ausreicht, reicht die Variable **{ADRESSE_NAME}**, die Variablen in kursiv sind optional. ** Suchbegriffe:** Textbaustein Kundename bei abweichende Rechnungsadresse, Zentralverrechner, ** Frage: Wie kann man eine IF-Abfrage auf die {LIEFERADRESSE} Variable machen um „entspricht Rechnungsadresse“ nicht einzublenden?**

**Antwort:** Das ist leider noch nicht möglich, da eine IF-Abfrage auf {LIEFERADRESSE} immer erfüllt ist, da im Hintergrund die Rechnungsadresse hinterlegt ist.

Man kann aber den Inhalt „entspricht Rechnungsadresse“ unter Administration ⇒ Einstellungen ⇒ Übersetzungen mit der Variable entspricht_rechnungsadresse übersetzen um den Inhalt zu ändern.

**Suchbegriffe: ** abweichende Rechnungsadresse, IF-Abfrage,** Frage: Nach dem Update auf eine höhere Xentral Version sind meine Textvorlagen verschwunden, was kann ich tun?**

**Antwort: ** Wenn Ihre Textvorlagen nach dem Update auf eine höhere Xentral Version verschwunden sind. Ist es nötig den Cache des entsprechenden Internet Browsers zu löschen. Anschließend stehen die Textvorlagen wieder wie gewohnt zur Verfügung.** Suchbegriffe:** Update, Textvorlagen weg