Als Verkäufer im B2B Bereich möchtest du möglicherweise standardisierte Liefer- und Zahlungsbedingungen verwenden um Transportkosten, Transportrisiko und Lieferort auf deinen Belegen klar zu regeln. Hierzu kannst du die sogenannten International Commercial Terms (wie z.B. EXW - Ab Werk oder FCA - Free Carrier) kundenspezifisch in Adressen hinterlegen und in Dokumenten einsetzen.

## Lieferbedingungen einrichten

Schritte zum Anlegen von Lieferbedingungen:

1. Gehe zu **Administration > Lager und Logistik > Lieferbedingungen**.
1. Klicke auf **+NEU**.
1. Gib eine Lieferbedingung als Text ein z.B. EXW.
1. Klicke auf **Speichern**, und klicke zurück zur Übersicht der Lieferbedingungen.
1. Wiederhole die Schritte für weitere Lieferbedingungen.

![2548170768.png](https://help.xentral.com/hc/article_attachments/9217939816476)

## Schritte zum Einfügen von Lieferbedingungen auf dem Firmenbriefpapier

Die jeweilige Lieferbedingung kannst du durch Verwendung der Variable {LIEFERBEDINGUNG} auf dem Briefpapier (z.B. Auftrag oder Lieferschein) einblenden.

1. Gehe zu **Administration > System > Grundeinstellungen > Reiter Einstellungen > Untergeordneter Reiter Textvorlagen**.
1. Wähle die richtige Vorlage, in der du den Baustein anzeigen lassen willst z.B. **Auftrag Text vor Artikeltabelle**. Prüfe, ob die Variable ggf. bereits als Baustein eingefügt ist und z.B. nur nicht auf deinen Dokumenten angezeigt wird, weil du keine Lieferbedingung im Beleg hinterlegt hattest.
1. Klicke in das Textfeld und füge die Variable **{LIEFERBEDINGUNG}** ein.
1. Klicke auf **Speichern**.
1. Erstelle ein neues Dokument als Entwurf und prüfe in der Vorschau, ob deine Änderung korrekt angezeigt wird.

> **Anmerkung**
>
> Möchtest du, dass die Lieferbedingung nur dann auf dem Beleg erscheint, wenn eine Lieferbedingung im Beleg ausgewählt wurde, nutze folgenden Baustein:
>
> {IF}{LIEFERBEDINGUNG}{THEN}Lieferbedingung: {LIEFERBEDINGUNG}{ELSE}{ENDIF}
>
> Weiterführende Informationen findest du bei denTextvorlagen.

## Lieferbedingungen in Kundendaten und auf Belegen einfügen

### Schritte zum Hinzufügen einer Lieferbedingung zu einer Kundenadresse

In einer Kundenadresse kannst du die Lieferbedingung auswählen und fest hinterlegen. Die Lieferbedingung wird bei der Erstellung eines Beleges automatisch aus den Adressdaten mit übernommen. (Sofern du die Variable für die Lieferbedingung in den Briefpapier Einstellungen hinterlegt hast s.o.)

1. Gehe zu **Stammdaten > Adressen** und wähle die gewünschte Adresse aus.
1. Unter **Stammdaten ** wähle das Feld **Lieferbedingung** aus.
1. Gib eine Lieferbedingung an, z.B. **EXW**, und wähle diese in der Suche aus.
1. Klicke auf **Speichern**.

![2548072460.png](https://help.xentral.com/hc/article_attachments/9217956401692)

### Schritte zum Einfügen einer Lieferbedingung auf einem Dokument

Die Lieferbedingung kannst du auch individuell für einen Auftrag oder Lieferschein eingeben oder ändern. Beim Erstellen eines neuen Belegs wird die Lieferbedingung automatisch aus den Adressdaten übernommen, wenn du die Variable für die Lieferbedingung in den Textvorlagen hinterlegt hast (s.o.).

1. Für einen Auftrag gehe zu **Verkaufen > Auftrag**.
1. Klicke auf den gewünschten Auftrag, den du bearbeiten möchtest.
1. Gehe zu den Zahlungs- und Versanddaten im Auftrag und wähle das Feld **Lieferbedingung** aus.
1. Klicke auf **Lieferbedingung ** und wähle die gewünschte Lieferbedingung, z.B. **EXW**.
1. Klicke auf **Speichern**.

![2548236306](https://help.xentral.com/hc/article_attachments/9217925528604)

Die Lieferbedingung wird nun im Dokument angezeigt.

![2547482755.png](https://help.xentral.com/hc/article_attachments/9217952271004)