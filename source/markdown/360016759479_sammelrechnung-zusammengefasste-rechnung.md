In Xentral besteht die Möglichkeit, Sammelrechnungen zu erstellen, die nicht strikt an einen Auftrag oder Teilauftrag gebunden sind, sondern einzelne Positionen aus verschiedenen Aufträgen umfassen. Die Ansicht '**Sammelrechnungen**' enthält eine Liste von Kunden, für die es aktuell abzurechnende Auftragspositionen gibt.

## Was ist eine Sammelrechnung?

Eine Sammelrechnung, auch Zusammengefasste Rechnung genannt, ist ein Dokument, das mehrere Einzeltransaktionen, Lieferungen oder Lieferscheinpositionen eines Kunden zu einer einzigen Rechnung konsolidiert. Dies geschieht, um den Abrechnungsprozess zu vereinfachen und zu rationalisieren, insbesondere in Situationen, in denen ein Kunde viele kleinere Bestellungen oder Lieferungen innerhalb eines bestimmten Zeitraums tätigt. Dadurch wird die Abrechnung erleichtert und der Verwaltungsaufwand reduziert.

## Funktionen

Diese Funktionen stehen dir im Modul **Sammelrechnung ** zur Verfügung: **Datenkonsolidierung**:

- Zusammenfassung mehrerer Lieferscheine oder Bestellungen eines Kunden zu einer einzigen Rechnung.
- Möglichkeit, Positionen aus verschiedenen Aufträgen und Teilaufträgen eines Kunden zu kombinieren.

**Filter- und Auswahlmöglichkeiten**:

- Auswahlkriterien für die einzuschließenden Lieferscheine oder Aufträge (z.B. Zeitraum, Kunde, Projekt).

**Preisanpassung**:

- Anpassung von Preisen der abzurechnenden Positionen für die zu erstellende Rechnung **Detaillierte Positionsübersicht**:

- Anzeige von Artikelnummer, Bezeichnung, Menge, Lieferdatum, Preis und Rabatt für jede Position.
- Kennzeichnung und Bearbeitung von Positionen (z.B. als kostenlos markieren, entfernen)

**Integrations- und Verknüpfungsoptionen**:

- Verknüpfung der zusammengefassten Rechnung mit den zugehörigen Lieferscheinen und Aufträgen.
- Möglichkeit, Kundenbestellnummern und Auftragsnummern in die Rechnung aufzunehmen.

**Sicherheits- und Berechtigungsmanagement**:

- Zugriffskontrolle, sodass nur autorisierte Benutzer zusammengefasste Rechnungen erstellen und bearbeiten können.

## Eine neue Sammelrechnung erstellen

Das Modul **Sammelrechnung ** kannst du über **Appstore > Sammelrechnung ** oder über die Smart-Search über**Sammelrechnung** aufrufen.

### Schritte um Positionen zur Abrechnung anzeigen zu lassen

1. Lege einen Auftrag an, füge Positionen hinzu und gib den Auftrag über die **Freigabe** frei.
1. Führe den Auftrag zu einem Lieferschein weiter. Alternativ kannst du einen Auftrag auch ohne Rechnungserstellung über einen Logistikprozess abwickeln.
1. Der Lieferschein erscheint nach der Freigabe des Dokuments im Modul **Sammelrechnung** in der Auflistung des entsprechenden Kunden.

![sammelrechnung_001.png](https://help.xentral.com/hc/article_attachments/14589123556636)

#### Basis für Sammelrechnungen

> **Anmerkung**
>
> Diese Voraussetzungen müssen zutreffen, damit deine offenen abzurechnenden Positionen in der Übersicht Sammelrechnung angezeigt werden:
>
> - **Lieferscheine**: Freigegebene und nicht stornierte Lieferscheine bilden die Grundlage.
> - **Auftragsverknüpfung**: Lieferscheine können, müssen aber nicht mit einem Auftrag verknüpft sein.
> - **Rechnungsrelevanz**: Lieferscheine dürfen nicht den Haken "keine Rechnung" gesetzt haben.
> - **Kostenlose Positionen**: Lieferscheinpositionen dürfen nicht als kostenlos markiert und nicht bereits abgerechnet sein.
> - **Projektrechte (Mitarbeiter)**: Ausschliesslich Lieferscheinpositionen, für die du ein gültiges Recht für das zugehörige Projekt besitzt, sind für dich sichtbar. Admins sehen alle Projekte und somit alle Lieferscheinpositionen.

> **Warnung**
>
> Wichtige Hinweise
>
> - **Kundenaufträge**: Eine Sammelrechnung bezieht sich nur auf (Teil-)Aufträge eines bestimmten Kunden.
> - **Lieferscheine**: Zu den Aufträgen des Kunden müssen bereits die entsprechenden Lieferscheine generiert sein.
> - **Besteuerungsarten**: Gemischte Besteuerungsarten können nicht in einer Rechnung mit dem Modul Sammelrechnung übernommen werden.

### Schritte um eine neue Sammelrechnung zu erstellen

1. Wähle in der Sammelrechnung Übersicht einen Kunden aus und klicke auf **bearbeiten**.
  Bei vielen Einträgen kannst du den Kunden auch über die Eingabe der Kundennummer in das Suchfeld oder die Spaltensuche aus der Liste erhalten.

1. In der Ansicht für diesen Kunden werden dir alle offenen Positionen aus Lieferscheinen angezeigt, die noch nicht abgerechnet wurden (Bedingungen s.o.).
1. Wähle die abzurechnende(n) Position(en) aus indem du das Häkchen vor der Positionszeile setzt. **Optional**: bei Bedarf kannst du den Positionsbetrag abändern.
1. Setze in der ‘**Stapelverarbeitung**’ die für dich wichtigen Einstellungen z.B. Anzeige der Auftragsnummer.
1. Klicke auf '**Markierte Positionen in Sammelrechnung nehmen**'.
1. Die neue Rechnung wird mit den Positionen erstellt und direkt freigegeben. Sie erhält eine Rechnungsnummer.

![sammelrechnung_003.png](https://help.xentral.com/hc/article_attachments/14589102731804)

> **Anmerkung**
>
> Im Protokoll der Rechnung werden die zugehörige Aufträge und Lieferscheine der abgerechneten Positionen angezeigt.

## Funktionen der Stapelverarbeitung

| Positionsauswahl | |
| --- | --- |
| alle markieren | Mit dieser Auswahl kannst du alle oben aufgelisteten Positionen anwählen oder abwählen. |
| *Lieferdatum* | |
| Lieferdatum aus Lieferschein | Für die Rechnung wird das Lieferdatum aus dem Lieferschein verwendet. |
| Lieferdatum aus Lieferscheinpositionen | Für die Rechnung wird das Lieferdatum aus der Lieferscheinposition verwendet. Sollte eine Position kein Datum eingetragen haben, wird das Datum des Lieferscheins eingetragen. |
| *Andruck auf der Rechnung* | |
| inkl. Ihre Bestellnummer | Die Bestellnummer des Kunden wird in die Rechnung übernommen. |
| inkl. Auftragsnummer | Die Auftragsnummer der Position wird in die Rechnung übernommen. |
| inkl. aller offenen Portoartikel aus Auftrag | alle offenen Positionen inkl. Porto werden in die Rechnung übernommen. Z.B. Versandkosten aus mehreren Aufträgen. |
| *Aktion für die Ausführung* | |
| Markierte Positionen in Sammelrechnung nehmen | Die neue Rechnung wird mit den Positionen erstellt und direkt freigegeben. Sie erhält eine Rechnungsnummer. |
| Markierte Positionen auf nicht abrechnen setzen | Die Positionen werden aus der Liste entfernt und können nicht mehr abgerechnet werden. |

## Übersicht Sammelrechnung

Die Übersicht der Funktion Sammelrechnung zeigt dir alle Kunden an, zu denen es offene und abzurechnende Positionen gibt. Für die Schnellansicht kannst du auf das Pfeil Icon klicken und einzelne Kunden durchsehen.

Die **Suchoptionen ** ermöglichen dir eine Filterung nach**Kundennummer **, ** Kundenname ** oder eine **Volltextsuche**. Die Liste der Kunden kannst du dir ebenso als CSV oder PDF anzeigen lassen.

![sammelrechnung_002.png](https://help.xentral.com/hc/article_attachments/14589072482588)

## Übersicht einzelner Kunde

Die **Suchoptionen ** ermöglichen dir eine Filterung nach**Auftrag **, ** Auftragsdatum, Lieferschein, Lieferscheindatum, Artikelnummer, Artikelbezeichnung, Lieferdatum, Preis, Rabatt, Gesamtpreis, Menge ** oder eine **Volltextsuche**. Die Liste der Positionen kannst du dir ebenso als CSV oder PDF anzeigen lassen.

![sammelrechnung_004.png](https://help.xentral.com/hc/article_attachments/14589113092636)

## Sammelrechnung Einstellungen

> **Anmerkung**
>
> Das Modul Sammelrechnung hat keine Systemeinstellungen.

## FAQ **Frage **: Warum tauchen in einer Sammelrechnung Positionen oder Mengen wieder auf, die ich zuvor in der Rechnung gelöscht habe? ** Antwort**: Eine Sammelrechnung ist eine eigenständige Rechnung. Sie fasst nicht bereits existierende Rechnungen zusammen, sondern erstellt aus den Lieferscheinen eine neue Rechnung, die Positionen aus mehreren Aufträgen enthält. Die Sammelrechnung nimmt die Positionen direkt aus den Lieferscheinen, nicht aus bestehenden Rechnungen (auch wenn diese aus den Lieferscheinen erstellt wurden). Wenn du eine Position oder Menge in einer Rechnung änderst, erscheint sie in der Sammelrechnung wieder, da die Lieferscheine durch Änderungen in der Rechnung nicht automatisch aktualisiert werden.In diesem Fall musst du die Position, die du ändern oder löschen möchtest, auch im Lieferschein anpassen (Schreibschutz entfernen → bearbeiten), nicht nur in der Rechnung. Danach kannst du den Auftrag wieder in eine neue Sammelrechnung mit den aktualisierten Positionen übernehmen.