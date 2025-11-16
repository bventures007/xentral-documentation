> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Zentrale App für viele Anpassungen an Xentral ist die xentral Customizing Suite (XCS). Hier können bestehende Datenstrukturen erweitert und neue, eigene Datenstrukturen angelegt werden. Zusätzlich bietet die XCS Optionen für die Verwaltung von Anpassungen. Dieser Bereich wird in naher Zukunft stark ausgebaut werden.

## Beschreibung XCS

Neue Tabellen können z.B. schnell als Daten-Container für Anpassungen verwendet werden, z.B. wenn eine dynamische Liste von PLZ oder Versandarten erstellt werden soll, die dann im Prozess eine Entscheidung für eine Versandart pro PLZ ermöglicht. Diese wäre dann - bei geeigneter Programmierung - auch durch den Benutzer direkt erweiterbar ohne die Programmierung neu anstossen zu müssen. Es lassen sich beliebig viele Tabellen anlegen, die Speicherung solcher Listen kann also auch in mehreren Tabellen geschehen. Die Tabellen sind mit dem Prefix xcs_ einfach im Code ansprechbar.

Beispiel:

- Tabellenname in XCS: custom_table
- Tabellenname in Datenbank: xcs_custom_table

Vorhandene System-Tabellen können mit Hilfe eigener Spalten erweitert werden. Diese werden zunächst nur in der Datenbank erweitert, eine Auswirkung auf die Benutzeroberfläche ergibt sich nicht automatisch. Spalten können in eigene oder bereits vorhandene Datenbanktabellen eingefügt werden.

Bespiel: Erweiterung der Tabelle auftrag um zusätzliche Spalte 'Ablehnungsgrund'

### Datenbanktabellen definieren

Die Übersicht der Tabellen bildet den Einstiegspunkt zur Bearbeitung der Definition und der Daten in den Tabellen.

Folgende Funktionen sind verfügbar:

- Stift-Icon: zum Bearbeiten der Tabellendefinitiondefinition
- gebogener Pfeil: zum Bearbeiten der Inhalte der Tabelle (siehe unten)
- X: zum Löschen der Tabelle und aller gespeicherten Datendata

Datenbanktabellen können durch Klick auf+ NEUangelegt werden.

Es sind lediglich die Angaben für den Tabellennamen und eine optionale Beschreibung einzugeben. Eine Änderung des Tabellennamens führt auch im Nachhinein zu einer Änderung des Namens in der Datenbank.

### Spalten anlegencolumns

Im ReiterSpaltenkönnen alle verfügbaren Spalten aller Tabellen bearbeitet werden. Bitte beachten Sie, dass beim Verändern von Spaltendefinitionen die Inhalte der Spalten in der Datenbank gelöscht werden können.

Best Practise: Finales Definieren &amp; Anlegen von Tabellen und Spalten vor der ersten Verwendung oder Befüllung mit Daten.

Neue Spalten können durch Klick auf+ Neuer Eintragangelegt werden.

Beispiel für das Anlegen einer Ganzzahl-Spalte:

![xcs_7.png](https://help.xentral.com/hc/article_attachments/5078195197340)

Wichtig ist hierbei der TypGanzzahl. Soll ein Text in der Spalte gespeichert werden, ist als TypTextzu wählen.

### Daten bearbeiten

Wird eine Tabelle über das Pfeil-Icon aufgerufen, können die Inhalte der Tabelle bearbeitet werden. Neue Inhalte (Zeilen) können durch Klick auf + NEU angelegt werden.

Der angezeigte Dialog verwendet die hinterlegten technischen Spaltennamen und ist daher zur Bearbeitung durch nicht eingewiesene Endbenutzer nur bedingt geeignet.

![xcs_9.png](https://help.xentral.com/hc/article_attachments/5078180119708)

Die hinzugefügten Zeilen werden wie gewohnt angezeigt und können über das Stift-Icon editiert und über das X gelöscht werden.

### Systemtabellen erweitern

Auch zu vorhandenen Systemtabellen können neue Spalten hinzugefügt werden. Diese Methode sollte sparsam verwendet werden, auch weil die maximale Beschränkung der Zeilengröße in MySQL / MariaDB vor allem bei Verwendung der InnoDB (siehe MySQL-Dokumentation für Row Size Limits) zu Problemen führen kann. Die Erweiterung von Systemtabellen könnte zu Seiteneffekten innerhalb anderer Bereiche der Software führen.

Best Practise: Erstellen einer neuen Tabelle und Erweiterung der Systemtabelle lediglich um eine Referenz auf die neue Tabelle. Hierfür muss bei XentralTabelle erweitern ein Haken gesetzt werden.

![xcs_11.png](https://help.xentral.com/hc/article_attachments/5078147021468)

Die folgenden Systemtabellen können erweitert werden:

- adresse
- artikel
- angebot und angebot_position
- auftrag und auftrag_position
- rechnung und rechnung_position
- gutschrift und gutschrift_position
- lieferschein und lieferschein_position
- bestellung und bestellung_position
- produktion und produktion_position

## Datenbank: Browsen und Strukturen einsehen

Im Reiter SQL-Viewer können alle Datenbanktabellen des eigenen Systems live aufgerufen werden. Dort ist aus Performancegründen in einigen Fällen eine verkleinerte Ansicht der Tabellen verfügbar (nicht alle Zeilen oder Spalten).

Weitere Informationen zum Umgang mit der Datenbank (u.a. XAMPP zum lokalen Test) finden Sie auch unter[Report Scripts.](https://help.xentral.com/hc/de/articles/360017383780)