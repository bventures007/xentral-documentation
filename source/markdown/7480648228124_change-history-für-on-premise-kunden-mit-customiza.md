> **Anmerkung**
>
> Diese Informationen sind nur für Kunden mit einer On-Premise-Instanz relevant.

Die Änderungshistorie in diesem Artikel listet alle Änderungen der XentralUmgebung auf, die ausschließlich für Kunden mit kundenspezifischen Änderungen (Customizations) in On-Premise Instanzen relevant sind.

## Custom code related changes

We are heavily restructuring the ErpAPI class. If you depend on this class in your custom code you need to check if your code is still compatible.

### Patch Version 23.0.10 **class.erpapi.php**

The following methods and functions have been removed from `www/lib/class.erpapi.php`:

- AnzahlOffeneAufgaben
- ArtikelAnzahlLagerPlatzMitSperre
- CheckBuchhaltung
- unicode_decode
- AdresseAlsAnsprechpartner
- formatmenulink
- ArtikelMindestlager
- GetWaage
- CheckUSTFormat
- isMailAdr
- filterMailAdr
- EndeMessung
- uniqueTimeStamp
- GetWartezeitTicket
- makeDifferenz
- makeString
- GetVerrechnungskontenReisekosten
- IsAdresseInGruppe
- CopyProjektDaten
- Wochenplan
- checkCell
- get_time_difference

## www folder related changes

We are heavily restructuring the `www/pages` folder and others. If you have custom pages and therefore hesitate to update, please let us know.

### Patch Version 23.0.10 **www/pages**

- We have moved all files from the `www/pages/_gen ` folder to the`www/pages/content` folder. This might affect custom code.
- We are applying consistent code formatting (PHP-CS-fixer rules) to all files in the `www/pages` folder. This probably doesn't have any impact for you.

**www/widgets**

We are in the process of unifying the files in `www/widgets/_gen` with files in `www/widgets`.