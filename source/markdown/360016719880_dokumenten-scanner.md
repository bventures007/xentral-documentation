Mit dem Extramodul "Dokumenten Scanner" kann in Verbindung mit der Android und iOS App "SwiftScan" Dokumente auf dem Smartphone gescannt werden und diese entweder manuell oder automatisch an Xentralübertragen. Dabei kann diese schon vorqualifizieren, ob das Dokument einer Adresse, Verbindlichkeit etc. zugewiesen werden soll. InXentral selber findet dann die finale Zuweisung statt.

- Belege einscannen und zuordnen (Lieferanten Rechnungen, Kassenzettel, Reisekosten, Verträge)
- Schnell und einfach den Vorgängen in Xentral zuweisen
- Bequem per App vom Smartphone oder per Drag and Drop (Einzel- und viele Dateien)

Das ist vor allem zum Scannen von Lieferanten-Rechnungen in Verbindlichkeiten sowie für Adress-Dateien wichtig, die schnell in der Adresse hinterlegt werden sollen.

App Center → Dokumenten Scanner

SwiftScan Android: https://play.google.com/store/apps/details?id=net.doo.snap&amp;hl=de

SwiftScan iOS: https://itunes.apple.com/de/app/scanbot-scanner-app-fax/id834854351

> **Anmerkung**
>
> Zu beachten ist, dass die Daten über SwiftScan laufen und laut DSGVO ggf. ein Datenvertrag abgeschlossen werden muss.

## Dokumenten Scanner Oberfläche

InXentral liegt die Oberfläche, in der alle gescannten Dokumente aus der App SwiftScan erscheinen. Natürlich kann das Modul auch teilweise ohne die App SwiftScan genutzt werden.

### Dateien

Im Reiter Dateien, sind alle Dateien ersichtlich, die in Xentral hochgeladen wurden, aber noch nicht zugewiesen wurden. Auch die Dokumente von GetMyInvoices werden hier angezeigt, sofern die Seite angebunden wurde.

#### Dokumente zuordnen

Mit dem "+" Icon in der Menü-Spalte kann eine Zuweisung des Dokuments durchgeführt werden.

Sollte die Zuweisung in SwiftScan schon geschehen sein, wird gleich das richtige Tab ausgewählt. Ansonsten können die Tabs manuell ausgewählt und mit dem Pfeil zugewiesen werden.

Das Dokument wird daraufhin dort als Datei gespeichert.

Filter Archiv (alle anzeigen)→ Zeigt auch bereits über das Modul zugewiesene Dateien an

### Vorschau + Upload

Via Drag &amp; Drop kann eine Datei in das graue Feld an der Seite ziehen, damit diese in das Modul geladen wird.

### Upload

Im Reiter Upload kann nach einer Datei auf der Festplatte gesucht und diese so in das Modul hochgeladen werden.

## Arbeiten mit der SwiftScan App

In Verbindung mit SwiftScan lassen sich die Dokumente direkt über das Smartphone einscannen und übertragen. Es ist zwingend die kostenpflichtige Version SwiftScanVIP notwendig, da sonst die Verbindung per WebDAV nicht hergestellt werden kann

Dafür muss eine Verbindung mit Xentral hergestellt werden. Dafür sind mehrere Schritte in Xentral und in SwiftScan nötig.

Xentral: WebDAV im Benutzer einrichtenuser

Damit die Verbindung mit SwiftScan besteht, muss WebDAV im jeweiligen Benutzer in Xentral freigeschaltet sein. Unter Administration → Einstellungen → System → Benutzer muss für den ausgewählten Benutzer der Haken gesetzt und ein Passwort vergeben werden:

> **Anmerkung**
>
> Unterhalb des Passwort Felds ist die Adresse ersichtlich, die für die Einrichtung in SwiftScan gebraucht wird.

SwiftScan App: Cloud Dienste aktivieren (Die Menüstruktur in SwiftScan kann sich ändern. Beschreibung Stand Dezember 2018) (Offizielle Support-Seite von SwiftScan: https://swiftscan.zendesk.com/hc/en-us))

Die Anleitung ist auf einem Android Gerät durchgeführt worden, die folgenden Schritte gelten aber auch für iOS-Geräte.

1. Öffne in der App das Menü durch drücken der drei Punkte rechts oben auf der Startseite.
1. Klicke auf Einstellungen.
1. Klicke auf Cloud-Dienste.
1. Drücke das "+"-Icon unten rechts.
1. Wähle WebDAV aus der Liste aus.
1. Gebe die WebDAV Zugangsdaten ein.

Hier sind die Daten aus Xentralfür den Benutzer einzutragen.

- WebDAV Adresse → (URL)Adresse im Benutzer unterhalb des WebDav Passwort
- Nutzername → Benutzername in Xentral (normaler Login Name in Xentral)
- Passwort → webDAV Passwort im Benutzer in Xentral

Wenn eine Verbindung hergestellt werden konnte, dann sollte eine Bestätigung erhalten und WebDAV in den Einstellungen als "Connected Cloud Service" angezeigt werden.

SwiftScan App: Automatisches Übertragen einstellen (optional)

Wenn erwünscht ist, dass SwiftScan jedes eingescannte Dokument automatisch an Xentralüberträgt, kann das automatische Übertragen in den Einstellungen aktiviert werden:

Hinweis von SwiftScan: Automatischer Upload ist nur dann verfügbar, wenn der Nutzer auf SwiftScan Pro geupgraded hat. Der manuelle Upload ist auch für "Free" Nutzer verfügbar.

> **Anmerkung**
>
> Wenn der automatische Upload nicht funktioniert, kann es nötig sein, dass der Ordner geändert und der Wert dort komplett herausgelöscht wird, sodass in den Einstellungen nur noch ein "/" erscheint.

### Manuell Dokumente von SwiftScan übertragen

Sollte die automatische Übertragung nicht aktiviert sein, kann ein gescanntes Dokument auch manuell übertragen und dabei schon gleich zugewiesen werden.

1. Klicke Freigeben/Send to nach Scan.
1. Wähle WebDAV/admin aus (könnte sich unter dem Punkt "Mehr" verbergen).
1. Wähle einen Ordner für die Zuweisung aus.
1. Übertrage das Dokument durch "Upload Here".