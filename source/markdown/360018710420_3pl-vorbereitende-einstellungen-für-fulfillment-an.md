Du möchtest einen Fulfillment- oder Logistikdienstleister an Xentral anbinden und fragst dich, was du dafür tun musst? Dann erfährst du in diesem Artikel, welche Schritte zur Grundeinrichtung gehören und welche konkreten Einstellungen du in Xentral vornehmen musst, um einen reibungslosen Datenaustausch zu gewährleisten.

> **Wichtig**
>
> Stelle sicher, dass du Folgendes erledigt hast, bevor du mit dem Übertragungen Modul in Xentral arbeitest und die ersten Einstellungen vornimmst:
>
> - Du hast dich für einen Fulfillment- bzw. Logistikdienstleister entschieden und eure Zusammenarbeit vertraglich geregelt
> - Du verfügst über Zugang zu einem geeigneten FTP-Server (je nach Workflow von dir oder deinem Dienstleister zur Verfügung gestellt), über den der Datenaustausch stattfinden wird
> - Du hast entschieden, welche Schritte deines Logistikprozesses ausgelagert werden und genau festgelegt, wie die Prozesse zur Auftragsabwicklung in deinem eigenen Unternehmen ablaufen
> - Deine Mitarbeiter sind über den Logistikprozess informiert und entsprechend geschult

Nachdem du die oben genannten Vorbereitungen abgeschlossen hast, kannst du damit beginnen, die notwendigen Einstellungen in deinem System vorzunehmen. In den folgenden Kapiteln findest du detaillierte Anleitungen zu den einzelnen Schritten.

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in die Einstellungen für Fulfillment-Anbindungen**
>
> Möchtest du dir innerhalb weniger Minuten einen Überblick über die vorbereitenden Einstellungen für Fulfillment-Anbindungen in Xentral verschaffen? Dann ist unser Video-Tutorial genau das Richtige für dich. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/XG5zGxLlT2I)**

## Einstellungen in Xentral vornehmen

Wenn du zum ersten Mal einen Fulfillment-Dienstleister an Xentral anbindest, ist es wichtig, die Einstellungen in genau der Reihenfolge vorzunehmen, in der sie in den folgenden Kapiteln beschrieben werden.

Hast du einige Schritte bereits erledigt oder möchtest spezielle Informationen nachlesen? Dann klicke einfach auf einen der folgenden Links, um schnell zum passenden Kapitel zu gelangen.

- [Schritt 1: Prozess aktivieren](#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt1Prozessaktivieren)
- [Schritt 2: API-Account erstellen](#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt2API-Accounterstellen)
- [Schritt 3: Projekt erstellen](#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt3Projekterstellen)
- [Schritt 4: Lager und Lagerplatz anlegen](#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt4LagerundLagerplatzanlegen)
- [Schritt 5: Übertragungen-Account anlegen](#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt5bertragungen-Accountanlegen)

### Schritt 1: Prozess aktivieren

Im ersten Schritt aktivierst du im Modul **Prozessstarter** einen so genannten Cronjob. Cronjobs (in Xentral auch gelegentlich als * Prozesse*bezeichnet) dienen dazu, bestimmte Aktionen in regelmäßigen Abständen auszuführen. Für den regelmäßigen Datenaustausch zwischen deinem XentralSystem und der Schnittstelle deines Fulfillment-Dienstleisters musst du also den benötigten Prozess in Xentral aktivieren.

Gehe wie folgt vor, um den Prozess zu aktivieren:

1. Öffne das Menü **Einstellungen > Administration > Prozessstarter**. * Oder:*Suche mit der Smart Search nach dem Begriff **Prozessstarter**.

1. Finde den Eintrag **Übertragenmodul (Fulfillment, Übertragen, EDI, XML)** mit dem Parameter * api_uebertragungen* in der Liste.
1. Klicke auf das Stift-Symbol, um die Einstellungen des Prozesses zu öffnen.
1. Wähle für die Einstellung **Art ** die Option **Periodisch** aus dem Dropdown-Menü.
1. **Optional **: Passe im Feld ** Periode** das Zeitintervall (in Minuten) an, in dem der Prozess ausgeführt wird. Standardmäßig ist hier 10 eingetragen. Das bedeutet, dass der Import und Export der Belege innerhalb deiner Übertragungen alle 10 Minuten stattfindet.
1. Aktiviere die Option **Aktiv**.
1. Klicke auf **Speichern**.

> **Anmerkung**
>
> Benötigst du weitere Informationen zum Thema Prozesse und Prozessstarter? Schau dir unserenpassenden Artikel zum Themaan, um mehr zu erfahren.

### Schritt 2: API-Account erstellen

> **Tipp**
>
> **Video-Tutorial: Dein schneller Einstieg in die Erstellung des API-Accounts**
>
> Die folgenden Schritte zur Erstellung des API-Accounts werden auch in unserem Video-Tutorial gezeigt. Schau es dir gleich an!
>
> **[YouTube Video](https://www.youtube.com/embed/WKBMDdfbIvA)**

Der API-Accounts ist die technische Grundlage der Datenübertragung zwischen deinem XentralSystem und deinem Fulfillment-Dienstleister. Deshalb musst du mindestens einen API-Account erstellen, damit die Kommunikation stattfinden kann

> **Wichtig**
>
> Damit Übertragungen in Xentral angelegt werden können und der Datenaustausch stattfinden kann, ist muss ein API-Account wie unten beschrieben angelegt werden und über einen Namen verfügen. Alle weiteren Einstellungen am API-Account selbst, wie beispielsweise Berechtigungen, sind für die Funktionsweise von Übertragungen nicht relevant und müssen nicht zwingend vorgenommen werden.

Gehe wie folgt vor, um einen API-Account zu erstellen:

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > APIs**. * Oder:*Suche mit der Smart Search nach dem Begriff **APIs**.

1. Klicke oben rechts auf **Übertragungs-Account hinzufügen**.
1. Aktiviere die Option **Aktiv**.
1. Vergib im Feld **Bezeichnung** einen eindeutigen Namen für den API-Account, damit du diesen eindeutig identifizieren kannst.
1. *Optional *: Lege im Bereich **Permissions ** die Berechtigungen fest, über die der API-Account verfügen soll. Wir empfehlen, per Klick auf die Schaltfläche**Alle aktivieren** sämtliche verfügbaren Berechtigungen zu vergeben. Du kannst natürlich je nach Anwendungsfall genau die Berechtigungen vergeben, die du benötigst, indem du die einzelnen Berechtigungen aktivierst.
1. Klicke auf **Speichern**.

### Schritt 3: Projekt erstellen

Nun erstellst du ein separates Projekt für die Zusammenarbeit mit deinem Fulfillment-Dienstleister, damit abzuwickelnde Aufträge korrekt übermittelt werden. Dabei ist es wichtig, dass du in diesem Projekt das passende Kommissionierverfahren einstellst.

Gehe wie folgt vor, um das Projekt zu erstellen:

1. Öffne das Menü **Einstellungen > Grundeinstellungen > Projekte**. * Oder *: Suche mit der Smart Search nach dem Begriff **Projekte**.

1. Klicke oben rechts auf **Projekt hinzufügen**.
1. Wähle die Option **Neues Projekt anlegen ** und klicke dann auf **Weiter**.
1. Gib eine aussagekräftige **Bezeichnung** für das Projekt ein.
1. Gib eine **Kennung** für das Projekt ein.
1. Klicke auf **Weiter**.
1. Öffne das Tab **Einstellungen ** und klicke dann auf **Logistik / Versand**.
1. Wähle das gewünschte **Kommissionierverfahren** aus.
  1. Möchtest du Artikel mit MHD- und Chargenverwaltung vom Fulfillment-Dienstleister verarbeiten lassen? Dann wähle die Option **Einfache Lagerbuchung und Scannen im Versandzentrum**.
  1. Nutzt du keine MHD- und Chargenverwaltung für deine Artikel, wähle die Option **Einfache Lagerbuchung ohne weiteren Prozess**.
1. Scrolle nach unten und klicke auf **Speichern**.

### Schritt 4: Lager und Lagerplatz anlegen

Bestände, die dein Fulfillment-Dienstleister für dich verwaltet, befinden sich typischerweise nicht in deinem eigenen Lager. Daher ist es umso wichtiger, dass die Artikel, die du extern einlagern lässt, in ihrem eigenen virtuellen Lager und Lagerplatz in deinem XentralSystem gepflegt werden.

Gehe wie folgt vor, um ein Lager zu erstellen:

1. Öffne das Menü **Einstellungen > Lager & Logistik > Lager > Lagerverwaltung **. ** Oder **: Suche mit der Smart Search nach dem Begriff ** Lagerverwaltung**.

1. Klicke oben rechts auf **+ NEU**.
1. Vergib im Feld **Lager** einen eindeutigen Namen für das Fulfillment-Lager.
1. *Optional*: Ordne das Lager einem Projekt zu und gib die Adresse des Lagers ein. Diese Angaben sind für die Einrichtung des Lagers nicht zwingend erforderlich, sondern dienen genau wie der Name lediglich zu deiner Information.
1. Klicke auf **Speichern**.

Fahre nun damit fort, im eben erstellten Lager einen Lagerplatz anzulegen. Auch bei diesem Schritt sind keine detaillierten Einstellungen notwendig - du vergibst lediglich einen geeignete Bezeichnung für den Lagerplatz.

1. Klicke auf das Tab **Lagerplätze**.
1. Klicke auf **Neuen Lagerplatz anlegen**.
1. Vergib im Feld **Bezeichnung** einen eindeutigen Namen für den Lagerplatz. Weitere Angaben sind für die Einrichtung des Lagerplatzes nicht notwendig, da es sich wie beim zuvor erstellten Lager um eine Art Platzhalter landet, um Bestände zu führen.
1. Klicke auf **Speichern**.

### Schritt 5: Übertragungen-Account anlegen

In diesem Schritt geht es darum, die eigentlichen Einstellungen für die Datenübertragung vorzunehmen. Je nachdem, ob du mit einem oder mehreren Fulfillment-Dienstleistern arbeitest, verschiedene Datenformate nutzen möchtest und ob du Informationen nicht nur senden, sondern auch empfangen willst, musst du mehrere separate Accounts in Xentral einrichten. Beachte, dass die Anzahl der Übertragungen-Accounts, die du anlegen musst, von den Workflows deines Unternehmens abhängt: Wenn du beispielsweise Lieferscheine an deinen Fulfillment-Dienstleister übertragen und Tracking-Informationen empfangen möchtest, solltest du für beide Abläufe jeweils eine separate Übertragung anlegen. Zudem erhältst du so eine bessere Übersicht über die laufenden Prozesse und kannst bei Problemen schneller reagieren.

Im Folgenden erfährst du, wie du eine Übertragung in Xentral anlegst und welche Einstellungen dir im Detail zur Verfügung stehen.

> **Tipp**
>
> Die folgenden Informationen sind sehr ausführlich und daher eher als Referenzmaterial zu verstehen. Die exakten Einstellungen, die du vornehmen musst, hängen davon ab, welche Daten zwischen deinem XentralSystem und dem Fremdsystem ausgetauscht werden sollen. Schau dir unseren separaten Artikel mitAnwendungsfällen für Übertragungenan, um genau abgegrenzte Anleitungen zur Einrichtung der häufigsten Übertragungstypen zu sehen.

Gehe wie folgt vor, um eine Übertragung anzulegen:

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > Übertragungen (CSV/XML/EDI/PDF)**. * Oder *: Suche mit der Smart Search nach dem Begriff **Übertragungen**.

1. Klicke oben rechts auf **+ NEU**.
1. Nimm die gewünschten Einstellungen vor. In den folgenden Kapiteln findest du alle verfügbaren Einstellungen und die passenden Erläuterungen.
1. Klicke auf **Speichern**.

#### Einstellungen und Informationen

In diesem Bereich aktivierst du die Übertragung, nachdem du alle notwendigen Einstellungen vorgenommen hast. Außerdem vergibst du hier eine Bezeichnung und kannst in bei bereits angelegten Übertragungen allgemeine Informationen zum Status der Datenübertragung sehen.

| Einstellung | Erläuterung |
| --- | --- |
| Bereich **Einstellungen** |
| **Aktiv **| Aktiviere diese Option, um die Übertragung produktiv für den Datenaustausch zwischen deinem Xentral System und deinem Fulfillment-Dienstleister zu nutzen. ** Achtung:** Wenn diese Option deaktiviert ist, findet kein Datenaustausch statt! Aktiviere diese Option erst, wenn du alle notwendigen weiteren Einstellungen für die Übertragung final vorgenommen hast. |
| **Bezeichnung** | Vergib einen aussagekräftigen Namen für die Übertragung. Dieser Name wird dir nur innerhalb deines Xentral Systems angezeigt und dient deiner eigenen Übersicht. Er ist nicht für Kunden oder Nutzer des externen Systems sichtbar. |
| Bereich **Informationen** |
| **Letzter Status ** und **Letzte Übertragung **| Das Feld ** Letzter Status **zeigt keine Daten an und wird künftig aus Xentral entfernt. Es ist also nicht relevant für dich. Im Feld ** Letzte Übertragung** kannst du den genauen Zeitpunkt einsehen, an dem die letzte Übertragung stattgefunden hat. |

#### Kommunikation

In diesem Bereich legst du die technischen Details der Übertragung fest und gibst die erforderlichen Daten für die Verbindung mit dem gemeinsamen Server aus, der für den Datenaustausch zwischen dir und deinem Fulfillment-Dienstleister genutzt wird.

| Einstellung | Erläuterung |
| --- | --- |
| **API **| Wähle hier den API-Account aus, den du zuvor im Menü ** Einstellungen > Administration > Datenaustausch > APIs** eingerichtet hast. |
| **Übertragungsformat **| Wähle das gewünschte Übertragungsformat aus. In den meisten Fällen kommen bei der Zusammenarbeit mit einem Fulfillment-Dienstleister die Formate ** XML **oder ** CSV** zum Einsatz. Dein Fulfillment-Dienstleister wird dich über das geforderte Dateiformat informieren und dir bei Bedarf die Optionen genauer erläutern. Folgende Übertragungsformate stehen dir zur Verfügung: - PDF<br>- XML<br>- XML mit integriertem PDF (Base64-kodiert)<br>- XML und PDF in separaten Dateien<br>- CSV<br>- App4sales<br>- Brickfox (weitere Informationen unter [info@brickfox.com](mailto:info@brickfox.com))<br>- DS<br>- EDI<br>- EDI (Sport2000)<br>- [Netstock](https://help.xentral.com/hc/de/articles/360016773679#UUID-ad413078-1edd-453e-f3fe-4766f7663cac)<br>- [Opentrans](https://help.xentral.com/document/preview/13973#UUID-c2b2b6f0-47b6-af28-e735-f59eda454bb1)<br>- Pixi<br>- [Smarty](https://help.xentral.com/hc/de/articles/4402393972242-Einf%C3%BChrung-Smarty) |
| **Typ **| Wähle die gewünschte Übertragungsart aus, die für die Datenübermittlung genutzt wird. Für die Datenübermittlung zwischen Xentral und dem System des Fulfillment-Dienstleisters über einen gemeinsamen Server kommen in den meisten Fällen FTP, FTPS oder SFTP zum Einsatz. Dein Fulfillment-Dienstleister wird dich informieren, welcher Übertragungsstandard genutzt wird. Die Übertragung von Daten per API-Schnittstelle ist ebenfalls möglich. Beachte in diesem Fall jedoch, dass du zur Einrichtung solcher Übertragungen tiefergehende technische Kenntnisse benötigst. Folgende Übertragungsarten stehen dir für Übertragungen zur Verfügung: - FTPS<br>- FTP<br>- SFTP<br>- E-Mail ⚠️** Wichtig:** Bei der Einrichtung von Übertragungen vom Typ FTP und SFTP empfehlen wir die Verwendung relativer Pfade für die Angabe des Antwort-Speicherorts. |
| **Codierung (Senden)** | Wähle aus, welche Codierung für die Datenübertragung von Xentral zum Fremdsystem genutzt werden soll. Diese Information erhältst du in der Regel von deinem Fulfillment-Dienstleister. |
| **Server** | Gib den Namen oder die IP-Adresse des Servers an, an den die Übertragung aus Xentral gerichtet wird. Diese Information erhältst du in der Regel von deinem Fulfillment-Dienstleister. |
| **Port** | Trage den spezifischen Port des zuvor angegebenen Servers ein, der die Übertragung empfängt. Diese Information erhältst du von deinem Fulfillment-Dienstleister, da dieser in der Regel den Server betreibt und dementsprechend für Zugangsfragen zuständig ist. |
| **SSL** | Aktiviere diese Option, wenn die Datenübertragung per SSL verschlüsselt werden soll. Falls dieses Verfahren angewendet wird, informiert dich dein Fulfillment-Dienstleister darüber. |
| **Username** | Gib den Benutzernamen für den Zugang zum zuvor angegebenen Server an. Diese Information erhältst du in der Regel von deinem Fulfillment-Dienstleister. |
| **Passwort** | Gib das Passwort für deinen Zugang zum Server an, falls es benötigt wird. Diese Information sowie das Passwort erhältst du in der Regel von deinen Fulfillment-Dienstleister. |
| **OAuth client id** | In den meisten Fällen wird diese Information nicht zwingend benötigt, um die Verbindung zum Server herzustellen. Halte Rücksprache mit deinem Fulfillment-Dienstleister. Dieser stellt dir bei Bedarf die Information zur Verfügung. |
| **OAuth client secret** | In den meisten Fällen wird diese Information nicht zwingend benötigt, um die Verbindung zum Server herzustellen. Halte Rücksprache mit deinem Fulfillment-Dienstleister. Dieser stellt dir bei Bedarf die Information zur Verfügung. |
| **OAuth url** | In den meisten Fällen wird diese Information nicht zwingend benötigt, um die Verbindung zum Server herzustellen. Halte Rücksprache mit deinem Fulfillment-Dienstleister. Dieser stellt dir bei Bedarf die Information zur Verfügung. |
| **Speicherort (Ausgang)**| Gib hier den Dateipfad an, auf dem ausgehende Dateien (also Dateien, die von Xentral an das Fremdsystem übertragen werden) abgelegt werden sollen. In der Regel nennt dir dein Fulfillment-Dienstleister den gewünschten Dateipfad für die Ablage der Dateien. ⚠️** Wichtig:** Bei der Einrichtung von Übertragungen vom Typ FTP und SFTP empfehlen wir die Verwendung relativer Pfade für die Angabe des Speicherorts. |
| **Dateiname Prefix** | Gib hier bei Bedarf einen Präfix an, den die Namen aller ausgehenden Dateien (also Dateien, die von Xentral an das Fremdsystem übertragen werden) automatisch erhalten. Die Verwendung eines Präfixes kann dir helfen, Dateien unterschiedlicher Übertragungen anhand ihrer Dateinamen zu unterscheiden. In manchen Fällen fordern Fulfillment-Dienstleister einen spezifischen Präfix und teilen dir ihre entsprechenden Anforderungen mit. |
| **Antwort-Speicherort (Eingang)**| Gib hier den Dateipfad an, auf dem eingehende Dateien (also Dateien, die vom Fremdsystem an Xentral übertragen werden) abgelegt werden sollen. In der Regel nennt dir dein Fulfillment-Dienstleister den Dateipfad für die Abholung der Dateien. ⚠️** Wichtig:** Bei der Einrichtung von Übertragungen vom Typ FTP und SFTP empfehlen wir die Verwendung relativer Pfade für die Angabe des Antwort-Speicherorts. |
| **Antwort-Dateiname Prefix** | Wenn du hier einen Präfix einträgst, werden bei eingehenden Übertragungen, die dich von deinem Fulfillment-Dienstleister erreichen, nur Dateinamen mit genau diesem Präfix berücksichtigt. Beachte, dass in diesem Fall keine Dateien importiert werden, die nicht über diesen Präfix verfügen. Erkundige dich vorab bei deinem Fulfillment-Dienstleister, ob ein spezieller Präfix notwendig oder gewünscht ist. |
| **Löschen von Server nach Download** | Aktiviere diese Option, um empfangene Belegdateien automatisch vom Server zu löschen, nachdem du die entsprechenden Dateien aus Xentral heruntergeladen hast. Die Löschung gilt nur für Belege, die vom Fremdsystem an Xentralübermittelt werden. |

#### Belege versenden

In diesem Bereich nimmst du zum Großteil Einstellungen vor, die für **ausgehende** Übertragungen relevant sind und diese näher bestimmen. Damit sind Belege und Dateien gemeint, die von Xentral an ein Fremdsystem übermittelt werden. Die häufigsten Anwendungsbeispiele sind dabei die Übertragung von[Lieferscheinen](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0_id_Praxisbeispielefrbertragungen-Lieferscheinebertragen)und[Artikeldaten](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0_id_Praxisbeispielefrbertragungen-Artikelbertragen)zu einem Fulfillment- oder Logistikdienstleister.

Du findest hier auch vereinzelt Einstellungen, die im Rahmen eingehender Übertragungen relevant sind, wie die Einstellungen zur Tracking- und Rechnungs-E-Mail.

| Einstellung | Erläuterung |
| --- | --- |
| **Belegart **| Wähle hier die Belegart aus, die übertragen werden soll. Die Auswahl hängt davon ab, welchen Workflow du mithilfe der Übertragung abwickeln möchtest. Wähle beispielsweise die Option ** Lieferschein** aus, wenn du eine Lieferscheine an deinen Fulfillment-Dienstleister übermittteln möchtest. Beachte hierzu auch die Erläuterungen in unserem [Artikel zum Thema Anwendungsfälle](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0). |
| **Belegstatus** | Gib den Status ein, in dem Belege sich befinden müssen, damit sie übertragen werden. In den meisten Anwendungsfällen ist hier die Eingabe “FREIGEGEBEN” korrekt. Somit werden beispielsweise Lieferscheine übertragen, sobald du sie in deinem Xentral System freigegeben hast. Je nach deinem Bedarf kannst du hier aber auch einen anderen Belegstatus auswählen. Verwende stets genau die Schreibweise für den Status, wie er auch in deinem Xentral angegeben ist. Andernfalls kommt es zu Fehlern bei der Übertragung. |
| **Projekt** | Wähle das Projekt aus, dessen Belege übermittelt werden sollen. Beachte, dass du für jedes weitere Projekt eine eigene Übertragung anlegen musst. Möchtest du sämtliche Belege deines Xentral Systems unabhängig vom hinterlegten Projekt übertragen, triff in diesem Feld keine Auswahl. |
| **Adresse** | Gib die Zieladresse der Belege an, die von Xentral ausgehend übermittelt wird. Somit verarbeitet der Fulfillment-Dienstleister nur Belege, die diese spezifische Adresse (und damit Kunden) enthalten. Dies kann bei Anwendungsfällen nützlich sein, bei denen von einem einzelnen Kunden ein großes Auftragsvolumen eingeht oder dessen Aufträge aus anderen Gründen separat von anderen Übertragungen verarbeitet werden sollen. |
| **Gruppe** | Gib die Adressgruppe der Zieladresse der Belege an, die von Xentral ausgehend übermittelt wird. Somit verarbeitet der Fulfillment-Dienstleister nur Belege, deren Adresse einer bestimmten Adressgruppe zugeordnet sind. Dies kann bei Anwendungsfällen nützlich sein, bei denen von einem einzelnen Kundengruppe ein großes Auftragsvolumen eingeht oder die betreffenden Aufträge aus anderen Gründen separat von anderen Übertragungen verarbeitet werden sollen. |
| **Manuelle Freigabe erforderlich **| Wenn diese Option aktiv ist, werden die Belege nicht automatisch übertragen. Stattdessen werden die Belege im Tab ** Warte auf Freigabe** aufgelistet. Dort wählst du die zu übertragenen Belege manuell aus und gibst sie anschließend zur Übertragung frei. Wir empfehlen, diese Funktion zu Testzwecken zu nutzen, wenn du eine neue Übertragung anlegst und die Datenübertragung zunächst manuell steuern möchtest. |
| **Start ab ID ** und **Start ab Datum **| Gib optional die ID des Belegs an, sodass die Übertragung der Belege ab dieser ID startet. Wenn du eine ID angibst, musst du zusätzlich das Datum des Belegs festlegen, ab dem die Übertragung starten soll. Achtung: Es werden erst Belege übertragen, wenn beide Kriterien gleichzeitig zutreffen. Nimmst du für diese Einstellungen keine Angaben vor, startet die Übertragung ab dem Zeitpunkt, zu dem du sie auf ** Aktiv** setzt. |
| **Labels **|** Hinweis **: Diese Option erscheint erst, nachdem du die Einstellungen für die Übertragung einmalig gespeichert hast! Labels erlauben dir, die in der Übertragung enthaltenen Belege auf einen Blick in deinem Xentral System zu unterscheiden und nach speziellen Labels zu filtern. Lege zuerst mithilfe der Option Filter-Labels fest, nach welchen Labels du innerhalb der Übertragung filtern möchtest. Nutze dann die Optionen ** Tag erfolgreiche Übertragung **und ** Tag fehlerhafte Übertragung**, um ein Tag für diese Szenarien auszuwählen. Das Tag wird in diesen Fällen dann automatisch für die betroffenen Belege vergeben und in deinem Xentral System angezeigt. Klicke auf die Filter-Symbole neben den genannten Optionen, um eine Liste aller verfügbaren Labels zu sehen. Scrolle bis an das Ende der Liste, um bei Bedarf neue Labels anzulegen und direkt zu verwenden. |
| **Briefpapier im XML** | Wenn die Dateiübertragung im XML-Format stattfindet, kannst du diese Option aktivieren, um jede XML-Datei mit einem speziellen Briefkopf zu erweitern. Der Briefkopf wird dabei im Format base64 kodiert, damit die ursprüngliche XML-Struktur nicht beeinträchtigt wird. |
| **Maximal gleichzeitige Übertragungen**| Gib die Anzahl der Belege ein, die gleichzeitig übertragen werden sollen. In den meisten Fällen sind 10 gleichzeitig übertragene Belege eine gute Wahl, du kannst jedoch auch 100 oder mehr Belege gleichzeig übertragen lassen. Voraussetzung ist, dass die betreffende Übertragung aktiv ist und du den Prozessstarter namens * api_uebertragungen* aktiviert hast. Weitere Informationen zu den notwendigen Einstellungen im Modul Prozessstarter findest du [im entsprechenden Kapitel](#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt1Prozessaktivieren). |
| **Jeder Beleg in einer eigenen XML **| Wenn du das Übertragungsformat ** XML** nutzt, empfehlen wir dir, diese Option zu aktivieren, damit jeder Beleg in einer eigenen XML-Datei gespeichert und übermittelt wird. Dieses Vorgehen entspricht in der Praxis meistens dem Standard. Falls dein Fulfillment-Dienstleister abweichende Anforderungen hat, wird er dir diese entsprechend kommunizieren. |
| **XML-Zusatz** | Falls von dir oder deinem Fulfillment-Dienstleister gewünscht, können mithilfe dieser Option statische Anhänge für XML-Dateien definiert werden. Dies kann nützlich sein, wenn jede übermittelte XML-Datei eine bestimmte Kennung zur Identifikation erhalten soll. Sprich mögliche Anwendungsfälle am Besten mit dem jeweiligen Dienstleister ab. |
| **Tracking Mail** | Aktiviere diese Option, wenn automatisch eine E-Mail mit den Tracking-Informationen (Tracking-Link und Sendungsnummer) an deine Kunden versendet werden soll, sobald diese Informationen von deinem Fulfillment-Dienstleister über die Übertragung zurückgemeldet wurden. |
| **Rechnung Mail** | Aktiviere diese Option, wenn automatisch eine E-Mail mit dem Rechnungsdokument an deine Kunden versendet werden soll, sobald die Tracking-Informationen von deinem Fulfillment-Dienstleister an Xentral zurückgemeldet wurden. Wird ein Auftrag in mehreren Paketen mit separaten Sendungsnummern versendet, erfolgt der Versand der Rechnungs-E-Mail nur einmal für den gesamten Auftrag. Folgende Voraussetzungen gelten, wenn du diese Option aktivierst: In Xentral muss die entsprechende Rechnung bereits erstellt worden sein. Der Name des Kunden sowie die zugehörige E-Mail-Adresse des Kunden müssen im Rechnungsdokument vorhanden sein. Außerdem muss der Rechnungsbetrag größer als 0 sein. |
| **Rechnung anlegen** | Wenn du diese Option aktivierst, erstellt Xentral automatisch eine Rechnung, sobald dein Fulfillment-Dienstleister die Tracking-Informationen für den betreffenden Auftrag zurückmeldet. Diese Einstellung ist relevant, wenn du den Workflow zum Import von Tracking-Informationen nutzt. Weitere Informationen dazu findest du [in unserem Artikel zum Thema Anwendungsfälle](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0). |
| **Datei Anhang übertragen **| Diese Einstellung ist nur für Übertragungen in den Formaten ** XML **oder ** XML+PDF **relevant. Entscheide hier, in welcher Form Belege wie den Lieferschein oder die Rechnung an das Fremdsystem übertragen werden. Aktiviere dazu erst die Einstellung und wähle dann unter ** Anhang übertragen als **die gewünschte Option aus. Die Option ** Als eigene Datei **übermittelt die Datei als separaten PDF-Anhang zusätzlich zur XML-Datei. Die Option ** Base64-Codiert im Beleg** sorgt dafür, dass automatisch eine Codierung stattfindet und der Anhang in der XML-Struktur des Belegs selbst gesendet wird. |

#### Lagerzahlen

In diesem Bereich nimmst du Einstellungen für Anwendungsfälle vor, in denen du Bestandsdaten deines XentralSystems an ein Fremdsystem übermitteln willst. Diese Einstellungen gelten **nicht** in Szenarien, in denen dein Fulfillment- oder Logistikpartner Artikel für dich einlagert, sondern wenn du selbst als dieser Partner auftrittst und dementsprechend Bestände verwaltest.

| Einstellung | Erläuterung |
| --- | --- |
| **Lagerzahlen von Xentral zu Fremdsystem **| Aktiviere diese Einstellung, wenn du selbst für ein Fremdsystem Lagerbestände verwaltest. Das kann der Fall sein, wenn du ein externes ERP-System anbindest, Bestände für einen größeren Kunden oder das System eines Mutter- oder Tochterunternehmen verwaltest. Die folgenden Einstellungen ** Lager **, ** Lagerplatz **, **"Verkaufbare" Menge senden ** und **Übertragen um** erlauben dir, weitergehende Einstellungen für diesen Anwendungsfall vorzunehmen. |
| **Lager** | Diese Einstellung bezieht sich auf die ausgehende Übermittlung von Lagerzahlen. Dies ist zum Beispiel der Fall, wenn du ein externes ERP-System oder einen Großkunden an Xentral angebunden hast und dementsprechend Lagerbestände für diese Partner verwaltest. Wenn du hier ein Lager auswählst, werden sämtliche Bestände dieses Lagers an das angebundene System übertragen. |
| **Lagerplatz **| Im Zusammenhang mit der vorherigen Einstellung ** Lager** kannst du hier bei Bedarf gezielt einen spezifischen Lagerort auswählen, sodass ausschließlich Bestände dieses Lagerorts aus Xentral an das Fremdsystem übertragen werden. |
| **“Verkaufbare” Menge senden** | Aktiviere diese Einstellung, um die noch verkaufbare Lagermenge von Xentral an das Fremdsystem zu übermitteln. Die übergebenen Lagerdaten werden wie folgt berechnet: (Absolute Lagermenge) - (Für offene Aufträge reservierte Bestände) = Verkaufbare Menge. |
| **übertragen um** | Wähle hier die Uhrzeit aus, zu der die Übertragung an das Fremdsystem täglich ausgeführt werden soll. Nutze die weiteren gleichnamigen Felder, um zu bestimmen, dass mehrere Datenübertragungen pro Tag stattfinden sollen. Normalerweise eignen sich vor allem Uhrzeiten am späten Abend und in der Nacht. |

#### Verkaufsreport

In diesem Bereich nimmst du die notwendigen Einstellungen vor, falls du für die Übertragung Verkaufsreporte, also Berichte über verkaufte Artikel, automatisch erstellen lassen und später abrufen und auswerten möchtest.

| Einstellung | Erläuterung |
| --- | --- |
| **Verkaufsreport senden **| Wenn du diese Option aktivierst, werden später im Tab ** Verkaufsreport** der Übertragung die Berichte über die entsprechenden Verkäufe angezeigt. |
| **Zeitbereich** | Lege fest, ob der Verkaufsreport einmal täglich, wöchentlich oder monatlich erstellt werden soll. |

#### Sonstige Aktionen

In diesem Bereich nimmst du Einstellungen zur[Übertragung von Artikeldaten](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0_id_Praxisbeispielefrbertragungen-Artikelbertragen)ausXentral zum Fremdsystem vor. Falls du mithilfe von Xentral selbst als Fulfillment- oder Logistikpartner arbeitest, aktivierst du hier die Übermittlung von Tracking-Informationen (Sendungsnummern) an das Fremdsystem.

| Einstellung | Erläuterung |
| --- | --- |
| **Tracking von Xentral zu Fremdsystem **| Wenn du selbst als Fulfillment-Dienstleister arbeitest, ermöglicht diese Einstellung die Übermittlung von Tracking-Informationen an ein Fremdsystem. Die Übertragung dieser Daten ist mittels der Übertragungsformate ** XML **und ** CSV** möglich. |
| **Artikel Übertragen** | Klicke auf diesen Button, um Daten neuer und geänderter Artikel an das System deines Fulfillment-Dienstleisters zu übertragen. |
| **automatisch neue Artikel übertragen **| Aktiviere diese Option, um Artikel, die du in Xentral neu anlegst, automatisch an deinen Fulfillment-Dienstleister zu übertragen. Beachte jedoch, dass diese Einstellung nicht greift, wenn du Daten bestehender Artikel in Xentral änderst. Wenn du Artikeldaten änderst, musst du die Option ** Artikel übertragen** nutzen, um diese Änderungen zu übermitteln. |

#### Belege empfangen

In diesem Bereich nimmst du ausschließlich Einstellungen vor, die für **eingehende** Übertragungen relevant sind und diese näher bestimmen. Es geht hier also um Belege und Dateien, die von einem Fremdsystem an Xentralübermittelt werden. Die häufigsten Anwendungsbeispiele sind dabei die Rückmeldung von[Lagerbeständen](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0_id_Praxisbeispielefrbertragungen-Lagerbestndeempfangen)und[Tracking-Informationen](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0_id_Praxisbeispielefrbertragungen-Tracking-Informationenempfangen)zu Aufträgen, die vom Fulfillment- oder Logistikdienstleister erfolgreich in den Versand übergeben wurden.

| Einstellung | Erläuterung |
| --- | --- |
| **Aufträge / Angebote empfangen** | Aktiviere diese Option, um Aufträge und Angebote aus einem Fremdsystem zu empfangen. Diese Einstellung ist für spezielle Anwendungsfällen vorgesehen, beispielsweise wenn du selbst als Fulfillment-Dienstleister agierst oder Aufträge von anderen externen Plattformen abrufen möchtest. |
| **Alle Belegtypen importieren** | Aktiviere diese Option, um innerhalb der gewählten Übertragung den Import aller möglichen Belegtypen in Xentral zu erlauben, anstatt nur spezielle Belegtypen zu senden oder empfangen. |
| **Kundennummer aus Fremdsystem übernehmen** | Diese Einstellung ist nur für eingehende Übertragungen von Angeboten und Aufträgen per XML relevant. Du benötigst sie, wenn du eine Anbindung an Shop- oder sonstige Drittsysteme vornimmst. Für die Zusammenarbeit mit Logistik- und Fulfllment-Dienstleistern ist diese Einstellung nicht nutzbar. Ist diese Option aktiviert, wird beim Auftragsimport in Xentral die Kundennummer aus dem Fremdsystem übernommen. Falls die Kundennummer in Xentral noch nicht existiert, wird automatisch ein neuer Kundendatensatz mit genau dieser Nummer angelegt. Falls du diese Option nutzen möchtest, lege für diese Übertragung ein [separates Projekt](https://help.xentral.com/hc/de/articles/360016723620#UUID-47d62f4f-3eac-f7b6-5144-f2353584abd5) mit eigenen Nummernkreisen für Kundennummern an, damit es nicht zu Überschneidungen kommt. |
| **Bestellungen empfangen** | Aktiviere diese Option, um Bestellungen von deinem Fulfillment-Dienstleister in Xentral zu importieren. |
| **Verbindlichkeiten** | Aktiviere diese Option, um Verbindlichkeiten von deinem Fulfillment-Dienstleister in Xentral zu importieren. |
| **Lagerzahlen empfangen** | Diese Option muss aktiviert werden, um Bestandsinformationen von deinem Fulfillment-Dienstleister in Xentral zu importieren. Weitere Informationen findest du in unserem [Artikel zum Thema Anwendungsfälle](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0). |
| **Lagerplatz in Dateieingang ignorieren** | Falls dein Fulfilment-Dienstleister dir Lagerplätze innerhalb einer XML-Datei zurückmeldet, werden die entsprechenden Bestände in Xentral auf den Lagerplatz gebucht, den du in den [Einstellungen der Übertragung](#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt5bertragungen-Accountanlegen) festgelegt hast. Wenn du diese Einstellung aktivierst, gilt dies auch, falls in der übermittelten XML-Datei abweichende Lagerplätze angegeben sind. Ist die Einstellung deaktiviert, werden die Lagerplätze übernommen, die vom Fulfillment-Dienstleister übermittelt werden. Wir empfehlen dir, diese Einstellung stets zu aktivieren. |
| **Lager** | Falls dein Fulfillment-Dienstleister Bestände ohne spezifische Lagerplatzangabe an Xentral zurückmeldet, ist dies der Lagerplatz, auf den die betreffenden Artikel gebucht werden. So kannst du diesen Lagerplatz regelmäßig gezielt prüfen und die Artikel auf ihre finalen Lagerplätze umbuchen. |
| **Einlagerungsverhalten **| Diese Einstellung ist nur relevant, wenn deine Übertragung Artikel mit Mindesthaltbarkeits- und Chargeninformationen enthält und es sich um eine in Xentral eingehende Übertragung handelt. Die Option ** Lagerzahlen an MHD/Chargen-Buchungen anpassen** ist standardmäßig aktiviert und sollte so belassen werden. Daraus folgt, dass bei der Versandabwicklung der Scan von MHDs oder Chargen als Bestandsänderung interpretiert wird und die Bestände auf Basis dieser MHDs und Chargen an Xentral zurück übermittelt werden. Wir empfehlen, die Standardeinstellung nicht zu ändern, da es andernfalls zu doppelten Buchungen und Inkonsistenzen bei MHD- und Chargeninformationen kommen kann. |
| **Tracking empfangen** | Aktiviere diese Option, um Tracking-Links zu den Aufträgen zu empfangen, die dein Fulfillment-Dienstleister erfolgreich an deine Endkunden verschickt hat. Weitere Informationen und eine Anleitung zum Empfangen von Tracking-Informationen findest du in unserem [Artikel zum Thema Anwendungsfälle](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0). |
| **Gemeldete MHD / Chargen auslagern** | Aktiviere diese Option, um die Informationen zu Mindesthaltbarkeitsdaten und Chargen in den Lieferschein zu übernehmen, soweit diese an den Artikeln enthalten sind. Beachte jedoch, dass diese Einstellung nicht zu einer realen Bestandsausbuchung führen. Die Ausbuchung findet unabhängig von dieser Einstellung bereits bei der [Übergabe des Auftrags in den Auto-Versand](https://help.xentral.com/hc/de/articles/6113578120092#UUID-99504608-d895-41ad-5059-de028e933077) in Xentral statt. |
| **Versandart im Lieferschein anpassen** | In einigen Fällen muss dein Fulfillment-Dienstleister für die Auslieferung der Waren an deine Endkunden vom festgelegten Standard-Versanddienstleister abweichen. Aktiviere diese Option, damit gleichzeitig mit der Rückmeldung der Tracking-Informationen auch der geänderte Versanddienstleister an dein Xentral System zurück übertragen wird. |
| **Automatische Rückmeldung **| Diese Einstellung steuert die automatische Rückmeldung abgeschlossener Aufträge (also vom Fulfillment-Dienstleister versendete Aufträge) an Xentral und darüber hinaus an Drittsysteme wie Shops und Marktplatz. Beispiel: Wenn dein Fulfiller die Ware versendet, allerdings ein Auftrag zu lange in der Logistik verbleibt, kannst du mit dieser Einstellung steuern, dass der Auftrag nach X Tagen automatisch trotz fehlender Info als abgeschlossen markiert wird. Gib in diesem Fall den Wert 3 ein, um sicherzustellen, dass spätestens 3 Tage nach Übergabe alle Aufträge auch als abgeschlossen zurückgemeldet sind und kein einzelner vergessen wurde. ** Hinweis**: Es werden nur die übergebenen Daten der letzten 14 Tage berücksichtigt. Wenn du 4 Tage Verzug einstellst, werden jeweils von dort zurückliegend die älteren 14 Tage berücksichtigt. Das stellt sicher, dass keine Aufträge, die älter als 14+x Tage sind an deine angebundenen Plattformen und Shops rückgemeldet wird. |
| **Artikel empfangen Nicht gefundene Artikel **| Es kann vorkommen, dass sich eine unbekannte Artikelnummer in einem Beleg befindet, der von deinem Fulfillment-Dienstleister in dein Xentral System übertragen wird. In diesem Fall scheitert der Import der Belegdaten meist vollständig. Wenn du diese Option aktivierst, wird im Tab ** Monitor** der entsprechenden Übertragung eine Fehlermeldung angezeigt. Diese Meldung weist dich auf den unbekannten Artikel hin, sodass du den Fall manuell kontrollieren kannst. |
| **Lieferantennummer auch durchsuchen **| Diese Option ist nur relevant, wenn du Artikeldaten oder Bestandsinformationen von deinem Fulfillment-Dienstleister in Xentral empfängst. Wenn du diese Option aktivierst, wird in den Stammdaten der betroffenen Artikel die Information ** Artikelnummer bei Lieferant** geprüft und beim Import korrekt zugeordnet. |
| **Bestellung immer auf Lieferant buchen** | Wähle einen in Xentral angelegten Lieferanten aus, um jeder Bestellung, die du von deinem Fulfillment-Dienstleister empfängst, standardmäßig diesen Lieferanten zuzuweisen. |

#### Artikel anlegen

In diesem Bereich bestimmst du, was genau in Xentral geschehen soll, falls das Fremdsystem Artikeldaten zurückmeldet, die in Xentral noch nicht vorhanden sind.

| Einstellung | Erläuterung |
| --- | --- |
| **Fehlende Artikel anlegen** | Falls sich eine unbekannte Artikelnummer in einem Beleg befindet, der von deinem Fulfillment-Dienstleister in dein Xentral System übertragen wird, scheitert der Import der Belegdaten normalerweise vollständig. Wenn du diese Option aktivierst, wird der unbekannte Artikel automatisch in deinem Xentral System angelegt und es findet kein Datenverlust statt. Du kannst den unbekannten Artikel dann später in der Xentral Artikelverwaltung überprüfen. |
| **Fehlende Artikel als Lagerartikel markieren **|** Hinweis **: Diese Option erscheint nur, wenn du die Einstellung ** Fehlende Artikel anlegen** ausgewählt hast! Aktivierst du die vorliegende Einstellung, werden Artikel mit unbekannten Artikelnummern aus importierten Belegen in Xentral automatisch als Lagerartikel angelegt. |

#### Artikel empfangen

In diesem Bereich nimmst du ausschließlich Einstellungen vor, die für die **eingehende** Übertragung von Artikeldaten relevant sind. Die Einstellungen bestimmen genauer, was in Xentral passieren soll, wenn das Fremdsystem völlig neue Artikeldaten oder Änderungen an bereits in Xentral vorhandenen Artikeldaten enthält.

| Einstellung | Erläuterung |
| --- | --- |
| **Artikel empfangen (neue Artikel)** | Wenn Artikeldaten per XML von einem Fremdsystem zu Xentral übertragen werden, legt diese Option fest, dass neue Artikel, die bisher nicht in Xentral angelegt sind, beim Datenimport ebenfalls berücksichtigt und entsprechend automatisch angelegt werden. Dieses Verhalten lässt sich zusätzlich zu XML auch bei einer Übertragung mittels [Smarty](https://help.xentral.com/hc/de/articles/4402393972242#UUID-46ee1d66-3282-cf80-dd01-5634ee9c3c56) erreichen. Dazu muss zusätzlich ein bestimmtes Tag zur Artikelanlage im Smarty-Template vorhanden sein, sodass der Artikel korrekt angelegt wird. |
| **Artikel updaten** | Wenn Artikeldaten per XML von einem Fremdsystem zu Xentral übertragen werden, legt diese Option fest, dass geänderte Artikelinformationen beim Datenimport automatisch in Xentral überschrieben und damit aktualisiert werden. Dieses Verhalten lässt sich zusätzlich zu XML auch bei einer Übertragung mittels [Smarty](https://help.xentral.com/hc/de/articles/4402393972242#UUID-46ee1d66-3282-cf80-dd01-5634ee9c3c56) erreichen. Dazu muss zusätzlich ein bestimmtes Tag zur Artikelanlage und ein weiteres Tag zur Aktualisierung von Artikeln im Smarty-Template vorhanden sein, sodass der Artkel korrekt angelegt wird. |