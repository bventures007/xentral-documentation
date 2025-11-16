Mit der Versandart **UPS (OAuth)** in Xentral bringst du deine Sendungen zuverlässig und flexibel auf den Weg. In diesem Artikel beschreiben wir die Einrichtung der Versandart ** UPS (OAuth)** in Xentral.

Du erfährst Schritt für Schritt, wie du die Anbindung vornimmst, Service- und Package-Codes korrekt auswählst, Zolldokumente automatisch erzeugst und Tracking-Informationen an deine Shops zurückspielst. So behältst du jederzeit den Überblick über deine Sendungen und stellst sicher, dass deine Kunden ihre Bestellungen pünktlich erhalten.

Die Versandart **UPS (OAuth)** eignet sich besonders für dich, wenn du internationale Märkte bedienst, zeitkritische Sortimente führst oder hochwertige Produkte vertreibst, die besonders schnell und zuverlässig deine Endkunden erreichen sollen.

## Features

DieXentralVersandart **UPS (OAuth)** bietet dir die folgenden Features:

- Nationaler und internationaler Versand
- Rückmeldung der Trackingnummer an deine Online-Shops und Verkaufsplattformen
- Automatischer Ausdruck von Versandlabels direkt aus Xentral
- Angabe des Produkttyps bei internationalen Sendungen (z. B. Standard, Express, Saver)
- Unterstützung von Paket-, Express- und Sperrgut-Sendungen
- Automatische Generierung und Übergabe der Zollinformationen für Sendungen außerhalb der EU
- Nutzung von Zusatzservices wie Nachnahme, Samstagszustellung, Transportversicherung, Signature Services

## UPS (OAuth) an Xentral anbinden

Um **UPS (OAuth)** als Versandart zu nutzen, legst du zunächst eine neue Versandart in Xentral an. Anschließend aktivierst du diese mit deinen vorliegenden Vertragsdaten von UPS. Es braucht nur einige Minuten und wenige Schritte, bis du deine ersten Produkte mit UPS versenden kannst!

> **Wichtig**
>
> Bevor du mit der Einrichtung der Versandart in Xentral startest, stelle sicher, dass du die OAuth-Authentifizierung in deinem UPS-Account aktiviert hast. Folge dazu denAnweisungen auf der UPS Entwicklerwebseite. Logge dich anschließend auf derUPS Entwicklerwebseiteein und aktiviere OAuth für dein Konto.

Gehe wie folgt vor, um die Versandart **UPS (OAuth)** in Xentral einzurichten.

1. Suche mithilfe der Smart Search nach **Versandarten**.
1. Klicke oben rechts auf **+ NEU**.
1. Klicke auf **UPS (OAuth)**.
1. Nimm die Einstellungen wie in der Tabelle unten beschrieben vor.
1. Klicke auf **Speichern**.

| Einstellung | Erläuterung |
| --- | --- |
| **Bezeichnung** | Gib eine Bezeichnung für die Versandart ein, die später bei der Auftragsbearbeitung in Xentral angezeigt wird. Die Bezeichnung ist nur für dich und deine Mitarbeiter sichtbar. Achte darauf, dass jede Bezeichnung nur einmal in Xentral vorkommt, damit die Versandart stets eindeutig identifiziert werden kann. |
| **Typ **| Dies ist eine interne Feldbezeichnung, die für die Zuordnung bei deinen Online-Shops und anderen Verkaufsplattformen benötigt wird. ⚠️** Wichtig:** Verändere diese Bezeichnung nicht! |
| **Modul** | Wähle das passende Modul aus dem Dropdown-Menü. Dabei muss der Modulname identisch zum Namen der Versandart sein, die du gerade einrichtest. |
| **Projekt **|** Optional**: Gib eine Projektzuordnung an. Diese wird benötigt, wenn du die Versandart auf einen bestimmten Verkaufskanal oder ein Projekt (beispielsweise eine spezifische Niederlassung) beschränken möchtest. |
| **Aktiv **| Aktiviere diese Option, sobald du alle benötigten Einstellungen für die Versandart vorgenommen hast. 💬** Anmerkung:** Nicht mehr verwendete Versandarten kannst du später deaktivieren. Beachte jedoch, dass deaktivierte Versandarten nur noch in bereits erstellten Belegen angezeigt werden. In neu erstellten Belegen und in Benutzerflächen wie der Auftragsübersicht oder in den Kundendaten steht eine deaktivierte Versandart nicht mehr zur Auswahl zur Verfügung. Du kannst Versandarten auch löschen. Dadurch wird jedoch auch die Versandhistorie gelöscht. Deshalb solltest du nur fälschlicherweise angelegte Versandarten löschen, die du nicht produktiv genutzt hast. |
| **Kein Portocheck** | Mit dieser Option kannst du den Porto-Check im Auftrag deaktivieren. Bleibt der Porto-Check aktiv, zeigt die Auftragsampel ein rotes Symbol für den Portocheck an, falls nicht mindestens ein Portoartikel in den Auftragspositionen enthalten ist. So wird verhindert, dass bei manuell angelegten Aufträgen der Portoartikel vergessen wird. Überlege anhand deiner eigenen Workflows und Arbeitsweise mit Xentral, ob du diese Option aktivieren oder deaktivieren willst. Legst du typischerweise viele Aufträge manuell in Xentral an, kann es sinnvoll sein, diese Option nicht zu aktivieren, sodass gerade bei hochpreisigen Artikeln oder internationalen Sendungen das Porto immer zuverlässig am Auftrag hinterlegt wird. |
| **Drucker Versandlabel** | Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für die Versandlabels genutzt werden soll. Beachte, dass hier nur Drucker auswählbar sind, die du bereits [in Xentral eingerichtet](https://help.xentral.com/hc/de/articles/360016756299#UUID-24ed3a57-a4df-da7a-08f6-141949df3855) hast. Je nachdem, wie und wo der Versandprozess in deinem Unternehmen abläuft, kannst du hier genau den Drucker auswählen, den du benötigst - egal ob direkt am Schreibtisch oder am Packtisch im Lager. |
| **Drucker Export **|** Nur bei internationalem Versand relevant**: Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für Zollpapiere (CN23) genutzt werden soll. |
| **Versand-E-Mail **| Lege hier fest, nach welchen Regeln Versandbenachrichtigungen per E-Mail an deine Kunden verschickt werden sollen, sobald sich die Sendung auf dem Weg befindet. Die folgenden drei Optionen stehen dir zur Verfügung: ** Standardverhalten **: Die Logistikeinstellungen aus dem Projekt werden verwendet. Diese Einstellungen nimmst du im Menü ** Einstellungen > Grundeinstellungen > Projekte > Projekt öffnen > Tab: Einstellungen > Tab: Logistik / Versand **vor. In den Bereichen ** Stufe 1 (Pick/Kommissionierung)**und ** Stufe 2 (Pack)**definierst du über die Checkboxen namens ** E-Mail **, bei welchen Schritten deine Kunden über den Stand der Auftragsbearbeitung informiert werden. ** Keine Versandmail **: Für diese Versandart wird keine Versandinformation per E-Mail versendet ** Eigene Textvorlage **: Für diese Versandart wird die ausgewählte Textvorlage per E-Mail versendet. Diese Vorlage musst du vorab im Menü ** Einstellungen > Grundeinstellungen > Belege > Textvorlagen **erstellen. Anschließend wählst du die gewünschte Vorlage im Dropdown-Menü ** Textvorlage** aus. Durch diese Auswahl werden die Logistikeinstellungen des Projekts für diese Versandart nicht genutzt. |
| **Lieferungen unterstützt **| Diese Option wird bei der Anlage der Versandart standardmäßig aktiviert. Sobald du alle weiteren benötigten Einstellungen vorgenommen und die Versandart auf ** Aktiv** gestellt hast, kannst du die Versandart in Aufträgen, Lieferscheinen und im Versandzentrum auswählen. |
| **Retouren unterstützt** | Aktiviere diese Option, um zu erlauben, dass Retouren zu Aufträgen angelegt werden können, die ursprünglich mit dieser Versandart erstellt wurden. |
| **UPS OAuth-Verbindung **| Klicke neben dieser Option auf ** Verbinden **. Du wirst zu deinem UPS-Konto weitergeleitet. Logge dich ein und folge den Anweisungen. Anschließend wirst du automatisch zu Xentral zurück geleitet. Neben der Einstellung ** UPS OAuth-Verbindung **wird nun statt ** Verbinden **das Wort ** Info** angezeigt. |
| **Bevorzugte Rücksendemethode** | Wähle eine bevorzugte Versandart für Retouren aus. Sobald in Xentral manuell eine Retoure zu einem Auftrag mit der vorliegenden Versandart angelegt ist, wird die hier gewählte Versandart automatisch im Retourenauftrag vorausgewählt. Diese Einstellung greift nur in Fällen der manuellen Retourenerstellung. |
| **Absender Name / Ansprechpartner / Straße / Hausnummer / PLZ / Ort / Bundesstaat / Land / E-Mail / Telefon /Internet / Steuerkennung **| Gib im Feld ** Absender Name **deinen Firmennamen ein und trage in den restlichen Feldern die Adressdaten deines Unternehmens ein. Bei der ** Steuerkennung **handelt es sich um die Umsatzsteuer-ID deines Unternehmens. Im Feld ** Internet **kannst du die E-Mail-Adresse des Kundenservice angeben. Die Angaben, die du hier machst, erscheinen als Absenderadresse auf deinen Versandlabels. 💬** Anmerkung:** Das Land muss als 2-stelliger ISO-Code angegeben werden, also z.B. DE, falls das Absenderland Deutschland ist. |
| **Standardgewicht **|** Optional**: Welches Gewicht haben die Sendungen typischerweise, die du mit dieser Versandart verschickst? Gib hier ein Standardgewicht in kg ein. Dieses Gewicht wird jedes Mal bei der Erstellung eines Versandlabels an den Versanddienstleister übermittelt, soweit es nicht vor dem Druck des Versandlabels manuell in Xentral geändert wird. |
| **Gewicht anpassen in **| Zur Erstellung des Versandlabels wird eine genaue Berechnung des Gesamtgewichts der Sendung inklusive Verpackungsmaterial benötigt. Xentral berechnet das Sendungsgewicht automatisiert im Hintergrund, indem das Gesamtgewicht der im Auftrag enthaltenen Positionen addiert wird. Mit der vorliegenden Option wird diesem Gewicht ein von dir festgelegtes Gewicht hinzugefügt. So entsteht ein Gesamtwert für die Versandanmeldung, der bei der Erstellung des Versandlabels berücksichtigt und automatisch an den Versanddienstleister gemeldet wird. Entscheide, ob das zusätzliche Gewicht des Verpackungsmaterials in ** kg **oder**%** angegeben werden soll. Mithilfe der folgenden Einstellung namens ** Gewicht anpassen um** definierst du das zusätzliche Gewicht genauer. |
| **Gewicht anpassen um **| Mithilfe dieser Einstellung bestimmst du deine Angaben für die Einstellung ** Gewicht anpassen in** näher. Gib hier das zusätzliche Sendungsgewicht je nach vorheriger Auswahl in Kilogramm oder Prozent ein. Für welche Berechnungsart und welche konkreten Werte du dich entscheidest, hängt von der Verpackungsart deiner Produkte und deinen verwendeten Verpackungsmaterialien ab. |
| **Länge / Breite / Höhe** | Gib die Standardmaße deiner Sendungen in cm an. Diese Maße werden dann an den Versanddienstleister übermittelt, falls sie nicht beim Druck des Versandlabels manuell in Xentral geändert werden. |
| **Standard Service Code** | Gib den Standard Service Code ein, den du im UPS-Kundenportal findest. Ein Standard Service Code entspricht dabei einem UPS-Produkt, das du gebucht hast. Hast du also beispielsweise das Produkt für die Standard- und auch Expresslieferung bei UPS gebucht, legst du für jedes Produkt eine eigene Versandart in Xentral an. Die folgende Liste enthält die am häufigsten verwendeten Standard Service Codes: - Express = 07<br>- Expedited = 08<br>- UPS Standard = 11<br>- Express Plus = 54<br>- UPS Saver = 65<br>- UPS Express 12:00 = 74 |
| **Standard Service Description **| Gib die Standard Service Description aus dem UPS-Kundenportal ein, z.B. ** UPS Standard**. |
| **Standard Package Code **| Gib den Standard Package Code aus dem UPS-Kundenportal an. Der Code** 02** ist in den allermeisten Anwendungsfällen zutreffend, denn er bedeutet, dass du deine Ware in deiner eigenen Verpackung an UPS übergibst. Falls du UPS-eigene Verpackungsoptionen vertraglich gebucht hast, findest du den benötigten Standard Package Code im UPS-Kundenportal. |
| **Standard Package Description **|** Optional **: Die Standard Package Description kannst du frei vergeben, z.B. ** Customer Supplied**. |
| **Referenz 1 auf Label **| Bestimme mithilfe der angezeigten Variablen, ob du zusätzliche Informationen auf dem UPS-Versandlabel abdrucken möchtest. Du kannst auch einen Freitext eingeben. Folgende Variablen stehen dir zur Verfügung: {LIEFERSCHEIN}, {AUFTRAG}, {PROJEKT},{IHREBESTELLNUMMER}, {INTERNET}. ⚠️** Wichtig:** Es darf nur eine der Variablen verwendet werden! |
| **Referenz 2 auf Label **| Bestimme mithilfe der angezeigten Variablen, ob du zusätzliche Informationen auf dem UPS-Versandlabel abdrucken möchtest. Du kannst auch einen Freitext eingeben. Nutze diese Option, wenn eine einzige Referenz (Einstellung ** Referenz 1 auf Label **) für deinen Anwendungsfall nicht ausreicht. Folgende Variablen stehen dir zur Verfügung: {LIEFERSCHEIN}, {AUFTRAG}, {PROJEKT},{IHREBESTELLNUMMER}, {INTERNET}. ⚠️** Wichtig:** Es darf nur eine der Variablen verwendet werden! |
| **Volumengewicht** | Aktiviere diese Option, damit Xentral das Volumenbericht automatisch aus den Sendungsmaßen ermittelt und im Rahmen der Sendungsanmeldung an den Versanddienstleister überträgt. |
| **Adressvalidierung deaktivieren** | Aktiviere diese Option, um die Adressprüfung durch UPS zu deaktivieren. |
| **Export Grund **|** Nur bei internationalem Versand relevant**: Trage hier den Exportgrund ein. Mögliche Angaben sind: - SALE<br>- GIFT<br>- SAMPLE<br>- RETURN<br>- REPAIR<br>- RETURN<br>- INTERCOMPANYDATA |
| **Logging **| Aktiviere diese Option, um den Datenaustausch mit dem Versanddientleister zusätzlich in einer XML-Datei zu protokollieren. Die Datei wird dann lokal im Verzeichnis ** userdata/tmp** abgelegt. |
| **Tracking-Nummer in Auftrag übernehmen** | Aktiviere diese Option, um die Tracking-Nummer nach der Erstellung des Versandlabels direkt im dazugehörigen Auftrag in Xentral zu übernehmen. So bleibt die Tracking-Nummer dauerhaft in deinem System vermerkt und du musst das Versandlabel nach der Erstellung nicht erneut scannen, um diese Daten in Xentral zu erfassen. |
| **ZPL als Ausgabeformat **| Aktiviere diese Option, um das Versandlabel im ZPL-Format und nicht als PDF anzufragen. Bei ZPL (Zebra Programming Language) handelt es sich um ein spezielles Dateiformat für Zebra-Etikettendrucker. 💬** Anmerkung:** ZPL-Dateien erhalten standardmäßig keine Dateiendung und können nicht manuell geöffnet werden, da sie für die direkte Verarbeitung durch den Etikettendrucker gedacht sind. Möchtest du den Inhalt einer ZPL-Datei prüfen, kannst du dies mit einem so genannten ZPL Viewer (online verfügbar) tun. |
| **UPS Sandbox (Testmodus): **| Aktiviere diese Option, um den Druck von Versandlabels vor dem produktiven Einsatz mit der UPS Sandbox zu testen. Jedes Versandlabel, das im Sandbox-Modus erstellt wird, ist durch einen speziellen Aufdruck als ** SAMPLE** gekennzeichnet und wird somit auch nicht abgerechnet. |
| **UPS Quantum View Notify** | Aktiviere diese Option, um deinen Kunden die Ankunftsvorhersage von UPS automatisch zusenden zu lassen. So werden Kunden durch UPS selbst über die anstehende Auslieferung ihrer Sendung informiert. |
| **Paperless Invoice** | |
| **JIT-Komponenten von CN22-Formular ausschließen **|** Nur bei internationalem Versand relevant **: Aktiviere diese Option, um die einzelnen Komponenten von Just-in-Time -Stücklisten nicht auf dem CN22-Formular aufzuführen, falls derartige Artikel in der Sendung enthalten sind. Wenn diese Option aktiviert ist, wird nur der Kopf- bzw. Hauptartikel der Stückliste aufgeführt. ⚠️** Wichtig:** Stelle beim Versand von Stücklistenartikeln immer sicher, dass alle benötigten zollrelevanten Daten (Zolltarifnummer, Herkunftsland, Gewicht) korrekt in den Stammdaten der Artikel gepflegt sind, da es ansonsten zu Fehlern bei der Erstellung des Versandlabels kommt. Stelle die Vollständigkeit dieser Informationen sicher, egal ob du die vorliegende Option aktivierst oder deaktivierst. Zolltarifnummer, Herkunftsland und Gewicht pflegst du in den entsprechenden Feldern unter Verkaufen > Artikel > Artikel öffnen > Tab: Details > Bereich: Hersteller. Weitere Informationen zum Thema Just-in-Time-Stücklisten findest du im Artikel [Stückliste](https://help.xentral.com/hc/de/articles/360019652739#UUID-443f8048-37aa-3974-fc46-63cd8ad757d1). |
| **Auto-Fallback für den HS-Code **|** Nur bei internationalem Versand relevant **: Falls für einen in der Sendung erhaltenen Artikel keine Zolltarifnummer in den Artikelstammdaten in Xentral hinterlegt ist, schlägt die Erzeugung des Versandlabels fehl. Du kannst diesen Fehler verhindern, indem du hier eine Zolltarifnummer eingibst, die genutzt wird, falls keine Zolltarifnummer in den Artikelstammdaten gepflegt ist. ⚠️** Wichtig:** Wir empfehlen außerdem, alle Artikelstammdaten sorgfältig zu pflegen, damit es nicht zu Fehlern kommt. Die Zolltarifnummer pflegst du unter Verkaufen > Artikel > Artikel öffnen > Tab: Details > Bereich: Hersteller. |
| **Rechnungsstellung an Drittanbieter (Zölle und Steuern)**| Aktiviere diese Option, wenn die Versandkosten nicht dir selbst als Absender, sondern einer dritten Person oder Unternehmen in Rechnung gestellt werden sollen. Bei den UPS-Abrechnungsmodellen ** Freight Collect ** (Empfänger zahlt die Versandkosten) und ** Third Party** (Drittanbieter zahlt die Versandkosten) ist es notwendig, diese Option zu aktivieren. |
| **Drittanbieter-Kundennummer **| Im Fall des UPS-Abrechnungsmodells ** Third Party** gibst du hier die UPS-Kundennummer des Drittanbieters ein, der die Versandkosten übernimmt. UPS stellt diesem dann die Versandkosten in Rechnung. |
| **Drittanbieter-PLZ / Land **| Im Fall des UPS-Abrechnungsmodells ** Third Party** gibst du hier die Postleitzahl und das Land des Drittanbieters ein, der die Versandkosten übernimmt. |

## Versandlabel drucken

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Druck von Versandlabels im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Gehe dazu wie folgt vor.

1. Öffne per Klick auf das Stift-Symbol rechts einen Lieferschein im Modul **Lieferschein**.
1. Öffne das Tab **Details**.
1. Scrolle nach unten, bis du den Bereich **Lieferschein** erreichst.
1. Wähle die Versandart **UPS (OAuth **) aus dem Dropdown-Menü ** Versandart**aus.
1. Klicke auf **Speichern**.
1. Öffne das Tab **Versandlabel**.
1. Passe, falls nötig, die Adressdaten an.
1. Klicke auf **Versandlabel drucken**.
1. Lade das Versandlabel herunter. Anschließend kannst du es öffnen und auf etwaige Fehler prüfen.

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss das Versandlabel im UPS-Geschäftskundenportal stornieren.

> **Anmerkung**
>
> Beachte, dass UPS-Versandlabels nur stornieren kannst, solange sie noch nicht von UPS bei dir abgeholt wurden. Nicht verwendete Versandlabels kannst du bis zu einer Frist von 90 Tagen stornieren.

## Häufige Fehlermeldungen und Lösungen

Die folgenden Fehlermeldungen können bei Verwendung der Versandart **UPS (OAuth)** auftreten:

| Fehlermeldung | Erläuterung und Lösung |
| --- | --- |
| **The request is not well formed **| Einige deiner Daten in der Versandart enthalten mindestens ein Sonderzeichen (z.B. **&** oder*****). Bitte überprüfe, ob dein Nutzername, Passwort oder andere Daten Sonderzeichen enthalten und entferne diese. |
| **Missing or invalid ShipTo PhoneNumber Code: 120209** | Diese Fehlermeldung tritt auf, wenn es Probleme mit der angegebenen Telefonnummer gibt. Dafür gibt es zwei mögliche Gründe: Die Telefonnummer ist in irgendeiner Weise falsch (z.B. zu kurz) oder fehlt. Die Telefonnummer kann aufgrund deiner DSGVO-Einstellungen nicht übertragen werden. Nutze die Smart Search, um das Modul Grundeinstellungen zu öffnen und klicke dort auf das Tab System. Im Bereich DSGVO Einstellungen darf die Option Telefon nicht dem Versandunternehmen übergeben nicht aktiviert sein. |
| **Failed to refresh oauth token** | Deine Authentifizierung wurde von UPS abgelehnt. Du kannst diesen Fehler beheben, indem du deine Authentifizierung wie folgt erneuerst: Öffne deine Versandart UPS OAuth und klicke neben der Einstellung UPS OAuth-Verbindung auf Info. Klicke auf Autorisierung widerrufen. Öffne erneut deine Versandart und klicke neben dem Feld UPS OAuth-Verbindung auf Verbinden. Du wirst zu UPS weitergeleitet und kannst deine Autorisierung erneuern. |
| **Missing or invalid ship to attention name (ErrorCode:120201)** | Dieser Fehler tritt auf, wenn das Feld für den Namen des Empfängers in der Lieferadresse entweder leer ist, ungültige Zeichen enthält oder die maximale Zeichenanzahl von 35 überschritten wurde. Prüfe die Eingaben für den Empfängernamen und korrigiere sie, falls nötig. |
| **Missing or invalid ship to address line 1 (ErrorCode:120202)**| Bei diesem Fehler kann UPS die Adresszeile 1 nicht interpretiere. Das bedeutet, dass das Feld ** Straße/Hausnummer **entweder leer ist oder ungültige Zeichen enthält. Prüfe die Eingaben im Feld ** Straße/Hausnummer** und korrigiere sie, falls nötig. |