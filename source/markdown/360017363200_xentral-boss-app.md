Mit der XentralBoss App kannst du dir schnell ein Überblick über die wichtigsten Kennzahlen und Eintwicklungen deines Unternehmens verschaffen. Die App richtet sich an Geschäftsführer und weitere Entscheidungsträger.

> **Anmerkung**
>
> Die App ist sowohl für iOS als auch für Android verfügbar.
>
> - Hier geht's zum kostenlosen Download im Google Play Store
> - Hier geht's zum kostenlosen Download im App Store

## Einrichtung

Im ersten Schritt wählst du aus, ob Daten von XentralHome oder Demo-Daten verwendet werden sollen. Letzteres ist dann sinnvoll, wenn noch kein XentralAccount vorhanden ist und du dir erst einmal ein Überblick verschaffen möchtest, welche Funktionen es in der App gibt.

Im nächsten Schritt werden Namen und Passwort abgefragt. Außerdem nimmst du Datenschutzeinstellungen vor. Wenn du angibst, dass die Daten aus einer aktiven XentralInstanz verwendet werden sollen, dann müssen diese noch mit der App synchronisiert werden, indem ein QR-Code in Xentral gescannt wird.

Dem QR-Code kannst du in Xentral anzeigen, indem du die folgenden Schritte durchführst:

1. Logge dich in Xentral ein.
1. Klicke oben rechts auf dein **Benutzer-Symbol**.
1. Klicke auf **Kontoeinstellungen**.
1. Öffne den Menüpunkt **Personal settings (old)**.
1. Klicke im Bereich **Mobile Apps ** auf **Zugang anlegen**.

## Allgemein

DieXentralBoss App verfügt über vier Tabs.

- [Home](#UUID-af321fe8-52bd-4df7-ddb9-a08770473223_id_360017363200_id_toc-2)
- [Finanzen](#UUID-af321fe8-52bd-4df7-ddb9-a08770473223_id_360017363200_id_toc-3)
- [Belege](#UUID-af321fe8-52bd-4df7-ddb9-a08770473223_id_360017363200_id_toc-4)
- [Einstellungen](#UUID-af321fe8-52bd-4df7-ddb9-a08770473223_id_360017363200_id_h_01EZQ9GM9BHCPAJCEEXBAAYFKJ)

### Home-Tab

Im Home-Tab erscheinen die wichtigsten Kennzahlen auf einen Blick.

![boss_home.png](https://help.xentral.com/hc/article_attachments/11332547914908)

Der Umsatzgraph in der oberen Hälfte des ersten Tabs zeigt den Umsatz der letzten 14 Tage, für die letzten 14 Wochen, für die letzten 12 Monate, oder für die letzten 10 Jahre an. Der Umsatz wird hierbei gebildet aus allen Rechnungen, abzüglich der Gutschriften für die jeweilige Periode, deren Status ungleich “angelegt” ist. Auf dem Graphen sind Kreise, welche den Tag sowie den Umsatz anzeigen, wenn darauf geklickt wird.

In der unteren Hälfte des Tabs befinden sich vier Kacheln:

- Die Kachel **Aufträge** zeigt die Anzahl aller Aufträge mit dem heutigen Datum.
- Die Kachel **Umsatz heute** zeigt die Summe des Netto-Umsatzes aller Rechnungen für den aktuellen Tag, bei denen der Status ungleich “angelegt” ist.
- Die Kachel **Pakete** zeigt die Anzahl der Einträge in der Versandtabelle am aktuellen Tag.
- Die Kachel **Aufträge heute** zeigt die Summe des Gesamtsumme-Feldes aller Aufträge für den aktuellen Tag, bei denen der Status ungleich “angelegt” ist.

### Finanz-Tab

Im zweiten Tab befinden sich die wichtigsten Finanzkennzahlen wie z.B. Umsätze, Verbindlichkeiten, Bankkontostand.

![boss_finance.png](https://help.xentral.com/hc/article_attachments/11332547965980)

- **Umsatz aktueller Monat (netto)**: Die Kachel zeigt die Summe des Felds ** umsatz_netto **aller Rechnungen für den aktuellen Monat abzüglich des Felds ** umsatz_netto** aller Gutschriften des aktuellen Monats an. Es werden nur Rechnungen und Gutschriften berücksichtigt, deren Status ungleich “angelegt” ist.
- **Umsatz letzter Monat (netto)**: Die Kachel zeigt die Summe des Felds ** umsatz_netto **aller Rechnungen für den letzten Monat abzüglich des Felds ** umsatz_netto** aller Gutschriften, des letzten Monats an. Es werden nur Rechnungen und Gutschriften berücksichtigt, deren Status ungleich “angelegt” ist.
- **Umsatz vorletzter Monat (netto)**: Die Kachel zeigt die Summe des Felds ** umsatz_netto **aller Rechnungen für den vorletzten Monat abzüglich des Felds ** umsatz_netto** aller Gutschriften, des vorletzten Monats an. Es werden nur Rechnungen und Gutschriften berücksichtigt, deren Status ungleich “angelegt” ist.
- **Offene Verbindlichkeiten (brutto)**: Die Kachel zeigt die Summe des Felds ** betrag** aller Verbindlichkeiten, deren Status nicht “bezahlt” oder “storniert” ist.
- **Offene Aufträge (netto)**: Die Kachel zeigt alle Auftragspositionen, bei welchen die gewünschte Liefermenge noch nicht erreicht wurde oder der Zustand “geliefert” noch nicht erreicht wurde und der zugehörige Auftrag weder den Status “abgeschlossen”, “storniert” oder “angelegt” hat. Dabei wird die Summe aller Auftragspositionen mit mit ihren Preisen multipliziert, unter Berücksichtigung etwaiger Rabatte.
- **Mahnwesen (brutto)**: Die Kachel zeigt die Summe der Differenzen von Soll- und Ist-Wert aller Rechnungen für Projekte in denen das Mahnwesen aktiviert ist an. Zusätzlich müssen die Rechnungen über die Information ** offen **im Feld ** Zahlungsstatus **verfügen. Das Feld ** Mahnwesen **darf nicht den Wert ** forderungsverlust **haben. Die Felder ** Belegnummer **und ** Mahnwesen **müssen jeweils einen Wert enthalten. Das Feld ** Mahnwesen_gesperrt**hat den Wert ** 0** und das Feld ** Mahnwesenfestsetzen** ist nicht gleich 1. Im Ergebnis werden alle ausstehende Forderungen angezeigt, die noch nicht abgeschrieben wurden.
- **Zeit gebucht**: Die Kachel zeigt die Summe aller Einträge in der Zeiterfassung für den aktuellen Monat in Stunden an.
- **Abolauf nächster Monat (brutto)**: Die Kachel zeigt den Betrag des für den nächsten Monat geplanten Abolaufs an (Summe aus den Tabs ** Rechnungen **und ** Aufträge **im Modul ** Abolauf**.
- **Bankkonten gesamt **: Die Kachel zeigt das gesamte Guthaben auf den Bankkonten an, die du im Modul ** Geschäftskonten** hinterlegt hast.
- **Gesamtumsatz laufendes Jahr (netto)**: Die Kachel zeigt die Summe des Felds ** umsatz_netto **aller Rechnungen für das aktuelle Jahr abzüglich des Felds ** umsatz_netto** aller Gutschriften des aktuellen Jahres an. Es werden nur Rechnungen und Gutschriften berücksichtigt, deren Status ungleich “angelegt” ist.

### Belege-Tab

In diesem Tab werden die Belegarten Angebote, Aufträge, Rechnungen, Lieferscheine und Gutschriften als Kacheln dargestellt. Wenn du auf eine dieser Kacheln tippst, werden die einzelnen Belege der Belegart mit Datum, Nummer, Name, Status und Betrag angezeigt. Auf diese einzelnen Aufträge kannst du wiederum tippen, um den einzelnen Beleg aufzurufen. Hier werden noch detailliertere Informationen angezeigt, wie beispielsweise die Adresse des Namens, die Versandart, die Zahlungsart, die enthaltenen Artikel, die Auftragsampel und das Auftragsprotokoll.

### Einstellungs-Tab

In den Einstellungen kannst du beispielsweise die Anmelde-PIN sowie deinen Namen ändern. Schau dir die folgende Tabelle an, um genauere Informationen zu den möglichen Aktionen im Tab **Einstellungen** zu erhalten.

| Bereich | Mögliche Aktionen |
| --- | --- |
| **Allgemeine Einstellungen **| Tippe auf das ** Stift-Symbol**, um die PIN zu ändern, mit der du dich in der Xentral Boss App anmeldest. |
| **Personalisierung **| Tippe auf das ** Stift-Symbol**, um den Namen zu ändern, der in der Xentral Boss App angezeigt wird. |
| **Registrierung **| Tippe auf die entsprechende Option, um bei Bedarf die ** Registrierung neu durchführen **, um die App (erneut) mit deiner oder einer anderen Xentral Instanz zu verbinden. Wenn du auf ** Auf Werkseinstellungen zurücksetzen **tippst, wird die Verbindung zur aktuellen Xentral Instanz aufgehoben und deine PIN entfernt. Mithilfe der Option ** Registrierung löschen** hebst du lediglich die aktuelle Verbindung zu einer Instanz auf. |
| **Support** | Hier findest du verschiedene Möglichkeiten, um entweder per E-Mail oder im Xentral Helpcenter Unterstützung für die Einrichtung und Benutzung der App zu erhalten. Außerdem kannst du hier die aktuell verwendete App-Version sowie die Build-Nummer einsehen. |
| **Rechtliche Hinweise **| In diesem Bereich kannst du bei Bedarf das ** Impressum **, die ** Allgemeinen Geschäftsbedingungen **, die ** Leistungsbeschreibung **und die ** Datenschutzerklärung** einsehen. |
| **Datenschutz **| Hier kannst du über die Option ** Firebase Analytics & Performance** die Bereitstellung von statistischen Daten (de)aktivieren. |

## Troubleshooting

### Servereinstellungen

Für die Verbindung zur XentralREST-API muss eine Weiterleitung des Authorization Headers von Apache zu PHP konfiguriert werden. Hierzu müssen folgende Zeilen in der PHP-FPM-Konfigurationsdatei eingefügt werden:

```
<IfModule setenvif_module>
SetEnvIfNoCase ^Authorization$ "(.+)" HTTP_AUTHORIZATION=$1
</IfModule>
```

Ohne diese Einstellung ist die PHP-Variable $_SERVER['HTTP_AUTHORIZATION'] nicht gesetzt. Es gibt auf PHP-Seite auch keine andere Möglichkeit, die die Login-Daten zu erreichen. Auf PHP-Seite sieht es also immer so aus, als ob kein Login stattgefunden hat (Fehler 7411).

Xentral stellt ein Testskript zur Verfügung, welches auf dem eigenen Server die korrekte Weiterleitung des Authorization Headers überprüft. Das Testskript findet sich im GitHub-Downloadbereich von Xentral. Die Datei heißt **authtest.php**.

Anleitung für den Test mit dem Testskript:

1. Lege die Datei an einem Platz innerhalb des Xentral-Verzeichnisses www ab. Der genaue Speicherort ist nicht relevant. Der Dateiname ist ebenfalls nicht relevant, die Datei muss nur über den Browser aufrufbar sein.
1. Rufe die Datei im Browser auf. Beim ersten Aufruf wird ein Eingabefeld für die Zugangsdate angezeigt. Gib hier beliebige Zugangsdaten ein. Jegliche Daten werden akzeptiert.
1. Bei korrekter Webserver-Konfiguration wird die Erfolgsmeldung "Authorisation-Header vorhanden" angezeigt. Bei fehlerhafter Konfiguration wird immer wieder das Login-Fenster angezeigt. Anschließend kannst du einfach auf **Abbrechen** tippen.
1. Lösche die Datei nach Abschluss deiner Tests vom Server.

### Keine Belege ausgegeben und Netzwerk nicht erreichbar

In der XentralBoss App werden keinerlei Belege ausgegeben und durch einen Klick auf das "rote Antenne"-Icon wird deutlich, dass ein Netzwerkfehler vorliegt. Das kann daran liegen, dass fehlende Rechte in Xentral vorliegen. Dieses Problem wird gelöst, wenn die App über den QR-Code des Admin-Users verbunden ist.

Falls die App über den QR-Code des Admin-Users verbunden ist und der Admin auch eingeloggt ist, kann das Problem auch in den fehlenden Rechten für die Belege bei den API-Permissions liegen.

**Mögliche Lösung: Rechte-Vergabe für Belege**

Dazu ist in der SuperSearch nach API-Accounts zu suchen und das Modul zu öffnen. Dort sind die API-Accounts für die XentralBoss App aufzurufen. Wenn die API für die App aufgerufen wird, sind folgende Haken zu setzen:

![Bildschirmfoto_2021-02-23_um_13.57.14.png](https://help.xentral.com/hc/article_attachments/5041780330524)

Pro Beleg ist es ausreichend, die Rechte get und list zu aktivieren. Falls dies nicht funktioniert, setze alle Rechte für die Belegarten und probiere es erneut.

Falls andere Belegarten nicht angezeigt werden und der API-Account nur für die Boss App genutzt wird, müssen alle Rechte gesetzt werden. Weitere Belegarten, in denen die Rechte für die Belege gesetzt werden können, sind **delivery note **, ** quote ** und **supply orders**.

### Versanddienstleister nicht angegeben

In der XentralBoss App wird der Versanddienstleister in den Belegarten Auftrag und Lieferschein nicht angeben. Zudem erscheint unter Standardversand die falsche Adresse auf jedem Lieferschein bzw. es wird immer die Adresse "Fuggerstraße 11, 86150 Augsburg" angegeben.