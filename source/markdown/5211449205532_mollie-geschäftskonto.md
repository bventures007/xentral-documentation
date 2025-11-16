## Xentral und Mollie einrichten

Um Mollie-Zahlungen in Xentral zu integrieren, stelle bitte sicher, dass:

- Du ein gültiges Konto bei Mollie und Xentral hast.
- Mollie als Geschäftskonto in Xentral verfügbar ist. Für jedes Mollie Konto das du hast, musst du ein eigenes Geschäftskonto in Xentral anlegen.

### Ein Geschäftskonto in Xentral erstellen

1. Melde dich bei Xentral an und gehe zu **Administration **>** Buchhaltung **>** Geschäftskonten**.
1. Klicke **Neu**.
1. Wähle Mollie.
1. Gib die Anzahl der Tage ein, ab denen du Daten importieren möchtest. Wenn du z. B. 30 eingibst, werden die Daten ab dem Zeitraum vor 30 Tagen importiert.
1. Logge dich in dein Mollie-Konto ein und verwende deine Anmeldedaten (E-Mail + Passwort).
1. Klicke **Verbindung prüfen**.
1. Du wirst nun zur Xentral-Oberfläche weitergeleitet und es wird eine Erfolgsmeldung angezeigt.

### Den Shop vorkonfigurieren

Du kannst jeden Online Shop, den du in Xentral eingerichtet hast, in deiner Mollie Anbindung nutzen. Bevor du mit Mollie in Xentral loslegst, solltest du die Settings deiner Online Shops prüfen.

Überprüfe insbesondere die folgenden Einstellungen:

> **Anmerkung**
>
> Wenn Xentral deine Transaktionen nicht automatisch bucht, kannst du das Problem beheben, indem du die Rundungsmethode einstellst. Gehe zu deinemOnline-Shop>Einstellungen, aktiviere das KontrollkästchenGesamtbetrag festsetzenund setze diemaximale Differenz zur berechneten Summeauf *0.01*.

- Nur für WooCommerce: Falls du den WooCommerce Online Shop nutzt, setze das Feld **Statusname Bestellung offen ** aufpending;on-hold. Hierfür navigiere zu den Einstellungen deiner Shop-Schnittstelle (**Online-Shops > WooCommerce > Details > Schnittstelle**).
- Für alle Online Shops: Navigiere zu **Details > Einstellungen**, um weitere Einstellungen zu bearbeiten:
  - **Auftragsstatus rückmelden**: Stelle sicher, dass das Kontrollkästchen ausgewählt ist.
  - **Stornierung rückmelden**: Stelle sicher, dass das Kontrollkästchen ausgewählt ist.
  - Vielleicht möchtest du auch die FelderPortound Belege im Auto-Versand erstellenüberprüfen, um sicherzustellen, dass diese wie gewünscht sind und zu deinen Geschäftsprozessen passen.

Nach der Einrichtung des Kontos bleiben die Zahlungsarten in der Shop-Oberfläche (**Details > Zahlungsweisen**) leer, bis die erste Bestellung importiert wird. Der Bestellstatus in WooCommerce sollte als "On Hold" markiert sein, damit Bestellungen in Xentral importiert werden können.

## Aufträge erstellen

Um einen Auftrag zu erstellen stelle bitte sicher, dass:

- Dein Shop online und am Laufen ist.
- Artikel verfügbar sind.
- Preise verfügbar sind.
- Mollie als Zahlungsmethode verfügbar ist.
- Die Verbindung zwischen deinem Shop und Xentral eingerichtet ist und läuft.

Der folgende Arbeitsablauf ist erforderlich, um einen Auftrag zu erstellen und in Xentral zu importieren:

1. Der Käufer erstellt ein Konto im Online Shop.
1. Der Käufer gibt eine Bestellung auf und verwendet Mollie als Zahlungsmethode.
1. Der Auftrag wird in Xentral importiert.
1. Sobald die Bestellung importiert wurde, erscheint eine neue Zahlungsmethode in der Shop-Oberfläche (**Details **>** Zahlungsweisen**).

Als Ergebnis dieses Workflows ist eine Bestellung in Xentral verfügbar, der Zahlungsstatus in Mollie ändert sich auf *Bezahlt* und die neue Zahlungsweise ist in der Shop-Oberfläche sichtbar.

> **Anmerkung**
>
> Wenn du Klarna als Zahlungsmethode in Mollie auswählst, beachte bitte, dass die Transaktion erst dann als *bezahlt* markiert wird, wenn die Bestellung als *versandt* markiert ist.

## Aufträge versenden

Um in Mollie erstellte Bestellungen von Xentral aus zu versenden, stelle bitte sicher, dass:

- Dein Shop online und am Laufen ist.
- Der Auftrag in deinem Shop platziert wurde.
- Der Kunde die Bestellung mit Mollie bezahlt hat.

Wenn der Kunde die Bestellung mit Mollie bezahlt, siehst du die Bestellung in Xentral. Sobald du die Bestellung bearbeitest und versendest, wird der Status in *versandt* geändert und an deinen Online-Shop zurückgemeldet. Dein Online-Shop benachrichtigt Mollie, und der Status wird auf *versandt* aktualisiert. Xentral erstellt die Rechnung und die Transaktionen aus Mollie sind für den Import verfügbar.

Wenn du die Option des automatischen Versands nutzt, sendet der Cron-Job diese Bestellungen automatisch an deinen Online-Shop.

## Zahlungen importieren

Sobald der Käufer die Zahlung in Mollie abgeschlossen hat, kannst du die Zahlung in Xentral importieren.

1. Melde dich in Xentral an und gehe zu **Buchhaltung **>** Zahlungseingang**.
1. Klicke auf, um das Konto zu Mollie zu öffnen.
1. Klicke auf **Live-Import**, um die neuen Zahlungen zu importieren.
1. Suche die Mollie-Zahlung, die du verarbeiten möchtest, und wähle **Rechnungseingang ** aus der**Aktion**

-Auswahlliste.
1. Gib die Rechnung in das Feld **Rechnung** ein.
1. Klicke auf, um die Buchung zu öffnen. Klicke dann auf **Speichern**.

Du hast die Zahlung über Mollie nun erfolgreich importiert und erfasst. Du kannst du Zahlung in **Auftrag **>** Protokoll** prüfen.

![protocol.png](https://help.xentral.com/hc/article_attachments/5211422581148)

## Aufträge stornieren

Damit du in Mollie erstellte Aufträge stornieren kannst, musst du verschiedene Schritte in Mollie und Xentral vornehmen.

### Aufträge in Xentral stornieren

Du erhältst eine E-Mail, dass der Käufer einen über Mollie erstellten Auftrag stornieren möchte.

1. Melde dich in Xentral an und gehe zu **Verkauf **>** Auftrag**.
1. Suche den Auftrag, der storniert werden soll, und öffne ihn.
1. Wähle aus der **Aktion **

-Auswahlliste die Option ** Auftrag stornieren**.
1. Bestätige die Stornierung und klicke auf **Speichern**.

Du hast die Stornierung des Auftrags in Xentral bestätigt. Xentral überträgt die Stornierung an deinen Online-Shop. Falls du Aufträge manuell bearbeitest, musst du den Stornierungsstatus an deinen Shop über den entsprechenden Eintrag im Aktionsmenü zurückmelden. Dein Online-Shop informiert Mollie. Sobald Mollie die Stornierung akzeptiert, wird eine Gutschrift mit dem Status *offen* angelegt.

> **Anmerkung**
>
> Der Status der Gutschrift wird in Mollie auf *gutgeschrieben* geändert - und nur diese Gutschriften sind für den Import nach Xentral verfügbar.

### Sonderfälle

Die folgenden Sonderfälle erfordern eine vom Standardprozess abweichende Vorgehensweise:

Rücknahme der Stornierung - Mach die Stornierungsanfrage in Mollie, deinem Online-Shop und Xentral rückgängig.

Teilstornierung - Enthält dein Auftrag mehrere Artikel, kannst du eine Teilstornierung vornehmen. Storniere die Artikel deines Auftrags manuell in Mollie, deinem Online-Shop und Xentral.

Service-Gutschrift - Du kannst einen Service manuell in Mollie, deinem Online-Shop und Xentral gutschreiben. Mollie erstellt eine Gutschrift.

Stornierung eines versendeten Auftrags - Du kannst den Service manuell in Mollie, deinem Online-Shop und Xentral gutschreiben. Lade die Buchung nach der Gutschrift in Xentral hoch.

Rückgabe - Möchte dein Kunde die Artikel seines Auftrags zurückgeben, kannst du die Rückgabe in Mollie, deinem Online-Shop und Xentral verarbeiten. Alle Gutschriften, die du manuell angelegt hast, werden mit dem nächsten Live-Import in Xentral importiert, jedoch nur dann, wenn sie den Status *gutgeschrieben* haben.