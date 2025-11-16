Die API-Anbindung zu PayPal ermöglicht es, Kontoauszüge automatisch in regelmäßigen Intervallen abzurufen und die Zahlungen direkt den entsprechenden Aufträgen und Rechnungen zuzuordnen. Diese Funktion vereinfacht den Abgleich von Prepayments im Auftragseingang und stellt sicher, dass Zahlungen präzise und ohne manuellen Aufwand verbucht werden. Die Transaktionsnummern, Beträge und Order-IDs werden genutzt, um Zahlungen automatisch mit den jeweiligen Aufträgen abzugleichen.

Durch die Integration der PayPal-API werden Kontoauszüge in Echtzeit importiert und automatisch den richtigen Buchungen zugewiesen. Das spart Zeit und reduziert Fehler bei der manuelle Zuordnung von Zahlungen. Zudem ermöglicht die regelmäßige Abholung der Auszüge eine stets aktuelle Übersicht über den Zahlungsstatus.

Wesentliche Funktionen der PayPal-API-Anbindung:

- **Automatisierte Abholung** von PayPal-Kontoauszügen in festgelegten Intervallen. Fallback oder optional CSV Import.
- **Automatische Zuordnung** der Zahlungen zu Aufträgen und Rechnungen basierend auf Transaktionsnummer, Betrag und Order-ID.

## PayPal (API)

Der Live Import der Kontoauszüge (Anbindung an xentral und Abholung der Auszüge per Knopfdruck) ist für Bankkonten mit FinTS und HBCI4PHP sowie PayPal möglich. Hierbei können die Auszüge der letzten X Tage abgeholt werden. Es darf nur ein Benutzer pro Konto hinterlegt werden, da es sonst zu doppelten Buchungen kommt. Bitte legen Sie ein Geschäftskonto nicht mehrfach an. Diese Einstellungen sind nur beim Live-Abholen des Kontoauszuges (z.B. PayPal) relevant. Buchungen können direkt automatisiert per Knopfdruck abgeholt werden.

Folgende Einstellungen sind hier relevant:

- Typ → Konto: PayPal (API)
- Live-Import aktiv → Haken aktiviert den Live-Import (Voraussetzung: korrekte Eingabe der API Daten bei „Zugangsdaten Live-Import)
- Zugangsdaten Live-Import → API Code für den Live-Import (zu finden in Ihrem PayPal Account → Anleitung s.u.)

Diese Felder werden mindestens benötigt:

- **API_USERNAME**→ PayPal API Username (zu finden in Ihrem PayPal Account → Anleitung s.u.)
- **API_PASSWORD**→ PayPal API Passwort (zu finden in Ihrem PayPal Account → Anleitung s.u.)
- **API_SIGNATURE**→ PayPal API Signature (zu finden in Ihrem PayPal Account → Anleitung s.u.)
- **API_DAYS**→ individuelle Einstellungsmöglichkeit (Abholung der letzten X Tage → kann individuell eingestellt werden, dabei ist die tägliche Menge der Transaktionen zu berücksichtigen. bei großen Mengen muss evtl. der Servertimeout umgestellt werden)
- **API_ALLPAYMENTS**→ Optional (kann auch weggelassen werden): Wert "1" bedeutet, dass sowohl Einnahmen, als auch Ausgaben abgeholt werden. Ohne diese Zeile (API_ALLPAYMENTS=>1;) werden nur die Einnahmen abgeholt.
- Mit dem Parameter **API_DAYS=>5;** würde die Abholung vom 20.08.2021 bis heute erfolgen. //Hinzunahme vom Datum der letzen Abholung
- Mit dem Parameter **API_MAX_DAYS_BEFORE=>1;** würde man die Abholung vom 14.08.2021 bis bis heute erfolgen lassen. //Abzug vom Datum der letzten Abholung
- Mit dem Parameter **API_DAYS_WAIT=>1;** würde man die Abholung vom 15.08.2021 bis zum 10.11.2021 erfolgen lassen. //Abzug vom aktuellen Tag

Einzutragen in xentral im Bereich Zugangsdaten Liveimport:

```
API_USERNAME=>XXXXXXX; 
API_PASSWORD=>XXXXX; 
API_SIGNATURE=>XXXXXXXXXX; 
API_DAYS=>5; 
API_ALLPAYMENTS=>1;
```

> **Anmerkung**
>
> Der Pfeil ist ein Gleichzeichen und ein Größer-Zeichen.

Wird die PayPal Rückzahlung aus xentral genutzt, sind folgende Informationen im Geschäftskonto PayPal (API) einzutragen:

- API_CLIENTID
- API_SECRET

Die **ClientID ** und das**Secret** bekommst du in deinem Paypal Live-Account. Generell kannst du entweder eine neue App erstellen oder für eine bestehende App die API Credentials auslesen (AppCenter → Verwalten Sie Ihre Apps → API-Berechtigungen).

> **Anmerkung**
>
> Willst du neben dem PayPal Plus Geschäftskonto auch die PayPal Plus Zahlungsweise in xentral für Zahlungseingänge anbinden, so muss im PayPal Plus Konto ein weiterer API-Einträg generiert werden. Es ist wichtig, dass **API_CLIENTID ** und **API_SECRET ** im Geschäftskonto und in der Zahlungsweise**nicht identisch** sind. Für die API Informationen generierst du einfach 2 Einträge im PayPal Plus Konto unter Rest API → Create App.

![AccPaypal1.png](https://help.xentral.com/hc/article_attachments/11619850339356)

![AccPaypal2.png](https://help.xentral.com/hc/article_attachments/11619836713116)

Der Live-Import holt die Einnahmen der letzten X Tage ab. Ausgaben können auch über den.csv Import eingespielt werden. Bei Ausgaben entstehen bei PayPal sehr viele Querbuchungen (z.B. Prüfungen und Währungsumrechnungen), die im Live-Import und.csv Import nicht ausgefiltert werden. Diese Buchungen können entweder auf ein "Durchlaufende Posten Konto" weggebucht werden oder als Importfehler verbucht werden.

### PayPal API Daten abrufen

Die Daten für die PayPal API erhältst du über dein PayPal Konto. Eine ausführliche Anleitung zur Anforderung einer API-Berechtigung mit Signatur oder Zertifikat findest du[hier](https://www.paypal.com/us/smarthelp/article/how-do-i-request-api-signature-or-certificate-credentials-faq3196).

### Aufruf PayPal-Konto zur Verarbeitung der Kontoauszüge

Sofern das PayPal Konto fertig in xentral eingerichtet ist, können die Kontoauszüge abgerufen werden über: Buchhaltung → Zahlungseingang →

Sollte der PayPal Live-Import per API nicht zur Verfügung stehen, können Sie alternativ den CSV-Import von PayPal wie folgt nutzen.

## PayPal (CSV)

### Manuelles Einspielen von CSV-Dateien

Der Live-Import holt die letzten X Tage ab. Größere Zeiträume können auch manuell eingespielt werden. Folgende Dateien können direkt von Ihrem PayPal Konto heruntergeladen und in xentral (im Zahlungseingang für das Konto: PayPal (API)) eingespielt werden:

Im PayPal Account sind die Dateien hier zu finden: Aktivitäten → Transaktionsliste herunterladen. Hier eignen sich folgende PayPal Export Typen:

- Abgeschlossene Zahlungen (CSV, kommagetrennt) → Geldeingänge/Guthaben z.B. von Shop Payment Transaktionen
- Guthaben-relevante Zahlungen (CSV, kommagetrennt) → Zahlungen von Ihrem PayPal Konto aus PayPalPlus

![paypal_bankanbindung_backend_001.png](https://help.xentral.com/hc/article_attachments/21469413243420)

### Umgang mit Gebühren

PayPal erhebt für jede eingehende Zahlung eine Transaktionsgebühr. Diese Gebühren wirken sich nicht auf den gezahlten Betrag aus, müssen aber in deinem Buchhaltungsexport ausgewiesen werden. InXentral werden die Gebühren separat behandelt und automatisch einem Gegenkonto deiner Wahl zugeordnet.

Um die automatische Zuordnung zu aktivieren, musst du einStandard Gegenkontoin deinem PayPal-Geschäftskonto im BereichKontenspezifische Einstellungeneintragen. Optional kannst du auch eineStandard Kostenstellefür die Gebühren eintragen. Das entsprechende Gegenkonto und Kostenstelle werden imZahlungseingangdann automatisch dem Eintrag für Gebühren zugeordnet.

## PayPalPlus (API)

Analog zu PayPal können über die Kontoeinstellung auch PayPal Plus Auszüge abgeholt werden. Die API Einstellungen werden durch die API Felder ergänzt, so dass die Transaktionsnummern von PayPalPlus ins Bankkonto abgeholt werden.

- Kontoauszug holt man klassisch mit API von Paypal
- Paypal Plus liefert typischerweise nur die TransaktionsID und nicht die PaymentID
- Um diese auch entsprechend korrekt aufzulösen kann man zusätzlich einen PayPal ClientID Account aus PaypalPlus in der Datenstruktur bei Paypal definieren
- Um Kontoauszüge abzuholen, muss man per API API_CLIENTID und API_SECRET definieren
- Anschließend wird automatisch versucht aus der TransaktionsID die PaymentID zu wandeln

Beispielhafte Angabe für PayPalPlus (ausreichend, sofern nur PayPalPlus verwendet wird; wie du deine Client ID und Secret findest kannst du[hier](https://help.xentral.com/hc/de/articles/360016725340#UUID-03f196f3-c6eb-7259-f418-938f7efa7606)lesen):

```
API_CLIENTID=>xXxzeUgKDsabRXBimeYKkLnnMpspMCgAP4HRmo8MHFzBPS;
API_SECRET=>xXxLyf-fPPdyNVAPNj-3wiCvySZafkeBnAKcFkdF6g-5uG8eD97zTog5SPsFY;
```Angabe für PayPalPlus+PayPal (sofern gemischte Zahlungen aus PayPalPlus und PayPal verwendet werden → Fallback für Möglichkeit beide Account-Zahlungsbuchungen):```
API_USERNAME=>meinusername.firma.de; 
API_PASSWORD=>xXxT6Z4EFCVPSL; 
API_SIGNATURE=>xXxafvPMMu5vafX7W3Z32VgvmJqvWcKJ3XQ; 
API_DAYS=>2; 
API_ALLPAYMENTS=>1; 
API_CLIENTID=>xXxzeUgKDsabRXBimeYKkLnnMpspMCgAP4HRmo8MHFzBPS; 
API_SECRET=>xXxxyf-fPPdyNVAPNj-3wiCvySZafkeBnAKcFkdF6g-5uG8eD97zTog5SPsFY;
```

## PayPal-Plus (CSV)

Manuelles Einspielen von.csv Dateien: Der Live-Import holt die letzten X Tage ab. Größere Zeiträume können auch manuell eingespielt werden. Folgende Dateien können direkt von Ihrem PayPal Konto heruntergeladen und in xentral eingespielt werden. Im Hintergrund ist ein festes Format vorgeben, sodass die Transaktionsdatei direkt im Zahlungseingang für das PayPal-Konto importiert werden kann.

### Feldeinstellungen

```
1: Date 

2: Time 

3: Time zone 

4: Name 

5: Type 

6: Status (e.g. Completed) 

7: Subject 8: Currency 

9: Gross (total amount) 

10: Fee (PayPal fee) 

11: Net (amount minus fee) 

12: Note (note of the buyer) 

13: From e-mail address 

14: To e-mail address 

15: Transaction code 

16: Payment type 

17: Counterparty status (e.g. US Verified) 

18: Address status (e.g. Outside USA) 

19: Item description (e.g. Order) 

20: Item number 

21: Amount for shipping costs 

22: Insurance amount 

23: Sales tax 

24: Option 1 - Name 

25: Option 1 - Value 

26: Option 2 - Name 

27: Option 2 - Value 

28: Auction Site 

29: Buyer ID 

30: Item URL 

31: Offer end 

32: Txn reference identifier 

33: Invoice number 

34: Individual number 

35: Receipt number 

36: Credit (PayPal account balance after each payment) 

37: Address line 1 

38: Additional information 

39: City 

40: State/Province/Region/County/Territory/Prefecture/Republic 

41: ZIP CODE 

42: Country 

43: Telephone number
```

## FAQ

### Wie gehe ich vor, wenn beim Live Import von PayPal ein Tag fehlt?

Du kannst folgende Einstellungen prüfen:

- **Abholung der letzten X Tage**→ Erfolgt die Abholung via Schaltfläche, könnte es sein, dass nicht lückenlos abgeholt wurde. Die weiter zurückliegenden Tage kannst du im Bankkonto über die Einstellung der Tage rückwirkend abholen. Sollte die Zeit zu weit zurückliegen, ist ein Nachimport via CSV möglich
- **Prozessstarter für die Abholung**→ Aktiviere den Prozessstarter im PayPal Geschäftskonto in xentral, um die Kontodaten automatisch abzuholen:
  Die Einstellungen sind idealerweise: Abholung der Kontoauszüge 1-2x pro Tag, Abholung der letzten 1-2 Tage (Nimm diese Einstellung im Live-Import des Kontos unter Berücksichtigung der Buchungsmenge vor, ggf. ist auch 1 Tag ausreichend)

- **CSV Import**→ Nachimport der Buchungen aus PayPal über den fehlenden Zeitraum. Bei PayPal ist das Format in xentral bereits eingestellt, die Info für die CSV findest du in der Beschreibung zum PayPal Konto

> **Warnung**
>
> Ein Wechsel zwischen Live-Import und CSV führt ggf. zu doppelten Buchungen. xentral filtert nur komplett identische Buchungen aus. Bei einer Formatänderung der Bank oder des Importkanals kommt es meist zu Abweichungen der Buchungsinformationen, sodass die Buchungen nicht als doppelt erkannt werden. In diesem Fall solltest du den Importzeitraum möglichst ohne Überschneidung wählen. Doppelte Buchungen kannst du auf "Importfehler" buchen.