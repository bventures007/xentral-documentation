In diesem Artikel findest du alle wichtigen Informationen zur Anbindung der Versandplattform Shipcloud an Xentral.

Falls du schon bestehende Verträge mit einem oder mehreren Versanddienstleister hast, kannst du diese einfach bei Shipcloud hinterlegen. Wende dich dazu nach deiner Anmeldung bei Shipcloud an[support@shipcloud.io](mailto:support@shipcloud.io). Es ist ebenfalls möglich, spezielle Shipcloud-Rahmenverträge zu nutzen, sodass du gerade beim Einstieg sofort startklar bist und keine Direktverträge abschließen musst.

Die Anbindung von Shipcloud an Xentral funktioniert ganz einfach, indem du in Xentral eine Versandart anlegst und sie mithilfe deiner Zugangsdaten von Shipcloud konfigurierst. Wenn du später Versandlabels mit der Versandart **Shipcloud** erstellst, fordert Xentral das Versandetikett bei der Shipcloud-API an. Es dauert nur wenige Sekunden, bis dir das Versandlabel direkt in Xentral vorliegt und ausgedruckt werden kann! Anschließend nimmst du die restliche Versandabwicklung wie gewohnt in Xentral vor.

![shipcloud_process_diagram.jpg](https://help.xentral.com/hc/article_attachments/22351581196956)

> **Anmerkung**
>
> Arbeitest du bislang noch nicht mit Shipcloud zusammen oder möchtest du dir einen Überblick über den Funktionsumfang und die Vorteile dieser Lösung verschaffen? Dann schauhier bei Shipcloudvorbei, um mehr über eine mögliche Zusammenarbeit zu erfahren und eine kostenlose Testversion zu erhalten. Du benötigst zwingend einen Zugang zu Shipcloud, um die Schnittstelle in Xentral zu nutzen.

## Wann sollte ich Shipcloud verwenden?

Im Folgenden haben wir einige Gründe gesammelt, die je nach deinen eigenen Workflows und den Anforderungen deines Business für die Anbindung von Shipcloud an Xentral sprechen können.

- **Vielzahl von Versanddienstleistern**: Verfügst du bereits über direkte Verträge mit zwei oder mehr Versanddienstleistern? Dann kannst du dir mithilfe der Anbindung an Shipcloud die Übersicht erleichtern. Über deinen Shipcloud-Zugang kannst du auch diverse Versanddienstleister anbinden, die bislang über keine direkte Schnittstelle mit Xentral verfügen.
- **Transparenz bei der Sendungsverfolgung**: In Shipcloud kannst du invididuelle Paket-Vorabankündigungen konfigurieren, um deine Kunden jederzeit über den Status der Lieferung auf dem Laufenden zu halten.
- **Potential für eigene Entwicklungen**: Shipcloud bietet für technisch versierte Anwender oder IT-Abteilungen vielfältige Möglichkeiten für die Anbindung an die Shipcloud-API, sodass du auch komplexere Workflows, die über den Standard hinausgehen, abbilden kannst.

> **Anmerkung**
>
> Typische Anwendungsfälle:
>
> - Du möchtest Versandarten anbinden, die Xentral jedoch nicht direkt unterstützt (z.B. Angel, Sendia, Cargo International).
> - Wenn du (z. B. als Fulfiller) sehr viele verschiedene Versandarten und Verträge nutzt, kann die Anbindung über Shipcloud in Bezug auf die Administration von Vorteil sein.
> - Shipcloud bietet erweiterte Services, die leider nur über das Shipcloud-Portal selbst genutzt werden können. Um diese erweiterten Services nutzen zu können, musst du als Anwender dann zwei Systeme nutzen.

## Shipcloud an Xentral anbinden

Um Shipcloud in Xentral zu nutzen, legst du zunächst eine neue Versandart an. Anschließend verwendest du deine Zugangsdaten von Shipcloud, um die Versandart einzurichten.

> **Wichtig**
>
> Für die Anbindung von Shipcloud benötigst du einen aktiven Zugang zu Shipcloud. Nur dann verfügst du über den API-Schlüssel, der zwingend für die Einrichtung in Xentral benötigt wird. Im Folgenden erklären wir dir genau, wie du den API-Schlüssel abrufst.

### Zugangsdaten in Shipcloud abrufen

Für die Einrichtung der Versandart in Xentral benötigst du lediglich den API-Schlüssel. Gehe wie folgt vor, um den API-Schlüssel in deinem Shipcloud-Konto abzurufen:

1. Logge dich im [Shipcloud-Kundenportal](https://app.shipcloud.io/) ein.
1. Klicke oben rechts auf deinen **Benutzernamen ** und dann auf **API-Schlüssel**.
1. Kopiere den API-Schlüssel aus dem entsprechenden Feld.

### Versandart anlegen und Grundeinstellungen vornehmen

Im nächsten Schritt legst du eine neue Versandart in Xentral an und gibst dabei den API-Schlüssel ein, die du wie im Kapitel[Zugangsdaten in Shipcloud abrufen](#UUID-14505a80-a862-8655-e601-51658f36406b_section-idm234858040180779)beschrieben aus dem Shipcloud-Kundenportal kopiert hast.

1. Suche mithilfe der Smart Search nach **Versandarten**.
1. Klicke oben rechts auf **+NEU**.
1. Klicke auf **Shipcloud**.
1. Füge den API-Schlüssel, den du zuvor aus dem Shipcloud-Kundenportal kopiert hast, im Feld **Shipcloud API key** ein.
1. Klicke auf **Weiter**.
1. Wähle im Dropdown-Menü **Versandfirma** den Versanddienstleister aus, den du über Shipcloud angebunden hast.
1. Klicke auf **Weiter**.
1. Nimm im nächsten Schritt folgende Einstellungen vor:
  - **Projekt-Filter** (optional): Gib ein Projekt an, wenn du pro Verkaufskanal einen anderen Drucker für das Versandlabel verwenden möchtest.
  - **Drucker**: Wähle den gewünschten Drucker für das Versandlabel aus.
  - **Export Drucker**: Wähle den gewünschten Drucker für die Zolldokumente bei Exportsendungen aus.
1. Klicke auf **Weiter**.

Nachdem du die oben beschriebenen Einstellungen vorgenommen hast, kannst du nun entweder zusätzliche Einstellungen vornehmen oder direkt einen Lieferschein aufrufen, um zu Testzwecken ein Versandlabel zu drucken.

## Zusätzliche Einstellungen vornehmen

Wenn du Shipcloud bereits als Versandart angelegt hast oder die oben beschriebenen Grundeinstellungen für deine Anforderungen nicht ausreichen, kannst du die im Expertenmodus zusätzliche Einstellungen für die Versandart vornehmen.

1. Suche mithilfe der Smart Search nach **Versandarten**.
1. Klicke bei der Versandart, für die du Einstellungen vornehmen möchtest, rechts auf das **Stift-Symbol**.
1. Aktiviere im Bereich **Experte ** die Option**Zusätzliche Einstellungen anzeigen**.
1. Nimm die Einstellungen vor. Die Tabelle unten enthält detaillierte Informationen zu den verfügbaren Optionen.
1. Klicke auf **Speichern**.

> **Wichtig**
>
> Als Allererstes solltest du im Feld **API Key ** den API-Schlüssel aus dem Shipcloud-Kundenportal einfügen und einmalig auf**Speichern** klicken. Erst dann nimmst du die restlichen Einstellungen vor. Wie du den API-Schlüssel abrufst, ist im KapitelZugangsdaten in Shipcloud abrufenbeschrieben.

| Einstellung | Erläuterung |
| --- | --- |
| **Bezeichnung** | Hier findest du die Bezeichnung der Versandart, wie sie in Xentral beispielsweise bei der Auftragsbearbeitung angezeigt wird. Die Bezeichnung ist nur für dich und deine Mitarbeiter sichtbar. Achte darauf, dass jede Bezeichnung nur einmal in Xentral vorkommt, damit die Versandart stets eindeutig identifiziert werden kann. |
| **Typ **| Dies ist eine interne Feldbezeichnung, die für die Zuordnung bei deinen Online-Shops und anderen Verkaufsplattformen benötigt wird. Falls du über Shipcloud verschiedene Versanddienstleister nutzt, musst du für jede einzelne in Xentral eine eigene Versandart anlegen. Verwende hierbei für das Feld ** Typ **die folgenden eindeutigen Bezeichnungen: -** Angel → angel_de **<br>-** Cargo International → cargo_international **<br>-** Deutsche Post → dpag **<br>-** DHL → dhl **<br>-** DHL Express → dhl_express **<br>-** DPD → dpd **<br>-** FedEx → fedex **<br>-** GLS → gls **<br>-** Hermes → hermes **<br>-** iIoxx → iloxx **<br>-** PARCEL.ONE → parcel_one **<br>-** Seven Senders → seven_senders **<br>-** TNT → tnt **<br>-** UPS → ups** |
| **Modul** | Wähle das passende Modul aus dem Dropdown-Menü. Dabei muss der Modulname identisch zum Namen der Versandart sein, die du gerade einrichtest. |
| **Projekt **|** Optional**: Gib eine Projektzuordnung an. Diese wird benötigt, wenn du die Versandart auf einen bestimmten Verkaufskanal oder ein Projekt (beispielsweise eine spezifische Niederlassung) beschränken möchtest. Lasse das Feld leer, falls die Versandart in allen Projekten genutzt werden soll. |
| **Aktiv **| Aktiviere diese Option, sobald du alle benötigten Einstellungen für die Versandart vorgenommen hast. 💬** Anmerkung:** Nicht mehr verwendete Versandarten kannst du später deaktivieren. Beachte jedoch, dass deaktivierte Versandarten nur noch in bereits erstellten Belegen angezeigt werden. In neu erstellten Belegen und in Benutzerflächen wie der Auftragsübersicht oder in den Kundendaten steht eine deaktivierte Versandart nicht mehr zur Auswahl zur Verfügung. Du kannst Versandarten auch löschen. Dadurch wird jedoch auch die Versandhistorie gelöscht. Deshalb solltest du nur fälschlicherweise angelegte Versandarten löschen, die du nicht produktiv genutzt hast. |
| **Kein Portocheck** | Mit dieser Option kannst du den Porto-Check im Auftrag deaktivieren. Bleibt der Porto-Check aktiv, zeigt die Auftragsampel ein rotes Symbol für den Portocheck an, falls nicht mindestens ein Portoartikel in den Auftragspositionen enthalten ist. So wird verhindert, dass bei manuell angelegten Aufträgen der Portoartikel vergessen wird. Überlege anhand deiner eigenen Workflows und Arbeitsweise mit Xentral, ob du diese Option aktivieren oder deaktivieren willst. Legst du typischerweise viele Aufträge manuell in Xentral an, kann es sinnvoll sein, diese Option nicht zu aktivieren, sodass gerade bei hochpreisigen Artikeln oder internationalen Sendungen das Porto immer zuverlässig am Auftrag hinterlegt wird. |
| **Drucker Versandlabel** | Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für die Versandlabels genutzt werden soll. Beachte, dass hier nur Drucker auswählbar sind, die du bereits wie im Artikel[Deinen Drucker mit Xentral verbinden](https://help.xentral.com/hc/de/articles/360016756299#UUID-24ed3a57-a4df-da7a-08f6-141949df3855) in Xentral eingerichtet hast. Je nachdem, wie und wo der Versandprozess in deinem Unternehmen abläuft, kannst du hier genau den Drucker auswählen, den du benötigst - egal ob direkt am Schreibtisch oder am Packtisch im Lager. |
| **Drucker Export **|** Nur bei internationalem Versand relevant**: Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für Zollpapiere (CN23) genutzt werden soll. |
| **Versand E-Mail **| Lege hier fest, nach welchen Regeln Versandbenachrichtigungen per E-Mail an deine Kunden verschickt werden sollen, sobald sich die Sendung auf dem Weg befindet. Die folgenden drei Optionen stehen dir zur Verfügung: ** Standardverhalten **: Die Logistikeinstellungen aus dem Projekt werden verwendet. Diese Einstellungen nimmst du im Menü ** Einstellungen > Grundeinstellungen > Projekte > Projekt öffnen > Tab: Einstellungen > Tab: Logistik / Versand **vor. In den Bereichen ** Stufe 1 (Pick/Kommissionierung)**und ** Stufe 2 (Pack)**definierst du über die Checkboxen namens ** E-Mail **, bei welchen Schritten deine Kunden über den Stand der Auftragsbearbeitung informiert werden. ** Keine Versandmail **: Für diese Versandart wird keine Versandinformation per E-Mail versendet. ** Eigene Textvorlage **: Für diese Versandart wird die ausgewählte Textvorlage per E-Mail versendet. Diese Vorlage musst du vorab im Menü ** Einstellungen > Grundeinstellungen > Belege > Textvorlagen **erstellen. Anschließend wählst du die gewünschte Vorlage im Dropdown-Menü ** Textvorlage**aus. Durch diese Auswahl werden die Logistikeinstellungen des Projekts für diese Versandart nicht genutzt. |
| **Lieferungen unterstützt **| Diese Option wird bei der Anlage der Versandart standardmäßig aktiviert. Sobald du alle weiteren benötigten Einstellungen vorgenommen und die Versandart auf ** Aktiv** gestellt hast, kannst du die Versandart in Aufträgen, Lieferscheinen und im Versandzentrum auswählen. |
| **Retouren unterstützt** | Aktiviere diese Option, um zu erlauben, dass Retouren zu Aufträgen erstellt werden können, die ursprünglich mit der vorliegenden Versandart erstellt wurden. |
| **Bevorzugte Rücksendemethode** | Wähle eine bevorzugte Versandart für Retouren aus. Sobald in Xentral manuell eine Retoure zu einem Auftrag mit der vorliegenden Versandart angelegt ist, wird die hier gewählte Versandart automatisch im Retourenauftrag vorausgewählt. Diese Einstellung greift nur in Fällen der manuellen Retourenerstellung. |
| **API Key **| Gib hier erneut den API-Schlüssel aus dem Shipcloud-Kundenportal ein und klicke unten auf ** Speichern**. Erst dann kannst du weitere Einstellungen vornehmen. Wie du den API-Schlüssel abrufst, ist im Kapitel [Zugangsdaten in Shipcloud abrufen](#zugangsdaten-in-shipcloud-abrufen) beschrieben. |
| **Standardhöhe / Standardbreite / Standardlänge (in cm)**| Gib hier die Standardabmessungen deiner Pakete ein. Du kannst diese Angaben später bei Bedarf im Tab ** Versandlabel** des Lieferscheins ändern, bevor das Versandlabel erstellt wird. |
| **Absender aus den Einstellungen verwenden **| Entscheide, welche Absenderadresse auf deinen Shipcloud-Versandlabels abgedruckt werden soll. ** Option 1 **: Du lässt diese Option deaktiviert. In diesem Fall wird auf den Versandlabels die Absender-Adresse gedruckt, die du im Shipcloud-Kundenportal unter ** Einstellungen > Versandadressen ** festgelegt hast, und du musst keine Informationen in den folgenden Feldern zu den Absenderdaten eintragen. ** Option 2 **: Du aktivierst diese Option und hast dadurch die Möglichkeit, eine abweichende Absender-Adresse auf das Versandlabel zu drucken. In diesem Fall musst du die gewünschten Absenderinformationen in den folgenden Feldern eintragen. ⚠️** Wichtig:** Beachte, dass du auch im Shipcloud-Kundenportal selbst abweichende Absender- und spezielle Retourenadressen eintragen kannst (Einstellungen > Versandadressen). Überlege dir im Vorfeld, welche Absender- und Retourenadressen wirklich genutzt werden sollen und achte darauf, dass sich die Angaben in den Einstellungen der Versandart in Xentral und im Shipcloud-Kundenportal nicht widersprechen, um Fehler zu vermeiden. |
| **Absender Ansprechpartner Vorname / Nachname / Straße / Hausnummer / PLZ / Ort / Land / Bundesstaat / E-Mail / Telefon **| Diese Felder müssen nur ausgefüllt werden, wenn du die vorherige Option ** Absender aus den Einstellungen verwenden **aktiviert hast. Gib hier die Adressdaten der gewünschten Absenderadresse ein. ⚠️** Wichtig:** Im Feld Land wird eine Eingabe im ISO-Format (in der Regel zweistellig) erwartet. Beachtest du dieses Format nicht, kommt es zu Fehlern bei der Erstellung des Versandlabels. |
| **Versandfirma **| Wähle hier den Versanddienstleister aus, den du über Shipcloud nutzt, um ihn für die Versandart zu übernehmen. Wenn du mehrere Versandarten über Shipcloud verwendest, dann erstelle analog auch mehrere Versandarten in Xentral. Diese Versandarten unterscheiden sich am Ende nur über die Angaben in den Feldern ** Bezeichnung **, ** Typ ** und **Versandfirma**. |
| **Service **| Mithilfe dieser Einstellung kannst du einen zusätzlichen Versandservice auswählen und somit fest in der Versandart ** Shipcloud **hinterlegen. ⚠️** Wichtig:** Diese Einstellung greift nur für die Versanddienstleister DHL und DPD. Für andere Versanddienstleister ist hier keine Auswahl möglich. |
| **Mindestgewicht** | Trage hier das erforderliche Mindestgewicht deiner Sendungen ein. Jeder Wert größer als 0 ist erlaubt. Diese Einstellung ist optional und kann zudem je nach Versanddienstleister, den du über Shipcloud angebunden hast, abweichen. Erkundige dich im Zweifel bei deinem Shipcloud- Kundenbetreuer oder beim Xentral-Support, um zu erfahren, welche Angabe hier erwartet wird. |
| **Gewicht anpassen in **| Zur Erstellung des Versandlabels wird eine genaue Berechnung des Gesamtgewichts der Sendung inklusive Verpackungsmaterial benötigt.Xentral berechnet das Sendungsgewicht automatisiert im Hintergrund, indem das Gesamtgewicht der im Auftrag enthaltenen Positionen addiert wird. Mit der vorliegenden Option wird diesem Gewicht ein von dir festgelegtes Gewicht hinzugefügt. So entsteht ein Gesamtwert für die Versandanmeldung, der bei der Erstellung des Versandlabels berücksichtigt und automatisch an den Versanddienstleister gemeldet wird. Entscheide, ob das zusätzliche Gewicht des Verpackungsmaterials in ** kg **oder**%** angegeben werden soll. Mithilfe der folgenden Einstellung namens ** Gewicht anpassen um** definierst du das zusätzliche Gewicht genauer. |
| **Gewicht anpassen um **| Mithilfe dieser Einstellung bestimmst du deine Angaben für die Einstellung ** Gewicht anpassen in** näher. Gib hier das zusätzliche Sendungsgewicht je nach vorheriger Auswahl in Kilogramm oder Prozent ein. Für welche Berechnungsart und welche konkreten Werte du dich entscheidest, hängt von der Verpackungsart deiner Produkte und deinen verwendeten Verpackungsmaterialien ab. |
| **Tracking-Nr. ab Position **| Damit die Tracking-Nummer korrekt übernommen wird, musst du in der Versandart ** Shipcloud **die richtige Position der Tracking-Nummer angeben. Die hier angegebene Anzahl an Zeichen wird am Anfang der Tracking-Nummer abgeschnitten (z.B. bei** 4 ** und ** abcdef ** bleibt ** ef** übrig). |
| **Tracking-Nr. Länge** | Gib die Anzahl der Stellen der Tracking-Nummer ein. Wenn du das Feld leer lässt, wird die Tracking-Nummer vollständig, also mit allen Stellen übernommen. |
| **Additional Service Advance Meldung deaktivieren** | Aktiviere diese Option, um die Vorab-Benachrichtigung zum Versand, die Shipcloud normalerweise automatisch an deine Kunden verschickt, zu deaktivieren. |
| **Tracking übernehmen** | Aktiviere diese Option, um die Tracking-Nummer nach der Erstellung des Versandlabels direkt im dazugehörigen Auftrag in Xentral zu speichern. So bleibt die Tracking-Nummer dauerhaft in deinem System vermerkt und du musst das Versandlabel nach der Erstellung nicht erneut scannen, um diese Daten in Xentral zu erfassen. |
| **DPD Food **| Diese Einstellung muss nur aktiviert werden, wenn du den Lebensmittelversandservice DPD Food über Shipcloud nutzt. Du kannst sie nur aktivieren, wenn du bei der Einstellung ** Versandfirma **die Option ** DPD **gewählt und gleichzeitig die Einstellung ** Additional Service Advance Meldung deaktivieren** deaktiviert ist. |

## Versandlabel drucken

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Druck des Versandlabels im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Gehe dazu wie folgt vor.

1. Öffne per Klick auf das Stift-Symbol rechts einen Lieferschein im Modul **Lieferschein**.
1. Öffne das Tab **Details**.
1. Scrolle nach unten, bis du den Bereich **Lieferschein** erreichst.
1. Wähle die Versandart **Shipcloud ** aus dem Dropdown-Menü**Versandart** aus.
1. Klicke auf **Speichern**.
1. Öffne das Tab **Versandlabel**.
1. Passe, falls nötig, die Adressdaten an.
1. Klicke auf **Versandlabel drucken**.
1. Lade das Versandlabel herunter. Anschließend kannst du es öffnen und auf etwaige Fehler prüfen.

> **Wichtig**
>
> Nachdem dein Testdruck abgeschlossen ist, solltest du im Anschluss das Versandlabel direkt in deinem Shipcloud-Konto stornieren. Gehe dazu wie folgt vor.

1. Logge dich in das[Shipcloud-Kundenportal](https://app.shipcloud.io/) ein.
1. Klicke im Menü links auf **Versand ** und dann auf **Sendungen**.
1. Klicke rechts neben dem Versandlabel, das du stornieren möchtest, auf das rote **Papierkorb-Symbol**.

## Häufige Fehlermeldungen und Lösungen

In diesem Kapitel haben wir die Fehlermeldungen aufgelistet, die bei der Verwendung der Versandart **Shipcloud** in Xentral auftreten können.

| Fehlermeldung | Erläuterung |
| --- | --- |
| **Sender: country [XY] cannot be mapped to a known ISO country code **| Diese Fehlermeldung tritt auf, wenn du die Option ** Absender aus den Einstellungen verwenden **in den Einstellungen der Versandart aktiviert hast und im Feld ** Land **der Absenderadresse keinen ISO-Code eingegeben hast. Trage im Feld ** Land **das Land der Absenderadresse als zweistelligen ISO-Code ein. Klicke anschließend auf ** Speichern**. Das Versandlabel sollte sich nun wie gewünscht erstellen lassen. |
| **Modul nicht vorhanden **| Diese Fehlermeldung kann bei der Anlage der Versandart ** Shipcloud **in Xentral auftreten und führt dazu, dass du nicht mit den Einstellungen für die Versandart fortfahren kannst. Um diesen Fehler zu umgehen und mit der Einrichtung fortzufahren, klicke direkt zu Beginn auf ** Expertenmodus**, um zu den Einstellungen der Versandart zu gelangen. | |
| |
| **From can't be** | Diese Fehlermeldung tritt bei der Erstellung des Versandlabels auf. Prüfe, ob du im Shipcloud-Kundenportal eine Absenderadresse sowohl im Live-Modus als auch im Sandbox-Modus hinterlegt hast. Ergänze die Angaben bei Bedarf. Anschließend solltest du wie gewohnt das Versandlabel in Xentral erstellen können. |