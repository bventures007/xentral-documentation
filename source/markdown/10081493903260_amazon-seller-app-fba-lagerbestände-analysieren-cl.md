Die Amazon Seller App erlaubt es dir, deine Artikeldaten (FBA - Fulfillment by Amazon/ FBM - Fulfillment by Merchant) und Lagerinformationen bei Amazon (nur FBA) an einem Ort zu verwalten und zu analysieren. Die App sammelt Daten über deine Bestände und den Lagerstandort deiner Produkte. Sie unterstützt dabei auch Läger in anderen europäischen Ländern (Pan-European FBA).

## Voraussetzungen

Bevor du die Amazon Seller App nutzen kannst, musst du sie zuerst einrichten. Dafür benötigst du Folgendes:

- Eine aktive Amazon-Schnittstelle, die [angebunden](https://help.xentral.com/hc/de/articles/6124566016540#UUID-c9a61828-5de0-1813-66dc-7851e3d0b425) und [konfiguriert](https://help.xentral.com/hc/de/articles/360016809939#UUID-c3dae2f2-8585-e44a-d7ae-9c5dec401a21) ist.
- Ein Lager ohne Lagerplätze. Dieses Lager sollte nur für Amazon FBA genutzt werden. Der Name des Lagers muss Amazon sein.
- Artikel, die über Amazon FBA synchronisiert werden sollen, dürfen nicht als "Just-in-time Stückliste" markiert sein.

## Set up Amazon Seller App

To set up the Amazon Seller App:

1. Go to Settings > Integrations > Amazon Seller App.
1. Select your Amazon shop interface in the Shop drop-down menu. Only connected interfaces are displayed here.
1. Select the warehouse without storage locations with the name Amazon in the Warehouse drop-down menu. The needed storage locations will automatically be created after the app is set up. This warehouse should only be used for Amazon FBA.
  You can find out more about the process in the [Lagerbestände zwischen mehreren EU-Ländern synchronisieren - Pan-European FBA](#UUID-bdf78785-1f98-024a-adc7-932e25426302_N1689944834141) section.

## Mit der Artikeltabelle arbeiten

Die Artikeltabelle enthält eine Übersicht all deiner Artikel bei Amazon und bietet dir die Möglichkeit sie zu sortieren, auf unterschiedliche Weise zu filtern und einzelne Spalten zu verbergen oder anzuzeigen. Weitere Informationen zur Arbeit mit Übersichtstabellen findest du[hier](https://help.xentral.com/hc/de/articles/6576078844572#UUID-b2789dbc-7d05-ab0c-fb22-b7f0c7927e49).

Die Tabelle zeigt dir den Artikel mit seinerASIN,Art der Listung(FBA oder FBM),SKU Amazon,SKUXentral und seinemLagerplatzan. Der Lagerplatz ist wichtig für Pan-European FBA.

![amazonsellerapp_table.png](https://help.xentral.com/hc/article_attachments/10530667215772)

## SKU Amazon mit SKU Xentral verknüpfen

Um eine korrekte Synchronisierung zwischen Amazon und Xentral zu gewährleisten, müssen die SKUs miteinander verknüpft werden. Die Verknüpfung ist dann korrekt, wenn sowohl die Spalten für SKU Amazon als auch die für SKUXentral gefüllt sind.

Falls die Spalte für SKUXentral leer ist, kannst du die SKU folgendermaßen verknüpfen.

1. Bewege die Maus über den Artikel, den du verknüpfen möchtest, und klicke auf das -Symbol, welches auf der rechten Seite erscheint.
1. Gib die Artikelnummer in Xentral in das Suchfeld ein und wähle deinen Artikel aus. Falls der Artikel in Xentral nicht existiert, kannst du ihn anlegen, indem du auf Neuen Artikel hinzufügen klickst.
1. Klicke auf Verknüpfen.

Beide Spalten sind nun gefüllt und die SKUs verknüpft. Dadurch werden auch die Einträge im Reiter[Fremdnummern](https://help.xentral.com/hc/de/articles/360016758199#UUID-be6a2725-3071-98cf-ad2e-1a9016c503cc)im Artikel, den du gerade verknüpft hast, aktualisiert.

Klicke auf![mapping_icon.png](https://help.xentral.com/hc/article_attachments/10081494261148)

, um die Verknüpfung rückgängig zu machen. Klicke anschließend aufVerknüpfung aufheben.

## Lagerbestände zwischen mehreren EU-Ländern synchronisieren - Pan-European FBA

Amazon ermöglicht es dir, deine Artikel in seinen Lägern in verschiedenen EU-Ländern zu lagern. Dieser Prozess wird als Pan-European FBA bezeichnet. Er kann deine Versandkosten verringern und deine Lieferzeiten verkürzen, falls du direkt in dem Land verkaufst, in dem du deine Artikel lagerst.

> **Anmerkung**
>
> Pan-European FBA unterscheidet sich von Amazon EFN (European Fulfillment Network). Bei EFN lagerst du deine Artikel in einem EU-Land und verschickst sie von dort in den Rest der EU. Falls du in UK verkaufen möchtest, benötigst du dort ein weiteres Lager. Bei Verwendung von EFN zeigt Xentral nur EU oder UK als Lagerplatz an.

Dieser Prozess führt jedoch dazu, dass sich deine Meldepflichten für die Umsatzsteuer ändern. Lagerst du deine Artikel in nur einem Land, so benötigst du auch nur eine USt-ID (Umsatzsteueridentifikationsnummer). Lagerst du deine Artikel in mehreren Ländern, so benötigst du eine USt-ID für jedes Land, in dem du deine Artikel lagerst.

Außerdem solltest du wissen, wo deine Artikel in welcher Menge gelagert werden und ob sie sich in einem verkaufsfähigen Zustand befinden. Die paneuropäische Lagersynchronisierung sammelt diese Daten für dich und funktioniert auf die folgende Weise:

1. Xentral importiert alle FBA-Artikel und sortiert sie nach Land und Zustand.
1. Diese Artikel werden dann in dem von dir in der [Einrichtung](#UUID-bdf78785-1f98-024a-adc7-932e25426302_section-idm4657506640604833798817479001) gewählten Lager hinterlegt. Dieses Lager hat zwei Lagerplätze pro Land: eines für verkäufliche (sellable) und eines für unverkäufliche Artikel (unsellable). Unverkäufliche Artikel sind z.B. Artikel, die im Versandprozess beschädigt wurden oder Retouren.
1. Diese Lagerplätze werden automatisch angelegt und sind wie folgt benannt: FBA-[Land]-[Zustand], z.B. ist FBA-FR-sellable der Lagerplatz für deine verkäuflichen Artikel in Frankreich.

Der Lagerplatz wird in der Artikeltabelle angezeigt.

## Anlieferung zu Amazon (in transit)

Du kannst den Lagerbestand der Artikel, die sich in Anlieferung zu Amazon befinden (=**in transit **) mit der ** Amazon Seller App**sehen.

Der Status der Anlieferung ist im Report von Amazon verfügbar und wird in Xentral ausgegeben.

- Wenn du z.B. 100 Kaffeetassen bei Amazon im Lager hast, wird beim entsprechenden Artikel "Kaffeetasse" in Xentral im Lager "Amazon" die Menge "100 Stck." auf dem Lagerplatz z.B. "AMAZON-PL" (= Amazon Lager Polen) angezeigt.
- Es wird eine Buchung im jeweiligen Artikel erzeugt. Bucht Amazon 50 Stück um, wird in dem Artikel eine erneute Buchung erzeugt: "- 50 Stck." von Lager "Amazon" / "Lagerplatz AMAZON-PL" - In Transit.

> **Anmerkung**
>
> Die Daten sind nicht "Echtzeit". Der Report wird nur einmal pro Tag nachts übertragen (= 1 Uhr nachts mitteleuropäische Zeit).