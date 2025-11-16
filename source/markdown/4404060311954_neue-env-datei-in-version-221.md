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

Im Stammverzeichnis einer xentral-Installation muss eine Datei namens `.env` vorhanden sein. Wenn diese nicht vorhanden ist, kannst du `.env.prod` dorthin kopieren.

Diese Datei ist der zukünftige Ort für die Credentials.

## APP_KEY

Dieser Wert wird für die Verschlüsselung/Entschlüsselung verwendet. Wir stellen einen Standardschlüssel zur Verfügung, um nicht in Fehler zu laufen.

Um einen neuen eindeutigen Schlüssel zu erzeugen, führe `php artisan key:generate` aus.

Führe dies einmal nach dem Update auf 22.1 aus.

## APP_URL

Diese Variable wird verwendet, um URL's außerhalb des Web-Kontextes zu generieren. Bitte trage die URL inkl. Protokoll in diese Variable ein.

Beispiel: `APP_URL=https://xentral.mydomain.tld`

## Veralteter conf-Ordner

In einem zukünftigen Update werden wir Konfigurationswerte wie z.B. Datenbank-Credentials in diese Datei verschieben.