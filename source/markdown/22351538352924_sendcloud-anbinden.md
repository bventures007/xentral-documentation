In diesem Artikel findest du alle wichtigen Informationen zur Anbindung der Versandplattform Sendcloud an Xentral.

Verfügst du bereits über bestehende Verträge mit einem oder mehreren Versanddienstleistern? Dann kannst du Sendcloud nutzen, um diese Verträge gebündelt an einer Stelle zu hinterlegen und den Versandprozess mit Sendcloud abzuwickeln. Aber auch, wenn du ohne Direktverträge neue Versanddienstleister nutzen möchtest, kannst du dies ganz unkompliziert mithilfe der verschiedenen Tarife bei Sendcloud umsetzen.

Die Anbindung von Sendcloud an Xentral funktioniert ganz einfach, indem du in Xentral eine Versandart anlegst und sie mithilfe deiner Zugangsdaten von Sendcloud konfigurierst. Wenn du später Versandlabels mit der Versandart **Sendcloud** erstellst, fordert Xentral das Versandetikett bei der Sendcloud-API an. Es dauert nur wenige Sekunden, bis dir das Versandlabel direkt in Xentral vorliegt und ausgedruckt werden kann! Anschließend nimmst du die restliche Versandabwicklung wie gewohnt in Xentral vor.

![sendcloud_xentral_process.jpg](https://help.xentral.com/hc/article_attachments/22351551522972)

> **Anmerkung**
>
> Arbeitest du bislang noch nicht mit Sendcloud zusammen oder möchtest du dir einen Überblick über den Funktionsumfang und die Vorteile dieser Lösung verschaffen? Dann schauhier bei Sendcloudvorbei, um mehr über eine mögliche Zusammenarbeit zu erfahren und eine kostenlose Testversion zu erhalten. Du benötigst zwingend einen Zugang zu Sendcloud, um die Schnittstelle in Xentral zu nutzen.

## Wann sollte ich Sendcloud verwenden?

Im Folgenden haben wir einige Gründe gesammelt, die je nach deinen eigenen Workflows und den Anforderungen deines Business für die Anbindung von Sendcloud an Xentral sprechen können.

- **Vielzahl von Versanddienstleistern**: Verfügst du bereits über direkte Verträge mit zwei oder mehr Versanddienstleistern? Dann kannst du dir mithilfe der Anbindung an Sendcloud die Übersicht erleichtern. Bei Sendcloud sind all deine bereits bestehenden Verträge, Produkte und Versandlabels übersichtlich in einem Dashboard zusammengefasst und jederzeit für dich zugänglich.
- **Unkomplizierte Erweiterungsmöglichkeiten**: Weißt du bereits heute, dass du in Zukunft mit zusätzlichen Versanddienstleistern zusammenarbeiten möchtest? Dann kannst du über Sendcloud jederzeit ganz einfach die Produkte weiterer Dienstleister hinzubuchen, ohne umständlich weitere Direktverträge abschließen zu müssen.
- **Flexible Konditionen und Internationalisierung**: Bei Sendcloud profitierst du je nach Sendungsvolumen von flexiblen Preisplänen, beispielsweise für Startups. So bindest du ganz einfach und ohne Risiken oder Direktverträge weitere Versanddienstleister an. Für deine Zukunftspläne stellt Sendcloud außerdem den Zugriff auf eine Vielzahl von internationalen Versanddienstleistern bereit, wann immer du ihn benötigst.
- **Nahtlose Integration in Xentral **: Du musst die Versandart ** Sendcloud** nur ein einziges Mal in Xentral anlegen und nicht mühsam für jeden Versanddienstleister einzeln Einstellungen vornehmen.

## Sendcloud an Xentral anbinden

Um Sendcloud in Xentral zu nutzen, legst du zunächst eine neue Versandart an. Anschließend verwendest du deine Zugangsdaten von Sendcloud, um die Versandart einzurichten.

> **Wichtig**
>
> Für die Anbindung von Sendcloud benötigst du einen aktiven Vertrag mit Sendcloud. Nur dann verfügst du über die Zugangsdaten, die zwingend für die Einrichtung in Xentral benötigt werden. Diese Zugangsdaten bestehen aus dem **Public Key ** und dem**Secret Key**. Im Folgenden erklären wir dir genau, wie du beides generierst.

### Zugangsdaten in Sendcloud generieren

Im ersten Schritt generierst du die Zugangsdaten, die du für die Einrichtung der Schnittstelle zu Sendcloud in Xentral benötigst. Gehe dazu wie folgt beschrieben vor.

1. Logge dich in das Sendcloud-Kundenportal ein. Folge dazu [diesem Link](https://account.sendcloud.com/login/).
1. Klicke unten links auf den Menüpunkt **Einstellungen ** und dann auf **Integrationen**.
1. Wähle die Option **Sendcloud API ** aus und klicke auf **Verbinden**.
1. Gib einen Namen für die Integration ein.
1. Klicke auf **Speichern**.
1. Kopiere die Zugangsdaten und lege sie an einem sicheren Ort ab, auf den du später noch Zugriff hast.

### Versandart anlegen und Grundeinstellungen vornehmen

Im nächsten Schritt legst du eine neue Versandart in Xentral an und gibst dabei die Zugangsdaten ein, die du wie im Kapitel[Zugangsdaten in Sendcloud generieren](#UUID-75fc5d54-519c-0c80-53bb-6742731ba842_section-idm234833894263277)beschrieben im Sendcloud-Kundenportal generiert hast.

1. Suche mithilfe der Smart Search nach **Versandarten**.
1. Klicke oben rechts auf **+NEU**.
1. Klicke auf **Sendcloud**.
1. Gib die Zugangsdaten **Public Key ** und **Secret Key** ein, die du zuvor im Sendcloud-Kundenportal generiert hast.
1. Klicke auf **Weiter**.
1. Nimm im nächsten Schritt folgende Einstellungen vor:
  - **Projekt-Filter** (optional): Gib ein Projekt an, wenn du pro Verkaufskanal einen anderen Drucker für das Versandlabel verwenden möchtest.
  - **Drucker**: Wähle den gewünschten Drucker für das Versandlabel aus.
  - **Export Drucker**: Wähle den gewünschten Drucker für die Zolldokumente bei Exportsendungen aus.
1. Klicke auf **Weiter**.

Nachdem du die oben beschriebenen Einstellungen vorgenommen hast, kannst du nun entweder zusätzliche Einstellungen vornehmen oder direkt einen Lieferschein aufrufen, um zu Testzwecken ein Versandlabel zu drucken.

### Zusätzliche Einstellungen vornehmen

Wenn du Sendcloud bereits als Versandart angelegt hast oder die oben beschriebenen Grundeinstellungen für deine Anforderungen nicht ausreichen, kannst du die im Expertenmodus zusätzliche Einstellungen für die Versandart vornehmen.

1. Suche mithilfe der Smart Search nach **Versandarten**.
1. Klicke bei der Versandart, für die du Einstellungen vornehmen möchtest, rechts auf das **Stift-Symbol**.
1. Wähle für die Option **Versender-Adresse ** aus, welche Absender-Adresse auf dem Versandlabel abgedruckt werden soll. Es stehen die Adressen zur Auswahl, die du im Sendcloud-Kundenportal unter **Einstellungen > Adressen** angelegt hast.
1. Aktiviere im Bereich **Experte ** die Option**Zusätzliche Einstellungen anzeigen**.
1. Nimm die Einstellungen vor. Die Tabelle unten enthält detaillierte Informationen zu den verfügbaren Optionen.
1. Klicke anschließend auf **Speichern**.

| Einstellung | Erläuterung |
| --- | --- |
| **Bezeichnung** | Hier findest du die Bezeichnung der Versandart, wie sie in Xentral beispielsweise bei der Auftragsbearbeitung angezeigt wird. Die Bezeichnung ist nur für dich und deine Mitarbeiter sichtbar. Achte darauf, dass jede Bezeichnung nur einmal in Xentral vorkommt, damit die Versandart stets eindeutig identifiziert werden kann. |
| **Typ **| Dies ist eine interne Feldbezeichnung, die für die Zuordnung bei deinen Online-Shops und anderen Verkaufsplattformen benötigt wird. ⚠️** Wichtig:** Verändere diese Bezeichnung nicht! |
| **Modul** | Wähle das passende Modul aus dem Dropdown-Menü. Dabei muss der Modulname identisch zum Namen der Versandart sein, die du gerade einrichtest. |
| **Projekt **|** Optional**: Gib eine Projektzuordnung an. Diese wird benötigt, wenn du die Versandart auf einen bestimmten Verkaufskanal oder ein Projekt (beispielsweise eine spezifische Niederlassung) beschränken möchtest. Lasse das Feld leer, falls die Versandart in allen Projekten genutzt werden soll. |
| **Aktiv **| Aktiviere diese Option, sobald du alle benötigten Einstellungen für die Versandart vorgenommen hast. 💬** Anmerkung:** Nicht mehr verwendete Versandarten kannst du später deaktivieren. Beachte jedoch, dass deaktivierte Versandarten nur noch in bereits erstellten Belegen angezeigt werden. In neu erstellten Belegen und in Benutzerflächen wie der Auftragsübersicht oder in den Kundendaten steht eine deaktivierte Versandart nicht mehr zur Auswahl zur Verfügung. Du kannst Versandarten auch löschen. Dadurch wird jedoch auch die Versandhistorie gelöscht. Deshalb solltest du nur fälschlicherweise angelegte Versandarten löschen, die du nicht produktiv genutzt hast. |
| **Kein Portocheck** | Mit dieser Option kannst du den Porto-Check im Auftrag deaktivieren. Bleibt der Porto-Check aktiv, zeigt die Auftragsampel ein rotes Symbol für den Portocheck an, falls nicht mindestens ein Portoartikel in den Auftragspositionen enthalten ist. So wird verhindert, dass bei manuell angelegten Aufträgen der Portoartikel vergessen wird. Überlege anhand deiner eigenen Workflows und Arbeitsweise mit Xentral, ob du diese Option aktivieren oder deaktivieren willst. Legst du typischerweise viele Aufträge manuell in Xentral an, kann es sinnvoll sein, diese Option nicht zu aktivieren, sodass gerade bei hochpreisigen Artikeln oder internationalen Sendungen das Porto immer zuverlässig am Auftrag hinterlegt wird. |
| **Drucker Versandlabel** | Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für die Versandlabels genutzt werden soll. Beachte, dass hier nur Drucker auswählbar sind, die du bereits [in Xentral eingerichtet](https://help.xentral.com/hc/de/articles/360016756299#UUID-24ed3a57-a4df-da7a-08f6-141949df3855) hast. Je nachdem, wie und wo der Versandprozess in deinem Unternehmen abläuft, kannst du hier genau den Drucker auswählen, den du benötigst - egal ob direkt am Schreibtisch oder am Packtisch im Lager. |
| **Drucker Export **|** Nur bei internationalem Versand relevant**: Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für Zollpapiere (CN23) genutzt werden soll. |
| **Versand-E-Mail **| Lege hier fest, nach welchen Regeln Versandbenachrichtigungen per E-Mail an deine Kunden verschickt werden sollen, sobald sich die Sendung auf dem Weg befindet. Die folgenden drei Optionen stehen dir zur Verfügung: ** Standardverhalten **: Die Logistikeinstellungen aus dem Projekt werden verwendet. Diese Einstellungen nimmst du im Menü ** Einstellungen > Grundeinstellungen > Projekte > Projekt öffnen > Tab: Einstellungen > Tab: Logistik / Versand **vor. In den Bereichen ** Stufe 1 (Pick/Kommissionierung)**und ** Stufe 2 (Pack)**definierst du über die Checkboxen namens ** E-Mail **, bei welchen Schritten deine Kunden über den Stand der Auftragsbearbeitung informiert werden. ** Keine Versandmail **: Für diese Versandart wird keine Versandinformation per E-Mail versendet. ** Eigene Textvorlage **: Für diese Versandart wird die ausgewählte Textvorlage per E-Mail versendet. Diese Vorlage musst du vorab im Menü ** Einstellungen > Grundeinstellungen > Belege > Textvorlagen **erstellen. Anschließend wählst du die gewünschte Vorlage im Dropdown-Menü ** Textvorlage**aus. Durch diese Auswahl werden die Logistikeinstellungen des Projekts für diese Versandart nicht genutzt. |
| **Lieferungen unterstützt **| Diese Option wird bei der Anlage der Versandart standardmäßig aktiviert. Sobald du alle weiteren benötigten Einstellungen vorgenommen und die Versandart auf ** Aktiv** gestellt hast, kannst du die Versandart in Aufträgen, Lieferscheinen und im Versandzentrum auswählen. |
| **Retouren unterstützt** | Aktiviere diese Option, um zu erlauben, dass Retouren zu Aufträgen erstellt werden können, die ursprünglich mit der vorliegenden Versandart erstellt wurden. |
| **Bevorzugte Rücksendemethode** | Wähle eine bevorzugte Versandart für Retouren aus. Sobald in Xentral manuell eine Retoure zu einem Auftrag mit der vorliegenden Versandart angelegt ist, wird die hier gewählte Versandart automatisch im Retourenauftrag vorausgewählt. Diese Einstellung greift nur in Fällen der manuellen Retourenerstellung. |
| **Standardhöhe / Standardbreite / Standardlänge (in cm)**| Gib hier die Standardabmessungen deiner Pakete ein. Du kannst diese Angaben später bei Bedarf im Tab ** Versandlabel** des Lieferscheins ändern, bevor das Versandlabel erstellt wird. |
| **Standardgewicht **| Gib hier das Standardgewicht deiner Pakete ein. Du kannst diese Angaben später bei Bedarf im Tab ** Versandlabel** des Lieferscheins ändern, bevor das Versandlabel erstellt wird. |
| **Gewicht anpassen in **| Zur Erstellung des Versandlabels wird eine genaue Berechnung des Gesamtgewichts der Sendung inklusive Verpackungsmaterial benötigt.Xentral berechnet das Sendungsgewicht automatisiert im Hintergrund, indem das Gesamtgewicht der im Auftrag enthaltenen Positionen addiert wird. Mit der vorliegenden Option wird diesem Gewicht ein von dir festgelegtes Gewicht hinzugefügt. So entsteht ein Gesamtwert für die Versandanmeldung, der bei der Erstellung des Versandlabels berücksichtigt und automatisch an den Versanddienstleister gemeldet wird. Entscheide, ob das zusätzliche Gewicht des Verpackungsmaterials in ** kg **oder**%** angegeben werden soll. Mithilfe der folgenden Einstellung namens ** Gewicht anpassen um** definierst du das zusätzliche Gewicht genauer. |
| **Gewicht anpassen um **| Mithilfe dieser Einstellung bestimmst du deine Angaben für die Einstellung ** Gewicht anpassen in** näher. Gib hier das zusätzliche Sendungsgewicht je nach vorheriger Auswahl in Kilogramm oder Prozent ein. Für welche Berechnungsart und welche konkreten Werte du dich entscheidest, hängt von der Verpackungsart deiner Produkte und deinen verwendeten Verpackungsmaterialien ab. |
| **Produkt **| Wähle das Produkt für das entsprechende Gewicht aus dem Dropdown-Menü aus. Die verfügbaren Versandprodukte kannst du im Sendcloud-Kundenportal einsehen. Alternativ kannst du das Produkt bei jedem Druck eines Versandlabels in Xentral neu auswählen, indem du die Option ** Auswahl im Paketmarkendialog** auswählst. Diese Option solltest du ebenfalls auswählen, wenn du keinen direkten Vertrag mit einem spezifischen Versanddienstleister hast, sondern lediglich mit Sendcloud zusammenarbeitest. |
| **Tracking-Nr. ab Position **| Damit die Tracking-Nummer korrekt übernommen wird, musst du in der Versandart ** Sendcloud **die richtige Position der Tracking-Nummer angeben. Die hier angegebene Anzahl an Zeichen wird am Anfang der Tracking-Nummer abgeschnitten (z.B. bei** 4 ** und ** abcdef ** bleibt ** ef **übrig). ⚠️** Wichtig:** Wenn du über einen separaten Vertrag mit DPD verfügst und diesen Versanddienstleister über die Versandart Sendcloud anbindest, musst du in diesem Feld zwingend den Wert 8 eintragen. |
| **Tracking-Nr. Länge** | Gib die Anzahl der Stellen der Tracking-Nummer ein. Wenn du das Feld leer lässt, wird die Tracking-Nummer vollständig, also mit allen Stellen übernommen. |
| **Tracking übernehmen** | Aktiviere diese Option, um die Tracking-Nummer nach der Erstellung des Versandlabels direkt im dazugehörigen Auftrag in Xentral zu speichern. So bleibt die Tracking.Nummer dauerhaft in deinem System vermerkt und du musst das Versandlabel nach der Erstellung nicht erneut scannen, um diese Daten in Xentral zu erfassen. |
| **Zusätzliche Versicherung deaktivieren **| Aktiviere diese Option, um im Tab ** Versandlabel** des Lieferscheins alle versicherungsrelevanten Auswahlfelder für eine zusätzliche Versicherung der Sendung auszublenden. Bleibt die Option deaktiviert, kannst du diese Felder bei Bedarf nutzen, um bei der Sendungsanmeldung Details über die Versicherungssumme an den Versanddienstleister zu übermitteln. |
| **JIT Komponenten von CN22 ausschließen** | Aktiviere diese Option, um die einzelnen Komponenten von Just-in-Time -Stücklisten nicht auf dem CN22-Formular aufzuführen, falls derartige Artikel in der Sendung enthalten sind. Wenn diese Option aktiviert ist, wird nur der Kopf- bzw. Hauptartikel der Stückliste aufgeführt. Stelle sicher, dass in diesem Fall alle benötigten zollrelevanten Daten (Zolltarifnummer, Herkunftsland, Gewicht) korrekt in den Stammdaten dieses Hauptartikels gepflegt sind, da es ansonsten zu Fehlern bei der Erstellung des Versandlabels kommt. Weitere Informationen zum Thema Just-in-Time-Stücklisten findest du im Artikel[Stückliste](https://help.xentral.com/hc/de/articles/360019652739#UUID-443f8048-37aa-3974-fc46-63cd8ad757d1). |

## Versandlabel drucken

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Versandlabeldruck im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Gehe dazu wie folgt vor.

1. Öffne per Klick auf das Stift-Symbol rechts einen Lieferschein im Modul **Lieferschein**.
1. Öffne das Tab **Details**.
1. Scrolle nach unten, bis du den Bereich **Lieferschein** erreichst.
1. Wähle die Versandart **Sendcloud ** aus dem Dropdown-Menü **Versandart** aus.
1. Klicke auf **Speichern**.
1. Öffne das Tab **Versandlabel** des Lieferscheins.
1. Falls du für die Einstellung **Produkt ** der Versandart die Option **Auswahl im Paketmarkendialog ** gewählt hast, wähle im Feld**Produkt** das passende Versandprodukt aus.
1. Klicke auf **Versandlabel drucken**.
1. Lade das Versandlabel herunter. Anschließend kannst du es öffnen und auf etwaige Fehler prüfen.

> **Wichtig**
>
> Nachdem dein Testdruck abgeschlossen ist, solltest du im Anschluss das Versandlabel direkt in deinem Sendcloud-Konto stornieren. Gehe dazu wie folgt vor.

1. Logge dich in das [Sendcloud-Kundenportal](https://account.sendcloud.com/login/) ein.
1. Öffne das Tab **Erstellte Labels**.
1. Aktiviere die Checkbox links, um ein oder mehrere Versandlabels für die Stornierung auszuwählen.
1. Klicke oben links auf das **Pfeil-Symbol ** direkt neben der Schaltfläche **Label drucken**.
1. Klicke auf **Abbrechen.**

## Häufige Fehlermeldungen und Lösungen

In diesem Kapitel haben wir die Fehlermeldungen aufgelistet, die bei der Verwendung der Versandart **Sendcloud** in Xentral auftreten können.

| Fehlermeldung | Erläuterung und Lösung |
| --- | --- |
| **parcel_items: ",,,,,,,"**| Diese Fehlermeldung wird direkt von Sendcloud an Xentral übergeben und tritt auf, wenn in den Artikelstammdaten keine oder eine fehlerhafte Angabe zum Herkunftsland vorhanden ist. Auch eine fehlende Gewichtsangabe in den Artikelstammdaten kann diesen Fehler verursachen, sodass die Erstellung eines Versandlabels nicht möglich ist. Öffne das Menü ** Verkaufen > Artikel > Artikel öffnen > Tab: Details **. Stelle sicher, dass im Feld ** Herkunftsland (ISO Code)**des Bereichs ** Hersteller **der korrekte ISO-Code des Herkunftslandes angegeben ist. Der Code ist in der Regel zweistellig. Das Artikelgewicht trägst du im Feld ** Gewicht (in kg)**im Bereich ** Lager/Abmessungen **ein. ⚠️** Wichtig:** Das Herkunftsland muss zwingend als ISO-Code angegeben werden, da ansonsten immer wieder die gleiche Fehlermeldung auftritt. |
| **Quantity must be at least 1** | Diese Fehlermeldung tritt bei der Erstellung des Sendcloud-Versandlabels auf, wenn sich im Lieferschein Positionen mit der Menge 0 befinden. Entferne die entsprechenden Positionen aus dem Lieferschein, indem du die nicht lieferbaren Positionen in eine Teillieferung oder einen Teilauftrag überführst. Anschließend kannst du das Versandlabel wie gewünscht erstellen. |
| **Für diese Lieferscheinkonfiguration ist kein Versandprodukt verfügbar.** | Diese Fehlermeldung tritt auf, wenn Abmessungen und/oder Gewicht deiner Sendung zu keinem deiner in Sendcloud gebuchten Versandprodukte passen, also beispielsweise zu groß sind. Überprüfe zunächst im [Sendcloud-Kundenportal](https://account.sendcloud.com/login/), welche Produkte du gebucht hast und welche Limitierungen gelten. Wende dich im Zweifel an den Xentral Support, um Unterstützung bei der Klärung zu erhalten. |
| **User not allowed to announce** | Diese Fehlermeldung wird direkt von Sendcloud an Xentral übergeben. Sie tritt auf, wenn die Einrichtung deines Sendcloud-Kontos noch nicht vollständig abgeschlossen wurde, oder du noch keine Zahlungsmethode für die Abrechnung und Zahlung deiner Versandlabels bei Sendcloud hinterlegt hast. Überprüfe zunächst den Status deines Kontos, indem du dich im [Sendcloud -Kundenportal einloggst](https://account.sendcloud.com/login/). Mehr zur Lösung findest du auch in den [Sendcloud API FAQs](https://support.sendcloud.com/hc/de/articles/7789894544276-Sendcloud-APIs-FAQ#h_01HV3G04DED0MBXR87817X2KEF). |