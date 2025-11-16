## Überblick

In diesem Beitrag erfährst du, wie du in Xentral Connect mit Artikeln arbeitest, deren Artikelnummern in Xentral sich von denen in deinen angebundenen Shop- oder Marktplatzsystemen unterscheiden.

Beispielsweise hast du einen Artikel, den du in mehreren Kanälen, z. B. Shopify, Shopware und Amazon, anbietest. Auf jedem Verkaufskanal verwendest du dafür eigene Produktnummern, in Xentral arbeitest du jedoch mit einer einzigen Artikelnummer. Es stellt sich die Frage, wie du sicherstellst, dass Bestände, Preise und Auftragsdaten trotz abweichender Nummern korrekt synchronisiert werden.

Hierfür zeigen wir dir in diesem Artikel,

- wie du solche Artikel korrekt in Xentral verwaltest und
- auf welche Weise du unterschiedliche Nummern in den Systemen miteinander verknüpfen kannst.

> **Anmerkung**
>
> Dieser Artikel baut auf den grundlegenden Kenntnissen über die Connect-Schnittstelle einschließlich deren Installation und Einrichtung auf. Falls du hierzu mehr Informationen benötigst, hilft dir dieser Handbuch-Abschnitt weiter:Shopware 6 Connector.
>
> Stelle sicher, dass deine Schnittstelle vollständig installiert und konfiguriert ist. In diesem Artikel gehen wir nur auf spezifischen Einstellungen für die Synchronisation von Matrixprodukten und Varianten ein.

Für die folgenden Abschnitte nehmen wir an, der Artikel, der in mehreren Kanälen angeboten wird, lautet wie folgt:

| Artikelnummer in Xentral | Artikelbezeichnung in Xentral | Produktnummer in Shopware 6 | SKU in Shopify |
| --- | --- | --- | --- |
| M102500 | Vollkornmüsli "5 Frucht" | SW45678 | SH98765 |

## Fremdnummern im Artikel eintragen

Um Fremdnummern einzutragen, öffne denArtikelim Xentral Artikelstamm und wechsele zum ReiterFremdnummern:

![Artikelfremdnummern_Artikel_Fremdnummern.png](https://help.xentral.com/hc/article_attachments/23262687421980)

Fülle den AbschnittAnlegenaus und klicke aufSpeichern. Stelle sicher, dass die Zeile dabei alsAktivmarkiert ist.

![Artikelfremdnummern_Artikel_Fremdnummern_Anlegen.png](https://help.xentral.com/hc/article_attachments/23262687427740)

- Bezeichnung: Nutze hier eine Bezeichnung, mit der du die Fremdnummern identifizieren kannst. Das kann z. B. die Bezeichnung des Verkaufskanals sein. Alternativ ist die Bezeichnung als "Shop-Nummer" denkbar, wenn du z. B. nur abweichende Nummern zwischen Online- und Ladenverkauf verwendest.
- Fremdnummer: Trage hier die eindeutige Produktnummer ein, die im Kanal verwendet wird.
- Shop: Wähle hier die zutreffende Connect-Schnittstelle.

Wiederhole dieses Vorgehen für andere Verkaufskanäle. In unserem Beispiel gibt es anschließend diese zwei Einträge:

![Artikelfremdnummern_Artikel_Fremdnummern_Angelegt.png](https://help.xentral.com/hc/article_attachments/23262687430940)

> **Anmerkung**
>
> **Hinweis**
>
> Alternativ kannst du die Nummern-Zuordnungen unter **Artikel Fremdnummern** (Suche in der Smart Search) eintragen:

## Fremdnummern-Unterstützung in der Schnittstelle aktivieren

Damit die Fremdnummern künftig verknüpft werden, navigiere unterEinstellungen (Zahnrad oben rechts) > Verkaufen > Shops/Marktplätzezu der Connect Schnittstelle des jeweiligen Verkaufskanals. Folge dann folgenden Schritten:

1. Klicke in der Schnittstelle auf das Zahnrad, um die Einstellungen zu öffnen.
1. Wechsele auf den Reiter Erweiterte Einstellungen.
1. Aktiviere Fremdnummern verwenden.
1. Trage die Fremdnummern Bezeichnung ein, die du für diesen Verkaufskanal verwendest. Dies ist die Bezeichnung, die zu im vorherigen Abschnitt verwendet hast.
1. Bestätige mit Speichern.

Wiederhole dieses Vorgehen für andere Verkaufskanäle.

> **Anmerkung**
>
> Mit diesen wenigen Schritten hast du die Unterstützung für Fremdnummern aktiviert und die Schnittstelle "übersetzt" im Hintergrund unterschiedliche Nummern in den Systemen automatisch.
>
> Im Journal wird der Artikel stets mit der Xentral Artikelnummer aufgelistet: