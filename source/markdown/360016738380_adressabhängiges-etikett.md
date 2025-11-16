> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Mit dem Modul **Adressabhängiges Etikett** können Sie für bestimmte Adressen ein persönliches Etikett erstellen, dass als Lieferschein-Positionen Etikett verwendet werden soll. Dieses Etikett kann entweder im Autoversand oder direkt über das Aktionsmenü des Lieferscheins erstellt werden.

## Übersicht

In der Übersicht sehen Sie alle bereits angelegten Adressetiketten.

## Adressetiketten anlegen

Mit dem **+NEU** Button können Sie weitere Adressetiketten hinzufügen.

Folgende Informationen werden dafür benötigt:

- **Adresse**: Der Kunde, für den das Etikett gelten soll
- **Etikett**: Die Auswahl des entsprechenden Etiketts
- **Verwenden als **: Hier können Sie ** Lieferschein Position **wählen. Weitere Optionen sind zum Beispiel: ** Artikel klein **, ** Seriennummer ** oder **Multiorder Picking Artike** l

## Adressetiketten drucken

Es gibt zwei Möglichkeiten die Adressetiketten zu drucken:

- im Autoversand
- im Lieferschein

### Druck im Autoversand

Dafür muss unter **Projekt > Einstellungen > Logistik / Versand ** ein Haken bei der Option **Lieferscheinposition: Etiketten ** im Bereich**Versandprozess und Komissionierung** gesetzt sein.

Sobald ein Auftrag über den Autoversand läuft, werden die Etiketten erstellt und die entsprechenden Adressetiketten gedruckt, sollte die Adresse mit der Auftrags-Adresse übereinstimmen.

### Direkt über den Lieferschein

Im jeweiligen Lieferschein unter **Lager > Lieferschein ** können Sie im **Aktion ** s-Menü die Option**Positionen als Etiketten** aus dem Dropdown-Menü wählen.

## Beispiel-Struktur für Etiketten

### Lieferscheinpositionen

Etikettenlayout erstellen

```
<span class="hljs-tag"><span class="hljs-name">label</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">barcode</span> <span class="hljs-attr">y</span>=<span class="hljs-string"> "1"</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr"> size</span>=<span class="hljs-string"> "6"</span> <span class="hljs-attr">type</span>=<span class="hljs-string"> "2"</span>></span>{NUMBER}<span class="hljs-tag"></<span class="hljs-name">barcode</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr"> y</span>=<span class="hljs-string"> "8"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>>/lt;/span>Item no. {NUMBER}<span class="hljs-tag"></<span class="hljs-name">line</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr"> y</span>=<span class="hljs-string"> "11"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>>{NAME_DE} <span class="hljs-tag"></<span class="hljs-name">line</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr"> y</span>=<span class="hljs-string"> "14"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>LS: {BELEGNR} Quantity: {QUANTITY} {STORAGE_PLACE_NAME}<span class="hljs-tag"></<span class="hljs-name">line</span>></span>
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

```

- **{NUMMER}**: Artikelnummer
- **{NAME_DE}**: Artikelname
- **{BELEGNR}**: Nummer des Lieferscheins
- **{MENGE}**: Menge dieser Position
- **{LAGER_PLATZ_NAME}**: Regal-Name, auf dem am meisten eingelagert ist. Wenn es keinen Bestand gibt, bleibt die Variable leer (das ist nicht das Standardlager des Artikels)