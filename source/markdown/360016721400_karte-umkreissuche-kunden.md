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

Mit dem Modul Umkreissuche können Sie auf einer Karte übersichtlich die Standorte Ihrer Kunden einsehen. Dazu geben Sie eine Adresse und den Umkreis ein, um die naheliegenden Kunden einsehen zu können. Dies erleichtert z.B. Ihre Planungen für einen Außentermin, wenn Sie mehrere Kundentermine in der Region verbinden wollen.

## Vorraussetzungen

Google Maps steuert die Karteninhalte, OpenStreetmap ist für das Befüllen der Adressen mit Geodaten zuständig. Somit braucht man beide API-Keys, um das Modul vollumfänglich zu nutzen.

### Openstreetmap API-Key

Um die Umkreissuche via OpenStreetMap zu aktivieren, gehen Sie wie folgt vor:

1. Bei Openstreetmap einen Account erstellen: [https://openrouteservice.org/sign-up/](https://openrouteservice.org/sign-up/)
1. API-Key anfordern
1. API-Key in den Umkreissuche-Einstellungen eintragen

### Google Maps API-Key

Um die Umkreissuche via Google Maps zu aktivieren, gehen Sie wie folgt vor:

1. API-Key bei Google Maps erstellen, dazu im folgenden Link oben auf „Schlüssel anfordern“ klicken und zustimmen: https://developers.google.com/maps/documentation/javascript/get-api-key?hl=de
1. Folgende APIs in Ihrem Google API Account aktivieren:Geocoding API, Maps JavaScript API
1. API-Key in den Umkreissuche-Einstellungen eintragen

### Prozessstarter erstellen

Unter Administration → Einstellungen → System → Prozessstarter erstellen Sie einen neuen Prozessstarter mit folgenden Werten:

- Bezeichnung→ Als Bezeichnung ist "Openstreetmap" einzugebenname
- Art→ Aus dem Drop-Down-Menü ist als Art "periodisch" auszuwählenmenu
- Wochentag→ Aus dem Drop-Down-Menü ist "Jeden Tag" auszuwählenmenu
- Startzeit→ Es ist die vorgegebene Startzeit zu belassenis
- Letzte Ausführung→ Es ist die vorgegebene Endzeit zu belassenplace
- Periode→ Als Periode ist 1500 in min. anzugeben
- Typ→ Als Typ ist "Cronjob" aus dem Drop-Down-Menü auszuwählen
- Parameter→ Als Parameter ist "openstreetmap" einzugeben
- Aktiv→ Durch Anhaken wird der Prozessstarter aktiviert

Der Prozessstarter füllt nach und nach die beiden Felder Geodaten unter Adressen → Sonstige Daten.

Es werden pro Tag maximal 2000 Adressen mit dem Prozessstarter verarbeitet - mehr lässt die API von Openstreetmap nicht zu. Somit sollte der Prozessstarter auf 25 Stunden (Periode = 1500 Minuten) gestellt sein.

## Umkreissuche benutzen

Folgende Felder gibt es in der Übersicht:

- Projekt→ Lädt alle Adressen, die diesem Projekt zugeordnet sind
- Suchadresse→ Um diese Adresse führt xentral die Umkreissuche aus (Zentrum des Suchradius)
- PLZ→ Statt einer Adresse lässt sich auch um eine PLZ herum suchen
- Umkreis→ Kilometeranzahl des Radius um die Suchadresse herum
- Suchen→ Button klicken um Umkreissuche zu starten
- Bei x von y Adressen sind die Geodaten vorhanden→ Der Prozessstarter hat bei diesen Adressen Geodaten hinterlegt. Wenn Geodaten bei einer Adresse nicht hinterlegt wurden, konnte die API die Adresse nicht eindeutig zuordnen.

### Über Zieladresse suchen

Wenn Sie um eine konkrete Adresse herum suchen wollen, dann geben Sie den Namen oder Kundennummer der Adresse im Feld „Suchadresse“ ein. Das Feld PLZ muss dabei leer bleiben.

### Über PLZ suchen

Sie können auch über die Postleitzahl suchen. Wenn nur 3 Zahlen für die PLZ eingegeben werden, werden die restlichen Ziffern mit 9er aufgefüllt. Beispiel: Aus der Eingabe 815 macht Xentral 81599.

Postleitzahlsuche im Ausland:

Das funktioniert indem man hinter der Postleizahl noch das Land als[2-stelliges ISO Länderkürzel](https://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste)angibt, also z.B. 3100 AT

## Adressen mit und ohne Geocodierung anzeigen

Manche (z.B. fehlerhafte) Adressen können durch den Dienst nicht eindeutig einer Geoposition zugewiesen werden, z.B. wenn Schreibfehler enthalten sind. In diesem Fall kann die Adresse korrigiert oder manuell verortet werden. Um einen Überblick über die Adressen mit und ohne Geocodierung zu erhalten, können Sie sich einen Bericht erstellen.

Gehen Sie dazu unter Stammdaten → Import/Export-Zentrale → Stammdaten-Export und legen sich mit „NEU“ einen neuen Export z.B. wie folgt an:

> **Anmerkung**
>
> Bis Version 21.1 unter Verwaltung → Import/Export-Zentrale → Stammdaten-Export.

![umkreissuche_7.png](https://help.xentral.com/hc/article_attachments/5041724489244)

Mögliche Felder für den Export:

typ; name; land; strasse; ort; plz; lat; lng;