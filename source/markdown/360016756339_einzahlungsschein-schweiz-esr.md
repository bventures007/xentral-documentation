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

Der Einzahlungsschein mit Referenznummer (kurz: ESR, auch als Oranger Einzahlungsschein bezeichnet) ist ein in der Schweiz gebräuchlicher Zahlschein, der es ermöglicht, offene Rechnungen in Schweizer Franken und Euro zu fakturieren und Zahlungseingänge rasch zu verbuchen. Es wird von allen Banken und der Schweizer PostFinance angeboten.

![PaymentSlipISR1.png](https://help.xentral.com/hc/article_attachments/5033327334812)

Das Xentral-Modul "Einzahlungsschein Schweiz" (techn. Name: paymentslip_swiss) ermöglicht die Eintragung der Referenznummern und Bankinformationen als System- oder Projekteinstellung. Für Empfänger von Sendungen in der Schweiz (Lieferland) wird der ESR durch Aufruf der Rechnung oder im Zuge des Autoversandes als Rechnungsanhang mit erstellt und kann dann auch automatisch versendet werden.

## Einstellungen

### Systemweite Einstellungen

Auf Systemebene können die folgenden Daten für die Erstellung des ESR gepflegt werden:

**Einstellungen **

-** Modul aktivieren:** Aktivieren / Deaktivieren des Moduls (siehe auch Projekteinstellungen)
- **ESR-Identifikationsnummer: ** Die eigene ESR-ID-Nummer zur Identifikation des Rechnungsstellers. Sie erhalten diese von Ihrer Bank.** Begünstigtenbank **

-** ESR-Teilnehmernummer:** Die ESR-Nummer der Bank. Diese werden von der Bank erhalten.
- **Bankname:** Name der Bank
- **Bank PLZ/Ort:** Postleitzahl und Ort der Bank

### Projekteinstellungen

Auf Basis der Projekte lässt sich die Einstellung des Systems überschreiben, z.B. um für einzelne Projekte andere Bankdaten zu hinterlegen.

Dabei stehen für jedes Projekt drei Optionen zur Auswahl:

- **Deaktiviert:** Schaltet den ESR für dieses Projekt aus
- **Aktiv:** Aktiviert den ESR mit den hier im Projekt hinterlegten Einstellungen
- **Systemeinstellungen verwenden:** Aktiviert den ESR für dieses Projekt mit den systemweit hinterlegten Einstellungen

### Einstellung: Details und Feldbedeutung

Die folgenden Details müssen beim ESR befüllt werden, um einen standardkonformen Einzahlungsschein auf der Projektebene generieren zu können.

**Einstellungen **

-** Modul aktivieren:** Aktivieren / Deaktivieren des Moduls
- **ESR-Identifikationsnummer: ** Die eigene ESR-ID-Nummer zur Identifikation des Rechnungsstellers. Sie erhalten diese von Ihrer Bank.** Begünstigtenbank **

-** ESR-Teilnehmernummer:** Die ESR-Nummer der Bank. Diese werden von der Bank erhalten.
- **Bankname:** Name der Bank
- **Bank PLZ/Ort:** Postleitzahl und Ort der Bank

## Anwendung

Bei Erstellung oder Änderung einer Rechnung mit dem Lieferland Schweiz wird im Rechnungsmodul automatisch der entsprechende ESR als Dateianhang erstellt. Dieser wird auch bei Änderung von Rechnungsdaten jeweils sofort aktualisiert.

Der ESR befindet sich im Reiter Dateien im Modul Rechnung.

Beim Versand einer Rechnung (z.B. per E-Mail) kann der Anhang mitgeschickt werden.

Die Rechnung und der ESR erscheinen dann beim Empfänger in Form von zwei separaten Dateianhängen.

![PaymentSlipISR2.png](https://help.xentral.com/hc/article_attachments/5033344319388)