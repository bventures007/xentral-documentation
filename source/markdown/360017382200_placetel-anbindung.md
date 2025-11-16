> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Administration → AppStore → Placetel Anbindung

Mein Bereich → Meine Apps → Placetel Anbindung

Dieses Modul bindet die Telefonanlage von Placetel an und macht es dir so möglich, direkt über xentral mit den Kontakten deines Adressstamms zu telefonieren.

## Einrichtung Placetel

Für die Einrichtung sind verschiedene Schritte sowohl in Placetel als auch in xentral umzusetzen.

### Einstellungen in Placetel

Um eine Programmanbindung zu Placetel einzurichten, benötigst du einen API-Key, den du in deinem Kundenkonto von Placetel unter Administration → Einstellungen → API vorfindest. Du kannst an dieser Stelle ebenfalls ein API Token generieren, falls das noch nicht geschehen ist:[Placetel Webseite](https://www.placetel.de).

Möchtest du darüber hinaus auch Benachrichtigungen über Placetel in xentral abbilden, sind noch folgende zusätzlichen Einstellungen unter Administration → Einstellungen → Externe APIs erforderlich:

- Haken setzen "Call Control-/Notify-API aktivieren"
- URL deines API-Endpoints (bitte URL angleichen): https://deineurl.de/index.php?module=callcenter&action=call&provider=placetel.
- Shared Secret für HMAC eingeben

### Einstellungen in xentral

Unter Administration → AppStore → Placetel Anbindung oder Mein Bereich → Meine Apps → Placetel Anbindung kannst du den API-Key eintragen, woraufhin er auf der rechten Seite deines Placetel-Accounts erscheinen sollte. Das optionale Shared Secret für die Verwendung von Benachrichtigungen kann hier ebenfalls hinterlegt werden:

Deine Accounts können dann im linken Textfeld angelegt werden. Folgende Nomenklatur ist dabei zu beachten:

**pro Zeile: Benutzername Xentral:UID von Placetel → Beispiel: MaxMustermann:77777777@fpbx.de**

Sofern nur einzelne Benutzer keine Benachrichtigungen erhalten möchten, können diese unter Mein Bereich → Persönliche Einstellungen im Bereich Einstellungen ausgeschlossen werden. Der Haken bei "Telefon-Benachrichtigungen" ist hier standardmäßig gesetzt und ist explizit zu deaktivieren.

## Verwendung Placetel

Mittels der fertig eingerichteten Placetel-App können ausgehende Anrufe getätigt sowie eingehende Anrufe bearbeitet werden.

![Placetel-01.png](https://help.xentral.com/hc/article_attachments/4996440845468)

### Ausgehende Anrufe

In der Übersicht kannst du in einem Eingabefeld eine Rufnummer eintragen und über den dazugehörigen Button anrufen. Daraufhin wird der Anruf zunächst über deine Telefonanlage geleitet und bei Abnahme des Hörers zum Empfänger durchgestellt. Im Telefonbuch werden alle Ansprechpartner mit Telefonnummer aus dem Adressstamm geladen.

Darüber hinaus kannst du auch direkt aus dem Adressstamm Telefonate mit den hinterlegten Kontakten starten. Dazu öffnest du die gewünschte Adresse und drückst den Telefon-Button neben der hinterlegten Telefonnummer.

### Eingehende Anrufe

Ab Version 19.1 können eingehende Anrufe auch bestehenden Adressen zugeordnet werden, womit die folgenden Benachrichtigungen zur Verfügung:

- Eingehender Anruf
- Anruf angenommen
- Anruf beendet

Im Fall eines nicht zuordenbaren Anrufs erscheint eine Benachrichtigung. Im Fall eines zuordenbaren Anrufs kann mittels der Benachrichtigung zur Adresse gesprungen werden oder eine Telefonnotiz erstellt werden.

> **Anmerkung**
>
> Anrufbenachrichtigungen werden nur global ausgegeben, d.h. eine Einschränkung auf einzelne Accounts ist nicht möglich.

#### Notifikations-Einstellung im Benutzer

Unter Mein Bereich → Einstellungen gibt es für jeden Mitarbeiter die Option die Telefon-Benachrichtigungen auszuschalten.

## xentral Anbindung weiterer Telefonanlagen **Ausgehende Anrufe:**

Wenn du ausgehend von xentral telefonieren willst, gibt es im Wesentlichen zwei Methoden. In xentral generieren wir zu jedem ausgehenden Anruf eine URL z.B. "tel:49123456789", diese wird von den meisten Software-Phones oder Programmen wie Skype, WhatsApp bzw. auch für TAPI-Clients von klassischen Telefonanlagen unterstützt.

Als zweite Methode bietet xentral die Möglichkeit APIs anzubinden, wobei aktuell standardmäßig nur die Anbindungsmöglichkeit über Placetel besteht.