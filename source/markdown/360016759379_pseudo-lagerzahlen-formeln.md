Mit den so genannten **Pseudo-Lagerzahlen** kannst du direkt in Xentral flexibel steuern, welche Lagerbestände an deine Online-Shops und Marktplätze gemeldet werden. Die Lagerbestände können dadurch unabhängig vom tatsächlich vorhandenen physikalischen Bestand auf deinen Verkaufsplattformen angezeigt werden. So kannst du Bestandsreserven sichern oder das Kaufverhalten deiner Endkunden durch gezielte Bestandsanzeigen beeinflussen.

Besonders hilfreich sind Pseudo-Lagerzahlen, wenn du auf mehreren Plattformen verkaufst, unterschiedliche Lagerorte nutzt oder separate Projekte für dein B2B- und B2C-Business nutzt. Durch einfach konfigurierbare Regeln und Bedingungen passt du die Bestandsmeldung individuell an. So sorgst du für mehr Kontrolle und vermeidest Überverkäufe.

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in die Pseudo-Lagerzahlen Formeln**
>
> Möchtest du dir innerhalb weniger Minuten einen Überblick über die Funktionen und die Nutzung der Pseudo-Lagerzahlen in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/00fODraHaNk)**

## Typische Anwendungsfälle für Pseudo-Lagerzahlen

Im Folgenden findest du einige praxisnahe Beispiele für die Verwendung von Pseudo-Lagerzahlen:

- Du verkaufst ein besonders stark nachgefragtes Produkt auf mehreren Marktplätzen (z. B. Amazon, eBay und in deinem Shopify-Shop). Das Produkt ist physisch nur im Hauptlager vorhanden. Um zu verhindern, dass es durch parallele Bestellungen auf verschiedenen Plattformen zu Überverkäufen kommt, kannst du eine Pseudo-Lagerzahlen Formel erstellen, die immer eine bestimmte Stückzahl als Reserve zurückhält.
- Du nutzt Shopify als deinen Premium-B2C-Verkaufskanal. Auf Amazon hingegen vertreibst du dein Produkt an ein breites Publikum. Das Produkt ist bei dir in zwei Lagern physisch vorhanden - für den schnellen Amazon-Versand im Hauptlager und für den etwas arbeitsintensiveren Versand an deine Premiumkunden in einem separaten Lager. In diesem Fall macht es Sinn, den kompletten Bestand des Hauptlagers im Shopify-Shop anzuzeigen. Falls der Gesamtbestand des Produkts einen gewissen Sicherheitsbestand unterschreitet, kannst du für Amazon den Bestand des Hauptlagers und des separaten Lagers kombiniert melden. So kannst du bei sinkenden Beständen trotzdem den Versand und die rechtzeitige Nachbestellung des Artikels gewährleisten.
- Neben deinem B2C-Vertrieb über die gängigen Verkaufsplattformen vertreibst du Produkte auch an Geschäfts- und Großkunden (B2B). Für jedes dieser beiden Geschäftsmodelle nutzt du getrennte Bereiche in deinem Lager. Dabei sollen Bestände gezielt nur dem jeweils passenden Kanal zugewiesen werden, z.B. weil du für B2B-Bestellungen ganze Paletten vorhältst, während du im B2C-Shop einzelne Produkte verkaufst. Um diese Trennung abzubilden, erstellst du zwei Regeln: Eine, die den verfügbaren Bestand aus dem B2B-Projektlager meldet und eine weitere für das B2C-Lager. So trennst du deine Bestände klar nach Geschäftsmodellen und reduzierst Fehlbuchungen.

## Pseudo-Lagerzahlen Formeln erstellen

InXentral kannst du Formeln für Pseudo-Lagerzahlen sowohl in den Artikelstammdaten als auch in den Einstellungen der jeweiligen Shop-Schnittstelle hinterlegen. Wo du die Formeln hinterlegst, hängt von deinen Anforderungen ab:

- **In den Artikelstammdaten**: Nutze diese Vorgehensweise, wenn du für bestimmte Artikel abweichende Bestandszahlen auf all deinen Verkaufsplattformen anzeigen möchtest.
- **In den Einstellungen der Shop-Schnittstelle**: Bei dieser Methode schränkst du die Bestandsanzeige pro Shop-Schnittstelle ein. Die eingetragene Formel wird dann auf alle Produkte angewendet, die über den jeweiligen Shop zum Verkauf angeboten werden.

> **Wichtig**
>
> InXentral hinterlegte Pseudo-Lagerzahlen Formeln werden in folgender Reihenfolge geprüft und abgearbeitet:
>
> - Es existierenFormeln in den Artikelstammdaten: Die Formeln werden angewendet, weitere Formeln werden nicht beachtet.
> - Es existierenFormeln in den Einstellungen der Shop-Schnittstelle: Die Formeln werden angewendet, weitere Formeln werden nicht beachtet (auch, wenn Formeln in den Artikelstammdaten hinterlegt sind).
> - Weder in den Artikelstammdaten noch in der Shop-Schnittstelle sind Formeln hinterlegt: In diesem Fall wird logischerweise auch keine Formel angewandt, sondern der Lagerbestand (abzüglich Reservierungen und offener Aufträge) wird als verfügbare Menge angezeigt. AnmerkungBeachte, dass die Option **Auto-Reservierung im Lager ** in den Projekteinstellugnen unter**Tab: Logistik / Versand > Bereich: Optionen** aktiviert sein muss, damit Xentral die benötigten Bestände für offene Aufträge bereits im Lager reserviert.

### Pseudo-Lagerzahlen Formeln in den Artikelstammdaten hinterlegen

Gehe wie folgt vor, um Formeln für die Meldung von Pseudo-Lagerzahlen an einen Online-Shop zu hinterlegen.

> **Anmerkung**
>
> Beachte, dass bei dieser Vorgehensweise die Formeln nur für die Bestandsanzeige dieses spezifischen Artikels gelten. Weitere Artikel, die du im selben Online-Shop verkaufst, bleiben davon unberührt. Wenn du Pseudo-Lagerzahlen für alle auf einer Verkaufsplattform gelisteten Artikel nutzen möchtest, musst du wie weiter unten im KapitelPseudo-Lagerzahlen Formeln in der Shop-Schnittstelle hinterlegenbeschrieben vorgehen.

1. Öffne das Menü **Verkaufen > Artikel**.
1. Öffne den gewünschten Artikel, indem du rechts auf das **Stift-Symbol** klickst.
1. Klicke auf **Online-Shop Optionen**.
1. Scrolle nach unten, bis du den Bereich **Lagerbestand** erreichst.
1. Gib im Feld **Pseudo Lagerzahl** die Formel(n) ein, anhand derer die Bestandszahlen berechnet und anschließend an deinen Online-Shop übermittelt werden sollen.
1. Klicke auf **Speichern**.

### Pseudo-Lagerzahlen Formeln in der Shop-Schnittstelle hinterlegen

Wenn du Pseudo-Lagerzahlen pro Online-Shop übermitteln möchtest, gibst du die Formeln direkt in den Einstellungen der Shop-Schnittstelle ein. Im folgenden Beispiel legen wir Pseudo-Lagerzahlen für den Marktplatz **Shopify** an.

> **Wichtig**
>
> Beachte, dass bei dieser Vorgehensweise die Formeln für **alle Artikel** gilt, die auf diesem Online-Shop gelistet werden.Individuell am Artikel hinterlegte Formelnwerden also nicht mehr berücksichtigt, sobald du Pseudo-Lagerzahlen Formeln in den Einstellungen der Shop-Schnittstelle hinterlegt hast!

1. Öffne das Menü **Einstellungen > Verkaufen > Shops / Marktplätze > Shops & Marktplätze Übersicht**.
1. Klicke auf den Eintrag des Shops, für den du Pseudo-Lagerzahlen einrichten möchtest. In diesem Beispiel ist das der Eintrag **Shopify**.
1. Klicke auf **Einstellungen**.
1. Scrolle nach unten, bis du den Bereich **Artikel Import / Export** erreichst.
1. Gib im Feld **Pseudolager Regeln** die Formel(n) ein, anhand derer die Bestandszahlen berechnet und anschließend an den Online-Shop übermittelt werden sollen.
1. Klicke auf **Speichern**.

## Formeln für Pseudo-Lagerzahlen aufbauen

> **Warnung**
>
> Beachte folgende Regeln und Einschränkungen beim Aufbau deiner Formeln:
>
> - Die Verwendung von Klammern ist **nicht zulässig**.
> - Vor und nachallen Operatorenmuss bei dir immer ein Leerzeichen stehen, damit die Zeichenkette nicht fälschlicherweise als Lagerplatz interpretiert wird.
> - Du kannst beliebig viele Formeln nacheinander angeben. Als Trennzeichen benutzt du ein Semikolon (**;**).
> - Bei Eingabe mehrerer Formeln werden die Formeln von oben nach unten geprüft und berücksichtigt. Achte also auf die Reihenfolge, in der du die Formeln eingibst.
> - Um Bedingungen abzubilden, gibst du zuerst den WENN-Teil ein, dann ein Pipe-Zeichen (**|**) und dann den DANN-Teil.
> - Formeln, die du in der Shop-Schnittstelle eingibst, dürfen nicht auf **0** enden.

Schauen wir uns zunächst folgendes Beispiel an, um zu sehen, wie du Formeln für Lagerzahlen aufbaust.

```
LP_HL001A - OFFEN > 10 AND L_Hauptlager > 20 | L_Hauptlager; 
LP_HL001B - RES > 10 | LP_HL001B; 
5 
```

In diesem Beispiel gibt es drei Formeln, die durch ein Semikolon (**; **) getrennt sind. Das Pipe-Zeichen (**|**) bewirkt, dass die Zeichenfolge vor dem Zeichen als Bedingung und der Wert danach als Formel verwendet wird, sobald die Bedingung zutrifft.

| Formel | Erläuterung |
| --- | --- |
| LP_HL001A - OFFEN > 10 AND L_Hauptlager > 20 \| L_Hauptlager; | **WENN ** der Bestand auf Lagerplatz HL001A abzüglich aller offenen Aufträge größer 10 ist **UND ** gleichzeitig der Bestand am Hauptlager größer als 20 ist, **DANN** wird der gesamte Bestand des Hauptlagers gemeldet. |
| LP_HL001B - RES > 10 \| LP_HL001B; | **WENN ** der Bestand auf Lagerplatz HL001B abzüglich aller reservierten Artikel größer als 10 ist, **DANN** wird der gesamte Lagerbestand des Lagerplatzes LP_HL001B gemeldet. |
| 5 | Treffen die beiden vorherigen Bedingungen **nicht zu **, wird ein statischer Bestand von** 5** gemeldet. |

### Beispiel: Feste Bestände melden

- Melde immer nur einen statischen Bestand von 100 Exemplaren:

### Beispiel: Einschränkung auf Lager oder Lagerplatz

- Melde nur im Hauptlager vorhandene Bestände:
- Melde nur Bestände eines bestimmten Lagerplatzes (in diesem Beispiel Lagerplatz **HL001A**):

### Beispiel: Einschränkung auf Projekt oder Lager

Dieses Beispiel ist hilfreich, wenn du deine Lagerbestände je nach Projekt unterschiedlich angeben möchtest. Das kann erforderlich sein, wenn du über verschiedene Online-Shops verkaufst und auf jeder dieser Plattformen unterschiedliche Bestandsinformationen anzeigen möchtest.

- Melde nur Bestände, die im Rahmen des Shopify-Projekts reserviert sind:
- Melde nur Bestände, die im Rahmen des Projekts **B2C** verfügbar, also nicht für aktuelle Aufträge reserviert sind:
- Melde nur Bestände, die im Hauptlager reserviert sind:
- Melde nur Bestände, die im Hauptlager verfügbar, also nicht reserviert sind:

### Beispiel: Verwendung von Bedingungen

Stelle dir folgenden Anwendungsfall vor: Wenn im Hauptlager ein Bestand von mehr als 200 Stück vorhanden sind, soll der Bestand des Hauptlagers gemeldet werden. Für den Fall, dass die Bedingung (mehr als 200 Stück)**nicht** erfüllt ist, soll der Bestand des Hauptlagers und der Bestand des Nachschublagerplatzes gemeldet werden.

Die entsprechende Formel ist wie folgt aufgebaut:

```L:Hauptlager > 200 | L:Hauptlager; L:Nachschublagerplatz + L:Hauptlager```

Hierbei trennt das Semikolon die beiden zurückzumeldenden Werte der voran gestellten Bedingung, vergleichbar mit

- **WENN** Hauptlager > 200
- **DANN** Hauptlager
- **SONST** Hauptlager und Nachschublagerplatz

### Verfügbare Variablen und Operatoren für Pseudo-Lagerzahlen Formeln

Folgende Variablen kannst du in Pseudo-Lagerzahlen Formeln verwenden:

| Variable(n) | Erläuterung |
| --- | --- |
| **RES ** oder **RESERVIERT** | Bestand, der bereits für Aufträge reserviert ist |
| **OFFEN** | Bestand, der in offenen Aufträgen enthalten ist |
| **LP_Kurzbezeichnung ** oder **LP:Kurzbezeichnung** | Lagerplatz |
| **L_Bezeichnung ** oder **L:Bezeichnung** | Lager |
| **PR:Projektkennung** | Projekt |
| **RES:PR:Projektkennung** | Bestand, der bereits für Aufträge eines bestimmten Projekts reserviert ist |

Folgende Operatoren kannst du in Pseudo-Lagerzahlen verwenden:

- AND
- OR
- <
- >
- <=
- >=
- "="
- <> bzw.!=
- "+"
- "-"