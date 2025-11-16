Du kannst deine Kontoauszüge in Xentral importieren und die importierten Transaktionen auf die entsprechenden Rechnungen und Gutschriften verbuchen.

Der Import erfolgt dabei automatisch oder manuell. Zusätzlich kannst du in den Einstellungen die Anzahl der Tage definieren, für die du Kontoauszüge importieren möchtest.

Damit du deine Kontoauszüge in Xentral importieren kannst, musst du entsprechende Geschäftskonten anlegen. Jedes angelegte Geschäftskonto darf nur mit einem Bankkonto verknüpft werden und umgekehrt. Es könnten sonst doppelte Buchungen auftreten.

> **Anmerkung**
>
> Es ist nicht möglich, nur einige bestimmte Daten zu importieren - es werden stets alle verfügbaren Daten des definierten Zeitraums importiert.

Es gibt zwei wichtige Arten von Geschäftskonten in Xentral zum Import der Kontoauszüge:

- Live Bank Anbindung (empfohlen) - unter Verwendung von finAPI
  Kontoauszüge werden über den BaFin-lizensierten Drittanbieter finAPI unter Anwendung des XS2A- oder FinTS-Standards abgerufen. Du musst keinen zusätzlichen Vertrag abschließen, um finAPI zu nutzen. Die Verwendung von finAPI zum Abrufen deiner Kontoauszüge ist Teil deines Xentral-Pakets.

- Typ: Bank per HBCI/FinTS (HBCI4PHP)
  Immer mehr Banken wechseln vom FinTS/HBCI-Standard auf den XS2A-Standard. Daher empfehlen wir die Nutzung von finAPI, da finAPI beide Standards unterstützt.

In den folgenden Abschnitten erfährst du, wie du

[ein bestehendes HBCI-Geschäftskonto in ein Live Bank Anbindung-Geschäftskonto umwandelst](#UUID-aa9fdcf6-d617-bcfe-7bdf-0c6af1ce7a16_UUID-df91b121-fa9a-aecd-27a5-f407adf4afb0). Diese Option wendest du an, wenn du deine Kontoauszüge bisher über ein HBCI-FinTS-Geschäftskonto abgerufen hast und dieses auf die Nutzung von finAPI ändern möchtest. Deine Einstellungen werden dabei beibehalten (empfohlen).

[ein Live Bank Anbindung-Geschäftskonto anlegst](#UUID-aa9fdcf6-d617-bcfe-7bdf-0c6af1ce7a16_UUID-d93ea48c-0e5c-1772-0a6f-d350938fcf9b). Diese Option wendest du an, wenn du noch kein Geschäftskonto in Xentral zum Abrufen deiner Kontoauszüge angelegt hast und nun deine Kontoauszüge in Xentral abrufen möchtest.

[ein HBCI/FINTS-Geschäftskonto anlegst](#UUID-aa9fdcf6-d617-bcfe-7bdf-0c6af1ce7a16_id_360016722800_id_h_01F9Y9GMJTGCSYADFCP2V79N42)- Diese Option wendest du an, wenn du ein HBCI/FINTS-Geschäftskonto anlegen möchtest. Dabei handelt es sich um eine Legacy-Funktion. Eine Anwendung wird nicht mehr empfohlen.

## Dein HBCI-Konto in ein Live Bank Anbindung-Konto umwandeln

Wenn du bereits ein HBCI-Konto eingerichtet hast, kannst du dieses in einLive Bank Anbindung-Konto umwandeln.

> **Anmerkung**
>
> Der Kontotyp kann nicht mehr zurück geändert werden, sobald du ihn aufLive Bank Anbindunggeändert hast.

Zur Umwandlung deines HBCI-Kontos in einLive Bank Anbindung-Konto gehst du wie folgt vor:

1. Navigiere zuApp Center > Buchhaltung > Geschäftskonten.
1. Wähle das HBCI-Konto, dass du umwandeln möchtest, und klicke auf, um es im Bearbeitungsmodus zu öffnen. Die folgende Meldung wird oben im Bildschirm angezeigt:
  Da das HBCI-Verfahren als Verbindung zu den Banken deaktiviert wird, empfehlen wir dir, auf das PSD2-Verfahren umzusteigen. Dabei bleiben alle existierenden Daten und Konfigurationen erhalten. Die Anbindung im PSD2-Verfahren erfolgt über finAPI. finAPI ist von der BaFin lizenziert, sodass deine Daten absolut sicher sind. Weitere Informationen findest du in den[Allgemeinen Geschäftsbedingungen](https://www.finapi.io/en/data-protection-policy/).

1. Klicke auf Wechsel zur PSD2-Anbindung, um die Autorisierung zu beginnen. Du wirst automatisch zur finAPI-Anmeldeseite weitergeleitet.
1. Gib die Anmeldedaten für dein Onlinebanking in das finAPI-Anmeldeformular ein und folge den Anweisungen. Du musst die Anbindung mit einer TAN autorisieren. Sobald die Verbindung hergestellt ist, kehre nach Xentral zurück.
1. Möchtest du deine Kontoauszüge automatisch importieren, führe Folgendes im Kontodetails-Formular aus:
  - Setze im Bereich Live-Import ein Häkchen bei Live-Import aktiv.
  - Prüfe im Bereich Live-Import deine IBAN und den definierten Importzeitraum im Feld Zugangsdaten. Bei Bedarf kannst du die Anzahl der Tage anpassen, deren Daten zu importieren möchtest.
  - Setze im Bereich Prozessstarter ein Häkchen bei Zahlungseingänge automatisch abholen.
1. Optional: Setze ein Häkchen beipain.001.001.03wenn du eine SEPA XML-Datei im Format pain.001.001.03 erstellen möchtest. Diese Datei kannst du manuell bei deiner Bank hochladen, um die Zahlung von Verbindlichkeiten und Gutschriften einzuleiten.
1. Klicke aufSpeichern.

Die Bezeichnung deines alten Kontos wird beibehalten, der Typ wird jedoch aufLive Bank Anbindunggeändert.

Du kannst dein ehemaliges HBCI-Konto nun wie gewohnt zum Import des Zahlungseingangs verwenden.

> **Warnung**
>
> Wenn du von HBCI zu finAPI (= Live-Banking) umsteigst, achte auf die Überschneidungs-Tage der alten und neuen Anbindung, um Doubletten in den importierten Transaktionen im Import zu vermeiden. Folgende Einstellungen sind wichtig:
>
> - Stelle die letzten abzuholenden Tage auf "1" - so stellst du sicher, dass nur der letzte Tag und nicht weitere zurückliegende Buchungen aus der Vergangenheit neu abgeholt werden.
> - Stelle die Abholung des Bankkontos auf manuell - so stellst du sicher, dass keine Buchungen automatisch abgeholt und versehentlich automatisch verbucht werden.

**Schritte für die Einstellungen bei der Abholung der Buchungen (Duplikate vermeiden): **

1. Um die Überschneidung zwischen HBCI und finAPI sowie die Anzahl der Duplikate so gering wie möglich zu halten, empfehlen wir vorübergehend die Anzahl an Tagen im Feld **Seit (Anzahl in Tagen)** auf “1” zu stellen. Wenn der Import über HBCI bis heute noch gelaufen ist, holst du somit die Buchungen von heute und und gestern ab.
  Hat der Import über HBCI in den letzten vier Tagen bereits nicht mehr funktioniert und keine Buchungen importiert, dann wäre der Wert “4” einzustellen, um die Buchungen der letzten vier Tage abzuholen.

1. Prüfe insbesondere am ersten Tag nach Umstellung den Zahlungseingang auf Duplikate. Falls die Option **Zahlungseingänge automatisch verbuchen** aktiviert ist, empfehlen wir diese Option temporär zu deaktivieren. Somit kannst du sehen, welche Buchungen automatisch gefunden und zugeordnet werden.
1. Buche Duplikate für diesen einen Überschneidungstag im Zahlungseingang auf "Importfehler". **Info**: Erkannte Duplikate zu Aufträgen/Rechnungen mit bereits verknüpften Buchungen, werden orange hinterlegt. Andere Duplikate können wie normale “neue” Buchungen aussehen und werden nicht automatisch als Duplikate gekennzeichnet. Duplikate müssen manuell als Importfehler markiert werden, um doppelte Buchungen zu vermeiden.
1. Nach z.B. 5 Tagen kannst du im Feld **Seit (Anzahl in Tagen)** wieder ein Wert von “5” eintragen. Oder nach 10 Tagen einen Wert von “10”, um wieder einen größeren zurückliegenden Zeitraum abzuholen. Du kannst die Verbuchung der Kontoauszüge nach einigen Tagen wieder auf automatisch umstellen, wenn du keine Duplikate erhalten hast.

![FIN_API_001.png](https://help.xentral.com/hc/article_attachments/13065862369820)

![FIN_API_002.png](https://help.xentral.com/hc/article_attachments/13065862380316)

## Ein neues Live Bank Anbindung-Geschäftskonto anlegen und anbinden

Gehe wie folgt vor, um ein neuesLive Bank Anbindung-Geschäftskonto anzulegen:

1. Navigiere zu App Center > Buchhaltung > Geschäftskonten.
1. Klicke auf +NEU.
1. Klicke auf die Kachel Live Bank Anbindung. Das finAPI-Anmeldeformular wird angezeigt.
1. Gib deine IBAN ein und klicke auf Weiter. Die Kontoanlage wird bestätigt.
1. Klicke auf Weiter. Das Kontodetailformular für dein neuesLive Bank Anbindung-Konto wird angezeigt. Die IBAN wird automatisch in die folgenden Felder eingefügt:
  - Bereich Live-Import > Feld Zugangsdaten
  - Bereich Kontenspezifische Einstellungen > Feld IBAN

Du kannst deine Kontoauszüge auch automatisch importieren.

Gehe wie folgt vor, um deine Kontoauszüge automatisch zu importieren:

1. Scrolle im Kontodetails-Formular runter bis zum Bereich Live-Import und setze ein Häkchen bei Live-Import aktiv. Dadurch wird der Live-Import deiner Kontoauszüge aktiviert.
1. Das Feld Zugangsdaten im Bereich Live-Import enthält deine IBAN sowie die Anzahl an Tagen, die, vom aktuellen Tag an rückwirkend gerechnet, für den Datenimport berücksichtigt werden sollen. Bei Bedarf kannst du Anzahl an Tagen für den Datenimport hier anpassen.
1. Scrolle runter bis zum Bereich Prozessstarter und setze ein Häkchen bei Zahlungseingänge automatisch abholen. Durch Auswahl dieser Option werden deine Bankdaten zu vier verschiedenen Zeiten täglich abgerufen: um 5 Uhr, 9 Uhr, 11 Uhr und 16 Uhr.
1. Klicke auf Speichern.

Optional:

Du kannst die Zahlungsinformationen für ausgehende Zahlungen (Verbindlichkeiten/Gutschriften) aus Xentral dazu verwenden, SEPA-Überweisungen zu initiieren. Weise dafür die entsprechenden Zahlungen im ModulZahlungseingangdemLive Bank Anbindung-Konto zu. Nun kann eine SEPA XML-Datei für den manuellen Upload bei deiner Bank erstellt werden. Einige Banken benötigen diese Datei im Format pain.001.001.03. Um die Datei im korrekten Format zu erstellen, setze ein Häkchen beipain.001.001.03im BereichKontenspezifische EinstellungendeinesLive Bank Anbindung-Geschäftskontos.

### Dein Bankkonto in finAPI autorisieren

Sehr wahrscheinlich hast du deine IBAN noch nicht bei finAPI registriert. Wenn das der Fall ist, erhältst du eine entsprechende Meldung oben in deinem Kontodetails-Formular. Hier findest du auch eine Schaltfläche, die dich direkt zu finAPI weiterleitet.

Du kannst deine IBAN wie folgt bei finAPI registrieren:

1. Klicke in der Informationsmeldung oben in deinem Xentral-Bildschirm auf Konto bei FinApi registrieren. Du wirst zur finAPI-Anmeldeseite weitergeleitet. Die Inhalte der Anmeldeseite hängen von deiner Bank ab; sie kann aber zum Beispiel wie folgt aussehen:
  Bei einigen Banken wirst du für die Anmeldung an deine Bank weitergeleitet.

1. Gib die Onlinebanking-Daten ein und folge den Anweisungen. Du musst die Anbindung mit einer TAN autorisieren.
  Nach der Autorisierung ruft finAPI deine Kontoinformationen ab. Dies kann einige Minuten dauern.

1. Hat finAPI deine Bankinformationen erfolgreich abgerufen, wird eine Bestätigung angezeigt. Nun wähle zwischen den folgenden Optionen:
  - Mit einem Klick auf den blauen, abwärts zeigenden Pfeil neben Importierte Bankkonten kannst du das verbundene Bankkonto prüfen. Deine angebundenen Konten werden angezeigt.
  - Wenn du mehrere Bankkonten für deine Firma nutzt (z.B. zusätzlich Kreditkartenkonten oder abteilungsspezifische Konten), kannst weitere Bankkonten hinzufügen, indem du auf Weitere Konten abrufen klickst.
  - Du kannst zu Xentral zurückkehren, indem du auf Zurück zur Anwendung klickst.
1. Zurück in Xentral klicke auf Speichern.

Deine IBAN ist bei finAPI registriert und du kannst deinLive Bank Anbindung-Geschäftskonto nutzen, um deine Kontoauszüge abzurufen.

Nun kannst du zuBuchhaltung > Zahlungseingangwechseln, wo dein neues Live Bank Anbindung-Konto angezeigt wird. Deinen neuen Zahlungseingang importierst du, indem du auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/6380901532828)

klickst. Das FormularZahlungen importierenwird angezeigt. Klicke aufLive-Import, um den Zahlungseingang zu importieren.

> **Anmerkung**
>
> Es kann sein, dass du die Anbindung von Zeit zu Zeit aus Sicherheitsgründen neu autorisieren musst. Wenn dies der Fall ist, wird dir oben in deinem Kontodetails-Formular eine entsprechende Meldung angezeigt. Klicke auf die Schaltfläche in der Meldung, um dich wieder anzumelden.
>
> Vergiss nicht, deine PIN oder dein Passwort in finAPI zu speichern, wenn du dich nicht jedes Mal bei der Nutzung von finAPI neu anmelden möchtest.

## Ein Bank per HBCI/FinTS (HBCI4PHP)-Geschäftskonto anlegen

> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Abschnitt des Artikels beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

### Einstellungen definieren

Hier kannst du den Typ auf HBCI/FinTS (HBCI4PHP) setzen und die Bankverbindung mit Inhaber, BIC, etc. eingeben.

![BankAccount1.png](https://help.xentral.com/hc/article_attachments/12044601007900)

Folgende Einstellungen kannst du vornehmen:

- **Bezeichnung**: Gib die Bezeichnung deines Kontos ein
- **Typ**: Wähle aus dem Drop-Down Menü einen Kontotyp aus
- **Projekt**: Gib optional ein Projekt an
- **Aktiv**: Durch Anhaken aktivierst du das Konto
- **Keine E-Mail**: Durch Anhaken wird bei Zahlungseingang keine E-Mail an den Kunden gesendet
- **Änderungen erlauben**: Durch Anhaken erlaubst du das nachträgliche Verändern von Kontobuchungen

> **Anmerkung**
>
> Ab Version 21.1 sind in Xentral die Kontotypen **FinTS ** und **HBCI ** in einer Schnittstelle vereint. Die Schnittstelle unterstützt also sowohl**FinTS **, als auch ** HBCI**.

### Live-Import Einstellungen definieren

API: Die PIN/TAN-URL erhältst du auf Anfrage von deiner Bank. Inzwischen besitzen die meisten Produkte ihre eigene Verbindungsdaten(bank).

![BankAccount2.png](https://help.xentral.com/hc/article_attachments/12044601126812)

```
FHP_BANK_URL=>https://urlyourbankissues.de/abc/def;
FHP_BANK_IBAN=>DE1234567890123456789;
FHP_BANK_BIC=>ABCDEF123456;
FHP_ONLINE_BANKING_USERNAME=>123456789;
FHP_ONLINE_BANKING_PIN=>{PASSWORD};
API_DAYS=>10;
LOGGING=>1;
FHP_TAN_VERFAHREN=>photoTAN;
```

Die folgenden Parameter sind besser über ein Beispiel verständlich. Nehmen wir an der letzte Liveimport fand am 01.01.2022 statt und heute ist der 19.01.2022.

Mit dem Parameter **API_DAYS ** wird angegeben, wie lange es dauert bis der nächste Import stattfindet. Es wird ein Zeitraum zwischem dem letzten Import und dem aktuellen Zeitpunkt geschaffen. In unserem Beispiel ist API_DAYS => 10, d.h. beim nächsten Import werden die Daten vom 10.01.22 bis zum heutigen Tag (19.01.22) importiert. Die Tage werden also zum letzten Importdatum hinzu addiert. **API_MAX_DAYS_BEFORE** gibt die Tage an, welche maximale Anzahl an Tagen vor dem letzten Import berücksichtigt werden sollen. Ist API_MAX_DAYS_BEFORE => 90, werden 90 Tage vor dem letzten Import mitberücksichtigt. Das wären in diesem Fall die Daten vom 03.10.2021 bis zum heutigen Tag (19.01.22). Die Tage werden also vom letzten Importdatum abgezogen.

> **Wichtig**
>
> Die Parameter **API_DAYS ** und**API_MAX_DAYS_BEFORE** sind nicht miteinander kompatibel und sollten nicht zusammen in einer Anfrage benutzt werden!

Beim Parameter **API_DAYS_WAIT ** können aktuelle Daten ignoriert werden. Ist API_DAYS_WAIT => 1, dann wird der heutige Tag nicht mit importiert. Dies bedeutet für unser Beispiel, dass nur die Daten vom 01.01.22 bis zum 18.01.22 importiert würden. Die hier angegebenen Tage werden also vom aktuellen Tag abgezogen. **LOGGING ** gibt bei aktiviertem logfile (module=logfile) die Transaktionen beim Abholen der Zahlungseingänge ab. Hier können die Detailstufen 1 bis 5 verwendet werden. **FHP_TAN_VERFAHREN** beinhaltet das TAN Medium über das die TAN generiert wird. Wie genau das Medium heißt, ist abhängig von der TAN Methode, die die Bank zulässt.

> **Anmerkung**
>
> Eine Liste mit FINTS fähigen Banken mit deren URL finden Sie hier:https://hbci4php.web-cloud-apps.com/fints_institute.xls

Beispiele für Bank-URLs:

- Deutsche Bank: [https://fints.deutsche-bank.de/](https://fints.deutsche-bank.de/)
- Postbank: [https://hbci.postbank.de/banking/hbci.do](https://hbci.postbank.de/banking/hbci.do)
- Volksbank Raiffeisenbank: [https://hbci11.fiducia.de/cgi-bin/hbciservlet](https://hbci11.fiducia.de/cgi-bin/hbciservlet)
- Haspa: [https://banking-hh7.s-fints-pt-hh.de/fints30](https://banking-hh7.s-fints-pt-hh.de/fints30)

Sonderfall: Bei der Postbank hat ein Business Konto unter Umständen hinter der neuen Zugangs-ID noch zusätzlich ein Profil hinterlegt. Dieses beginnt mit dem Zeichen #, dann folgen Buchstaben und Zeichen. Damit funktioniert der Live-Import unter Umständen.

```
FHP_BANK_URL=>https://hbci.postbank.de/banking/hbci.do;
FHP_BANK_IBAN=>DE123456789012345678;
FHP_BANK_BIC=>PBNKDEFF;
FHP_ONLINE_BANKING_USERNAME=> (Customer-ID)#XXX;
FHP_ONLINE_BANKING_PIN=>{PASSWORD};
API_DAYS=>7;
```

> **Anmerkung**
>
> Der Live Import ist leider nicht für die Commerzbank, die HypoVereinsbank und die Comdirect Bank verfügbar.

### Passwort setzen

Klicke auf die Schaltfläche **Passwort setzen** und gib das Passwort ein. Das Passwort wird bei der Eingabe verschlüsselt dargestellt und das Feld nach dem Speichern geleert. Wenn du dir nicht mehr sicher bist, ob das Passwort richtig ist, gib es erneut ein. Das Setzen des Passworts ist ein eigenes Recht in der Benutzerverwaltung.

> **Anmerkung**
>
> Das Passwort darf nur 1 Sonderzeichen enthalten, sonst funktioniert der Live-Import nicht. Im API-Code darf die Zeile FHP_ONLINE_BANKING_PIN=>{PASSWORT}; nicht verändert werden, wenn der Passwort-Tresor verwendet wird.

Bitte prüfe, ob in deinem Online Banking die Funktion HBCI + bzw. FinTS oder PIN/TAN aktiviert ist. Diese Funktion kann z.B. bei der Deutschen Bank hier aktiviert werden:

- Services → OnlineSelf Services → TelefonBanking Pin bestellen und HBCI + Freischaltung → HBCI Plus-Nutzung aktivieren (ist aktiviert)

## Einzelbuchungen aktivieren

Sammellastschriften und Verbindlichkeiten können in Xentral im Modul **Zahlungsverkehr** erstellt werden. Dabei werden mehrere Zahlungen zu einer gesammelten Zahlung zusammengefasst.

Diese Zahlungen können durch Xentral wieder in Einzelpositionen aufgelöst werden. Dies ist in den Kontoauszügen in Xentral sichtbar und erleichtert die Zuordnung der Zahlungen zu Aufträgen, Gutschriften und Rechnungen.

Gehe wie folgt vor, um Einzelbuchungen zu aktivieren:

- Für HBCI/FinTS (HBCI4PHP): Setze ein Häkchen bei Einzelbuchungen aktivieren im Bereich Kontenspezifische Einstellungen.
- Für Live Bank Anbindung: Navigiere zum Bereich Live-Import und gib *individual_payments=>1;* in das Feld Zugangsdaten ein.

## Konfiguration von finAPI im Problemfall zurücksetzen

Manchmal kann es zu Verbindungsproblemen oder inkonsistenter Kommunikation zwischen Xentral und finAPI kommen. WennXentral einen solchen Verbindungsfehler feststellt, wird eine Meldung über dem Formular für das Geschäftskonto angezeigt. Klicke in der Meldung aufVerbindung löschen, um deine Konfiguration zurückzusetzen und die Verbindung von Grund auf neu zu konfigurieren. In vielen Fällen werden dadurch die Fehler in der Verbindung behoben.

> **Wichtig**
>
> Dieser Vorgang löscht weder das Geschäftskonto noch die gebuchten Daten! Es wird lediglich die mit dem Geschäftskonto verbundene finAPI-Verbindung zurückgesetzt.
>
> Die Schaltfläche zum Zurücksetzen der Verbindung wird nur angezeigt, wenn ein Fehler aufgetreten ist.

![finapi_resetconnection.png](https://help.xentral.com/hc/article_attachments/13065905664156)

## FAQ

### Warum muss ich mich jeden Tag erneut bei finAPI anmelden?

Falls deine Bank FinTS nutzt, benötigt sie regelmäßig eine starke Authentifizierung von dir, um neue Transaktionen abzurufen. Diese Authentifizierung kann nicht, wie bei XS2A, über einen längeren Zeitraum genutzt werden und du musst dich daher häufig neu anmelden, z.B. täglich. Dieser Prozess ist von deiner Bank abhängig und kann weder von Xentral noch finAPI beeinflusst werden.