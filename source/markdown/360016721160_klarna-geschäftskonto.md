Der Zahlungsanbieter Klarna steht in verschiedenen Shops und Marktplätzen als Zahlungsweise zur Verfügung und kann für Verkäufer das Erstellen der Rechnung übernehmen. Neben der häufigen Zahlungsweise Klarna Rechnung gibt es auch Klarna Vorkasse für Vorkasse-Bestellungen.

Mit dem Modul Klarna im Xentral AppStore können Sie eine direkte Anbindung an Klarna vornehmen. Damit ist es möglich, die Trackingnummer des Auftrags als Auslieferbestätigung über die API an Klarna zu übertragen, sobald der Auftrag in Xentral versendet wird. Klarna wird dann die Zahlung vom Kunden einfordern.

Alternativ können Sie Klarna auch als Zahlungsweise anlegen, ohne Ihren Account anzubinden. Dann muss man manuell vorgehen, d.h. den Status der Aufträge in Klarna manuell als 'verschickt' markieren und in Klarna ggf. die Trackingnummer hinterlegen. Für manche Shops gibt es Plugins, die die Kommunikation an Klarna vollständig übernehmen. Dann muss eine Anbindung in Xentral nicht mehr vorgenommen werden.

Zusätzlich kann Klarna als Geschäftskonto angebunden werden, um die Zahlungen per Live-Import zu importieren.

## Klarna als Zahlungsweise anbinden

### Credentials eintragen

Um Klarna direkt per API anzubinden, müssen die Zugangsdaten (Credentials) im System hinterlegt werden. Unter Administration → Einstellungen → Zahlungsweisen können Sie über den Button +NEU eine weitere Zahlungsweise in Xentral definieren. Als Modul muss dabei Klarna gewählt werden.

Im Anschluss können Sie die Zahlungsweise aktiv setzen und Ihre Klarna-Accountdaten hinterlegen.

![Klarna1.png](https://help.xentral.com/hc/article_attachments/15492829149084)

Benötigt wird der **Benutzername/Username ** (ehemals Merchant-ID) und das ** Passwort** (ehemals Shared Secret), welche du beide in deinem Klarna-Account findest. Benutzername und Passwort dienen für Anbindungen an Klarna als API Credentials, sie sind eine Form der Authentifizierung.

Wo diese im Klarna-Backend gefunden werden, wird[hier im Entwicklerportal von Klarna](https://developers.klarna.com/api/#authenticationhttp://)erläutert.

Bitte beachten Sie dass der Typ eindeutig sein muss, am besten kleingeschrieben klarna.

In Xentral können Sie die Aufträge vorab als bezahlt markieren, damit diese nicht im Mahnwesen landen. Die Zahlungsabwicklung übernimmt Klarna.

### Kontrolle der Rückmeldung

Nachdem Sie die Daten erfolgreich hinterlegt haben, können Sie sich einen Auftrag in Xentral mit Zahlungsweise Klarna aussuchen, den Sie bis zum Versand, sprich bis zum Druck der Paketmarke und dem Erfassen der Trackingnummer, verfolgen.

Sobald die Trackingnummer erfasst wurde, wird ein Request an Klarna übermittelt. Wenn dieser erfolgreich zurückgemeldet wurde, erhalten Sie im Auftrag einen Protokolleintrag zur Klarna Rückmeldung, den Sie über das Minidetail einsehen können.

### Beispiel: Rückmeldung des Zahlungsstatus von Klarna

In diesem Beispiel wird Klarna Rechnung direkt per API angebunden. Weil die Zahlungabwicklung vollständig von Klarna durchgeführt wird, werden die Aufträge in Xentral bereits vorab als bezahlt markiert.

Im Autoversand erstellt Xentral für diesen Auftrag nur einen Lieferschein, da die Rechnung von Klarna gestellt und an den Kunden geschickt wird.

![Klarna2.png](https://help.xentral.com/hc/article_attachments/15492845162908)

Im Protokoll des Auftrags finden Sie die Rückmeldung von Klarna. Wurden Rechnung und Zahlungsrisiko positiv zurückgemeldet, so erhalten Sie eine solche Meldung.

![Klarna3.png](https://help.xentral.com/hc/article_attachments/15492873928604)

Sollte die Rückmeldung fehlschlagen, erhalten Sie an selber Stelle eine Fehlermeldung und können die Rechnung in Klarna von Hand prüfen.

![Klarna4.png](https://help.xentral.com/hc/article_attachments/15492829293084)

### Stornos

Bei Stornierungen über Klarna werden keine Einträge zurückgemeldet, und auch keine Stornos in das Rechnungsprotokoll mit aufgenommen.

## Anbindung als Geschäftskonto

Eine weitere Möglichkeit ist es, Klarna als Geschäftskonto anzubinden, um Zahlungen per Live-Import holen zu können. Dazu werden die API-Credentials von Klarna (API_USER, API_KEY, API_DAYS) benötigt.

> **Anmerkung**
>
> Klarna kann im Live Import die Zahlungen nur alle 7 Tage abholen.

Die API-Credentials können auf der Seite von Klarna gefunden werden. Dazu wird in die Einstellungen-App im Händlerportal navigiert und dort auf "neue API-Credentials generieren" geklickt. Die neu erzeugten API-Anmeldeinformationen sollten unbedingt gespeichert werden, da diese nur einmal gesehen werden können.

Das Modul "Geschäftskonten" findet sich unter Administration → Einstellungen → Buchhaltung → Geschäftskonten und zum Anlegen eines neuen Kontos wird auf "Neu" geklickt. Dort wird "Custom" ausgewählt und als Bezeichnung Klarna. Der Typ ist Konto:Klarna. Die API-Credentials werden in das Feld "Zugangsdaten" in folgender Form eingegeben:

```
API_USER=>XX;
API_KEY=>XX;
API_DAYS=>X;
```

Zum Hinzufügen des Geschäftskontos wird nun gespeichert.