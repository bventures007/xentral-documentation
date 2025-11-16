## Wie man das Modul in Xentral konfiguriert

- Das Modul ist konfigurierbar über /index.php?module=xero&action=settings.

- Client-ID und Client Secret erstellen und dann in Xero konfigurieren. Die Client-ID und das Client Secret findest du in der Xero-App.

![mceclip0.png](https://help.xentral.com/hc/article_attachments/5077629388700)

Den entsprechenden Link für den Rückruf findest du unter /index.php?module=xero&action=settings.

> **Anmerkung**
>
> Die Xero-Integration unterstützt nur Rechnungen und Gutschriften, aber keine Verbindlichkeiten.

### Füge Client ID und Client secret zum System hinzu

Gehe zu /index.php?module=xero&action=settings.

Nachdem du auf Speichern geklickt hast, wirst du zu Xero weitergeleitet, um die Erlaubnis für die App zu bestätigen.

Klicke auf Zulassen, um fortzufahren. Du wirst wieder zu Xentral geleitet.

![mceclip2.png](https://help.xentral.com/hc/article_attachments/5077617466524)

![mceclip4.png](https://help.xentral.com/hc/article_attachments/5077565675804)

Für den Rest brauchst du dem System lediglich einige Rechnungen oder Gutschriften hinzufügen und sicherstellen, dass der Prozessstarter aktiviert ist.

- Transaktionsfehler prüfen: /index.php?module=xero&action=error
- Erfolgreiche Transaktionen prüfen: /index.php?module=xero&action=log
- Rechnungen von Xero prüfen

![mceclip5.png](https://help.xentral.com/hc/article_attachments/5077629489308)

![mceclip6.png](https://help.xentral.com/hc/article_attachments/5077609481756)