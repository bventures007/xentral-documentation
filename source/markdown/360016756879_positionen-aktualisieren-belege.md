Mit dem Modul **Positionen Aktualisieren** erhältst du in allen Belegen im Entwurfsmodus einen zusätzlichen Button, um die Belegpositionen erneut aktualisieren und Daten aus dem Artikelstamm nachzuladen. Diese Funktion hilft dir Klickpfade abzukürzen, wenn sich in deinen Belegen im Entwurfsmodus vor der Freigabe Änderungen z.B. an der Artikelbeschreibung oder den Preisen ergeben haben. Du kannst größere Angebote oder Aufträge bereits frühzeitig anlegen und die Positionen später kurz vor der Freigabe kontrollieren und aktualisieren.

> **Tipp**
>
> **Anwendungsbeispiel **: Angenommen, du hast ein Angebot verschickt. Zwei Monate später möchtest du ein zweites Angebot mit aktualisierten Preisen verschicken. Hierfür könntest du das Angebot einfach kopieren, auf ** Positionen aktualisieren**klicken und würdest für das zweite Angebot die aktuellen Preise erhalten, ohne dass Positionen manuell entfernt und wieder eingefügt werden müssen.

Das Modul kannst du über **Appstore **>** Positionen aktualisieren ** oder über die Smart Search über **Positionen aktualisieren ** aufrufen. ** Schritte Positionen aktualisieren z.B. im Auftrag:**

1. Gehe in einen Auftrag, den du duplizieren möchtest.
1. Wähle die Aktion **Auftrag kopieren**. Du erhältst als Kopie einen neuen Auftrag im Entwurfsmodus.
1. Klicke auf den Reiter **Positionen**.
1. Klicke auf den Button **Positionen aktualisieren**. Die Artikelpositionen werden mit dem Artikelstamm abgeglichen und nachgeladen.
1. Gib den Auftrag frei und versende diesen an deinen Kunden.

## Aktualisierte Werte

Folgende Werte werden bei einem Klick auf den Button in den Beleg-Positionen aktualisiert:

- **Bezeichnung (de)**: deutschsprachige Artikelbezeichnung
- **Beschreibung (de)**: deutschsprachige Artikelbeschreibung
- **Preis (Einkaufs- bzw. Verkaufspreis)**: Einkaufspreis und Verkaufspreis sofern nicht anders eingestellt
- **Artikelnummer beim Kunden**: Artikelbezeichnung für den Kunden, die im Verkaufspreis mit hinterlegt werden kann
- **Zolltarifnummer**: Zolltarifnummer im Artikel
- **Herkunftsland**: Herkunftsland im Artikel
- **Freifeld 1-20**: Freifelder im Artikel
- **Bezeichnung (en)**: Sofern die Belegsprache auf Englisch umgestellt wurde und die Artikelbezeichnung englischsprachig hinterlegt ist
- **Beschreibung (en)**: Sofern die Belegsprache auf Englisch umgestellt wurde und die Artikelbeschreibung englischsprachig hinterlegt ist

> **Anmerkung**
>
> Voraussetzung für die Anzeige in der Belegvorschau bzw. im PDF Beleg ist eine Einblendung dieser Daten über deine individuellen Briefpapier- und Dokumenteneinstellungen. Daten, die du z.B. systemweit in Belegen ausgeblendet hast, werden zwar aktualisiert, aber dennoch im Beleg nicht mit angezeigt.

## Features

- Möglich bei Angebot, Auftrag, Rechnung, Lieferschein, Gutschrift und Proformarechnung
- Belege im Entwurfsmodus haben in der Positionsübersicht den Button **Positionen aktualisieren **

- Ist die Einstellung ** Positionen aktualisieren erlauben unabhängig vom Status des Belegs** aktiviert, ist der Button in der Positionsübersicht unabhängig des Belegstatus zu sehen
- Ist die Einstellung **Position wird nicht aktualisiert, wenn kein VK-Preis beim Artikel hinterlegt ist** aktiviert, wird die Position nicht aktualisiert wenn der Artikel keinen Verkaufspreis hat
- Falls Artikel eine Variante von einem anderen Artikel ist und seine Beschreibung leer ist, wird die Beschreibung des Hauptartikels genommen
- Wenn ein Verkaufspreis mit "Artikelnummer für Kunde" vorhanden ist, wird die "Artikelnummer für Kunde" als Artikelnummer aktualisiert, sonst die Artikelnummer des Artikels
- Felder die aktualisiert werden, werden weiter unten aufgelistet

## Einstellungen: Positionen Aktualisieren

Für die Funktion findest du folgende Einstellungen:

- **Positionen aktualisieren erlauben unabhängig vom Status des Belegs:** Positionen können auch aktualisiert werden, wenn der Beleg bereits freigegeben ist.
- **Position wird nicht aktualisiert, wenn kein VK-Preis beim Artikel hinterlegt ist:** Ist kein Verkaufspreis im Artikel hinterlegt (eingefügt in Positionen mit 0 Euro), wird beim Klick auf den Button kein Feld dieser Position aktualisiert.

![positionen_aktualisieren_004.png](https://help.xentral.com/hc/article_attachments/13773865805084)