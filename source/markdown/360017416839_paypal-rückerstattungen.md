In Xentral ist es möglich, eine getätigte Zahlung zu stornieren und eine Rückerstattung (auch Rückzahlung oder Refund genannt) zu veranlassen.

Dieses Modul ist besonders relevant für alle, die eine Zahlung per PayPal anbieten.

## Voraussetzungen

Damit eine Rückerstattung per Paypal erfolgen kann, muss eine Gutschrift vorliegen und Paypal als API Geschäftskonto angebunden sein. Im Geschäftskonto muss dafür unbedingt folgende Info gepflegt sein:

API_CLIENTID =>

API_SECRET=>

Das gilt für das Geschäftskonto PayPal Plus und für normales Paypal. Ohne diese Info kann die PayPal Rückerstattung nicht ausgeführt werden. Eine Anleitung, wo diese Informationen erstellt werden können, ist[hier](https://help.xentral.com/hc/en-us/articles/360016725340-Payment-method-PayPal-Plus)zu finden.

> **Anmerkung**
>
> Willst du neben dem PayPal Plus Geschäftskonto auch die PayPal Plus Zahlungsweise in Xentral für Zahlungseingänge anbinden, so muss im PayPal Plus Konto ein weiterer API-Einträg generiert werden. Es ist wichtig, dass **API_CLIENTID ** und **API_SECRET ** im Geschäftskonto und in der Zahlungsweise**nicht identisch** sind. Für die API Informationen generierst du einfach 2 Einträge im PayPal Plus Konto unter Rest API > Create App.

## Rückerstattung tätigen

Im ersten Schritt sind die Gutschriften unter **Buchhaltung > Zahlungsverkehr** zu laden.

Es besteht auch die Möglichkeit direkt aus der Gutschrift in den Zahlungsverkehr zu springen. Dies ist in der Gutschrift über das Aktionsmenü möglich. Hier ist die Option **Zahlung erstatten** auszuwählen.

Anschließend erscheint die Seite mit dem Zahlungsverkehr.

Dann ist unter dem Bereich **Aktion ** auf die Schaltfläche**Gutschriften laden** zu klicken. Anschließend erscheinen diese in der Übersicht und können ausgewählt werden.

![PaypalRefunds1.png](https://help.xentral.com/hc/article_attachments/15492830821532)

Über die Stapelverarbeitung ist dann das Paypal Konto im Dropdown auszuwählen, bevor auf die Schaltfläche **Zahlungen zuordnen und freigeben** geklickt werden kann.

Im nächsten Schritt erscheinen die zuvor ausgewählten Gutschriften im Reiter **Konto: Paypal ** Hier können dann die Gutschriften, für die eine Rückerstattung erfolgen soll, ausgewählt werden. Über die Schaltfläche**Zahlung ausführen** kann die Zahlung ausgeführt werden.

> **Anmerkung**
>
> Aktuell muss die Transaktionsnummer des Auftrags noch manuell hinterlegt werden (siehe nächster Punkt).

### Spalte: Menü

Hier können in der Liste unter der Spalte **Menü** verschiedene Aktionen durchgeführt werden.

- Mit dem **Stift**

-Symbol kann der Zahlungsempfänger, der Betrag sowie die Währung überprüft und verändert werden. Außerdem kann hier die Transaktionsnummer vom Auftrag hinterlegt werden.
- Über das **X** kann die Gutschrift aus dem Paypal Konto storniert werden.
- Über den **gebogenen Pfeil** kann direkt in die Gutschrift gesprungen werden.
- Über das **PDF**

-Symbol wird die PDF der Gutschrift angezeigt.

### Minidetail

Über das Minidetail können alle Details der Gutschrift eingesehen werden.

![PaypalRefunds2.png](https://help.xentral.com/hc/article_attachments/15492863162140)

#### Fehlermeldungen **PaypalApi: Forbidden NOT_AUTHORIZED: Authorization failed due to insufficient permissions ** Sollte diese Fehlermeldung erscheinen, muss im Geschäftskonto ein neues Api-Secret und eine neue Api-ClientID erstellt werden. **Client Authentication failed ** Bei dieser Fehlermeldung bitte sicherstellen, dass API_CLIENTID und API_SECRET ausschließlich im Geschäftskonto verwendet werden und nicht bspw. auch in den Zahlungsweisen für PayPal Plus (hier benötigt man zwei separate API Accounts). **PaypalApi: Not Found RESOURCE_NOT_FOUND: The specified resource does not exist ** Wenn diese Fehlermeldung auftritt, wurde versucht eine Rückzahlung zu tätigen, deren ursprüngliche Zahlung nicht über PayPal eingegangen ist. Das ist im Feld **Verwendungszweck** erkennbar, da hier immer die PayPal TransaktionsID der ursprünglichen Zahlung übernommen wird. Der Fehler tritt auf, wenn es sich hierbei nicht um eine PayPal Transaktions ID handelt.