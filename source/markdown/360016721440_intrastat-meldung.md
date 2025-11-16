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

Mit dem Modul Intrastat kann eine Liste von Warenpositionen erstellt werden, basierend auf den Lieferscheinen, die ins EU-Ausland verschickt wurden. Diese Liste kann dann als CSV-Import im entsprechenden Portal des Statistischen Bundesamtes hochgeladen werden.

## Übersicht

Hier werden verschiedene Attribute gespeichert, die beim Anlegen des Artikels angegeben werden können, wie z.B. die Ursprungsregion, Gewicht, "besondere Masseinheit". In der Intrastat Meldung werden folgende Informationen gespeichert:

- Monat: Monat (Zahl des Monats) in dem die Ausfuhr stattgefunden hat
- Bestimmungsland: Land aus den Stammdaten des Lieferscheins
- Ursprungsregion: Ursprungsregion im Artikel
- Warennummer: Zolltarifnummer im Artikel
- Warenbezeichnung:Name des Artikels
- Eigenmasse: Gesamtgewicht des Artikels aus dem Lieferschein. Positionsmenge multipliziert mit Artikelgewicht
- Besondere Masseinheit: Einheit im Artikel
- Rechnungsbetrag: Gesamtverkaufspreis des Artikels aus dem Lieferschein. Positionsmenge multipliziert mit Verkaufspreis

Welche Parameter und Werte Sie hier in den Spalten eingeben können und wie diese genau heißen müssen, erfahren Sie beim Statistischen Bundesamt. Je nach Branche & Geschäftsbereich sind unterschiedliche Parameter relevant. Die Spaltenbezeichnungen müssen genau übernommen werden. So könnte es zum Beispiel aussehen:

Sie haben die Möglichkeit die Intrastat Meldung nach einem Zeitraum zu filtern. Es ist auch möglich drei neue Spalten hinzuzufügen und diesen einen Wert zu vergeben. Außerdem gibt es die Möglichkeit die Zeilen nach Artikel zu gruppieren.

> **Anmerkung**
>
> Es können nur Werte vergeben werden, keine Variablen.

## Grundlage für die Berechnung

Beim Warenausgang werden die Lieferscheine jeden Statuses (auch Entwurf und storniert) für die Berechnung hergenommen. Wichtig dabei: Im Beleg muss ein Land ausgewählt sein, das der EU angehört.

> **Wichtig**
>
> Im Dokument muss ein Land ausgewählt werden, das der EU angehört.

Beim Wareneingang werden nur Bestellungen angezeigt, die über den großen Wareneingang, also die Paketdistribution gegangen sind (Einstellung "Große Paketannahme" in den Firmendaten).

## Intrastat Import

Bevor Sie die exportierte Datei auf das Portal des Statistischen Bundesamtes laden können, müssen Sie zuerst eine Importdefinition anlegen.

Nach dem Sie die Importdefintion gemäß den exportierten Daten aus xentral angepasst haben, können Sie in folgender Oberfläche die CSV hochladen:

Hierdurch können die Daten in das Formular für die Intrastat-Meldung übernommen werden.