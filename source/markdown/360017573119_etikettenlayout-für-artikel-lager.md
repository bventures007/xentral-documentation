Etiketten sind ein wichtiger Bestandteil vieler Geschäftsprozesse: Sie erleichtern die Kennzeichnung, Identifikation und Nachverfolgung von Waren und Materialien. Ob im Lager, in der Produktion, beim Versand oder im Verkauf – Etiketten sorgen dafür, dass Artikel schnell gefunden, korrekt verbucht und eindeutig zugeordnet werden können.

In Xentral kannst du Etikettenlayouts erstellen für:

- **Artikeletiketten**: für die Kennzeichnung einzelner Produkte
- **Lageretiketten**: zur Beschriftung von Regalen und Lagerplätzen
- **Kommissionieraufkleber**: zur Unterstützung im Versandprozess (In entsprechenden Pick Prozessen z.B. Multi-Order-Picking)

Durch die Kombination von Text, Barcodes, QR-Codes und Variablen entstehen Etiketten, die automatisch mit den richtigen Daten befüllt werden.

> **Tipp**
>
> **Hinweis zur Nutzung in Prozessen:**
>
> Du musst **nicht für jeden Artikel manuell ein eigenes Etikett hinterlegen oder erstellen **. In Xentral definierst du ein oder mehrere ** Etikettenlayouts**, die sich zentral über das Modul Etiketten verwalten lassen. Diese Layouts kannst du bestimmten Einsatzzwecken zuweisen – z. B. artikel_klein für einzelne Produkte oder lagerplatz_klein für Regaletiketten.
>
> Ein solches Layout kann bei Bedarf **manuell im Artikel aufgerufen und gedruckt ** werden (z. B. für Muster oder Nachdrucke). In**Prozessen wie Wareneingang, Logistik, Produktion oder am Packtisch** erfolgt der Etikettendruck jedoch automatisiert, sobald der Prozessschritt ausgeführt wird – und zwar basierend auf dem zuvor festgelegten Layouttyp.
>
> Das bedeutet: Sobald dein Layout richtig zugeordnet ist, wird es im Alltag automatisch verwendet. Du sparst dir also die manuelle Zuweisung pro Artikel – das System erkennt selbst, wann welches Etikett benötigt wird.

> **Tipp**
>
> Für die Erstellung spezieller Etiketten – zum Beispiel Lebensmitteletiketten, EAN-Etiketten oder andere individuelle Formate – kannst du verschiedene Tools selbst nutzen. Damit lassen sich beispielsweise Versandboxen eindeutig etikettieren oder spezielle Lebensmittelaufkleber gestalten. Durch die Vergabe von Barcodes und QR-Codes können diese Artikel anschließend ganz normal in den jeweiligen Xentral-Prozessen erfasst, gescannt und weiterverarbeitet werden.

## Übersicht (Etiketten)

In der Übersicht der Etiketten werden die vorhandenen Layouts in einer Tabelle dargestellt. Die Spalte **Name ** zeigt die jeweilige Bezeichnung des Etiketts, zum Beispiel „EAN“ oder „Test Lagerplatz Barcode“. Unter **Verwenden als ** ist der Einsatzbereich angegeben, etwa artikel_klein, lieferschein_position oder lagerplatz_klein. Die Spalte**Format** gibt die Maße und Abstände des Etiketts in Millimetern an (Breite x Höhe x Abstand). Über das Menü kannst du ein Etikett direkt bearbeiten oder löschen.

## Ein Artikeletikett erstellen (Produkt Etikett)

Mit einem Artikeletikett kannst du deine Produkte eindeutig kennzeichnen – zum Beispiel mit Artikelnummer, Name oder Barcode – und so dafür sorgen, dass sie im Lager, beim Versand und in der Produktion schnell erkannt und fehlerfrei verarbeitet werden.

> **Tipp**
>
> In der Übersicht der Etiketten werden alle vorhandenen Etikettenlayouts aufgelistet. Im Standard ist bereits das „Artikeletikett klein“ angelegt. Weitere Beispiel-Layouts stehen dir ebenfalls zur Verfügung und werden automatisch angezeigt, sobald du ein neues Etikett erstellst.

**Schritte Vorbereitung**: Bevor du startest, stelle sicher, dass:

- ein **Etikettendrucker** in Xentral eingerichtet ist (siehe separate Anleitung),
- die benötigten **Variablen ** (z. B. Artikelnummer, Name, Gewicht, MHD) im Artikel gepflegt sind. ** Schritte**: Neues Etikettenlayout anlegen:

1. Gehe im Menü zu: **Einstellungen > Lager & Logistik > Lager > Etiketten **. Oder über die Smart-Suche: ** Etiketten**.
1. Klicke auf **Etikett erstellen**, um ein neues Layout anzulegen.
1. Vergib einen **Namen** für dein Etikett (z. B. 'Artikeletikett klein').
1. Trage die **Abmessungen** des Etiketts ein, z. B. 30 x 15 mm (Breite x Höhe).
1. Layout definieren: Im Feld XML hinterlegst du den Code für dein Etikett.
1. Wähle die Option für die Verwendung '**Verwenden als **' z.B. '** Artikel klein **', '** Lager klein **' oder '** Etikettendrucker 2-zeilig **' - um festzulegen, dass dieses Etikett z.B. automatisch im ** Wareneingang **oder bei der Erstellung der ** Lagerplätze** gedruckt wird.
1. Klicke auf **Speichern**.

Erklärung der Bausteine:

**<barcode>**: erzeugt einen Barcode aus der Artikelnummer {NUMMER}**<line>**: druckt Text, hier die Artikelnummer und den Artikelnamen in Klartext

> **Anmerkung**
>
> Damit hast du ein eigenes Artikeletikett erstellt, das du flexibel für Wareneingang, Lager oder Versand einsetzen kannst.

## Artikeletikett verwenden **Schritte**:

1. Öffne den gewünschten **Artikel** in Xentral.
1. Wähle das Tab **Etiketten**.
1. Wähle dein neues Layout aus.
1. Drucke das Etikett direkt oder teste es zunächst als **PDF-Download**.

## Einstellungen (Etikettenlayout)

Unter Einstellung der Etiketten kannst du alle relevanten Parameter für deine Etikettenlayouts festlegen – von den allgemeinen Feldern wie Name oder Verwendungszweck, über die XML-Definition für den Aufbau des Layouts, bis hin zu Abmessungen, Positionierungen und den Variablen, mit denen die Etiketten automatisch mit Inhalten aus Xentral befüllt werden.

### Felder (Etikettenlayout)

Die Felder im Etikettenlayout legen Grunddaten wie Name, Verwendungszweck und XML-Definition fest.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Name | Gib deinem Etikettenlayout einen eindeutigen Namen, damit du es später leicht wiederfindest. |
| XML | Hier fügst du den eigentlichen Layout-Code im XML-Format ein. Dieser bestimmt, wie das Etikett aussieht. |
| Bemerkung | Trage hier interne Hinweise oder kurze Notizen ein, z. B. für welchen Zweck das Layout gedacht ist. |
| Verwenden als | Bestimme den Einsatzzweck des Layouts (z. B. Artikel, Lager, Lieferschein), damit Xentral weiß, wann es genutzt werden soll. - *Artikel klein *– Standardetikett für einzelne Artikel, meist mit Barcode und Artikelname.<br>-* Lager klein *– Etikett zur Kennzeichnung von Lagerplätzen, Regalen oder Boxen.<br>-* Etikettendrucker 2-zeilig *– erzeugt zweizeilige Etiketten, z. B. für kurze Beschriftungen.<br>-* Kommissionieraufkleber *– unterstützt den Versandprozess, indem Aufträge oder Positionen beim Kommissionieren markiert werden.<br>-* Seriennummer *– erstellt Etiketten zur eindeutigen Kennzeichnung und Nachverfolgung von Geräten oder Bauteilen mit Seriennummer.<br>-* Lieferschein Position *– druckt Etiketten für einzelne Positionen eines Lieferscheins, z. B. zur einfacheren Zuordnung im Warenausgang.<br>-* Multiorder Picking Artikel *– wird beim Multi-Order-Picking für die Kennzeichnung einzelner Artikel eingesetzt.<br>-* MultiOrder Picking Lieferschein *– dient der Etikettierung von Lieferscheinen im Multi-Order-Picking-Prozess.<br>-* MultiOrder Picking Trenner* – erzeugt Etiketten als Trennmarker, um unterschiedliche Aufträge im Multi-Order-Picking klar voneinander abzugrenzen. |
| Etikett in mm angeben | Lege die Größe des Etiketts in Millimetern fest. Wichtig, damit Drucker und Layout übereinstimmen. |
| Breite / Höhe | Definiert die genauen Abmessungen des Etiketts. Miss dein Etikettenpapier vorher genau aus. |
| Abstand | Der Abstand zwischen mehreren Etiketten auf einem Bogen. Verhindert Überlappungen beim Druck. |
| Offset Links / Oben | Verschiebt den Inhalt des Etiketts nach rechts oder unten. Nützlich, wenn der Drucker nicht exakt mittig druckt. |
| Etiketten pro Zeile | Bestimmt, wie viele Etiketten nebeneinander auf einem Bogen stehen. Wichtig für Etikettenbögen. |
| Textbaustein | Erzeugt eine einfache Textzeile. Du kannst Position (x/y) und Schriftgröße festlegen. |
| Barcode | Erzeugt einen Barcode. Stelle Größe und Typ ein (z. B. Code128, Code39 oder EAN13). |
| QR-Code | Fügt einen QR-Code ein. Praktisch für weiterführende Informationen oder Links. |
| Artikel klein | Vordefiniertes Layout für kleine Artikeletiketten mit Barcode und Artikelname. Kann als Vorlage genutzt werden. |
| Lager klein | Vordefiniertes Layout für Lageretiketten. Hilfreich zur Kennzeichnung von Regalen und Lagerplätzen. |
| EAN13 Barcode | Generiert einen EAN13-Barcode. Achte darauf, dass die Artikelnummer genau 13 Stellen hat. |
| Etikettenbild | Fügt ein Bild (z. B. Produktfoto) in das Etikett ein. Nur mit PDF-Drucker nutzbar. |
| Rechteck | Zeichnet ein Rechteck zur optischen Trennung. Wenn Höhe = 0, wird eine Linie erzeugt. |

#### Variablen Übersicht (Etikettenlayout)

Variablen füllen Etiketten automatisch mit Daten wie Artikelnummer, Name, MHD oder Lagerplatz.

**Allgemeine Variablen**:

| Variable | Beschreibung |
| --- | --- |
| {NUMMER} | Artikelnummer aus Xentral |
| {SERIENNUMMER} | Seriennummer des Artikels |
| {VERKAUFSPREISBRUTTO} | Verkaufspreis inkl. MwSt. |
| {ARTIKEL_NAME_DE} | Artikelname in deutscher Sprache |
| {LAGER_PLATZ_NAME} | Name des Lagerplatzes |
| {LAGER_PLATZ_ID} | ID des Lagerplatzes |
| {CHARGE} | Chargennummer für Rückverfolgung |
| {MHD} | Mindesthaltbarkeitsdatum im engl. Format (YYYY-MM-DD) |
| {MHD2} | Mindesthaltbarkeitsdatum im deutschen Format (DD.MM.YYYY) |
| {MHD3} | Mindesthaltbarkeitsdatum im Format JJMMTT (z. B. für NVE) |
| {BELEGNR} | Belegnummer (z. B. Auftrag, Lieferschein) |
| {BELEGID} | ID des Belegs |
| {BELEGART} | Belegart, z. B. Auftrag oder Lieferschein |
| {PROJEKT} | Projektkennung |
| {PROJEKTNAME} | Projektname |
| {EIGENSCHAFT:NAME} | Eigenschaft des Artikels mit Namen |
| {ETIKETTENBILD} | Artikelbild (nur in PDF nutzbar) |
| {BEZEICHNUNG1}, {BEZEICHNUNG2} | Texte für 2-zeiligen Etikettendruck |

**Variablen für Produktion:**

| Variable | Beschreibung |
| --- | --- |
| {SERIENNUMMER} | Seriennummer im Produktionsprozess |
| {CHARGENNUMMER} | Nummer der Produktionscharge |
| {MHD} | Mindesthaltbarkeitsdatum (engl. Format) |
| {MHD2} | Mindesthaltbarkeitsdatum (deutsches Format) |
| {CHARGEMHDALL} | Kombination aus Charge und MHD |
| {PRUEFER} | Name oder Kürzel des Prüfers |
| {KOMMENTAR} | Kommentar zum Produktionsschritt |
| {ZEITSTEMPEL} | Erstellungsdatum/-zeit des Labels |
| {BELEGNR} | Belegnummer des Produktionsauftrags |

**Variablen für Produktionslabel**

| Variable | Beschreibung |
| --- | --- |
| {BELEGNR} | Belegnummer für das Produktionslabel |
| {KUNDENNAME} | Name des Kunden |
| {KUNDENNUMMER} | Nummer des Kunden |
| {DATUMAUSLIEFERUNG} | Geplantes Auslieferungsdatum |
| {ARTIKELNAME} | Artikelname (Standard) |
| {ARTIKELNUMMER} | Artikelnummer |
| {ARTIKELNUMMERKUNDE} | Artikelnummer des Kunden |
| {MENGE} | Auszugebende Menge |
| {LAGERPLATZ} | Zugeordneter Lagerplatz |
| {CHARGE} | Charge für das Produkt |
| {MHD} | MHD (engl. Format: YYYY-MM-DD) |
| {MHD2} | MHD (deutsches Format: DD.MM.YYYY) |

#### Beispiele für Etikettenbausteine

Etikettenbausteine im XML sind die einzelnen Code-Elemente wie Text, Barcode, QR-Code, Bilder oder Formen, mit denen du den Aufbau und Inhalt eines Etiketts definierst.

> **Anmerkung**
>
> **Hinweis**
>
> Damit hast du alle Grundbausteine:
>
> - **line **= gibt eine einzeilige Textausgabe wieder. Du steuerst die Position über ** x ** (horizontal) und ** y ** (vertikal), beide in Millimetern. Die ** size **definiert die Schriftgröße (üblich: 1–5). Der Textinhalt steht zwischen den Tags: **<line>** TEXT **</line>**. Das kann entweder fester Text oder eine Variable sein. <line x="5" y="10" size="3">Artikel: {NAME_DE}</line>
> - **barcode **= Strichcode. Erzeugt einen maschinell lesbaren Barcode, z. B. für Scanner im Lager, Versand oder Wareneingang. Die Position des Barcodes auf dem Etikett wird über die Koordinaten ** x ** (horizontal) und ** y ** (vertikal) festgelegt, die Höhe über den Wert ** size **. Mit dem Attribut ** type **wird der Barcode-Typ definiert – gängige Werte sind** 1 für Code128 **, ** 2 für Code39 ** und** E30 für EAN13 **. Als Inhalt kann entweder eine feste Zeichenkette oder eine Variable wie {NUMMER} verwendet werden. Die ** Breite ** des Barcodes lässt sich ** ausschließlich **beim ** Typ 1 (Code128)**anpassen. <barcode x="3" y="1" size="8" type="1">{NUMMER}</barcode>
> - **qrcode **= QR-Code. Gibt einen zweidimensionalen QR-Code aus, der sich ideal für weiterführende Informationen, URLs oder verschlüsselte Daten eignet. Die Position des QR-Codes wird über die Werte ** x **und ** y **in Millimetern auf dem Etikett bestimmt. Mit ** size **legst du die Größe des Codes fest – üblich sind Werte zwischen** 1 und 4 **. Der Parameter ** type ** wird meist mit dem Wert ** 3** verwendet, was dem ** Standard-QR-Code** entspricht. Als Inhalt kannst du beispielsweise Produktinformationen, eine Artikelnummer oder eine URL einfügen. <qrcode x="10" y="15" size="3" type="3">https://deinshop.de/{NUMMER}</qrcode>
> - **image **= Bild. Bindet ein Produktbild oder Symbol auf dem Etikett ein. x/y = Position, width/height = Breite und Höhe des Bildes (in mm). Inhalt = Variable {ETIKETTENBILD}, das im Artikel gepflegt wurde. ** Nur bei PDF-Druckern** verwendbar (nicht für Thermodrucker geeignet). <image x="3" y="16" width="36" height="30">{ETIKETTENBILD}</image>
> - **rectangle**= Formen (Linien/Rechtecke). Erzeugt ein Rechteck oder eine Linie, um das Etikett optisch zu strukturieren. x/y = Startpunkt der Form. width/height = Breite und Höhe (in mm). size = Linienstärke. Wenn height = 0, wird eine horizontale Linie erzeugt. Ideal für Rahmen, Trenner oder visuelle Gruppen auf dem Etikett. Bsp. Linie: <rectangle x="3" y="20" width="40" height="0" size="1"/> Bsp. Rechteck: <rectangle x="3" y="1" width="60" height="20" size="1"/>
> - **label**= Container für das gesamte Etikettenlayout. Umschließt den gesamten Etiketteninhalt. Jedes Etikett beginnt mit <label> und endet mit </label>. Alles, was zwischen <label> und </label> steht, gehört zu einem Etikettenlayout. Ein Etikettenbogen mit mehreren Etiketten enthält mehrere label-Abschnitte. <label> <barcode x="3" y="1" size="8" type="1">{NUMMER}</barcode> <line x="3" y="11" size="3">Artikel: {NAME_DE}</line> </label>

##### Textbaustein

```<line x="5" y="1" size="3">Test</line>```

- **line** = erstellt eine Textzeile.
- **x / y** = Position in mm vom linken bzw. oberen Rand.
- **size** = Schriftgröße (1–5, je größer, desto größer die Schrift).
- **Inhalt **= Der Text zwischen den Tags (Test) wird auf das Etikett gedruckt. ** Ergebnis**: Ein einfacher Text „Test“ in mittlerer Schriftgröße, oben links auf dem Etikett.

##### Barcode Code128, Code39, EAN13

```<barcode x="5" y="1" size="3" type="1">Test</barcode>```

- **barcode** = fügt einen Barcode ein.
- **x / y** = Position des Barcodes.
- **size** = Höhe des Barcodes (1–8).
- **type** = Barcode-Typ (z. B. 1 = Code128, 2 = Code39, E30 = EAN13).
- **Inhalt **= Der Wert im Tag (hier Test oder {NUMMER}) wird als Barcode kodiert. ** Ergebnis**: Ein Barcode an der oberen linken Ecke, Größe 3, Typ Code128.

> **Anmerkung**
>
> **Hinweis**
>
> **Typ 1 → entspricht Code128**
>
> - Dieser Barcode-Typ unterstützt alphanumerische Inhalte und kann sowohl gerade als auch ungerade Stellenanzahlen verarbeiten.
> - Nur hier lässt sich im PDF-Druck auch die Breite des Barcodes anpassen (width).
> - In der Praxis ist Typ 1 flexibler und wird am häufigsten eingesetzt.
>
> **Typ 2 → entspricht Code39**
>
> - Hier können nur Artikelnummern mit gerader Stellenanzahl korrekt hinterlegt werden (z. B. 6- oder 8-stellig).
> - Die Breite kann nicht angepasst werden, nur die Höhe.
> - Der Unterschied zu Typ 1 ist sichtbar: Code39 wird „breiter“ dargestellt, daher wirkt der Barcode größer.
>
> **Typ E30 → entspricht EAN13**
>
> - Standardisierter Barcode für den Handel, der genau 13 Ziffern benötigt.
> - Auch hier lässt sich die Breite nicht ändern.
> - EAN13 ist ein international anerkannter Code, der für Produktkennzeichnung im Einzelhandel genutzt wird.

##### QR-Code

```<qrcode x="5" y="1" size="3" type="3">Test</qrcode>```

- **qrcode** = fügt einen QR-Code ein.
- **x / y** = Position des QR-Codes.
- **size** = Größe des QR-Codes (1–4).
- **type** = Variante des QR-Codes, meist 3.
- **Inhalt **= Text oder Variable, die im QR-Code verschlüsselt wird. ** Ergebnis**: Ein QR-Code mit der Info „Test“, der beim Scannen ausgelesen werden kann.

##### EAN13 Barcode

```
<label>
  <barcode x="3" y="1" size="8" type="E30">{EAN}</barcode>
</label>
```

- **type="E30"** = erstellt einen EAN13-Barcode.
- **{EAN}**= Platzhalter für die Artikel-EAN aus Xentral. ** Ergebnis**: Ein Etikett mit einem standardisierten EAN13-Barcode – nutzbar im Handel und bei Scannern im Wareneingang/Versand.

##### Datumsformate (MHD) im Etikettenlayout

Für das Mindesthaltbarkeitsdatum (MHD) kannst du in Etiketten unterschiedliche Datumsformate ausgeben. Dafür stehen drei Variablen zur Verfügung:

- {MHD} – englisches Format (YYYY-MM-DD), z. B. 2022-08-29, besonders für Scanner geeignet
- {MHD2} – deutsches Format (DD.MM.YYYY), z. B. 29.08.2022, zur klaren Anzeige für Endnutzer
- {MHD3} – kompaktes Format (JJMMTT), z. B. 220829, häufig für NVE-/GS1-Codes verwendet

##### IF-Bedingungen

Mit IF-Bedingungen kannst du steuern, ob bestimmte Inhalte auf dem Etikett nur dann ausgegeben werden, wenn die dazugehörige Variable auch wirklich gefüllt ist. Das funktioniert ähnlich wie bei den Textvorlagen.

**Beispiel:**

Das Feld „MHD“ mit dem entsprechenden Datum soll nur erscheinen, wenn tatsächlich ein Mindesthaltbarkeitsdatum hinterlegt ist (z. B. MHD: 23.08.2025).

```{IF}{MHD}{THEN}MHD: {MHD}{ELSE}{ENDIF}```

**Ergebnis**: In diesem Beispiel wird die Zeile „MHD: …“ nur dann aufgedruckt, wenn die Variable {MHD} einen Wert enthält.

##### Etikettenbild

```
<label>
  <image x="3" y="1" size="8" width="10" height="20">{ETIKETTENBILD}</image>
</label>
```

- **image** = fügt ein Bild ein.
- **width / height** = Größe des Bildes in mm.
- **{ETIKETTENBILD}**= Bild, das im Artikel in Xentral hinterlegt ist. ** Ergebnis**: Ein Artikeletikett mit Bild (nur für PDF-Drucker nutzbar, nicht für Thermodrucker).

##### Sonderelemente: Linien und Rechtecke **Rechteck:**

```
<label>
  <rectangle x="3" y="1" width="10" height="20" size="1"></rectangle>
</label>
```

- **rectangle** = erzeugt ein Rechteck.
- **width / height** = Breite und Höhe des Rechtecks.
- **size **= Linienstärke. ** Ergebnis **: Ein Rechteck auf dem Etikett. Wenn height=0, wird statt eines Rechtecks nur eine Linie gezeichnet. ** Linie:**

```<rectangle y="1" x="1" width="122" height="0" size="1"></rectangle>```

Eine Linie erzeugst du, indem du die Höhe (height) des Rechtecks auf 0 setzt. So entsteht eine horizontale Linie in der angegebenen Breite:

##### Mehrzeilige Textausgabe (Multiline)

Ein Multiline-Tag wird verwendet, wenn der Inhalt eines Etiketts zu lang ist, um in eine einzelne Zeile zu passen. Anstatt den Text abzuschneiden, kannst du mit diesem Tag den Inhalt automatisch umbrechen lassen.

```<multiline x="2" y="6" size="2" wrap="50" wrapheight="3">{EAN}</multiline>```

- **multiline** = Gibt den Text mehrzeilig aus.
- **wrap** = Maximale Anzahl an Zeichen pro Zeile, bevor ein Zeilenumbruch erfolgt (hier: 50 Zeichen).
- **wrapheight** = Höhe, um die der Textblock je Zeile nach unten wächst.
- Inhalt = Beliebige Variable oder Text (im Beispiel {EAN}).

**Ergebnis**: Damit kannst du z. B. lange Produktbezeichnungen, Adressen oder zusätzliche Artikelinfos sauber auf mehrere Zeilen verteilen, ohne dass der Text das Layout sprengt.

#### Beispiele für komplette Layouts

Unter Beispiele für komplette Layouts findest du fertige XML-Vorlagen, wie zum Beispiel ein Artikeletikett oder Lageretikett, die dir als Grundlage für eigene Etikettenlayouts dienen können.

##### Artikel klein

```
<label>
  <barcode x="3" y="1" size="8" type="1">{NUMMER}</barcode>
  <line x="3" y="10" size="3">NR {NUMMER}</line>
  <line x="3" y="13" size="3">{NAME_DE}</line>
</label>
```

- **label** = Beginn des Etikettenlayouts.
- **barcode** = Artikelnummer als Barcode ({NUMMER}).
- **line **= Artikelnummer und Artikelname zusätzlich als Text. ** Ergebnis**: Ein kleines Artikeletikett mit Barcode, Artikelnummer und Artikelname. Ideal für Einzelprodukte.

##### Lager klein

```
<label>
  <barcode x="3" y="1" size="8" type="1">{KURZBEZEICHNUNG}</barcode>
  <line x="3" y="10" size="4">Lager: {KURZBEZEICHNUNG}</line>
</label>
```

- **barcode** = erzeugt einen Barcode für die Lagerkurzbezeichnung.
- **line **= zeigt den Text „Lager: …“ mit der Kurzbezeichnung an. ** Ergebnis**: Ein Lageretikett, das sowohl als Barcode als auch als Text die Lagerbezeichnung darstellt. Praktisch für Regale oder Boxen.

##### Etikettenlayout mit Bild

Neben Text- und Barcode-Elementen kannst du in einem Etikettenlayout auch ein Bild aus dem Artikelstamm einbinden. So lassen sich Etiketten optisch ansprechender gestalten oder mit produktrelevanten Bildern ergänzen.

```
<label> 
  <barcode y="1" x="3" size="8" type="2">{NUMMER}</barcode>
  <line x="3" y="10" size="3">NR {NUMMER}</line>
  <line x="3" y="13" size="3">{NAME_DE}</line>
  <image y="16" x="3" size="8" width="36" height="30">{ETIKETTENBILD}</image>
</label>
```

Abmessungen: 50 × 46 mm (Breite × Höhe)

Das Bild wird im Artikel unter Dateien hochgeladen und dort als Etikettenbild markiert. Sobald dies hinterlegt ist, kann es automatisch auf dem Etikett ausgegeben werden.

Die detaillierten Bildeinstellungen im Artikel findest du in den Artikeleinstellungen.

##### Etikettenbogen

Etikettenbogen (z.B. mehrere Etiketten auf einem DIN-A4-Bogen als PDF)

Ein Etikettenbogen ermöglicht es, mehrere einzelne Etiketten in einem Raster auf einem einzigen DIN-A4-Bogen darzustellen und anschließend als PDF auszugeben. Dieses Vorgehen eignet sich insbesondere, wenn du vorgestanzte Bögen mit Etiketten nutzt (z. B. Produktetiketten), sodass beim Druck alle Etiketten auf dem Bogen automatisch richtig positioniert werden.

Im gezeigten Beispiel wird das Grundmuster für einen Etikettenbogen definiert. Dabei werden mehrere Etiketten in Spalten und Reihen nebeneinander gesetzt. Jedes Etikett enthält Barcode, Artikelnummer, Artikelnamen, Kurztext, Zusatztext und ein Haltbarkeitsdatum. Die Positionen der einzelnen Bausteine werden über die x-/y-Koordinaten gesteuert, sodass jedes Etikett genau auf die vorgesehene Stelle des Bogens passt.

```
<label>
  <barcode y="1" x="10" size="8" type="2">{NUMMER}</barcode>
  <line x="10" y="11" size="3">NR {NUMMER}</line>
  <line x="10" y="15" size="5">{NAME_DE}</line>
  <line x="10" y="20" size="3">{KURZTEXT_DE}</line>
  <line x="10" y="26" size="3">{ANABREGS_TEXT}</line>
  <line x="10" y="29" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="10" y="32" size="3">ab Abfülldatum</line>
  <line x="10" y="35" size="4">{DATUM_VERSION5}</line>
  
  <!-- Zweites Etikett rechts daneben -->
  <barcode y="1" x="120" size="8" type="2">{NUMMER}</barcode>
  <line x="120" y="11" size="3">NR {NUMMER}</line>
  <line x="120" y="15" size="5">{NAME_DE}</line>
...
</label>
```

Dieses Muster wird mehrfach wiederholt, um die Etiketten auf dem Bogen zeilenweise anzuordnen (oben links, oben rechts, zweite Zeile links, zweite Zeile rechts usw.).

Abmessungen: 210 × 270 mm (entspricht ungefähr einem DIN-A4-Bogen)

Damit kannst du komplette Bögen mit gleichartigen Etiketten drucken. Praktisch z. B. für Produktetiketten.

**Beispiel für einen ganzen Bogen:**

```
<label>
  <!-- 1. Reihe, links -->
  <barcode y="1" x="10" size="8" type="2">{NUMMER}</barcode>
  <line x="10" y="11" size="3">NR {NUMMER}</line>
  <line x="10" y="15" size="5">{NAME_DE}</line>
  <line x="10" y="20" size="3">{KURZTEXT_DE}</line>
  <line x="10" y="26" size="3">{ANABREGS_TEXT}</line>
  <line x="10" y="29" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="10" y="32" size="3">ab Abfülldatum</line>
  <line x="10" y="35" size="4">{DATUM_VERSION5}</line>

  <!-- 1. Reihe, rechts -->
  <barcode y="1" x="120" size="8" type="2">{NUMMER}</barcode>
  <line x="120" y="11" size="3">NR {NUMMER}</line>
  <line x="120" y="15" size="5">{NAME_DE}</line>
  <line x="120" y="20" size="3">{KURZTEXT_DE}</line>
  <line x="120" y="26" size="3">{ANABREGS_TEXT}</line>
  <line x="120" y="29" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="120" y="32" size="3">ab Abfülldatum</line>
  <line x="120" y="35" size="4">{DATUM_VERSION5}</line>

  <!-- 2. Reihe, links -->
  <barcode y="51" x="10" size="8" type="2">{NUMMER}</barcode>
  <line x="10" y="61" size="3">NR {NUMMER}</line>
  <line x="10" y="75" size="5">{NAME_DE}</line>
  <line x="10" y="80" size="3">{KURZTEXT_DE}</line>
  <line x="10" y="86" size="3">{ANABREGS_TEXT}</line>
  <line x="10" y="89" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="10" y="92" size="3">ab Abfülldatum</line>
  <line x="10" y="95" size="4">{DATUM_VERSION5}</line>

  <!-- 2. Reihe, rechts -->
  <barcode y="51" x="120" size="8" type="2">{NUMMER}</barcode>
  <line x="120" y="61" size="3">NR {NUMMER}</line>
  <line x="120" y="75" size="5">{NAME_DE}</line>
  <line x="120" y="80" size="3">{KURZTEXT_DE}</line>
  <line x="120" y="86" size="3">{ANABREGS_TEXT}</line>
  <line x="120" y="89" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="120" y="92" size="3">ab Abfülldatum</line>
  <line x="120" y="95" size="4">{DATUM_VERSION5}</line>

  <!-- 3. Reihe, links -->
  <barcode y="111" x="10" size="8" type="2">{NUMMER}</barcode>
  <line x="10" y="121" size="3">NR {NUMMER}</line>
  <line x="10" y="135" size="5">{NAME_DE}</line>
  <line x="10" y="140" size="3">{KURZTEXT_DE}</line>
  <line x="10" y="146" size="3">{ANABREGS_TEXT}</line>
  <line x="10" y="149" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="10" y="152" size="3">ab Abfülldatum</line>
  <line x="10" y="155" size="4">{DATUM_VERSION5}</line>

  <!-- 3. Reihe, rechts -->
  <barcode y="111" x="120" size="8" type="2">{NUMMER}</barcode>
  <line x="120" y="121" size="3">NR {NUMMER}</line>
  <line x="120" y="135" size="5">{NAME_DE}</line>
  <line x="120" y="140" size="3">{KURZTEXT_DE}</line>
  <line x="120" y="146" size="3">{ANABREGS_TEXT}</line>
  <line x="120" y="149" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="120" y="152" size="3">ab Abfülldatum</line>
  <line x="120" y="155" size="4">{DATUM_VERSION5}</line>

  <!-- 4. Reihe, links -->
  <barcode y="171" x="10" size="8" type="2">{NUMMER}</barcode>
  <line x="10" y="181" size="3">NR {NUMMER}</line>
  <line x="10" y="195" size="5">{NAME_DE}</line>
  <line x="10" y="200" size="3">{KURZTEXT_DE}</line>
  <line x="10" y="206" size="3">{ANABREGS_TEXT}</line>
  <line x="10" y="209" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="10" y="212" size="3">ab Abfülldatum</line>
  <line x="10" y="215" size="4">{DATUM_VERSION5}</line>

  <!-- 4. Reihe, rechts -->
  <barcode y="171" x="120" size="8" type="2">{NUMMER}</barcode>
  <line x="120" y="181" size="3">NR {NUMMER}</line>
  <line x="120" y="195" size="5">{NAME_DE}</line>
  <line x="120" y="200" size="3">{KURZTEXT_DE}</line>
  <line x="120" y="206" size="3">{ANABREGS_TEXT}</line>
  <line x="120" y="209" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="120" y="212" size="3">ab Abfülldatum</line>
  <line x="120" y="215" size="4">{DATUM_VERSION5}</line>
</label>
```

## Spezielle Etikettenlayouts

xx

### Xentral Freifelder im Artikel-Etikettenlayout

Auf einem Artikeletikett können nicht nur Standardvariablen wie Artikelnummer, Name oder Barcode ausgegeben werden, sondern auch individuell gepflegte Artikelfreifelder.

Dazu wird im Etikettenlayout an der gewünschten Stelle die entsprechende Variable eingefügt, z. B.:

```<line x="3" y="10" size="3">{NUMMER} / {FREIFELD1}</line>```

- {FREIFELD1} steht dabei für den Inhalt des ersten Freifeldes, das im Artikelstammsatz gepflegt wurde.
- Damit ein Freifeld im Etikett erscheint, muss es im Artikel aktiv hinterlegt sein. Falls Freifelder noch nicht sichtbar sind, können sie in den Grundeinstellungen aktiviert werden.
- Sobald ein Freifeld im Artikel gepflegt ist, wird es beim Etikettendruck automatisch mit ausgegeben.

**Beispiel:**

Im Artikel ist das Freifeld 1 mit „Doppelpack“ gefüllt. Auf dem Etikett erscheint dann die Zeile:

```NR 700001 / Doppelpack```

So lassen sich zusätzliche Informationen wie Verpackungseinheiten, interne Hinweise oder spezielle Merkmale flexibel auf Etiketten darstellen.

### Lebensmittel-Etikett

Die folgenden Beispiele zeigen unterschiedliche Varianten von Lebensmitteletiketten, die je nach Anforderung mit Artikelinformationen, Gewicht, Haltbarkeitsdaten und Zusatztexten gestaltet werden können.

#### Lebensmitteletikett

Ein kompaktes Etikett für Lebensmittelprodukte mit Artikelnummer, Name, Gewicht und Zusatztexten.

```
<label>
  <barcode y="1" x="3" size="8" type="2">{NUMMER}</barcode>
  <line x="3" y="13" size="3">NR {NUMMER}</line>
  <line x="3" y="16" size="3">{NAME_DE}</line>
  <line x="3" y="19" size="3">Nettofuellmenge: {GEWICHT} Gramm</line>
  <line x="3" y="24" size="3">{KURZTEXT_DE}</line>
  <line x="3" y="27" size="3">{ANABREGS_TEXT}</line>
</label> 
```

Abmessungen: 65 x 30 mm

#### Lebensmitteletikett mit Datum

Erweitertes Etikett mit zusätzlicher Angabe verschiedener Datumsvarianten für Mindesthaltbarkeit, Produktion oder Abfülldatum.

```
  <label>
  <barcode y="1" x="3" size="8" type="2">{NUMMER}</barcode>
  <line x="3" y="13" size="3">{NUMMER}</line>
  <line x="3" y="16" size="3">{NAME_DE}</line>
  <line x="3" y="19" size="3">Nettofuellmenge: {GEWICHT} Gramm</line>
  <line x="3" y="24" size="3">{KURZTEXT_DE}</line>
  <line x="3" y="27" size="3">{ANABREGS_TEXT}</line>
  <line x="3" y="30" size="3">{DATUM}</line>
  <line x="3" y="33" size="3">{DATUM_VERSION1}</line>
  <line x="3" y="36" size="3">{DATUM_VERSION2}</line>
  <line x="3" y="39" size="3">{DATUM_VERSION3}</line>
  <line x="3" y="42" size="3">{DATUM_VERSION4}</line>
  <line x="3" y="45" size="3">{DATUM_VERSION5}</line>
  <line x="3" y="48" size="3">{DATUM_VERSION6}</line>
  <line x="3" y="51" size="3">{DATUM_VERSION7}</line>
</label> 
```

Abmessungen: 60 x 70 mm

#### Lebensmitteletikett Variante

Eine größere Variante mit stärker hervorgehobenem Artikelnamen und zusätzlichem Haltbarkeitshinweis.

```
<label>
  <barcode y="1" x="3" size="8" type="2">{NUMMER}</barcode>
  <line x="3" y="11" size="3">NR {NUMMER}</line>
  <line x="3" y="15" size="5">{NAME_DE}</line>
  <line x="3" y="20" size="3">{KURZTEXT_DE}</line>
  <line x="3" y="26" size="3">{ANABREGS_TEXT}</line>
  <line x="3" y="29" size="3">Bei 10°C mindestens haltbar bis 6 Monate,</line>
  <line x="3" y="32" size="3">ab Abfülldatum</line>
  <line x="3" y="35" size="4">{DATUM_VERSION5}</line>
</label> 
```

Abmessungen: 70 x 40 mm

### GS-1 Transportlabels

Mit einem GS-1-Transportetikett kennzeichnest du Versand- und Transporteinheiten (z. B. Kartons, Paletten) standardkonform. Es kombiniert menschenlesbare Daten (Absender/Empfänger, GTIN, Menge, MHD, Charge) mit maschinenlesbaren GS1-128-Barcodes (u. a. SSCC/NVE), sodass Waren entlang der Lieferkette eindeutig identifiziert und verfolgt werden können.

Beispiel-Layout (100 × 150 mm):

Das folgende XML erzeugt ein GS-1-Transportetikett im Format Breite 100 mm, Höhe 150 mm. Der Aufbau ist in Inhaltsblöcke gegliedert (Adressen, NVE/SSCC, GTIN, Menge, MHD, Charge) und nutzt unten zwei GS1-128-Barcodes, die über einen Online-Generator im &lt;image&gt;-Tag eingebunden werden:

```
<label>
  <!-- Absender (links oben) -->
  <line x="3" y="3" size="3">Absender</line>
  <line x="3" y="6" size="3">{ABSENDERNAME}</line>
  <line x="3" y="9" size="3">{ABSENDERSTRASSE}</line>
  <line x="3" y="12" size="3">{ABSENDERPLZ}</line>
  <line x="10" y="12" size="3">{ABSENDERORT}</line>

  <!-- Empfänger (rechts oben) -->
  <line x="60" y="3" size="3">Empfänger</line>
  <line x="60" y="6" size="3">{NAME}</line>
  <line x="60" y="9" size="3">{STRASSE}</line>
  <line x="60" y="12" size="3">{PLZ}</line>
  <line x="69" y="12" size="3">{ORT}</line>

  <!-- NVE/SSCC & Produktdaten (mittig) -->
  <line x="3" y="18" size="4">NVE (SSCC)</line>
  <line x="3" y="22" size="5">{NVE}</line>

  <line x="3" y="31" size="4">GTIN</line>
  <line x="3" y="35" size="5">{EAN}</line>

  <line x="80" y="31" size="4">Menge</line>
  <line x="82" y="35" size="5">{MENGE}</line>

  <line x="3" y="47" size="3">MHD</line>
  <line x="3" y="50" size="5">{MHD2}</line>

  <line x="70" y="47" size="3">Charge</line>
  <line x="70" y="50" size="5">{CHARGE}</line>

  <!-- GS1-128 Produkt-/Chargen-Barcode: (01)GTIN (15)MHD (10)Charge -->
  <image x="3" y="70" width="90" height="28"
  src="http://www.keepautomation.com/online_barcode_generator/linear.aspx?TYPE=11&DATA=(01){EAN}(15){MHD3}(10){CHARGE}&PROCESS-TILDE=true&UOM=1&X=0.0495&Y=3.175&ROTATE=0&RESOLUTION=72&FORMAT=png&LEFT-MARGIN=0&RIGHT-MARGIN=0&SHOW-TEXT=true&TEXT-FONT=Arial%7c9%7cRegular"></image>

  <!-- Vertikales 'N V E' Label links neben dem SSCC-Barcode -->
  <line x="3" y="110" size="5">N</line>
  <line x="3" y="115" size="5">V</line>
  <line x="3" y="120" size="5">E</line>

  <!-- GS1-128 SSCC/NVE-Barcode: (00)SSCC -->
  <image x="13" y="100" width="70" height="40"
  src="http://www.keepautomation.com/online_barcode_generator/linear.aspx?TYPE=11&DATA=(00){NVE}&PROCESS-TILDE=true&UOM=1&X=0.0495&Y=3.175&ROTATE=0&RESOLUTION=72&FORMAT=png&LEFT-MARGIN=0&RIGHT-MARGIN=0&SHOW-TEXT=true&TEXT-FONT=Arial%7c9%7cRegular"></image>

  <!-- Layout-Rahmen und Trenner (Grid) -->
  <rectangle y="1" x="1" width="98" height="15" size="1"></rectangle>
  <rectangle y="16" x="1" width="98" height="15" size="1"></rectangle>
  <rectangle y="31" x="1" width="98" height="15" size="1"></rectangle>
  <rectangle y="46" x="1" width="98" height="15" size="1"></rectangle>
  <rectangle y="61" x="1" width="98" height="88" size="1"></rectangle>
</label>
```

**Wesentliche Punkte und Variablen: **

-** Absenderfelder**: {ABSENDERNAME}, {ABSENDERSTRASSE}, {ABSENDERPLZ}, {ABSENDERORT}
- **Empfängerfelder**: {NAME}, {STRASSE}, {PLZ}, {ORT}
- **Identifikatoren/Produktdaten:** {NVE} (SSCC), {EAN} (GTIN), {MENGE}, {MHD2} (MHD in DE-Format), {MHD3} (MHD JJMMTT für Barcode), {CHARGE}
- **Layout-Raster**: Die fünf <rectangle>-Elemente erzeugen Rahmen/Trenner für die Sektionen (Adressen, NVE, GTIN/Menge, MHD/Charge, Barcodes).
- **Größe**: Breite 100 mm, Höhe 150 mm (Transportlabel-Standardgröße im Beispiel).
- **Barcodes (GS1-128, „TYPE=11“): **

-** Produkt-/Chargen-Barcode**: DATA=(01){EAN}(15){MHD3}(10){CHARGE}
  - (01) = GTIN, (15) = MHD (JJMMTT → {MHD3}), (10) = Charge (alphanumerisch, variable Länge).
  - **SSCC/NVE-Barcode**: DATA=(00){NVE}
  - (00) = SSCC/NVE (18-stellig).
  - Beide Barcodes werden als PNG-Bild über <image src="…"> eingebettet (externer Dienst). Vorteile: GS1-128-Kompatibilität ohne lokale Barcode-Schriftarten.

> **Anmerkung**
>
> **Hinweis zu Datumsformaten**: Für die Anzeige wird {MHD2} (DE-Format, z. B. 29.08.2025) genutzt. Für den Barcode verlangt GS1 das kompakte Format JJMMTT, daher {MHD3} (z. B. 250829).
>
> **Hinweis zur Einbindung per URL**: Die <image src="…"> -Lösung nutzt einen Online-Barcode-Generator. Stelle sicher, dass beim Druck Internet-Zugriff verfügbar ist. Alternativ kannst du Barcodes lokal erzeugen und als Bild einbinden.

#### Spezialfelder für „Spedition“

Wenn du zusätzliche Felder aus dem Modul Spedition auf dem Etikett ausgeben willst, fügst du sie in Großschreibung in geschweiften Klammern ein.

Beispiel: Hat das Feld die Bezeichnung „Halbpalette“, verwendest du auf dem Etikett die Variable {HALBPALETTE}.

So erhältst du ein vollständig beschriftetes, GS1-konformes Transportlabel, das sowohl für die manuelle Kontrolle (klar lesbare Texte) als auch für die automatisierte Verarbeitung (GS1-128-Barcodes mit SSCC, GTIN, MHD, Charge) geeignet ist.