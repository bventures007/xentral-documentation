In diesem Artikel zeigen wir euch einen schnellen und einfachen Weg, um in Xentral vorhandene Daten an separate Tools zur Datenaufbereitung, wie beispielsweise Power BI oder Google Sheets zu nutzen. Um eure Daten in diesen externen Anwendungen nach euren Bedürfnissen strukturiert und grafisch aufgearbeitet darzustellen, sind einige vorbereitende Einstellungen notwendig, die im Folgenden beschrieben werden.

> **Wichtig**
>
> Die im Folgenden beschriebenen Methoden erfordern fortgeschrittene Kenntnisse zum Thema Datenstrukturen, -aufbereitung und -analyse. Du solltest sie nur nutzen, wenn es unabdingbar ist, dass externe Tools deine Daten aus Xentral auswerten. Außerdem solltest du über das entsprechende Know-How verfügen, wie du deine sensiblen Geschäftsdaten sicher behandelst und lagerst.
>
> Schau dir vorher unbedingt den ArtikelÜbersicht: Berichtswesen - Controlling, Statistiken und Reportsan, um zu sehen, ob deine Anforderungen auch mit dem Modul **Berichte** direkt in Xentral erfüllt werden können.

## Welche Optionen zum Datenexport gibt es?

Xentral bietet dir die folgenden Optionen, um deine Daten in externe Tools zu überführen:

- **Daten über Xentral-API anfordern**: Du kannst die Daten über einen dedizierten API-Call abrufen.
- **Daten auf FTP-Server sichern**: Du kannst einen FTP-Server mit Xentral verbinden, sodass später in fest definierten Abständen aktuelle Daten auf diesem Server abgelegt werden.
- **Daten per Permalink bereitstellen**: Du kannst in Xentral einen so genannten Permalink mit stets aktuellen Daten erstellen, den du in anderen Tools hinterlegst.
- **Daten in Google Sheets überführen**: Werte deine Berichtsdaten in Google Tabellen aus, indem du ein bestimmtes Skript ausführst.

> **Wichtig**
>
> Alle drei genannten Vorgehensweisen verbrauchen Abfragen aus deinem monatlichen Kontingent, das je nach Tarifmodell (Basis oder Premium) limitiert ist. Falls du regelmäßig vollständige und umfangreiche Datenexporte benötigst, musst du die **Premium**

-Version des Berichtesmoduls buchen!

## Verfügbare Berichtsvorlagen in Xentral

Speziell für den Einsatz externer BI-Tools haben wir in Xentral eine vorgefertigte Sammlung mit den am häufigsten benötigten Daten erstellt.

Schau dir vor der Erstellung eines Datenexports diese Sammlung an, um zu sehen, welche enthaltenen Daten für dich relevant sind.

1. Logge dich in Xentral ein.
1. Öffne das Menü **Berichtswesen > Berichte (Neu)**.
1. Klicke auf den Eintrag **[8] FTP-Backup und BI-Reports**.

> **Tipp**
>
> Findest du in der Liste nicht genau den Bericht, den du benötigst? Dann kannst du dir ganz einfach mithilfe des **No-Code Editors ** eigene Berichte konfigurieren. Für fortgeschrittene Nutzer findest du zusätzlich einen**SQL-Editor**, den du für die Erstellung komplexer Abfragen nutzen kannst.
>
> Alle wichtigen Informationen zur Erstellung individueller Berichte findest du im KapitelIndividuelle Berichte erstellen.

### Liste aller verfügbaren Berichtsvorlagen

Im Folgenden findest du eine Auflistung aller verfügbaren Berichtsvorlagen der Sammlung **[8] FTP-Backup und BI-Reports** inklusive einer kurzen Beschreibung der enthaltenen Daten.

| Berichtsname | Daten |
| --- | --- |
| **Adressen** | Liste aller Kunden- und Lieferadressen |
| **Alle EKs** | Alle Einkaufspreise mit Artikelinformationen |
| **Alle VKs** | Alle Verkaufspreise mit Artikelinformationen |
| **Angebots_Position + Angebote** | Artikelpositionen inklusive zugehöriger Angebote |
| **Artikel** | Stammdate aller Produkte/Artikel |
| **Auftrag_Position + Aufträge** | Auftragspositionen und zugehörige Aufträge |
| **Bestellung_Position + Bestellungen** | Bestellpositionen und Bestellungen mit Lieferanteninformationen |
| **Gutschrift_Position + Gutschriften** | Gutschriften und deren Positionen |
| **Kategorien** | Produktkategorien mit Hierarchie |
| **Lager_Reservierungen** | Reservierungen im Lager |
| **Lagerbestand inkl. Charge/MHD** | Aktueller Lagerbestand inklusive Chargen- und MHD-Information |
| **Lagerbewegung inkl. MHD/Charge** | Alle Lagerbewegungen mit MHD- und Chargenverfolgung |
| **Lagerwerte** | Warenwerte im Lagerbestand |
| **Lieferschein_Position + Lieferschein** | Lieferscheine und deren Positionen |
| **Produktion_Position + Produktion** | Produktionspositionen und zugehörige Produktionsaufträge |
| **Projekte inkl. Teilprojekte** | Projektstammdaten inklusive Teilprojekten |
| **Rechnung_Position + Rechnungen** | Rechnungspositionen und zugehörige Rechnungen |
| **Retouren_Position + Retouren** | Retouren und deren Positionen |
| **Verbindlichkeit_Positionen + Verbindlichkeiten** | Verbindlichkeiten und deren Positionen |
| **Zeiterfassung mit Projektzuweisung** | Erfasste Zeiten mit Bezug zu Projekten |

## Berichtsdaten per Permalink bereitstellen

Nachdem du den für dich passenden Bericht ausgewählt hast, kannst du damit fortfahren, den Datenexport zu konfigurieren.

Die einfachste und schnellste Möglichkeit ist meist die Erstellung eines Permalinks (Kurzform für **permanenter Link**). Permalinks sorgen dafür, dass jederzeit zuverlässig auf dieselbe Datenquelle verwiesen wird. Dies kannst du dir wie folgt zu Nutze machen:

- Du öffnest den gewünschen Bericht in Xentral und generierst im Tab **Exporteinstellungen** einen Permalink zu diesem Bericht.
- Den so erstellten Permalink hinterlegst du dann in externen BI-Tools wie z.B. **PowerBI**.
- Einmal täglich (über Nacht) werden die Berichtsdaten, auf die der Permalink verweist, durch Xentral neu berechnet.
- Anschließend kannst du die aktuellsten Geschäftsdaten in deinem externen BI-Tool einsehen.

Gehe wie folgt vor, um einen Permalink zu den Daten eines Berichts zu erstellen.

1. Öffne das Menü **Berichtswesen > Berichte (Neu)**.
1. Klicke auf den Eintrag **[8] FTP-Backup und BI-Reports**.
1. Öffne den gewünschten Bericht, indem du auf den Berichtsnamen klickst.
1. Öffne das Tab **Exporteinstellungen**.
1. Klicke auf **Permalink (URL)**.
1. Nimm die gewünschten Einstellungen für den Permalink vor.
1. Klicke auf **Permalink erstellen**.

## Berichtsdaten auf FTP-Server exportieren

Wenn du in regelmäßigen Abständen deine Berichtsdaten auf einem eigenen FTP-Server ablegen willst, müssen folgende Bedingungen erfüllt sein:

- Du verfügst über alle Zugangsdaten zu deinem FTP-Server und über das notwendige Wissen, wie dieser funktioniert
- Du hast die Verbindung zu deinem FTP-Server im Menü **Einstellungen > Administration > Datenaustausch > FTP** angelegt, also deine Zugangsdaten eingegeben

Gehe wie folgt vor, um Berichtsdaten auf deinem FTP-Server abzulegen.

1. Öffne das Menü **Berichtswesen > Berichte (Neu)**.
1. Klicke auf den Eintrag **[8] FTP-Backup und BI-Reports**.
1. Öffne den gewünschten Bericht, indem du auf den Berichtsnamen klickst.
1. Öffne das Tab **Exporteinstellungen**.
1. Klicke auf **FTP-Export**.
1. Nimm die genauen Einstellungen für den FTP-Export vor.
1. Klicke auf **Export anlegen**.

## Berichtsdaten in Google Sheets bereitstellen

Wenn du kein separates BI-Tool verwendest, kannst du deine Berichtsdaten aus Xentral auch alternativ in Google Sheets (auch Google Tabellen) aufbereiten.

Klicke auf den folgenden Link, um Schritt für Schritt durch die Anbindung an Google Sheets geführt zu werden:

- [Xentral Google Sheets Connection](https://github.com/xentral/xentral-gsheet-connection)