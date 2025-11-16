Du kannst Standardantworten auf Kundenanfragen im Modul[Service&Support](https://help.xentral.com/hc/de/articles/360016774259#UUID-938c8659-8712-e2aa-5cc5-db372c3b6779)in Form von Ticketvorlagen hinterlegen. Du kannst diese Ticketvorlagen ordnen, indem du Kategorien und Unterkategorien anlegst und die Ticketvorlagen entsprechend zuweist.

Du legst Ticketvorlagen auf folgenden Pfad an:Administration > System > Ticket Vorlagen. Dort kannst du sie auch verwalten.

## Vorlagenkategorien und -unterkategorien anlegen

Zur besseren Übersicht kannst du Vorlagen in Kategorien und Unterkategorien einteilen. Beispiele für Kategorien sind z.B. Beschwerden, Support-Anfragen, Rechnungsfragen, Softwareprobleme, o.ä. Diese kannst du dann auch noch in Unterkategorien aufteilen, um die Übersicht weiter zu verbessern. Bei Beschwerden könntest du zum Beispiel die Unterkategorien Software-Beschwerden, Support-Beschwerden, Beschwerden zur Qualität anlegen.

Die Kategorien und Unterkategorien werden in Form eines Vorlagenbaums auf der linken Seite des FormularsTicket Vorlagenangezeigt:

![TicketTemplateTree.png](https://help.xentral.com/hc/article_attachments/7550961013532)

Kategorien und Unterkategorien werden alphabetisch angeordnet.

Eine neue Kategorie legst du wie folgt an:

1. Gib den Namen deiner Kategorie in das Feld Name im Bereich Neue Kategorie ein.
1. Klicke auf Speichern.

Eine neue Unterkategorie legst du wie folgt an:

1. Klicke im Vorlagenbaum links auf die Kategorie, der du eine neue Unterkategorie zuweisen möchtest.
1. Gib den Namen deiner Unterkategorie in das Feld Name im Bereich Neue Unterkategorie ein.
1. Klicke auf Speichern.

Möchtest du den Namen deiner Kategorie oder Unterkategorie ändern, gehe wie folgt vor:

1. Klicke im Vorlagenbaum links auf die Kategorie oder Unterkategorie, deren Namen du ändern möchtest. Der Name der Kategorie oder Unterkategorie wird im Feld Name im Bereich Neue Kategorie angezeigt.
1. Ändere den Namen wie gewünscht.
1. Klicke auf Speichern.

Eine Kategorie oder Unterkategorie löschst du wie folgt:

1. Klicke im Vorlagenbaum links auf die Kategorie oder Unterkategorie, die du löschen möchtest. Diese ist nun markiert. Der Name der Kategorie oder Unterkategorie wird im Feld Name im Bereich Neue Kategorie angezeigt.
1. Klicke auf Löschen im Bereich Neue Kategorie, um die Kategorie oder Unterkategorie zu löschen.

> **Anmerkung**
>
> Löscht du eine Kategorie, für die Unterkategorien angelegt sind, werden alle dazugehörigen Unterkategorien ebenfalls gelöscht.

## Ticketvorlage erstellen

1. Navigiere zu Administration > System > Ticket Vorlagen.
1. Gib den Namen deiner Ticketvorlage in das Feld Neue Vorlage ein und klicke auf Speichern.
1. Ein Pop-up-Fenster wird angezeigt. Hier kannst du Folgendes definieren:
  1. Text - Der Antworttext deiner E-Mail-Vorlage.
  1. Projekt - Du kannst deine Vorlage mit einem Projekt in Xentral verknüpfen.
  1. In-Aktiv - Setze hier ein Häkchen, um diese Vorlage zu deaktivieren, z.B. wenn du sie überarbeiten möchtest oder wenn sie derzeit nicht aktuell ist (z.B. wenn Weihnachtsgrüße enthalten sind).
  1. Kategorie - Sind bereits Kategorien angelegt, kannst du hier eine Kategorie auswählen und deine Vorlage dieser Kategorie zuordnen.
  1. Sortierung - Hier kannst du die Sortierung deiner Tickets in der Live-Tabelle definieren.
1. Klicke auf Speichern.

Deine neue Ticketvorlage wird in der Ticketvorlagen-Tabelle angezeigt.

Du kannst deine Ticketvorlage bearbeiten, indem du auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/7550961095708)

in der SpalteMenüklickst. Du kannst deine Ticketvorlage löschen, indem du auf![close_preview_x21.png](https://help.xentral.com/hc/article_attachments/7550961170076)

in der SpalteMenüklickst.

## Variablen im Ticketsystem

Die folgenden Variablen stehen dir zur Verfügung:

| Feld | Feldbezeichnung |
| --- | --- |
| {NAME} | Name des mit dem Ticket verknüpften Kontakts aus dem Stammdaten (Feld: Name). |
| {ANREDE} | Anrede des mit dem Ticket verknüpften Kontakts aus dem Stammdaten (Feld: Anrede). |
| {ANSPRECHPARTNER} | Ansprechpartner des mit dem Ticket verknüpften Kontakts aus dem Stammdaten (Feld: Ansprechpartner) |
| {GRUSSWORT} | Im Standard fest hinterlegte Grußformel: DE: "Mit freundlichen Grüßen", EN: "Kind regards," 💬 **Anmerkung:** Eine eigene Signatur kannst du auch in den E-Mail Accounts direkt hinterlegen. |

## Ticketvorlagen verwenden

Deine Ticketvorlagen kannst du an folgenden Stellen im System verwenden:

- Klicke im Hauptmenü auf Inbox und öffne das Ticket, das du beantworten möchtest. Klicke dann auf Beantworten.
- Klicke im Hauptmenü auf Inbox und dann auf +NEU. Alternativ klickst du im Hauptmenü auf Inbox, öffnest ein Ticket und klickst dann auf +NEU.
- Gehe zu Verkauf > Service & Support. Öffne das Ticket, dass du beantworten möchtest und öffne dann den Reiter Ticket-Nachrichten. Klicke im Bereich Aktionen auf Neuen Gesprächsverlauf starten.