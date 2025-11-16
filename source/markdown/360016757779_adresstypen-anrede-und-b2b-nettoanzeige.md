Jede Adresse kann zu einem Kunden, Lieferanten, Partner oder einer internen Organisation gehören. Damit du diese Adressen nicht nur speichern, sondern auch sinnvoll strukturieren kannst, bietet Xentral die Möglichkeit, Adresstypen zu verwenden.

Adresstypen helfen dir dabei, deine Adressdaten nach bestimmten Kriterien zu gliedern – etwa nach Anrede, Unternehmensform oder Einsatzzweck. So stellst du sicher, dass die Kommunikation mit Kunden und Partnern konsistent bleibt und deine internen Prozesse klar voneinander abgegrenzt sind.

Standardmäßig stehen dir die Typen **Firma **, ** Frau **, ** Herr ** und **Sonstige ** zur Verfügung. Darüber hinaus kannst du **eigene Adresstypen** definieren und mit projektspezifischen Einstellungen verknüpfen.

> **Anmerkung**
>
> Grundsätze der Adresstypen:
>
> - Jeder Adresstyp sollte pro Projekt nur **einmalig ** mit einer**eindeutigen Bezeichnung** existieren.
> - Wenn mehrere Bezeichnungen für denselben Typ angelegt werden, verwendet das System automatisch die zuerst angelegte.
> - Eine gleichzeitige Anzeige mehrerer Bezeichnungen pro Typ ist nicht möglich.

**Praxisnutzen:**

- Einheitliche Anrede und Kommunikation mit Geschäftskunden.
- Automatische Anzeige der korrekten Preislogik (Netto statt Brutto).
- Klare Trennung in Projekten.

![adresse_typ.png](https://help.xentral.com/hc/article_attachments/21959671276188)

## Neuen Adresstyp anlegen

Gehe folgendermaßen vor, um einen neuen Adresstyp einzurichten: Du kannst den Menüpunkt **Adresse Typ ** entweder über die Smart-Search mit dem Begriff **Adresse Typ ** oder über **Einstellungen > Stammdaten > Adresse > Adresse Typ ** aufrufen. **Schritte:**

1. Klicke auf **Typ hinzufügen**.
1. Trage im Feld **Bezeichnung** den Namen des Typs ein. Z.B. Firma, Herr, Frau, Gewerblich, Privat. Diese Bezeichnung wird u.a. als Anrede in Serienbriefen oder Dokumenten verwendet.
1. Wähle im Feld **Typ ** den passenden Adresstyp aus: **Firma, Herr, Frau, Sonstige**.
1. Optional: Ordne im Feld **Projekt** ein Projekt zu, in dem dieser Typ gelten soll um eine Projekteinschränkung vorzunehmen.
1. Optional: Aktiviere **Anzeige Belege in Netto**, wenn Nettobeträge (z. B. B2B) für Belege auf diesen Adresstyp angezeigt werden sollen: * Netto Beträge zzgl. Steuer*.
1. Setze den Adress Typ auf **Aktiv**, um den neuen Adress Typ freizuschalten. Nicht mehr verwendete Adresstypen können deaktiviert werden.
1. Klicke auf **Speichern**. Der neue Adresstyp erscheint anschließend in der Übersicht und ist für eine Adresse auswählbar.

## Adresstyp bearbeiten

Bestehende Typen kannst du jederzeit ändern:

**Schritte**:

1. Klicke in der Übersicht auf das Stift-Symbol des gewünschten Typs.
1. Passe die gewünschten Felder an z.B. Bezeichnung.
1. Klicke auf **Speichern**. Der geänderte Adresstyp erscheint anschließend in der Übersicht und ist für eine Adresse auswählbar.

### Achtung

Stelle immer sicher, dass du den **korrekten Adresstyp** ausgewählt hast.

## Adresstyp deaktivieren oder löschen

Nicht mehr benötigte Adresstypen lassen sich entweder **deaktivieren ** oder**vollständig löschen **. ** Schritte deaktivieren:**

1. Öffne den Adresstyp über das **Stift-Symbol**.
1. Entferne den Haken bei **Aktiv** und speichere.

> **Anmerkung**
>
> In der Übersicht erscheint der Typ nun durchgestrichen.

**Schritte löschen: **

1. Klicke auf das **x-Symbol** neben dem Adresstyp.
1. Bestätige die Abfrage mit **OK**.

### Achtung

Der Adresstyp wird dauerhaft entfernt und nicht mehr angezeigt.

## Beispiel: Adresstyp für B2B-Kunden

In vielen Unternehmen ist es sinnvoll, separate Adresstypen für Geschäftskunden (B2B) anzulegen. Damit lassen sich bestimmte Einstellungen und Besonderheiten direkt steuern.

**Ein typisches Szenario: **

- Geschäftskunden benötigen in Angeboten und Rechnungen meist ** Nettopreise **, während Privatkunden (B2C)** Bruttopreise** sehen sollen.
- Dafür kannst du einen eigenen Adresstyp **B2B-Kunde ** anlegen und im Feld **Anzeige Belege in Netto** aktivieren.
- Sobald dieser Adresstyp einem Kunden zugewiesen ist, erscheinen alle Belege automatisch mit Nettobeträgen.

Zusätzlich kannst du den Adresstyp „B2B-Kunde“ einem bestimmten Projekt zuordnen, etwa wenn du deine Geschäftskunden in einem eigenen Vertriebsprojekt führst. Dadurch werden Auswertungen und Zuordnungen einfacher und sauberer getrennt.

## FAQ

### Warum wird der Adress-Typ ({ADRESSE_TYP}) nicht auf meinen Belegen angezeigt?

Ich möchte, dass der Adress-Typ (z. B. „Herr“, „Frau“, „Firma“) auch auf meinen Belegen wie Angebot, Auftrag oder Rechnung erscheint. Wie kann ich das einstellen?

**Antwort:**

Das Feld „Typ“ ist in der Adresse hinterlegt (standardmäßig frau, herr, firma in Kleinschreibung). Um es auf Belegen wie Angeboten, Aufträgen oder Rechnungen sichtbar zu machen, kannst du den Platzhalter {ADRESSE_TYP} in dein Beleglayout einfügen.

So gehst du vor:

- Öffne die gewünschte Vorlage für Angebot, Auftrag oder Rechnung. (Modul: Textvorlage in Belegen).
- Ergänze den Platzhalter {ADRESSE_TYP} an der Stelle, an der der Adress-Typ erscheinen soll.
- Speichere die Vorlage. Beim nächsten Belegdruck wird der Typ automatisch angezeigt.

Wenn du bestehende Typen umbenennst, müssen alle betroffenen Adressen neu zugewiesen werden, damit die Änderung auch in den Belegen greift.