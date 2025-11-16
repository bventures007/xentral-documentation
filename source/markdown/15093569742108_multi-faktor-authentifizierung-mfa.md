## Was ist Multi-Faktor-Authentifizierung?

Die Multi-Faktor-Authentifizierung (MFA) - gelegentlich auch als Zwei-Faktor-Authentifzierung (2FA) bezeichnet - verwendet zwei unabhängige Authentifizierungsfaktoren, wie Wissen (Geheimcode), Besitz (Sicherheitsschlüssel) und Inhärenz (biometrische Merkmale) um die Identität eines Benutzers zu prüfen. Dies erhöht die Sicherheit, da mehrere Faktoren erforderlich sind, um Zugang zu gewähren, wodurch das Risiko unbefugter Zugriffe verringert wird.

Vor dem Login in Xentral verlangt die Multi-Faktor-Authentifizierung, dass zwei unterschiedliche und voneinander unabhängige Formen der Identifizierung vorgelegt werden, zum Beispiel ein zeitlich begrenztes One-Time-Password (OTP), das nur für eine einzige Sitzung oder Transaktion gültig ist. Zur Generierung des OTP wird häufig eine App auf einem mobilen Endgerät verwendet, beispielsweise Google Authenticator.

## App zur Authentifizierung nutzen

Du kannst die weit verbreiteten Apps **Google Authenticator ** oder **Microsoft Authenticator ** nutzen. **App herunterladen**:

1. Öffne den App Store (auf iOS-Geräten) oder den Google Play Store (auf Android-Geräten).
1. **App herunterladen **: Lade die App Google Authenticator herunter und installiere die App. ** Multi-Faktor-Authentifizierung beim nächsten regulären Login einrichten**:

1. Rufe die Login-Seite deiner Xentral Instanz auf.
1. Melde dich mit E-Mail und Passwort oder per Google-Login in Xentral an.
1. Beim ersten Login wird ein QR-Code angezeigt. Scanne den QR-Code mit deiner Authentifizierungs-App.
  **Optional**: Sollte ein Scan nicht möglich sein, kannst du alternativ auch einen Code anfordern.

1. Die App fügt automatisch den Account hinzu und beginnt, One-Time Passwords zu generieren.
1. Gib das One-Time-Password aus der App im Xentral Login ein, um dich vollständig einzuloggen.

> **Wichtig**
>
> Stelle sicher, dass du alle Wiederherstellungscodes, die während des Einrichtungsprozesses bereitgestellt werden, sicher speicherst. Diese Codes sind wichtig, falls du Zugriff auf dein Gerät verlierst.

## Multi-Faktor-Authentifizierung als Admin für deine Xentral Instanz aktivieren

Gehe wie folgt vor, um die Mutli-Faktor-Authentifizierung für alle Benutzer deiner XentralInstanz verpflichtend zu aktivieren.

1. Öffne das Menü **Einstellungen > Grundeinstellungen > Benutzerverwaltung > Multi-Faktor-Authentifizierung**.
1. Aktiviere die Option **Multifaktor-Authentifizierung aktiviert**.
1. Nach Aktivierung der Option **Multifaktor-Authentifizierung aktiviert** haben Admins die Möglichkeit, einzelne Benutzer ihrer Instanz von der MFA-Pflicht auszunehmen. Dies kann erforderlich sein, wenn es sich um gemeinsam genutzte Xentral-Konten handelt, die an Packstationen verwendet werden, für die eine Multi-Faktor-Authentifizierung-Anforderung eine unnötige Belastung darstellen würde.
1. Administratoren können ebenfalls die Einstellungen für die Multi-Faktor-Authentifizierung für einzelne Benutzer zurückzusetzen. Dies ist beispielsweise notwendig, wenn der Benutzer das Gerät verloren hat, mit dem er die Multi-Faktor-Authentifizierung durchgeführt hat oder wenn ein neues Gerät gekauft wurde. Eine genaue Anleitung findest du im Kapitel [Multi-Faktor-Authentifizierung entsperren (Gerät verloren)](#UUID-aa113e8e-3ec3-f46b-361a-0e97f78f7af1_section-id235141355039109).

## Multi-Faktor-Authentifizierung entsperren (Gerät verloren)

Falls ein Mitarbeiter das Gerät verliert, das er üblicherweise für die Multi-Faktor-Authentifizierung nutzt, kannst du als Admin folgende Schritte durchführen, um die Authentifizierung des Mitarbeiters wieder zu ermöglichen.

1. Logge dich als Administrator in Xentral ein.
1. Öffne das Menü **Grundeinstellungen > Benutzerverwaltung > Multi-Faktor-Authentifizierung**.
1. Finde den gewünschten Benutzer in der Liste.
1. Klicke in der Spalte **Aktionen ** auf **Zurücksetzen**.
1. Informiere den Benutzer, dass er sich nun erneut mit seiner Authenticator‑App und den benötigten Wiederherstellungscodes einloggen muss.