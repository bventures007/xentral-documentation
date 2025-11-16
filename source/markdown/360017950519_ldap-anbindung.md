Mit der LDAP Anbindung kann man den firmeninternen LDAP-Client mit xentral verbinden, um die Mitarbeiter über LDAP beim Einloggen in xentral identifizieren zu können.

> **Anmerkung**
>
> Die folgende Anleitung setzt das Wissen um den Umgang mit LDAP voraus. Unser Support kann Ihnen bei der Erstellung der Konfiguration nicht helfen - hier müssten Sie Ihren Systemadministrator fragen.

## Paket für LDAP nachinstallieren

Als Erstes muss man am Server das Paket php7.x-ldap nachinstallieren (also z.B. php7.0-ldap wenn der Server mit PHP 7.0 läuft).

## Einstellungen in den Firmendaten

Unter Administration → Einstellungen → System → Grundeinstellungen → System gibt es die folgenden Einstellungsmöglichkeiten:

- LDAP URI→ Die URI um Ihren LDAP-Client zu erreichen
- LDAP RDN→ Hauptgruppe der Nutzer, die sich einloggen können
- LDAP Basis DN→ Definiert, wo im Verzeichnisbaum abwärts die Suche nach bestimmten Objekten gestartet werden soll.
- LDAP Filter→ Innerhalb der Verzeichnisse kann nach hinterlegten Daten gefiltert werden. Z.B. kann man prüfen ob der Benutzer der passenden Gruppe angehört und ob es sich überhaupt um eine Person handelt. (Die Angabe des LDAP Filters ist Pflicht sonst klappt die Authentifzierung nicht)

**Hinweis:** Den entsprechenden Benutzernamen in Xentral können Sie auf 2 Weisen übergeben:

- %user%
- {USER}

**Beispiel** Beispiel für die Einstellungen auf einem Active Directory wäre z.B. Folgendes:

![LDAP-2.png](https://help.xentral.com/hc/article_attachments/4996396483740)

## Einstellung im Benutzer

Unter Administration → Einstellungen → Benutzer kann man innerhalb eines Benutzers dann das Anmeldeverfahren "LDAP Verzeichnis" ausgewählt werden.

Der Benutzername muss dem Namen des Benutzers im LDAP Verzeichnis entsprechen. Das Passwort kann leer gelassen werden

## Anmelden des Benutzers

Damit sich der Benutzer nun anmelden kann, braucht er seinen LDAP Benutzernamen und das Passwort des Benutzers im LDAP Verzeichnis.

## Interner Ablauf (für Administration)

Für ein besseres Verständnis ist im folgenden der interne Ablauf beschrieben.

```

  // Connect to the LDAP Server
$ds = ldap_connect($this->app->erp->Firmendaten("ldap_host"));

$search = $this->app->erp->Firmendaten("ldap_searchbase");
$filter = $this->app->erp->Firmendaten("ldap_filter");

$bind_name = str_replace('{USER}',$username,$this->app->erp->Firmendaten("ldap_bindname"));

// Bind LDAP server
$ldapbind = ldap_bind($ds, $bind_name, $password);

// Search on LDAP server
$sr=ldap_search($ds,$search, $filter);

// if find then bind

if(ldap_count_entries($ds,$sr) > 0)
if($ldapbind)
  
```