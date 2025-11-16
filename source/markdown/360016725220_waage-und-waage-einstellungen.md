> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Mit den Modulen **Waage ** und **Waage Einstellungen ** bietet xentral eine mobile Oberfläche, an welche eine Waage angeschlossen werden kann. Diese kann z.B. im Produktionsprozess genutzt werden, um Artikel zu wiegen und zu kontrollieren. Hierfür wird die App **Waage ** benötigt. Es können auch Buttons mit bestimmten Artikeln vorbelegt werden, über welche direkt die Etiketten für die Produkte gedruckt werden können. Hierfür wird die App**Waage Einstellungen** benötigt.

## Waage Einstellungen

In **Waage Einstellungen ** können die Artikel festgelegt werden, die auf den vier Flächen der Waage-Oberfläche in der**Waage** App erscheinen sollen.

### Neuen Artikel für die Waage hinzufügen

Mit dem **+NEU** Button kann eine der Schaltflächen auf der Waage belegt werden:

- **Beschriftung**: Die eingepflegte Beschriftung für den Artikel ist auf der Waage-Oberfläche sichtbar
- **Artikel**: Es ist der Artikel, der hinter einer Fläche der Waage stehen soll und dann auch ausgebucht wird, auszuwählen
- **Button Nummer**: Hier sind die Nummern 1 bis 4 wählbar, die den Platz auf der Waage-Oberfläche festlegen
- **MHD Datum + in Tage**: Gibt das MHD Datum auf dem Etikett an (Variable {MHDDATUM}) und nimmt dafür das heutige Datum und summiert dieses mit dem eingegebenen Wert
- **Etikettendrucker Auswahl**: Hier kann aus dem Drop-Down-Menü ausgewählt werden, welcher Etikettendrucker das Etikett drucken soll
- **Etikett XML**: Etikett in XML, das beim Abschluss gedruckt werden soll

Beispiel Etikett

```
  <label>
  <barcode y="1" x="3" size="8" type="2">{NUMMER}</barcode>
  <line x="3" y="10" size="3">Xentral Bonbons</line>
  <line x="3" y="13" size="3">Gewicht: {GEWICHT} kg</line>
  <line x="3" y="16" size="3">Haltbar bis: {MHDDATUM}</line>
</label>

  
```

## Waage

Im folgenden Beispiel wurden die Artikel Taster, Gehäuse, Tischfräse und Rahmen eingestellt und einem der vier Buttons der Waage zugewiesen. Die Oberfläche der App Waage sieht dann so aus:

![scale_1.png](https://help.xentral.com/hc/article_attachments/5080846935964)

Mit einer angeschlossenen Waage kann nun das Gewicht gewogen werden, auf eine der Schaltflächen geklickt und das Etikett ausgedruckt werden.

## Anbindung der Waage

Unter **Administration > Einstellungen > Adapterbox ** ist die Adapterbox für die Waage einzurichten. In Schritt 3 bei**Verwenden als: ** die Option ** Waage** auswählen und das Modell der Waage auswählen, um die Waage an xentral anzubinden.

### "PCE-PB N" Waage Einstellungen: Dauermodus einstellen

1. Taste **Unit ** und**Return** für 2 Sekunden gemeinsam drücken bis ein Geräusch ertönt
1. Danach die Taste **Unit ** drücken bis**SEnd** im Display erscheint
1. Mit der Taste **Return** in das Menü gehen
1. Taste **Unit ** drücken bis **ConT ** im Display erscheint, danach mit der Taste**Return** bestätigen