Wenn du täglich viele E-commece Bestellungen in dein Xentral importierst, kann es immer wieder passieren, dass du in der Logistik direkt am Packtisch oder im Paketmarken Stapeldruck ein Label nicht bekommen kannst, weil die Adressdaten falsch eingetragen worden sind.

Die Adressprüfung (= Adressvalidierung) prüft deine Auftragsadressen nach Standards und zeigt dir bereits vor der Übergabe an die Logistik die fehlerhaften Adressen in der Auftragsübersicht als Ampelsymbol an.

**Folgende Funktionen stehen dir zur Verfügung:**

- Automatische Prüfung der Standards für eine richtige Adresse, so dass dein Team in der Logistik keine Zeit mehr verliert.
- Anzeige fehlgeschlagener Prüfungen in der Auftragsübersicht als Auftragsampel ‘orange’. Zusätzlich erhältst du im Auftrag das Ergebnis der Prüfung, um die Adresse zu korrigieren.
- Freigabe Option einer Adresse - trotz fehlgeschlagener Prüfung.
- Expertenmodus zur technischen individuellen Erweiterung der Adressvalidierung und der Validierungsregeln.

## Standard Regeln der Adressprüfung

Folgende Standards werden geprüft:

- Hausnummer muss vorhanden sein und zusätzlich neben der Nummer ein Text für die Straße.
- Liefer Postleitzahl muss eine 4,5-stellige Nummer sein (Deutschland und Österreich).
- Packstation, Postfiliale oder Paketshop müssen in den entsprechenden Feldern stehen und ebenso eine 6-10-stellige Nummer für z.B. Packstation eingegeben sein.

## Adressvalidierung aktivieren

Die Adressvalidierung (= Adressprüfung) findest du über **Einstellungen > Lager & Logistik > Logistik > Adressvalidierung **. Alternativ kannst du über die ** Smart-Suche >****Adressvalidierung** eingeben.

1. Setze das Häkchen für ‘**Aktiv**'.
1. Setze das Häkchen für ‘**Adressvalidierung in Adresse deaktivieren **’ und wähle ein ‘** Freifeld für Deaktivierung’** aus. Definiere dieses [Freifeld](https://help.xentral.com/hc/de/articles/360017612120-Freifelder) als Checkbox, so dass du später in einer Adresse für die manuelle Freigabe ein Häkchen setzen kannst.
1. Klicke auf ‘**Speichern’**.

![image-20240604-152942.png](https://help.xentral.com/hc/article_attachments/14307327002268)

### Adressvalidierung nur für bestimmte Verkaufskanäle aktivieren

- Ist in der Aktivierung für Projekte kein Projekt hinterlegt, so greift die Adressprüfung für alle Verkaufskanäle/ Logistikkanäle (= Projekte).
- Ist ein Projekt eingetragen, so greift die Adressvalidierung nur noch für dieses Projekt und jedes später hinzugefügte Projekt in dieser Liste.

Ein Projekt kannst du über ‘**Neuer Eintrag**’ hinzufügen und über X löschen.

## Adressprüfung (Workflow)

Die Funktion Adressvalidierung wird in der Auftragsübersicht mit folgendem Ampel-Symbol angezeigt:![image-20240604-160910.png](https://help.xentral.com/hc/article_attachments/14307327018524)

![image-20240604-160824.png](https://help.xentral.com/hc/article_attachments/14307327028252)

. Hier kannst du sofort sehen, welche Aufträge noch eine Korrektur der Adresse benötigen.

### Adressprüfung erfolgreich

![image-20240604-160910.png](https://help.xentral.com/hc/article_attachments/14307327018524)

grünes Ampel-Symbol: erfolgreiche Adressprüfung, der Auftrag wird für die Adressvalidierung für die Logistik freigegeben.

> **Tipp**
>
> Der Auftrag wird im gewohnten Logistikworkflow abgearbeitet.

### Adressprüfung fehlgeschlagen

![image-20240604-160824.png](https://help.xentral.com/hc/article_attachments/14307327028252)

oranges Ampel-Symbol: fehlgeschlagene Adressprüfung, der Auftrag wird nicht automatisch an die Logistik übergeben.

> **Warnung**
>
> Der Auftrag wird für die Logistik/ Versandprozess blockiert und erfordert eine Korrektur der Adressdaten (oder eine manuelle Freigabe über die Kundenadresse).

### Adressprüfung im Auftrag (Fehlermeldung)

Bei fehlgeschlagener Adressprüfung erhältst du im Auftrag eine Fehlermeldung, die dir anzeigt, welche Prüfung nicht erfolgreich war. Du kannst die Adresse nachbearbeiten und ‘speichern’, um die Ampel auf grün zu schalten z.B. indem du die Packstation-Nummer hinzufügst.

> **Anmerkung**
>
> Beachte, dass für den Paketmarkendruck die Lieferadresse ausschlaggebend ist. Sofern dein Kunde nur eine Adresse angegeben hat, kannst du die Allgemeine Adresse bearbeiten. Bei abweichender Lieferadresse bearbeitest du die Lieferadresse.

![image-20240430-063227.png](https://help.xentral.com/hc/article_attachments/14307327088796)

### Validierung in der Adresse abschalten

Die Validierung für eine Adresse kannst du auch deaktivieren, indem du im Auftrag auf die Kundennummer klickst und die Adresse über deine Freifeldeingabe s.o. manuell validierst.

![image-20240604-163329.png](https://help.xentral.com/hc/article_attachments/14307232159004)

### Mögliche Fehler und Fehlermeldungen

| | |
| - | - |
| | |

## Expertenmodus zur Anpassung der Validierungsregeln

Im Expertenmodus kannst du die Regeln für die Adressprüfung individuelle erweitern oder anpassen. Du kannst z.B. weitere Länder hinzufügen oder die Bedingungen für Paketshops anderer Dienstleister erweitern.

> **Anmerkung**
>
> Diese Einstellung setzt eine entsprechende technische Schnittstellenkenntnis voraus oder ggf. eine Konfiguration. Möglicherweise benötigst du bei dieser Einstellung technische Unterstützung im Setup deines Workflows und/oder Konfigurationsunterstützung in der Einstellung der Workflows, Versandregeln und Validierungsregeln.

> **Anmerkung**
>
> **Adressvalidierung ist ungültig**:
>
> wenn
>
> - Liefername = “herr” oder “frau”
>
> oder
>
> wenn Lieferland = “DE” order “AT” und:
>
> - Liefer-PLZ nicht 4 oder 5 stellige Nummern
> - oder Lieferstraße enthält nur Ziffern
> - oder Lieferadresse enthält keine Ziffern
> - oder Liefer-Adresszusatz enthält eine 6 bis 10 stellige Nummer
> - und Lieferstrasse enthält NICHT: Packstation, Postfiliale, Paketshop oder DHL
> - oder Liefer-Adresszusatz enthält DHL
> - oder Liefer-Adresszusatz enthält Post
> - oder Liefer-Adresszusatz enthält Postnummer
> - oder Liefer-Adresszusatz enthält Paketshop
> - oder Liefer-Adresszusatz enthält Postfiliale
> - oder Liefer-Adresszusatz enthält Packstation
> - oder Liefer-Adresszusatz endet nicht mit einer 6-10 stelligen Zahl
>
> und
>
> - Liefer-Straße enthält DHL
> - oder Liefer-Straße enthält Post
> - oder Liefer-Straße enthält Postnummer
> - oder Liefer-Straße enthält Paketshop
> - oder Liefer-Straße enthält Postfiliale
> - oder Liefer-Straße enthält Packstation

![image-20240604-145908.png](https://help.xentral.com/hc/article_attachments/14307295961628)