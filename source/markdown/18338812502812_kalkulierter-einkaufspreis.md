Der kalkulierte Einkaufspreis (EK) in Xentral ermöglicht eine detaillierte Kostenkalkulation und dient als Grundlage für die Margenberechnung sowie die Inventarbewertung. Er kann manuell im Artikel hinterlegt oder automatisch anhand von Bestelldaten berechnet werden. Zudem können Zusatzkosten wie Zoll, Logistik oder Versandkosten einbezogen werden, um eine realistische Preisstruktur zu erhalten.

Xentral bietet verschiedene Möglichkeiten zur Berechnung des kalkulierten EK:

- **Manuelle Eingabe **: Direkte Hinterlegung des EK-Preises im Artikel unter ** Details**.
- **Automatische Berechnung**: Ermittlung auf Basis von abgeschlossenen Bestellungen oder vorkonfigurierten Kalkulationsregeln.
- **Stücklisten-Kalkulation**: Berechnung der Gesamtkosten basierend auf den Einkaufspreisen der einzelnen Komponenten.

Der kalkulierte EK kann in Belegen wie Bestellungen und Aufträgen genutzt werden und beeinflusst sowohl die Deckungsbeitragsrechnung als auch die Bewertung des Lagerbestands. Änderungen am kalkulierten EK werden automatisch aktualisiert, es sei denn, eine abweichende Berechnungslogik ist definiert. Zudem lassen sich Einkaufspreise und Margen durch Import- und Exportfunktionen flexibel anpassen.

Durch die korrekte Pflege des kalkulierten Einkaufspreises kannst du eine präzisere Kostenkontrolle gewährleisten und fundierte Preisentscheidungen treffen.

## Stücklisten-Kalkulation des kalkulierten EK-Preises

Bei der Nutzung von Stücklisten kann der kalkulierte Einkaufspreis (EK) der Unterkomponenten automatisch in den Hauptartikel (Kopfartikel) übernommen werden. Dies ermöglicht eine präzisere Kostenkalkulation für zusammengesetzte Produkte.

> **Anmerkung**
>
> **Hinweis**
>
> **Automatische Berechnung des kalkulierten EK für Stücklisten:**
>
> - Der kalkulierte EK wird standardmäßig nicht automatisch von den Unterkomponenten auf die Stückliste durchgereicht.
> - Um dies zu aktivieren, muss die Einstellung „Autostücklisten berechnen“ gesetzt werden.
> - Falls kein Faktor angegeben ist, werden die kalkulierten EK-Preise der Unterkomponenten einfach aufaddiert.
> - Falls ein Faktor (z. B. 30 für einen Aufschlag von 30%) angegeben ist, wird der kalkulierte EK entsprechend angepasst.
>
> **Automatische oder manuelle Aktualisierung:**
>
> - Der kalkulierte EK der Stückliste wird standardmäßig über Nacht automatisch aktualisiert, ohne dass ein separater Prozessstarter eingerichtet werden muss.
> - Alternativ kann die Berechnung manuell über einen Button in den Einstellungen sofort ausgelöst werden.
> - Dabei wird der kalkulierte EK des Kopfartikels überschrieben, falls sich der EK einer Unterkomponente geändert hat oder ein neuer Faktor hinterlegt wurde.

Durch diese Mechanismen stellt Xentral sicher, dass Stücklisten immer mit aktuellen Einkaufspreisen kalkuliert werden, was zu genaueren Margen- und Preisberechnungen führt.

### Einstellungen Stücklisten-Kalkulation

Die Einstellungen zum **Kalkulierten EK für Stücklisten ** findest du im **Bereich Einstellungen > Stammdaten > Artikel > Auto Stücklisten Berechnung ** oder über die Smart-Suche über**Auto Stücklisten Berechnung **. ** Schritte:**

- Setze für die automatische Berechnung des Kalkulierten EK den Haken auf ** Aktiv**.
- **Optional**: Verwende ein Artikel-Freifeld für einen Faktor, der für den Kalkulierten Einkaufspreis aufgeschlagen werden soll. Wenn du keinen Faktor verwendest, werden die Kalkulierten Einkaufspreise der Stücklisten Kind-Artikel aufaddiert.
- Klicke auf **Speichern** um die Einstellungen zu setzen.

> **Anmerkung**
>
> Der Faktor wird als prozentualer Aufschlag berechnet:
>
> *Kalkulierter Einkaufspreis = (Berechneter Einkaufspreis × Menge) × (1 + Faktor/100)*
>
> **Beispiel**: Ein Faktor von 30 erhöht den kalkulierten EK um 1,3-fach.
>
> **Verwende ganze Zahlen oder Kommazahlen mit '.'** z.B. '** 30 **' oder '**

35.5**'.
>
> Falls kein Faktor angegeben ist, wird nur die Summe der kalkulierten EK-Preise der Unterkomponenten addiert.

### Achtung

Wenn die Funktion **Auto Stücklisten Berechnung ** aktiviert ist, wird der Haken**Kalkulierter EK** im Stücklisten-Kopfartikel automatisch gesetzt.

Die kalkulierten EK-Preise der Kind-Artikel werden dann nachts durch einen Systemprozess oder sofort per Buttonauslösung aufaddiert und in den Kopfartikel übernommen. Dabei werden bestehende manuelle Einträge im Kopfartikel überschrieben.

![stuecklisten_einstellungen_kalkulierter_Einkaufspreis.png](https://help.xentral.com/hc/article_attachments/18356090872092)

| Feld | Beschreibung |
| --- | --- |
| Aktiv | Bei aktivierter 'Auto-Stücklistenberechnung' wird 'Kalkulierter EK' im Kopfartikel automatisch gesetzt, und die EK-Werte der Unterkomponenten über Nacht oder manuell summiert, wodurch manuelle Preise überschrieben werden. |
| Freifeld für Faktor | Freifeld zur Definition eines Preiserhöhungsfaktors. Der kalkulierte Stücklistenpreis wird aus der Summe aller Materialien plus eines Faktors in Prozent berechnet. Der Faktor muss als ganze Zahl oder Dezimalzahl mit Punkt als Trennzeichen eingegeben werden. Beispiele: '30' für 30 % oder '30.5' für 30,5 %. |

### Kalkulierten Einkaufspreis im Artikel eingeben

Um eine genaue Kalkulation für Stücklistenartikel zu gewährleisten, kannst du den kalkulierten EK für die Unterkomponenten (Kind-Artikel) hinterlegen. Diese Werte werden anschließend in den Kopfartikel der Stückliste übernommen.

**Schritte: **

- Kind-Artikel öffnen und kalkulierten EK hinterlegen: Navigiere zu ** Stammdaten > Artikel**.
- Suche den gewünschten Unterartikel (Kind-Artikel), der Bestandteil einer Stückliste ist.
- Öffne den Artikel und gehe zum Reiter **Details ** und Scrolle nach unten zum Feld **Kalkulierter EK-Preis**.
- Trage hier den kalkulierten Einkaufspreis ein, entweder: **Manuell **: Direkt den Preis eingeben. ** Automatisch**: Falls der Preis aus Bestellungen übernommen werden soll, kann dies über den Reiter Kalkulation konfiguriert werden.
- Klicke auf **Speichern**.

![artikel_einstellungen_kalkulierter_Einkaufspreis_001.png](https://help.xentral.com/hc/article_attachments/18356129316508)

### Aktualisierung des Kopfartikels in der Stückliste **Schritte:**

- Navigiere zum Stücklisten-Kopfartikel.
- Stelle sicher, dass die Option **Autostücklisten berechnen** in den Einstellungen aktiviert ist.
- Falls eine sofortige Aktualisierung gewünscht ist: Klicke auf **Kalkulation ausführen**, um die neuen kalkulierten EK-Preise direkt zu übernehmen.

> **Anmerkung**
>
> Falls kein manueller Eingriff erfolgt, wird der kalkulierte EK in der Nacht automatisch aktualisiert und in den Kopfartikel übernommen.

![stuecklisten_einstellungen_kalkulierter_Einkaufspreis_001.png](https://help.xentral.com/hc/article_attachments/18356129317660)