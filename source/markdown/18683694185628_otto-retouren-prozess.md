## Allgemeines

Eine Besonderheit gegenüber anderen Shops und Marktplätzen ist der Retouren-Prozess bei OTTO. Generell hast du folgende Möglichkeiten:

![OTTO_Retourenprozess_Chart.png](https://help.xentral.com/hc/article_attachments/18684072473500)

Wie bei allen Shop- und Marktplatz-Anbindungen benötigst du eine oder mehrere Versandarten in Xentral. Je nach Szenario sind für die OTTO-Schnittstelle verschiedene Versandarten erforderlich, die wir im folgenden darstellen.

Um eine Versandart anzulegen, suche einfach über die **Smart Search ** nach **Versandarten ** und klicke auf**+NEU**. Wenn du generelle Informationen zum Thema Versandarten in Xentral benötigst, schau dir diesen[Handbuchabschnitt](urn:resource:component:72738)an.

> **Anmerkung**
>
> Natürlich kannst du die Optionen kombinieren, so dass du sowohl Paket- als auch Speditionsversand anlegen und nutzen kannst.

## Automatisierter Paketversand mit DHL

Voraussetzungen: Sowohl Hin- als auch Rückversand erfolgen über denselben Versandmodus (DHL 3.0)

Vorteile: Die Anbindung erfolgt automatisiert. Ein Retourennummernpool ist nicht erforderlich.

> **Anmerkung**
>
> *) Alternativ kannst du den Prozess auch über Hermes automatisieren. Dafür ist eine kleine Anpassung im Backend erforderlich. Wende dich bei Bedarf an unseren Support.

Für den automatisierten Paketversand mit DHL benötigst du zwei verschiedene Versandarten:

- Versandart für Lieferungen
- Versandart für Retouren

Lege sie zunächst beide an. Im Anschluss musst du beide nochmal zur Bearbeitung öffnen, um sie miteinander zu verknüpfen.

#### Versandart für Lieferungen

1. Klicke auf **+ NEU**.
1. Wähle **DHL**.
1. Klicke auf **Expertenmodus**.
1. Trage im oberen Abschnitt deine DHL Zugangsdaten ein und setze den Haken im Abschnitt Experte, um die Details der Versandart eintragen zu können.
1. Wir empfehlen folgende Einstellungen:
  (1) Trage eine Bezeichnung deiner Wahl ein, mit der du die Versandart identifizieren kannst.

  (2) Wähle das Projekt, das du für den Marktplatz vorgesehen hast.

  (3) Das Feld “Bevorzugte Rücksendemethode” kannst du erst auswählen, nachdem du die Versandart für Retouren angelegt hast. Lasse also dieses Feld zunächst leer und kehre später zurück.

  (4) Aktivieren

  (5) Auch das Feld “Retouren-Versandart für beigelegtes Rücksendeetikett” kann erst nach Anlegen der Retouren-Versandart ausgewählt werden. Lasse dieses Feld ebenfalls leer und setze die Verknüpfung später.

  (6) Aktivieren

#### Versandart für Retouren

1. Klicke auf **+ NEU**.
1. Wähle **DHL Retoure**.
1. Klicke auf **Expertenmodus**.
1. Trage im oberen Abschnitt deine DHL Zugangsdaten ein und setze den Haken im Abschnitt Experte, um die Details der Versandart eintragen zu können.
1. Wir empfehlen folgende Einstellungen:
  (1) Trage eine Bezeichnung deiner Wahl ein, mit der du die Retouren-Versandart identifizieren kannst.

  (2) Wähle das Projekt, das du für den Marktplatz vorgesehen hast.

  (3) Das Feld “Retourenempfänger” kannst du erst auswählen, nachdem du die normale Versandart und die Retouren-Versandart miteinander verknüpft hast. Lasse also dieses Feld zunächst leer und kehre zurück, nachdem du die beiden Verknüpfungen in der Versandart für Lieferungen gesetzt hast. Beachte dazu die Anleitung im vorherigen Abschnitt.

  (4) Aktivieren

## Speditionsversand

Voraussetzungen: Retourennummernpool (beim Spediteur anfragen)

Wenn du deine Waren per Spedition versendest, ist keine besondere Retouren-Abwicklung erforderlich, um einen Auftrag als “fulfilled” an den OTTO Market rückmelden zu können. Hier genügt somit eine einzige Versandart für die Lieferungen, bei der du das Modul “Spedition” wählst und die gewünschten Daten einträgst.

![image-20240912-103340.png](https://help.xentral.com/hc/article_attachments/18684056949276)

(1) Trage eine Bezeichnung deiner Wahl ein, mit der du die Versandart identifizieren kannst.

(2) Wähle das Projekt, das du für den Marktplatz vorgesehen hast.

(3) Das Feld “Bevorzugte Rücksendemethode” belässt du so, wie es vorbelegt ist. Nachdem du die Versandart gespeichert hast, wird die Feldbezeichnung der neuen Versandart automatisch in dieses Feld übernommen.

## Paketversand über einen anderen Versanddienstleister (nicht DHL 3.0, nicht Hermes) / über einen Fulfiller

Voraussetzungen: Retourennummernpool (beim Versanddienstleister / Fulfiller anfragen)

> **Anmerkung**
>
> Der Modus ist auch dann zutreffend, wenn Hin- und Rückversand mit unterschiedlichen Anbietern erfolgen soll.

Falls du deinen Versand- und Retouren-Prozess an einen Fulfiller ausgelagert hast, oder deine Pakete mit einem anderen Dienstleister als DHL/Hermes versendest, kannst du deine gewünschte(n) Versandart(en) ganz normal anlegen. Wähle als Modul den zutreffenden Dienstleister aus und trage die Daten ein. Wenn du diese Option nutzt, frage bei deinem Versanddienstleister einen Retourennummernpool an.

> **Anmerkung**
>
> Du benötigst diesen Retourennummernpool bei der Konfiguration deiner OTTO Connect Schnittstelle, damit ein Auftrag über die Schnittstelle als “fulfilled” an den Marktplatz zurückgemeldet werden kann.