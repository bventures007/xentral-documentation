Mit dem extra Modul "Paypal Plus" können Sie in den Zahlungsweisen als Typ Paypal Plus auswerten. Dadurch bekommen Aufträge, die mit dieser Zahlungsweise vom Shop importiert werden, einen speziellen Freitext auf dem Rechnungsbeleg ausgegeben wenn benötigt bei Rechnungskauf.

- Angabe von Client und Secret ID
- Xentral blendet auf der Rechnung Kontodaten / Zahlungsinformationen von PayPal Plus ein, falls vorhanden

Informationen zur Anbindung von Paypal Plus als Geschäftskonto sind[hier](https://help.xentral.com/hc/de/articles/360016721920#UUID-5b7950ea-43de-e5a2-45a6-d9e4455abe51)zu finden. Damit können Kontoauszüge abgeholt werden.

> **Anmerkung**
>
> Willst du neben der PayPal Plus Zahlungsweise auch das PayPal Plus Geschäftskonto in xentral für Zahlungseingänge anbinden, so muss im PayPal Plus Konto ein weiterer API-Einträg generiert werden. Es ist wichtig, dass **API_CLIENTID ** und **API_SECRET ** im Geschäftskonto und in der Zahlungsweise**nicht identisch** sind. Für die API Informationen generierst du einfach 2 Einträge im PayPal Plus Konto unter Rest API → Create App.

## Einstellungen aus PayPal

1. Einloggen unter https://developer.paypal.com/developer/applications
1. Zum Punkt REST API im Dashboard scrollen und eine App "PayPal Plus" erstellen
1. In der obigen Oberfläche klicken Sie dann auf die erstellte "PayPal Plus" App.

> **Wichtig**
>
> Im PayPal-Backend muss unbedingt der Live-Modus für den Produktiveinsatz aktiviert werden. Im Sandbox-Modus ist keine funktionierende Anbindung an Xentral möglich.

Wichtige Werte sind hier:

- Client ID
- Secret → Hier muss erst auf "Show" geklickt werden

## Einstellungen in xentral

Unter Administration → Einstellungen → Zahlungsweisen → NEU können Sie eine neue Zahlungsweise für PayPal Plus anlegen.

Als Text sollte hinterlegt sein (HÄNDLERNAME mit Firmenname ersetzen):

HÄNDLERNAME hat die Forderung gegen Sie im Rahmen eines laufenden Factoringvertrages an die PayPal (Europe) S.àr.l. et Cie, S.C.A. abgetreten. Zahlungen mit schuldbefreiender Wirkung können nur an die PayPal (Europe) S.àr.l. et Cie, S.C.A. geleistet werden.

## Abbildung auf Belegen

Sobald ein Auftrag mit dieser Zahlungsweise vom Shop kommt, wird automatisch:- Der spezielle Zahlungstext via API in den sogenannten Systemfreitext des Belegs im Hintergrund gespeichert

- Dieser wird auf den Belegen unterhalb der Artikeltabelle ausgegeben