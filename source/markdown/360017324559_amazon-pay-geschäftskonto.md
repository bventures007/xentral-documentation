Amazon Pay ist ein Zahlungs-Plug-in für Onlineshops, das du in unterschiedlichen Onlineshops verwenden kannst.

InXentral kannst du sowohl eingehende Amazon Pay-Zahlungen als auch Rückerstattungen über Amazon Pay verarbeiten. Eingehende Zahlungen und Rückerstattungen werden dabei unterschiedlich behandelt:

- Eingehende Zahlungen werden über das Bankkonto CSV-Geschäftskonto verarbeitet. Weitere Infos zu dieser Art Geschäftskonto und dessen Einrichtung findest du [hier](https://help.xentral.com/hc/de/articles/360020073639#UUID-5f6d6683-98a0-d026-f695-8a17ae8b143c).
- Rückerstattungen über Amazon Pay werden über das Amazon Pay-Geschäftskonto verarbeitet.

## Eingehende Amazon Pay-Zahlungen importieren

### Bank per CSV-Import-Geschäftskonto anlegen

Eingehende Amazon Pay-Zahlungen werden über das GeschäftskontoBank per CSV-Importabgewickelt.

[Dieser Artikel](https://help.xentral.com/hc/de/articles/360020073639#UUID-5f6d6683-98a0-d026-f695-8a17ae8b143c)erklärt dir, wie du deinBank per CSV-Import-Geschäftskonto anlegst.

Bitte beachte bei Amazon Pay Folgendes:

| Feld im Bereich CSV-Import in Xentral | Spalte in Amazon Pay CSV-Vorlage |
| --- | --- |
| Datum | TransactionPostedDate |
| Betrag | TransactionAmount |
| Buchungstext | AmazonTransactionId |
| Währung | CurrencyCode |

Du kannst das FeldZugangsdatenim BereichLive-Importdazu verwenden, Konten zu definieren, auf die gebucht werden sollen.

### Amazon Pay-Bericht für den Import abrufen

Gehe wie folgt vor, um deine Amazon Pay-Berichte abzurufen:

![amazonpay_berichtsrepository_download.png](https://help.xentral.com/hc/article_attachments/17334725352604)

1. Melde dich in deinem Amazon Pay-Konto in Amazon Seller Central an.
1. Klicke im Menü auf Zahlungen und wähle die Option Berichtsrepository aus.
1. Öffne den Reiter Berichte nach Zeitraum aus dem Menü.
1. Klicke im ReiterBerichte nach ZeitraumaufBericht erstellen. Der DialogBerichte nach Zeitraum erstellenwird angezeigt.
1. Wähle den Berichtstyp Transaktion. Wähle den Berichtszeitraum:
  - Monat. Hier kannst du einen Bericht nach Monat erstellen.
  - Benutzerdefiniert. Gib den Zeitraum, für den du einen Bericht erstellen möchtest, in die passenden Felder ein.
1. Klicke auf Bericht anfordern. Dein Amazon Pay-Bericht wird erstellt und im Reiter Berichte nach Zeitraum angezeigt.
1. Klicke bei deinem Bericht auf Aktualisieren. Die Schaltfläche Herunterladen wird angezeigt. Lade den Amazon Pay-Bericht auf deinen Computer herunter.

Du kannst den Amazon Pay-Bericht nun in Xentral importieren.

### Eingehende Amazon Pay-Zahlungen importieren

Gehe wie folgt vor, um eingehende Amazon Pay-Zahlungen zu importieren:

1. Navigiere zu Buchhaltung > Zahlungseingang.
1. Klicke auf in der Spalte Menü für das Konto, das du für den Import der Amazon Pay-Berichte angelegt hast.
1. Klicke auf Datei auswählen und wähle die Amazon Pay-CSV-Datei, die du aus deinem Amazon Pay-Konto für den Import heruntergeladen hast.
1. Klicke auf Importieren.

Dein Amazon Pay-Bericht wird importiert und die Transaktionen werden im ReiterKontoauszügeangezeigt. Du kannst die Zahlungseingänge nun nach Bedarf weiter verarbeiten.

## Amazon Pay-Rückerstattungen verarbeiten

### Amazon Pay-Geschäftskonto anlegen

App Center > Buchhaltung > Geschäftskonten

Gehe wie folgt vor, um ein Geschäftskonto für Amazon Pay anzulegen:

1. Klicke auf +NEU und wähle Konto: Amazon Pay (API) im Bereich Auswahl. Das Amazon-Anmeldeformular wird angezeigt.
1. Hast du deine Amazon-Zugriffsdaten bereits in deiner Amazon-Schnittstelle hinterlegt, d.h. die Amazon Seller ID und die Amazon AWS Access Key ID, kannst du die entsprechende Schnittstelle unter Daten aus Schnittstelle auswählen.
  Alternativ kopiere oder gib die entsprechenden Informationen aus dem Amazon-Verkäuferkonto unter Amazon SellerID und Amazon AWSAccessKeyID ein.

Das Konto ist nun angelegt. Klicke aufKlassein der Bestätigungsmeldung. Die SeiteDetailswird für das Konto angezeigt. Hier kannst du deine Kontoeinstellungen pflegen. Wie du deine Kontoeinstellungen für Amazon Pay pflegst, wird im nächsten Abschnitt beschrieben.

### Dein Amazon Pay-Geschäftskonto pflegen

App Center > Buchhaltung > Geschäftskonten > Öffne dein Amazon Pay-Geschäftskonto mit einem Klick auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/6412259413532)

.

Gehe wie folgt vor, um dein Amazon Pay-Geschäftskonto zu pflegen:

> **Anmerkung**
>
> Die BereicheBankverbindungundCSV-Importsind für Amazon Pay-Geschäftskonten nicht relevant.

1. Standardmäßig fügt Xentral bei Anlage eines neuen Geschäftskontos einen Namen für dieses Konto in das Feld Bezeichnung ein. Möchtest du einen anderen Namen verwenden, kannst du ihn in diesem Feld ändern.
1. Stelle Sicher, dass das Feld Typ die Option Konto: Amazon Pay (API) enthält.
1. Wähle das passende Projekt im Feld Projekt.
1. Stelle sicher, dass ein Häkchen bei Aktiv gesetzt ist. Ist hier kein Häkchen gesetzt, kannst du dieses Konto nicht verwenden.
1. Setze ein Häkchen bei Keine E-Mail, wenn beim Zahlungseingang keine E-Mail an den Kunden versendet werden soll. Standardmäßig wird eine E-Mail versendet.
1. Setze ein Häkchen bei Änderungen erlauben, wenn spätere Änderungen an den Buchungen möglich sein sollen.
1. Scrolle runter bis zum Bereich DATEV und gib dein DATEV-Konto ein.
1. Scrolle runter bis zum Bereich Live-Import. Für Amazon Pay-Geschäftskonten sind keine Live-Imports möglich. Du kannst jedoch Folgendes in das Feld Zugangsdaten eingeben, um Rückerstattungen über dieses Konto zu verarbeiten:
  - Option1:
  [Hier](https://help.xentral.com/hc/de/articles/6124566016540#UUID-9ee45046-bcb9-f7f9-26b8-19a117a484d4) kannst du herausfinden, wie du den MWS-Autorisierungstoken generierst.

  - Option 2:
  Du findest diese Informationen in deinem Amazon-Verkäuferkonto.

1. Klicke auf Speichern.

Du kannst dein Amazon Pay-Konto nun nutzen.

### Rückerstattungen über Amazon Pay verarbeiten

Die Verarbeitung der Rückerstattungen über Amazon Pay ist identisch zur Verarbeitung der Rückerstattungen in PayPal. Weitere Informationen dazu, wie du Paypal-Rückerstattungen verarbeitest, findest du[hier](https://help.xentral.com/hc/de/articles/360017416839#UUID-d95f79b2-836e-9f04-5bfc-ecd171d4550d).