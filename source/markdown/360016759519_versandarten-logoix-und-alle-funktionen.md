> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Mit der Versandart LogoiX an- bzw. verbindest du dein xentral mit dem Versandservice-Unternehmen LogoiX, um Online-Etiketten für den Versand zu erstellen. Diese Etiketten kannst du auch individuell gestalten. Die Website des Versanddienstleisters mit weiteren Informationen findest du[hier](https://mein.logoix.com/cgi-bin/portal.pl).

Eine allgemeine Übersicht über die Versandarten und Paketmarken, die du in xentral nutzen kannst, findest du[hier](https://help.xentral.com/hc/articles/360016722580#UUID-7d97af0c-3e39-6798-67c6-50f26028c174).

## Features

LogoiX bietet dir folgende Features:

- Verwenden einer selbst erstellten Etikettenvorlage
- Bestimmung der Frachtart
- Angabe einer Inhaltsbeschreibung im Lieferschein
- Auswahl des Empfängertyps
- Angabe zu zerbrechlicher Ladung

## Anbindung von LogoiX an xentral

Um LogoiX an xentral anzubinden, benötigst du die API-Daten für deinen Account. Diese erhältst du bei deinem LogoiX-Geschäftskundenbetreuer.

## Einstellungen in xentral

Diverse Einstellungen kannst du in xentral für die Nutzung der Versandart LogoiX vornehmen, unter anderem die Neuanlage der Versandart und die Gestaltung von XML-Etiketten.

### Versandart anlegen

Unter **Administration > Einstellungen > Versandarten > +NEU > LogoiX** legst du die neue Versandart an.

Befülle folgende Felder:

- **Bezeichnung:** Wähle frei eine Bezeichnung für die Versandart. Diese wird in xentral u.a. im Auftrag zur Auswahl im Drop-Down Menü angezeigt
- **Typ:** Gib den Typ/die Feldbezeichnung an. Diese kannst du generell beliebig wählen, sofern sie nicht für das Shop Mapping oder andere Mappings notwendig ist. Idealerweise behältst du Voreinstellung bei
- **Modul: ** Wähle ** Logoix** aus dem Drop-Down Menü aus
- **Projekt:** Wähle optional ein Projekt aus, sofern für jedes Projekt eine eigene LogoiX-Versandart angelegt wird
- **Aktiv:** Durch Anhaken aktivierst du die Versandart und machst sie sicht- und nutzbar
- **Kein Portocheck:** Durch Anhaken wird kein Portocheck im Auftrag durchgeführt
- **Drucker Paketmarke:** Wähle aus dem Drop-Down Menü den Standarddrucker, welcher die Paketmarken druckt, aus
- **Drucker Export:** Wähle aus dem Drop-Down Menü den Standarddrucker aus, welcher die Exportpapiere druckt
- **Versandmail:** Wähle aus dem Drop-Down Menü das Verhalten der Versandmail aus. "Standardverhalten" bedeutet, dass eine Standard-Trackingmail versendet wird, "keine Versandmail" bedeutet, dass keine Trackingmail bei dieser Versandart versendet wird und "eigene Textvorlage" bedeutet, dass für diese Versandart eine eigene Textvorlage für die Versandbestätigung verwendet wird, unabhängig vom Projekt und Logistikprozess
- **Etikettenvorlage verwenden:** Wenn du dieses Feld anhakst, kannst du aus dem Feld darunter eine Etikettenvorlage auswählen. Dieses Feld ist aber optional
- **Etikettenvorlage:** Wenn du das Feld "Etikettenvorlage verwenden" angehakt hast, kannst du nun aus dem Drop-Down Menü eine von dir zuvor angelegte Etikettenvorlage auswählen
- **API Benutzername:** Gib deinen API Benutzernamen ein. Diesen erfährst du von deinem LogoiX-Geschäftskundenbetreuer
- **API Passwort:** Gib dein API Passwort ein. Dieses erfährst du ebenfalls von deinem LogoiX-Geschäftskundenbetreuer

Klicke abschließend auf **Speichern**.

### XML Etiketten einstellen

Möchtest du XML Etiketten verwenden, musst du diese zunächst er- und einstellen. Das geschieht unter **Administration > Einstellungen > System > Etiketten ** über die Schaltfläche**+NEU**.

Befülle in jedem Fall folgende Felder:

- **Name:** Vergib eine Bezeichnung für das Etikett, die auf einen Blick erkennen lässt, dass das ein Etikett für LogoiX ist
- **XML:** Gib deinen frei gewählten XML-Code ein, mit welchem du das Etikett individuell einstellst
  Folgenden XML-Code kannst du beispielsweise zur Erstellung deines individuellen Etiketts verwenden:

- **Verwenden als:** Wähle das Format des Etiketts aus dem Drop-Down Menü aus

Weitere Informationen zum Erstellen von Etiketten findest du[hier.](https://help.xentral.com/hc/articles/360017573119#UUID-fe2f31f1-3109-8b78-4b73-57cb4e78138d)

### Etikett mit Empfänger- und Lieferadresse

Wenn du das Etikett in den Etiketten-Einstellungen größer gewählt hast, kannst du auch die Empfänger- und Lieferadresse angeben.

Folgenden XML-Code kannst du beispielsweise zur Erstellung deines individuellen Etiketts verwenden:

```
<label>
 <span class="hljs-tag"><span class="hljs-name">line</span>
 <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr">y</span> =<span class="hljs-string"> "3"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>sender<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr">y</span>=< span class="hljs-string"> "6"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{ABSENDERNAME}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr">y</span>=< span class="hljs-string"> "9"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{ABSENDERSTRASSE}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr">y</span>=< span class="hljs-string"> "12"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{ABSENDERPLZ}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "10"</span> <span class="hljs-attr">y</span>=< span class="hljs-string"> "12"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{ABSENDERORT}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><span class="hljs-name">barcode</span> <span class="hljs-attr">x</span>=< span class="hljs-string"> "3"</span> <span class="hljs-attr">y</span>=<span class="hljs-string"> "15"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr">type< /span>=<span class="hljs-string"> "1"</span>></span>{LIX}<span class="hljs-tag">barcode</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "3"</span> <span class="hljs-attr">y</span> =<span class="hljs-string"> "18"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{LIX}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "60"</span> <span class="hljs-attr">y</span> =<span class="hljs-string"> "3"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>recipient<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "60"</span> <span class="hljs-attr">y</span> =<span class="hljs-string"> "6"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{NAME}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "60"</span> <span class="hljs-attr">y</span> =<span class="hljs-string"> "9"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{STRASSE}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "60"</span> <span class="hljs-attr">y</span> =<span class="hljs-string"> "12"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{PLZ}<span class="hljs-tag">line</span>>
 <span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x</span>=<span class="hljs-string"> "69"</span> <span class="hljs-attr">y</span>=< span class="hljs-string"> "12"</span> <span class="hljs-attr">size</span>=<span class="hljs-string"> "3"</span>></span>{location}<span class="hljs-tag">line</span>>
</label>
```

### XML Etiketten verwenden

Hast du alle Einstellungen im Etikett wie gewünscht vorgenommen, kannst du dieses auch in der Versandart LogoiX verwenden.

Navigiere zu **Administration > Einstellungen > Versandarten > LogoiX ** und hake dazu das Feld**Etikettenvorlage verwenden** an und hinterlege ein existierendes Etikett, das du aus der Liste auswählst:

![logoix5.png](https://help.xentral.com/hc/article_attachments/5009694799900)

## Paketmarke erzeugen und drucken

Sobald du alle Einstellungen wie oben beschrieben vorgenommen hast, kannst du den Paketmarkendruck im Versandzentrum, in einem Auftrag oder auch in einem einzelnen Lieferschein testen. Wähle dazu unter **Lager & Logistik > Lieferschein > Details > Lieferschein ** im Bereich **Lieferschein ** die**Versandart****LogoiX ** aus dem Drop-Down Menü aus. Klicke auf die **Speichern**

-Schaltfläche, bevor du in den Paketmarkendialog navigierst.

Klicke im Anschluss im Lieferschein auf den Reiter **Paketmarke ** und erzeuge über**Packstück erfassen** eine Paketmarke für die enthaltenen Artikel:

![logoix7.png](https://help.xentral.com/hc/article_attachments/5009654529180)

Nachdem dein Testdruck abgeschlossen ist, kannst du im Anschluss die Paketmarke im LogoiX-Geschäftskundenportal stornieren.

### Weitere Features

Die Versandart LogoiX bietet dir im Paketmarkendialog weitere Features an:

**Einfügen einer Inhaltsbeschreibung ** Im Lieferschein kannst du optional auch noch eine Inhaltsbeschreibung deiner Waren im Paket angeben. Nutze dazu das Feld **Inhaltsbeschreibung **. Sei so konkret wie möglich, da diese Inhaltsbeschreibung auch auf dem Onlineetikett zu lesen ist. ** Bestimmung der Frachtart ** Zusätzlich kannst du über ein Drop-Down Menü die Frachtart deiner Sendung einstellen. Zur Auswahl stehen im Feld **Frachtart ** Paket, Sperrgut, Europalette und Einmalpalette. ** Bestimmung des Empfängers ** Du kannst darüber hinaus auch den Empfänger individuell festlegen. Nutze dazu das Drop-Down Menü im Feld **Empfänger ** und wähle zwischen Privatperson und Unternehmen aus. ** Bestimmung von zerbrechlicher Ladung ** Ist die Ladung zerbrechlich, kannst du das auch auf der Paketmarke deutlich machen. Hake dazu das Feld **Zerbrechlich ** an und klicke erst im Anschluss auf **Packstück erfassen**.