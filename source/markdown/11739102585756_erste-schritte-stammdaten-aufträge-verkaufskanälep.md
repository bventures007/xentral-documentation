In Xentral umfassen die Stammdaten Adressen und Artikel. Die Adressen bestehen aus deinen Kunden-, Lieferanten- und Mitarbeiterdaten, die Artikel aus deinen Waren. In den folgenden Abschnitten erfährst du, wie du diese anlegst und mit ihnen arbeitest.

> **Anmerkung**
>
> Du kannst bereits bestehende Stammdaten aus einem anderen System oder anderen Quellen nach Xentral importieren. Voraussetzung dafür ist, dass die Daten als CSV-Datei vorliegen.
>
> Weitere hilfreiche Informationen zum Import findest du zusammengefasst unterErsteinrichtungsartikel - Stammdatenimport - Adressen, Artikeloder im Handbuchartikel zum Datenimport:Import von Stammdaten und Unternehmensdaten.

Abschließend erfährst du etwas über das Arbeiten mit Aufträgen im Verkaufsprozess und der Abgrenzung einzelner Geschäftsbereiche mithilfe von Projekten.

## Adressen

Öffne in der linken Seitenleiste unter **Verkaufen > Adressen ** (im Classic Design: ** Stammdaten > Adressen **) die Adressenübersicht. Klicke hier auf**+NEU **, um eine neue Adresse anzulegen. Es öffnet sich ein Formular, welches für Kunden, Lieferanten und Mitarbeiter gleichermaßen gilt. Trage die neue Adresse in den Bereich[Stammdaten](https://help.xentral.com/hc/articles/4539623305500#UUID-e43fd5c1-e0e0-d665-e41b-d9f5cde1dbe9)ein und klicke auf ** Speichern**.

Du wirst nun aufgefordert der Adresse eine[Rolle](https://help.xentral.com/hc/de/articles/4544271298716-Adressstammdaten-pflegen#UUID-cdc4cbcc-2c78-f143-6e7f-88d87e4192a6_id_4544271298716_id_h_01G21R9ABAF35B85PVPQRAVW29)zuzuweisen. Dir stehen die Rollen **Kunde **, ** Lieferant ** und **Mitarbeiter** zur Verfügung, wobei auch eine Mehrfachauswahl möglich ist, wenn z.B. einer deiner Mitarbeiter gleichzeitig einer deiner Kunden ist. Je nachdem welche Rolle du zugewiesen hast, erhält die Adresse eine entsprechende Kunden-, Lieferanten- oder Mitarbeiternummer aus deinem Nummernkreis.

> **Anmerkung**
>
> Du kannst der Adresse jederzeit im Reiter **Rolle** weitere Rollen zuweisen. Informationen dazu findest du im ArtikelAdressstammdaten pflegen.
>
> Je nach Rolle kannst du unterschiedliche Belege direkt aus der Adresse erstellen:
>
> - Kunde: Angebot, Auftrag, Rechnung, Lieferschein, Gutschrift
> - Lieferant: Bestellung.

> **Tipp**
>
> Wie deine Mitarbeiter Zugang zu deiner Xentral-Instanz bekommen und du ihre Benutzerrechte anpassen kannst, erfährst du im EinrichtungsartikelSystem und Einstellungen (Einrichtung).

### Besonderheiten bei Adressen für Geschäftskunden (B2B)

Ein Geschäftskunde unterscheiden sich oft in einigen Aspekten von einem Standardkunden:

- **Mehrere Standorte (Lager, Filialen, etc.)**: Du kannst im Reiter ** Lieferadressen** mehrere Lieferadressen hinterlegen und anschließend im Auftrag die richtige Adresse als abweichende Lieferadresse auswählen.
- **Abweichende Rechnungsadresse **: Durch die Verwendung mehrerer Lieferadressen unterscheidet sich in der Regel die Rechnungs- von der Lieferadresse. Im ** Reiter Details > Unterreiter Adressdaten **kannst du im Bereich ** Stammdaten **ein Häkchen bei ** Abw. Rechnungsadresse** setzen und anschließend die Adresse eintragen.
- **Besteuerung **: Im ** Reiter Details > Unterreiter Zahlungskonditionen/ Besteuerung **kannst du im Bereich ** Steuer/ Währung/ Zoll **eine ** USt-ID** (= Umsatzsteuer-Identifikationsnummer) hinterlegen, sodass dein Kunden den Vorsteuerabzug nutzen kann.
- **Zahlung per Rechnung **: Im B2B-Bereich wird häufig mit Rechnung bezahlt. Im ** Reiter Details > Unterreiter Zahlungskonditionen/ Besteuerung** kannst du besondere Zahlungsbedingungen für Rechnungen hinterlegen.

## Artikel

Alles was du in Xentral verkaufst, wird als Artikel angesehen. Dazu gehören unter anderem die Lagerartikel, die du physisch in deinem Lager aufbewahrst und an deine Kunden verschickst. Zusätzlich werden aber auch nicht-physische Waren ohne Lagerbestand als Artikel angesehen. Zu dieser Kategorie gehören Versandkosten, Rabatte und Dienstleistungen.

Deine Artikel findest du unter **Verkaufen > Artikel ** (im Classic Design: ** Stammdaten > Artikel**). Hier sind alle von dir angelegten Artikel in einer Tabelle gelistet. Du kannst[Artikel suchen, filtern und bestehende Artikel bearbeiten](https://help.xentral.com/hc/articles/5355868449180#UUID-33f03def-c1b7-78d7-cbf5-ea2efe31fe45). Hier ist auch der Startpunkt, um neue Artikel anzulegen.

### Artikel anlegen

Klicke in der Artikeltabelle rechts oben auf **+ NEU**, um einen[neuen Artikel anzulegen](https://help.xentral.com/hc/articles/5355868375324#UUID-7b466ccc-d331-8e18-2f8e-9a396ad6b84d). Es öffnet sich ein Formular, in dem du eine Artikelbezeichnung eingeben sowie die Art des Artikels bestimmen musst. Für die Art des Artikels stehen dir vier Möglichkeiten zur Verfügung:

- **Lagerartikel**: Lagerartikel sind alle Artikel, für die ein Lagerbestand geführt wird.
- **Artikel ist Porto**: Mit einem Portoartikel kannst du Versandgebühren als eigene Position in Belegen darstellen.
- **Artikel ist Rabatt**: Mit einem Rabattartikel kannst du einen Rabatt auf den gesamten Auftrags- oder Rechnungswert gewähren und diesen im Beleg als eigene Position darstellen. Der Rabatt gewährt einen prozentuellen Nachlass auf den gesamten Auftrag.
- **Kein Häkchen**: Setzt du bei keiner der Optionen ein Häkchen handelt es sich um eine Dienstleistung.

Es gibt keine weiteren obligatorischen Felder. Die Artikelnummer wird automatisch aus dem entsprechenden Nummernkreis der gewählten **Artikelkategorie ** vergeben. Den Verkaufspreis des Artikels legst du im Reiter**Verkauf** fest.

Für Lagerartikel empfehlen wir dir dennoch die weiteren Felder bestmöglich zu befüllen, da sie in anderen Teilbereichen von Xentral eine wichtige Funktion haben können. So kannst du eine Artikelbeschreibung hinzufügen, die du an deine Online-Shops übertragen kannst oder eine Zolltarifnummer hinterlegen, die beim Versand ins Ausland wichtig wird. Eine Beschreibung weiterer Felder und ihrer Möglichkeiten findest du unter[Artikelstammdaten pflegen](https://help.xentral.com/hc/articles/5355868406428#UUID-1d1e8a13-6479-2b8d-d64e-2d5a4a044eb1).

### Stücklisten anlegen

Eine[Stückliste](https://help.xentral.com/hc/articles/360019652739#UUID-443f8048-37aa-3974-fc46-63cd8ad757d1)ist ein Artikel, der aus mehreren Artikeln oder Komponenten besteht. In Xentral wird dabei zwischen zwei Arten von Stücklisten unterscheiden:

- **Stückliste**: Eine Stückliste ist ein Artikel, der aus mehreren einzelnen Artikeln besteht, z.B. ein Geschenkkorb. Hierbei lagerst du die einzelnen Artikel zuvor aus und erstellst mithilfe der Stückliste einen neuen Artikel mit einer Artikelnummer und lagerst diesen einmal ein.
- **Just-in-Time (JIT) Stückliste**: Die Just-in-Time Stückliste bietet dir mehr Flexibilität in der Lagerhaltung. Die Bestandteile der Stückliste haben einen eigenen Lagerplatz und können in unterschiedlichen Stücklisten angeboten werden. Die Stückliste wird im Pickprozess zusammengestellt und die einzelnen Bestandteile werden erst beim Kauf der Stückliste aus dem Lager ausgebucht. Hast du z.B. mehrere Elektronikartikel im Angebot, die als Zubehör das gleiche Ladekabel benötigen, kannst du Geräte und Kabel getrennt lagern, um Kosten zu sparen.

Die Art der Stückliste legst du im Hauptartikel der Stückliste fest. Öffne einen Artikel und setze im Bereich **Sonstige Einstellungen ** ein Häkchen bei **Stückliste ** oder**Just-In-Time Stückliste **. Es erscheint der neue Reiter ** Stückliste**. In diesem kannst du weitere Artikel zur Stückliste hinzufügen.

> **Anmerkung**
>
> Du kannst die Einzelpositionen deiner Stücklisten für den Kunden in Belegen anzeigen oder ausblenden lassen. Alternativ kannst die Positionen einer normalen Stückliste in die Artikelbeschreibung aufnehmen.

### Varianten anlegen

Über Varianten kannst du schnell eine Reihe an ähnlichen Artikeln anlegen, z.B. Kleidung in unterschiedlichen Größen und Farben. Varianten legst du in Xentral über das[Matrixprodukt](https://help.xentral.com/hc/articles/360016725120#UUID-44725c2a-a728-20a2-d526-e12c9e8d88eb)an. Hierbei werden die Varianten aus einem allgemeinen Produkt (Elternartikel) hergeleitet, so können z.B. aus einem T-Shirt die Varianten rotes T-Shirt und blaues T-Shirt hergeleitet werden. Achte darauf die Artikelinformationen deines Elternartikels ausführlich zu pflegen, da dessen Artikelinformationen an die Varianten weitervererbt werden.

> **Anmerkung**
>
> Du kannst einen Artikel auch direkt als eine Variante eines Elternartikels anlegen. Wir empfehlen jedoch deine Varianten immer über das Matrixprodukt anzulegen, da dieses eine einfachere Bearbeitung bietet und viele Online-Shops Varianten in Form des Matrixprodukts bevorzugen.

Ein Matrixprodukt kannst du direkt im Artikel anlegen. Öffne den Artikel und setze im Bereich **Varianten ** ein Häkchen bei**Matrixprodukt **. Es erscheint der neue Reiter ** Matrixprodukt **. In diesem kannst du dem Artikel neue Eigenschaften zuordnen, z.B. eine Farbe. Klicke dazu auf ** neue Gruppe **, um die Eigenschaft anzulegen. Anschließend kannst du der Gruppe über ** Option hinzufügen**eine Ausprägung der Eigenschaft zuweisen, z.B. rot. In der graphischen Oberfläche kannst du aus den so entstehenden Kombinationen die Artikel auswählen, die du anlegen möchtest.

> **Tipp**
>
> Die so hinzugefügten Gruppen und Optionen gelten nur für den ausgewählten Artikel. Hast du bestimmte Eigenschaften, die du immer wieder für unterschiedliche Artikel benutzen möchtest, kannst du diese im Modul **Matrixprodukt** anpassen.
>
> Hier kannst du eine sogenannte Grundtabelle anlegen, in der die Eigenschaft mit ihren Optionen dauerhaft gespeichert ist. So kannst du einen Artikel schnell mit den benötigten Eigenschaften versehen.

## Aufträge

Der[Auftrag](https://help.xentral.com/hc/articles/6113604302620#UUID-a0cc0500-9af9-7a68-ed9d-3747c3458479)ist das wichtigste Element im Verkaufsprozess von Xentral. Aus diesem Beleg gehen alle weiteren Belege wie Lieferscheine und Rechnungen hervor.

Aufträge können auf drei Arten angelegt werden:

- **Weiterführung eines Angebots**: Dies ist besonders im B2B-Bereich üblich. Du kannst alle Daten des Angebots übernehmen und in einen Auftrag überführen.
- **manuell**: Du kannst Aufträge, die per Telefon oder E-Mail eingehen, manuell im System anlegen.
- **automatisch**: Dies ist der typische Fall im B2C-Bereich. Aufträge werden aus einem Online-Shop wie Shopify oder einem Marktplatz wie Amazon importiert und automatisch angelegt. Hierzu findest du mehr im Abschnitt Online-Shops.

Eine Auflistung aller Aufträge findest du unter **Verkaufen > Auftrag ** (im Classic Design: ** Verkauf > Auftrag**). Hier kannst du Aufträge bearbeiten und neue Aufträge manuell anlegen.

Bevor du mit der automatischen Anlage startest, empfehlen wir dir einige Aufträge manuell anzulegen, um dich mit den für einen Auftrag benötigten Informationen vertraut zu machen.

### Auftrag manuell anlegen

Klicke in der Auftragstabelle rechts oben auf **+ NEU **, um einen[neuen Auftrag anzulegen](https://help.xentral.com/hc/articles/360016758399#UUID-aa321171-0ea6-5098-d7eb-a8175197d560). Es öffnet sich ein neues Formular. In diesem solltest du zuerst im Feld ** Kunde **eine Kundenadresse aus deinen Adressstammdaten auswählen und auf ** übernehmen **klicken. Die für den Auftrag benötigten Stammdaten werden dann aus der Adresse übernommen. Dazu gehören neben der ** Adresse **auch weitere Informationen wie ** Projekt **, ** Zahlungsweise **, ** Versandart ** und **Besteuerung**. Bei Bedarf kannst du diese aber auch manuell anpassen und z.B. eine abweichende Lieferadresse eintragen.

Im Unterreiter **Positionen ** kannst du dem Auftrag Artikel hinzufügen. Der Verkaufspreis wird den Artikelstammdaten entnommen, kann über das**Stift **

-Symbol aber auch manuell angepasst werden. Im Unterreiter ** Vorschau**kannst du deine Angaben und die Gestaltung der Auftragsbestätigung überprüfen.

Klicke abschließend auf **Freigabe**. Hierdurch erhält der Auftrag eine Auftragsnummer aus dem zentralen Nummernkreis und kann weiter verarbeitet werden. Freigegebene Aufträge können nicht mehr gelöscht, sondern nur noch storniert werden. Außerdem wird durch die Freigabe die Auftragsampel für den Auftrag in der Übersicht aktiviert.

### Die Auftragsampel verwenden

Die[Auftragsampel](https://help.xentral.com/hc/articles/360016759019#UUID-a67e1eee-4a52-2b43-3f73-4782e28d05b7)hilft dir mithilfe farbiger Symbole dabei den aktuellen Status eines Auftrags nachzuvollziehen. Prozessschritte, die erfolgreich abgeschlossen wurden, werden grün angezeigt. Offene und noch zu prüfende Prozessschritte werden orange angezeigt.

![image-20240126-131415.png](https://help.xentral.com/hc/article_attachments/12913872428700)

Sobald alle Symbole grün angezeigt werden, kannst du den Auftrag an die Logistik weiter geben.

> **Anmerkung**
>
> Du kannst Symbole der Auftragsampel unter **Einstellungen > Dein System einrichten > Systemeinstellungen ** im Bereich**Auftragsampel ausblenden** aktivieren und deaktivieren.

### Aufträge über das Aktion-Menü verarbeiten (Lieferschein und Rechnung)

Über das **Aktion **

-Menü auf der rechten Seite kannst du einen[Auftrag auf vielfältige Weise verarbeiten](https://help.xentral.com/hc/articles/6113558323740#UUID-82a95736-aa02-4bd6-342c-1f937e949928). Du kannst unter anderem eine Auftragsbestätigung an deinen Kunden senden (** Auftrag abschicken **) oder die im Auftrag enthaltenen Artikel bei deinem Lieferanten nachbestellen (** als Bestellung weiterführen**). Die im Auftrag enthaltenen Informationen werden dabei komplett an den Folgebeleg weitergegeben und beeinflussen den Status des Auftrags nicht. Du kannst also mehrere unterschiedliche Belege aus einem Auftrag erstellen.

Die zwei wichtigsten Belege, die aus dem Auftrag hervorgehen können, sind der Lieferschein (**als Lieferschein weiterführen **) und die Rechnung (** als Rechnung weiterführen**). Im Falle einer Retoure kannst du die Rechnung auch zu einer Gutschrift weiterführen.

> **Anmerkung**
>
> Wenn du einen Beleg in einen neuen überführst, z.B. einen Auftrag als Rechnung weiterführst, werden die Belege miteinander verknüpft. Im Protokoll kannst du dann auf alle verknüpften Belege zugreifen, d.h. in diesem Fall siehst du die Rechnung, deren Bearbeiter und das Datum der Rechnungserstellung.

Bei der Übergabe an den Versand wird standardmäßig zu jedem Auftrag automatisch ein Lieferschein und eine Rechnung angelegt.

### Auftrag an die Logistik weitergeben (Auto-Versand)

Sind alle Symbole der Autragsampel grün, kannst du den[Auftrag an die Logistik weitergeben](https://help.xentral.com/hc/articles/6113578120092#UUID-99504608-d895-41ad-5059-de028e933077). Dazu stehen dir folgende Optionen zur Verfügung:

- **Einzelner Auftrag **: Wähle im ** Aktion **

-Menü des Auftrags ** Auto-Versand: an Versandzentrum übergeben**.
- **Mehrere Aufträge **: Markiere zuerst im Reiter ** Versandübergabe **alle Aufträge, die du versenden möchtest. Wähle dann im Bereich ** Stapelverarbeitung **“** Auto-Versand **” im Dropdown-Menü aus und klicke auf ** Ausführen**.
- **Automatische Weitergabe**: Hast du den [Prozessstarter](https://help.xentral.com/hc/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a) “autoversand_plus” eingerichtet, werden in regelmäßigen Abständen alle versandfertigen Aufträge automatisch an das Versandzentrum weitergeleitet.

> **Anmerkung**
>
> Weitere Informationen zum Versandprozess findest du im ArtikelLogistik und Lagerverwaltung.

## Vertriebskanäle/ Projekte

Der Verkauf von Artikeln kann in Xentral über[Projekte](https://help.xentral.com/hc/articles/360016723620#UUID-47d62f4f-3eac-f7b6-5144-f2353584abd5)gesteuert werden, die z. B. Einfluss auf den Import deiner Aufträge und deine Logistik haben. Du kannst mit Projekten Geschäftsbereiche voneinander abgrenzen (z.B. B2B und B2C) und eigene Logistikprozesse für jedes Projekt definieren.

Bevor du ein Projekt anlegst, solltest du dir überlegen, wie du dein Unternehmen aufbauen und welche Bereiche du voneinander abtrennen möchtest:

- Zielgruppe (B2B, B2C)
- Währung, Zoll und Steuern (Inland, Ausland)
- Vertriebswege (Filialen, Fulfillment by Amazon (FBA)/Fulfillment by Merchant (FBM))
- Logistikprozesse (Paketversand, Spedition)

> **Anmerkung**
>
> Wir empfehlen dir, für jeden Shop/ Marktplatz ein eigenes Projekt anzulegen. Dies ist besonders bei Amazon wichtig, falls du sowohl über FBA als auch über FBM verkaufst, da sich hier die Logistik drastisch unterscheidet.

Projekte erlauben es dir auch bestimmte Unternehmensbereiche Mitarbeitern zuzuordnen. Neben der Vergabe von Rechten, ist dies eine weitere Möglichkeit um den Datenschutz in deinem Unternehmen zu gewährleisten.

### Projekt einrichten

Ein neues[Projekt](https://help.xentral.com/hc/articles/360016723620#UUID-47d62f4f-3eac-f7b6-5144-f2353584abd5)kannst du unter **Einstellungen > Dein System einrichten > Projekte ** erstellen. Dabei kannst du entweder ein komplett neues Projekt erstellen oder ein bestehendes kopieren und nur leicht abwandeln. Gib eine **Bezeichnung ** und eine **Kennung ** ein. Diese helfen dir dein Projekt in der Software zu identifizieren. Alle weiteren Felder sind optional. Klicke auf**Weiter**.

Öffne anschließend den Reiter **Einstellungen**. Hier kannst du dein Projekt einrichten:

- **Grundeinstellungen**: Entscheide, ob E-Mails für bezahlte oder verpasste Zahlungen und bei Stornierungen versendet werden sollen. Außerdem kannst du ein eigenes Briefpapier für das Projekt einrichten.
- **Logistik / Versand**: Richte den Logistikprozess für das Projekt ein. Dazu gehören unter anderem die Wahl des Kommisionierverfahrens, eines Druckers und der zu druckenden Dokumente. Weitere Informationen zu Logistikprozessen findest du hier: [Logistik und Lager (Einrichtung)](https://help.xentral.com/hc/de/articles/11739147762332#UUID-3c034c43-eb9c-5e2a-81d3-c84579746e5d).
- **Eigene Nummernkreise**: Mit projektspezifischen [Nummernkreisen](https://help.xentral.com/hc/de/articles/5697692402204-Nummernkreise-verwenden) kannst du z.B. B2B und B2C steuerrechtlich trennen oder Aufträge aus dem Ausland besonders kennzeichnen.
- **Steuer / Währung**: Gib finanzielle Informationen zum Projekt an. Hier kannst du z.B. die Steuersätze und Währung angeben, falls es sich um ein Projekt im Ausland handelt. Standardmäßig sind die Werte für Deutschland eingetragen.

Optional kannst du noch Einstellungen zu deinem Kassensystem/ Point of Sale (POS) und die Adresse einer Filiale hinterlegen.