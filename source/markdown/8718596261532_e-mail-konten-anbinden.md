Die E-Mail-Funktion in Xentral ermöglicht dir die Kommunikation mit Kunden, Lieferanten und internen Teams. Damit du alle wichtigen E-Mail-Prozesse nutzen kannst, solltest du folgende Einstellungen unbedingt vornehmen.

- **E-Mail-Konto anbinden**: Verbinde dein Geschäftskonto mit Xentral – unterstützte Anbieter sind Microsoft (Office 365, Outlook, Hotmail) und Google (Gmail). Falls du einen anderen Anbieter nutzt, kannst du ein E-Mail-Konto auch manuell per SMTP/IMAP einrichten.
- **Standard-E-Mail-Adresse definieren**: Bestimme eine Haupt-E-Mail-Adresse für den Versand von Rechnungen, Auftragsbestätigungen und anderen Dokumenten.
- **Signatur einfügen**: Erstelle eine standardisierte E-Mail-Signatur mit relevanten Unternehmensinformationen, um ein professionelles Erscheinungsbild sicherzustellen.

> **Tipp**
>
> Menüpfad: **Einstellungen **>** Grundeinstellungen **>** E-Mail**.
>
> E-Mails sind ein zentrales Kommunikationsmittel in Xentral. Standardmäßig werden automatische E-Mails, wie z. B. für den Auto-Versand, über das Standard-E-Mail-Konto versendet. Falls erforderlich, kannst du in den Projekteinstellungen für bestimmte Projekte abweichende E-Mail-Konten festlegen.

## E-Mail-Konten anbinden

Du kannst in Xentral externe E-Mail-Konten, wie z.B. Microsoft oder Google E-Mail-Konten, zur Kommunikation im Ticketsystem oder für das E-Mail-Archiv (Webmail) anbinden. Microsoft- und Google-Konten werden über OAuth autorisiert und die Verbindungsinformationen automatisch bei Autorisierung abgerufen. Möchtest du E-Mail-Konten anderer Anbieter anbinden, z.B. web.de, gmx.de und andere, so ist dies auch möglich. Hierbei musst du jedoch die Verbindungsinformationen (SMTP-/IMAP-Informationen) manuell eingeben.

**Schritte**: Neues E-Mail-Konto in Xentral anbinden:

1. Navigiere zum Menüpfad: **Einstellungen **>** Grundeinstellungen **>** E-Mail **>** E-Mail-Konten **

1. ** Neues Konto hinzufügen **: Klicke auf**+ Konto hinzufügen**. Wähle den gewünschten Anbieter: Microsoft (Office 365, Outlook, Hotmail), Google (Gmail) oder Manuelle Einrichtung (SMTP/IMAP).
1. **Zugangsdaten eingeben**: Bei Microsoft/Google: Anmeldung über OAuth und Autorisierung bestätigen. Bei manueller Einrichtung: SMTP- und IMAP-Daten manuell eingeben.
1. **Verbindung testen**: Nach erfolgreicher Einrichtung wird eine Test-E-Mail gesendet. Falls Fehler auftreten: Verbindungsdetails prüfen und ggf. Reconnect durchführen.
1. **Standard-E-Mail-Konto festlegen**: Falls gewünscht, das neue [Konto als Standard für ausgehende E-Mails festlegen](#UUID-0209e297-82f9-2aa0-91f0-4a7b87bdd5b4_section-idm4579352578972833750443978245).

![e-mail_anbinden_neu_001.png](https://help.xentral.com/hc/article_attachments/18578224171420)

### Microsoft-Konto (Office 365, Outlook, Hotmail) anbinden

> **Anmerkung**
>
> **Hinweis**
>
> Klicke auf das Bild unten um eine interaktive Klick-Tour zu starten.

> **Anmerkung**
>
> Freigegebene Postfächer können auf diese Weise nicht an Xentral angebunden werden. Es ist ein Benutzername und ein eigenes Passwort notwendig!

Ein neues Microsoft E-Mail-Konto fügst du folgendermaßen hinzu:

1. Klicke auf + Konto hinzufügen. Es wird ein Dropdown-Menü angezeigt.
1. Wähle die Option Office 365 und gib deine Microsoft E-Mail-Adresse (Office 365, Outlook oder Hotmail) in das nun angezeigte Fenster ein. Klicke auf Verbinden. Du wirst zum Anmeldeformular des Microsoft E-Mail-Kontos weitergeleitet.
1. Gib die Anmeldedaten deines E-Mail-Kontos ein. Sobald du deine E-Mail-Adresse und dein Passwort eingegeben und bestätigt hast, wirst du wieder zur XentralE-Mail-Konten-Ansicht geleitet.

Dein neu hinzugefügtes E-Mail-Konto wird in der Übersicht angezeigt. Die technischen Verbindungseinstellungen für SMTP und IMAP werden automatisch mit den Standardeinstellungen deines E-Mail-Kontos gefüllt.

Gleichzeitig wird eine Testmail durch das System versendet. Konnte diese erfolgreich versendet werden, erscheint rechts unten eine grüne Erfolgsmeldung. Wird eine Fehlermeldung angezeigt, kontrolliere, ob du die Verbindungsdetails korrekt eingegeben hast.

Tritt ein Verbindungsfehler auf, klicke im BereichVerbindungsdetailsaufReconnectund melde dich in deinem Microsoft-Konto an, falls du nicht bereits angemeldet bist. Dein Konto sollte nun wieder verbunden sein.

> **Anmerkung**
>
> Die Erfolgs- oder Fehlermeldung zur Testmail wird unter Umständen einige Sekunden nach der Erfolgsmeldung bei Hinzufügen des E-Mail-Kontos angezeigt. Bitte warte einige Sekunden.

> **Wichtig**
>
> - Möchtest du weitere Microsoft Office-E-Mail-Konten hinzufügen, stelle sicher, dass du dich aus allen Microsoft-Konten in deinem Browser abgemeldet hast, bevor du fortfährst. Alternativ kannst du auch den Cache löschen. Tust du das nicht, wird das Konto, das du neu hinzufügen möchtest, mit den Informationen des letzten Kontos fehlerhaft in Xentral angelegt.
> - Bitte beachte, dass es sich bei dem E-Mail Konto um ein eigenständiges Konto handeln muss. Gruppen-E-Mails, Alias und nur freigegebene E-Mail Konten (delegierte Postfächer) können nicht angebunden werden.

### Gmail-Konto anbinden

Ein neues Gmail-Konto fügst du folgendermaßen hinzu:

1. Klicke auf + Konto hinzufügen. Es wird ein Dropdown-Menü angezeigt.
1. Wähle die Option Google und gib deine E-Mail-Adresse in das nun angezeigte Fenster ein. Klicke auf Verbinden. Du wirst zum Anmeldeformular des Gmail-Kontos weitergeleitet.
1. Gib die Anmeldedaten deines E-Mail-Kontos ein. Sobald du deine E-Mail-Adresse und dein Passwort eingegeben und bestätigt hast, wirst du wieder zur XentralE-Mail-Konten-Ansicht geleitet.

Dein neu hinzugefügtes E-Mail-Konto wird in der Übersicht angezeigt. Die technischen Verbindungseinstellungen für SMTP und IMAP werden automatisch mit den Standardeinstellungen deines E-Mail-Kontos gefüllt.

Gleichzeitig wird eine Testmail durch das System versendet. Konnte diese erfolgreich versendet werden, erscheint rechts unten eine grüne Erfolgsmeldung. Wird eine Fehlermeldung angezeigt, kontrolliere, ob du die Verbindungsdetails korrekt eingegeben hast.

> **Anmerkung**
>
> Die Erfolgs- oder Fehlermeldung zur Testmail wird unter Umständen einige Sekunden nach der Erfolgsmeldung bei Hinzufügen des E-Mail-Kontos angezeigt. Bitte warte einige Sekunden.

> **Wichtig**
>
> - Möchtest du weitere Gmail-Konten hinzufügen, stelle sicher, dass du dich aus allen Google-Konten in deinem Browser abgemeldet hast, bevor du fortfährst. Alternativ kannst du auch den Cache löschen. Tust du das nicht, wird das Konto, das du neu hinzufügen möchtest, mit den Informationen des letzten Kontos fehlerhaft in Xentral angelegt.
> - Bitte beachte, dass es sich bei dem E-Mail Konto um ein eigenständiges Konto handeln muss. Gruppen-E-Mails, Alias und nur freigegebene E-Mail Konten (delegierte Postfächer) können nicht angebunden werden.

### E-Mail-Konten manuell anbinden (SMTP/IMAP)

Um andere E-Mail-Konten hinzuzufügen, gehe wie folgt vor:

1. Klicke auf +Konto hinzufügen. Es wird ein Dropdown-Menü angezeigt.
1. Wähle die Option Manuell einrichten. Das FormularE-Mail-Konto hinzufügenwird angezeigt. Die Felder dieses Formulars sind Pflichtfelder.
1. Gib die E-Mail-Kontodaten in die Felder Name, E-Mail-Adresse, Benutzer und Passwort ein.
1. Gib die Verbindungsinformationen für den E-Mail-Eingang (IMAP) und den E-Mail-Ausgang (SMTP) in die Felder IMAP-Server, IMAP-Port, IMAP-Verschlüsselung, SMTP-Server, SMTP-Port und SMTP-Verschlüsselung ein. Diese Informationen findest du normalerweise in den Einstellungen deines E-Mail-Kontos.
1. Klicke auf Verbinden.

Dein neu hinzugefügtes E-Mail-Konto wird in der Übersicht angezeigt. Bei erfolgreicher Anlage wird eine grüne Erfolgsmeldung rechts unten angezeigt.

Gleichzeitig wird eine Testmail durch das System versendet. Konnte diese erfolgreich versendet werden, erscheint rechts unten eine grüne Erfolgsmeldung. Wird eine Fehlermeldung angezeigt, kontrolliere, ob du die Verbindungsdetails korrekt eingegeben hast.

> **Anmerkung**
>
> Die Erfolgs- oder Fehlermeldung zur Testmail wird unter Umständen einige Sekunden nach der Erfolgsmeldung bei Hinzufügen des E-Mail-Kontos angezeigt. Bitte warte einige Sekunden.

### Standard-E-Mail-Konto definieren

In der Regel erfolgt die automatische Kommunikation, z.B. für den Auto-Versand, über das Standard-E-Mail-Konto. Bei Bedarf kannst du aber auch abweichende E-Mail-Konten unterAdministrationsmenü > Projekte > Reiter Einstellungen > Unterreiter Logistik/ Versandim BereichE-Mail Versand Einstellungenfestlegen.

> **Wichtig**
>
> Bevor du ein Standardkonto definieren kannst, musst du ein E-Mail-Konto (Microsoft, Gmail oder SMTP/IMAP), wie in den obigen Abschnitten beschrieben, anbinden.

Zum Anlegen des Standard-E-Mail-Kontos gehst du wie folgt vor:

1. Navigiere zu **Einstellungen **>** Grundeinstellungen **>** E-Mail **>** Standard E-Mail Einstellungen**.
1. Gib im Bereich Standard Einstellung E-Mail (bei Versand von E-Mails) die folgenden Informationen ein:
  - E-Mail-Adresse - E-Mail-Adresse, die Empfänger sehen. Diese Adresse muss mit einem der E-Mail-Konten (Microsoft, Gmail oder SMTP/IMAP) identisch sein, die du zuvor angebunden hast.
  - Name des Absenders - Name, den die Empfänger sehen (z.B. der Namen deines Unternehmens).
  - Standardsignatur - Hier kannst du deine Standard-Signatur definieren. Im Feld Standardsignatur kannst du die folgenden Variablen verwenden: {MITARBEITER}, {MITARBEITER_TELEFON}, {MITARBEITER_MOBIL}, {MITARBEITER_EMAIL} und {MITARBEITER_TELEFAX}.
  Wie du ein Bild zu deiner Signatur hinzufügst, kannst du im Artikel [E-Mail-Konten anbinden](https://help.xentral.com/document/preview/8126#UUID-8b0a668e-1a4e-ddae-70f0-e83532c07364) nachlesen.

1. Definiere im Feld Standard Grußformel deine Grußformel, die am Ende der E-Mail eingefügt wird. Du kannst hier die folgenden Variablen verwenden: {MITARBEITER},{MITARBEITER_TELEFON},{MITARBEITER_MOBIL}, {MITARBEITER_EMAIL} und {MITARBEITER_TELEFAX}.
1. Du kannst E-Mail-Adressen hinzufügen, die eine Kopie per E-Mail erhalten sollen. Dazu verwendest du die folgenden Felder:
  - Kopie-Empfänger 1 und Kopie-Empfänger 2 für E-Mail-Adressen, die eine Kopie der E-Mail erhalten sollen.
  - BCC für eine E-Mail-Adresse, die eine Blindkopie der E-Mail erhalten soll.
1. Optional: Du kannst eine HTML-Vorlage erstellen und diese beim Versenden von E-Mails anwenden. Kopiere dazu deinen gültigen HTML-Code in das Feld HTML Template.
1. Klicke auf Speichern.

![e-mail_standard_einstellungen_001.png](https://help.xentral.com/hc/article_attachments/18578240866332)

## Einstellungen deines E-Mail-Kontos bearbeiten

In den E-Mail-Kontoeinstellungen kannst du die Konto- und Verbindungsinformationen ändern, die E-Mail-Adresse für bestimmte Module aktivieren, automatische Antworten definieren oder eine Signatur hinzufügen.

Um bestimmte Informationen zu bearbeiten, klicke auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/8718629107868)

auf der rechten Seite des entsprechenden Bereichs. Zum Speichern deiner Änderungen klicke aufSpeichernauf der rechten Seite des Bereichs im Bearbeitungsmodus.

### Konto- und Verbindungsdaten ändern

Wenn du ein Microsoft oder Google E-Mail-Konto hinzufügst, erstellt Xentral automatisch einen Kontonamen während der Anlage. Als Basis wird der Text vor dem @-Zeichen verwendet. Fügst du eine E-Mail-Adresse manuell hinzu, musst du den Kontonamen eingeben. Es kann sein, dass du diesen jedoch nachträglich für eine bessere Identifizierung noch anpassen möchtest.

Du kannst die folgenden Informationen im BereichKontodetailsbearbeiten:

1. Gib den Namen, den du für das E-Mail-Konto verwenden möchtest, in das Feld Angezeigter Name ein.
1. Bei Bedarf kannst du über das Dropdown-Menü Sichtbar nur für einschränken, wer dieses E-Mail-Konto sehen kann. Lässt du dieses Feld leer, können alle Benutzer mit Zugriff auf das Ticketmodul und das E-Mail-Archiv die E-Mails dieses Kontos lesen und E-Mails von diesem Konto aus versenden.

Du kannst die Verbindungsdetails deines E-Mail-Kontos anpassen, wenn sich z.B. Zugriffspunkte geändert haben oder du dein Passwort geändert hast.

Um die Verbindungseinstellungen deines E-Mail-Kontos zu ändern, suche im BereichVerbindungsdetailsnach dem entsprechenden Feld und ändere den Inhalt nach Bedarf.

### E-Mail-Konto für das Ticketsystem oder E-Mail-Archiv aktivieren

Du kannst deine E-Mail-Adresse für die Kommunikation im[Ticketsystem](https://help.xentral.com/hc/de/articles/360016721620#UUID-b352e666-1c92-a00d-1c1f-af4f150272b7)oder zum Speichern deiner E-Mails im E-Mail-Archiv für zukünftige Referenzzwecke freigeben.

Dein E-Mail-Konto aktivierst du folgendermaßen für das Ticketsystem:

1. Aktiviere den Schalter Für Ticket-Modul aktivieren, damit das E-Mail-Konto im Ticketsystem verwendet werden kann.
1. Das Feld Standard-Projekt enthält im Normalfalls das von dir definierte Standardprojekt. Möchtest du dieses ändern, wähle das gewünschte Projekt aus dem Dropdown-Menü.
1. Möchtest du das E-Mail-Konto einer bestimmten Warteschlange im Ticketsystem zuweisen, wähle die gewünschte Warteschlange im Standard-Warteschlange-Dropdown-Menü. [Hier](https://help.xentral.com/hc/de/articles/360016721620#UUID-b352e666-1c92-a00d-1c1f-af4f150272b7_section-idm4542691880084833175048366148) ist beschrieben, wie du Warteschlangen anlegst.
1. Klicke auf das Feld Ab Datum. Es wird ein Kalender angezeigt. Wähle im Kalender das Startdatum für den Import von E-Mails dieses E-Mail-Kontos aus. Du kannst auch ein vergangenes Datum wählen, wenn du ältere E-Mails importieren möchtest.
1. Aktiviere den Schalter E-Mails nach dem Import löschen, um E-Mails nach dem Import in Xentral bei deinem Anbieter zu löschen.
1. Aktiviere den Schalter Automatisch schließen, wenn alle importierten E-Mails/Tickets automatisch auf geschlossen gesetzt werden sollen. Beispiel: Du hast die E-Mails/Tickets bereits in einem anderen System verarbeitet, möchtest sie aber trotzdem zu Analysezwecken in Xentral importieren.

Das E-Mail-Archiv aktivierst du folgendermaßen:

1. Aktiviere den Schalter Webmail, wenn E-Mails dieses E-Mail-Kontos im E-Mail-Archiv gesichert werden sollen.
1. Gib in das Feld E-Mails löschen die Anzahl der Tage ein, für die E-Mail archiviert werden sollen, bevor sie endgültig gelöscht werden. Möchtest du deine E-Mails unbegrenzt im E-Mail-Archiv aufbewahren, gib hier *0* ein.

### Automatische Antwort einrichten

Du kannst eine automatische Antwort hinzufügen, die versendet wird, wenn eine neue E-Mail eingeht.

Führe die folgenden Schritte aus, um eine automatische Antwort einzurichten:

1. Aktiviere den Schalter Automatische Antwort aktivieren, um automatische Antworten von diesem E-Mail-Konto aus zu senden.
1. Gehen im System an einem Tag mehrere E-Mails vom selben Versender ein und die automatische Antwort soll nur einmal täglich pro Versender versendet werden, aktiviere den Schalter Nur eine E-Mail pro Tag.
1. Gib den Betreff deiner automatischen Antwort in das Feld Betreff ein.
1. Bearbeite den Text deiner automatischen Antwort im Texteditor. Die kannst die Formatierungsoptionen des Texteditors verwenden, um deinen Text zu formatieren

### Signatur in E-Mails einfügen

Du kannst eine Signatur definieren, die am Ende deines E-Mail-Textes eingefügt wird, wenn du E-Mails versendest.

1. Wenn du eine Signatur verwenden möchtest, aktiviere den Schalter Signatur aktivieren.
1. Gib die gewünschte Signatur in den Texteditor ein. Die kannst die Formatierungsoptionen des Texteditors verwenden, um deinen Text zu formatieren. Bei Bedarf kannst du auch HTML-Code hinzufügen.

## E-Mail-Konto einem bestimmten Projekt/ Vertriebskanal zuweisen

Du kannst dein E-Mail-Konto einem bestimmten Projekt/ Verkaufskanal zuweisen, z.B. Amazon, POS, Shopify, etc.

Gehe dazu wie folgt vor:

1. Öffne das Formular Logistik-Einstellungen pro Vertriebskanal auf eine der folgenden Weisen:
  - Klicke in der E-Mail-Konten-Übersicht auf für das entsprechende Projekt. Scrolle herunter bis zum Bereich Projektverknüpfungen und klicke auf den Link Logistikeinstellungen pro Vertriebskanal im Fließtext.
  - Navigiere zu Einstellungen > Lager > Logistik-Einstellungen pro Vertriebskanal
1. Öffne den Vertriebskanal, dem du dein E-Mail-Konto hinzufügen willst, indem du für den jeweiligen Kanal auf klickst.
1. Scrolle bis zum Bereich E-Mail Versand Einstellungen (falls abweichend von Daten aus Firmeneinstellungen) runter und gibt die E-Mail-Adresse deines E-Mail-Kontos in das Feld E-Mail ein.
1. Scrolle ganz nach unten und klicke auf Speichern.

Das E-Mail-Konto ist nun dem Vertriebskanal zugewiesen. Du siehst du Vertriebskanäle, die einem E-Mail-Konto zugewiesen sind, in derE-Mail-Konten-Übersicht unter der E-Mail-Adresse/dem Kontonamen und in den Kontoinformationen unterProjektverknüpfungen.

## E-Mail-Konto löschen

Wenn du ein E-Mail-Konto nicht mehr verwendest, kannst du es in Xentrallöschen, so dass es nicht mehr im Ticketsystem oder im E-Mail-Archiv verwendet werden kann.

Gehe wie folgt vor, um das E-Mail-Konto zu löschen:

1. Öffne das Konto, das du löschen möchtest, mit einem Klick auf des entsprechenden Kontos in der E-Mail-Konten-Übersicht.
1. Scrolle im Formular ganz nach unten.
1. Klicke auf Konto löschen.
1. Um die Löschung des E-Mail-Kontos zu bestätigen, gib die E-Mail-Adresse deines Kontos ein.
1. Klicke auf Konto löschen.

Das E-Mail-Konto ist gelöscht und wird nicht mehr in derE-Mail-Konten-Übersicht angezeigt.

## FAQ

### Probleme beim E-Mail-Versand beheben

Xentral protokolliert all deine ausgehenden E-Mails. Falls eine E-Mail den Empfänger nicht erreicht hat, zeigt das Protokoll eine Fehlermeldung für diese E-Mail an. Dies kann dir dabei helfen, Probleme beim E-Mail-Versand zu beheben.

Gehe wie folgt vor, um die Fehlerbehebung zu starten:

1. Navigiere zu
  Du siehst eine Tabelle mit einer Übersicht all deiner ausgehenden E-Mails.

  - Team > Email Log
1. Betrachte die Spalte Statusmeldung auf der rechten Seite. Falls die E-Mail nicht versendet werden konnte, wird hier eine Fehlermeldung angezeigt.
1. In der folgenden Tabelle findest du mögliche Ursachen der Fehlermeldung und empfohlene Lösungsschritte.

| Fehlermeldung | Mögliche Ursachen und empfohlene Lösungsschritte |
| --- | --- |
| You must provide at least one recipient‘s email address | Es wurde kein Empfänger angegeben. Trage einen Empfänger ein und versende die E-Mail erneut. |
| Mailer is not supported | Der E-Mail-Anbieter wird nicht unterstützt. Versuche es mit einem anderen Anbieter erneut. |
| Could not instantiate mail function | Mehrere Probleme können diesen Fehler erzeugen: - Der Anhang ist größer als vom E-Mail-Anbieter unterstützt<br>- Die Authentifizierungsmethode, die E-Mail-Adresse des Senders oder andere SMTP-Einstellungen könnten falsch sein. Vergleiche die SMTP-Einstellungen deines E-Mail-Kontos in Xentral mit den Vorgaben deines E-Mail-Anbieters. |
| SMTP error: Could not authenticate | Der SMTP-Benutzername oder das Passwort sind falsch oder das Authentifizierungsverfahren wird nicht unterstützt. |
| The following From address failed | Der E-Mail-Anbieter erkennt die E-Mail-Adresse nicht, von der die E-Mail gesendet werden soll. Prüfe, ob die E-Mail-Adresse vom E-Mail-Anbieter gehostet wird. |
| SMTP Error: the following recipients failed | Die E-Mail-Adresse des Empfängers ist unbekannt oder existiert nicht. In seltenen Fällen kann der Fehler auch durch Beschränkungen des E-Mail-Anbieters hervorgerufen werden. |
| SMTP error: Data not accepted | Der E-Mail-Anbieter akzeptiert keine E-Mails von dieser Adresse oder diesem Nutzer. Mögliche Gründe dafür sind: - Der E-Mail-Anbieter erlaubt keine Absenderadresse, die sich vom Nutzernamen unterscheidet.<br>- Der SMTP-Nutzer ist nicht berechtigt, E-Mails von dieser Adresse zu versenden.<br>- Die Adresse ist kein verifizierter Absender beim E-Mail-Anbieter.<br>- Der Speicher des Empfängers beim E-Mail-Anbieter ist voll.<br>- Das Versandlimit für E-Mails ist beim Anbieter überschritten. |
| SMTP error: Could not connect to SMTP host | Der SMTP-Hostname ist möglicherweise falsch geschrieben oder existiert nicht. Eine andere Möglichkeit ist, dass die falsche SSL-Methode verwendet wird. |
| Could not access file | Eine Datei, die als Anhang gesendet werden sollte, existiert nicht auf dem Server. |
| File Error: Could not open file | Auf eine Datei, die als Anhang gesendet werden sollte, kann nicht zugegriffen werden. In diesem Fall existiert die Datei entweder nicht oder du hast nicht die erforderlichen Zugriffsrechte für die Datei. |
| Unknown encoding | Die Kodierung zum Versenden der E-Mail wird nicht unterstützt. |
| Signing error | Möglicherweise gibt es ein Problem mit der offenen SSL-Verschlüsselung auf dem Server. |

### Woher stammen Standardtexte in automatisch versendeten E-Mails in Xentral? Beim Versand von Belegen (z. B. AB, RE, LS) tauchen in den E-Mails immer wieder Standardtexte oder Grußformeln auf, die ich nicht zuordnen kann. Wo kommen diese Texte her und wie kann ich sie anpassen oder entfernen?

Standardtexte und Grußformeln in Xentral können aus mehreren Stellen stammen. Prüfen solltest du insbesondere:

- **Standard-E-Mail-Einstellungen**: Hier wird ein globaler Standardtext für alle E-Mails hinterlegt.
- **E-Mail-Konten**: Jedes Konto kann eine eigene Signatur oder Grußformel mitbringen.
- **E-Mail-Texte (Geschäftsbriefvorlagen)**: Diese definieren Textbausteine für bestimmte Dokumenttypen (z. B. Auftrag, Rechnung, Lieferschein).
- **Projekt-Einstellungen **: Projekte können eigene E-Mail-Texte enthalten, die dann für alle Belege dieses Projekts verwendet werden. ** Vorgehen**: Zuerst die Standard-E-Mail-Einstellungen checken. Danach das E-Mail-Konto kontrollieren. Falls dort nichts hinterlegt ist, die E-Mail-Texte für den betroffenen Belegtyp prüfen. Zum Schluss die Projekt-Einstellungen prüfen.

Xentral liefert im Standard z.B: die Signatur und Standard Grußformel 'Für Rückfragen stehe ich Ihnen gerne zur Verfügung. Mit freundlichen Grüßen{MITARBEITER}' aus.