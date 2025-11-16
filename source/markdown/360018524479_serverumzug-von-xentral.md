> **Wichtig**
>
> **End-of-Life für On-Premise-Instanzen**
>
> Ende März 2023 beenden wir die Unterstützung von Xentral-Instanzen, die „On-Premise“ von unseren Kunden selbst gehostet werden. Wir empfehlen dir daher, deine Xentral-Instanz in unsere Cloud zu migrieren. Kontaktiere uns gerne jederzeit unteraccount@xentral.com, um diesbezügliche Fragen zu klären oder einen Termin für deine Migration zu buchen. Alternativ kannst du weitere Informationen aufunserer Websiteoder inunserer Communityfinden.
>
> Beachte bitte, dass wir Ende März 2023 jegliche Supportleistungen für On-Premise-Instanzen beenden. Wir stellen dann keine weiteren Bug-Fixes oder Updates mehr zur Verfügung. Außerdem wird es keine weitere Open-Source-Version mehr geben.

## Ablauf

Der Ablauf eines Xentral-Server-Umzuges (Verschieben eines Xentral-Systems auf einen anderen Server oder Provider) besteht aus 10 Schritten. Hier zunächst ein Überblick über den Ablauf - im Folgenden ist jeder Schritt noch einmal detaillierter erklärt.

1. Prozessstarter des Altsystems global deaktivieren
1. Daten des Altsystems sichern
1. Neues System installieren
1. CRON-Job einrichten
1. Datenbank in das neue System einspielen
1. Dateidaten in das neue System einspielen (userdata) und ggf. Korrekturen vornehmen
1. Neues System updaten
1. Hardware an das neue System anbinden
1. Abschließende Prüfungen
1. Prozessstarter des neuen Systems aktivieren

### Ablauf im Detail

1. Prozessstarter des Altsystems deaktivieren: Die Prozessstarter des Altsystems werden global deaktiviert. Diese Option finden Sie unter **Administration > Einstellungen > System > Prozessstarter ** rechts im Aktionsmenü**Prozessstarter global deaktivieren**.
1. Daten des Altsystems sichern: Die Daten werden mit einem Systembackup gesichert. Alternativ können die Daten auch per DB-Dump und Kopie des userdata-Ordners gesichert werden. Es empfiehlt sich, sowohl den userdata-Ordner als auch die Datenbank in einem Archivformat zu packen (z.B. tar.gz oder zip).
  Details hierzu finden sich im Artikel Datenumzug.

1. Neues System installieren: Auf dem neuen Server wird das neue System installiert. Bitte dazu die OperSource-Version (OS-Version) im Downloadbereich der Webseite (herunterladen) und nach Anleitung installieren. Durch das spätere Einspielen des Lizenzschlüssels wird die korrekte Version und Lizenz später wieder hergestellt.
1. CRON-Job einrichten: Auf dem neuen Server sollte nun sichergestellt werden, dass der sog. Heartbeat-Cronjobs läuft, dahinter verbirgt sich der Trigger für den Prozessstarter-Mechanismus in Xentral. Alle Informationen dazu finden sich im Artikel: Einrichten des Heartbeat-Cronjobs.
1. Datenbank in das neue System einspielen: Die Datenbank aus dem Altsystem wird nun in das neue System eingespielt. Dabei sollte folgendes nach dem Import die Anzahl der Tabellen überprüft werden um sicherzustellen, dass alle Tabellen kortrekt exportiert und importiert wurden. Aussder sollte stichprobentartig die Anzahl der Zeilen wichtiger Tabellen geprüft werden (z.B. adresse, artikel, auftrag).
  Die Lizenzdaten wurden mit der Datenbank auch in das neue System übertragen.

  Weitere Hinweise zu diesem Punkt siehe auch Artikel Datenumzug.

1. Dateidaten in das neue System einspielen: Die Daten des Ordners userdata werden in das neue System eingespielt. Wenn möglich, ist es sinnvoll für die Übertragung dieser Daten eine Server-zu-Server Verbindung (z.B. mit scp) zu verwenden anstatt die Daten erst lokal (auf dem eigenen Rechner) zu speichern und dann auf den neuen Rechner hochzuladen.
  Nach der Übertragung sollte an Hand der Gesamtgröße des Ordners (du -hs) und der Anzahl der Dateien überprüft werden ob die Übertragung vollständig ist.

  Durch die Übertragung des Ordners sind oftmals die Besitz-/ Schreibrechte der Ordnerstruktur nicht korrekt. Diese können dann rasch angepasst werden. Detailliertere Informationen dazu liefert auch der Artikel **Datenumzug **. ** Einfluss des Datenbank-Namens** Im userdata-Ordner befinden sich Unterordner in denen wiederum Unterordner liegen, deren Namen von der alten Datenbank abhängen. Diese Ordner müssen in den neuen Datenbanknamen umbenannt werden.

  Meistens sind folgende Ordner betroffen:

  Falls weitere Ordner vorhanden sind, müssen diese ebenfalls überprüft werden. Auch vorhandene Dateien, die den Datenbanknamen im Dateinamen führen müssen umbenannt werden wie z.B. das Briefpapier. sinf ggf. anzupassen oder neu zu konfigurieren.

  Eigens angelegte Schriftarten werden durch den Umzug aus dem Ordner www/lib/pdf/font/unifont nicht mitkopiert. Die Schriften sollten daher nun manuell im System nachgetragen werden. Hinweis zum Vorgehen finden sich in Artikel Briefpapier.

  Detailliertere Informationen dazu liefert auch der Artikel **Datenumzug**.

  - Im Ordner dms
  - Im Ordner emailbackup (Falls vorhanden)
  - Im Ordner pdfarchiv
  - Im Ordner pdfmirror
1. Neues System updaten Nun kann das neue System zum ersten Mal upgedated werden, dabei wird auf Basis der Lizenzdaten auch die korrekte Lizenz aktiviert und ggf. fehlende Module nachgeladen.
  Siehe Artikel Zugang zum Updateserver **Bitte beachten Sie:** Das Altsystem hat nun keine gültige Lizenz mehr.

1. Hardware an das neue System anbinden Nach der Umstellung einer Serverinstallation müssen bei einem Wechsel der Adresse (Suddomain oder DOmain) ggf. auch die lokalen Anbindungen der Hardware umgestellt werden. Dazu gehören z.B. Scanner / Kameras oder Etikettedrucker an Adapterboxen oder Druckerspooler.
  Im Grunde sind dazu dieselben Schritte nötig wie bei einer Installation der Geräte, nur dass die ersten Schritte übersprungen werden können. Siehe dazu auch Artikel Drucker Schnelleinstieg.

  Grundsätzlich müssen aber nur die URLs und ggf. key angepasst werden, die beim Spooler in den Einstellungen hinterlegt sind, und bei der Adapterbox über die Konfig-Datei vorgegeben ist.

1. Abschließende Prüfungen Es ist sinnvoll einige abschließende Prüfungen vorzunehmen, bevor das System wieder in den produktiven Betrieb geht:
  - Prüfen Sie ob ggf. Benutzer in den persönlichen Einstellungen noch auf das Altsystem referenzieren (Startseite)
  - Prüfen Sie ob der Webserver Zugriff auf das Dateisystem (userdata) hat: Dazu über die Oberfläche eine Datei (z.B. einer Adresse). Wenn diese im Anschluß heruntergeladen wird und eine Dateigröße von 0 Byte hat stimmen vermutlich die Zugriffsrechte nicht. Kann man die Datei allerdings öffnen, hat alles geklappt. Ansonsten siehe Artikel Datenumzug z.B. unter Finale Anpassungen.
1. Prozessstarter des neuen Systems aktivieren Die Prozessstarter des neuen Systems werden global aktiviert. Diese Option finden Sie unter Administration → Einstellungen → System → Prozessstarter rechts im Aktionsmenü Prozessstarter global aktivieren.