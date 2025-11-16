Der Auto-Versand ist die Standardmethode, um den Versandprozess in Xentral zu starten. Im Rahmen des Auto-Versands werden ein Lieferschein und eine Rechnung für deinen Auftrag erstellt. Anschließend werden die bestellten Artikel dem Lager entnommen.

> **Tipp**
>
> Auf Wunsch kannst du kannst jeweils lediglich eine Rechnung oder einen Lieferschein im Auto-Versand erstellen. Nimm dazu die entsprechenden Einstellungen direkt in der von dir genutzten Shop-Schnittstelle vor. Beachte, dass diese Einstellungsmöglichkeit je nach Schnittstelle variiert.
>
> Du kannst auch für bestimmte Kunden festlegen, welche Belege im Auto-Versand erstellt werden sollen. Öffne dazu in Xentral das MenüVerkauf > Adressenund wähle die gewünschte Adresse. Öffne dann das Tab **Zahlungskonditionen / Besteuerung ** und wähle im Dropdown-Menü**Belege im Auto-Versand erstellen** die passende Option.

Anschließend kannst du im MenüLager > Versandzentrumden Versandprozess weiterführen. Arbeitest du mit einem Fulfillment-Dienstleister zusammen, werden durch die Auslösung des Auto-Versands alle notwendigen Informationen an das entsprechende Fremdsystem übertragen.

> **Wichtig**
>
> Aufträge können nur an den Auto-Versand übergeben werden, wenn sämtliche Symbole in der Auftragsampel grün sind und sich der Auftrag im Status **Freigegeben** befindet.

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in den Auto-Versand**
>
> Möchtest du dir in nur drei Minuten einen Überblick über die Funktionen und die Nutzung des Auto-Versands in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/hDEnBSJ6HcQ)**

Du wünscht dir einen Überblick über den Ablauf und die Vorteile des Auto-Versands in Xentral? Dann schau dir unser Video-Tutorial zum Thema an:

## Einen Auftrag an den Auto-Versand übergeben

Gehe wie folgt vor, um einen einzelnen Auftrag an den Auto-Versand zu übergeben:

1. Öffne das Menü Verkauf > Auftrag.
1. Öffne einen Auftrag, indem du in die Zeile des Auftrags klickst.
  **Optional **: Öffne das Detailansicht des Auftrags über das ** Pfeil-Symbol** auf der linken Seite des Auftrags.

1. Öffne das Dropdown-Menü **Aktion** oben rechts.
1. Klicke auf **Auto-Versand: an Versandzentrum übergeben**.
1. Klicke in der anschließenden Sicherheitsabfrage auf Ok.

## Mehrere Aufträge an den Auto-Versand übergeben

Bei Bedarf kannst du auch in einem Arbeitsschritt mehrere Aufträge zugleich an den Auto-Versand übergeben. Dazu zeigt dir Xentral eine Übersicht aller Aufträge an, die in den Auto-Versand übergeben werden können.

Gehe wie folgt vor, um zu dieser Übersicht zu gelangen und die benötigten Aufträge für den Auto-Versand auszuwählen.

1. Öffne das Menü Verkauf > Auftrag > Tab: Versandübergabe.
1. Wähle die Aufträge aus, die du an den Auto-Versand übergeben möchtest, indem du sie über mithilfe Checkboxen links markierst.
1. Wähle im Dropdown-Menü Stapelverarbeitung links unten die Option **Auto-Versand** aus. Klicke optional auf Auto-Versand (mit Kommissionierbez.). Auf diese Weise kannst du deinem Auftrag eine Bezeichnung zuweisen, die es bei der späteren Bearbeitung erleichtert, den Auftrag im Kommissionierlauf zu finden.
1. Klicke auf Ausführen.

> **Anmerkung**
>
> Falls du deinen Auftrag in der Versandübergabe nicht findest, wurde die Auftragsampel möglicherweise nicht aktualisiert. Klicke aufAuto-Versand berechnen, um den Status der Auftragsampel zu aktualisieren. Du kannst ebenso den Prozess **autoversand_berechnung** nutzen, um die Auftragsampel in festgelegten Zeitintervallen automatisch zu aktualisieren. Weitere Informationen zu diesem Prozess findest duhier.

## Auftragsübersicht für den Auto-Versand anpassen

Wenn mehrere Aufträge gleichzeitig an den Auto-Versand übergeben werden, kann schnell der Überblick verloren gehen. Daher bietet Xentral dir die Möglichkeit selbst zu bestimmen, welche Auftragsdaten angezeigt werden sollen.

Öffne zunächst das MenüVerkauf > Auftrag > Tab: Versandübergabe. Hier findest du alle Aufträge, die bereit für den Auto-Versand sind. Füge nun die folgenden Schritte aus, um die angezeigten Informationen in der Auftragsübersicht anzupassen:

1. Klicke oben rechts über der Tabelle auf **Spalten**.
1. Wähle im Dropdown-Menü die Informationen aus, die in der Auftragsübersicht angezeigt werden sollen. Setze dazu ein Häkchen links neben der jeweiligen Information.
1. Entferne die Häkchen links neben den Informationen, die du **nicht** in der Auftragsübersicht sehen möchtest.
1. Die gewünschten Informationen werden je nach deiner Auswahl sofort ein- oder ausgeblendet. Schließe das Dropdown-Menü, indem du erneut auf **Spalten** klickst.

> **Tipp**
>
> Welche Auftragsinformationen benötigst du im Tagesgeschäft mit Xentralhäufig? Möchtest du direkt sehen, ob eine bestimmte Artikelnummer in einem der Aufträge enthalten ist? Dann kannst du mithilfe der Anleitung oben dieses Feld in der Auftragsübersicht anzeigen lassen. Dies ermöglicht dir anschließend, Aufträge mit genau dieser Artikelnummer über die Stapelfunktion unterhalb der Tabelle auszuwählen und gesammelt an den Auto-Versand zu übergeben. Dieses Prinzip kannst du auf alle verfügbaren Spalten anwenden und somit bei der manuellen Übergabe in den Auto-Versand noch zielgerichteter nach Aufträgen filtern, um diese weiterzuverarbeiten.

## Den Auto-Versand automatisieren

Du kannst den Versandprozess mit dem Prozess **autoversand_plus** vollständig automatisieren. Somit werden alle Aufträge mit einer grünen Auftragsampel automatisch in fest definierten Zeitintervallen an den Auto-Versand übergeben. Die Aufträge werden in diesem Fall jedoch nicht mehr zusätzlich von Xentral geprüft. Daher empfehlen wir dir, den Prozess zu testen, bevor du ihn produktiv in deinem Tagesgeschäft anwendest.

1. Suche mithilfe der Smart Search nach **Prozesstarter**.
1. Öffne das Modul.
1. Klicke oben rechts auf **+NEU**.
1. Nimm die Einstellungen wie in der folgenden Abbildung gezeigt vor.
1. Klicke auf **Speichern**.

> **Wichtig**
>
> Wir empfehlen dir, in den Einstellungen des Prozesses **autoversand_plus ** stets die Art **Uhrzeit ** auszuwählen. Falls du die Art**Periodisch** verwendest, musste du darauf achten, dass die das Zeitintervall mindestens 31 Minuten lang ist. Bei kürzeren Zeitabständen wird der Prozess nicht ausgeführt. Weitere Informationen zu Prozessen und deren Einrichtung findest du im ArtikelAutomatisierung per Prozessstarter.