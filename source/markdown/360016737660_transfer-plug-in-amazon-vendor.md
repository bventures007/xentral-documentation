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

## Amazon Vendor

Mit Hilfe der Amazon Vendor-Schnittstelle können Lieferungen für das Amazon Vendorenprogramm bearbeitet werden. Voraussetzung ist das Übertragungen Modul.

Dazu ist es möglich Bestellungen von Amazon zu empfangen und zu verarbeiten (ORDER). Nach Abschluss der Lieferung kann gegenüber Amazon angerechnet werden (INVOICE).

Die Datenübertragung erfolgt z.B. mit SFTP.

## EDI-Verbindung

EDI Messages sind in in Codezeilen unterteilt, in denen jeweils genau definierte Daten übermittelt werden.

### UNB: Kommunikationspartner

Die UNB Zeile definiert unter anderem den Empfänger und Absender. Das "Gegenüber" erwartet hier meist ein "weltweit" eindeutiges Kennzeichen für den Kommunikationspartner. Dafür existieren verschiedene Möglichkeiten:

- Quasi-Standard ist hier eine GLN (Global Location Number, früher auch ILN) aus dem GS1 System (vormals EAN System), die in Deutschland von der[GS1.de](https://gs1.de/) verwaltet wird. Diese GLN UNB ID Typ "14" ist aber nur eine Möglichkeit von vielen.
- Für einen schnellen Start und wenn die Schnittstellte selbst entwickelt wird kann als UNB-ID auch der Typ "9" gewählt werden, dort wird die DUNS Nummer (auch D-U-N-S, kurz für Data Universal Numbering System) erwartet, die unter[https://www.upik.de/upik_suche.cgi](https://www.upik.de/upik_suche.cgi) abgefragt werden kann. Alle Kapitalgesellschaften bekommen nach Anmeldung bei den entsprechenden Behörden automatisch eine DUNS-Nummer zugewiesen.
- Zuletzt besteht auch die Möglichkeit die Telefonnummer mit intl. Vorwahl und als UNB-ID Typ "12" zu verwenden.

### Übertragungsstandard EDI / EDIFACT

Bei EDI/EDIFACT wird so gut wie alles mit Codelisten übertragen, denn das Protokoll stammt aus den 1980er Jahren wo jedes Byte noch teuer war. Dafür existieren einige Quellen, die das Format erläutern und den Umgang damit aufzeigen:

- Einen guten Einstieg bekommt man unter[https://www.stylusstudio.com/edifact/](https://www.stylusstudio.com/edifact/)
- etwas komplizierter aber dafür sehr umfangreich[https://service.unece.org/trade/untdid/d96a/trmd/orders_t.htm](https://service.unece.org/trade/untdid/d96a/trmd/orders_t.htm)

Die Datenübertragung erfolgt z.B. mit SFTP ausschließlich per keyfile (ssh pub-key). Die EDI-Datei an sich ist eine reine Textdatei, idealerweise codiert in UTF8 - das ist aber nicht zwingend im Standard vorgeschrieben. Wird eine Datei vom Gegenüber gesendet die nur eine eine Zeile enthält, kann das EDI Satzendzeichen ' (einfaches Anführungszeichen, das wird im UNA Segment definiert) durch ein LF bzw. CR/LF ersetzen damit wird die Struktur sehr gut lesbar. Bestimme Segmente können in EDI mehrfach vorkommen und haben dann evtl. eine unterschiedliche Bedeutung z.B. Daten im Kopf (Header) und auf Positions-Ebene.

Beispiel ORDER

Zum schnellen Start in das Thema haben wir ein paar Segmente in einer ORDER zusammengefasst - so lässt sich schnell verstehen, wie eine ORDER zu parsen wäre.

BGM+220+4HQ7EBLG+9' → Bestellung mit PO Nummer 4HQ7EBLG, → die 9 am Schluss bedeutet es werden die EAN/GS1 Codelisten verwendet DTM+137:20190107:102' → Belegdatum im Format 102 DTM+63:20190111:102' → Lieferdatum spätestens im Format 102 DTM+64:20190107:102' → Lieferdatum frühestens im Format 102

Benötigt wird das GLN Verzeichnis aus dem Vendor-Central, damit die Lieferadressen zugeordnet werden können.

NAD+BY+5450534000017::9' → Käufer, GLN Codiert NAD+SU+4016428000009::9' → Lieferant, hier wird die eigene UNB-ID wieder angegeben NAD+DP+5450534002325::9+++++++DE' → Lieferadresse mit Land NAD+IV+5450534005838::9++AMAZON EU SARL:NIEDERLASSUNG DEUTSCHLAND+MARCEL-BREUER-STR. 12+MUENCHEN++80807+DE' → Rechnungsadresse als GLN und Klartext muss in der INVOICE Message auch komplett → im Klartext übertragen werden.

Im Folgenden (ab LIN) beginnen die Positionen, zwischen NAD und LIN können noch weitere Zeilen kommen z.B. RFF (Referenz jeweils zum aktuellen Element) und CUX (hier wird die Währung definiert).

Jedes LIN definiert den Beginn einer neuen Position an (LIN+1, LIN+2, LIN+3 usw.) LIN+1++4016428352115:EN' → Artikel Pos 1 mit Artikel EAN, EN=Datenherkunft EAN, könnte evtl. auch SA sein QTY+21:52' → Pos Menge in Stück PRI+AAA:55.9' → Preis pro Stück netto

Im Anschluss folgen noch Rahmendaten die vor allem der Validierung dienen:

- Mit UMS+S beginnt der Summenblock, der mit Hilfe verschiedener Summen eine Validierung ermöglicht.
- Sollten mehrere Belege ein einer UNB Übertragung enthalten sein, folgen diese nun durch ein UNH bzw. BGM getrennt wieder mit dem Belegkopf.