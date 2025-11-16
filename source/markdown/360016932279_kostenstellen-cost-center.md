Kostenstellen sind eine Möglichkeit im internen Rechnungswesen deine Kosten unter Kontrolle zu halten. Eine Kostenstelle ist ein Bereich in deinem Unternehmen in dem Kosten anfallen oder Leistungen erbracht werden. Kostenstellen werden durch eine eindeutige Nummer repräsentiert. Da Kostenstellen nur für das interne Rechnungswesen genutzt werden, unterliegen sie keinen rechtlichen Anforderungen und können beliebig von dir strukturiert werden.

Typische Arten, um Kostenstellen zu strukturieren sind:

- Funktion: Deine Kostenstellen können auf den Abteilungen deines Unternehmens basieren, wie Verkauf, Lager und Verwaltung.
- Ort: Unterschiedliche Filialen oder Gebäude können als eigene Kostenstellen definiert werden.
- Projekt: Große Projekte können ihre eigenen Kostenstellen bekommen, damit du schnell die Kosten des Projekts nachvollziehen kannst.

InXentral kannst du Kostenstellen in Artikeln, Belegen (inklusive Verbindlichkeiten) und im Zahlungseingang hinterlegen.

Kostenstellen werden als eigene Spalte beim Export von Rechnungen und Verbindlichkeiten im Finanzbuchhaltungsexport exportiert. In Belegen kannst du die Kostenstelle über die Variable {KOSTENSTELLE} in der entsprechenden[Textvorlage](https://help.xentral.com/hc/de/articles/360021441799#UUID-7f7f61af-1277-f484-2138-07f5c0f301be)anzeigen lassen.

> **Anmerkung**
>
> Zur Auswertung von Kostenstellen steht dir dervorgefertigte Berichtmit dem Namen074 - Auswertung der Kostenstelleim ModulBerichtezur Verfügung.

## Kostenstellenplan strukturieren

Du kannst deine Kostenstellen beliebig strukturieren, jedoch empfehlen wir dir eine logische Struktur für die Gesamtheit deiner Kostenstellen (auch Kostenstellenplan genannt) anhand der folgenden Punkte aufzubauen:

- **Hierarchisch**: Die ersten Ziffern deiner Kostenstelle sollten allgemein gehalten werden und dann mit weiteren Ziffern spezifischer werden. Du kannst z.B. die ersten Ziffern deinen Filialen zuweisen, die folgenden deinen Abteilungen, und so weiter.
- **Erweiterbar**: Üblicherweise solltest du etwas 2-3 Ziffern pro Information bereit stellen, damit du bei Bedarf die Information erweitern kannst (z.B. aufgrund neuer Filialen oder Abteilungen) oder um die Kostenstellen in Zukunft spezifischer zu gestalten (die allgemeine HR-Abteilung wird in Verwaltung und Talentakquise aufgeteilt).
- **Zweckmäßig**: Je mehr Kostenstellen du hast, desto genauer wird auch die Kontrolle über deine Kosten. Gleichzeitig macht es die Buchhaltung komplexer und erhöht den Verwaltungsaufwand. Allgemein sollten kleinere Unternehmen weniger Kostenstellen haben als ein großes Unternehmen.

> **Anmerkung**
>
> Beachte, dass jedes Unternehmen anders ist und je nach Branche, Standort und Organisationsstruktur unterschiedliche Anforderungen hat. Bitte überprüfe die Kostenstruktur und Anforderungen deines Unternehmens bevor du Kostenstellen implementierst.

## Anlegen einer neuen Kostenstelle

DasKostenstellen-Modul erlaubt es dir neue Kostenstellen anzulegen und gibt dir eine Übersicht über alle deine Kostenstellen in einer durchsuchbaren Tabelle.

Gehe wie folgt vor, um eine Kostenstelle anzulegen:

1. Gib Kostenstellen in der Smart Search ein und öffne den entsprechenden Eintrag. Das Modul öffnet sich.
1. Klicke auf +NEU.
1. Gib die Nummer deiner Kostenstelle an. Idealerweise hast du schon einen [Kostenstellenplan](#UUID-7497bd65-7248-838c-8e6f-04487fd8ecd2_section-idm4503131981576034265226005345) angelegt und brauchst die Nummer nur einzutragen.
1. Gib eine aussagekräftige Beschreibung der Kostenstelle in das Feld Bezeichnung ein, z.B. Vertrieb DACH. Dies hilft dir dabei, dich an die Aufgabe der Kostenstelle zu erinnern. Du kannst in der Übersicht nach der Bezeichnung suchen. Sie wird außerdem angezeigt, wenn du die Kostenstelle einem Artikel, Beleg oder Verbindlichkeit zuordnest.
1. Optional: Gib weitere interne Informationen zur Kostenstelle in das Feld Interne Bemerkung ein. Du kannst z.B. die Aufgabe der Kostenstelle ausführlicher beschreiben oder die Struktur der Nummer erläutern. Diese Informationen werden nur angezeigt, wenn du die entsprechende Kostenstelle im Kostenstellen-Modul bearbeitest.
1. Klicke auf Speichern.

Die Nachricht:Die Daten wurden gespeichert!erscheint. Klicke auf denZurück-Pfeil![ArrowLeft.png](https://help.xentral.com/hc/article_attachments/13755997110940)

, um wieder zur Übersicht der Kostenstellen zu gelangen.

Du kannst deine Kostenstellen und deinen Kostenstellenplan jederzeit ändern, indem du neue Kostenstellen hinzufügst, bestehende mit demStift-Symbol![PenIcon.png](https://help.xentral.com/hc/article_attachments/13755966067356)

bearbeitest oder Kostenstellen mit derX-Schaltfläche![CrossIcon.png](https://help.xentral.com/hc/article_attachments/13755971983388)

löschst.

> **Tipp**
>
> Bevor du eine Kostenstelle löschst oder andere große Änderungen vornimmst, solltest du eine Sicherungskopie mit denCSV-,Excel-, oderPDF-Schaltflächen über der Übersichtstabelle zu erstellen.

## Kostenstellen zu Belegen hinzufügen

Kostenstellen können zu Dokumenten hinzugefügt werden, indem du entweder Artikel Kostenstellen zuweist oder du direkt einem einzelnen Beleg eine Kostenstelle hinzufügst.

### Artikeln Kostenstellen zuweisen

Beim Zuweisen einer Kostenstelle zu einem Artikel, wird die Kostenstelle jedes Mal auf den Artikel angewendet, wenn der Artikel in einem Beleg vorhanden ist. Andere Artikel oder der Beleg selbst werden nicht von der Kostenstelle beeinflusst.

Du kannst eine Kostenstelle einem Artikel zuweisen, indem du zuVerkaufen > Artikelnavigierst und den entsprechenden Artikel öffnest. Öffne denReiter Details > Unterreiter Finanzbuchhaltungund gib die Kostenstelle unten links ein.

![product__financialaccounting__costcenter.png](https://help.xentral.com/hc/article_attachments/13755989872924)

### Belegen Kostenstellen zuweisen

Du kannst einem gesamten Beleg eine Kostenstelle zuweisen, indem du den entsprechenden Beleg öffnest und bis zum BereichEinstellungrechts unten scrollst. Hier kannst du die Kostenstelle für Angebote, Aufträge, Lieferscheine und Rechnungen eintragen. Die Kostenstelle wird auf alle Artikel im Beleg angewandt, bei der keine abweichende Kostenstelle im Artikel hinterlegt ist.

> **Anmerkung**
>
> Du kannst jedem Artikel eines Belegs eine abweichende Kostenstelle im UnterreiterPositionendes Belegs zuweisen, indem du auf dasStift-Symbolklickst. Öffne den BereichSteuernauf der rechten Seite und gib dieKostenstelledort ein.

Du kannst einer Verbindlichkeit auf die selbe Art und Weise eine Kostenstelle hinzufügen, jedoch befindet sich hier die Option in der Mitte der linken Seite. Beim Export von Verbindlichkeiten und Rechnungen im[Finanzbuchhaltungsexport](https://help.xentral.com/hc/de/articles/360016725100#UUID-a322c08d-1f79-6bbe-adfe-2ca542c4bd6e)werden die Kostenstellen in einer extra Spalte exportiert.

### Im Zahlungseingang Kostenstellen zuweisen

Sobald eine Buchung im[Zahlungseingang](https://help.xentral.com/hc/de/articles/360016758959#UUID-49ed70ab-a286-4305-202f-d317f265f31f)durchgeführt wird, kannst du der Buchung eine Kostenstelle zuweisen. Öffne dazu die Buchung über dasStift-Symbol![PenIcon.png](https://help.xentral.com/hc/article_attachments/13755966067356)

und gib dieKostenstelleauf der rechten Seite ein.

![receiptofpayment_bankstatements_costcenter.png](https://help.xentral.com/hc/article_attachments/13755982924956)

Du kannst außerdem jeder manuellen Buchung im ReiterKontenblattimZahlungseingangeine Kostenstelle zuweisen.

![receiptofpayment_accountsheet_costcenter.png](https://help.xentral.com/hc/article_attachments/13755974140956)

In deinem[PayPal Geschäftskonto](https://help.xentral.com/hc/de/articles/360016721920#UUID-adabbd9f-f973-20fe-e774-3a9455a818dd)kannst du eine Standard-Kostenstelle hinterlegen, die du nutzen kannst, um deine PayPal-Gebühren auf eine eigene Kostenstelle zu buchen.