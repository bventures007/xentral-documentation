## SSL-Verschlüsselung

Um das System über SSL-Zertifikate verschlüsseln zu lassen, wenden Sie sich bitte an Ihren Server-Administrator oder Provider. Diese müssen immer am Webserver aktivieren werden.

SSL-Zertifikate haben eine begrenzte Gültigkeitsdauer (z.B. 1 Jahr). Um zu verhindern, dass Xentral wegen eines abgelaufenen Zertifikats nicht mehr über den Browser erreichbar ist, sollte dies vom Serveradministrator rechtzeitig aktualisiert werden. Ist ein Zertifikat abgelaufen, so muss der Serveradministrator ein Neues anlegen.

## Externe Dienste / Software

### Let's Encrypt SSL Verschlüsselung

> **Anmerkung**
>
> Diese Funktion ist aktuell noch im Test (Stand 11/2016).

Diese Option in der Datei verwenden:

```
/etc/apach2/apache2.conf

Header always append X-Frame-Options SAMEORIGIN

```Bzw. für nginx```add_header X-Frame-Options SAMEORIGIN;```

Danach müssen Sie die Webserver neu starten, sonst kann man keine Positionen bei Belegen einfügen.

### CryptoMagic

Mit dem Dienst[CryptoMagic](https://www.cryptomagic.eu/xentral/)für Xentral können Sie SSL-Zertifikate erstellen, einzeln für jeden Benutzer, der auf das System zugreift.

So kann man sicherstellen, dass nur ein Benutzer, welcher manuell ein Zertifikat vergeben darf, überhaupt auf Xentral zugreifen kann.