> **Wichtig**
>
> **End-of-Life für On-Premise-Instanzen**
>
> Ende März 2023 beenden wir die Unterstützung von Xentral-Instanzen, die „On-Premise“ von unseren Kunden selbst gehostet werden. Wir empfehlen dir daher, deine Xentral-Instanz in unsere Cloud zu migrieren. Kontaktiere uns gerne jederzeit unteraccount@xentral.com, um diesbezügliche Fragen zu klären oder einen Termin für deine Migration zu buchen. Alternativ kannst du weitere Informationen aufunserer Websiteoder inunserer Communityfinden.
>
> Beachte bitte, dass wir Ende März 2023 jegliche Supportleistungen für On-Premise-Instanzen beenden. Wir stellen dann keine weiteren Bug-Fixes oder Updates mehr zur Verfügung. Außerdem wird es keine weitere Open-Source-Version mehr geben.

## xentral 19.1 Installer herunterladen

Im ersten Schritt ist der xentral 19.1 Installer aus Github herunterzuladen: Xentral Installer (Open-Source Version / PHP Quelltext).

Die Downloaddatei findet sich unter der Sparte "README.md" im unteren Bereich der Seite.

![Installation-1.png](https://help.xentral.com/hc/article_attachments/4996354447132)

1. Die "installer.zip" ist zu entpacken → installer.php
1. Die Datei "installer.php" ist auf den Webspace hochzuladen und im Browser aufzurufen, z.B.: Deine_Domain.de/installer.php
1. Es ist zu kontrollieren, ob alle benötigten Komponenten auf dem Webserver installiert sind:
1. Die Zugangsdaten zur Datenbank sind einzutragen:
1. Der Pfad für das Dateiverzeichnis ist zu bestätigen (Unter Userdata legt xentral die erzeugten PDF's und Dateien ab):
1. Jetzt können zu Testzwecken Demodaten installiert werden:

Das Setup bzw. die Installation von xentral ist jetzt abgeschlossen.

## Aufruf des Cronjobs

Im Folgenden wird beschrieben, wie der Cronjob aufgerufen werden kann. Zunächst ist die Einrichtung eines Cronjobs für xentral empfehlenswert.

Danach kann dieser aufgerufen werden:

![Installation-7.png](https://help.xentral.com/hc/article_attachments/4996360965276)

Dann ist die Anmeldung in xentral mit dem Benutzernamen "admin" und dem Passwort "admin" möglich.

![Installation-8.png](https://help.xentral.com/hc/article_attachments/4996310103708)

### Einrichtung des Heartbeat-Cronjobs

Die Einrichtung eines Heartbeat-Cronjobs für xentral wird generell empfohlen.

> **Anmerkung**
>
> Folgende Schritte sind nur auszuführen, wenn ausreichend fachliche Kenntnisse vorhanden sind.

Um in xentral Prozesse automatisieren zu können, wird ein sog. Heartbeat-Cronjob benötigt. Dieser dient als Taktgeber für den integrierten Prozessstarter. Dieser Heartbeat-Cronjob kann beispielsweise für folgendes verwendet werden:

- Das automatische Abholen von E-Mails
- Das Archivieren von PDF-Dokumenten zur Datensicherung
- Die Übertragung von Lagerzahlen an Online-Shops
- Andere automatische Prozesse, die regelmäßig laufen müssen

Der Cronjob muss mit einem Benutzer ausgeführt werden, der auf den Ordner „userdata“ zugreifen darf. Zusätzlich muss der Webserver Dateien bearbeiten können, die von diesem Cronjob erstellt wurden.

Als Zeitintervall für die Ausführung des Cronjobs vom Server ist eine Minute bzw. minütlich anzugeben:

sudo crontab -e -u www-data

und dann diese Zeile:

* * * * * php /var/www/html/cronjobs/starter2.php

Danach ist die Einrichtung des Cronjobs abgeschlossen.

Informationen zur Einrichtung von automatischen Prozessen in xentral sind[hier](#)zu finden.