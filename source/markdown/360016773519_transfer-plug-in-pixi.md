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

## Anbindung von Descartes Pixi (Warehouse Management System)

Durch die Anbindung von Xentral ist es möglich das Warehouse Management System (WMS) Pixi mit Xentral als ERP zu betreiben. So wird die Auftragsbearbeitung mit Hilfe eines umfangreichen WMS möglich. Gleichzeitig führt Xentral immer aktuelle Lagerzahlen und gibt diese zuverlässig in der Folge auch an alle angeschlossenen Shops und Marktplätzen weiter. Xentral bietet mit der vorhandenen Schnittstelle die folgenden Übertragungswege an: Xentral → Pixi

- Übertragung der Aufträge
- Übertragung von Artikeln

Pixi → Xentral

- Übertragung aktueller Lagerzahlen
- Übertragen der Trackingnummern inkl. Seriennummern, MHDs und Chargen

Für die Anbindung an Pixi wird das[Übertragungen Modul](https://xentral.com/helpdesk/edi-xml-pdf)benötigt.

### Einstellungen

#### API-Zugang

Zunächst muss ein neue API-Zugang angelegt werden, diesen beinhaltet jedoch selbst noch keine Zugangsdaten und dient nur einer korrekten Zuordnung im System.

#### Modul Übertragungen

Die Einstellungen werden im Modul Übertragungen vorgenommen. Dazu ist lediglich ein neuer Account anzulegen und der Übertragungstyp Pixi zu wählen.

1. Erstelle ein neues Konto mit +NEU.
1. Aktiviere unter Einstellungen das Kontrollkästchen Aktiv und gib eine Bezeichnung ein (z. B. "Descartes Pixi").
1. Wähle unter Kommunikation das zuvor für Pixi erstellte API-Konto und in der Dropdown-Liste Übertragungsformat die Option "Pixi".
1. Gib die Zugangsdaten für den API-Zugang im Pixi-Backend in den folgenden Feldern im Abschnitt Kommunikation an:
  - Server
  - Port
  - Username
  - Passwort
1. Wähle im Abschnitt Belege versenden die Belegart "Auftrag" und den Belegstatus "Freigegeben".
1. Aktiviere im Bereich Belege empfangen das Kontrollkästchen "Lagerzahlen empfangen" und das Kontrollkästchen "Tracking empfangen".
1. Definiere übertragungsspezifische Einstellungen:
  - WSDL → Pfad zur WDSL-Definition
  - Channel → Kanalsauswahl. Die Kanäle stehen nach der ersten erfolgreichen Verbindung zu Pixi austomatisch zur Auswahl bereit.
  - ShopId → Eintrag der festgelegten Shop ID
  - Pixi-Datenbank → Pixi-Datenbank (Setting im Backend von Pixi)
  - Kundennummer → Bitte fragen Sie unseren Support
  - Zahlungsweise überschreiben → Zahlungsweise wird grundsätzlich mit dem hier enthaltenen Wert überschrieben
  - pixiImportProcessXML ausführen → Führt die unter pixiImportProcessXML hinterlegten Daten aus
  - Interne Bemerkung in Pixi-GiftMessage → Interne Bemerkung
  - Auftragspositionen mit Subpositionen nummerieren → Bitte fragen Sie unseren Support
  - Stücklistenelemente nicht übertragen → Stücklistenelemente werden nicht übertragen
  - Debugfunktionen → Erweitertes Logging um fehlerhafte Werte in der Übertragung zu identifizieren
  - UTF-8 → Sprachabhängig
  - Artikel Catalog-ID → Aus Pixi Backend
  - Artikel Catalog-Version → Aus Pixi Backend
  - Artikelnummer statt EAN wenn EAN leer → Bei leerer Artikelnummer werden EANs übertragen
  Nur Lagerartikel übertragen → Es werden nur Lagerartikel übertragen

Bei den Einstellungen zur Pixi-API unterstützt Sie gerne auch unser Support-Team. Wir empfehlen die Buchung eines unserer Supportpakete zur Schnittstellenanbindung. Nähere Informationen dazu bekommen Sie von unserem Support.

### Monitoring

Bitte sichten Sie regelmäßig den Monitor im Übertragungen Modul. Mögliche Fehlermeldungen werden dort dargestellt.