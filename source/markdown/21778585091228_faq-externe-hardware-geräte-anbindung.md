In dieser FAQ-Sektion finden sich Antworten auf häufige Fragen zur Anbindung und Verwendung externer Hardware wie Scanner, Drucker, MDE-Geräte und mobile Endgeräte.

## Warum erkennt mein Barcodescanner bestimmte Zeichen - wie Sonderzeichen oder Leerzeichen - nicht korrekt (z. B. „&“ oder Verwechslung von Z/Y)?

Die Lesbarkeit hängt sowohl von der verwendeten Hardware als auch vom gewählten Zeichensatz bzw. Barcodetyp ab. Viele Scanner haben Einschränkungen bei Sonderzeichen wie &amp;, %, $, /,, #, +, =,? oder bei Umlauten (ä, ö, ü). Auch Leerzeichen sollten vermieden werden, da sie von weiterführenden Prozessen in Xentral oder angebundenen Systemen als Ende der Artikelnummer interpretiert werden. Best Practice ist es daher, Leerzeichen durch Minuszeichen (-) oder Unterstriche (_) zu ersetzen und auf Sonderzeichen zu verzichten.

**Praxisbeispiel **: Wenn ein Scanner beim Scannen von Tracking-Nummern oder Artikeln Zeichen wie Z/Y vertauscht, liegt das meist an einer falschen Tastatur- oder Spracheinstellung (z. B. englisches Tastaturlayout). Die Umstellung erfolgt über spezielle Konfigurations-Barcodes, die im Handbuch des Geräts zu finden sind. ** Best Practices:**

-** Artikelnummern sauber pflegen**: Nur Ziffern und Großbuchstaben verwenden, keine Leerzeichen oder Sonderzeichen. Leerzeichen wenn nötig durch - oder _ ersetzen.
- **Barcodetyp passend wählen**: Für einfache Nummern eignen sich EAN/UPC oder Code39, für komplexere Nummern mit Sonderzeichen besser Code128 oder QR-Codes.
- **Scanner-Einstellungen prüfen**: Tastaturlayout und Eingabemodus (z. B. HID vs. COM-Port) anpassen, um Probleme mit Zeichen oder Z/Y-Verwechslungen zu vermeiden.
- **Fremdnummern nutzen**: Shop-SKUs können beim Import auf Xentral-Artikelnummern gemappt werden. So lassen sich auch externe Nummern zuverlässig scannen und verarbeiten.
- **Standardisierung im Betrieb **: Möglichst einheitliche Barcodetypen und Nummernformate im gesamten Prozess einsetzen, um Fehlerquellen zu reduzieren. ** Unterschiede bei Barcodetypen:**

| Barcodetyp | Unterstützte Zeichen | Besonderheiten |
| --- | --- | --- |
| Code39 | Ziffern, Großbuchstaben, einige Sonderzeichen (-,., $, /, +, %, Leerstelle) | Eingeschränkt, keine Kleinbuchstaben oder Umlaute |
| Code128 | Vollständiger ASCII-Satz (alle 128 Zeichen) | Flexibel, unterstützt Sonderzeichen |
| EAN/UPC | Nur Ziffern (0–9) | Standard im Handel, keine Buchstaben oder Sonderzeichen |
| QR-Code | Alphanumerisch, Sonderzeichen, UTF-8 | Sehr robust, unterstützt auch Umlaute und komplexe Daten |