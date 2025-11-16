Über das Modul “Sammeldebitoren” ist es möglich abweichende Debitorennummern für bestimmte Gruppen bzw. Debitoren zu nutzen. Diese können für verschiedene Varianten festgelegt werden. Im Finanzbuchhaltungsexport sind die abweichenden Debitorennummern anschließend sichtbar.

## Übersicht

In der Übersicht werden alle Regeln aufgelistet.

### Neue Regel

Mit dem Klick auf "+Neu" kann eine neue Regel definiert werden.

Dieses Modul ermöglicht das Aufstellen von Regeln anhand von den nachstehenden Attributen.

- Zahlungsweise → eine bestimmte Zahlungsweise soll immer verwendet werden
- Kanal (z.B. Shop) → Aufträge stammen von einem bestimmten Shop
- Lieferland → Aufträge sind an ein ausgewähltes Lieferland adressiert
- Projekt → einem bestimmten Projekt angehören
- Kundengruppe → einen Kunden beinhalten, der einer ausgewählten Kundengruppe angehört
- Buchungskonto → Die abweichende Debitorennummer (im Kunde und im Finanzbuchhaltung Export sichtbar)
- In Adresse speichern → Nie = die abweichende Debitorennummer wird nie im Kunden gespeichert, “Nur bei Neukunden” = Die abweichende Debitorennummer wird nur für Neukunden hinterlegt und “Bei allen Adressen (überschreibt)” = Für alle betroffenen Kunden wird die abweichende Debitorennummer zusätzlich angelegt bzw. je nach Rangfolge überschrieben

Die Spalte Reihenfolge gibt die Reihenfolge wieder in der die abweichenden Debitorennummern vergeben werden (z.B. Nr 1. vor 2)

> **Anmerkung**
>
> Bei Bestandskunden müssen die Kriterien wie z.B. die Zahlungsweise bereits in den Kundenstammdaten hinterlegt sein, damit die abweichende Debitorennummer genutzt werden kann. Es ist möglich auch Kombinationen verschiedener Kriterien einzustellen.

## Anwendungsbeispiel Sammeldebitoren

Wird nun eine Rechnung erstellt (und freigegeben) die die Zahlungsweise Vorkasse besitzt, wird das folgende Feld im Kunden gemäß der Einstellung im Modul ausgefüllt:

![SD-3.png](https://help.xentral.com/hc/article_attachments/5077617652508)

### Finanzbuchhaltungs Export mit Sammeldebitoren

Wird nun ein Buchhaltungsexport durchgeführt der nach Positionen gruppiert ist, erscheint hier die abweichende Debitorennummer:

![collectivedebitors_3.png](https://help.xentral.com/hc/article_attachments/5077578520860)