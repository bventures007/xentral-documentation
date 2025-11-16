In der Version 22.1 führen wir folgende Änderungen ein, die deine Aufmerksamkeit erfordern, da sie Einfluss auf deine laufenden Prozesse haben können.

> **Wichtig**
>
> Diese Informationen sind für dich relevant, wenn du ein Update von einer älteren Version, die niedriger als 22.1 ist, auf eine aktuelle Version 22.1 oder höher durchführst.

> **Anmerkung**
>
> Einige dieser Informationen sind nur für Kunden mit einer On-Premise-Instanz relevant.

Die folgende Liste gibt dir einen Überblick - folge den Links für weitere Informationen:

- Für alle Kunden relevant (Cloud und On-Premise)
  - [Änderungen bei der Authentifizierung](https://help.xentral.com/hc/articles/4404066836114#UUID-0559cd84-4194-d6bc-e2cf-bcc8a403b462)
  - Keine Stichwörter
  - Entfernung bestimmter Module, siehe[Release Notes](https://help.xentral.com/hc/articles/4409075372828#UUID-aff6bc5c-d41a-bd8d-6879-54f85d28510c)
- Nur für On-Premise Kunden relevant
  - [Hosting-Anforderungen für Xentral](https://help.xentral.com/hc/articles/360017436039#UUID-dc5a1e39-8c4d-6bef-619f-f6bec2725cac), nur für On-Premise-Instanzen relevant
  - [Neue .env-Datei](https://help.xentral.com/hc/articles/4404060311954#UUID-cfc8c03b-f285-642e-27a5-cb7cc767c8a9), nur für On-Premise-Instanzen relevant
  - [Änderungen in "firmendaten"](https://help.xentral.com/hc/articles/4404066668690#UUID-a2c3bfec-9dac-d813-a1d2-472db40c4651), nur für On-Premise-Instanzen relevant
  - [Warteschlangenprozess konfigurieren](https://help.xentral.com/hc/articles/4408098681234#UUID-dee51b85-45fc-0ba7-f05e-eff760804cc3), nur für On-Premise-Instanzen relevant
  - [Modul-Metadaten-Dateien](https://help.xentral.com/hc/articles/4408107066514#UUID-d1671ed8-135d-f9d0-397a-01ee123c9b40), nur für On-Premise-Instanzen relevant

Weitere Informationen zur neuen Version 22.1 findest du[hier](https://xentral.community/updates-zur-xentral-plattform-17/die-highlights-der-neuen-version-22-1-1206).

> **Anmerkung**
>
> Falls du nach dem Update eine Fehlermeldung erhältst, bedeutet dies, dass der alte Aufruf mit der 22.1 nicht mehr funktioniert.
>
> Bitte verwende dazu den Wrapper der REST-API. Um die REST-API anzusprechen, musst du eine DIGEST-Authentifizierung mit MD5-Verschlüsselung durchführen. Mit dem Wrapper kannst du alle Aufrufe der Standard-API verwenden, mit der Ausnahme, dass kein HASH und keine api_id mehr übergeben werden müssen.