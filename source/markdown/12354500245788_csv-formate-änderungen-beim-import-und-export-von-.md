Bitte beachte, dass es seit Version 23.26.10 folgende Veränderungen beim Import und Export von CSV-Dateien gibt:

> **Anmerkung**
>
> Diese Änderungen wirken sich auf denImportundExportvon Stammdaten sowie aufBerichteaus.

## Änderungen in der Maskierung

Um maximale Kompatibilität zu gewährleisten, haben wir den Import & Export von CSV-Dateien den international gängigen Standards angepasst.

## Wichtige Hinweise für den CSV-Export

Beim Export aus Xentral muss nun zwingend ein Maskierungszeichen ausgewählt werden. Standardmäßig wird der Apostroph genutzt.

Während des Exports werden lediglich Zelleninhalte maskiert, die bestimmten Kriterien entsprechen, zum Beispiel:

- Text mit Leerzeichen
- Zellen mit Zeilenumbrüchen

Das bedeutet, dass ab sofort nicht mehr alle exportierten Zellen automatisch maskiert sind. Bitte überprüfe, ob Skripte auf eurer Seite entsprechend angepasst werden müssen.

## Wichtige Hinweise für den CSV-Import

Wenn ein Datenfeld bereits Anführungszeichen oder Hochkomma hat, wird dies durch das Standard-CSV-Format verdoppelt. Zum Beispiel:

- HTML Links sollen in eine Artikel-Beschreibung importiert werden:
  <a href="https://xentral.com">xentral</a> muss zukünftig mit zwei Hochkommas angegeben werden: <a href=""https://xentral.com"">xentral</a>.

Am besten ist hier der Apostroph als Maskierung zu nutzen, damit CSV-Editoren die Texte richtig erkennen.

## CSV-Import in Tabellenkalkulationssoftware

Solltest du die von Xentral exportierten Daten anschließend in Microsoft Excel weiterverarbeiten wollen, wähle bitte als Maskierung das Anführungszeichen ", da Excel lediglich dieses unterstützt. Als Alternative zu Excel kannst du auch LibreOffice oder OpenOffice nutzen.