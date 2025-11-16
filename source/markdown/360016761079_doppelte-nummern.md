Das Modul **Doppelte Nummern** überprüft das System regelmäßig auf doppelt vergebene Artikelnummern, Seriennummern, sowie Rechnungs- und Gutschriftsbelegnummern. Eine rote Warnung erscheint dann in der System Health-Übersicht der xentral-Oberfläche, falls das System doppelte Nummern ausfindig gemacht hat.

## Technische Features

- Durchsucht Artikel nach doppelt vergebenen Artikelnummern
- Durchsucht Rechnungen und Gutschriften nach doppelt vergebenen Belegnummern
- Durchsucht Adressen nach doppelt vergebenen Kunden- und Lieferantennummern (Debitoren- und Kreditorennummer)

## Überprüfung aktivieren

Unter **Administration > Einstellungen > System > Grundeinstellungen > Nummernkreise** befindet sich am unteren Ende die Option, um die Warnung vor doppelten Nummern zu aktivieren. Direkt darunter befindet sich auch eine Option, um vor doppelten Seriennummern gewarnt zu werden. Diese zu aktivieren ist nützlich, wenn Artikel mit Seriennummern im Bestand geführt oder verkauft werden.

Die Prüfung auf doppelte Nummern erfolgt durch den **Doppelte Nummern prüfen**. Dieser muss aktiviert sein und regelmäßig ausgeführt werden, damit das Modul funktionsfähig ist. Wurden doppelte Nummern gefunden, so wird eine entsprechende Fehlermeldung in der System Health Übersicht von xentral angezeigt.

![duplicatenumbers_1.png](https://help.xentral.com/hc/article_attachments/13991461784860)

## Übersicht

Wird vor doppelten Nummern gewarnt, ist es möglich direkt über die System Health Übersicht in das Modul zu springen oder über **App Center > Doppelte Nummern**. Im Modul befindet sich eine Übersicht über alle gefundenen doppelten Nummern.

Im Beispiel unten hat das Modul zwei Artikel mit gleicher Artikelnummer entdeckt und führt diese in der Liste auf.

![duplicatenumbers_2.png](https://help.xentral.com/hc/article_attachments/13991445611804)

## Doppelte Artikelnummern

Schon bei der Erstellung von Artikeln wird davor gewarnt, wenn eine Artikelnummer doppelt vergeben wurde.

![duplicatenumbers_3.png](https://help.xentral.com/hc/article_attachments/13991458266396)

Eine Vergabe doppelter Artikelnummern kann vorkommen, wenn es eine Überschneidung zwischen dem globalen Nummernkreis aus den Firmendaten (**Administration > Einstellungen > System > Grundeinstellungen > Nummernkreis**), dem projektspezifischen Artikelnummernkreise und den Nummernkreisen in den Artikelkategorien gibt.

Lösung:

Im Artikel selber können Artikelnummern händisch geändert werden. Falls innerhalb einer Artikelkategorie keine eigenen Nummern verwendet werden sollen, sondern stattdessen der globale Nummernkreis, kann für jede Kategorie die Option **Zentralen Nummernkreis verwenden ** gesetzt werden. Dies ist möglich unter**Administration > Einstellungen > Stammdaten > Artikel Kategorien** und anschließendem Klick auf die gewünschte Kategorie.

## Doppelte Rechnungs- oder Gutschriftnummern

Doppelte Belegnummern bei Rechnungen und Gutschriften sollten in der Regel nicht vorkommen. Es kann aber dazu kommen, wenn z.B. der eingestellte globale oder projektspezifische Nummernkreis zurücksetzt/verändert wurde, oder wenn Belege über den Belege Importer ins System geladen wurden.

Lösung:

Über die xentral-Oberfläche kann man doppelte Belegnummern nicht beheben. Die Belegnummern müssen direkt in den Datenbank-Tabellen gutschrift und rechnung beim Wert belegnr umgetippt werden.

![duplicatenumbers_4.png](https://help.xentral.com/hc/article_attachments/13991445752988)

## Doppelte Seriennummern

Doppelte Seriennummern können vorkommen, wenn beim Einlagern eine schon vorhandene Seriennummer nochmal eingelagert wurde oder wenn eine Seriennummern mehrfach auf einen oder mehrere Liefescheine verknüpft ist.

Lösung:

**Lieferschein: ** Direkt auf die fett-hinterlegte Lieferscheinnummer klicken, um die Seriennummer zu ändern.** Lager: ** Auf die fett-hinterlegte Artikelnummer klicken um in das ** Seriennummer **Tab des Artikels zu gelangen. Im Reiter ** Lager** kann man die Seriennummern manuell editieren.