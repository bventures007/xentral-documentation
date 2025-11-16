## Vor der Anbindung

In diesem Artikel erfährst du alles über die Anbindung von Online Shops und Marktplätzen (z.B. Shopify, WooCommerce, Amazon, eBay etc.) an Xentral. Mit der Anbindung ist es ein Leichtes, die Vorteile beider Systeme voll auszuschöpfen und deine Prozesse zu automatisieren, damit du dich auf dein Kerngeschäft konzentrieren kannst.

Einige Einstellungen und Möglichkeiten sind für alle Anbindungen gleich, andere sind shopspezifisch. Die shopspezifischen findest du in den jeweiligen Unter-Artikeln. Wenn es schnell gehen muss, kommst du[hier](#UUID-7b472917-dd79-f7ac-843a-cc4ef7e3c691_id_xentralConnect-ConnectSchnittstellenOut-of-the-BoxQuicklinks)direkt zu den entsprechenden Shop-Anleitungen. Wichtig in diesem Fall: Die grundlegenden Entscheidungen solltest du bereits getroffen und alle[Voraussetzungen](#UUID-7b472917-dd79-f7ac-843a-cc4ef7e3c691_id_xentralConnect-ChecklisteShop-AnbindungChecklisteShopAnbindung)geschaffen haben.

### Grundlegende Erwägungen & Wahl der Schnittstelle

Wenn du bisher noch keinen Shop/ Marktplatz im Einsatz hast, stehst du vor der Entscheidung, welcher für dich am besten geeignet ist. Dies ist u. a. abhängig von deinem Geschäftsmodell (online/Ladenshop POS), dem Auftragsvolumen, der Zielgruppe, der Komplexität deiner Lagerhaltung (ein/mehrere Standorte) und ob die Schnittstelle zum Shop/Marktplatz von Xentral überhaupt unterstützt wird. Wenn du hierbei Entscheidungshilfe brauchst, wende dich gerne an deinen Solution Consultant.

> **Tipp**
>
> Wenn du noch keinen Solution Consultant hast, öffne ein Ticket bei unserem Support.

#### Featurematrix

Als weitere Hilfestellung zur Auswahl eines für dich geeigneten Shops, findest du im folgenden eine Übersicht darüber, welche Schnittstellen welche Features bieten. Diese Übersicht hilft dir ebenfalls, wenn du bereits einen Shop/ Marktplatz gewählt hast und es anschließend darum geht, zu entscheiden, welche Daten konkret zwischen den beiden Systemen ausgetauscht werden sollen.

![Featurematrix.png](https://help.xentral.com/hc/article_attachments/21847984438172)

> **Anmerkung**
>
> **Die Übersicht findest du hier auch als PDF zum Downloaden: Feature-Matrix (PDF).**
>
> Bei den hier aufgeführten Möglichkeiten handelt es sich um den derzeitigen Standard-Umfang in Xentral. Wenn du als "Nicht verfügbar" gekennzeichnete Features benötigst, setze sie gerne auf die Roadmap, oder wende dich an unser Support-Team, um die Möglichkeiten einer kundenindividuellen Anpassung zu prüfen.

### Checkliste Shop-Anbindung

Um einen Shop anzubinden, kannst du dich nach folgender Checkliste richten. Details zu den einzelnen Schritten findest du in den Hilfe-Artikeln.

- Shop einrichten (Details je nach Shop/Marktplatz)
- [Projekt für Shop-Integration anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-ProjektfrShop-IntegrationanlegenProjektAnlegentrue)
- [Portoartikel anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-PortoartikelanlegenPortoartikelAnlegentrue)
- [Rabattartikel anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-RabattartikelanlegenRabattartikelAnlegentrue)
- [Zahlungsweisen anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-ZahlungsweisenanlegenZahlungsweiseAnlegentrue)
- [Versandarten anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-VersandartenanlegenVersandartAnlegentrue)
- *optional*: [Lieferbedingung anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-LieferbedingunganlegenoptionalLieferbedingungAnlegentrue) (falls du Lieferbedingungen nutzen möchtest)
- *optional*: [Default-Kundennummer anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-Default-KundennummeranlegenoptionalDefaultkundeAnlegentrue) (falls du Gastkunden zulässt oder für den Fall, dass keine automatische Kundenzuordnung anhand bestimmter Kriterien möglich ist)
- *optional*: [POS-Kundennummer anlegen](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62_id_xentralfrConnect-Anbindungvorbereiten-POS-KundennummeranlegenoptionalPosKundeAnlegentrue) (falls du deinen Shop für Kunden nutzt, die vor Ort im Laden kaufen und von denen dir nicht alle Daten vorliegen, um ein einzelnes Kundenkonto anzulegen)

### Voraussetzungen für Connect Schnittstellen

Bevor du einen Shop mit Connect anbinden kannst, stelle sicher, dass deine Xentral-Oberfläche in der NextGen-Version läuft. Falls nicht, klicke im Menübaum links unten auf#NextGen UI.

![Prep01NextGen_0314p.png](https://help.xentral.com/hc/article_attachments/13235027918620)

## Vorbereitungen in Xentral

Um eine reibungslose Einrichtung der Schnittstelle zu gewährleisten, ist es wichtig, zunächst einige allgemeine Einstellungen in Xentral im Bereich der Stammdaten durchzuführen. In diesem[Handbuchabschnitt](https://help.xentral.com/hc/de/articles/13235039280796#UUID-efc2789d-fff6-f3d6-8a10-5c87f55efd62)findest du alle Informationen, wie du Xentral optimal vorbereitest.

## Vorbereitungen im Shop/Marktplatz

Bevor du mit der Anbindung starten kannst, stelle sicher, dass du seitens des Shops alle Voraussetzungen geschaffen hast. Wie du das genau tust, ist abhängig vom jeweiligen Shop/Marktplatz. Hinweise dazu findest du in den zugehörigen Shop-Hilfetexten:

[OTTO-Connector: Marktplatz einrichten](https://help.xentral.com/hc/de/articles/16510612893212#UUID-5e9ddc13-b362-9644-1614-2618e61c93e3)

[Shopify Connector: Shop einrichten](https://help.xentral.com/hc/de/articles/13235023151388#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8)

[Shopware6-Connector: Shop einrichten](https://help.xentral.com/hc/de/articles/14528027834396#UUID-7f8b2f2c-e958-a26f-e0b5-3fbcd24afe62)

[Tradebyte Connector: TB.One Plattform einrichten](https://help.xentral.com/hc/de/articles/20346733712540#UUID-a2138779-5fd4-f9b7-0993-9ace10e46396)

[WooCommerce Connector: Shop einrichten](https://help.xentral.com/hc/de/articles/13235060367132#UUID-2a79e5ba-33b3-ebdd-fdd7-60e3dae5c478)

## Connect Schnittstellen “Out-of-the-Box”

Die “Out-of-the-box”-Schnittstellen der neuen Connect Anbindung haben wir so konzipiert, dass du nach den obigen Vorbereitungen einfach den Einrichtungswizard für eine neue Schnittstelle oder den Übernahmewizard für eine bestehende Classic Schnittstelle starten und anschließend sofort loslegen kannst. Es sind keine besonderen technischen Kenntnisse erforderlich und deckt die allermeisten Anwendungsszenarien bestens ab.

> **Anmerkung**
>
> Falls du eine Classic Shop Schnittstelle nutzt und diese auf eine Xentral Connect Schnittstelle umstellen möchtest, besuchediesen Artikelfür Details.

> **Anmerkung**
>
> Wenn du mit Konfigurationsartikeln, personalisierten Artikeln oder variablen Stücklisten arbeitest, ist eine “Out-of-the-box”-Lösung für deine Anwendungszwecke wahrscheinlich nicht ausreichend. In diesem Fall leisten dir die“Extended”-Schnittstellen(siehe weiter unten) hervorragende Dienste.

Folge den Anleitungen auf den folgenden Seiten, um deine Schnittstelle einzurichten:

### Mirakl-Connector

Mithilfe unserer Connect-Schnittstelle lässt sich Mirakl nahtlos in dein Xentral integrieren, so dass du zahlreiche Marktplätze (u. a. Conrad, Decathlon, Douglas, Fressnapf, Hornbach, Home24, Mediamarkt/Saturn, Shop Apotheke, Voelkner) anbinden und die Prozesse einschließlich Produktlisting und Versandabwicklung automatisieren kannst. Mehr Informationen zur Anbindung von Mirakl-Marktplätzen mit der Connect Schnittstelle findest du in den folgenden Abschnitten:

[Mirakl: Neue Anbindung anlegen](https://help.xentral.com/hc/de/articles/18583267455772#UUID-6d683a83-07d3-a736-316a-d0b0cd0a1f5c)

[Mirakl: Artikel zuordnen](https://help.xentral.com/hc/de/articles/18583246646684#UUID-9e1f9a28-77b4-16d1-be1a-bb9985f2090a)

[Mirakl: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/18583279316508#UUID-5d094ba0-1fed-0788-676f-f0b69060c13c)

[Kategorienmapping auf Mirakl](https://help.xentral.com/hc/de/articles/18583279345308#UUID-1ac8a492-f607-1d17-e40b-80283d05dc67)

[Mirakl: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589768508828#UUID-94e6be55-89a9-e758-91fc-d82d54bd7940)

[Mirakl: Einstellungen anpassen](https://help.xentral.com/hc/de/articles/18583263311516#UUID-f35ac2cb-b44e-e95f-9cf2-386347a60a32)

[Mirakl: Journal](https://help.xentral.com/hc/de/articles/18583263358108#UUID-2c706abd-1741-7567-9171-df43c2e898f3)

### OTTO-Connector

Mit Hilfe unserer OTTO-Schnittstelle kannst du deinen OTTO Market nahtlos an Xentral anbinden. Mehr Informationen zum OTTO Market und die Anbindung mit der Connect Schnittstelle findest du in den folgenden Abschnitten:

[OTTO-Connector: Marktplatz einrichten](https://help.xentral.com/hc/de/articles/16510612893212#UUID-5e9ddc13-b362-9644-1614-2618e61c93e3)

[OTTO Connector: Neue Anbindung anlegen](https://help.xentral.com/hc/de/articles/16510622697116#UUID-3370c66d-310c-6b25-6fa6-16c252347e84)

[OTTO Connector: Artikel zuordnen](https://help.xentral.com/hc/de/articles/16510627621532#UUID-eecfb261-6503-5309-fcae-89ad123f65c3)

[OTTO Connector: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/16510599518876#UUID-91f7b739-70c3-735c-3269-c7b31a73b85a)

[OTTO Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589740879132#UUID-76f3afac-0b29-56cb-47ca-10af39e437d6)

[OTTO Connector: Einstellungen anpassen](https://help.xentral.com/hc/de/articles/16510637433628#UUID-690579c5-f7ff-c3c4-c118-33fc054bfeb2)

[OTTO Connector: Journal](https://help.xentral.com/hc/de/articles/16510622825756#UUID-cc81f147-fc32-992b-080c-a5e78d6107b5)

### Shopify-Connector

Mit dieser Schnittstelle kannst du Xentral und Shopify verbinden, um Bestellungen aus dem Shop in Xentral zu importieren und deine im Shop verkauften Artikel in Xentral zu verwalten. Die Anbindung erfolgt über die neue Connect-Schnittstelle. Die Erstellung und der Versand von Lieferscheinen und Rechnungen wird über Xentral abgewickelt, wobei du den Auto-Versand nutzen kannst. Aktualisierte Auftragsstatus, Trackingnummern versendeter Lieferungen und Lagerzahlen der Artikel meldet Xentral an den Shop zurück. Die perfekte Kombination für e-Commerce-Unternehmen!

Mehr Informationen zu Shopify und die Anbindung mit der Connect Schnittstelle findest du in den folgenden Abschnitten:

[Shopify Connector: Shop einrichten](https://help.xentral.com/hc/de/articles/13235023151388#UUID-3ba63925-6ffd-3781-71fd-f7c3621b46e8)

[Shopify Connector: Neue Anbindung anlegen](https://help.xentral.com/hc/de/articles/13235060103068#UUID-566aaf84-943d-ce48-b27c-8ec1f93d6b9f)

[Shopify Connector: Daten übernehmen](https://help.xentral.com/hc/de/articles/13235023216156#UUID-e411fce4-0b3a-6983-0e8d-e8686b8f38ad)

[Shopify Connector: Artikel zuordnen](https://help.xentral.com/hc/de/articles/13235060173596#UUID-6b6b31e2-79dc-2826-dd07-8cf4e4976109)

[Shopify Connector: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/13235060220444#UUID-55e1cf94-dd5f-eb68-4337-cabda5e7ee49)

[Shopify Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589752911516#UUID-e51cce39-191a-dec1-8f90-44b0af01a9f4)

[Shopify Connector: Einstellungen anpassen](https://help.xentral.com/hc/de/articles/13234991774620#UUID-b9eec352-e0ad-26d5-c6a1-a7944bae9951)

[Shopify Connector: Journal](https://help.xentral.com/hc/de/articles/13921857699612#UUID-d8ed9992-afac-447b-5f28-2e5f96fd98ac)

### Shopware-Connector

Shopware ist eine lang etablierte, deutsche Open-Source-Software und ist sowohl für Einsteiger / Start-Ups als auch für etablierte Online-Unternehmen bestens geeignet, da es unterschiedlichste Pläne und Preismodelle mitbringt. Insbesondere für den Einsteig mit der kostenlosen Community-Variante, aber auch für Unternehmen, die Wert auf eine self-hosted / on-premise-Lösung legen, ist Shopware ein ideales Angebot. Über die Connect-Schnittstelle kannst du Shopware mit Xentral verbinden und so die Vorteile beider Systeme voll ausschöpfen!

**Shopware5-Connector (nur Migration)**>** Anmerkung**
>
> Shopware hat Shopware 5 zum Juli 2024 endgültig abgekündigt, bietet bis dahin nur noch sicherheitsrelevante Updates und empfiehlt, die Umstellung auf Shopware 6 rechtzeitig durchzuführen.

Unser Shopware5-Connector ist so aufgebaut, dass er dich bei der Umstellung von Shopware5 auf 6 optimal unterstützt. Eine Produktiv-Anbindung von Xentral an Shopware 5 ist über die neue Connect Schnittstelle nicht vorgesehen.

[Shopware5-Connector: Neue Anbindung anlegen](https://help.xentral.com/hc/de/articles/14528063566236#UUID-5cac4b2b-776a-b39e-9c73-fd81c7fcb037)

[Shopware5-Connector: Daten importieren](https://help.xentral.com/hc/de/articles/14528034519324#UUID-18275b4c-fb14-8219-d391-d5592a3ba692)

[Shopware5-Connector: Zugangsdaten anpassen](https://help.xentral.com/hc/de/articles/14528044126364#UUID-98a8d893-88dd-fe60-46b0-837a74749188)

**Shopware6-Connector**

Mehr Informationen zu Shopware 6 und der Anbindung über die Connect-Schnittstelle findest du in den folgenden Abschnitten:

[Shopware6-Connector: Shop einrichten](https://help.xentral.com/hc/de/articles/14528027834396#UUID-7f8b2f2c-e958-a26f-e0b5-3fbcd24afe62)

[Shopware6-Connector Neue Anbindung anlegen](https://help.xentral.com/hc/de/articles/14528034737436#UUID-5fc85b9c-c5b5-e720-3bda-0a29de11ffdd)

[Shopware6-Connector: Daten übernehmen](https://help.xentral.com/hc/de/articles/19385101720220#UUID-aa9bd09e-88ec-92c2-3b68-00a605cfc2c4)

[Shopware6-Connector: Artikel zuordnen](https://help.xentral.com/hc/de/articles/14528034786588#UUID-cfece960-9538-6fea-fdc4-64d9bbdfe08f)

[Shopware6-Connector: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/14528034840732#UUID-b0386169-a59f-1d8d-1375-62b9ba1825d5)

[Shopware6-Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589763018012#UUID-51edb066-e697-e70b-6116-829fdd05e479)

[Shopware6-Connector: Einstellungen anpassen](https://help.xentral.com/hc/de/articles/14528064061596#UUID-6d4dffad-8633-5d25-a378-9864446787dc)

[Shopware6-Connector: Journal](https://help.xentral.com/hc/de/articles/14528034952476#UUID-0748de4e-37e4-85a3-21a3-6a2c51fcb42b)

### Tradebyte-Connector

Mit der Tradebyte-Plattform kannst du deine Produkte auf zahlreichen namhaften Marktplätzen effizient vertreiben. Mit dem Softwaretool TB.One von Tradebyte kannst du deine Produktdaten zentral verwalten und schließlich über unsere Connect Schnittstelle mit Xentral nahtlos verbinden. So gelingt dir die bequeme Automatisierung deines E-Commerce-Geschäfts!

Mehr Informationen zu Tradebyte und der Anbindung über die Connect Schnittstelle findest du in den folgenden Abschnitten:

[Tradebyte Connector: TB.One Plattform einrichten](https://help.xentral.com/hc/de/articles/20346733712540#UUID-a2138779-5fd4-f9b7-0993-9ace10e46396)

[Tradebyte Connector: Neue Anbindung anlegen](https://help.xentral.com/hc/de/articles/20346718463772#UUID-5fb3a0d4-94f6-4848-0d94-dba78e08a344)

[Tradebyte Connector: Artikel zuordnen](https://help.xentral.com/hc/de/articles/20346718496156#UUID-71d16cd8-aed2-e377-65d6-acb76c1171c2)

[Tradebyte Connector: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/20346726895772#UUID-fe7d1d8a-b137-3d43-66fd-c75fb5b486bd)

[Tradebyte Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/20346726922524#UUID-da47e695-24d4-715a-88a1-24755f9f7500)

[Tradebyte Connector: Einstellungen anpassen](https://help.xentral.com/hc/de/articles/20346740412444#UUID-d1969a73-3d21-2b97-e04f-9ae71771f79c)

[Tradebyte Connector: Journal](https://help.xentral.com/hc/de/articles/20346726988060#UUID-6bb90a04-de32-e4b8-4290-85677e0c9b29)

### WooCommerce-Connector

Mit dieser Schnittstelle kannst du Xentral und einen WordPress-basierten Online-Shop der WooCommerce-Plattform verbinden, um Bestellungen vom Shop in Xentral zu importieren und deine im Shop verkauften Artikel in Xentral zu verwalten. Die Anbindung erfolgt über die neue Connect-Schnittstelle.

Mehr Informationen zu WooCommerce und der Anbindung über die Connect Schnittstelle findest du in den folgenden Abschnitten:

[WooCommerce Connector: Shop einrichten](https://help.xentral.com/hc/de/articles/13235060367132#UUID-2a79e5ba-33b3-ebdd-fdd7-60e3dae5c478)

[WooCommerce Connector: Neue Anbindung anlegen](https://help.xentral.com/hc/de/articles/13235039683100#UUID-26f17c26-81e3-1f26-3031-15c362060d29)

[WooCommerce Connector: Daten übernehmen](https://help.xentral.com/hc/de/articles/13235023523228#UUID-e7601775-eed8-d291-fa9f-32518eb82b8a)

[WooCommerce Connector: Artikel zuordnen](https://help.xentral.com/hc/de/articles/13235023557532#UUID-2e1a76ae-2150-3aca-98cf-7f80d6c6f0b7)

[WooCommerce Connector: Workflows konfigurieren](https://help.xentral.com/hc/de/articles/13234992002460#UUID-2da1fca7-0bf6-4ed1-5caa-064075c28cd0)

[WooCommerce Connector: Produktiv schalten](https://help.xentral.com/hc/de/articles/18589740730012#UUID-3482c0db-0cbb-26a5-6a44-9a82f4cfb81a)

[WooCommerce Connector: Einstellungen anpassen](https://help.xentral.com/hc/de/articles/13235023642012#UUID-4f2df68c-a35e-1277-ee1f-bf278b87c71c)

[WooCommerce Connector: Journal](https://help.xentral.com/hc/de/articles/13921840987036#UUID-24f64971-99da-b968-5ba9-ff6a97dfabb5)

## Connect-Schnittstellen “Extended”

In wenigen Anwendungsfällen ist eine Out-of-the-Box-Schnittstelle leider nicht ausreichend und es bedarf der individuellen Anpassung der Anbindung. Wenn du folgende Artikel im Angebot hast, fällt dein Anwendungsszenario wahrscheinlich darunter:

- Konfigurationsartikel
- Personalisierte Artikel (wie bedruckte T-Shirts, Grußkarten, Gravuren)
- Variable / veränderliche Stücklisten

Wende dich in diesem Fall gerne an deinen Solution Consultant. Er unterstützt sich bei der kundenindividuellen Beratung und Anpassung oder kann dich an einen geeigneten Partner vermitteln.

> **Tipp**
>
> Wenn du noch keinen Solution Consultant hast, öffne ein Ticket bei unserem Support.

Grundsätzlich ist es auch möglich, Zugriff auf das Connect Backend zu bekommen, das die individuelle Erstellung und Anpassung von eigenen Workflows ermöglicht. Die Nutzung dieser Funktionalität erfordert erweiterte technische Kenntnisse, so dass der Zugang zur Connect-Instanz nur nach Schulung und Unterweisung zur Verfügung steht. Wenn du Interesse an der Nutzung individueller Workflows hast, wende dich ebenfalls an deinen Solution Consultant.

## Connect-FAQs

Eine Sammlung häufiger Fragen zu Connect-Schnittstellen findest du hier:[Connect-FAQs](https://help.xentral.com/hc/de/articles/16510627451804#UUID-54e783b7-eec3-8d97-9ada-3137c9a4db11).

## Classic Schnittstellen

### Amazon (Classic)

Mit dieser Schnittstelle kannst du Xentral und Amazon verbinden, um Bestellungen von dort in Xentral zu importieren und deine bei Amazon verkauften Artikel in Xentral zu verwalten. Die Anbindung geschieht über eine API-Schnittstelle (Shopimporter). Mehr Informationen findest du in diesem Hilfeabschnitt:[Überblick: Amazon Classic (Classic)](https://help.xentral.com/hc/de/articles/360016809939#UUID-c3dae2f2-8585-e44a-d7ae-9c5dec401a21).

### ebay (Classic)

Du kannst deinen eBay-Shop mit Xentral verbinden, deine Aufträge importieren und in Xentral weiter verarbeiten. Wenn du Hilfestellung bei der Einrichtung deiner eBay-Shopschnittstelle benötigst, besuche die folgenden Seiten. Dort findest du auch Beschreibungen und Erklärungen verschiedener Anwendungsfälle sowie Informationen zur eBay App, die du im App Center findest und die dir viele verschiedene Features bietet - von einer Übersicht aller Auktionen über Einstellungen zu Rahmenbedingungen bis hin zu Lagerinformationen.

[eBay (Classic)](https://help.xentral.com/hc/de/articles/18589763213980#UUID-3844967d-dff7-bcc8-f69a-f3d2a5bf4093)

[eBay App - Übersicht und Verwaltung von Listings (Classic)](https://help.xentral.com/hc/de/articles/18589749660316#UUID-c126d15b-0ebb-8a5b-cd0e-aa0d6d3c6fdf)

### Kaufland (Classic)

Mit dieser Schnittstelle kannst du Aufträge von Kaufland in Xentral zu importieren, Artikel zwischen beiden Systemen übertragen, aktuelle Lagerzahlen und Auftragsstatus zurückmelden, sowie Rechnungen an Kaufland übertragen. Mehr Informationen findest du in diesem Hilfeabschnitt:[Kaufland (Classic)](https://help.xentral.com/hc/de/articles/18589768780828#UUID-d6f615a0-852c-e3e0-0d41-ecf86e546fb1).