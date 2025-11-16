> **Anmerkung**
>
> Diese Schnittstelle befindet sich in der Einführungsphase und steht allen Kunden auf Anfrage zur Verfügung. Wenn du vorzeitig Zugriff haben möchtest, wende dich gerne an deinen Solution Consultant.

## Überblick

Der neue CSV-Importer ermöglicht es, Datenbestände aus anderen Systemen in die XentralDatenbank einzufügen. Dazu müssen die Daten aus den Fremdsystemen als CSV-Datei exportiert bzw. in Excel aufbereitet und als CSV-Datei abgespeichert werden. Wenn du Unterstützung bei der Vorbereitung der Fremddaten benötigst, schau gerne in[diesen Artikel](https://help.xentral.com/hc/de/articles/360016758939#UUID-3c5b4c7a-6650-f55b-9943-edb0ed852574). Dort findest du Hilfestellung im Abschnitt **Tipps im Umgang mit Excel und CSV-Dateien**.

## Funktionsumfang des neuen CSV-Importers

Mit dem neuen CSV-Importer von Xentral kannst du auf einfache und übersichtliche Weise Daten aus CSV-Dateien in Xentral importieren. Der CSV-Importer bietet aktuell folgende Hauptfunktionen:

- [Artikeldaten importieren](https://help.xentral.com/hc/de/articles/19857384088348#UUID-361e9146-d218-1c27-1993-f17796604275)
- [Verkaufspreise importieren](https://help.xentral.com/hc/de/articles/19857336333980#UUID-d19c6535-89a2-e066-cf41-c0bc2ff8efa7): Du kannst zu bestehenden Artikeln Verkaufspreise (Standardpreise, kundenspezifische Preise, Gruppenpreise) importieren.
- [Einkaufspreise importieren](https://help.xentral.com/hc/de/articles/19857367677724#UUID-53c62d01-fd81-b842-8008-ecdc4aad2d86): Du kannst zu bestehenden Artikeln Einkaufspreise (Standardpreise, lieferantenspezifische Preise) importieren.
- [Medien importieren](https://help.xentral.com/hc/de/articles/19861120858140#UUID-bdf97c49-e951-e133-516e-9f043ff88d47)
- [Stückliste importieren](https://help.xentral.com/hc/de/articles/19860038849820#UUID-2feefb7c-6e23-1f25-4d7f-8073e55e535c)
- [Freifelder importieren](https://help.xentral.com/hc/de/articles/19859219300380#UUID-2e98b163-b74c-aaa2-d3d6-3e1a8ae34716)
- [Aufträge importieren](https://help.xentral.com/hc/de/articles/19984028262556#UUID-7dadf684-0e12-6fe4-b3e5-4b3e136bde97)
- [Kategorien importieren](https://help.xentral.com/hc/de/articles/20107585914140#UUID-77e86c5d-302f-ab14-c742-6863a3b2839d)
- [Daten über einen Custom-Workflow importieren](https://help.xentral.com/hc/de/articles/17467558830108#UUID-97d61bdb-1bde-b669-0b96-9dc4acd8cef0): Mit einem so genannten Custom-Workflow kannst du beliebige Daten importieren und individuell anpassen.

> **Anmerkung**
>
> Der Funktionsumfang des neuen CSV-Imports wird schrittweise erweitert. Zukünftige Versionen des CSV-Importers werden es ermöglichen, weitere Datentypen wie z. B. Kundendaten über einen Standardprozess zu importieren. Für solche Daten kannst du bis auf Weiteres die bekannte Import-/Exportzentrale weiterhin nutzen.

## CSV-Importer Übersicht

Du findest den CSV-Importer im Menü **Einstellungen > Administration > Datenaustausch > CSV-Importer**. Du befindest dich dann in der so genannten CSV-Importer Übersicht. Beim ersten Aufruf ist die Übersicht leer und dir steht nur die Funktion zum Erstellen eines neuen CSV-Imports zur Verfügung:

![CSV-Importer_NeuenImportErstellen.png](https://help.xentral.com/hc/article_attachments/18704795609244)

Nachdem du einen Import angelegt hast, wird er dir in der Übersicht angezeigt. Du kannst dort folgende Aktionen durchführen:

![CSV-ImporterUbersichtAktionsschaltflachen.png](https://help.xentral.com/hc/article_attachments/18704809707420)

(1) Durch Klick auf das Stift-Symbol öffnest du den Import in der Mapping-Vorschau.

(2) Die zweite Schaltfläche führt dich zum Reporting. Dort kannst du den Importstatus aller in diesem Import enthaltenen Datensätze verfolgen.

(3) Hinter der dritten Schaltfläche stehen folgende Funktionen zur Verfügung:

![CSV-ImporterUbersichtWeitereAktionen.png](https://help.xentral.com/hc/article_attachments/18704809710620)

- **Ursprüngliche Daten herunterladen**: Diese Funktion ermöglicht dir, die ursprünglichen Daten in einer CSV-Datei herunterzuladen.
- **Als Vorlage wiederverwenden**: Hiermit kannst du eine vorhandene Importvorlage duplizieren. Diese Funktion kannst du nutzen, um einen bestehenden Import mit einer neuen Datei noch einmal auszuführen. Sobald du diese Schaltfläche betätigst, gelangst du zu der Seite, auf der du eine CSV-Datei hochladen kannst. Das Mapping aus der kopierten Vorlage wird geladen. Du kannst es beibe-halten oder Anpassungen vornehmen. Sobald du die Mapping-Seite verlässt, steht dir die zusätzliche Importvorlage in der Übersicht zur Verfügung.
- **Import löschen**: Löscht die Importvorlage.