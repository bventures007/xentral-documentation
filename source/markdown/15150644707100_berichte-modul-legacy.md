### Achtung

Dieses alte Berichte Modul wird ersetzt durch[Berichte (neu)](https://help.xentral.com/hc/de/articles/14743167748252-Berichte-neu). Stand: 07/2024.

Stand 2025: Das erstellen von Berichten und Ausführung von Berichten im alten Berichtemodul wird abgekündigt zum 30.06.2025.

Verwende die Funktionen im neuen Berichtemodul. Bei Fragen und Problemen melde dich gerne bei unserem Support.

In NextGen:Berichtswesen > Berichte

Im Classic Design:Controlling > Berichte

Xentral bietet eine Vielzahl an Berichten, mit denen du verschiedenste Daten deiner Firma analysieren kannst, z.B. Anzahl angelegter Aufträge pro Mitarbeiter, erstellte Versandlabel in einem bestimmten Zeitraum, Umsatz pro Produkt, aktive Kundenabonnements und viele mehr.

Neben der Nutzung der existierenden Berichte kannst du auf Basis deiner Anforderungen eigene Berichte anlegen.

> **Wichtig**
>
> Das Anlegen eigener Berichte erfordert Erfahrung im Umgang mit SQL. Wenn du noch keine ausreichenden SQL-Kenntnisse hast, empfehlen wir dir, einen unsererPartnerzu kontaktieren. Er kann die gewünschten Berichte für dich anlegen.

Berichte könnten in verschiedenen Orten in der Software angezeigt werden oder heruntergeladen werden. Beim Download stehen dir folgende Formate zur Verfügung:

- CSV
- PDF

Du kannst dann mit den heruntergeladenen Daten in Drittsystemen wie Excel, Power BI oder Minubo weiterarbeiten.

Berichte werden in Form von Tafeln in der Berichtsübersicht angezeigt:

![Report_tile.png](https://help.xentral.com/hc/article_attachments/15150678442780)

Eine Berichtstafel enthält die folgenden Elemente:

| Element | Beschreibung |
| --- | --- |
| | Klicke auf das Sternchen, um den Bericht als Favoriten zu markieren. Das Sternchen wird dann gelb angezeigt. Die Markierung als Favorit bietet die folgenden Vorteile: - Wenn du das nächste Mal die Berichtsübersicht öffnest, werden die als Favoriten markierten Berichte zuoberst angezeigt und sind somit leichter für dich zu finden.<br>- Xentral bietet ein Filter, mit dem du nach deinen Favoriten suchen kannst. Wenn du diesen Filter anwendest, werden nur deine Favoriten angezeigt, wodurch die Navigation für dich erleichtert wird. |
| | Du kannst deinen Bericht einer Kategorie zuweisen, z.B. Buchhaltung & Finanzen, Lager & Logistik u.s.w., um ihn für einen Fachbereich zu kennzeichnen. Du kannst die Kategorie bei Anlage des Berichts auswählen oder aber auch, wenn du einen bestehenden Bericht bearbeitest. |
| | Mit einem Klick auf das Bearbeiten-Symbol kannst du deinen Bericht bearbeiten. Weitere Informationen zu den verfügbaren Feldern im Bearbeitungsmodus findest du im Abschnitt [Deinen Bericht anlegen und pflegen](#deinen-bericht-anlegen-und-pflegen). |
| | Mit einem Klick auf das Löschen-Symbol kannst du deinen Bericht löschen. |
| | Mit einem Klick auf das Kopieren-Symbol kannst du eine Kopie deines Berichts anlegen. Das ist besonders dann sinnvoll, wenn du verschiedene Berichte mit ähnlichen Einstellungen hast. |
| | Wenn du mit dem Mauszeiger auf das Informationssymbol gehst, wird eine Beschreibung deines Berichts angezeigt, wenn eine hinzugefügt wurde. Du kannst eine Beschreibung hinzufügen, wenn du einen Bericht anlegst oder einen bestehenden bearbeitest. |
| | | Name deines Berichts. |
| |
| | Mit einem Klick auf das Tabellen-Symbol werden die Berichtsdaten in Tabellenform im Reiter Ansicht des Berichts angezeigt. |
| | Mit einem Klick auf das CSV-Symbol kannst du deinen Bericht im CSV-Format als Download erstellen. |
| | Mit einem Klick auf das PDF-Symbol kannst du deinen Bericht im PDF-Format als Download erstellen. |

## Nach einem Bericht suchen

Xentral bietet verschiedene Optionen, nach einem bestimmten Bericht zu suchen oder zu filtern. Diese Optionen findest du über den Berichtskacheln in der Berichtsübersicht. Dir stehen hier die folgenden Filteroptionen zur Verfügung:

- Du kannst den Filter Nur eigene verwenden, wenn du nur von dir angelegte Berichte anzeigen möchtest. Die Xentral-Standardberichte werden ausgeblendet. Der Filter wird automatisch angewendet. Du musst zur Anwendung nicht auf Anwenden klicken.
- Um nur deine Favoriten anzuzeigen, klicke auf den Filter Nur Favoriten. Der Filter wird automatisch angewendet. Du musst zur Anwendung nicht auf Anwenden klicken.
- Möchtest du die Anzeige auf Berichte einer bestimmten Kategorie einschränken, z.B. Lager & Logistik, wähle die gewünschte Kategorie im Feld Kategorie aus. Klicke auf Anwenden, um passende Berichte zu finden.
- Möchtest du nach einem bestimmten Begriff im Berichtstitel suchen, z.B. Konten, gib den entsprechenden Suchbegriff in das Feld Suche ein. Klicke auf Anwenden, um die passenden Berichte zu finden.

Die vorhandenen Filter und Suchoptionen können kombiniert werden.

## Deinen Bericht anlegen und pflegen

> **Wichtig**
>
> Das Anlegen eigener Berichte erfordert Erfahrung im Umgang mit SQL. Wenn du noch keine ausreichenden SQL-Kenntnisse hast, empfehlen wir dir, einen unsererPartnerzu kontaktieren. Er kann die gewünschten Berichte für dich anlegen.

Du kannst einen neuen Bericht auf zwei Wegen anlegen - du kannst entweder einen komplett neuen Bericht anlegen oder einen ähnlichen Bericht kopieren und die Einstellungen auf Basis deiner Anforderungen anpassen. Die letztgenannte Option ist dabei die gängigere, da sie Zeit und Aufwand spart.

| Einen komplett neuen Bericht anlegen | Einen Bericht auf Basis eines bestehenden Berichts anlegen |
| --- | --- |
| Klicke im Bereich Aktionen auf +Neuer Eintrag. Das Fenster Neuer Bericht wird angezeigt. Gib einen Namen für deinen Bericht in das Feld Name ein und klicke auf Speichern. Zu diesem Zeitpunkt sind noch keine Einstellungen vorhanden. Bitte folge den nachfolgenden Anweisungen, um die erforderlichen Informationen hinzuzufügen. Suche nach deinem Bericht mit der Suchfunktion. | Suche in der Berichtsübersicht nach einem Bericht, der demjenigen ähnelt, den du anlegen möchtest. Die Suchoptionen in der Übersicht sind hier beschrieben. Klicke beim gewünschten Bericht auf das Kopieren-Symbol. Passe die Felder wie gewünscht an. Die Felder sind in nachstehender Anleitung erklärt. Vergiss nicht, deinen Bericht umzubenennen. Klicke auf Speichern. |

Dein Bericht ist angelegt und wird in der Berichtsübersicht angezeigt.

Du kannst nun deinen neuen oder bestehenden Bericht bearbeiten. Dieser Prozess besteht aus zwei Schritten:

1. [Deine Berichtseinstellungen bearbeiten](#deine-berichtseinstellungen-bearbeiten)
1. [Tabellenspalten anlegen, pflegen und löschen](#tabellenspalten-anlegen,-pflegen-und-loeschen)

### Deine Berichtseinstellungen bearbeiten

Gehe wie folgt vor, um deinen neuen oder bestehenden Bericht zu bearbeiten:

1. Klicke auf bei dem Bericht, den du bearbeiten möchtest. Der Reiter Details deines Berichts wird angezeigt.
1. Im Bereich Einstellung kannst du Folgendes hinzufügen, bearbeiten oder auswählen:
  - Name: Bei Anlage des Berichts bekommt der Bericht automatisch einen Namen. Diesen kannst du jederzeit bei Bedarf ändern.
  - Kategorie: Bei Bedarf kannst du deinen Bericht einer Kategorie zuweisen, das heißt einer Abteilung oder einem Bereich, für den der Bericht angelegt wird. z.B. Buchhaltung, Verkauf, etc.
  - Beschreibung: Gib eine Beschreibung deines Berichts ein. Diese Beschreibung wird angezeigt, wenn du mit dem Mauszeiger auf das Informationszeichen in der Berichtskachel in der Berichtsübersicht gehst.
  - Projekt: Bezieht sich dieser Bericht auf ein bestimmtes Projekt, kannst du das passende Projekt in diesem Feld auswählen.
  - Aus Datei laden: Mit einem Klick auf Datei auswählen kannst du Informationen aus einer bestehenden JSON-Datei laden. Im Allgemeinen lädst du hier Dateien hoch, die du mittels der Schaltfläche Definitionsdatei unten im Reiter Details anderer Berichte in Xentral heraus angelegt hast.
  - Variablen: Mehr Informationen zu Variablen und dazu, wie du diese anlegst, findest du [hier](#UUID-14597dcc-d945-c257-1864-cd30ac61a416_section-idm459181717663043342398997836).
1. Im Bereich Struktur kannst du das passende SQL-Statement für deinen Bericht hinzufügen.
  Du kannst dein SQL-Statement testen. Klicke dazu auf die Play-Schaltfläche neben dem Feld SQL Statement. Das Ergebnis findest du im Feld Ergebnis.

  Beachte dabei Folgendes:

  [Am Ende dieses Dokuments](#UUID-14597dcc-d945-c257-1864-cd30ac61a416_section-idm4582677074606433649711547582) findest du ein Beispiel für eine SQL-Anfrage als Referenz.

  - Die SQL-Befehle UPDATE und SET können nicht verwendet werden, da diese Konflikte verursachen können.
  - Die Benutzertabelle und andere Tabellen, die den Begriff *User* beinhalten, müssen in Backticks gesetzt werden, damit die Begriffe nicht mit einem Befehl verwechselt werden, z.B. ``User rights``.
1. Wähle im Bereich CSV Eigenschaften ein CSV-Trennzeichen und bei Bedarf ein Feldtrennzeichen aus dem Dropdown-Menü.
1. Im Bereich Notiz kannst du bei Bedarf eine interne Bemerkung hinterlegen.
1. Klicke auf Speichern.

Dein Bericht mitsamt den Einstellungen wird gespeichert.

> **Anmerkung**
>
> Du kannst deine Berichtseinstellungen als JSON-Datei herunterladen, um diese wiederzuverwenden, indem du aufDefinitionsdateiklickst.

### Tabellenspalten anlegen, pflegen und löschen

Die Tabellenspalten werden über den BereichAktionendeines Berichts gepflegt.

Nach Einrichtung deiner Berichtseinstellungen, Eingabe eines gültigen SQL-Statements und Speichern deines Berichts musst du die Tabellenspalten anlegen. Diese Tabellenspalten werden dann im ReiterAnsichtdeines Berichts sowie in deinen Berichtsexporten angezeigt.

Je nachdem, ob du einen komplett neuen Bericht angelegt oder einen bestehenden Bericht und SQL-Statement bearbeitet hast, führst du Folgendes aus:

- Hast du einen komplett neuen Bericht angelegt und ein neues SQL-Statement definiert, musst du nun die Tabellenspalten auf Basis deines SQL-Statements generieren. Zum Generieren der Tabellenspalten klickst du im Bereich Aktionen auf Spalten erzeugen.
- Hast du das SQL-Statement eines bestehenden Berichts überarbeitet, empfehlen wir dir, die bestehenden Spalten durch Klicken der Schaltfläche Alle Spalten löschen im Bereich Aktionen zu löschen und dann mit einem Klick auf Spalten erzeugen neu zu generieren. Dies ist die einfachste und schnellste Methode, die Spalten anzupassen. Alternativ kannst du mit einem Klick auf +Neue Spalte neue Spalten erstellen und so neue Spalten auf Basis des SQL-Statements hinzufügen.

Hast du die gewünschten Spalten erzeugt, kannst du die Spalteneinstellungen bei Bedarf anpassen. Klicke dafür auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/15150646037020)

in der jeweiligen Spalte.

> **Anmerkung**
>
> Diese Einstellungen finden nur in der Berichtsansicht im ReiterAnsichtAnwendung. Sie finden keine Anwendung beim Export des Berichts.

Du kannst die folgenden Spalteneinstellungen anpassen:

- Spaltenname SQL: Der Name der Spalte wie im SQL-Statement erfasst. Ändere diesen Namen nur dann, wenn du ihn auch im SQL-Statement geändert hast.
- Bezeichnung: Die Bezeichnung ist der Spaltenkopf. Möchtest du einen anderen als den automatisch angelegten Spaltenkopf verwenden, kannst du diesen hier ändern.
- Spaltenbreite: Die Spaltenbreite wird automatisch durch das System definiert. Bei Bedarf kannst du die Spaltenbreite hier anpassen.
- Ausrichtung: Wähle hier aus, ob die angezeigten Werte linksbündig, mittig oder rechtsbündig in der Spalten angezeigt werden sollen.
- Sortierung: Hier kannst du die Sortierung deiner Aufträge definieren. Du kannst sie numerisch oder alphabetisch sortieren.
- Formatierung: Hier kannst du die Formatierungseinstellung für deine Werte anpassen. Ist dein Wert zum Beispiel ein Geldbetrag, kannst du die Summe in deutscher Formatierung, d.h. mit einem Komma (45,00), oder im englischen Format mit einem Punkt (45.00) anzeigen lassen. Weiterhin kannst du zwischen unterschiedlichen Datums- und Zeitformaten wählen und deine eigene Formatierung erstellen.
- Spalte summieren: Wenn du hier ein Häkchen setzt, wird deinem Bericht unten eine Zeile hinzugefügt, wo die Geldbeträge dieses Spalte aufsummiert werden.
- Reihenfolge: Du kannst eine andere Reihenfolge definieren, um die Anzeige im Bericht anders zu sortieren. Änderst du z.B. die Reihenfolgenummer von eins auf drei, ist die Spalte nicht mehr die erste Spalte von links sondern die Dritte.

Klicke nach dem Bearbeiten der erforderlichen Spalten aufSpeichern.

Bei Bedarf kannst du einzelne Spalten löschen, indem du für die jeweilige Spalte auf![CrossIcon.png](https://help.xentral.com/hc/article_attachments/15150646537884)

klickst.

## Variable zu einem Bericht hinzufügen

Du kannst Variablen als Platzhalter in SQL-Statements einfügen. Variablen haben dabei die nachfolgende Formatierung:

{PROJEKTNAME}

Der Variablenname muss in Großbuchstaben geschrieben sein. Derzeit sind nur deutsche Variablennamen möglich.

Die Variablen, die du hier anlegst, stehen dir zusätzlich als Parameter zur Verfügung, wenn du einen Bericht im ReiterAnsichterstellst. Du kannst diese Variablen/ Parameter dazu verwenden, bestimmte Daten in deinen Bericht einzuschließen oder aus diesem auszuschließen, sowie zum Filtern.

Eine neue Variable erstellst du wie folgt:

1. Öffne den Bericht, dem du eine Variable hinzufügen möchtest, mit einem Klick auf.
1. Klicke im Bereich Einstellung auf +Neue Variable. Das Formular Parameter bearbeiten wird angezeigt.
1. Gib den Variablennamen ein.
1. Gib einen Standardwert für deine Variable in das Feld Standardwert ein.
1. Du kannst außerdem einen Wertebereich definieren, aus dem du bei Anlage des CSV- oder PDF-Berichts wählen kannst, z.B. bestimmte Monate, Wochen oder Jahre. Setze dafür ein Häkchen bei Manuell bearbeiten und gib Folgendes ein:
  - Dialogtext: Name des Auswahlfeldes, welches die Werte des Feldes Werteauswahl enthält.
  - Beschreibung: Interne Bezeichnung.
  - Eingabe: Wähle die Art der erforderlichen Eingabe, z.B. Datumsauswahl, Dropdown-Menü, Textfeld, etc.
  - Werteauswahl: Gib die gewünschten Werte für deine Auswahl durch Komma getrennt ein. Der finalen Variable wird automatisch ein Alias per Doppelpunkt hinzugefügt, z.B. können Projekt-Kennungen wie LP, ST zu Logistik:LP,Standard:ST werden. Dies dient der Verarbeitung im SQL-Statement.
1. Klicke auf Speichern.

Die Variable ist gespeichert. Sie wird dir im ReiterDetailsdeines Berichts unter dem FeldVariablenmit ihren Standardwerten angezeigt:

![ReportVariables.png](https://help.xentral.com/hc/article_attachments/15150690154012)

Zum Bearbeiten oder Löschen einer bestimmten Variable, klicke auf die Variable und das FormularParameter bearbeitenfür die Variable wird angezeigt. Du kannst die Variable nun bearbeiten oder löschen.

Neben den Variablen, die du selbst anlegst, kannst du auch noch die folgenden Variablen im SQL-Statement deines Berichts verwenden:

- {USER_ID}. Die ID des aktuellen Benutzers.
- {USER_PROJECTS}. Liste aller Projekte, auf die der Benutzer Zugriff hat. Mit dieser Variable kannst du die Ausgabe auf Nutzer mit Administratorrechten einschränken
- {USER_ADMIN → 1}. Gib eine 1 ein, um die Ausgabe nur zuzulassen, wenn der aktuelle Benutzer Admin-Rechte hat, oder eine 0, um die Ausgabe für alle Nutzer zuzulassen.
- {REPORT_PROJECT}. ID des Projekts, dem der aktuelle Bericht zugewiesen ist.
- {DOCTYPE}. Verwende diese Variable nur dann, wenn der Bericht über das Belegmenü geöffnet wird. Diese Variable zeigt die Belegart.
- {DOCID}. Der Wert wird nur dann angezeigt, wenn der Bericht über das Belegmenü geöffnet wird. Diese Variable zeigt die Datenbank-ID des Belegs.

## Freigaben für die Anzeige/Integration eines Berichts definieren

Neben der normalen Berichtsansicht im Reiter[Ansicht](#UUID-14597dcc-d945-c257-1864-cd30ac61a416_section-idm4494875453336033627388461194)des Berichts bietet Xentral auch die Möglichkeit, spezifische Anzeigemethoden oder Integrationen für jeden Bericht für bestimmte Mitarbeiter freizugeben. Der Bericht kann dabei auf verschiedene Weisen in den Arbeitsablauf des Mitarbeiters integriert werden:

| Anzeigemethode/Integration | Beschreibung |
| --- | --- |
| Diagramm | Die Berichtsdaten werden als Diagramm über die Berichtskachel in der Berichtsübersicht angezeigt (funktioniert nur für einzelne Tabellen, nicht für Joint-Tabellen). |
| Aktionsmenü | Der Bericht wird dem Aktionsmenü einer Belegart, die du in den Einstellungen definierst, hinzugefügt. |
| Download | Der Bericht kann über die Berichtsübersicht heruntergeladen werden. |
| Reiter | Der Bericht wird als separater Reiter einer Belegart, die du definierst, hinzugefügt. Das heißt, dass dir beim Öffnen eines Belegs der definierten Belegart ein zusätzlicher Reiter mit den Berichtsdaten angezeigt wird. |

Wenn du deine Freigaben zugewiesen hast, kannst du die Einstellungen der verschiedenen Anzeigemethoden/ Integrationen definieren.

Freigaben für Mitarbeiter erteilst du unter folgendem Pfad:

Berichtswesen > Berichte > Bericht öffnen![PenIcon.png](https://help.xentral.com/hc/article_attachments/15150646037020)

> Reiter Freigaben

Im ReiterFreigabenfindest du alle bestehenden Freigaben deines Berichts und du kannst neue Freigaben hinzufügen und die Einstellungen zu den Freigaben definieren.

Gehe wie folgt vor, um einem Benutzer eine Freigabe für die Anzeige/ Integration der Berichtsdaten in einem bestimmten Format zu erteilen:

1. Klicke im Bereich Aktionen auf +Neue Freigabe. Das Formular Integration in Xentral wird angezeigt.
1. Wähle den Mitarbeiter, dem du Freigaben erteilen möchtest, im Feld Mitarbeiter.
1. Wähle die Freigaben, die du erteilen möchtest.
1. Klicke auf Speichern.

Der Mitarbeiter wird mit den ihm oder ihr zugewiesenen Freigaben in der Tabelle angezeigt.

### Die Diagrammeinstellungen definieren

Reiter Freigaben > Bereich 1. Graph im Dashboard

Du kannst die Berichtsdaten in Diagrammform bereitstellen lassen.Xentral bietet unterschiedliche Visualisierungsoptionen.

Die Diagrammeinstellungen definierst du wie folgt:

1. Möchtest du das Diagramm für alle Benutzer verfügbar machen und nicht nur für solche mit entsprechender Freigabe, setze ein Häkchen bei Öffentlich freigeben.
1. Wähle die Art des Diagramms, das angezeigt werden soll (z.B. Kuchendiagramm), aus dem Typ-Dropdown-Menü.
1. Gib deine Beschreibungen für die FelderY-Achsenbeschriftung,Achsenspalte,Daten-Spalte(n)undGruppier-Spalteein.
1. Gib in die Datumsformat-Felder ein, wie viele Tage, Wochen oder Monate an Daten angezeigt werden sollen. Wähle dazu das entsprechende Intervall aus dem Dropdown-Menü und gib in das Feld davor die numerische Zahl ein.
1. Scrolle ganz nach unten und klicke auf Speichern.

Deine Diagrammeinstellungen werden gespeichert. Alle Mitarbeiter mit entsprechender Freigabe sehen nun das folgende Element in der Berichtskachel in der Berichtsübersicht:

![Report_chart.png](https://help.xentral.com/hc/article_attachments/15150682430108)

Der Benutzer öffnet die Berichtsdaten in Diagrammform, indem er darauf klickt.

### Einstellungen für das Herunterladen des Berichts in der Berichtsübersicht definieren

Reiter Freigaben > 2. Datei-Download im Dashboard

Standardmäßig steht in der Berichtsübersicht der Berichtsdownload im PDF- und CSV-Format zur Verfügung. Möchtest du eine oder beide Optionen für einen Benutzer ausschließen, gehe wie folgt vor:

- Setze ein Häkchen bei Öffentlich freigeben.
- Wähle das Format, in dem der Bericht nicht mehr zum Download zur Verfügung stehen soll.
- Klicke auf Speichern.

### Aktionsmenü-Einstellungen definieren

Reiter Freigaben > 3. Bereich Aktionsmenü in Belegen

Du kannst deinen Bericht als Download über das Aktionsmenü einer Belegart verfügbar machen. Dies ist hilfreich, wenn du die Berichtsdaten bei der Arbeit mit bestimmten Belegarten benötigst, z.B. Lieferscheinen.

Die Aktionsmenü-Einstellungen richtest du folgendermaßen ein:

1. Möchtest du den Bericht allen Benutzern per Download bereitstellen und nicht nur für solche mit den entsprechenden Freigabe, setze ein Häkchen bei Öffentlich freigeben.
1. Wähle die gewünschte Belegart im Auswahlfeld Beleg.
  Die Belegart findest du auch in der URL, wenn du das gewünschte Modul öffnest.

1. Wenn du eine bestimmte Beschriftung im Aktionsmenü angezeigt haben möchtest, gib diese in das Feld Menü-Beschriftung ein. Wenn du hier nichts eingibst, wird der Name des Berichts angezeigt.
1. Wähle das Format, in dem Bericht heruntergeladen werden soll.
1. Klicke Speichern.

Wenn du nun mit einem Beleg der entsprechenden Belegart arbeitest und dasAktion-Dropdown-Menü öffnest, findest du die Download-Option für deinen Bericht dort. Durch Auswahl dieser Option wird dein Bericht heruntergeladen.

### Reiter-Einstellungen definieren

Reiter Freigaben > 4. Bereich Tab (Reiter) in Software

Ist es erforderlich, die Berichte direkt in den Belegdaten anzuzeigen, kannst du die Anzeige des Berichts als separaten Reiter in den Belegdaten freigeben.

Die Reiter-Einstellungen definierst du wie folgt:

1. Möchtest du den Bericht allen Benutzern bereitstellen und nicht nur für solche mit der entsprechenden Freigabe, setze ein Häkchen bei Öffentlich freigeben.
1. Wähle die Belegart, der du einen zusätzlichen Reiter für den Bericht hinzufügen möchtest, im Feld Modul aus.
1. Gib die Aktion, bei der der Reiter erscheinen soll, in das Feld Action ein.
  Die Aktionen findest du in der URL, wenn du einen Beleg öffnest.

1. Gib den Namen deines Reiters in das Feld Tab-Beschriftung ein.
1. Wähle die Anordnung deines Reiters in das Feld Position ein. Du kannst ihn vor oder hinter dem Reiter Freifeld anordnen.
1. Klicke auf Speichern.

Der Berichte-Reiter wird mit dem von dir definierten Reiternamen in den ausgewählten Belegen angezeigt. Mit einem Klick auf den Reiternamen wird der Bericht in einem Pop-up-Fenster geöffnet.

## Übertragungsoptionen definieren

Berichtswesen > Berichte > Bericht öffnen![PenIcon.png](https://help.xentral.com/hc/article_attachments/15150646037020)

> Reiter Übertragung

Du kannst den Bericht automatisch über verschiedene Kanäle versenden oder teilen. Dir stehen hier die folgenden Optionen zur Verfügung:

### Per FTP übertragen

Zum Übertragen des Berichts via FTP gehe wie folgt vor:

1. Setze im Bereich Per FTP übertragen ein Häkchen bei Aktivieren, um die FTP-Übertragung zu aktivieren.
1. Wähle den zu verwendenden FTP-Typ aus dem Typ-Dropdown-Menü. Wähle zwischen den folgenden Optionen: FTP, FTP mit SSL und SFTP.
1. Du kannst ein Häkchen bei Passiver Modus setzen, wenn der Server keine Verbindung zum Client herstellen kann, z.B. wenn eine Firewall verwendet wird. Die Firewall wird in diesem Fall die Verbindung erlauben, da die Quelle innerhalb des geschützten Bereichs liegt. Die Option ist nur dann möglich, wenn du FTP oder SFTP verwendest. Wir empfehlen die Verwendung von SFTP.
1. Gib die passenden FTP-Informationen in die folgenden Felder ein: FTP-Host, Port, FTP-Benutzer und FTP-Passwort. Gibst du keinen Port ein, wird der Standard-Port verwendet. Der Standard-Port für FTP und FTPS ist 21, der für SFTP ist 22.
1. Gib das Übertragungsintervall in die Übertragungsintervall-Felder ein. Wähle aus dem Dropdown-Menü das Übertragungsintervall: Alle X Tage, Wöchentlich am oder Monatlich am. Gib in das Feld rechts daneben den entsprechenden numerischen Wert ein. Beispiel: Wählst du das Übertragungsintervall Wöchentlich am aus und gibst den numerischen Wert 3 ein, erfolgt die Übertragung am dritten Tag der Woche, d.h. Mittwoch.
1. Klicke auf das Feld Uhrzeit. Das Fenster Uhrzeit wählen wird angezeigt. Benutze die Schieber für Stunde und Minute, um die gewünschte Uhrzeit festzulegen. Möchtest du die aktuelle Zeit verwenden, klicke auf Aktuelle Zeit. Zur Bestätigung klicke auf OK.
1. Wähle das Dateiformat für die Übertragung.
1. Möchtest du einen anderen als den Standard-Berichtsnamen als Dateinamen verwenden, gib ihn in das Feld Dateiname ein. Du kannst die Variablen, die im Formular gelistet sind, hier verwenden.
1. Scrolle zum unteren Ende des Reiters und klicke auf Speichern, um die Einstellungen für die FTP-Übertragung zu speichern.

Die FTP-Übertragung erfolgt nun automatisch in dem definierten Intervall.

### Bericht per E-Mail versenden

Du kannst den Bericht per E-Mail versenden, z.B. an einen Mitarbeiter, der diesen Bericht regelmäßig bewerten muss.

Gehe dazu wie folgt vor:

1. Setze im Bereich E-Mail-Versand ein Häkchen bei Aktivieren, um die Übertragung per E-Mail zu erlauben.
1. Gib den Empfänger der E-Mail sowie den E-Mail-Betreff in die entsprechenden Felder ein.
1. Gib das Übertragungsintervall in die Übertragungsintervall-Felder ein. Wähle aus dem Dropdown-Menü das Übertragungsintervall: Alle X Tage, Wöchentlich am oder Monatlich am. Gib in das Feld rechts daneben den entsprechenden numerischen Wert ein.
1. Mit einem Klick auf das Feld Uhrzeit wird das Fenster Uhrzeit wählen geöffnet. Benutze die Schieber Stunde und Minute, um die gewünschte Uhrzeit einzustellen oder klicke auf Aktuelle Zeit, um die aktuelle Zeit zu wählen. Bestätige deine Auswahl mit OK.
1. Wähle das Dateiformat für die Übertragung.
1. Möchtest du einen vom Standard-Berichtsnamen abweichenden Namen anwenden, gib diesen in das Feld Dateiname ein. Du kannst die Variablen, die im Formular gelistet sind, hier verwenden.
1. Scrolle bis zum unteren Ende des Reiters und klicke auf Speichern, um die Einstellungen zum E-Mail-Versand zu speichern.

Die E-Mail wird nun automatisch im definierten Intervall versendet.

### Bericht per URL teilen

Du kannst deinen Bericht über eine spezifische URL teilen.

Gehe dazu wie folgt vor:

1. Wähle im Bereich URL teilen das Format, in dem du den Bericht teilen möchtest, aus dem Format-Dropdown-Menü.
1. Wenn du auf die Verfügbarkeit-Felder klickst, wird ein Kalender geöffnet. Wähle den Zeitraum aus, für den der Bericht über die generierte URL abrufbar sein soll. Wenn du keinen Zeitraum definierst, kann keine URL generiert werden.
1. Klicke auf Neue URL erzeugen, um eine URL für das Teilen des Berichts zu generieren. Das Fenster wird automatisch neu geladen und die neu generierte URL wird im Feld Abruf über URL angezeigt.
1. Um die URL zu teilen, klicke auf das Kopiersymbol.

Die generierte URL kannst du nun in eine E-Mail oder einen Chat kopieren, um den Bericht zu teilen.

### Bericht über API teilen

Du kannst deinen Bericht über ein API-Konto teilen.

Gehe dazu wie folgt vor:

1. Setze im Bereich API-Zugriff freigeben ein Häkchen bei Aktivieren, um die API-Übertragung zu erlauben.
1. Wähle das API-Konto, mit dem du den Bericht teilen möchtest, aus dem Feld API-Account. API-Konten richtest du unter Administration > System > API-Account ein.
1. Wähle das Format, in dem du den Bericht teilen möchtest, aus dem Format-Dropdown-Menü.
1. Klicke aufSpeichern.

## Einen Bericht anzeigen

Berichtswesen > Berichte > Bericht öffnen![PenIcon.png](https://help.xentral.com/hc/article_attachments/15150646037020)

> Reiter Ansicht

Der Bericht wird automatisch generiert, wenn du den ReiterAnsichtöffnest.

Du kannst die angezeigten Berichtsdaten durch die Parameter im BereichParametergenauer definieren oder einschränken. Die hier angezeigten Parameter und Optionen der einzelnen Parameter sind identisch zu den[Variablen](#UUID-14597dcc-d945-c257-1864-cd30ac61a416_section-idm459181717663043342398997836), die du im ReiterDetailshinzugefügt hast. Um Parameter anzuwenden, wähle die entsprechenden Werte der gewünschten Parameter und klicke aufParameter festlegen. Die Berichtsdaten werden auf Basis der angezeigten Parameter aktualisiert.

Du kannst zusätzlich die Spaltenfilter verwenden, um nach spezifischen Daten zu filtern, oder den Bericht als CSV-Datei oder PDF-Datei herunterladen. Klicke dazu im BereichDownloadaufExport CSVoderExport PDF, je nach Bedarf.

## Beispiel für eine SQL-Anfrage - Anzahl Aufträge pro Kunde für Zeitraum X

```
select count(*) as Anzahl_Bestellungen,ad.kundennummer as Kundennummer, au.name as Kunde from auftrag au inner join adresse ad on ad.id=au.adresse where au.datum between '{VON}' and '{BIS}' and au.status <> 'angelegt' group by au.adresse",
  "columns
```

> **Anmerkung**
>
> '{VON}' und '{BIS}' sind Variablen.