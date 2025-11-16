> **Anmerkung**
>
> Das Modul **Scanner-Test ** befindet sich aktuell im**Beta-Status**.
>
> Hast du Interesse, diese Funktion schon jetzt zu verwenden und zu testen? Dann wende dich ansupport@xentral.com, damit das Modul für deine Xentral-Instanz freigeschaltet wird.
>
> **Typischer Anwendungsfall **: Diese Funktion richtet sich an Nutzer, die mit dem Modul ** Wareneingang (GS1)**arbeiten und Artikel per MDE-Gerät oder Handscanner erfassen möchten. Im vorliegenden Artikel werden die benötigten Voreinstellungen für diese Geräte beschrieben.
>
> **Relevanz **: Das Modul ** Scanner-Test **ist ausschließlich für die Erfassung von gelieferten Artikeln im Menü ** Lager > Wareneingang (GS1)**relevant.
>
> **Nicht relevant für **: Das Modul ** Scanner-Test**ist nicht relevant für Warenausgang, Versandzentrum, Kommissionierverfahren.

MDE-Geräte und Handscanner sind unerlässliche und effiziente Tools im Logistik-Alltag: Mit ihrer Hilfe erfasst du Barcodes und damit auch die Vielzahl der darin verschlüsselten Informationen, um sie anschließend in Xentral weiterzuverarbeiten. Höchstwahrscheinlich nutzt du an mindestens einem Computer in deinem Lager bereits einen Handscanner, beispielsweise um Artikel am Packtisch im[Xentral Versandzentrum](https://help.xentral.com/hc/de/articles/360016757139#UUID-8ee2b6e8-1c6c-8f2e-1259-35d3532701b0)zu erfassen, bevor sie verpackt und versandt werden.

Besonders für die Arbeit mit dem neuen Modul **Wareneinang (GS1)** empfehlen wir dir die Nutzung eines zeitgemäßen MDE-Geräts. Der Grund? Gerade bei umfangreichen Wareneingängen mit zahlreichen Artikeln ist die manuelle Auswahl von Artikeln und die Eingabe der entsprechenden Informationen nicht nur mühsam und zeitintensiv, sondern auch fehleranfällig.

Im vorliegenden Artikel erfährst du,[welche MDE-Modelle wir empfehlen](#UUID-94d554c0-9368-d875-caaa-e688ccdf6367_section-idm234979286100035)und welche Einstellungen du vorab vornehmen musst, um deine Geräte korrekt einzustellen und somit effizient und fehlerfrei mit dem Modul **Wareneingang (GS1)** zu arbeiten.

> **Wichtig**
>
> Bitte beachte, dass wir trotz aller Bemühungen nicht für jeden Hersteller oder jedes Modell ausführliche Anleitungen bereitstellen können. Prüfe deshalb in jedem Fall auch die Betriebsanleitung deines Handscanners oder MDE-Geräts. Wir stellen in diesem Artikel eine spezifische Anleitung für Zebra-MDEs vor, können aber nicht in jedem Einzelfall die Durchführbarkeit der Einrichtung garantieren.

## Empfohlene MDE-Geräte

Für die Artikelerfassung im Modul **Wareneingang (GS1)** empfehlen wir die folgenden MDE-Geräte:

- Zebra TC 21
- Zebra TC 22
- Zebra TC 26

> **Anmerkung**
>
> Es ist möglich, auch Modelle von anderen Herstellen zu verwenden. Stelle in diesem Fall aber sicher, dass du über die Bedienungsanleitung deines MDE-Geräts oder Handscanners verfügst und die Konfiguration selbstständig vornimmst undmithilfe des Moduls Scanner-Test testest, bevor du produktiv mit dem Modul **Wareneingang (GS1)** arbeitest.

## Einstellungen für Zebra-MDEs

Auf den oben genannten und den meisten gängigen MDEs des Herstellers Zebra musst du die App **DataWedge** direkt auf dem Gerät nutzen, um darin ein neues Profil für die Erkennung von GS1-Barcodes zu erstellen. Ohne dieses Profil kann das Gerät die im Barcode verschlüsselten Daten nicht korrekt entschlüsseln.

Gehe wie folgt vor, um das DataWedge-Profil für die Erfassung von GS1-Barcodes zu erstellen.

> **Tipp**
>
> Verwendest du mehrere Zebra-MDEs in deinem Lager? Dann musst du die unten beschriebenen Einstellungen nur auf einem einzigen Gerät vornehmen. Zebra bietet die Möglichkeit, bereits erstellte DataWedge-Profile auf weitere Geräte zu übertragen.
>
> Für weitere Informationen steht dir dazu dieoffizielle Anleitung von Zebrazur Verfügung. Gehe hier bitte sorgfältig vor und kontaktiere im Zweifel den Zebra-Support, um Fehler zu vermeiden.

1. Nimm dein Zebra-MDE zur Hand und öffne auf dem Startbildschirm die App **DataWedge**.
1. Stelle sicher, dass du dich im Menü **DataWedge-Profile** befindest.
1. Öffne oben rechts das **Dreipunkt-Menü ** und tippe auf **+ Neues Profil**.
1. Gib einen aussagekräftigen Namen für das Profil ein, z.B. "Barcode GS1". Tippe dann auf **OK**.
1. Tippe auf das soeben erstellte Profil, um es zu öffnen.
1. Aktiviere die Option **Profil aktiviert**.
1. Scrolle nach unten, bis du den Bereich **Barcode-Eingabe** erreichst.
1. Aktiviere die Einstellung **Scannereingabe aktivieren/deaktivieren**.
1. Tippe auf **Scanner-Einstellungen konfigurieren**.
1. Tippe auf **Scan-Parameter**.
1. Wähle die Option **Code-ID-Typ - Ziel**.
1. Navigiere zu **Barcode-Eingabe > Scanner-Einstellungen konfigurieren**.
1. Aktiviere beim Menüpunkt **Decoder** die folgenden Optionen:
  - **Code128 **

-** Code39 **

-** EAN8 **

-** EAN13 **

-** GS1 DataBar **

-** Erweiterter GS1-Barcode **

-** GS1 DataMatrix **

-** GS1 QRCode **

1. Tippe unten links auf deinem Gerät auf **Zurück** (Pfeil nach links), um in die Profile instellungen zurückzukehren.
1. Navigiere zum Bereich **Tastenanschlag-Ausgabe > Schlüsselereignisoptionen**.
1. Nimm im Bereich **Schlüsselereignisoptionen** folgende Einstellungen vor:
  1. Aktiviere die Einstellung **Zeichen als Ereignisse senden**.
  1. Aktiviere die Einstellung **Tastenanschlagausgabe ** im Bereich **Erweiterte Datenformatierung**.
1. Gehe zum Bereich **Einfache Datenformatierung ** und aktiviere die Optionen **Aktivieren **, ** Daten senden ** und **Senden mit EINGABE**.
1. Navigiere zu **Tastenanschlag-Ausgabe > Erweiterte Datenformatierung > Regeln**.
1. Öffne den Eintrag **Rule0**.
1. Tippe auf die entsprechende Checkbox, um die Regel zu **aktivieren**.
1. Tippe oben rechts auf das Drei-Punkte-Menü und dann auf **Neue Aktion**.
1. Tippe auf **Ersatzzeichenfolge**.
1. Tippe auf den **Ersatzzeichenfolge**.
1. Gib im oberen Eintrag die im Screenshot gezeigte Zeichenfolge ein.
1. Tippe auf **OK**.
1. Tippe erneut auf **Ersatzzeichenfolge ** und gib zusätzlich die Zeichenfolge **[[GS]]** ein. Anschließend solltest du folgende Zeichenfolgen hinterlegt haben:

## Einstellungen für Handscanner

Handscanner sind Datenerfassungsgeräte, die per USB oder per Bluetooth an deinen Computer angeschlossen sind. Im Gegensatz zu MDE-Geräten verfügen sie über kein eigenes Display. Die grundlegende Funktion ist jedoch gleich: Mit dem Handscanner erfasst du die Barcodes deiner Produkte. Daraufhin werden die im Barcode verschlüsselten Informationen entschlüsselt und somit die Datenerfassung in Xentral ermöglicht.

Im Folgenden weisen wir auf die Einstellungen hin, die für Handscanner notwendig sind, um erfolgreich mit dem Modul **Wareneingang (GS1)** zu arbeiten. Du findest zunächst allgemeine Einstellungen, die grundsätzlich für jeden Handscanner ausgeführt werden müssen. Weiter unten stellen wir eine beispielhafte Anleitung inklusive der zu scannenden Barcodes für das Modell Netum C750 zur Verfügung.

### Allgemein benötigte Einstellungen für Handscanner

Die folgenden Einstellungen solltest du unabhängig von Hersteller oder Modell an deinem Handscanner vornehmen, damit GS1 Barcodes korrekt erfasst werden:

- **AIM Identifier** aktivieren
- Zeilenumbruch-Bezeichnung auf **CR** umstellen
- **ASCII-Modus** einschalten
- **GS1-128 Barcodes** aktivieren

> **Tipp**
>
> Du bist dir nicht sicher, wie du die oben genannten Einstellungen vornimmst? Das Handbuch deines Handscanners hilft dir weiter. In vielen Fällen enthalten diese Handbücher einen Barcode pro benötigter Einstellung, den du ganz einfach abscannen kannst.

### Netum C750 einrichten

In diesem Kapitel erfährst du, welche Schritte du konkret durchführen musst, wenn du den Handscanner Netum C750 verwendest. Bei diesem Modell scannst du eine Abfolge von Barcodes, um die passende Konfiguration auf dem Gerät herzustellen.

Die folgende Tabelle zeigt dir alle erforderlichen Schritte und den benötigten Barcode, den du direkt von deinem Bildschirm abscannen kannst.

| Einstellung | Barcode |
| --- | --- |
| AIM Identifier aktivieren | | |
| |
| Zeilenumbruch-Bezeichnung auf CR umstellen | | |
| |
| ASCII-Modus einschalten | | |
| |
| GS1-128 Barcodes aktivieren | | |
| |

## Scanner-Konfiguration testen

Gehe abschließend wie folgt vor, um zu testen, dass die Konfiguration deines MDE-Geräts oder Handscanners korrekt funktioniert.

1. Öffne Xentral auf deinem Computer.
1. Öffne das Menü **Lager > Scanner-Test**.
1. Platziere den Cursor im Feld **Scan barcode**.
1. Nimm deinen Handscanner oder MDE-Gerät zur Hand und scanne den angezeigten QR-Code.

![scanner-test-de.png](https://help.xentral.com/hc/article_attachments/20444776499100)

> **Anmerkung**
>
> Solltest du bei einzelnen Punkten **rote Meldungen** angezeigt bekommen, ist dein MDE-Gerät oder Handscanner noch nicht korrekt eingestellt. Falls du ein MDE-Gerät des Herstellers Zebra verwendest, prüfe noch einmal die Anleitungim vorherigen Kapitel. Nutzt du andere Geräte, solltest du die jeweilige Betriebsanleitung konsultieren.