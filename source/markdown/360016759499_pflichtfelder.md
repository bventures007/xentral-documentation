Im Modul **Pflichtfelder** kannst du systemweite Pflichtfelder für einzelne Module und Oberflächen festlegen, sodass diese Pflichtfelde beim Speichern von Oberflächen und Inhalten ausgefüllt werden müssen. Diese Felder werden dann mit einer individuellen Beschriftung markiert und dem Bearbeiter angezeigt.

Besonders relevant ist dieses Modul, wenn bestimmte Felder immer auszufüllen sind bzw. nicht vergessen werden dürfen.

> **Anmerkung**
>
> Aus technischen Gründen kann die Prüfung von Feldern in einigen Fällen nicht vorgenommen werden. Dazu gehören beispielsweise Spezialfelder in Systemmeldungen oder Felder in Dialogfenstern (so genannte Overlays).

## Neue Pflichtfelder erstellen

Ein neues Pflichtfeld erstellst du, indem du das Menü **Pflichtfelder ** öffnest und auf**+NEU** klickst.

Es öffnet sich ein Dialogfenster. Fülle die angezeigten Felder aus und klicke anschließend auf **Speichern**.

### Feldeinstellungen

In den Feldeinstellungen kann das Pflichtfeld definiert werden:

- Modul: Modulname (in das Modul klicken und oben in der URL ablesen z.B: in einen Artikel klicken: "..module=artikel&amp;action=edit&amp;id=1")
- Action: Seite des Moduls (in das Modul klicken, dann auf die Seite für das Pflichtfeld klicken und oben in der URL ablesen z.B: in einen Artikel klicken: "..module=artikel&amp;action=edit&amp;id=1")
- Feld-ID: Feldbezeichnung des einzelnen Feldes (in das Feld klicken, rechte Maustaste, "Element untersuchen", id="kurztext_de" wäre z.B. im Artikel der Kurztext → genaue Beschreibung s.u.)
- Typ: Auswahl des Inhalt Typs: z.B. Text, Ganzzahl, Dezimalzahl, etc.
- Mindestlänge: Mindestanzahl an Zeichen muss festgelegt werden (Info: dann diese Info idealerweise für die bearbeitende Person in den "Fehlermeldung" Text eingeben)
- Maximallänge: Maximalanzahl an Zeichen muss festgelegt werden (Info: dann diese Info idealerweise für die bearbeitende Person in den "Fehlermeldung" Text eingeben)
- Fehlermeldung: Text für die Fehlermeldung z.B. "Pflichtfeld", wird dann rot angezeigt sobald die bearbeitende Person speichert
- Pflichtfeld: aktiv setzen. Markiert diesen Eintrag in der Oberfläche als Pflichtfeld

## Pflichtfelder in der Oberfläche

Das Pflichtfeld in der Oberfläche wird angezeigt, sobald die Seite vom Benutzer gespeichert wird.

## Beispiel für Pflichtfelder

In einem Artikel soll der Kurztext als Pflichtfeld angelegt werden. Das Ergebnis soll folgendermaßen aussehen:

![mandatoryfields_1190.png](https://help.xentral.com/hc/article_attachments/5078085686940)

Folgende Schritte sind hierbei durchzuführen:

1. Pflichtfeld anlegen
1. Modul, Action, Feld-ID finden
1. Restliche Daten eintragen und speichern
1. In der Oberfläche testen

### 1. Pflichtfeld anlegen

In dem Modul Pflichtfelder ist auf den Button+NEUzu klicken, damit sich ein Dialogfeld öffnet, über das dann ein neues Pflichtfeld angelegt werden kann.

### 2. Modul, Action, Feld-ID finden

Im nächsten Schritt sind die FelderModul,ActionundFeld-IDauszufüllen.

- Modul: Das Modul kann über die URL gefunden werden. In einen Artikel klicken und oben die URL ablesen: Stammdaten>Artikel > in einen Artikel klicken

![mandatoryfields_5.png](https://help.xentral.com/hc/article_attachments/5078187020444)

- Action: Die Seite kann über die URL gefunden werden. In einen Artikel klicken und oben die URL ablesen: ©Stammdaten > Artikel > in einen Artikel klicken (auf dieser Seite soll das Pflichtfeld sein, ist dieselbe Seite wie "1. Modul")

![mandatoryfields_6.png](https://help.xentral.com/hc/article_attachments/5078085745308)

- Feld-ID: Mit der rechten Maustaste in das gewünschte Feld klicken (das ein Pflichtfeld werden soll, in diesem Fall im Artikel das Feld "Kurztext"). AnschließendElement untersuchenanklicken.

Die ID kann abgelesen werden kurztext_de:

![mandatoryfields_1193.png](https://help.xentral.com/hc/article_attachments/5078101929244)

### 3. Restliche Daten eintragen:

Anschließend müssen die restlichen Daten eingetragen werden.

### 4. In der Oberfläche testen

Einen bestehenden Artikel anklicken und nochmals speichern. Das Pflichtfeld wird dann markiert.