Mit dem Xentral-Modul **Kopie Belege Empfänger** kannst du gezielt automatisch Kopien von Belegen (z. B. Rechnungen, Lieferscheine, Angebote) an E-Mail-Adressen oder Drucker versenden – vollständig ohne manuelle Zwischenschritte.

Beispiel aus der Praxis: Ein **Lieferschein kann automatisch an einen Drucker im Lager geschickt werden**, sobald der Beleg erzeugt wird – ohne dass ein Arbeitsplatz mit Xentral im Lager vorhanden sein muss. Genauso kann eine Kopie der Rechnung automatisiert an die Buchhaltung oder ein externes System geschickt werden.

## Funktionen im Überblick

### Kopie - Versand per E-Mail

- **Absenderadresse**: Wird aus der Standard-E-Mail-Adresse unter Einstellungen > System > Grundeinstellungen > E-Mail gezogen.
- **Absendername**: Wird aus dem Feld „Name“ in denselben E-Mail-Einstellungen übernommen. Ist dieses leer, wird der Firmenname verwendet.

### Kopie - Versand an Drucker

- Es stehen ausschließlich **Standarddrucker** zur Auswahl (keine Faxgeräte oder Etikettendrucker).
- Belege werden direkt ohne Benutzerinteraktion auf dem Zielgerät gedruckt.

### Unterstützte Belegtypen

Du kannst das automatische Versenden für folgende Belege aktivieren:

- Angebot
- Auftrag
- Rechnung
- Gutschrift
- Lieferschein
- Proformarechnung

## Einstellungen

Die Einstellungen erreichst du über den Button „+NEU“, um einen neuen Empfänger anzulegen. Im Dialog kannst du Folgendes konfigurieren:

**Belegkonfiguration:**

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Belegtyp | Auswahl des zu überwachenden Belegtyps (z. B. Rechnung, Lieferschein) |
| Art | Versandart: E-Mail oder Drucker |
| Nur bei Autoversand | Beleg wird nur dann gesendet, wenn Xentral ihn automatisch versendet |
| Empfänger E-Mail-Adresse | Zieladresse für die E-Mail (nur bei Versandart E-Mail) |
| Empfänger Name | Interner Name zur besseren Zuordnung (z. B. „Lagerdrucker Nord“) |
| Aktiv | Checkbox zum Aktivieren oder Deaktivieren der Konfiguration |

![kopie_belege_empfaenger.png](https://help.xentral.com/hc/article_attachments/22009159532700)

## Filtermöglichkeiten für gezielten Versand

### Projektfilter

- Bezieht sich auf das im Beleg hinterlegte Projekt.
- Es stehen alle Projekte zur Auswahl, für die du entsprechende Rechte hast.
- Ist kein Projekt angegeben, gilt die Konfiguration für **alle Projekte**.

### Adressfilter

- Bezieht sich auf die Adresse (z. B. Kunde oder Lieferant) im Beleg.
- Auswahl ist auf Adressen beschränkt, die im Kontext von Projekten stehen, auf die du Zugriff hast.
- Ohne Adressangabe gilt die Regelung für **alle Belege**, unabhängig vom Adressaten.

> **Anmerkung**
>
> **Hinweis**
>
> **Beispiel**: Mit dem Modul kannst du z. B. alle Rechnungen automatisch an den Steuerberater per E-Mail senden oder alle Angebote an eine zentrale Archivadresse weiterleiten – ganz ohne manuelles Eingreifen.