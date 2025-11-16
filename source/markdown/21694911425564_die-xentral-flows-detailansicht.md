Du erreichst die Detailansicht, indem du in der Xentral Flows Übersicht auf das Lupen-Symbol klickst:

![XentralFlows_DetailansichtOffnen.png](https://help.xentral.com/hc/article_attachments/21695012758300)

## Überblick

In der Xentral Flows Detailansicht

- erhälst du detaillierte Informationen zu einem Flow,
- kannst du den Workflow manuell ausführen und testen,
- bekommst du einen genauen Überblick über den Status des ausgeführten Workflows,
- kannst du Parameter und Trigger für den Workflow einstellen.

![XentralFlows_DetailansichtUberblick.png](https://help.xentral.com/hc/article_attachments/21694981341596)

## Informationen

Im BereichInformationenfindest du detaillierte Informationen zum vorliegenden Flow. Möglich sind hier neben einer textlichen Beschreibung auch Bilder.

![XentralFlows_Detailansicht_Information.png](https://help.xentral.com/hc/article_attachments/21694981342364)

## Workflow ausführen

Im BereichWorkflow ausführenlässt sich ein Flow manuell ausführen und testen.

![XentralFlows_Detailansicht_WorkflowAusfuhren.png](https://help.xentral.com/hc/article_attachments/21695012763804)

- Um einen Flow zu starten, klicke auf Workflow ausführen. Der Workflow wird direkt gestartet. Es wird eine Erfolgsmeldung am unteren Bildschirmrand angezeigt.
- Um einen Flow mit bestimmten Parametern zu starten, kannst du vor der Ausführung Anpassungen in dem Codefeld vornehmen. Gib dort beliebige Parameter im JSON-Format ein. Die per Default angezeigten Parameter entsprechen den im Bereich Parameter (rechte Spalte) eingetragenen Werten. In aller Regel kannst du Parameter also über das Formular im Bereich Parameter definieren und diese im Codefeld zu Testzwecken überschreiben.

> **Anmerkung**
>
> Die Definition der für einen Workflow verfügbaren Parameter erfolgt im Zuge der Workflow-Erstellung in Xentral Connect und kann in der Xentral Flows Oberfläche nicht verändert werden.

## Letzte Ausführungen

Im BereichLetzte Ausführungenwerden dir die letzten Ausführungen des jeweiligen Workflows angezeigt. Je nach Workflow sind enthalten:

- Content Identifier (meist eine sprechende Nachricht über den Status des Workflows)
- Case Identifier (meist eine eindeutige ID, Produktnummer, Auftragsnummer oder Ähnliches)
- Status der letzten Flow-Ausführung (Bevorstehend, erfolgreich abgeschlossen, fehlerhaft, …)
- Dauer der letzten Ausführung
- Startzeitpunkt der letzten Ausführung

![XentralFlows_Detailansicht_LetzteAusfuhrungen.png](https://help.xentral.com/hc/article_attachments/21695012765212)

(1) Über dieFreitextsuchekannst du in der Liste der Ausführungen suchen.

(2) MitNeu ladenkannst du die Anzeige aktualisieren.

(3) Du kannst du Liste nachCode Identifier,Case Identifier,StatusoderGestartet amauf- oder absteigend sortieren, indem du ein- bzw. zweimal auf die entsprechenden Spaltentitel klickst.

## Reiter Status

Generell gibt es zwei Möglichkeiten, einen Workflow auszuführen:

1. Manuell im Bereich Workflow ausführen.
1. Automatisch entsprechend der konfigurierten Trigger.

Wenn du nur eine manuelle Ausführung benötigst, belasse die Schaltfläche im Reiter Status inaktiv und führe den Workflow manuell aus, sobald erforderlich.

Für die automatische Ausführung stelle zunächst dieTriggerim gleichnamigen Reiter nach deinem Bedarf ein. Setze anschließend die Schaltfläche im ReiterStatusauf aktiv:

![XentralFlows_Detailansicht_Status.png](https://help.xentral.com/hc/article_attachments/21695012766492)

## Reiter Parameter

![XentralFlows_Detailansicht_Parameter.png](https://help.xentral.com/hc/article_attachments/21694981344540)

In diesem Reiter werden alle für den Workflow definierten Parameter gelistet. Parameter sind Werte, die im jeweiligen Workflow als Variablen definiert werden und pro Instanz konfiguriert werden können. Ein Parameter kann sehr unterschiedliche Arten von Informationen abfragen. Je nach Feldtyp können textliche Inhalte, numerische Werte oder Auswahlwerte aus vordefinierten Werten eingegeben werden.

## Reiter Trigger

![XentralFlows_Detailansicht_Trigger.png](https://help.xentral.com/hc/article_attachments/21694981347612)

Im ReiterTriggerwird die Ablaufsteuerung eines Workflows konfiguriert. Es stehen drei verschiedene Arten von Triggern zur Verfügung:

- Manueller Trigger: Der manuelle Trigger ist immer aktiv und kann nicht deaktiviert werden. Das bedeutet, ein hinterlegter Workflow kann immer manuell im Bereich Workflow ausführen gestartet werden. Der manuelle Trigger funktioniert auch, wenn der Workflow nicht aktiv geschaltet ist.
- Zeitgesteuerter Trigger: Optional. Workflow wird per Cronjob entsprechend der definierten Regeln gestartet. Wähle die gewünschte Methode aus der vorgegebenen Liste. Je nach gewählter Methode lässt sich diese dann weiter spezifizieren (z. B. lässt sich die Uhrzeit definieren, wenn der Workflow täglich zu einer bestimmten Uhrzeit gestartet werden soll).
- Eventbasierter Trigger: Workflow wird gestartet, wenn ein definiertes Ereignis in Xentral auftritt. Um den Workflow bei einem bestimmten Ereignis in Xentral zu starten, wähle zuerst das Topic aus der definierten Liste. Typischerweise entspricht das Topic dem Datentyp, der in Xentral verändert wird (z. B. Product, Customer, SalesOrder, Invoice, etc.). Wähle im nächsten Schritt die zugehörige Action. Die Action definiert, welche Art von Ereignis mit dem ausgewählten Datentyp passieren soll (Create, Update, Delete, etc.).