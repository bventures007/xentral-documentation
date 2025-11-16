Lieferantenstammdaten sind das Fundament für Einkauf und Beschaffung. Jeder Bestellprozess, jede Eingangsrechnung und jede Zahlung hängt davon ab, dass der Lieferant korrekt angelegt ist. Ohne Bankverbindung kann nicht bezahlt werden, ohne Zahlungsziel keine korrekte Rechnungsprüfung.

## Lieferant anlegen – Schritt-für-Schritt Logik

Das Anlegen eines Lieferanten erfolgt im Adressenmodul. Jeder Lieferant ist hier ein eigener Datensatz, der anschließend für Bestellungen, Eingangsrechnungen und Zahlungen genutzt wird.

### Neue Adresse anlegen **Schritte**:

1. Neue Adresse anlegen:
  - Gehe zu **Verkaufen **>** Adressen ** und klicke auf**+ Neu**.
1. Basisdaten eingeben:
  - Trage die **Stammdaten** ein (Name, Telefon, E-Mail, ggf. USt-ID, Steuernummer).
  - Füge bei Bedarf eine abweichende Lieferadresse für die Anlieferung hinzu.
  - **Projektzuordnung **: Trage das entsprechende Projekt ein - um eine Lieferantennummer aus dem Nummernkreis zuzuordnen, um den Lieferanten einem Kanal zuzuordnen. ** Standardprojekt und zentraler Nummernkreis sind bei Lieferanten oft ausreichend.**

1. Adresse speichern:
  - Klicke auf **Speichern**, um den Datensatz anzulegen.
1. Adresse als Lieferant kennzeichnen:
  - Aktiviere im Bereich **Rollen ** den Haken "**Ist Lieferant **" und ** speichere**.
  - Eine **Lieferantennummer ** wird **automatisch** vergeben (global oder projektspezifisch).

## Stammdaten (Basisdaten des Lieferanten)

Pflichtfelder sind **Name/Firma **, ** Straße **, ** PLZ/Ort ** und **Land **. Zusätzlich kannst du ** Ansprechpartner **für den ** Einkauf **eintragen oder eine interne ** Lieferantennummer **vergeben. Besonders wichtig: Die „** Kundennummer bei Lieferant**“. Viele Lieferanten ordnen Bestellungen ausschließlich über diese Nummer zu. Wenn du sie nicht einträgst, kommt es leicht zu Verzögerungen.

Optionale, aber wichtige Felder:

- Ansprechpartner, Abteilung, Adresszusatz (z. B. „Tor 3, Warenannahme“)
- Lieferbedingungen (müssen vorher im Modul Lieferbedingungen angelegt sein)
- Abweichende Rechnungsadresse → z. B. wenn Bestellungen ins Lager gehen, Rechnungen aber an die Buchhaltung
- GLN (nur nötig bei EDI-Anbindungen)

## Kontaktdaten

Auch beim Lieferanten ist die E-Mail-Adresse Pflicht, wenn du Bestellungen per Mail verschickst. Trage am besten eine Funktionsadresse (z. B. einkauf@lieferant.de) ein. So stellst du sicher, dass Bestellungen auch ankommen, wenn ein Mitarbeiter im Urlaub ist.

## Zahlungskonditionen und Besteuerung

Die Konditionen kommen meist aus der Lieferantengruppe: „Rechnung, 30 Tage netto, 2 % Skonto bei 10 Tagen“. Trage hier die vereinbarten Ziele ein.

Bei der Besteuerung gilt:

- Inlandslieferant → normale MwSt.
- EU-Lieferant mit USt-ID → Reverse-Charge (keine MwSt. auf der Rechnung, aber Versteuerung im Inland)
- Drittland → Import, Zollinformationen erforderlich

> **Tipp**
>
> Prüfe die Konditionen mit Finance ab. Wenn Einkauf 14 Tage einträgt und Finance 30 Tage, entstehen unnötige Skontoverluste.

## Bankverbindung (Pflicht)

Ohne Bankdaten keine Zahlungen. Darum ist dieser Bereich bei Lieferanten obligatorisch. Trage IBAN, BIC, Bankname und Inhaber immer sofort ein. Optional kannst du auch PayPal oder Fremdwährungen hinterlegen.

## Versand- und Logistikoptionen

Lieferanten unterscheiden sich oft stark in ihrer Versandabwicklung. Trage Standardlieferzeit, Standardlieferart (Spedition, Paketdienst) und Porto-Regeln sauber ein. Wenn der Lieferant Konsignationslager führt, kannst du das hier kennzeichnen.

Beispiel: Ein Lieferant liefert Standardware in 2 Tagen mit Paketdienst, Maschinen aber nur mit Spedition in 5 Tagen. Wenn du beides pflegst, können Bestellungen realistisch geplant werden.

## Weitere Stammdaten

Hinweistexte für Bestellungen, interne Bemerkungen oder Freifelder nutzt du nach Bedarf. Auch hier gilt: Alles, was du einmal sauber einträgst, spart später Nacharbeit.

## Typische Fehler und Best Practices

- Bankdaten fehlen → Zahlung blockiert.
- Keine Kundennummer bei Lieferant eingetragen → Bestellung nicht zuordenbar.
- Falsche USt-ID → führt zu Problemen bei der Reverse-Charge-Buchung.
- Kontaktperson fehlt → Rückfragen verzögern Bestellungen.

> **Tipp**
>
> Praxiswissen: Während beim Kunden Bankdaten optional sind, sind sie beim Lieferanten Pflicht. Umgekehrt ist beim Kunden die USt-ID kritisch, beim Lieferanten eher die Kundennummer.