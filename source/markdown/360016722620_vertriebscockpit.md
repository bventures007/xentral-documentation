> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Das Modul Vertriebscockpit bietet Ihnen einen bequemen Überblick über alle Kunden, die speziell Ihnen als Vertrieb zugewiesen sind. Durch spezielle Übersichten und Filter haben Sie die Möglichkeit, alle wichtigen Verkaufszahlen und Aktivitäten Ihrer Kunden zu überwachen und bei Bedarf Schritte einzuleiten, damit Ihre Kunden zufrieden sind.

App Center → Vertriebscockpit

> **Anmerkung**
>
> Es handelt sich um ein Legacy-Modul, das nicht mehr von xentral unterstützt oder weiterentwickelt wird. Um unseren Kunden die Arbeit mit der vorhandenen Funktionsweise weiterhin zu ermöglichen, ist es noch immer im xentral App Store verfügbar.

Wie schon erwähnt, ist es notwendig, dass der Mitarbeiter als „Vertrieb“ bei den Kunden (Stammdaten → Adressen) hinterlegt ist:

![SalesCockpit1.png](https://help.xentral.com/hc/article_attachments/5033228603420)

### Übersicht

Auf der Startseite des Vertriebscockpits sieht man seine

- Letzten 5 Rechnungen
- Letzten 5 Angebote
- Umsatz für die laufende Woche, Monat, Jahr
- Wiedervorlagen

![SalesCockpit2.png](https://help.xentral.com/hc/article_attachments/5033183523868)

> **Anmerkung**
>
> Die Rechnungs- und Angebotsnummern sind direkte Links zu den jeweiligen Dokumenten.

Die Wiedervorlagen werden farblich voneinander getrennt und mit der folgenden Reihenfolge gelistet:

- Grün → Heute fällig
- Rot → In der Vergangenheit fällig
- Normal → In der Zukunft fällig

Mit dem![SalesCockpitGreyArrow.png](https://help.xentral.com/hc/article_attachments/5033257178908)

Pfeil rechts kommen Sie direkt in die Korrespondenzen der Adresse und können dort die Wiedervorlagen bearbeiten.

### Umsätze

Im Tab Umsätze stehen für Sie Filter bereit, mit denen Sie zielsicher Ihre Wunsch-Kundengruppe finden und deren Rechnungsbeträge in Summe anzeigen können.

> **Anmerkung**
>
> Einige Filterfelder stellen Sie unter dem Tab „Einstellungen“ ein.

Die Felder „Umsatzpotential“ und „Kontaktursprung“ werden der Adresse als Gruppenkategorie übergeben. Wie Sie eine Gruppe und die Gruppenkategorien erstellen und zuweisen erfahren Sie hier:[Gruppen](https://help.xentral.com/hc/articles/360016722000#UUID-27c9f5ac-bebe-bc23-79b2-b19285784cfc).

Beispiele für nützliche Filtereinstellungen:

- Alle Kunden einer bestimmten PLZ & einer Umsatzhöhe bis 10000 Euro
- Alle Kunden eines bestimmten Landes mit Kontaktursprung der letzten Messe
- Alle Kunden eines Vertriebsmitarbeiters mit dem Umsatzpotential von über 10000 Euro

> **Anmerkung**
>
> Ab Version 17.2 gibt es nun eine neue Spalte „Letzter Kontakt“. Diese Spalte stellt das letzte Datum da, des letzten Eintrags unter Adressen → CRM. Also Belegdatum oder ein eingetragener Termin, Notiz, etc.

Dazu benötigt man noch folgenden[Prozessstarter](https://help.xentral.com/hc/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a):

![SalesCockpit3.png](https://help.xentral.com/hc/article_attachments/5033130803868)

### Angebote

Das „Angebote“ Tab funktioniert entsprechend des „Umsätze“ Tabs. Nur werden hier statt Rechnungen, die erstellten Angebote berücksichtigt.

### Notizen

Im „Notizen“ Tab haben Sie die Möglichkeit, ihr CRM durch entsprechende Filter zu kontrollieren. Es werden hier Notizen und E-Mails in der Übersicht aufgeführt.

Neben den Filtern aus dem „Einstellungen“ Tab (Kontaktursprung, Umsatzpotential, Freifelder) bekommen Sie hier auch folgende Felder an die Hand:

- Kunden mit Notizen: Zeigt alle Kunden an, die in diesem Zeitraum eine Notiz in den Adressdaten erhalten haben
- Kunden ohne Notizen: Zeigt alle Kunden an, die seit einem best. Datum keine Notizen mehr bekommen haben
- Kunden ohne offene Wiedervorlagen: Zeigt alle Kunden an, zu denen seit einem best. Datum keine Wiedervorlagen erstellt worden sind.

Dies ermöglicht Ihnen die Kunden zu filtern, bei denen Sie nicht „aktiv“ waren und vielleicht wieder etwas mehr Aufmerksamkeit bräuchten, in Form von Angeboten / Wiedervorlagen. Vor allem in Kombination mit dem Umsatzpotential kann dies ein hilfreicher Filter sein.

Beispiele für nützliche Filtereinstellungen:

- Zeige alle Kunden, die seit einem best. Datum keine Notizen und Wiedervorlagen bekamen
- Zeige alle Kunden, die seit einem best. Datum keine Wiedervorlagen bekamen und einem best. Vertriebsmitarbeiter zugeordnet sind
- Zeige alle Kunden, die seit einem best. Datum keine Wiedervorlagen bekamen und das Umsatzpotential über 15000 Euro haben

### CSV Export

Ein Klick auf dieses Tab erstellt eine umfangreiche CSV Datei aller Adressdaten mit hilfreichen Spalten, wie z.B.:

- Kontaktursprung
- Umsatzpotential
- Vertriebsmitarbeiter
- Datum der offenen Wiedervorlage
- Anzahl und Betragssumme der Angebote
- Gesamtumsatz

> **Anmerkung**
>
> Dynamisch werden die 3 Spalten in den Vertriebscockpit - Einstellungen mit in die CSV gespeist (siehe nächster Punkt).

### Einstellungen

Hier können Sie die Filterfelder wählen, die bei den einzelnen Tabs angezeigt werden.

![SalesCockpit4.png](https://help.xentral.com/hc/article_attachments/5033181389980)

### Spezielle Rechteverteilung durch das Vertriebscockpit

Durch das Vertriebscockpit bekommen Sie auch eine spezielle Rechteeinstellung, die es ermöglicht Ihren Vertretern bestimmte Kunden zuzuordnen. Die Vertreter sehen dadurch auch nur die Kunden, denen Sie zugewiesen sind.

Voraussetzung:

- In der Adresse muss der Vertriebsmitarbeiter unter dem Feld „Vertrieb“ hinterlegt sein.
- Die Vertreter-Adresse darf keine Projekte als Rollen haben.
- Das Projekt der Adressen darf nicht öffentlich für alle Mitarbeiter sein.

Auswirkungen: Wenn diese Voraussetzungen erfüllt sind, trifft Folgendes für den eingeloggten Benutzer mit der Vertreteradresse zu:

- In den Adressen sieht er nur die Kunden, die im Feld Vertrieb seine Adresse haben
- In Belegen kann er nur seine Kunden auswählen und sieht auch in der Überschrift nur Belege mit seinen Kunden

Soll ein solcher Mitarbeiter auch die Gruppen in den Adressen sehen, bedarf es eines Workarounds:

- Neues Projekt GRUPPEN erstellen
- Dem Vertreter die Rolle „Mitglied von Projekt GRUPPEN“ geben
- Den einzelnen Gruppen das Projekt GRUPPEN zuweisen.

### Erweiterungen bei den Adressen durch das Vertriebscockpit

Ab Version 19.1 sind bei den Adressen zusätzliche Angaben bei der Nutzung des Vertriebscockpits verfügbar.

In der Adressübersicht sind nun die verwendeten Rollen in den Mini-Details einsehbar.

Außerdem befinden sich unter den Adressdetails die Angaben zu den verwendeten Gruppen.