## Installation der benötigten Programme

Damit Sie Ihre Daten aus Lexware Warenwirtschaft Premium exportieren können, benötigen Sie folgende Software:

- LX Connect
- Razor SQL

> **Anmerkung**
>
> Alle Anwendungen müssen als 32-bit laufen. Beachten Sie, dass sowohl Lexware, als auch LX Connect und Razor SQL auf dem selben System (Server / Rechner) installiert sein müssen.

## Daten eingeben in LX Connect

1. Starten Sie LX Connect und melden Sie sich mit den selben Zugangsdaten wie bei Lexware an
1. Wählen Sie die zutreffende Firma aus und klicken Sie auf Einrichtung starten

## Verwendung von Razor SQL

### Datenbank Verbindung herstellen

Als nächstes starten Sie Razor SQL und klicken oben links auf "Click to connect to a Database" um die Datenbankverbindung herzustellen. Mit einem Klick auf Connect wird die Verbindung hergestellt.

### Neuere Versionen von RazorSQL

Wenn Sie eine neuere Version haben, könnte es sein, dass Sie erstmal diese Oberfläche sehen:

![Lexware4.png](https://help.xentral.com/hc/article_attachments/21633891242140)

Hier können Sie auch anhand der angelegten Verbindung prüfen, welcher Database Type vorhanden ist und diesen auswählen.

Als nächsten Schritt müssen Sie an der Seite die Option mit "JDBC" wählen und können die Daten dann entsprechend eingeben.

> **Anmerkung**
>
> Der Treiber-Datenort ist in RazorSQL vorhanden und kann dort für den entsprechenden Datenbank-Typ ausgewählt werden.

### Datenbanken einsehen und exportieren

Nun sollten alle Datenbanktabellen der gewählten Firma auf der linken Seite zu sehen sein.

Unter F2 → Owners → F1 → FK_xxx sind die benötigten Daten zu finden. Je nach Ihrer Version bzw. Softwareart (Lexware Premium, Handel, Faktura) können die Tabellen in welchen Ihre Daten zu finden sind abweichen. Grundsätzlich beginnen diese in der Regel jedoch mit „FK_“.

Suchen Sie die benötigten Tabellen und klicken Sie jeweils mit der rechten Maustaste auf den Tabellennamen. Wählen Sie aus dem Menü "View Content (Fetch all Rows)" aus, um alle Inhalte der Tabelle anzuzeigen.

Im unteren, rechten Fenster werden Ihnen die Tabelleninhalte gezeigt. Klicken Sie auf einen Spaltennamen und drücken Sie anschließend "STRG + A" um den gesamten Tabelleninhalt zu markieren.

Klicken Sie auf das Icon "Export Query Results" um die Daten in eine Datei zu speichern.

![Lexware9.png](https://help.xentral.com/hc/article_attachments/21633891242908)

Das Zielformat können Sie frei wählen, für xentral jedoch benötigen wir eine CSV Datei mit den Spaltennamen in der ersten Zeile. Falls Sie als Zielformat eine CSV Datei gewählt haben, wählen Sie die Auswahl "Delimited File" und legen falls nötig weitere Eigenschaften fest.

Für einen kompletten Datenimport in xentral, benötigen wir folgende Dateien:

- FK_Anschrift => weitere Lieferanschriften
- FK_Artikel => Artikelbeschreibungen
- FK_Auftrag => Aufträge, Rechnungen, Angebote, Gutschriften und Lieferscheine
- FK_AuftragPos => Beleg-Positionen
- FK_Branchen => falls Sie Branchen in Lexware festgelegt hatten und diese übernehmen möchten
- FK_Kontaktperson => weitere Ansprechpartner
- FK_Kunde => Kundendaten
- FK_Kunde2Kontaktperson =>Zuordnung von Kunde zu Kontaktperson
- FK_Kundengruppen => Kundengruppen
- FK_Preis => Preise der Artikel
- FK_Preismatrix => Preise der Artikel