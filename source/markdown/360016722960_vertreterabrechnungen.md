Das Modul Vertreterabrechnung ermöglicht es, einen zuständigen Vertreter für jeden Kunden festzulegen. Dieser erhält dann bei jedem Verkauf an diesen Kunden, die angegebene prozentuale Provision.

> **Anmerkung**
>
> Es handelt sich um ein Legacy-Modul, das nicht mehr von xentral supportet oder weiterentwickelt wird. Um unseren Kunden die Arbeit mit der vorhandenen Funktionsweise weiterhin zu ermöglichen, ist es noch immer im xentral App Store verfügbar.

## Vertreterabrechnung verwenden

Die Festlegung des Vertreters kann unmittelbar in denAdressdatenunterEinstellungenvorgenommen werden, die in der Startansicht auf der rechten Seite jeder Adresse zu finden ist. Die zugehörige Provisionshöhe kann weiterhin unterSonstige Dateneingestellt werden.

Die Abrechnung der Provisionen erfolgt unterBuchhaltung>Vertreterabrechnungen. Dazu ist unterVertreterdie gewünschte Adresse auszuwählen und ein Datumsbereich festzulegen. Wenn dann aufUmsätze ladengeklickt wird, erscheint eine nach Kunden gegliederte Übersicht über die fälligen Provisionen des angegebenen Vertreters innerhalb des angegebenen Zeitraums.

Um die aktuelle Jahresberichte für die Vertreter zu erhalten, ist im ReiterBerechnungdurchführenauf den ButtonJetzt Berechnungdurchführenzu klicken. Erst dann werden im ReiterJahresberichteInformationen dargestellt.

Unter dem ReiterJahresberichtesind alle Vertreter aufgelistet. Über dasDownload-Symbol am Ende eines Listeneintrages, kann der Jahresbericht für den entspr. Vertreter, in Form einer CSV-Datei, heruntergeladen werden. Der Bericht enthält die Monatsumsätze, sowie den Jahresgesamtumsatz des Vertreters, aufgeschlüsselt nach Kunden.

Im ReiterDiagrammwird die Entwicklung der Verkaufszahlen aller Vertreter im aktuellen Kalenderjahr grafisch dargestellt.

> **Anmerkung**
>
> Die Provisionssperre gibt es für dieses Modul nicht. Wenn eine Provisionsperre verwendet werden soll, müsste das Nachfolge-ModulProvisionenverwendet werden.

## Prozessstarter Vertreterabrechnung einrichten

Um die Vertreterprovisionen regelmäßig vom System berechnen zu lassen, muss ein Prozessstarter eingerichtet werden. Zu beachten ist, dass die Berechnung der Provisionen sehr Datenbank- und rechenintensiv sein können. Daher empfiehlt sich für diesen Prozess unbedingt ein Startzeitpunkt außerhalb der Geschäftszeiten.

Zum Einrichten des Prozessstarters ist unterAdministration>Einstellungen>Prozessstarterauf+Neuzu klicken.

Die Textfelder sind wie folgt auszufüllen:

- Bezeichnung: Als Bezeichnung ist "Provisionsabrechnung" einzugeben
- Art: Aus dem Dropdown-Menü ist als Art "Uhrzeit" auszuwählenmenu
- Wochentag: Aus dem Dropdown-Menü ist "Jeden Tag" auszuwählenmenu
- Startzeit: Ein Startzeitpunkt außerhalb der Geschäftszeiten wird empfohlen
- Letzte Ausführung: Es ist die vorgegebene Endzeit zu belassenplace
- Typ: Als Typ ist "Cronjob" aus dem Dropdown-Menü auszuwählenmenu
- Parameter: Als Parameter ist "provisionen" einzugebenparameter
- Aktiv: Durch Anhaken wird der Prozessstarter aktiviertstarter