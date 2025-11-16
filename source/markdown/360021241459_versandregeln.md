Mithilfe des Moduls **Versandregeln** kannst du flexible Regelwerke aufbauen, anhand derer Xentral automatisch eine Versandart für einen Auftrag auswählt, sobald ebendiese Versandregeln zutreffen. Versandregeln können auf dem Umsatz, dem Gewicht, den enthaltenen Artikeln, dem Lieferland, der Zahlungsweise oder anderen Parametern basieren.

Durch die Verwendung von Versandregeln kannst du einen Teil deiner Versandabwicklung automatisieren und somit Zeit sparen, da du in diesem Fall nicht mehr den Versanddienstleister in jedem Auftrag manuell auswählen musst. Stattdessen wird der Versanddienstleister automatisch aufgrund der von dir bestimmten Kriterien vorausgewählt.

## Typische Anwendungsfälle für Versandregeln

Die Festlegung von Versandregeln ist besonders dann für dich interessant, wenn du mit mehr als einem Versanddienstleister zusammenarbeitest und zusätzlich auch in mehrere Länder versendest. Im Folgenden findest du einige praxisnahe Beispiele:

- In der Praxis werden Versandregeln oft verwendet, um die Versandart für Aufträge zu ändern, die bestimmte Werte überschreiten. Ein Anwendungsfall ist beispielsweise die Änderung der Versandart je nach Sendungsgewicht. In diesem Fall wird bis zu einem Sendungsgewicht von 1,00 kg die Versandart **DHL Kleinpaket ** gewählt und ab 1,01 kg der reguläre Paketversand über die Versandart **DHL National **. Bei einem Sendungsgewicht über 31,5 kg wird die Versandart ** Spedition** zugeordnet.
- Die Versandart kann auch auf Basis des Ziellandes ausgewählt werden. Beispielsweise kannst du alle Aufträge mit dem Zielland **Deutschland ** in der Empfängeradresse automatisch mit der Versandart **DHL National ** versehen lassen, und analog dazu alle Aufträge mit dem Zielland **Österreich ** per **POST.AT ** versenden. Für die restlichen EU-Länder kann dann die Versandart**UPS** automatisch zugeordnet werden.
- Du bietest deine Artikel auf verschiedenen Verkaufskanälen an. Einige davon erfordern vielleicht einen schnelleren Versand der Artikel. Du kannst ganz einfach Versandregeln pro Verkaufskanal erstellen, sodass du Bestellungen aus bestimmten Verkaufskanälen eine Express-Versandart zuweisen kannst. So entsprichst du den Anforderungen des jeweiligen Marktplatzes und stellst zusätzlich sicher, dass die bestellten Artikel schnell bei denen Endkunden ankommen.

## Features

Das Modul **Versandregeln** in Xentral enthält die folgenden Features:

- Definition von Regeln, sodass Xentral automatisch eine bestimmte Versandart auswählt, sobald bestimmte Bedingungen zutreffen
- Anwendung der Regeln auf manuelle und importierte Aufträge: Bei manuellen Aufträgen schlägt Xentral dir eine Änderung der Versandmethode vor. Bei importierten Aufträgen wird die Versandart automatisch anhand der Regeln angepasst.
- Festlegung einer Vielzahl von Versandregeln und gezielte Steuerung der Anwendung mithilfe von Prioritäten

> **Warnung**
>
> Beachte die folgenden Einschränkungen für die Verwendung von Versandregeln in Xentral:
>
> - Es ist nicht möglich, automatisch die optimale Versandart auszuwählen, z.B. im Hinblick auf die Versandkosten. Die Auswahl der Versandart basiert einzig und allein auf den Einstellungen, die du innerhalb der Versandregeln vornimmst.
> - Falls Aufträge durch das Modul **Übertragungen** in Xentral importiert werden, kann die Versandart nicht mithilfe von Versandregeln geändert werden.

## Versandregeln erstellen

Gehe wie folgt vor, um Versandregeln in Xentral zu erstellen.

1. Nutze die Smart Search, um das Modul **Versandregeln** zu öffnen.
1. Klicke oben rechts im Bereich **Aktionen ** auf **+ Neue Regel**.
1. Nimm die Einstellungen wie in der folgenden Tabelle beschrieben vor.
1. Klicke auf **Speichern**.

![versandregel-einstellungen-1-en.png](https://help.xentral.com/hc/article_attachments/21202734246812)

![versandregel-einstellungen-2-en.png](https://help.xentral.com/hc/article_attachments/21202780174108)

| Einstellung | Erläuterung |
| --- | --- |
| **Name** | Gib hier einen beliebigen Namen für die Versandregel ein. Dieser Name ist nur in Xentral für dich und deine Mitarbeiter sichtbar, jedoch nicht für deine Endkunden. |
| **Ziel-Versandart** | Wähle die gewünschte Ziel-Versandart aus, die Aufträgen mit den festgelegten Kriterien zugeordnet werden soll. Wenn die Regel zutrifft, wird bei manueller Auftragseingabe ein Hinweis nach der Freigabe angezeigt. Bei Aufträgen, die aus einem Onlineshop importiert wurden, wird eine passende Regel automatisch angewandt und die Versandart im Auftrag verändert, ohne dass du selbst aktiv werden musst. |
| **Aktiv **| Aktiviere diese Option, um die Versandregel in Xentral zu aktivieren. Nur so kann die Versandregel vorgeschlagen oder automatisch ausgeführt werden. ⚠️** Wichtig:** Deaktivierte Versandregeln finden keine Anwendung! |
| **Prio **| Mithilfe der Priorisierung legst du fest, welche Regel gelten soll, falls zwei unterschiedliche Regeln auf denselben Auftrag zutreffen. Je kleiner die Zahl, die du hier eingibst, desto höher ist die Gewichtung der Regel. - Eingabe** 0 **: Höchste Gewichtung. Die Versandregel hat somit Vorrang vor anderen möglicherweise zutreffenden Versandregeln<br>- Eingabe** 1 **: Zweithöchste Gewichtung. Trifft gleichzeitig eine Versandregel mit der Priorität** 0 ** auf einen Auftrag zu, so findet die Regel mit der Priorität** 1** keine Anwendung. |
| **Artikel **| Nutze diese Einstellung, um die Versandregel je nach bestimmten, im Auftrag enthaltenen Artikeln einzugrenzen. ⚠️** Wichtig:** Achte bei dieser Einstellung darauf, welche Operatoren du verwendest. Bei Verwendung der Operatoren <, > oder zwischen musst du die Artikel-ID und ausdrücklich nicht die Artikelnummer angeben. Am Einfachsten findest du die Artikel-ID, wenn du im Menü Verkaufen > Artikel den gewünschten Artikel öffnest. Die allerletzten Ziffern der URL (oben in der Adressleiste deines Browsers, direkt nach dem =-Zeichen) stellen die Artikel-ID dar. Du kannst sie anschließend bei der Erstellung der Regel im Modul Versandregeln eintragen. |
| **Fast-Lane** | Wähle aus, ob die Versandregel für Aufträge greifen sollen, die zuvor mithilfe der [Fast-Lane](https://help.xentral.com/hc/de/articles/360018083500#UUID-f6daef86-8b7a-d629-b91b-0175831892b3) als priorisierte Aufträge markiert wurden. |
| **Auftragssumme** | Hier kannst du Eingrenzungen bezüglich der Auftragssumme vornehmen, sodass die Versandregel, falls gewünscht, gezielt auf besonders niedrige oder hohe Auftragssummen angewandt werden kann. |
| **Zahlungsweise** | Lege eine Zahlungsweise fest, damit die Versandregel nur für Aufträge mit genau dieser Zahlungsweise angewandt wird. |
| **Versandart **| Wähle hier die Versandart aus, die ursprünglich am Auftrag hinterlegt ist. Die Versandregel greift dann für alle Aufträge mit dieser Versandart und ändert sie zur zuvor in der Regel definierten ** Ziel-Versandart**. |
| **Projekt **| Diese Einstellung erlaubt dir, die Versandregel gezielt auf die Aufträge eines bestimmten Projekts anzuwenden. ⚠️** Wichtig:** Die Versandregel greift in diesem Fall lediglich für Aufträge des ausgewählten Projekts und lässt alle Aufträge aus anderen Projekten unberührt, auch wenn die in der Versandregel definierten Kriterien auch dort zutreffen würden. Überlege dir also sorgfältig, ob du diese Einstellung nutzt! |
| **Lieferland** | Wähle ein Lieferland aus, für die die Versandregel gelten soll. Das Lieferland ist in diesem Fall das Zielland, in die die Bestellung geliefert wird, also das Land der Kundenadresse. |
| **Shop** | Wähle hier den Shop aus, über den der Auftrag dich erreicht hat. Somit wird die Versandregel nur für Aufträge aus diesem spezifischen Verkaufskanal angewandt. |
| **Volumen **| Gib hier das Volumen des Auftrags ein, um die Versandregel anhand dieser Eigenschaft anzuwenden. 💬** Anmerkung:** Deine Angabe in diesem Feld muss der Summe der Volumina aller Artikel im Auftrag entsprechen. Du kannst das Volumen eines Artikels berechnen, indem du die Maße miteinander multiplizierst (Länge x Breite x Höhe). Beispielrechnung: Länge: 5 cm, Breite: 10 cm, Höhe: 25 cm = 1250. Die Abmessungen des Artikels findest du unter Verkaufen > Artikel > [Artikel öffnen] > Bereich: Lager/Abmessungen. |
| **Gewicht** | Schränke die Versandregel anhand des Gesamtgewichts des Auftrags ein. Bei Gewichtsangaben unter 1 kg muss ein Dezimalpunkt verwendet werden. Angaben, die ein Komma enthalten werden nicht gewertet. Ein Gewicht von 100 g gibst du also als 0.1 kg an. |

### Verfügbare Operatoren für Versandregeln

Innerhalb der Einstellungen für Versandregeln sind verschiedene Operatoren verfügbar. Diese Operatoren kannst du nach Belieben verwenden oder leer lassen, falls ein Kriterium nicht in der Regel angewandt werden soll.

Es gibt einen Unterschied zwischen den Operatoren **=** und ** in **. Betrachten wir die Einstellung ** Artikel**, erkennst du folgende Unterschiede:

- Verwendung des Operators **=**: Nur ein bestimmter Artikel darf exklusiv im Auftrag enthalten sein, damit die Versandregel Anwendung findet. Sind weitere Artikel im Auftrag enthalten, wird die Regel ** nicht** angewandt.
- Verwendung des Operators **in**: Hiermit können mehrere Artikel zu einer Versandregel hinzugefügt werden. Ist ein beliebiger Artikel dieser Versandregel in einem Auftrag enthalten, wird die Regel angewandt. Dabei können auch andere Artikel im Auftrag enthalten sein.
- **Besonderheiten bei JIT-Stücklisten **: Just-in-time (JIT) Stücklisten kannst du nur mit dem Operator ** in **registrieren. Die Verwendung des Operators**=** ist ** nicht** möglich.

> **Wichtig**
>
> Beachte, dass nicht jeder Operator für jede Einstellungsmöglichkeit sinnvoll ist. Die Operatoren **<** und **>** machen bei metrischen Angaben wie beispielsweise dem ** Gewicht **Sinn, finden aber keine Anwendung bei den Einstellungen zum ** Projekt**.

## Versandregeln anwenden

Nachdem du[wie oben beschrieben](#UUID-b0348b4e-1c8b-a85c-4458-f5fd59567909_id_360021241459_id_h_01FAMTHGP40ZP37SCKMZEDC08D)deine benötigten Versandregeln in Xentral erstellt hast, fragst du dich vermutlich, wie diese Versandregeln konkret zur Anwendung kommen.

Die Antwort hängt davon ab, ob du deine Aufträge manuell angelegt hast, oder ob Aufträge automatisiert (z.B. über einen Online-Shop) in Xentral importiert werden.

> **Tipp**
>
> Benötigst du noch mehr Informationen zur manuellen Auftragsanlage oder einen Überblick über die Möglichkeiten zum Auftragsimport in Xentral? Dann schau dir folgende Artikel genauer an:
>
> - Auftragserfassung und Datenpflege
> - Aufträge importieren und exportieren

- **Manuelle Auftragsanlage **: Sobald du in einem manuell angelegten Auftrag auf ** Freigeben **klickst, wird eine Meldung mit dem Text "Es wurde eine Versandregel gefunden. Versandart ändern?" angezeigt, falls eine Versandregel zutrifft. Per Klick auf ** Versandart ändern** wird die Ziel-Versandart im Auftrag hinterlegt.
- **Automatischer Auftragsimport**: Diese Aufträge erreichen dein System über die Schnittstelle zu deinen angebundene Online-Shops oder sonstige Importmöglichkeiten. Im Zuge dieses Imports wird die von dir aufgestellte Versandregel automatisch berücksichtigt und die gewünschte Ziel-Versandart am Auftrag hinterlegt. Du hier also nicht aktiv werden und kannst wie gewohnt mit der Auftragsbearbeitung fortfahren.

## Historie einsehen

Im Tab **Historie ** werden die Aufträge angezeigt, bei denen du im Zuge der manuellen Auftragsanlage in XentralAuftrag bei der Meldung "Es wurde eine Versandregel gefunden. Versandart ändern?" auf**Versandart ändern** geklickt hast. Die Ansicht der ausgeführten Änderungen in der Historie erlaubt dir, im Zweifelsfall nachzuvollziehen, ob und welche Regeln angewandt wurden.

## Beispielhafte Anwendungsfälle

### Versandart nach Sendungsgewicht zuordnen

In der Praxis werden oft Versandregeln genutzt, die eine Änderung der Versandart nach Gewichtsstaffeln vorsieht. In diesen Fällen ist es nützlich, wenn du dir vorab eine Gewichtsstaffel erstellst und erst dann für jede Regel eine entsprechende Versandregel in Xentral anlegst.

Hier ist eine Beispiel-Matrix für eine Gewichtsstaffel:

| Regel | von | bis | Versand per | Versandart in Xentral | Produkt |
| --- | --- | --- | --- | --- | --- |
| Gewicht in kg | 0.01 | 0.5 | Warensendung | **internetmarke** | Bücher- und Warensendung 500 g |
| kg | 0.51 | 1.0 | DHL Kleinpaket (ehemals Warenpost) | **dhl** | Bücher- und Warensendung 1000 g |
| kg | 1.01 | 3.0 | DHL Paket National | **dhl** | Paket (bis 31,5 kg) |
| kg | 3.01 | 31.5 | DPD Classic | **dpdapi** | Paket (bis 31,5 kg) |
| kg | 31.6 | 1000 | Spedition | **spedition** | Palettenversand |

Unabhängig mit welcher Versandart die Aufträge im System importiert oder angelegt werden, soll laut der Gewichts-Regel die gewünschte Versandart gewählt werden.

Lege entsprechend fünf verschiedene Versandregeln fest. Für diese gibst du eine Bezeichnung und die Gewichtsspanne sowie die gewünschte Versandart ein.

### Versandart nach Sendungsgewicht und Lieferland zuordnen

Ein weiterer Anwendungsfall ist die automatische Zuordnung einer Versandart für bestimmte Lieferländer. Die Zuordnung je nach Lieferland wird häufig zusätzlich zu einer Staffelung nach Sendungsgewicht vorgenommen. Wir erweitern in diesem Anwendungsfall also das oben beschriebene Beispiel zum Sendungsgewicht um das zusätzliche Kriterium des Lieferlands.

Im folgenden Beispiel soll die zuvor erstellte Gewichtsklasse generell, also unabhängig vom Lieferland, gültig sein. Nur für den Fall, dass das Zielland Österreich ist, soll den Aufträgen eine andere Versandart zugeordnet werden.

Wir fügen also folgende Regel für das Lieferland Österreich hinzu. Hier soll generell immer DPD gewählt werden, egal welches Gewicht der Auftrag hat:

| Regel | = | Versand per | Versandart in Xentral | Produkt |
| --- | --- | --- | --- | --- |
| Lieferland | Österreich | DPD | **dpdapi** | Paket |

InXentral gibst du bei der Neuanlage der Regel die Priorität **0** sowie das Lieferland Österreich an.

Da in den Regeln nach Gewichten zuvor keine Vorgabe für das Lieferland eingetragen wurde, müssen wir hier mit einer Priorisierung arbeiten. Denn bei Aufträgen mit dem Lieferland Österreich würde nun eine Regel aufgrund des Gewicht und dem Land greifen.

Durch Vergabe der Priorität **0** wird die Regel nach Lieferland bevorzugt. Alle weiteren Regeln werden schwächer gewichtet (0 > 1 > 2 > 3 > 4 > 5).