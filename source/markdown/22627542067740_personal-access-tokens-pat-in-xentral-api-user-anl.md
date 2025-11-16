In Xentral kannst du über sogenannte Personal Access Tokens (PAT) dedizierte API-Accounts anlegen, um externe Anwendungen oder interne Skripte sicher mit der Xentral-API zu verbinden. Diese API-Accounts ermöglichen eine feingranulare Steuerung von Rechten und Zugriffen, ohne dass persönliche Benutzerkonten oder Passwörter genutzt werden müssen. So lässt sich klar definieren, welche Daten und Aktionen (Lesen, Erstellen, Ändern, Löschen) über die API erlaubt sind und wie lange der Zugriff gültig bleibt.

Mit **Personal Access Tokens (PAT)** lassen sich externe Anwendungen oder interne Skripte sicher mit der Xentral-API verbinden. PATs ersetzen dabei klassische Zugangsdaten und bieten die Möglichkeit, präzise festzulegen, ** wie lange **ein Zugriff gültig ist und ** welche Daten **gelesen, erstellt, geändert oder gelöscht werden dürfen. ** Funktionen:**

-** Granulare Ressourcenzugriffe (Scopes)**: Für jede Ressourcengruppe wie CRM, Produkte oder Buchhaltung lässt sich individuell steuern, ob der Token Zugriff hat.
- **Feingranulare Berechtigungen (CRUD)**: Innerhalb einer Ressource kann unterschieden werden, ob Daten gelesen, erstellt, aktualisiert oder gelöscht werden dürfen. ** Hinweis**: CRUD-Rechte legen fest, ob ein Token Daten erstellen (Create), lesen (Read), aktualisieren (Update) oder löschen (Delete) darf, und ermöglichen so eine feingranulare Steuerung des Zugriffs.
- **Konfigurierbare Laufzeit**: Jedes Token erhält ein Ablaufdatum, das frei definiert werden kann (Standard: 180 Tage). Abgelaufene Tokens verlieren automatisch ihre Gültigkeit.
- **Logging**: Alle Aktionen rund um Tokens (Erstellung, Änderungen, Sperren) werden protokolliert, was die Nachvollziehbarkeit und Sicherheit erhöht.
- **Lock-Funktion**: Admins können Tokens sperren.
- **Admin-View**: Administratoren haben eine zentrale Übersicht über alle ausgestellten Tokens und können diese verwalten.
- **Automatisches Entfernen inaktiver Tokens**: Tokens, die länger als 180 Tage nicht genutzt wurden, werden automatisch gelöscht. Vorher erhält der Besitzer Erinnerungsmails mit der Möglichkeit zur Verlängerung.

## Einen neuen Token erstellen **Schritte:** Token erstellen (für Admins > Men Bereich):

1. **Zugang zum Modul: ** Öffne das Menü unter:** Kontoeinstellungen > Developer Einstellungen > Personal Access Token**. Prüfe vorab, ob du die notwendigen Rechte hast. Nur Admins dürfen standardmäßig Tokens erstellen.
1. **Neuen Token anlegen **: Klicke oben rechts auf „** Token erzeugen**“. Damit startest du den Erstellungsdialog.
1. Allgemeine Angaben pflegen:
1. **Scopes (Zugriffsbereiche) zuweisen**: Lege fest, auf welche Datenbereiche der Token zugreifen darf:
1. **CRUD-Rechte (feingranular) einstellen **: CRUD-Rechte legen fest, ob ein Token Daten erstellen (Create), lesen (Read), aktualisieren (Update) oder löschen (Delete) darf, und ermöglichen so eine feingranulare Steuerung des Zugriffs. Für jede Ressource können gezielt Berechtigungen vergeben werden: ** Allgemeines Beispiel**: Ein Reporting-Tool benötigt oft nur Leserechte, während eine Integrationsschnittstelle möglicherweise auch Erstellen und Aktualisieren benötigt – Löschen sollte nur in Ausnahmefällen erlaubt werden.

  Ein Reporting-Tool benötigt nur **Read **. Ein ERP-Sync-Prozess braucht Read und ** Update **. ** Delete ** sollte nur in Ausnahmefällen vergeben werden, da es zu **Datenverlust** führen kann.

1. **Token erstellen und protokollieren **: Klicke auf „** Erstellen**“, um den Token zu generieren.

> **Warnung**
>
> **Sicherheitsmaßnahmen umsetzen:**
>
> - Stelle sicher, dass der Token nicht unverschlüsselt verteilt wird (keine E-Mail/Chat).
> - Nutze zentralisierte Ablagen oder Secrets-Management-Systeme (z. B. Vault, Passwort-Manager).
> - Überprüfe regelmäßig die Übersicht im Modul und entferne nicht mehr genutzte Tokens.
> - Beachte, dass ungenutzte Tokens nach 180 Tagen automatisch entfernt werden, der Besitzer jedoch vorher benachrichtigt wird.
> - Admins sollten strikt das **Minimalprinzip ** anwenden –**aktiviere nur die Scopes, die für den konkreten Anwendungsfall zwingend erforderlich sind.**

## Einen Token bearbeiten

Du kannst einen bestehenden Personal Access Token in Xentral nur in einem sehr eingeschränkten Rahmen bearbeiten. Konkret lässt sich ausschließlich die Laufzeit (Duration) anpassen – also das Ablaufdatum des Tokens verlängern oder verkürzen.

### Achtung

Möchtest du die Rechte (Scopes oder CRUD-Berechtigungen) eines Tokens ändern oder neue Rechte hinzufügen, musst du dafür einen neuen Token erstellen. Der alte Token sollte anschließend gelöscht werden, um Doppelungen und potenzielle Sicherheitsrisiken zu vermeiden.

**Kurz**:

- Ablaufdatum ändern = bearbeiten,
  Rechte ändern = neu erstellen.

So stellst du sicher, dass die Berechtigungen eines Tokens jederzeit klar nachvollziehbar sind und keine unkontrollierten Rechte im System verbleiben.

![personal_access_token_005.png](https://help.xentral.com/hc/article_attachments/22676301131036)

## Token Übersicht (für Admins)

Über die **Smart Search ** kannst du direkt nach **Personal Access Token ** suchen und so eine **zentrale Admin-Ansicht ** öffnen. Diese Ansicht steht ausschließlich **Admins ** zur Verfügung. Dort wird eine vollständige Liste aller im System erstellten Tokens angezeigt – inklusive**Token-Name **, ** Scopes **, ** Ablaufdatum **, ** Status **, ** zuletzt verwendet ** sowie dem jeweiligen **Ersteller (Admin)**.

Damit haben Administratoren jederzeit Transparenz über sämtliche ausgestellten Tokens im System und können deren Nutzung, Laufzeiten und Zuständigkeiten zentral überwachen. Dies erleichtert sowohl die Verwaltung als auch die Einhaltung von Sicherheitsrichtlinien.