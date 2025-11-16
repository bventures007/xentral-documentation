## Überblick

> **Anmerkung**
>
> **Funktionserweiterung 02/2025:** Ab sofort kannst du dich aktiv über den Auftragsimport-Status per e-Mail benachrichtigen lassen. Richte einfach über die Systemstatus-Seite > Alarms verwalten > Alarm erstellen ein Abo ein. Du kannst deine Schnittstelle(n) und die Häufigkeit der Benachrichtigung wählen und festlegen, ob eine Benachrichtigung bei Warnung und/oder im Fehlerfall erfolgen soll. Mehr Infos zum Systemstatus findest du unterSystemstatus

Das Journal unterstützt dich dabei, den aktuellen Status deiner Anbindung zu überprüfen und mögliche Fehlerquellen bei der Einrichtung oder im laufenden Betrieb einzugrenzen.

Du erreichst das Journal unter dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware6 Connector > Journal**:

![Shopware_Journal_Ubersicht.png](https://help.xentral.com/hc/article_attachments/18671654982684)

Dieser Bereich umfasst folgende Funktionen:

- Testen der Workflow-Konfiguration vor der Produktivschaltung mit einzelnen Datensätzen
- Überwachen der Datensynchronisation im Produktivbetrieb
- Manuelles Anstoßen der Übertragung einzelner Datensätze im laufenden Betrieb

## Artikel

### Statusansicht

Im Reiter Artikel bekommst du einen Detailüberblick zum Synchronisierungsstatus der Artikeldaten zwischen Shop und Xentral. Dies umfasst die Artikelstammdaten, Bestände und Preise.

![connect_reportingstatus.png](https://help.xentral.com/hc/article_attachments/18671654983964)

Die farbcodierten Felder in der Mitte zeigen dir den Synchronisierungsstatus der einzelnen Artikel. Beim ersten Aufruf ist der Status grau. Folgende Status sind generell möglich:

![Shared_Journal_Status.png](https://help.xentral.com/hc/article_attachments/18671702040732)

Ist der Export fehlerhaft, wird dir eine Fehlermeldung angezeigt, die bei der Suche nach der Fehlerursache helfen kann. Nutze die[Filterfunktionen](#UUID-0748de4e-37e4-85a3-21a3-6a2c51fcb42b_section-idm234565914622809)(siehe unten), um nach fehlerhaften Datensätzen zu suchen und diese nach der Fehlerbehebung erneut zum Austausch anzustoßen.

### Manuelle Synchronisation

Um Daten manuell zu synchronisieren, nutze die Aktions-Schaltflächen auf der rechten Seite:

![connect_manuelle-synchronisation_aktions-schaltflachen.png](https://help.xentral.com/hc/article_attachments/18671702041372)

**(1)** Verwende ** Artikel synchronisieren > Artikel-Synchronisierung starten**, um einen bestimmten Artikel von Xentral an den Shop zu senden. Es werden dann die Stammdaten dieses Artikels übertragen.

![Shopify_ReportingArtikelSync_0404p.png](https://help.xentral.com/hc/article_attachments/18671654991004)

> **Anmerkung**
>
> Es werden hier nur diejenigen Datentypen übertragen, die in den Workflows aktiviert wurden. Hast du z. B. unter **Workflows > Artikel ** den Datentyp “Freifelder” nicht aktiviert, so werden hier keine Freifelder synchronisiert. ** (2)** Verwende ** Bestand synchronisieren > Bestand-Synchronisierung starten**, um den Bestand eines bestimmten Artikels von Xentral an den Shop zu senden.

![Shopify_ReportingBestandSync_0404p.png](https://help.xentral.com/hc/article_attachments/18671702043676)

**(3)** Verwende ** Preise synchronisieren > Preis-Synchronisierung starten**, um die Preise eines bestimmten Artikels von Xentral an den Shop zu senden.

![Shopify_ReportingPreisSync_0404p.png](https://help.xentral.com/hc/article_attachments/18671702044828)

> **Anmerkung**
>
> Durch Anhaken mehrerer Datensätze kannst du die oben genannten Funktionen gleichzeitig für alle ausgewählten Datensätze durchführen:
>
> (1) Alle darunter liegende Datensätze markieren. Einzelne können bei Bedarf wieder abgewählt werden.
>
> (2) Markiert alle Datensätze, die den Filterkriterien entsprechen - auch die Einträge, die auf Seite zwei, drei usw. aufgelistet sind.
>
> (3) Startet die Synchronisierung für alle markierten Datensätze.

Nachdem du eine Synchronisierung gestartet hast, kannst du den Verlauf verfolgen, indem du auf **Neu Laden** klickst.

![connect_journal_neu-laden.png](https://help.xentral.com/hc/article_attachments/18671702048156)

> **Anmerkung**
>
> Im Produktivbetrieb werden die Artikel-, Bestands- und Preis-Daten zwischen Shop und Xentral ereignisbasiert ausgetauscht, also immer nur dann, wenn ein Datensatz geändert wird. Wenn du einzelne Datensätze unabhängig von Änderungen manuell anstoßen möchtest, kannst du die in diesem Abschnitt beschriebenen Aktionen nutzen.

#### Such- und Filtermöglichkeiten Artikel

Zur einfachen und übersichtlichen Analyse stehen dir im Artikel-Journal verschiedene Such- und Filtermöglichkeiten zur Verfügung:

- **Freitextsuche**: Du kannst die angezeigten Einträge über einen Freitext im Suchfeld einschränken:
- **Filter nach Status und/oder Zeitraum**: Klicke auf “Stammdaten”, “Bestand” bzw. “Preis”, um z.B. nur fehlerhafte Exporte in einem bestimmten Zeitraum anzeigen zu lassen:
- **Filter nach Typ**: Diesen Filter kannst du nutzen, um nach Matrixprodukten oder Varianten zu filtern. Dies unterstützt bei der Performanceoptimierung des manuellen Datenaustauschs.

> **Anmerkung**
>
> Wenn ein übergeordnetes Matrixprodukt zur Synchronisierung angestoßen wird, werden dazugehörige Varianten automatisch mit synchronisiert. Wenn du Matrixprodukte hast, empfiehlt es sich daher,
>
> - auf “Keine Varianten” zu filtern und auf dieser Ebene zu triggern, um Varianten nicht doppelt in die Warteschlange zu bringen.
> - “Nur Varianten” dann zu verwenden, wenn nachträglich neue Varianten dazukommen, die manuell angestoßen werden sollen.

## Aufträge

> **Anmerkung**
>
> Funktionserweiterung 02/2025: Ab sofort kannst du dich aktiv über den Auftragsimport-Status per e-Mail benachrichtigen lassen. Richte einfach über die Systemstatus-Seite > Alarms verwalten > Alarm erstellen ein Abo ein. Du kannst deine Schnittstelle(n) und die Häufigkeit der Benachrichtigung wählen und festlegen, ob eine Benachrichtigung bei Warnung und/oder im Fehlerfall erfolgen soll. Mehr Infos zum Systemstatus findest du unterSystemstatus

Im Reiter **Aufträge** kannst du den Synchronisierungsstatus deiner Aufträge zwischenShopund Xentral verfolgen.

Klicke auf **Aufträge importieren**…

![connect_journal_testworkflow.png](https://help.xentral.com/hc/article_attachments/18671702053916)

... und gib eine Auftragsnummer ein und bestätige mit **Importieren**.

![Shopify_ReportingWorkflowsAuftr01_0502p.png](https://help.xentral.com/hc/article_attachments/18671702057372)

> **Tipp**
>
> Du kannst mehrere Aufträge importieren, indem du die Auftragsnummern durch Komma getrennt eingibst.

Ein Auftrag wird zunächst zu Connect geladen und von dort im zweiten Schritt in Xentral importiert. Mit **Neu Laden ** (1) kannst du den Status aktualisieren, über ** Verlauf anzeigen** (2) die Statushistorie ansehen. Der Tooltipp gibt dir ggf. Hinweise, weshalb Daten nicht übertragen werden konnten, z. B. wegen fehlender Steuerangaben im Shop. Mit Schaltfläche (3) kannst du Datensätze erneut ausführen, nachdem du die entsprechenden Korrekturen vorgenommen hast.

![Shopify_ReportingWorkflowsAuftr02_0502p.png](https://help.xentral.com/hc/article_attachments/18671655004188)

> **Anmerkung**
>
> Bereits vorhandene Aufträge werden nicht erneut importiert, um Duplikate zu vermeiden.

Auch in der Statushistorie kannst du den Status **Neu Laden**:

![Shopify_ReportingWorkflowsAuftr03_0502p.png](https://help.xentral.com/hc/article_attachments/18671655005596)

> **Anmerkung**
>
> Im Produktivbetrieb werden die Auftrags-Daten zwischen Shop und Xentral alle 15 Minuten automatisiert ausgetauscht. Wenn du einzelne Datensätze vorher manuell anstoßen möchtest, kannst du die in diesem Abschnitt beschriebenen Aktionen nutzen.

### Such- und Filtermöglichkeiten Aufträge

Zur einfachen und übersichtlichen Analyse stehen dir im Auftrags-Journal verschiedene Such- und Filtermöglichkeiten zur Verfügung:

- **Freitextsuche**: Du kannst die angezeigten Einträge über einen Freitext im Suchfeld einschränken:
- **Filter nach Status**: Klicke auf “Status”, um z. B. nur fehlerhafte Exporte anzeigen zu lassen:
- **Filter nach Auftragsdatum**: Diesen Filter kannst du nutzen, um nach einem bestimmten Auftragsdatum zu filtern:

## Auftragsstatus und Tracking

Im Reiter **Auftragsstatus & Tracking** siehst du den Synchronisierungsstatus deiner Auftragsstatus- und Tracking-Daten zwischenShopund Xentral.

Klicke auf **Auftragsstatus & Tracking exportieren**…

![connect_journal_salesorderstatus.png](https://help.xentral.com/hc/article_attachments/18671702063260)

... und gib eine Auftragsnummer ein und bestätige mit **Exportieren**.

![Shopify_ReportingWorkflowsAuftrStatus01_0502p.png](https://help.xentral.com/hc/article_attachments/18671702064156)

> **Tipp**
>
> Du kannst mehrere Aufträge importieren, wenn du die Auftragsnummern durch Komma getrennt eingibst.

Mit **Neu Laden ** (1) kannst du den Status aktualisieren, über ** Verlauf anzeigen** (2) die Statushistorie ansehen. Mit Schaltfläche (3) kannst du Datensätze erneut ausführen, nachdem du ggf. Korrekturen vorgenommen hast

![Shopify_ReportingWorkflowsAuftrStatus02_0502p.png](https://help.xentral.com/hc/article_attachments/18671655011356)

Auch in der Statushistorie kannst du den Status **Neu Laden**:

![connect_reporting_salesorderstatus_shopware6.png](https://help.xentral.com/hc/article_attachments/14528192540444)

Sobald du alle Daten erfolgreich getestet hast, ist dein System bereit für die Liveschaltung.

> **Anmerkung**
>
> Im Produktivbetrieb werden die Auftragsstatus- & Tracking-Daten zwischen Shop und Xentral ereignisbasiert ausgetauscht, also immer nur dann, wenn ein Datensatz geändert wird. Wenn du einzelne Datensätze unabhängig von Änderungen manuell anstoßen möchtest, kannst du die in diesem Abschnitt beschriebenen Aktionen nutzen.

### Such- und Filtermöglichkeiten Auftragsstatus & Tracking

Zur einfachen und übersichtlichen Analyse stehen dir im Auftragsstatus-Journal verschiedene Such- und Filtermöglichkeiten zur Verfügung:

- **Freitextsuche**: Du kannst die angezeigten Einträge über einen Freitext im Suchfeld einschränken:
- **Filter nach Status**: Klicke auf “Status”, um z. B. nur fehlerhafte Exporte anzeigen zu lassen:
- **Filter nach Auftragsdatum**: Diesen Filter kannst du nutzen, um nach einem bestimmten Auftragsdatum zu filtern:
- **Filter nach Tracking**: Mit diesem Filter kannst du Vorgänge bzgl. des Tracking-Exportstatus einschränken:

## Belege

> **Anmerkung**
>
> Funktionserweiterung 02/2025: Falls du die Schnittstelle schon länger nutzt, kann es sein, dass du diesen Reiter noch nicht sehen kannst. Um ihn zu aktivieren, folge in Xentral dem Pfad **Einstellungen > Verkaufen > Shops/Marktplätze > Shopware6-Connector > Einstellungen (Zahnrädchen)** und aktiviere dort das Feature "Belege". Gehe außerdem zu den Workflows und aktiviere dort die Schaltflächen. Mehr Infos dazu findest duhier.

Im Reiter **Belege** kannst du den Exportstatus der Belege von Xentral an denShopverfolgen.

Klicke auf **Belege exportieren**....

![MiraklSW6_Journal_Belege_BelegeExportieren.png](https://help.xentral.com/hc/article_attachments/18671655016476)

... und gib eine Auftragsnummer ein und bestätige mit **Exportieren**.

![MiraklSW6_Journal_Belege_BelegeExportieren_Auftragsnummer.png](https://help.xentral.com/hc/article_attachments/18671655017500)

> **Tipp**
>
> Du kannst Belege mehrerer Aufträge exportieren, indem du die Auftragsnummern durch Komma getrennt eingibst.

Ein Beleg wird zunächst zu Connect geladen und von dort im zweiten Schritt an denShopexportiert. Mit **Neu Laden ** (1) kannst du den Status aktualisieren, über ** Verlauf anzeigen** (2) die Statushistorie ansehen. Der Tooltipp gibt dir ggf. Hinweise, weshalb Belege nicht übertragen werden konnten. Mit Schaltfläche (3) kannst du Datensätze erneut ausführen, nachdem du die entsprechenden Korrekturen vorgenommen hast.

![MiraklSW6_Journal_Belege_Schaltflachen.png](https://help.xentral.com/hc/article_attachments/18671702069532)

> **Anmerkung**
>
> Bereits vorhandene Belege werden nicht erneut exportiert, um Duplikate zu vermeiden.

Auch in der Statushistorie kannst du den Status **Neu Laden**:

![MiraklSW6_Journal_Belege_Historie.png](https://help.xentral.com/hc/article_attachments/18671655022876)

> **Anmerkung**
>
> Im Produktivbetrieb werden die Belege zwischen Xentral undShopereignisbasiert ausgetauscht, also immer nur dann, wenn ein Beleg erstmalig erzeugt wird.

### Such- und Filtermöglichkeiten Belege

Zur einfachen und übersichtlichen Analyse stehen dir im Belege-Journal verschiedene Such- und Filtermöglichkeiten zur Verfügung:

- **Freitextsuche**: Du kannst die angezeigten Einträge über einen Freitext im Suchfeld einschränken:
- **Filter nach Status**: Klicke auf “Status”, um z. B. nur fehlerhafte Exporte anzeigen zu lassen:
- **Filter nach Belegdatum**: Diesen Filter kannst du nutzen, um nach einem bestimmten Belegdatum zu filtern: