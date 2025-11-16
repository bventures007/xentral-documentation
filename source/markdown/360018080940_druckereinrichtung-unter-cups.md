> **Anmerkung**
>
> Diese Einrichtung wird von Xentral nicht supportet.

Wie Sie Drucker generell an Xentral anschließen können erfahren Sie im Drucker Schnelleinstieg.

## Installation bzw. Aktivierung von CUPS

### Weboberfläche für CUPS unter macOS aktivieren

Aktivieren lässt sich das Interface mit folgender Eingabe im Terminal:

cupsctl WebInterface=yes

Deaktivieren:

cupsctl WebInterface=no

Quelle und weitere Dokumentation: https://www.cups.org/

### CUPS unter Linux Debian bzw. Ubuntu installieren

Sollte CUPS unter Linux nicht vorhanden sein (Server-Version), können Sie dies mit diesen Befehlen installieren:

Server/Client Komponenten:

sudo apt-get install cups cups-client cups-bsd

Druckertreiber Bibliotheken:

sudo apt-get install hplip hpijs printer-driver-gutenprint

### Weboberfläche für CUPS unter Linux aktivieren

Aktivieren lässt sich die Weboberfläche und die Freigabe der Netzwerkdrucker mit folgender Eingabe im Terminal:

sudo cupsctl --share-printers --remote-admin

Jetzt müssen Sie den Dienst neu starten:

systemctl restart cups

Quelle und weitere Informationen zu CUPS unter Linux:[https://wiki.ubuntuusers.de/CUPS/](https://wiki.ubuntuusers.de/CUPS/)

## Arbeiten mit CUPS

Öffnen sie einen Webbrowser und rufen Sie CUPS auf. Der Aufruf erfolgt im unseren Beispiel lokal auf dem System, in welchem CUPS installiert ist: https://127.0.0.1:631**

Sollten Sie nach Benutzernamen und Passwort gefragt werden, geben Sie diesen entsprechend ein (den Benutzernamen findet man über die Kommandozeile heraus).

### Dokumentendrucker anlegen

Um einen neuen Drucker anzulegen, gehen Sie auf Administration und dann auf → Add Printer:

Im Beispiel installieren wir den "Brother MFC-7440N (Brother MFC-7440N)". Markieren Sie den Drucker und klicken Sie auf Continue:

![drucker-cups_3.png](https://help.xentral.com/hc/article_attachments/4996407937820)

Vergeben Sie den Drucker eine eindeutige Bezeichnung:

![drucker-cups_4.png](https://help.xentral.com/hc/article_attachments/4996369791260)

Wählen Sie den passenden Treiber aus:

![drucker-cups_5.png](https://help.xentral.com/hc/article_attachments/4996404318620)

Im letzten Schritt können Sie noch zusätzliche Einstellungen am Drucker vornehmen:

![drucker-cups_6.png](https://help.xentral.com/hc/article_attachments/4996408094876)

Im Bereich Printers können Sie den angelegten Drucker jetzt sehen und verwalten:

![drucker-cups_7.png](https://help.xentral.com/hc/article_attachments/4996369888284)

#### Eine bestimmte Papierzufuhr ansprechen

Um eine bestimmte Papierzufuhr bzw. Papierkassette anzusprechen, müssen Sie diesen Drucker einfach nochmals neu anlegen und entsprechend auch neu bezeichnen. Gehen Sie in der Einrichtung genau so vor wie im Punkt "Dokumentendrucker anlegen" beschrieben und passen Sie die Druckereinstellungen entsprechend an.

Beispiel für die Bezeichnung:

![drucker-cups_8.png](https://help.xentral.com/hc/article_attachments/4996431897756)

Beispiel für eine manuelle Papierzufuhr um A5 Versandlabel zu drucken:

![drucker-cups_9.png](https://help.xentral.com/hc/article_attachments/4996369943452)

Ergebnis in der Printer Übersicht:

![drucker-cups_10.png](https://help.xentral.com/hc/article_attachments/4996369966364)

### Versandlabel Drucker anlegen

Generell müssen ZEBRA Versandlabel Drucker immer über CUPS angelegt bzw. konfiguriert werden. Die Konfiguration über die Standard Druckerverwaltung in macOS bzw. Linux führt in 99% der Fälle nicht zum gewünschten Ergebnis.

Beispiel für: ZEBRA GK420t

Öffnen sie einen Webbrowser und rufen Sie CUPS auf. Der Aufruf erfolgt im unseren Beispiel lokal auf dem System wo CUPS installiert ist.

{wikilink https://127.0.0.1:631 **{{:entwickler:cups_01.jpg?nolink}} |https://127.0.0.1:631** {{:entwickler:cups_01.jpg?nolink}}}

Um einen neuen Drucker anzulegen, gehen Sie auf Administration und dann auf → Add Printer:

Im Beispiel installieren wir den "Zebra Technologies ZTC GK420t Labeldrucker“. Markieren Sie den Drucker und klicken Sie auf Continue:

![drucker-cups_12.png](https://help.xentral.com/hc/article_attachments/4996404516380)

Vergeben Sie eine eindeutige Bezeichnung für den Drucker:

![drucker-cups_13.png](https://help.xentral.com/hc/article_attachments/4996370000924)

Wählen Sie den passenden Treiber aus, als Model markieren Sie bitte "Zebra ZPL Label Printer":

![drucker-cups_14.png](https://help.xentral.com/hc/article_attachments/4996393421212)

Jetzt müssen Sie noch das Papierformat für das Versandlabel einstellen. Klicken Sie hier auf die Mediengröße und stellen Sie diese auf Custom um, beachten Sie bitte auch die Umstellung der Einheiten auf mm:

![drucker-cups_15.png](https://help.xentral.com/hc/article_attachments/4996432009628)

Tragen Sie jetzt die Breite und Höhe für das von Ihnen verwendete Versandlabel ein. Für DHL-Versandlabels tragen Sie bitte 100 für die Breite ein und 200 für die Höhe ein:

![drucker-cups_16.png](https://help.xentral.com/hc/article_attachments/4996408443420)

Papierformate:

- DHL: B:100mm x H:200mm → Bitte auch entsprechend unter https://www.dhl-geschaeftskundenportal.de das Labelformat auswählen.
- UPS, DPD: B:100mm x H:150mm

Nachdem der Versandlabel Drucker eingerichtet wurde, können Sie unter Maintenance eine Testseite drucken → "Print Test Page":

![drucker-cups_17.png](https://help.xentral.com/hc/article_attachments/4996449546396)

Damit ist die Einrichtung der Drucker unter CUPS abgeschlossen. Die Anbindung an Xentral erfolgt hier: Drucker in Xentral