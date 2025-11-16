Mit dieser Schnittstelle kannst du Xentral mit Amazon verbinden, um Bestellungen von dort in Xentral zu importieren und deine bei Amazon verkauften Artikel in Xentral zu verwalten. Die Anbindung geschieht über eine API-Schnittstelle (Shopimporter).

Als Verkäufer bei Amazon stehen dir prinzipiell zwei unterschiedliche Arbeitsweisen zur Verfügung:

- Fulfillment by Merchant (FBM): Du versendest deine Ware aus deinem eigenen Lager.
- Fulfillment by Amazon (FBA): Amazon versendet die Ware für dich.

Beide Arbeitsweisen lassen sich mithilfe der Amazon Schnittstelle in Xentral abbilden:

- Bei einem Versand aus dem eigenen Lager werden die Aufträge abgeholt und durchlaufen danach den gesamten Versandprozess in Xentral, wobei neben einer Rechnung auch ein Lieferschein und - wenn gewünscht - eine Paketmarke erzeugt werden.
- Bei einem FBA Auftrag hingegen erkennt die Schnittstelle, dass du keinen physischen Versand durchführen musst, sodass lediglich eine Rechnung erzeugt wird, die deinem Kunden automatisch per Email zugestellt werden kann, wenn du dies wünschst.

Aufgrund der Konzeption der Schnittstelle kannst du auch ein Geschäftsmodell aus kombinierten Versandarten in Xentral abbilden, da für jeden Auftrag automatisch der richtige Prozess angestoßen wird.

## Typische Anwendungsfälle

- Du verkaufst deine Artikel bereits auf anderen Plattformen, möchtest aber auch auf Amazon verkaufen (FBM / FBA). Mit Xentral kannst du deinen Warenbestand plattformübergreifend abgleichen. Außerdem kannst du zum Versenden in Xentral automatisiert Bestellungen nach Status importieren und den Status für den Versand zurückmelden.
- Du verkaufst ausschließlich auf Amazon (FBM). MitXentral kannst du deine Prozesse optimieren, indem du Lagerverwaltung und Autoversand nutzt.

## Features der Schnittstelle **Enthaltene Funktionalitäten**

Mit dem Amazon Shop Importer kannst du

- Aufträge von Amazon (Marktplätzen) nach Xentral importieren
- Statusinformationen samt Tracking-Nummer und Versanddienstleister zu Amazon (nur FBM) zurück übermitteln
- Lagerzahlen zu Amazon übermitteln
- Rechnungen hochladen (FBA/FBM)
- Amazon VAT Services nutzen
- den [Status deiner Schnittstelle und des Seller Central-Kontos via System Health prüfen](https://help.xentral.com/hc/de/articles/22381438026524#UUID-2bd545a6-423c-98f9-397c-858c57e1d552_UUID-c0b5c595-7f8d-6080-5cd7-7b5c2646bc25)

**Nicht enthaltene Funktionalitäten**

Folgende Aktionen sind nicht möglich:

- Vollumfängliches Hochladen von Artikeldaten (inkl. Preisen) zu Amazon
- Verwendung von Just-in-Time Stücklisten &amp; FBA
- Übermittlung von Gutschriften (FBM) an Amazon
- Unterstützung des Amazon Advantage Programms

## Es kann losgehen...

- [Amazon-Schnittstelle anbinden (Classic)](https://help.xentral.com/hc/de/articles/6124566016540#UUID-c9a61828-5de0-1813-66dc-7851e3d0b425): Schau dir diesen Guide an, um die Amazon Schnittstelle erstmalig zu verbinden.
- [Amazon (Classic): Shop Einstellungen](https://help.xentral.com/hc/de/articles/22381409575068#UUID-53655238-f9be-6f6b-34b7-6f5518d9a875): Besuche diese Seite, um mehr über die Einstellungen der Schnittstelle zu lernen.
- [Amazon (Classic): Workflows](https://help.xentral.com/hc/de/articles/22381416567196#UUID-9c9ef210-f01a-af88-ad63-f2ef8b412a35): Konsultiere diesen Bereich, um mit verschiedenen Workflows vertraut zu werden.
- [Amazon (Classic): Spezialanwendungen & sonstige Einstellungen](https://help.xentral.com/hc/de/articles/22381438026524#UUID-2bd545a6-423c-98f9-397c-858c57e1d552): Klicke hier für mehr Spezialwissen und FAQs sowie um die System Health der Schnittstelle zu verstehen.