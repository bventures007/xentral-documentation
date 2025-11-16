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

Meta-Informationen aus `www/lib/class.erpapi.php` wurden in Modulklassendateien in `app/Modules/` verschoben.

Diese Dateien enthalten Informationen über jedes Modul wie z.B.:

- Modulbezeichner (der `module` GET Parameter)
- Menschenlesbarer Modulname
- URLs zur Dokumentation
- Spezielle Flags, wie z.B. "beta"
- Routen (noch nicht verwendet)

Diese Informationen werden verwendet, um den App Store anzuzeigen und statische Informationen zu den einzelnen Modulen bereitzustellen.

In Zukunft werden weitere Daten in diese Dateien verschoben.