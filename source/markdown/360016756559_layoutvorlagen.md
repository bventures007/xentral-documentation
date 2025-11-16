DieLayoutvorlagenkönnen Sie für Serienbriefe, Ausdrucke oder als Grundlage für den Zertifikatsgenerator nutzen.

## Erstellen einer Layoutvorlage

Als Ausgangspunkt für eine Layoutvorlage empfiehlt sich eine vorher erstellte Office Datei (z.B. Word, Open Office Writer), die als PDF exportiert wird. Auf diesem PDF können dann dynamische Variablen aus xentral, wie z.B. Adressdaten geladen werden.

Mit einem Klick auf den+NEU-Button können Sie eine neue Layoutvorlage anlegen. UnterHintergrundkönnen Sie sich das in Office erstellte PDF hochladen.

Klicken Sie aufSpeichernum die Vorlage zu sichern. Danach können Sie unterPositionen / ElementeTexte, Bilder und andere Elemente dynamisch mit Variablen hinzufügen. Dazu wählen Sie mindestens eine Beschreibung, den Typ, die Positionen des Elements und den Inhalt aus.

![layoutvorlagen_3.png](https://help.xentral.com/hc/article_attachments/5078191104284)

> **Anmerkung**
>
> Die gewünschte Position des Elements kann auch auf dem Papier abgemessen werden, um Zeit zu sparen. Unter Vorschau können Sie die Anordnung der Elemente begutachten. Hier wäre es der Adressblock in geschweiften Klammern (Variablen) unter der Adresse.

## Workflow Layoutvorlagen und Layoutvorlagen Anhang

Um zum Beispiel ein Deckblatt zu einem Angebot hinzuzufügen, musst du die Module Layoutvorlagen und Layoutvorlagen Anhang nutzen.

Du kannst mit dem Layoutvorlagen Modul (Suchleiste > Layoutvorlagen) dein Deckblatt hochladen:

Anschließend kannst du unter Positionen/Elemente in der erstellten Vorlage Elemente hinzufügen, wie z.B. den Namen. Anschließend kannst du die Position des Namens (über Variablen) einstellen:

![mceclip2.png](https://help.xentral.com/hc/article_attachments/5078154866204)

Anschließend musst Du in das Modul Layoutvorlagen Anhang (Suchleiste > Layoutvorlagen Anhang) und dort das erstellte Layout dem Angebot zuordnen:

![mceclip3.png](https://help.xentral.com/hc/article_attachments/5078138645660)

Wenn dann im entsprechenden Projekt (Stammdaten > Projekte > 'Dein Projekt XY' > Einstellungen > Logistik/Versand) dann der 'PDF Anhang' aktiviert ist, wird das Deckblatt jedes Mal mit ausgedruckt. Beim E-Mail Versand wird das Deckblatt als zusätzliche PDF-Datei angehängt:

![mceclip4.png](https://help.xentral.com/hc/article_attachments/5078191274908)

## Layoutvorlagen herunterladen

Wenn Sie besonders große / komplizierte Layoutvorlagen erstellen, kann es Sinn machen diese zu sichern um sie beliebig auszutauschen oder wiederzuverwenden. Klicken Sie dazu einfach in der Übersicht auf das Download-Symbol![mceclip1.png](https://help.xentral.com/hc/article_attachments/5078144568732)

.

### Variablen

Eine Liste aller Variablen, die sie im Moment in denLayoutvorlagenverwenden können:

- {NAME}
- {STRASSE}
- {PLZ}
- {ORT}
- {ANSCHREIBEN}

Weitere Variablen stehen Ihnen in der App[Layoutvorlagen Anhang](https://help.xentral.com/hc/de/articles/360016754659-Layoutvorlagen-Anhang)zur Verfügung.

## Serienbriefe

Folgende Variablen können als Elemente für Serienbriefe verwendet werden:

- {TITEL}: Titel der Adresse
- {NAME}: Name der Adresse
- {ABTEILUNG}: Abteilung der Adresse
- {ANSPRECHPARTNER}: Ansprechpartner der Adresse
- {STRASSE}: Straße der Adresse
- {ADRESSZUSATZ}: Adresszusatz der Adresse
- {PLZ}: PLZ der Adresse
- {ORT}: Ort der Adresse
- {LAND}: Land der Adresse
- {TELEFON}: Telefonnummer der Adresse
- {TELEFAX}: Telefax der Adresse
- {MOBIL}: Mobilnummer der Adresse
- {EMAIL}: E-Mail Adresse der Adresse
- {USTID}: USt ID der Adresse
- {KUNDENNUMMER}: Kundennummer der Adresse
- {LIEFERANTENNUMMER}: Lieferantennummer der Adresse
- {BANK}: Bankname der Adresse
- {INHABER}: Kontoinhaber der Adresse
- {IBAN}: IBAN der Adresse
- {BIC}: BIC der Adresse
- {WAEHRUNG}: Währung der Adresse
- {ANREDE}: Anrede der Adresse
- {FREIFELD1}: Freifeld1 der Adresse, die Zahl 1 kann mit den Zahlen von 1 bis 20 ersetzt werden
- {DATUM_HEUTE}: Heutiges Datum im Format dd.mm.jjjj

## Geburtstagskarten / Grußkarten

Es ist auch möglich verschiedenste Karten über die Layoutvorlage zu erstellen. Wie z.B. eine Geburtstagskarte, hier kann auch ein Hintergrund hochgeladen werden. Man kann aber auch bereits von einer Druckerei benutztes Druckpapier für verschiedenste Karten verwenden. Diese Layoutvorlagen können gespeichert und benutzt werden um Serienbriefe zu drucken.

Zu den Serienbriefen gelangt man über App Center > Serienbriefe.

Hier ist es möglich über den Filter Button z.B. nach dem Geburtstag von Personen (Geburtstag von Personen muss in den Adressen angelegt werden) zu filtern. Danach lassen sich ganz bequem für diese ausgewählten Personen Geburtstagskarten (oder auch andere Karten) drucken.

## Besuchsbericht

Über die Layoutvorlagen können Sie auch einen Besuchsbericht anlegen. Diesen können Sie dann in Adressen > Edit > Korrespondenz > Termine per Knopfdruck für den Kunden erstellen und drucken. In den Layoutvorlagen legen Sie eine Vorlage mit der Kategorie Besuchsbericht an.

Danach erscheint ein Button Besuchsbericht unter einem bestehenden Termin in der Adresse:

![layoutvorlagen_9.png](https://help.xentral.com/hc/article_attachments/5078144589724)

Nach einem Klick darauf, wird der Besuchsbericht mit den in der Layoutvorlage angelegten Variablen zum Kunden gedruckt.

### Variablen für Besuchsbericht

Adresse: Alle möglichen Felder aus der Kundenadresse (Tabelle adresse), z.B:

- {ADRESSE_NAME}
- {ADRESSE_ANSPRECHPARTNER}
- {ADRESSE_STRASSE}
- {ADRESSE_ORT}
- {ADRESSE_PLZ}
- {ADRESSE_TELEFON}{ADRESSE_MOBIL}
- {ADRESSE_EMAIL}

Kalender: Alle möglichen Felder aus einem Kalendereintrag (Tabelle kalender_event), z.B:

- {DATUM}
- {DATUMBIS}
- {UHRZEIT}
- {UHRZEITBIS}
- {BEZEICHNUNG}
- {BESCHREIBUNG}
- {BEARBEITER}

## Multilabelprint

Um das Modul Multilabelprint nutzen zu können, müssen Sie zuerst in den Layoutvorlagen ein neues Layout dazu anlegen.

Um verschiedene Artikel auf einen PDF-Bogen zu bekommen, werden die Variablen für den Inhalt der Layout-Elemente durchnummeriert. Z.B. {1_NUMMER}, {2_NUMMER} für die Artikelnummern der ersten beiden Artikel.

> **Anmerkung**
>
> Es muss immer nur die Nummerierung auf Seite 1 unterschieden werden. Ab Seite 2 wird dann wieder am Anfang der Nummerierung begonnen.

Beispiel: 4 Artikel passen auf 1 Seite. Wir markieren aber 7 Artikel im Modul Multilabelprint. Trotzdem müssen wir für die Artikelnummern nur {1_NUMMER}, {2_NUMMER}, {3_NUMMER} und {4_NUMMER} verwenden. Ab Seite 2 benutzt der 5. Artikel wieder die erste Variable, aber trotzdem seine richtige Artikelnummer.

### Variablen

Folgende Variablen können als Elemente für den Multilabelprint verwendet werden (X steht hierbei immer für die Nummerierung):

- {X_NUMMER}: Artikelnummer
- {X_NAME_DE}: Artikelbezeichnung
- {X_NAME_EN}: Artikelbezeichnung englisch
- {X_ANABREGS_TEXT}: Artikelbeschreibung
- {X_ANABREGS_TEXT_EN}: Artikelbeschreibung englisch
- {X_HERSTELLER}: Hersteller des Artikels
- {X_EAN}: EAN des Artikels
- {X_ZOLLTARIFNUMMER}: Zolltarifnummer des Artikels
- {X_GEWICHT}: Gewicht des Artikels
- {X_VERKAUFSPREIS}: Verkaufspreis des Artikels
- {X_EIGENSCHAFT_Y}: Eigenschaft des Artikels, Y muss hierbei mit dem Eigenschaftsnamen ersetzt werden, wie er unter Stammdaten > Artikel > Edit > Eigenschaften eingetragen wurde.
- {X_FREIFELD1}: Freifeld1 des Artikels, Zahl 1 kann durch beliebige Zahl von 1 bis 40 ersetzt werden
- {X_EINHEIT}: Einheit des Artikels
- {X_LAENGE}: Länge des Artikels
- {X_BREITE}: Breite des Artikels
- {X_HOEHE}: Höhe des Artikels
- {X_HERKUNFTSLAND}: Herkunftsland des Artikels
- {X_URSPRUNGSREGION}: Ursprungsregion des Artikels

Beispiel für einen PDF Bogen

In unserem Beispiel bilden wir folgendes ab:

- Artikelnummer
- Artikelname
- Verkaufspreis
- 2 Eigenschaftswerte
- Artikelbild

Als Elemente für 1 Seite erstellen wir 6 Beschreibungen und 6 Bilder:

![layoutvorlagen_10.png](https://help.xentral.com/hc/article_attachments/5078138771484)

Der Inhalt eines Beschreibungsfelds sieht z.B. so aus (3. Element):

![layoutvorlagen_11.png](https://help.xentral.com/hc/article_attachments/5078191478172)

> **Anmerkung**
>
> Für die Eigenschaften geben Sie bitte als Variable am Schluss den Eigenschaftsnamen an, wie er unter Stammdaten > Artikel > Edit > Eigenschaften eingetragen wurde. Groß/Kleinschreibung, Umlaute müssen dabei nicht genau beachtet werden. Als Vorschau im Mulitlabelprint Modul bekommen wir dann diesen PDF Bogen.

![layoutvorlagen_12.png](https://help.xentral.com/hc/article_attachments/5078138842012)

Sie können das Layout auch als JSON Datei hochladen. Den Code kopieren Sie in einen Texteditor und speichern die Datei als.json Datei. Danach laden Sie diese in den Layoutgenerator.

```{"Layout":{"id":"1","name":"Artikellabels","typ":"pdf","pdf_hintergrund":"","format":"A4","kategorie":""},"Layoutpositionen":[{"id":"1","layoutvorlage":"1","name":"beschreibung-1","beschreibung":"Beschreibung 1","typ":"textfeld","position_typ":"absolute","position_x":"10","position_y":"10","position_parent":"0","breite":"60","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"{1_NUMMER}\r\n{1_NAME_DE}\r\n{1_VERKAUFSPREIS} \u20ac\r\nFarbe: {1_EIGENSCHAFT_FARBE}\r\nGr\u00f6\u00dfe: {1_EIGENSCHAFT_GROESSE}","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"8"},{"id":"2","layoutvorlage":"1","name":"beschreibung-2","beschreibung":"Beschreibung 2","typ":"textfeld","position_typ":"absolute","position_x":"100","position_y":"10","position_parent":"0","breite":"60","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"{2_NUMMER}\r\n{2_NAME_DE}\r\n{2_VERKAUFSPREIS} \u20ac\r\nFarbe: {2_EIGENSCHAFT_FARBE}\r\nGr\u00f6\u00dfe: {2_EIGENSCHAFT_GROESSE}","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"7"},{"id":"3","layoutvorlage":"1","name":"beschreibung-3","beschreibung":"Beschreibung 3","typ":"textfeld","position_typ":"absolute","position_x":"10","position_y":"100","position_parent":"0","breite":"60","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"{3_NUMMER}\r\n{3_NAME_DE}\r\n{3_VERKAUFSPREIS} \u20ac\r\nFarbe: {3_EIGENSCHAFT_FARBE}\r\nGr\u00f6\u00dfe: {3_EIGENSCHAFT_GROESSE}","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"6"},{"id":"4","layoutvorlage":"1","name":"beschreibung-4","beschreibung":"Beschreibung 4","typ":"textfeld","position_typ":"absolute","position_x":"100","position_y":"100","position_parent":"0","breite":"60","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"{4_NUMMER}\r\n{4_NAME_DE}\r\n{4_VERKAUFSPREIS} \u20ac\r\nFarbe: {4_EIGENSCHAFT_FARBE}\r\nGr\u00f6\u00dfe: {4_EIGENSCHAFT_GROESSE}","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"5"},{"id":"5","layoutvorlage":"1","name":"beschreibung-5","beschreibung":"Beschreibung 5","typ":"textfeld","position_typ":"absolute","position_x":"10","position_y":"190","position_parent":"0","breite":"60","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"{5_NUMMER}\r\n{5_NAME_DE}\r\n{5_VERKAUFSPREIS} \u20ac\r\nFarbe: {5_EIGENSCHAFT_FARBE}\r\nGr\u00f6\u00dfe: {5_EIGENSCHAFT_GROESSE}","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"5"},{"id":"6","layoutvorlage":"1","name":"beschreibung-6","beschreibung":"Beschreibung 6","typ":"textfeld","position_typ":"absolute","position_x":"100","position_y":"190","position_parent":"0","breite":"60","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"{6_NUMMER}\r\n{6_NAME_DE}\r\n{6_VERKAUFSPREIS} \u20ac\r\nFarbe: {6_EIGENSCHAFT_FARBE}\r\nGr\u00f6\u00dfe: {6_EIGENSCHAFT_GROESSE}","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"5"},{"id":"7","layoutvorlage":"1","name":"1-produktbild","beschreibung":"1_produktbild","typ":"bild","position_typ":"absolute","position_x":"10","position_y":"40","position_parent":"0","breite":"50","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"4"},{"id":"8","layoutvorlage":"1","name":"2-produktbild","beschreibung":"2_produktbild","typ":"bild","position_typ":"absolute","position_x":"100","position_y":"40","position_parent":"0","breite":"50","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"3"},{"id":"9","layoutvorlage":"1","name":"3-produktbild","beschreibung":"3_produktbild","typ":"bild","position_typ":"absolute","position_x":"10","position_y":"130","position_parent":"0","breite":"50","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"2"},{"id":"10","layoutvorlage":"1","name":"4-produktbild","beschreibung":"4_produktbild","typ":"bild","position_typ":"absolute","position_x":"100","position_y":"130","position_parent":"0","breite":"50","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"1"},{"id":"11","layoutvorlage":"1","name":"5-produktbild","beschreibung":"5_produktbild","typ":"bild","position_typ":"absolute","position_x":"10","position_y":"220","position_parent":"0","breite":"50","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"1"},{"id":"12","layoutvorlage":"1","name":"6-produktbild","beschreibung":"6_produktbild","typ":"bild","position_typ":"absolute","position_x":"100","position_y":"220","position_parent":"0","breite":"50","hoehe":"40","schrift_art":"times","zeilen_hoehe":"5","schrift_groesse":"12","schrift_farbe":"#000000","schrift_align":"left","hintergrund_farbe":"#FFFFFF","rahmen":"0","rahmen_farbe":"#FFFFFF","sichtbar":"1","inhalt_deutsch":"","inhalt_englisch":"","bild_deutsch":"","bild_englisch":"","schrift_fett":"0","schrift_kursiv":"0","schrift_underline":"0","bild_deutsch_typ":"","bild_englisch_typ":"","sort":"1"}]}```

## Scheck

Layoutvorlagen werden auch benötigt um in dem Extra-Modul[Scheck](https://help.xentral.com/hc/de/articles/360016721360#UUID-e3b50722-8679-8b26-0d69-bf1f6a628df9)eine Scheckvorlage zu erstellen.

![layoutvorlagen_13.png](https://help.xentral.com/hc/article_attachments/5078191579292)

> **Anmerkung**
>
> Wichtig ist die Kategoriescheck. Ob ein Blanko-Scheck der Bank als PDF hinterlegt werden darf, sollten Sie mit Ihrer Bank abklären.