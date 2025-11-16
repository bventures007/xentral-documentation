Mit der App "Bestellvorschlag E-Mail" kann eingestellt werden, dass in regelmäßigen Abständen E-Mails mit einem Bestellvorschlag an den xentral User gesendet werden. Falls die Lagermenge geringer als der Mindestbestand ist, prüft das System, welche Menge im Vergleich zum Mindestbestand fehlt. Zudem wird kontrolliert, ob verplante Artikel von offenen Aufträgen ausreichend auf Lager sind, um die Aufträge abzufertigen.

## Übersicht

Über App Center → Bestellvorschlag E-Mail kann die E-Mail-Adresse hinterlegt werden, an welche die Bestellvorschläge geschickt werden sollen:

![order_proposal_email.png](https://help.xentral.com/hc/article_attachments/5037947365660)

- Modul aktivieren → Anhaken, um die App zu nutzen
- Empfänger für Mail aus Cronjob → E-Mail-Adresse eintragen, an welche der Bestellvorschlag gesendet wird. Um mehrere Adressen einzutragen, ist ein Semikolon zu verwenden
- Benachrichtigungen nur an Werktagen → Anhaken, um E-Mails nur an Werktagen zu erhalten

## Prozessstarter

Das automatische Verschicken der E-Mails funktioniert über den Prozessstarter "Bestellvorschlag Mail". Dazu muss ein neuer Prozessstarter angelegt werden, aktiviert sein und den richtigen Parameter besitzen.

In folgendem Beispiel wird der Prozessstarter neu angelegt: Er läuft immer montags um 17 Uhr und verschickt die E-Mail mit dem Bestellvorschlag, falls Positionen in diesem vorhanden sind:

![process_starter_ope.png](https://help.xentral.com/hc/article_attachments/5037961749788)

- Bezeichung → Hier ist "Bestellvorschlag Mail" einzugeben
- Art → Aus dem Dropdown-Menü ist die gewünschte Art auszuwählen
- Wochentag → Der entsprechende Wochentag ist einzustellen
- Startzeit → Die Startzeit sowie das Startdatum sind anzugeben
- Letzte Ausführung → Die Zeit sowie das Datum der letzten Ausführung können eingegeben werden
- Typ → Typ "Cronjob" ist aus dem Dropdown-Menü auszuwählen
- Parameter → Als Parameter ist "bestellvorschlagemail" einzupflegen
- Aktiv → Um den Prozessstarter zu verwenden, ist der Haken zu setzen

## E-Mail

Die jeweilige E-Mail zeigt das gleiche Ergebnis wie die Oberfläche "Bestellvorschlag". In der Spalte ganz rechts wird angezeigt, wie viele Einheiten der jeweiligen Artikel im Lager im Vergleich fehlen, sodass kontrolliert werden kann, ob offene Aufträge bedient bzw. der Mindestbestand eingehalten werden kann.