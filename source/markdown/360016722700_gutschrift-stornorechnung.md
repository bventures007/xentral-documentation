Eine Rechnung kann mit einer Gutschrift oder Stornorechnung storniert werden. Die Stornierung einer Rechnung in der Buchhaltung erfolgt immer mit einem "Gegendokument". Eine Gutschrift wird in Xentral als Stornorechnung betitelt, wenn die Option "Stornorechnung" gesetzt wird. Die Beträge im Beleg werden dann negativ, während diese in der Gutschrift positiv sind.

Es gibt folgende Möglichkeiten:

- Rechnung stornieren → erzeugt direkt eine Stornorechnung oder Gutschrift ("löschen" Icon)
- Rechnung weiterführen als Gutschrift / Stornorechnung → erzeugt direkt eine Stornorechnung oder Gutschrift (gleiche Funktion, aber über das "Aktionsmenü")
- Gutschrift / Stornorechnung erstellen ohne vorhergehende Rechnung → kann rückwirkend aber auch auf eine Rechnung verknüpft werden

> **Anmerkung**
>
> Bitte überprüfen, ob die erstellte Gutschrift auch freigegeben wurde und eine fortlaufende Nummer erhalten hat. Nur dann wird die stornierte Rechnung auch beim Buchhaltungsexport mit einem negativen Betrag exportiert.

## Rechnung stornieren

Eine Rechnung kann mit der Aktion "stornieren" als Gutschrift / Stornorechnung weitergeführt werden:

![gutschrift_3155.png](https://help.xentral.com/hc/article_attachments/5077578552860)

Sobald eine Gutschriftnummer vergeben wurde, kann das Dokument nicht mehr gelöscht werden. Eine Gutschrift kann vor dem Abschicken:

- noch auf einen anderen Kunden umgebucht werden
- ebenso ist es möglich, den Betrag abzuändern und die Positionen zu bearbeiten (evtl. eine 0 EUR Gutschrift, sollte hier durch ein Versehen eine Nummer vergeben worden sein)
- ansonsten gibt es noch die Möglichkeit, eine zusätzliche Gutschrift mit einem Minusbetrag zu erstellen, dann heben sich die beiden Gutschriften auf

## Rechnung weiterführen als Gutschrift

Eine Rechnung kann ebenso über das Aktionsfeld als Gutschrift / Stornorechnung weitergeführt werden.

## Gutschrift / Stornorechnung erstellen ohne vorhergehende Rechnung

Zum Erstellen einer Gutschrift gibt es folgende Möglichkeiten:

- Buchhaltung → Gutschrift → "+NEU"
- Stammdaten → Adressen → Edit-Icon → Gutschrift (Button)
- Manuell: Angebot → Auftrag → Lieferschein / Rechnung → Gutschrift / Stornorechnung

### Rechnung mit einer Gutschrift verknüpfen

Wurde die Gutschrift autonom über Buchhaltung → Gutschrift / Stornorechnung → "+NEU" erstellt, kann diese rückwirkend auf eine Rechnung verknüpft werden. Hierzu ist im Gutschrift-Dokument die Rechnungsnummer einzugeben und zu speichern.

## Rechnung teilstornieren

Über das Aktionsmenü können auch Teilstornos für Rechnungen angelegt werden.

Im nächsten Schritt erscheint eine neue Oberfläche. Dort kann ausgewählt werden, welche Position/en in einer Gutschrift übergeben werden soll/en.

Falls bereits Positionen teilstorniert wurden, werden diese nicht mehr angezeigt in der Teilstorno Oberfläche.

> **Anmerkung**
>
> Die Rechnung wird dadurch auf den Status "TEILSTORNIERT" gestellt.

## Gutschrift stornieren

Gutschriften können nur storniert werden, wenn sie im Reiter "in Bearbeitung" auftauchen, d.h. wenn sie noch im Entwurf sind.

Um bereits erstellte Gutschriften zu "stornieren", gibt es folgende zwei Optionen:

1. Falls die versehentlich erstellte Gutschrift die Rechnung komplett storniert (über den gesamten Betrag), gleichen sich die Dokumente buchhalterisch aus. Falls die Rechnung also eigentlich gar nicht hätte storniert werden sollen, so kann dem Kunden eine neue Rechnung über den gleichen Betrag ausgestellt werden. Die alte Rechnung und die falsche Gutschrift heben sich dann gegenseitig auf und die neue Rechnung hat den Status "offen".
1. Alternativ kann die Rechnung ein zweites Mal als Gutschrift weitergeführt und vor die Beträge ein "Minus" gesetzt werden (Minusgutschrift). Die ursprüngliche (versehentlich erstellte) Gutschrift wird dann wiederum durch die Minusbeträge der Minusgutschrift ausgeglichen, sodass weiterhin eine offene Forderung an den Kunden in Höhe der ursprünglichen Rechnung vorhanden ist.

## Massenbearbeitung in Gutschriften

Genau wie in Rechnungen ist es möglich, die Gutschrift-Belege durch eine Massenbearbeitung abzuarbeiten.

[]![gutschrift_3161.png](https://help.xentral.com/hc/article_attachments/5077571596316)

Filter:

- Alle offenen Gutschriften → Alle Gutschriften, die keinen Zahlungseingang haben (der diese ausgleicht) und alle Gutschriften, die keinen Eintrag im "erledigt am" Feld haben (Datumsfeld)
- Alle Gutschriften von heute → Datum der Gutschrift ist heute (Erstellungsdatum des Dokumentes)
- Alle nicht erledigten Gutschriften → Gutschriften, die im "Erledigt am" Feld (Datumseingabe)

Stapelverarbeitung

- als erledigt markieren → Setzt das "erledigt am" Datum in der Gutschrift mit dem heutigen Datum. Signalisiert, dass die Gutschrift ausgezahlt ist
- erledigt Markierung entfernen → Entfernt das "erledigt am" Datum in der Gutschrift
- per Mail versenden → Versendet die Gutschrift an die in der Gutschrift hinterlegten E-Mail Adresse
- als versendet markieren → Stellt den Status der Gutschrift auf Versendet
- Sammel-PDF → Erstellt ein Sammel-PDF der ausgewählten Gutschriften mit den Gutschrift-Belegen
- drucken → Druckt die ausgewählten Gutschriften am hinterlegten Drucker

## Nicht versendet

In diesem Reiter ist eine Übersicht über alle Gutschriften, die noch nicht versendet wurden.

## In Bearbeitung

In diesem Reiter ist eine Übersicht über alle Gutschriften, die in Bearbeitung sind.

## Gutschrift von Rechnung abziehen

Als Beispiel haben wir hierzu eine Rechnung und eine Gutschrift erstellt. Der Betrag der Rechnung ist höher. In der Gutschrift kannst du die offene Rechnungsnummer angeben:

![inline1237238906.png](https://help.xentral.com/hc/article_attachments/5077609593884)

Der Betrag der Gutschrift taucht dann im Protokoll der Rechnung auf und der Saldo wird entsprechend angepasst. Die Gutschrift wird also mit der Rechnung verrechnet.

![inline-1145631542.png](https://help.xentral.com/hc/article_attachments/5077617931932)

Danach musst du noch die Gutschrift auf erledigt setzen.

Sobald die 7,41€ überwiesen werden kannst du diese im Zahlungseingang der Rechnung zuordnen.

## Gutschrift per Lastschrift ausgleichen

Falls du Gutschriften über den Zahlungseingang mit der Zahlungsweise Lastschrift ausgleichen willst, ist es notwendig die Gutschrift auf "bezahlt" bzw. "erledigt" zu setzen. Andernfalls kann die Gutschrift per Zahlungseingang erneut ausgezahlt werden.

Um den Status einer Gutschrift zu ändern, wählst du diese in der Gutschriftenübersicht (Gutschrift / Stornorechnung>Übersicht) aus, wählst unten in der Stapelverarbeitung die Optionals erledigt markierenund klickst auf die Schaltflächeausführen.

Der Status der Gutschrift ändert sich nun und die Gutschrift kann nicht mehr in den Zahlungsverkehr geladen werden.

> **Wichtig**
>
> Ist die Gutschrift einmal in den Zahlungsverkehr geladen, wird sie durch die Statusänderung nicht verschwinden und muss über das X-Symbol manuell entfernt werden.