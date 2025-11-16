> **Wichtig**
>
> Die hier beschriebene Funktionalität ist aktuell nur fürXentral-Kunden mit einem Pro-Vertrag verfügbar.

InXentral kannst du Versandlabels gesammelt ausdrucken, um wertvolle Zeit im Versand zu sparen und somit deine Produkte noch schneller an deine Kunden auszuliefern. Diese Optimierung ist in spezifischen Fällen für dich interessant, die wir am Besten an den folgenden Beispielen deutlich machen können:

- **Aufträge mit jeweils einer einzigen, identischen Auftragsposition**: Du versendest zum Beispiel im Rahmen einer Werbeaktion eine Tragetasche mit deinem Firmenlogo an all deine Bestandskunden. In jeder Sendung befindet sich ein Exemplar dieser Tragetasche. Oder du veranstaltet einen zeitlich limitierten Flash-Sale in deinem Shop, bei dem ein bestimmtes Produkt nur einmal bestellbar ist, beispielsweise als Einführungsangebot oder im Rahmen einer Sonderaktion.
- **Aufträge mit mehreren identischen Auftragspositionen **: Du versendest im Rahmen deiner Werbeaktion die oben erwähnte Tragetasche, aber zusätzlich auch einen Kugelschreiber und ein Notizbuch an deine B2B-Kunden. Jede Sendung enthält dabei eine Tragetasche, einen Kugelschreiber und ein Notizbuch. In solchen Fällen kannst du den Sammeldruck der Versandlabels auf spezielle Projekte (in diesem Fall ** B2B** anwenden.

> **Anmerkung**
>
> In beiden Beispielen ist es ganz egal, auf welchen Versandkarton welches Versandlabel angebracht wird - denn jede Bestellung verfügt über den identischen Inhalt, der an Kunden versendet wird. Und genau das machst du dir beim Sammeldruck von Versandetiketten in Xentral zum Vorteil: Die mühsame Einzelbearbeitung von Aufträgen über das Versandzentrum entfällt. Während ein Teil deiner Lagermitarbeiter die benötigten Artikel in Kartons packt, können direkt im Anschluss die bereits im Voraus ausgedruckten Versandlabels angebracht werden, ohne dass jeder einzelne Paketinhalt zeitaufwändig kontrolliert und separaten Empfängern zugeordnet werden muss.

Um in den oben beschriebenen Anwendungsfällen den Versandprozess zu beschleunigen und zu vereinfachen, sind einige vorbereitende Einstellungen in Xentral notwendig. Hauptsächlich ist hier das Modul[Picklisten-Profile](https://help.xentral.com/hc/de/articles/360016722600#UUID-a3288421-c888-8d23-a2a3-e7de468d630b)relevant, mit dem du ganz genau steuerst, für welche Aufträge der Sammeldruck von Versandlabels ausgeführt wird.

In den folgenden Kapiteln erfährst du Schritt für Schritt, welche Einstellungen du in Xentral vornehmen musst und wie später der konkrete Versandprozess abläuft.

### Achtung

Beachte **vor der weiteren Einrichtung** folgende Einschränkungen und Hinweise für den Sammeldruck von Versandlabels:

- Diese Funktion steht nur für Aufträge mit der Versandart **DHL **, ** GLS **, ** UPS (OAuth)**, ** Sendcloud** und den [Carrier Integration Service](https://help.xentral.com/hc/de/articles/21036407616924#UUID-f3131fcf-e600-8b3e-abd3-e1a661adf83e) zur Verfügung.
- Der Sammeldruck von Versandlabels funktioniert nur für Artikel, die sich **im gleichen Lager ** befinden und die in den Artikelstammdaten als **Lagerartikel** markiert sind.
- Aufträge, die Artikel mit Mindesthaltbarkeitsdaten, Seriennummern und Chargen beinhalten, sind vom Sammeldruck von Versandlabels ausgenommen.
- Der Sammeldruck von Versandlabels kann zu Performanceproblemen in Xentral, führen. Dies äußert sich in verlängerten Ladezeiten bei der Arbeit mit dem System.

## Picklisten-Profil erstellen

Im ersten Schritt erstellst du ein Picklisten-Profil für deinen Anwendungsfall. Picklisten-Profile werden benötigt, um für die gewünschten Aufträge automatisch Picklisten zu generieren, sodass das Lagerpersonal die Kommissionierung durchführen kann. Außerdem sorgt das Picklisten-Profil dafür, dass die benötigten Versandlabels automatisch als Stapel über den gewünschten Etikettendrucker gedruckt werden und sofort bereitstehen, wenn die Pakete fertig gepackt sind.

> **Tipp**
>
> Benötigst du weitere Hintergrundinformationen zu Picklisten-Profilen und ihrer Funktionsweise? Dann schau dir unseren Artikel zum ThemaPicklisten-Profile genauer an.

Gehe wie folgt vor, um ein Picklisten-Profil für den Sammeldruck von Versandlabels zu erstellen.

1. Nutze die Smart Search, um das Modul **Picklisten-Profile** zu öffnen.
1. Klicke oben rechts auf **+ NEU**.
1. Vergib im Feld **Bezeichnung** einen eindeutigen Namen für das Picklisten-Profil, zum Beispiel * Sammeldruck_Versandlabels*.
1. **Optional **: Trage im Feld ** Kommentar** eine Bemerkung ein, die für dich und deine Mitarbeiter sichtbar ist und den Zweck des Profils näher beschreibt.
1. Nimm im Bereich **Eigenschaften Pickliste** folgende Einstellungen vor:
  1. Option **Aufträge**: Lege fest, ab welcher Anzahl von Aufträgen mit identischem Inhalt das Picklisten-Profil greifen soll. In unserem Beispiel entscheiden wir uns, ab 10 identischen Aufträgen das Picklisten-Profil automatisch Picklisten generieren zu lassen, da wir bei weniger als 10 Aufträgen unseren regulären Versandprozess als ausreichend befinden.
  1. Option **Identischer Paketinhalt**: Diese Option muss zwingend aktiviert werden, damit das Picklisten-Profil die Aufträge mit identischem Inhalt verarbeiten und somit die Versandlabels als Stapel gedruckt werden können.
1. Nimm im Bereich **Ausführung Picklisten erstellung** folgende Einstellungen vor:
  1. Aktiviere die Option **Automat. Ausführung**.
  1. Klicke auf **Filter bearbeiten**, um einen Zeitpunkt für die Ausführung des Picklisten-Profils zu erstellen. In unserem Beispiel entscheiden wir uns für eine automatische Ausführung täglich um 05:00 Uhr, sodass die Versandlabels morgens bereitstehen, sobald das Lagerpersonal die Arbeit aufnimmt und somit direkt mit dem Versand starten kann.
1. Nimm im Bereich **Filter Aufträge** folgende Einstellungen vor:
  1. Wähle für die Option **Lager ** den Lagerplatz aus, das die Artikel enthält, für deren Bestellungen der Sammeldruck von Versandetiketten stattfinden soll. In unserem eingangs beschriebenen Beispiel lagern unsere Taschen, Kugelschreiber und Notizbücher im Lagerplatz **Hauptlager**.
  1. **Optional **: Schränke das Picklisten-Profil auf ein bestimmtes ** Projekt **ein, falls du unterschiedliche Anwendungsfälle für dein ** B2B **und ** B2C**

-Business oder den Vertrieb über einen spezifischen Online-Shop umsetzen möchtest.
1. Nimm im Bereich **Versandeinstellungen** folgende Einstellungen vor:
  1. Wähle für die Option **Drucker Versandlabel** den Drucker aus, der für den Versandlabeldruck genutzt werden soll.
  1. Aktiviere die Option **Versandlabel drucken**.
  1. Aktiviere die Option **Massenlabeldruck mit Begrenzung**.
  1. Wähle dein gewünschtes **Kommissionierverfahren ** aus. In unserem Beispiel entnehmen wir die Artikel direkt ihren Lagerplätzen und platzieren sie in den Versandkartons - ohne weiteren Qualitäts-Scan. Daher wählen wir die Option **Einfache Lagerbuchung ohne weiteren Prozess**.
1. Klicke auf **Speichern**, nachdem du alle Einstellungen für das Picklisten-Profil vorgenommen hast.

## Ablauf im Lager und beim Versand

Nachdem du die notwendigen Voreinstellungen durchgeführt hast, schauen wir uns nun an, wie der Sammeldruck von Versandlabels konkret in der Praxis funktioniert.

Im Folgenden bekommst du einen Überblick über den Ablauf und die verschiedenen Bearbeitungsschritte in Xentral und in deiner Versandabteilung.

1. Das von dir definierte Picklisten-Profil prüft alle Aufträge in Xentral.
1. Alle Aufträge, die den Regeln des Picklisten-Profils entsprechen, werden in Picklisten überführt.
1. Der Prozessstarter **batches** wird in Xentral ausgeführt.
1. Nach dem Durchlauf des Prozessstarters werden die benötigten Versandlabels für die Aufträge in den entsprechenden Picklisten automatisch ausgedruckt.
1. Dein Lagerpersonal holt am Etikettendrucker die Versandlabels ab.
1. An den im Sammeldruck enthaltenen Start- und Trennlabels können direkt die benötigten Artikel abgelesen werden. Bei einem kleinen Lager mit übersichtlichem Sortiment kann das Lagerpersonal diese Labels nutzen, um die Artikel zu picken. Falls die Kartons schon vorgepackt sind, kann anhand dieser Labels der Inhalt kontrolliert werden.
1. Die Versandlabels werden an den vorbereiteten Versandkartons angebracht. Wie eingangs erwähnt: Es spielt keine Rolle, welcher Karton welches Versandlabel erhält, da alle Aufträge aus identische Inhalten bestehen.

### Kennzeichnung durch Start- und Endlabels

Beim Sammeldruck von Versandlabels wird nicht nur eine Reihe von Versandlabels ausgedruckt. Vielmehr unterstütztXentral dich dabei, den Überblick zu behalten, damit du zwischen Aufträgen aus verschiedenen Picklisten unterscheiden kannst und schnellstmöglich auf etwaige Fehler aufmerksam gemacht wirst.

Zu Beginn des Sammeldrucks gibt der Etikettendrucker folgendes Startlabel aus:

![startlabel.png](https://help.xentral.com/hc/article_attachments/22020172069148)

> **Anmerkung**
>
> Das Startlabel zeigt dir auf einen Blick, ob der Labeldruck für einen bestimmten Auftrag fehlgeschlagen ist. Außerdem sind Artikelname, -menge und die Picklisten-ID vermerkt.

Nach dem Startlabel werden direkt aufeinanderfolgend die Versandlabels ausgegeben. Je nach Anzahl der Label entsteht dabei ein langer Streifen an Labels - denke also darüber nach, einen Eimer oder Ähnliches unter dem Etikettendrucker zu positionieren. So kann das Lagerpersonal die Labels einfach an einem festen Platz entnehmen, sobald sie fertig gedruckt wurden.

Nach dem letzten Versandlabel wird das Endlabel gedruckt. Das sieht wie folgt aus:

![endlabel.png](https://help.xentral.com/hc/article_attachments/22020172070812)

> **Tipp**
>
> Falls zu einem Auftrag kein Versandlabel automatisch gedruckt werden konnte, siehst du unten auf dem Label den Namen des Kunden, die Lieferscheinnummer und einen Barcode. Mit fehlgeschlagenen Labels geschieht folgendes:
>
> - Für den betroffenen Lieferschein legt Xentral automatisch einen Klärfall im Versandzentrum an.
> - Vor Ort im Lager scannst du den abgedruckten Barcode mit deinem Handscanner, um den betroffenen Lieferschein direkt zu öffnen und das Versandlabel manuell zu erstellen.

## Troubleshooting

Wenn der automatische Sammeldruck einzelner Versandlabels fehlschlägt, liegt die Ursache in den meisten Fällen an Fehlern bei der Kundenadresse, die im Lieferschein erfasst ist. Hier empfehlen wir die Verwendung des XentralModuls **Adressvalidierung**, das dich bereits vor dem Versandprozess über fehlerhafte Adressen informiert.

> **Tipp**
>
> Weitere Informationen zur Adressvalidierung und den benötigten Einstellungen findest du im ArtikelAdressprüfung für Logistikprozesse (Adressvalidierung).

Falls der automatische Ausdruck der Versandlabels trotz aktivierter Adressvalidierung weiterhin nicht funktioniert oder gar nicht erst gestartet wird, probiere folgende Lösungen aus:

- Öffne das Modul **Versandzentrum ** und klicke dann auf **Kommissionierläufe **. Rechts in der Spalte ** Menü** kannst du per Klick auf das Drucker-Symbol ganz rechts den Sammeldruck erneut anstoßen.
- Öffne das Modul **Druckaufträge**, um zu prüfen, ob ein Druckauftrag erteilt wurde.
- Überprüfe den ausgewählten Drucker in den Einstellungen des Picklisten-Profils sowie die Druckerkonfiguration an sich.

Wurden die Versandlabels bereits wie gewünscht gedruckt und du benötigst einen zweiten Ausdruck der gleichen Labels, beispielsweise weil die Etiketten beschädigt wurden?

- Öffne das Modul **Kommissionierung **. Klicke rechts in der Spalte ** Menü** auf das Drucker-Symbol ganz rechts, um die Versandlabels erneut auszudrucken.