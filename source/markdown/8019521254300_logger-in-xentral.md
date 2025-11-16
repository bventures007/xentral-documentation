Logger sind dafür zuständig, die Ereignisse und Statusinformationen während des Betriebs von Xentral automatisch zu protokollieren. Bei den protokollierten Ereignissen und Informationen handelt es sich zum Beispiel um Systemnachrichten, Fehlermeldungen oder Statusmeldungen. In diesem Artikel bekommst du eine kurze Übersicht über die Logger in Xentral.

In den folgenden Abschnitten werden die verschiedenen Logger erläutert.

## Log File

Hierbei handelt es sich um den Systemlog. Der Logfile wird als Datei auf dem Server gespeichert und kann gegebenenfalls durch Ingenieure für Debugging Zwecke genutzt werden. Das ModulLog File(Logviewer) ließt den Logfile aus und macht die Informationen für den Nutzer in Xentral sichtbar. Der Logger ist immer aktiv und muss nicht extra aktiviert werden. In den Einstellungen (Log File > Einstellungen) kannst du wählen, welche Arten von Logleveln angezeigt werden sollen.

Hier eine kurze Übersicht zu den Logleveln

| Loglevel | Beschreibung |
| --- | --- |
| Warning | Außergewöhnliche Ereignisse, die keine Fehler sind. - Dinge, die es noch nicht gibt, die aber in Zukunft zu Problemen werden können<br>- Fallback-Szenario wegen unvollständiger Konfiguration verwenden<br>- Schlechte Performance<br>- Neben einer Warnmeldung auf dem Bildschirm könnte eine Warnprotokollmeldung erscheinen Es funktioniert so, aber es ist nicht ideal - das solltest du ändern. |
| Notice | Bemerkenswerte Ereignisse, mit denen Sie die Absicht eines Benutzers verstehen können. - Keine technischen Details oder Dumps!<br>- Max. eine pro Benutzeraktion<br>- Ein Cronjob gestartet/beendet<br>- z.B. "Benutzer XY hat einen neuen Lead erstellt." Was der Benutzer versucht hat, bevor die Anwendung abgestürzt ist. |
| Info | Häufige Ereignisse, die die Absicht eines Benutzers detaillierter beschreiben. - Ausführlichere Form von NOTICE. Kann hilfreich sein, um die genauen Aktionen des Benutzers zu reproduzieren. |
| Error | Abfangbarer Fehler, der die Anwendung nicht unterbricht. Fehlerprotokollmeldungen sollten dem Entwickler einen Hinweis geben, wo er nach einem Problem suchen kann. - Vorübergehendes Problem<br>- Fehlerantwort von einer anderen API<br>- Fehler, der vom Benutzer behoben werden könnte<br>- Eine Fehlerprotokollmeldung könnte zusammen mit einer „Fehler“-Meldung auf dem Bildschirm erscheinen<br>- Kann nach dem Neuladen der Seite behoben werden Diese Informationen sollten zumindest im Protokoll erscheinen, wenn ein Fehler gemeldet wird. |
| Emergency | Ein Notfallfehler sollte dazu führen, dass der Kunde den Support wegen „Notfallproblem“ anruft. - Sofortiges Handeln erforderlich<br>- Drohender Datenverlust<br>- Software ist nicht mehr lauffähig<br>- Nur ein erfahrener Systemadministrator oder unser Support kann das Problem lösen Der letzte Hilferuf, bevor die Anwendung stirbt. |
| Debug | Detaillierte Debug-Informationen. - Verfolge den Code bei Bedarf Zeile für Zeile<br>- Variable Dumps<br>- Technische Information Ich möchte ihr Produktionssystem nicht debuggen, also sage ich ihnen, sie sollen den DEBUG-Level einschalten und mir das Protokoll schicken. |
| Critical | Unbehandelte/unbekannte Fehler und Fehler, die dazu führen, dass eine Software nicht mehr funktioniert. Idealerweise sollten alle CRITICALs im Laufe der Zeit in ERRORs umgewandelt werden. - Komponente oder Abhängigkeit fehlt<br>- Unbehandelte Ausnahme (Ausnahmefehlerseite)<br>- Einzelne Seite/Modul/Cronjob kann nicht dauerhaft arbeiten Irgendetwas an diesem Modul ist dauerhaft kaputt - Aufmerksamkeit des Entwicklers erforderlich. |
| Alert | Verwenden Sie die Benachrichtigung in Fällen, in denen ein Administrator eine Benachrichtigung per E-Mail oder SMS wünscht. - Weniger schwerwiegend als ein Notfall<br>- Problem ist hartnäckig<br>- Der Systemadministrator kann das Problem beheben<br>- z.B. Datenbank kann nicht verbunden werden<br>- z.B. userdata hat keinen Speicher meh Hey DevOps, du musst das beheben! Anderenfalls sind einige/viele Menschen nicht arbeitsfähig. |

## Protokoll

Hierbei handelt es sich um eine Liste mit Aktionen, die der eingeloggte Nutzer in Xentral ausführt. Sie kann über das ModulProtokolleingesehen werden.

## Mailausgang Log

Der Mailausgang Log ist ein Logger für alle versendeten Mails und Fehler. Mehr Informationen erhältst du[hier](https://help.xentral.com/hc/de/articles/8718596261532#UUID-0209e297-82f9-2aa0-91f0-4a7b87bdd5b4).

## Systemlog

Die Logdatei des Systems mit allen wichtigen Informationen.

## System Health

Der LoggerSystem Healthzeigt den "Gesundheitszustand" des Systems an. Entdeckt das System an verschiedenen Stellen Unstimmigkeiten, wie etwa doppelte Nummern, Fehler beim Ausführen von Prozessstartern, einen vollgelaufenen Speicher o.Ä. wird eine Warn- oder Fehlermeldung in der System Health Übersicht erzeugt. Mehr Informationen zum Modul erhältst du[hier](https://help.xentral.com/hc/de/articles/360016725020#UUID-c4d97aa6-3ed1-272b-146c-bf5f28819ff3).