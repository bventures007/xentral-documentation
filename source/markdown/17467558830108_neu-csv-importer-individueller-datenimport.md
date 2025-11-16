> **Anmerkung**
>
> Die Nutzung dieser Funktionalität erfordert die Definition eines Workflows im Connect-Backend. Die Erstellung individueller Workflows erfordert erweiterte technische Kenntnisse, so dass der Zugang zur Connect-Instanz nur nach Schulung und Unterweisung zur Verfügung steht. Wenn du Interesse an der Nutzung individueller Workflows hast, wende dich an deinen Solution Consultant.

Mit der hier beschriebenen Funktion kannst du unterschiedlichste Daten, die in einer CSV-Datei vorliegen, in Xentral importieren. Das können z. B. sein:

- Kunden- / Adressdaten
- Bestellungen
- Lieferscheine
- Notizen
- Wiedervorlagen
- Artikeldaten, die nicht über den standardisierten Workflow eingelesen werden sollen

Der Import individueller Daten über den CSV-Importer läuft nach folgendem Prozess ab:

![IndividuellerImport_Workflow.png](https://help.xentral.com/hc/article_attachments/18704841988380)

## Individuellen Workflow definieren

> **Wichtig**
>
> Die Erstellung individueller Workflows erfordert erweiterte technische Kenntnisse, so dass der Zugang zur Connect-Instanz nur nach Schulung und Unterweisung zur Verfügung steht. Wenn du Interesse an der Nutzung individueller Workflows hast, wende dich an deinen Solution Consultant. Gerne vermitteln wir dich an einen auf deine jeweiligen Bedürfnisse spezialisierten Partner.

Du erreichst das Connect-Backend deiner Xentral-Instanz über einen Link, den du auf Anfrage erhältst. Klicke dort auf **+ Workflow erstellen ** und konfiguriere den individuellen Workflow nach deinem Bedarf. Wichtig ist, dass der Trigger**CSV Import** enthalten ist. Dieser Trigger gewährleistet, dass der Import später im CSV-Importer in Xentral zur Auswahl steht.

![Connect-Instanz_WorkflowUbersicht.png](https://help.xentral.com/hc/article_attachments/18704870453020)

## CSV-Import erstellen

Du findest den CSV-Importer im Menü **Einstellungen > Administration > Datenaustausch > CSV-Importer**.

![CSV-Importer_Menupfad__1_.png](https://help.xentral.com/hc/article_attachments/18704870453404)

Klicke auf **+ CSV-Import erstellen**, um einen neuen Import anzulegen:

![CSV-Importer_NeuenImportErstellen__1_.png](https://help.xentral.com/hc/article_attachments/18704841990940)

Lege die allgemeinen Daten deines Imports an, um ihn später wiederfinden zu können und lade die CSV-Datei hoch:

![IndividuellerImport_Dateihochladen.png](https://help.xentral.com/hc/article_attachments/18704870454812)

1. Trage einen **Namen** und
1. eine **Beschreibung** ein, die dir bei der Identifikation des Imports helfen.
1. Um individuelle Daten zu importieren, wähle den **Datentyp Individuell**.
1. Wähle den individuellen Workflow aus, mit dem du Daten importieren möchtest.
1. Füge deine **CSV-Datei** ein.
1. Unter den **Erweiterten Einstellungen** kannst du bei Bedarf Anpassungen an den Trennzeichen und Sonderzeichen vornehmen, falls die Spalten der Importdatei auf der rechten Seite nicht korrekt angezeigt werden.
1. Wähle eine oder mehrere Spalten, die als eindeutiger Bezeichner (Datenbank-ID) dienen.

## Daten in der Vorschau prüfen

Sobald du auf **Mit dem Import starten** geklickt hast, werden die Daten in eine Vorschau geladen. Hier kannst du überprüfen, ob die Daten wunschgemäß zugeordnet werden. Falls dies nicht der Fall ist, überprüfe deinen Workflow im Connect-Backend oder nimm Anpassungen an der CSV-Datei vor.

## Daten importieren

Sobald alle Daten in der Vorschau so vorliegen, wie du es benötigst, kannst du mit dem Import starten. Klicke dazu zunächst auf **Abschließen**:

![IndividuellerImport_Abschließen.png](https://help.xentral.com/hc/article_attachments/18704870457628)

Das System führt eine Datenvalidierung durch. Wenn keine invaliden Daten gefunden wurden, wird eine Erfolgsmeldung angezeigt und kannst den **Import starten**:

![IndividuellerImport_ImportStarten.png](https://help.xentral.com/hc/article_attachments/18704870458652)

Nachdem du auf Import starten geklickt hast, startet der Import im Hintergrund und du gelangst automatisch auf die Statusseite. Beim Importieren durchläuft jede Datenzeile den Workflow einmal. Auf der Statusseite kannst du die Ansicht über die Filter oben einschränken und den Status über die Schaltfläche rechts aktualisieren:

![Artikelimport_ImportstatusNeuladen__1_.png](https://help.xentral.com/hc/article_attachments/18704870459420)

Nach erfolgreichem Abschluss des Imports ist der Status für alle Datensätze grün:

![IndividuellerImport_ImportStarten.png](https://help.xentral.com/hc/article_attachments/18704870458652)

> **Anmerkung**
>
> Nach dem Start des Imports kannst Du diese Seite jederzeit schließen. Der Import läuft im Hintergrund weiter, solange noch Datensätze übrig sind. Du kannst jederzeit über dieCSV-Importer Übersichtzum Reporting zurückkehren und den Status verfolgen.

## Reporting in Connect-Instanz

Eine detaillierte Auswertung für jeden Datensatz kannst du in der Connect-Instanz betrachten. Klicke in der Workflow-Übersicht oder im Workflow selbst auf die Lupe, um das Reporting zu öffnen:

![Connect-Instanz_WorkflowUbersicht_DetailsAufrufen.png](https://help.xentral.com/hc/article_attachments/18704841998876)

Du siehst eine Liste der einzelnen Importjobs:

![Connect-Instanz_WorkflowUbersicht_JobDetailsAufrufen.png](https://help.xentral.com/hc/article_attachments/18704841999516)

Per Klick auf das Info-Symbol rechts kannst du weitere Details zu den einzelnen Datensätzen einsehen:

![Connect-Instanz_WorkflowUbersicht_JobDetailsLogs.png](https://help.xentral.com/hc/article_attachments/18704842000156)