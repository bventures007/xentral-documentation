**AUF INTERN GESETZT (12.11.2024) -> BITTE AUF DEN NEUEN GEHEN:****https://help.xentral.com/hc/de/articles/16853851788572-DATEV-Rechnungsdatenservice-1-0-Unternehmen-Online** DerDATEV Rechnungsdatenservice 1.0erlaubt es dir deine Buchhaltungsbelege (Rechnungen, Gutschriften, Verbindlichkeiten) direkt über eine API zu DATEV zu exportieren, d.h. der Export wird automatisch von Xentral zu DATEV übertragen. Alle Exporte werden in der Übersichtstabelle unten angezeigt.

![rechnungsdatenservice_protokoll.png](https://help.xentral.com/hc/article_attachments/13978378017180)

> **Anmerkung**
>
> Xentral unterstützt die Anbindung zur Version 1.0 des DATEV Rechnungsdatenservice. Die neuere Version 2.0 ist derzeit nicht kompatibel.

Du findest das Modul über dieSmart Searchoder im Standard in der Seitenleiste unterBuchhaltung > DATEVconnect Online.

## Verbindung zu DATEV herstellen

Bevor du den Export starten kannst, musst du eine Verbindung zu DATEV herstellen:

> **Anmerkung**
>
> Für den Export zu DATEV musst du außerdem deine Berater- und Mandantennummer für DATEV im ReiterEinstellungendes ModulsFinanzbuchhaltung Exporthinterlegen. Falls du das nicht bereits getan hast, findest du im folgenden Link weitere Informationen zur Einrichtung des Exports:Grundeinstellungen für den Buchhaltungsexport.
>
> Dein Steuerberater benötigt Administrationsrechte in DATEV, damit die Verbindung funktioniert. Wie du die Konfiguration in DATEV durchführst, erfährst du im folgenden Artikel im DATEV Hilfe-Center:Rechnungswesen 1.0 als Steuerberater in DATEV einrichten.

1. Navigiere zu Buchhaltung > DATEVconnect Online und öffne den Reiter Einstellungen.
1. Klicke auf Authentifizieren. Ein neuer Reiter öffnet sich in deinem Browser. Logge dich hier bei DATEV ein.
1. Wähle dein Anmeldeverfahren. Du kannst die folgenden Verfahren für die Zweifaktor-Authentifizierung wählen:
  - DATEV SmartCard / DATEV mIDentity: Ein separates Kartenlesegerät und Karte, die du von DATEV für eine sicherere Authentifizierung kaufen kannst. Das Kartenlesegerät mit Karte muss während des Anmeldevorgangs mit dem USB-Anschluss deines Computers verbunden sein.
  - DATEV SmartLogin: Eine kostenlose App für Smartphones und Tablets, mit der du dich über einen QR-Code anmelden kannst.
1. Klicke auf Weiter und melde dich mit dem ausgewählten Anmeldeverfahren an.
1. Klicke auf Ich stimme zu, um Xentral die Erlaubnis zu erteilen Daten mit DATEV auszutauschen.

Die Authentifizierung ist abgeschlossen und ein Authentifizierungstoken wird in Xentral hinterlegt. Du wirst zum ReiterEinstellungendes ModulsDATEV Rechnungsdatenservice 1.0in deiner Xentral-Instanz weitergeleitet.

Die Person, die sich in DATEV eingeloggt hat, wird im ReiterEinstellungenalsToken-Erstellerangezeigt. Die Gültigkeit des Tokens wird im FeldToken gültig bisangegeben.

## Einstellungen konfigurieren

Nachdem du[die Verbindung zu DATEV hergestellt](#UUID-c1b69d4d-77b1-306d-05ba-8c3f5e0fe54f_id_360016757739_id_Connection)hast, kannst du im ReiterEinstellungendie folgenden Einstellungen vornehmen:

- Import Benutzer: Alle Benutzer, die mit dem genutzten DATEV-Konto verbunden sind, werden hier aufgelistet. Wähle hier das Unternehmen aus, für das du deine Belege exportieren möchtest.
- Testzugang: Wähle diese Option, wenn du deine Belege testweise in die DATEV Sandbox exportieren möchtest, bevor du live gehst.
- Verbindlichkeit Datumsfilter: Wähle aus, ob deine Verbindlichkeiten nach Eingangsdatum oder nach Rechnungsdatum exportiert werden sollen.

## Belege exportieren

Du kannst deine Rechnungen, Gutschriften und Verbindlichkeiten direkt über eine API zu DATEV exportieren. Dies ist für einen Zeitraum von maximal einem Monat möglich.

> **Anmerkung**
>
> DATEV unterstützt nur Kundennummern, welche mindestens 6-stellig sind und nicht mit einer "0" beginnen.
>
> In der Oberfläche kannst du dies überAdresse > Zahlungskonditionen/Besteuerungenverändern. Nach der Änderung werden die Referenzen in den Belegen abgeändert, so dass diese anschließend erfolgreich exportiert werden können.

Gehe wie folgt vor, um deine Belege via API zu DATEV zu exportieren:

1. Navigiere zu Buchhaltung > DATEVconnect Online und öffne den Reiter Export.
1. Wähle den Typ des Belegs, den du exportieren möchtest. Du kannst aus Rechnungen, Gutschriften und Verbindlichkeiten im Dropdown-Menü wählen. Du kannst nur einen Belegtyp auf einmal exportieren.
1. Optional: Wähle ein Projekt. Nur Belege, die dem ausgewählten Projekt zugewiesen sind, werden exportiert. In den meisten Fällen sollte dieses Feld leer bleiben. Ein Export nach Projekt ist z.B. sinnvoll, falls du eine getrennte Buchhaltung benötigst.
1. Wähle das gewünschte Startdatum und Enddatum deines Exports. Start- und Enddatum müssen im selben Monat und Jahr liegen. Daraus folgt, dass du maximal einen Monat auf einmal exportieren kannst.
1. Optional: Setze ein Häkchen bei Bereits exportierte Dokumente ignorieren. Bei Nutzung dieser Option erkennt Xentral bereits exportierte Belege und exportiert diese kein zweites Mal.
1. Klicke auf Export.

Der Export wird nun zu DATEV übertragen und mit einem Zeitstempel und einem Status (Fehler oder Erfolgreich) in der untenstehenden Tabelle protokolliert.

Für jeden erfolgten Export wird der Zeitraum mit Zeitstempel und Status in den Belegtabellen protokolliert. Zusätzlich kannst du eine CSV-Datei des Exports durch einen Klick aufProtokollim jeweiligen Eintrag herunterladen. Diese Datei enthält Informationen zum Status der im Export enthaltenen Belege in DATEV.

> **Anmerkung**
>
> Das Protokoll ist nur fürXentral-Instanzen ab Version 24.14.6 verfügbar und nur für Exporte, die nach Update auf diese oder eine neuere Version durchgeführt wurden.

![rechnungsdatenservice_protokoll.png](https://help.xentral.com/hc/article_attachments/13978378017180)

## Fehlerbehebung

Wenn dir eine Fehlermeldung angezeigt wird, so gibt es verschiedene Maßnahmen, welche du durchführen kannst:

- Prüfe Beraternummer und MandantennummerunterFinanzbuchhaltungsexport > Einstellungen. Authentifiziere anschließend erneut und versuche dich mit dem DATEV Rechnungsservice zu verbinden.
- Prüfe die Einstellungen in DATEV selbst. Hier sollten alle Berechtigungen korrekt gesetzt sein (z.B. Steuerberater). Manchmal hilft es auch wenn du die Berechtigungen in DATEV löschst und erneut vergibst.
- Kürze den Exportzeitraum, z.B. auf einen Tag. Manchmal können bei längeren Zeiträumen Probleme auftreten.
- Erneuere den Access Token. Der Token der DATEV API ist aus Gründen der Datensicherheit nur wenige Stunden gültig. Daher kann die Fehlermeldung angezeigt werden, dass die Zugangsdaten nicht korrekt sind (bzw. "Error: invalid Grant").
- Erhältst du die Fehlermeldung: "Fehler: In DATEV Unternehmen online ist kein Bestand angelegt oder Wirtschaftsjahr vorhanden", sollte der für DATEV verantwortliche Mitarbeiter oder dein Steuerberater den DATEV Rechnungsservice 1.0 für Xentral aktivieren. In DATEV können sie dies auf die folgende Weise umsetzen:
- DATEV akzeptiert bis zu 5000 Dateien pro Export mit einer maximalen Dateigröße von 20 MB. Der kleinste Zeitraum der aus Xentral exportiert werden kann, ist ein Tag. Daraus folgt, dass du maximal 5000 Dateien pro Tag zu DATEV hochladen kannst. Exportierst du deine Belege in mehrere Dateiformate, wie XML und PDF, verringert dies die Anzahl der Belege, die du hochladen kannst, da pro Beleg mehrere Dateien benötigt werden.
  Ein Workaround für dieses Problem ist, die Belege herunterzuladen, in Gruppen kleiner als 5000 einzuteilen und sie manuell über die App [Finanzbuchhaltung Export](https://help.xentral.com/hc/de/articles/360016725100#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e) hochzuladen. Du kannst die Belege in der App im Bereich Datev Unternehmen Online links unten hochladen.