### Auftragsstatus Rückmelden

Das Rückmelden des Auftragsstatus ist nur bei FBM möglich. Es werden nur offene und nicht versendete Bestellungen an Amazon zurückgemeldet.

### Rechnungen

Bei FBA und FBM möglich: Ab der Version 20.1 ist der automatische Upload von Rechnungen zu Amazon möglich. Um den Rechnungsupload-Service zu aktivieren, setze den Haken beim Auswahlkästchen **Rechnungsupload-Service verwenden**. Der zeitliche Trigger zum Upload der Rechnung ist das Eintreffen der Versandinformation (Trackingnummer) in Xentral. Zusätzlich kannst du eine Zeitdifferenz einstellen, um sicherzustellen, dass die Rechnungen spätestens nach einer definierten Zahl an Tagen zu Amazon geladen werden, auch wenn kein Tracking-Code empfangen wurde. Beachte, dass nur Rechnungen hochgeladen werden, die den Status “versendet” haben. Das kannst du über die Projekteinstellungen oder bei Rechnungserstellung aus dem Übertragen-Modul auch einstellen.

Mit Hilfe des Datums im Feld "Upload Startdatum" kannst du auch rückwirkend bereits erstellte Rechnungen an Amazon übertragen.

![Amazon-15.png](https://help.xentral.com/hc/article_attachments/22381425902364)

### Erstellen von Rechnungen und Gutschriften

Im Folgenden wird erklärt, wie du Rechnungen und Gutschriften für Amazon in Xentral erstellen kannst.

#### Variante 1: Mit Verwendung des Amazon VAT Services

Amazon bietet die Möglichkeit, sich Rechnungen und Gutschriften direkt von Amazon (VAT Service) erstellen zu lassen. Das bedeutet, die Daten für die Rechnung (Rechnungsnummer, Umsatzsteuer, Beträge, etc.) kommen von Amazon und nicht aus Xentral. Wenn du die Rechnungen und Gutschriften auf Grundlage des VAT Service auch in Xentral erstellen willst so war bis zur Version 20.2 unsere Amazon Seller App notwendig. Ab der Version 20.3 brauchst du diese für die Nutzung des Amazon VAT Services nicht mehr. Bei Verwendung des VAT Services brauchst du keinen V2 Bericht. Verwendest du den VAT Service von Amazon, erstelle für die entsprechenden Aufträge in xentral keine Rechnungen oder Gutschriften, da diese aus Amazon übertragen werden.

![Amazon-16.png](https://help.xentral.com/hc/article_attachments/22381440070428)

> **Anmerkung**
>
> InXentral kannst du nur den normalen Amazon VAT-Service abbilden, nicht aber den Amazon VAT-Service light. Beim VAT-Service light wird nur die Berechnung der Umsatzsteuer von Amazon übernommen, wohingegen die Rechnung vom Kunden selbst erstellt und bei Amazon hochgeladen werden muss.

#### Variante 2: Ohne Verwendung des Amazon VAT Services

Du hast die Möglichkeit Rechnungen und Gutschriften aus den Aufträgen in Xentral zu erstellen.

Außerdem ist es dir auch möglich keine Rechnungen und Gutschriften für importierte Aufträge zu erzeugen. Das wäre beispielsweise möglich wenn du für die Erstellung der Rechnungen Amainvoice oder Amazon VAT Service verwendest.

![Amazon-17.png](https://help.xentral.com/hc/article_attachments/22381440070812)

Für die Erstellung von FBA-Gutschriften ist der Abrechnungsbericht V2 notwendig. Sollte der Abrechnungsbericht V2 nicht in deinem Amazon-Konto vorhanden sein, musst du diesen über den Amazon-Kundensupport freischalten lassen.

![Amazon-18.png](https://help.xentral.com/hc/article_attachments/22381440071196)

> **Anmerkung**
>
> Gutschriften werden standardmäßig mit dem Bezahldatum angelegt, nicht dem Importdatum.

### SKU Nummer / Fremdnummer pflegen

Um für Amazon eine Unterscheidung zwischen FBA und FBM Artikel zu gewährleisten, ist es zwingend notwendig, dass du die Fremdnummern korrekt pflegst. Für Amazon FBA Artikel musst du als Bezeichnung SKU_FBA und für FBM Artikel die Bezeichnung SKU_FBM verwenden. Im Reiter **Fremdnummer** in den Artikelstammdaten musst du die entsprechende Amazon SKU eintragen und als Shop die Amazon Schnittstelle auswählen. Eine Anleitung zum Import von Fremdnummern findest du[hier](https://help.xentral.com/hc/de/articles/360016758199#UUID-be6a2725-3071-98cf-ad2e-1a9016c503cc).

![Amazon-19.png](https://help.xentral.com/hc/article_attachments/22381425903260)

Du kannst auch einen Artikel als **FBA ** und**FBM** Artikel anbieten, indem du auf Amazon die Option "Weiteren Zustand hinzufügen" nutzt.

![Amazon-20.png](https://help.xentral.com/hc/article_attachments/22381425904156)

Es ist **wichtig**, dass du bei den Angeboten mit dem dazugehörigen Artikel nicht häufig zwischen "Versand durch Verkäufer" und "Versand durch Amazon" hin und her wechselst, sondern dazu immer einen weiteren Zustand hinzufügst.

### Artikel anlegen

MitXentral kannst du Artikel in Amazon anlegen. Nach der Verknüpfung mit dem Marktplatz erscheint eine weitere Schaltfläche **Amazon Einstellungen**, wo du diverse Einstellungen ausfüllen kannst. Im Wesentlichen kannst du "Grunddaten" ausfüllen (bzw. werden diese von Xentralübergeben). Zusätzlich musst du eine Kategorie wählen, woraufhin weitere Amazon-spezifischen Pflichtfelder erscheinen.

Minimal wird von Xentral unterstützt:

- Artikel-Name
- Bulletpoints
- Gewicht
- EAN
- Artikelbeschreibung
- Artikelabmessung

Artikel kannst du nicht mehr wie bisher direkt in den Artikelstammdaten anlegen, sondern wie folgt:

![Amazon-25.png](https://help.xentral.com/hc/article_attachments/22381425904668)

![Amazon-26.png](https://help.xentral.com/hc/article_attachments/22381440072604)

![Amazon-27.png](https://help.xentral.com/hc/article_attachments/22381425907356)

![Amazon-28.png](https://help.xentral.com/hc/article_attachments/22381440074012)

1. Du rufst den Amazon Importer über**Administration > Shop Schnittstelle >* Amazon***auf.
1. Dann klickst du auf den Reiter **Artikel anlegen (BETA)**

1. Dort klickst du auf **+Neuer Eintrag **

1. Du wählst das passende Flatfile (Vorlage) und klickst auf die Schaltfläche **Weiter**

1. Nun trägst du in der erscheinenden Übersicht im Feld "Artikel" die Artikelnummer ein und wartest auf das Ergebnis
1. Derzeit werden die Artikeldaten noch nicht in das Formular geladen, sondern müssen händisch eingetragen werden (Beta)
1. Der angezeigte Artikel ist über die Schaltfläche **Speichern** am Ende des Felds hinzuzufügen

## Systemmeldungen zu Amazon verstehen (System Health)

Es gibt in der System Health App einen Abschnitt, der dich den Status deiner Amazon-Schnittstelle und deines Seller-Central-Kontos beobachten lässt. Du findest die System Health App folgendermaßen:

- In Xentral NextGen: Administrationsmenü > Systemmeldungen
- Im Classic Design: Am oberen Ende der Seite neben der Suchleiste

Die App zeigt für Amazon im Abschnitt Onlineshops folgendes an:

- **sellingPartnerApiRefreshToken**
  Diese Meldung erscheint, wenn eine deiner Amazon Shop-Schnittstellen aufgrund eines leeren Tokens deaktiviert wurde. Die betroffene Shop-ID wird in eckigen Klammern angezeigt, z.B. Verkaufskanal [12].

- **Amazon_shopID_MarketplaceID**
  Diese Meldung gibt dir Informationen über den aktuellen Zustand deines Amazon Seller-Central-Kontos. Jede Marketplace ID erhält einen eigenen Eintrag, der ungefähr so aussieht: Amazon_1_A1PA6795UKMFR9, wobei sich die Werte für die Shop- und Marketplace-ID unterscheiden können.

  Die Meldung ist folgendermaßen aufgebaut: *[Marketplace ID] from sales channel [x] is [Status]*.

  Solltest du eine andere Meldung als "ok" erhalten, dann prüfe bitte dein Amazon Seller-Central-Konto, um das Problem zu identifizieren. Dein Konto kann als gefährdet eingestuft werden, wenn du z. B. aufgrund einer negativen Kundenbewertung unter die Leistungsrichtlinien Amazons fällst.

  - Die *[Marketplace ID]* lässt dich erkennen, welcher deiner Marktplätze betroffen ist. Die Marketplace ID für Deutschland ist z.B. A1PA6795UKMFR9.
  - Das [x] nach sales channel zeigt die Shop-ID des betroffenen shopimporters in Xentral an. Alle Shop-IDs werden ganz links in der Übersichtstabelle der App Online-Shops angezeigt.
  - Das Feld [Status] kann die folgenden drei Status haben:

## FAQ

### Schattenangebote entfernen

Schattenangebote bei Amazon entstehen, wenn ein FBM-Angebot zu einem FBA-Angebot umgewandelt wird, ohne das der Lagerbestand zuvor auf null gesetzt wird.

Gleichermaßen kann ein Schattenangebot entstehen, wenn für ein FBA-Angebot neue Lagerbestände übertragen werden.

Eine weitere Möglichkeit ist, dass die falsche Fremdnummernbezeichnung im ReiterFremdnummerngewählt wurde. Dies ist z.B. der Fall, wenn die Bezeichnung SKU_FBM für ein FBA-Angebot genutzt wird.

Gültige Werte für die Fremdnummern-Bezeichnungen sind ausschließlich:

- SKU_FBM
- SKU_FBA

Gehe wie folgt vor, um Schattenangebote zu löschen:

1. Navigiere zuAmazon Seller Central > Lagerbestand > Lagerbestand verwalten.
1. Gib im oberen Suchfeld die entsprechende ASIN ein und klicke aufSuchen.
1. Auf der rechten Seite siehst du einen kleinen Kasten nebenBearbeiten mit einem Pfeil nach oben und einem Pfeil nach unten. Klicke auf diesen kleinen Kasten.
1. Wähle die OptionZu Versand durch Verkäufer ändern. Diese Änderung kann systembedingt einige Minuten in Anspruch nehmen. Bitte habe etwas Geduld.
1. Storniere alle offenenVersand durch Händler-Aufträge (FBM), welche du nicht erfüllen kannst bzw. möchtest, da dieser Bestand sonst wieder im System erscheint. Diese Änderung kann systembedingt einige Minuten in Anspruch nehmen. Bitte habe auch hier etwas Geduld.
1. Setze den Bestand des Angebots auf 0.
1. Konvertiere das Angebot zurück zu Versand durch Amazon (FBA), indem du die OptionZu Versand durch Amazon ändern nutzt.

Durch das Entfernen des Bestandes, sowie durch die Hin- und Herkonvertierung, wird das Schattenangebot im System entfernt.

### Troubleshooting: Import von Aufträgen

Sollte der Import von Aufträgen nicht richtig funktionieren, überprüfe bitte Folgendes:

1. Zeigt der Prozessstartershopimport einen Fehler an? Wenn ja, dann starte den Prozessstarter neu. Der ProzessstarterAmazon ist für den Import von Aufträgen nicht relevant.
1. Gibt es in der Zwischentabelle beschädigte oder gesperrte Aufträge? Du kannst die Zwischentabelle prüfen, indem du aufShopimport Zwischentabelle in deiner Amazon-Schnittstelle klickst.
1. Tritt das Problem bei einem bestimmten Datum auf? Ändere das Importdatum zu einem neueren Datum und setze denImport-Modus auf Manuell (mit Importzentrale). Sollte das funktionieren, dann stelle ein früheres Datum ein und wiederhole den Prozess bis ein Fehler im Importprozess auftritt.
  Überprüfe die Aufträge dieses Tages in deinem Amazon Seller Central.

### Fehlende Informationen bei einem Auftrag

Falls bestimmte Informationen im Auftrag fehlen, sind womöglich nicht alle relevanten Informationen im Bericht von Amazon enthalten. Dies kann z.B. passieren, wenn sich die Rechnungs- und Lieferadresse unterscheiden.

Gehe wie folgt vor, um dem Bericht weitere Informationen hinzuzufügen:

1. Logge dich in dein Amazon Seller Central ein.
1. Navigiere zuBestellungen > Bestellberichte.
1. Klicke aufSpalten im Bestellbericht hinzufügen oder entfernen.
1. Aktiviere die entsprechende Spalte. Im Fall der fehlenden Rechnungsaddresse. aktiviere Fakturierung im Bereich Optionale Spalten.

Die Information wird nun allen neuen Aufträgen hinzugefügt. Sie kann nicht nachträglich alten Aufträgen hinzugefügt werden.