Diese Schnittstelle erlaubt es dir, über eine API Aufträge von Kaufland nach Xentral zu importieren, und bietet die folgenden Funktionalitäten:

- Aufträge von Kaufland importieren
- Automatische Änderung des Auftragsstatus bei Versand mit Sendungsverfolgung
- Übertragung einzelner Artikel von Xentral nach Kaufland und umgekehrt
- Meldung aktueller Lagerzahlen
- Übertragung von Rechnungen zu Kaufland

## Kaufland mit Xentral verbinden

Um die Schnittstelle anzubinden, benötigst du sowohl Zugang zu Kaufland als auch zu Xentral.

### API-Zugangsdaten bei Kaufland erzeugen

Führe die folgenden Schritte aus, um deine API-Zugangsdaten bei Kaufland zu erzeugen:

1. Logge dich im Händlerbereich von Kaufland ein (www.kaufland.de/seller).
1. Klicke im Hauptmenü aufHändlereinstellungen > Shopeinstellungen und öffne den Reiter API.
1. WähleXentral als Schnittstelle aus und speichere.
1. Klicke aufZugangsdaten neu generieren.
1. Kopiere Client Key und Secret Key. Du benötigst diese, um die Schnittstelle in Xentral einzurichten.

### Kaufland-Schnittstelle in Xentral anlegen

Gehe wie folgt vor, um die Kaufland-Schnittstelle in Xentral anzulegen:

1. In Xentral, navigiere zu:
  - Im Classic Design: Administration > Shop Schnittstelle und klicke auf NEU.
  - In Xentral NextGen: Einstellungen > Verkaufen > Shops/ Marktplätze und klicke auf Verbindung hinzufügen.
1. Wähle Kaufland. Ein Dialog erscheint.
1. Trage deinen Client Key und Secret Key in die entsprechenden Felder ein und klicke auf Weiter.

Du landest direkt im ReiterDetails > Schnittstelle. Hier kannst du die API-Daten eintragen.

## Kaufland-Schnittstelle konfigurieren

Du kannst die grundlegenden Einstellungen der Schnittstelle unterReiter Details > Unterreiter Schnittstellekonfigurieren.

1. Gib eine aussagekräftige Bezeichnung ein, z.B. den Namen deines Shops und das dazugehörige Projekt.
1. Setze ein Häkchen bei Aktiv, um die Schnittstelle zu aktivieren. Du kannst das Häkchen auch wieder entfernen, um die Schnittstelle zu deaktivieren.
1. Wähle ein Projekt. Mit einem spezifischen [Projekt](https://help.xentral.com/hc/de/articles/360016723620#UUID-47d62f4f-3eac-f7b6-5144-f2353584abd5) für deinen Shop kannst du Logistik, Belege, Zahlweisen und andere Funktionalitäten bestmöglich an deinen Shop anpassen. Kaufland hat einige spezielle Anforderungen, die du mit einem Projekt lösen kannst - beispielsweise was den Upload von Rechnungen betrifft. Am Ende des Artikels findest du eine genauere Beschreibung, auf [welche Besonderheiten du in deinem Projekt achten solltest](#UUID-d6f615a0-852c-e3e0-0d41-ecf86e546fb1_id_360016721780_id_h_01FF7VYNGVRGJS9WWMHQEXE2J1).
1. Wähle den Abholmodus. In der Kaufland-Schnittstelle ist ab Datum die einzige Option.
1. Das Feld Datum von wird automatisch ausgefüllt, wenn du die Schnittstelle einrichtest und wird jedes Mal aktualisiert, wenn du auf Aufträge abholen klickst oder Aufträge vom Prozessstarter importiert werden.

Im BereichEinstellungen für Shop oder Marktplatzkannst du einige optionale Einstellungen vornehmen:

- Wähle Protokollierung im Logfile, wenn du Anfragen der Schnittstelle protokollieren möchtest. Dies kann bei der Fehlerbehebung hilfreich sein. Die Logs findest du am unteren Ende dieser Einstellungsseite.
- Wähle Produktdaten immer übertragen, falls du deine Artikeldaten und Beschreibungen häufig wechselst. Standardmäßig werden Artikeldaten nur einmal übertragen. Mit dieser Option werden sie jedoch jedes Mal übertragen, sobald du einen Artikel exportierst.
- Wähle Artikel ohne Lagerbestand automatisch bei Aktualisierung aus dem Shop entfernen, falls du nicht planst, den Lagerbestand deiner Artikel zu erneuern.

## Aufträge importieren

Du kannst aus drei Optionen für denImport-Modusauswählen:

1. Demo (zum Testen) - Nutze diese Option zu Testzwecken. Bei dieser Option wird der Auftragsstatus im Shop nicht aktualisiert. Artikel und Lagerzahlen werden nicht übertragen.
1. Manuell (mit Importzentrale) - Xentral importiert nur Aufträge, wenn du auf Aufträge abholen im Aktions-Menü auf der rechten Seite klickst.
  Wählst du Aufträge in Zwischentabelle, werden die Aufträge in einer Zwischentabelle gespeichert, in der du sie auf Fehler überprüfen kannst, bevor du sie in dein System übernimmst.

  Du kannst die Schnittstelle testen, indem du auf Nur 1 Auftrag pro Anfrage klickst und anschließend prüfst, ob der Importprozess für einen Auftrag funktioniert.

1. Automatisch (per Prozessstarter) - Xentral importiert Aufträge in regelmäßigen Abständen. Dieser Prozess wird vom [Prozessstarter](https://help.xentral.com/hc/de/articles/360016760599#UUID-fe00da18-8f96-5958-328c-f04d36cd905a) shopimport gesteuert.
  Wählst du in diesem Import-Modus Aufträge in Zwischentabelle aus, so wird die Zwischentabelle als Fallback genutzt, d.h. sollte beim Importprozess ein Fehler auftreten, dann kannst du die Zwischentabelle auf Fehler und fehlende Aufträge prüfen.

Du kannst außerdem aufShopimport ZwischentabelleimAktions-Menü auf der rechten Seite klicken, um eine Zwischentabelle deiner letzten Aufträge zu importieren.

## Einstellungen in zusätzlichen Reitern konfigurieren

Es gibt mehrere zusätzliche Reiter, in denen du weitere Einstellungen konfigurieren kannst. Da die Schnittstellen aller Onlineshops auf dem selben Grundgerüst basieren, sind nicht alle Reiter für jeden Shop relevant.

Weitere Informationen zu den folgenden Reitern findest du im[Online-Shops](https://help.xentral.com/document/preview/42450#UUID-9f183a72-7906-0ad5-3f24-f4eeabc42c07)Artikel:

- Einstellungen (Artikelimport, Lagerzahlensynchronisation)
- Zahlweisen
- Versandarten
- Sprache-/Lieferland

Klicke[hier](https://help.xentral.com/document/preview/13979#UUID-e55a4c1d-d861-ef5d-741d-94856c3b5b50), um mehr über die Nutzung von Smarty in der Onlineshop-Schnittstelle zu erfahren.

> **Anmerkung**
>
> Die folgenden Reiter sind für die Kaufland-Schnittstelle nicht relevant:
>
> - Freifelder
> - Subshop
> - Gruppenmapping

## Artikelmapping: Artikel in Kaufland und Xentral verknüpfen

Du musst deine Artikel aus Kaufland mit denen in Xentral verknüpfen. Auf diese Weise wird eine Synchronisierung der Artikel zwischen Kaufland und Xentral ermöglicht. Zusätzlich können so Aufträge aus Kaufland den verknüpften Artikeln in Xentral zugewiesen werden.

Gehe wie folgt vor, um Artikel aus Kaufland mit denen in Xentral zu verknüpfen:

1. Navigiere in der Kaufland-Shopschnittstelle in Xentral zuDetails > Artikelmapping.
1. Klicke aufArtikelliste abholen.
  Die Artikel aus Kaufland werden abgerufen und hier aufgelistet. Die SpalteZuordenbarzeigt an, welche Artikel auf Basis identischer EANs automatisch mit ihrem Gegenstück in Xentral verknüpft werden können.

  Xentral legt dabei automatisch über die Daten, die über die Shopschnittstelle importiert wurden, zwei Einträge für Fremdnummern des Artikels in Xentral an.

  - apiitemid - Die alte Bezeichnung, die von der veralteten API verwendet wurde. Diese wird automatisch angelegt, da sie durch die Kaufland-Shopschnittstelle übertragen wird. Diese Nummer kannst du ignorieren.
  - apiunitid - Die gültige Bezeichnung für die Kaufland-Fremdnummer.
1. Klicke aufArtikel zuordnen.
  Die Artikel, die alsZuordenbarerkannt wurden, werden nun verknüpft. Das bedeutet Folgendes:

  - Die SpalteZuordenbarzeigt an, dass sie verknüpft wurden.
  - Im ReiterFremdnummerndes entsprechenden Artikels werden die beiden Kaufland-Fremdnummern (apiitemidundapiunitid) aufAktivgesetzt.

> **Anmerkung**
>
> Wenn du aufArtikelliste abholenklickst, werden bereits bestehende Artikelverknüpfungen gelöst. Du musst alle Artikel mit einem erneuten Klick aufArtikel zuordnenneu verknüpfen.

Bei Bedarf kannst du die aktive Verknüpfung eines Artikels manuell lösen oder die Verknüpfung auf einen anderen Artikel in Xentralübertragen.

Um eine Artikelverknüpfung manuell zu lösen und eine neue Verknüpfung zu ermöglichen, gehst du wie folgt vor:

1. Navigiere in der Kaufland-Shopschnittstelle in Xentral zuDetails > Artikelmapping.
1. Klicke in der Liste der Kaufland-Artikel auf rechts neben dem Artikel, dessen Verknüpfung du lösen möchtest.
  Die Verknüpfung wird gelöst. Das bedeutet Folgendes:

  - Die SpalteZuordenbarzeigt an, dass keine Verknüpfung vorhanden ist.
  - Im ReiterFremdnummerndes entsprechenden Artikels werden die Häkchen im FeldAktivfür die beiden Kaufland-Fremdnummern (apiitemidundapiunitid) entfernt.
  Die beiden Fremdnummern werden nicht gelöscht, sondern nur deaktiviert. So kannst du sie jederzeit durch eine neue Verknüpfung im ReiterArtikelmappingreaktivieren - siehe nachfolgende Beschreibung.

Gehe wie folgt vor, um die Verknüpfung eines Kaufland-Artikels auf einen anderen Artikel in Xentral zu übertragen:

1. Navigiere in der Kaufland-Shopschnittstelle in Xentral zuDetails > Artikelmapping.
1. Klicke in der Liste der Kaufland-Artikel auf rechts neben dem Artikel, dessen Verknüpfung du ändern möchtest.
1. Der DialogArtikel bearbeitenwird angezeigt. Gib den gewünschten Artikel aus Xentral ein. Alternativ kannst du im Eingabefeld auf klicken, um nach dem gewünschten Artikel zu suchen.
1. Klicke aufSpeichern.
  Die Verknüpfung wird erstellt: Im ReiterFremdnummerndes entsprechenden Artikels werden die beiden Kaufland-Fremdnummern (apiitemidundapiunitid) aufAktivgesetzt.

## Artikel exportieren

Um einen Artikel bei Kaufland zu listen, ist es notwendig, einige besondere Einstellungen vorzunehmen. Allgemeinere Informationen zum Export von Artikeln zu einem Onlineshop findest du in[diesem Artikel](https://help.xentral.com/document/preview/42450#UUID-9f183a72-7906-0ad5-3f24-f4eeabc42c07).

Gehe wie folgt vor, um einen Artikel zu Kaufland zu exportieren:

1. Navigiere zu
  - Im Classic Design: Stammdaten > Artikel > Wähle den Artikel > Reiter Details > Unterreiter Online-Shop Optionen.
  - In Xentral NextGen: Verkaufen > Artikel > Wähle den Artikel > Reiter Details > Unterreiter Online-Shop Optionen.
1. Klicke im Abschnitt Online-Shops auf Neuer Eintrag. Es öffnet sich ein neues Fenster.
1. Wähle deine Kaufland-Schnittstelle im Online-Shop Dropdown-Menü und klicke auf Speichern.
1. Klicke auf in derselben Zeile wie Kaufland. Ein neues Fenster mit Kaufland-spezifischen Einstellungen öffnet sich.
1. Klicke auf Suchen im Feld Kategorie und wähle eine Kategorie für deinen Artikel. Kaufland schlägt dir Kategorien auf Grundlage der Artikelbeschreibung vor. Sollte der Vorschlag nicht zutreffen, kannst du eine Kategorie über die Manuelle Kategoriesuche auswählen.
1. Gib deine Artikeldaten in die Kategorie-spezifischen Felder ein. Einige der Felder sind verpflichtend und notwendig, um deinen Artikel bei Kaufland anzubieten. Sollte Xentral eine passende Information erkennen, wird das entsprechende Feld mit den Artikeldaten aus Xentral befüllt, z.B. mit dem Hersteller.
1. Wähle eine Versandgruppe. Bevor du eine Versandgruppe auswählen kannst, musst du sie im Kaufland Seller Portal anlegen.
1. Wähle einen Zustand. Ist der Zustand nicht Neu, solltest du im nächsten Feld eine Zustandsbeschreibung eintragen.
1. Gib eine Minimale Lieferzeit und Maximale Lieferzeit in Tagen ein.
1. Klicke auf Speichern.

> **Anmerkung**
>
> Ist ein Artikel nicht verfügbar, obwohl alle Felder befüllt wurden, liegt der Fehler womöglich bei Kaufland. Bearbeitest du einen Artikel direkt bei Kaufland, werden Pflichtfelder in roter Schrift angezeigt.

## Artikelinformationen aktualisieren

Beachte darüber hinaus, dass Kaufland Artikelbeschreibungen nicht direkt übernimmt, sondern erst auf Inhalt prüft. Die Artikelbeschreibung aus Xentral wird also nicht direkt auf dem Marktplatz angezeigt, sondern hilft nur, die bereits bestehende zu verbessern. Sollte ein Artikel nicht verfügbar sein, obwohl alle Felder eingegeben worden sind, bietet es sich an, direkt auf Kaufland nach der Ursache des Problems zu suchen. Wenn der Artikel direkt editiert wird, werden zwingend erforderliche Felder mit fetter roter Schrift angezeigt.

- Kaufland nutzt die aus Xentral übertragene Artikelbeschreibung nicht direkt, sondern prüft die Beschreibung und integriert passende Inhalte in die bestehende Beschreibung.
- Bilder müssen auf einen FTP-Server oder ähnliches hochgeladen werden. Die URL deines Artikels kannst du dann unter Artikel > Wähle den Artikel > Reiter Details > Unterreiter Online-Shop Optionen > Klicke auf für Kaufland im Feld Bild eintragen.

## Kaufland-Projekt einrichten

Es gibt einige Besonderheiten bezüglich des Uploads von Rechnungen und dem Versand von E-Mails, die du beim Einrichten eines Kaufland-Projektes beachten solltest. Die Gründe dafür sind folgende:

- Rechnungen müssen, sobald sie abgeschlossen sind, zu Kaufland übertragen werden. Dies bedeutet, dass die Rechnung vor dem Versandprozess erzeugt werden muss.
- Kaufland verbietet Drittanbietern, wie Xentral, E-Mails in ihrem Namen zu versenden.

Richte dein Projekt folgendermaßen ein:

1. Navigiere zu
  - Im Classic Design: Stammdaten > Projekt > Öffne dein Kaufland-Projekt > Reiter Einstellungen > Unterreiter Logistik/ Versand.
  - In Xentral NextGen: Einstellungen > Lager > Logistik Einstellungen pro Vertriebskanal > für deine Kaufland-Schnittstelle.
1. Stelle im Bereich Stufe 1 (Pick/ Kommissionierung) sicher, dass kein Häkchen bei Rechnung erst im Versandprozess erzeugen gesetzt ist.
1. Stelle sicher, dass keine Häkchen bei E-Mail gesetzt sind. Dies gilt für Stufe 1 (Pick/ Kommissionierung) und Stufe 2 (Pack) an Versandstation.