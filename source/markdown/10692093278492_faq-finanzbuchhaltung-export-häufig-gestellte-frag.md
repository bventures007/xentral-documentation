Willkommen zu unserer FAQ-Seite! Hier findest du Antworten auf die am häufigsten gestellten Fragen zu unseren Produkten und Services. Diese Seite dient dazu, dir schnelle und hilfreiche Informationen zu bieten, die dir bei der Nutzung unserer Plattform weiterhelfen. Ob zur Einrichtung, Fehlerbehebung oder für Tipps zur optimalen Nutzung – unsere FAQ bieten dir umfassende Unterstützung.

> **Warnung**
>
> Der neue Datev Export gilt ab Xentral Version 23.17.3 und späteren Versionen. Der Service ist nur auf unserer Cloud verfügbar.

> **Anmerkung**
>
> Wir arbeiten kontinuierlich daran, den neuen Finanzbuchhaltungs-Export für euch zu verbessern und euer Feedback direkt in die Entwicklung einfließen zu lassen.
>
> Falls ein Problem auftreten sollte, aktualisiert bitte auf die neueste Xentral-Version, um von den neuesten Optimierungen zu profitieren.
>
> Alle Änderungen und Updates findet ihr in denRelease Notes (alle Versionen in 2024).

Wenn du auf einer sehr alten Datev Export Version (vor 2018 arbeitest) oder den Datev Export für andere Buchhaltungssysteme aufbereitest, kann es sein, dass durch Neuerungen des Exports und der zugehörigen API alte Funktionen nicht mehr verfügbar sind oder durch neue Felder auf Seiten Xentrals und Datevs ersetzt wurden. Sollten in deiner Version Probleme auftreten kannst du in dieser FAQ Liste schnell die wichtigsten Fragen und Antworten finden.

Solltest du eine Frage hier nicht finden, erstelle bitte ein Support-Ticket.

## Mein Export funktioniert nicht wie gewohnt und ich erhalte eine Fehlermeldung. Was soll ich tun?

Die Validierung prüft den Export auf gültige Zeichen nach Anforderungen von Datev, die ansonsten beim Import in DATEV unter Umständen abgeschnitten, ignoriert oder falsch importiert werden würden. Das bedeutet nicht unbedingt, dass diese Prüfung in deinem Fall relevant ist. Bitte deaktiviere deshalb im Modul **Finanzbuchhaltung Export ** zuerst die CSV Validierung (Option: **CSV Validierung deaktivieren**) und prüfe, ob dein Export in Ordnung ist. Erstelle gerne ein Support-Ticket, falls du trotzt Deaktivierung der Validierung Probleme hast.

![2640642106.png](https://help.xentral.com/hc/article_attachments/10692130735772)

## Fehlermeldung “Beraternummer fehlt”: Ich habe keine Berater- oder Mandantennummer, weil ich DATEV nicht nutze, bekomme aber eine Fehlermeldung?

Bitte deaktiviere im Modul **Finanzbuchhaltung Export ** die CSV Validierung (Option: **CSV Validierung deaktivieren**) oder hinterlege eine Pseudo-Berater/-Mandantennummer im ReiterEinstellungen.

Für den Datev Export ist eine[Mandaten- und Beraternummer](https://help.xentral.com/hc/de/articles/360016725100#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e)eine Pflichtangabe, damit dein Steuerbüro eine automatische Zuordnung deiner Daten zu deiner Firma erhält. Solltest du den Datev Buchhaltungsexport in andere Systeme einspielen und keine Berater- und Mandantennummer haben, kannst du selbst eine fünfstellige Nummer vergeben. Die Nummer wird im Exportformat z.B. in der Kopfzeile übergeben.

![2640642106.png](https://help.xentral.com/hc/article_attachments/10692130735772)

## Fehlermeldung “Beraternummer fehlt”, ich nutze aber projektspezifische Beraternummern

Wenn du den Datev Export bisher nur für einzelne Projekte verwendet hast, und keine Beraternummer als Standard vergeben hast, füge einen[Eintrag ohne Projekt als Fallback hinzu](https://help.xentral.com/hc/de/articles/360016725100#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e). Diese Beraternummer wird für Exporte ohne Projektzuordnung verwendet und verhindert, dass du hier eine Fehlermeldung erhältst.

**Schritte**:

Füge einen Eintrag ohne Projekt zu, indem du Beraternummer, Mandantennummer, Sachkontenlänge und Wirtschaftsjahr in einen Neuen Eintrag eingibst. Lasse das Feld für **Projekt** in diesem Fall einfach leer.

![2640642115.png](https://help.xentral.com/hc/article_attachments/10692108368796)

## Ich nutze kein DATEV und benötige das alte Export-Format mit Dateibezeichnung EINNAHMEN_FORMAT3.csv in folgendem Format:

![2640642121.png](https://help.xentral.com/hc/article_attachments/10692108425756)

Unser Export ist für DATEV ausgelegt und unterstützt deshalb immer das aktuellste DATEV-Format. Bitte schreibe uns ein Ticket, wenn und weshalb du nicht das neue Format nutzen kannst und wir prüfen gerne deinen Fall.

## Datev Unternehmen Online: Warum hat sich die Dateibezeichnung der XML Dateien in “accountsReceivableLedger_Ausgangsrechnungen” geändert? Warum ist die Datumsbezeichnung in der Datei nicht mehr da?

In der neuen Version des Finanzbuchhaltung Exports haben wir die Dateibezeichnungen so angepasst, dass diese den Empfehlungen und Anforderungen von DATEV entsprechen. Der alte Dateiname war früher von Xentral individuell gewählt worden.

## Beim Export von Kunden/ Lieferanten erhalte ich die Fehlermeldung, dass die IBAN oder BIC falsch ist

Der neue Finanzbuchhaltung Export beinhaltet eine Überprüfung deiner Daten (Validierung). Unter anderem wird die in deinen Kontakten hinterlegte Bankverbindung (IBAN, BIC) auf Gültigkeit und Konformität geprüft.

Bitte deaktiviere die CSV-Validierung, damit der Export dennoch funktioniert. In der exportierten Datei kannst du die falschen IBANs/BICs (meist zu kurz oder zu lang) identifizieren und die betroffenen Adresse (unterAdresse/Kontakte > Bankverbindung) in Xentral korrigieren.

## Fehlermeldung “an exchange rate should be a positive number”

Xentral prüft, ob es beim Export von Belegen in Fremdwährung eine Währungsumrechnung gibt, die im Modul **Währung Umrechnung** hinterlegt werden muss bzw. abgerufen werden kann. Falls nicht, muss diese hinzugefügt werden. Mehr Infos findest du hier:[Währungsverwaltung und Währungsumrechnung](https://help.xentral.com/hc/de/articles/360016806879#UUID-b60d5e65-b01f-3c42-8fa5-c6d5d46f5a8c).

Am einfachsten ist es, die Kurse von der EZB zu laden und den Prozessstarter zu aktivieren, damit diese aktuell bleiben, wie im folgenden Screenshot zu sehen:

![2640642109.png](https://help.xentral.com/hc/article_attachments/10692093688988)

## Fehlermeldung: der Wert “90" in der Spalte BU-Schlüssel (009) is ungültig. Regel/Format: /^([“]\d{4}[“]){0,1}$/. 10019

Hierbei handelt es sich um einen aktuellen Programmfehler in manchen Instanzen, der dafür sorgt, dass die Fehlermeldung fälschlicherweise angezeigt und der Export nicht durchgeführt wird. Wir arbeiten bereits an der Behebung dieses Fehlers. Bitte deaktiviere die CSV-Validierung als Workaround, damit der Export dennoch funktioniert.

## Datev Connect: Warum ist die Fortschrittsanzeige beim Export verschwunden?

Zuvor geschah der Export in Datev Connect asynchron im Hintergrund. Grund hierfür war die langsamere Export-Geschwindigkeit des alten Exports. Aus diesem Grund war eine Fortschrittsanzeige notwendig. Dies ist nun nicht mehr der Fall, da der neue Export direkt nach dem Klick auf **Export** angestoßen und ausgeführt wird. Die Validierung der Daten finden bereits beim Export statt, der Fortschritt ist deshalb nicht mehr notwendig.

## Datev Connect: Wie sehe ich, welchen Export ich zuletzt durchgeführt habe?

Wir haben bereits das Feedback erhalten, dass dies nützlich war und werden die Oberfläche zeitnah entsprechend anpassen. Falls der letzte exportierte Zeitraum nicht mehr bekannt ist, dann kann dieser im Modul `Datenbank Ansicht` in der Tabelle `datevconnect_online_export` eingesehen werden. Hier bitte nach *Id* sortieren.

![2640642112.png](https://help.xentral.com/hc/article_attachments/10692093612572)

## Kann DATEV führende Nullen verarbeiten? Nullen in DATEV (Konten, Debitoren, Kreditoren)

Ja, technisch schon – Felder für Konten, Debitoren und Kreditoren sind alphanumerisch. Führende Nullen werden aber im Standard nicht genutzt und können bei Export/Import oder Abstimmungen für Verwirrung sorgen.

### Wie werden Sachkonten in DATEV erfasst? (Nullen)

Standard ist eine 4-stellige Kontonummer (z. B. 1000 Kasse). Eine Eingabe wie 01000 wird auf 1000 reduziert. Empfehlung: immer 4-stellig, ohne führende Nullen.

### Welche Nummernkreise gelten für Debitoren und Kreditoren? (Nullen)

Debitoren: ab 10000, Kreditoren: ab 70000. Eine Kundennummer 00123 kann zwar importiert werden, entspricht aber nicht dem Standard.

### Gibt es einen Unterschied zwischen führenden Nullen und Füllnullen?

Führende Nullen sind rein optisch und entfallen im Standard. Füllnullen sind nötig, wenn ein Feld eine feste Länge haben muss (z. B. bei bestimmten Schnittstellen).

### Was ist die empfohlene Praxis? (Nullen)

Sachkonten: immer 4-stellig, keine führenden Nullen. Debitoren: ab 10000, keine führenden Nullen. Kreditoren: ab 70000, keine führenden Nullen.