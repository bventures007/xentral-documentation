PARCEL.ONE ist ein Anbieter von internationalen bzw. ausländischen Versanddienstleistern. In diesem Artikel erfährst du, wie du die Schnittstelle PARCEL.ONE an xentral anbinden und nutzen kannst. Weitere Informationen zum Versanddienstleister PARCEL.ONE erhältst du unter[https://parcel.one/.](https://parcel.one/)

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du[hier](https://help.xentral.com/hc/articles/360016722580#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

## Features

PARCEL.ONE bietet dir folgende Features:

- Angabe von Zolldokumenten
- Individuelle Angaben zu Spediteur und Produkt
- Sandbox Anbindung

## Anbindung von PARCEL.ONE an xentral

Um PARCEL.ONE an xentral anbinden zu können, benötigst du eine Kundennummer und ein Kennwort. Diese sind die Voraussetzung für den API-Zugriff. Du erhältst sie bei deinem Geschäftskundenbetreuer bei PARCEL.ONE.

## Einstellungen in xentral

Zur Schnittstelle PARCEL.ONE kannst du in xentral verschiedene Einstellungen vornehmen. Dazu richtest du zunächst unter Administration → Einstellungen → Versandarten → "+NEU" → PARCEL.ONE als Versandart in xentral ein:

![parcelone1.png](https://help.xentral.com/hc/article_attachments/5009654587804)

Trage die gewünschten Einstellungen in folgenden Feldern ein:

- **Bezeichnung** → Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ** → Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du Voreinstellung bei
- **Modul** → Wähle "Parcelone" aus dem Drop-Down Menü aus
- **Projekt** → Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene PARCEL.ONE Versandart angelegt wird
- **Aktiv** → Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck** → Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke** → Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Paketmarken druckt
- **Drucker Export** → Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail** → Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Kundennummer** → Gib deine PARCEL.ONE Kundennummer ein
- **Passwort** → Gib dein PARCEL.ONE Passwort ein
- **Absender Land** → Gib das Absenderland als zweistelligen ISO-Code ein, bspw. "DE" für Deutschland und "AT" für Österreich
- **Zolldokumente** → Wähle aus dem Drop-Down Menü die Zolldokumente aus, die du benötigst. Benötigst du keine, wähle "Nicht benötigt"
- **Referenz 1**→ In dieses Feld kannst du zusätzliche Referenzen, die auf dem Etikett erscheinen, eintragen. Folgende Platzhalter kannst du zur Individualisierung der Texte nutzen: *{LIEFERSCHEIN}, {AUFTRAG}, {PROJEKT}, {IHREBESTELLNUMMER}, {INTERNET}*-**Referenz 2**→ Fülle hier ein weiteres Referenzfeld aus, das auf das Label gedruckt wird. Folgende Platzhalter kannst du zur Individualisierung der Texte nutzen: *{LIEFERSCHEIN}, {AUFTRAG}, {PROJEKT}, {IHREBESTELLNUMMER}, {INTERNET}*-**Spediteur & Produkt** → Wähle aus dem Drop-Down Menü Spediteur und Produkt aus
- **Standardgewicht** → Trage das Standardgewichts einer Sendung in kg ein
- **Tracking übernehmen** → Durch Anhaken dieses Felds kannst du das Scannen der Tracking-Nummer von der Paketmarke überspringen. Diese wird dann von xentral automatisch ausgewählt und eingetragen
- **Sandbox Anbindung** → Die Sandbox ist eine Testpaketmarke. Durch Anhaken erscheint dann auf dem Barcode groß das Wort "Sandbox", um die Paketmarke als Testmarke zu kennzeichnen

Nach einem erstmaligen Speichern über die "Speichern"-Schaltfläche unten rechts, werden deine Kundennummer und das dazugehörige Passwort geprüft. Fehlerhafte Zugangsdaten werden mit einer Fehlernachricht gemeldet.

Diese sieht dann so aus:

![parcelone2.png](https://help.xentral.com/hc/article_attachments/5009723504668)

Überprüfe dann nochmal deine Kundennummer und dein Passwort zu deinem PARCEL.ONE Account auf Richtigkeit.

Stimmen die Daten dagegen, stehen dir im Feld “Spediteur & Produkt” die von PARCEL.ONE bereitgestellten Versandoptionen zur Auswahl. Diese können allerdings von den hier abgebildeten Optionen abweichen:

![ParcelOne-3.png](https://help.xentral.com/hc/article_attachments/5009709856156)

Du kannst lediglich eine Option aus dem Drop-Down Menü auswählen. Möchtest du deine Sendungen über verschiedene Produkte oder Spediteure liefern lassen, lege weitere Versandarten vom Modul “parcelone” an.

Nachdem du ein Produkt gewählt hast, speichere die Einstellungen erneut über die "Speichern"-Schaltfläche.

## Paketmarke drucken

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Paketmarkendruck im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Wähle dazu im Lieferschein im Reiter "Lieferschein" die Versandart "PARCEL.ONE" aus dem Drop-Down Menü aus:

![parcelone3.png](https://help.xentral.com/hc/article_attachments/5009654625948)

Klicke auf die **Speichern** Schaltfläche, bevor du in den Paketmarkendialog navigierst.

Klicke im Anschluss im Lieferschein auf den Reiter **Paketmarke ** und drucke über**Paketmarke drucken** eine Paketmarke für die enthaltenen Artikel.

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss die Paketmarke im PARCEL.ONE-Geschäftskundenportal stornieren.

### Weitere Services

Im Lieferschein stehen dir, abhängig vom gewählten Produkt, weitere Services zur Auswahl, welche du für deine Sendung anwählen kannst.

**Sendungsvernichtung ** Durch Anhaken des Felds "Sendungsvernichtung" stimmst du zu, dass die Sendung nicht zurück versendet, sondern vernichtet wird, wenn der Adressat das Paket nicht annimmt. Damit kannst du Rücksendekosten vermeiden. **Retourelabel ** Durch Anhaken des Services "Retourelabel" wird vorab ein Retourelabel für die Sendung gedruckt, welches du dann vor dem Versenden dem Paket beilegen kannst. **Transportversicherung 255 EUR ** Das Feld "Transportversicherung 255 EUR" bietet dir die Option einer Transportversicherung für deine Sendung. Diese ist auf 255 € bei Sendungen mit dem Service „Höherversicherung“ begrenzt. **Einzelretoure**

Das Feld "Einzelretoure" ist hilfreich für dich, wenn du nur hin und wieder Retouren zu verzeichnen hast oder ein Empfänger eine Sendung ohne PARCEL.ONE Retourenlabel an PARCEL.ONE zur Rückbeförderung weiterleitet. In beiden Fällen erhebt PARCEL.ONE den Zuschlag Einzelretoure, unabhängig vom mit dem Versender vereinbarten Porto für Retourensendungen. Wichtig ist, dass du je nach Lieferadresse des Kunden ein entsprechendes Retourenlabel ausstellst, z.B. DHL für Deutschland, Post AT für Österreich.

Im Anschluss kannst du die Tracking-Nummer einscannen und bestätigen:

![ParcelOne-6.png](https://help.xentral.com/hc/article_attachments/5009710723612)

Eine Testpaketmarke (Sandbox) sieht dann so aus:

![ParcelOne-7.png](https://help.xentral.com/hc/article_attachments/5009695052956)