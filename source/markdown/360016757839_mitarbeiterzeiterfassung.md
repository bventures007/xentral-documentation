Das Modul “Stechuhr” ermöglicht deinen Mitarbeitern die Erfassung ihrer Arbeitszeit. Die Oberfläche der Stechuhr steht direkt in der Xentral-Instanz zur Verfügung und stellt zum Beispiel für Büroangestellte und Remote-Worker eine gute Möglichkeit dar, ihre Arbeitszeit zu registrieren.Manche unserer Kunden möchten ihren Mitarbeitern darüberhinaus auch ermöglichen ihr Kommen und Gehen mittels eines RFID-Chips in der Stechuhr zu registrieren, ohne sich in die Xentral-Instanz selbst einloggen zu müssen. Dafür stellt unser Partner Projektraum Reger eine Xentral-spezifische RFID-Stechuhr zur Verfügung.

[Mehr Informationen zur RFID-Stechuhr von Projektraum Reger.](https://www.projektraum-reger.de/xentral-stechuhr/)

Nachfolgend ist die Nutzung des Stechuhr-Moduls direkt in der Xentral-Instanz beschrieben.

## Buchen am Terminal

In der Xentral Stechuhr können Mitarbeiter Anwesenheits- und Pausenzeiten buchen.

Bitte beachte, dass du mit der Zeiterfassung immer zum Ersten des Monats beginnst, damit es zu keinen Minusstunden kommt bzw. kein manueller Nachtrag vorgenommen werden muss.

Gebucht werden können diese Ereignisse:

- Kommen
- Gehen
- Pause Start
- Pause Stop

Aus den addierten Arbeitszeiten errechnet sich die geleistete Arbeitszeit jedes Mitarbeiters.

![etr2.png](https://help.xentral.com/hc/article_attachments/14124106553372)

Die Stechuhr-Oberfläche beinhaltet folgende Elemente:

- Name des Mitarbeiters (erste Zeile)
- Aktueller Status des Mitarbeiters (zweite Zeile)
- Tasten für die Buchung eines Ereignisses (dritte, vierte und fünfte Zeile)
- "Logout" Taste für die Abmeldung, ohne die Buchung eines Ereignisses (unten)

## Manuelles Buchen in der Mitarbeiterzeiterfassung

Sie können auch manuell Zeiten buchen unterAdministration > Einstellungen > Mitarbeiter Verwaltung > Mitarbeiterzeiterfassung > Gebuchte Zeiten > Neuer Eintrag.

Im Kalender kann durch einen Klick auf den entsprechenden Tag ebenfalls eine Zeit gebucht werden (z.B. Urlaub, Krank).

> **Wichtig**
>
> Bitte klicken Sie beim Anlegen immer in den richtigen Tag. Eine manuelle Änderung wird unter Umständen nicht durch das Speichern übernommen. Kontrollieren Sie den Eintrag gegebenenfalls später im Kalender.

### Auswertung von gebuchten Zeiten

Die Auswertung der gebuchten Zeiten Ihrer Mitarbeiter erfolgt unterAdministration > Einstellungen > Mitarbeiter Verwaltung > Mitarbeiterzeiterfassung. Dort sind die Buchungsinformationen des in der Auswahlliste links ausgewählten Mitarbeiters in folgenden Reitern dargestellt:

- Urlaub/Krankheit
- Anwesenheitsstatistik
- Stundenübersicht
- Gebuchte Zeiten
- Gebuchte Projektzeiten
- Gebuchte Kundenzeiten

Über den ReiterAnwesenheitsstatistikkönnen Sie sich die Zeiten der Anwesenheit Ihres Mitarbeiter für einen frei wählbaren Zeitraum anzeigen lassen und die Anwesenheitsstatistik sowie die gebuchten Zeiten können jederzeit als PDF- oder CSV-Datei exportiert werden.

Zudem wird in dem Dashboard die bisherig erbrachte Arbeitszeit, die gesamte Soll-Arbeitszeit und die Differenz der Beiden angezeigt. So können Minus- bzw. Plus-Stunden zum Ausdruck gebracht und geleistete Überstunden errechnet und angezeigt werden.

Unter dem ReiterZeiterfassung druckenkann für den ausgewählten Mitarbeiter für einen frei wählbaren Zeitraum ein Nachweis der Arbeitszeit erzeugt und gedruckt werden. Sollten Arbeitsbeginn und -ende mehr als 16 Stunden auseinander liegen, wird davon ausgegangen, dass der Mitarbeiter vergessen hat zu stempeln. Damit dies auffällt, werden Fragezeichen auf dem Zeitnachweis angezeigt.

Im ReiterEinstellungenkönnen, mitarbeiterspezifisch, verschiedene Parameter der Zeiterfassung festgelegt werden.

Sie haben hier die Möglichkeit verschiedene Pausenlängen zu definieren, die nach einer gewissen Arbeitszeit automatisch abgezogen werden soll. Ebenso können Sie hier die Anzahl der für den Mitarbeiter hinterlegten Urlaubstage eintragen.

Bei der Erfassung über das Dashboard für die Mitarbeiterzeiterfassung musst du die konkreten Tage angeben, für die Urlaub genommen wird. Das heißt, du gibst, wenn du eine Woche frei nimmst, nicht die ganze Woche einschließlich Samstag und Sonntag an, sondern nur Montag bis Freitag.

- Vorlage Wochenstunden: Mo: Di: Mi: Do: Fr: Sa: So: von bis
- Hilfe Wochenstunden: Mo: Di: Mi: Do: Fr: Sa: So: von Monat: bis Stunden im Monat: Nach berechnen auf übernehmen klicken um Daten Sollstunden zu speichern.
- Standard Arbeitsbeginn: Diese Zeit wird verwendet falls an diesem Tag keine Zeiten per Stechuhr gebucht wurden, aber per Hand eine Ist-Zeit eingetragen wurde. Es muss die Form Stunde:Minute z.B. 08:00 verwendet werden
- Hochsetzen auf Arbeitsbeginn: Ist eine Standardzeit gesetzt und dieser Haken wird die Kommenzeit hochgesetzt falls der Mitarbeiter früher bucht.
- Runden "Kommen" Stechuhr: Rundet die Zeit auf oder ab für die nächsten 5,10,15... Minuten beim Starten der Arbeitszeit
- Runden "Gehen" Stechuhr: Rundet die Zeit auf oder ab für die nächsten 5,10,15... Minuten beim beenden der Arbeitszeit
- Runden Pausen in Minuten: Hier kann eine runde Pause festgelegt werden, z.B. 60 Minuten
- Pause automatisch abziehen: fest von Arbeitszeit abziehen PauseArbeitszeit
- Pause automatisch abziehen: Stunden:Minuten ab Arbeitsstunden. Hier können für drei unterschiedliche Arbeitszeiten automatische Pausen eingetragen werden. So können z.B. nach 4 Stunden automatisch 15 Minuten abgezogen werden, ab 6 Studen aber automatisch 30 Minuten.
- Pause Dauer: wird ignoriert falls Staffelung aktiviert
- Pause aus Stechuhr immer addieren zu automatischer Pause: Ist der Haken aktiviert, werden manuell gebuchte Pausen auf die Pausenzeit der automatisch abgezogenen Pause addiert. Bsp.: 6 Std Arbeitszeit mit 30 Min automatisch abgezogener Pause + 10 Min manueller Pause → 40 Min Pause und 5:20 IST-Zeit
- Urlaub: 2016 2017 2018 2019 2020 2021
- Urlaubstage im Jahr: Angabe der Urlaubstage im angegebenen Jahr
- Resturlaub im Vorjahr: Manuelle Angabe des Resturlaubs aus dem Vorjahr
- Stunden pro Urlaubstag: Gibt an, wieviele Stunden pro Urlaubstag abgerechnet werden. So können z.B. für eine Teilzeitkraft mit 20 Stunden pro Woche 4 Stunden abgerechnet werden.

> **Anmerkung**
>
> Hast du eine Staffelung der Pausen gewählt, musst du diese aufsteigend nach Arbeitsstunden eintragen, sonst funktioniert die Staffelung nicht.

### Einstellungen

Sei finden einen globalen ReiterEinstellungenin der Mitarbeiterzeiterfassung.

- Automatischer Logout nach Sekunden: Der Mitarbeiter wird automatisch aus der Stechuhr-Maske ausgeloggt, wenn er nach x Sekunden keinen Klick getätigt hat.
- Farbe im Kalender: Die Farbe, in der die gebuchten Zeiten deines Mitarbeiters in im Kalender angezeigt werden.

### Urlaubsübersicht der Mitarbeiter

Unter dem ReiterUrlaubsplan (alle Mitarbeiter)können Sie übersichtlich sehen, welcher Mitarbeiter wann Urlaub genommen hat. Mit einem Hover über die Urlaubsmarkierungen sehen Sie die Namen der Mitarbeiter.

Zusätzlich gibt es noch eine weitere Übersicht im ReiterUrlaubsübersicht. Hier wird für jeden Mitarbeiter für ein bestimmtes Jahr angezeigt:

- Gesamtanzahl an Urlaubstagen
- Genommene Urlaubstage - auch bereits in Zukunft eingetragene Tage
- Resturlaub - also wie viele Urlaubstage können noch verplant werden
- Vorjahresurlaubstage, die für dieses Jahr übernommen wurden

> **Anmerkung**
>
> Falls ein Mitarbeiter keine Urlaubstage hinterlegt hat, wird dieser mit **fehlt**

-Einträgen gelistet.

Anzeige von Urlaub / Abwesend im Haupt-Kalender

Sie können in der Mitarbeiterzeiterfassung eingetragenen Urlaubs oder Fehltage im Kalender anzeigen lassen. Somit haben Sie für alle Mitarbeiter einen Urlaubskalender, den Sie zwar einsehen können, aber nur der Administrator in der Mitarbeiterzeiterfassung ändern kann.

![etr3.png](https://help.xentral.com/hc/article_attachments/14124130796188)

Dazu werden die imUrlaub / Krankheit-Reiter eingetragenen Werte genommen:

![etr4.png](https://help.xentral.com/hc/article_attachments/14124146200348)

## Ein- und Ausblenden ehemaliger Mitarbeiter

Sollte ein Mitarbeiter aus dem Unternehmen ausscheiden, kann man den Gültigkeitszeitraum der Rolle wie folgt ändern. Navigiere zur gewünschtenAdresseund klicke im TabRollenauf dasStift-Icon der entsprechenden Rolle. Anschließend kannst du eingeben, bis zu welchem Datum die Rolle aktiv sein soll.

In der Mitarbeiterzeiterfassung kann man nun über den Filter auch ehemalige Mitarbeiter anzeigenselbiges tun.

## Arbeitsfreie Tage

Feiertage können über das ModulArbeitsfreie Tage / Feiertage eingetragen werden. Administration > Einstellungen > Mitarbeiter Verwaltung > Arbeitsfreie Tage > +NEU

- Bezeichnung: Beschreibung eingeben
- Datum: Datum des Feiertages eingeben
- Typ: Typ festlegen (Feiertag, Brückentag oder Betriebsferien)
- Projekt: Wähle ein Projekt aus
- Land: Wähle ein Land aus dem Drop-Down Menü aus

Klicke abschließend aufSpeichern.

### Arbeitsfreie Tage laden

Es gibt auch noch die Möglichkeit, die arbeitsfreien Tage eines bestimmten Bundeslandes automatisch in die Liste zu laden:

![etr5.png](https://help.xentral.com/hc/article_attachments/14124122122012)

### Arbeitsfreie Tage in der Mitarbeiterzeiterfassung

Arbeitsfreie Tage, die Sie definiert haben, werden als vollständig abgeleistete Arbeitszeit behandelt, d.h. es werden automatisch die für den betrachteten Tag voreingestellten Stunden alsgearbeiteteingetragen und durch eine farbliche Markierung als Feiertag gekennzeichnet:

![etr6.png](https://help.xentral.com/hc/article_attachments/14124115191964)

- Das rote Feld zeigt die Krankheitsstunden
- Das orangene Feld zeigt die unbezahlten Stunden (Urlaub)
- Das blaue zeigt die vertraglichen Urlaubsstunden

Die Mitarbeiterzeiterfassung/Stechuhr arbeitet minutengenau; Sekunden werden in Berechnungen abgeschnitten. Rundungsdifferenzen sind nicht als Fehler zu betrachten.

## Abwesenheiten beantragen

Mitarbeiter können in der Mitarbeiterzeiterfassung Urlaubstage und Krankheitstage beantragen. Dafür gibt es im Modul die ReiterAnträge einreichenundAnträge bearbeiten. Ersteren sehen alle Benutzer, die Abwesenheiten anfragen dürfen, letzteren sehen nur Benutzer, die Abwesenheiten Ihrer Kollegen freigeben dürfen, also z.B. Abteilungsleiter oder Personaler. Voraussetzung hierfür ist, dass alle Mitarbeiter auch in xentral als Adressen mit der RolleMitarbeiterangelegt sind und ihre Soll-Arbeitszeiten in der Mitarbeiterzeiterfassung hinterlegt sind.

Wer Abwesenheiten beantragen und wer sie freigeben darf, wird über[Gruppen](#)und die Benutzerrechteverwaltung gesteuert. Jede Abteilung kann als Gruppe angelegt werden und die Adressen Eurer Mitarbeiter werden zu dieser Gruppe hinzugefügt. In jeder Gruppe muss es mindestens einen Verantwortlichen geben, der die angefragten Abwesenheiten genehmigen darf.

Dieser Verantwortliche (also z.B. Abteilungsleiter/Personaler) braucht das Rechttimemanagementhandle aus der Benutzerrechteverwaltung. Dieser Verantwortliche erhält eine E-Mail, sobald ein Mitarbeiter aus seiner Gruppe eine Abwesenheit anfragt.

Es ist für Benutzer, die zu keiner Gruppe gehören, nicht möglich, Abwesenheiten anzufragen – dann erscheint eine Fehlermeldung. Gehört ein Benutzer zu einer Gruppe, zu der nicht auch mindestens ein weiterer Benutzer mit dem Rechttimemanagementhandle (also ein Verantwortlicher) gehört, erscheint ebenfalls eine Fehlermeldung.

### Anträge einreichen

In der Übersicht sieht man in der Grundeinstellung die eigene Urlaubsplanung im aktuellen Jahr. Bei den Jahren kann man jeweils eines vor und eines zurück navigieren. Bei den Gruppen sind die Gruppen aufgeführt, in denen man selbst Mitglied ist. Wenn man eine Gruppe auswählt werden zusätzlich zu den eigenen Abwesenheiten anonymisiert diejenigen der anderen Gruppenmitglieder in der Zukunft angezeigt. Abwesenheiten vor dem heutigen Datum werden nicht dargestellt. Anonymisiert heißt, die Abwesenheiten der anderen Mitglieder werden prinzipiell alsAbwesendangezeigt, egal ob es sich um einen Urlaub oder eine Krankheit handelt. Als letztes gibt es noch die CheckboxAufgeteilt nach Mitarbeiternder, wenn aktiv, zeilenweise die Abwesenheiten der einzelnen Gruppenmitglieder anzeigt

Wenn man auf einen Tag klickt, öffnet sich ein Fenster in dem man das Startdatum, das Enddatum, den Typ der Abwesenheit, einen zusätzlichen Kommentar ausfüllt. Außerdem kann man auswählen ob es sich bei der Abwesenheit um einen halben Tag handelt.

Wenn man sowohl ein Startdatum wie auch ein Enddatum ausgewählt hat, wird automatisch aus dem ausgewählten Zeitraum ermittelt wie viele Urlaubstage benötigt werden. Feiertage werden prinzipiell herausgerechnet. Samstage und Sonntage werden abhängig davon ob im ReiterMitarbeiter > Einstellungenin den Feldern Vorlage Wochenstunden Stunden eingegeben wurden, herausgerechnet oder nicht.

Mögliche Aktionen in dieser Übersicht:

- Urlaub beantragen (muss freigegeben werden)
- Krankheit beantragen (muss freigegeben werden)
- Urlaub entfernen (muss freigegeben werden)
- Krankheit entfernen (muss freigegeben werden)
- Urlaubsantrag löschen (geht nicht bei Urlaub in der Vergangenheit)
- Krankheitsantrag löschen (geht nicht bei Urlaub in der Vergangenheit)

### Anträge bearbeiten

In diesem Reiter dürfen Verantwortliche alle Anträge bearbeiten, die von Mitgliedern Ihrer Gruppe(n) stammen, d.h. die angefragten Abwesenheiten freigeben oder ablehnen. Benutzer mit dem Rechttimemangementsuperprivilegedarf ein Benutzer sogar alle Urlaubsanträge aller Mitarbeiter bearbeiten. Dieses Recht sollte daher für Personalleiter oder abteilungsübergreifende Führungspersonen reserviert sein. Administratoren haben jedes Recht, inklusive dertimemangementsuperprivilege.

Wenn Urlaubs- oder Krankheitsanträge abgelehnt werden, werden diese in der ÜbersichtAnträge einreichenfür einige Zeit farblich markiert und können dann vom Mitarbeiter wieder bearbeitet werden. Wenn der Löschung einer Abwesenheit zugestimmt wird, wird der Status von diesem Tag entfernt. Wenn eine Löschung abgelehnt wird, bleibt der Tag als Urlaub oder Krankheit markiert.

In diesem Reiter gibt es außerdem noch das UntermenüAbgeschlossene Anträgein dem man alle bearbeiteten Anträge sehen kann.

Es wird grundsätzlich eine E-Mail verschickt, wenn ein Vorgesetzter einem Antrag zustimmt oder ablehnt. Der Text dieser E-Mails kann im Modul[Geschäftsbriefvorlagen](#)konfiguriert werden.

In der Dokumentenvorlage stehen sowohl im Textkörper wie im Betreff folgende Variablen zur Verfügung:

- {DAYTYPE}: Vorheriger Status des Tages
- {FROMDATE}: Startdatum
- {TILLDATE}: Enddatum
- {EMPLOYEECOMMENT}: Kommentar des Antragstellers
- {SUPERVISORCOMMENT}: Kommentar des Vorgesetzten
- {EMPLOYEENAME}: Name des Antragstellers
- {EMPLOYEENUMBER}: Nummer des Antragstellers
- {AMOUNTDAYS}: Anzahl der benötigten Urlaubs-Tage
- {REJECT}: wurde der Antrag angenommen oder abgelehnt