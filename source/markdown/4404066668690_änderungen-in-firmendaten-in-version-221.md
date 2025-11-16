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

In Version 22.1 wird die Datenbanktabelle `firmendaten` komplett entfernt. Daher MUSS aller Code, der über eine direkte SQL-Abfrage auf diese Tabelle zugreift, aktualisiert werden.

Zusätzlich wird empfohlen, auch die direkten SQL-Abfragen mit der Tabelle `firmendaten_werte` nicht mehr zu verwenden, da dadurch Performance-Verbesserungen möglich sind.

## Beispiele:

### Beispiel 1 - Aktualisieren des Firmendatenwerts:

Der alte Code, der eine direkte SQL-Abfrage verwendet, wird nicht mehr funktionieren:

```$this->app->DB->Query("UPDATE firmendaten SET freifeld13='Duft' where id='1'");```So aktualisierst du: Verwende den ` SystemSettings`service:```app(\App\Core\Settings\SystemSettings::class)->set('freifeld13', 'Duft');```

### Beispiel 2 - Holen eines Wertes aus der Firmendaten-Tabelle:

Der alte Code holt den Wert von `briefpapier2` mit einer direkten SQL-Abfrage:```$briefpapier2 = $this->app->DB->Select("SELECT briefpapier2 FROM firmendaten WHERE id={$firmendatenid}");```So aktualisierst du: Verwende den ` SystemSettings`service:```$briefpapier2 = app(\App\Core\Settings\SystemSettings::class)->get('briefpapier2');```

### Beispiel 3 - Zugriff auf die Tabelle firmendaten_werte:

Es wird dringend empfohlen, auch bei der Tabelle `firmendaten_werte` keine direkten SQL-Abfragen mehr zu verwenden.

Alter Code:

```$land = $this->app->DB->Select("SELECT wert FROM firmendaten_werte WHERE name = 'land'");```So gehst du jetzt vor:```$land = app(\App\Core\Settings\SystemSettings::class)->get('land');```