Die korrekte Konfiguration für die Rechnungsabwicklung mit Amazon kann herausfordernd sein. Hier stellen wir sinnvolle Einstellungen für die verschiedenen Szenarien vor.

## Szenario 1: VCS (Vat Calculation Service)

Die komfortabelste Variante ist die Nutzung des VCS Services. Hier erstellt Amazon deine Rechnungen und du hast den geringsten Konfigurationsaufwand. Stelle zuerst sicher, dass du den[VCS Service in Amazon Seller Central aktiviert hast](https://help.xentral.com/hc/de/articles/7911527325852#UUID-8dbe2247-fec2-704a-56b3-6cd4c4c4d215). Rechnungen und Gutschriften nutzen bei VCS den Nummernkreis von Amazon. Eine Rechnungsnummer aus dem Xentral-Nummernkreis solltest du aus legalen Gründen nicht nutzen.

Wähle im Abschnitt Invoice Handling den Service VCS (download invoice data). Beachte, dass du die Steuersätze der Lieferländer gepflegt hältst. Weitere Informationen zu Steuersätzen erhälst du[hier](https://help.xentral.com/document/preview/32603#UUID-59cbbaff-f1d6-4853-535c-7ce6837ffe79).

![Amazon_InvoiceHandling_VCS.png](https://help.xentral.com/hc/article_attachments/18590723138076)

> **Anmerkung**
>
> Es ist nicht möglich bei aktiviertem VCS eigene Rechnungen hochzuladen (VCS Lite).

## Szenario 2: IDU (Invoice Document Uploader)

Wenn du deine eigenen Rechnungen zu Amazon hochladen möchtest, stelle sicher, dass du den Amazon VCS Service in der Amazon Seller Central deaktiviert hast. Dann kannst du Rechnungsnummern aus dem Xentral-Nummernkreis nutzen und die Rechnungsdokumente in Amazon hochladen.

Wähle im Abschnitt Invoice Handling den Service **IDU (invoice upload service)** und nimm die entsprechenden Einstellungen in den weiteren Feldern vor:

![Amazon_InvoiceHandling_IDU.png](https://help.xentral.com/hc/article_attachments/18590713163164)

## Szenario 3: Drittanbieter

Nutzt du einen Drittanbieter wie Amainvoice für die Erstellung der Rechnungen, dann wähle als Service **None / Amainvoice** und setze die Haken nach deinem Bedarf:

![Amazon_InvoiceHandling_NoneAmainvoice.png](https://help.xentral.com/hc/article_attachments/18590723141916)