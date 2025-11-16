## Inhaltsverzeichnis

- Online-Shop-Anbindung: Einstellungen
  - Schnittstelle anlegen
  - Schnittstelle
  - Allgemeine Einstellungen
  - Einstellungen für Shop oder Marktplatz
  - Aktionen
  - Alle Einstellungen im Überblick
  - Einstellungen zum Auftragsimport
  - Einstellungen zum Artikel Import und Export
  - Einstellungen zu den Rabatten
  - Einstellungen zu den Positionen im Auftrag
  - Einstellungen zum Adressen Import
  - Kommunikations-Einstellungen
  - Weiterführende Informationen zu den Einstelloptionen
  - Multiprojekt Shop (Sonderfunktion)
  - Vorab als bezahlt markieren
  - Artikelbilder übertragen
  - Lagerzahlen Übertragung erlauben
  - Lagerkorrektur überschreiben
  - Auftragsstatus rückmelden
  - Manuelle Adressübertragung
  - Freitext aus Shopschnittstelle
  - Gesamtbetrag festsetzen und Maximale Differenz zur berechneten Summe
  - Artikel für Porto, Nachnahmegebühr und Rabatt
  - Porto
  - Nachnahmegebühr
  - Rabatt
  - Extra Verkaufspreise
  - Zugangsdaten für Xentral Import Plugin
  - Zeiträume
  - Modus für die Einrichtungsphase oder Shopumstellungen
  - Import der Artikel aus dem Shop nach Xentral (Einrichtungsphase/ Erstimport)
  - Artikeleinstellungen für den Online-Shop
  - Import von Aufträgen aus Online Shops
  - Synchronisation der Lagerzahlen
  - Vorraussetzungen für den Lagerzahlensync
  - Artikel zum Shop exportieren/aktualisieren
  - Zahlungsweisen Mapping
  - Einstellungen
  - Versandarten Mapping
  - Einstellungen
  - Freifelder Mapping
  - Freifeldname aus dem Shop herausfinden
  - Freifelder eintragen
  - Subshop
  - Gruppen Mapping
  - Shopfunktionen: Featurematrix für Shopschnittstellen

# Online-Shop-Anbindung: Einstellungen

Administration → Online-Shops / Marktplätze

In diesem Artikel wird die Anbindung von Online Shops und Marktplätzen (z.B. Amazon, Shopware, Shopify) an Xentral beschrieben. In jedem Shopimporter gibt es allgemeine und importer-spezifische Einstellungen, die hier näher erläutert werden.Bitte beachten Sie, dass nicht alle Shopschnittstellen auch alle Features beherrschen. Eine Übersicht darüber, welche Schnittstellen welche Features bieten finden Sie in Xentral unter Administration → Online Shops → Shopfunktionen.

## Schnittstelle anlegen

Um einen neuen Shop anzulegen, können Sie unter Administration → Online Shops → NEU einen neuen Importer anlegen. Je nachdem welches Shopsystem Sie anbinden wollen, können Sie das entsprechende Modul auswählen.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_1.png)

Im Anschluss gelangen Sie in die angelegte Schnittstelle und können Ihre Zugangsdaten eintragen und speichern.

## Schnittstelle

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_2.png)

## Allgemeine Einstellungen

Bezeichnung → Name frei wählbar für den Shop (wird z.B. im Artikel und im Import-Menü angezeigt). Aktiv → Haken setzen, damit die Schnittstelle aktiv ist. Nicht mehr benötigte Schnittstellen können auf inaktiv gesetzt werden. Projekt → Verknüpfung des Shops auf ein Projekt. Im Projekt können die Logistikeinstellungen vorgenommen werden. Abholmodus → Je nach Shopschnittstelle gibt es hier unterschiedliche Optionen, z.B: nach Status, Datum oder Nummer.

Import Modus:- Demo (zum Testen) → Der Auftragsstatus im Shop nicht umgestellt, keine Artikel oder Lagerzahlen übertragen.

- Manuell (mit Importzentrale) → Die Aufträge werden erst abgeholt, wenn der Button Aufträge abholen geklickt wird.
- Automatisch (per Prozessstarter) → Die Aufträge werden regelmäßig automatisch vom Shop abgeholt. Hierfür wird der [Prozessstarter Shopimporter](https://xentral.com/helpdesk/prozessstarter?#nav-prozessstarter--auftragsimport-aus-dem-shop---shopimporter) benötigt.

Nur 1 Auftrag pro Anfrage: Es wird nur 1 Auftrag pro Anfrage vom Shop übertragen. Aufträge in Zwischentabelle: Beim Abholen der Aufträge werden die Aufträge nicht direkt angelegt, sondern erstmal zum Durchschauen in einer Zwischentabelle gespeichert. Hier kann man entscheiden welche Aufträge man anlegen will und welche erst später importiert werden sollen. Anzahl abholen begrenzen: Möglichkeit um eingehende Aufträge auf einmal zu begrenzen. Steht nichts (0) drin gilt die Default-Begrenzung von 100

## Einstellungen für Shop oder Marktplatz

Diese Einstellungen sind je Shop-Schnittstelle unterschiedlich und beinhalten unter anderem die Felder für die Zugangsdaten, die Sie eintragen müssen um die Verbindung zwischen Xentral und Shop herzustellen, das können z.B. eine API URL, ein Admin-Benutzername und ein API Key (Passwort). Pro Schnittstelle sind allerdings andere Daten notwendig.

Unten finden Sie shopspezifische Einstellungen. Nähere Informationen finden Sie in den Artikeln zu der jeweiligen Schnittstellen.

## Aktionen

Rechts finden Sie Buttons für verschieden Aktionen, die Sie in der Shopschnittstelle durchführen können.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_3.png)

Verbindung prüfen

Xentral überprüft, ob mit den eingetragenen Zugangsdaten eine Verbindung zum Shop erfolgreich hergestellt werden konnte. Bei einer erfolgreichen Verbindung wird 'success' angezeigt. Falls im Shop mehrere Subshops existieren, werden die Subshops und deren IDs aufgelistet.

Eine graue Meldung bedeutet, dass die Verbindung erfolgreich ist. Sollte die Verbindung nicht klappen, wird eine rote Fehlermeldung angezeigt. In diesem Fall sind wahrscheinlich die Zugangsdaten falsch und müssen noch einmal überprüft werden.Unter Umständen müssen Aufträge im Shop vorhanden sein, damit der Test der Verbindung erfolgreich ist, da diese Funktion einen Dummy-Request für die Auftragsabholung schickt, um zu prüfen, ob einen Antwort vom Shop kommt. Gegebenenfalls können Sie dafür im Shop einen Testauftrag anlegen. Ab Version 19.3 wird ein anderer Request gesendet, sodass die Verbindungsprüfung auch ohne vorhandene Aufträge klappt.Aufträge abholen

Holt alle Aufträge vom Shop ab, die zu den Einstellugnen passen (gemäß Auftragsstatus, Nummer, etc.). Der Button muss nur beim Manuellen Importmodus betätigt werden.

Shopimport Zwischentabelle

Springt zur Zwischentabelle der Aufträge vom Shop. Die Zwischentabelle wird nur im Manuellen Importmodus befüllt und wenn die Option 'Aufträge in Zwischentabelle' aktiviert ist.

Artikelliste abholen

Gleicht die Artikel im Shop mit denen in Xentral ab. Fehlende Artikel werden angelegt, bereits vorhandene werden aktualisiert (im Moment verfügbar für Magento, Shopify und Shopware).

Abgeglichen werden Name, Nummer, Artikelbeschreibung und Standardpreis des Artikels.Damit die Artikelliste abgeholt werden kann, wird der Prozessstarter Artikelimport (Link zum Prozessstarter) benötigt.

## Alle Einstellungen im Überblick

## Einstellungen zum Auftragsimport

Die Einstellungen in den Optionen regeln die Art der Übertragung und Synchronisation zwischen Xentral und Shop. Bitte beachten Sie, dass nicht jede Shopschnittstelle auch jede Funktion unterstützt. Welche Shopschnittstellen welchen Funktionsumfang abdecken, entnehmen Sie bitte den Artikeln zu den einzelnen Schnittstellen.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_5.png)

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_4.png)

- Zahlungweisen-Mapping verwenden → Zahlungsweisen in Xentral sollen auf Zahlungsweisen im Shop verknüpft werden.
- Versandarten-Mapping verwenden → Versandarten in Xentral sollen auf Versandarten im Shop verknüpft werden.
- Vorab als bezahlt markieren → Aufträge aus dem Shop werden in Xentral vorab als bezahlt markiert
- UTF8-Codierung → Der Shopimporter verwendet die UTF8-Codierung (bitte aktiveren, um Anzeigefehler bei Sonderzeichen usw. zu vermeiden!)
- Multiprojekt Shop → In diesem Shop werden Artikel aus verschiedenen Projekten angeboten
- USt. geprüft + Freigabe für Versand → Der Haken 'UST-ID geprüft' wird in alle Aufträgen aus dem Shop automatisch gesetzt, sodass die Umsastzsteuer-Prüfung die Aufträge für den Versand freigibt
- Porto → Artikel aus Xentral, der die Versandkosten aus dem Shopauftrag als eigene Position abbildet (mehr Informationen unten)
- Porto ermäßigt → Artikel aus Xentral, über den ermäßigte Versandkosten für Aufträge aus diesem Shop, abgebildet werden sollen
- Portoartikel anlegen → Falls kein Portoartikel hinterlegt ist, wird ein Portoartikel mit der Bezeichnung aus dem Shop angelegt und in den Auftrag in Xentral eingefügt, um das Porto abzubilden
- Nachnahmegebühr als extra Position → Bei Nachnahme-Aufträgen wird die Nachnahme-Gebühr als eigene Position im Auftrag eingefügt
- Nachnahmegebühr → Artikel in Xentral, der die Nachnahmegebühr als Auftragsposition abbildet
- Auftragsstatus rückmelden → Xentral darf den Status importieren Aufträge nach der Verarbeitung in der Logistik zurückmelden
- Automatische Rückmeldung deaktivieren → Deaktiviert die automatische Rückmeldung der Auftragsstati an den Shop
- Hole jeden Status → Es werden unabhängig vom Status alle Aufträge vom Shop zu Xentral übertragen
- Freitext aus Shopschnittstelle → Kundeninformationen/Kundenkommentare werden mit in den Auftrag nach Xentral ins Feld 'Freitext' übernommen und werden somit auf den Dokumenten mit abgedruckt
- Angebote statt Aufträge anlegen → Die Aufträge aus dem Shop werden in Xentral nicht als Aufträge, sondern als Angebote angelegt
- Autoversand bei Kommentar in Warenkorb deaktivieren → Hat der Kunde im Shop ein Kommentar beim Checkout im Shop hinterlassen, so wird der Autoversand für diesen Auftrag in Xentral deaktiviert (und erlaubt somit ein manuelles Prüfen der Aufträge durch den Mitarbeiter)
- Stornierung rückmelden → Wird ein Auftrag in Xentral storniert, wird die Stornierung an den Shop gemeldet, damit der Auftrag auch dort den Status 'storniert' bekommt (aktuell verfügbar für Shopify, Shopware und WooCommerce)
- Besteuerung im Drittland abhängig von Lieferadresse machen → Die Besteuerung bei Export-Aufträgen wird anhand der Lieferadresse statt an der Rechnungsadresse bestimmt
- Gesamtbetrag festsetzen → Der Gesamtbetrag der Aufträge wird aus dem Shop für Xentral übernommen und nicht in Xentral neu aus den Artikelpositionen berechnet
- Maximale Differenz zur berechneten Summe → Bereich, für den die Einstellung Gesamtbetrag festsetzen gelten soll. Nützlich z.B. wenn Auftragssummen auf 0,05 Währungseinheiten gerundet werden oder es zu Rundungsfehler bis zu 1 Cent kommt
- Lastschriftdaten in Adresse überschreiben → Die Lastschriftdaten einer Adresse im Adressstamm werden überschrieben, wenn sie bei einem Shopauftrag dieses Kunden abweichend waren

## Einstellungen zum Artikel Import und Export

- Lagerzahlen Übertragung erlauben → Xentral darf die Lagerbestände der Artikel in den Shop exportieren
- Lager Grundlage → Lagerbestand des Artikels, der an den Shop gemeldet werden soll (Verkaufbare oder gesamter Lagerbestand minus Reservierungen)
- Lagerkorrekturwert überschreiben → Der hier eingetragene Lagerkorrekturwert wird für alle Artikel an den Shop gemeldet und muss somit nicht mehr pro Artikel im Artikelstamm gepflegt werden (anklicken, damit Lagerkorrekturwert eingetragen werden kann)
- Pseudolager Regeln → Meldet Lagerzahlen [nach einem über Formeln einstellbaren Regelwerk](https://xentral.com/helpdesk/kurzanleitung-pseudostorage?) an den Shop
- Artikel Übertragung erlauben → Xentral darf Artikel in den Shop exportieren
- Bilder übertragen → Xentral darf Artikelbilder in den Shop exportieren
- Eigenschaften übertragen → Xentral darf Artikeleigenschaften in den Shop exportieren
- Kategorien übertragen → Xentral darf Artikelkategorien in den Shop exportieren
- Crossselling übertragen → Xentral darf die [Crossselling-Verknüpfungen](https://xentral.com/helpdesk/kurzanleitung-crossselling) zwischen Artikeln in den Shop exportieren
- Staffelpreise übertragen → Xentral darf Staffelpreise der Artikel in den Shop exportieren
- Gutscheine übertragen ->
- Artikeltext Übertragung unterdrücken → Der Export von Artikeltexten von Xentral zum Shop wird für die ganze Schnittstelle deaktiviert
- Artikelliste abholen nur neue Artikel anlegen → Bei der Aktion 'Artikelliste abholen' werden nur fehlende Artikel neu angelegt, aber bereits im Adressstamm von Xentral vorhandenen Artikel werden nicht aktualisiert
- Artikelnummer beim Anlegen aus Shop übernehmen → Die Artikelnummer aus dem Shop wird auch als Artikelnummer in Xentral angelegt, wenn der Artikel aus dem Shop importiert wird

## Einstellungen zu den Rabatten

- Rabatt → Artikel aus Xentral, der Rabatte im Shopauftrag als eigene Position im Auftrag mit negativem Verkaufspreis abbildet
- Steuersatz für Rabatt-Artikel → MwSt.-Satz des verwendeten Rabatt-Artikels (normal oder ermäßigt)

## Einstellungen zu den Positionen im Auftrag

- Fehlende Artikel anlegen → Artikel, die im Shopauftrag enthalten sind, aber nicht im Adressstamm gefunden werden, werden automatisch im Adressstamm von Xentral angelegt
- Rabatte Porto festschreiben → Rabatte und Porto werden aus dem Shop übernommen und festgeschrieben
- Beschreibungstexte aus Shop → Texte aus dem Shop werden in den Artikelstamm von Xentral übernommen
- Artikelnummern aus Nummernkreis → Den Artikeln, die aus dem Shop kommen, werden Artikelnummern aus dem Nummernkreis von Xentral vergeben
- einzeln → Nur bei Artikeln mit der Option 'Online Shop Abgleich' im Artikelstamm findet die obige Einstellung Anwendung
- Artikelnummern aus dem Shop → Falls die Artikelnummern aus dem Shop sich von denen in Xentral unterscheiden (gefunden über die Fremdnummern), werden die Artikelnummern vom Shop übernommen
- Artikelbezeichnung aus Xentral → Es werden die Artikelbezeichnungen aus Xentral in die Auftragspositionen übernommen
- Artikelbeschreibungen aus Xentral → Es werden Artikelbeschreibungen aus Xentral in die Auftragspositionen übernommen
- Artikelbeschreibungen aus dem Shop → Falls der Shop die Artikelbeschreibungen überträgt, werden diese im Auftrag übernommen
- Stücklisten ergänzen → Bei 'Mix & Match'-Artikel (z.B. Bündelartikel bei Magento) werden die Stücklisten analog zum Shop ergänzt
- Spezielle Steuersätze pro Positionen → Die Steuersätze aus dem Shop werden auch bei Aufträgen mit gemischten Steuersätzen übernommen

## Einstellungen zum Adressen Import

- Bestehende Kunden nur aus Projekt verwenden → Haken setzen, wenn der Kunde pro Projekt mit einer neuen Adresse angelegt werden soll (die Kundenadresse existiert dann pro Projekt und z.B. pro Shop, also insgesamt mehrmals in Xentral, sofern der Kunde über mehrere Shops bestellt)
- Bestehende Adressen nicht überschreiben → die im Shop neu eingegebenen Daten überschreiben nicht die Kundenadresse in Xentral (keine Adressaktualisierung in den Stammdaten)
- Manuelle Adressübertragung → Fügt einen Button im Adressstamm aller Adressen von Xentral hinzu, um die Adressdaten von Xentral manuell zum Shop zu übertragen

## Kommunikations-Einstellungen

Wenn Sie Ihren Shop-Anbieter wechseln können Sie hier auch das Modul im Shopimporter umstellen oder aktualsieren. Dazu gehört z.B. auch ein Wechsel von einem externen Importer auf einen neuen internen Importer.

Alle allgemeinen Einstellungen sowie alle Verknüpfungen zu Artikeln, Kategorien, Fremdnummern, Versand- und Zahlungsmappings sowie Subshops bleiben dann bestehen, es wird aber eine neue API angesprochen.Wichtig: Alle shopspezifischen Einstellungen gehen hierdurch verloren! Die Zugangsdaten müssen neu eingetragen und gespeichert werden.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_6.png)

## Weiterführende Informationen zu den Einstelloptionen

## Multiprojekt Shop (Sonderfunktion)

Diese Option wird nur benötigt, wenn im Shop Artikel aus verschiedenen Projekten angeboten werden.Beispiel: In einem Shop werden einige Artikel angeboten die einen anderen Logistikprozess erfordern oder bei denen direkt nach der Bestellung eine spezielle Kundenprüfung (z.B. Handelsregisterauszug anfordern) notwendig ist.Diese Artikel können auf diese Weise gemeinsam gekauft werden. Nach dem Abholen der Aufträge nach Xentral werden jedoch verschiedene Prozesse angestoßen (z.B. andere E-Mail Vorlagen, Kundenprüfung ist erforderlich, anderen Logistikprozess, anderen Rechnungsversand, anderes Briefpapier etc.)

## Vorab als bezahlt markieren

Diese Funktion markiert Aufträge mit besonderen Bezahlarten (spezielle Bezahlarten über Zahlungsanbieter, Geldinstitute) als "vorab bezahlt". Die Ampel wird für diese Bezahlarten immer auf grün gestellt![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_8.png)

. Die Ampel mit dem Bezahlt-Icon schaltet also nicht auf orange![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_7.png)

(Aufträge ohne Zahlung (bei Vorab Bezahlarten) sind normalerweise immer orange, da eine manuelle Zahlungsfreigabe oder die Verknüpfung der Zahlung mit dem Auftrag über den Kontoauszug erforderlich ist).

## Artikelbilder übertragen

Manche Shop-Schnitstellen ermöglichen einen Export von Artikelbildern von Xentral zum Shop, wenn diese in Xentral im Artikelstamm unter Dateien mit dem Stichwort Standard Artikelbild (Shopbild) angelegt wurden. Nur Bilder mit diesem Stichwort wrden an den Shop exportiert.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_9.png)

Bilderreihenfolge für Export ändern

Im Artikelstamm können Sie anhand der Sortierung festlegen, in welcher Reihenfolge die Artikelbilder im Shop gezeigt werden sollen.

Bitte beachten Sie, dass nicht alle Shop-APIs die Reihenfolge beachten, obwohl von Xentral immer übergeben wird. Übernommen wird die Reihenfolge z.B. von Shopware. Das erste Bild in der Reihenfolge dient dort als Vorschau-Bild.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_10.png)

## Lagerzahlen Übertragung erlauben

Lagerzahlen automatisch an den Shop Rückmelden.Die Lagerzahl wird z.B. auch neu gemeldet, wenn ein Auftrag mit einem Artikel angelegt wird. Dieser Artikel wird dann vom Bestand, der gekauft werden kann, weggerechnet.

Wichtig:[Um die automatische Meldung zu aktivieren, muss ein Prozessstarter eingerichtet werden. Die Anleitung finden Sie hier.](https://xentral.com/helpdesk/prozessstarter#prozesstarterlagerzahlen-shop-synchronisation)Wichtig: Lagerzahlenabgleich Amazon: Hier müssten alle Fremdnummern in den Artikeln gepflegt werden. Da der Amazonimporter alles in einer Liste sammelt und alles auf einmal überträgt. Hier könnte es passieren wenn ein Artikel fehlt die ganze Liste nicht aktualisiert wird. Hinweis: Im Projekt kann auch eine "automatische Reservierung" der Artikel eingestellt werden. Die Artikel werden dann immer reserviert, sobald ein Auftrag freigegeben wurde (= eine fortlaufende Dokumentennummer erhalten hat = die Ampelanzeige aktiv ist (orange-grün).

Lager_Grundlage: Ab 18.4 gibt es die Möglichkeit einzustellen, wie sich der "Bestand" der an den Shop zurückgemeldet werden soll zusammensetzen soll:

- Anhand "Artikel verkaufbare", es wird der "berechnete Bestand" im Artikel an den Online - Shop zurückgemeldet- Anhand "Lagerbestand minus Reservierungen", es wird der Lagerbestand minus der reservierten Aufträge zurückgemeldet (offene nicht reservierte Aufträge werden nicht berücksichtigt)

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_11.png)

## Lagerkorrektur überschreiben

Wird diese Option aktiviert, so kann man den Lagerkorrekturwert global für alle Artikel in diesem Shop einstellen. Der Lagerkorrekturwert muss dann nicht mehr pro Artikel im Artikelstamm gepflegt werden. Der eingestellte Lagerkorrekturwert im Artikelstamm des Artikels wird von diesem Wert überschrieben.

## Auftragsstatus rückmelden

Diese Option meldet z.B. den Status Sendung "ausgeliefert" an den Shop zurück.Die Trackingnummer und andere Stati werden je nach Shop ebenfalls rückgemeldet.So ist im Shop-Backend ersichtlich, welche Aufträge aktuell sind und welche schon importiert oder abgearbeitet wurden.

## Manuelle Adressübertragung

Diese Funktion erlaubt das manuelle Übertragen von Adressdaten in den Shop.Die Manuelle Adressübertragung zeigt in Adresse (Stammdaten → Adressen →![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_12.png)

einen Button an (Voraussetzung: die Adresse hat das gleiche Projekt wie der Shop), der - wenn man ihn betätigt - die Adresse im Shop anlegt. Automatisch wird aber nichts übertragen. Die manuelle Übertragung zeigt auch das Passwort an, was die Kundennummer ist.

## Freitext aus Shopschnittstelle

Durch folgende Einstellung ist es Ihnen möglich den Freitext (Kommentarfeld im Shop) entweder in den Freitext oder in die interne Bemerkung des Auftrags zu übernehmen.Stellen Sie hierzu die Einstellung auf:

- in Feld Freitext laden
- oder: in Feld interne Bemerkung laden

![blobid0.png](https://help.xentral.com/hc/article_attachments/360025591719/blobid0.png)

Praxistipp: in der Logistik kann in den versandprozessen am Packtisch diese Info zusätzlich als rote Box angezeigt werden.[Diese Information muss am Packtisch bestätigt werden. Die Einstellungen sind in den Systemeinstellungen (zentrale Einstellungen zu finden).](https://xentral.com/helpdesk/kurzanleitung-logistikprozesse#weiterfuehrende-funktionen)

## Gesamtbetrag festsetzen und Maximale Differenz zur berechneten Summe

Diese Einstellung legt fest, dass beim Auftragsimport immer der Gesamtbetrag, den der Shop übermittelt hat, festgeschrieben und verwendet werden soll.Xentral rechnet den Gesamtbetrag dann nicht mehr neu aus den Preisen der einzelnen Positionen aus, sondern verwendet den Gesamtbetrag aus dem Shop.Das kann z.B. hilfreich sein, wenn der Shop mit weniger Nachkommastellen als Xentral rechnet und so durch die Mehrwertsteuer Rundungsfehler (meistens genau 1 Cent) entstehen. Ebenso werden in manchen Ländern Beträge auf 0,05 Währungseinheiten gerundet, sodass Xentral in diesem Fall eine Abweichung vom tatsächlichen Gesamtpreise erkennen würde.

Direkt darunter können Sie im Feld Maximale Differenz zur berechneten Summe festlegen, wie hoch die Differenz zwischen Auftrag im Shop und in Xentral maximal sein darf, damit Xentral die Gesamtsumme aus dem Shop übernimmt und nicht neu ausrechnet (und den Auftrag ggf. aufhält, wenn eine Differenz erkannt wurde).

## Artikel für Porto, Nachnahmegebühr und Rabatt

Um Versandkosten (Porto), Nachnahmegebühren und Rabatte in den Positionen Ihrer vom Shop importierten Aufträge darzustellen, können Sie jeweils einen Artikel im Artikelstamm von Xentral anlegen und in der Schnittstelle verknüpfen.

## Porto

Der hier hinterlegte Artikel wird verwendet, um Porto/Versandkosten im Auftrag als eigenen Position darzustellen.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_14.png)

Voraussetzung ist, dass der hinterlegte Artikel im Artikelstamm die Einstellung 'Artikel ist Porto' besitzt.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_15.png)

## Nachnahmegebühr

Ist die Option 'Nachnahmegebühr als extra Position' in der Schnittstelle aktiviert, wird die Nachnahmegebühr als eigene Position im Auftrag eingefügt, zusätzlich zum normalen Portoartikel. Die vollständigen Versandkosten des Kunden setzen sich also aus diesen zwei Positionen zusammen: Nachnahmegebühr + Porto.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_16.png)

## Rabatt

An folgender Stelle können Sie eine Rabattartikel einpflegen auf den die Rabatte Ihres Shops übertragen werden.

Im Eingabefeld darunter können Sie festlegen, wie der Rabatt (im buchhalterischen Sinn eine Gutschrift) besteuert werden soll. Sollten Sie den Steuersatz aus dem Artikelstamm übernehmen wollen, dann lassen Sie das Feld leer.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_17.png)

Voraussetzung hierfür ist, dass der Artikel im Artikelstamm mit der Einstellung 'Artikel ist Rabatt' versehen ist und das %-Feld leer gelassen wird:![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_18.png)

## Extra Verkaufspreise

Es gibt auch die Möglichkeit in den Shopeinstellungen eine Preisgruppe anzugeben, für die deren Verkaufspreis in den Shop übertragen werden soll.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_19.png)

Sobald der Verkaufspreis auf diese Gruppe angelegt wird, überträgt Xentral diese Verkaufspreis in den Shop und nicht z.B. den Standardverkaufspreise.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_20.png)

## Zugangsdaten für Xentral Import Plugin

- URL: Hier die URL zum Importer eingeben
- ImportKey: 32 Zeichen langes Sicherheitspasswort
- ImportToken: 6 Zeichen langes Sicherheitstoken

## Zeiträume

- Hier können Sie festlegen, wie viele Aufträge je Request und damit gleichzeitig abgeholt werden sollen
- Lassen Sie dieses Feld bspw. bei einem Shopware Shop leer, so werden alle Aufträge abgeholt, deren Auftragsstatus noch auf offen steht, wohingegen bei Amazon die Aufträge der letzten 90 Tage abgeholt werden
- Bei der Umstellung empfiehlt es sich jedoch (i. Abh. Ihrer offenen Aufträge) diese Zahl ggf. zu beschränken, um bei Anlaufschwierigkeiten den manuellen Aufwand für Korrekturen möglichst gering zu halten

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_21.png)

## Modus für die Einrichtungsphase oder Shopumstellungen

- Demo Modus (Modus für die Einrichtungsphase oder Shopumstellungen): Der letzte Auftrag aus dem Shop wird geladen - der Status (des Auftrags im Shop) aber nicht umgestellt, so kann dieser Auftrag immer wieder zu Demozwecken importiert werden.
- Einzel Sync (Modus für die Einrichtungsphase oder Shopumstellungen): Es wird beim Import immer nur EIN Auftrag importiert. Diesen Modus bei der Einrichtung und Testphase verwenden. Auf diese Weise wird sichergestellt, dass die Aufträge langsam und einzeln nacheinander importiert und gleichzeitig sofort kontrolliert werden können. Erst wenn die ersten 10-20 Aufträge (hängt generell von der Tagesmenge an Aufträgen ab) fehlerfrei importiert wurden kann der Haken herausgenommen und die nächste Ladung an Aufträgen zusammen importiert werden.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_22.png)

## Import der Artikel aus dem Shop nach Xentral (Einrichtungsphase/ Erstimport)

Liegen in Xentral zu einem Artikel folgende Felder vor, können die restlichen Daten nach WaWsion importiert werden:- Artikelnummer (ist dieselbe Artikelnummer wie im Shop)

- Artikelbeschreibung

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_23.png)

- Verknüpfung des Artikels auf den Onlineshop

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_24.png)

## Artikeleinstellungen für den Online-Shop

[Weitere Einstellungen für den Import und Export von Artikeln zwischen Shop und Xentral sind direkt im jeweiligen Artikel zu finden. Diese Einstellungsoptionen finden Sie hier.](https://xentral.com/helpdesk/kurzanleitung-artikel-anlegen#artikelonline-shop-optionen)

## Import von Aufträgen aus Online Shops

[Die Informationen zum Abholen der Aufträge aus dem Online-Shop über die Shopschnittstelle finden Sie hier.](https://xentral.com/helpdesk/kurzanleitung-import-von-bestellungen-aus-online-shops)

## Synchronisation der Lagerzahlen

## Vorraussetzungen für den Lagerzahlensync

1. In der Shop-Schnittstelle → Einstellungen muss die Option "Lagerzahlen Übertragung erlauben" aktiviert sein
1. Im Artikel → Online-Shop Optionen muss die Option "Lagerzahlen Sync." aktiviert sein & der Artikel mit dem Shop verknüpft sein

Manuell übertragen: Wenn man die Lagerzahl eines einzelnen Artikels übertragen will, geht man unter Artikel → Online-Shop Optionen und drückt den Button "Export"

Automatisch übertragen: Wenn es automnatisch gehen soll, muss der Prozessstarter "lagerzahlen"aktiviert sein (ideal 5 oder 10 Minuten). Dann wird zyklisch der Wert im Shop angepasst bei Lagerdifferenzen zwischen Xentral und dem Shop.

Information zum Prozessstarter:[https://www.wawision.de/helpdesk/prozessstarter#nav-prozessstarter--lagerzahlen-shop-synchronisation](https://www.wawision.de/helpdesk/prozessstarter#nav-prozessstarter--lagerzahlen-shop-synchronisation)Zeitpunkt des Lagerzahlensyncs:[https://www.wawision.de/akademie-faq/prozessstarter-hd-wie-wird-die-systemmeldung-fur-den-abgleich-der-lagerzahlen-mit-dem-shop-ausgelost-und-was-ist-das-systemmeldung-auto-update-lagerlampen](https://www.wawision.de/akademie-faq/prozessstarter-hd-wie-wird-die-systemmeldung-fur-den-abgleich-der-lagerzahlen-mit-dem-shop-ausgelost-und-was-ist-das-systemmeldung-auto-update-lagerlampen)Hinweis zum Lagersync:

- Die Bestandsänderung muss auf Xentral Seite passieren
- Xentral merkt sich, was das letzte mal an den Shop gemeldet wurde
- Wenn sich hieraus eine Änderung im Lagerbestand ergeben hat, werden genau diese Artikel übertragen
- Eine alleinige Änderung im Shop löst noch keine Bestandsänderung in Xentral aus, eine Bestandsänderung in Xentral löst aber eine Rückmeldung zum Shop aus (sofern keine Pseudo-Lagerzahlen als Bestand verwendet werden)

Durch Betätigung des folgenden Buttons können Sie die zuletzt gespeicherten Bestanddswerte löschen. Im Anschluss holt der Cronjob "lagerzahlen" erneut alle neuen Bestände ab und meldet diese an den Shop zurück.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_25.png)

## Artikel zum Shop exportieren/aktualisieren

Die Artikel Übertragung exportiert Artikel mitsamt den gepfleten Daten an den Shop, wie z.B. Texte, Standardpreis, Gewichte, Abverkauf usw.

Für den automatischen Export von Artikeln zu einem Online-Shop gibt es den Prozessstarter[Artikel Übertragen](https://xentral.com/helpdesk/prozessstarter#nav-prozessstarter--artikel-zum-shop-exportieren). Dieser überträgt alle zum Shop verknüpften Artikel nach und nach im Hintergrund, wenn der Export in der Schnittstellen über den Bereich 'Artikel Übertragung' angestoßen wurde.Wurde ein Artikel verändert, können im Artikelstamm unter Details → Online Shop Optionen auch direkt per Knopfdruck in den Shop exportiert werden.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_26.png)

Hinweis: Sollen nur die Lagerzahlen der Artikel übertragen werden, da alle anderen Artikeldaten im Shop gepflegt werden, sollte die Option 'Artikel Übertragung erlauben' nicht gesetzt werden, sondern nur die Option 'Lagerzahlen Übertragen erlauben'.

## Zahlungsweisen Mapping

Im Tab Zahlweisen können Sie die aus dem Shop übergebenen Parameter für die unterschiedlichen Zahlungsweisen auf die in Xentral angelegten Zahlungsweisen mappen. Dafür muss unter Einstellungen die Option Zahlungweisen-Mapping verwenden aktiviert sein.

Damit unbekannte Zahlungsweisen aus Online-Shops auf bekannte Zahlungsweisen in Xentral verknüpft werden können, werden die vom Shop übergebenen Parameter automatisch als leerer Eintrag in der Mapping-Tabelle angelegt.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_27.png)

## Einstellungen

Pro Zahlungsweise können Einstellungen vorgenommen werden, wie Aufträge mit dieser Zahlungsweise zu behandeln sind.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_28.png)

- Zahlweise Shop → Bezeichnung der Zahlungsweise im Shop

- Zahlweise Xentral → Zahlungsweise in Xentral
- Vorab als bezahlt markieren → Aufträge mit dieser Zahlungsweise vorab als bezahlt markieren
- Autoversand aktiv → Aufträge mit dieser Zahlungsweise werden für den Autoversand freigegeben
- Keine Rechnung erstellen → Es wird keine Rechnung für Aufträge mit dieser Rechnung erstellt
- Fast-Lane → Aufträge mit dieser Zahlungsweise automatisch in die Fast-Lane übergeben
- Aktiv → Zahlungsweise ist aktiv

## Versandarten Mapping

Im Tab Versandarten können Sie die aus dem Shop übergebenen Parameter für die unterschiedlichen Versandarten auf die in Xentral angelegten[Versandarten](https://xentral.com/helpdesk/kurzanleitung-versandarten)mappen. Dafür muss unter Einstellungen die Option Versandarten-Mapping verwenden aktiviert sein.

Damit unbekannte Versandarten aus Online-Shops auf bekannte Versandarten in Xentral verknüpft werden können, werden die vom Shop übergebenen Parameter automatisch als leerer Eintrag in der Mapping-Tabelle angelegt.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_29.png)

## Einstellungen

Pro Versandart können Einstellungen vorgenommen werden, wie Aufträge mit dieser Versandart zu behandeln sind.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_30.png)

- Versandart Shop → Bezeichnung der Versandart im Shop

- Versandart Xentral → Versandart in Xentral
- Land (mit Komma getrennt, zweistellig ISO) → Einschränkung, für welches Land Versandart verfügbar ist (leer = keine Einschränkung)
- Fast-Lane → Aufträge mit dieser Versandart automatisch in die Fast-Lane übergeben
- Autoversand aktiv → Aufträge mit dieser Versandart werden für den Autoversand freigegeben
- Aktiv → Versandart ist aktiv

Die textuelle Beschriftung der Versandart für die Software-Oberfläche und die Beschriftung auf den Dokumenten (abgedruckter Text auf Rechnung, Auftrag, etc.) erfolgt über das Mapping in den Versandarten (Administration → Einstellungen → Versandarten).

Dort wird der Typ (= Feldbezeichnung in Xentral, z.B. "selbstabholer") auf die textuelle Beschreibung wie z.B. "Selbstabholer" oder "Hofverkauf" verknüpft.Nähere Informationen zur Einstellung der Versandarten finden Sie[hier](https://xentral.com/helpdesk/kurzanleitung-versandarten?).

## Freifelder Mapping

Im Tab Freifelder können Sie für einige Shopschnittstellen (z.B. Shopware) können Sie Freifelder in Xentral mit Freifeldern im Shop mappen, um sie für beim Export zu übertragen bzw. zu aktualisieren.

## Freifeldname aus dem Shop herausfinden

Im Beispiel Shopware findet man die Freitextverwaltung unter Einstellungen im Hauptmenü:

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_31.png)

Dabei ist der Spaltenname wichtig für Xentral (attr1, attr2, etc.)

## Freifelder eintragen

In der Shopschnittstelle unter Freifelder-Mapping können Sie dann die Freifelder zuweisen:

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_32.png)

## Subshop

Falls ein Shop mit Subshops angebunden wurde, können Sie im Tab Subshop können Sie die verschieden Subshops ihres Online-Shops mappen. Subshops werden z.B. für die Trennung nach Sprache oder Domain (z.B. meinshop.de und meinshop.com) verwendet.

So könnte ein Mapping beispielsweise aussehen:![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_33.png)

## Gruppen Mapping

In Onlineshops, die Kundengruppen übergeben, kann ein Gruppenmapping eingestellt werden. Um festzustellen, ob der Shopimporter die Information der Kundengruppe übermittelt, kann man im Warenkorb eines importierten Auftrags nachsehen.

![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_34.png)

Die Gruppen im Shop können auch Gruppen in Xentral gemappt werden. Die Mechanik funktioniert dabei anhand von Rollen. Die Rollen können wiefolgt verwendet werden:

Import (Shop zu Xentral)Export (Xentral zu Shop)

KundeBeim Bestellimport werden Adressen, wenn sie in der entsprechenden Shopgruppe sind, als Kunden bei der Xentral gruppe hinzugefügt. Die Option Neukunden zuweisen fügt alle über den Shop neu angelegten Adressen als Kunden bei der Xentral gruppe hinzu.—

MitgliedBeim Bestellimport werden Adressen, wenn sie in der entsprechenden Shopgruppe sind, als Mitglieder bei der Xentral gruppe hinzugefügt. Die Option Neukunden zuweisen fügt alle über den Shop neu angelegten Adressen als Mitglieder bei der Xentral gruppe hinzu.—

Artikel—Legt fest, welche Artikelpreise in den Shop übertragen werden sollen und in welcher Preisgruppe sie im Shop landen.

So könnte das Mapping beispielhaft aussehen:![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_35.png)

In diesem Fall wird jeder Kunde, der neu angelegt wird, automatisch als 'Kunde der Gruppe Neue Kunden' angelegt. Sofern der Kunde im Shop Mitglied der Gruppe KR33 ist, wird der Kunde zudem als 'Mitglied der Gruppe Gute Kunden' aufgenommen.Das dritte Mapping sorgt bei einem Artikelexport dafür, dass Staffelpreise der 'Preisgruppe für Großhändler' als Preise für die Shopgruppe 'H' übertragen werden. Dadurch lässt sich steuern, welche Preisgruppen in den Shop übertragen werden und wo sie landen sollen.

## Shopfunktionen: Featurematrix für Shopschnittstellen

Administration → Online Shops / Marktplätze → Shopfunktionen

Die Übersicht Shopfunktionen gibt eine Übersicht aller Shopschnittstellen von Xentral. Dort kann man nachsehen, welche Features ein bestimmter Shopimporter unterstützt.Beispiel: In der sechsten Spalte der ersten Zeile können Sie anhand der Symbole erkennen, dass der Shopware-Importer von Xentral sowohl einen Import (Shopware → Xentral) als auch einen Export (Xentral → Shopware) der Artikelbezeichnungen ermöglicht.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_36.png)

Unten werden in der Legende die Symbole erklärt.![](https://xentral-wiki-assets.s3.eu-central-1.amazonaws.com/images2/wiki_37.png)

- Import und Export verfügbar → Export des Feldes von Xentral zum Shop sowie Import von Shop zu Xentral möglich

- Ein-/Ausschaltbar → Es kann in der Shopschnittstelle eingestellt werden, ob dieses Feld übertragen werden soll
- Nicht verfügbar → Feature ist für diesen Importer nicht verfügbar
- Im Shop nicht verfügbar → Übertragung wird von diesem Shop/Marktplatz nicht unterstützt
- Export aus Xentral verfügbar → Feld kann von Xentral zum Shop übertragen werden
- Import in Xentral verfügbar → Feld kann vom Shop zu Xentral importiert werden
- Unbekannt → Aktuell ist unbekannt, ob dieses Feature unterstützt wird