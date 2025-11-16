Sobald du die[vorbereitenden Einstellungen](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc)vorgenommen und[eine Übertragung angelegt](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt5bertragungen-Accountanlegen)hast, läuft der Datenaustausch zwischen deinem XentralSystem und deinem Fulfillment-Dienstleister automatisiert ab. In der Regel musst du dich nur noch in ganz bestimmten Fällen aktiv mit dem Übertragungen Modul beschäftigen. Es kann zum Beispiel zu Fehlern beim Datenaustausch kommen, oder du möchtest ganz einfach den Status der Übertragung oder einzelner Dateien prüfen. All dies und einiges mehr kannst du im Übertragungen Modul tun. Dieser Artikel zeigt dir, welche Informationen du an welcher Stelle einsehen kannst.

## Übertragungen mit dem Monitor überwachen

Der so genannte **Monitor** ist das Allererste, das du siehst, wenn du das Übertragungen Modul in deinem XentralSystem öffnest. Er funktioniert als eine Art Schaltzentrale, der dir den aktuellen Status aller bestehenden Übertragungen zeigt. Für jede einzelne ein- und ausgehende Datei findest du einen separaten Eintrag im Monitor. Dementsprechend findest du hier zahlreiche Einträge. Um trotzdem den Überblick zu behalten, bietet der Monitor einige Filtermöglichkeiten, sodass du relevante Einträge wie zum Beispiel fehlerhafte Übertragungen schnell identifizieren und die notwendigen Maßnahmen ergreifen kannst. Im Folgenden erklären wir, wie du die Filter optimal nutzt.

### Informationen im Monitor filtern

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > Übertragungen (CSV/XML/EDI/PDF)**. * Oder:*Suche mit der Smart Search nach dem Begriff **Übertragungen**.

1. Du befindest dich nun im Monitor. Direkt oberhalb der Übersichtstabelle werden dir verschiedene Filteroptionen angezeigt. Nutze einen oder mehrere der unten beschriebenen Filter, um die Einträge im Monitor nach dem gewünschten Kriterium zu sortieren.

| Filter | Erläuterung |
| --- | --- |
| **Nur Fehler anzeigen **| Klicke auf diesen Filter, um nur Belege anzuzeigen, bei denen Fehler beim Senden oder Empfangen aufgetreten sind. im Falle eines Fehlers wird die Spalte ** Letzter****Status ** rot markiert angezeigt und enthält den Hinweis auf den Fehler. In der Spalte **Meldung** siehst du genauere Informationen zur Fehlerursache. |
| **Lagerzahlen** | Dieser Filter ermöglicht es dir, nur übertragene Lagerzahlen anzuzeigen, die Xentral vom Fremdsystem erreichen. Beachte, dass dieser Filter nur Ergebnisse liefert, wenn entsprechende Übertragungen in deinem System angelegt und aktiviert sind. Weitere Informationen zum Empfang von Lagerbeständen und wie du diesen einrichtest findest du [hier](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0_id_Praxisbeispielefrbertragungen-Lagerbestndeempfangen). |
| **Tracking** | Dieser Filter ermöglicht es dir, nur die Tracking-Informationen anzuzeigen, die vom Fremdsysten an Xentral gemeldet werden. Beachte, dass dieser Filter nur Ergebnisse liefert, wenn entsprechende Übertragungen in deinem System angelegt und aktiviert sind. Weitere Informationen zum Empfang von Tracking-Informationen und wie du diesen einrichtest findest du [hier](https://help.xentral.com/hc/de/articles/16169504579868#UUID-9582360d-b71b-d673-bcb6-d0146d02aaf0_id_Praxisbeispielefrbertragungen-Tracking-Informationenempfangen). |
| **Artikel **/** Aufträge **/** Bestellung **/** andere **| Die vier verbleibenden Filter erlauben dir, nach Artikeln, Aufträgen und Bestellungen zu filtern, die du an deinen Fulfillment-Dienstleister übermittelst. Mit dem Filter ** andere** zeigst du gezielt Datentypen an, die in den anderen Filtern nicht genannt sind. Erwähnenswert sind vor allem die Lieferscheine, die mit diesem Filter angezeigt werden können. Beachte auch bei all diesen Filtern die Bedingung, dass zur Anzeige von Einträgen entsprechende Übertragungen in deinem System eingerichtet und aktiviert sein müssen. Andernfalls bleibt die Ergebnisliste leer. |

### Datenspalten sortieren und durchsuchen

Zusätzlich zu den[oben beschriebenen Filtermöglichkeiten](#UUID-2e4e5ae1-18e2-8825-e29e-b9ecc181152a_id_ArbeitenmitdembertragungenModul-InformationenimMonitorfiltern)kannst du die Inhalte in der Übersichtstabelle nach spezifischen Daten durchsuchen und anordnen. Das funktioniert, indem du rechts an der gewünschten Spaltenüberschrift auf die Pfeil-Symbole klickst und somit die Einträge auf- oder absteigend sortierst. Diese Möglichkeit hast du für sämtliche Spalten der Tabelle - du kannst also sowohl die Einträge in der Spalte **Datum ** entsprechend sortieren als auch die restlichen Angaben zum**Account ** (hier ist die Übertragung gemeint), ** Datei ** (Dateiname im Fremdsystem), ** Datei Xentral ** (Dateiname in Xentral), ** Beleg ** (Belegart), ** Beleg Nr.**, ** Projekt **, ** Letzter Status ** und **Meldung**.

> **Tipp**
>
> Wenn du gezielt fehlerhaften Dateien aller existierenden Übertragungen im Blick behalten möchtest, beachte dazu dieInformationen im vorherigen Kapitelund nutze den dafür vorgesehenen Filter **Nur Fehler anzeigen**.
>
> Suchst du nach ganz bestimmten Fehlermeldungen, Belegarten oder Sonstigem, beispielsweise um Einzelfälle nachzuprüfen? Dann trage die gewünschten Informationen in den Feldern namens **Suche** ein, die direkt unterhalb jeder Spaltenüberschrift angezeigt werden.

## Informationen zu einzelnen Übertragungen einsehen

Um den Status einer bestimmten Übertragung zu prüfen und weitere Informationen einzusehen, navigierst du zum Übertragungen Modul und öffnest dann die gewünschte Übertragung. Gehe dazu wie im Folgenden beschrieben vor.

1. Öffne das Menü **Einstellungen > Administration > Datenaustausch > Übertragungen (CSV/XML/EDI/PDF)**. * Oder:*Suche mit der Smart Search nach dem Begriff **Übertragungen**.

1. Öffne das Tab **Accounts**, um eine Übersicht aller Übertragungen-Accounts zu sehen, die du angelegt hast.
1. Klicke bei der Übertragung, die du prüfen möchtest, auf das Stift-Symbol ganz rechts.

Du befindest dich nun im Tab **Details**, wo du die Einstellungen der Übertragung einsehen und bei Bedarf ändern kannst. Zusätzlich kannst du weitere Tabs sehen und öffnen. Genauere Informationen dazu findest du in den folgenden Kapiteln.

### Events

> **Wichtig**
>
> Dieses Tab ist veraltet und wird künftig aus allen XentralInstanzen entfernt. Das bedeutet, dass es für deine Arbeitsabläufe nicht relevant und in Teilen ohne Funktion ist.

### Nicht freigegeben

In diesem Tab findest du nur Inhalte, wenn du im Tab **Details ** die Option**Manuelle Freigabe erforderlich** aktiviert hast. Ist dies der Fall, wird eine Liste von ausgehenden Belegen angezeigt, die noch nicht an deinen Fulfillment-Dienstleister übertragen wurden. Du musst jeden Beleg mithilfe der entsprechenden Option einzeln freigeben, damit sie an deinen Fulfillment-Dienstleister übermittelt werden.

> **Tipp**
>
> Gut zu wissen: Wir empfehlen, die Option **Manuelle Freigabe erforderlich** bei der Einrichtung der Übertragungen zunächst zu aktivieren. So kannst du die ersten Belege testweise manuell übertragen, um sicherzustellen, dass alles korrekt funktioniert und genau die gewünschten Daten bei deinem Fulfillment-Dienstleister ankommen.

### Zu übertragen

Wenn eine große Anzahl von Belegen gleichzeitig aus deinem XentralSystem übermittelt werden soll, werden die noch nicht übertragenen Belege hier in einer Art Warteschlange dargestellt.

Dies bedeutet jedoch in den meisten Fällen nicht, dass für dich Handlungsbedarf besteht oder du eingreifen musst. Die angezeigten Belege werden nach und nach vom Prozessstarter abgearbeitet und automatisch übertragen. Falls du dir einmal nicht sicher bist, kannst du den Erfolg der Übertragung anschließend[im Tab Übertragen](#UUID-2e4e5ae1-18e2-8825-e29e-b9ecc181152a_id_ArbeitenmitdembertragungenModul-bertragen)oder[im Monitor](#UUID-2e4e5ae1-18e2-8825-e29e-b9ecc181152a_id_ArbeitenmitdembertragungenModul-bertragungenmitdemMonitorberwachen)überprüfen.

> **Wichtig**
>
> Die Anzahl der Belege, die gleichzeitig übertragen werden, bestimmst du selbst mithilfe der Einstellung **Maximal gleichzeitige Übertragungen ** im Tab**Details** der jeweiligen Übertragung. Das Zeitintervall, in dem Belege übertragen werden, legst du in den Einstellungen des Prozesses * api_uebertragungen*fest. Weitere Informationen zum Prozessstarter findest duhier.

### Übertragen

Hier findest du eine Auflistung aller Belege, die von Xentral an ein Fremdsystem übertragen wurden. Dementsprechend verfügt dieser Tab nur über Inhalt, wenn es sich um eine ausgehende Übertragung handelt.

Im Tab **Übertragen** kannst du folgende Aktionen durchführen:

- Zentrale Informationen zu übertragenen Belegen auf einen Blick sehen: Du kannst transparent nachverfolgen, welcher Beleg wann erstellt (Spalte **Vom **) und zu welchem Zeitpunkt die Übertragung stattgefunden hat (Spalte ** Übertragen am **). Die Spalten ** Projekt **und ** Status** beinhalten dementsprechend weitere Informationen.
- Belege erneut übertragen, falls es bei der Datenübertragung zu einem Fehler kam: Markiere dazu die Checkboxen links neben jedem Eintrag und klicke anschließend unten auf **Auswahl erneut übertragen**.
- Den übertragenen Beleg direkt aufrufen: Klicke auf den fett gedruckten Eintrag in der Spalte **Nummer**, um den Beleg direkt zu öffnen und ihm weitere Informationen zu entnehmen.
- Die Adresse des Kunden oder Lieferanten direkt aufrufen: Möchtest du den Addressdatensatz eines Endkunden oder Lieferanten öffnen, klicke einfach auf den fett gedruckten Eintrag in der Spalte **KD-Nr. / Lief.-Nr.**.

### Dateien

In diesem Tab findest du eine Auflistung der eigentlichen Dateien, die von Xentral an das Fremdsystem übertragen wurden. In der Spalte **Status** des Tabs sind sie entsprechend mit dem Vermerk * hochgeladen*gekennzeichnet; im System des Fulfillment-Dienstleisters als * heruntergeladen*oder ähnlich. In den meisten Fällen liegen diese Dateien im XML-Format vor. Diese Übersicht bleibt dir stets erhalten und du kannst sie über das Download-Symbol rechts neben jeder Datei nutzen, um Belege bei Bedarf erneut herunterzuladen - auch, wenn sie eventuell bereits vom Server gelöscht wurden.

In den einzelnen Spalten kannst du Informationen zum **Zeitstempel ** der Übertragung und zur **Größe ** der einzelnen Dateien einsehen. Falls die Datei vom Server gelöscht oder schon einmal über das Tab **Dateien ** heruntergeladen wurde, findest du die Angabe “ja” in den Spalten **Download ** und**Gelöscht auf Server**.

### Tracking

Wenn dein Fulfillment-Dienstleister dir Tracking-Informationen übermittelt, findest du in diesem Tab die Trackingnummer für jeden einzelnen Auftrag. Bei Übertragungen, bei denen keine Tracking-Informationen übermittelt werden, bleibt dieses Tab folglich leer.

Im Tab **Tracking** kannst du folgende Aktionen ausführen:

- Lieferscheine direkt aufrufen: Klicke in der Spalte **Lieferschein** auf die fett gedruckte Lieferscheinnummer, um den übertragenen Lieferschein anzuzeigen
- Trackingnummern einsehen: Die Trackingnummern der Lieferscheine werden angezeigt, sobald deren Positionen erfolgreich vom externen System an den Versanddienstleister übergeben wurden.
- Datum der Lieferscheinerstellung und der Rückmeldung der Tracking-Informationen genau nachvollziehen: Diese Informationen findest du in den Spalten **LS-Datum ** und **Zeitstempel**.

### Lagerzahlen

Bei Übertragungen, die Lagerbestände von deinem Fulfillment-Dienstleister in dein XentralSystem importieren, findest du in diesem Tab eine Auflistung des Lagerbestands, getrennt nach Artikelnummer. So entsteht eine vollständige Übersicht aller eingelagerten Artikel und ihrer aktuellen Bestände. Beachte, dass dieses Tab ohne Inhalt ist, falls die Option **Lagerzahlen empfangen ** im Tab**Details** der Übertragung nicht aktiviert ist und es sich nicht um eine Übertragung handelt, bei der Lagerzahlen gemeldet werden.

Die folgenden Informationen sind im Tab **Lagerzahlen** verfügbar:

- **Artikel-Nr.:** Nummer des Artikels, der im Bestand geführt wird. Dieser Eintrag ist jeweils fett gedruckt - das bedeutet, dass du auf die Nummer klicken kannst, um direkt zum Datensatz des jeweiligen Artikels in deinem Xentral System zu gelangen.
- **Artikel:** Name des Artikels, der im Bestand geführt wird.
- **Lager:** Anzahl an Artikeln, die aktuell eingelagert sind.
- **Zeitstempel:** Zeitpunkt, an dem die Lagerzahlen zuletzt an Xentral übermittelt wurden. Die Häufigkeit des Datenabgleichs richtet sich nach deinen [Einstellungen im Modul Prozessstarter](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc_id_VorbereitendeEinstellungeninXentral-Schritt1Prozessaktivieren).

### Fehler

Bei der Datenübertragung kann es hin und wieder zu Fehlern kommen, die sich entweder auf eine Übertragung als Ganzes oder auch einzelne Belege auswirken können. Generell werden dir Fehler auch im[Monitor](#UUID-2e4e5ae1-18e2-8825-e29e-b9ecc181152a_id_ArbeitenmitdembertragungenModul-bertragungenmitdemMonitorberwachen)angezeigt. Dort kannst du am Schnellsten etwaige Fehler ausfindig machen, indem du den Filter **Nur Fehler anzeigen ** aktivierst. Falls du doch einmal eine spezifische Übertragung näher auf Fehler prüfen möchtest, kannst du auch die Übertragung öffnen und das Tab**Fehler** nutzen. Aufgetretene Fehler werden hier - genau wie im Monitor - mit einer entsprechenden Fehlermeldung und einem präzisen Zeitstempel aufgeführt. So kannst du anhand der Fehlermeldung identifizieren, was zu tun ist. In vielen Fällen handelt es sich um fehlerhafte Zugangsdaten zum Server oder sonstigen Änderungen an den Verbindungswegen, die du leicht mit der Hilfe deines Fulfillment-Dienstleisters beheben kannst.

> **Tipp**
>
> Wenn du eine Übertragung nutzt, um Artikeldaten von einem Fremdsystem in Xentral zu importieren, solltest du im Tab **Details ** der entsprechenden Übertragung die Einstellung **Artikel empfangen Nicht gefundene Artikel ** aktivieren. So stellst du sicher, dass im Tab**Fehler** der Übertragung eine eindeutige Fehlermeldung erscheint, falls vom Fulfillment-Dienstleister Artikel zurückgemeldet haben, die in deinem XentralSystem nicht gepflegt sind. Andernfalls wird aufgrund dieser unbekannten Artikel der Import des kompletten Auftrags verweigert, was zu Folgefehlern führt.