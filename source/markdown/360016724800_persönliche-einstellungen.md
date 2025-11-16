*Mein Bereich – Einstellungen*

## Favoriten

Über die Favoriten-App können verschiedene Modulaufrufe als Schnellansicht hinterlegt werden.

### Favoriten hinzufügen

Favoriten können über dasStern-Icon im jeweiligen Modul hinzugefügt werden. Mit dem aufkommenden Fenster kann festgelegt werden, mit welchem Namen der Link angezeigt werden soll und ob der Aufruf in einem neuen Tab erfolgen soll.

### Favoriten bearbeiten

Favoriten können über dasZahnrad-Symbol auf derStartseitebearbeitet werden. Dort können ebenfalls Favoriten hinzugefügt werden. Darüber hinaus kann der Pfad auch durch weitere “actions” angepasst werden. Die Ansicht zu den Favoriten erfolgt über dieStartseite.

Ebenfalls kann die Einstellung hier geändert werden, ob der Modulaufruf über ein eigenes Modul ausgeführt wird.

## Features

In diesem Bereich kannst du dir deine xentral-Oberfläche anpassen, deine Zugangsdaten bearbeiten oder unsere Apps und persönliche Kalender an xentral anbinden.

### Passwort

Ändern das Passwort deines Benutzers, indem du ein neues Passwort in das FeldPasswortund im FeldPasswort wiederholeneingibst. Das Passwort muss mindestens aus 8 Zeichen bestehen. DerAnzeigebalkenneben dem Passwortfeld bewertet die Komplexität und somit die Sicherheit des von ihnen gewählte Passworts. Die SchaltflächePasswort ändernwird aktiviert, wenn beide Passwörter übereinstimmen. Betätigen der SchaltflächePasswort ändernändert das Passwort.

### Profilbild

Lege ein neues Profilbild für deinen Benutzer fest, indem du die SchaltflächeDatei auswählenbetätigst. Ein Dialog zur Auswahl eines Bildes auf deinem Computer öffnet sich. Wähle das gewünschte Bild aus und bestätige den Dialog zur Dateiauswahl. Mit der SchaltflächeNeues Profilbild hochladenlegst du das Bild als dein neues Profilbild fest.

## Einstellungen

Im Bereich Einstellungen kannst du verschiedene Einstellungen zur Personalisierung deines Benutzerkontos vornehmen. Geänderte Einstellungen werden erst durch Betätigung der SchaltflächeEinstellungen speichernaktiviert.

### Startseite

Mit dieser Einstellung kannst du die Seite festlegen, welche direkt nach der Anmeldung in xentral angezeigt werden soll. Möchtest du zum Beispiel die Pinnwand direkt nach der Anmeldung angezeigt bekommen, so trage: "index.php?module=welcome&action=pinwand" in das Feld ein.

### Sprache

Wähle die Sprache aus der xentral Oberfläche aus. Hierbei hast du im Standard die Wahl zwischen Deutsch und Englisch. Sollte sich die Änderung der Sprache nicht sofort in der Oberfläche widerspiegelt, lade die Seite im Webbrowser neu. Weitere Sprachen lassen sich mit dem ModulOberflächen-Übersetzungaus unserem App Center einrichten und nach Bedarf selbst anpassen.

### Eigene Kalenderfarbe

Wähle die Farbe, in der deine Kalendereinträge standardmäßig eingefärbt werden. Betätige hierzu die Kachel neben dem Text. Es öffnet sich ein Dialogfeld zur Auswahl der gewünschten Farbe.

### Chat

Aktiviere diese Option wenn das Chatfenster, anstatt im derzeitigen Browser-Tab, in einem neuen Browser-Tab geöffnet werden soll.

### Telefon

Ein über Placetel integriertes Telefon zeigt Telefon-Benachrichtigungen direkt in xentral an. Solltest du dies für deinen Benutzer nicht wünschen, dann deaktiviere diese Option.

### Mobile Apps

Um mit der xentral Mobile App auf deine Unternehmensdaten zugreifen zu können, musst du den API Zugang aktivieren. Dieser ist aus Sicherheitsgründen standardmäßig deaktiviert. Betätige hierzu die SchaltflächeZugang aktivieren. Du bekommst im Anschluss einen QR-Code angezeigt, mit dessen Hilfe du die xentral Mobile App bequem verbinden kannst. Solltest du den Zugriff durch die xentral Mobile App wieder deaktivieren wollen, betätige hierzu die SchaltflächeZugang deaktivieren.

## Mein Google Kalender

xentral kann Termine zwischen dem internen Kalender und einem Google Kalender synchronisieren. Bevor ein Google Kalender angebunden werden kann, muss zunächst ein aktiver API Zugang zu Google angelegt werden. Die Einrichtung ist unter[Einrichtung Google API](#)beschrieben.

### Google Konto / G-Mail Adresse

Benutzernamen des Google Kontos (typischerweise handelt es sich dabei um eine Google E-Mail Adresse / GMail-Adresse).

### API Account

Konfigurierter API Zugang für xentral in Google. Stehen mehr als eine Option zur Auswahl oder existiert keine Auswahl, sollten die eingerichteten Google API Verbindungen überprüft werden.

### Aktiv

Hier kann die gesamte Synchronisierung der Kalender des Google Kontos vorübergehend deaktiviert werden. Wenn der Haken nicht gesetzt ist, wird lediglich die xentral-seitige Synchronisierungsfunktion abgeschalten. Wurde zuvor bereits die Autorisierung durchgeführt, bleibt diese bestehen. Die Synchronisierung der Kalender kann in diesem Fall sofort fortgesetzt werden wenn der Haken wieder gesetzt wird.

### Autorisierung der Google Kalender API

Damit xentral die Google Termine abrufen kann, muss der Zugriff auf das Google Konto für xentral autorisiert werden:

1. Google E-Mail Adresse eintragen
1. Google API auswählen
1. Speichern
1. Klick auf Autorisieren
1. Es wird zum Google Zustimmungsbildschirm weitergeleitet. Falls noch kein Login bei Google im aktuellen Browser stattgefunden hat, bitte nun mit einem Google Account einloggen.
1. Anschließend bitte bestätigen, dass xentral auf den Google Kalender zugreifen darf.
1. Nun wirst du nach xentral zurückgeleitet. Es erscheint eine Meldung, die aussagt, ob die Autorisierung erfolgreich war oder nicht.
1. Durch Klick auf Termine importieren importierst du erstmalig alle Google Termine der letzten Woche und der nächsten 3 Wochen. Dieser Schritt muss nach der Autorisierung mindestens einmal durchgeführt werden.

### Trennen

Durch Klicken aufTrennenwird xentral die Autorisierung zum Zugriff auf das Google Konto entzogen. Eine Synchronisierung kann dann solange nicht mehr stattfinden, bis die Autorisierung wieder erteilt wird.  Ab der Version 21.1 entfällt der Button "Trennen". Um ab dieser Version den Zugriff zu entziehen, klicke bitte einfach noch einmal auf Autorisieren. Hierdurch wird die Verbindung getrennt.

### Termine Importieren

- Kleiner Import: Jedesmal wenn der xentral Kalender neu geladen wird, werden die geänderten, hinzugefügten und gelöschte Termine seit der letzten Synchronisation importiert.
- Großer Import: Ein Prozessstarter führt regelmäßig einen großen import durch, bei dem alle Termine der letzten Woche und der nächsten 3 Wochen importiert werden. Wie häufig dieser Import durchgeführt wird, hängt von den Einstellungen des Prozessstarters ab (Standardeinstellung: jede Nacht um 00:00 Uhr).
- Durch Klicken aufTermine Importierenkann ein großer Import manuell gestartet werden.

### Hinweise zum Import- und Exportverhalten

-... wenn dieser Benutzer selbst die Google Kalender Synchronisierung nutzt
-... oder wenn die Google E-Mail Adresse in der Adresse des Benutzers hinterlegt ist
-... oder wenn die Google E-Mail Adresse in der Adresse des Benutzers unter "Weitere Kontaktinfos" als "Google E-Mail", "Google Account", oder "Google Kalender" hinterlegt ist.

-... wenn die E-Mail Adresse aus dem Termin in Adressen gefunden wird
-... oder wenn die E-Mail Adresse aus dem Termin unter "Weitere Kontaktinfos" als "Google E-Mail", "Google Account", oder "Google Kalender" gefunden wird
-... oder wenn die E-Mail Adresse aus dem Termin in den Ansprechpartnern einer Adresse (z.B. einer Firma) gefunden wird.

- Folgende Informationen eines Google Termins werden importiert: Titel, Organisator, Teilnehmer, Zeitpunk, Ort, Farbe, Sichtbarkeit, Beschreibung
- xentral versucht alle Teilnehmer beim Import auf User (= Mitarbeiter) oder Adressen zuzuordnen.
- Ein Benutzer / Mitarbeiter kann nur dann verknüpft werden...
- Ein Externer Kontakt (=Kunde o.Ä.) kann nur dann verknüpft werden...
- Wenn in xentral ein Termin angelegt wird, wird dieser direkt nach dem Speichern nach Google synchronisiert und Google verschickt Termineinladungen an alle Teilnehmer.
- Terminserien aus Google werden beim Import in einzelne voneinander unabhängige Termine aufgeteilt.
- Ein Termin, der von einem Benutzer aus Google importiert wurde kann nicht von einem anderen Benutzer in xentral verändert werden.

## Zwei Faktor Authentifizierung

> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Abschnitt des Artikels beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

xentral ermöglicht jedem Benutzer den Login per Zwei-Faktor-Authentifizierung. Hierzu wird der TOTP-Algorithmus (Time-based One-time Password) verwendet.

Mit der SchaltflächeTOTP einschaltenwird ein QR Code erstellt, der dann mit dem Google Authenticator oder einer beliebigen anderen TOTP-App gescannt werden kann. In der App wird anschließend ein Passwort oder Code gezeigt, welches beim Login in xentral eingegeben werden muss, damit sich der Benutzer anmelden kann.

Ab dann meldet sich der Benutzer immer mit der Zwei-Faktor-Authentifizierung an, sprich mit Benutzername, Passwort und einem in der App jedes mal aufs Neue generierten Code. Der Code ist immer nur für einige Sekunden gültig.