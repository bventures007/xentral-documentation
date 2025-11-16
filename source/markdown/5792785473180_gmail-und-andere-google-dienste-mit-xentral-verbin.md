> **Wichtig**
>
> Diese Methode zur Anbindung von Gmail funktioniert, wird von uns jedoch als veraltet angesehen. Wir empfehlen dir dein Gmail-Konto in Xentral NextGen, wie im folgenden Artikel beschrieben, anzubinden:E-Mail-Konten anbinden.

Über Google APIs kannst du einige der Google-Dienste wie Gmail und Google Kalender mit Xentral verbinden. Dafür benötigst du ein gültiges Google-Konto und musst Xentral20.1 oder höher verwenden. Der Vorgang besteht aus mehreren Schritten.

## Ein neues Projekt in deinem Google-Konto anlegen

Dies ist der erste Schritt, um Google-Dienste mit Xentral zu verbinden. Projekte enthalten Einstellungen, Berechtigungen und weitere Metadaten, die zur Verbindung eines Google-Kontos mit Xentral notwendig sind.

1. Melde dich in deinem Google-Konto an und öffne die [Google Cloud Console](https://console.cloud.google.com/getting-started) im gleichen Browser.
1. Klicke zuerst auf Projekt auswählen und anschließend auf Neues Projekt.
1. Gib den Namen deines Projekts und deiner Organisation ein und klicke auf Erstellen.

### Gmail API aktivieren

Dies ist der zweite Schritt, um Google-Dienste mit Xentral zu verbinden.

1. Wähle das Projekt, welches du gerade erstellt hast, indem du in den Benachrichtigungen auf PROJEKT AUSWÄHLEN klickst oder das Projekt Dropdown-Menü nutzt.
1. Navigiere zu APIs und Dienste und klicke auf Aktivierte APIs und Dienste.
1. Klicke auf + APIS UND DIENSTE AKTIVIEREN.
1. Gib *Gmail API* in das Suchfeld ein. Alternativ kannst du auch nach unten scrollen und im Bereich Google Workspace die Gmail API auswählen.
1. Öffne die Gmail API und klicke auf AKTIVIEREN.

### Neuen Zustimmungsbildschirm anlegen

Dies ist der zweite Schritt, um Google-Dienste mit Xentral zu verbinden. Sobald du dein neues Projekt erstellt hast, musst du den OAuth-Zustimmungsbildschirm anlegen.

1. Navigiere zu APIs und Dienste und wähle OAuth-Zustimmungsbildschirm.
1. Wähle den bevorzugten Nutzertyp (intern) und klicke auf Erstellen.
1. Gib im Bildschirm Anwendungsinformation die folgenden Informationen ein:
  1. Anwendungsname - Der Name der App, die um Zustimmung bittet
  1. Nutzersupport-E-Mail - Für Nutzer, die dich wegen Fragen zu ihrer Zustimmung kontaktieren möchten
  1. Anwendungslogo - Lade ein Bild auf den Zustimmungsbildschirm, das nicht größer als 1 MB ist, damit Nutzer die Anwendung besser erkennen können
1. Gib unter Anwendungsdomain die folgenden Informationen ein:
  1. Startseite der Anwendung - Gib einen Link zu deiner Startseite an
  1. Link zur Datenschutzerklärung der Anwendung - Gib einen Link zu deiner öffentlichen Datenschutzerklärung an (optional)
  1. Link zu den Nutzungsbedingungen der Anwendung - Gib einen Link zu deinen öffentlichen Nutzungsbedingungen an (optional)
1. Gib im Bereich Autorisierte Domains die Xentral-Domain an. Klicke auf +Domain hinzufügen und gib *xentral.biz* ein.
1. Gib im Bereich Kontaktdaten des Entwicklers die E-Mail-Adresse an, die Google verwenden darf, um dich über Änderungen an deinem Projekt zu informieren.
1. Klicke auf Speichern und Fortfahren.
1. Im Bildschirm Bereiche kannst du Zugangsberechtigungen festlegen, die Nutzer autorisieren müssen, um deinem Projekt Zugriff auf spezifische private Nutzerdaten ihres Google-Kontos zu erlauben. Bereiche sind nicht verpflichtend. Klicke auf Speichern und Fortfahren, um auf den nächsten Bildschirm zu gelangen.
1. Überprüfe deine eingegebenen Daten und klicke auf Zurück zum Dashboard, falls du keine Änderungen vornehmen möchtest.

Dies vervollständigt die Einrichtung deiner Google API und du kannst nun dein Gmail-Konto mit Xentral verbinden.

## OAuth Client ID anlegen

Dies ist der dritte Schritt, um Google-Dienste mit Xentral zu verbinden. Dieser Schritt ist notwendig, um Xentralfür OAuth-Server sichtbar zu machen.

1. Logge dich in Xentral ein und navigiere zu Administration>System>Google API.
1. Kopiere den Link aus dem Feld Redirect URI.
1. Navigiere zu [Google Cloud Console](https://console.cloud.google.com/getting-started) und öffne Anmeldedaten.
1. Klicke auf Anmeldedaten erstellen und wähle OAuth-Client-ID.
1. Wähle Webanwendung in der Anwendungstyp-Auswahlliste. Gib nun den Namen der App ein, zum Beispiel *Xentral ERP*.
1. Klicke im Bereich Autorisierte Weiterleitungs-URIs auf URI hinzufügen. Füge hier den zuvor kopierten Link aus Xentral ein und klicke auf Erstellen.
1. Die Dialogbox OAuth-Client erstellt erscheint und zeigt die Informationen Ihre Client-ID und Ihr Clientschlüssel an. Kopiere diese Zeichenfolge und füge sie in die entsprechenden Felder im Modul Google API in Xentral ein (Administration > System >Google API).
  1. Kopiere die Zeichenfolge Ihre Client-ID aus der Google Cloud Console in das Feld Client ID in Xentral ein.
  1. Kopiere die Zeichenfolge Ihr Clientschlüssel aus der Google Cloud Console in das Feld Client Schlüssel in Xentral ein.
1. Klicke auf Speichern.
1. Klicke auf Ok, um die Dialogbox OAuth-Client erstellt in der Google Cloud Console zu schließen.

## Dein Gmail-Konto an Xentral anbinden

Nun da du die API-Verbindung zwischen der Google Cloud und deiner Xentral-Instanz eingerichtet hast, musst du dein E-Mail-Konto in Xentral einrichten.

1. Navigiere zu Administration > System > Benutzer und öffne das Konto des Administrators.
1. Füge die E-Mail-Adresse im Bereich Bearbeiten Administrator in das Feld E-Mail ein und klicke auf Speichern.
1. Navigiere zu Stammdaten > Adressen und öffne die Adresse des Administrators.
1. Füge die gleiche E-Mail-Adresse, die du zuvor benutzt hast, im Bereich Kontaktdaten ein und klicke auf Speichern.
1. Navigiere zu Administration > System > Email Accounts und klicke auf Neu, um einen neuen Eintrag anzulegen.
1. Trage die folgenden Informationen ein:
  1. E-Mail-Adresse - die zuvor hinzugefügte E-Mail-Adresse
  1. Benutzername - optional
  1. Passwort - Passwort deines E-Mail-Kontos
  1. IMAP-Server - Der Standard IMAP-Server ist *imap.gmail.com * 1. IMAP-Port -*993* und wähle IMAP für Google in der Auswahlliste.
1. Gib im Bereich Einstellungen Senden SMTP (Optional) die folgenden Informationen ein:
  1. SMTP-Server: *smtp.gmail.com * 1. SMTP-Port: *587*
  1. SMTP-SSL: TLS
  1. SMTP-Authentifizierung: *Google OAuth*
  1. SMTP-DEBUG aktivieren: Setze hier ein Häkchen.
1. Klicke auf Speichern.
1. Nun musst du die E-Mail-Adresse autorisieren, um E-Mails in Xentral senden und empfangen zu können. Klicke auf das Profil-Symbol in der rechten oberen Ecke des Bildschirms und klicke dann auf Profil bearbeiten.
1. Trage im Bereich Mein GoogleMail Konto deine E-Mail-Adresse ein und klicke auf Autorisieren.
1. Der Zustimmungsbildschirm, den du zuvor angelegt hast, erscheint und du musst die Bedingungen akzeptieren.
1. Klicke auf Test Email, um deine Einstellungen zu überprüfen.