# Hilfestellung bei Lizenzkonflikten

Wenn ein Kunde in xentral zwei Systeme über eine Lizenz laufen lässt, dann ist dies seit der 20.3 ein großes Problem.

Dadurch wird zum einen

1. die Lizenz fest mit der neuen Version verknüpft,

2. zum anderen wird eine Doppelnutzung der Systeme unterbunden.

Wie erkenne ich dies?

Aufruf des xentral-Systems (index.php) ist nicht möglich. Es wird ein weißer Bildschirm gezeigt. In der Browser-Konsole wird Serverfehler (Fehler 500) ausgegeben. Guckt man in die Serverlogs wird angezeigt, das ein ungültige key.php verwendet wird.

## 1. Verknüpfung der Lizenz mit einer Version

In der Vergangenheit war es möglich, das eine Lizenz für mehrere Versionen verwendet werden konnte. Ein Downgrade war in der Regel nicht möglich, jedoch konnte in einem frischen System mit einer beliebigen Version von xentral gearabeitet werden. Dies ist nun nicht mehr möglich.

D.h. wenn ein Kunde von einem Testsystem auf ein Live-System gewechselt hat, dann muss dieser im Live-System auch zwingend auf die Version 20.3 upgraden. Für manche Kunden ist dies aber nicht ohne Weiteres möglich, weshalb hier in der Regel immer Probleme vorprogrammiert sind.

Möglichkeiten:

-Kunde geht mit dem Live-System auf die Version 20.3 oder höher

-Lizenz wird von Entwickler mit Zugang zum Update-Server (z.B. Bruno oder Manu) auf die Version 20.2 zurückgesetzt

-Kunde bezahlt für einen neue Lizenz für das Testsystem. Zusätzlich muss die Lizenz aber dennoch zurückgestuft werden

Konkretes Doing:

-Lizenz aus dem Testsystem entfernen

-Direktes Update des Live-Systems über liveURL.de/update.php aufrufen und Update für die 20.2 ziehen. Hier wird dann eine neue key.php ausgeliefert.

Sonderfall:

Es gab zeitweise einen Bug, das die update.php, welche sonst immer unverschlüsselt ist, verschlüsselt ausgeliefert wurde. Dadurch war auch der Aufruf der /update.php nicht möglich, aufgrund der key.php-Fehlermeldung.

Hier muss dann folgendes Update-Skript auf dem Server hinterlegt werden.

-UpdateSkript-

Wichtig ist, das dieses z.B. nicht in var/xentral/ abgelegt wird sondern in var/xentral/www/.

## 2. Unterbindung der Doppelnutzung:

Wenn beide Lizenzen aktiv genutzt werden, dann wird innerhalb von wenigen Minuten die Arbeit im zweiten System unterbunden werden. Hier dürfte zumindest in den Serverlogs dann eine Fehlermeldung gezeigt werden.