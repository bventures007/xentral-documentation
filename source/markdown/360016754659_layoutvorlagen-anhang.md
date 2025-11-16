Die App Layoutvorlagen Anhang dient dazu, Regeln zu definieren mit denen angelegte Layoutvorlagen aus der App Layoutvorlagen automatisch an zu versendende Belege angefügt werden können.

## Übersicht

Die Übersicht zeigt alle angelegten Anhangregeln in einer Livetabelle.

![layouttemplateattachment_1.png](https://help.xentral.com/hc/article_attachments/5078156043676)

Die EinstellungenSprache,LandundProjektwirken einschränkend: Wird hier etwas ausgewählt, so gilt die Regel nur für Belege, in denen diese Werte übereinstimmen und nur dann wird die Layoutvorlage mitverschickt.

Beispiel: Die erste Regel im Screenshot legt fest, dass die Layoutvorlage "ABC" als Anhang an alle Auftragsbestätigungen angefügt werden soll, die die Belegsprache Deutsch haben, an einen Kunden in Deutschland versendet werden und zum Projekt "TESTPROJEKT" gehören. Legt man eine weitere Regel an, in der keine Belegsprache, Land oder Projekt definiert sind, so würde diese Regel für alle Aufträge berücksichtigt werden, die von der ersten Regel ausgeschlossen werden.

## Neuen Anhang anlegen

Über+NEUkann eine neue Anhangregel angelegt werden. Dann kann man definieren, wann welche Vorlage als Anhang mitgeschickt werden soll.

- Modul: Modul bzw. zu welchem Beleg die Layoutvorlage immer als Anhang angefügt werden soll
- Layoutvorlage: Layoutvorlage, die mitgeschickt werden soll (muss zuvor in der App Layoutvorlagen hochgeladen sein)
- Sprache: Layoutvorlage wird nur mitgeschickt, wenn Belegsprache mit dieser übereinstimmt
- Land: Layoutvorlage wird nur mitgeschickt, wenn Land im Beleg mit diesem übereinstimmt
- Projekt: Layoutvorlage wird nur mitgeschickt, wenn Projekt des Belegs mit diesem übereinstimmt
- Aktiv: Die Regel ist aktiv (gültig)

## Variablen speziell für Layoutvorlagen Anhang

Die App kann mehrere Variablen verwenden:

- {MITARBEITER}: gibt den aktuell angemeldeten Mitarbeiter aus
- {DATUM_HEUTE}: gibt das aktuelle Datum aus
- {POSx_BESCHREIBUNG}: gibt die Artikelbeschreibung der x-ten Position aus (von angebot, auftrag, bestellung, gutschrift, lieferschein, rechnung, oder produktion). "x" ist mit der Positionsnummer ersetzen
- {POSx_HERSTELLERNUMMER}: gibt die Herstellernumme der x-ten Position des Artikel aus (von angebot, auftrag, bestellung, gutschrift, lieferschein, rechnung, oder produktion). "x" ist mit der Positionsnummer zu ersetzen
- {SPRACHE}: gibt die Sprache aus der dazugehörigen Adresse aus.

Alle Spalten aus der Positionstabelle des Belegs und der Artikeltabelle können verwendet werden. Gibt es in beiden Tabellen Überschneidungen, wie z.B. nummer, dann sticht die Positionstabelle die Artikeltabelle, da diese spezifischer ist.Die Schreibweise der Variablen bleibt weiterhin wie folgt, z.B. {POSx_EAN}.

Beispiel, wie man diese in der Layouvorlage einsetzen könnte:

![layouttemplateattachment_3.png](https://help.xentral.com/hc/article_attachments/5078139653020)