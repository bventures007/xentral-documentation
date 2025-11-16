Die Ursache liegt in der Konfiguration deiner Browser-Einstellungen. Dieser erlaubt im Standard 2 bzw. 6 parallele Downloads zur gleichen Zeit. Um die Einstellung zu ändern, rufe z.B. bei Firefox folgende Seite auf: about:config

Suche dann nach der Einstellung:network.http.max-persistent-connections-per-server.

![image.png](https://help.xentral.com/hc/article_attachments/4996411827612)

Hier kannst du den Wert von 2 bzw. 6 auf 60 oder 100 parallele Downloads setzen. Ein Neustart des Browsers ist normalerweise nicht notwendig.

Weitere Informationen findest du in unserem Handbuch: