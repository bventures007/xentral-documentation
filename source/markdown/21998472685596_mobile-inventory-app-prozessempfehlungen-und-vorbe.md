Bevor du deine erste Inventur mit der Mobile Inventory App von Xentral durchführst, soll dir dieser Artikel einen Überblick darüber geben, wie der Inventurprozess grob abläuft und was du im Vorfeld beachten solltest, um einen korrekten und effizienten Ablauf zu gewährleisten.

> **Wichtig**
>
> Beachte die Hinweise in diesem Artikel sorgfältig und stelle sicher, dass du alle Punkte bedacht hast, **bevor** du mit der Inventur in deinem Lager startest.
>
> Vor allem die vorbereitenden Schritte in Xentral solltest du gewissenhaft durchführen, da es sonst zu gravierenden Bestandsabweichungen kommen kann und somit andere wichtige Geschäftsabläufe, wie beispielsweise der Versand, gestört werden können. Die vorbereitenden Schritte werden im KapitelNotwendige Arbeitsschritte vor der Inventureingehend beschrieben. Am Ende des Artikels findest du auch eine Checkliste, die du nutzen kannst, um sicherzustellen, dass du alles erledigt hast.

## Allgemeiner Ablauf und Empfehlungen

Mit der Mobile Inventory App folgt die Inventur folgendem groben Ablauf:

- **Lagerplätze nacheinander zählen**: Das Lagerpersonal bewegt sich von einem Lagerplatz zum nächsten. Sobald die Bestände eines Lagerplatzes final gezählt wurden, wird die Zählung am nächsten Lagerplatz fortgesetzt.
- **Inventurläufe organisieren**: Vor der Inventur wird in der App festgelegt, in welchem Lager die Zählung stattfindet, welche Lagerplätze gezählt werden sollen, welche Person die Bestände zählt, welche Person die Zählergebnisse prüft und (optional) welcher Namen der Inventurlauf zugewiesen werden soll, damit er später im Rahmen der Auswertung in Xentral möglichst leicht zu identifizieren ist.
- **Arbeit in Zweier-Teams**: Idealerweise wird die Inventur in Zweier-Teams durchgeführt. Dabei bedient eine Person (der * Zähler*) die Mobile Inventory App auf dem MDE-Gerät. Eine zweite Person (der * Prüfer*) überwacht den Prozess um sicherzustellen, dass Bestände nicht doppelt gezählt oder vergessen werden.

> **Warnung**
>
> Mit zunehmender Anzahl an Artikeln innerhalb eines Lagerplatzes kann sich die Performance der Inventory App spürbar verlangsamen. Erfahrungsgemäß betrifft dies Konstellationen, in denen pro Regal **mehr als 300 Artikel** vorhanden sind.
>
> Daher empfehlen wir, Lagerplätze mit besonders vielen Artikeln in mehrere (ggf. virtuelle) Regale zu unterteilen. Das betrifft insbesondere POS-Lager, bei denen z. B. ein gesamter Store als ein Lagerplatz geführt wird. Durch die Aufteilung in mehrere Regale innerhalb des Lagerplatzes könnt ihr die gezählten Artikelmengen besser strukturieren und gleichzeitig sicherstellen, dass die App flüssig und zuverlässig bleibt. Schau dir bei Bedarf den ArtikelLagerstruktur erstellen (XentralLagerverwaltung)an, um zu erfahren, wie du Änderungen an deiner Lagerstruktur vornimmst.

## Notwendige Arbeitsschritte vor der Inventur

Vor der Inventur müssen mehrere Arbeitsschritte durchgeführt werden. Das ist einerseits wichtig, um sicherzustellen, dass die Mobile Inventory App alle Artikel und Lagerplätze korrekt erfassen kann und die dafür benötigten Informationen vollständig in deiner Xentral-Instanz gepflegt sind. Andererseits gibt es konkrete Aktionen, die direkt vor Inventurbeginn durchgeführt werden müssen, wie die globale Deaktivierung deiner Prozessstarter und die Abarbeitung aller noch offenen Aufträge, damit es nicht zu Bestandsfehlern kommt.

### Artikelstammdaten in Xentral kontrollieren

Vor der Inventur muss sichergestellt sein, dass deine Artikelstammdaten aktuell und vollständig sind. Nur so können die Artikel von der App korrekt erfasst und identifiziert werden.

Kontrolliere unter **Verkaufen > Artikel > Artikel öffnen > Details** die folgenden Punkte:

- Korrekte Artikelnummern und EANs
- Korrekte Artikelbezeichnung
- **Keine** mehrfach vergebenen Artikelnummern oder EANs

Falls deine Artikel über Fremdnummern aus Online-Shops oder anderen Verkaufsplattformen verfügen, muss sichergestellt sein, dass dein MDE-Gerät diese Fremdnummern auch während des Inventurvorgangs korrekt erfassen und zuordnen kann.

Die relevante Einstellung dazu findest du unter **Verkaufen > Artikel > Artikel öffnen > Tab: Fremdnummern **. Stelle sicher, dass die Optionen ** Barcode **und ** Aktiv**aktiviert sind, also beide Häkchen gesetzt sind. Achte auch bei der Anlage neuer Fremdnummern darauf, dass diese Optionen aktiviert werden.

> **Tipp**
>
> Für bereits bestehende Fremdnummern kannst du noch einfacher prüfen, ob die Checkboxen aktiviert sind, indem du über die Smart Search das Modul **Artikel Fremdnummern** öffnest und die dort angezeigte Liste prüfst.

### Prozessstarter in Xentral global deaktivieren

Die globale Deaktivierung der Prozessstarter in Xentral ist essentiell, damit während der Inventur keine Aufträge an das Versandzentrum übergeben werden oder sonstige Aktionen, die sich auf Bestände auswirken, automatisiert weiterlaufen, während die Bestände gezählt werden. Führe diesen Schritt also besonders gewissenhaft durch, um fehlerhafte Bestandszahlen und mühsame Nacharbeiten zu vermeiden. Erst nach Abschluss aller Inventur aktivierst du die Prozessstarter wieder.

> **Wichtig**
>
> Arbeitest du mit einem Fulfillment-Dienstleister zusammen? Dann stimmt euch vorab über das genaue Datum und den Zeitraum der Inventur ab. Während die Prozessstarter deaktiviert sind, finden keine Datenübertragungen mehr ab. Dies kann im schlimmsten Fall den Arbeitsablauf bei deinem Logistiker erheblich stören oder die Versandabwicklung durcheinander bringen. Informiere deinen Fulfillment-Dienstleister und sonstige Anbieter, die per Prozessstarter mit Daten versorgt werden, daher im Voraus.

Gehe wie folgt vor, um die Prozessstarter global zu deaktivieren:

1. Nutze die Smart Search, um das Modul **Prozessstarter** zu öffnen.
1. Klicke oben rechts unter **Aktion ** auf **Prozessstarter global deaktivieren**.

Alle Prozessstarter werden deaktiviert. Ab diesem Zeitpunkt finden keine automatisierten Aktionen, Datenübertragungen, Picklisten-Erstellungen, Autoversand etc.

### Offene Aufträge in Logistikprozessen abschließen

Nachdem du die Prozessstarter in Xentral deaktiviert hast, musst du im nächsten Schritt alle noch offenen Aufträge, die sich noch innerhalb des Logistikprozesses befinden, abschließen. So stellst du sicher, dass unmittelbar für Kundenbestellungen benötigte Artikel noch dein Lager verlassen, also ausgebucht und versendet werden, damit diese Bestände nicht fälschlicherweise bei der Inventur mit erfasst werden.

Auf folgende Module solltest du achten und ganz genau prüfen, welche Aufträge, Picklisten und Kommissionierläufe sich bereits aktiv im Logistikprozess finden und diese zum Abschluss bringen:

- [Versandzentrum](https://help.xentral.com/hc/de/articles/360016757139#UUID-4a4119b7-84ae-169f-4a72-a56040f24881) (**Lager > Versandzentrum **) inklusive aktiver Kommissionierläufe (zu finden im Tab ** Kommissionierläufe **im Modul ** Versandzentrum**)
- [Picklisten-Profile](https://help.xentral.com/hc/de/articles/360016722600#UUID-639a7179-6df9-467b-1821-cda20df3f8be) (**Lager > Picklisten-Profile**)
- [Multi-Order-Picking](https://help.xentral.com/hc/de/articles/360016721080#UUID-956d8415-1374-323b-6023-f9a789a6e245)

### Alle Arbeiten in Xentral einstellen

Ab dem Zeitpunkt, an dem du die Prozessstarter global deaktiviert und alle offenen Aufträge abgeschlossen hat, sollten **keine Aktionen** mehr in Xentral durchgeführt werden. Sprich dich also gut mit deinen Mitarbeitern ab und informiere dein Team, vor allem auch die Versandabteilung.

> **Warnung**
>
> Während die Inventur durchgeführt wird, dürfen keine Aufträge bearbeitet und keine Bestände angepasst werden. Am Besten stoppt ihr alle Arbeiten im System und achtet darauf, die Inventur möglichst schnell abzuschließen.
>
> Wird diese Warnung nicht beachtet und werden trotzdem manuell Aufträge bearbeitet oder Bestände angepasst, müsst ihr im Nachgang mühsam die Bestände korrigieren und könnt nicht effizient direkt ins Tagesgeschäft zurückkehren.

## Checkliste für die Inventurvorbereitung

Gehe jetzt die folgende Checkliste durch, um sicherzustellen, dass du alle notwendigen Vorbereitungen für die Inventur getroffen hast:

- [Artikelstammdaten in Xentral kontrolliert](#UUID-badddbbc-9058-15cb-8736-56e991dfc0fc_section-idm235111917376211)
- [Prozessstarter global deaktiviert](#UUID-badddbbc-9058-15cb-8736-56e991dfc0fc_section-idm235111921105906)
- [Offene Aufträge in Logistikprozessen abgeschlossen](#UUID-badddbbc-9058-15cb-8736-56e991dfc0fc_section-idm235111921460604)
- Fulfillment-Dienstleister oder Logistikpartner über die Inventur informiert
- Interne Abteilungen über die Inventur informiert
- [Benötigte Benutzerzugänge inklusive QR-Codes und PINs für die Mobile Inventory App angelegt](https://help.xentral.com/hc/de/articles/21998472676252#UUID-32630639-9f22-b6e2-b021-26a264f6f6f7_section-idm235110542006543)
- Alle Arbeiten in Xentral final eingestellt