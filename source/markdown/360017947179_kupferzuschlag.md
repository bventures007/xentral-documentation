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

Das Modul Kupferzuschlag wurde in Xentral Version 21.5 entfernt und steht somit ab der Version 21.5 nicht mehr zur Verfügung.

Zu finden unter **App Center > Stammdaten > Kupferzuschlag **. Das Modul dient dazu, Extrapositionen zu Belegen hinzuzufügen, welche einen Kupferanteil haben. Die Einkaufspreise dieser zusätzlichen Artikel können dann über die App ** Tagespreise**gepflegt werden.

## Einrichtung

Im Modul werden folgende Werte gepflegt:

- **Kupferzuschlagsartikel:** Ein Artikel, welcher dann als zusätzliche Position hinzugefügt wird
- **Position einfügen:** Hier ist auszuwählen, wie die Zuschlagsartikel in einem Beleg ergänzt werden sollen
- **Kupferzuschlag - Angebot zu Auftrag:** Der Kupferkurs zu einem bestimmten Datum ist hier für den Kupferzuschlag einzupflegen
- **Kupferzuschlag Rechnung erstellen:** Hier ist auszuwählen, welches Datum des Kupferkurses für die Rechnung gesetzt werden soll
- **Wie sollen die Daten gespeichert werden?: ** Hier ist entweder das Feld ** mit der App Rohstoffliste **oder das Feld ** mit Artikelzusatzfeldern** auszuwählen um einen Artikel als Kupferartikel zu kennzeichnen
- **Bezugskosten:** Die Bezugskosten sind in % anzugeben
- **Standard Kupferbasis:** Der Preis für die Standard Kupferbasis ist in EUR pro 100kg einzufügen
- **Artikelspezifische Kupferbasis: ** Der Preis der artikelspezifischen Kupferbasis ist in EUR pro 100kg einzupflegen ** Position einfügen**

Es gibt drei Möglichkeiten, wie die Zuschlagsartikel in einem Beleg ergänzt werden können:

1. **Pro Position eine Kupferzuschlagsposition einfügen:** Für jeden Artikel im Beleg, der als Kupferartikel gekennzeichnet ist, wird ein Kupferzuschlagsartikel hinzugefügt
1. **Nur eine Sammelposition einfügen:** Der Kupferzuschlag aller Kupferartikel wird aufsummiert und in einer Position hinzugefügt. Diese Position steht immer am Ende der Positionen
1. **Pro Gruppe eine Kupferzuschlagsposition einfügen: ** Pro Gruppe werden alle Kupferzuschläge aufsummiert und immer am Ende der Gruppe als Position eingefügt ** Kupferzuschlag - Angebot zu Auftrag**

Es gibt zwei Auswahlmöglichkeiten:

1. **Kupferkurs vom Angebotsdatum:** Wenn ein Auftrag aus einem Angebot weitergeführt wurde, wird das Datum dieses Angebots als Grundlage verwendet. Sonst das Auftragsdatum
1. **Kupferkurs vom Auftragsdatum: ** Es wird immer das Auftragsdatum verwendet ** Kupferzuschlag Rechnung erstellen**

Es gibt vier Auswahlmöglichkeiten, welches Datum als Grundlage verwendet werden kann:

1. **Kupferkurs vom Auftragsdatum:** Hier wird das Datum des Auftrags gewählt. Wenn dieses nicht vorhanden ist, ist das aktuelle Datum zu setzen
1. **Kupferkurs vom Lieferschein/Lieferdatum:** Hier ist das Lieferdatum zu wählen. Wenn dieses nicht vorhanden ist, ist das aktuelle Datum zu verwenden
1. **Kupferkurs vom Rechnungsdatum (taggenau):** Es ist das Datum der Rechnung einzugeben
1. **Kupferkurs vom Angebotsdatum: ** Das Datum des Angebots ist zu wählen. Wenn dieses nicht vorhanden ist, ist das aktuelle Datum zu verwenden ** Wie sollen die Daten gespeichert werden?**

Es gibt zwei Möglichkeiten, wie ein Artikel als Kupferartikel gekennzeichnet werden kann. Entweder kann dafür zusätzlich die Rohstoff-App verwendet werden oder ein weiteres Artikelzusatzfeld für die Artikelspezifische Kupferzahl:

- **Artikelspezifische Kupferzahl (kg/km):** Dieses Feld erscheint nur, wenn vorher die Pflege der Daten per Artikelzusatzfelder ausgewählt wurde
- **Bezugskosten (in %):** Die derzeitige Berechnungsgrundlage beinhaltet immer einen Bezugskostenzuschlag. Dieser ist derzeit mit 1% voreingestellt und kann hier für alle Zuschlagspositionen geändert werden
- **Standard Kupferbasis (in EUR pro 100kg):** Auch dieser Wert kommt in der Berechnungsgrundlage vor und kann hier für alle Artikel geändert werden
- **Artikelspezifische Kupferbasis (in EUR pro 100kg):** Falls für spezielle Artikel die Kupferbasis geändert werden soll, kann hier das Freifeld ausgewählt werden, welches dann im Artikel ausgefüllt werden kann

## Kupferzuschlagsartikel erstellen

Die zusätzlichen Zuschlagspositionen benötigen einen Artikel als Grundlage. Dafür wird ein neuer Artikel angelegt. Dieser Artikel muss dann im Bereich **Varianten ** als Tagespreisartikel markiert werden, d.h. Haken bei**Tagespreise**.

Im Feld **Artikelbeschreibung(DE)** werden noch folgende Variablen erkannt und bei Verwendung ersetzt: {ARTIKELNUMMER}, {ARTIKELNAME}, {NETPRICE} der Nettopreis des Zuschlags, {COPPERBASIS} die Kupferbasis (siehe Berechnungsgrundlage), {COPPERNUMBER} das Kupfergewicht (kg/km) (siehe Berechnungsgrundlage), {DELVALUE} der verwendete Tagespreis

![coppersurcharge_1.png](https://help.xentral.com/hc/article_attachments/5091171999004)

### Artikel als Kupferartikel markieren

Damit ein Artikel als Kupferartikel erkannt wird, muss dieser entweder als Rohstofflistenartikel markiert werden oder das zusätzliche Freifeld für das Kupfergewicht (kg/km) ausgefüllt werden. Dies richtet sich je nach der Auswahl im Modul. Falls die Rohstoffliste verwendet wird, muss im Reiter Rohstoffe eine neue Position hinzugefügt werden. Hier soll der Zuschlagsartikel als **Artikel ** verwendet werden und**Menge** als Kupfergewicht (kg/km).

![coppersurcharge_2.png](https://help.xentral.com/hc/article_attachments/5091280162844)

### Markierung als Rohstoff

![coppersurcharge_3.png](https://help.xentral.com/hc/article_attachments/5091186816540)

Im jeweiligen **Artikel ** ist im Bereich **Stückliste ** ein Haken bei**Rohstoffliste** zu setzen.

### Verwendung von Zusatzfeldern

Hier können weitere Informationen wie die artikelspezifische Kupferbasis und die Kupferzahl in km/kg als Zusatzfelder eingegeben werden.

## Tagespreise

Im Modul **Tagespreise ** im Reiter **Konfiguration ** ist für einen der sieben Artikel wieder der Kupferzuschlagsartikel auszuwählen und ein Spaltenname, z.B. **Kupferzuschlag,** zu vergeben.

![coppersurcharge_4.png](https://help.xentral.com/hc/article_attachments/5091267900444)

Im Reiter **Übersicht** kann, uneingeschränkt oft, ein neuer Preis eingetragen werden.

![coppersurcharge_5.png](https://help.xentral.com/hc/article_attachments/5091263986716)

Sobald ein neuer Preis gespeichert wird, wird im alten das Gültigkeitsdatum auf gestern gesetzt und ein neuer Einkaufspreis hinzugefügt.

Als Berechnungsgrundlage dient folgende Formel:

Kupferzuschlag EUR/km = (Kupfergewicht (kg/km) * (DEL + 1% Bezugskosten)) - Kupferbasis / 100

DEL ist hier als Deutsche Elektrolyt-Kupfer-Notierung für Leitmaterial zu verstehen.

Ein Beispiel:

Kupfergewicht/km: 13,00 kg Kupferbasis: 150,00 EUR/100 kg DEL: 550,00 EUR/100 kg

13 *((550,00 + (550,00* 0.01)) - 150,00) / 100 = 52,72 EUR/km