Auf dieser Seite findest du eine Übersicht der häufigsten bekannten Probleme in Xentral, ergänzt um kurze Lösungen oder Workarounds.

Diese Liste wird regelmäßig aktualisiert und dient als erste Anlaufstelle, bevor du den Support kontaktierst.

## 1. Login, Benutzer Rechte

## 2. Belege & Dokumente

### Warum kann ich bei einer neuen Zahlungsweise vom Typ „Rechnung“ keine eigenen Tage und Skonto hinterlegen - sondern nur in den Systemeinstellungen?

**Problem: ** Bei neu angelegten Zahlungsweisen, die sich wie „Rechnung“ verhalten (z. B. „rechnung_b2b“), können die Felder für Zahlungsziel (Tage) und Skonto nicht individuell befüllt werden. Die Eingabe ist nur in den zentralen Firmeneinstellungen unter Administration → Einstellungen → Firma möglich.** Hintergrund: ** Xentral zieht die Standardwerte für Zahlungsziel und Skonto aktuell global aus den Firmeneinstellungen, nicht aus den einzelnen Zahlungsweisen. Das bedeutet: Wenn du mehrere Varianten vom Typ „Rechnung“ anlegst, teilen sich alle dieselben zentral hinterlegten Werte.** Workaround / Lösung:**

- Hinterlege die Standard-Tage und das Standard-Skonto in den Firmeneinstellungen.
- Falls du für bestimmte Kunden oder Projekte abweichende Werte brauchst, nutze die Felder Zahlungsziel und Skonto direkt in der Kundenadresse oder im Projekt. Diese überschreiben die globalen Firmeneinstellungen für den jeweiligen Beleg.
- Für komplexere Konstellationen (z. B. B2B/B2C mit unterschiedlichen Konditionen) kann es nötig sein, zusätzlich mit Projekten oder Preisgruppen zu arbeiten.

**Status:**

Das Verhalten ist bekannt und systembedingt. Eine direkte Einstellung pro Zahlungsweise vom Typ „Rechnung“ ist aktuell nicht vorgesehen.

### Wie kann ich Bestellungen von den Kanarischen Inseln korrekt als Drittland besteuern, obwohl sie Teil von Spanien sind?

**Problem: ** Bestellungen von den Kanarischen Inseln werden in Xentral standardmäßig wie Lieferungen innerhalb Spaniens behandelt (ISO: ES) und somit als EU-Lieferung besteuert. Eine getrennte Länderkonfiguration für die Kanaren (z. B. ES-CN mit Drittland-Besteuerung) kann seit 2024 nicht mehr eigenständig in die Länderliste eingetragen werden.** Hintergrund: ** Die Kanarischen Inseln gehören zwar politisch zu Spanien, gelten steuerrechtlich jedoch als Drittland. Im aktuellen Xentral-Standard gibt es keine Möglichkeit, sie als separates Land mit eigener ISO-Kennung zu hinterlegen.** Workaround / Lösung:**

- Setze den Auftrag in Xentral manuell von EU-Lieferung auf Export, damit die Besteuerung korrekt als Drittland erfolgt.
- Alternativ kann eine individuelle Anpassung oder ein Mapping im Importprozess erfolgen, um Bestellungen mit der Region „Kanaren“ automatisch auf Export zu setzen (nur per technischer Umsetzung möglich).

**Status:**

Das Verhalten ist bekannt und systembedingt. Eine direkte ISO-Ländercodierung für „ES-CN“ ist derzeit nicht im Standard verfügbar.

## 3. Zahlungen & Zahlungsweisen

## 4. Artikel, Lager & Bestände

## 5. Versand & Logistik

## 6. Einkauf & Lieferanten

## 7. Schnittstellen & Import/Export

### Warum wird beim Connect Shopimport immer automatisch auch die Lieferadresse befüllt, obwohl sie identisch zur Rechnungsadresse ist?

**Problem: ** Beim Import von Bestellungen aus einem angebundenen Shop (Connect) wird in Xentral aktuell automatisch die Lieferadresse mit den gleichen Daten wie die Rechnungsadresse gefüllt – auch dann, wenn im Shop gar keine abweichende Lieferadresse hinterlegt ist.** Hintergrund:**

Das Verhalten entsteht, weil die Shop-Schnittstelle beim Import standardmäßig immer ein Lieferadress-Objekt mitliefert. Auch wenn die Daten identisch sind, schreibt Xentral diese beim Auftrag an die Lieferadresse.

Es gibt derzeit keine automatische Prüfung, ob Rechnungs- und Lieferadresse identisch sind.

Workaround / Lösung:

- Prüfe im Shop, ob eine Einstellung existiert, die das Mitsenden der Lieferadresse nur bei Abweichung erlaubt (abhängig vom Shopsystem).
- Falls das Shopsystem diese Möglichkeit nicht bietet, kannst du in Xentral die Lieferadresse manuell leeren oder anpassen, wenn keine Abweichung benötigt wird.
- Bei automatisierten Prozessen kann alternativ ein individueller Import-Filter oder ein Mapping-Skript eingesetzt werden, das identische Adressen unterdrückt (nur mit technischer Anpassung möglich).

**Status:**

Das Verhalten ist bekannt und technisch durch den Standardimport bedingt.

## 8. System & Performance

> **Tipp**
>
> Falls dein Problem hier nicht gelistet ist oder die vorgeschlagene Lösung nicht greift, wirf einen Blick in die FAQ & Supportdokumentation oder kontaktiere unser Support-Team.