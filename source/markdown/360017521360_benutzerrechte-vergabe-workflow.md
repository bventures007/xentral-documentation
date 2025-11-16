## Benutzeraccount einrichten

Folgende Schritte sind notwendig, um einen Benutzeraccount vollständig anzulegen:

1. Adresse für den Benutzer (Mitarbeiter) anlegen
1. Rolle Mitarbeiter vergeben
1. Neuen Benutzer anlegen
1. Adresse auf diesen Benutzer verknüpfen
1. Einstellungen im Benutzeraccount vornehmen (z.B. Rechteeinstellungen)

### Adresse anlegen

Legen Sie direkt eine neue Adresse für den Mitarbeiter an:Stammdaten > Adresse

- Namen eingeben (ggf. auch direkt weitere Daten)
- Speichern

Weitere Informationen zur Adresse finden Sie auch[hier](https://help.xentral.com/hc/de/articles/360016721600#UUID-4a84b844-4f7d-7c54-898e-0f7fb80bd760).

### Rolle "Mitarbeiter" vergeben

Gehen Sie direkt in das TabRolleund vergeben Sie folgende Rolle:

- Rolle: "Mitarbeiter"
- von: "Projekt"
- Projektfeld: dieses Feld bitte leer lassen (alternativ: mit demjenigen Projekt füllen, für das der Mitarbeiter die Rechte erhalten soll)
- Abschließend klicken Sie aufals neue Rolle anlegen **Ergebnis **: Die Adresse hat nun eine fortlaufende Mitarbeiternummer aus dem Nummernkreis erhalten und die Berechtigung, die Vorgänge zu einem oder mehreren Projekten zu sehen.Es können beliebig viele Rollen vergeben werden. Die Mitarbeiternummer wird nur erstmalig mitvergeben (analog zu Kundennummer, Lieferantennummer). Unabhängig davon erfolgt die Vergabe der Menüpunkte. Diese werden direkt im Administrationsbereich[Benutzer](https://help.xentral.com/hc/de/articles/360016724780#UUID-f297da39-ce3c-8544-761b-4711490dd65a)individuell vergeben. Weitere Informationen zu ** Gruppen **finden Sie auch[hier](https://help.xentral.com/hc/de/articles/360016722000#UUID-27c9f5ac-bebe-bc23-79b2-b19285784cfc). ** Praxistipp**: Wenn Sie die Rechte nicht Projektspezifisch aufteilen müssen/ möchten, legen Sie im Standard bitte die Rolle Mitarbeiter an und lassen Sie das Projektfeld leer. Dann erhält der Benutzer automatisch auch die Berechtigung für neue Projekte, die später hinzukommen. Das ist inbesondere ratsam, da Daten, die keine Projektzuweisung haben, von Benutzern nicht gesehen werden können, wenn diese nicht die Rollenzuweisung auf ALLE Projekte besitzen. Nur Administratoren können immer alle Daten sehen.

### Neuen Benutzer anlegen

Administration > Einstellungen > System > Grundeinstellungen > Benutzer

- Legen Sie über den+NEUButton einen neuen Benutzer an
- Weisen Sie dem Benutzer die zuvor angegebene Adresse zu
- Vergeben Sie den Account-Typ:
  - Administrator: uneingeschränkter Benutzer mit allen Rechten
  - Benutzer: Benutzer mit vielen Rechten aber z.B: Einschränkungen bei den Systemeinstellungen oder auf Abteilungen/Teams/Bereiche
- Zugriff aus Ferne erlauben: nur falls geboten (z.B. bei Außendienst-Mitarbeitern) oder falls xentral auf einem externen Server installiert wurde, z.B. der xentral Cloud

Weitere Informationen zur Benutzerverwaltung finden Sie auch[hier](https://help.xentral.com/hc/de/articles/360016724780#UUID-f297da39-ce3c-8544-761b-4711490dd65a).

### Einstellungen im Benutzeraccount vornehmen

#### Menüpunkte vergeben

Nun können die Rechte im Benutzer vergeben werden (TabRechte): Am besten Sie überlegen zunächst, welche Menüpunkte der Mitarbeiter bekommen soll.

Zugewiesene Rechte werden blau angezeigt, nicht zugewiesene Rechte grau.

Sie können alle Rechte eines Moduls zuweisen oder entfernen. Um alle Rechte eines Moduls zuzuweisen, klicken Sie auf **Alle setzen ** neben der Modulbezeichnung. Um alle Rechte eines Moduls zu entfernen, klicken Sie auf**Alle entfernen** neben der Modulbezeichnung.

Sie können auch einzelne Rechte zu einem Modul vergeben. Klicke Sie dazu auf das entsprechende Recht eines Moduls. Beispiel:

![UserRights.png](https://help.xentral.com/hc/article_attachments/21346743556892)

#### Feinjustierung der Rechtevergabe

- Wie finde ich das einzelne Recht heraus?
- Klicken Sie aufVerkauf > Auftrag
- Klicken Sie oben in die Browserzeile: hier ist zu sehen: module=auftrag&action=list

![UserRights1.png](https://help.xentral.com/hc/article_attachments/21346743557916)

- module: zeigt immer den Hauptpunkt an
- action: zeigt immer das einzelne Recht an

Vergabe eines Menüpunktes: Ist meist das einzelne Recht "list". In der Praxis klicken Sie am besten direkt bei sich im Admin Account auf den gewünschten Menüpunkt. Die Browserzeile zeigt Ihnen dann das zu vergebende Recht an.

##### Systemlog

Der Systemlog ist eine Hilfefunktion, um bei der Vielzahl der Einzelrechte das fehlende Recht (Benennung mit Modul und Action) für einen Benutzer zu finden. Den Systemlog finden Sie unterApp Center > Systemlog. Klickt ein Mitarbeiter auf eine Aktion, deren Recht er nicht besitzt erhält er eine dementsprechende Meldung. Möchten Sie direkt dieses Recht neu vergeben, so prüfen Sie im Systemlog, auf welche Schaltfläche der Mitarbeiter geklickt hatte, als diese Meldung erschienen ist.

![UserRights2.png](https://help.xentral.com/hc/article_attachments/21346698922012)

Mitarbeiter 1 benötigt z.B. noch das Recht:

- Module: Kalender
- Action: Data

##### Einzelne Rechte

> **Anmerkung**
>
> Die vergebenen Rechte beziehen sich immer auf die Gesamtheit des verwendeten Moduls. Hat ein Nutzer z.B. das Rechteditim RechteblockAdresse, so kann dieser in jedem Bereich der Adresse Änderungen vornehmen. Es ist nicht möglich einzelne Felder für bestimmte Nutzer zu sperren, z.B. nur das FeldVertriebbesonders zu schützen.

Spezielle Rechte ohne Systemlog

Einige Rechte lösen keinen Eintrag im Systemlog aus, da die Funktion nicht klickbar ist oder der Menüpunkt nicht für den Benutzer ersichtlich ist. Hierzu zählt auch das Recht ajaxwerte (Modul Artikel), das dazu dient, dass auch Artikel in Positionen (z. B. im Auftrag) eingefügt werden können.

**Dokument / Adresse übernehmen**

Eine Adresse / ein Dokument / bestimmte Vorgänge können nur von einer Person bearbeitet werden. Ist die Person zu lange in diesem Vorgang bzw. evtl. aktuell nicht am Platz, aber dennoch eingeloggt, kann eine andere berechtigte Person den Vorgang übernehmen. Alle nicht gespeicherten Informationen des "Erstbesitzers" gehen hierbei jedoch verloren. Sollte man die Person nicht erreichen, kann man auf diese Weise jedoch trotzdem dringende Aufträge bearbeiten. Button ist für den Benutzer nicht sichtbar:

![UserRights3.png](https://help.xentral.com/hc/article_attachments/21346698923932)

Wenn Sie das folgende Recht zuweisen:

- Modul: Welcome
- Recht: unlock

wird ein Button zur Übernahme des Dokuments angezeigt:

![UserRights4.png](https://help.xentral.com/hc/article_attachments/21346698926236)

**Buttons und Aktionen**

Buttons und Aktionen sind meist keine einzelnen Rechte sondern greifen auf Module zurück - sie sind sozusagen Querverlinkungen in ein anderes Modul und ziehen sich dort die Rechte. Z.B. wird in einem Dokument beim Einfügen eines Ansprechpartners auf Rechte der Adresse zugegriffen. Der Benutzeraccount muss also diese Rechte freigeschaltet bekommen. Sie befinden sich im Modul Adresse. Button: Lieferadresse, Ansprechpartner

Modul: Adresse Action: ansprechpartnerpopup Action: lieferadressepopup

![UserRights5.png](https://help.xentral.com/hc/article_attachments/21346743565468)

**Sichteinschränkung pro Projekt** Bitte bedenken Sie, dass kein Eintrag im Systemlog erzeugt wird, wenn ein Benutzer aufgrund fehlender Projektzuweisung in den Rollen bestimme Daten nicht sehen kann. Dann muss das entsprechende Projekt noch als Rolle Mitarbeiter vergeben werden, oder falls die Daten keine Projektzuweisung besitzen, die Rolle Mitarbeiter auf ALLE Projekte.

## Beispiele zur Rechtevergabe

### Freigabe und Schreibschutz in Dokumenten

In diesem Beispiel sind beiAngebotalle Rechte vergeben worden bis aufSchreibschutzundFreigeben. Modul: Angebot Action: freigabe Action: schreibschutz

![UserRights6.png](https://help.xentral.com/hc/article_attachments/21346743567644)

### Grundlegende Rechte in Tabellen und Datensätzen

- list: ist immer die Ansicht der Tabelle z.B. Adresse list ist die Adresstabelle von außen
- edit: reinklicken und bearbeiten
- minidetail: ist in der Übersicht immer das graue kleine Pfeilchen zum aufklappen (das reicht ggf. auch bereits aus bei Artikeln oder Adressen)

![UserRights7.png](https://help.xentral.com/hc/article_attachments/21346698932124)

## Rechte-Datei verwenden

Man kann auch die Rechte eines Nutzers als Datei herunterladen und diese bei einem anderen Benutzer wieder heraufladen. In der Übersicht gibt es das Download-Icon:

![UserRights8.png](https://help.xentral.com/hc/article_attachments/21346698933916)

Um die Datei bei einem anderen Benutzer wieder heraufzuladen, können Sie im Benutzer ganz unten beiRechtedatei heraufladendie Datei hinterlegen:

## Spezielle Rechte im Projektdashboard

Für das Dashboard im Projekt hat man nun zusätzliche Einstellungsmöglichkeiten, um die Sichten der Mitarbeiter anzupassen/einzuschränken.