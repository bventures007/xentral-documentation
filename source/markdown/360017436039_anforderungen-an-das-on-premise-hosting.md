> **Wichtig**
>
> **End-of-Life für On-Premise-Instanzen**
>
> Ende März 2023 beenden wir die Unterstützung von Xentral-Instanzen, die „On-Premise“ von unseren Kunden selbst gehostet werden. Wir empfehlen dir daher, deine Xentral-Instanz in unsere Cloud zu migrieren. Kontaktiere uns gerne jederzeit unteraccount@xentral.com, um diesbezügliche Fragen zu klären oder einen Termin für deine Migration zu buchen. Alternativ kannst du weitere Informationen aufunserer Websiteoder inunserer Communityfinden.
>
> Beachte bitte, dass wir Ende März 2023 jegliche Supportleistungen für On-Premise-Instanzen beenden. Wir stellen dann keine weiteren Bug-Fixes oder Updates mehr zur Verfügung. Außerdem wird es keine weitere Open-Source-Version mehr geben.

Dieser Artikel beschreibt die Hardware- und Software-Anforderungen für das Hosting von XentralOn-Premise sowie die erforderliche Konfiguration auf dem Server. Hier werden auch die Anforderungen beschrieben, die erforderlich sind, um Support für deine On-Premise gehostete Xentral-Instanz zu erhalten. Sollten diese Anforderungen nicht erfüllt sein, läuftXentral unter Umständen nicht richtig und wir bieten keine Unterstützung.

> **Tipp**
>
> Xentral bietet Neukunden nur Cloud-Hosting an und möchte Altkunden motivieren, in die Xentral-Cloud zu migrieren.

## Hardware-Anforderungen

Mindestanforderung an deinen Server:

- 8 CPU-Kerne
- 16 GB Arbeitsspeicher (RAM)
- 500 GB verfügbarer SSD-Festplattenspeicher

Sind diese Anforderungen nicht erfüllt, kann das zu Leistungsproblemen deiner Xentral-Instanz führen.

## Software-Anforderungen

Zur Sicherstellung, dass deine Xentral-Instanz korrekt eingerichtet und ausgeführt werden kann, müssen die folgenden Software-Anforderungen erfüllt werden.

### Betriebssystem

Auf deinem Server ist eine der folgenden Linux-Distributionen als Betriebssystem erforderlich:

- Ubuntu
  - 64-Bit
  - Version 18.04 oder höher (`>=18.04`)
- Debian
  - 64-Bit
  - Version 10.3 oder höher (`>=10.3`)

> **Wichtig**
>
> Du musst SSH-Zugriff auf dein Betriebssystem haben, um die erforderlichen Cronjobs einrichten zu können.

### PHP

Du musst PHP-FPM und PHP-CLI auf deinem Server mit der folgenden Version, Konfiguration und den folgenden Erweiterungen installieren.

| Version | PHP 7.4 oder höher (PHP^7.4), aber noch nicht 8.0 |
| --- | --- |
| **Konfiguration** | Stelle sicher, dass die folgenden `php.ini `-Werte definiert sind: -` max_execution_time = 600 `Wert in Sekunden, d.h. 600 entspricht 10 Minuten.<br>-` max_input_time = 1000 `Wert in Sekunden, d.h. 1000 entspricht ungefähr einer Viertelstunde.<br>-` memory_limit = 512M` |
| **Erweiterungen**| Die nachfolgend beschriebenen PHP-Erweiterungen sind erforderlich, wobei "*" bedeutet, dass jede Version verwendet werden kann und z.B. ">=10.4" bedeutet, dass Version 10.4 oder höher erforderlich ist: |

### Webserver

Wir unterstützen offiziell nur den folgenden Webserver:

- Nginx Version 1.18 oder höher (`>=1.18`)

### Datenbank

Wir unterstützen offiziell nur die folgende Datenbank:

- MySQL 5.7

> **Warnung**
>
> MySQL 8.0 wird **nicht** unterstützt.

Einige andere Datenbank-Systeme können funktionieren, ein Funktionieren wird von uns aber nicht garantiert und eine Nutzung solcher Systeme kann die Support-Dienstleistungen, die wir unterstützen, beeinflussen, siehe[Support-Anforderungen](#UUID-dc5a1e39-8c4d-6bef-619f-f6bec2725cac_section-idm467254917197763323003201353)

## Anforderungen an die Konfiguration

Stelle sicher, dass du dich bei Einrichtung deines Xentral-Systems an die folgenden Konfigurationsanforderungen hältst.

### Dokumentenstamm

Der Dokumentenstamm des Webservers muss auf die Ordner `www` des Xentral-Repositories verweisen.```
server {
2 location / {
3 #...
4 root /xentral/www
5 #...
6} 
7}
```

### SSL-Zertifikat

Der Server muss über ein gültiges SSL-Zertifikat verfügen, um die Kommunikation mit dem Xentral-System zu ermöglichen.

Du kannst gratis SSL-Zertifikate über[Let's Encrypt](https://letsencrypt.org/)erhalten.

## Support-Anforderungen

Bitte beachte, dass unsere Support-Dienstleistungen fürXentral-Systeme, die On-Premise gehostet werden, an spezielle Bedingungen geknüpft sind.

### Prüfung der Hosting-Anforderungen

Stelle sicher, dass du die tatsächliche Systemkonfiguration mit der aktuellen Hardware, Software und Konfigurationsanforderungen dieses Artikels vergleichst, bevor du den Xentral-Support kontaktierst.

Sollte es Abweichungen geben, nenne diese bitte zu Beginn deiner Support-Anfrage.

Bitte beachte, dass wir für abweichende Systeme und Konfigurationen unter Umständen keinen Support leisten können.

> **Warnung**
>
> Hast es du unterlassen, uns in deinem Support-Ticket über ein abweichendes Set-up zu unterrichten und dies führt zu einem Mehraufwand bei der Prüfung auf unserer Seite, können wir dir diesen Mehraufwand in Rechnung stellen.

### Zugriff auf dein On-Premise-System

Um dir Support anbieten zu können, brauchen wir Zugriff auf dein Xentral-System und den Server, auf dem es gehostet wird.

Stelle bitte Folgendes sicher:

- Du hast einen Support-Benutzer mit Admin-Rechten auf deiner Xentral-Instanz eingerichtet und stellst diesen dem Xentral-Support-Team zur Verfügung.
- Du hast SSH-Zugriff auf deinem Server mit `sudo`-Berechtigungen eingerichtet und stellst diesen dem Xentral-Support-Team zur Verfügung.