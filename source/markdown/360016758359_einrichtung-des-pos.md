> **Anmerkung**
>
> Als Bestandskunde kannst du die neue POS ganz einfach selbst aktivieren: Über einen **Button in der POS ** schaltest du**das neue Modul eigenständig frei**.
>
> Für den Umstieg empfehlen wir einen Blick in die aktuelle Dokumentation zur neuen POS, die dich bei der Einrichtung und Umstellung unterstützt.
>
> Folgende Neuerungen wurden umgesetzt – und so gelingt dir der **schnelle und reibungslose Umstieg von der alten zur neuen POS**:
>
> - **Modernisierte Benutzeroberfläche**: Die neue POS bietet ein frisches, modulares Design mit optimierter Nutzerführung – ideal für schnelles Kassieren und klare Abläufe.
> - **Browser- und App-Kompatibilität **: Die POS ist als Desktop-Version für die Betriebssystem ** Windows und macOS**sowieals Android-Appverfügbar. Die bisherige Web-Browseranwendung bleibt zusätzlich bestehen.
> - **Hardwareanbindung **:Drucker und Kassenschubladen werden jetzt über eine zentrale POS-App angebunden. Das vereinfacht Konfiguration und Wartung. Vorhandene IP-fähige Geräte können weiterverwendet werden. Wenn du bereits ein bestehendes Drucker-Setup mit Adapterbox nutzt, kannst du diese auch mit der neuen POS-Anwendung weiterhin in der Übergangszeit verwenden. ** Wichtig **: Langfristig solltest du für die ** neuen Desktop-Apps**den Drucker einmalig neu in der App einrichten. Die Einrichtung sind wenige Klicks und hier erklärt.
> - **Vereinfachter Umstieg für Bestandskunden**: Du kannst die neue POS direkt im System per Button aktivieren – ganz ohne Supportanfrage oder Wartezeit.
> - **Neue Zahlungsfunktionen**: Mischzahlungen (z. B. Bar + EC) und Teilzahlungen über Rechnungsnummern sind jetzt möglich – ideal für Omnichannel- und Filialprozesse.
> - **KassenSichV-konform**: Die neue POS ist vollständig vorbereitet für rechtliche Anforderungen in Deutschland. TSE-Module können weiterhin genutzt werden.
> - **Daten und Artikel bleiben erhalten**: Artikelstammdaten, Kunden und Kassenlogik sind weiterhin nutzbar. Es ist keine Migration deiner POS-Daten notwendig, nur das Setup wird aktualisiert. WichtigSchließe vor der Nutzung von Xentral POS idealerweise alle alten Vorgänge ab (z.B. alte Teilrechnungen).

Bevor du mit dem Verkauf über die Xentral POS startest, solltest du einige grundlegende Einstellungen vornehmen. Diese sorgen dafür, dass dein Kassenprozess reibungslos funktioniert, rechtssicher ist und sauber mit Buchhaltung, Lager und Belegdruck verbunden wird.

In diesem Abschnitt findest du eine Übersicht aller zentralen Konfigurationspunkte für deine POS – von der Einrichtung deines POS-Projekts bis hin zu Zahlungsarten und Druckersteuerung. Du kannst die Einstellungen je nach Geschäftsmodell flexibel anpassen, ob für B2B, B2C oder hybride Szenarien.

**Wichtige Konfigurationsbereiche (mit Sprungmarken):**

- [Strategische Entscheidungen bei der POS-Einrichtung](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm23484624198379)
- [POS-Projekt & Kassenbuch anlegen](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234835766859589)
- [Laufkundschaft & Kundenverwaltung](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234835767139193)
- [Kassierer anlegen & Rechte vergeben](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234835767318719)
- [POS-Einstellungen im Projekt vornehmen](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234835768012693)
- [Zahlungsarten & Belegarten](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234846213076909)
- [POS-Tasten & Sonderfunktionen (z. B. Rabatt, Trinkgeld)](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234846213076909)
- [POS App – Nutzung auf Desktop und mobilen Geräten](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234845879692454)
- [Belegdruck & Bondrucker einrichten](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm23484581280645)
- [Kassenschublade & Hardwareintegration](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm234845855266871)
- [TSE-Anforderungen](https://help.xentral.com/hc/de/articles/360021356660#UUID-1697c2f7-1864-3aef-2ee5-1a6fdb64b89a)
- [Kartenterminal: EC-/ Kreditkartenterminal](#UUID-3e786329-72d8-2127-72cf-db6f23a57223_section-idm23484583762517)

## Strategische Entscheidungen bei der POS-Einrichtung

Diese Punkte helfen dir, dein POS-System passend zu deinem Geschäftsmodell (B2C, B2B oder Hybrid) und deinen operativen Abläufen einzurichten:

> **Anmerkung**
>
> **Hinweis**
>
> - POS-Lager & Warenfluss: - **Eigenes POS-Lager verwenden? ** Sinnvoll bei getrenntem Filialbetrieb oder Messeverkauf. -** Lagerprozess aktivieren (mit Lagerabzug)? ** Aktivieren, wenn du Lagerbestände automatisch abbuchen willst. -** POS-Lager vom Hauptlager trennen oder gemeinsam nutzen?** Möglich je nach Regalzuordnung in der Lagerverwaltung.
> - Struktur: Eine oder mehrere POS-Kassen: - **Mehrere POS pro Standort möglich? ** Lege pro Kasse ein eigenes Projekt an (z. B. Filiale A / Filiale B). -** Mitarbeiter-Zuweisung je Kasse**: Kassierer müssen spezifisch einem POS-Projekt zugewiesen werden.
> - Kundenzuordnung: Laufkundschaft vs. Kundenbindung: - **Laufkundschaft (anonym)? ** Adresse „Laufkundschaft“ im Projekt hinterlegen. -** Kunden aus Stammdaten auswählen oder neu anlegen? ** Ermöglicht personifizierte Belege und spätere Zuordnung. -** Kundennummern aus anderen Projekten verwenden?** Optional aktivierbar.
> - Zahlungsweisen & Abrechnungslogik: - **Welche Zahlungsarten sollen in der POS aktiv sein? ** Barzahlung, EC-Zahlung (mit oder ohne Terminal), Kreditkarte, Überweisung, Gutschein (als Artikel), Gutschrift, Teilzahlungen (Kombination mehrerer Zahlungsarten), Trinkgeld (optional je Zahlungsart aktivierbar) -** Wie willst du Belege ausgeben?** Quittung, Rechnung, Gutschrift, Lieferschein.
> - Tasten / Buttons aktivieren: - **Rabatte & Trinkgeld? ** Prozentualer Rabatt auf den Warenkorb oder einzelne Artikel sowie feste Beträge über Rabattartikel möglich. Trinkgeld kann optional je nach Zahlungsart (Bar, EC, Kreditkarte) aktiviert werden. -** Kassenvorgänge **: Einlagen und Entnahmen zur Verwaltung von Bargeld (z. B. Wechselgeld, Geldtransit) sowie das Öffnen der Kassenschublade über die Benutzeroberfläche. -** Kassenvorgänge**: Einlagen und Entnahmen zur Verwaltung von Bargeld (z. B. Wechselgeld, Geldtransit) sowie das Öffnen der Kassenschublade über die Benutzeroberfläche.
> - Buchhaltung & Kassenabschluss: - **Wie sollen die Umsätze verbucht werden? ** Einzelbuchungen mit Belegverknüpfung (ideal für B2B) oder Tagessummen (empfohlen bei vielen Kleinbeträgen / B2C). -** Kassenbuch-Zuordnung **: Jedem POS-Projekt muss ein spezifisches Geschäftskonto vom Typ „Kasse“ zugewiesen sein. -** Tages-/Monatsabschluss**: Automatisch erstellt. Vervollständige den Tagesabschluss durch dein Zählprotokoll.
> - Hardwarestrategie & Geräteeinsatz - **Welches Gerät nutzt du? ** Xentral POS App alternativ POS im Xentral-Browser starten. -** Welches Gerät nutzt du? ** Xentral POS App alternativ POS im Xentral-Browser starten. -** Belegdruck konfigurieren**: Anzahl, Typ und Kombination von Rechnung / Quittung / Lieferschein einstellbar.

> **Tipp**
>
> Kläre diese Punkte frühzeitig mit deinem Steuerberater oder deinem Xentral-Partner – vor allem, wenn du mit mehreren Kassen oder gemischten Geschäftsmodellen arbeitest.

## Voraussetzungen und Einrichtung

Bevor du mit dem Verkauf über die POS starten kannst, musst du einige grundlegende Voraussetzungen erfüllen und die nötigen Stammdaten in Xentral anlegen. In diesem Abschnitt zeigen wir dir Schritt für Schritt, wie du ein POS-Projekt erstellst, ein Kassenbuch einrichtest, die Adresse für Laufkundschaft definierst und Kassierer korrekt berechtigst.

### Projekt für POS anlegen **Schritte: **

1.** Für ein neues Projekt **: Gehe zu ** Einstellungen > Grundeinstellungen > Projekte**.
1. Klicke auf **+NEU**, um ein neues Projekt für die POS zu erstellen.
1. Vergib einen eindeutigen Namen (z. B. 'POS MUC').
1. Setze die gewünschten POS-Einstellungen im Projekt im Tab **Einstellungen > POS Einstellungen** (siehe weiter unten).

### Kassenbuch anlegen **Schritte**:

1. Gehe zu **Einstellungen > Buchhaltung > Zahlungen & Geschäftskonten > Bank & Zahlungskonten**.
1. Lege ein neues Konto mit dem Typ **Kasse** an.
1. Verknüpfe dieses Konto mit dem POS Projekt - wähle das Konto dort aus und klicke auf **Speichern**.
1. Dieses Kassenbuch wird automatisch unter **Smart-Search > Kassenbuch** sichtbar und dient zur automatischen Erfassung aller Kassenvorgänge deiner POS.

### Adresse für Laufkundschaft erstellen **Schritte**:

1. Öffne **Stammdaten > Adressen ** und klicke auf **+NEU**.
1. Erstelle eine Adresse mit Namen **Laufkundschaft** oder ähnlich.
1. Verknüpfe diese Adresse im POS-Projekt - wähle die Adresse dort aus und klicke auf **Speichern**.
1. Diese Adresse wird bei Verkäufen ohne Kunden Adresseingabe automatisch ausgewählt.

### Kassierer anlegen und berechtigen

> **Anmerkung**
>
> Die Ausführliche Anleitung findest du hier auf dieser Seite: Kassierer neu anlegen.

**Schritte**:

1. Gehe zu **Einstellungen > Verkaufen > Kassenfunktion (POS) > POS Konfiguration (Kassierer)**.
1. Klicke auf +NEU, um einen neuen Kassierer zu erstellen.
1. **Voraussetzung**: Der Kassierer muss bereits als Adresse mit der Rolle 'Mitarbeiter des POS-Projekts' im System existieren.
1. Vergib mindestens folgende Rechte (in der Benutzer Rechtevergabe): **POS ** und **WELCOME**: login, logout, settings, start, startseite.

> **Anmerkung**
>
> Führe einen Test-Login durch und prüfe im **Systemlog**, ob alle nötigen Rechte vorhanden sind.

## POS-Einstellungen im Projekt

Navigiere zu **Einstellungen > Grundeinstellungen > Projekte **. Klicke auf das gewünschte Projekt oder lege ein neues Projekt an. Gehe im Projekt auf ** Einstellungen > POS Einstellungen**.

### POS Einstellungen

In der folgenden Tabelle findest du eine Übersicht über alle relevanten Felder in den POS-Projekteinstellungen, inklusive kurzer Beschreibung ihrer Funktion. Diese Einstellungen steuern u. a. das Lagerverhalten, die Preislogik, verwendete Artikel sowie Druckoptionen und Abschlussberichte in der Kassenumgebung.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Lagerprozess | Legt fest, ob beim Verkauf Lagerbewegungen erzeugt werden. - **Keine Lagerbuchung erzeugen **: deaktiviert die Lagerverwaltung für POS-Vorgänge.<br>-** Aus beliebigem Lager entnehmen **: entnimmt den Artikel aus einem beliebigen Lager.<br>-** Aus eingestelltem POS Lager entnehmen**: entnimmt den Artikel nur aus dem im Projekt eingestellten POS Lager (s.u.). |
| Adapterbox für POS | 💬 **Hinweis:** Abgekündigt: 01/2025 (Neue POS). Diese Einstellung ist nicht mehr relevant! Verbindet Bondrucker und andere POS-Hardware über die Adapterbox mit Xentral. |
| POS Lager für den Verkauf | Definiert das Lager, aus dem die Artikel bei POS-Verkäufen entnommen werden – z. B. separates Ladenlager. |
| Preisgruppe bevorzugt | Legt fest, welche Preisgruppe für den POS-Verkauf angewendet wird. Nur Preise aus dieser Gruppe werden angezeigt. |
| Kasse für Bar | Das zugehörige Kassenbuch (und Geschäftskonto Einstellung) für Barzahlungen, auf dem POS-Umsätze erfasst werden. |
| Laufkundschaft | Vordefinierte Adresse für anonyme Kunden. Wird automatisch verwendet, wenn keine konkrete Kundenadresse ausgewählt ist. |
| Kunden aus fremden Nummernkreisen abwickeln | Ermöglicht das Abrechnen von Kunden aus anderen Projekten (z. B. bei Filialen oder gemischten Datenstrukturen). |
| Nur Artikel aus Projekt erlauben | Zeigt im POS nur die Artikel an, die zum jeweiligen POS-Projekt gehören. |
| Gleiche Artikel summieren bei nacheinander Eingabe | Fasst identische Artikelpositionen im Warenkorb automatisch zusammen. |
| Artikel für EUR-Rabatt | Hier wird der Artikel ausgewählt, mit dem Rabatte in Euro abgebildet werden (z. B. durch negativen Preis). |
| pos.items_for_splitting | Artikelnummer, die für Anzahlungen oder Aufteilungen verwendet wird – z. B. 'Anzahlung' oder 'Teilzahlung'. |
| Lieferschein erstellen | Aktiviert das Erstellen eines Lieferscheins beim Verkauf. Notwendig bei MHD-/Chargenartikeln oder Seriennummern. |
| Kasse Beschriftung 1 | Bezeichnung für das Feld 'Interne Bemerkung' - wird abgedruckt auf Rechnungen und Quittungen – frei wählbar. |
| Kasse Beschriftung 2 | Bezeichnung für das Feld 'Freitext' auf Belegen – z. B. Zusatzinfos zum Kauf oder Hinweise – frei wählbar. |
| Artikelbeschreibung in Belege übernehmen | Druckt die Artikelbeschreibung aus dem Artikelstamm auf den Beleg. |
| POS Anzeige in netto | Zeigt Preise im POS in Netto statt Brutto – relevant für B2B-Verkäufe. |
| Mehrere Aufträge pro Kassierer | Erlaubt es, mehrere Vorgänge parallel zu speichern und später abzuschließen – z. B. bei Beratung oder unterbrochenem Einkauf. |
| Detaillierte Ansicht im Abschluss-PDF | Erzeugt ein PDF mit allen Einzelpositionen im Tagesabschluss. |
| Einzelbuchungen ausblenden | Reduziert das Abschluss-PDF auf Summen und blendet Einzelbuchungen aus – übersichtlicher bei hoher Frequenz. |
| Monatsberichte ohne Einzeltage | Erstellt einen Monatsbericht ohne Aufschlüsselung der einzelnen Tagesabschlüsse. |
| Zählprotokoll ausblenden | Unterdrückt die detaillierte Bargeldzählung im Abschlussbericht. |
| Unterschriftblock ausblenden | Verbirgt das Unterschriftenfeld auf Tages- oder Monatsabschlussdokumenten – z. B. bei rein digitaler Verwaltung. |

### Buttons

Die folgenden Einstellungen für die Buttons in der POS-Oberfläche ermöglichen das Erfassen von Zahlungen, das Erstellen von Belegen, Rabatten sowie weiteren Kassenvorgängen. Hier findest du eine Übersicht mit Erklärung, wie jeder Button im Verkaufsprozess verwendet wird. Ideal zur Orientierung bei der Nutzung oder Einrichtung deiner Xentral POS.

| Feldbeschreibung | Bezeichnung |
| --- | --- |
| Zahlungsweise Bar | Markiert den Verkauf als bar bezahlt und schließt den Vorgang ab. **Rechnung als bezahlt markieren**: markiert die Rechnung als 'bezahlt' ohne eine Kontobuchung z.B. Hand-Kassenbuch |
| Zahlungsweise EC | Markiert den Verkauf als per EC-Karte bezahlt. Betrag wird an das Kartenlesegerät gesendet (sofern verbunden). **Rechnung als bezahlt markieren **: markiert die Rechnung als 'bezahlt' ohne eine Kontobuchung z.B. Geschäftskonto für EC Kartenzahlungen. (Optional)** Kasse**: Sonderfall: Für bestimmte Zahlungsarten – z. B. Kreditkartenzahlungen – kannst du ein eigenes Kassenbuch anlegen. Diese Funktion ist optional und sollte nur verwendet werden, wenn du eine saubere Trennung der Buchungen benötigst. Lege für bestimmte Zahlungsweisen (z. B. Kreditkarte) ein separates Kassenbuch an – nicht ins POS-Hauptkassenbuch buchen. |
| Zahlungsweise Kreditkarte | Markiert den Verkauf als mit Kreditkarte bezahlt. Für die Anbindung ist ein kompatibles Terminal erforderlich. **Rechnung als bezahlt markieren **: markiert die Rechnung als 'bezahlt' ohne eine Kontobuchung z.B. Geschäftskonto für Kreditkartenzahlungen. (Optional)** Kasse**: Sonderfall: Für bestimmte Zahlungsarten – z. B. Kreditkartenzahlungen – kannst du ein eigenes Kassenbuch anlegen. Diese Funktion ist optional und sollte nur verwendet werden, wenn du eine saubere Trennung der Buchungen benötigst. Lege für bestimmte Zahlungsweisen (z. B. Kreditkarte) ein separates Kassenbuch an – nicht ins POS-Hauptkassenbuch buchen. |
| Zahlungsweise Überweisung | Kennzeichnet den Verkauf als per Überweisung bezahlt. Zur späteren Nachverfolgung in der Buchhaltung. **Rechnung als bezahlt markieren **: markiert die Rechnung als 'bezahlt' ohne eine Kontobuchung z.B. Geschäftskonto für die Bank. (Optional)** Kasse**: Sonderfall: Für bestimmte Zahlungsarten – z. B. Kreditkartenzahlungen – kannst du ein eigenes Kassenbuch anlegen. Diese Funktion ist optional und sollte nur verwendet werden, wenn du eine saubere Trennung der Buchungen benötigst. Lege für bestimmte Zahlungsweisen (z. B. Kreditkarte) ein separates Kassenbuch an – nicht ins POS-Hauptkassenbuch buchen. |
| Weitere Zahlungsweise | Kennzeichnet den Verkauf als 'Wählbare Zahlungsweise' bezahlt. Zur späteren Nachverfolgung in der Buchhaltung. **als bezahlt markieren **: markiert die Rechnung als 'bezahlt' ohne eine Kontobuchung z.B. Hand-Kassenbuch. (Optional)** Kasse**: Sonderfall: Für bestimmte Zahlungsarten – z. B. Kreditkartenzahlungen – kannst du ein eigenes Kassenbuch anlegen. Diese Funktion ist optional und sollte nur verwendet werden, wenn du eine saubere Trennung der Buchungen benötigst. Lege für bestimmte Zahlungsweisen (z. B. Kreditkarte) ein separates Kassenbuch an – nicht ins POS-Hauptkassenbuch buchen. |
| Beleg Rechnung | Erstellt eine vollständige Rechnung mit Kundenangabe und Steuerausweis. |
| Beleg Quittung | Erstellt einen einfachen A4-Beleg mit der Bezeichnung 'Quittung' anstelle von 'Rechnung'– ideal für Laufkundschaft ohne Kundenbindung. Der erstellte Beleg enthält keine Kundeninformationen und ersetzt **nicht ** den Bondruckerbeleg. 💬**Anmerkung:** Dies ist nicht der Kassenbon aus dem Bondrucker. Für Bondruck bitte die entsprechenden Einstellungen im Bereich Bondrucker vornehmen. |
| Rabatt in % | Wendet einen prozentualen Rabatt auf den gesamten Warenkorb an. |
| Rabatt in EUR | Zieht einen festen Betrag in Euro vom Gesamtpreis ab. |
| Entnahme | Erfasst eine Entnahme von Bargeld aus der Kasse, z. B. für Wechselgeld oder Abrechnung. |
| Einlage | Erfasst eine Bareinlage in die Kasse, z. B. zu Beginn des Tages oder nach Geldwechsel. |
| Trinkgeld | Erfasst freiwilliges Trinkgeld bei Barzahlung und bucht es auf das definierte Konto. |
| Trinkgeld bei EC und Kreditkarte | Erlaubt die Erfassung von Trinkgeld bei EC- oder Kreditkartenzahlung direkt im Bezahlvorgang. |
| Lade öffnen | Öffnet manuell die Kassenschublade – z. B. zur Vorbereitung des Kassiervorgangs. |
| Belege laden | Lädt eine bereits erstellte Rechnung oder einen Auftrag zur Abrechnung oder Stornierung. |
| Storno | Storniert den aktuellen Verkaufsvorgang vollständig oder teilweise. |
| Automatisches Ausloggen | Aktiviert das automatische Abmelden nach einer definierten Zeit ohne Aktivität. |
| Automatisches Ausloggen nach Abschluss Zahlung | Loggt den Kassierer direkt nach Verkaufsabschluss automatisch aus – z. B. bei wechselndem Personal. |

### Weitere Einstellungen

Diese Einstellungen steuern das Verhalten der POS-Oberfläche beim Erfassen von Kundendaten und Zahlungsarten. Sie helfen dabei, vollständige und korrekte Verkaufsdaten sicherzustellen – insbesondere bei der Abwicklung von Rechnungen im B2B-Umfeld oder im Umgang mit sensiblen Buchungen.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| Erweiterte Adressfelder | Blendet zusätzliche Felder (z. B. Straße, PLZ, Ort) bei der Neuanlage von Kunden direkt in der POS-Oberfläche ein – nützlich für vollständige Rechnungsdaten. |
| Zwangsauswahl Zahlweise | Erzwingt jedes Mal neu die Auswahl einer Zahlungsart vor Abschluss des Verkaufs – verhindert versehentlich falsche Buchungen. |
| Vorauswahl Anrede | Erzwingt jedes Mal neu die Auswahl einer Zahlungsart vor Abschluss des Verkaufs – verhindert versehentlich falsche Buchungen. |

### Drucker Einstellungen (Dokumentendrucker)

Diese Einstellungen definieren, welche Belege im Verkaufsprozess automatisch gedruckt werden und auf welchem Gerät. Damit steuerst du gezielt, wie viele Kopien erstellt werden, ob Lieferscheine oder Quittungen mitgedruckt werden sollen und ob ein QR-Code zur Kundeninteraktion auf dem Kassenbon erscheinen soll. Ideal für B2B-Prozesse, Lagerlogistik oder papierlose Belegstrategien.

| Feldbezeichung | Beschreibung |
| --- | --- |
| Belegausgabe nach Abschluss | Legt fest, ob und welche Belege nach Abschluss des Verkaufs automatisch ausgedruckt werden sollen – z. B. Rechnung, Quittung-Beleg oder Lieferschein. (Standard: PDF A4 Format) - **Keine Ausgabe **: Gibt keine Belege am Drucker aus. Speichert nur Digital ab.<br>-** Drucker**: Gibt die Belege am unten ausgewählten Drucker aus |
| Drucker | Wählt den Standarddrucker aus, auf dem die POS-Dokumente ausgegeben werden – z. B. ein Bondrucker oder ein Netzwerkdrucker. |
| Anzahl an Lieferscheinen | Gibt an, wie viele Lieferscheine pro Verkaufsvorgang gedruckt werden sollen. |
| Anzahl Rechnung | Definiert die Anzahl der zu druckenden Rechnungen pro Transaktion. |
| Anzahl Gutschrift | Bestimmt, wie oft eine Gutschrift bei einem Storno ausgedruckt wird. |
| Anzahl an doppelten Lieferscheinen | Ermöglicht den zusätzlichen Ausdruck eines Lieferscheins als Kopie – z. B. für Lager oder Kunden. |
| Bei Rechnungsausdruck immer auch Quittung (Kassenbon) ausdrucken | Wenn diese Funktion aktiv ist, wird automatisch ein **Kassenbon** ausgedruckt – so wie man ihn von einer normalen Kasse kennt. Der Bon enthält die wichtigsten Transaktionsdaten in kompaktem Format und eignet sich für die direkte Ausgabe an den Kunden. Zusätzlich kannst du bei Bedarf auch noch den vollständigen Rechnungsbeleg (z. B. A4) separat mitdrucken lassen. |
| QR-Code auf Quittung (Kassenbon) drucken | Aktiviert das Drucken eines QR-Codes auf dem Kassenbon – z. B. für Kundenumfragen, digitale Belege oder weiterführende Links. |

### Bondrucker

In diesem Abschnitt legst du fest, wie der Bon-Ausdruck an der Kasse erfolgt. Du kannst die Anzahl der Ausdrucke definieren, individuelle Textzeilen für Kopf und Fuß gestalten (z. B. für rechtliche Hinweise oder Unternehmensinfos) und steuern, ob zusätzliche Daten wie Artikel-Freifelder oder ein QR-Code mit der Belegnummer auf dem Bon erscheinen sollen. Ideal zur Optimierung des Kundenerlebnisses und für interne Prozesse.

| Feldbezeichnung | Beschreibung |
| --- | --- |
| aktiv | Aktiviert den Bondruck für Transaktionen. Nur aktivierte Drucker können für Quittungen und Kassenzettel genutzt werden. |
| Anzahl Ausdrucke | Legt fest, wie viele Bon-Ausdrucke pro Verkaufsvorgang erstellt werden sollen. |
| Zeile 1 | Individuelle Textzeilen für den Kopf oder Fuß des Kassenbons – z. B. Firmenname, Adresse, Telefonnummer oder rechtliche Hinweise. z.B. **Xentral Store** |
| Zeile 2 | Individuelle Textzeilen für den Kopf oder Fuß des Kassenbons – z. B. Firmenname, Adresse, Telefonnummer oder rechtliche Hinweise. z.B. **Xentral GmbH Fuggerstrasse 11 86152 Augsburg Tel: 0821/123455678910 www.xentral.com** |
| Zeile 3 | Individuelle Textzeilen für den Kopf oder Fuß des Kassenbons – z. B. Firmenname, Adresse, Telefonnummer oder rechtliche Hinweise. z.B. **Vielen Dank fuer Ihren Einkauf! Umtausch innerhalb 8 Tagen gegen Vorlage des Kassenbons UST.-IDNr: 1234567890** |
| Freifeld aus Artikel auf Bon | Gibt an, ob ein zusätzliches Freifeld aus dem Artikel (z. B. Hinweise oder Varianten) auf dem Bon mit ausgegeben werden soll. |

## Kassierer neu anlegen

Die Bedienung der Kassenoberfläche kann nur durch ausgewiesene Kassierer erfolgen. Die Erstellung eines Kassierers im System setzt voraus, dass dieser Kassierer bereits als Mitarbeiter unter **Verkauf > Adressen** vorhanden ist. Wichtig hierbei ist, dass der Mitarbeiter explizit die Rolle "Mitarbeiter des entsprechenden POS - Projektes" ist, es reicht nicht wenn der Mitarbeiter nur die Rolle "Mitarbeiter von Projekt ALLE" besitzt.

![pos_adresse_kassierer_001.png](https://help.xentral.com/hc/article_attachments/19096996282140)

Ist der Datensatz für den Mitarbeiter vorhanden, kann er unter **App Center > POS (Konfiguration) > Übersicht** als Kassierer hinzugefügt werden.

Lege mit **+ Kassierer hinzufügen ** einen neuen Kassierer an und wähle den entsprechenden **Mitarbeiter ** aus den Stammdaten und das**Projekt ** (bzw. den Standort, die Filiale) aus, und vergebe eine ** Kassierernummer **. Klicke anschließend auf ** Speichern**.

![pos_kassierer_anlegen_001.png](https://help.xentral.com/hc/article_attachments/19097055215772)

### Rechtevergabe für Kassierer im POS

Damit Kassierer an der Kasse vollständig arbeitsfähig sind, müssen bestimmte Rechte im POS-Modul vergeben werden.

Mindestens notwendig sind die Rechte **POS ** sowie**WELCOME ** (für Login, Logout, Startseite, grundlegende Navigation: ** login **, ** logout **, ** settings **, ** start **, ** startseite**).

Führe anschließend den vollständigen Kassen-Workflow einmal durch (von Login über Verkauf bis Tagesabschluss) und prüfe im[Systemlog](https://help.xentral.com/hc/de/articles/8019521254300#UUID-66d8e7e4-88fa-26b4-71b1-cf3101215125), ob weitere Rechte fehlen. Fehlende Rechte können dann gezielt ergänzt werden.

> **Tipp**
>
> Für eine Ladenkasse kannst du einen separaten Kassierer mit **eingeschränkten Rechten** anlegen. Zusätzlich lässt sich einstellen, dass dieser Kassierer nach jedem Verkaufsvorgang automatisch ausgeloggt wird. So stellst du sicher, dass nur der dafür vorgesehene Benutzer Verkäufe tätigen und einsehen kann. Einen vollumfänglicheren Kassierer-Account kannst du dann nach Ladenschluss ausschließlich für die Tages- oder Monatsabrechnung nutzen.

### Achtung

Das Recht **settings** (Kasseneinstellungen ändern) sollte nicht an Kassierer vergeben werden, da es nur für Administratoren vorgesehen ist.

| Systemrecht | Beschreibung |
| --- | --- |
| abschluss | Tagesabschluss an der Kasse durchführen. |
| abschlusspdf | Tagesabschluss als PDF erzeugen/herunterladen. |
| archiv | Zugriff auf Archiv abgeschlossener Verkäufe (Tab: Letzte Rechnungen). |
| artikel | Artikel an der Kasse anzeigen und auswählen. |
| checkkass | Kassenprüfung durchführen (z. B. Kassenbestand kontrollieren). |
| finsess | Aktuelle Kassensession beenden. |
| ladeoeffnen | Kassenschublade öffnen. |
| list | Verkaufslisten anzeigen. |
| loadaddr | Kundendaten (Adressen) laden. |
| loadart | Artikeldetails laden. |
| loadkassstand | Kassenbestand abrufen. |
| loadsess | Offene Kassensession laden. |
| logoutkass | Aus der Kassensession abmelden. |
| minidetail | Kurzdetails eines Belegs anzeigen. |
| monatsabschlusspdf | Monatsabschluss als PDF erzeugen. |
| printreceipt | Kassenbon drucken. |
| resetsess | Kassensession zurücksetzen. |
| saveinfo | Beleg- oder Kundendaten speichern. |
| saveinternebemerkung | Interne Bemerkung zu einem Beleg speichern. |
| storesess | Aktuelle Kassensession speichern. |
| storno | Artikel oder Beleg stornieren. |
| suche | Suche nach Artikeln oder Kunden. |

## Entnahme / Einlage Konten

Es ist möglich in Xentral bestimmte Konten für die Entnahme bzw. Einlage von Geldbeträgen in der POS zu definieren mit den entsprechen Steuersätzen. Im Tab **Entnahme / Einlage Konten ** kann über den Button**+Neuer Eintrag** ein neues Konto definiert werden.

Wenn in der POS der Button **Einlage ** oder**Entnahme** gedrückt wird, erscheint sobald man ein Konto definiert hat ein Grund, in dem man das Entnahme/ Einlage Konto auswählen kann.

Im Kassenbuch der POS erscheint der Grund auch als Eintrag.

Es erfolgt zusätzlich ein Bonausdruck bei jedem Entnahme- / Einlage-Vorgang

## Hardware und Bondrucker

Hardware anschließen:

Hardware anschließen: Bondrucker, Barcodescanner, EC-Terminal, Kassenschublade, Dokumenten (Belege) Drucker.

### POS App – Nutzung auf Desktop und mobilen Geräten

Mit der neuen Xentral POS Applikation kannst du deine Kasse flexibel auf verschiedenen Geräten nutzen. Die Anwendung lässt sich wie gewohnt installieren (Desktop oder Google Play Store für die Nutzung auf mobilen Geräten) und mit deiner Xentral Cloud verbinden:

- Xentral **POS Desktop-Installation** (Windows und macOS)
- **Xentral POS App ** für Android-Geräte [im Google Play Store](https://play.google.com/store/apps/details?id=com.xentral.pos_app&pli=1)**Xentral POS Desktop-Installation (Windows & macOS):**

**Schritte:**

1. Installiere die Xentral POS als Desktop-App auf Windows oder macOS:
1. Öffne nach der Installtion die 'pos_app'.
1. Gib in den folgenden Dialog deine Xentral-URL ein und klicke auf **Speichern**.
1. Melde dich mit deinen Zugangsdaten an.
1. Es öffnet sich die Startseite deiner Xentral-Instanz.

### Anbindung eines Bondruckers an die POS-App **Schnellstart Bondrucker anbinden:**

- In der POS App gibst du einfach die IP-Adresse deines Bondruckers (z. B. Epson TM-m30II) ein. Diese IP-Adresse kannst du ganz einfach über den Drucker selbst abrufen
- Beim Startvorgang oder per Knopfdruck gibt der Drucker automatisch einen Bon aus, auf dem die aktuelle IP-Adresse aufgedruckt ist. (Alternativ kannst du auch die offizielle Epson Konfigurations-App nutzen, um den Drucker ins lokale Netzwerk (WLAN oder LAN) einzubinden und zu konfigurieren.)

![pos_bondrucker_mit_app_verbinden_IPadresse_001.png](https://help.xentral.com/hc/article_attachments/19097055226396)

![pos_bondrucker_ipadresse_netzwerk.png](https://help.xentral.com/hc/article_attachments/19097055228444)

**Einbindung des Druckers in dein lokales Netzwerk: ** Um in der POS-App Belege oder Bons zu drucken, muss ein Bondrucker wie z. B. der Epson TM-m30II in dein lokales Netzwerk eingebunden werden. Da diese Geräte in der Regel kein Display oder keine Tastatur haben, erfolgt die Einrichtung über eine Hilfs-App (z. B. Epson TM Utility App), mit der du dem Drucker deine WLAN-Zugangsdaten übermittelst.** Wichtige Voraussetzungen & Schritte**:

1. **Netzwerkanbindung erforderlich**: Der Drucker muss über LAN (Ethernet) oder WLAN ins gleiche Netzwerk gebracht werden, in dem sich auch das Gerät mit der POS-App (z. B. ein Tablet oder Laptop) befindet.Eine direkte Verbindung über USB oder ohne Netzwerk (z. B. nur lokal am Laptop) wird aktuell nicht unterstützt.
1. **Einrichtung via Utility-App**: Die benötigte App bekommst du vom Druckerhersteller – zum Beispiel im App Store oder auf der Website von Epson. Darüber kannst du dem Drucker deine WLAN-Zugangsdaten (SSID &amp; Passwort) übermitteln.
1. **Netzwerkumgebung**: Ob du einen mobilen Hotspot, eine Fritz!Box, ein Unternehmens-WLAN oder einen separaten POS-Router nutzt – der Drucker und das POS-Gerät müssen im gleichen Netzwerk angemeldet sein. Nur dann kann die POS-App den Drucker erkennen und Druckbefehle senden.
1. **Verbindung testen**: Nach der Einrichtung solltest du über die POS-App einen Testdruck durchführen können. Wird kein Drucker erkannt, prüfe die Netzwerkeinstellungen, IP-Adressen und ggf. die Firewall-Regeln.

### Kassenschublade

Die Kassenschublade wird direkt an den Bondrucker angeschlossen. Sobald der Drucker korrekt mit der POS-Anwendung in Xentral verbunden ist, lässt sich die Schublade über die Benutzeroberfläche bequem steuern. Der Befehl „Lade öffnen“ wird vom System an den Drucker gesendet, der ihn automatisch an die angeschlossene Kassenschublade weiterleitet.

Du kannst die Kassenschublade jederzeit öffnen – entweder über die Startseite der POS oder im Abschlussdialog bei den Zahlungsarten per Klick auf das Icon 'Kassenschublade öffnen'.

Die Informationen zur Bedienung der Kassenschublade findest du im Artikel[POS-Funktionen und Bedienung](https://help.xentral.com/hc/de/articles/360016756919#UUID-f9c2fd56-fc63-9774-4412-2e05d54d7338).

### Kartenterminal: EC-/Kreditkartenterminal

Du kannst das EC-/Kreditkartenterminal manuell parallel zur POS verwenden. Gib dazu einfach den Betrag manuell am Terminal ein, führe den Zahlungsvorgang dort durch und schließe anschließend die Transaktion in der POS ab.

#### Wie funktioniert die Anbindung eines Kartenterminals an Xentral POS?

Wenn du mit der Kasse in Xentral eine Kartenzahlung startest, soll das Kartenterminal automatisch den Betrag anzeigen – ohne dass du nochmal tippen musst. Dafür braucht es eine technische Verbindung zwischen der Kasse und dem Terminal.

Diese Verbindung wird über eine sogenannte **Middleware ** hergestellt – ein kleines Zusatzprogramm, das zwischen der Kasse und dem Terminal „übersetzt“. Sie läuft auf einem kleinen Server oder Computer und sorgt dafür, dass alle Zahlungsdaten korrekt weitergeleitet werden. **So funktioniert es Schritt für Schritt:**

1. Du startest die Zahlung über die Xentral POS-Kasse.
1. Die Kasse sendet automatisch eine Nachricht mit Zahlungsdaten (z. B. Betrag, Währung).
1. Die Middleware empfängt diese Daten und leitet sie ans Kartenterminal weiter.
1. Das Terminal zeigt den Betrag an und der Kunde zahlt.
1. Das Terminal meldet den Zahlungsstatus zurück – Xentral weiß dann, ob die Zahlung erfolgreich war.

> **Anmerkung**
>
> **Hinweis**
>
> **Was du als Unternehmen brauchst:**
>
> - Ein **Kartenterminal**, das übers Netzwerk ansprechbar ist (LAN oder WLAN).
> - Einen **IT-Partner**, der: eine Middleware aufsetzt, die Verbindung zwischen Kasse und Terminal herstellt.

> **Anmerkung**
>
> **Hinweis**
>
> **Technische Details zur Anbindung über die Xentral API:**
>
> Für die technische Umsetzung der Kartenterminal-Anbindung über eine Middleware stellt Xentral eine standardisierte Webhook-Schnittstelle bereit. Alle notwendigen Informationen zur Struktur, dem Webhook-Typ und dem erwarteten Payload findest du in der offiziellen API-Dokumentation.
>
> - Beschreibung des Webhook-Typs für Kartenzahlungen
> - Payload-Details (z. B. Betrag, Währung, Vorgangsart)
> - Beispiele für die Integration mit externer Middleware
> - Hinweise zur Authentifizierung und Absicherung
>
> **Zur technischen API-Dokumentation:** developers.xentral.com – Webhook:Terminal Integration (Credit Debit Card Terminal)
>
> Empfohlen für: IT-Partner, Entwickler und Dienstleister, die die technische Anbindung eines Kartenterminals planen oder umsetzen möchten.

> **Tipp**
>
> **Anbindung Mollie **: Die Anbindung an Mollie ist über den Xentral Partner ** ditegra **möglich. Für Anfragen kannst du dich mit dem Betreff ** Xentral & Mollie Terminal**direkt über dasKontaktformular bei ditegraals Interessent melden.

##### Was du über Terminals & Payment Provider wissen solltest (SMB-Guide)

Damit Kartenzahlungen funktionieren, brauchst du zwei Dinge:

1. **Ein Kartenterminal (Hardware): **

1.** Einen Payment Provider (Dienstleister): **>** Anmerkung**
>
> **Warum das wichtig ist:** Nicht jedes Terminal lässt sich automatisch ansteuern. Es muss eine sogenannte „Schnittstelle“ (API oder Netzwerkprotokoll) unterstützen. Dein Payment Provider kann dir sagen, ob das Terminal geeignet ist – oder dir eines empfehlen, das passt.

#### Kartenterminal ohne Anbindung an die Kasse – So läuft es in der Praxis mit Xentral

Auch ohne direkte Anbindung an Xentral POS kannst du ein Kartenterminal problemlos im Tagesgeschäft nutzen. In kleinen und mittleren Unternehmen ist das eine gängige Praxis – einfach, zuverlässig und sofort einsetzbar.

**So funktioniert es:**

1. Du gibst den Zahlbetrag ganz normal in Xentral POS ein und druckst den Beleg (korrekte Zahlungsweise beachten, z.B. Kreditkarte).
1. Danach **tippst du den gleichen Betrag manuell** ins Kartenterminal ein.
1. Der Kunde bezahlt mit Karte oder Smartphone.
1. Du erhältst einen Zahlungsbeleg vom Terminal – dieser wird **nicht** automatisch in Xentral übernommen.
1. In Xentral wurde der Verkauf als „bezahlt per Kreditkarte“ auf den Beleg ausgedruckt.

> **Tipp**
>
> **Kartenzahlung zuerst am Terminal, dann im POS erfassen:**
>
> Du kannst die Zahlung auch **zuerst direkt am Kartenterminal durchführen**– unabhängig von der Kasse. Sobald die Zahlung erfolgreich war, wählst du im Xentral POS einfach die passende Zahlungsart (z. B. EC-Karte oder Kreditkarte) aus und schließt den Verkauf ab.
>
> Dein Vorteil:
>
> - Du **vermeidest Stornos**, falls: die Karte nicht funktioniert, der Kunde doch bar zahlen will, die Zahlungsart am Terminal wechselt (z. B. von EC zu Kreditkarte).
> - Der Bezahlvorgang bleibt flexibel – die Kasse wird erst nach erfolgreicher Zahlung belastet.

| Vorteile | Nachteile |
| --- | --- |
| Kein technischer Aufwand Funktioniert sofort mit jedem Kartenterminal Unabhängig vom Modell oder Provider | Die Zahlung und der Kassenvorgang sind nicht automatisch verknüpft Du musst sicherstellen, dass Betrag und Zahlung manuell korrekt übertragen werden Keine automatische Rückmeldung an Xentral bei Storno oder Fehlern |

> **Anmerkung**
>
> **Fazit**: Ideal für einfache Setups oder als Übergangslösung – vor allem, wenn du schnell starten willst oder keine Middleware zur Verfügung steht.

## FAQ

### Ist es möglich, dass der Betrag bei Kartenzahlung direkt auf dem Kartenlesegerät angezeigt wird, ohne dass er händisch eingegeben werden muss?

**Antwort**:

Aktuell ist die direkte Übergabe des Betrags an ein Kartenlesegerät (z. B. EC- oder Kreditkartenterminal) in der neuen Xentral POS noch nicht nativ integriert.

Stattdessen erfolgt die Eingabe des Zahlungsbetrags manuell direkt am Terminal durch das Kassenpersonal. Diese Vorgehensweise ist im aktuellen MVP-Stand vorgesehen, um eine einfache und flexible Nutzung unabhängig von bestimmten Geräten zu ermöglichen.

**Geplant**:

Eine erweiterte Anbindung über Webhooks ist bereits technisch vorbereitet. In einem späteren Release soll die Integration von kompatiblen Geräten über Connect erfolgen, sodass Beträge automatisiert an das Terminal übertragen werden können – inkl. Rückmeldung an Xentral zur Zahlungsbestätigung.

In einer Cloud-Umgebung ist eine automatische Anbindung an Kartenterminals nicht für alle Anbieter möglich, da es keine einheitlichen Standards gibt und jedes Terminal eigene Schnittstellen und Anforderungen an Sicherheit und Netzwerkanbindung stellt.

> **Anmerkung**
>
> Du kannst dein Terminal heute schon über eine individuelle API-Anbindung oder Partnerlösung integrieren – sprich dafür bitte mit deinem IT-Dienstleister oder Xentral-Partner.

### Kann ich mit dem POS-System Staffelpreise und individuelle Preise für Kundengruppen nutzen?

In den POS Projekt-Einstellungen findest du das Feld „Preisgruppe bevorzugt“. Hier legst du fest, welche Preisgruppe im POS verwendet werden soll (z.B. B2B). Dadurch werden beim Verkauf nur die Preise dieser ausgewählten Gruppe angezeigt und angewendet – zum Beispiel spezielle Konditionen für Stammkunden, Händler oder bestimmte Kundensegmente.