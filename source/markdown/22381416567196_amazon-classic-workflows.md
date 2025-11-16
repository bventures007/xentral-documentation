### Artikel importieren

#### Amazon Schnittstelle

Wenn du die XentralAmazon Schnittstelle zum Importieren von Aufträgen verwendest, werden Artikel nur mit Name (Titel) und Nummer importiert.

#### Amazon SellerApp

Wenn du die XentralAmazon SellerApp zusätzlich verwendest, können folgende Informationen zusätzlich importiert werden:

'Publisher', 'Studio', 'ProductGroup', 'ProductTypeName', 'Size', 'Color', 'Manufacturer', 'Label', 'Model', 'NumberOfItems', 'Brand'. Es wird zusätzlich noch ein Minibild als Gruppenbild importiert.

Wenn du eine Preisgruppe in der Shopschnittstelle angegeben hast, wird der Artikelpreis als Gruppenpreis importiert. Dies funktioniert jedoch nur, wenn du auf einem Marktplatz verkaufst.

Sobald die Amazon Schnittstelle initialisiert ist, du den Artikel mit der Schnittstelle verknüpft hast und du die Amazon Seller-App besitzt, wird ein neuer Lagerort namens "Amazon" angelegt. Dort werden die Bestände der FBA-Artikel via API ins System geladen.

> **Anmerkung**
>
> Damit die Schnittstelle vollständig initialisiert werden kann, musst du den Importmodus auf manueller Import einstellen.

Einige Shop-Schnittstellen erlauben dir einen Import der Artikel aus deinem Shop zu xentral über die Aktion **Artikelliste abholen** unter Schnittstellen. Shopartikel, die bereits in xentral vorhanden waren, werden aktualisiert, fehlende Artikel werden angelegt. Die Artikel werden nach dem Ausführen der Aktion nach und nach vom Prozessstarter[Artikelimport](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a)abgeholt.

Einen einzelnen Artikel kannst du in den Stammdaten des Artikels unter **Details > Online Shop Optionen** importieren. Das ist hilfreich um diesen zu aktualisieren, wenn Daten im Shop geändert wurden.

![Online-Shops-17.png](https://help.xentral.com/hc/article_attachments/22381431639196)

Damit der richtige Artikel aus dem Shop zugeordnet wird, musst du die[Fremdnummer](https://help.xentral.com/hc/de/articles/360016758199#UUID-be6a2725-3071-98cf-ad2e-1a9016c503cc)bereits verknüpft haben.

> **Anmerkung**
>
> Es kann immer nur ein Shopartikel einem Lagerartikel zugeordnet werden. Soll z.B. eine Unisex Sonnenbrille im Shop eigene Einträge als Frauen und Männer Sonnenbrille erhalten, kann der hier beschriebene Workaround genutzt werden.

### Artikel exportieren

Die Artikelübertragung exportiert Artikel mitsamt der gepflegten Daten an den Shop. Exportiert werden u.a. die Online-Shop-Texte, Standardpreis, Gewichte, Abverkauf usw.

Für den automatischen Export von Artikeln zu einem Online-Shop gibt es den Prozessstarter[artikeluebertragen](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a). Dieser überträgt alle zum Shop verknüpften Artikel nach und nach im Hintergrund, wenn der Export in der Schnittstellen über den Bereich "Artikel Übertragung" angestoßen wurde. Wurde ein Artikel verändert, kannst du im Artikelstamm (**Stammdaten > Artikel >* Artikel auswählen***) unter ** Details > Online Shop Optionen**auch direkt per Knopfdruck in den Shop exportiert werden.

> **Anmerkung**
>
> Beim Export von (JIT-)Stücklisten darf nur der Kopfartikel an den Shop übertragen werden. Die einzelnen Bestandteile der (JIT-)Stückliste werden dann beim Import des Auftrags wieder in Xentral ergänzt. Falls du die einzelnen Bestandteile auch im Shop anzeigen möchtest, kannst du diese in der Artikelbeschreibung eintragen.

![Online-Shops-18.png](https://help.xentral.com/hc/article_attachments/22381468950684)

Willst du nur die Lagerzahlen der Artikel übertragen, da alle anderen Artikeldaten im Shop gepflegt werden, solltest du die Option "Artikel Übertragung erlauben" nicht setzen, sondern nur die Option "Lagerzahlen Übertragen erlauben".

### Lagerzahlen synchronisieren

Beim Lagerzahlenabgleich zu Amazon gibt es eine Besonderheit. Du musst alle Fremdnummern in den Artikeln pflegen, da die Amazon-Schnittstelle diese in einer Liste sammelt und die Lagerzahlen aller Artikel auf einmal überträgt. Hier könnte es also passieren, dass die ganze Liste nicht aktualisiert wird, wenn die Fremdnummer eines Artikels fehlt.

Beachte, dass sich Reservierungen, die auf einen Artikel vorgenommen werden, auf den gemeldeten Lagerbestand auswirken.

#### Lagerzahlen Übertragung erlauben

Um den Lagerbestand der Artikel automatisch an den Shop zurückzumelden, musst du die Option "Lagerzahlen Übertragung erlauben" aktivieren. Die Lagerzahl wird z.B. auch neu gemeldet, wenn du einen Auftrag mit einem Artikel anlegst. Dieser Artikel wird dann vom Bestand, der gekauft werden kann, weggerechnet.

Die automatische Meldung der Lagerzahlen an den Shop erfolgt, wenn der Prozessstarter[lagerzahlen](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a)aktiv ist und ausgeführt wird.

Damit die Übertragung der Lagerzahlen möglichst wenige Ressourcen beansprucht, wird diese nicht jedes mal für alle Artikel durchgeführt. Nur Artikel, die seit ihrer letzten Synchronisation eingelagert, ausgelagert oder in einen Auftrag eingefügt werden, werden neu synchronisiert, wenn der Prozessstarter durchläuft. Zur Sicherheit werden zusätzlich alle 12 Stunden die Lagerbestände aller Artikel noch einmal synchronisiert.

Mit der Einstellung Lager Grundlage unter Details > Einstellungen definierst du, wie sich der "Bestand", der an deinen Shop zurückgemeldet werden soll, zusammensetzen soll:

Anhand "Artikel verkaufbare": Es wird der "berechnete Bestand" im Artikel an den Onlineshop zurückgemeldet

Anhand "Lagerbestand minus Reservierungen": Es wird der Lagerbestand minus der reservierten Aufträge zurückgemeldet (offene nicht reservierte Aufträge werden nicht berücksichtigt)

#### Lagerkorrektur überschreiben

Aktivierst du diese Option, kann der Lagerkorrekturwert global für alle Artikel in diesem Shop einstellen. Den Lagerkorrekturwert musst du dann nicht mehr pro Artikel im Artikelstamm pflegen. Der eingestellte Lagerkorrekturwert im Artikelstamm des Artikels wird von diesem Wert überschrieben.

#### Vorraussetzungen für den Lagerzahlensync

- In der Shop-Schnittstelle > Einstellungen muss die Option "Lagerzahlen Übertragung erlauben" aktiviert sein
- Im Artikel > Online-Shop Optionen muss die Option "Lagerzahlen Sync." aktiviert sein & der Artikel mit dem Shop verknüpft sein **Manuell übertragen: ** Wenn die Lagerzahl eines einzelnen Artikels übertragen werden sollen, musst du unter Artikel > Online-Shop Optionen gehen und auf die Schaltfläche "Export" klicken ** Automatisch übertragen:** Wenn es automatisch gehen soll, musst du den Prozessstarter "lagerzahlen" aktivieren (ideal 5 oder 10 Minuten). Dann wird zyklisch der Wert im Shop angepasst bei Lagerdifferenzen zwischen Xentral und dem Shop.

Allgemeine Informationen zu Prozessstartern findest du[hier](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a)und Informationen zum Zeitpunkt des Lagerzahlensyncs unter[diesem Link](https://help.xentral.com/hc/de/articles/18567521362332#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

> **Anmerkung**
>
> Im Bezug zum Lagersync:
>
> - Die Bestandsänderung muss auf Xentral-Seite passieren
> - Xentral merkt sich, was das letzte mal an den Shop gemeldet wurde
> - Wenn sich hieraus eine Änderung im Lagerbestand ergeben hat, werden genau diese Artikel übertragen
> - Eine alleinige Änderung im Shop löst noch keine Bestandsänderung in xentral aus, eine Bestandsänderung in Xentral löst aber eine Rückmeldung zum Shop aus (sofern keine Pseudo-Lagerzahlen als Bestand verwendet werden)

Durch Betätigung der Schaltfläche Lagerzahlen zurücksetzen kannst du die zuletzt gespeicherten Bestandswerte löschen. Im Anschluss holt der Cronjob "lagerzahlen" erneut alle neuen Bestände ab und meldet diese an den Shop zurück.

### Aufträge importieren

> **Anmerkung**
>
> Im Demo-Modus werden Lagerzahlen bzw. Auftragsdaten nicht gesendet und keine Rechnungen hochgeladen. VAT-Reports und Inventory-Reports werden hingegen abgeholt.

In folgendem DropDown-Menü siehst du, welche verschiedenen Import-Modi zur Verfügung stehen.

![Amazon-13.png](https://help.xentral.com/hc/article_attachments/22381468951068)

Zum Test der Abholung empfehlen wir den "Demo-Modus", da hier lediglich der letzte Auftrag abgeholt und dabei der Status bei Amazon nicht umgestellt wird.

Im Anschluss musst du nur noch auf die Schaltfläche **Aufträge abholen** klicken. Solltest du die Option "Aufträge in Zwischentabelle" gewählt haben, dann wird dir im Anschluss an den Abholvorgang eine Zwischentabelle angezeigt, in der du den Import nochmals bestätigen, abbrechen oder auf später verschieben kannst. Ansonsten wird der Auftrag direkt in die Auftragsübersicht unter Verkauf > Auftrag eingespielt.

Du hast auch die Möglichkeit das Startabholdatum manuell über eine Schaltfläche auf "gestern" zurückzustellen wenn die Schnittstelle warnt, dass das Start Abholdatum weit zurückliegt.

![Amazon-14.png](https://help.xentral.com/hc/article_attachments/22381431640732)

#### Importierte Auftragsstatus

Aufträge mit folgenden Auftragsstatus lassen sich von Amazon abholen, wenn FBM versendet wird:

- unfulfilled
- partially fulfilled

Alle anderen Auftragsstatus werden derzeit ignoriert und nicht importiert. Wenn es sich um FBA Aufträge handelt, holen wir jeden Status ab.

#### Aufträge importieren

Die Shopschnittstelle von Xentral erlaubt einen manuellen oder automatischen Auftragsimport vom Shop zu Xentral. Zudem gibt es einen Modus "Demo (Zum Testen)", bei dem der Auftragsstatus im Shop nicht umgestellt und keine Artikel oder Lagerzahlen übertragen werden.

Um Aufträge manuell zu importieren wählst du zunächst unter Details > Schnittstelle den Import-Modus aus und benutzt anschließend die Schaltfläche **Aufträge abholen**.

Beim Import werden automatisch die neuen Aufträge auf bestehende Kunden gebucht, bzw. neue Kunden angelegt. Anhand der farblichen Markierung in der Shopimport Zwischentabelle ist erkennbar, ob ein Kunde bereits in der Datenbank existiert, oder ein ähnlicher Kunde gefunden wurde, dessen E-Mail-Adresse mit einem importierten Auftrag übereinstimmt.

Ein Kunde wird beim Import als vorhanden erkannt (grüne Markierung), wenn folgende Datenfelder übereinstimmen:

- Name
- E-Mail-Adresse
- Abteilung
- Strasse
- PLZ
- Ort

Wenn nur eines der folgenden Datenfelder übereinstimmt, ist eine manuelle Prüfung der Verknüpfung notwendig (lila Markierung):

- Name, oder
- E-Mail

In der Zwischentabelle kannst du entscheiden, ob du die Aufträge direkt importieren, später importieren oder auf den Müll legen willst.

![Online-Shops-24.png](https://help.xentral.com/hc/article_attachments/22381468952348)

- Grün > eindeutig gefunden > die Daten sind identisch zu den in den Stammdaten gespeicherten Werten
- Lila > Kunde anhand der Mail Adresse gefunden, allerdings hat der Kunde eine andere Adresse eingegeben (zumindest liegt eine Abweichung vor)
- Rot > Der Kunde hat seine Kundennummer im Shop eingegeben (sofern der Shop das unterstützt) > diese Nummer sollte ggf. manuell geprüft werden
- Rote Shopbestellnummer > Der Auftrag wurde bereits abgeholt, in diesem Fall steht der Auftrag auf "später"

Der Auftragsimport aus dem Shop kann auch automatisch per Prozessstarter erfolgen.

Hierfür muss der Prozessstarter **shopimport ** aktiv sein und der Import-Modus der Shopschnittstelle muss auf**Automatisch (per Prozessstarter)** eingestellt sein.

Eine ausführliche Anleitung für den Import von Aufträgen aus dem Online Shop befindet sich[hier](https://help.xentral.com/document/preview/42498#UUID-261d26b3-4119-fdc4-df27-ba7054e67b4b).

Beim Abholen von älteren Aufträgen kann es passieren, dass nicht alle Aufträge importiert werden können.

> **Anmerkung**
>
> Alte Aufträge können nur importiert werden, wenn sie max. 89 Tage vor dem aktuellen Datum liegen.