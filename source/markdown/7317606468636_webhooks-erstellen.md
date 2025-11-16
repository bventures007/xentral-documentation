> **Anmerkung**
>
> Das Webhooks-Feature ist ab Version 23.2.3 für alle Nutzer verfügbar.
>
> Da sich das Feature momentan in der Beta-Phase befindet, beobachten wir es genau und möchten sicherstellen, dass alle Events korrekt ausgelöst werden. Sind dir Probleme aufgefallen? Dann kontaktiere uns unter: api[at]xentral.com.

Ein Webhook erlaubt es dir, Informationen über Ereignisse in Xentral, sogenannte Events, in einem externen System zu empfangen. Du kannst zum Beispiel eine Benachrichtigung in deiner Anwendung erhalten, sobald ein neuer Auftrag erstellt wird. Diese Information wird über eine HTTP POST-Anfrage an dein externes System gesendet.

> **Tipp**
>
> Zusätzliche technische Informationen zu Webhooks und möglichen Events findest du in derEntwicklerdokumentation.

## Webhooks erstellen

> **Anmerkung**
>
> Das Erstellen von Webhooks erfordert Administrator-Rechte.

Gehe wie folgt vor, um einen Webhook zu erstellen:

1. Navigiere zu Einstellungen > Integrationen > Webhooks. Eine Liste aller aktiv verwendeten Webhooks wird angezeigt.
1. Klicke auf + Webhook erstellen. Sind keine Webhooks aktiv, findest du die Schaltfläche in der Mitte des Bildschirms. Ansonsten findest du sie auf der rechten Seite über deiner Liste.
1. Gib einen eindeutigen Namen für deinen Webhook ein. Der Name darf aus maximal 100 Zeichen bestehen.
1. Gib den URL-Endpunkt ein, der Informationen vom Webhook erhalten soll. Es sind nur sichere https-URLs erlaubt. Die URL darf aus maximal 255 Zeichen bestehen.
1. Achte auf den Signaturschlüssel. Er wird in deine Zwischenablage kopiert, sobald du die Erstellung des Webhooks abgeschlossen hast. Dieses Feld wird automatisch mit einer zufälligen 20-stelligen Zeichenfolge gefüllt, welche als Signaturschlüssel dient. Wenn du möchtest, kannst du ihn mit einer eigenen Zeichenfolge von 20 bis 255 Zeichen überschreiben oder den Schlüssel selbst in die Zwischenablage kopieren, indem du auf im Feld Signaturschlüssel klickst und die Zeichenfolge kopierst.
1. Wähle ein Event aus. Du kannst bei Bedarf auch mehrere Events auswählen. Der Webhook sendet immer dann Informationen an den Endpunkt, sobald eines der Events eintritt.
1. Klicke auf Erstellen. Der Signaturschlüssel wird in die Zwischenablage kopiert und erscheint ein letztes Mal auf dem Bildschirm. Klicke auf, um sicher zu stellen, dass der Schlüssel kopiert wurde.
1. Schließe das Fenster.

Dein neuer Webhook wird in der Liste der aktiven Webhooks angezeigt. In der Übersicht kannst du die URL-Endpunkte und zugehörigen Events deiner Webhooks schnell erkennen

## Webhooks bearbeiten und löschen

Alle Webhooks sind unter![createbookmark_x21.png](https://help.xentral.com/hc/article_attachments/7952128515356)

Einstellungen > Integrationen > Webhooksgelistet. Wenn du auf![PenIcon.png](https://help.xentral.com/hc/article_attachments/7952128603676)

Bearbeitenklickst, hast du zwei Optionen:

- Einstellungen bearbeiten - Du kannst den Namen, URL-Endpunkt und Signaturschlüssel ändern sowie Events zum Webhook hinzufügen oder entfernen. Falls du den Signaturschlüssel änderst, musst du ihn auch in deiner externen Anwendung anpassen.
- Webhook löschen - Klicke auf Webhook löschen unterhalb der Liste von Events und bestätige die Löschung. Das externe System wird nun keine neuen Informationen mehr über Events in Xentral erhalten.

## Signatur des Webhooks überprüfen

Der Header des HTTP-Requests des Webhooks besteht aus der `xentral-signature` und dem `xentral-request-timestamp`.

Die `xentral-signature` kannst du wie folgt überprüfen:

1. Bilde die Nachricht aus dem `RequestBody ` und dem`xentral-request-timestamp `. Hierzu gibst du den` RequestBody `ein und fügst diesem den` xentral-request-timestamp` ohne Leerzeichen oder ähnliches direkt an.
1. Generiere einen `HMAC ` aus der Nachricht und dem Signaturschlüssel mithilfe einer`SHA-256 ` Hashfunktion. DerSignaturschlüssel dient hierbei als`Secret Key`.
1. Vergleiche den hexadezimalen Output des HMAC mit der `xentral-signature` im Header des HTTP-Requests. Diese sollten identisch sein.

Wir können dies an einem Beispiel mit den folgenden Werten nachvollziehen:

- `RequestBody `: *{"type":"com.xentral.salesOrder.protocolCreated.v1","body":{"createdAt":"2024-05-28T17:30:07+02:00","salesOrderId":169,"salesOrderProtocolId":586}}*-` xentral-request-timestamp `: * 1716910210 *-` Secret Key`: * e4nRJ04Ss2m3EkQxn19V*

Dies führt zur folgenden Nachricht:

Nachricht: *{"type":"com.xentral.salesOrder.protocolCreated.v1","body":{"createdAt":"2024-05-28T17:30:07+02:00","salesOrderId":169,"salesOrderProtocolId":586}}1716910210 * Nachricht und `Secret Key` ergeben die folgende `xentral-signature` im Hexadezimal-Code bei Benutzung eines `HMAC` mit `SHA-256`: *67b9db5fbe8add6c5b073f42091f593e994de32c83741573015442c154214bcf*.