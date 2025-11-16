Wenn du über Amazon verkaufst, berechnet Amazon dir für die Nutzung seiner Dienste Gebühren, wie z.B. Servicegebühren, Lagergebühren (FBA), etc.

Über das Amazon Zahlungsberichte-Geschäftskonto kannst du deine Amazon-Transaktionen sowie die damit verbundenen Gebühren importieren und auf die passenden Konten verbuchen.

## Geschäftskonto für Amazon Zahlungsberichte anlegen

Einstellungen > Buchhaltung > Zahlungen & Geschäftskonten > Bank & Zahlungskonten

![settings_businessaccounts_amazonpaymentreport.png](https://help.xentral.com/hc/article_attachments/15697957915548)

Gehe wie folgt vor, um ein neues Geschäftskonto für Amazon Zahlungsberichte anzulegen:

1. Klicke auf Konto hinzufügen und dann im Bereich Auswahl auf die Kachel Custom. Das Kontodetails-Formular wird angezeigt.
1. Gib einen Namen für dein neues Geschäftskonto in das Feld Bezeichnung ein.
1. Wähle im Typ-Dropdown-Menü die Option Amazon Zahlungsberichte.
1. **Optional**: Schränke über das FeldProjekt das Konto auf ein bestimmtes Projekt ein, z.B. dein Projekt für Amazon FBA.
1. Stelle sicher, dass ein Häkchen bei Aktiv gesetzt ist. Ist hier kein Häkchen gesetzt, kannst du dieses Konto nicht verwenden.
1. **Optional**: Setze ein Häkchen bei Änderungen erlauben, wenn spätere Änderungen an den Buchungen ermöglicht werden sollen. Dies ist nur möglich, falls du deine Kontoauszüge manuell einträgst und wird nicht von uns empfohlen.
1. Scrolle ganz nach unten und klicke auf Speichern.

Du hast nun die Grundeinstellungen für dein neues Amazon Zahlungsberichte-Geschäftskonto vorgenommen.

## Amazon Zahlungsberichte konfigurieren

Einstellungen > Buchhaltung > Zahlungen & Geschäftskonten > Bank & Zahlungskonten > Öffne das Geschäftskonto für Amazon Zahlungsberichte durch einen Klick auf das Stift-Symbol

Gehe wie folgt vor, um dein Amazon Zahlungsberichte-Geschäftskonto zu konfigurieren:

> **Anmerkung**
>
> Der BereichBankverbindungist für Amazon Zahlungsberichte-Geschäftskonten irrelevant.

1. Scrolle runter bis zum Bereich DATEV und gib deinen DATEV-Kontenrahmen ein.
1. Scrolle runter bis zum Bereich Live-Import. Du musst hier keine Zugangsdaten eingeben. Du kannst im Feld Zugangsdaten jedoch Konten zum Verbuchen der unterschiedlichen Amazon-Gebühren erfassen.
  Die Einträge müssen im folgenden Format erfolgen:

  **Format **: {Gebührenart}=>{Nummer des Kontos}; ** Beispiel**: KONTO_GEBUEHRAUFTRAG=>3123;

  Der Pfeil besteht aus einem Gleich-Zeichen (=) und einem Größer-Zeichen (>). Du kannst mehrere Gebührenarten auf das selbe Konto buchen.

  Nachdem du unterZugangsdaten die entsprechenden Einträge eingetragen hast, werden sie auch im Abschnitt Kontospezifische Einstellungen angezeigt und können dort bearbeitet werden. Jede Änderung in einem der Bereiche wird sofort auch auf den anderen Bereich angewandt.

1. Klicke auf Speichern.

Du kannst dein Amazon Zahlungsberichte-Geschäftskonto nun verwenden.

## Amazon Zahlungsberichte importieren

> **Anmerkung**
>
> Damit du deine Amazon Zahlungsberichte importieren und verarbeiten kannst, ist der V2-Bericht erforderlich, den du von Amazon herunterladen kannst.

Du kannst deine Amazon Zahlungsberichte entweder automatisch über den Live-Importer importieren oder aber manuell.

> **Wichtig**
>
> Sobald ein Eintrag importiert wurde, kannst du ihn nicht mehr rückwirkend ändern!

Gehe wie folgt vor, um Amazon Zahlungsberichte automatisch zu importieren:

1. Navigiere zu Einstellungen > Buchhaltung > Zahlungen & Geschäftskonten > Bank & Zahlungskonten > Öffne das Geschäftskonto für Amazon Zahlungsberichte durch einen Klick auf das Stift-Symbol.
1. Stelle sicher, dass im Bereich Live-Import ein Häkchen bei Live-Import aktiv gesetzt ist.
1. Setze im Bereich Prozessstarter ein Häkchen bei Zahlungseingänge automatisch abholen und Zahlungseingänge automatisch verbuchen, um die Zahlungseingänge automatisch zu verbuchen.
1. Klicke auf Speichern.

Gehe wie folgt vor, um Amazon Zahlungsberichte manuell zu importieren:

1. Navigiere zu Buchhaltung > Zahlungseingang.
1. Klicke auf das **Stift-Symbol** in der Spalte Menü für das Bankkonto, das du für Amazon Zahlungsberichte angelegt hast.
1. Klicke auf Datei auswählen und wähle die Amazon Zahlungsbericht-CSV-Datei, die du aus deinem Amazon Seller-Konto für den Import heruntergeladen hast.
1. Klicke auf Importieren.

Dein Amazon Zahlungsbericht wird importiert und die Transaktionen werden im ReiterKontoauszügeangezeigt. Du kannst die Zahlungseingänge nun nach Bedarf weiter verarbeiten.

## Liste der Gebührenarten

Amazon verfügt aktuell über ca. 130 unterschiedliche Gebührenarten, die du auf unterschiedliche Geschäftskonten in Xentral buchen kannst. In der folgenden Liste findest du einige häufig genutzte Gebührenarten. Bitte beachte, dass diese Liste nicht vollständig ist.

- KONTO_GEBUEHRAUFTRAG=>XXXX;
- KONTO_SERVICEGEBUEHR=>XXXX;
- KONTO_VERSANDLABELGEBUEHR=>XXXX;
- KONTO_VERSANDGEBUEHR=>XXXX;
- KONTO_SHIPPINGHB=>XXXX;
- KONTO_REFUNDCOMMISSION=>XXXX;
- KONTO_VERSAND=>XXXX;
- KONTO_Shippinglabelpurchaseforreturn=>XXXX;
- KONTO_ShippingLabelpurchase=>XXXX;
- KONTO_ErstattungShippingTax=>XXXX;
- KONTO_WAREHOUSE_LOST_MANUAL=>XXXX;
- KONTO_WAREHOUSE_DAMAGE=>XXXX;
- KONTO_ShippingServicesRefund=>XXXX;
- KONTO_UEBERTRAG=>XXXX;
- KONTO_WERBEKOSTEN=>XXXX;
- KONTO_REVERSAL_REIMBURSEMENT=>XXXX;
- KONTO_TransactionTotalAmount=>XXXX;
- KONTO_RE_EVALUATION=>XXXX;
- KONTO_total-amount=>XXXX;
- KONTO_CurrentReserveAmount=>XXXX;
- KONTO_COMMISSION=>XXXX;