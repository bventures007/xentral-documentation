Eine **Teillieferung** erlaubt dir, nur einen Teil der Artikel aus einem Auftrag an den Kunden zu versenden – beispielsweise weil nicht alle Artikel auf Lager sind oder weil bestimmte Artikel vorab geliefert werden sollen.

## Teillieferung aus einem Auftrag erstellen

In Xentral kann eine Teillieferung direkt aus einem Auftrag heraus gestartet werden. Mit der Teillieferungsfunktion können lagernde Artikel aus einem Auftrag vorab versendet werden. Nicht verfügbare Artikel verbleiben im Originalauftrag und können später ausgeliefert werden.

**Schritte: **

1. Gehe in die Auftragsübersicht:** Verkauf > Auftrag**.
1. Klicke im Minidetail auf **Auftrag > Aktion > Teillieferung erstellen**. Alternativ klicke in einen Auftrag und wähle dort diese Aktion aus.
1. Wähle die Positionen aus, die in die Teillieferung übernommen werden sollen: Automatischer Vorschlag für den neuen Auftrag (Teillieferung). Die manuelle Auswahl kann jederzeit überschrieben oder angepasst werden.
1. Zusatzoptionen prüfen: Optional kannst du: Die **manuelle Zahlungsfreigabe ** erteilen, Die **Portoprüfung** ausschalten.
1. Klicke auf "**Teillieferung erzeugen**", um die Teillieferung zu erstellen.
1. Es wird ein neuer Teilauftrag mit Suffix -1 (z. B. 200005-1) erstellt.
1. Restauftrag bleibt bestehen: Der ursprüngliche Auftrag 200005 enthält weiterhin die nicht versendeten Artikel und kann später abgeschlossen werden.

![auftrag_teillieferung_aktion2_001.png](https://help.xentral.com/hc/article_attachments/22399624803484)

## Auswahlmaske für Teillieferung im Detail

Nach dem Klick auf „**Teillieferung erstellen**“ öffnet sich eine Benutzeroberfläche, in der du gezielt auswählst, welche Positionen versendet werden sollen. Hier die einzelnen Bereiche:

| Spaltenbezeichnung | Beschreibung |
| --- | --- |
| Pos | Positionsnummer innerhalb des Auftrags |
| Artikel | Bezeichnung des Artikels, wie im Artikelstamm hinterlegt. |
| Nummer | Die eindeutige Artikelnummer, die intern zur Identifikation verwendet wird. |
| Menge | Die ursprünglich im Auftrag bestellte Menge dieses Artikels. |
| Reserviert | Zeigt, wie viele Stück für diesen Auftrag (links) und insgesamt systemweit (rechts) bereits reserviert wurden. Format: z. B. „0 / 0“. |
| Lager | Gibt an, wie viele Stück aktuell im Lager physisch verfügbar sind. Bei mehreren Lagerorten werden Details darunter eingeblendet (z. B. Lagername, Lagerplatz, Menge). Z.B. 'Hauptlager Lagerplatz1 (Verfügbare Menge: 30)' |
| Versenden | Eingabefeld für die gewünschte Versandmenge im Rahmen dieser Teillieferung. Nur vollständig verfügbare Artikel werden hier mit Menge vorgeschlagen; andere Felder bleiben leer oder auf „0“. |

> **Anmerkung**
>
> **Hinweis**
>
> **Beispiel:** Teillieferung aus Auftrag 200005
>
> Der Auftrag enthält drei Artikel. Nur die **LED-Deckenlampe** ist vollständig auf Lager.
>
> Beim Anlegen einer Teillieferung wird automatisch ein neuer **Teilauftrag 200005-1** erzeugt, der nur diese lagernde Position enthält.
>
> Die **nicht verfügbaren Artikel ** (Trinkflasche und Schneidebrett) verbleiben im ursprünglichen Auftrag** 200005** und können später separat geliefert werden, sobald sie wieder verfügbar sind.

![auftrag_teillieferung_auswahl_artikel_001.png](https://help.xentral.com/hc/article_attachments/22399624805532)

## Informationen im Originalauftrag nach einer Teillieferung

Auch nach der Erstellung einer Teillieferung behält der ursprüngliche Auftrag alle relevanten Informationen. Diese werden im Protokoll festgehalten und ermöglichen eine vollständige Nachverfolgung.

### Mengenübersicht (inklusive Teilaufträgen)

Die Tabelle zeigt alle im Auftrag enthaltenen Positionen mit ihrem jeweiligen Status:

- Menge: ursprünglich bestellte Stückzahl
- Geliefert: Anzahl der bereits ausgelieferten Artikel
- Offen: Anzahl der noch nicht gelieferten Artikel

Damit ist auf einen Blick erkennbar, welche Positionen bereits verschickt wurden und welche noch ausstehen.

### Teilaufträge

Zusätzlich wird unter „Teilaufträge“ dokumentiert, welche neuen Teilaufträge aus dem Originalauftrag entstanden sind. Die Übersicht enthält:

- Datum der Teillieferung
- Belegnummer des Teilauftrags
- Kunde / Name
- Betrag des Teilauftrags
- Aktion (z. B. Status oder Folgeprozesse)

Auf diese Weise bleibt der gesamte Liefer- und Rechnungsprozess nachvollziehbar: Das Protokoll im Originalauftrag dient als zentrale Referenz, während der Originalauftrag mit den Teilaufträgen die tatsächlichen Lieferungen abbilden.

![auftrag_teillieferung_mindetail_originalauftrag.png](https://help.xentral.com/hc/article_attachments/22399640587164)

## Informationen im Teilauftrag nach einer Teillieferung

Nach dem Anlegen einer Teillieferung wird ein neuer Teilauftrag erzeugt. Dieser erhält die Auftragsnummer des Hauptauftrags mit dem Zusatz „-1“.

Im Teilauftrag werden nur die Positionen aufgeführt, die in der originalen Lieferung **nicht mehr enthalten** sind und somit lagernd sind und geliefert werden können.

Die Übersicht enthält pro Artikel:

- **Nummer**: die Artikelnummer
- **Name_de**: die Bezeichnung des Artikels
- **Menge**: die ursprünglich bestellte Stückzahl
- **Geliefert**: bleibt leer, da diese Artikel noch nicht versendet wurden
- **Offen**: zeigt die Menge, die in einem späteren Schritt geliefert werden muss

Damit dient der Teilauftrag als Arbeitsgrundlage für die Nachlieferung. Sobald die Artikel verfügbar sind, kann aus diesem Teilauftrag die nächste Lieferung erzeugt werden.

![auftrag_teillieferung_minidetail_teilauftrag_1.png](https://help.xentral.com/hc/article_attachments/22399640589852)