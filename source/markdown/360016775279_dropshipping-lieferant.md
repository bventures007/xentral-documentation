Das Modul **Dropshipping Lieferant** ermöglicht die direkte Übergabe von Kundenaufträgen an externe Lieferanten, die den Versand im eigenen Namen übernehmen. Die Bestellungen werden an einen oder mehrere Dropshipping-Partner übermittelt, wodurch Lagerhaltung und Versandprozesse im eigenen Unternehmen entfallen.

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in das Modul Dropshipping Lieferant**
>
> Möchtest du dir innerhalb weniger Minuten einen Überblick über die Funktionen und die Nutzung des Moduls **Dropshipping Lieferant** in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/CIM6thS9ezQ)**

## Was ist Dropshipping?

Beim Dropshipping verkaufst du Produkte, ohne sie selbst auf Lager zu haben. Sobald ein Kunde in deinem Shop bestellt, gibst du die Bestellung direkt an deinen Lieferanten weiter. Der versendet die Ware in deinem Namen direkt an den Kunden – du musst dich also weder um Lagerung noch um den Versand kümmern.

> **Anmerkung**
>
> **Hinweis**
>
> **Beispiel**: Du betreibst einen Onlineshop für Fitnesszubehör, unter anderem hochwertige Edelstahl-Trinkflaschen. Sobald ein Kunde über deinen Shop bestellt, leitest du die Bestellung an deinen Trinkflaschen-Großhändler weiter. Dieser übernimmt den Versand und schickt die Trinkflasche direkt aus seinem Lager an den Endkunden. Für den Käufer wirkt es so, als käme das Produkt direkt von dir, obwohl du weder Lagerfläche noch eigene Logistik benötigst.

## Wie funktioniert Dropshipping in Xentral?

Mit dem Modul **Dropshipping Lieferant** kannst du ganz einfach steuern, welche Artikel direkt vom Lieferanten an den Kunden gehen sollen. Dafür hinterlegst du im Artikel, dass es sich um einen Dropshipping-Artikel handelt – und welcher Lieferant ihn versendet.

Sobald ein Kunde diesen Artikel bestellt, erkennt Xentral dies automatisch und erstellt eine **Lieferantenbestellung** mit allen nötigen Infos, z. B. dem Lieferschein. Der Lieferant verschickt den Artikel dann direkt an deinen Kunden.

Optional kann der Lieferant dir Rückmeldungen wie **Trackingdaten** oder den Lieferstatus schicken – entweder manuell oder automatisch über das[Übertragungen-Modul](https://help.xentral.com/hc/de/articles/360016738020#UUID-b5241f40-f7c5-2595-dcc9-6824f63e6930).

![DropshippingLieferant_Workflow.png](https://help.xentral.com/hc/article_attachments/20225556740380)

## Was passiert, wenn der Auftrag gemischt ist?

Kein Problem: Enthält ein Auftrag Artikel von verschiedenen Lieferanten oder teilweise aus deinem eigenen Lager, dann teilt Xentral den Auftrag automatisch auf. So bekommt jeder Versender genau seinen Teil – und deine Kunden alles pünktlich geliefert.

> **Anmerkung**
>
> Nicht enthaltene Funktionalitäten:
>
> - Porto-Kosten aufteilen: Du kannst die Porto-Kosten (Artikel/ Auftragsposition) nicht automatisch oder anteilig aufsplitten.
> - Unterschiedliche Versandarten: Es ist nicht möglich, unterschiedliche Versandarten (je Artikel/Lieferant) automatisch abzubilden.
> - Lieferantendaten importieren: Mit diesem Modul kannst du keine Lieferantendaten (Artikel, Preise, Bestände) importieren. Nutze für den Import von Artikelkatalogen die Import-/ Exportzentrale.
> - Kein Rückkanal vom Lieferanten: Es wird kein Status vom Dropshipping-Lieferanten zurück an Xentralübermittelt. Um Trackings zu empfangen, kannst du das Übertragungen-Modul nutzen.

## Vorbereitende Maßnahmen

### Schritt 1: Dropshipping-Gruppe anlegen

Im ersten Schritt legst du eine Dropshipping-Gruppe an. Hier nimmst du die Grundeinstellungen für einen Dropshipping Lieferanten vor. Später kannst du dieser Gruppe alle passenden Artikel zuordnen, die von diesem Lieferanten in der festgelegten Art und Weise versendet werden sollen.

1. Nutze die Smart Search, um das Modul **Dropshipping Lieferant** zu öffnen.
1. Öffne das Tab **Gruppen**.
1. Klicke rechts auf **+ Neuen Eintrag anlegen**.
1. Vergib eine eindeutige **Bezeichnung** für diese Gruppe, zum Beispiel "Dropshipping-Lieferant Müller".
1. Wähle den **Lieferant ** aus, indem du auf das **Lupe-Symbol** klickst. Für diesen Lieferanten werden dann später die Bestellungen angelegt.
1. Nutze die Einstellung Ziel Projekt (Optional), um für diesen Lieferanten ein eigenes Projekt zu verwenden. So kannst du später in der Auftragsübersicht einfacher nach Lieferanten filtern – besonders praktisch bei vielen Lieferanten. Das Projekt kannst du im Modul **Projekt > + Neu anlegen** erstellen.

Wenn du die Grundeinstellungen vorgenommen hast, kannst du die spezifischen Einstellungen für Auftrag, Bestellung und Aktionen dieser Gruppe vornehmen. Diese Einstellungen gehen wir in den folgenden Kapiteln detailliert durch.

### Schritt 2: Einstellungen für den Dropshipping-Auftrag vornehmen

Im Bereich **Auftrags-Einstellungen** kannst du die Einstellungen für den Dropshipping-Auftrag festlegen, zum Beispiel, welche Belege benötigt werden und ob diese automatisch oder manuell erstellt werden sollen.

| Einstellung | Erläuterung |
| --- | --- |
| **Nur falls Zahlung ok** | Wenn du diese Option aktivierst, wird ein Dropshipping Auftrag nur erstellt, wenn die Zahlungs-Ampel im Originalauftrag auf grün (= Zahlung freigegeben) steht. |
| **Lieferdatum aus Artikel berechnen** | Die Funktion dieses Feldes wird überarbeitet und steht aktuell leider nicht zur Verfügung. |
| **Auto-Versand **| Gib hier an, wie der Auto-Versand für den Dropshipping-Teilauftrag durchgeführt werden soll. Die folgenden Optionen stehen zur Verfügung: -** Auto-Versandfreigabe deaktivieren **: Der Auto Versand muss manuell ausgeführt werden.<br>-** Auto-Versand durchführen **: Führt den Autoversand für den Dropshipping-Auftrag durch, wenn alle Auftragsampeln auf grün stehen.<br>-** Auto-Versandfreigabe unverändert lassen **: Die Autoversandeinstellungen des jeweiligen Projekts werden beibehalten. 🚨** Warnung:** Wenn unten im Bereich Bestellung die Optionen Als Anhang Lieferschein und Als Anhang Rechnung gesetzt ist, wird dieses Feld übersteuert und der Autoversand ausgeführt. Wenn du die Option Einstellung aus Kundenadresse verwenden aktivierst, dann wird die Einstellung aus den Kundenstammdaten übernommen, die im Tab Zahlungskonditionen / Besteuerung im Feld Belege im Auto-Versand erstellen hinterlegt ist. |

### Schritt 3: Einstellungen für den Versand der Bestellung vornehmen

Im BereichBestellunglegst du fest, ob eine Bestellung automatisch an den Dropshipping-Lieferanten geschickt werden soll. Außerdem kannst du auswählen, welche Anhänge – wie Lieferschein, Rechnung oder Auftragsbestätigung – mitgeschickt werden sollen und ob die Kundenadresse übernommen werden soll.

| Einstellung | Erläuterung |
| --- | --- |
| **automatisch anlegen** | Es wird automatisch eine Bestellung für den Lieferanten angelegt. Voraussetzung ist, dass für den/die Dropshipping-Artikel ein Einkaufspreis hinterlegt ist. |
| **abweichende Lieferadresse** | Die Kundenadresse aus dem Hauptauftrag wird in der Bestellung als Abweichende Lieferadresse übernommen. So kann man direkt in der Bestellung sehen, an welchen Kunden der Lieferant den/die Artikel senden muss. |
| **Als Anhang Lieferschein** | Der Lieferschein für den Kunden wird als PDF-Datei in der Bestellung unter Dateien angehängt und kann direkt mit versendet werden. |
| **Inkl. Lieferschein als CSV** | Der Lieferschein für den Kunden wird als CSV-Datei in der Bestellung unter Dateien angehängt und kann direkt mit versendet werden. |
| **als Anhang Rechnung** | Die Rechnung für den Kunden wird als PDF-Datei in der Bestellung unter Dateien angehängt und kann direkt mit versendet werden. |
| **als Anhang Auftrag** | Die Auftragsbestätigung für den Kunden wird als PDF-Datei in der Bestellung unter Dateien angehängt und kann direkt mit versendet werden. |
| **inkl. Auftrag als CSV** | Die Auftragsbestätigung für den Kunden wird als CSV-Datei in der Bestellung unter Dateien angehängt und kann direkt mit versendet werden. |
| **Bestellung abschließen** | Wenn du diese Option aktivierst, wird die Bestellung automatisch auf den Status abgeschlossen gesetzt. |

### Schritt 4: Aktionseinstellungen der Dropshipping-Gruppe vornehmen

Im BereichAktionenstellst du ein, welche Belege automatisch per E-Mail an den Lieferanten versendet werden. Außerdem kannst du festlegen, welche Belege automatisch in welchem Drucker gedruckt werden sollen. Dies kann nützlich sein, um den Prozess der Bestellabwicklung zu beschleunigen, indem ohne manuellen Email-Versand oder Druckbefehl die Belege direkt versendet bzw. ausgedruckt werden.

| Einstellung | Funktion |
| --- | --- |
| **Bestellung E-Mail an Lieferant** | Aktiviere diese Option, wenn die Bestellung automatisch an deinen Dropshipping-Lieferant versendet werden soll. |
| **Bestellung direkt drucken** | Falls die Bestellung direkt gedruckt werden soll, kann hier ein Dokumentendrucker aus dem Dropdown-Menü ausgewählt werden. |
| **Lieferschein-E-Mail an Lieferant** | Aktiviere diese Option, wenn der Lieferschein automatisch an deinen Dropshipping-Lieferant versendet werden soll. |
| **Lieferschein direkt drucken** | Falls der Lieferschein direkt gedruckt werden soll, kann hier ein Dokumentendrucker aus dem Dropdown-Menü ausgewählt werden. |
| **Rechnung E-Mail an Kunden** | Aktiviere diese Option, wenn die Rechnung automatisch an deinen Dropshipping-Lieferant versendet werden soll. |
| **Rechnung direkt drucken** | Falls die Rechnung direkt gedruckt werden soll, kann hier ein Dokumentendrucker aus dem Dropdown-Menü ausgewählt werden. |
| **Rückmeldung an Shop** | Wenn der Dropshipping-Auftrag aus dem Onlineshop nach Xentral übertragen wurde und du diese Option aktivierst, wird der Bestellstatus im Shop automatisch auf „versendet“ gesetzt. |

## Artikel zur Gruppe hinzufügen

Sobald du die Grundeinstellungen für die Artikelgruppe erledigt hast, kannst du Artikel zu dieser Gruppe hinzufügen.

Dafür gibt es verschiedene Möglichkeiten:

- Artikel manuell eintragen
- Eine Artikelliste hochladen
- Den Assistenten verwenden

### Artikel manuell eintragen

Gehe wie folgt vor, um Artikel manuell zur Dropshipping-Gruppe hinzuzufügen.

1. Navigiere im Modul **Dropshipping Lieferant ** zum Tab **Artikel**.
1. Klicke rechts auf **+ Neuer Eintrag**.
1. Wähle die Dropshipping-Gruppe aus, der du den Artikel zuordnen möchtest, indem du auf das **Lupe-Symbol ** im Feld **Gruppe** klickst. Dir werden alle bereits erstellten Gruppen angezeigt.
1. Wähle den Artikel aus, den du der Gruppe hinzufügen möchtest, indem du auf das **Lupe-Symbol ** im Feld **Artikel** klickst.
1. Klicke auf **Speichern**.

### Artikelliste hochladen

Gehe wie folgt vor, um eine Liste von Artikeln hochzuladen, die der Dropshipping-Gruppe hinzugefügt werden sollen.

1. Navigiere im Modul **Dropshipping Lieferant ** zum Tab **Gruppen**.
1. Klicke auf das **Pfeil-Symbol** neben der gewünschten Gruppe.
1. Die CSV-Datei muss folgendes Format haben:
  1. Die erste Zeile wird als Überschrift identifiziert (z.B. Artikelnummer)
  1. Der einzige benötigte Inhalt sind die Artikelnummern in Spalte A
1. Klicke auf **Hochladen**. Xentral zeigt dir in einer Vorschau an, welche Artikelnummern im nächsten Schritt der Gruppe hinzugefügt werden.
1. Passt alles? Dann klicke auf **Importieren **. Falls du Fehler entdeckst, klicke auf ** Abbrechen**. Korrigiere deine CSV-Datei und wiederhole die Schritte.
1. Nachdem du auf Importieren geklickt hast, bestätigt Xentral dir, wieviele Artikel importiert wurden. Du kannst auch unter Dropshipping Lieferant > Artikel überprüfen, ob alle Artikel korrekt deiner Gruppe zugeordnet wurden.

### Den Assistenten verwenden

Alternativ hast du die Möglichkeit, einer Gruppe alle Artikel eines bestimmten Herstellers hinzuzufügen. Dafür musst du zwei Dinge vorbereiten:

- In den Artikelstammdaten muss das Feld Hersteller ausgefüllt sein.
- Im Modul Dropshipping Lieferant muss eine Gruppe angelegt sein, die genau so heißt wie der Eintrag im Feld Hersteller im Artikel.

Navigiere zuDropshipping Lieferant > Artikelund klicke rechts auf die SchaltflächeAssistent. Wenn du mitSpeichernbestätigst, dann verknüpftXentral alle Artikel mit einer Gruppe, deren Inhalt im FeldHerstellermit einem Dropshipping-Gruppennnamen übereinstimmen.

> **Tipp**
>
> **Artikelzuordnung aufheben**
>
> Falsch verknüpft? Deine Artikelzuordnung zu einer Gruppe hat sich geändert? Kein Problem. Klicke aufAlle Einträge löschenunterDropshipping Lieferant > Artikel, um alle Verknüpfungen aufzuheben. Möchtest du nur eine einzelne Artikelverknüpfung entfernen, so kannst du hier auf dasX-Symbolin der Übersicht klicken. Keine Sorge, dein Artikelstamm bleibt erhalten. Es wird hierdurch nur die Verknüpfung zum Dropshipping-Modul gelöscht.

## Auftragsabwicklung für Dropshipping-Aufträge

Wenn das ModulDropshipping Lieferantfertig eingerichtet ist, gibt es zwei Möglichkeiten, wie die Auftragsabwicklung abläuft:

- Auftrag aus dem Onlineshop importieren
- Auftrag manuell anlegen

### Funktionalität beim Import aus dem Onlineshop

- Xentral erkennt automatisch Dropshipping-Artikel im Auftrag und legt für jede Dropshipping-Gruppe einen eigenen Teilauftrag an.
- Optional wird eine Bestellung an den Lieferanten als Entwurf erzeugt (je nach Einstellung).
- Es wird eine Rechnung pro Teilauftrag erstellt und verknüpft.

### Funktionalität beim manuellen Anlegen

Wenn du einen neuen Auftrag anlegst, der Dropshipping-Artikel enthält, erscheint nach Freigabe des Auftrags die SchaltflächeDropshipping-Auftrag anlegen. Mit einem Klick wird der Auftrag automatisch in Teilaufträge aufgeteilt.

### Achtung

Der Artikel darf keinen Lagerbestand haben - andernfalls wird kein Dropshipping-Auftrag erstellt.

## Besonderheiten bei Dropshipping-Aufträgen

Beachte folgende Besonderheiten bei Dropshipping-Aufträgen:

> **Anmerkung**
>
> - **Porto-Artikel: ** Ist ein Porto-Artikel zusammen mit einem Dropshipping-Artikel im Auftrag, wird der Auftrag ** nicht aufgesplittet **. Stattdessen wird der Hauptauftrag zu einem Dropshipping-Auftrag, und das Projekt des Belegs wird auf das ** Projekt**der Dropshipping-Gruppeneinstellungen geändert. So werden keine Aufträge angezeigt, die nur Porto-Artikel enthalten – die Auftragsübersicht bleibt übersichtlich.
> - **Verschiedene Dropshipping-Projekte in einem Auftrag: ** Enthält ein Auftrag Dropshipping-Artikel aus verschiedenen Projekten, wird für ** jedes Projekt ein eigener Teilauftrag** erstellt.
> - **Bestand bei Dropshipping-Artikeln: ** Ist der Dropshipping-Artikel vollständig im eigenen Lager verfügbar, wird ** kein Dropshipping-Auftrag** erzeugt.
> - **Internetnummer:** Eine vorhandeneInternetnummer(Bestellnummer aus dem jeweiligen Onlineshop) wird auch in die aufgesplitteten Dropshipping-Teilaufträge übernommen.
> - **Sendungsverfolgung:** Die Trackingnummmern können über das Übertragen-Modul importiert werden. Ein Praxisbeispiel findest duhier.