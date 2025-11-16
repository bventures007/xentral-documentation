Mithilfe der AppZeiterfassung Stundenübersichtkann sich ein Überblick über die Arbeitsstunden der Angestellten verschafft werden. Die App gliedert sich in zwei Bereiche: Auf der einen Oberfläche besteht die Möglichkeit, die Rahmenbedingungen für die Angestellten festzulegen. Auf der anderen Oberfläche können die einzelnen Mitarbeiter die Daten einsehen, ohne allerdings Änderungen vornehmen zu können.

## Personalverwaltung - Funktionen und Ansicht

Die Startansicht besteht aus einer Auflistung aller Adressen, bei denen die Rolle "Mitarbeiter" hinterlegt wurde.

Die Übersicht zeigt für alle Mitarbeiter die Soll- und Ist-Stunden des aktuellen Monats, die durch einen Klick auf dasStift-Icon bearbeiten werden können.

![Time_Recording_Hour_start.png](https://help.xentral.com/hc/article_attachments/5010421331228)

Mit einem Klick auf dasStift-Icon erscheint die zweite Oberfläche:

![Time_Recording_Hour_edit.png](https://help.xentral.com/hc/article_attachments/5010450723356)

In der oberen Zeile sind zunächst einige allgemeine Einstellungen möglich. Folgende Angaben können gemacht werden:

- Jahr: Im Drop-Down Menü ist das gewünschte Jahr für die Übersicht auszuwählen. Dabei ist es möglich, ein Jahr im Voraus zu planen und die letzten vier Jahre einzusehen
- Arbeitsvertrags-Basis: Ist in den Adressstammdaten des Mitarbeiters eine Wochenarbeitszeit hinterlegt, so wird diese an dieser Stelle verwendet. Andernfalls wird eine 40-Stunden-Woche unterstellt. Dies gilt nur beim initialen Aufruf der Oberfläche des Mitarbeiters. Der umgekehrte Fall gilt jedoch nicht. D.h. die Angabe einer Wochenarbeitszeit an dieser Stelle hat keinerlei Auswirkungen auf Werte, die in den Stammdaten des Mitarbeiters hinterlegt sind
- Überstundentoleranz: Hier kann eine Toleranzgrenze angegeben werden, bis zu welcher Überstunden nicht berücksichtigt werden
- Urlaubstage pro Jahr: Die Urlaubstage können für die nächsten drei Jahre angegeben werden

> **Anmerkung**
>
> Die Angabe zur Wochenarbeitszeit wird nur dann aus den Adressstammdaten übernommen, wenn es zuvor keinen manuellen Eintrag unter "Arbeitsvertrags-Basis" gab, d.h. das Feld leer war. Wenn es einen Eintrag gab, dann überschreibt eine Änderung der Arbeitszeit in der Adresse des Mitarbeiters unter "Arbeitszeit pro Woche" dieses Feld nicht.

Zum Jahreswechsel sollten die Überstunden und Urlaubstage stets aktualisiert werden, sofern noch welche offen sind.

In der Tabelle werden verschiedene Informationen aufgeführt:

- Monat: Die Stunden werden für die jeweiligen Monate aufgeschlüsselt
- Ist-Stunden: Die Ist-Stunden ergeben sich aus der Zeiterfassung und können hier nicht manuell verändert werden
- Soll-Stunden: Die Soll-Stunden werden auf Basis aller Werktage berechnet. Entscheidend für die erste Berechnung ist die hinterlegte Wochenarbeitszeit in den Stammdaten, andernfalls wird eine 40 Stunden Woche unterstellt. Da bei dieser Berechnung allerdings keine Feiertage berücksichtigt werden, sollten am Jahresanfang die Zahl der tatsächlichen Werkstunden für jeden Monat angepasst werden. Dies ist auch zu tun, falls sich während des Jahres einmal die Wochenarbeitszeit verändern sollte
- Differenz-Stunden: Die Differenz-Stunden spiegeln den aktuellen Stand offener Stunden wider, die im laufenden Monat noch abgeleistet werden müssen
- Stunden minus Toleranz: Diese Spalte entspricht den Differenzstunden, wobei eine mögliche Überstundentoleranz hier zusätzlich berücksichtigt wird. Diese Spalte zeigt die Überstunden, die ausbezahlt, als Urlaub angerechnet werden könnten oder nachzuholen sind
- Überstd. eingelöst: Hier können die Überstunden eingetragen werden, die der Mitarbeiter diesen Monat eingelöst hat bzw. plant einzulösen
- Überstd. aktueller Stand: Hier werden die verbleibenden Über- bzw. Minusstunden aufgeführt, wobei auch die Einträge des laufenden Monats bereits eingerechnet werden
- Urlaub eingelöst: Hier sind die Urlaubstage zu vermerken, die vom Mitarbeiter eingelöst werden sollen
- Urlaub aktueller Stand: Analog zur Überstundenberechnung werden hier die verbleibenden Urlaubstage angezeigt
- Notizen: Hier können etwaige Bemerkungen hinterlegt werden, die nicht durch den einzelnen Mitarbeiter veränderbar sind

## Mitarbeiter - Ansicht

Dieselbe Oberfläche steht auch dem einzelnen Mitarbeiter zur Verfügung. Dieser kann aber die eingetragenen Werte nicht verändern.

![Time_Recording_Hour_employee_view.png](https://help.xentral.com/hc/article_attachments/5010421379868)

Diese Oberfläche lässt sich überTeam > Meine Startseite > Stundenübersichtaufrufen, sofern der Mitarbeiter die entsprechende Berechtigung hierfür erhalten hat. Das zugehörige Recht kann über die Rechte in der Benutzerverwaltung erteilt werden (Administration > System > Benutzer > Benutzer bearbeiten > Rechte), indem für das Modul Zeiterfassung Stundenübersicht bei zeiterfassung_stundenuebersicht das Recht "listmitarbeiter" durch einen Klick auf dieses Feld ausgewählt wird.

![Time_Recording_Hour_rights.png](https://help.xentral.com/hc/article_attachments/5010405026588)