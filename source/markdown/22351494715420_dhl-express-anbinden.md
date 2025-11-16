Neben dem klassischen DHL Paket-Service (Versandart **DHL** in Xentral) bietet DHL Express einen eigenen Premiumdienst an, der auf besonders schnelle, zuverlässige und zeitgenaue Zustellungen ausgelegt ist.

DHL Express ist die passende Wahl für dich, wenn du zeitkritische Lieferungen durchführst oder hochwertige Produkte verschickst. Typische Anwendungsfälle sind internationale B2B-Sendungen, ein globaler Kundenstamm oder Hersteller, die Ersatzteile und Produkte in kürzester Zeit zustellen müssen. Mit DHL Express bildest du diese und weitere Business Cases sicher und zuverlässig ab. Zusätzlich kannst du die Versandart **DHL Express** wie folgt in deinen Versandprozess integrieren:

- Manuelle Erstellung von Versandlabels zu einzelnen Lieferscheinen
- Automatische Erstellung von Versandlabels innerhalb verschiedener Logistikprozesse
- Zuverlässiger nationaler und Internationaler Expressversand für verschiedenste Sendungsgrößen und optionale Zusatz-Services
- Transparente Rückmeldung von Tracking-Nummern an deine Online-Shops und sonstige Verkaufsplattformen

> **Tipp**
>
> DHL Express ist ein separater Dienstleister, der nicht in Verbindung mit deinem eventuell bestehenden DHL-Geschäftskundenvertrag steht. Für DHL Express benötigst du einen eigenen Vertrag und erhältst separate Zugangsdaten.
>
> Hier sind die wichtigsten Unterschiede auf einen Blick:
>
> - **Vertrag und Zugangsdaten**: Für DHL Express schließt du einen separaten Vertrag ab und erhältst eine spezifische Kundennummer, die nur für DHL Express gilt
> - **Zustellung**: DHL Express nutzt ein separates Kurier- und Luftfrachtnetzwerk, zusätzlich werden DHL Express-Sendungen in Sortierzentren bevorzugt behandelt
> - **Adressierung**: DHL Express-Sendungen können nicht an Packstationen oder Postfilialen adressiert werden, sondern nur an physische Empfängeradressen
> - **API und Portale**: Bei DHL Express nutzt du nicht das DHL-Geschäftskundenportal, sondern erhältst einen Login im PortalmyDHL+und greifst bei Bedarf auf dieMyDHL APIzu

## Features

Die Versandart **DHL Express** bietet dir die folgenden Features:

- Nationaler und internationaler Expressversand
- Anwendung verschiedener DHL Express-Servicetypen
- Nutzung zusätzlicher lokaler Servicetypen für besondere Anwendungsfälle (Versand von Gefahrgut, besonders schwere Sendungen, Samstagszustellung oder Empfängerunterschrift)
- Festlegung der Incoterms (DDP und DAP) in den Einstellungen der Versandart
- Rückmeldung der Trackingnummer an deine Online-Shops und Verkaufsplattformen
- Speichern der Trackingnummer in Xentral
- Direkter Ausdruck des Versandlabels in Xentral

## Wichtige Hinweise zur Verwendung der Versandart

Beachte die folgenden Hinweise und Einschränkungen, bevor du die Versandart **DHL Express** in Xentral einrichtest und verwendest:

> **Wichtig**
>
> - **Verfügbarer Inhaltstyp **: In den Einstellungen der Versandart muss für die Einstellung ** Inhaltstyp **die Option ** DOCUMENTS**gewählt werden. Andere Inhaltstypen werden in der Schnittstelle nicht unterstützt!
> - **Internationaler Versand außerhalb der EU **: Für den Versand in Länder außerhalb der EU (z.B. Großbritannien) mit dem Service P muss zwingend der Inhaltstyp ** NON_DOCUMENTS**ausgewählt werden.

## DHL Express an Xentral anbinden

Die Anbindung an DHL Express funktioniert über die MyDHL API und findet somit über eine separate Schnittstelle statt.

> **Anmerkung**
>
> **Zur Erinnerung **: Für die Einrichtung der Versandart ** DHL Express**kannst du deine regulären DHL-Zugangsdaten nicht nutzen.
>
> Falls du noch kein Geschäftskunde bei DHL Express bist, findest duhier bei DHLalle notwendigen Informationen und das Kontaktformular. Im Anschluss meldet sich DHL bei dir, sodass der Vertrag finalisiert und dir am Ende die benötigten Zugangsdaten zur Verfügung gestellt werden können.

Falls du bereits einen Account bei DHL Express hast, erhältst du den benötigten **DHL Express Key **, das ** DHL Express Passwort **und die ** DHL Account Number**direkt bei deinem DHL Express-Kundenbetreuer.

### Grundeinstellungen vornehmen

Im ersten Schritt der Anbindung legst du die Versandart **DHL Express** in Xentral an und gibst die Zugangsdaten für DHL Express ein, ein, die du von deinem Kundenbetreuer erhalten hast.

1. Nutze die Smart Search, um das Modul **Versandarten** zu öffnen.
1. Klicke oben rechts auf **+ NEU**.
1. Klicke auf **DHL Express**.
1. Gib deine Zugangsdaten wie in der folgenden Tabelle beschrieben ein.
1. Klicke auf **Weiter**.
1. Nimm folgende Einstellungen vor:
  - **Projekt-Filter** (optional): Gib ein Projekt an, wenn du pro Verkaufskanal einen anderen Drucker für das Versandlabel verwenden möchtest.
  - **Drucker**: Wähle den gewünschten Drucker für das Versandlabel aus.
  - **Export Drucker**: Diese Einstellung ist nur relevant, wenn die Versandart für den internationalen Versand mit DHL Express konfiguriert wird.
  Wähle in diesem Fall aus dem Dropdown-Menü den Drucker aus, der standardmäßig für Zollpapiere (CN23) genutzt werden soll.

1. Klicke auf **Weiter**.

### Zusätzliche Einstellungen vornehmen

Nachdem du wie oben beschrieben deine Zugangsdaten für DHL Express eingegeben und die Versandart in Xentral angelegt hast, nimmst du jetzt weitere Einstellungen für die Versandart vor. Unter anderem gibst du hier auch die gewünschten[Servicetypen für DHL Express](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235139971445952)ein.

> **Tipp**
>
> Die Pflichtangaben und damit auch die Einstellungen, die für die Versandart **DHL Express** in Xentral vornimmst, weichen je nach Service-Typ ab.
>
> Konkret bedeutet das: DHL Express benötigt unterschiedliche Informationen, je nachdem, ob du zollfrei oder zollpflichtig versendest. Welche Angaben in welchem dieser Fälle zwingend benötigt werden, haben wir im KapitelPflichtangaben für DHL Express-Sendungenfür dich transparent aufgelistet.

1. Nutze die Smart Search, um das Modul **Versandarten** zu öffnen.
1. Klicke bei der soeben angelegten Versandart **DHL Express ** rechts auf das **Stift-Symbol**.
1. Aktiviere im Bereich **Experte ** die Einstellung **Zusätzliche Einstellungen anzeigen**.
1. Nimm die Einstellungen wie in der folgenden Tabelle beschrieben vor.
1. Klicke auf **Speichern**.

| Einstellung | Erläuterung |
| --- | --- |
| **Bezeichnung** | Gib eine Bezeichnung für die Versandart ein, die später bei der Auftragsbearbeitung in Xentral angezeigt wird. Die Bezeichnung ist nur für dich und deine Mitarbeiter sichtbar. Achte darauf, dass jede Bezeichnung nur einmal in Xentral vorkommt, damit die Versandart stets eindeutig identifiziert werden kann. |
| **Typ **| Dies ist eine interne Feldbezeichnung, die für die Zuordnung bei deinen Online-Shops und anderen Verkaufsplattformen benötigt wird. ⚠️** Wichtig:** Verändere diese Bezeichnung nicht! |
| **Modul** | Wähle das passende Modul aus dem Dropdown-Menü. Dabei muss der Modulname identisch zum Namen der Versandart sein, die du gerade einrichtest. |
| **Projekt **|** Optional**: Gib eine Projektzuordnung an. Diese wird benötigt, wenn du die Versandart auf einen bestimmten Verkaufskanal oder ein Projekt (beispielsweise eine spezifische Niederlassung) beschränken möchtest. Lasse das Feld leer, falls die Versandart in allen Projekten genutzt werden soll. |
| **Aktiv **| Aktiviere diese Option, sobald du alle benötigten Einstellungen für die Versandart vorgenommen hast. 💡** Tipp:** Nicht mehr verwendete Versandarten kannst du später deaktivieren. Beachte jedoch, dass deaktivierte Versandarten nur noch in bereits erstellten Belegen angezeigt werden. In neu erstellten Belegen und in Benutzerflächen wie der Auftragsübersicht oder in den Kundendaten steht eine deaktivierte Versandart nicht mehr zur Auswahl zur Verfügung. Du kannst Versandarten auch löschen. Dadurch wird jedoch auch die Versandhistorie gelöscht. Deshalb solltest du nur fälschlicherweise angelegte Versandarten löschen, die du nicht produktiv genutzt hast. |
| **Kein Portocheck** | Mit dieser Option kannst du den Porto-Check im Auftrag deaktivieren. Bleibt der Porto-Check aktiv, zeigt die Auftragsampel ein rotes Symbol für den Portocheck an, falls nicht mindestens ein Portoartikel in den Auftragspositionen enthalten ist. So wird verhindert, dass bei manuell angelegten Aufträgen der Portoartikel vergessen wird. Überlege anhand deiner eigenen Workflows und Arbeitsweise mit Xentral, ob du diese Option aktivieren oder deaktivieren willst. Legst du typischerweise viele Aufträge manuell in Xentral an, kann es sinnvoll sein, diese Option nicht zu aktivieren, sodass gerade bei hochpreisigen Artikeln oder internationalen Sendungen das Porto immer zuverlässig am Auftrag hinterlegt wird. |
| **Drucker Versandlabel** | Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für die Versandlabels genutzt werden soll. Beachte, dass hier nur Drucker auswählbar sind, die du bereits[in Xentral eingerichtet](https://help.xentral.com/hc/de/articles/360016756299#UUID-24ed3a57-a4df-da7a-08f6-141949df3855) hast. Je nachdem, wie und wo der Versandprozess in deinem Unternehmen abläuft, kannst du hier genau den Drucker auswählen, den du benötigst - egal ob direkt am Schreibtisch oder am Packtisch im Lager. |
| **Drucker Export **|** Nur bei internationalem Versand relevant**: Wähle aus dem Dropdown-Menü den Drucker aus, der standardmäßig für Zollpapiere (CN23) genutzt werden soll. |
| **Versand-E-Mail **| Lege hier fest, nach welchen Regeln Versandbenachrichtigungen per E-Mail an deine Kunden verschickt werden sollen, sobald sich die Sendung auf dem Weg befindet. Die folgenden drei Optionen stehen dir zur Verfügung: ** Standardverhalten **: Die Logistikeinstellungen aus dem Projekt werden verwendet. Diese Einstellungen nimmst du im Menü ** Einstellungen > Grundeinstellungen > Projekte > Projekt öffnen > Tab: Einstellungen > Tab: Logistik / Versand **vor. In den Bereichen ** Stufe 1 (Pick/Kommissionierung)**und ** Stufe 2 (Pack)**definierst du über die Checkboxen namens E-Mail, bei welchen Schritten deine Kunden über den Stand der Auftragsbearbeitung informiert werden. ** Keine Versandmail **: Für diese Versandart wird keine Versandinformation per E-Mail versendet. ** Eigene Textvorlage **: Für diese Versandart wird die ausgewählte Textvorlage per E-Mail versendet. Diese Vorlage musst du vorab im Menü ** Einstellungen > Grundeinstellungen > Belege > Textvorlagen **erstellen. Anschließend wählst du die gewünschte Vorlage im Dropdown-Menü ** Textvorlage**aus. Durch diese Auswahl werden die Logistikeinstellungen des Projekts für diese Versandart nicht genutzt. |
| **Lieferungen unterstützt **| Diese Option wird bei der Anlage der Versandart standardmäßig aktiviert. Sobald du alle weiteren benötigten Einstellungen vorgenommen und die Versandart auf ** Aktiv** gestellt hast, kannst du die Versandart in Aufträgen, Lieferscheinen und im Versandzentrum auswählen. |
| **Retouren unterstützt** | Aktiviere diese Option, um zu erlauben, dass Retouren zu Aufträgen erstellt werden können, die ursprünglich mit dieser Versandart erstellt wurden. |
| **Bevorzugte Rücksendemethode** | Wähle eine bevorzugte Versandart für Retouren aus. Sobald in Xentral manuell eine Retoure zu einem Auftrag mit der vorliegenden Versandart angelegt ist, wird die hier gewählte Versandart automatisch im Retourenauftrag vorausgewählt. Diese Einstellung greift nur in Fällen der manuellen Retourenerstellung. |
| **DHL Express Key** | Gib den DHL Express Key ein. |
| **DHL Express Passwort** | Gib dein Passwort für DHL Express ein. |
| **DHL Express Account Number** | Gib deine DHL Express Account Number ein. |
| **Sandbox aktivieren** | Aktiviere diese Option, um den Testmodus zu verwenden, bevor du die Versandart produktiv im Tagesgeschäft nutzt. |
| **Absender Firma / Ansprechpartner / Telefon / E-Mail / Straße / Ort / PLZ **| Gib im Feld ** Absender Firma **deinen Firmennamen ein und trage in den restlichen Feldern die Adressdaten deines Unternehmens ein. Die Angaben, die du hier machst, erscheinen als Absenderadresse auf deinen Versandlabels. 💬** Anmerkung:** Um die Telefonnummer zu übertragen, müssen deine DSGVO-Einstellungen korrekt konfiguriert sein. Nutze die Smart Search, um das Modul Grundeinstellungen zu öffnen und klicke dort auf das Tab System. Im Bereich DSGVO Einstellungen darf die Option Telefon nicht dem Versandunternehmen übergeben nicht aktiviert sein. |
| **Absender Land (2-stellig)**| Gib den ISO-Ländercode für das Land ein, aus dem du versendest. Für Deutschland lautet der korrekte ISO-Code ** DE**. |
| **Service Typ** | Gib hier das Kürzel des Servicetypen ein. Im Kapitel [Verfügbare Servicetypen für DHL Express](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235139971445952) sind alle möglichen Servicetypen beschrieben. |
| **Optionaler lokaler Service Typ **|** Optional**: Gib hier das Kürzel für den lokalen Servicetypen ein. Der lokale Service Typ bezeichnet spezielle, zusätzliche Versandservices, die du direkt bei DHL Express anfragen und buchen kannst. Diese Services sind kostenpflichtig und weichen je nach Zielland oder -gebiet deiner Sendung ab. Sie decken beispielsweise die Lieferung von Gefahrgut, temperaturempfindlichen Produkten oder Empfänger-Unterschrift bei Zustellung ab. Erkundige dich bei deinem DHL Express-Kundenbetreuer, um eine Liste aller verfügbaren lokalen Servicetypen zu erhalten und die Services bei Bedarf zu buchen. |
| **Währung **|** Nur für zollpflichtige Lieferungen relevant **: Gib das Währungskürzel ein, z.B. ** EUR ** für Euro oder **USD** für US-Dollar. |
| **Maßeinheit **| Gib die Maßeinheit ein, in der Länge, Breite, Höhe und Gewicht der Sendung an DHL Express übermittelt werden sollen. Diese Angaben werden zwingend für die Ermittlung des Frachttarifs und die weitere Logistikplanung bei DHL Express benötigt. Die Optionen ** SI **für kg und cm sowie ** SU** für lb und in stehen zur Verfügung. |
| **Label Typ **| Gib das Format ein, in dem dir das Versandlabel nach der Generierung zur Verfügung gestellt werden soll. Du kannst aus Versandlabel-Formaten PDF, ZPL, EPL oder LP wählen. Die Eingabe ** PDF** deckt die meisten Anwendungsfälle ab. Fortgeschrittene Nutzer können eins der anderen Formate nutzen. |
| **Label Template **| Für die meisten Anwendungsfälle ist die Eingabe ** ECOM26_84_001** geeignet. Kontaktiere im Zweifelsfall den IT-Ansprechpartner bei DHL Express, um zu klären, welches Label den jeweiligen Anforderungen entspricht. |
| **Payment Info **| Trage die Payment Info ein. Zur Auswahl stehen ** DAP **und ** DDP **. -** DAP ** (Delivery At Place): Verkäufer ist verantwortlich für Lieferung der Ware inkl. Transportkosten bis zum Käufer. Ausgenommen sind Kosten für Einfuhrformalitäten (bei ausländischen Käufern) wie Mehrwertsteuer und Zoll. Diese zahlt der Kunde, wenn sie über der Freigrenze liegen.<br>-** DDP** (Delivery Duty Paid): Entspricht DAP plus Zoll- und Steuerabwicklung. Der Verkäufer muss die Ware auf eigene Kosten und Gefahr bis zu dem vom Kunden ausgewählten Ort im Importland transportieren. |
| **Standardgewicht **|** Optional**: Welches Gewicht haben die Sendungen typischerweise, die du mit dieser Versandart verschickst? Gib hier ein Standardgewicht in kg ein. Dieses Gewicht wird jedes Mal bei der Erstellung eines Versandlabels an den Versanddienstleister übermittelt, soweit es nicht vor dem Druck des Versandlabels manuell in Xentral geändert wird. |
| **Länge / Breite / Höhe** | Gib die Standardmaße deiner Sendungen in cm an. Diese Maße werden dann an den Versanddienstleister übermittelt, falls sie nicht beim Druck des Versandlabels manuell in Xentral geändert werden. |
| **Beschreibung **| Trage eine kurze Beschreibung des Paketinhalts ein. Die Beschreibung wird unterhalb der ** Referenz auf Label** auf das DHL Express-Versandlabel gedruckt. Diese Angabe ist bei zollpflichtigen Sendungen verpflichtend und sollte möglichst auf Englisch verfasst sein. |
| **Referenz auf Label** | Bestimme mithilfe der angezeigten Variablen, ob du zusätzliche Informationen auf dem Versandlabel abdrucken möchtest. Du kannst auch einen Freitext eingeben. Folgende Variablen stehen dir zur Verfügung: {LIEFERSCHEIN}, {PROJEKT}, {AUFTRAG}, {IHREBESTELLNUMMER}, {NAME3}, {INTERNET}. |
| **Inhaltstyp **| Wähle den Inhaltstyp aus dem Dropdown-Menü aus. Grundsätzlich funktioniert die Anbindung von DHL Express nur mit der Auswahl ** DOCUMENTS**. Eine Ausnahme besteht für den internationalen Versand in Zielländer außerhalb der EU (zollpflichtige Lieferungen). Schau im Kapitel [Wichtige Hinweise zur Verwendung der Versandart](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235139952555467) nach, um mehr zu erfahren. |
| **Tracking-Nummer in Auftrag übernehmen** | Aktiviere diese Option, um die Tracking-Nummer nach der Erstellung des Versandlabels direkt im dazugehörigen Auftrag in Xentral zu übernehmen. So bleibt die Tracking-Nummer dauerhaft in deinem System vermerkt und du musst das Versandlabel nach der Erstellung nicht erneut scannen, um diese Daten in Xentral zu erfassen. |

## Pflichtangaben für DHL Express-Sendungen

Damit nationale wie auch internationale Sendungen fehlerfrei mit DHL Express abgewickelt werden, müssen bestimmte Informationen bei jeder Sendung an DHL Express übermittelt werden. Diese Informationen und damit benötigten Einstellungen in der Versandart kannst du folgender Tabelle entnehmen.

> **Wichtig**
>
> Beachte besonders die benötigten Angaben für den zollpflichtigen Versand, also Lieferungen in Länder außerhalb der EU. Zur Zollabwicklung werden in diesen Fällen ganz bestimmte Daten benötigt.

| Pflicht bei jeder DHL Express-Sendung (Inland und EU) | Pflicht bei zollpflichtigen DHL Express-Sendungen (außerhalb der EU) |
| --- | --- |
| - **Gesamtgewicht der Sendung **: Einstellung ** Standardgewicht **in den [Einstellungen der Versandart](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235148533261493) sowie Checkbox ** Gewicht **im Tab ** Versandlabel **des Lieferscheins<br>-** Abmessungen der Sendung **: Einstellungen ** Länge **, ** Breite ** und **Höhe ** in den [Einstellungen der Versandart](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235148541074263) sowie gleichnamige Checkboxen im Tab **Versandlabel ** des Lieferscheins | -** Währungsangabe für die Angabe des Warenwerts **: Einstellung ** Währung **in den [Einstellungen der Versandart](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235148541074263)<br>-** Warenwert pro Position und Gesamtwert **: Auf der beigelegten Rechnung dargestellt<br>-** Artikelbeschreibung (idealerweise auf Englisch)**: Einstellung ** Beschreibung **in den [Einstellungen der Versandart](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235148541074263)<br>-** Zolltarifnummer **: Einstellung ** Zolltarifnummer **im Bereich ** Hersteller **in den Artikelstammdaten Tipp Alles Wichtige zu Zolltarifnummern findest du im Artikel Zolltarifnummer (HS Code - Harmonized System Code).<br>-** Herkunft der Waren **: Einstellung ** Herkunftsland (ISO-Code)**und optional ** Ursprungsregion **im Bereich ** Hersteller**der Artikelstammdaten<br>-** Incoterms **: Einstellung ** Payment Info** in den [Einstellungen der Versandart](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235148541074263) |

## Verfügbare Servicetypen für DHL Express

Die folgende Tabelle enthält eine Auflistung aller verfügbaren Servicetypen für die Versandart **DHL Express **. Bei der Einrichtung der Versandart trägst du das passende Kürzel aus der Spalte ** Service Typ**im entsprechenden Feld in den Einstellungen der Versandart ein.

> **Wichtig**
>
> Hinterlege nur die Servicetypen in Xentral, deren Verwendung du bei **DHL Express** vertraglich gebucht hast.
>
> Eine Übersicht aller DHL Express-Produkte findest duhier auf der offiziellen Website.

| Service Typ (Globaler NW Typ) | Produkt | |
| --- | --- | --- |
| **I** | DOMESTIC EXPRESS 9:00 | Nationaler Expressversand (Inland) |
| **O** | DOMESTIC EXPRESS 10:00 |
| **1** | DOMESTIC EXPRESS 12:00 |
| **N** | DOMESTIC EXPRESS |
| **X **| EXPRESS ENVELOPE | Internationaler Expressversand (in EU-Länder und damit ** nicht zollpflichtig**) |
| **D** | EXPRESS WORLDWIDE |
| **K** | EXPRESS 9:00 |
| **L** | EXPRESS 10:30 |
| **T** | EXPRESS 12:00 |
| **U** | EXPRESS WORLDWIDE |
| **E **| EXPRESS 9:00 | Internationaler Expressversand (in Drittländer und damit ** zollpflichtig**) |
| **M** | EXPRESS 10:30 |
| **Y** | EXPRESS 12:00 |
| **P** | EXPRESS WORLDWIDE |
| **W** | ECONOMY SELECT EU | Economy Select |
| **H** | ECONOMY SELECT NON-EU |

## Versandlabel drucken

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Druck des Versandlabels im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Gehe dazu wie folgt vor.

![lieferschein_dhl_express_versandlabel-de.png](https://help.xentral.com/hc/article_attachments/22351550919452)

1. Öffne per Klick auf das Stift-Symbol rechts einen Lieferschein im Menü **Einstellungen > Lager > Lieferschein**.
1. Öffne das Tab **Details**.
1. Scrolle nach unten, bis du den Bereich **Lieferschein** erreichst.
1. Wähle die Versandart **DHL Express ** aus dem Dropdown-Menü**Versandart** aus.
1. Klicke auf **Speichern**.

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss das Versandlabel bei myDHL+ stornieren. Gehe dazu wie folgt vor.

1. Logge dich bei [myDHL+](https://mydhl.express.dhl/de/de/home.html) ein.
1. Klicke auf den Menüpunkt **Sendungsverlauf**.
1. Wähle das Versandlabel, aus das storniert werden soll. Klicke dann auf **Stornieren**.

## Häufige Fehlermeldungen und Lösungen

Die folgenden Fehler können bei Verwendung der Versandart **DHL Express** auftreten:

| Fehlermeldung | Fehlerbehebung |
| --- | --- |
| **Exception: [ISC.0082.9464] Value is shorter than minimum length ------------ /shipreq:ShipmentRequest/ RequestedShipment/Ship/Recipient/Contact/ PhoneNumberProcess failure occurred. **| Diese Fehlermeldung tritt auf, wenn es Probleme mit der angegebenen Telefonnummer gibt. Dafür gibt es zwei mögliche Gründe: Die Telefonnummer ist in irgendeiner Weise falsch (z.B. zu kurz) oder fehlt. Die Telefonnummer kann aufgrund deiner DSGVO-Einstellungen nicht übertragen werden. Nutze die Smart Search, um das Modul ** Grundeinstellungen **zu öffnen und klicke dort auf das Tab ** System **. Im Bereich ** DSGVO Einstellungen **darf die Option ** Telefon nicht dem Versandunternehmen übergeben** nicht aktiviert sein. |
| **Exception: Requested product(s) not available at payer, 1/-Process failure occurred. Process ID associated for that transaction **| Sobald du ein Paket im Inland versendest, d.h. du I,O,1 oder N im Feld ** Service Typ **eingegeben hast, musst du auch für die Einstellung ** Inhaltstyp **die Option ** DOCUMENTS** auswählen. Dadurch kennzeichnest du die Sendung als zollfrei. |
| **Exception: [ISC.0082.9460) No matching enumeration value ---/ shipreq:ShipmentRequest/RequestedShipment/Shipmentinfo/ LabelTypeProcess failure occurred. Process ID associated for that transaction** | Gib im Feld**Label Typ** in den Einstellungen der Versandart den Text "PDF" ein. |
| **ExportDeclaration is mandatory when provided product is Dutiable** | Wähle für die Einstellung **Inhalts Typ**die Option ** DOCUMENTS**aus dem Dropdown-Menü. Klicke anschließend auf ** Speichern** und versuche erneut, das Versandlabel zu erstellen. Weitere Informationen dazu findest du im Kapitel [Wichtige Hinweise zur Verwendung der Versandart](#UUID-36e05436-5eac-4475-6580-e8e29c2fbdee_section-id235139952555467). |