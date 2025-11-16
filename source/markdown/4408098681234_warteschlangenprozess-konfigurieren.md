> **Anmerkung**
>
> Diese Informationen sind nur für Kunden mit einer On-Premise-Instanz relevant.

> **Wichtig**
>
> **End-of-Life für On-Premise-Instanzen**
>
> Ende März 2023 beenden wir die Unterstützung von Xentral-Instanzen, die „On-Premise“ von unseren Kunden selbst gehostet werden. Wir empfehlen dir daher, deine Xentral-Instanz in unsere Cloud zu migrieren. Kontaktiere uns gerne jederzeit unteraccount@xentral.com, um diesbezügliche Fragen zu klären oder einen Termin für deine Migration zu buchen. Alternativ kannst du weitere Informationen aufunserer Websiteoder inunserer Communityfinden.
>
> Beachte bitte, dass wir Ende März 2023 jegliche Supportleistungen für On-Premise-Instanzen beenden. Wir stellen dann keine weiteren Bug-Fixes oder Updates mehr zur Verfügung. Außerdem wird es keine weitere Open-Source-Version mehr geben.

Xentral 22.1 verfügt über eine Warteschlangenkomponente zur Normalisierung der Arbeitslast. Die Aufträge in der Warteschlange werden von einem lang laufenden Worker Prozess ausgeführt.

## Worker Prozess starten und anhalten

Um den Worker manuell zu starten, gib folgenden Befehl im Command Line Interface ein:

```php /xentral_root_dir/artisan queue:work```Um den Worker manuell anzuhalten, gib folgenden Befehl im Command Line Interface ein:```php /xentral_root_dir/artisan queue:restart```

> **Anmerkung**
>
> Der Befehl heißt zwar "restart", hält aber nur den Prozess an.

Weitere Informationen und Befehlsoptionen findest du in der[Laravel-Dokumentation](https://laravel.com/docs/8.x/queues#running-the-queue-worker).

## Prozesskontrollsysteme verwenden

Wir empfehlen dir, ein Prozesskontrollsystem oder einen Prozessmonitor zu verwenden, um die Worker neu zu starten, wenn sie beendet wurden oder abgestürzt sind.

Du kannst hierfür ein System deiner Wahl nutzen, das fähig ist, angehaltene Prozesse automatisch über Konsolenbefehle zu starten.

### Systemd nutzen

Unter Linux kannst du mit `systemd` einen Dienst als Prozesskontrollsystem definieren und ausführen.

Führe folgende Schritte durch:

1. Erstelle eine Datei unter folgendem Pfad und Dateinamen, um darin den Dienst zu definieren:
1. Trage die gewünschte Konfiguration in die Datei ein, siehe im Beispiel unten.
  Beachte, dass du im Beispiel `/var/www/xentral ` durch das Root Verzeichnis deiner Xentral installation ersetzen musst. Außerdem, musst du gegebenenfalls`www-data` durch den tatsächlichen Web Server Nutzer in deiner Umgebung ersetzen.

1. Nachdem du die Konfiguration in der Datei gespeichert hast, musst du den Daemon durch den folgenden Befehl neu laden.
1. Nun kannst du einen oder mehrere Worker laufen lassen.
  Um den ersten Worker zu starten, nutze den folgenden Befehl:

  Du kannst weitere Worker starten, indem du die Befehle erneut eingibst und dabei fortlaufende Nummern hinter dem `@` Symbol einträgst.

### Supervisor nutzen

Als Alternative zu Systemd kannst du Supervisor als  Prozesssteuerungssystem verwenden, um den Warteschlangenprozess zu konfigurieren.

Weitere Informationen zur Verwendung von Supervisor findest du in der[Supervisor-Dokumentation](http://supervisord.org/).

Konfigurationsbeispiel:

```
[program:queue-worker]
user=www-data
process_name=%(program_name)s_%(process_num)02d
command=php /var/www/xentral/artisan queue:work --max-time=3600
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
numprocs=2
redirect_stderr=true
stdout_logfile=/var/www/xentral/storage/logs/queue-worker.log
stopwaitsecs=3600
```

Weitere Informationen zur Konfiguration findest du in der[Laravel-Dokumentation](https://laravel.com/docs/8.x/queues#running-the-queue-worker).

### Regelmäßiger Neustart

Wenn du ein Prozesskontrollsystem verwendest, musst du den Worker Prozess regelmäßig anhalten und neu starten, um Probleme zu vermeiden. Eine Möglichkeit, dies zu erreichen, ist es, die folgenden Optionen mit dem Befehl `artisan queue:work` zu verwenden:

- `--max-jobs=1000`: Der Worker stoppt nach Verarbeitung der angegebenen Zahl von Aufträgen. [Weitere Informationen](https://laravel.com/docs/8.x/queues#processing-a-specified-number-of-jobs)
- `--max-time=3600`: Der Worker stoppt nach der angegebenen Zeitspanne (in Sekunden). [Weitere Informationen](https://laravel.com/docs/8.x/queues#processing-jobs-for-a-given-number-of-seconds)

Eine Kombination aus beiden Optionen ist möglich.

> **Tipp**
>
> Du wirst vermutlich verschiedene Einstellungen durchprobieren müssen, um die für deine Umgebung passende Einstellung zu finden. Wenn beispielsweise ein Worker häufig seine Speichergrenze überschreitet, empfiehlt es sich, diesen häufiger neu starten zu lassen.

### Mehrere Worker laufen lassen

Du kannst mehrere Worker Prozesse gleichzeitig laufen lassen. Dies wird jedoch von verschiedenen Prozesskontrollsystemen auf unterschiedliche Weise gesteuert: Für Systemd musst du mehrere Dienste starten; Supervisor hingegen verwendet die Eigenschaft `numprocs`.

Berücksichtige die folgenden Aspekte bei der Entscheidung, wie viele Worker laufen sollen:

- Wie viele unbearbeitete Aufträge gibt es?
  Die Aufträge in der Warteschlange werden in der Tabelle `queue_jobs` gespeichert. Wenn sich zu viele Aufträge in der Warteschlange befinden, solltest du eventuell weitere Worker hinzufügen.

- Leistung
  Eine höhere Anzahl an laufenden Worker Prozessen führt zu einer höheren CPU- und RAM-Auslastung. Dies kann die Antwortzeit der Anwendung insgesamt beeinträchtigen.