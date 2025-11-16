Willkommen auf unserer FAQ-Seite! Hier findest du Antworten auf die am häufigsten gestellten Fragen zur Druckeranbindung und zum XentralSpooler. Diese Seite bietet dir schnelle und hilfreiche Informationen, die dir bei der Nutzung unserer Plattform weiterhelfen. Ob zur Einrichtung, Fehlerbehebung oder für Tipps zur optimalen Nutzung – unsere FAQ bieten dir umfassende Unterstützung.

## Wie funktioniert die Spooler-App?

Die Spooler-App fragt einmal pro Sekunde bei Xentral nach Druckaufträgen. Wenn vorhanden, holt die Spooler-App maximal 10 Druckaufträge ab und versieht diese in Xentral mit dem Status **processing **. Anschließend sendet die Spooler-App jeden Druckauftrag einzeln an den jeweiligen Drucker. Sobald der Drucker mit dem Druckauftrag fertig ist (erfolgreich oder fehlgeschlagen), markiert die Spooler-App den jeweiligen Druckauftrag als ** completed **oder ** failed**.

Der Prozess läuft wie folgt ab:

1. Empfang des Druckauftrags in der Spooler-App
1. Sicherung der Datei auf der Festplatte (damit der Drucker darauf zugreifen kann)
1. Ausführung des Druckbefehls (mit Pfad zur Datei)
1. Löschung der Datei von der Festplatte nach dem Druck

## Was bedeuten die Status der Druckaufträge?

Die Druckaufträge im Menü **Druckaufträge** in Xentral haben folgende Bedeutung:

| Status | Bedeutung |
| --- | --- |
| **created** | Der Druckauftrag wurde erstellt, aber nicht von der Spooler-App abgeholt (z.B. keine Internetverbindung, App nicht gestartet). |
| **pending** | Der Druckauftrag wurde von der Spooler-App abgeholt, aber noch nicht bearbeitet (er befindet sich in der Warteschlange des Betriebssystems). |
| **processing **| Dieser Status wird gesetzt, sobald die Spooler-App die Druckaufträge bearbeitet, z.B. sobald sie aus Xentral abgeholt werden. Bleiben Druckaufträge auf ** processing**, bedeutet dies, dass das Betriebssystem oder der Drucker selbst keine Rückantwort an die Spooler-App sendet (z.B. durch einen Printer Timeout oder weil sich die Druckaufträge in der Warteschlange befinden). |
| **completed** | Das Dokument wurde erfolgreich gedruckt, zumindest wurde dies vom Betriebssystem an den Spooler zurückgemeldet. Wenn Dokumente trotzdem nicht gedruckt werden, liegt ein Problem beim Betriebssystem oder Drucker vor. |
| **failed **| Das Betriebssystem/der Drucker konnten den Auftrag nicht drucken. Bitte überprüfe die Fehlermeldung, die du im Menü ** Druckaufträge **ganz rechts in der Spalte ** Grund** findest. |

## Kann man Druckaufträge löschen?

Nein, Druckaufträge können nicht gelöscht werden. Du kannst entweder das Dokument herunterladen, um es manuell auszudrucken oder den Druckauftrag wiederholen (Retry). Für Retry gibt es derzeit noch keine Stapelverarbeitung.

## Das Druckformat ist falsch. Was kann ich tun?

Der Spooler ändert oder passt das Format nicht an. Falls du dies ändern möchtest, musst du dies extern tun, zum Beispiel im DHL-Geschäftskundenportal, wenn es sich um DHL-Versandlabels handelt, oder direkt in den Druckereinstellungen deines Betriebssystems.

> **Anmerkung**
>
> Der Spooler manipuliert keine Dateien, sondern druckt sie so, wie er sie erhält.

## Warum wird die Testseite nicht gedruckt?

Dieses Problem kommt insbesondere bei Etikettendruckern vor und liegt meist am Druckertreiber. Der Spooler ändert nichts am Format. Wenn der Druckertreiber das Format nicht verarbeiten kann, wird nichts gedruckt. Die Testseite-Vorlage ist immer im DinA4-Format. Versuche stattdessen, einen Beleg oder eine echtes Versandlabel zu drucken.

## Wie kann ich verschiedene Druckerfächer ansteuern?

Der Spooler bzw.Xentral sind nicht in der Lage, direkt verschiedene Druckerfächer zu bedienen. Als Workaround muss auf dem jeweiligen Rechner, auf dem die Spooler-App läuft, für jedes Fach ein eigener Drucker eingerichtet werden. Du musst sozusagen den Drucker im Betriebssystem duplizieren und in den Einstellungen jeweils ein Fach hinterlegen. Diese "Fächer" erscheinen dann im Spooler und müssen in Xentral jeweils als eigener Drucker hinterlegt werden. Du erstellst also eine Drucker-Konfiguration pro Fach.

## Benötige ich mehrere Spooler, wenn wir verschiedene Arbeitsplätze haben?

Nicht unbedingt. Grundsätzlich kann man, wenn die Spooler-App Zugriff auf alle Drucker hat, sich also alle Drucker im gleichen Netzwerk oder Server befinden, beliebige Drucker über einen Spooler bedienen, unabhängig davon, wie viele Benutzer sie nutzen und an welchem Standort sie sich befinden.

> **Anmerkung**
>
> Je weniger Spooler im Einsatz sind, desto performanter wird das System.

## Wie lege ich fest, welche Person welche Dokumente über welchen Drucker druckt?

InXentral kannst du die Bedienung deiner Drucker an den folgenden Stellen festlegen:

- **Automatischer Druck **: Hierzu findest du die relevanten Einstellungen direkt im Projekt (** Projekte > Projekt öffnen > Tab: Einstellungen > Tab: Logistik/Versand **) in den Abschnitten ** Versandprozess und Kommissionierung **, ** Stufe 1 (Pick/Kommissionierung ** und **Stufe 2 (Pack) an Versandstation **. Zusätzlich wird der automatische Druck in den Einstellungen der von dir genutzten Versandarten (** Versandarten > Versandart öffnen > Experte **) und in den Einstellungen deiner Picklisten-Profilen (Modul ** Picklisten-Profile**) gesteuert.
- **Manueller Druck **: In den Benutzereinstelliungen (** Benutzer > Benutzer öffnen > Tab: Sonstige Einstellungen ** legst du mithilfe der einstellungen **Standard Drucker **, ** Standard Etikettendrucker **, ** Drucker Stufe (Versand)** und **Drucker Stufe (Paketmarke)** fest, auf welche Drucker der Benutzer zugreifen kann.