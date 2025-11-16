Willkommen zu unserer FAQ-Seite! Hier findest du Antworten auf die am häufigsten gestellten Fragen zu unseren Produkten und Services. Diese Seite dient dazu, dir schnelle und hilfreiche Informationen zu bieten, die dir bei der Nutzung unserer Plattform weiterhelfen. Ob zur Einrichtung, Fehlerbehebung oder für Tipps zur optimalen Nutzung – unsere FAQ bieten dir umfassende Unterstützung.

## Warum muss ich für den vollen Funktionsumfang des Berichtswesens extra bezahlen?

Das alte Berichtsmodul ist technisch veraltet und kann die hohen Datenanforderungen nicht mehr bewältigen, was oft zu Systemverlangsamungen führt. Zudem wird es nicht mehr aktiv gewartet. Ein Teil des alten Systems wird durch eine neue API ersetzt, die besser auf eure Bedürfnisse abgestimmt ist. Für das neue, leistungsfähigere Berichtswesen (basierend auf gänzlich neuer Infrastruktur) erheben wir deshalb eine zusätzliche Gebühr, um den langfristigen Betrieb zu sichern.

Neben neuer Infrastruktur und aktiver Wartung bietet das Modul allen Kunden die Möglichkeit, moderne no-code Berichte zu erstellen, einen vollständigen SQL Editor zu nutzen sowie auf zuverlässige, durchdachte Berichtsvorlagen zuzugreifen.

## Wie geht es mit dem alten legacy Berichtemodul weiter?

Das alte Berichtemodul bleibt bis zum Jahresende 2024 unverändert. Ab Januar 2025 werden wir erste Einschränkungen vornehmen, um den Verkehr auf diesem Modul langsam runter zu fahren (es können keine neuen Berichte mehr angelegt werden, auf bestehende Berichte kann nur noch lesend zugegriffen werden). Aktuell ist geplant, das Modul Ende Juni 2025 zu sunsetten. Wir empfehlen, dass du dich frühzeitig mit dem neuen Berichtswesen (oder alternativ der API) vertraut machst, um in Q2 2025 nicht unnötig unter Druck zu geraten.

## Warum werden die Aufträge die ich soeben in Xentral importiert habe nicht auf den Dashboards angezeigt? Warum tauchen sie nicht in den Berichten auf?

Die komplette Infrastruktur, die für das neue Berichtswesen verwendet wird, befindet sich außerhalb deiner XentralInstanz. Dort werden alle Daten gebündelt und können effizient abgerufen werden ohne Last auf deiner eigenen Datenbank zu erzeugen. Deshalb müssen die Daten regelmäßig zwischen deiner Datenbank und unserer Analytics Platform synchronisiert werden. Das geschieht im Regelfall einmal am Tag zwischen 22 Uhr abends und 4 Uhr morgens. Aufträge oder andere Daten, die du im Laufe des Tages einspielst, sind deshalb erst am nächsten Tag zu sehen.

## Warum sehe ich am Anfang des Monats keine Daten?

Wir synchronisieren die Daten nachts zwischen deiner XentralDatenbank und unserer Analytics Platform, dem Motor, der das gesamte neue XentralBerichtswesen antreibt. Siehe hierzu “Warum werden die Aufträge die ich soeben in Xentral importiert habe nicht auf den Dashboards angezeigt? Warum tauchen sie nicht in den Berichten auf?”. Das bedeutet zum Beispiel, dass am 1. eines jeden Monats in der Regel noch keine Daten für den aktuellen Monat zur Verfügung stehen. Wenn du dann die Verkaufszahlen des aktuellen Monats mit dem vorherigen Monat vergleichen willst, geht das in der Regel erst am nächsten Tag.

## Ich verwende Berichte zur Steuerung operativer Prozesse und benötige eine Echtzeit-Synchronisation der Daten. Bietet Xentral das an?

Für die Synchronisation in Nahe-Echtzeit bieten wir den Unlimited Plan an. Wir prüfen hierzu deine Anforderungen an Synchronisationsintervalle (stündlich bis nahe-Echtzeit), Datenvolumina sowie Komplexität der Abfragen und leiten daraus die zusätzlichen Infrastrukturkosten ab. Bitte habe Verständnis dafür, dass wir diese direkt an dich weiter verrechnen müssen.

## Warum werden mir auf einer bestimmten Komponente eines Dashboards keine Daten angezeigt?

Wenn der Rest der Metriken auf dem Dashboard aktuell ist, dann liegt das mit ziemlicher Wahrscheinlichkeit daran, dass du die notwendigen Daten für diese Metrik nicht in Xentral eingepflegt hast oder für den ausgewählten Zeitraum keine Daten vorliegen. Im Allgemeinen gilt: Je mehr Daten wir über dein Business haben, desto mehr und bessere Analysen können wir dir bieten. Um mehr Informationen zu den einzelnen Metriken zu erhalten, kannst du mit dem Mauszeiger über des Fragezeichensymbol am rechten oberen Rand der Metrik fahren. In den Tooltips findest du Hinweise darüber, wie wir die Metrik berechnen und was wir dafür für Daten benötigen.

Wenn du unser Premium Add-on erworben hast, stehen dir viele Filteroptionen zur Verfügung. Versuche auch die Zeitintervalle zu ändern. Eventuell liegen für den ausgewählten Zeitraum keine Daten vor.

Wenn du ein Neukunde bist, ist es wichtig zu verstehen, dass wir gerade für die Lageranalyse erst einmal Daten von dir über einige Zeit sammeln müssen, um dir gewisse Metriken anzeigen zu können.

## Warum kann ich Spalte/Tabelle xyz nicht im Datenmodell finden?

Um die Komplexität im neuen Datenmodell gering zu halten, haben wir erstmal nur bestimmte Tabellen bereitgestellt (nämlich die, die notwendig waren, um 98% der 13.200 custom reports nachzubauen).

Weitere Tabellen und Felder können auf Kundenanfrage jederzeit von uns hinzugefügt werden, sofern diese für das Berichtswesen benötigt werden (und nicht etwa nur Funktionalität der noch fehlenden XentralAPI Endpunkte abdecken).

## Warum kann ich nur 5 Zeilen sehen?

Du befindest dich im Vorschau-Modus. Dieser dient hauptsächlich zu Test- und Entwicklungszwecken. Du kannst die Inhalte der Berichte prüfen oder testweise eigene Berichte entwickeln, ohne dir Sorgen zu machen, dass sofort Kosten verursacht werden. Es werden dir jedoch immer nur die ersten 5 Zeilen des Ergebnisses angezeigt.

## Was ist mit der Tabelle “artikelbaum_artikel” passiert?

Diese Tabelle wurde zur besseren Nutzbarkeit in die Tabelle product_trees integriert.

## Geldbeträge in Berichten: System- und Originalwährung

Im neuen Berichtemodul werden Geldbeträge standardmäßig in deiner Systemwährung angezeigt (standardmäßig EUR). Das erleichtert Analysen, da Beträge über alle Einträge hinweg direkt aggregiert werden können, ohne dass eine manuelle Umrechnung nötig ist.

Xentral speichert die Währung eines Eintrags jedoch auch explizit. Wenn du Geldwerte in der Originalwährung sehen möchtest, kannst du auf die untransformierten Felder **xen_***in den relevanten Tabellen zugreifen (z. B. ** xen_net_revenue ** oder **xen_net_profit in invoices ** oder **sales_orders **). Das Feld ** original_currency**zeigt dabei an, in welcher Währung der Betrag ursprünglich erfasst wurde.

Beispiel:

```SELECT net_revenue AS “Revenue in EUR”, xen_net_revenue AS “Revenue in original currency”, original_currency AS “Original currency” FROM invoices;```

Damit kannst du sowohl in der standardisierten Systemwährung arbeiten als auch die Rohdaten aus dem Beleg abrufen.

In Tabellen, die das Feld **original_currency ** nicht haben, gibt es keine**xen_***Felder, da dort standardmäßig keine Euro-Transformationen vorgenommen werden. Alle Geld-Spalten sind hier immer in der Originalwährung. Ein Beispiel hierfür ist die Tabelle ** products**.

## Das Laden der exportierten Daten nach Excel funktioniert nicht. Was kann ich tun?

Exportierte Daten werden im Standardformat CSV bereitgestellt. In den Berichtseinstellungen lässt sich festlegen, welches Trennzeichen verwendet werden soll. Probleme beim CSV-Export und dem Import in Excel treten häufig auf, wenn das gewählte Trennzeichen auch innerhalb der Datenwerte vorkommt.

Ein Artikelname wie „Schraube, M3“ kann beispielsweise zu Formatierungsfehlern führen, wenn ein Komma (,) als Trennzeichen verwendet wird.

Zur Lösung des Problems kann entweder ein alternatives Trennzeichen gewählt oder die Datenwerte in der SQL-Abfrage bereinigt werden, z. B. mit der Funktion REPLACE.

## Wie sind die numerischen Ergebnisse formatiert?

Im neuen Berichtswesen werden Zahlen in den Ergebnistabellen standardmäßig ohne Tausendertrennzeichen und mit Punkt (.) als Dezimaltrennzeichen dargestellt.

Beispiele:

- Eintausend wird als **1000.00** ausgegeben.
- Zehntausendfünfhundert als **10500.00**.

Felder mit dem Typ „numeric“ im Datenkatalog sind standardmäßig auf sechs Nachkommastellen gerundet (z. B. 123.456789).

Falls ein anderes Zahlenformat erforderlich ist – beispielsweise eine bestimmte Anzahl von Nachkommastellen, Tausendertrennzeichen oder ein Komma als Dezimaltrennzeichen – kann dies direkt im SQL-Ausdruck angepasst werden.

Beispiel für Redshift:

Soll das Feld **net_price** auf zwei Nachkommastellen gerundet und gleichzeitig mit Tausenderpunkten sowie Komma als Dezimaltrennzeichen ausgegeben werden, kann in Redshift folgender Ausdruck verwendet werden:

```REPLACE(REPLACE(REPLACE(TO_CHAR(net_price, 'FM999G999G999D00'), ',', '#'), '.', ','), '#', '.')```

> **Anmerkung**
>
> Bei dieser Formatierung darf der numerische Wert im Feld net_price maximal neun Stellen vor dem Komma enthalten.

Erklärung der Bestandteile:

- **TO_CHAR(...)** formatiert den numerischen Wert
- '**FM**' unterdrückt führende Leerzeichen
- '**G**' steht für das Tausendertrennzeichen
- '**D**' steht für das Dezimaltrennzeichen
- **REPLACE(..., '.', ',')** ersetzt den Punkt durch ein Komma

## Was muss ich beim neuen SQL-Dialekt beachten?

Das alte Modul verwendete MySQL, um Berichte zu erstellen.

Im neuen Berichtswesen wird der SQL-Dialekt von Amazon Redshift verwendet, der wiederum eine leicht abgewandelte Form von PostgreSQL ist. Die wichtigsten Änderungen im Überblick:

- **Primärschlüssel-Benennung **: Es gibt keine generischen id-Felder mehr. Der Primärschlüssel einer Tabelle heißt nun**{tabellenname_im_singular}_id **. Beispiel: ** invoice_id ** anstelle einfach **id ** in der Tabelle **invoices**.
- **JOINS werden eindeutiger**: Durch die geänderte Benennung der IDs sind JOINs nun meist symmetrisch aufgebaut:
  Es gibt jedoch wenige Ausnahmen von dieser Regel.

- **Frühestes Datum **: Anstelle von '** 0000-00-00 **' im legacy Modul ist das frühestmögliche Datum nun '** 0001-01-01**'.
- **Booleans **: Boolean-Felder sind nun echte Booleans** (TRUE/FALSE)** und nicht mehr ** 0** oder ** 1**. Beispiel: ** artikel.geloescht = 0 ** wird zu**products.is_deleted = FALSE **. Alle Boolean-Felder beginnen mit ** is_**oder ** has_**.
- **GROUP BY Verhalten **: Redshift folgt dem ANSI-SQL-Standard. Das bedeutet: Alle nicht-aggregierten Spalten müssen in der ** GROUP BY**

-Klausel enthalten sein. Die MySQL-Einstellungen im legacy Modul waren hier weniger streng, was zu inkonsistenten Ergebnissen führen konnte.
- **Groß-/Kleinschreibung **: In MySQL ist die ** WHERE **

-Klausel standardmäßig case-insensitive. In Redshift hingegen müssen Filter exakt dem Wert im Datensatz entsprechen. Beispiel: ** WHERE groups.group_type = 'Gruppe'** funktioniert nicht, wenn der Eintrag **gruppe** lautet.