Mit der Anbindung von HubSpot an Xentral kannst du deine Verkaufsaktivitäten weiter optimieren, indem du Daten zwischen den beiden Systemen importierst, exportierst und synchronisierst.

![Hubspot_Xentra_graphics.png](https://help.xentral.com/hc/article_attachments/9393628943900)

Die in HubSpot verfügbaren Daten sind in Kontakte und Unternehmen aufgeteilt. Diese werden folgendermaßen in Xentral zugeordnet.

| HubSpot | Xentral | Synchronisationsbedingungen |
| --- | --- | --- |
| Kontakt | Adresse des Typs Herr oder Frau | Datensätze stimmen überein, wenn: - E-Mail-Adresse zu 100 % übereinstimmt Adressen ohne E-Mail-Adresse werden nicht synchronisiert! |
| Unternehmen | Adresse des Typs Firma | Datensätze stimmen überein, wenn: - Der Firmenname zu 70% oder mehr übereinstimmt und - Postleitzahl zu 100% übereinstimmt |

## Funktionsumfang der Anbindung

Du kannst Daten zwischen HubSpot und Xentral auf folgende Weisen austauschen:

- Kontakte/ Unternehmen zwischen den beiden Umgebungen synchronisieren - Kontakte/ Unternehmen werden hinzugefügt und können mit zusätzlichen Daten von Xentral an HubSpot und anders herum aktualisiert werden.
- Kontakte/ Unternehmen von HubSpot nach Xentral importieren - Du kannst Kontakte/ Unternehmen aus HubSpot in Xentral hinzufügen und diese mit zusätzlichen Informationen aus HubSpot aktualisieren.
  Du kannst den Import auf bestimmte Lifecycle-Phasen beschränken. Weitere Informationen hierzu findest du im Abschnitt [Import durch Lifecycle-Phasen beschränken](#import-durch-lifecycle-phasen-beschraenken).

- Kontakte/ Unternehmen aus Xentral nach HubSpot exportieren - Du kannst Kontakte/ Unternehmen von Xentral nach HubSpot exportieren und diese mit zusätzlichen Informationen aus Xentral aktualisieren.
- Deals synchronisieren - Neue Aufträge können als Deal von Xentral zu HubSpot übertragen werden. Weitere Informationen findest du im Abschnitt: [Deals synchronisieren](#deals-synchronisieren).

Beachte beim Löschen oder Ändern von Daten den folgenden Verarbeitungsprozess der sowohl für die Synchronisierung als auch für den Import und Export gilt:

Wenn du die kompletten Kontaktdaten oder einzelne Informationen wie die Telefonnummer in einem System (z.B.Xentral) löscht, werden diese durch den Datenaustausch nicht neu hinzugefügt. Sie werden auch nicht im anderen System (z.B. HubSpot) gelöscht.

Ebenso werden in einem System geänderte Kontaktdaten wie z.B. die Telefonnummer nicht an das andere System übergeben. Bei zwei Systemen mit gegenseitiger Synchronisierung wird die Änderung bei der nächsten Synchronisierung nicht rückgängig gemacht.

## Xentral und HubSpot verbinden

Die Verbindung von Xentral und HubSpot erfolgt per OAuth-Authentifizierung. Gehe wie folgt vor, um Xentral und HubSpot zu verbinden:

1. Melde dich in Xentral an und navigiere zum App Center.
1. Suche nach der HubSpot-App und klicke auf Öffnen.
1. Klicke zur Herstellung der Verbindung auf Verbindung zu HubSpot herstellen.
1. Gib im angezeigten HubSpot-Fenster die Anmeldedaten (E-Mail-Adresse und Passwort) eines Admin-Benutzers in HubSpot ein und bestätige.
  Wenn du bereits in HubSpot eingeloggt bist, wähle das HubSpot-Konto, dass du verbinden möchtest, und klicke auf Konto auswählen.

Möchtest du die Verbindung zwischen Xentral und HubSpot trennen, gehe dazu wie folgt vor:

1. Navigiere zu App Center > HubSpot.
1. Klicke in den HubSpot-Einstellungen auf Widerrufe Verbindung zu HubSpot.
1. Klicke in der OAuth Account-Ansicht, auf die du weitergeleitet wurdest, auf Autorisierung widerrufen und bestätige dies mit OK, um die Verbindung zu trennen.

## Richtung des Datenaustauschs wählen

WennXentral und HubSpot verbunden sind, kannst du die Form des Datenaustauschs auswählen. In den HubSpot-Einstellungen in Xentral kannst du zwischen den folgenden Optionen wählen:

- Sync: Xentral ↔ HubSpot
- Import: HubSpot → Xentral
- Export: Xentral → HubSpot

Klicke aufSpeichern, nachdem du einen anderen Datenaustausch-Typ gewählt hast.

Importierst oder synchronisierst du Daten aus HubSpot, so werden deine HubSpot-Nutzer als Addressen des Typs Herr oder Frau und der Rolle Mitarbeiter nach Xentralübertragen. Dies geschieht, damit die Verbindung zwischen dem Kontakt und dem zuständigen Mitarbeiter aufrechterhalten werden kann. Die Information wird im FeldInnendiensteiner Adresse in Xentral gepflegt.

> **Anmerkung**
>
> Beachte, dass deine HubSpot-Nutzer beim Import einem Projekt zugeordnet werden. Weitere Informationen findest du im AbschnittProjekt zuordnen.

Mehr über die Möglichkeiten des Datenaustauschs in die jeweilige Richtung erfährst du im Abschnitt[Funktionsumfang der Anbindung](#UUID-17fb5b04-cfd4-f066-ca67-55a03e936dd7_section-idm4576288918516833394492833855).

## Automatischer oder manueller Datenaustausch

Der Datenaustausch zwischen Xentral und HubSpot erfolgt automatisch oder manuell. Dies kannst du im BereichAktionenin den HubSpot-Einstellungen in Xentral einstellen, indem du auf die entsprechende Schaltfläche klickst. Wenn du für den Datenaustausch die automatische Synchronisierung auswählst, wird das Intervall, in dem synchronisiert wird, durch den[Prozessstarter](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a)HubSpot Data Syncgesteuert.

Das Intervall des Datenaustauschs kannst die folgendermaßen anpassen:

1. Navigiere zu Administration > System > Prozessstarter, suche nach dem Prozessstarter Hubspot Data Sync und klicke auf.
1. Passe die Einstellungen des Prozessstarters an und klicke auf Speichern.

Wenn du Daten manuell zwischen Xentral und HubSpot austauschen möchtest, gehe wie folgt vor:

1. Wähle je nach gewünschter Aktion in den HubSpot-Einstellungen die Option Import: HubSpot → Xentral oder die OptionExport: Xentral → HubSpot und klicke auf Speichern.
1. Klicke im Bereich Aktionen auf Manuellen Import: HubSpot → Xentral starten oder Manuellen Export: Xentral → HubSpot starten, je nachdem was du im vorherigen Schritt ausgewählt hast.
1. Die Aktion wird nun ausgeführt und entsprechende Informationen werden dir in der Nachrichtenleiste angezeigt. Wenn die Aktion abgeschlossen ist, kannst du im Reiter Übersicht prüfen, ob Konflikte aufgetreten sind. Ein Konflikt entsteht z.B. wenn sich Daten widersprechen.
  Im Reiter Übersicht siehst du ein Protokoll aller Importprozesse. Jeder Prozess ist mit einem Zeitstempel versehen und zeigt an, wie viele Datensätze neu erstellt oder bearbeitet wurden und wie viele Konflikte aufgetreten sind.

![hubspot_overview.png](https://help.xentral.com/hc/article_attachments/9393629133852)

## Import durch Lifecycle-Phasen beschränken

Du kannst Untergruppen deiner HubSpot Kontakte/ Unternehmen importieren, indem du den Import auf bestimmte Lifecycle-Phasen beschränkst. Dies kann dir dabei helfen deine Stammdaten in Xentral besser organisiert zu halten. Typische Lifecycle-Phasen sind: Lead, Sales-Qualified-Lead und Kunde. Du kannst deine Lifecycle-Phasen in HubSpot anpassen und zuordnen.

Gehe wie folgt vor, um den Import einzuschränken:

1. Wähle im Reiter Einstellungen die Lifecycle-Phasen aus, auf die du den Import beschränken möchtest.
  Die Liste der Lifecycle-Phasen auf der rechten Seite wird aus HubSpot importiert, sobald die beiden Systeme miteinander verbunden sind. Nachdem die Verbindung angelegt ist, kannst du in HubSpot neu erstellte Lifecycle-Phasen durch einen Klick auf Update Lifecycle-Phasen importieren.

1. Klicke auf Speichern.

Der Import ist nun auf die ausgewählten Lifecycle-Phasen beschränkt. Du kannst die ausgewählten Lifecycle-Phasen jederzeit ändern, indem du zusätzliche Phasen auswählst oder bestehende abwählst und anschließend speicherst.

## Projekt zuordnen

Vor dem Import kannst du neu in Xentral angelegten Kontakten und Unternehmen ein Projekt zuordnen. Sollte der importierte Kontakt oder das importierte Unternehmen schon in Xentral exisitieren, so wird das Projekt nicht verändert.

Gehe wie folgt vor, um ein Projekt zuzuordnen:

1. Wähle die für das Projekt relevanten Lifecycle-Phasen aus. Dies limitiert den Import auf bestimmte Untergruppen deiner Kontakte und Unternehmen in HubSpot.
1. Wähle dasProjekt, das du deinem Import zuweisen möchtest, im Suchfeld im BereichProjektzuordnung aus.

Sobald das nächste Mal ein Kontakt oder ein Unternehmen aus HubSpot importiert wird, werden sie dem gewählten Projekt zugeordnet. Möchtest du anderen Lifecycle-Phasen ein anderes Projekt zuordnen, dann prüfe den ReiterÜbersicht, um sicherzustellen, dass der Import beendet wurde. Wähle dann deine neuen Lifecycle-Phasen und ein neues Projekt für den nächsten Import aus.

## Deals synchronisieren

Wenn du die Deal Synchronisierung aktivierst, werden alle neuen Aufträge aus Xentral als "Deal Won" in deine HubSpot Pipeline übertragen und dem Käufer zugeordnet. Dies ermöglicht dir einen Überblick über deine aktuellen Verkäufe und erlaubt dir somit deine Marketingaktivitäten besser auf das Kaufverhalten deiner Kunden abzustimmen.

Du aktivierst die Deal Synchronisierung, indem du ein Häkchen beiDeal Synchronisierung aktivsetzt und dann aufSpeichernklickst.

![hubspot_dealsync.png](https://help.xentral.com/hc/article_attachments/11623178629148)

Sobald ein neuer Auftrag den StatusFreigegebenerhält, werden der Kontakt und der Bestellwert als Deal von Xentral nach HubSpot übertragen. Der Deal wird in deiner Standardpipeline (ID = 1) angelegt und mit dem entsprechenden Kontakt oder Unternehmen verknüpft. Handelt es sich um einen neuen Kunden, wird ein neuer Kontakt oder ein neues Unternehmen angelegt.