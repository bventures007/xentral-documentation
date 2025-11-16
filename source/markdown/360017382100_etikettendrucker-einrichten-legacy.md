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
> Der Etikettendrucker kann, wie ein Dokumentendrucker, ohne Adapterbox über den Druckerspooler an Xentral angeschlossen werden. Die Anbindung wird in diesem Artikel beschrieben:Deinen Drucker mit Xentral verbinden.

Diese Anleitung zeigt Schritt für Schritt die Einrichtung eines Etikettendruckers, der über eine Adapterbox an xentral angebunden wird. Für die Einrichtung werden folgende Dinge benötigt:

- Etikettendrucker Zebra GK420t, inkl. Netzgerät (Link zum Shop)
- Raspberry PI (im Folgenden Adapterbox genannt) konifiguriert laut Anleitung.
- USB-Kabel zum Anschluss des Druckers an die Adapterbox
- Netzwerkkabel (oder WLAN-USB-Stick bei Drahtloser Netzwerkanbindung) zur Anbindung der Adapterbox an das Netzwerk
- USB-Stick (leer, FAT formatiert)
- Etiketten
- Thermofolie, passend für Zebra GK420t

Etiketten Drucker sind auch mit dem xentral Spooler anbindbar, dann wird vorzugsweise ein netzwerkfähigen Etikettendrucker verwendet.

## Schritt 1: Entpacken und Überprüfen auf Vollständigkeit

Der Etikettendrucker ist zu entpacken und es ist sicherzustellen, dass alle Teile vorhanden und unbeschädigt sind. Für die Durchführung der ersten 5 Schritte dieser Anleitung ist die Adapterbox noch nicht notwendig.

## Schritt 2: Einlegen der Thermofolie

- Der Deckel des Etikettendruckers ist zu öffnen, indem die seitlich angebrachten grünen Verriegelungen in Richtung der Gerätevorderseite aufgedrückt werden.
- Die Thermofolie ist zu entpacken und die mitgelieferte Papprolle zur Hand abzulösen.
- Der Anfang der Thermofolie ist von der Rolle zu lösen und auf die Papprolle zu wickeln - zwei bis drei Wicklungen genügen. Die Papprolle dient als Träger zum Aufwickeln der verbrauchten Thermofolie während des Druckens (im folgenden auch Leer-Rolle).
- Die beiden Rollen im Deckel des Etikettendruckers sind in die vorgesehenen Halter einzulegen. Zu beachten ist, dass die volle Rolle von unten her eingelegt wird, und die Leer-Rolle von oben her (siehe Fotos). Zum Einlegen sind die Papprollen gegen die gefederten konischen Naben zu drücken und in der gegenüberliegenden Nabe einzurasten.
- Wenn beide Rollen eingelegt sind, ist der korrekte Sitz zu prüfen, indem mit Hilfe des grünen Rades neben der Leer-Rolle ein bis zwei Wicklungen aufgedreht werden.

![ZEBRA1.png](https://help.xentral.com/hc/article_attachments/4996393589916)

![ZEBRA-2.png](https://help.xentral.com/hc/article_attachments/4996408554908)

![ZEBRA-3.png](https://help.xentral.com/hc/article_attachments/4996449654812)

![ZEBRA-4.png](https://help.xentral.com/hc/article_attachments/4996404809116)

## Schritt 3: Einlegen der Etiketten

Die Etiketten-Rolle ist zur Hand zu nehmen und, wie auf der Abbildung zu sehen, in das Unterteil des Etikettendruckers einzulegen. Die Rolle wird zwischen den beiden grünen Naben durch Federdruck gehalten. Der Rollen Anfang ist, wie abgebildet zum Ausgabe-Schlitz des Geräts, einzuführen. Danach ist der Deckel des Druckers zu schließen.

![ZEBRA-5.png](https://help.xentral.com/hc/article_attachments/4996449691292)

![ZEBRA-6.png](https://help.xentral.com/hc/article_attachments/4996393777180)

## Schritt 4: Automatische Kalibrierung des Druckbereichs

Der Etikettendrucker muss sich auf die Etikettengröße kalibrieren. Die Kalibrierung muss jedes mal nach dem Einlegen einer Etikettenrolle durchgeführt werden! Um die Kalibrierung durchzuführen sind diese Schritte zu befolgen:

- ggf. den Deckel des Druckers schließen
- Die Stromversorgung des Geräts herstellen und den Netzschalter auf der Geräterückseite unten links betätigen
- Die Taste auf der Gehäuseoberseite des Etikettendruckers ist zu drücken und zu halten, bis die LED neben der Taste 2 Mal (4 Mal blinken → Drucker wird auf die Werkseinstellungen zurückgesetzt.) hintereinander blinkt. Dann ist die Taste loszulassen – der Drucker kalibriert sich nun auf die Größe der eingelegten Etiketten.

> **Anmerkung**
>
> Beim Halten der Taste blinkt die LED zunächst einmal, nach einer kurzen Pause zweimal, dann dreimal und so weiter...

![ZEBRA-7.png](https://help.xentral.com/hc/article_attachments/4996449729564)

## Schritt 5: Kalibrierung der Druckintensität

Die Druckintensität sollte so konfiguriert werden, dass die Etiketten, insbesondere auch für Barcode-Scanner, gut lesbar sind. Die Taste auf der Gehäuseoberseite des Etikettendruckers ist zu drücke und zu halten, bis die LED neben der Taste 6 Mal hintereinander blinkt. Dann ist sofort die Taste loszulassen. Das Gerät beginnt darauf hin mehrere Testausdrucke auszugeben, wobei die Druckintensität schrittweise erhöht wird. Sobald das Druckbild sauber und gut lesbar ist, die Taste auf der Gehäuseoberseite einmal kurz drücken, um die Einstellung zu bestätigen.

![ZEBRA-8.png](https://help.xentral.com/hc/article_attachments/4996404887452)

## Schritt 6: Einrichtung der Adapterbox

Um die Verbindung von xentral mit dem externen Gerät (Etikettendrucker, Waage, Bondrucker, Kassendisplays etc.) herzustellen, benötigt es einen kleinen "Zwischen-Server" (Adapterbox), den man käuflich erwerben kann. Lösungen hierfür findest du bei unserem Partner Ruhr Agency.

Aus technischen Gründen ist dazu derzeit ein Raspberry Pi bis max. Version 3B notwendig

### Adapterbox konfigurieren

Sobald die Adapterbox erworben wurde, kann diese mit folgenden Schritten konfiguriert werden:

1. Die Adapterbox ist an einen Monitor sowie an Tastatur und Maus anzuschließen. Außerdem ist sicherzustellen, dass eine Internetverbindung besteht.
1. Das Betriebssystem ist zu installieren und den darauffolgenden Hinweis mit OK zu bestätigen.
1. Es ist auf LX Terminal (Taskleiste dunkles Icon) zu gehen und folgende Befehle einzugeben. Dann sind diese jeweils mit der ENTER Taste zu bestätigen.

```
sudo apt-get --yes install libcurl3 php7.0-curl php7.0-cli php7.0-xml
sudo usermod -a -G lpadmin pi
sudo systemctl enable ssh
wget http://www.wawision.de/adapterbox.deb 
sudo dpkg -i adapterbox.deb
echo "Seriennummer eingeben gefolgt von einem [ENTER]:"
read seriennummer
echo "<?php \$config['serial'] = '$seriennummer';?>" > /tmp/config.php
sudo mv /tmp/config.php /root/config.php
sudo halt

```

Die echo-Befehle dienen mit Ausnahme des letzten Aufrufs nur der Anschaulichkeit.

> **Wichtig**
>
> Die Debian-Datei (deb-Datei) für den wget-Befehl können Sie imGitHub-Downloadverzeichnisherunterladen.

Wenn die Ausführung des Skripts nicht funktionieren sollte, muss ggf. noch die PHP-Version mit dazugehörigen Extensions installiert und aktiviert werden.

**Installation php **```sudo apt -y install php php-common```** Installation PHP-Extension**```sudo apt -y install php-cli php-fpm php-json php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath```

Es ist zu warten, bis die Aufforderung kommt eine Seriennummer einzugeben. Es ist eine 9-stellige Nummer einzugeben und zu bestätigen mit der ENTER Taste - diese Seriennummer wird dann später in xentral gebraucht. Die Box schaltet sich danach automatisch aus. Danach ist die Adapterbox konfiguriert und es kann mit dem nächsten Schritt fortgefahren werden.

> **Anmerkung**
>
> Sollte dein Drucker nicht drucken, dann stelle den Treiber von cpcl auf zpl (Zebra zb 230) um. Weitere Informationen findest du auf diesen Seiten:
>
> - https://supportcommunity.zebra.com/s/article/CPCL-Manual-for-Zebra-Mobile-Printers?language=de
> - https://supportcommunity.zebra.com/s/article/ZPL-Command-Information-and-DetailsV2?language=de

## Schritt 7: Einrichtung in xentral

Um die Einrichtung des Etikettendruckers fortzuführen, ist mit der Adapterbox an einen Computerarbeitsplatz zu gehen und sich mit einem Account mit ausreichenden Rechten in xentral anzumelden. In der Ansicht Administration → Einstellungen → System sind die ‚Grundeinstellungen’ zu öffnen

Der Reiter 'API’s' ist zu öffnen und die markierte Option zu auszuwählen. Dann ist auf „Key generieren“ zu klicken und zu speichern.

In der Ansicht Administration → Einstellungen → System ist der Punkt ‚Adapterbox’ zu öffnen.

In der Adapterbox-Ansicht ist,NEU' auszuwählen. Danach wird von xentral in 3 Schritten durch die Einrichtung geführt.

Zunächst können, falls nötig, die Netzwerkeinstellungen manuell festgelegt werden. Sollten hier Änderungen vorgenommen werden, sind diese zu speichern. Um zum nächsten Schritt zu gelangen, ist auf 'weiter mit Schritt 2' zu klicken.

> **Anmerkung**
>
> xentral empfiehlt den Betrieb über ein Netzwerkkabel, da es so am besten und stabilsten läuft. Betrieb über WLAN ist prinzipiell möglich, wird aber von xentral nicht supported, da dies eher fehleranfällig ist und die möglichen Probleme vor allem in den Netzwerkeinstellungen zu finden sind.

Für diesen Schritt stellt xentral eine Liste von durchzuführenden Aktionen bereit. Diese Liste ist in der vorgegebenen Reihenfolge sorgfältig abzuarbeiten. Dann wird der FAT-formatierten USB-Stick benötigt.

Wenn Sie die Liste abgearbeitet haben. Nehmen Sie die vom Drucker ausgegebene Etikette mit zurück zu Ihrem Computerarbeitsplatz und Klicken Sie in xentral auf 'weiter mit Schritt 3'.

![ZEBRA-17.png](https://help.xentral.com/hc/article_attachments/4996404910492)

Vergeben Sie nun einen Namen für den gerade eingerichteten Etikettendrucker und geben Sie die Seriennummer ein, die Ihr Drucker im vorigen Schritt auf die Etikette gedruckt hat (dritte Zeile auf dem Etikett in der Abbildung oben).

In der Ansicht Administration → Einstellungen → System ist der Punkt 'Drucker' zu öffnen.

In der Liste erscheint nun der eingerichtete Etikettendrucker. Es ist auf das Bearbeiten-Symbol zu klicken, um Einstellungen für den Drucker vorzunehmen.

Als Geräteart ist 'Etikettendrucker' einzustellen. Bei Format ist die Größe der Etiketten einzustellen, die in den Drucker eingelegt wurden. Die Anbindungsart muss noch auf 'Adapterbox' eingestellt werden.

Nun ist sicherzustellen, dass die USB-Verbindung zwischen Drucker und Adapterbox sowie die Netzwerkverbindung der Adapterbox hergestellt ist. Die Geräte sind mit Spannung zu versorgen und der Drucker einzuschalten, um im Folgenden den Drucker zu testen.

![ZEBRA-21.png](https://help.xentral.com/hc/article_attachments/4996408861084)

Jetzt ist ein Testdruck durchzuführen, um zu prüfen ob die Einbindung des Druckers korrekt funktioniert hat. Dazu ist in xentral die Ansicht Lager & Logistik → Etikettendrucker zu öffnen. Im obersten Textfeld ist ein beliebiger kurzer Text anzugeben und auf 'Drucken' zu klicken. Wenn der eingegebene Text vom Etikettendrucker gedruckt wird, war die Einrichtung erfolgreich.

> **Anmerkung**
>
> Bis Version 21.1 unter Verwaltung → Etikettendrucker.

Die Erstellung von Etiketten-Layouts ist hier beschrieben.

## PDF-Etikettendrucker einrichten

Etiketten können einzeln auch direkt als PDF ausgegeben werden. Der Abruf der Etiketten erfolgt über den Spooler (direkt in den Druckereinstellungen) Oder das PDF kann an eine E-Mail-Adresse gesendet werden Die Art der Anbindung kann direkt ausgewählt werden:

### PDF in Verzeichnis

Anbindung über Kommandozeilenbefehl/PDF in Verzeichnis:

- Verzeichnis → das Verzeichnis angeben (z.B. kann bei Linux /tmp/ verwendet werden)

### PDF als E-Mail

Bei der Anbindung an eine E-Mail Adresse noch folgende Felder ausfüllen:

- E-Mail Drucker Empfänger → E-Mail Adresse, an die das PDF gesendet wird
- E-Mail Drucker Betreff → Betreff, den diese o.g. E-Mail erhält
- E-Mail Drucker Text → Zusatztext, der in der o.g. E-Mail mit übermittelt wird:entwickler:etikettendrucker_email.png

### Etikettenerstellung für PDF-Etiketten

Die Etiketten können ebenso als XML erstellt werden. Einziger Unterschied zum Drucker ist, dass die Etikettengrößen nicht fest vorgegeben sind und beliebig eingestellt werden können. Einstellung der beliebigen Größe direkt im Etikettengenerator::entwickler:etikettendrucker_anbindung_einstellung.png

### Versandlabel-Etikettendrucker einrichten

Ein Etikettendrucker kann auch für Versandlabels verwendet werden. Dieser ist im Logistikprozess für die Paketmarkenlabels auszuwählen. Im Drucker selbst sind folgende Einstellungen vorzunehmen (Anbindung per Kommandozeilenbefehl):

- Geräteart → Drucker (Etikettendrucker wird nur in Verbindung mit den xentral Etiketten verwendet)
- Format → DinA5
- Anbindung → Kommandozeilenbefehl
- Befehl oder Verzeichnis → lpr -o fit-to-page -o media=A6 -H 192.168.0.XXX -P ZebraGC420d
- Seriennummer → bitte tragen Sie hier Ihre Seriennummer ein (für den Spooler entsprechend die Seriennummer für die Niederlassung)

lpr -o fit-to-page -o media=A6 -H 192.168.0.XXX -P ZebraGC420d

> **Anmerkung**
>
> Die fettgedruckten Bereiche (s.o.) müssen durch eigene Bezeichnungen ersetzt werden:entwickler:kurzanleitung_etikettendrucker_versandlabels.png

### Benutzerdefiniertes Etiketten Label-Format einrichten

Um ein benutzerdefiniertes Etiketten Label-Format einzurichten, ist zuerst in die Einstellungen des Labeldruckers unter xentral zu gehen. Dies ist zu finden unter → Administration → Einstellungen → Drucker → “Ihren Labeldrucker auswählen“. Das Format ist auf “leer“ umzustellen.

Im nächsten Schritt muss der CUPS-Server auf den Linux-Druckerserver aufgerufen werden. Hierzu ist folgende Adresse im Webbrowser einzutragen:127.0.0.1:631

## Druckerempfehlung

Wir unterstützen gängige Etikettendrucker von Zebra. Hierbei bitte darauf achten, dass es sich um einen Netzwerkdrucker via LAN/WLAN handelt, und nicht via USB.