Barcode-Scanner sind ein zentrales Hilfsmittel, um Prozesse in Lager, Versand und Logistik effizient und fehlerfrei abzuwickeln. Sie ermöglichen eine schnelle Identifikation von Artikeln, Aufträgen oder Sendungen und reduzieren manuelle Eingabefehler.

## Einsatzgebiete von Barcode-Scannern

- **Versand & Packtisch**: Scannen von Lieferscheinen, Artikeln oder Kisten zur automatisierten Verarbeitung. Scan von Seriennummern und Chargen.
- **Lagerprozesse**: Beim Kommissionieren oder Umlagern sorgen Barcodescanner für eine klare Zuweisung von Artikeln zu Lagerplätzen.
- **Wareneingang**: Artikel und Lieferungen lassen sich schnell erfassen und mit Bestellungen abgleichen. Mit GS1 können auch ganze Paletten gescannt werden.
- **Retourenabwicklung**: Rücksendungen können effizient den richtigen Aufträgen und Kunden zugeordnet werden.
- **POS (Point of Sale)**: Direktes Scannen von Artikeln an der Kasse für eine schnelle und fehlerfreie Abwicklung von Verkäufen.

## Best Practices für die Verwendung

Damit Barcode-Scanner reibungslos in Xentral eingesetzt werden können, sollten einige Grundregeln beachtet werden:

- **Artikelnummern standardisieren**: Nur Ziffern und Großbuchstaben verwenden, keine Leerzeichen oder Sonderzeichen. Statt Leerzeichen besser Bindestriche (-) oder Unterstriche (_) nutzen.
- **Den richtigen Barcodetyp wählen**: Code128 oder QR-Code für komplexere Daten oder Sonderzeichen. Code39 für Buchstaben/Zahlen mit begrenzten Sonderzeichen.
- **Scanner-Einstellungen prüfen**: Viele Scanner können zwischen Eingabemodi wie Keyboard Emulation (HID) und Serial/COM-Port umgestellt werden. Auch das Tastaturlayout (DE vs. EN) spielt eine Rolle, z. B. bei vertauschten Z/Y-Eingaben.
- **Fremdnummern einsetzen**: Shop-SKUs lassen sich im Shopimport auf Xentral-Artikelnummern mappen (Fremdnummern). So können auch externe Artikelnummern zuverlässig eingescannt werden.
- **Standardisierung im Betrieb**: Möglichst einheitliche Barcode-Standards im gesamten Unternehmen verwenden, um Komplexität und Fehlerquellen zu reduzieren.

## Maximale Zeichenzahl, Robustheit und unterstützte Formate bei Barcodetypen

- **Code128**: Kompakter und effizienter als Code39 (gleiche Daten: kürzerer Code). Unterstützt Prüfziffern, was die Fehlererkennung verbessert. Deutlich robuster bei längeren Codes im Vergleich zu Code39.
- **QR-Code**: Am robustesten durch eingebaute Fehlerkorrektur (ECC). Kann je nach ECC-Stufe bis zu 30 % beschädigt/verdeckt sein und wird trotzdem gelesen. Sehr gut bei schwierigen Umgebungen (Schmutz, Abnutzung, kleine Label).
- **Code39**: Einfacher Aufbau, aber relativ ineffizient (lange Codes = sehr breiter Barcode). Robust bei kurzen Codes, allerdings bei längeren Barcodes schwieriger lesbar. Fehleranfälliger als Code128, weil weniger „Redundanz“ in der Kodierung.
- **EAN/UPC**: Sehr weit verbreitet, aber nicht besonders robust. Feste Länge, einfache Struktur: wird gut gelesen, solange Druckqualität stimmt. Weniger tolerant bei Verschmutzung oder Teilabdeckung.

> **Tipp**
>
> **Praxisempfehlung:**
>
> - Für klassische Artikelnummern, Handelsware und interne Prozesse ist **Code128** die beste Wahl. Er ist kompakter als Code39, unterstützt den kompletten ASCII-Zeichensatz (inklusive Sonderzeichen) und eignet sich auch für längere Artikelnummern. Damit ist er ein sehr flexibler Standard, der von nahezu allen modernen Scannern unterstützt wird.
> - Für längere Inhalte, komplexe Daten oder mobile Anwendungen empfiehlt sich der **QR-Code**. Dank integrierter Fehlerkorrektur kann er auch dann noch gelesen werden, wenn Etiketten teilweise beschädigt oder verschmutzt sind. Zudem unterstützt er UTF-8, sodass auch Umlaute und Sonderzeichen problemlos darstellbar sind.
> - Sonderfall eher für Branchenstandards: Für einfache Artikelnummern und wenn maximale Kompatibilität mit älteren Scannern oder Systemvorgaben gefragt ist, eignet sich **Code39**. Er ist sehr robust bei kurzen Codes, allerdings weniger platzsparend und nur eingeschränkt für Sonderzeichen nutzbar.

## Typische Probleme und Lösungen bei Barcode-Scanner

- **Scanner liest bestimmte Zeichen nicht**: Viele Scanner unterstützen Sonderzeichen (&amp;, %, $,? etc.) nicht. Hier hilft die Nutzung von Code128 oder die Anpassung der Artikelnummern.
- **Vertauschte Eingaben (z ↔ y)**: Ursache ist meist ein falsches Tastaturlayout (EN statt DE). Lösung: Umstellen im Scanner-Handbuch per Konfigurations-Barcodes.
- **Scanner reagiert nicht**: Kabel- und Stromverbindungen prüfen. Bei Bluetooth-Modellen sicherstellen, dass der Scanner korrekt gekoppelt ist.