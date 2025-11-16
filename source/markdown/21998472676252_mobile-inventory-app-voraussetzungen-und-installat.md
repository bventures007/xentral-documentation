Du möchtest die Mobile Inventory App von Xentralfür die Inventur mithilfe mobiler Geräte in deinem Lager nutzen und fragst dich, was die allerersten Schritte sind? Dann bist du hier genau richtig.

In diesem Artikel erfährst lernst du,

- [auf welchen Geräten du die Mobile Inventory App nutzen kannst](#UUID-32630639-9f22-b6e2-b021-26a264f6f6f7_section-idm235098416252108)
- [welche allgemeinen Voraussetzungen vorab erfüllt sein sollten, damit du bestmöglich mit der Mobile Inventory App arbeiten kannst](#UUID-32630639-9f22-b6e2-b021-26a264f6f6f7_section-idm235098431517367)
- [wie du die Mobile Inventory App auf deinen Geräten installierst](#UUID-32630639-9f22-b6e2-b021-26a264f6f6f7_section-idm235110522967304)
- [wie du die notwendigen Benutzerrechte für die Mobile Inventory App in Xentral vergibst](#UUID-32630639-9f22-b6e2-b021-26a264f6f6f7_section-idm235110546247412) und
- [wie du dich in die App einloggst](#UUID-32630639-9f22-b6e2-b021-26a264f6f6f7_section-idm235110546542098).

## Hardware-Anforderungen und Empfehlungen

Um von den Vorteilen der Mobile Inventory App zu profitieren und eine möglichst fehlerfreie Inventur durchzuführen, nutzt du bestenfalls ein professionelles MDE-Gerät, das für die typischen Arbeitsabläufe im Lager geeignet ist. Je nach Größe deines Lagers und deiner Mitarbeiteranzahl verfügst du gegebenenfalls bereits über solche Geräte.

Wir empfehlen folgende Hersteller und Modelle:

- Zebra TC26
- Zebra MC 3300
- Honeywell
- Sunmi

> **Tipp**
>
> Für einen allerersten Test kannst du die Mobile Inventory App auch auf einem beliebigen Smartphone mit Android-Betriebssystem installieren. Voraussetzung hierfür ist, dass das Smartphone über eine integrierte Kamera verfügt, sodass du die Barcodes deiner Lagerplätze und Artikel scannen kannst.
>
> Wir empfehlen für den produktiven Einsatz der Mobile Inventory App dringend die Verwendung der oben genannten MDE-Geräate. Diese Geräte werden speziell für die Anforderungen der Lagerverwaltung konzipiert und bieten dir somit eine reibungslose und professionelle Benutzererfahrung.

## Allgemeine Voraussetzungen

Folgende Voraussetzungen gelten für die Mobile Inventory App, egal auf welchem Gerät du sie nutzt:

- **Aktuellste Xentral Version**: Um die bestmöglichste Stabilität sicherzustellen, empfehlen wir dir, stehts die aktuellste Version von Xentral zu verwenden.
- **Verfügbarkeit nach Plan**: Du kannst die Mobile Inventory App ab dem Business-Plan und höher nutzen. Verschaffe dir [hier](https://xentral.com/de/preise) einen Einblick in alle verfügbaren Xentral-Pläne und ihren Funktionsumfang.
- **Barcodes für Lagerplätze und Artikel**: Die Mobile Inventory App ist auf die Erfassung von Lagerplätzen und Artikeln per Barcode ausgelegt. Stelle sicher, dass all deine Artikel und Lagerplätze über eindeutige Barcodes verfügen.

## Mobile Inventory App installieren

Gehe wie folgt vor, um die Mobile Inventory App aus dem GooglePlay Store zu installieren:

1. Nimm dein gewünschtes Gerät zur Hand und suche im Google Play Store nach der App namens **Xentral Inventory**.
1. Tippe auf **Installieren**.

> **Wichtig**
>
> Falls dein MDE-Gerät nicht für Google-Dienste lizensiert ist, ist der oben beschriebene Installationsweg nicht möglich. Keine Sorge - du kannst die Mobile Inventory App trotzdem installieren, indem du die APK-Datei der App aus dem Google Play Store herunterlädst. Klicke auf den folgenden Link, um zu erfahren, wie das funktioniert und welche Schritte du in diesem Fall ausführen musst:
>
> - Anleitung: Eine APK-Datei aus dem Google Play Store herunterladen

### App-Login ermöglichen und PIN erstellen

Nachdem du die App auf deinem Gerät installiert hast, sorgst du im nächsten Schritt dafür, dass Benutzer sich in die App einloggen und mit ihr arbeiten können.

Der Login in die App funktioniert für jeden einzelnen App-Benutzer mithilfe eines persönlichen QR-Codes und einer PIN.

Entscheide zunächst, welche Benutzer deiner Xentral-Instanz mit der Mobile Inventory App arbeiten sollen und daher Zugang zur App bekommen sollen. Fahre dann mit den unten beschriebenen Schritten fort, um den App-Login für diese Benutzer freizuschalten und die benötigten PINs für den Login in die App festzulegen.

> **Wichtig**
>
> Falls du keine Berechtigung hast, um die Benutzerverwaltung aufrufen, kannst du die folgenden Schritte nicht durchführen. Besprich das weitere Vorgehen in diesem Fall bitte mit dem Admin deiner Xentral-Instanz.

1. Öffne in Xentral das Menü **Einstellungen > Grundeinstellungen > Benutzerverwaltung > Benutzer verwalten**.
1. Öffne den gewünschten Benutzer, indem du rechts auf das **Stift-Symbol** klickst.
1. Klicke auf das Tab **Mobile Apps**.
1. Falls noch kein QR-Code angezeigt wird, klicke auf **Mobile Device Token erstellen**.
1. Gib im Feld **PIN (4 Stellen, numerisch)** die gewünschte PIN ein, die der Benutzer später für den App-Login verwenden wird.
1. Klicke auf **PIN aktualisieren**.

### Benutzerrechte für die App vergeben

Um eine App mithilfe der Inventur vorzunehmen und alle benötigten Funktionen nutzen zu können, benötigen alle App-Benutzer, die **keine Admins** sind, mindestens die folgenden Berechtigungen:

- **Benutzer > list **

-** Projekt > list **

-** Warehouse > exportproducts**

Gehe wie folgt vor, um Benutzern diese Rechte zu erteilen.

1. Öffne in Xentral das Menü **Einstellungen > Grundeinstellungen > Benutzerverwaltung > Benutzer verwalten**.
1. Öffne den gewünschten Benutzer, indem du rechts auf das **Stift-Symbol** klickst.
1. Klicke auf das Tab **Rechte**.
1. Aktiviere im Bereich **Benutzer ** das Recht **list**.
1. Aktiviere im Bereich **Projekt ** das Recht **list**.
1. Aktiviere im Bereich **Warehouse ** das Recht **exportproducts**.

> **Anmerkung**
>
> Es ist nicht notwendig, auf **Speichern** zu klicken. Sobald du das gewünschte Recht anklickst, wechselt die Farbe von grau zu blau. Mehr ist nicht notwendig, um das Recht zu vergeben.

## In die Mobile Inventory App einloggen

Nachdem du alle bisher beschriebenen Schritte durchgeführt hast, bist du startklar für den Login in die App.

Gehe wie folgt vor, um dich in die Mobile Inventory App einzuloggen.

1. Öffne auf deinem mobilen Gerät die Mobile Inventory App.
1. Scanne am Bildschirm deines Computers den QR-Code, den du wie im Kapitel [App-Login ermöglichen und PIN erstellen](#app-login-ermoeglichen-und-pin-erstellen) beschrieben erstellt hast.
1. Gib die PIN ein, die du wie im Kapitel [App-Login ermöglichen und PIN erstellen](#app-login-ermoeglichen-und-pin-erstellen) beschrieben erstellt hast.