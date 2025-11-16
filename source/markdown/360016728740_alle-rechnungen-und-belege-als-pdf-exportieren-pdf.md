Mit der Funktion PDF Archivierung in Xentral kannst du alle **Ausgangsrechnungen ** oder andere Belege **gesammelt als PDF-Dateien ** exportieren. Statt einzelne Dokumente manuell herunterzuladen, lassen sich **beliebige Belegarten ** für einen bestimmten Zeitraum in einer**ZIP-Datei bündeln** und bequem exportieren.

Damit eignet sich das Modul ideal, wenn du z. B. für die Buchhaltung alle Rechnungen eines Monats oder Jahres auf einmal benötigst. Die exportierten Dateien bleiben außerdem im Archiv gespeichert und können jederzeit erneut heruntergeladen werden.

> **Anmerkung**
>
> Mit dem Modul PDF Archivierung kannst du alle Belegarten für einen frei wählbaren Zeitraum gesammelt in einem Archiv ablegen und als ZIP-Datei exportieren. Die Belege werden dabei automatisch über den Prozessstarter **pdfarchiv_app** abgeholt, dessen Intervall individuell eingestellt werden kann (Administration → Einstellungen → System → Prozessstarter).

## Übersicht PDF Archivierung

In der Übersicht in dem Tab "Archivierung" sind alle PDF Dokumente aufgelistet, die archiviert wurden.

## Neue PDF Archivierung

1. Aktivierung des Prozessstarters (Administration → Einstellungen → System → Prozessstarter pdfarchiv_app).
1. PDF-Archivierung aufrufen.
1. Eine neue PDF Archivierung anlegen, Dokumente aus Datumsbereich auswählen (Haken setzen) und speichern.
1. Der Download wird nach Durchlaufen des Prozessstarters und der Archivierung der PDF Dokumente zum Download angezeigt.

Erst wenn das Download-Icon erscheint, ist der Prozess abgeschlossen, dies kann je nach Einstellungen im Prozessstarter und der Menge der zu erzeugenden Dokumente unterschiedlich lange dauern. Idealerweise kann der Cronjob auch immer außerhalb der Betriebszeiten durchlaufen. Für sofortige Bereitstellung der Daten muss der Cronjob dann in einer kürzeren Periode, z.B. alle 10 Minuten eingestellt werden.

Über "+Neu" lassen sich neue Archivierungsvorgänge für die Belegarten anlegen. Nach Fertigstellung wird die Datei als Download angezeigt und kann heruntergeladen werden.

## Sondereinstellungen

Mit Auswahl des Expertenmodus, können zusätzliche Einstellungen zu den Standardeinstellungen getroffen werden.

- Generiere noch nicht archivierte PDFs: Das ist die Standardeinstellung
- Alle PDF-Versionen: Wenn du diesen Haken setzt werden alle PDF-Versionen generiert
- Generiere alle Dokumente neu: Wenn du diesen Haken setzt werden alle Dokumente neu generiert
- PDFs in einzelne Tage bündeln: Bündelt die PDFs von einzelnen Tagen

## Was kann ich tun, wenn mein PDF-Archiv nicht ausgeführt wird?

Wenn dein PDF-Archiv (Smart-Search: PDF Archivierung) nicht startet oder keine Downloads erscheinen, gehe folgendermaßen vor:

1. Öffne das Modul **PDF Archivierung**.
1. Klicke auf **+ Neu**, um einen neuen Eintrag anzulegen.
1. Aktiviere den Haken bei **Expertenmodus **→** Experteneinstellungen**.
1. Setze den Haken bei **PDFs in einzelne Tage bündeln**.
1. Klicke auf **Speichern**.

Wichtig: Stelle sicher, dass der Prozessstarter **pdfarchiv_app** aktiviert ist.