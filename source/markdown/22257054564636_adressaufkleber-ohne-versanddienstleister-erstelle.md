In bestimmten Ausnahmefällen kann es sinnvoll sein, nur einen Adressaufkleber in Xentral ohne die Anbindung an einen Versanddienstleister zu nutzen – z. B. für interne Sendungen, Briefe mit Briefmarke oder grenzüberschreitende Lieferungen ohne Track & Trace. Diese Funktion ist nicht für den regulären Versandprozess vorgesehen, sondern richtet sich an Nutzer mit speziellen Anforderungen außerhalb der gängigen Versandarten.

Es ist möglich, eine individuelle Etikettenvorlage zu erstellen, die Versandart „Adressaufkleber“ zu konfigurieren und die Labels anschließend manuell im Versandzentrum oder über den Lieferschein zu drucken.

### Achtung

Für den Großteil der Versandprozesse empfiehlt Xentral den Einsatz angebundener Versanddienstleister mit Paketmarken und automatischem Tracking.

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du[hier](https://help.xentral.com/hc/de/articles/18567521362332#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

## Features

Der Adressaufkleber bietet dir diese Features:

- Erstellung von Adressaufklebern für Versandgut
- Versenden von Versandgut per Briefmarke
- Cross-Boarder Versand
- Interne Lieferungen

## Einstellungen für Adressaufkleber

Im folgenden Abschnitt findest du Informationen darüber, wie du in xentral verschiedene Einstellungen für Adressaufkleber vornehmen kannst. Zunächst richtest du einen Etikettendrucker ein, mit welchem du später deine Adressaufkleber druckst. Über das Etiketten-Modul legst du danach das Format deines Adressaufklebers fest.

### Etikettendrucker einrichten

Unter **Administration > Einstellungen > System > Drucker > +NEU** richtest du einen Etikettendrucker ein. Entweder du bindest eine[Etikettendrucker](https://help.xentral.com/hc/de/articles/360017382100#UUID-7093d366-0a7d-c197-44f6-08cb948daefa)direkt an oder du verwendest einen sogenannten PDF-Etikettendrucker, der dir die Etiketten als PDF direkt im Browser anzeigt.

Folgende Einstellungen nimmst du vor:

- **Name/Standort:** Gib einen von dir gewählten Namen des Druckers ein
- **Bezeichnung:** Gib eine von dir gewählte Bezeichnung des Druckers ein
- **Aktiv:** Setze den Haken, um den Drucker angezeigt zu bekommen und zu verwenden
- **Geräteart: ** Wähle aus dem Drop-Down Menü ** Etikettendrucker** aus
- **Format: ** Wähle aus dem Drop-Down Menü das Format ** DINA4** aus
- **Kein Hintergrund:** Hake dieses Kästchen nur an, wenn dieser Drucker Briefpapier ohne Hintergrund drucken soll
- **Anbindung: ** Als Anbindung wähle ** Download** aus dem Drop-Down Menü aus

### Etikett erstellen

Um einen Adressaufkleber zu erzeugen, lege unter **Administration > Einstellungen > System > Etiketten ** ein neues Etikett über**+NEU** an. Dabei steht es dir frei, welche Variablen und welche Positionierung du für das Etikett vornimmst. Hier ein Beispiel:

![Address-Labels-1.png](https://help.xentral.com/hc/article_attachments/22257055874588)

Die XML des Beispiel-Etiketts lautet wie folgt:

```
<label>

<line x="3" y="3" size="3">Absender</line>
<line x="3" y="6" size="3">{ABSENDERNAME}</line>
<line x="3" y="9" size="3">{ABSENDERSTRASSE}</line>
<line x="3" y="12" size="3">{ABSENDEROPLZ}</line>
<line x="10" y="12" size="3">{ABSENDERORT}</line>
<line x="60" y="3" size="3">Empfänger</line>
<line x="60" y="6" size="3">{NAME}</line>
<line x="60" y="9" size="3">{STRASSE}</line>
<line x="60" y="12" size="3">{PLZ}{ORT}</line>
<line x="69" y="12" size="3">{PLZ}{ORT}</line>

</label>
```

### Etikett im Adressaufkleber

Nachdem du alle Einstellungen für deinen Adressaufkleber wie oben beschrieben vorgenommen hast, kannst du dein individuelles Etikett auch in der Versandart **Adressaufkleber** verwenden.

#### Versandart Adressaufkleber

Navigiere dazu über **App Center > Versandarten ** in das Versandarten-Modul. Über**+NEU > Adress Aufkleber** legst du die Versandart Adressaufkleber an.

Befülle folgende Felder:

- **Bezeichnung:** Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ:** Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du die Voreinstellung bei
- **Modul: ** Wähle ** Adress Aufkleber** aus dem Drop-Down Menü aus
- **Projekt:** Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene DHL Versandart angelegt wird
- **Aktiv:** Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck:** Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Paketmarken druckt
- **Drucker Export:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail:** Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Etikettenvorlage verwenden:** Hake diese Kästchen nur an, wenn du eine Etikettenvorlage verwenden möchtest. Diese muss zuvor angelegt worden sein
- **Etikettenvorlage:** Hast du zuvor eine Etikettenvorlage angelegt und den Haken bei "Etikettenvorlage verwenden" gesetzt, dann wähle aus dem Menü eine Etikettenvorlage aus

Klicke abschließend auf **Speichern**.

#### Etikettenvorlage verwenden

Wenn du eine, von dir bereits angelegte Etikettenvorlage für deinen Adressaufkleber verwenden möchtest, wähle diese in der Versandarten-Oberfläche aus. Diese zwei Felder sind dabei wichtig:

- **Etikettenvorlage verwenden:** Hake dieses Kästchen unbedingt an, damit du eine Vorlage verwenden kannst
- **Etikettenvorlage:** Wähle aus der Liste die Etikettenvorlage aus, die du für den Adressaufkleber angelegt hast

Alternativ kannst du auch einen vorgegebenen Adressaufkleber verwenden.

## Adressaufkleber drucken

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Druck des Adressaufklebers im Versandzentrum oder auch in einem einzelnen Lieferschein testen. Wähle dazu unter **Lager & Logistik > Lieferschein > Details > Lieferschein ** im Bereich **Lieferschein ** die Versandart**Adressaufkleber** aus dem Drop-Down Menü aus.

> **Anmerkung**
>
> Alternativ kannst du diese auch unter **Lager & Logistik > Versandzentrum** am eingestellten Drucker ausdrucken.

Klicke auf die **Speichern**

-Schaltfläche, bevor du in den Paketmarkendialog navigierst.

Klicke im Anschluss im Lieferschein auf den Reiter **Paketmarke ** und drucke über**Packstück erfassen** einen Adressaufkleber für die enthaltenen Artikel.

Als Resultat erhältst du den eingestellten Adressaufkleber:

![Address-Labels-2.png](https://help.xentral.com/hc/article_attachments/22257078523804)