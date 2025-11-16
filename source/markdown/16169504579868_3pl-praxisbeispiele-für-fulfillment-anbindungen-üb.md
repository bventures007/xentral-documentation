Dieser Artikel bietet dir einen Überblick über die gängigsten Workflows bei der Zusammenarbeit mit einem Fulfillment-Dienstleister und die entsprechenden Einstellungen, die du dazu in Xentral vornehmen musst. In diesem Artikel findest du genaue Anleitungen über die Einstellungen, die absolut notwendig sind. Zusätzlich erhältst du einige Empfehlungen und Hinweise auf optionale Funktionen, die entsprechend gekennzeichnet sind.

> **Tipp**
>
> Möchtest du dir innerhalb weniger Minuten einen Überblick über die Praxisbeispiele für Fulfillment-Anbindungen in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> [en-us]Are you looking for a quick overview on the practical examples for fulfillment integrations in Xentral? Then, our video tutorial is exactly right for you. Take a look right away!
>
> **[YouTube Video](https://www.youtube.com/embed/rU3MkCSSLp8)**>** Wichtig**
>
> Die folgenden Inhalte setzen voraus, dass du die erforderlichen Schritte zur Grundeinrichtung in Xentral bereits durchgeführt hast. Wenn du dir nicht sicher bist oder die Informationen noch einmal prüfen möchtest, lies dir unseren ArtikelVorbereitende Einstellungen in Xentral durch. Die folgenden Schritte müssen abgeschlossen sein, bevor du mit den Einstellungen für die einzelnen Workflows fortfahren kannst:
>
> - Schritt 1: Prozess aktivieren
> - Schritt 2: API-Account erstellen
> - Schritt 3: Projekt erstellen
> - Schritt 4: Lager und Lagerplatz anlegen

Pro Anwendungsfall erstellst du in Xentral separate so genannte Übertragungen (gelegentlich auch als *Übertragungen-Accounts* oder *Accounts* bezeichnet). **Beispiel**: Wenn du lediglich Lieferscheine übertragen möchtest, benötigst du eine einzige Übertragung für diesen Zweck. Für alle zusätzlichen Aktionen, wie zum Beispiel den Import von Tracking-Daten zurück in Xentral, benötigst du jeweils weitere Übertragungen.

> **Tipp**
>
> Mithilfe der Informationen auf dieser Seite kannst du den Datenaustausch so einrichten, dass die am häufigsten benötigten Standard-Daten übermittelt werden. Wenn du dich für fortgeschrittene Anwendungsfälle interessierst oder die Strukturen innerhalb des Datenaustausches selbstständig anpassen möchtest, musst du weitere Schritte ausführen. Mit den entsprechenden technischen Kenntnissen kannst du den Datenaustausch zu einem hohen Grad individualisieren. Schau dir dazu unsere Informationen zu **Smarty** an:
>
> - Einführung Smarty
> - Smarty Felddefinitionen
> - Smarty im Übertragungen Modul

## Lieferscheine übertragen

Wenn du in Xentral erstellte Lieferscheine an deinen Fulfillment-Dienstleister übermittelst, sieht das Personal im Fulfillment-Lager anhand der Lieferscheine, welche Artikel versendet werden müssen. Das bedeutet, dass du deine Aufträge bis einschließlich zur[Übergabe in den Auto-Versand](https://help.xentral.com/hc/de/articles/6113578120092#UUID-99504608-d895-41ad-5059-de028e933077)und damit der Erzeugung des Lieferscheins ganz regulär in Xentral verarbeitest. Anschließend werden die Lieferscheine mittels einer eigenen Übertragung an den Fulfillment-Dienstleister übermittelt, der den weiteren Versandprozess abwickelt.

![praxisbeispiel_lieferschein.jpg](https://help.xentral.com/hc/article_attachments/19499485180060)

Lege eine neue Übertragung an, um die Übermittlung der Lieferscheine an deinen Fulfillment-Dienstleister zu ermöglichen. Gehe dazu wie folgt vor.

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > Übertragungen (CSV/XML/EDI/PDF)**. * Oder *: Suche mit der Smart Search nach dem Modul **Übertragungen (CSV/XML/EDI/PDF)**.

1. Klicke oben rechts auf **+ NEU**.
1. Nimm die Einstellungen wie unten beschrieben vor und klicke dann auf **Speichern**.

### Bereich Einstellungen

| Option | Einstellung |
| --- | --- |
| **Aktiv** | Aktiviere diese Option, um den Datenaustausch zu ermöglichen und somit Lieferscheine an deinen Fulfillment-Dienstleister zu übertragen. |
| **Bezeichnung** | Vergib einen Namen für die Übertragung, die du zur Übermittlung von Lieferscheinen anlegst. Der Name sollte für dich und deine Mitarbeiter eindeutig sein und ist außerhalb deines Xentral Systems nicht sichtbar. |

### Bereich Kommunikation

| Option | Einstellung |
| --- | --- |
| **API** | Wähle den zuvor für die Übertragung angelegten API-Account aus. Weitere Informationen dazu, wie du den API-Account in Xentral anlegst, findest du [hier](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt2API-Accounterstellen). |
| **Übertragungsformat** | Wähle das gewünschte Dateiformat, in dem Lieferscheine aus deinem Xentral System übertragen werden sollen. Wir empfehlen die Übertragung per CSV oder XML. |
| **Typ **| Wir empfehlen dir, hier die Option ** SFTP** auszuwählen. |
| **Server** | Gib den Server an, an den die Übertragung gerichtet wird. Diese Information erhältst du in der Regel von deinem Fulfillment-Dienstleister. |
| **Port** | Trage den spezifischen Port des zuvor angegebenen Servers an, der die Übertragung empfängt. Diese Information erhältst du in der Regel von deinem Fulfillment-Dienstleister. |
| **Username** | Gib deinen Benutzernamen für den zuvor angegebenen Server an. Diese Information erhältst du in der Regel von deinem Fulfillment-Dienstleister. |
| **Passwort** | Gib das Passwort für deinen Zugang zum Server an, falls es benötigt wird. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Speicherort (Ausgang)** | Gib den Speicherort auf dem Server an, auf dem die ausgehenden Lieferscheine abgelegt werden. Diese Information erhältst du in der Regel von deinem Fulfillment-Dienstleister. Tipp: Verwende bei der Angabe des Speicherorts nach Möglichkeit relative Pfade. |
| **Dateiname Prefix**|* Optional*: Trage einen Präfix ein, den jeder Lieferschein automatisch im Rahmen der Übertragung erhält. So kannst du übertragene Lieferscheine später anhand verschiedener Merkmale, z.B. dem Projekt, leichter unterscheiden. |

### Bereich Belege versenden

| Option | Einstellung |
| --- | --- |
| **Belegart **| Wähle die Option ** Lieferschein** aus. |
| **Belegstatus** | Gib den Status ein, in dem Lieferscheine sich befinden müssen, damit sie übertragen werden. In den meisten Anwendungsfällen ist hier die Eingabe “FREIGEGEBEN” korrekt. Somit werden Lieferscheine übertragen, sobald du sie in deinem Xentral System freigegeben hast. Je nach deinem Bedarf kannst du hier aber auch einen anderen Belegstatus auswählen. Verwende stets genau die Schreibweise für den Status, wie er auch in deinem Xentral System angegeben ist. Andernfalls kommt es zu Fehlern bei der Übertragung. |
| **Projekt** | Wähle das Projekt aus, dessen Lieferscheine übertragen werden sollen. |
| **Adresse oder Gruppe**|* Optional*: Wähle eine spezifische Adresse oder Gruppe aus, um die Übertragung auf Lieferscheine zu beschränken, die zu genau dieser Adresse oder Gruppe gehören. |
| **Manuelle Freigabe erforderlich**|* Optional *: Wenn du diese Option aktivierst, musst du jeden Lieferschein einzeln für die Übertragung freigeben, bevor die Übertragung stattfindet. Diese Einstellung kann nützlich sein, wenn du deine Übertragung zu Beginn erst einmal testen möchtest. Du kannst diese Option jederzeit wieder deaktivieren, um Lieferscheine anschließend automatisch zu übertragen. Solange die Option **Manuelle Freigabe erforderlich ** aktiviert ist, gibst du die einzelnen Belege manuell zur Übertragung frei, indem du im Menü**Übertragungen (CSV/XML/EDI/PDF)** auf das Tab ** Manuelle Freigabe** klickst. |
| **Start ab ID oder Start ab Datum** | Entscheide dich für eine bestimmte Lieferschein-ID und ein bestimmtes Datum, ab dem die Lieferscheine an deinen Fulfillment-Dienstleister übertragen werden sollen. Die Lieferscheine werden übermittelt, sobald beide Bedingungen gleichzeitig zutreffen. |
| **Filter-Labels **| Achtung: Diese Option erscheint erst, nachdem du die Einstellungen für die Übertragung einmalig gespeichert hast! Labels erlauben dir, die in der Übertragung enthaltenen Lieferscheine auf einen Blick in deinem Xentral System zu unterscheiden und nach speziellen Labels zu filtern. Lege zuerst mithilfe der Option ** Filter-Labels **fest, nach welchen Labels du innerhalb der Übertragung filtern möchtest. Nutze dann die Optionen ** Label erfolgreiche Übertragung **und ** Label fehlerhafte Übertragung**, um ein Label für diese Szenarien auszuwählen. Das Label wird in diesen Fällen dann automatisch für die betroffenen Lieferscheine vergeben und in deinem Xentral System angezeigt. Klicke auf die Filter-Symbole neben den genannten Optionen, um eine Liste aller verfügbaren Labels zu sehen. Scrolle bis an das Ende der Liste, um bei Bedarf neue Labels anzulegen und direkt zu verwenden. |
| **Jeder Beleg in einer eigenen XML** | Wenn du das Übertragungsformat XML nutzt, empfehlen wir dir, diese Option zu aktivieren, damit jeder Lieferschein in einer separaten XML-Datei übermittelt wird. |

## Tracking-Informationen empfangen

In diesem Anwendungsfall zeigen wir dir, wie du eine Übertragung anlegst, sodass Tracking-Informationen von deinem Fulfillment-Dienstleister automatisiert in dein XentralSystem übertragen werden. Nachdem dein Fulfillment-Dienstleister die benötigte Ware für die Aufträge kommissioniert und verpackt hat, steht als nächster Schritt der Versand der Ware an. Dabei erhält jedes Paket, das an deine Endkunden versandt wird, eine Sendungsnummer und einen Tracking-Link. Diese Daten fordert Xentral dann beim Server deines Fulfillment-Dienstleisters an und importiert sie anschließend in dein System - es handelt sich also um eine eingehende Datenbewegung. Im Anschluss kannst du diese informationen deinen Kunden bereitstellen, um sie über den Versand der Ware zu informieren und ihnen zu ermöglichen, die Sendungen nachzuverfolgen.

![praxisbeispiel_tracking.jpg](https://help.xentral.com/hc/article_attachments/19501987019420)

Lege eine neue Übertragung an, um die Rückmeldung der Tracking-Informationen vonseiten deines Fulfillment-Dienstleisters zu ermöglichen. Gehe dazu wie folgt vor.

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > Übertragungen (CSV/XML/EDI/PDF)**. * Oder *: Suche mit der Smart Search nach dem Modul **Übertragungen (CSV/XML/EDI/PDF)**.

1. Klicke oben rechts auf **+ NEU**.
1. Nimm die Einstellungen wie unten beschrieben vor und klicke dann auf **Speichern**.

### Bereich Einstellungen

| Option | Einstellung |
| --- | --- |
| **Aktiv** | Aktiviere diese Option, um den Datenaustausch zu ermöglichen und somit Tracking-Informationen von deinem Fulfillment-Dienstleister zu empfangen. |
| **Bezeichnung** | Vergib einen Namen für die Übertragung, die du zum Empfang von Tracking-Informationen anlegst. Der Name sollte für dich und deine Mitarbeiter eindeutig sein und ist außerhalb deines Xentral Systems nicht sichtbar. |

### Bereich Kommunikation

| Option | Einstellung |
| --- | --- |
| **API** | Wähle den zuvor für die Übertragung angelegten API-Account aus. Weitere Informationen dazu, wie du den API-Account in Xentral anlegst, findest du [hier](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt2API-Accounterstellen). |
| **Übertragungsformat** | Wähle das gewünschte Dateiformat, in dem Tracking-Informationen in dein Xentral System übertragen werden sollen. Wir empfehlen die Übertragung per XML. |
| **Typ **| Wir empfehlen dir, hier die Option ** SFTP** auszuwählen. |
| **Server** | Gib den Server an, von dem die Tracking-Informationen abgeholt werden sollen. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Port** | Trage den spezifischen Port des zuvor angegebenen Servers an. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Username** | Gib deinen Benutzernamen für den zuvor angegebenen Server an. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Passwort** | Gib das Passwort für deinen Zugang zum Server an, falls es benötigt wird. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Speicherort (Ausgang)** | Gib den Speicherort auf dem Server an, von dem die Tracking-Informationen abgeholt werden. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. Tipp: Verwende bei der Angabe des Speicherorts nach Möglichkeit relative Pfade. |
| **Dateiname Prefix** | Trage einen Präfix ein, um nur Dateien in Xentral zu übernehmen, die genau diesen Präfix enthalten. Sprich die Details in jedem Fall mit deinem Fulfillment-Dienstleister ab, bevor du diese Einstellung verwendest. Beachte, dass Dateien ohne diesen Präfix nicht in dein Xentral System übertragen werden. |

### Bereich Belege empfangen

| Option | Einstellung |
| --- | --- |
| **Tracking empfangen** | Aktiviere diese Option, um den Datenaustausch zu ermöglichen und somit Tracking-informationen von deinem Fulfillment-Dienstleister zu erhalten. |
| **Gemeldete MHD / Chargen auslagern** | Diese Option ist für dich nur relevant, wenn du an deinen Artikeln Mindesthaltbarkeitsdaten oder Chargennummern pflegst. Wenn du diese Option aktivierst, werden keine Bestände ausgebucht, sondern die entsprechenden MHD- und Chargeninformationen werden automatisch in den Lieferschein und die Datenbank übernommen. |

### Bereich Belege versenden

| Option | Einstellung |
| --- | --- |
| **Belegart **| Wähle hier die Einstellung**

- keine Belege -** aus, da du keine Belege versenden, sondern Tracking-Informationen empfangen möchtest. |
| **Tracking Mail** | Aktiviere diese Option, um automatisch eine E-Mail mit den Tracking-Informationen an deine Kunden zu versenden, nachdem die entsprechenden Informationen deines Fulfillment-Dienstleisters in dein Xentral System übertragen wurden. |
| **Rechnung Mail**|* Optional *: Aktiviere diese Option, um automatisch eine E-Mail mit der Rechnung an deine Kunden zu versenden, nachdem die Tracking-Informationen deines Fulfillment-Dienstleisters in dein Xentral System übertragen wurden. **Wichtig**: Die Voraussetzung für den Versand dieser E-Mail ist, dass für die entsprechenden Aufträge bereits eine Rechnung in deinem Xentral System erstellt wurde. Diese Rechnung muss den vollständigen Namen und die E-Mail-Adresse des Kunden enthalten und der Rechnungsbetrag muss größer als 0,00 € sein. |
| **Rechnung anlegen**|* Optional*: Aktivierst du diese Option, wird nach der Bereitstellung der Tracking-Informationen in Xentral automatisch eine Rechnung für den entsprechenden Auftrag angelegt, falls der Beleg zuvor noch nicht erzeugt wurde. |

## Lagerbestände empfangen

![praxisbeispiel_lagerbestand.jpg](https://help.xentral.com/hc/article_attachments/19501968350364)

Lege eine neue Übertragung an, um die Rückmeldung der Lagerbestände vonseiten deines Fulfillment-Dienstleisters zu empfangen. Gehe dazu wie folgt vor.

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > Übertragungen (CSV/XML/EDI/PDF)**. * Oder *: Suche mit der Smart Search nach dem Modul **Übertragungen (CSV/XML/EDI/PDF)**.

1. Klicke oben rechts auf **+NEU**.
1. Nimm die Einstellungen wie unten beschrieben vor und klicke dann auf **Speichern**.

### Bereich Einstellungen

| Option | Einstellung |
| --- | --- |
| **Aktiv** | Aktiviere diese Option, um den Datenaustausch zu ermöglichen und somit die Lagerzahlen von deinem Fulfillment-Dienstleister zu empfangen. |
| **Bezeichnung** | Vergib einen Namen für die Übertragung, die du zum Empfang von Lagerzahlen anlegst. Der Name sollte für dich und deine Mitarbeiter eindeutig sein und ist außerhalb deines Xentral Systems nicht sichtbar. |

### Bereich Kommunikation

| Option | Einstellung |
| --- | --- |
| **API** | Wähle den zuvor für die Übertragung angelegten API-Account aus. Weitere Informationen dazu, wie du den API-Account in Xentral anlegst, findest du [hier](#). |
| **Übertragungsformat** | Wähle das gewünschte Dateiformat, in dem Lagerzahlen in dein Xentral System übertragen werden sollen. Wir empfehlen die Übertragung per XML. |
| **Typ **| Wir empfehlen, hier die Option ** SFTP** auszuwählen. |
| **Server** | Gib den Server an, von dem die Bestandsinformationen abgeholt werden sollen. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Port** | Trage den spezifischen Port des zuvor angegebenen Servers an. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Username** | Gib deinen Benutzernamen für den zuvor angegebenen Server an. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Passwort** | Gib das Passwort für deinen Zugang zum Server an, falls es benötigt wird. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Speicherort (Ausgang)** | Gib den Speicherort auf dem Server an, von dem die Lagerzahlen abgeholt werden. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. Tipp: Verwende bei der Angabe des Speicherorts nach Möglichkeit relative Pfade. |
| **Dateiname Prefix**|* Optional*: Trage einen Präfix ein, um nur Dateien in Xentral zu übernehmen, die genau diesen Präfix enthalten. Sprich die Details in jedem Fall mit deinem Fulfillment-Dienstleister ab, bevor du diese Einstellung verwendest. Beachte, dass Dateien ohne diesen Präfix nicht in dein Xentral System übertragen werden. |

### Bereich Belege empfangen

| Option | Einstellung |
| --- | --- |
| **Lagerzahlen empfangen** | Aktiviere diese Option, um den Datenaustausch zu ermöglichen und somit Lagerzahlen von deinem Fulfillment-Dienstleister zu erhalten. |
| **Lagerplatz in Dateieingang ignorieren** | Falls dein Fulfilment-Dienstleister dir Lagerplätze innerhalb einer XML-Datei zurückmeldet, werden die entsprechenden Bestände in Xentral auf den Lagerplatz gebucht, den du in den [Einstellungen der Übertragung](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt5bertragungen-Accountanlegen) festgelegt hast. Wenn du diese Einstellung aktivierst, gilt dies auch, falls in der übermittelten XML-Datei abweichende Lagerplätze angegeben sind. Ist die Einstellung deaktiviert, werden die Lagerplätze übernommen, die vom Fulfillment-Dienstleister übermittelt werden. Wir empfehlen dir, diese Einstellung stets zu aktivieren. |
| **Lager** | Falls dein Fulfillment-Dienstleister Bestände ohne spezifische Lagerplatzangabe an Xentral zurückmeldet, ist dies der Lagerplatz, auf den die betreffenden Artikel gebucht werden. So kannst du diesen Lagerplatz regelmäßig gezielt prüfen und die Artikel auf ihre finalen Lagerplätze umbuchen. |
| **Einlagerungsverhalten **| Hier empfehlen wir die Option ** Überschreiben**. |

## Artikel übertragen

Wenn du neue Artikel in Xentral anlegst oder Daten bereits vorhandener Artikel änderst, also zum Beispiel Informationen wie den Artikelnamen anpasst, kannst du diese Änderungen ebenfalls über eine Übertragung an deinen Fulfillment-Dienstleister kommunizieren, der diese Artikel für dich lagert und versendet.

> **Wichtig**
>
> Beachte, dass geänderte Artikeldaten niemals automatisch an den Fulfillment-Dienstleister übertragen werden. Diesen Prozess musst du manuell anstoßen, indem du die Funktion **Artikel übertragen** innerhalb der Einstellungen der Übertragung nutzt. Du hast jedoch die Option, neu angelegte Artikel automatisch übertragen zu lassen. Weitere Informationen dazu findest du in der Tabelle unten.

![praxisbeispiel_artikel.jpg](https://help.xentral.com/hc/article_attachments/19499787274780)

Lege eine neue Übertragung an, um Artikel an deinen Fulfillment-Dienstleister zu senden. Gehe dazu wie folgt vor.

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > Übertragungen (CSV/XML/EDI/PDF)**. * Oder *: Suche mit der Smart Search nach dem Modul **Übertragungen (CSV/XML/EDI/PDF)**.

1. Klicke oben rechts auf **+ NEU**.
1. Nimm die unten beschriebenen Einstellungen vor und klicke dann auf **Speichern**.

### Bereich Einstellungen

| Option | Einstellung |
| --- | --- |
| **Aktiv** | Aktiviere diese Option, um den Datenaustausch zu ermöglichen und somit Artikeldaten an deinen Fulfillment-Dienstleister zu übertragen. |
| **Bezeichnung** | Vergib einen Namen für die Übertragung, die du für die Übertragung von Artikeln an deinen Fulfillment-Dienstleister erstellst. Der Name sollte für dich und deine Mitarbeiter eindeutig sein und ist außerhalb deines Xentral Systems nicht sichtbar. |

### Bereich Kommunikation

| Option | Einstellung |
| --- | --- |
| **API** | Wähle den zuvor für die Übertragung angelegten API-Account aus. Weitere Informationen dazu, wie du den API-Account in Xentral anlegst, findest du [hier](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt2API-Accounterstellen). |
| **Übertragungsformat** | Wähle das gewünschte Dateiformat, in dem Artikeldaten von deinem Xentral System an deinen Fulfillment-Dienstleister übertragen werden sollen. Wir empfehlen die Übertragung per XML. |
| **Typ** | Wähle hier den gewünschten Typ der Dateiübertragung aus. Den korrekten Typ erhältst du in der Regel von deinem Fulfillment-Dienstleister. |
| **Server** | Gib den Server an, von dem die Bestandsinformationen abgeholt werden sollen. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Port** | Trage den spezifischen Port des zuvor angegebenen Servers an. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Username** | Gib deinen Benutzernamen für den zuvor angegebenen Server an. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **Passwort** | Gib das Passwort für deinen Zugang zum Server an, falls es benötigt wird. Diese Information erhältst du in der Regel von deinen Fulfillment-Dienstleister. |

### Bereich Sonstige Aktionen

| Option | Einstellung |
| --- | --- |
| **Artikel übertragen** | Klicke auf diesen Button, um Daten neuer und geänderter Artikel an das System deines Fulfillment-Dienstleisters zu übertragen. |
| **Automatisch neue Artikel übertragen **| Aktiviere diese Option, um Artikel, die du in Xentral neu anlegst, automatisch an deinen Fulfillment-Dienstleister zu übertragen. Beachte jedoch, dass diese Einstellung nicht greift, wenn du Daten bestehender Artikel in Xentral änderst. Wenn du Artikeldaten änderst, musst du die Option ** Artikel übertragen** nutzen, um diese Änderungen zu übermitteln. |