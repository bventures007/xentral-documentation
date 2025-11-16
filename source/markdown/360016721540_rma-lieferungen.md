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

Der vorliegende Artikel beschreibt, wie du das RMA- sowie das Retoure-Modul in xentral nutzen und Paketannahmen in xentral vermerken kannst. Wichtig zu wissen ist, dass das RMA-Modul im Gegensatz zum Retouren-Modul mehr oder weniger verwaltet ist und wesentlich weniger Möglichkeiten bietet. Das RMA-Modul erkennt den Liefereingang eines Kunden als RMA, ermöglicht eine Übersicht sowie eine Gutschrifterstellung. Das Retoure-Modul hingegen bildet alle Optionen wie bspw. Ersatzlieferungen und Belegerstellung ab.

**Lager & Logistik > RMA Lieferungen **>** Anmerkung**
>
> Bis Version 21.1: **Verwaltung > RMA Lieferungen**

## Angenommene RMA Artikel

Angenommene RMA Artikel kannst du direkt in der Adresse einsehen. Navigiere dazu zu **Stammdaten > Adresse > gewünschte Adresse öffnen > Artikel > RMA**.

### RMA: Kleine Paketannahme

Idealerweise erfolgt der Wareneingang in einem Schritt mit Annahme und Distribution. Navigiere dafür zu dem Modul **Wareneingang Paket Annahme **, über das ** Pfeil**

-Icon gelangst du in das einzelne Paket. Über die Paketannahme kannst du Kunden-Rücksendungen zu Aufträgen annehmen werden. Voraussetzung ist, dass ein Artikel zurückgenommen wird, der zuvor über einen Auftrag/Lieferschein an den Kunden versendet wurde.

#### Schritt 1 und 2: Kunde und Artikel

Schritt 1 und 2 der kleinen Paketannahmen beinhalten den Kunden sowie den dazu gehörigen Artikel:

1. Wähle daher zunächst den **Kunden** aus
1. Ordne dann **Artikel** zu

Diese Schritte sind bei jedem Wareneingang identisch, unabhängig davon, ob es sich um die Artikel eines Kunden oder Warenlieferungen eines Lieferanten handelt. Schritt 1 und 2 sind identisch mit der kleinen Warenannahme. Die Beschreibung findest du[hier](https://help.xentral.com/hc/articles/360016763959#UUID-f3eadbf9-8f35-62af-1a6f-6bdc4ace44d9).

Zu Schritt 2 siehst du im Modul**Wareneingang Paket Annahme > Paketannahme >* Kunden öffnen *> Unangekündigte Retouren **alle ausgelieferten Artikel an diesen Kunden. Trage in das leere Feld in der Aktionsspalte die Menge ein, die zurückgesendet wurde und klicke auf ** zuordnen**.

#### Schritt 3: RMA Grund angeben

Retourenartikel werden von dir nicht direkt eingelagert, sondern mit einem **Retourengrund** der Kundenadresse zugeordnet.

Wähle einen dieser möglichen Retourengründe aus dem Drop-Down Menü aus, das erscheint, nachdem du einem Artikel eine Menge zugeordnet hast:

- Reparatur
- 14 Tage Rückgaberecht
- Retourensendung
- Defekt und sofort neues schicken
- Falscher Artikel geliefert

Klicke abschließend auf **Speichern**.

### RMA: Große Paketannahme

Die Bearbeitung von Rückläufern mit dem **großen Wareneingang ** erfolgt im Prinzip wie oben beschrieben, allerdings ist diese aufgeteilt in die zwei Schritte **Annahme ** und**Distribution**.

#### RMA Weiterbearbeitung

Unter **Lager & Logistik > RMA Lieferungen ** (bis Version 21.1: ** Verwaltung > RMA Lieferungen **) legst du für jede Paketannahme einen Retouren-Eintrag an. Navigiere dazu über das ** Pfeil**

-Icon in eine Adresse und wähle über Anhaken die gewünschten Pakete aus.

Wähle aus den verschiedenen Optionen für die RMA-Sendungen aus dem Drop-Down Menü am unteren rechten Rand aus:

- Gutschrift zu ausgewählten Artikeln
- Kostenlose Ersatzlieferung veranlassen
- Rücksendung der ausgewählten Artikel
- ausgewählte zur internen Reparatur geben
- ausgewählte für Reparatur zurückschicken
- ausgewählte Artikel auf abgeschlossen setzen
- ausgewählte Artikel auf offen setzen

Nachdem du die Option durch Anklicken ausgewählt hast, klicke auf die Schaltfläche **Ausführen**.

#### RMA direkt einlagern

Es gibt auch die Möglichkeit, Artikel einer RMA Lieferung im Popup oben direkt einzulagern.

Dieser Fall tritt aus diesen zwei Gründen ein:

- Wenn ein Standardregal für den Artikel hinterlegt ist, wird dieses vorausgefüllt
- Ist kein Standardregal hinterlegt, wird das Regal mit dem höchsten Bestand vorausgefüllt

Mit der **Ausführen**

-Schaltfläche unten erstellst du eine Gutschrift, wenn du die Option angehakt hast, dass die Artikel im entsprechenden Regal eingelagert werden.

## Gutschrift zu ausgewählten Artikeln erzeugen

Wenn du die Option **Gutschrift** zuvor aus dem Drop-Down Menü ausgewählt hast, gelangst du nach dem Markieren der entsprechenden Artikel für die Gutschrift in ein Pop-up-Fenster.

Trage folgende Informationen ein:

- **Interner Kommentar**→ Trage einen internen Kommentar zu der zu erstellenden Gutschrift ein
- **für Kunde (Freitext)**→ Trage optional einen Freitext ein, der als Text auf der Gutschrift erscheint

Mit einem Klick auf **Ausführen** erzeugst du eine Gutschrift für die ausgewählten Artikel. Du gelangst dann in die Gutschriften-Maske, die du entsprechend ausfüllst. Weitere Informationen dazu findest du[hier.](https://help.xentral.com/hc/articles/360016722700#UUID-5de8c502-e59a-837f-c8c4-b1e1a340bbed)

## Neue Paketmarke drucken

Falls dein Paket nicht zugestellt werden konnte, die Verpackung aber unbeschädigt ist, kannst du direkt eine neue Paketmarke drucken. Navigiere dazu über **Lager & Logistik > Lieferschein > Adresse suchen (Kundennummer)** in die Übersicht. Wähle eine einzelne Adresse über das ** Stift **

-Icon aus, navigiere zum Reiter ** Paketmarke **und klicke auf die Schaltfläche ** Paketmarke drucken**.

> **Anmerkung**
>
> Die Anbindung zur Paketmarken-Software muss aktiv sein.

Die Trackingnummer wird direkt im Protokoll (**Details > Protokoll**) des Lieferscheins gespeichert:

## Storno + Artikel einlagern

Macht der Kunde vom 14-tägigen Rückgaberecht Gebrauch oder wird die Ware (oder ein Teil der Ware) zurückgenommen, dann führe folgende Schritte durch:

1. Artikel prüfen und einlagern (direkt über **Artikel > Lager oder Lager & Logistik > Ein-/Auslagern > Einlagern**)
1. Rechnung stornieren / weiterführen als Gutschrift (**Buchhaltung > Rechnung > Kreuz-Icon in der Menü-Spalte**)
1. Gutschrift an den Kunden senden, über das Drop-Down Menü **Aktion **, wähle dort ** Abschicken**

## Defekten Artikel austauschen

Defekte Artikel können auf zwei Arten ausgetauscht werden:

1. Kostenlose Neulieferung
1. Erstellung eines neuen Auftrags, Stornierung des ursprünglichen Auftrags

### Kostenlose Lieferung erstellen

Die einfachste Möglichkeit ist die Erstellung einer kostenlosen Lieferung (ohne Rechnung). Die ursprüngliche Rechnung und der Lieferschein werden nicht storniert.

Gehe wie folgt vor:

1. Auftrag kopieren, über **Verkauf > Auftrag ** und Klick auf das**Kopieren**

-Symbol in der Menü-Spalte.
1. Ggf. Positionen bearbeiten
1. Wähle im Auftrag folgende Option: **Nur Lieferschein erstellen** oder: optional können alle Beträge in den Positionen auf 0 EUR gesetzt werden, dann wird die Erstellung einer Rechnung unterbunden
1. Auftrag freigeben
1. Auftrag abschicken (ggf. an das Versandzentrum übergeben)

### Neuen Auftrag erstellen

Eine andere Möglichkeit ist die Stornierung des alten Auftrags, der Rechnung und des Lieferscheins. Ein komplett neuer Auftrag wird erstellt:

1. **Verkauf > Auftrag > Stift-Symbol in der Menü-Spalte > Kopieren-Symbol in der Menü-Spalte**

1. Auftrag freigeben
1. Buche evtl. bereits empfangene Zahlungseingänge auf den neuen Auftrag
1. Abschicken (ggf. an Versandzentrum übergeben)

Die ursprünglichen Dokumente werden storniert:

- Rechnung weiterführen als Gutschrift /ggf. Stornorechnung erstellen
- Ggf. Auftrag und Lieferschein stornieren

## Reparatur

Zudem hast du die Option, nach der Reparatur den Artikel wieder einzulagern, z.B. mit einer gesonderten Artikelnummer oder als Lagerartikel. Alternativ kannst du einen **Kostenlosen Auftrag** (s.o.) mit dieser neuen Artikelnummer erstellen.

> **Anmerkung**
>
> Separate Artikelnummern, z.B. "100001 RMA Artikel" (> Haken **Lagerartikel** gesetzt), kannst du für Rückläufer verwenden. Je Auftrag kannst du die Beschreibung umändern. Auf diese Weise ist es auch möglich, dass du zusätzlich versendetes Material des Kunden mit erfasst. Dieser Artikel kollidiert nie mit der originalen Artikelnummer. Du kannst zudem auch nicht versehentlich einen neuen Artikel versenden.

## Retouren-Modul

Mit dem Retoure-Modul (**Lager & Logistik > Retoure**) ist es möglich, aus den Belegen (Auftrag, Lieferschein, Rechnung) eine Retoure zu erstellen. Im Vergleich zum bisherigen RMA-Modul muss so noch kein primärer Wareneingang erfolgen, um einen Retouren-Eintrag im System zu erzeugen. Stattdessen werden Retouren immer zunächst als solche im System erfasst und danach per Wareneingangsbeleg gebucht. Das hat auch den Vorteil, dass du für den Kunden vorab ein Transportlabel/Retourenschein für den Rückversand übermitteln kannst. Wie du Retouren im Retouren-Modul anlegen kannst, liest du[hier](https://help.xentral.com/hc/articles/360016764099#UUID-c22344fc-f20e-937d-0ee7-ad77535ee85b). Außerdem kannst du im Modul[Retouren Gründe](https://help.xentral.com/hc/articles/360016809179#UUID-197b3aa5-1ada-b1a0-897b-23f6799bf5c7)Vorlagen für Retouren-Gründe definieren, die du dann aus dem Drop-Down Menü auswählen kannst.