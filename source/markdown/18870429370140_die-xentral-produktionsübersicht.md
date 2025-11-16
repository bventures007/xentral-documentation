In diesem Artikel zeigen wir dir den grundsätzlichen Aufbau der Produktionsübersicht. Außerdem findest du detaillierte Erklärungen der Menüs und Aktionen, die dir dort zur Verfügung stehen.

Um das Produktionsmodul zu erreichen, folge dem PfadLager > Produktionoder suche über die Smart Search nach “Produktion”. Du befindest dich dann direkt in der Produktionsübersicht.

> **Tipp**
>
> Das Produktionsmodul wird in Xentral NextGen standardmäßig nicht in der Navigationsleiste auf der linken Seite angezeigt. Du kannst das Modul der Navigationsleiste für deinen Benutzer hinzufügen, indem du den Anweisungen im folgenden Artikel folgst:Individuelle Navigationsleiste einrichten.

## Reiter Übersicht

Die sog. Produktionsübersicht, der ReiterÜbersicht, ist die tabellarische Ansicht aller Produktionen. Hierüber kannst du

- dir einen Überblick über alle Produktionen und ihren Status verschaffen
- eine einzelne Produktion per Aktionsmenü bearbeiten
- mehrere ausgewählte Produktionen über die Stapelverarbeitung bearbeiten

### Produktionsstatus

Generell sind folgende Status in der Produktion möglich:

`ANGELEGT `→` FREIGEBEN `→` GESTARTET `→` ABGESCHLOSSEN ` (→` STORNIERT`)

Angelegte, aber noch nicht freigegebene Produktionen findest du unter der Schaltflächein Bearbeitung

![Produktionsubersicht_InBearbeitung.png](https://help.xentral.com/hc/article_attachments/19368060548636)

Zur besseren Übersicht empfiehlt es sich, die Anzahl der Vorgänge in diesem Reiter gering zu halten, indem du Produktionen entweder zur weiteren Verarbeitung freigibst oder indem du verworfene Produktionen, die du z. B. nur für Planungszwecke angelegt hast, regelmäßig löschst.

Alle Produktionen, die über den Status `ANGELEGT` hinaus gehen, findest du unter der SchaltflächeProduktionssuche.

![Produktionsubersicht_Produktionssuche.png](https://help.xentral.com/hc/article_attachments/19368093772188)

### Filterfunktionen

Die Filterfunktionen helfen dir, die angezeigten Produktionen einzugrenzen, um dich optimal auf deinen Bearbeitungszweck fokussieren zu können. Eine Kombination der Filter ist möglich.

Über den Statusfilter kannst du verschiedene Status ein- oder ausblenden. Ist kein Haken gesetzt, werden Produktionen aller Status angezeigt.

- Freigegebene: Zeigt alle Produktionen, die `FREIGEGEBEN` sind, aber noch nicht gestartet
- Gestartet: Zeigt alle `GESTARTETEN` Produktionen, die nicht storniert oder abgeschlossen sind
- Storniert: Zeigt alle `STORNIERTEN` Produktionen
- Abgeschlossen: Zeigt alle `ABGESCHLOSSENEN` Produktionen

Mit dem Filter kannst du Produktionen nach dem Materialstatus ein- und ausblenden:

- Material fehlt
- Material fehlt auf Produktionslager
- Material lagernd

### Monitor

Der Monitor zeigt dir den Status aller Schritte einer Produktion an.

| Status Freigabe | Material-verfügbarkeit | Status Material-Auslagerung | Status Erzeugnis-Einlagerung | Zeiterfassung | Status Lieferung |
| --- | --- | --- | --- | --- | --- |
| angelegt | | | | | |
| freigegeben | Material fehlt | Auslagerung noch nicht erfolgt | Einlagerung noch nicht erfolgt | keine Zeiten erfasst | Versand offen |
| gestartet | Material verfügbar | Auslagerung erfolgt | Einlagerung erfolgt | Zeiten erfasst | Versand erfolgt (oder nicht mit Auftrag verknüpft) |
| abgeschlossen | | Teilauslagerung erfolgt | Teileinlagerung erfolgt | | |
| storniert | | | | | |

### Mini-Detail

Diese Ansicht öffnest du über den Pfeil am linken Rand jeder Produktionszeile. Über sie kannst du Details zu einem Vorgang einblenden. So kannst du z. B. auf einen Blick den Lagerbestand deines Materials für eine Produktion überblicken.

![Produktionsubersicht_MiniDetail.png](https://help.xentral.com/hc/article_attachments/19368093799836)

### Aktionsmenü

Das Aktionsmenü der Produktionsübersicht befindet sich am rechten Rand jeder Produktions-Zeile.

![Produktionsubersicht_Aktionsmenu.png](https://help.xentral.com/hc/article_attachments/19368093801500)

Du kannst eine einzelne Produktion über das Aktionsmenü

- zur Bearbeitung öffnen
- löschen/stornieren
- kopieren
- als PDF drucken
- mit Labels versehen

### Stapelverarbeitung

Die Stapelverarbeitung befindet sich am unteren Ende der Seite.

![Produktionsubersicht_Stapelverarbeitung.png](https://help.xentral.com/hc/article_attachments/19368093803164)

Über sie kannst du mehrere ausgewählte Produktionen

- Starten: Hiermit änderst du den Status der ausgewählten Produktion von `FREIGEGEBEN ` auf`GESTARTET`. Voraussetzung ist, dass das notwendige Material in ausreichender Menge verfügbar ist.
- Starten und Auslagern: Hiermit änderst du den Status der ausgewählten Produktionen von `FREIGEGEBEN ` auf`GESTARTET` und gelangst zum “Artikel für Produktion”-Dialog, mit dem du Material für die Produktion auslagern kannst. Voraussetzung ist, dass das notwendige Material in ausreichender Menge verfügbar ist.
- Als Sammel-PDF drucken: Hiermit erzeugst du eine PDF-Datei mit allen ausgewählten Produktionen. Die Datei enthält die allgemeinen Daten, die Fertigungsstückliste und die Arbeitsanweisung.
- Drucken: Mit dieser Funktion sendest du für jede ausgewählte Produktion ein eigenes PDF an den Spooler.
- Einlagern: Mit dieser Aktion lagerst du das hergestellte Erzeugnis einer Produktion ein.
- Auslagern: Hier gelangst zum “Artikel für Produktion”-Dialog, mit dem du Material für die ausgewählten Produktionen auslagern kannst. Voraussetzung ist, dass das notwendige Material in ausreichender Menge verfügbar ist.
- Abschließen inkl. Einlagerung: Hiermit lagerst du das hergestellte Erzeugnis einer Produktion ein und schließt die eine Produktion ab.

## Reiter Zeitplanung

Der ReiterZeitplanunggibt dir einen Überblick über die verschiedenen Prozessschritte in Kalenderform, hier in der AnsichtWoche.

![Produktionsubersicht_Zeitplanung.png](https://help.xentral.com/hc/article_attachments/19368060584988)

Folgende Farbcodierungen werden im Kalender verwendet:

- Blau: Bereitstellungsdatum
- Türkis: Produktionsprozess
- Orange: Auslieferungsdatum
- Grau: Abgeschlossene Vorgänge

Durch Klick auf einen Prozessschritt gelangst du in die Karte der betreffenden Produktion.

> **Anmerkung**
>
> Zwar lassen sich Prozessschritte in der Kalenderansicht verschieben, wir empfehlen jedoch, Änderungen am Datum nur in der Produktionskarte vorzunehmen.

## Reiter Beistellungen

> **Anmerkung**
>
> Der ReiterBeistellungenist nur relevant, wenn du Produktionsschritte bei externen Dienstleistern beauftragst, denen du Material beistellst. Nähere Informationen zur externen Produktion findest zuhier.

![Produktionsubersicht_Beistellungen.png](https://help.xentral.com/hc/article_attachments/19368060586908)

## Reiter Materialbestand berechnen

Dieser Reiter stellt dir einen Auszug aus dem[klassischen Bestellvorschlag](https://help.xentral.com/hc/de/articles/360016757859#UUID-b36d5a57-67bd-5185-edda-fd68cadb28a5)dar.

### Tab Lieferanten

In diesem Tab sind alle Lieferanten aufgelistet, von denen Material für die Produktion fehlt. Die Spalte Menge zeigt die Anzahl der fehlenden Artikelnummern. Rote Zahlen bedeuten eine Fehlmenge für echte Bedarfe, schwarze Zahlen beziehen sich auf eine Unterschreitung der Mindestlagermenge (Artikel → Details → Min. Lagermenge). Mit Klick auf Bestellvorschlag kannst du auf den klassischen Bestellvorschlag wechseln und von dort Bestellungen anstoßen.

![Produktionsubersicht_Materialbestand_Lieferanten.png](https://help.xentral.com/hc/article_attachments/19368093809948)

### Tab Fehlende Artikel

Hier findest du eine Liste aller fehlenden Artikelnummern und den dahinter stehenden Mengen und Produktionen. Von hier kannst du durch Klick auf Produktionsnummer die Produktion und beim Klicken der Artikelnummer den Artikel öffnen.

![Produktionsubersicht_Materialbestand_FehlendeArtikel.png](https://help.xentral.com/hc/article_attachments/19368093810844)

### Tab Nachbestellte Artikel

Diese Liste zeigt dir alle offenen Bestellungen, die Material für die Produktion enthalten. Von dort kannst du die jeweilige Bestellung zum Bearbeiten bzw. zum Betrachten als PDF öffnen.

![Produktionsubersicht_Materialbestand_NachbeestellteArtikel.png](https://help.xentral.com/hc/article_attachments/19368060592028)

## Reiter Seriennummern

Im ReiterSeriennummernwerden nur Produktionen aufgelistet, die

- mind. den Status `GESTARTET` haben. Angelegte oder freigegebene Produktionen sind hier nicht enthalten und
- mind. einen seriennummern-geführten Artikel enthalten. Das kann das Fertigerzeugnis sein, das können Bauteile oder beides sein.

Über das Aktionsmenü im Reiter Seriennummern kannst du ins Produktionszentrum wechseln und dort Seriennummern erzeugen/zuweisen/löschen:

![Produktionsubersicht_Seriennummern.png](https://help.xentral.com/hc/article_attachments/19368093814940)

## Reiter Chargen

Im ReiterChargenerhälst du einen Überblick über die in der Produktion eingesetzten und produzierten Chargen. Es werden nur Produktionen aufgelistet, die

- mind. den Status `GESTARTET` haben. Angelegte oder freigegebene Produktionen sind hier nicht enthalten und
- mind. einen chargengeführten Artikel enthalten, für den eine Chargen zugeordnet wurde. Das kann das Fertigerzeugnis sein, das können Bauteile oder beides sein.

Unter dem TabEingesetzte Chargensind alle chargengeführten Bauteile oder Bauteile mit Mindesthaltbarkeitsdatum aufgelistet mit der Angabe, in welcher Produktion sie verwendet wurden. Über das X am rechten Rand kannst du eine Zuweisung entfernen.

![Produktionsubersicht_Chargen.png](https://help.xentral.com/hc/article_attachments/19368060596124)

Unter dem TabProduzierte Chargenfindest du alle erzeugten Chargen bzw. Mindesthaltbarkeitsdaten der von dir produzierten Artikel. Über die Produktionsnummer kannst du zu einer betreffenden Produktion wechseln.

## Reiter Einstellungen

In diesem Reiter kannst du generelle Einstellungen zur Produktion und Produktionskorrektur vornehmen:

![Produktionsubersicht_Einstellungen.png](https://help.xentral.com/hc/article_attachments/19368060598684)

Wenn du im PDF der Arbeitsweisung Bilder andrucken möchtest, setze den entsprechenden Haken.

Im Rahmen der Produktionskorrektur hast du die Möglichkeit, den sog. “Untermengedialog” immer anzuzeigen und Buchungstexte für Unter- bzw. Übermenge anzupassen.