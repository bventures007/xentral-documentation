Wenn du Pfand für bestimmte Artikel in deinen Aufträgen berücksichtigen musst, und du sicherstellen willst, dass nichts vergessen wird und der richtige Preis und Steuersatz angewendet wird, kannst du die Xentral Pfand Funktion verwenden.

Dies gilt insbesondere für Produkte wie Behälter oder Spezialverpackungen, die ein Pfandsystem erfordern z.B. Lebensmittel in Pfand Behältern oder Spezialverpackungen für Laborgeräte, bei denen die Auflistung der Pfand-Position im Lieferschein oder Rückgabe der Verpackung gewünscht wird.

> **Tipp**
>
> **B2B Funktion**: Die automatische Pfandberechnung ist für die B2B Auftragsabwicklung in Xentral optimiert. Wenn Pfandpositionen in Xentral hinzugefügt werden, bleiben die Preise der pfandpflichtigen Artikel unverändert. Die Pfandposition wird dem Auftrag zusätzlich hinzugefügt. So kannst du in manuell angelegten Großaufträgen, die evtl. später auch per EDI weiterverarbeitet werden, das Pfand automatisch einfügen lassen.

> **Anmerkung**
>
> Für Aufträge, die von einem B2C Kanal z.B. Onlineshop importiert werden, kannst du die Pfandartikel aus dem Shop bereits in Xentral übernehmen lassen. So stellst du sicher, dass für Endverbraucher mit bereits vollständig bezahlten Bestellungen der Auftragswert bereits im Shop berechnet wird und bestehen bleibt. Du benötigst in diesem Fall die Pfandfunktion in Xentral nicht.
>
> **Voraussetzung** für die Nutzung der Funktion ist, dass die Artikelnummer vom Shop im Xentral Standard wie ein normaler Artikel mit übernommen wird. Spezielle Artikelkonfigurationen im Shop und Abgleiche zu Drittsystemen (ausserhalb des Xentral Shop- und Marktplatz Standards) und deren Synchronisation fallen in denAdvanced Bereich. Beachte, dass du hierfür die entsprechenden Schnittstellen oder IT-Unterstützung von deinem Partner benötigst.
>
> **Tip für die Verwendung B2B und B2C** (Die Xentral Pfandfunktion für manuelle Aufträge und Pfandartikel im Onlineshop): Für den Pfandartikel (Shopimport) solltest du im Artikelstamm einen separaten Artikel anlegen, der nicht in der Xentral Pfandfunktion hinterlegt ist. So stellst du sicher, dass bei der manuellen Bearbeitung von Shop-Aufträgen durch dein Team keine Pfadberechnung mehr in Xentral stattfindet.

## Automatische Integration von Pfandartikeln in Aufträge

Die Pfand Funktion ermöglicht dir eine automatisierte Einbindung zusätzlicher Pfandartikel in bestehende Aufträge. Diese Funktion erkennt selbstständig, wenn ein Artikel, der einem Pfand unterliegt, zu einem Auftrag hinzugefügt wird, und fügt entsprechend die erforderlichen Pfandartikel dem Auftrag hinzu.

> **Tipp**
>
> Diese Automatisierung optimiert deinen Workflow, reduziert manuelle Eingriffe für dich und dein Team und minimiert Fehlerquellen bei der Erfassung von Pfandartikeln.

## Konfigurierbare Pfandartikel-Zuweisung pro Produkt

Du hast die Möglichkeit, spezifische Zuordnungsregeln für Pfandartikel auf Basis einzelner Produkte zu definieren:

- Du kannst festlegen, welcher Pfandartikel einem bestimmten Produkt zugeordnet ist.
- Die Menge des Pfandartikels kann frei definiert werden und wird automatisch angepasst, basierend auf der bestellten Menge des Hauptprodukts.
- Die Pfand Position kannst du unter dem Artikel oder alle Pfandartikel als gebündelten Block anzeigen lassen.

> **Anmerkung**
>
> Beispielsweise kannst du für eine Verpackungseinheit z.B. Stückliste eines Produkts festlegen, dass automatisch eine höhere Anzahl an Pfandartikeln dem Auftrag zugebucht wird. Diese flexible Konfiguration ermöglicht eine präzise und bedarfsgerechte Abwicklung von Pfandartikeln, die sich nach den spezifischen Anforderungen des Unternehmens richtet.

### Achtung

Die beschriebenen Funktionalitäten zur automatischen Integration von Pfandartikeln in Aufträge sowie die konfigurierbare Pfandartikel-Zuweisung pro Produkt sind für dich automatisch in der Xentral Pro-Version enthalten.

### Workflow Beispiele

Für jeden Artikel kannst du eine spezifische Artikelnummer für den zugehörigen Pfandartikel in einem festgelegten Freifeld in der App hinterlegen. Zum Beispiel, wenn im Freifeld 39 der passende Pfandartikel eingetragen wird. Zusätzlich gibt es die Möglichkeit, in einem weiteren Freifeld (z.B. Freifeld 38) die Anzahl anzugeben, wie oft der Pfandartikel hinzugefügt werden soll – ideal, wenn du zum Beispiel eine Kiste hast und definieren möchtest, dass der Artikel sechsmal hinzugefügt wird.

Es ist wichtig zu beachten, dass die Kombination aus Träger und Flaschen mit Pfand in der klassischen Getränkebranche nicht unterstützt wird.

Eine neue Option in unserer Pfand-App erlaubt es dir, global einzustellen, ob das Pfand direkt unter den hinzugefügten Positionen, wie zum Beispiel bei einer Bierbank und deren Pfand, aufgelistet oder am Ende des Auftrags aufsummiert und als Liste dargestellt werden soll. Beim Einfügen wird der Name des Pfandartikels sowie der Verkaufspreis automatisch aus dem Zentralsystem übernommen, wobei auch Staffelpreise berücksichtigt werden können.

Diese Funktionalitäten sind darauf ausgerichtet, die Verwaltung von Pfandartikeln in deinem ERP-System zu vereinfachen und zu automatisieren, wodurch du Zeit sparst und Fehler vermeidest.

### Integration und Verwaltung von Pfandartikeln

Die Funktion '**Pfandartikel **' findest du über ** Einstellungen > Lager & Logistik > Logistik > Pfandartikel **. Alternativ kannst du über die Smart-Suche '** Pfandartikel**' eingeben.

#### Schritt 1: Anlegen von Pfandartikeln

1. **Stammdatenpflege **: Starte mit dem Anlegen der Pfandartikel in den Stammdaten. Jeder Pfandartikel wird als echter Artikel angelegt, um eine eindeutige Identifikation und separate Einstellung der Artikeleigenschaften zu gewährleisten. Du kannst z.B. die Bezeichnung des Pfand-** Artikels** allgemein halten oder spezifisch auf den zugeordneten Artikel anpassen. Auch den Steuersatz kannst du natürlich im Pfand-Artikel individuell frei wählen.
1. **Pfandartikel-Kennzeichnung (Xentral Freifelder)**: Bestimme ein Freifeld in den Artikel Einstellungen, das für die Verlinkung des Pfandartikels zu deinem Hauptartikel verwendet wird. In diesem Freifeld wird die Artikelnummer des Pfandartikels hinterlegt. Definiere ein Freifeld, das du aktuell noch nicht in Verwendung hast z.B. Freifeld 38.
1. **Pfandartikel-Menge (Xentral Freifelder)**: Bestimme ein weiteres Freifeld in den Artikel Einstellungen, das für die Menge des Pfandartikels zu deinem Hauptartikel verwendet wird. In diesem Freifeld wird die Stückzahl des Pfandartikels hinterlegt. Definiere ein Freifeld, das du aktuell noch nicht in Verwendung hast z.B. Freifeld 39.

![2823913603](https://help.xentral.com/hc/article_attachments/13364163931548)

#### Schritt 2: Einstellung in der Pfand App (= Xentral Pfandartikel)

1. **Aktiv **: Setze das Häkchen für ** Aktiv **um die Pfand-App zu aktivieren. Klicke auf ** Speichern**.
1. **Pfand-Artikel Positionierung **: Lege fest, ob die Positionierung des Pfandartikels jeweils unter deinem zugehörigen Hauptartikel oder als Block in einer Liste ausgegeben werden soll: ** Pfand immer ans Ende des Auftrags **: Bündelt alle Pfandartikel am Ende der Positionstabelle. ** Pfandartikel nach jeder Position hinzufügen**: Fügt jeden Pfandartikel unter den jeweils zugehörigen Hauptartikel ein.

1. **Pfandartikel-Zuweisung (Xentral Feifelder)**: Stelle die oben ausgewählten Freifelder ein und weise sie der Pfand App zu: ** Freifeld für Pfandartikel pro Artikel **: Das Freifeld im Artikel, in das du in deinem Haupt-Artikel die Verlinkung zu deinem Pfand-Artikel eintragen kannst. ** Freifeld für Anzahl pro Pfand Artikel für Hauptartikel**: Das Freifeld, in das du die Menge/ Stückzahl in deinem Haupt-Artikel einträgst, mit der der Pfand-Artikel im Auftrag eingefügt werden soll.

![image-20240403-084449.png](https://help.xentral.com/hc/article_attachments/13364149667356)

![image-20240403-093332.png](https://help.xentral.com/hc/article_attachments/13364169143324)

In diesem Beispiel ist der Pfandartikel PFAND-17-1 aus Freifeld 1 dem Haupt-Artikel Schraube zugewiesen.

#### Schritt 3: Verknüpfung von Pfandartikeln

1. **Artikelverwaltung**: Bei der Artikelanlage oder -bearbeitung kannst du einem Hauptartikel einen Pfandartikel zuweisen, indem du die Artikelnummer des Pfandartikels im zuvor definierten Freifeld einträgst.
1. **Mengenangabe**: Die Menge, wie oft ein Pfandartikel hinzugefügt werden soll (z.B. bei Verpackungseinheiten), trägst du im zweiten zuvor definierten Freifeld ein.

#### Schritt 4: Auftragsbearbeitung

1. **Automatische Integration**: Beim Hinzufügen eines Hauptartikels zu einem Auftrag liest das System automatisch die im Freifeld hinterlegte Artikelnummer des Pfandartikels und integriert diesen in den Auftrag.
1. **Mengenanpassung**: Die App fügt den Pfandartikel entsprechend der angegebenen Menge zum Auftrag hinzu. Bei Verpackungseinheiten wird der Pfandartikel somit in der korrekten Anzahl berücksichtigt.

#### Schritt 5: Konsolidierung von Pfandartikeln

Wenn weitere Hauptartikel zum Auftrag hinzugefügt werden, die denselben Pfandartikel nutzen:

1. **Mengenaktualisierung**: Das System erhöht automatisch nur die Menge des bereits eingefügten Pfandartikels im Auftrag.
1. **Vermeidung von Duplikaten **: Es wird keine separate Position für denselben Pfandartikel angelegt. Stattdessen reflektiert die angepasste Menge im Auftrag die Gesamtzahl aller erforderlichen Pfandartikel. ** Voraussetzung**: die Pfand-Artikel werden am Ende des Auftrags als Block dargestellt.

## Alternativen - Artikel händisch einpflegen oder Pfand-Artikel in Stücklisten einfügen

### Pfand Artikel manuell anlegen und in einen Auftrag einfügen

Wenn du selten Pfandartikel verwendest und nur eine einzelne Position einfügen möchtest, kannst du einen Artikel natürlich auch im Artikelstamm anlegen und als Pfandartikel benennen. Diesen Artikel fügst du manuell in einen Auftrag ein. Der Artikel wird behandelt wie ein normaler Lagerartikel oder Dienstleistungsartikel.

### Pfand Artikel in eine Stückliste einfügen

Wenn ein Pfandartikel ein fester Bestandteil eines Produktes ist, kannst du den Artikel auch fest in der Stückliste hinterlegen. Dies gilt ebenso für andere Komponenten, die zu deinem Verkaufs-Set gehören.

**Beispiel für eine Just-in-time Stückliste**:

Du verkaufst Getränke in Pfandflaschen. Damit direkt Pfand mit aus dem Lager ausgebucht und zurückgegeben werden kann, musst du die Flasche wie folgt anlegen:

Du legst eine Wasserflasche inkl. Pfand an und setzt folgende Einstellungen: Markierung des Artikels als JIT Stückliste, Auswahl: kein Lagerartikel

- Wasserflasche: Bestandsgeführter Artikel (Markierung Lagerartikel), Bestandteil der Stückliste
- Pfand: Bestandsgeführter Artikel (Markierung Lagerartikel), Bestandteil der Stückliste

Nun kannst du in einen Auftrag den Artikel "Wasserflasche inkl. Pfand" einfügen. Wird das Pfand zurückgegeben, kannst du es entweder manuell ein buchen oder beispielsweise über die Stornofunktion in der POS Bestand einlagern.