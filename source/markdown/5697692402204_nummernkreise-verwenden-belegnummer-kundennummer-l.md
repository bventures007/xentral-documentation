Für die Erstellung von Belegen ist es erforderlich, dass jeder Beleg eine eindeutige, fortlaufende und identifizierbare Nummer hat. Dies erreichst du über Nummernkreise. Zusätzlich definierst du Nummernkreise für Kundennummern, Lieferantennummern, Mitarbeiternummern und Artikelnummern.

Die Nummern deiner Belege und Datensätze werden fortlaufend ab der ersten von dir festgelegten Nummer vergeben.

> **Anmerkung**
>
> **Hinweis**
>
> In diesem Artikel findest du neben allgemeine Überlegungen und Tips auch weiterführende Artikel zu folgenden Kategorien:
>
> - Kunden- und Lieferantennummern (Debitoren, Kreditoren)
> - Belegnummern (Dokumente wie Rechnung, Auftrag, Angebot)
> - Artikelnummern (Sortiment und Artikelkategorien)

## Was ist ein Nummernkreis?

Ein Nummernkreis in einem ERP-System bezieht sich auf eine vordefinierte Sequenz oder Reihe von Nummern, die für die eindeutige Identifizierung verschiedener Geschäftsobjekte wie Belege, Bestellungen, Kunden, Lieferanten und andere Datensätze verwendet wird. Nummernkreise sind essentiell für die Organisation, das Tracking und die Verwaltung von Daten innerhalb des ERP-Systems, da sie eine systematische und konsistente Vergabe von Kennungen ermöglichen.

**Wichtige Aspekte eines Nummernkreises: **

-** Einzigartigkeit**: Jede Nummer in einem Nummernkreis ist einzigartig und wird genau einem Datensatz zugeordnet. Dies verhindert Verwechslungen und Dopplungen.
- **Sequenzialität**: Die Nummern innerhalb eines Nummernkreises folgen einer bestimmten Sequenz, die aufsteigend, absteigend oder basierend auf spezifischen Regeln definiert sein kann.
- **Anpassbarkeit**: ERP-Systeme erlauben oft die Anpassung von Nummernkreisen an die spezifischen Anforderungen des Unternehmens. Dies umfasst die Definition des Startwerts, des Endwerts, des Inkrements und des Formats der Nummern. Automatisierung: Die Vergabe von Nummern aus einem Nummernkreis erfolgt typischerweise automatisch durch das System, was manuelle Fehler reduziert und die Effizienz steigert.
- **Organisatorische Struktur**: Nummernkreise können so konfiguriert werden, dass sie die organisatorische Struktur eines Unternehmens widerspiegeln, indem beispielsweise unterschiedliche Sequenzen für verschiedene Abteilungen, Standorte oder Geschäftsbereiche verwendet werden.
- **Rechtliche und operative Anforderungen**: In einigen Fällen erfüllen Nummernkreise auch rechtliche Anforderungen, wie z.B. die fortlaufende Nummerierung von Rechnungen für steuerliche Zwecke.

> **Anmerkung**
>
> Nummernkreise spielen eine zentrale Rolle in der Datenintegrität und -organisation innerhalb von ERP-Systemen und sind ein grundlegendes Werkzeug für effizientes Datenmanagement und -analyse.

## Überlegungen zu Dokumenten- und Artikelnummernkreisen

Dein **Geschäftsmodell **, die ** Größe deiner Firma **, ** Wachstumspläne ** und die **Integration von Drittsystemen ** wie Shops, Marktplätzen oder **Steuerbüros** beeinflussen oft die Wahl der Nummernkreise in deinem ERP-System. Idealerweise findest du eine gute Möglichkeit für das aktuelle Setup deiner Firma, die dir ausreichend Flexibilität und auch Kontinuität für die nahe und weitere Zukunft bietet.

Hier einige Faktoren, die eine Rolle spielen könnten:

- **B2C-Geschäftsmodell**: Ein B2C-Geschäftsmodell mit vielen Kanälen und Abhängigkeiten zu Drittsystemen, die verschiedene Nummern und Zuordnungen voraussetzen.
- **Gemischtes Geschäftsmodell**: B2C-Auftragsvolumen gemischt mit hochpreisigen B2B-Lieferungen an Kunden, die andere Dokumenten- und Debitorennummern erfordern als dein B2C-Kanal.
- **Firmenwachstum**: Dein eigenes Firmenwachstum, das deine Nummernkreise vor allem in der Steuersoftware an Grenzen oder Limitierungen bringen kann.
- **Zukunftsplanung**: Die Abschätzung, wie sich dein Unternehmen und dein Team in den kommenden Monaten und Jahren entwickeln wird.
- **Vorhandene Struktur**: Eine bereits existierende Nummernstruktur, die du ersetzen oder in eine neue Struktur überführen möchtest.

Kriterien für die Nummernvergabe in deinem Geschäftsmodell können sein:

- **Arbeitsablauf**: Tägliche Handhabung im Arbeitsablauf für Waren und Team mit Artikelnummern und Dokumentennummern.
- **Nummernkreis-Längen**: Ausreichende Nummernkreis-Längen für die nächsten 18 Monate in Dokumentennummern.
- **Datenstruktur**: Saubere Strukturierung deiner Daten, die du später analysieren willst.
- **Steueranforderungen**: Monatliche Anforderungen für dein Steuerbüro, einschließlich Debitoren-, Kreditoren- und Dokumentennummern.

> **Anmerkung**
>
> Konzentriere dich auf die wichtigsten Aspekte. Es ist oft nicht möglich, alle Anforderungen zu erfüllen, was bedeutet, dass Kompromisse notwendig sein können. Beispielsweise könnte es erforderlich sein, Abstriche beim Datenimport zu machen, um eine neue Struktur zu unterstützen, oder Abhängigkeiten mit Drittsystemen zu klären. In der Regel lässt sich eine Lösung finden, die die wichtigsten Kriterien berücksichtigt.

### Nummernkreise zum Jahreswechsel

Bei der Auswahl deiner Nummernkreise solltest du an den nächsten Jahreswechsel denken und entscheiden, wie du die Nummern diesbezüglich handhaben willst. Nummernkreise in Xentralzählen automatisch die letzte Ziffernfolge nach oben und sind fortlaufend. Zum Jahreswechsel werden die Nummernkreise jedoch nicht automatisch zurückgesetzt. Du kannst ausreichend große Nummernkreise - z.B. sechsstellige Belegnummernkreise - über den Jahreswechsel fortlaufen lassen. Oder du wählst eine Variable für das Jahr, die sich automatisch über den Jahreswechsel anpasst. Beachte dabei, dass die fortlaufende Nummer nicht automatisch zurückgesetzt wird. Du musst dies am 1. Januar manuell einstellen, bevor das neue Jahr beginnt.

### Abhängigkeiten der Xentral Nummern mit Drittsystemen

#### Nummernkreise: DATEV

Du kannst für DATEV die Kunden- und Lieferantennummer aus Xentral verwenden, ohne eine abweichende Debitoren- und Kreditorennummer in Xentral zu pflegen. DATEV erwartet hier je nach Einstellungen und Kontenrahmen fünf- bis neunstellige Nummern.

> **Anmerkung**
>
> **Hinweis**
>
> Hier einige Tipps für die Verwendung von Nummernkreisen mit DATEV:
>
> - Verwende keine Buchstaben oder andere Variablen in deinen Kunden- oder Lieferantennummern
> - Nutze ausschließlich die gleiche Anzahl von Ziffern für Kunden- und Lieferantennummern.
> - Wähle die Nummernkreise gemäß den DATEV-Vorgaben und kläre dies mit deinem Steuerbüro ab (z.B. SKR04 mit fünfstelligen Debitoren- und Kreditorennummern: Debitoren von 10000 bis 69999, Kreditoren von 70000 bis 99999)
>
> **Beispiel SKR04:**
>
> - Debitoren (Kunden) 10000–69999: Debitorenkonten werden in diesem Bereich geführt.
> - Kreditoren (Lieferanten) 70000–99999: Kreditorenkonten werden in diesem Bereich geführt.
>
> **Beispiel B2C und B2B:**
>
> Im SKR04 können B2B- und B2C-Kunden durch getrennte Nummernkreise klar voneinander abgegrenzt werden: Beispielsweise könnten B2B-Kunden die Nummern 10000–19999 erhalten, wie ein Großhändler für Elektronik (10001) oder ein Maschinenbauunternehmen (10002), während B2C-Kunden die Nummern 20000–69999 nutzen, wie ein Privatkunde aus dem Online-Shop (20001) oder ein Einzelkunde im stationären Handel (20123). Diese Unterteilung schafft Übersichtlichkeit, erleichtert das Reporting, sichert die Revisionssicherheit und bietet ausreichend Raum, um das höhere Kundenaufkommen im B2C-Bereich zu bewältigen.

### Achtung **Sachkonten ** auf z.B. 8 Stellen **verlängern**:

Wenn Sachkonten in DATEV auf 8 Stellen erweitert werden, verlängern sich Personenkonten automatisch auf 9 Stellen. Eine separate Anpassung der Personenkonten ist nicht möglich.

**Wichtige Hinweise:**

- Nachträgliche Änderungen sind aufwendig und nur zu Beginn eines neuen Wirtschaftsjahres möglich.
- Bestehende Buchungen und Nummernkreise beachten.
- Schnittstellen und Exporte müssen angepasst werden.
- Lohnbuchhaltung Module auf Kompatibilität prüfen.

**Für eine reibungslose Umstellung empfiehlt sich eine Absprache mit dem Steuerberater oder DATEV-Support.** Evtl. gibt es andere besser geeignete Möglichkeiten. S.u. Strategien zur Verlängerung von Nummernkreisen.

#### Nummernkreise: Shops

Kundenbestellungen aus deinem Online-Shop werden beim Import nach Xentral automatisch in Aufträge mit eigenen Xentral-Auftragsnummern umgewandelt. Die Shop Bestellnummer kannst du in der Schnell-Vorschau des Auftrags einsehen oder über die Suche in der Auftragsübersicht finden. Deine Shop-Bestellnummer wird beispielsweise auch für die Zuordnung von Zahlungen verwendet.

Artikelnummern werden entweder über Datenimporte nach Xentral importiert, von deinem Team manuell im Artikelbereich angelegt oder über Shop-Bestellungen nach Xentralübertragen. Wenn du verschiedene Shops und Plattformen mit unterschiedlichen Artikelnummern/SKUs verwendest, erfolgt die Zuordnung über Fremdnummern.

## Nummernkreise erweitern: Strategien für hohe Kundenzahlen und Belegvolumen

Wenn die Nummernkreise für Debitoren, Kreditoren oder Belege überlaufen, weil z. B. im B2C-Bereich viele Kunden generiert werden, gibt es verschiedene Strategien, um das Problem zu lösen. Hier sind einige Möglichkeiten:

1. **Erweiterung der Nummernkreise: **

1.** Nutzung alphanumerischer Nummern: **

1.** Nummernkreise nach Jahr trennen: **

1.** Kundengruppen in separate Nummernkreise aufteilen: **

1.** Prüfung, ob alle Debitoren erforderlich sind: **

1.** Kombination mehrerer Strategien:**

## Nummernkreise für Kunden, Belege und Artikel – Überblick & Links

Eine klare Struktur für Kunden- und Lieferantennummern, Belegnummern und Artikelnummern erleichtert dir den Arbeitsalltag, hilft dir, Daten schnell zu finden, Berichte präzise zu erstellen und Abläufe wie Buchhaltung oder Lagerverwaltung reibungslos zu gestalten.

### Kunden- und Lieferantennummern (Debitoren, Kreditoren)

Die Vergabe von Kunden- und Lieferantennummern ist essenziell für die klare Zuordnung und Verwaltung deiner Stammdaten. Debitorennummern (Kunden) und Kreditorennummern (Lieferanten) sollten so gestaltet sein, dass sie deine internen Workflows unterstützen und für dein Team leicht nachvollziehbar sind. Eine durchdachte Struktur hilft dir, Kunden- und Lieferantendaten schnell zu finden, Berichte effizient zu erstellen und Anforderungen deines Steuerbüros zu erfüllen.

> **Anmerkung**
>
> **Hinweis**
>
> **Weiterführende Links:**
>
> - In diesem Artikel: Tipps für die Verwendung von Nummernkreisen mit DATEV:Nummernkreise: DATEV.

### Belegnummern (Dokumente wie Rechnung, Auftrag, Angebot)

Belegnummern bilden die Grundlage für die Nachvollziehbarkeit deiner Geschäftsprozesse und die rechtliche Absicherung deiner Dokumente. Sie dienen der eindeutigen Identifizierung von Angeboten, Aufträgen, Rechnungen, Gutschriften, Lieferscheinen und weiteren Belegen. Eine klare und konsistente Nummernstruktur erleichtert nicht nur den täglichen Workflow, sondern ist auch unverzichtbar für Buchhaltung, Archivierung und Steuerprüfung.

> **Anmerkung**
>
> **Hinweis**
>
> **Weiterführende Links:**
>
> - In diesem Artikel:XentralStandard Nummernkreise

### Artikelnummern (Sortiment und Artikelkategorien)

Eine durchdachte Artikelnummerierung ist der Schlüssel für die effiziente Verwaltung deines Sortiments. Artikelnummern sollten nicht nur eindeutig sein, sondern auch deine internen Prozesse und die Logistik optimal unterstützen. Egal, ob du mit Artikelkategorien arbeitest oder individuelle Artikelnummern vergibst – die richtige Struktur hilft dir, Bestände zu verwalten, Analysen durchzuführen und Fehler in der Abwicklung zu vermeiden.

> **Anmerkung**
>
> **Hinweis**
>
> **Weiterführende Links:**
>
> - Artikelnummern und Artikelkategorien und deren Bedeutung für dein Sortiment:Artikelnummernkreis und SKU (Stock Keeping Unit) (Xentral Artikelkategorien)
> - Zuordnung der Nummern zu Drittsystemen z.B. Shops:Artikel aus Fremdsystemen in Xentral zuordnen - Artikel FremdnummernundArtikelbaum.

## Projektbezogene Nummernkreise

Wenn dir der zentrale Nummernkreis für dein XentralSystem nicht ausreicht, kannst du für einzelne Vertriebskanäle neue Nummernkreise definieren. Ein Grund kann z.B. sein, dass dein Online-Shop ein sehr großes Auftragsvolumen liefert und der zentrale Nummernkreis in Xentral, den du für die B2B Kunden angelegt hast, dafür nicht ausreicht. In diesem Fall kannst du für einen oder mehrere Vertriebskanäle (= ein Projekt) einen eigenen separaten Nummernkreis anlegen.

> **Anmerkung**
>
> Überlege, ob du diese zusätzliche Komplexität im System wirklich brauchst, oder es sich um eher eine optische Unterscheidung handelt, die du auch auf anderem Wege erreichen kannst (z.B. indem du nach Projekten filterst oder einen Report in Xentral anlegst).

Gründe für einen eigenen Projektbezogenen Nummernkreis können sein:

- Der Systemweite Xentral Nummernkreis reicht für einen einzelnen Vertriebskanal nicht aus.
- Du möchtest B2B und B2C steuerrechtlich trennen.
- Du hast Vertriebskanäle in anderen Ländern und möchtest die Nummernkreise für ein Projekt kennzeichnen.

Du kannst projektspezifische Nummernkreise folgendermaßen definieren:

1. Navigiere zu **Stammdaten > Projekt**.
1. Öffne das gewünschte Projekt durch einen Klick darauf.
1. Wechsle zum Tab **Einstellungen ** und dann zum Untertab **Eigene Nummernkreise**.
1. Setze ein Häkchen bei **Eigene Nummernkreise**.
1. Klicke auf den **Speichern**.
1. Passen den gewünschten Nummernkreis mit einem Klick auf **bearbeiten** an.

> **Warnung**
>
> Wenn du projektbezogene Nummernkreise nutzt, empfehlen wir dringend, eindeutige Nummernkreise für jede Belegart anzulegen. Wenn du für eine bestimmte Belegart keinen Nummernkreis definierst, beginnt das System mit der Zählung ab 1. Dies kann zu Konflikten führen, wenn die Nummern mit denen aus dem allgemeinen Nummernkreis übereinstimmen.

Weitere Informationen zum Thema Projekte findest du[hier](https://help.xentral.com/hc/de/articles/360020356760#UUID-10d13e5f-6834-7413-3e87-faa523e90735).

## Nummernkreise vor dem Xentral Go-Live definieren

Wenn du Xentral in deinem Unternehmen einführen möchtest, ist es wichtig, die Nummernkreise im Vorfeld korrekt einzurichten.Xentral liefert standardmäßig vorkonfigurierte Nummernkreise, die an den SKR04 angepasst sind und für mittelgroße Unternehmen geeignet sind.

### Xentral Standard Nummernkreise

In der Standardkonfiguration sind die Nummernkreise so eingestellt, dass die Nummernkreise für verschiedene Belegtypen wie Angebot, Auftrag, Rechnung, Gutschrift, etc. Platz für hunderttausend Belege bieten, bevor der Nummerkreis “voll” ist. Für die meisten Unternehmen im B2B-Segment oder mit gemischten Geschäftsmodellen (B2B + B2C) mit mittlerem Shop- und Plattformvolumen ist dies für mehrere Jahre ausreichend.

Sollte die Stellenanzahl der Belege Stand heute bei dir für das kommende Jahr nicht ausreichen, kannst du darüber nachdenken, ob du die Nummern mit weiteren Nullen nach hinten verlängern willst. Das würde dir die (vollständige) Nummernkreise-Anpassung zum Jahreswechsel ersparen.

Vorkonfigurierter Nummernkreis in Xentral(Beispiel für die wichtigsten Belege)

- Angebotsnummer: 100000
- Auftragsnummer: 200000
- Lieferscheinnummer: 300000
- Rechnungsnummer: 400000
- Gutschriftennummer: 900000
- Bestellnummer: 100000
- Kundennummer: 10000
- Lieferantennummer: 70000
- Mitarbeiternummer: 90000
- Artikelnummer: 1000000

> **Anmerkung**
>
> Die Standard-Einstellungen in Xentral bieten einige Vorteile:
>
> - **Keine Überschneidungen in den Nummernkreisen**: Kunden (Debitoren) und Lieferanten (Kreditoren) haben separate Nummernkreise: - 10.000-69.999 (Kundennummern) - 70.000-99.999 (Lieferantennummern)
> - **Schnelle Identifikation von Belegen**: Belege können schnell anhand der ersten Ziffer identifiziert werden und haben alle die gleiche Anzahl an Stellen. Rechnungs- und Gutschriftsnummern sind systemweit eindeutig identifizierbar.
> - **Kompatibilität mit SKR04 in DATEV**: Die Nummernkreise sind an den SKR04-Kontenrahmen in Datev angepasst, was die Zusammenarbeit mit dem Steuerbüro erleichtert.

### Nummernkreise in den Systemeinstellungen vergeben

Schritte um den Standard Nummernkreis zu ändern:

1. Navigiere zu **Administration > System > Grundeinstellungen > Reiter Einstellungen >** Untergeordneter Reiter ** Nummernkreise**.
1. Klicke auf **bearbeiten** neben der gewünschten Nummer und vergib eine neue “nächste” Nummer.
1. Klicke auf **OK** zur Bestätigung.
1. Wiederhole diese Schritte für alle Nummernkreise, die du ändern möchtest.

> **Warnung**
>
> Vermeide doppelte Nummernkreise. Stelle sicher, dass es keine Überschneidungen zwischen den neuen und bisher vergebenen Nummern gibt. Die aktuelle Nummer wird dir angezeigt.
>
> Wenn du deinen Nummernkreis vergrößern möchtest, kannst du an die letzten Stellen weitere Nullen anhängen.

> **Anmerkung**
>
> Beim Definieren eines Nummernkreises gilt Folgendes:
>
> - Die Nummernkreise müssen unterschiedlich sein und dürfen sich **nicht** überschneiden. z.B. Kunden: 100000 und Lieferanten: 700000 (SKR04).
> - Du kannst Buchstaben in Dokumentennummern verwenden. Achte darauf, dass am Ende eine fortlaufende Nummer steht z.B. 10000 (Xentralzählt nur die letzte Nummer fortlaufend nach oben. Ausnahme sind natürlich Variablen).
> - Die Anzahl der Stellen (Zeichen) sollte sich nicht ändern (nicht bei 1 anfangen sondern z.B. 100001).
> - Verwende die gleiche Anzahl von Stellen für Lieferanten- und Kundennummern. Idealerweise sollten die Nummern 5, 6 oder 7 Stellen lang sein und keine Buchstaben enthalten, um für den Export in dein Buchhaltungssystem geeignet zu sein.
> - Verwende keine Sonderzeichen wie Leerzeichen, Punkte, Kommas, Doppelpunkte, Semikolons und Umlaute.
> - Projektspezifische Nummernkreise dürfen nicht identisch sein. Du kannst sie durch einen Buchstaben oder Zahlenkennung am Anfang kennzeichnen (z.B. AZ100000 oder 321000000, 111000000, etc.).

![2558558379.png](https://help.xentral.com/hc/article_attachments/9365501177500)

### Xentral Nummernkreisformate - Variablen

Wenn du in deinen Dokumentennummern zusätzlich das Jahr automatisch mit angeben willst, kannst du dafür eine Variable vergeben.

> **Anmerkung**
>
> Möchtest du vor deine fortlaufende Dokumentennummer das Jahr einfügen, kannst du beispielsweise folgendes Format verwenden:
>
> - **{JAHR}-100000** liefert dir Dokumentennummern 2023-100000, 2023-100001, …, 2023-199999. Beim Jahreswechsel aktualisiert sich das Jahr automatisch.
>
> Achtung: Die fortlaufende Nummer wird nicht automatisch auf 100000 zurück gesetzt. Das kannst du direkt am 1. Januar manuell vornehmen, um wieder mit dem vollem Nummernkreis zu starten.

Diese Variablen stehen dir in Xentral zur Verfügung:

- **{JAHR}** → Variable für das Jahr
- **{MONAT}** → Variable für den Monat
- **{TAG}** → Variable für den aktuellen Tag
- **{KW}** → Variable für die aktuelle Kalenderwoche
- **{ADRESSE_}**→ Beleg-Adressinhalte, z.B. **{ADRESSE_LAND}, {ADRESSE_KUNDENNUMMER}, {ADRESSE_FREIFELD1}**. Xentral greift hier auf die Adresstabelle und die Feldbezeichnung zurück.

> **Anmerkung**
>
> Diese Datumsformate werden oft im B2B-Bereich verwendet, um hochpreisige Artikel eindeutig zuzuordnen. Im B2C-Bereich mit hohem Durchsatz empfiehlt es sich, längere Dokumentennummern oder Kennungen mit Jahr oder Buchstaben zu verwenden. Hierbei kannst du zwischen systemweiten oder projektbezogenen Einstellungen für Kanäle mit hohem Volumen wählen.

### Spezialeinstellungen

- **Warnung doppelte Nr** → Eine Systemmeldung, die in der Kopfleiste in Xentral erscheint, wenn doppelte Kunden-, Artikel-, Rechnungs- oder Gutschriftsnummern vergeben wurden.
- **Warnung doppelte Seriennummern** → Eine Systemmeldung, die in der Kopfleiste in Xentral erscheint, wenn eine doppelte Seriennummer vergeben wurde.
- **Belegnummer numerisch sortieren** → In Xentral sind Dokumentenübersichten standardmäßig alphabetisch sortiert. Stelle die Sortierung nur auf numerisch um, wenn du in deinen Belegnummern keine Buchstaben und Sonderzeichen verwendest.