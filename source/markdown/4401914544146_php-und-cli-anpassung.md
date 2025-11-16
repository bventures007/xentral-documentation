> **Wichtig**
>
> **End-of-Life für On-Premise-Instanzen**
>
> Ende März 2023 beenden wir die Unterstützung von Xentral-Instanzen, die „On-Premise“ von unseren Kunden selbst gehostet werden. Wir empfehlen dir daher, deine Xentral-Instanz in unsere Cloud zu migrieren. Kontaktiere uns gerne jederzeit unteraccount@xentral.com, um diesbezügliche Fragen zu klären oder einen Termin für deine Migration zu buchen. Alternativ kannst du weitere Informationen aufunserer Websiteoder inunserer Communityfinden.
>
> Beachte bitte, dass wir Ende März 2023 jegliche Supportleistungen für On-Premise-Instanzen beenden. Wir stellen dann keine weiteren Bug-Fixes oder Updates mehr zur Verfügung. Außerdem wird es keine weitere Open-Source-Version mehr geben.

xentral ist eine serverseitige Software, d.h. sie läuft primär über einen Server und nicht über einen Client. Das Grundgerüst für Basisfunktionen bildet für xentral die Skriptsprache **PHP **, während die meisten Apps mit Cronjobs über die ** Command Line Input (CLI)**Sprache ablaufen.

PHP und CLI haben verschiedene Versionen und immer wieder neue Release Zyklen, um Bugs o.ä. zu beseitigen, weshalb du ab und an eine neue Version installieren musst. Zusätzlich wird noch Ioancube zur Verschlüsselung der Skriptdateien verwendet sowie der **Ioncube Loader**, um Schlüssel aufzurufen. Auf den Ioncube Loader musst du manchmal aktualisieren, da sonst unter Umständen xentral nicht geöffnet werden kann. Nach einem Update der PHP Version empfiehlt sich ein Serverneustart.

## Überprüfung der Versionen

Du kannst überprüfen, welche Versionen von PHP und CLI installiert sind. Das machst du in der App **Systemlog **. Navigiere dazu auf ** Administration > Einstellungen > System > Systemlog**oder nutze die Super-Search.

Die *PHP-Versionsnummer* findest du im Tab **PHP-Info**.

Die *CLI-Versionsnummer* findest du im Tab **PHP-Info (CLI)** an oberster Stelle.

Idealerweise solltest du PHP und CLI auf derselben Version halten. Neben der Versionsnummer sind im Systemlog auch weitere Informationen wie das Verzeichnis der Konfigurationsdatei (.ini) angegeben. Es wird hier immer die gleiche Datei aus dem angegebenen Verzeichnis ausgelesen, auch wenn du die PHP oder CLI Version aufgrund eines neuen Features aktualisierst. Möchtest du eine andere Konfigurationsdatei verwenden, so muss diese serverseitig ausgetauscht werden.

Unter **Systemlog > Aktualisieren > Systemlogs** kannst du z.B. sehen, welche Datei aktuell ausgelesen wird. Das kannst du für das Live-Debugging verwenden.

## Einlesen von Konfigurationsdateien

Beim Start von PHP wird die Konfigurationsdatei (php.ini) eingelesen. Dir stehen verschiedene Optionen zur Auswahl, um die Konfigurationsdatei einzulesen.

- **Option 1: ** Einlesen mit ** Umgebungsvariablen**. Ein Pfad, aus dem die Konfigurationsdatei eingelesen werden kann, könnte so aussehen:

```PHPRC=/home/USER/etc/php72/php.ini /usr/local/bin/php -f /home/USER/www/ERP/cronjobs/starter2.php```

- **Option 2: ** Einlesen zusätzlicher Pfade über ** Direktiven**.
- **Option 3: ** Arbeiten mit einer **.htaccess Datei**: Solche Dateien werden primär bei der Webserverkonfiguration genutzt. Du kannst hier vorgeben, welche Benutzer standardmäßig in welchem Verzeichnis aufgerufen werden. Zudem kannst du blockieren, dass ein alter Pfad ausgelesen wird.
- **Option 4: ** Eine weitere Möglichkeit ist es, zunächst eine ** neue Version** von PHP zu installieren, um anschließend die alte Version zu deinstallieren.

> **Anmerkung**
>
> Oft wird die PHP-Version über die AppSystem Healthausgelesen. Diese wird allerdings über den gleichnamigen Prozessstarter System Health aktualisiert, weshalb nach einem Update hier nicht direkt die neuste Version angezeigt wird, sondern erst, nachdem der Prozessstarter einmal gelaufen ist.

Informationen zu den Systemvoraussetzungen für die Installation bei Webhosting-Anbietern findest du[hier](https://help.xentral.com/document/preview/13955#UUID-515f84e5-d62e-7591-21b4-2ff95951a2d0).