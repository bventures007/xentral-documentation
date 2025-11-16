In der Auftragsübersicht im Menü **Verkaufen > Auftrag ** wird dir für jeden Auftrag die so genannte Auftragsampel angezeigt. Die Auftragsampel dient dazu, den aktuellen Status eines Auftrags nachzuvollziehen. Sie zeigt dir, welche Schritte der Auftragsbearbeitung bereits abgeschlossen wurden und welche noch offen sind. Dabei werden bereits abgeschlossene Schritte mithilfe **grüner Symbole ** angezeigt. Offene und noch zu prüfende Prozessschritte erkennst du an der **roten ** Farbe. Bei Aufträgen, die sich noch im Entwurfsmodus befinden, werden sämtliche Symbole der Auftragsampel als **blaue Kreise ** angezeigt. Bei stornierten Aufträgen enthält die Auftragsampel**graue** Symbole mit einem Kreuz.

Die Auftragsampel wird durch Prozessstarter *autoversand_berechnen* laufend aktualisiert. Der Prozessstarter wird auch ausgeführt, wenn du einen Auftrag zur Bearbeitung öffnest. Dadurch kann der Status in der Auftragsampel in einem Auftrag von der in der Auftragsübersicht abweichen. So können einige Symbole in der Auftragsübersicht immer noch als offen (rot) angezeigt werden, während sie im geöffneten Auftrag bereits als abgeschlossen (grün) angezeigt werden. In diesem Fall wird die Auftragsampel in der Auftragsübersicht aktualisiert, sobald du in das Menü **Verkaufen > Auftrag** zurückkehrst.

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in die Auftragsampel**
>
> Möchtest du dir innerhalb weniger Minuten einen Überblick über die Funktionen und die Nutzung der Auftragsampel in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/YpXdaiTE6cw)** Die Auftragsampel findest du in der SpalteMonitordes Menüs ** Verkaufen > Auftrag**.

![auftragsuebersicht_ampel_1.png](https://help.xentral.com/hc/article_attachments/18609919300124)

Die Auftragsampel wird auch im Auftrag selbst angezeigt, wenn du ihn öffnest. In diesem Fall findest du die Auftragsampel direkt oben im Auftrag neben der Auftrags- und Kundennummer.

![auftragsuebersicht_ampel_2-de.png](https://help.xentral.com/hc/article_attachments/18609871489564)

Sobald ein Auftrag den StatusAbgeschlossenerreicht hat, werden dir in der SpalteMonitorgraue Symbole mit einem Haken angezeigt. Diese zeigen dir, dass die Auftragsbearbeitung in Xentral erfolgreich abgeschlossen wurde.

Aufträge können auf verschiedenen Wegen den StatusAbgeschlossenerreichen:

- Über den Auto-Versand. Weitere Informationen findest du im Artikel [Aufträge an Versandprozesse übergeben (Xentral Auto-Versand)](https://help.xentral.com/hc/de/articles/6113578120092#UUID-d9ce4c66-b4ed-5121-ace3-a2be70b43b4e).
- Manuell durch die Erstellung entsprechender Belege (beispielsweise Lieferscheine und Rechnungen)
- Durch Verarbeitung des Auftrags im Modul **Übertragungen**. Weitere Informationen findest du im Artikel [Übersicht: Fulfillment-Dienstleister (3PL) anbinden](https://help.xentral.com/hc/de/articles/360016738020#UUID-72f37f06-2871-0785-7286-1f7a2707c88d).

## Bedeutung der Auftragsampel-Symbole

Schau dir die Informationen in der folgenden Tabelle an, um mehr über die Bedeutung der einzelnen Symbole innerhalb der Auftragsampel zu erfahren.

> **Anmerkung**
>
> Die folgende Tabelle enthält alle Auftragsampel-Symbole, die standardmäßig in Xentral angezeigt werden. Beachte, dass du Symbole auch ausblenden kannst, falls gewünscht. Wie das geht, erfährst du im KapitelAuftragsampel-Symbole deaktivieren. Außerdem hast du die Möglichkeit, eigene Auftragsampel-Symbole hinzuzufügen. Informationen zu diesen individuellen Symbolen findest du im KapitelZusätzliche Auftragsampel-Symbole hinzufügen.

| | Der Auftrag befindet sich im Entwurfsmodus |
| --- | --- |
| | Der Auftrag wurde storniert |
| | Alle Bearbeitungsschritte und Prüfungen für den Auftrag wurden abgeschlossen |
| **Lagerbestand** |
| | Ausreichender Bestand vorhanden |
| | Für mindestens ein Artikel kein ausreichender Bestand vorhanden |
| **Portoberechnung** |
| | Porto-Berechnung korrekt durchgeführt |
| | Der Auftrag enthält keinen Porto-Artikel (bezieht sich auf eine Projekt-Versandmethode, bei der ein Portoartikel enthalten sein muss) |
| **Umsatzsteuer-ID-Prüfung für Geschäftskunden im europäischen Ausland** |
| | Umsatzsteuer-ID-Prüfung erfolgreich oder nicht erforderlich |
| | Umsatzsteuer-ID-Prüfung fehlgeschlagen oder nicht ausgeführt |
| **Zahlungseingang** |
| | Bereits vollständig bezahlt |
| | Teilzahlung vorhanden |
| | Vorauszahlung nicht erfolgt |
| **Berechnung der Nachnahmegebühr** |
| | Nachnahmegebühr wie geplant berechnet oder keine Nachnahmegebühr erforderlich |
| | Berechnung der Nachnahmegebühr nicht erfolgt |
| **Freigabe für Auto-Versand** |
| | Für den Auto-Versand freigegeben |
| | Für den Auto-Versand gesperrt (nur manuelle Freigabe möglich) |
| **Kundenprüfung** |
| | Kundenprüfung erfolgreich oder nicht erforderlich ⚠️ **Wichtig:** Dieses Symbol wird künftig aus der Auftragsübersicht entfernt! |
| **Adressvalidierung** (Anzeige nur bei Verwendung des Moduls [Adressvalidierung](https://help.xentral.com/hc/de/articles/14307279799068#UUID-94254e89-9257-9493-f357-aef3f31e546e)) |
| | Adressvalidierung erfolgreich durchgeführt |
| | Adressvalidierung nicht erfolgreich |
| **Datumsprüfung für Liefertermin** |
| | Lieferdatum am aktuellen Tag oder kein geplantes Lieferdatum |
| | Lieferdatum in der Zukunft |
| **Kreditlimit des Kunden** |
| | Ausreichendes Kreditlimit vorhanden oder kein Kreditlimit festgelegt |
| | Kreditlimit überschritten |
| **Liefersperre für Kunden** |
| | Lieferung zulässig oder keine Liefersperre vorhanden |
| | Liefersperre aktiv |
| **Produktion** (Anzeige nur bei Verwendung des Moduls [Produktion](https://help.xentral.com/document/preview/25841#UUID-c5c2af4d-468b-cc9e-c77c-ef9bd6d80483)) |
| | Keine Produktion vorhanden |
| | Produktion wurde angelegt |
| | Produktion wurde genehmigt |
| | Produktion wurde gestartet |
| | Produktion wurde abgeschlossen |
| | Produktion wurde ausgelagert |
| | Produktion wurde teilweise ausgelagert |
| | Produktion wurde nicht ausgelagert |
| | Produktion wurde eingelagert |
| | Produktion wurde teilweise eingelagert |
| | Produktion wurde nicht eingelagert |
| | Die Produktion wurde abgelehnt (Ausschuss) |

## Auftragsampel-Symbole deaktivieren

Wenn du bestimmte Symbole der Auftragsampel bei deiner täglichen Auftragsabwicklung mit Xentral nicht benötigst, hast du die Möglichkeit, diese gezielt zu deaktivieren. Auf diese Weise werden sie in der Auftragsübersicht im Menü **Verkaufen > Auftrag** und in Aufträgen selbst ausgeblendet.

Gehe wie folgt vor, um Auftragsampel-Symbole zu deaktivieren.

1. Öffne das Menü Einstellungen > Administration > Systemeinstellungen.
1. Scrolle nach unten, bis du den Bereich Auftragsampeln ausblenden erreichst.
1. Wähle die Auftragsampel-Symbole aus, die nicht mehr angezeigt werden sollen, indem du sie mit einem Häkchen markierst.
1. Scrolle nach unten und klicke auf Speichern.

> **Wichtig**
>
> Auch wenn du die Anzeige einiger Symbole deaktiviert hast, werden weiterhin Prüfprozesse für den Auto-Versand im Hintergrund ausgeführt. Hast du beispielsweise das Symbol für die Bestandsprüfung deaktiviert und es kein ausreichender Bestand vorhanden, um den Auftrag abzuwickeln, steht die Option für den Auto-Versand erst dann wieder zur Verfügung, wenn ausreichend Bestand vorhanden ist.

## Zusätzliche Auftragsampel-Symbole hinzufügen

Neben der allgemeinen Auftragsampel bietet Xentral dir auch das ModulAuftragsampel. Mithilfe dieses Moduls kannst du die Auftragsampel um weitere Prozessschritte ergänzen und diese Schritte per zusätzlichem Symbol innerhalb der Auftragsampel anzeigen lassen. Das macht Sinn, wenn du beispielsweise deine Mitarbeiter auf die notwendige Personalisierung von Artikeln oder auf extra Aufgaben wie eine manuelle Adressprüfung aufmerksam machen möchtest.

Gehe wie folgt vor, um Auftragsampel-Symbole hinzuzufügen.

1. Nutze die Smart Search, um das Modul **Auftragsampel** zu öffnen.
1. Nimm im Bereich **Anlegen ** des Tabs **Übersicht** die Einstellungen wie in der Tabelle unten beschrieben vor.
1. Klicke auf **Speichern**.

> **Tipp**
>
> Wenn du erstmalig einen zusätzlichen Prozessschritt im Auftrag als erledigt markierst, erscheint ein neuer Filter namens **Auftragsampel ** für den zusätzlichen Prozessschritt oben im Menü**Verkaufen > Auftrag **. Das angezeigte Symbol hängt von dem Symbol an, das du im Modul ** Auftragsampel**ausgewählt hast. Klicke auf das Symbol neben dem neuen Filter, um Aufträge je nach Status der Erledigung des neuen Prozessschritts zu filtern.
>
> Filtersymbol
> Handlung
> Alle Aufträge anzeigen
> Nur Aufträge anzeigen, bei denen der zusätzliche Prozessschritt als erledigt markiert wurde
> Nur Aufträge anzeigen, bei denen der zusätzliche Prozessschritt noch offen ist

Wenn du ein oder mehrere zusätzliche Auftragsampel-Symbole in Xentral nutzt, bildest du also zusätzliche Arbeitsschritte ab, die passend auf dein Unternehmen zugeschnitten sind. Nach erfolgreicher Bearbeitung dieser Schritte innerhalb der Auftragsabwicklung solltest du sie nach Abschluss auch im System entsprechend als "erledigt" markieren, sodass die Darstellung der Symbole auf **grün** wechselt.

Gehe wie folgt vor, um zusätzliche Prozessschritte als "erledigt" zu markieren.

1. Öffne das Menü **Verkaufen > Auftrag**.
1. Öffne den gewünschten Auftrag.
1. Öffne das Tab **Auftragsampel**.
1. Markiere den Eintrag mit dem gewünschten Icon per Klick auf die Checkbox namens **Fertig**.
1. Gib bei Bedarf einen Kommentar zur Fertigstellung des Prozessschritts ein, z.B. "Artikel personalisiert" oder "Adresse geprüft".
1. Klicke auf **Speichern**.