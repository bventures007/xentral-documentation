Mit den so genannten Lagerampeln bietet dir Xentral eine ganz neue Möglichkeit, jederzeit auf die aktuellsten Berechnungen der Lagerbestände für deine Aufträge zuzugreifen. Diese Funktionalität richtet sich an fortgeschrittene Systemnutzer und ermöglicht eine genaue Steuerung der Bestandszuteilung sowie Einstellungen zur Anzeige der verfügbaren Lagerbestände in der Auftragsübersicht.

In diesem Artikel erläutern wir, welche Bedeutung die Symbole der Lagerampel haben, die als Teil der gewohnten[Auftragsampel](https://help.xentral.com/hc/de/articles/360016759019#UUID-a67e1eee-4a52-2b43-3f73-4782e28d05b7)zur Verfügung stehen. Außerdem beschreiben wir hier die Einstellungen, die du vornehmen kannst, um ein effizientes **First In - First Out** Prinzip (FIFO) oder eine freie Bestandszuteilung für deine Aufträge in Xentral zu verwalten.

## Variante für die Bestandszuteilung auswählen

Zunächst solltest du dir überlegen, wie Xentral bei der Zuteilung von Warenbeständen für Aufträge vorgehen soll.

Grundsätzlich gibt es zwei Möglichkeiten, die im Folgenden näher beschrieben werden.

### Achtung

Beachte folgende Einschränkungen und Hinweise, bevor du die neue Zuteilungslogik aktivierst:

- **Manuelle Reservierungen**: Bestände, die bereits manuell in Xentral reserviert wurden, werden nicht berücksichtigt. Nähere Informationen zur manuellen Bestandsreservierung findest du im Kapitel [Reservierung für einen Auftrag](https://help.xentral.com/hc/de/articles/4402048488722#UUID-b7b9b68a-45e7-fb72-d417-718dacbbc32a_id_Reservierungen-ReservierungfreinenAuftrag).

### Freie Bestandszuteilung

Die so genannte freie Zuteilung bedeutet, dass die Zuteilung von Warenbeständen für jeden Auftrag individuell stattfindet. Dabei wird die Bestandszuteilung nicht durch ältere, also schon länger in Xentral bestehende und auf Warenbestand wartende Aufträge blockiert oder beeinflusst.

Im Detail bedeutet das:

- Jeder Auftrag ist bereit zur Weiterverarbeitung, sobald streng für ihn allein genommen ausreichend Warenbestand vorhanden ist.
- Bei der Bestandszuteilung findet **keine Priorisierung** anhand Kriterien wie z.B. dem Erstellungsdatum des Auftrags statt.
- Neuere Aufträge können zuerst bearbeitet werden, wenn ihr Warenbestand vollständig verfügbar ist. Ältere Aufträge, die zusätzlich auf fehlende Artikel warten, bleiben zurück. Es kann also passieren, dass sobald nachbestellte Artikel eintreffen, andere benötigte Waren inzwischen für neuere Aufträge verwendet wurden. Dadurch kann sich die Bestandszuteilung und damit die weitere Bearbeitung für die älteren Aufträge weiter verzögern.

Nimm die folgenden Systemeinstellungen in Xentral vor, um die freie Bestandszuteilung zu aktivieren.

1. Nutze die Smart Search, um das Modul **Grundeinstellungen** zu öffnen.
1. Öffne das Tab **System**.
1. Aktiviere im Bereich **Beschleunigung/Limitierungen ** die Option **Verbesserte Zuteilung von Warenbestand bei Lagerampel-Berechnung**.
1. Wähle im Dropdown-Menü **Bestandszuteilung ** die Option **Freie Zuteilung** aus.
1. Klicke auf **Speichern**.

### First In - First Out (FIFO) für Aufträge

Mit First In - First Out (kurz: FIFO) für Aufträge erreichst du in XentralFolgendes: Die ältesten Aufträge im System bekommen als Erstes den benötigten Warenbestand zugeteilt, sodass die entsprechenden Artikel anschließend für den Versand vorbereitet werden können und die Auftragsabwicklung fortgesetzt werden kann.

> **Anmerkung**
>
> **Prüfkriterien der Bestandszuweisung bei First In - First Out für Aufträge**
>
> Wenn du dich für diese Variante entscheidest, finden zunächst im Hintergrund folgende Prüfungen des Auftrags nacheinander statt. Anhand dieser Prüfungen wird die passende Reihenfolge ermittelt, in der Aufträgen der benötigte Bestand zugeteilt wird.
>
> - Zuerst wird Folgendes geprüft: Befindet sich der **Auftrag in der Fast-Lane**? Aufträge mit Fast-Lane Markierung werden bevorzugt zu Aufträgen ohne diese Markierung einpriorisiert.
> - Als Nächstes wird das **Reservierungsdatum** geprüft, das am Auftrag hinterlegt ist. Hier gilt weiter das Prinzip: Aufträge werden höher priorisiert, je länger das Reservierungsdatum zurückliegt.
> - Nun wird das **Belegdatum** des Auftrags in Xentral geprüft. Aufträge mit den am weitesten zurück liegenden Belegdaten werden zuerst berücksichtigt.
> - Zuletzt wird noch die Reihenfolge geprüft, in dem die Aufträge in Xentral **erstellt** wurden.

Um festzulegen, dass die ältesten Aufträge zuverlässig nach FIFO Bestand zugewiesen bekommen, musst du vorab in Xentral die folgenden Systemeinstellungen vornehmen.

![settings_fifo_bestand-de.png](https://help.xentral.com/hc/article_attachments/20044763267100)

1. Nutze die Smart Search, um das Modul **Grundeinstellungen** zu öffnen.
1. Öffne das Tab **System**.
1. Aktiviere im Bereich **Beschleunigung/Limitierungen ** die Option **Verbesserte Zuteilung von Warenbestand bei Lagerampel-Berechnung**.
1. Wähle im Dropdown-Menü **Bestandszuteilung ** die Option **FIFO** aus
1. Klicke auf **Speichern**.

## Bedeutung der Lagerampel-Symbole

Wie du bereits weißt, kannst du den aktuellen Stand der Auftragsbearbeitung immer auf einen Blick in der Auftragsübersicht oder in einem geöffneten Auftrag auf einen Blick erkennen - und zwar mithilfe der[Auftragsampel](https://help.xentral.com/hc/de/articles/360016759019#UUID-a67e1eee-4a52-2b43-3f73-4782e28d05b7).

Innerhalb der Auftragsampel findest du auch das Symbol für den Lagerbestand, das je nach Situation unterschiedlich dargestellt wird. Je nachdem, ob du dich für[die freie Zuteilung](#UUID-ec127141-b3a4-0baf-0c32-7f4e168d6b79_section-idm234797633839577)oder[FIFO](#UUID-ec127141-b3a4-0baf-0c32-7f4e168d6b79_section-idm234797634490709)für die Bestandszuteilung in Xentral entschieden hast, werden diese Symbole unterschiedlich dargestellt und geben dir somit einen detaillierten Einblick.

> **Wichtig**
>
> Die unten gezeigten Symbole stehen in direktem Zusammenhang mit der neuen Logik für die Bestandszuteilung in Xentral. Das bedeutet, dass du dich für die Testphase anmelden musst, um die neuen Symbole sehen und nutzen zu können. Melde dich bei Interesse bei deinem Onboarding Manager, um deine Instanz freischalten zu lassen.

Im Folgenden findest du einen Überblick aller möglichen Symbole der Lagerampel. So kannst du genauer nachvollziehen, welche Bedeutung die Symbole haben.

### Symbole bei der freien Bestandszuteilung

Wenn du dich für[die freie Bestandszuteilung](#UUID-ec127141-b3a4-0baf-0c32-7f4e168d6b79_section-idm234797633839577)entschieden hast, gibt es je nach Status der Bestandszuweisung die folgenden Darstellungsformen für das Lager-Symbol innerhalb der Auftragsampel.

| Symbol | Erläuterung |
| --- | --- |
| | Der für den Auftrag benötigte Bestand ist teilweise verfügbar, d.h. mindestens eine Auftragsposition ist in der geforderten Menge lieferbar. Der Auftrag ist also teillieferbar. |
| | Der für den Auftrag benötigte Bestand ist unter Berücksichtigung der Bestände im Nachschublagerplatz verfügbar. Der Auftrag ist also lieferbar, wenn Artikel aus dem Nachschublagerplatz umgelagert werden. |
| | Der für den Auftrag benötigte Bestand ist vollständig verfügbar. Der Auftrag ist also vollständig lieferbar. |
| | Der für den Auftrag benötigte Bestand ist nicht verfügbar. Der Auftrag ist also nicht lieferbar. |

### Symbole bei First In - First Out für Aufträge

Wenn du dich für[FIFO](#UUID-ec127141-b3a4-0baf-0c32-7f4e168d6b79_section-idm234797634490709)für die Bestandszuteilung entschieden hast, gibt es je nach Status der Bestandszuweisung die folgenden Darstellungsformen für das Lager-Symbol innerhalb der Auftragsampel.

> **Tipp**
>
> Bei der Bestandszuweisung nach First In - First Out enthält die Auftragsampel nicht nur ein, sondern zwei Symbole für den Lagerbestand.
>
> Dabei zeigt dir das erste Symbol an, ob der Auftrag gemäß des FIFO-Prinzips für die Bestandszuweisung an der Reihe ist. Am zweiten Symbol erkennst du, ob im Lager genug Bestand vorhanden ist, um den betreffenden Auftrag kurzfristig vorzuziehen, also auf Wunsch schneller an die Logistik zu übergeben und anschließend an deine Kunden auszuliefern.

| Symbol | Erläuterung |
| --- | --- |
| | Die Bestandszuweisung für den Auftrag wird momentan durchgeführt. |
| | Der für den Auftrag benötigte Bestand ist teilweise verfügbar, d.h. mindestens eine Auftragsposition ist in der geforderten Menge lieferbar. Der Auftrag ist also teillieferbar und der Auftrag ist an der Reihe, als nächstes verfügbaren Bestand zugewiesen zu bekommen. |
| | Der für den Auftrag benötigte Bestand ist unter Berücksichtigung der Bestände im Nachschublagerplatz verfügbar. Der Auftrag ist also lieferbar, wenn Artikel aus dem Nachschublagerplatz umgelagert werden. |
| | Der für den Auftrag benötigte Bestand ist vollständig verfügbar. Der Auftrag ist also vollständig lieferbar und der Auftrag ist an der Reihe, als Nächstes den verfügbaren Bestand zugeteilt zu bekommen. |
| | Entweder ist der für den Auftrag benötigte Bestand nicht verfügbar. Der Auftrag ist also momentan nicht lieferbar. Zusätzlich wird dieses Symbol auch angezeigt, wenn dem Auftrag im Rahmen der FIFO-Prinzips aktuell noch kein Bestand zugewiesen werden kann, da andere Aufträge vor diesem Auftrag an der Reihe sind, den verfügbaren Bestand zugewiesen zu bekommen. |

## Filter in der Auftragsübersicht

Sobald du die freie Bestandszuteilung oder First In - First Out (FIFO) für Aufträge aktiviert hast, stehen dir zusätzlich zu den oben beschriebenen Lagerampel-Symbolen auch neue Filtermöglichkeiten in der Auftragsübersicht zur Verfügung. So kannst du schnell und einfach die Aufträge in der Übersicht sortieren und erkennen, welche Aufträge über ausreichend Bestand verfügen und somit weiter bearbeitet werden können.

Diese Auftragsfilter stehen zur Verfügung:

- **Lieferung nicht möglich **

-** Lieferung möglich mit Nachschub **

-** Teillieferung mögl. **>** Tipp**
>
> Auf Wunsch kannst du mehrere dieser Filter gleichzeitig aktivieren. Dabei werden die Filterkriterien nicht untereinander kombiniert, sondern die Ergebnisse gemeinsam aufgelistet (**ODER **

-Verknüpfung, nicht ** UND**). Du kannst also beispielsweise Aufträge für die Lieferungen mithilfe der Bestände im Nachschublagerplatz gemeinsam mit den Aufträgen, für die eine Teillieferung möglich ist, in einer Liste darstellen, wenn du die beiden Filter aktivierst.

Gehe wie folgt vor, um die Filter in der Auftragsübersicht zu verwenden.

1. Öffne das Menü **Verkaufen > Auftrag**.
1. Klicke oben links über der Tabelle auf das **Filter-Symbol**.
1. Wähle einen oder mehrere Filter aus.

![filter_verbesserte_bestandszuteilung-de.png](https://help.xentral.com/hc/article_attachments/20044804739740)