Mit dem Modul "Filiallieferung" kann über eine extra Oberfläche ein Auftrag auf eine Filialadresse mit einem Klick eingelagert werden. Dadurch muss man nicht manuell alle einzelnen Positionen der Filiallieferung erfassen und einlagern, was bei großen Lieferungen eine erhebliche Zeitersparnis bedeutet. Voraussetzung ist, dass sich im Auftrag eine Adresse befindet, die man zuvor mit einer Filiale verknüpft hat. Die Filiallieferung setzt sich aus folgenden Schritten zusammen:

- Filialen und Zentrale definieren
- Lagermindestmengen für Artikel auf Filialläger festlegen
- Alternativ zur Lagermindestmenge können auch direkt Aufträge angelegt werden
- Filialen von Zentrale aus beliefern und Lagermengen als Filialauftrag ohne Rechnungsstellung anlegen und über den Autoversand abwickeln

## Filiallieferung (Workflow)

Folgende Schritte sind für die Filiallieferung mit Lagermindestmengen einzustellen:

1. Adresse für die Filiale anlegen (im Beispiel: Filiale München)
1. Projekt für diese Filiale anlegen (im Beispiel: POSMUENCHEN → oder bestehendes Projekt verwenden); im Projekt die Filialadresse und das Projekt, auf das der Filialauftrag angelegt werden soll (im Beispiel: "ONLINESHOP")
1. Lager für die Filiale anlegen (im Beispiel: MUENCHEN_001 → das Lager auf das Projekt "POSMUENCHEN" buchen)
1. Lagerartikel anlegen und für diesen ein Mindestlager bestimmen (Lager & Logistik → Lagermindestmengen)
1. Im Modul "Lagermindestmengen" über "Aktion" eine Filiallieferung auslösen

Folgende Schritte sind für die Filiallieferung ohne Lagermindestmengen einzustellen:

1. Schritte 1-3 identisch zur Filiallieferung mit Lagermindestmengen. Es ist eine zusätzliche Einstellung in den Stammdaten der Filialadresse notwendig, damit bei den Belegen im Autoversand nur Lieferscheine erstellt werden und keine Rechnungen
1. Auftrag anlegen mit der Filial-Adresse und die Artikel welche an die Filiale/ Lager geliefert werden sollen, dem Auftrag zufügen
1. Auftrag an Versandzentrum übergeben zur Lieferung (bspw. per Autoversand)

## Filiallieferung mit Lagermindestmengen

### 1. Adresse für Filiale

Eine Adresse im Adressstamm für die Filiale anlegen: Stammdaten → Adresse → +NEU.

Eine neue Adresse für die Filiale anlegen. Hier wird eine Kundennummer vergeben. Für diese Kundennummer wird bei der Filiallieferung ein Auftrag angelegt (die Lieferung erfolgt an die Filialadresse).

Im Beispiel ist die Adresse eine Filiale in München "POS München", die von Augsburg (Zentrale) aus beliefert werden soll.

### 2. Projekt für Filiale

Für diese Filiale "POS München" ein Projekt anlegen unter "Stammdaten → Projekte → NEU". Das Projekt wird im Beispiel "POSMUENCHEN" bezeichnet. Dieses Projekt hat einen Ladenverkauf, es kann aber auch einfach eine andere Filiale mit einem Büro oder einem eigenen Logistikprozess sein.

Sofern es bereits ein Projekt für diese Filiale gibt, kann das bereits bestehende Projekt verwendet werden (gilt auch für das Lager im nächsten Punkt).

In diesem neuen Projekt wird im Tab "Filiale" folgendes eingetragen:

- Adresse aus Stammdaten → Die Filialadresse muss die Rolle Kunde haben (s.o.) (Filialadresse für die Filiale, die zu diesem Projekt gehört: in diesem Beispiel ist das für das Projekt "POSMUENCHEN" auch die oben angelegte Adresse "Pos München" mit der Kundennummer "10011"
- Projekt für Lieferung der Zentrale an Filiale → Lieferungen werden über dieses Projekt versendet (Der Auftrag für die Lieferung an die Filiale wird auf dieses Projekt gebucht. Idealerweise sollte hier das Projekt verwendet werden, das einen Logistikprozess eingestellt hat, über den die Zentrale versenden kann. Alternativ kann auch ein neues Projekt angelegt werden, das auf alle Läger in der Zentrale Zugriff hat) → im Beispiel wird das Projekt "ONLINESHOP" verwendet. Dieses Projekt ist das Projekt für die Zentrale in Augsburg.

### 3. Lager für Filiale

Für die Filiale in München wird ein neues Lager angelegt: Lager "München", Regal: "MUENCHEN_001". Diesem Lager wird das Projekt "POSMUENCHEN" zugeordnet und wird somit zu einem Projektlager. In dieses Lager wird die Filiallieferung später von der Zentrale aus eingebucht.

Lager: Muenchen → Projekt "MUENCHENPOS" vergeben

![filiallieferung_3.png](https://help.xentral.com/hc/article_attachments/5080760502812)

Regal: MUENCHEN_001

![filiallieferung_4.png](https://help.xentral.com/hc/article_attachments/5080760523164)

### 4. Artikel Mindestlagermenge für Filiallager

Für einen Artikel (Lagerartikel) wird nun ein Mindestbestand für das Filiallager "MUENCHEN_001" vergeben:

Lager → Lagermindestmengen → Mindestmengen pro Artikel

Artikel, Lagerplatz und Menge eingeben und speichern

Im Beispiel soll der Artikel "Tasse Xentral" mit der Artikelnummer "1000005" die Mindestmenge "20" für das Lager "MUENCHEN_001" erhalten.

Beispiel für eingetragene Mengen bei den "Mindestmengen":

![filiallieferung_6.png](https://help.xentral.com/hc/article_attachments/5080822984860)

### 5. Filialbestellung auslösen

Um eine Filialbestellung von Augsburg nach München auszulösen, wird im nächsten Tab "Aktionen" die Filiale ausgewählt:

Manuelle Umlagerliste um Mindestmengen auffüllen zu können (PDF)

Lieferung für Projekt / Filiale / Außenlager anlegen

Im Anschluss die zu beliefernde Filiale aus der Liste auswählen.

Im nächsten Schritt werden die fehlenden Artikel aufgelistet, um die Mindestmenge in der Filiale aufzufüllen. Im Beispiel ist die "Tasse Xentral" im Augsburger Lager 300-mal vorrätig und es sollen von dort aus 20 Stück nach München geliefert werden. Hier kann die Menge nochmals verändert werden. Über "Auftrag erstellen" wird auf das im Projekt "POSMUENCHEN" hinterlegte Projekt für die Zentrale der Auftrag erstellt. Im Beispiel ist das der "ONLINESHOP" der Zentrale in Augsburg.

Angelegt wird der Auftrag auf die Münchner Adresse "Pos München" und auf die Kundennummer der Filiale. Den Auftrag kann man nun freigeben und im Anschluss kann dieser ganz normal in die Logistik übergeben werden.

Der Auftrag für die Filiallieferung wird im Standard immer ohne Rechnungserstellung voreingestellt. Somit erfolgt bei der Lieferung keine Rechnungsstellung über den Logistikprozess. Es wird lediglich ein Lieferschein erstellt:

Die Nummernvergabe für die Auftragsnummer erfolgt aus dem Nummernkreis des im Filialprojekt angegebenen Projekt der Zentrale in Augsburg im Projekt "ONLINESHOP" ganz normal wie bei der manuellen Anlage eines Auftrages auf das Projekt "ONLINESHOP".

Gekennzeichnet werden Filialaufträge über ein (F) in der Auftragsübersicht. Nach dem "(F)" kann ebenso in der Suche gesucht werden.

Im Modul Filiallieferung unter "offene Lieferungen" können Sie den angelieferten Artikel dann im Filiallager einlagern.

## Filiallieferung ohne Lagermindestmengen

### 1. Adresse für die Filiale anlegen

Nachdem Sie die Adresse für die Filiale wie zuvor beschrieben angelegt haben, ist dort noch eine zusätzliche Einstellung notwendig, damit bei der Weiterverarbeitung im Autoversand automatisch nur der Lieferschein erstellt und keine Rechnung erzeugt wird. Gehen Sie hierzu in den Stammdaten der Filialadresse unter den Reiter "Zahlungskonditionen/ Besteuerung" und stellen dort bei Belege im Auto-Versand erstellen auf "nur Lieferschein erstellen"

### 2. Manuell Auftrag für das Filiallager anlegen

Wenn Sie nicht mit Mindestbeständen für Artikel (Lagerartikel) arbeiten möchten, können Sie auch direkt einen Auftrag anlegen. Sie wählen dazu Ihre Filialadresse aus und ergänzen Ihre Artikel die Sie an die Filiale liefern möchten. Durch die Auswahl der Filialadresse wird der Auftrag auch entsprechend mit (F) für Filiallieferung in der Auftragsübersicht gekennzeichnet.

### 3. Auftrag an Versandzentrum übergeben

Der Auftrag auf die Münchner Adresse "Pos München", Kundennummer "10011" kann im Anschluss ganz normal in die Logistik übergeben werden.

## Modul Filiallieferung

Nachdem der Filialauftrag über die Logistik abgewickelt wurde, wird dieser in der Liste aller offenen Filiallieferungen angezeigt: Im Modul Filiallieferung werden die Lieferinhalte pro Filiale und Lieferung in einer Übersicht angezeigt. Über das Edit-Icon gelangen Sie in die Inhalte der Lieferung und können dort die Regale der Filiale zum Einlagern der Ware auswählen.

### Filiallieferung offene

Administration → Appstore → Filiallieferung. Hier sind die versendeten Filialaufträge sichtbar.

![filiallieferung_15.png](https://help.xentral.com/hc/article_attachments/5080838371612)

![filiallieferung_16.png](https://help.xentral.com/hc/article_attachments/5080792890268)

### Wareneingang für Filiallieferung

Mit dem Stift-Icon kann die Menge in das Filiallager eingebucht werden. Die Buchung in die Filiale "POSMUENCHEN" erfolgt von der Zentrale aus (aus Augsburg):

Der Artikel "Tasse Xentral" ist nun 280-mal im Lager Augsburg und 20-mal im Lager München lagernd.

## Filiallieferung Benutzerrechte

Bitte beachten Sie, dass für die Filiallieferung folgende Modulrechte zu "Filiallieferung" mit berührt und ggf. benötigt werden:

- Artikel
- Auftrag
- Bestellvorschlag Filiale
- Adresse
- Lager
- Lieferschein

### Bestand aus Hauptlager berücksichtigen

Beim Erstellen des Auftrags für die Fililallieferung kann mit der Option der Bestand im Quellager auf die umzulagernde Mindestmenge geprüft werden.

Im Anschluss wird nach Auswahl der Filiale eine Gegenüberstellung des verfügbaren Bestands des Hauptlagers mit der Mindestlagermenge des Artikels bei der Filiale vorgenommen.