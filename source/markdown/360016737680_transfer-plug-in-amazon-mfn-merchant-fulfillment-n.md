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

Über die Anbindung von Amazon MFN (Amazon Fulfillment Network) ist es möglich, Aufträge aus Xentral an Amazon weiterzuführen, damit diese über das Amazon Merchant Fulfillment Network (MFN) verschickt werden können. Amazon kann so auch für Nicht-Amazon-Aufträge als Versanddienstleister genutzt werden. Die Übertragung erfolgt auf Grundlage der Lieferscheine.

Für den Einsatz von MFN benötigst du dasÜbertragungen-Modul und die Amazon-Schnittstelle, damit du Lieferscheine an MFN weiterleiten kannst.

## Einstellungen

Die Einstellungen nimmst du imÜbertragungen-Modul vor. Wähle im FeldÜbertragungsformatim BereichKommunikationdie OptionAmazonMfnaus dem Drop-down:

![TransferAmazonMfn_1.png](https://help.xentral.com/hc/article_attachments/4996451726364)

DamitXentral weiß, welcher Amazon Seller Account für MFN angebunden wird, musst du den passenden Amazon-Shop verknüpfen. Wähle den Shop, den du mit dem Amazon Fulfillment zusammen verwenden möchtest, im FeldAmazon Shopim BereichÜbertragungsspezifische Einstellungenaus.

![TransferAmazonMfn_2.png](https://help.xentral.com/hc/article_attachments/4996433766812)

## Prozessstarter

Die Rückmeldungen von Amazon werden von den Prozessstartern Amazon und API Übertragungen abgeholt. Stelle sicher, dass die erforderlichen Prozessstarter aktiv sind, andernfalls können keine Übertragungen ausgeführt werden.

## Arbeitsablauf

### Exportlieferungen

Zollwerte werden bei Exportlieferungen automatisch mit übergeben. Diese werden direkt aus den Lieferscheinen gezogen. Falls im Lieferschein keine Zollwerte hinterlegt sind, werden die Werte aus dem Auftrag verwendet.

### Monitoring

Sichte regelmäßig den Monitor im ModulÜbertragungen. Mögliche Fehlermeldungen werden dort dargestellt. Wenn z.B. die SKU fehlt, eine Datenzeile nicht korrekt befüllt ist o.Ä., wird unterÜbertragungen → Monitoreine Logeintrag mit Fehler erzeugt:

![TransferAmazonMfn_3.png](https://help.xentral.com/hc/article_attachments/4996440458396)

## Voraussetzungen

Grundsätzlich können nur Aufträge übermittelt werden, deren Positionen bei Amazon bekannt sind und die über ausreichend Bestand verfügen.

Um dies sicherzustellen, berücksichtige bitte die Informationen aus dem[Amazon-Artikel](https://help.xentral.com/hc/articles/360016809939).