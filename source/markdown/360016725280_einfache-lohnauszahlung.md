Über das Modul "Einfache Lohnauszahlung" können Gehälter separat von anderen Verbindlichkeiten überwiesen werden. Hierbei wird eine XML-Datei für den Sepa Zahlungsverkehr erzeugt.

## Neue Mitarbeiter hinzufügen

Neue Mitarbeiter können über den Button "+NEU" zur Überweisungs-Liste hinzugefügt werden. Dazu ist ein Mitarbeiter (Adresse benötigt Rolle: Mitarbeiter) auszuwählen und und über den "Pfeil"-Button rechts einzufügen. Der Mitarbeiter ist nun der Überweisungs-Liste für die Gehälter hinzugefügt.

## Betrag eingeben

Das "Stift"-Icon ganz rechts kann zur Eingabe des zu überweisenden Gehalts genutzt werden. Dabei ist das Gehalt anzugeben und anschließend auf "Speichern" zu klicken.

## Gehälter überweisen

Um Gehälter zu überweisen, ist ein neuer Überweisungslauf für die gewünschten Mitarbeiter zu starten. Anhaken auszuwählen. Diese Positionen werden in den nächsten Lauf als XML-Datei übernommen. Folgende Vorgehensweise ist einzuhalten:

1. Über Anhaken sind die entsprechenden Mitarbeiter auszuwählen
1. Falls für die Mitarbeiter verschiedene Bankkonto angelegt sind, ist aus dem Drop-Down Menü die gewünschte Bank auszuwählen. Für die Überweisung muss zuvor aber für jeden Mitarbeiter die Bankverbindung als Geschäftskonto mit IBAN und BIC angelegt worden sein
1. Es ist auf den Button "Sammelüberweisung Gehalt XX.XXXX anlegen und Zahlungen als bezahlt markieren" zu klicken
1. Die XML-Datei öffnet sich zum Download

Dann werden die mitgenommenen Positionen mit dem Datum von heute als bezahlt markiert, verbleibende Positionen sind weiterhin für diesen Monat offen bzw. werden als ausstehend angezeigt.

> **Anmerkung**
>
> Diese erzeugte XML Datei kann in das Banking Programm oder das Online Banking, welches bei einigen Banken unterstützt wird, importiert werden. Bei den entsprechenden Mitarbeitern wird als Info das letzte Überweisungsdatum gesetzt. Alle verbleibenden Gehälter werden dann jeweils automatisch immer mit vorgeschlagen. Um die zuletzt erzeugte XML-Datei nochmal herunterzuladen, ist auf den Button "Letzte XML Datei herunterladen" zu klicken.

Die Spalte "Gehalt" zeigt unten die Summe über alle anmarkierten Überweisungspositionen im Vergleich zur Gesamtsumme aller Positionen. Dadurch kann die richtige Anzahl an Überweisungspositionen für das vorhandene Überweisungslimit ausgewählt werden.

## Mitarbeiter löschen

Eine monatliche Überweisung für einen Mitarbeiter kann über "löschen" deaktiviert/gelöscht werden. Dazu ist auf das "Kreuz"-Icon in der Menü-Spalte zu klicken. Dadurch werden nur Mitarbeiter aus der vorliegenden Liste in den nächsten Zahlungslauf übernommen.