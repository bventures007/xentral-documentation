### Alle Prozessstarter laufen in einen Error (AB, 16.07.2021)

- ioncube loader version für PHP und PHP-CLI muss zwingend gleich sein

- PHP und PHP-CLI Version muss gleich sein

- PHP mindestens 7.3, besser 7.4

-[Heartbeat](https://community.xentral.com/hc/de/articles/360017377620-Installation-von-xentral-ab-Version-19-1#h_01F0BCJR3XAE429CWMHB8CTKKZ)muss aktiviert sein

- Bitte prüfen, ob Rechte richtig vergeben. Heartbeat über root starten ist problematisch, besser über Gruppe www-data. Gerne auch mit www-data oder einem Benutzer einloggen und PHP ausführen. Klappt das?

`cd cronjobs`

`php command.php starter2.php`

Hier tauchen dann errors auf, z.B. wenn heartbeat nicht läuft.

- Dateiberechtigung prüfen, z.B. um starter.php oder starter2.php auszuführen.

- memory limit bei php-cli üeber 256MB, besser 512MB.

- Gerne auch Logfiles unter `storage/logs` prüfen.