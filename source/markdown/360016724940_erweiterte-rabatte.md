Mit dieser App ist es möglich, neben relativen Rabatten auch absolute Rabatte für bestimmte Kunden, Gruppen, Artikel usw. zu definieren.

Um Rabatte anzulegen:

1. Öffne die App Erweiterte Rabatte. Der Reiter **Details** zeigt alle bestehenden Rabatte.
1. Klicke auf **+NEU**.
1. Ein Dialogfenster öffnet sich. Wähle im Feld **Basis Typ ** die gewünschte Art des Rabatts: **Prozente Rabatt ** oder **Preis Rabatt**.
  Das Dialogfenster wird je nach Auswahl mit den passenden Feldern erweitert.

1. Wähle im Feld **Typ ** aus, ob der Rabatt für einen**Kunden **, eine ** Gruppe ** (z.B. Lieferanten) oder ** Allgemein** sein soll.
  - Hast du als Typ **Kunde ** ausgewählt, gib im nachfolgend angezeigten Feld**Kunde** den gewünschten Kunden ein oder suche nach deinem Kunden mit dem Lupen-Symbol.
  - Hast du als Typ **Gruppe ** ausgewählt, gib im nachfolgend angezeigten Feld**Gruppe** die gewünschte Gruppe ein oder suche nach deiner Gruppe mit dem Lupen-Symbol.
  - Bei Auswahl des Typs **Allgemein** musst du keine entsprechende Eingabe vornehmen. Der Rabatt gilt dann für alle.
1. Wähle im Feld **Art ** aus, ob der Rabatt für einen spezifischen**Artikel **, eine Artikel-** Kategorie ** oder alle Artikel (** Allgemein**) gelten soll.
1. Hast du als ArtArtikelausgewählt, gib im nachfolgend angezeigten FeldArtikelden gewünschten Artikel ein oder suche nach ihm mit dem Lupen-Symbol.Hast du als ArtKategorieausgewählt, gib im nachfolgend angezeigten FeldArtikelkategoriedie gewünschte Artikelkategorie ein oder suche nach ihr mit dem Lupen-Symbol.Bei Auswahl der ArtAllgemeinmusst du keine entsprechende Eingabe vornehmen. Der Rabatt gilt dann für alle Artikel.
  - Hast du als Art **Artikel ** ausgewählt, gib im nachfolgend angezeigten Feld**Artikel** den gewünschten Artikel ein oder suche nach ihm mit dem Lupen-Symbol.
  - Hast du als Art **Kategorie ** ausgewählt, gib im nachfolgend angezeigten Feld**Artikelkategorie** die gewünschte Artikelkategorie ein oder suche nach ihr mit dem Lupen-Symbol.
  - Bei Auswahl der Art **Allgemein** musst du keine entsprechende Eingabe vornehmen. Der Rabatt gilt dann für alle Artikel.
1. Gib je nach ausgewählten Rabatt Folgendes ein:
  - Für einen **Preis Rabatt **: Gib den rabattierten Betrag (mit Währungszeichen, Berechnung in EUR) in das Feld ** Betrag **ein. Optional: Setze ein Häkchen bei ** Rabatt in Beschreibung ausweisen**.
  - Für einen **Prozente Rabatt **: Gib den gewünschten Rabattprozentsatz (ohne Prozentzeichen) in das Feld ** Rabatt**ein.
1. Optional: Setze ein Häkchen bei **Rabatt als Artikel ** und wähle dann im nachfolgend angezeigten Feld**Rabattartikel** den entsprechenden Rabattartikel.
1. Optional: Gib eine Mindestmenge in das Feld **Ab Menge** ein. Mit Erreichen dieser Mindestmenge wird der Rabatt angewendet.
1. Setze ein Häkchen bei **Aktiv**.
1. Klicke auf **Speichern **. ** Die Ausgabe im Beleg (Auftrag) sieht wie folgt aus:**

![erweiterte_rabatte_auftrag_004-1.png](https://help.xentral.com/hc/article_attachments/15589324866204)

> **Anmerkung**
>
> Es können nicht mehrere Rabatte auf denselben Artikel angewendet werden. Der erste passende Rabatt wird angewendet, die restlichen Rabatte werden ignoriert.

Die Rabatte werden in folgender Reihenfolge angewendet:

- (1) Artikel und Kunde
- (2) Artikelkategorie und Kunde
- (3) Artikel und (Kunden-)Gruppe
- (4) Artikelkategorie und (Kunden-)Gruppe
- (5) Artikel, allgemein
- (6) Artikelkategorie, allgemein
- (7) Allgemein, Kunde
- (8) Allgemein, (Kunden-)Gruppe
- (9) Allgemein, allgemein

Weitere Anpassungen kannst du über Template Skripte vornehmen. Das gleichzeitige Ausweisen von beispielsweise prozentualen und absoluten Rabatten ist aktuell nicht möglich.