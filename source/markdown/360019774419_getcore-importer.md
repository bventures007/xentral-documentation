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

> **Anmerkung**
>
> **Hinweis**
>
> Diese App hat das LabelSpezial. Das bedeutet, dass die App für einen speziellen Anwendungsfall entwickelt wurde, der möglicherweise nicht für jeden Kunden geeignet ist.

## Installation und Einrichtung GetCoreIO Schnittstelle

Um den GetCoreIO-Shop von ZMB in xentral integrieren zu können, benötigt man zwei Schritte. xentral bindet externe Shops, auch wenn diese extra APIs anbieten, immer über einen xentral Shop-Importer an. Das ist die genormte Schnittstelle für xentral.

![Getcore-1.png](https://help.xentral.com/hc/article_attachments/5102248761756)

Features der Schnittstelle

- Aufträge abholen
- Rückmeldung Trackingnummer

Die Belege werden im Versandprozess automatisch erstellt und versendet bzw. am Versanddrucker ausgedruckt.

### Allgemeiner Ablauf der Installation (für Techniker)

1. Installation des Shop-Importers im Webspace des Kunden
1. Anlegen eines Shops in xentral + Übertragungsschlüssel für die Kommunikation
1. Abspeichern des Übertragungsschlüssels Shop-Importer
1. Anlegen eines (nicht öffentlichen) Pfades für die Ablage der importieren Bestelldaten
1. Test der Übertragung

### Schritt 1: Anlegen eines neuen Shops in xentral

Administration → Shop Schnittstelle → Übersicht → Neu

> **Anmerkung**
>
> Bis Version 21.1: Administration → Online-Shops → Neu

- Getcore anklicken
- Erstellen eines ImportKey und ImportToken

### Schritt 2: Installation des Shop-Importers auf dem Magento-Server

- Kopieren des Ordner getcoreioimporter in Magento
- Erstellen der Konfigurationsdatei (Kopieren user.inc.php.tpl nach user.inc.php)
- Konfiguration der Pfadeinstellungen in der Datei user.inc.php
- ImportKey ein 32 Zeichen langen Schlüssel in der Datei user.inc.php hinterlegen
- ImportToken ein 6 Zeichen langen Schlüssel in der Datei user.inc.php hinterlegen

### Schritt 3: Verbindung von xentral zum Shop-Importer

- Einstellen der URL zum Shop-Importer (URL + Key + Token)
- Test der Verbindung (bei Export)

### Schritt 4: Datenabgleich

Damit der Webshop die Trackingdaten übernehmen kann, müssen diese von der Firma ZMB abgeholt werden. Dies geschieht durch das Anlegen eines FTP Benutzers, der auf die CSV Datei mit den Trackingdaten zugreifen kann.

Klicken Sie auf "Verbindung prüfen" und Sie sollten folgende Erfolgsnachricht erhalten:

![Getcore-3.png](https://help.xentral.com/hc/article_attachments/5102241337244)

### Pfade

Um korrekt funktionieren zu können, braucht der Importer zwei lokale Pfadangaben sowie eine URL:

- **CSVOrder**

- Dies ist der Pfad an dem die Bestelldaten zwischengespeichert werden bevor sie vom Importer ausgelesen werden. Dieser Pfad sollte vom Internet aus nicht erreichbar sein, da sonst jeder alle Bestelldaten herunterladen kann.
- **CSVTracking**

- Dies ist der Pfad an dem der Webshop die Trackingdaten ausliest. Dieser Pfad sollte vom Internet aus nicht erreichbar sein, da sonst jeder die Trackingdaten herunterladen kann.
- **CSVURL**

- Die URL ist die Adresse unter der die Bestelldaten heruntergeladen werden können. Man bekommt sie entweder vom Kunden, oder von ZMB selbst.