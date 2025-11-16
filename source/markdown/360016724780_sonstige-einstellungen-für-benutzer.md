Jeder Benutzer in Xentral verfügt über einen eigenen Benutzeraccount. Diese Accounts werden im ModulBenutzerverwaltet. In diesem Modul legst du neue Benutzer an und bestimmst die Rechte pro Benutzer. Wie du dabei vorgehst und welche Einstellungen verfügbar sind, ist[in diesem Artikel](https://help.xentral.com/hc/de/articles/360017521360#UUID-52c33128-d310-d4ed-0de8-b78d0cc6887f)näher beschrieben.

Zusätzlich zu den Benutzerrechten kannst du weitere Einstellungen pro Benutzer vornehmen, beispielsweise zur Nutzung des Xentral-Kalenders oder zu den Standard-Druckereinstellungen.

## Sonstige Einstellungen vornehmen

Öffne zunächst per Smart Search das Modul **Benutzer **. Öffne dann den gewünschten Benutzer per Klick auf das ** Stift-Symbol **rechts und klicke dann auf ** Sonstige Einstellungen**.

Im TabSonstige Einstellungenkannst du diverse Benutzereinstellungen verfeinern. Du kannst eigene Druckereinstellungen vornehmen, die Vorrang vor den Standardeinstellungen haben, deinen Xentral-Kalender auf einem externen Gerät abonnieren und andere Einstellungen vornehmen.

![user_othersettings.png](https://help.xentral.com/hc/article_attachments/11225588179868)

- **Projekt bevorzugen**: Wähle ein bevorzugtes Projekt, welches automatisch ausgewählt wird, wenn der Benutzer Stammdaten oder Belege anlegt. Diese Einstellungen haben Vorrang vor den Standard-Projekteinstellungen.
  Du kannst diese Einstellung nutzen, um zwischen verschiedenen Bereichen deines Unternehmens zu unterscheiden, z.B. zwischen Mitarbeitern, die hauptsächlich für B2B oder B2C verantwortlich sind. Du kannst im Projekte-Modul außerdem Projekte auf bestimmte Benutzer beschränken und dies im bevorzugten Projekt widerspeigeln. Hast du z.B. zwei Zweigstellen, eine in Berlin und eine in München, dann sollten Mitarbeiter in Berlin ihr eigenes Projekt haben und es als bevorzugtes Projekt hier einstellen.

- Sprache: Wähle die Standardsprache für die Benutzeroberfläche für den Benutzer.
  Benutzer können die Sprache der Benutzeroberfläche jederzeit selbst ändern, wie im folgenden Artikel beschrieben: [Sprache der Benutzeroberfläche in Xentral NextGen ändern](https://help.xentral.com/hc/de/articles/8080124976796#UUID-78ea6a23-55e9-bc8e-bd70-c90d303c8474).

- Eigene E-Mail bevorzugen: Beim Versenden von E-Mails wird die E-Mail des Benutzers verwendet, anstelle der Firmen-E-Mail-Adresse.
  Diese Option ist für Vertriebsmitarbeiter interessant, die nach dem Versand eines Angebots persönlich verfügbar sein möchten.

- Standard Fax: Wähle das Standardfax für diesen Benutzer.
- GPS Stechuhr: Diese Funktion wird nicht mehr unterstützt.
- Im Kalender/Chat ausblenden: Blendet den Benutzer auf dem Kalender aus. Die Chat-Funktion wird nicht mehr unterstützt.
- **Rolle**: Du findest dieses Feld am Ende des Formulars. Hier kannst du die Rolle eintragen, die der Benutzer in deinem Unternehmen hat, z.B. Büro oder Logistik.

### Standarddruckereinstellungen ignorieren

Du kannst deine Druckereinstellungen an mehreren Orten in Xentral konfigurieren. Die Einstellungen, die du im ModulBenutzervornimmst, haben immer Vorrang vor anderen Einstellungen. Wählst du hier keine Option, werden die Standardeinstellungen verwendet.

Diese Einstellungen erlauben dir festzulegen, an welchen Orten Dokumente für diesen Benutzer gedruckt werden sollen.

- **Standard Drucker**: Dieser Drucker druckt Belege, für die kein anderer Drucker angegeben ist.
  Du kannst diesen Drucker verwenden, falls du z.B. Musterartikel aus deinem Büro versenden möchtest, die nicht im Lager vorhanden sind oder du eine Zweigstelle besuchst und deinen regulären Standarddrucker nicht benutzen kannst.

  Diese Einstellung hat Vorrang vor den Standarddrucker-Einstellungen in den Grundeinstellungen.

- **Standard Etikettendrucker**: Dieser Drucker druckt Artikel- und Lageretiketten. Versandlabels können nicht über den Etikettendrucker gedruckt werden.
  Diese Einstellung hat Vorrang vor den Standard-Etikettendrucker-Einstellungen in den Grundeinstellungen.

- **Drucker Stufe (Versand)**: Dieser Drucker druckt im Versand benötigte Belege wie z.B. Rechnungen.
  Diese Einstellung hat Vorrang vor den Drucker Stufe (Versand) Einstellungen unter Projekte > Projekt öffnen > Einstellungen > Logistik/ Versand.

- **Drucker Stufe (Paketmarke)**: Dieser Drucker druckt Versandlabel.
  Diese Einstellung hat Vorrang vor den Drucker Stufe (Paketmarke) Einstellungen in den Versandarten.

### Xentral-Kalender auf einem anderen Gerät abonnieren

Du kannst deinen Xentral-Kalender auf einem anderen Gerät verfügbar machen, indem du die ICS-Version des[Kalenders](https://help.xentral.com/hc/de/articles/360016728620#UUID-1afe6b8c-4b84-0821-239c-cb86d490fe42)abonnierst. Das ICS-Format wird von den meisten Kalender-Apps unterstützt. Im folgenden Beispiel abonnieren wir den Kalender mit dem Apple Kalender auf Mac.

Gehe wie folgt vor, um den Kalender zu abonnieren:

1. Aktiviere die OptionICS Kalender.
1. Gib ein beliebiges Passwort unterICS Kalender Passwort ein.
1. Klicke aufSpeichern.
1. Kopiere die URL unter dem Passwortfeld, z.B. https://beispiel123.xentral.biz/index.php?module=kalender&amp;action=ics.
1. Öffne deine Kalender-App und abonniere einen ICS-Kalender.
  Für die Kalender-App auf Mac ist dies unterAblage > Neues Kalenderabonnement möglich.

1. Füge die URL in das entsprechende Feld ein. In der Apple Kalender-App klickst du jetzt aufAbonnieren.
1. Gib deine Anmeldedaten ein. Hierfür benötigst du deinen Benutzername aus Xentral und das Passwort, welches du zuvor im FeldICS Kalender Passwort eingegeben hast.

Du hast nun den Kalender abonniert und bekommst automatische Kalender-Updates von deiner Xentral-Instanz.

### Dokumentenscanner konfigurieren

Du kannst Dokumente mit einer Scanner App, z.B. SwiftScan, auf deinem Smartphone einscannen und diese manuell oder automatisch zu Xentral übertragen. Dies ist besonders für Verbindlichkeiten hilfreich. Weitere Informationen zum Dokumentenscanner findest du in diesem Artikel:[Dokumenten Scanner](https://help.xentral.com/hc/de/articles/360016719880#UUID-f7304051-0622-abae-eb1c-b070b90ee17d).

Um ein Dokument aus der App zu übertragen, musst du WebDAV konfigurieren:

1. Aktiviere die Option Docscan/WebDAV Upload.
1. Gib ein beliebiges Passwort in das Feld Docscan/WebDAV Passwort ein.

Die restliche Konfiguration findet in deiner Scanner App statt. In diesem Beispiel benutzen wir SwiftScan:

1. Tippe auf der Startseite auf die drei Punkte oben rechts. Das Menü öffnet sich.
1. WähleEinstellungen und dannCloud Dienste.
1. Tippe aufDienst hinzufügen.
1. WähleWebDAV.
1. Gib deine WebDAV Anmeldedaten aus Xentral ein:
  - Kopiere die URL unter dem Passwortfeld, z.B. https://beispiel123.xentral.biz/docscan/upload.php/ in das Feld WebDAV Adresse (URL) ein.
  - Gib deinen Xentral Benutzernamen in das FeldNutzername ein.
  - Gib das Passwort, welches du unter Docscan/WebDAV Passwortdefiniert hast, in das Passwort Feld ein.

WebDAV wird nun in den Einstellungen der App als angebundener Cloud Dienst angezeigt.