## Stripe (API)

Für Stripe können Live-Importe eingestellt werden. Darüber hinaus können auch Rückzahlungen von Stripe via API importiert werden.

![AccStripe1.png](https://help.xentral.com/hc/article_attachments/15492894967708)

![AccStripe2.png](https://help.xentral.com/hc/article_attachments/15492895021852)

Die Payouts können über den Schalter API_SKIPPAYOUTS=>1; ausgelassen werden. Dadurch werden diese nicht abgeholt.

### API Key eintragen

Unter[https://dashboard.stripe.com/account/apikeys](https://dashboard.stripe.com/account/apikeys)können Sie die API Keys einsehen. Der Secret Key wird benötigt, damit Xentral die Zahlungen von Stripe abholen kann. Im Geschäftskonto unter dem Punkt Live-Import können Sie diesen wie folgt eingeben:

API_USERNAME=>sk_live_xxxxxx;API_DAYS=>3;API_ALLPAYMENTS=>1;USE_PAYMENT_INTENT=>1;

- API_USERNAME → Secret Key aus dem Stripe Dashboard
- API_DAYS → Zahlungen aus vergangenen x Tage abholen
- API_ALLPAYMENTS → Kann 0 oder 1 sein. Bei 0 werden nur die Einzahlungen importiert. Wird der Parameter hingegen auf 1 gesetzt, werden auch Rückzahlungen importiert.
- USE_PAYMENT_INTENT=>1; → Als Buchungstext wird die last_trans_id eingetragen.

## Stripe (CSV)

| id | Description | Created (UTC) | Amount | Amount Refunded | Currency Converted | Amount Converted | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Amount Refunded | Fairy | Tax Converted | Currency | Fashion | Status | Statement | Descriptor | Customer ID |
| Customer Description | Customer Email | Captured | Card ID | Card Last4 | Card Brand | Card Funding | Card Exp Month | |
| Card Exp Year | Card Name | Card Address | Zip | Card Issue Country | Card Fingerprint | Card CVC Status | | |
| Card AVS Zip Status | Card AVS Line1 Status | Card Tokenization Method | Disputed Amount | | | | | |
| Dispute status | Dispute Reason | Dispute Date (UTC) | Dispute Evidence Due (UTC) | Invoice ID | Payment Source | | | |
| Type | Destination | Transfer | Interchange Costs | Merchant | Service Charge | Transfer Group | email (metadata) | |
| order_id (metadata) | | | | | | | | |