Du kannst in Xentral ein Ticketsystem einrichten und es als primäre Kommunikationsplattform für deine Kunden verwenden. Die Verwendung des Ticketsystems bietet im Vergleich zur Korrespondenz per E-Mail viele Vorteile:

- Klar definierte Kommunikationsstränge, die einer Ticketnummer zugeordnet sind.
- Einem bestimmten Mitarbeiter zugewiesene Tickets
- Volle Kontrolle über den Bearbeitungsstand des Tickets.
- Zentralisierte und strukturierte Verarbeitung eingehender Kundenanfragen durch einen oder mehrere Mitarbeiter.

Stelle sicher, dass du über die entsprechenden Berechtigungen verfügst, bevor du das Ticketsystem einrichtest. Die Einrichtung des Ticketsystems in Xentral besteht aus mehreren Schritten.

## E-Mail-Konto für Ticketsystem einrichten

Du kannst ein bestehendes E-Mail-Konto einrichten, um Anfragen deiner Kunden zu erhalten.

1. Öffne das Menü **Einstellungen > Grundeinstellungen > E-Mail > E-Mail Konten**.
1. Klicke auf die E-Mail-Adresse, die du für das Ticketsystem verwenden möchtest.
1. Klicke im Abschnitt Ticketsystem auf das **Stift-Symbol ** d und aktiviere die Option **Für Ticket-Modul aktivieren**.
1. Optional kannst du Standard-Projekte und eine Standard-Warteschlange festlegen. Eingehende E-Mails an dieses Konto werden dann automatisch dem hier definierten Mitarbeiter (Warteschlange) oder Projekt zugeordnet.
1. Mithilfe der folgenden zusätzlichen Optionen kannst du das Ticketsystem an deine Bedürfnisse anpassen:
  1. Ab Datum: Startdatum, ab dem Xentral E-Mails abholt und in Tickets umwandelt.
  1. Ausgehende E-Mailadresse: Aktiviere diese Option, damit diese E-Mail-Adresse immer als ausgehende E-Mail-Adresse verwendet wird.
  1. E-Mails auf Server löschen: Aktiviere diese Option, um E-Mails nach dem Empfang vom Server zu löschen. Gelöschte E-Mails können nicht wiederhergestellt werden.
  1. Ticket als abgeschlossen markieren: Aktiviere diese Option, um die Tickets nach dem Import automatisch als abgeschlossen zu markieren.

## Warteschlangen einrichten

1. Öffne das Menü **Einstellungen > Team > Ticketsystem > Ticket Warteschlangen**.
1. Klicke oben rechts auf **Warteschlange hinzufügen**.
1. Gib den Namen und die Kennung in die entsprechenden Felder ein.
1. Trage einen Namen in das Feld Verantwortlicher ein, um eine bestimmte Person für diese Warteschlange festzulegen Ansonsten ist die Warteschlange für jeden Mitarbeiter verfügbar, der Zugriff auf das Ticketsystem hat.

## Auto-Responder einrichten

Du kannst eine automatische Antwort auf eingehende E-Mails im Ticketsystem einrichten.Xentral sendet eine vordefinierte E-Mail an den Kunden. Wähle im Dropdown-MenüAuto-Responderdie Optionaktiv, um automatische Antworten zu verwenden. Im Texteditor kannst du deine automatische Antwort definieren. Du kannst dabei die folgenden Variablen verwenden:

- {BETREFF} - Diese Variable fügt den Betreff dem Text deiner E-Mail hinzu.
- {TICKET} - Dies ist die Ticketnummer. Du kannst diese Variable dem Betreff oder dem Text der E-Mail hinzufügen.

> **Wichtig**
>
> Um die automatische Zuweisung der Folge-E-Mails im Ticketsystem zu gewährleisten, musst du das Rautezeichen#vor die {TICKET}-Variable im Betreff schreiben. Das korrekte Format ist #{TICKET}.

## E-Mails automatisch importieren

Um automatisch E-Mails zu importieren, musst du den entsprechenden Prozessstarter im Modul **Prozessstarter** einrichten. Bitte beachte, dass E-Mails, die ins Ticketsystem importiert wurden, möglicherweise aus deinem IMAP-Konto gelöscht werden. Dies hängt davon ab, wie der Prozess eingerichtet wurde. Du solltest E-Mails nur löschen, falls andere Software das E-Mail-Archiv sicherstellt.

> **Anmerkung**
>
> Xentral importiert nur neue E-Mails, die noch nicht geöffnet wurden.

Im Folgenden wird beschrieben, wie du einen Prozessstarter einrichtest, der automatisch E-Mails abholt. Falls du ihn schon eingerichtet hast, dann brauchst du ihn nur zu aktivieren.

1. Nutze die Smart Search, um das Modul **Prozessstarter** zu öffnen.
1. Klicke auf +NEU und trage die folgenden Informationen in die entsprechenden Felder ein:
  1. Bezeichnung: Beliebige Bezeichnung
  1. Art: Periodisch
  1. Wochentag: Jeden Tag
  1. Typ:Cronjob
  1. Parameter: tickets_oauth
  1. Aktiv: Setze hier ein Häkchen.
1. Klicke auf Speichern.

Für jede eingehende E-Mail in eines der konfigurierten E-Mail-Konten wird nun automatisch ein Ticket erzeugt. Alle ein- und ausgehenden Nachrichten, die eine Ticketnummer im Betreff enthalten, werden automatisch dem Ticket zugeordnet und dem Kommunikationsverlauf des Tickets hinzugefügt.

## Tickets verarbeiten

Du findest alle Tickets, die nicht den StatusabgeschlossenoderPapierkorbhaben, im Menü **Team > Ticketsystem**. Du kannst Tickets nach ihrem Status filtern. Der TabIn Bearbeitungenthält alle offenen Tickets, die du bearbeiten kannst.

![Tickets_filter.png](https://help.xentral.com/hc/article_attachments/6474536278684)

Wähle eine beliebige Anzahl an Tickets im BereichStapelverarbeitungaus und wähle eine der Optionen, die du auf sie anwenden möchtest:

- SPAM entfernen
- Ungelesen ins Archiv
- als persönlich markieren
- als privat markieren
- als Prio markieren - E-Mails, die als Priorität markiert wurden, erhalten das Tag Prio.

Jedes Ticket hat einen Status, der seinen Bearbeitungszustand beschreibt. Die folgende Tabelle gibt einen Überblick über die Ticketstatus.

| Status | Beschreibung |
| --- | --- |
| Neu | Automatischer Status für alle neu eingehenden Nachrichten. |
| Offen | Status für Tickets, die gerade bearbeitet werden. |
| Warten auf Intern | Status für Tickets, die noch nicht abgeschlossen wurden und vor der weiteren Bearbeitung Informationen aus deinem Unternehmen benötigen. |
| Warten auf Kunden | Status für Tickets, die noch nicht abgeschlossen wurden und vor der weiteren Bearbeitung Informationen vom Kunden benötigen. |
| Klären | Status für Tickets, bei denen vor der Zuweisung oder weiteren Bearbeitung ein Sachverhalt geklärt werden muss. |
| Abgeschlossen | Status für Tickets, bei denen die Bearbeitung abgeschlossen ist, weil sie entweder manuell geschlossen wurden oder der Kunde nicht mehr antwortet. |
| Papierkorb | Status für Tickets, die nicht bearbeitet werden sollen. Dies sind zum Beispiel Tickets, die als Spam E-Mails empfangen wurden. |

Klicke auf das **Stift-Symbol**, um ein Ticket zu öffnen. Das FeldInterner Kommentarerlaubt dir Kommentare zu hinterlegen, die du nicht mit dem Kunden teilen möchtest.

## Auf Tickets antworten

> **Wichtig**
>
> Um auf Tickets zu antworten, musst du Pop-ups in deinem Browser erlauben.

Klicke aufbeantworten. Ein Pop-up Fenster öffnet sich. In dieses Fenster kannst du deine Antwort eingeben oder eine Textvorlage verwenden. Du kannst die OptionOriginale Nachricht anhängenauswählen, sodass zusätzlich zu deiner Antwort auch die originale Nachricht enthalten ist. Du kannst auch weitere Anhänge hinzufügen. Sobald du deine Nachricht fertig gestellt hast, klicke aufSenden.

## Regeln für Tickets erstellen

Im TabRegelnkannst du Regeln für eingehende E-Mails definieren. Du kannst zum Beispiel E-Mails von bestimmten Adressen als Spam markieren oder einer bestimmten Warteschlange zuordnen. Die Regeln kannst du auf Grundlage von Empfänger- und Sender-E-Mail-Adresse, Name oder Betreff erstellen.