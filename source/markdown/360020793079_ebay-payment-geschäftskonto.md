Mit **eBay Payments ** übernimmt eBay seit 2020 die gesamte**Zahlungsabwicklung** für einen Großteil seiner Händler. Das bedeutet, dass eBay die Zahlungen für Bestellungen vollständig abwickelt und dem Händler anschließend direkt auf dessen Bankkonto weiterüberweist.

eBay ermöglicht dem Endkunden unterdessen eine breite Auswahl an Zahlungsmöglichkeiten, darunter auch PayPal, ApplePay, GooglePay, Kreditkarte, Klarna Sofortüberweisung und Lastschrift.

Genauere Informationen von eBay findet Ihr[hier auf der Webseite des eBay Kundenservice](https://www.ebay.de/help/help/selling/getting-paid/introducing-managed-payments-ebay?id=4795).

Für seine Händler erstellt eBay desweiteren **Zahlungsberichte**, vergleichbar mit den[Amazon-Zahlungsberichten](https://help.xentral.com/document/preview/24317#UUID-dbebb0b4-b5e7-735c-853a-c162fd8ae4d5). Diese Zahlungsberichte können zu xentral importiert werden, damit alle Zahlungseingänge für eure eBay-Aufträge auch mit den Aufträgen und Rechnungen in xentral verknüpft werden können und eure Buchhaltung vollständig ist.

## eBay Payment Konto anlegen

Über den Button +NEU in der Kontenübersicht kann ein neues eBayPayment Konto angelegt werden. Wurde bereits ein Konto in xentral angelegt, so kann dieses über den Edit-Button bearbeitet werden.

Im nächsten Schritt wird "Konto: ebay Payment" als Kontenart ausgewählt.

![AccEbayPayment1.png](https://help.xentral.com/hc/article_attachments/15492828694684)

Im nächsten Schritt wird der eBay Account ausgewählt und auf "Weiter" geklickt.

![AccEbayPayment2.png](https://help.xentral.com/hc/article_attachments/15492873346972)

Zur Verwendung von eBay Payments ist es wichtig, dass in den Einstellungen des angebundenen eBay Accounts der **Auftragsimport über die alternative API** ausgewählt ist (Administration → Einstellungen → Shop Schnittstelle →* eBay auswählen*).

> **Anmerkung**
>
> Nähere Informationen zum Auftragsimport über die alternative API findet Ihrhier.

![AccEbayPayment3.png](https://help.xentral.com/hc/article_attachments/15492827275420)

Nach der Auswahl es Accounts erscheint eine neue Seite, in der die nötigen Einstellungen bearbeitet werden können.

![AccEbayPayment4.png](https://help.xentral.com/hc/article_attachments/15492873463580)

### Einstellungen

- Bezeichnung → Bezeichnung des Kontos
- Typ → Typ des Kontos. Hier ist "Konto: Ebay Payment (API)" auszuwählen
- Projekt → Zuordnung des Kontos zu einem Projekt
- Aktiv → Angabe, dass dieses Konto aktiv genutzt wird
- Keine E-Mail → Normalerweise wird beim Zahlungseingang eine Mail an den Kunden gesendet. Soll dies unterdrückt werden muss diese Option gesetzt werden
- Änderungen erlauben → Es dürfen nachträglich Kontobuchungen verändert werden

### Bankverbindung (bei Typ Bank)

Da es sich bei dem eBay Payment Konto nicht um den Typ Bank handelt, sind diese Felder zu vernachlässigen.

### DATEV

![AccEbayPayment5.png](https://help.xentral.com/hc/article_attachments/15492828886428)

- Konto → Angabe des DATEV Kontos

### CSV-Import

Dieser Bereich wird für die eBay Payments Funktion nicht benötigt und kann freigelassen werden.

### Live-Import

![AccEbayPayment6.png](https://help.xentral.com/hc/article_attachments/15492828927004)

- Live-Import aktiv → Haken aktiviert den Live-Import
- Zeitraum → Zeitraum, in der der Live-Import stattfindet
- Zu Zeiten → Angabe der Uhrzeit zu der der Live-Import stattfindet
- Zugangsdaten → API Code für den Live-Import. Die Shop-ID wird hier automatisch eingefügt, kann aber auch manuell eingetragen werden.
- Passwort Tresor → Der Inhalt des Passwort-Tresors kann in der Datenstruktur der Zugangsdaten über die Variable {PASSWORT} genutzt werden

### Kontenspezifische Einstellungen

- Ebay-Shop → Hier wählst du deinen Ebay-Shop aus
- Konto Order Fee → Konto, auf das die Ordergebühren gebucht werden sollen
- Konto SHIPPING_LABEL → Konto, auf dass die Gebühren für das Versandetikett gebucht werden sollen
- Konto TRANSFER → Konto für Transfergebühren
- Konto NON_SALE_CHARGE → Konto für Gebühren bei Nichtverkauf
- Konto andere → Konto für sonstige Gebühren

### Prozessstarter

Für den **Prozessstarter ** kann außerdem eingestellt werden, dass Zahlungseingänge automatisch abgeholt und verbucht werden. Bei Bedarf kann ein**Startwert** für das Konto eingegeben werden.