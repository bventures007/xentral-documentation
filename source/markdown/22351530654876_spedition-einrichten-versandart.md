Mit dem Modul **Spedition** kannst du für beliebige Speditionen Palettenbeschriftungen bzw. Speditionsscheine erstellen, ausdrucken und anschließend der Spedition melden bzw. als CSV-Datei übermitteln. Das Modul unterstützt NVEs, Mindesthaltbarkeitsdaten und Chargen und du kannst, wenn nötig, GS1 Barcodes erstellen.

## Enthaltene Funktionalitäten

- Du kannst manuell Speditionsaufträge anlegen.
- Du kannst ein individuelles Label für Packstücke mit Sendungs-/ NVE-Nummer und Freifeldern erstellen. Diese können mithilfe der Versandart **Spedition ** im Tab **Versandlabel** des Lieferscheins erstellt werden.
- Du kannst deine Packstücke auf einen Speditionsauftrag pro Spedition zusammenfassen. Die generierten Sendungs-/ NVE-Nummern und Freitext-Informationen sind darin enthalten.
- Du kannst deine Speditionsaufträge als CSV-Datei exportieren.
- Du kannst deine Speditionsaufträge als PDF-Datei exportieren und manuell per E-Mail an die Spedition übermitteln.

## Nicht enthaltene Funktionalitäten

- Du kannst nicht automatisch Speditionsaufträge aus “offenen Packstücken” erstellen.
- Du kannst keine Sendungs- /NVE-Nummern über eine API zu einer Spedition übertragen.
- Du kannst Services wie NextDay etc. nicht automatisch konfigurieren. Du musst deine Informationen über Freifelder angeben.
- Du kannst deine Sendung nicht über Echtzeit-Tracking verfolgen.
- Du kannst kein eigenes Schnittstellen-Exportformat je Spedition konfigurieren. Die Konfiguration ist nur über die vorgegebene CSV-Datei möglich. Viele Speditionen arbeiten jedoch nicht mit CSV, sondern XML, EDI und Webservices.
- Du kannst die CSV-Export-Datei des Speditionsauftrags nicht über das Modul Übertragungen übermitteln.

> **Anmerkung**
>
> **Typischer Anwendungsfall **: Du versendest gelegentlich Speditionsaufträge. Die Versandart ** Spedition**ist nicht geeignet, wenn du selbst Fulfillment-Dienstleister oder Großhändler mit vielen Speditionsaufträgen bist.

## Features

Die Versandart **Spedition** bietet dir folgende Features:

- Erstellung von Palettenbeschriftungen bzw. Speditionsscheinen
- Individuelle Anpassung von Versandlabels

## Versandart Spedition anlegen

Um den Versand per Spedition in Xentral einzurichten, erstellst zu im ersten Schritt die Versandart **Spedition**. Gehe dazu wie folgt vor.

1. Suche mithilfe der Smart Search nach **Versandarten**.
1. Klicke oben rechts auf **+NEU**.
1. Klicke auf **Spedition**.
1. Nimm die Einstellungen wie in der Tabelle unten beschrieben vor.
1. Klicke auf **Speichern**.

| Einstellung | Erläuterung |
| --- | --- |
| **Bezeichnung** | Hier findest du die Bezeichnung der Versandart, wie sie in Xentral beispielsweise bei der Auftragsbearbeitung angezeigt wird. Die Bezeichnung ist nur für dich und deine Mitarbeiter sichtbar. Achte darauf, dass jede Bezeichnung nur einmal in Xentral vorkommt, damit die Versandart stets eindeutig identifiziert werden kann. |
| **Typ **| Dies ist eine interne Feldbezeichnung, die für die Zuordnung bei deinen Online-Shops und anderen Verkaufsplattformen benötigt wird. ⚠️** Wichtig:** Verändere diese Bezeichnung nicht! |
| **Modul** | Wähle das passende Modul aus dem Dropdown-Menü. Dabei muss der Modulname identisch zum Namen der Versandart sein, die du gerade einrichtest. |
| **Projekt **|** Optional**: Gib eine Projektzuordnung an. Diese wird benötigt, wenn du die Versandart auf einen bestimmten Verkaufskanal oder ein Projekt (beispielsweise eine spezifische Niederlassung) beschränken möchtest. Lasse das Feld leer, falls die Versandart in allen Projekten genutzt werden soll. |
| **Aktiv **| Aktiviere diese Option, sobald du alle benötigten Einstellungen für die Versandart vorgenommen hast. 💬** Anmerkung:** Nicht mehr verwendete Versandarten kannst du später deaktivieren. Beachte jedoch, dass deaktivierte Versandarten nur noch in bereits erstellten Belegen angezeigt werden. In neu erstellten Belegen und in Benutzerflächen wie der Auftragsübersicht oder in den Kundendaten steht eine deaktivierte Versandart nicht mehr zur Auswahl zur Verfügung. Du kannst Versandarten auch löschen. Dadurch wird jedoch auch die Versandhistorie gelöscht. Deshalb solltest du nur fälschlicherweise angelegte Versandarten löschen, die du nicht produktiv genutzt hast. |
| **Kein Portocheck** | Mit dieser Option kannst du den Porto-Check im Auftrag deaktivieren. Bleibt der Porto-Check aktiv, zeigt die Auftragsampel ein rotes Symbol für den Portocheck an, falls nicht mindestens ein Portoartikel in den Auftragspositionen enthalten ist. So wird verhindert, dass bei manuell angelegten Aufträgen der Portoartikel vergessen wird. Überlege anhand deiner eigenen Workflows und Arbeitsweise mit Xentral, ob du diese Option aktivieren oder deaktivieren willst. Legst du typischerweise viele Aufträge manuell in Xentral an, kann es sinnvoll sein, diese Option nicht zu aktivieren, sodass gerade bei hochpreisigen Artikeln oder internationalen Sendungen das Porto immer zuverlässig am Auftrag hinterlegt wird. |
| **Drucker Versandlabel** | Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für die Versandlabels genutzt werden soll. Beachte, dass hier nur Drucker auswählbar sind, die du bereits [in Xentral eingerichtet](https://help.xentral.com/hc/de/articles/360016756299#UUID-24ed3a57-a4df-da7a-08f6-141949df3855) hast. Je nachdem, wie und wo der Versandprozess in deinem Unternehmen abläuft, kannst du hier genau den Drucker auswählen, den du benötigst - egal ob direkt am Schreibtisch oder am Packtisch im Lager. |
| **Drucker Export **|** Nur bei internationalem Versand relevant**: Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für Zollpapiere (CN23) genutzt werden soll. |
| **Versand-E-Mail **| Lege hier fest, nach welchen Regeln Versandbenachrichtigungen per E-Mail an deine Kunden verschickt werden sollen, sobald sich die Sendung auf dem Weg befindet. Die folgenden drei Optionen stehen dir zur Verfügung: ** Standardverhalten **: Die Logistikeinstellungen aus dem Projekt werden verwendet. Diese Einstellungen nimmst du im Menü ** Einstellungen > Grundeinstellungen > Projekte > Projekt öffnen > Tab: Einstellungen > Tab: Logistik / Versand **vor. In den Bereichen ** Stufe 1 (Pick/Kommissionierung)**und ** Stufe 2 (Pack)**definierst du über die Checkboxen namens ** E-Mail **, bei welchen Schritten deine Kunden über den Stand der Auftragsbearbeitung informiert werden. ** Keine Versandmail **: Für diese Versandart wird keine Versandinformation per E-Mail versendet ** Eigene Textvorlage **: Für diese Versandart wird die ausgewählte Textvorlage per E-Mail versendet. Diese Vorlage musst du vorab im Menü ** Einstellungen > Grundeinstellungen > Belege > Textvorlagen **erstellen. Anschließend wählst du die gewünschte Vorlage im Dropdown-Menü ** Textvorlage**aus. Durch diese Auswahl werden die Logistikeinstellungen des Projekts für diese Versandart nicht genutzt. |
| **Lieferungen unterstützt **| Diese Option wird bei der Anlage der Versandart standardmäßig aktiviert. Sobald du alle weiteren benötigten Einstellungen vorgenommen und die Versandart auf ** Aktiv** gestellt hast, kannst du die Versandart in Aufträgen, Lieferscheinen und im Versandzentrum auswählen. |
| **Retouren unterstützt** | Aktiviere diese Option, um zu erlauben, dass Retouren zu Aufträgen erstellt werden können, die ursprünglich mit der vorliegenden Versandart erstellt wurden. |
| **Bevorzugte Rücksendemethode** | Wähle eine bevorzugte Versandart für Retouren aus. Sobald in Xentral manuell eine Retoure zu einem Auftrag mit der vorliegenden Versandart angelegt ist, wird die hier gewählte Versandart automatisch im Retourenauftrag vorausgewählt. Diese Einstellung greift nur in Fällen der manuellen Retourenerstellung. |
| **Standard Gewicht **|** Optional**: Welches Gewicht haben die Sendungen typischerweise, die du mit dieser Versandart verschickst? Gib hier ein Standardgewicht in kg ein. Dieses Gewicht wird jedes Mal bei der Erstellung eines Versandlabels an den Versanddienstleister übermittelt, soweit es nicht vor dem Druck des Versandlabels manuell in Xentral geändert wird. |
| **Spedition** | |
| **Etikettenvorlage Master / Palette** | Wähle eine von dir zuvor erstellte Etikettenvorlage im XML-Format für die Palette aus. |
| **Etikettenvorlage Slave / Packstück** | Wähle eine von dir zuvor erstellte Etikettenvorlage im XML-Format für das Packstück aus. |

## Einstellungen im Speditions-Modul vornehmen

Du kannst das Modul **Spedition** in Xentralüber die Smart Search öffnen. Hier kannst du Packstücke für das Speditionsunternehmen erzeugen und die wesentlichen Charakteristika hinterlegen. Weitere Informationen findest im Artikel[Spedition](https://help.xentral.com/hc/de/articles/360016719700#UUID-1bddba5f-1b60-4ca0-f149-80849d012ba2).

### Allgemeine Einstellungen

Im Tab **Einstellungen ** des Moduls**Spedition** kannst du verschiedene Informationen pro Spedition definieren und eine Übersicht zu allen Speditionen sehen, zu denen du Spezialfelder angelegt hast.

![spedition-einstellungen-en.png](https://help.xentral.com/hc/article_attachments/22873731688860)

### Einstellungen zu NVE, Barcode, Lieferschein und Packstück

Im Tab **Einstellungen ** des Moduls**Spedition** kannst du zunächst Einstellungen zu NVE, Barcode, Lieferschein und Packstück vornehmen, die für den Druck des Versandlabels relevant sind. Dabei kannst du eine fortlaufende NVE vergeben, auf die durch eine Variable zugegriffen werden kann.

Die folgende Tabelle erläutert die Informationen, die du hinterlegen kannst.

| Einstellung | Erläuterung |
| --- | --- |
| **Nächste NVE** | Trage die eingetragene NVE fortlaufend ein. |
| **extra Barcode** | Aktiviere diese Option, um einen zusätzlichen Barcode zu erstellen und zu drucken. |
| **Inhalt extra Barcode **| Gib hier den Inhalt des zusätzlichen Barcodes ein, falls du die vorherige Option namens ** extra Barcode** aktiviert hast. |
| **URL für GS1 Barcode** | Gib hier die URL für den GS1 Barcode ein. |
| **URL für NVE Barcode** | Gib hier die URL für den NVE Barcode ein. |
| **Lieferschein erst nach Abschluss drucken** | Aktiviere diese Option, um den Lieferschein erst nach Abschluss des Speditionsauftrags zu drucken. |
| **Etikettenvorlage verwenden **| Aktiviere diese Option, wenn du eine Etikettenvorlage verwenden möchtest, die du zuvor in Xentral angelegt hast. 💡** Tipp:** Weitere Informationen zur Erstellung von Etikettenvorlagen findest du im Artikel Etikettenlayout für Artikel, Lager. |
| **Packstück** | Aktiviere diese Option, um einzustellen, dass es sich um ein einzelnes Packstück handelt. |
| **Vorlage Slave/Packstück **| Falls du die vorherige Option namens ** Etikettenvorlage verwenden** aktiviert hast, wähle hier die gewünschte Vorlage für das Packstück-Etikett aus. |

### Verfügbare Variablen für das Versandlabel

Um die Angaben für das Versandlabel weiter zu spezifizieren, kannst du auf verschiedene Variablen zurückgreifen.

Folgende Variablen stehen dir zur Verfügung:

- **{LIEFERSCHEIN}**

-**{TELEFONNUMMER}**

-**{PROJEKT}**

-**{AUFTRAG}**

-**{NVE}**

-**{MHD}**

-**{EAN}**

-**{HERSTELLERNUMMER}**

-**{ANZAHLPACKSTUECKE}**

-**{ARTIKELNAME}**

-**{NUMMER}**

-**{MENGE}**

-**{CHARGE}**

-**{PACKSTUECKNUMMER}**

### XML-Transportlabels/GS-1 Transportetiketten

Um Transportlabels von verschiedenen Speditionen zu spezifizieren, kannst du außerdem eigene XML-Etikettenlayouts erstellen, die als Etikettenvorlage verwendet werden können. Wie du ein GS-1 Transportetikett gestalten kannst und wie du Spezialfelder auf dem Etikett einblenden kannst, erfährst du im Artikel[Etikettenlayout für Artikel, Lager](https://help.xentral.com/hc/de/articles/360017573119#UUID-fe2f31f1-3109-8b78-4b73-57cb4e78138d).

## Versandlabel/Transportlabel in Xentral erstellen

Je nach Handelspartner und Produkten gibt es Anforderungen an das Transportlabel, die du im Modul **Spedition** in Xentral einstellen kannst. Wenn du in den Lieferscheinpositionen Artikel mit MHD- oder Chargenverwaltung verschicken möchtest, müssen diese Informationen ebenso auf dem Transportlabel abgebildet werden.

### Einstellungen für das Versandlabel vornehmen

Je nach Vorgaben des Spediteurs oder des Handelspartner kannst du in den Einstellungen der Versandart **Spedition** verschiedene Eingabefelder definieren, die beim Druck des Versandlabels mit zusätzlichen Informationen befüllt und auf das Transportlabel gedruckt werden können.

Beim Druck des Versandlabels wird folgende Abfrage angezeigt:

![Forwarding-6.png](https://help.xentral.com/hc/article_attachments/22351572077468)

Folgende Angaben kannst du eintragen, bevor du auf **Etikett erzeugen** klickst:

| Feldbezeichnung | Erläuterung |
| --- | --- |
| **Anzahl Packstücke** | Trage die Anzahl der Packstücke ein. |
| **Artikel / GTIN** | Gib die Artikelnummer/GTIN ein. |
| **MHD** | Gib das Mindesthaltbarkeitsdatum der Sendung ein. |
| **Menge** | Gib die Anzahl an Versandlabels ein, die ausgedruckt werden sollen. |

Das gedruckte Versandlabel (in diesem Fall mit Angabe des Mindesthaltbarkeitsdatums) kann beispielhaft so aussehen:

![Forwarding-7.png](https://help.xentral.com/hc/article_attachments/22351572085276)

> **Tipp**
>
> Das benötigte Etikettenlayout findest du im ArtikelEtikettenlayout für Artikel, Lager.