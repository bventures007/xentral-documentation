Amainvoice ist ein Drittanbieter, der eine Buchhaltungssoftware für Amazon-Verkäufer anbietet. Mit dieser Software kannst du steuerkonforme Rechnungen und Gutschriften für deine Kunden erstellen. Zusätzlich kannst du bei Bedarf Aufträge zusammen mit deinen Amainvoice-Rechnungen importieren.

Xentral bietet eine Schnittstelle zu Amainvoice.

Es gibt zwei allgemeine Vorgehensweisen, denen du folgen kannst

- Xentral importiert die Aufträge von Amazon ohne Rechnungen zu erstellen. Du kannst dies in der Amazon-Schnittstelle einrichten. In diesem Fall kannst du Xentral für den Versandprozess und Lageranpassungen verwenden, während Amainvoice gleichzeitig die Rechnung erstellt. Die Rechnungen werden dann in Xentral importiert.
- Wenn Xentral die Aufträge nicht von Amazon importiert, können diese durch Amainvoice ebenfalls angelegt und zusammen mit den Rechnungen importiert werden. Wenn du diese Vorgehensweise anwendest, hast du den Hauptverkaufsfall in deinem System und so Zugriff auf alle Statistiken.

Du kannst jedoch die Einrichtung frei nach deinen Geschäftsanforderungen vornehmen.

## Amainvoice mit Xentral verbinden und konfigurieren

Um Amainvoice mit Xentral verbinden zu können, benötigst du einen Authentifizierungstoken von Amainvoice und deine Amainvoice-Kundennummer.

Du kannst deinen Xentral-Authentifizierungstoken wie folgt in Amainvoice generieren:

1. Melde dich in Amainvoice an und navigiere zu Einstellungen > Fimendaten > Amainvoice-API > Xentral API.
1. Verschiebe den Schieber bei Xentral API inaktiv nach rechts. Dadurch wird die Xentral-API aktiviert.

Der Authentifizierungstoken wird erstellt und unter dem Schieber angezeigt. Klicke auf dasKopiersymbol deines Tokens, um ihn zu kopieren.

Deine Kundennummer findest du oben rechts in Amainvoice neben deinem Firmennamen.

Gehe wie folgt vor, um Amainvoice mit Xentral zu verbinden und zu konfigurieren:

1. Navigiere in Xentral zu App Center > Buchhaltung > amainvoice. Der Amainvoice-Reiter Einstellungen wird angezeigt.
1. Gib deine Amainvoice-Kundennummer in das Feld AmaInvoice Kundennummer ein.
1. Gib den Authentifizierungstoken aus Amainvoice in das Feld Xentral Auth Token ein.
1. Im Feld Rechnungen abholen ab kannst du das Datum auswählen, ab dem du Rechnungen und Gutschriften aus Amainvoice importieren möchtest. Wenn du auf das Feld klickst, wird ein Kalender angezeigt. Wähle das gewünschte Datum im Kalender aus.
1. Falls du unterschiedliche Projekte für FBA (Versand durch Amazon) und/oder FBM (Versand durch Händler) angelegt hast, wähle die entsprechenden Projekte in den Feldern Projekt FBA und Projekt FBM.
1. Optional:
  Mit Setzen eines Häkchens bei Experten Modus wird das Kontrollkästchen Aufträge angezeigt. Im Allgemeinen erstellt Amainvoice nur Rechnungen und Gutschriften für bestehende Aufträge. Setzt du ein Häkchen bei Aufträge, erstellt Amainvoice auch den Auftrag, der dann zusammen mit der Rechnung in Xentral importiert wird.

1. Klicke auf Speichern.

Deine Amainvoice-Verbindung kann nun verwendet werden.

Stelle sicher, dass derAmaInvoice-Prozessstarter eingerichtet und aktiv ist, um deine Schnittstelle korrekt nutzen zu können. Weitere Informationen zum Thema Prozessstarter findest du[hier](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a).

> **Anmerkung**
>
> Daten werden oft zeitverzögert versendet, d.h. Rechnungen werden nicht immer mit dem nächsten Import übermittelt.

## Rechnungen/Gutschriften nachladen

InXentral kannst du Amainvoice-Daten der letzten beiden Monate nachladen, wenn Rechnungen, Gutschriften oder Aufträge fehlen.

Du kannst deine Amainvoice-Daten folgendermaßen nachladen:

1. Navigiere in Xentral zu App Center > Buchhaltung > amainvoice. Der Amainvoice-Reiter Einstellungen wird angezeigt. Öffne den Reiter Logs.
1. Wenn du die Daten eines bestimmten Datums, für den ein Logeintrag existiert, nachladen möchtest, setze auf der linken Seite ein Häkchen bei dem entsprechenden Eintrag und klicke dann auf Rechnungen/Gutschriften nachladen.
  Wenn du die Daten eines bestimmten Zeitraums nachladen möchtest, definiere den Zeitraum über die Felder von und bis im Bereich Aktionen und klicke auf Daten erneut von AmaInvoice herunterladen. Die Daten werden über die API geladen. Dieser Prozess kann mehrere Stunden dauern.

Die Daten werden nachgeladen und du kannst sie wie gewohnt verarbeiten.

### Achtung

Belegnachladung und Importdauer:

Beim Nachladen von Belegen sollte der Import idealerweise wochenweise, maximal monatsweise erfolgen, um lange Ladezeiten zu vermeiden. Eine Begrenzung gibt es nicht, jedoch sind etwa 300 Belege pro Import eine empfohlene Richtlinie.

- Der Prozessstarter läuft standardmäßig alle 60 Minuten.
- Pro Durchlauf wird nur eine Datei importiert.
- Ein vollständiger Tagesimport umfasst drei Dateien (.tax,.inv,.rem), weshalb größere Reimporte mehrere Tage dauern können.
- Der Nachlade-Button kann den Importprozess erheblich verlangsamen.