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

> **Anmerkung**
>
> **Hinweis**
>
> Diese App hat das LabelSpezial. Das bedeutet, dass die App für einen speziellen Anwendungsfall entwickelt wurde, der möglicherweise nicht für jeden Kunden geeignet ist.

Mit dem Modul „Überzahlte Rechnungen“ können vom Kunden überzahlte Rechnungen angezeigt werden.

## Prozessstarter aktivieren

Um die überzahlten Rechnungen in eine Liste zu laden, muss ein Prozessstarter mit folgenden Werten unter Administration → Einstellungen → System → Prozessstarter aktiviert werden:

- **Bezeichnung** → Als Bezeichnung ist "Überzahlte Rechnungen" einzugeben
- **Art** → Aus dem Drop-Down-Menü ist als Art "periodisch" auszuwählen
- **Wochentag** → Aus dem Drop-Down-Menü ist "Jeden Tag" auszuwählen
- **Startzeit** → Es ist die vorgegebene Startzeit zu belassen
- **Letzte Ausführung** → Es ist die vorgegebene Endzeit zu belassen
- **Periode** → Als Periode ist 10 in min. anzugeben
- **Typ** → Als Typ ist "Cronjob" aus dem Drop-Down-Menü auszuwählen
- **Parameter** → Als Parameter ist "ueberzahlterechnungen" einzugeben
- **Aktiv** → Durch Anhaken wird der Prozessstarter aktiviert

Es ist darauf zu achten, dass der Haken bei "Aktiv" gesetzt ist.

## Übersicht der überzahlten Rechnungen

Unter App Center → Überzahlte Rechnungen kann das Modul aufgerufen werden.

Mit dem "Stift"-Icon kann die entsprechende Rechnung angesehen werden.

> **Anmerkung**
>
> Doppelte Zahlungseingänge (auch bei Live Import) bleiben vorne und sind orange markiert, ähnlich wie beim CSV-Import.

Sofern die Rechnung voll bezahlt und anschließend eine Buchung importiert wurde, die einen anderen Buchungstext aufweist, wird diese Position nicht orange markiert, aber auch nicht automatisch gematcht. Hier muss ein manuelles Matching stattfinden.

Ist eine Rechnung noch nicht voll gedeckt und anschließend erscheint eine zweite, dazugehörige Zahlung, so wird die zweite Buchung orange markiert, da bei dieser Rechnung bereits eine Zahlung vorliegt. Voraussetzung hierfür ist, dass die Buchungstexte auf den selben Beleg verweisen.

## Einstellungen zur Toleranz

Im Reiter "Einstellungen" kann die Toleranz in EUR, die bei überzahlten Rechnungen Anwendung findet, eingetragen werden.