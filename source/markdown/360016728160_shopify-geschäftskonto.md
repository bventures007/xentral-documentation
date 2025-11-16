## Shopify Payments per API

Die Zahlungen von Shopify Payments können direkt über eine API-Schnittstelle via Live-import abgeholt werden. Trage hierzu die Shopify-Zugangsdaten in das Bankkonto ein. Das Konto muss den Typ Konto: Shopify (API) erhalten.

> **Anmerkung**
>
> Damit das Shopify Payments Geschäftskonto korrekt funktioniert, muss es schon mindestens einen Payout (Überweisung von Shopify Payments auf das eigene Bankkonto) gegeben haben. Einzelne Transaktionen reichen nicht aus.
>
> Wenn die Zahlungen über die API importiert werden, werden die Zahlungen über die Auftragsnummer (Internetnummer in xentral) abgebildet.

![AccountShopify1.png](https://help.xentral.com/hc/article_attachments/6577131545500)

### Live Import Zugangsdaten

Bei den Live-import Zugangsdaten folgende Felder eingeben und mit Ihren Shopify Zugangsdaten befüllen:

- SHOP=>https://shop.myshopifyshop.de;** > bitte hier die eigene Shop-URL Ihres Shopify Shops eintragen.

Bei der Anbindung von mehreren Shopify Payments musst du darauf achten, dass du die Konfiguration "Zu Zeiten" versetzt machst, ansonsten spricht die API nur mit der Ersten.

Beispiel:

Konto_1 zu Zeiten 00,02,04,06,08,10,12,14,16,18,20,22

Konto_2 zu Zeiten 01,03,05,07,09,11,13,15,17,19,21,23

- USER=>Benutzername; > bitte hier den API KEY aus Ihrem Shopify Shop eintragen
- DAYS=>2; > optional, die Anzahl der Tage, die abgeholt werden sollen. Ansonsten werden standardmäßig 5 Tage abgeholt, aber dieser Wert kann auch angegeben werden: DAYS=>5;

![AccountShopify2.png](https://help.xentral.com/hc/article_attachments/6577115299100)

Folgende Keys können verwendet werden.- SHOP: SHOP, URL

- SHOP: SHOP, URL
- USER: USER, USERNAME, USER_NAME
- DAYS: DAYS, TAGE

### Einstellungen in Shopify

Damit Zahlungen für Shopify in Xentral abgerufen werden können, müssen einige Berechtigungen in Shopify Payments erteilt sein. Xentral benötigt Lesezugriffe für Auszahlungen, Bankkonten und Konten auf Shopify Payments.

![AccShopify3.png](https://help.xentral.com/hc/article_attachments/15492810701980)

Außerdem sind noch weitere Lesezugriffe notwendig. Dazu muss auf “Inaktive Admin-API-Berechtigungen anzeigen” geklickt werden und dort allen Rechten Leserechte gegeben werden.

![AccShopify4.png](https://help.xentral.com/hc/article_attachments/15492810743068)

> **Anmerkung**
>
> Damit das Shopify Payments Geschäftskonto korrekt funktioniert, muss es schon mindestens ein Paypot, d.h. eine Überweisung von Shopify Payments auf das eigene Bankkonto, gegeben haben. Einzelne Transaktionen reichen hier nicht aus.

### Status abgeholter Buchungen

Der Live Import von Shopify Payments-Buchungen importiert ausschließlich Buchungen mit dem Status "paid", da die API nur den Import eines bestimmten Status erlaubt. Vorgemerkte Buchungen ("scheduled", "in transit") oder stornierte ("canceled") Buchungen werden nicht abgeholt.

### Fehlermeldung bei Live-Import (Verbindungsprobleme)

Bitte prüfen Sie, ob die Daten korrekt eingegeben wurden oder sich ggf. bei Shopify ein User oder ein Passwort etc. geändert hat. Ggf. hat der User auch die Berechtigung nicht zuzugreifen.

## Shopify Payments per CSV

Alternativ können die Buchungen von Shopify Payments manuell per CSV-Datei eingespielt werden. Beispiel für eine Shopify Payments CSV:

![AccShopify6.png](https://help.xentral.com/hc/article_attachments/15492873077148)

## Kontoauszug Import

Der Import der Shopify Payments ist sowohl als Live Import als auch als CSV-Import möglich. Die Order Nummer wird zur Zuordnung der Shopbestellungen verwendet.

## Bekannte Probleme

Shopify bietet die Möglichkeit die Einnahmen sowohl wöchentlich als täglich auszahlen zu lassen. Bei einer monatlichen Auszahlung kann der Live Import auf Fehler laufen, da die zu abholende Datenmenge zu groß ist. Daher ist eine tägliche Auszahlung empfohlen.

## Mit Gebühren umgehen

Beim Live-Import werden die Gebühren im Zahlungseingang nicht angezeigt. Auch beim CSV-Import werden die Gebühren nur zu Informationszwecken angezeigt und nicht automatisch addiert und mit berechnet. Im Buchhaltungsexport fehlen deshalb die Gebühren.

Die Gebühren findest du auf dem Shopify Kontoauszug in einer Summe. Diese kann z.B. als separate Buchung von Hand monatlich gebucht werden. Die Buchung kannst du unterZahlungseingang > Kontenblattim BereichBuchungam unteren Ende der Seite vornehmen.

Du siehst im Anschluss eine neue Zeile unterZahlungseingang > Konto: Shopify > Import, die du dann mitBuchungen fertigstellenabschließen kannst.

## Shopify Refund (Rückzahlungen mit Shopify)

Über unsere Connect-Schnittstelle ist es möglich, Gutschriften nach Freigabe automatisch als Rückzahlung an Shopify Pay zu übergeben und dem Kunden auszuzahlen. Mehr Informationen, wie du die Rückzahlungs-Funktion im Shopify Connector einrichtest und aktivierst, findest du[hier](https://help.xentral.com/hc/de/articles/13235060220444-Shopify-Connector-Workflows-konfigurieren#UUID-55e1cf94-dd5f-eb68-4337-cabda5e7ee49_UUID-601e9bbb-690a-13c9-0176-7ba5c3dd1da8).

> **Anmerkung**
>
> Beachte: Shopify Refund steht nur in Xentral Connect, nicht im klassischen Shop-Importer, zur Verfügung.