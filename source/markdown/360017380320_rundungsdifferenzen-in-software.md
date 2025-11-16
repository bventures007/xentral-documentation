Dieser Artikel behandelt Rundungsdifferenzen in einer Software. Nachstehend wird erläutert, wie Rundungsdifferenzen entstehen können und warum es schwierig ist, eine einheitliche Lösung zu finden.

## Verschiedene Berechnungsmethoden für die Steuer

Der Hauptgrund für Rundungsdifferenzen sind die unterschiedlichen Methoden für die Addition der Mehrwertsteuer in den Belegpostionen. Es gibt zwei Methoden, die gesetzlich anerkannt sind.

### Variante 1: Spaltenweise (vertikale) Berechnung

Um spaltenweise zu berechnen, bestimme zunächst die Nettosumme pro Steuersatz für die gesamte Rechnung. Multipliziere dann die Nettosumme mit dem entsprechenden Steuersatz. Die Mehrwertsteuersumme wird auf der Rechnung pro Steuersatz getrennt ausgewiesen.

Bespiel: Es wird eine Kundenrechnung mit 3 Artikelzeilen ausgestellt. Jeder Artikel kostet netto 0,99 EUR. Der Steuersatz beträgt 19%.

1. Berechne die Nettosumme der Artikel: 0,99 EUR x 3 = 2,97 EUR
1. Multipliziere mit dem Steuersatz: 2,97 x 1,19 = 3,5343 EUR
1. Ergebnis mit Rundung: 3,53 EUR

Berechnung: (0,99 EUR x 3) x 1,19 = 2,97 EUR x 1,19 = 3,5343 EUR = 3,53 EUR

### Variante 2: Zeilenweise (horizontale) Berechnung

In diesem Fall wird für jede einzelne Artikelzeile die Mehrwertsteuer, unter Verwendung des entsprechenden Steuersatzes, berechnet. Die Summe ergibt sich als Summe aller einzelnen Artikelzeilen. Die Mehrwertsteuer wird auch hier auf der Rechnung pro Steuersatz getrennt ausgewiesen.

Bespiel:Es wird eine Kundenrechnung mit 3 Artikelzeilen ausgestellt. Jeder Artikel kostet netto 0,99 EUR. Der Steuersatz beträgt 19%.

1. Multipliziere den Steuersatz mit jedem einzelnen Artikel: 0,99 EUR x 1,19 = 1,1781 EUR
1. Durch Rundung erhält man 1,18 EUR pro Artikel
1. Berechne die Summe aller Artikel mit Steuer: 1,18 EUR x 3 = 3,54 EUR

Berechnung: (0,99 EUR x 1,19) x 3 = 1,18 EUR x 3 = 3,54 EUR

### Differenz bei der Berechnung in den Beispielen

Je nach Berechnungsmethode, ergibt sich eine Rundungsdifferenz von 0,01 EUR. Das zeigt, dass Beträge mit Nachkommastellen ggf. zu Rundungsdifferenzen führen können.

## Übernahme von Bestellungen aus dem Shop

Auch bei bekannten Online-Shops gibt es Rundungsfehler. Wenn in Verbindung mit einem ERP-System gearbeitet wird, ist es denkbar, dass der Shop an sich bereits Rundungsfehler erstellt hat. In diesem Fall ist es möglich, dass der Kunde die Belegsumme des Shops bereits bezahlt hat. xentral würde die gerundeten Zahlen übernehmen und entsprechend weiterverarbeiten, um zu vermeiden, dass weitere Rundungsdifferenzen entstehen.

## Sehr kleine Preise

Manche Branchen geben Preise unterhalb eines Cents an. Daher können bei der Arbeit mit zu kleinen Preisen ebenfalls Rundungsdifferenzen enstehen. Daher bilder xentral sehr viele Nachkommastellen ab. Dennoch können auch in xentral durch die Multiplikation mit Mengen Rundungsfehler entstehen.

## Vorgehen bei Rundungsdifferenzen

Wenn Rundungsdifferenzen beim Zahlungsimport entstehen, sollten diese beseitigt werden. Das ist v.a. bei einem hohen Auftragsaufkommen wichtig. Dazu ist im Shop-System zu prüfen, zu welchem Zeitpunkt diese Differenzen auftreten.

### Entfernen von Rundungsdifferenzen

Teilweise ist es unvermeidbar, dass Differenzen in die Steuersoftware übernommen werden. Daher sind diese in der Software auf ein entsprechendes Konto zu buchen. Wichtig ist, dass sich die Rundungsbeträge im Cent Bereich bewegen. Andernfalls ist der Ursprung für größere Differenzen herauszufinden.