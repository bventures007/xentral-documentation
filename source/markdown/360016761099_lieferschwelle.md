Mit dem Modul „Lieferschwelle“ besteht die Möglichkeit Lieferschwellen für ein bestimmtes Land generell oder für einen bestimmten Artikel zu hinterlegen. Es kann eingestellt werden, ob sich der Steuersatz beim Erreichen eines gewissen Umsatzes automatisch anpasst und ob über das Erreichen der Lieferschwelle per E-Mail benachrichtigt werden soll.

Das One-Stop-Shop Verfahren stellt ab 01.07.2021 die Basis für die Umsetzung der EU-Mehrwertsteuerreform dar. Für B2C Geschäfte innerhalb Europas gilt damit eine einheitliche Lieferschwelle von 10.000€. Sobald Waren von insgesamt 10.000€ ins EU Ausland geliefert wurden, ist in allen EU Ländern der Steuersatz des Bestimungslandes auszuweisen und abzuführen. Informationen dazu findest du[hier](https://help.xentral.com/hc/de/articles/4402395359890#UUID-9db3d441-a701-4c55-b1fc-cc9e7313f28b).

## Übersicht

In der Übersicht werden alle hinterlegten Lieferschwellen aufgelistet.

Über "+ Neue Lieferschwelle" kann eine neue Lieferschwelle erstellt werden.

Es ist möglich, verschiedene Lieferschwellen auch in Bezug auf ein Lagerland einzustellen. Das heißt es können verschiedene Länder hinterlegt werden, in denen Sie ein Lager besitzen. Dadurch kann die Lieferschwelle entweder direkt gezogen oder die Einstellung für eine spezielle Lieferschwellenhöhe getätigt werden.

Trage in der Übersicht "Lieferschwelle" folgendes ein:

- Empfängerland:Land, für das die Lieferschwelle gelten soll
- Lager:Kann aufLageroderHauptlagergesetzt werden, um dem System mitzuteilen, dass man im Empfängerland selbst ein Lager besitzt und somit für jeden Auftrag in das Empfängerland der dort geltende Umsatzsteuersatz zu verwenden ist. SobaldLageroderHauptlagerausgewählt ist, berücksichtigt xentral, dass dieser Umsatz nach lokalen MwSt.-Sätzen auf der Rechnung abgebildet werden muss. Der Umsatz wird aber nicht in die Summe von 10.000 € eingerechnet.
- Lieferschwelle in EUR:Wert der verkauften Waren im Zielland bis zum Erreichen der Lieferschwelle.
- Ust-ID:Ihre USt.-ID im Zielland. In den Geschäftsbriefvorlagen als Variable {DELIVERYTHRESHOLDVATID} verfügbar. Die Variablemuss zwingendgroß geschrieben werden
- Steuersatz normal:Normaler USt.-Satz im Zielland
- Steuersatz ermäßigt:Ermäßigter USt.-Satz im Zielland
- Steuersatz spezial:Spezieller USt.-Satz im Zielland
- in Ursprungsland:Spezieller USt.-Vergleichssatz im Ursprungsland
- Überschreitung ab:Datum der Überschreitung der Lieferschwelle - wird vom System gesetzt
- Aktueller Umsatz:Aktueller Gesamtumsatz im Zielland - wird mit der Überschreitung der Lieferschwelle nicht weiter aufaddiert. Hier werden freigegebene Rechnungen als Grundlage genommen. Gutschriften mindern den Umsatz nicht
- Netto Preise anpassen:Du hast folgende Optionen für die Übertragung von Nettopreisen vom Online-Shop:
  - Keine Anpassung: Die Nettopreise vom Online-Shop werden ohne Anpassung in den Auftrag übernommen. Der Bruttopreis für den Kunden kann dadurch abweichen.
  - Nur mit Lieferschwelle-Artikeln: Die Nettopreise von Artikeln, die als Lieferschwelle-Artikel gekennzeichnet sind, werden beim Auftragsimport aus einem Online-Shop ggf. angepasst. Der Bruttobetrag dieser Artikel bleibt für den Kunden gleich.
  - Immer anpassen: Die Nettopreise aller Artikel werden beim Auftragsimport aus einem Online-Shop ggf. angepasst. Der Bruttobetrag der Artikel bleibt für den Kunden gleich.
- Lieferschwelle aktiv:Die Lieferschwelle ist aktiv und der eingestellte Steuersatz wird verwendet. Dieser Haken wird automatisch gesetzt, wenn die "Lieferschwelle in EUR", also die Gesamtumsätze in das Land, überschritten wurden. Als Messgröße dienen die Beträge freigegebener Rechnungen

Trage in der Übersicht "Erlöskonten" folgendes ein:

- Erlöskonto normal:Erlöskonto normal für die Buchung von Erlösen nach der Überschreitung der Lieferschwelle
- Erlöskonto ermäßigt:Erlöskonto ermäßigt für die Buchung von Erlösen nach der Überschreitung der Lieferschwelle
- Erlöskonto befreit:Erlöskonto befreit für die Buchung von Erlösen nach der Überschreitung der Lieferschwelle

> **Anmerkung**
>
> Für eine erfolgreiche DATEV-Übertragung müssen die Konten zuvor hinterlegt sein.

Weitere Informationen findest du[hier](https://help.xentral.com/hc/de/articles/4402395359890#UUID-9db3d441-a701-4c55-b1fc-cc9e7313f28b).

## Artikel

Im Reiter "Artikel" kann Ware hinterlegt werden, die im Zielland einer anderen Steuerklasse zugeordnet ist, als im Ursprungsland.

### Artikel hinzufügen

Mit der Schaltfläche „Neuer Artikel“ lässt sich ein neuer Artikel hinzufügen.

- Artikel:Artikel, der im Zielland in eine andere USt.-Klasse eingruppiert wird als im Ursprungsland
- Empfängerland:Zielland
- Steuersatz:Veränderter USt.-Satz im Zielland
- Bemerkung:Interne Anmerkung
- Aktiv:Nur aktive Artikel werden berücksichtig

Artikeleinstellungen sind nur dann aktiv, wenn unterLieferschwellefür das zugehörige Land im FeldNetto-Preise anpassendie OptionNur mit Lieferschwelle-Artikelnausgewählt wurde.

## Einstellungen

In den Einstellungen wird das Verhalten beim Erreichen der Lieferschwelle festgelegt.

- E-Mail bei Überschreitung:Bei der Überschreitung der Lieferschwelle wird eine E-Mail an einen oder mehrere Empfänger verschickt
- Umsatzzähler erhöhen:Wenn "beim Freigeben": Bei der Freigabe von Rechnungen wird der Betrag hochgezählt. Bei der Überschreitung der Lieferschwelle werden automatisch die USt.-Sätze des Ziellandes verwendet
- Bei Überschreitung neue Steuer verwenden:Bei der Überschreitung der Lieferschwelle werden automatisch die USt.-Sätze des Ziellandes verwendet
- E-Mail Empfänger:Empfänger (mehrere Empfänger können per; getrennt eingegeben werden: pers1@example.com;pers2@example.com)
- Empfängername:Empfänger (mehrere Empfänger können per; getrennt eingegeben werden)
- Betreff:Betreff der gesendeten E-Mail
- Text:Inhalt der gesendeten E-Mail. Verwenden der angegebenen Variablen in geschweiften Klammern, um die E-Mail mit Informationen zur überschrittenen Lieferschwelle anzureichern
- Projekte ausschließen:In diesem Bereich kannst du Projekte vom Einfluss des Moduls Lieferschwelle ausschließen. Klicke dazu auf +Neuer Eintrag, gib den Namen des jeweiligen Projekts ein und speichere

Hinweis bzgl. EU Lieferung:Für die Lieferschwelle wird die Besteuerung und die UST-ID ausgewertet, nicht der Typ einer Adresse (Herr/Frau/Firma).

**Hinweis:** Bei aktiver Lieferschwelle kann die Besteuerung im Auftrag nicht nachträglich geändert werden. Einstellungen für die Lieferschwelle werden bei Auftragsanlage übernommen, Änderungen des Felds "Besteuerung" im Auftrag wirken sich nicht aus. Wenn ein Auftrag mit Lieferung in ein Land, für das eine Lieferschwelle aktiv ist, ohne Lieferschwelle abgewickelt werden soll, weil z.B. der Kunde die Ware im Inland abholt, musst du vor Auftragsanlage in der Adresse den Haken bei "Lieferschwelle nicht anwenden"(Tab: Zahlungskonditionen/Besteuerung) setzen.

## Erlöskonten pflegen

In Xentral gibt es verschiedene Module, in welchen Erlöskonten hinterlegt werden können. Nachfolgend siehst du die Reihenfolge der unterschiedlichen Möglichkeiten nach Relevanz. Das bedeutet, die Einstellungen in den Lieferschwellen stechen beispielsweise die anderen Einstellungen immer aus, da sie für jedes Land unterschiedlich sind.

Du hast die folgenden Möglichkeiten:

1. Einstellungen der angelegten Lieferschwellen (Lieferschwelle > Übersicht)
1. Einstellungen im betroffenen Artikel (Stammdaten > Artikel > Details > Finanzbuchhaltung)
1. Einstellungen in der betroffenen Artikelkategorie (Artikel Kategorien > Übersicht > Details)
1. Einstellungen im Projekt (Stammdaten > Projekt > Einstellungen > Steuer / Währung)
1. Grundeinstellungen (Administration > System > Grundeinstellungen)