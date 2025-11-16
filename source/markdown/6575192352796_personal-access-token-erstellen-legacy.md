> **Anmerkung**
>
> Dieser Artikel bezieht sich auf die Verwendung von Personal Access Tokens (PAT) mit der alten Legacy API.
>
> Bitte beachte: Für neue Integrationen steht in Xentral ein neues PAT-Modul zur Verfügung. Dieses bietet erweiterte Funktionen wie projekt- und ressourcenspezifische Zugriffe, konfigurierbare Laufzeiten sowie feingranulare Berechtigungen (Create, Read, Update, Delete).
>
> **Für alle neuen Setups und Schnittstellen sollte ausschließlich das aktuelle PAT-Modul verwendet werden.**
>
> Die vollständige Dokumentation dazu findest du hier:Personal Access Token (NEU)

Personal Access Token erlauben es dir, aus einer externen Anwendung sicher mit Xentral-APIs zu kommunizieren. Diese Anwendungen können kleine Skripte sein, die du entwickelt hast, oder eine Anpassung eines Xentral-Partners. Mithilfe von Personal Access Token kannst du die API mit mehreren Anwendungen gleichzeitig verwenden.

> **Anmerkung**
>
> Du kannst dich mithilfe von Personal Access Token bei allen Xentral-APIs (aktuelle Xentral-API,REST-API,Standard-API) authentifizieren. Auf diese Weise musst du die Authentifizierungsmethode nicht wechseln, wenn du eine ältere API verwenden möchtest.
>
> Wir empfehlen dir aber im Regelfall die aktuelle Xentral-API zu verwenden, da die älteren REST- und Standard-APIs bei der Verwendung von Personal Access Token nicht alle Endpunkte verarbeiten können.
>
> Du findest eineListe nicht verfügbarer Endpunkteam Ende dieses Artikels.

## Personal Access Token erstellen

> **Anmerkung**
>
> Das Erstellen von Personal Access Token erfordert Administrator-Rechte.

Gehe wie folgt vor, um einen Personal Access Token zu erstellen:

1. Klicke auf deinen Benutzernamen unten links, um das Administrations-Menü zu öffnen und klicke dann auf Kontoeinstellungen.
1. Navigiere zu Entwickler Einstellungen > Personal Access Token. Es wird eine Liste aller aktiv verwendeten Token angezeigt.
1. Klicke auf + Token erstellen. Sind keine Token aktiv, findest du die Schaltfläche in der Mitte des Bildschirms. Andernfalls findest du sie auf der rechten Seite über deiner Liste.
1. Gib einen eindeutigen Namen für deinen Token ein. Der Name sollte nicht länger als 50 Zeichen sein.
1. Klicke auf Token erstellen. Der neue Token erscheint auf dem Bildschirm.
1. Klicke auf, um den Token zu kopieren. Die Nachricht Der Token wurde in die Zwischenablage kopiert erscheint.
1. Schließe das Fenster.

Der Name des Token erscheint nun in der Liste derPersonal Access Token.

Du kannst den Token in die Anwendung einfügen, der du Zugang zur XentralAPI verschaffen möchtest.

> **Warnung**
>
> Personal Access Token erlauben API-basierten Zugriff auf Xentral mit unbeschränkten Rechten und ohne Ablaufdatum. Da dies ein potenzielles Sicherheitsrisiko darstellt, wird empfohlen, Token nicht öffentlich zu teilen und nicht direkt in den Quellcode der externen Anwendung einzubauen. Achte darauf, dass du den Anwendungen, denen du Zugriff zu Xentral verschaffst, vollständig vertraust.
>
> Du kannst den Zugriff einer Anwendung auf die Xentral-API jederzeit beenden, indem du das entsprechende Token löschst.

## Personal Access Token bearbeiten und löschen

Alle Personal Acccess Token, die du verwendest, werden unterAdministrations-Menü > Konto Einstellungen > Entwickler Einstellungen > Personal Access Tokengelistet. Du kannst alle Token eingeschränkt bearbeiten. Wenn du aufBearbeitenklickst, hast du zwei Optionen:

- Namen ändern - Du kannst den Namen des Token verändern, um ihn besser von anderen Token unterscheiden zu können. Gib den neuen Namen ein und klicke auf Token aktualisieren.
- Token löschen - Du kannst der externen Anwendung den Zugriff auf die API entziehen, indem du auf Token löschen klickst. Die Software, die du über den Token angebunden hast, ist in der Xentral-Umgebung nicht mehr nutzbar. Du kannst gelöschte Token nicht wiederherstellen.

## Nicht verfügbare Endpunkte in der REST- und Standard-API

Auf die folgenden Endpunkte der Legacy-APIs kannst du über Personal Access Token nicht zugreifen. Diese Liste erhebt keinen Anspruch auf Vollständigkeit.

- /shopimport/auth
- /shopimport/syncstorage/{articlenumber:.+}
- /shopimport/articletoxentral/{articlenumber:.+}
- /shopimport/articletoshop/{articlenumber:.+}
- /shopimport/ordertoxentral/{ordernumber:.+}
- /shopimport/articlesyncstate
- /shopimport/statistics
- /shopimport/modulelinks
- /shopimport/disconnect
- /shopimport/reconnect
- /shopimport/status
- /shopimport/refund
- /v1/reports