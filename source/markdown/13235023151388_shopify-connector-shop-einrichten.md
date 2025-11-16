Wenn du bisher noch keinen Shop im Einsatz hattest und ganz von Anfang startest, möchten wir dich an das Helpcenter von Shopify verweisen. Dort findest du die ausführlichen und aktuellen Anleitungen zu jedem Thema im Shop. An dieser Stelle hier schneiden wir nur die für die Anbindung relevanten Themen kurz an. Nimm bei der Vorbereitung des Shops gern die folgende Checkliste als Grundlage:

- [Shop anlegen](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_id_ShopifyConnectorShopeinrichten-ShopanlegenShopAnlegentrue)
- [Vertriebskanal anlegen](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_id_ShopifyConnectorShopeinrichten-VertriebskanalanlegenVertriebskanalAnlegentrue)
- [Standort anlegen und Inventar verwalten](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_id_ShopifyConnectorShopeinrichten-StandortanlegenundInventarverwaltenStandortAnlegentrue)
- [Zahlungsmethode anlegen](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_id_ShopifyConnectorShopeinrichten-ZahlungsmethodeanlegenZahlungsmethodeAnlegentrue)
- [Versandtarif und Zustellmethode anlegen](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_id_ShopifyConnectorShopeinrichten-VersandtarifundZustellmethodeanlegenVersandtarifAnlegentrue)
- [Optional: Kollektion für reduzierte Steuersätze anlegen](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_id_ShopifyConnectorShopeinrichten-OptionalKollektionfrreduzierteSteuerstzeanlegenSteuerreduktionAnlegentrue)
- [Optional: Kundengruppen als Katalog anlegen](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_N1751614608946)
- [Optional: Berechtigungen setzen](#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8_id_ShopifyConnectorShopeinrichten-BerechtigungensetzenBerechtigungen)

## Shop anlegen

Bei der Erstanlage eines Shops sind einige Schritte zu durchlaufen. Halte dich an die von Shopify zur Verfügung gestellte[Checkliste](https://help.shopify.com/de/manual/intro-to-shopify/initial-setup/new-to-shopify-checklists/general-checklist#einrichtung-eines-onlineshops)und du bist auf der sicheren Seite, nichts zu vergessen.

## Vertriebskanal anlegen

> **Anmerkung**
>
> Um einen Vertriebskanal anzulegen oder zu ändern, musst du in Shopify als Administrator angemeldet sein.

In Shopify kannst du mit verschiedenen Vertriebskanälen arbeiten. So kannst du neben dem eigentlichen Shop z. B. eine “Kaufen”-Schaltfläche in deine persönliche Webseite einbinden. Außerdem kannst du mit Drittanbieter-Channels arbeiten.

Bei der Xentral-Shopify-Anbindung kannst du jedem Shopify-Vertriebskanal ein Xentral-Projekt zuweisen, so dass du deine Prozesse entsprechend steuern und auswerten kannst.

Mehr Infos zu den Vertriebskanälen in Shopify findest du[hier](https://help.shopify.com/de/manual/online-sales-channels).

## Standort anlegen und Inventar verwalten

Damit die Lagerbestände zwischen Xentral und Shopify synchronisiert werden können, brauchst du in Shopify mindestens einen Standort, wobei ein Standort je nach Belieben ein ganzes Lager sein kann, aber auch ein einzelnes Lagerregal oder ein externer Standort z. B. eines Logistikdienstleisters. Hier ist es wichtig, dass du dir Gedanken machst, welche Struktur deine Bedürfnisse am besten abbildet. Sobald du mehrere Standorte anlegst, ist es möglich, Bestände nach Standorten getrennt auszuwerten.

> **Anmerkung**
>
> Die Synchronisierung der Lagerbestände erfolgt derzeit nur mit einem einzigen Lagerort.

Mehr Infos zu den Standorten in Shopify findest du[hier](https://help.shopify.com/de/manual/locations).

Außerdem musst du die Inventarverwaltung für die Produkte aktivieren. Mehr Infos dazu findest du[hier](https://help.shopify.com/de/manual/products/inventory/getting-started-with-inventory).

## Zahlungsmethode anlegen

Um Zahlungen abwickeln und den Zahlstatus vom Shop in Xentral übertragen zu können, benötigst du mindestens eine Zahlungsmethode in Shopify. Besuche[diese Seite](https://help.shopify.com/de/manual/payments), um alles über die verschiedenen Zahlungsmethoden zu erfahren.

## Versandtarif und Zustellmethode anlegen

Wie du deine Logistik im Detail abwickelst, kann ein sehr komplexes Thema sein. Wir möchten dich an dieser Stelle an die umfangreichen[Hilfestellungen](https://help.shopify.com/de/manual/shipping)von Shopify verweisen. Erforderlich für die Anbindung an Xentral ist, dass mindestens ein Versandtarif in Shopify angelegt ist.

## Optional: Kollektion für reduzierte Steuersätze anlegen

Bietest du Produkte an, die einer Steuerreduktion unterliegen (z. B. Bücher), kannst du die reduzierte Steuer allen betroffenen Produkten in Shopify über eine Kategorie zuweisen. Genaueres dazu kannst du in diesen[Artikeln](https://help.shopify.com/de/manual/taxes/tax-overrides#apply-tax-override)lesen.

## Optional: Kundengruppen als Katalog anlegen

Wenn du mit der Erweiterten Preisfunktion arbeiten möchtest, müssen die Kundengruppen als Katalog in Shopify angelegt werden. Die Namen müssen dort dieselben sein wie die Namen der Kundengruppen in Xentral. Genaueres zu Katalogen kannst du in diesen[Artikeln](https://help.shopify.com/de/manual/markets-new/catalogs)lesen.

> **Tipp**
>
> Beispiel:

## Optional: Berechtigungen setzen

### Achtung **Wir empfehlen, die Shop-Schnittstelle über die Public App anzubinden.** In diesem Fall kannst du diesen Abschnitt überspringen. Das hier beschriebene manuelle Setzen der Berechtigungen ist nur notwendig, wenn du die Shop-Schnittstelle über eine Custom App anbinden möchtest.

> **Anmerkung**
>
> Für das Setzen der Berechtigungen musst du in Shopify als Administrator angemeldet sein.

Setze die erforderlichen Rechte im Shop. Gehe dazu wie folgt vor:

1. Melde dich in Shopify als Administrator an.
1. Gehe in den **Einstellungen ** auf **Apps und Vertriebskanäle ** und dort auf**Apps erstellen**.
1. Auf der nächsten Seite kannst du entweder eine bereits existierende benutzerdefinierte App öffnen oder eine neue erstellen. Weitere Informationen zu benutzerdefinierten Apps findest du auf [dieser Seite](https://help.shopify.com/de/manual/apps/app-types/custom-apps).
1. Klicke in der **App ** auf **Konfiguration ** und dort auf**Bearbeiten**, um die Berechtigungen festzulegen.
1. Setze für folgende Ressourcen Schreib- und Lesezugriff:
  1. read_all_orders, read_assigned_fulfillment_orders, read_companies, read_customers, read_discounts, read_draft_orders, read_locations, read_metaobject_definitions, read_metaobjects, read_orders, read_payment_terms, read_product_listings, read_products, read_publications, read_returns, read_shipping, read_shopify_payments_accounts, read_shopify_payments_payouts, read_themes, write_assigned_fulfillment_orders
  1. write_files, write_fulfillments, write_gift_cards, write_inventory, write_locales, write_merchant_managed_fulfillment_orders, write_metaobject_definitions, write_metaobjects, write_orders, write_products, write_returns, write_shipping, write_third_party_fulfillment_orders, write_translations