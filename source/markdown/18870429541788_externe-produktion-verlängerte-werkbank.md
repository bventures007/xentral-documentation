## Einführung

Wenn du deine Produktion oder auch nur einzelne Prozessschritte der Produktion an externe Dienstleister, auslagern möchtest, hilft dir Xentral den Überblick zu bewahren und die Warenbewegungen transparent abzubilden.

> **Tipp**
>
> **Exkurs **: Was versteht man unter ** verlängerter Werkbank**?
>
> Die verlängerte Werkbank bedeutet, dass du Teile deiner Produktion an externe Firmen oder Standorte auslagerst, um Kosten zu senken und die Effizienz zu steigern. Du behältst die Kontrolle über Design, Qualität und Endmontage, während standardisierte / einfache Produktionsschritte extern durchgeführt werden. Dies ermöglicht dir, Kosten zu reduzieren, flexibel zu bleiben und dich auf deine Kernkompetenzen zu konzentrieren.
>
> Abweichend zu einer normalen Bestellung, mit der du einfach nur Artikel nach Katalog / nach Zeichnung / nach Spezifikation bestellst, stellst du bei der verlängerten Werkbank Material an den durchführenden Dienstleister bei. Es kann sich dabei um das gesamte für die Stückliste benötigte Material oder nur um einzelne Komponenten handeln.

### Anwendungsbeispiel

Ein Hersteller erzeugt in seinem Werk verschiedene Fruchtgummi-Sorten in Mini-Verpackungen. Die Konfektionierung dieser kleinen Päckchen in Adventskalender, wird an einen spezialisierten Verpackungsdienstleister ausgelagert.

## Stammdaten

Eine generelle Übersicht zur Anlage der Artikel für die Produktion findest du unter[Einrichtung & Stammdaten](https://help.xentral.com/hc/de/articles/18870446011164#UUID-35a8b305-3e2a-255f-7831-4660e3d6d72f). In den folgenden Abschnitten ist beschrieben, wie die o. g. Artikelarten für die Externe Produktion genau konfiguriert werden müssen.

Um eine externe Produktion veranlassen zu können, brauchst du bei den Stammdaten folgende Artikelarten:

- Dienstleistungsartikel: Artikel, der die durch den externen Anbieter durchzuführende Tätigkeit definiert
- Beistellungsartikel: Artikel, die von deiner Firma an den externen Dienstleister gesendet werden, damit dieser die Tätigkeit durchführen kann
- Stückliste: Artikel mit Stückliste, die sowohl den Dienstleistungsartikel als auch die Beistellungsartikel beinhaltet

### Dienstleistungsartikel

Richte den Dienstleistungsartikel so ein:

Artikel > Details

- Name und Nummer des Artikels: Dienstleister als Standardlieferant eintragen
- Artikel Optionen: Lagerartikel deaktivieren
- Sonstige Einstellungen: Dienstleistung aktivieren

Artikel > Einkauf

Füge den Einkaufspreis ein, den du für die Dienstleistung an den Lieferanten zahlst:

![ExtProduktion_Stammdaten_Dienstleistungsartikel_Einkauf.png](https://help.xentral.com/hc/article_attachments/19368045943196)

### Beistellungsartikel

Nimm für die Beistellungsartikel folgende Einstellungen vor:

Artikel > Details

- Artikel Optionen: Lagerartikel aktivieren

### Stücklistenartikel

Der Stücklistenartikel ist das fertige Gut, das du von deinem Dienstleister nach der externen Produktion zurückerhälst. Ihn konfigurierst du so:

Artikel > Details

- Name und Nummer des Artikels: Dienstleister als Standardlieferant eintragen
- Artikel Optionen: Lagerartikel aktivieren
- Sonstige Einstellungen:
  - Stückliste aktivieren
  - Produktionsartikel aktivieren
  - Externe Produktion aktivieren

Artikel > Stückliste

Füge sowohl Dienstleistungs- als auch alle Beistellungsartikel in die Stückliste ein.

![ExtProduktion_Stammdaten_Stucklistenartikel_Stuckliste.png](https://help.xentral.com/hc/article_attachments/19368077201436)

Die Art wählst du beim Einfügen einer neuen Position aus:

![ExtProduktion_Stammdaten_Stucklistenartikel_Stuckliste_NeuePosition.png](https://help.xentral.com/hc/article_attachments/19368045959580)

## Einrichtung

Wenn du die externe Produktion nutzt, empfehlen wir, die Produktionskorrektur aktiv zu haben. Beachte dazu die Angaben zur[Produktionseinrichtung](https://help.xentral.com/hc/de/articles/18870446011164#UUID-35a8b305-3e2a-255f-7831-4660e3d6d72f_section-idm234811349796097), dort insbesondere Punkt (4).

## Produktion anlegen

Nachdem die Stammdaten angelegt sind, läuft der Workflow bei der externen Produktion wie folgt ab:

![ExtProduktion_Workflow.png](https://help.xentral.com/hc/article_attachments/19368077204636)

### Produktion anlegen und freigeben

Die Anlage und Freigabe der Produktion erfolgt bei der externen Produktion exakt wie bei jeder anderen auch. Orientiere dich dabei einfach an dieser[Anleitung](https://help.xentral.com/hc/de/articles/18870446128284#UUID-78e48b0c-91b7-3780-0e62-f7de4326197f_section-idm234820028443828). Die Produktionspositionen könnten zum Beispiel so aussehen:

![ExtProduktion_Produktion_Positionen_Fertigungsstuckliste.png](https://help.xentral.com/hc/article_attachments/19368045966748)

### Externe Produktionsschritte anlegen

Nachdem du die Produktion angelegt und freigegeben hast, veranlasst du nun die externen Produktionsschritte. Öffne dafür den ReiterProtokollder entsprechenden Produktion. Klicke dort aufanlegen:

![ExtProduktion_Produktion_Protokoll.png](https://help.xentral.com/hc/article_attachments/19368077212956)

Die folgende Maske zeigt dir im oberen Teil das vom Dienstleister zu erzeugende Produkt - hier der bestückte Adventskalender - mit der durchzuführenden Dienstleistung und allen beizustellenden Materialien. Im unteren Teil der Maske legst du

- mit der Angabe in Bereich (1) eine Bestellung über die Dienstleistung an und
- mit der Auswahl in Bereich (2) einen Verkaufsauftrag, mit dem du das beizustellende Material an den Lieferanten senden kannst:

![ExtProduktion_Produktion_Protokoll_BelegeAnlegen.png](https://help.xentral.com/hc/article_attachments/19368079524764)

Beide Belege werden nach der Bestätigung mit Ok angelegt. Durch Klick auf ENTWURF kannst du die Belege öffnen, bei Bedarf anpassen / ergänzen und schließlich freigeben und versenden:

![ExtProduktion_Produktion_Protokoll_ExterneProduktionsschritte.png](https://help.xentral.com/hc/article_attachments/19368077227420)

Der Auftrag dient dem Versand des beizustellenden Materials an den Lieferanten und du kannst deinen Standard-Prozess für ausgehende Ware nutzen: Entweder über das Versandzentrum oder als Weiterführung des Auftrags in einen Lieferschein.

### Wareneingang

Sobald die bearbeiteten Waren von deinem Dienstleister zurückkommen, müssen die Produktion und die Bestellung abgeschlossen werden.

> **Anmerkung**
>
> Beachte, dass du einen der Vorgänge - Produktion oder Bestellung - ohne Warenbuchung abschließt, damit die Zubuchung ans Lager nicht doppelt erfolgt. Wir empfehlen, den Warenzugang über die Produktion zu erfassen und die Bestellung ohne Buchung abzuschließen.

#### Produktion abschließen

Öffne die Produktion und wechsele zum ReiterAbschluss. Klicke dort aufEinlagern + Produktion abschließen, um zum Abschlussdialog zu gelangen:

![ExtProduktion_Produktion_Abschluss.png](https://help.xentral.com/hc/article_attachments/19368079527708)

Buche den Zugang mit Klick aufKorrektur jetzt durchführen:

![ExtProduktion_Produktion_Abschluss_KorrekturDurchfuhren.png](https://help.xentral.com/hc/article_attachments/19368079529372)

#### Bestellung abschließen

Öffne die Bestellung und wähleBestellung abschließenim Aktionsmenü:

![ExtProduktion_BestellungAbschließen.png](https://help.xentral.com/hc/article_attachments/19368079530012)

Bestätige abschließend die Meldung:

![ExtProduktion_BestellungAbschließen_Bestatigen.png](https://help.xentral.com/hc/article_attachments/19368079531932)