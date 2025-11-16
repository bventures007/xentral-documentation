## Von der Planung zur Steuerung

Xentral hilft dir nicht nur bei der Produktionsplanung, sondern auch bei der Produktionssteuerung. Während die Produktionsplanung über einen gewissen zeitlichen Vorlauf bestimmt, was und wann produziert werden soll, sorgt die Produktionssteuerung dafür, dass die Planung zum gegebenen Zeitpunkt in die Tat umgesetzt wird – effizient, termintreu und fehlerfrei. Bei der Produktionssteuerung geht es also um die Feinjustierung. In unserem Fall zählen wir auch die Materialentnahme zur Produktionssteuerung.

Nachdem du entschieden hast, ob du nach Auftrag (make-to-order) oder auf Lager (make-to-stock) produzierst, stellt sich die Frage, wie du die Produktion tatsächlich steuerst. Du musst überwachen, dass alle Aufträge rechtzeitig und in der richtigen Reihenfolge bearbeitet werden, und sicherstellen, dass Materialien verfügbar sind.

## Priorisierung und Produktionsstart

Ein wichtiger Aspekt der Produktionssteuerung ist die punktgenaue Einlastung in die Produktion. Sinnvollerweise hälst du stets nur so viele Produktionen im StatusGESTARTET, dass die Produktion zwar aus- aber nicht überlastet ist.

Eine Überlastung der Produktion führt zu zahlreichen negativen Effekten und Folgeeffekten: Ein hohes "Work-in-Progress" (WIP) führt zu längeren Durchlaufzeiten. Dadurch ergibt sich ein hoher Bestand an unfertigen Erzeugnissen. Das führt wiederum zu höheren Lagerkosten, höherem Verwaltungsaufwand und schwierigeren Abschlüssen. Darüber hinaus verliert die Organisation Überblick, was eine höhere Fehleranfälligkeit bedeuten kann. Außerdem verlierst du an Flexibilität und kannst schlechter auf neue Aufträge oder Störungen reagieren. Im Gegensatz dazu solltest du aber auch dringend sicherstellen, dass deine Produktion nie leerläuft, denn dies wäre ineffizient, führt zu höheren Stückkosten, demotiviert Mitarbeiter in der Produktion und führt ebenfalls zu einer höheren Fehleranfälligkeit.

Berücksichtige diese Aspekte beim Starten deiner Produktionen: "So viele wie nötig, so wenige wie möglich." So erreichst du einen stabilen, fließenden Prozess, der sich an den Kundenbedarfen orientiert. Es bietet sich an, dass du zyklisch (z. B. täglich, wöchentlich) prüfst, wie hoch die aktuelle Auslastung in der Produktion ist und daraufhin genau so viele Produktionen startest, dass eine optimale Auslastung für den nächsten Zyklus sichergestellt ist.

Nun stellt sich noch die Frage, welche Produktionen du für den nächsten Durchlauf startest. Möglicherweise ist es hilfreich, sich an gängigen Prioritätsregeln zu orientieren:

- First In, First Out (FIFO): Die ältesten Aufträge werden zuerst bearbeitet. Das ist sinnvoll, wenn es keine besonderen Dringlichkeiten gibt.
- Dringlichkeitssteuerung: Besonders eilige Aufträge werden bevorzugt behandelt, um Lieferzeiten einzuhalten.
- Losgrößenoptimierung: Wenn du Losfertigung nutzt, können ähnliche Aufträge gebündelt werden, um Rüst- und Vorbereitungszeiten zu minimieren.

> **Tipp**
>
> Xentral überprüft die Materialverfügbarkeit im Hintergrund stetig und stellt sicher, dass du nur Produktionen starten kannst, für die ausreichend Material verfügbar ist.

### Produktion in Xentral starten

Um das Produktionsmodul zu erreichen, folge dem PfadLager > Produktionoder suche über die Smart Search nach “Produktion”. Du befindest dich in der Produktionsübersicht.

Nutze die Filter, um z. B. nur Produktionen anzeigen, für die Material verfügbar ist und die noch nicht gestartet wurden:

![Produktionssteuerung_Produktionsubersicht_Filter.png](https://help.xentral.com/hc/article_attachments/19368060889500)

Orientiere dich an den oben genannten Prioritätsregeln und den individuellen Bedürfnissen in deinem Unternehmen, um die Produktionen festzulegen, die gestartet werden sollen. Hake die entsprechenden Produktionen an und nutze die Stapelverarbeitung zum Starten:

![Produktionssteuerung_Produktionsubersicht_ProduktionenStarten.png](https://help.xentral.com/hc/article_attachments/19368060896028)

### Achtung

Beachte, dass die kombinierte AktionStarten und Auslagernbei Artikeln mit Chargennummern zu Diskrepanzen zwischen Lager- und Chargenbestand führt. Wenn du chargen-geführte Artikel hast, achte hier unbedingt darauf, die FunktionStartenzu nutzen!

Die Produktionen befinden sich nun im StatusGESTARTETin der Produktionsübersicht:

![Produktionssteuerung_Produktionsubersicht_GESTARTET.png](https://help.xentral.com/hc/article_attachments/19368060899996)

## Materialentnahme für die Produktion (Material auslagern)

Nachdem du die Produktion gestartet hast, kannst du das Material dafür auslagern. Je nachdem, ob du chargen-geführte Artikel hast oder nicht, unterscheidet sich das Vorgehen geringfügig.

> **Anmerkung**
>
> Die Materialauslagerung kann - je nach Berechtigung - entweder durch dich oder durch die Mitarbeiter im Lager erfolgen.

### Mit chargen-geführten Artikeln bzw. Artikeln mit Mindesthaltbarkeitsdatum

> **Anmerkung**
>
> Dieses Vorgehen trifft zu, wenn mindestens eine Komponente chargen-geführt ist bzw. ein Mindesthaltbarkeitsdatum hat.

1. Öffne die Produktion zur Bearbeitung.
1. Gehe zum Reiter Chargen.
1. Buche deine eingesetzten Chargen aus, indem du den Artikel, die Charge / das Mindesthaltbarkeitsdatum und die Anzahl eingibst und auf hinzufügen klickst:
1. Sobald du nun zum ReiterDetailswechselst, wird dir der Auslagerungsstatus gelb (Produktion teilausgelagert) angezeigt. Sowohl deine Charge(n) / die Mindesthaltbarkeitsdaten als auch der Lagerbestand der chargen-geführten Artikel bzw. Artikel mit Mindesthaltbarkeitsdatum wurden in einem Schritt reduziert.
1. Wähle nun die Aktion Produktion auslagern.
1. Du gelangst automatisch auf die Seite Artikel für Produktionen. Bestätige dort die Entnahme mit Klick auf Lager anpassen.
1. Damit werden die restlichen, nicht-chargen-geführten Artikel aus dem Lager ausgebucht und der Auslagerungsstatus wechselt zu grün (Produktion ausgelagert).

### Vereinfachter Prozess ohne chargen-geführte Artikel

### Achtung

Verwende dieses Vorgehen nur, wenn du keine chargen-geführten Artikel hast, um Diskrepanzen zwischen Lager- und Chargenbestand zu vermeiden!

1. Hake die Produktionen, für die du Material auslagern möchtest, in der Produktionsübersicht an und wähle in der Stapelverarbeitung Auslagern.
1. Damit werden die Artikel aus dem Lager ausgebucht und der Auslagerungsstatus wechselt zu grün (Produktion ausgelagert).

## Mit dem Produktionszentrum arbeiten

Nachdem du die Produktion gestartet hast, steht dir das Produktionszentrum zur Verfügung.

> **Anmerkung**
>
> Das Produktionszentrum kann - je nach Berechtigung - durch dich und/oder durch die Mitarbeiter der Produktion genutzt werden. Letztere Variante ermöglicht Euch z. B., dass die Produktion selbst zeitnah Eintragungen zu Funktionsprotokoll, Seriennummern und Ausschuss vornimmt, Doppelerfassungen vermieden werden, und du in Echtzeit Rückmeldungen zum Status hast und darauf bei Bedarf reagieren kannst.

Mit dem Produktionszentrum kannst du:

- Den Status der Zeiterfassung überblicken,
- Den Status der Funktionstests beobachten,
- Seriennummern zuordnen bzw. vergeben,
- Chargennummern und Mindesthaltbarkeitsdatum für das Erzeugnis eintragen.

### Produktionszentrum-Übersicht

Um das Produktionszentrum zu erreichen, folge dem PfadLager > Produktionszentrumoder suche über die Smart Search nach “Produktionszentrum”. Du befindest dich dann in der Produktionszentrums-Übersicht.

#### Reiter Übersicht

In der Übersicht siehst du alle gestarteten Produktionen auf einen Blick. Von hier kannst du eine bestimmte Produktion in der Einzelansicht öffnen (1).

![Produktionssteuerung_Produktionszentrum_Ubersicht.png](https://help.xentral.com/hc/article_attachments/19368094128412)

Falls ein anderer Nutzer eine Produktion geöffnet hat (du erkennst dies an dem roten Hinweis "in Bearbeitung von xxx"), und du die Produktion bearbeiten willst, kannst du die Nutzer-Sperre durch die Schaltfläche (2) aufheben.

#### Reiter Einstellungen

Im ReiterEinstellungenkannst du festlegen, ob der Funktionstest als einzelne Icons dargestellt werden soll und einen globalen Seriennummernkreis festlegen, wenn du für alle Erzeugnisse denselben Seriennummernkreis verwenden möchtest:

![Produktionssteuerung_Produktionszentrum_Einstellungen.png](https://help.xentral.com/hc/article_attachments/19368094130204)

Setzt du den Haken beim Funktionstest, wird in der Einzelansicht des Produktionszentrums für jeden Prüfschritt ein eigenes Symbol anzeigt:

![Produktionssteuerung_Produktionszentrum_Einzelansicht_FT-einzeln.png](https://help.xentral.com/hc/article_attachments/19368060927900)

Lässt du den Haken weg, erscheint dagegen ein Sammelsymbol:

![Produktionssteuerung_Produktionszentrum_Einzelansicht_FT-kompakt.png](https://help.xentral.com/hc/article_attachments/19368060930204)

### Produktionszentrum-Einzelansicht

Um die Einzelansicht zu öffnen, klicke auf den Pfeil in der Übersicht. Alternativ gelangst du auch über eine gestartete Produktion hierher.

#### Reiter EInzelproduktionen erfassen

Dieser Reiter ist das Kernstück des Produktionszentrums.

![Produktionssteuerung_Produktionszentrum_Einzelansicht_Vorversion.png](https://help.xentral.com/hc/article_attachments/19368094138780)

Im oberen Teil kannst du

- die Seriennummer des Erzeugnisses vom Produktions-PDF scannen, sofern im Vorfeld eine Seriennummer vergeben wurde, um die Funktionstests zu starten und zu protokollieren,
- verwendete Komponenten-Seriennummern (Unterseriennummern) scannen, um sie dem Erzeugnis zuzuordnen,
- über den Generator neue Seriennummern bzw. Chargennummern definieren.
- Außerdem kannst du verschiedene Dokumente an den Drucker senden.

Im unteren Teil erhälst du einen Überblick über die in der Produktion zu erzeugenden Baugruppen, den Status von Seriennummern und Funktionstests. Im Menü stehen dir von links nach rechts folgende Aktionen zur Verfügung:

- Seriennummer ändern: Nutze diese Schaltfläche, wenn du eine Seriennummer für das Erzeugnis manuell eingeben oder ändern möchtest. Falls du eine automatische Vergabe bevorzugst, nutze den Generator oder den globalen Seriennummernkreis (Produktionszentrum > Übersicht > Einstellungen).
- Unterseriennummer ändern: Hier ordnest du die verwendeten Komponenten-Seriennummern (Unterseriennummern) dem Erzeugnis zu.
- Funktionstest ausführen: Öffne hier, um die Testschritte durchzuführen und zu protokollieren.
- Kommentar ändern: Hier kannst du einen kurzen Kommentar eingeben.
- Etikettenset für Baugruppe drucken
- setze Baugruppe auf Ausschuss: Klicke hier, um eine Baugruppe als Ausschuss zu kennzeichnen.

#### Reiter Arbeitsanweisungen

In diesem Reiter erhälst du bzw. die Mitarbeiter der Produktion einen Überblick über die durchzuführenden Arbeitsschritte.

![Produktionssteuerung_Produktionszentrum_Arbeitsanweisungen.png](https://help.xentral.com/hc/article_attachments/19368094140572)

#### Reiter Funktionsprotokoll

In diesem Reiter erhälst du bzw. die Mitarbeiter der Produktion einen Überblick über die durchzuführenden Testschritte.

![Produktionssteuerung_Produktionszentrum_Funktionsprotokoll.png](https://help.xentral.com/hc/article_attachments/19368094145948)

#### Reiter Seriennummern

Hier bekommst du einen Überblick über die zu der Produktion gehörigen Seriennummern - sowohl der Erzeugnisse (1), als auch der Komponenten (2). Über den Stift (3) gelangst du zum ReiterEinzelproduktionen erfassen.

![Produktionssteuerung_ReiterSeriennummern.png](https://help.xentral.com/hc/article_attachments/19368060941596)

#### Reiter Chargen

Hier erhälst du einen Überblick über die in der Produktion eingesetzten und produzierten Chargen bzw. Mindesthaltbarkeitsdaten.

Unter dem TabEingesetzte Chargensind alle chargengeführten Bauteile oder Bauteile mit Mindesthaltbarkeitsdatum aufgelistet mit der Angabe, in welcher Produktion sie verwendet wurden. Über das X am rechten Rand kannst du eine Zuweisung entfernen.

![Produktionsubersicht_Chargen.png](https://help.xentral.com/hc/article_attachments/19368060942364)

Unter dem TabProduzierte Chargenfindest du alle erzeugten Chargen bzw. Mindesthaltbarkeitsdaten der von dir produzierten Artikel. Über die Produktionsnummer kannst du zu einer betreffenden Produktion wechseln.

#### Reiter Abschluss

Eine ausführliche Beschreibung dieses Reiters und zu dem generellen Vorgehen beim Produktionsabschluss findest du[hier](https://help.xentral.com/hc/de/articles/18870451160988#UUID-29284617-b0fc-fc6e-2df7-284c68337605).

## Zeiten auf Produktionen erfassen

Wenn du die Zeiterfassung in Xentral nutzt, können deine Produktionsmitarbeiter Zeiten auf Produktionen buchen. Dazu verwendet Ihr die Stechuhr. Generelle Informationen zur Zeiterfassung in Xentral findest du[hier](https://help.xentral.com/hc/de/articles/360016728560#UUID-bf44543b-82c9-1fe7-9f42-c180c152a6f3).

> **Anmerkung**
>
> Damit Zeiten auf Produktionen zugeordnet werden, nutze dieStechuhr. Bei einer Eingabe über Zeiterfassung > Zeiterfassung buchen, erfolgt keine Zuordnung auf Produktionsschritte!

Im Folgenden findest du eine Schritt-für-Schritt-Anleitung zum Erfassen ohne Verwendung eines Barcode-Scanners:

Um die Stechuhr zu erreichen, suche über die Smart Search nach “Stechuhr”.

1. Tagesbeginn: Dokumentiere den Start deines Arbeitstages mit der Schaltfläche Kommen.
1. Um die Arbeitsschritterfassung zu starten, verwende die Schaltfläche Arbeitsschritte:
1. Start eines Arbeitsschrittes:
1. Um laufende Arbeitsschritte aufzurufen, verwende diese Schaltfläche:
1. Beenden eines Arbeitsschrittes:
1. Sobald ein Arbeitsschritt vollständig abgeschlossen ist, kannst du den Abschluss mit dieser Schaltfläche dokumentieren:
  Im Protokoll der Produktion ist der Abschluss nun aufgezeichnet:

1. Tagesende: Dokumentiere das Ende deines Arbeitstages mit der Schaltfläche Gehen.