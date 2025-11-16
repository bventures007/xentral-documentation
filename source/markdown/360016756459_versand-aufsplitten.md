Wenn du Waren mit gemischten Steuersätzen in einem Auftrag zusammen versendest und in Rechnung stellst, kann es sein, dass du verschiedene Möglichkeiten anwenden darfst, die die Porto Besteuerung betreffen. Je nach Sortiment und Regel im Steuerrecht kannst du möglicherweise dein Porto entsprechend der Artikelbesteuerung aufsplitten z.B. in 7% und 19%. Oder du musst den Steuersatz verwenden, auf den der wertmäßig größte Umsatzanteil entfällt.

Das Modul **Versand Aufsplitten** legt fest, ob die Portokosten nach Steuersätzen aufgeteilt werden oder ob diese durch den wertmäßigen Anteil der Steuersätze bestimmt werden.

Die Versandkosten können beim Import von Aufträgen aus Shopsystemen und Marktplätzen aufgesplittet werden. Die Berechnung erfolgt anschließend beim Aktualisieren im Auftrag.

Das Modul **Versand Aufsplitten** bietet dir die folgenden Features:

- Einen Portobetrag im Auftrag anteilig nach Steuersätzen aufteilen
- Einen Portobetrag im Auftrag anhand des größten Umsatzanteils setzen
- Einen beliebigen Portobetrag im Auftrag händisch als brutto oder netto Betrag einfügen und aufteilen
- Einen Portobetrag vom Onlineshop (z.B. Shopify) importieren und in Xentral aufteilen lassen

> **Warnung**
>
> Bevor du mit der Aufsplittung der Kosten im Auftrag beginnst, stelle sicher, welche Steuerrechtlichen Vorgaben für dein Geschäft gelten, indem du dich an dein lokales Steuerbüro oder das Finanzamt/Steuerbehörde wendest.

## Versand Aufsplitten einrichten

1. Gehe auf **Appstore > Versand Aufsplitten**.
1. Wähle die passende Einstellung aus, indem du:
  - keinen Haken setzt (manueller Betrieb des Moduls im Auftrag über Button)

  - den Haken für A **utomatisch nach Steuersätzen aufsplitten/anpassen** setzt

  - oder beide Haken setzt - den ersten und **Steuersatz aus überwiegenden Positionswert**

1. Speichern erfolgt durch das Setzen der Haken automatisch.

Du hast zwei Möglichkeiten zur Verfügung, um den Versand deiner Artikel aufzusplitten:

- **Automatisch nach Steuersätzen aufsplitten/anpassen**: Die Portoartikel werden automatisch nach Steuersätzen anteilig aufgeteilt. Es werden zwei Portoartikel eingefügt jeweils mit dem automatisch berechneten Wert des Splits.
- **Steuersatz aus überwiegenden Positionswert**: Der Portoartikel wird mit dem Steuersatz veranschlagt, der summenmässig den größten Anteil der Bestellung ausmacht.

> **Anmerkung**
>
> Die zweite Checkbox **Steuersatz aus überwiegenden Positionswert ** kann nur verwendet werden, wenn die erste Checkbox**Automatisch nach Steuersätzen aufsplitten/anpassen** ebenfalls aktiviert ist. Wurde die erste Checkbox deaktiviert, dann hat die zweite Checkbox keine Auswirkungen mehr. Konkret heißt das:
>
> - Die erste Checkbox kann allein verwendet werden
> - Die zweite Checkbox kann nur in Kombination mit der ersten Checkbox verwendet werden
>
> Hast du keinen der Haken gesetzt und das Modul in deiner Xentral Version aktiviert, so kannst du die Funktion im Auftrag bei der Positionseingabe über den Button **Versandsplitting** durchführen.

![819202.png](https://help.xentral.com/hc/article_attachments/10502131321244)

## Berechnung der Versandkosten im Auftrag

Die Porto Besteuerung kannst du in der Belegart Auftrag eingeben.

- Das Dokument kann im Bearbeitungsmodus oder im freigegebenen Modus sein.
- Du kannst immer die manuelle Eingabe über den Dialog verwenden
- Du kannst den Portoartikel mit Betrag auch über die Positionseingabe eintragen. Das spart dir viel Zeit, ist allerdings nur möglich, wenn du im Modul den automatischen Modus eingestellt hast.

### Manuelle Eingabe der Portokosten und Split im Auftrag (Dialog Eingabe)

1. Klicke auf den Button **Versandsplitting**.
1. Gib den Portobetrag ein z.B. 10 EUR.
1. Wähle aus, ob der Gesamt Porto Betrag **netto ** oder **brutto** sein soll.
1. Klicke auf **Versandartikelbetrag ändern**. Der Portobetrag wird automatisch neu berechnet oder aufgesplittet.

> **Anmerkung**
>
> Wird ein Auftrag freigegeben, wird automatisch die Split Funktion ausgeführt, sollte es zuvor im Bearbeitungsmodus noch nicht erfolgt sein.

![884738.png](https://help.xentral.com/hc/article_attachments/10502108065692)

### Automatisch nach Steuersätzen aufsplitten/anpassen (Position Eingabe)

> **Anmerkung**
>
> Voraussetzung Moduleinstellung:
>
> Immer automatisch beim Bearbeiten des Beleges nach Steuersätzen aufsplitten bzw. anpassen

Die Versandkosten werden im Auftrag automatisch bei Eingabe eines Versandkostenartikels gesplittet, indem ein weiterer Versandkostenartikel hinzugefügt wird und die anteilige Berechnung stattfindet. Hierfür gibst du die Positionen vollständig ein. Der Splitt erfolgt bei Eingabe des Portoartikels, d.h. der Artikel muss in den Einstellungen als **Artikel ist Porto** gekennzeichnet sein:

- Verkauf Artikel mit 7% eingeben, der Steuersatz ist vorher im Artikel eingestellt worden.
- Verkauf Artikel mit 19% eingeben, der Steuersatz ist vorher im Artikel eingestellt worden.
- Portoartikel eingeben, dabei ist der Artikel als Portoartikel gekennzeichnet.
- Beim Einfügen des Portoartikels wird automatisch ein Steuersatz anteilig eingefügt. Im selben Schritt wird ein weiterer Portoartikel mit dem anderen Steuersatz eingefügt. Die Portobeträge werden in dieser automatischen Berechnung wertmässig aufgeteilt. Der ursprüngliche Portobetrag ist der Verkaufspreis des Portoartikels, der im Artikel hinterlegt ist.

Bsp.

Porto Artikel Positionseingabe

![884745.png](https://help.xentral.com/hc/article_attachments/10502131447836)

Bsp.

Porto Artikel automatischer Split

![851971.png](https://help.xentral.com/hc/article_attachments/10502146740508)

#### Versandartikel mit automatischer Splittberechnung aus dem Auftrag löschen

Wird ein Portoartikel aus dem Auftrag gelöscht, so wird automatisch der Zweite eingefügt. Zum Löschen müssen beide Artikel vorne in der Spalte **Position ** ausgewählt werden. Der Löschvorgang erfolgt dann über den Button**Versandsplitting**:

- **Versandartikel löschen**: löscht alle Portoartikel komplett (Eine Neueingabe ist wieder möglich).
- **Versandartikelbetrag ändern**: ermöglicht die Änderung des kompletten Portobetrags.

Markiere die Artikel, die du für das Versandsplitting nutzen möchtest an und klicke auf den Button **Versandsplitting **. Nun kannst du den Versandartikelbetrag ändern, indem du auf den Button ** Versandartikelbetrag ändern**klickst und in das dann erscheinende Feld einen neuen Betrag eingibst.

![819211.png](https://help.xentral.com/hc/article_attachments/10502146789788)

> **Anmerkung**
>
> Das Löschen der Artikel ist auch über die Auswahl der Artikel und die Stapelverarbeitung möglich. Dazu markierst du die Artikel, die gelöscht werden sollen, und wählst im Drop-Down Menü der Stapelverarbeitung **Löschen** aus.

![851977.png](https://help.xentral.com/hc/article_attachments/10502146833180)

## Auftragsimport aus einem Online Shop

Wenn du Aufträge aus einem Online Shop in Xentral importierst, kannst du beim Import das Porto im Auftrag automatisch gemäß der Steuersätze aufsplitten lassen.

> **Anmerkung**
>
> Diese Einstellung setzt eine entsprechende Online Shop Konfiguration voraus. Möglicherweise benötigst du bei dieser Einstellung Unterstützung im Setup deines Onlineshops und/oder Konfigurationsunterstützung im Mapping der Shopaufträge (Online Shop Einstellungen/Konfiguration) in Xentral.

Folgende Voraussetzungen müssen dafür erfüllt sein:

- Dein Shop (z.B. Shopify) kann die Versandkosten korrekt übergeben und in Xentral auf einen Portoartikel matchen.
- Du hast im Modul **Versand Aufsplitten ** die automatische Funktion **Automatisch nach Steuersätzen aufsplitten/anpassen** aktiviert.
- Du hast die Steuersätze in deinem Shop entsprechend gepflegt und die Artikel werden mit korrekten Beträgen und Steuersätzen zu Xentral in den Auftrag übergeben.

## FAQ **Frage **: Kann ich mit dem Modul ** Versand Aufsplitten **Steuersätze und Portokosten verändern und Shopimporte korrigieren? ** Antwort **: Nein, du solltest das Modul ** Versand Aufsplitten**nur verwenden, wenn du Portokosten und Portobeträge aus deinem Shop für diene Rechnungsstellung aufteilen musst. Wenn du deinen Shop richtig konfiguriert hast und die entsprechende Konfiguration in Xentral darauf abgestimmt hast, ist es nicht notwendig Aufträge zu korrigieren. Du solltest dieses Setup richtig wählen und entsprechend sauber aufsetzen und auf deine Firmenbedürfnisse abstimmen. Natürlich können technische Gegebenheiten oder betriebswirtschaftliche und steuerrechtliche Anforderungen ein Standard Setup zwischen Xentral und deinem Shop erschweren. In diesem Fall solltest du dir Hilfe bei der Shop Konfiguration und der Konfiguration von Xentral holen und entscheiden, ob die Möglichkeit Versand Aufsplitten bei deinem Workflow möglich und gegeben ist.