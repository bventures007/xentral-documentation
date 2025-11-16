## Überblick

Um eine reibungslose Einrichtung einer neuen Shop-Schnittstelle zu gewährleisten, ist es wichtig, zunächst einige allgemeine Einstellungen in Xentral im Bereich der Stammdaten durchzuführen. Wenn du Xentral bereits im Einsatz hast, hast du wahrscheinlich schon einige der folgenden Einrichtungsschritte durchgeführt. Stelle dann jedoch sicher, dass die formellen Anforderungen erfüllt sind (z. B. Gleichnamigkeit der Zahlungsart in Shop und Xentral).

## Berechtigungen setzen

Für die Installation, die Einrichtung und die initialen Tests der Connect-Schnittstelle benötigst du Administrations-Rechte in Xentral. Es gibt keine untergeordneten Rechte wie bei anderen Modulen.

## Projekt für Shop-Integration anlegen

Für jede Shop-Integration wird mindestens ein Projekt benötigt, das dem Shop zugeordnet wird. Arbeitest du mit Vertriebskanälen kannst du mehrere Projekte anlegen und jedem Channel ein Projekt zuweisen (Funktionalität abhängig vom Shop).

Wie du ein Projekt in Xentral anlegst und verwaltest, findest du in diesem Handbuchartikel:[Projekte: Nutzung und Einstellungen](https://help.xentral.com/hc/de/articles/360016723620#UUID-47d62f4f-3eac-f7b6-5144-f2353584abd5).

## Portoartikel anlegen

Ein sogenannter Portoartikel dient dazu, Portokosten als eigene Position in den Belegen darzustellen. Um Versandgebühren aus Shop-Aufträgen in Xentral zu importieren, benötigst du also einen solchen Portoartikel.

Um einen Portoartikel anzulegen folge dem Menüpfad **Verkaufen > Artikel > + Artikel hinzufügen**, gib einen passenden Namen und die allgemeinen Daten ein und scrolle nach unten zum Bereich Artikel Optionen. Dort setzt du das Häkchen bei “Artikel ist Porto” und speicherst anschließend.

![Prep07Porto_0314p.png](https://help.xentral.com/hc/article_attachments/13235061324188)

Wenn du mehr Informationen zum Thema Artikel anlegen brauchst, schau in diesem Handbuchartikel:[Artikel manuell anlegen](https://help.xentral.com/hc/de/articles/5355868375324#UUID-7b466ccc-d331-8e18-2f8e-9a396ad6b84d).

## Rabattartikel anlegen

Ein Rabattartikel wird genutzt, um Rabatte zu gewähren und diesen im Beleg als eigene Position darzu-stellen, z.B. "Aktionsrabatt 10%". Im Beleg ist die Rabattartikel-Position dann mit einem entsprechenden negativen Betrag versehen, der den Gesamtbetrag mindert. Um Rabatte aus dem Shop in Xentral zu übertragen benötigst du also einen solchen Rabattartikel.

Um einen Rabattartikel anzulegen folge dem Menüpfad **Verkaufen > Artikel > + Artikel hinzufügen**, gib einen passenden Namen und die allgemeinen Daten ein und scrolle nach unten zum Bereich Artikel Optionen. Dort setzt du das Häkchen bei “Artikel ist Rabatt” und speicherst anschließend. Das Feld für den Prozentsatz kannst du in diesem Fall leer lassen, weil die Rabattwerte später vom Shop übergeben werden.

![Prep07Rabatt_0314p.png](https://help.xentral.com/hc/article_attachments/13235040594076)

## Zahlungsweisen anlegen

Um die Zahlungsweisen in Shop und Xentral miteinander verknüpfen zu können, müssen sie in beiden Systemen mit derselben Benennung angelegt werden.

Um eine Zahlungsweise anzulegen, suche einfach über die **Smartsearch ** nach**Zahlungsweisen**.

Wenn du mehr Informationen zum Thema Zahlungsweisen in Xentral benötigst, schau dir diesen Handbuchabschnitt an:[Zahlungsweisen & Zahlungsbedingungen](https://help.xentral.com/hc/de/articles/360016722120#UUID-2d28bdae-9755-4485-10de-ac5d40abb969).

### Zahlungsweisen zwischen Xentral und Shop abgleichen

Wenn du Bestellungen aus deinem Shop in Xentral importierst, wird jeder Vorgang mit einer bestimmten Zahlungsart übergeben. Damit Xentral diese richtig erkennt und automatisch die passende interne Zahlungsweise setzt, musst du die Verknüpfungen im Shopmodul anlegen.

> **Anmerkung**
>
> **Hinweis**
>
> Wenn du Zahlungsweisen zwischen deinem Shop und Xentral verknüpfst, kannst du drei Dinge festlegen:
>
> - Was passiert, wenn der Shop keine Zahlungsart mitschickt – in diesem Fall kannst du eine Standardoption hinterlegen, die automatisch gesetzt wird, damit der Beleg vollständig bleibt.
> - Du kannst bestimmen, wie die im Shop genutzten Zahlungsarten automatisch den passenden Zahlungsweisen in Xentral zugeordnet werden, damit z. B. „Kreditkarte“ oder „Vorkasse“ aus dem Shop auch in Xentral korrekt gesetzt werden.
> - Du hast die Möglichkeit, für bestimmte Zahlungsarten den automatischen Versand zu deaktivieren, etwa wenn du vor dem Versand erst den Zahlungseingang prüfen möchtest.
>
> **Weitere Informationen und die genaue Einrichtung findest du in der Workflow-Konfiguration der jeweiligen Shops und Marktplätze (Workflows > Reiter Aufträge > Zahlungsarten).**

## Versandarten anlegen

Um die Versandarten in Shop und Xentral miteinander verknüpfen zu können, müssen sie in beiden Systemen mit derselben Benennung angelegt werden.

Um eine Versandart anzulegen, suche einfach über die **Smartsearch ** nach**Versandarten**.

Wenn du mehr Informationen zum Thema Versandarten in Xentral benötigst, schau dir diesen Handbuchabschnitt an:[Übersicht: Versandarten in Xentral](https://help.xentral.com/hc/de/articles/18567521362332#UUID-1c7f1ac7-1f9a-1592-4caa-a2bb5dc422ad).

## Lieferbedingung anlegen (optional)

Falls du Lieferbedingungen nutzen möchtest und um Shopaufträgen eine feste Lieferbedingung zuweisen zu können, muss eine Lieferbedingung angelegt werden.

Um das zu tun, suche einfach über die **Smartsearch ** nach**Lieferbedingungen**.

Wenn du mehr Informationen zum Thema Lieferbedingungen in Xentral benötigst, schau dir diesen Handbuchabschnitt an:[Lieferbedingungen](https://help.xentral.com/hc/de/articles/360019776399#UUID-f5e6a3ba-07c8-3a18-ea88-daba1713c9bf).

## Default-Kundennummer anlegen (optional)

Shop-Kunden werden grundsätzlich automatisch anhand bestimmter Kriterien einem Xentral-Kunden zugeordnet. Für den Fall, dass keine automatische Zuordnung möglich ist, z. B. weil die Adressdaten nicht eindeutig sind, erfolgt die Zuordnung auf eine Default-Kundennummer.

> **Anmerkung**
>
> Die Zuordnungskriterien und ob die Default-Kundennummer genutzt werden soll oder nicht, wird später bei der Shop-Anbindung festgelegt.

Um einen Kunden anzulegen folge dem Menüpfad **Verkaufen > Adressen > + NEU**, gib eine passende Bezeichnung als Namen ein und speichere anschließend den Datensatz. Nach dem Speichern wirst du gefragt, welche Rolle zugeordnet werden soll. Belasse das Häkchen bei “als Kunde markieren” und klicke auf “Jetzt markieren”.

![Prep07Kunde_0314p.png](https://help.xentral.com/hc/article_attachments/13235061443740)

Wenn du mehr Informationen zum Thema Kunden anlegen brauchst, schau in diesem Handbuchabschnitt:[Adressen anlegen (Legacy)](https://help.xentral.com/hc/de/articles/4539623305500#UUID-e43fd5c1-e0e0-d665-e41b-d9f5cde1dbe9).

## POS-Kundennummer anlegen (optional)

Falls du deinen Shop für Kunden nutzt, die vor Ort im Laden kaufen, also am Point-of-Sales (POS), kannst oder möchtest du möglicherweise nicht für jeden Kunden ein individuelles Konto anlegen. Stattdessen möchtest du für diesen Zweck eine allgemeine Kundennummer nutzen.

Um einen Kunden anzulegen folge dem Menüpfad **Verkaufen > Adressen > + NEU**, gib eine passende Bezeichnung als Namen ein und speichere anschließend den Datensatz. Nach dem Speichern wirst du gefragt, welche Rolle zugeordnet werden soll. Belasse das Häkchen bei “als Kunde markieren” und klicke auf “Jetzt markieren”.

![Prep07Kunde_0314p.png](https://help.xentral.com/hc/article_attachments/13235061443740)

Wenn du mehr Informationen zum Thema Kunden anlegen brauchst, schau in diesem Handbuchabschnitt:[Adressen anlegen (Legacy)](https://help.xentral.com/hc/de/articles/4539623305500#UUID-e43fd5c1-e0e0-d665-e41b-d9f5cde1dbe9).