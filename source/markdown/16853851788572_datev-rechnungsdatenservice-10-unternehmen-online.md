Der DATEV Rechnungsdatenservice 1.0 ermöglicht dir, Belege wie Rechnungen und Gutschriften direkt und automatisch aus deinem Xentral-System in DATEV Unternehmen online zu übertragen. Dabei werden sowohl Belegbilder als auch wichtige Daten (z. B. Betrag, Datum, Lieferant) ohne manuellen Aufwand übermittelt.

Für dich bedeutet das eine große Zeitersparnis: Alle relevanten Rechnungsdaten landen strukturiert und korrekt im DATEV-System und stehen dort direkt für die Buchhaltung bereit. So sparst du Aufwand und minimierst Fehler bei der Dateneingabe.

![DATEV_unternehmenonline_xml_Workflow_kurzueberblick.png](https://help.xentral.com/hc/article_attachments/18155702396956)

Der DATEV Rechnungsdatenservice 1.0 ermöglicht dir, deine Buchhaltungsbelege (Rechnungen, Gutschriften, Verbindlichkeiten) direkt per API zu DATEV zu exportieren. Der Export wird dabei automatisch von Xentral an DATEV übertragen. Alle Exporte werden in einer Übersichtstabelle angezeigt.

> **Anmerkung**
>
> Xentral unterstützt die Verbindung mit dem **DATEV Rechnungsdatenservice in Version 1.0**. Die neuere Version 2.0 wird aktuell nicht unterstützt.

## Schnellstart: Einrichtung und Export mit Rechnungsdatenservice 1.0 **Schnellstart Schritte:**

1. Gib die Daten für die [Initiale Stammdaten-Einrichtung](https://help.xentral.com/hc/de/articles/360016725100#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e_section-idm2346058023653) für die Übertragung ein und speichere sie ab. Z.B. Mandanten und Beraternummer.
1. Verbinde Xentral mit DATEV über[**SmartLogin** oder **DATEV SmartCard / DATEV mIDentity**.](#UUID-a0703471-aeb2-3876-7f6a-6b407c12941d_section-idm23462696315916)
1. [**Exportiere** die Daten zu DATEV Unternehmen Online](#UUID-a0703471-aeb2-3876-7f6a-6b407c12941d_section-idm234628144591797) indem du einen **Belegtyp ** auswählst und einen **Datumsbereich ** angibst und den**Export startest**.
1. [Erweiterte Einstellungen](#UUID-a0703471-aeb2-3876-7f6a-6b407c12941d_section-idm234628128546799): Wähle den Account aus, wähle für Verbindlichkeiten das Eingangs- oder Rechnungsdatum des Belegs aus.

### Achtung

Dein Steuerberater benötigt Administrationsrechte in DATEV, damit die Verbindung reibungslos funktioniert. Eine Anleitung zur Konfiguration in DATEV findest du im folgenden Artikel im **DATEV Hilfe-Center**: '[Rechnungswesen 1.0 als Steuerberater in DATEV einrichten](https://apps.datev.de/help-center/documents/1007329)'.

## Verbindung mit DATEV Rechnungsdatenservice 1.0

Das Modul **DATEV Rechnungsdatenservice 1.0 ** findest du über die Smart-Suche über** DATEV Rechnungsdatenservice 1.0 ** oder im Menü unter** Buchhaltung > DATEV Rechnungsdatenservice 1.0. **### Verbindung zu DATEV über SmartLogin oder DATEV SmartCard/ DATEV mIDentity ** Schritte: **

1. Klicke im Modul ** DATEV Rechnungsdatenservice 1.0**auf den Reiter: ** Einstellungen**.
1. Klicke auf **Authentifizieren**. Ein neuer Reiter öffnet sich in deinem Browser. Logge dich bei DATEV ein.
1. Wähle dein verwendetes **Anmeldeverfahren** aus:
1. Klicke auf **Weiter** und melde dich mit dem ausgewählten Anmeldeverfahren an.
1. Klicke auf **Ich stimme zu** um Xentral die Erlaubnis zu erteilen, Daten mit DATEV auszutauschen.
1. Die **Authentifizierung wird nun abgeschlossen ** und ein Authentifizierungstoken in Xentral hinterlegt. Du wirst zurück zum Reiter: **Einstellungen ** des Moduls **DATEV Rechnungsdatenservice 1.0** in deiner Xentral-Instanz weitergeleitet.

> **Anmerkung**
>
> Die Person, die sich in DATEV eingeloggt hat, wird im Reiter Einstellungen als **Token-Ersteller ** angezeigt. Die Gültigkeit des Tokens wird im Feld: **Token gültig bis** angezeigt.

## Datenübertragung zu DATEV über Rechnungsdatenservice 1.0

### Datenübertragung an DATEV konfigurieren (= Einstellungen)

Nachdem du die Verbindung zu DATEV hergestellt hast, kannst du im Reiter: **Einstellungen** die folgenden Kofigurationen vornehmen:

![DATEV_rechnungsdatenservice1_0_xentral_einstellungen_erweitert.png](https://help.xentral.com/hc/article_attachments/18155686018588)

| Feld | Beschreibung |
| --- | --- |
| **Import Benutzer** | Wenn du mehrerer Benutzer oder Firmen hast: Alle Benutzer, die mit dem genutzten DATEV-Konto verbunden sind, werden hier aufgelistet. Wähle hier das Unternehmen aus, für das du deine Belege exportieren möchtest. |
| Testzugang | Optional: Wähle diese Option, wenn du deine Belege testweise in die DATEV Sandbox exportieren möchtest, bevor du live gehst. |
| **Verbindlichkeit Datumsfilter **| Wähle aus, ob deine Verbindlichkeiten nach Eingangsdatum oder nach Rechnungsdatum exportiert werden sollen: -** Nach Eingangsdatum **: Eingangsdatumsfeld im Modul Verbindlichkeiten (Eingangsdatum in der Belegeingabe)<br>-** Nach Rechnungsdatum**: Rechnungsdatumsfeld im Modul Verbindlichkeiten (Rechnungsdatum in der Belegeingabe) |

### Belege an DATEV übertragen (= Export)

Du kannst deine Rechnungen, Gutschriften und Verbindlichkeiten direkt per API an DATEV exportieren – und das für einen **Zeitraum von bis zu einem Monat **. ** Schritte, um deine Belege via API zu DATEV zu exportieren:**

1. Klicke im Modul **DATEV Rechnungsdatenservice 1.0** auf den Reiter: ** Export**.
1. Wähle den **Typ ** des Belegs, den du exportieren möchtest: **Rechnungen **, ** Gutschriften ** und **Verbindlichkeiten** kannst du im Dropdown-Menü anwählen. Es kann jeweils nur ein Belegtyp gleichzeitig exportiert werden.
1. Wähle **Startdatum ** und **Enddatum** deines Exports. Achte darauf, dass sich der Exportzeitraum im selben Monat befindet. Z.B. 01.10.2024 bis 31.10.2024.
1. Klicke auf **Export**.
1. Der Export wird nun zu DATEV übertragen und mit einem **Zeitstempel ** und einem **Status** (Fehler oder Erfolgreich) in der untenstehenden Tabelle protokolliert.

Für j **eden erfolgten Export ** wird der **Zeitraum ** mit **Zeitstempel ** und**Status** in den Belegtabellen protokolliert. Zusätzlich kannst du eine CSV-Datei des Exports durch einen Klick auf Protokoll im jeweiligen Eintrag herunterladen. Diese Datei enthält Informationen zum Status der im Export enthaltenen Belege in DATEV.

![DATEV_Rechnungsdatenservice1_0_export_protokoll.png](https://help.xentral.com/hc/article_attachments/18155702433180)

> **Anmerkung**
>
> Das Protokoll ist nur für Xentral-Instanzen ab Version 24.14.6 verfügbar und nur für Exporte, die nach Update auf diese oder eine neuere Version durchgeführt wurden.

**Export Optionen auf einen Blick:**

| Feld | Beschreibung |
| --- | --- |
| **Typ **| Definiere, welche Datenkategorien exportiert werden sollen, z. B. ** Rechnungen **, ** Gutschriften **, ** Verbindlichkeiten**. Es kann jeweils nur ein Belegtyp gleichzeitig exportiert werden. |
| Projekt | Optional / Standardmäßig leer lassen: Das Projekt nur angeben, wenn du ausschliesslich einen Kanal exportieren möchtest. |
| **Startdatum **| Wähle einen Exportbereich aus, indem du ein ** Datum von ‘TT.MM.JJJJ**’ bis ‘TT.MM.JJJJ' angibst. Exportiere für DATEV z.B. den Zeitraum eines Monats für den Monatsabschluss. |
| **Enddatum **| Wähle einen Exportbereich aus, indem du ein ** Datum **von ‘TT.MM.JJJJ’** bis ‘TT.MM.JJJJ'** angibst. Exportiere für DATEV z.B. den Zeitraum eines Monats für den Monatsabschluss. |
| Bereits exportierte Dokumente ignorieren | Optional/ Besonderer Workflow: Ignoriert die bereits gezogenen Daten z.B. wenn du täglich exportierst kannst du die Daten von gestern ausschliessen. |

## Fehlerbehebung

Wenn eine Fehlermeldung angezeigt wird, stehen dir verschiedene Maßnahmen zur Verfügung. Weitere Informationen findest du in den[FAQ zum Buchhaltungsexport](https://help.xentral.com/hc/de/articles/10692093278492-FAQ-Finanzbuchhaltung-Export).

| Fehler | Fehlerbehebung |
| --- | --- |
| | Prüfe Beraternummer und Mandantennummer unter Finanzbuchhaltungsexport & Einstellungen. Authentifiziere anschließend erneut und versuche dich mit dem DATEV Rechnungsservice zu verbinden. |
| | Prüfe die Einstellungen in DATEV selbst. Hier sollten alle Berechtigungen korrekt gesetzt sein (z.B. Steuerberater). Manchmal hilft es auch wenn du die Berechtigungen in DATEV löschst und erneut vergibst. |
| | Kürze den Exportzeitraum, z.B. auf einen Tag. Manchmal können bei längeren Zeiträumen Probleme auftreten. |
| 'Error: invalid Grant' | Erneuere den Access Token. Der Token der DATEV API ist aus Gründen der Datensicherheit nur wenige Stunden gültig. Daher kann die Fehlermeldung angezeigt werden, dass die Zugangsdaten nicht korrekt sind (bzw. 'Error: invalid Grant'). |
| Fehler: In DATEV Unternehmen online ist kein Bestand angelegt oder Wirtschaftsjahr vorhanden | Erhältst du die Fehlermeldung: "Fehler: In DATEV Unternehmen online ist kein Bestand angelegt oder Wirtschaftsjahr vorhanden", sollte der für DATEV verantwortliche Mitarbeiter oder dein Steuerberater den DATEV Rechnungsservice 1.0 für Xentral aktivieren. In DATEV können sie dies auf die folgende Weise umsetzen: Deaktiviere DATEV Unternehmen online compact. Stelle die Bearbeitungsform von Standard auf Erweitert um. Schalte die Buchungsjahre für das jeweilige Jahr frei. Richte Rechnungsdatenservice 1.0 für den Xentral-Nutzer ein. |
| | DATEV akzeptiert bis zu 5000 Dateien pro Export mit einer maximalen Dateigröße von 20 MB. Der kleinste Zeitraum der aus Xentral exportiert werden kann, ist ein Tag. Daraus folgt, dass du maximal 5000 Dateien pro Tag zu DATEV hochladen kannst. Exportierst du deine Belege in mehrere Dateiformate, wie XML und PDF, verringert dies die Anzahl der Belege, die du hochladen kannst, da pro Beleg mehrere Dateien benötigt werden. Ein Workaround für dieses Problem ist, die Belege herunterzuladen, in Gruppen kleiner als 5000 einzuteilen und sie manuell über[Finanzbuchhaltung Export](#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6ehttps://help.xentral.com/hc/de/articles/360016725100-Finanzbuchhaltung-Export-DATEV-Export-Einstellungen#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e) hochzuladen. Du kannst die Belege in der App im Bereich Datev Unternehmen Online links unten hochladen. |