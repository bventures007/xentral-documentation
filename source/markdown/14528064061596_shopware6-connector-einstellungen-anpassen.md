## Überblick

Um die Schnittstelle in den Produktivmodus zu setzen, folge dem Menüpfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware6 Connector**. Wähle dann dasZahnrädchen.

![connect_modifysettings_overview.png](https://help.xentral.com/hc/article_attachments/15365120701084)

### Grundeinstellungen

Hier kannst du den Namen der Integration ändern, den Produktivmodus aktivieren / deaktivieren und bei Bedarf die Zugangsdaten sowie die bei der initialen Einrichtung gewählten Features anpassen.

![Shopware6_Einstellungen_StatusURLFeatures.png](https://help.xentral.com/hc/article_attachments/19385157543708)

> **Anmerkung**
>
> Detailanpassungen an einzelnen Features kannst du im BereichWorkflowsvornehmen.

### Zurücksetzen in den Migrationsmodus

Falls du nach der Produktiv-Schaltung weitere Daten migrieren möchtest, gehst du wie folgt vor:

1. **Einstellungen > Verkaufen > Shops / Marktplätze > Shopware6 Connector > Zahnrädchen**: Aktiviere den Migrationsmodus. Dies deaktiviert automatisch den Produktivmodus.
1. Warte einige Minuten.
1. **Einstellungen > Verkaufen > Shops / Marktplätze > Shopware6 Connector > Migration**: Führe die Migration durch, wie im entsprechenden [Handbuchabschnitt](https://help.xentral.com/hc/de/articles/19385101720220#UUID-aa9bd09e-88ec-92c2-3b68-00a605cfc2c4) beschrieben.
1. **Einstellungen > Verkaufen > Shops / Marktplätze > Shopware6 Connector > Zahnrädchen**: Deaktiviere den Migrationsmodus wieder.
1. Aktiviere den Produktivmodus. Dies startet alle Workflows, die sich vor der erneuten Migration im Livemodus befanden.

## Erweiterte Einstellungen

Im Reiter Erweiterte Einstellungen kannst dudie Verknüpfung der Artikel über Fremdnummern (statt über Artikelnummern/SKUs) freischalten.

### Verarbeitung von Fremdnummern

#### Überblick

Standardmäßig sind Artikel zwischen Xentral und dem Shop/Marktplatz über die Artikelnummer (SKU) miteinander verknüpft. Für den Fall, dass du im Shop/Marktplatz andere SKUs verwendest als in Xentral, kannst du den Abgleich über die Fremdnummern aktivieren.

#### Eingabe und Pflege der Fremdnummern

Du kannst Fremdnummern grundsätzlich auf zwei Arten eingeben und verwalten:

1. Mit der App **Artikel Fremdnummern** (Suche über die Supersearch): Hier kannst du für alle in Xentral hinterlegten Artikel Fremdnummern anlegen und verwalten.
1. Unter**Stammdaten > Artikel >* Artikel öffnen *> Reiter Fremdnummern**. Hier kannst du Fremdnummern für den geöffneten Artikel eintragen und pflegen.

Wenn du mehr Informationen zum Anlegen und Verwalten von Fremdnummern brauchst, findest du hier den entsprechenden[Hilfe-Artikel](https://help.xentral.com/hc/de/articles/360016758199#UUID-af5d8ee2-07dd-16dd-7655-bfa265d5cd7c).

> **Anmerkung**
>
> **Hinweis**
>
> *Beispiel*
>
> Angenommen, du verkaufst die beiden Artikel "Wasser Kirsche" und "Wasser Himbeere", die in Xentral die Artikelnummern PN-100012 bzw. PN-100014 haben, in drei verschiedenen Shops. Dort haben die Artikel jeweils unterschiedliche SKUs.
>
> Du trägst die je Shop gültige **Fremdnummer ** ein, verknüpfst den **Shop ** und wählst eine eindeutige**Bezeichnung** für die jeweilige Fremdnummern-Kategorie.

> **Anmerkung**
>
> Als Fremdnummer musst du die shop-/marktplatzseitige SKU verwenden. Andere Felder wie Produkt-ID o. ä. sind nicht wirksam.

#### Aktivierung der Fremdnummern-Verknüpfung in der Shop-Schnittstelle

Um die Fremdnummern-Verknüpfung zu aktivieren, gehe wie folgt vor:

![Shopware_Einstellungen_ErweiterteEinstellungen_Fremdnummern.png](https://help.xentral.com/hc/article_attachments/19385157546652)

1. Navigiere in den Einstellungen zum Reiter "Erweiterte Einstellungen".
1. Setze die Schaltfläche Fremdnummern nach rechts (aktiv).
1. Trage die Bezeichnung der Fremdnummern-Kategorie in das Feld ein.
1. Klicke auf Speichern.

#### Löschen von Artikelnummern

### Achtung

Beachte, dass Einträge aus der Fremdnummern-Tabelle entfernt werden, wenn ein Artikel in Xentral gelöscht wird. Deshalb werden Artikel im Shop/Marktplatz bei aktiver Fremdnummern-Verknüpfung nicht automatisch gelöscht, wenn sie in Xentral gelöscht werden. In diesem Fall musst du die Löschung im Shop manuell vornehmen.

Generell empfehlen wir jedoch, Artikel nicht zu löschen, sondern nur inaktiv zu setzen.

## Löschen der Integration

> **Warnung**
>
> **Diese Funktion entfernt die Integration unwiderruflich. Dies bedeutet, dass alle verbundenen Daten und Einstellungen entfernt werden und die Integration nicht wiederhergestellt werden kann. ** Wenn du dir ganz sicher bist, dass du die Integration nicht mehr benötigst, z. B. weil du sie nur testweise angelegt hattest, kannst du die Funktion im Abschnitt ** Gefahrenbereich **verwenden. Stelle sicher, dass du alle benötigten Daten gesichert hast und dass du die richtige Integration ausgewählt hast. Klicke dann auf ** Löschen**.

![Mirakl_Einstellungen_Loschfunktion.png](https://help.xentral.com/hc/article_attachments/19385157549468)

Du erhälst eine Sicherheitsabfrage, die du bestätigen musst. Die Integration wird nach Bestätigung endgültig und unwiderruflich entfernt.