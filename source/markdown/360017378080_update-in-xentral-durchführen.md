Die Lizenz und der Schlüssel können direkt in Xentral unter folgendem Menüpunkt eingegeben werden: **Administration > Einstellungen > System > Grundeinstellungen > Lizenz**. Die Open-Source- oder Free-Version kann später jederzeit zu einer kommerziellen Professional- oder Enterprise-Version geupgradet werden, ohne das System neu installieren zu müssen.

> **Anmerkung**
>
> Damit ein Upgrade auf eine höhere Version aktiviert wird, muss noch ein Update gemacht werden (siehe nächster Punkt). Es ist sicherzustellen, dass der Schlüssel ohne Zeilenumbrüche oder Leerzeichen eingetragen wird. (Andernfalls erscheint beim Update eine Fehlermeldung, die auf ungültige Zeichen bei der Lizenz, bzw. beim Schlüssel hinweist)

> **Wichtig**
>
> Ein Update kann nicht mehr rückgängig gemacht werden, d.h. nach einem Update ist kein Downgrading auf ältereXentral-Versionen möglich.

## Rechte prüfen

Die Zugriffsrechte der Dateien müssen so gesetzt sein, dass der Webserver auf die Dateien zugreifen und ändern darf. Oftmals läuft der Webserver zum Beispiel unter dem Benutzer "www-data". In diesem Fall müssen die Dateien vom Benutzer "www-data" geändert werden dürfen.

## Update durchführen

### Update innerhalb einer Version durchführen

Es kann über die Oberfläche ein Update gestartet werden. Auf der Startseite befindet sich rechts unten ein Link zur Update-Ansicht. Ab der Version 22.1.18 zeigen wir die Update-Schaltfläche auf der Startseite nur noch an, wenn tatsächlich ein neues Update verfügbar ist. Wenn nicht, wird er ausgeblendet. Wenn ein Kunde ein Update innerhalb der selben Version benötigt, so wird dies von uns über url.com/update.php vorgeschlagen.

![Update-2.png](https://help.xentral.com/hc/article_attachments/4996380250140)

Um ein Update durchzuführen, ist wie folgt vorzugehen:

1. 1. Das Update ist über die Update Schaltfläche zu starten.
1. 2. Es ist zu warten, bis der Balken vollständig durchgelaufen sind. Dies kann einige Minuten dauern.
1. 3. Es ist über die Schaltfläche **Zurück zu** Xentral zurückzukehren.

### Fehlermeldung nach Update

Wenn ein Update nicht funktioniert oder eine Fehlermeldung erhalten wird, kann zunächst immer folgendes probiert werden:

Erneutes Update über folgenden URL Aufruf ziehen: https://MEINXENTRAL.xentral.biz/update.php (MEINXENTRAL → eure xentral URL)

### Update auf eine höhere Version

Sobald eine höhere Version freigeschaltet wurde, erscheint ein Drop-Down neben der "Updaten"-Schaltfläche

![mceclip0.png](https://help.xentral.com/hc/article_attachments/4996329608092)

Im Drop-Down kann die höhere Version ausgewählt und das Update gestartet werden.

> **Wichtig**
>
> Es sollte ein Versionsupgrade (Update auf eine höhere Version) nicht im laufenden Betrieb gemacht werden, sondern zu einem geeigneten Zeitpunkt, z.B. abends oder am Wochenende.

Eine höhere Version kann unter Umständen bereits vor dem offiziellen Release freigeschaltet werden. Infos dazu sind im Bereich[Beta Programm](#)zu finden.

### Update über die Kommandozeile - Nur bis Version 17.4

Im Datei-Ordner von Xentral befinden sich die Dateien "upgradesystemclient2.php" und "upgradedbonly.php". Diese sind wie folgt auf der Kommandozeile auszuführen.

> **Wichtig**
>
> Diese Befehle sollten nur als Benutzer des Webservers ausgeführt werden oder, wenn es nicht anders geht, als root user. Dann sind bei den Dateien die Rechte des Webservers anzugeben (ganz wichtig, dass die Dateien dem Webserver gehören, sonst kann es zu massiven Problemen kommen). Den Benutzernamen vom Webserver müssen entsprechend herausgefunden werden. Z.B. unter einem Linuxsystem können sich mit "ps axu" alle Prozesse auflisten lassen, die laufen. In der Liste befindet sich auch der Webserver als Eintrag (z.B. apache oder nginx).

1. Kommandozeile öffnen - sich auf den Server verbinden - den xentralordner ansteuern cd /var/www/html/wawision
1. Systemupdate starten php upgradesystemclient2.php oder php5 upgradesystemclient2.php
1. Datenbankupdate starten php upgradedbonly.php oder php5 upgradedbonly.php