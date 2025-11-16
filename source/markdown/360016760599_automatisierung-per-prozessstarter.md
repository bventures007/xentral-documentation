Prozessautomatisierungen spielen eine entscheidende Rolle dabei, deinen Unternehmensalltag effizienter zu gestalten und Zeit zu sparen. InXentral kannst du automatische Prozesse aktivieren und beispielsweise Berechnungen durchführen lassen. Du kannst sie so einstellen, dass sie entweder zu einer bestimmten Uhrzeit am Tag oder periodisch in einem von dir festgelegten Intervall aktiv werden.

Die Prozessautomatisierung im Modul **Prozessstarter** ermöglicht es dir, verschiedenste Aktionen zu steuern. Dabei handelt es sich beispielsweise um den Import von Aufträgen aus Shops in Xentral, die Abwicklung versandfertiger Aufträge innerhalb der Logistikprozesse, die E-Mail-Kommunikation mit deinen Kunden und mehr.

## Prozessstarter aktivieren und konfigurieren

Die Prozessautomatisierung findest du im Menü **Einstellungen > Administration > Prozessstarter **. Gib alternativ den Begriff ** Prozessstarter**in die Smart Search ein, um das Menü zu öffnen.

![prozesstarter_001.png](https://help.xentral.com/hc/article_attachments/15512650601628)

> **Tipp**
>
> Öffne das Tab **Laufzeiten**, um die Ausführungen der Prozessstarter zu überprüfen. Die Ausführungen werden nach Laufzeit grafisch dargestellt.
>
> Falls die Laufzeit eines bestimmten Prozesses zu viel Zeit in Anspruch nimmt, überprüfe vor allem bei periodischen Prozessstartern deinen Eingaben im Feld **Periode** und passe den Wert an.

### Prozessstarter periodisch oder zur festen Zeit ausführen

Prozessstarter können entweder in spezifischen Zeitabständen (periodisch) oder täglich zu einer festgelegten Uhrzeit ausgeführt werden. Beachte, dass der Prozessstarter zu deinen sonstigen Einstellungen in Xentral passt und die Intervalle aufeinander abgestimmt sind. Verwendest du beispielsweise Prozessstarter für den Import von Aufträgen von Verkaufsplattformen in Xentral, dann sollte genug Zeit eingeplant werden, damit dieser Prozessstarter alle Aufträge aus den Plattformen abholen kann. Andernfalls werden weitere Prozesse oder ein weiterer Abholversuch für diesen Prozessstarter gestoppt. Solange ein Prozess läuft, werden alle weiteren Prozesse je nach Priorisierung erst im Anschluss abgearbeitet.

> **Anmerkung**
>
> **Hinweis**
>
> (1) Beispieleinstellung für einen **periodischen Prozessstarter**:
>
> - **Art**: periodisch
> - **Wochentag**: jeden Tag
> - **Periode**: Angabe in Minuten z.B. 1, 5 oder 10 (bei Shops mit Versand bis Mittag genügt auch 2x pro Tag)
>
> (2) Beispieleinstellung für einen **Prozessstarter zu festgelegter Uhrzeit**:
>
> - **Art**: Uhrzeit
> - **Wochentag**: jeden Tag oder ein bestimmter Wochentag
> - **Startzeit**: Uhrzeit, z.B. aktuelles Datum und Ausführung um 15:00:00

![prozesstarter_002.png](https://help.xentral.com/hc/article_attachments/15512606278172)

![prozesstarter_003.png](https://help.xentral.com/hc/article_attachments/15512634777244)

### Prozessstarter limitieren

Du kannst die Anzahl parallel laufender Prozesse limitieren, um eine zu hohe Systemauslastung zu vermeiden. Öffne dazu das Menü **Einstellungen > Administration > Systemeinstellungen ** und nutze die Einstellung **Prozessstarter limitieren ** unten im Bereich**Beschleunigungen/Limitierungen**.

## Übersicht der Prozessstarter

Hier findest du einen Überblick über die typischen Prozessstarter inklusive der passenden Erläuterung.

> **Wichtig**
>
> Stelle bei der Einrichtung von Prozessstartern sicher, dass du stets den korrekten Parameter angibst. Die Parameter sowie sonstige wichtige Hinweise und Einschränkungen findest du in den Tabellen der folgenden Kapitel.

- [Prozessautomatisierung für die Logistik](#prozessautomatisierung-fuer-die-logistik)
- [Prozessautomatisierung für Shopsysteme und Marktplätze](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724153369767)
- [Prozessautomatisierung für Belege](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724241270851)
- [Prozessautomatisierung für Artikel, Lagerwert, Produktion und Dropshipping](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724243494656)
- [Prozessautomatisierung für Buchhaltung, Steuern, Währung und Berichtswesen](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724241371818)
- [Prozessautomatisierung für den E-Mail-Versand](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724242338452)
- [System, Systeminformation Prozessautomatisierung](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724242398119)
- [Prozessautomatisierung für externe Tools](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724242416002)
- [Sonstige Prozessautomatisierung](#UUID-90d7b13f-2e36-1fc7-8eb6-1c4615dc892a_N1724242430940)

### Prozessautomatisierung für die Logistik

These process starters control the logistics process by first checking the availability of inventory and updating order indicators accordingly. Then, ready-to-ship orders are (automatically) forwarded to logistics based on priority or specific criteria. In the warehouse, the orders can then be processed at defined intervals and prepared for shipping.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **Auftrag Lagercheck **| auftraglagercheck | Ein Prozessstarter mit dem Parameter ** auftraglagercheck **prüft und aktualisiert den Lagerstatus von Aufträgen, die als „out of stock“ markiert sind, indem sie speziell die orangefarbene Lagerampel neu berechnet. 🚨** Warnung:** Verwende diesen Prozessstarter nicht in Kombination mit dem Modul Pickllisten-Profile in Xentral, da es ansonsten zu einer erhöhten Systemlast und damit zu längeren Laufzeiten für die einzelnen Prozesse kommt. |
| **Autoversand berechnen **| autoversand_berechnung | Ein Prozessstarter mit dem Parameter ** autoversand_berechnung** aktualisiert automatisch die Auftragsampeln für den Autoversand, einschließlich Überprüfungen von Lagerverfügbarkeit, Porto und Zahlungseingängen bei Vorkasse. Er prüft alle Ampeln unabhängig von ihrem aktuellen Status und führt zusätzlich Preisberechnungen durch, einschließlich der Aktualisierung von Aufträgen und der Berechnung von Deckungsbeiträgen. |
| **Autoversand manuell **| autoversand_manuell | Beim Klick auf die Option ** Auto-Versand starten** innerhalb eines Auftrags lädt dieser Prozessstarter geprüfte Aufträge (mit grüner Auftragsampel) in eine Warteschlange und übergibt sie kontinuierlich an den Autoversand. Bei hohem Auftragsaufkommen verhindert dieser Prozessstarter Server-Timeouts. Achtung Die Prozessstarter autoversand_manuell und autoversand_plus können nicht gleichzeitig verwendet werden. |
| **AutoversandPLUS **| autoversand_plus | Ein Prozessstarter mit dem Parameter ** autoversand_plus **macht die manuelle Ausführung der Option ** Auto-Versand starten **überflüssig. Alle freigegebenen Aufträge mit dem Status ** Autoversand OK** werden im im Hintergrund kontinuierlich an den Auto-Versand übergeben. Achtung Die Prozessstarter autoversand_manuell und autoversand_plus können nicht gleichzeitig verwendet werden. Ampelberechnungen werden mithilfe des Prozessstarters autoversand_plus automatisch durch einen vorausgehenden Prozess durchgeführt, wodurch die Performance optimiert wird. Stelle für diesen Prozessstarter stets eine bestimmte Uhrzeit zur Ausführung ein. Falls doch eine Periode gewählt wurde, müssen als Intervall mindestens 31 Minuten eingestellt sein. Bei einem niedrigeren Intervall wird der Prozessstarter nicht ausgeführt. |
| **Batches **| batches | Ein Prozessstarter mit dem Parameter ** batches** steuert das Modul [Picklisten-Profile](https://help.xentral.com/hc/de/articles/360016722600#UUID-a3288421-c888-8d23-a2a3-e7de468d630b) für die Erstellung und Weitergabe von Picklisten, die nach in definierten Regelwerken angelegt werden. Er ermöglicht es, versandbereite Aufträge nach Verkaufskanal, Artikelmenge und weiteren Kriterien zu sortieren und an den Auto-Versand zu übergeben. Achtung Bei Verwendung dieses Prozessstarters sollten keine anderen Prozessstarter aktiv sein. Nutze ausschließlich das Modul Picklisten-Profile für die Verwaltung und Erstellung der Picklisten. Für die Abarbeitung verbleibender Einzelaufträge am Tagesende kannst du ein spezielles Picklisten-Profil einrichten, um die Systemleistung zu optimieren und andere Prozesse nicht zu beeinträchtigen. |
| **Uebertragungen Fulfillment **| api_uebertragungen | Ein Prozessstarter mit dem Parameter ** api_uebertragungen **ist Grundlage für die automatisierte Übertragung von Belegen wie Lieferscheinen und Rechnungen sowie weiterer Daten an einen Fulfillment-Dienstleister. Weitere Informationen über die Verwendung des Moduls ** Übertragungen** findest du [in diesem Artikel](https://help.xentral.com/hc/de/articles/360016738020#UUID-72f37f06-2871-0785-7286-1f7a2707c88d). |

### Prozessautomatisierung für Shopsysteme und Marktplätze

Der nahtlose Import von Aufträgen, die dich über Shopsysteme und Marktpätze erreichen, ist entscheidend für eine reibungslose Abwicklung dieser Aufträge in Xentral. Die folgenden Prozessstarter unterstützen dich nicht nur bei der Automatisierung des Auftragsimports, sondern bieten beispielsweise für Amazon auch die Möglichkeit, die Rückmeldung des Versands oder von Lagerzahlen sowie die Übermittlung von Zahlungsberichten zu automatisieren. Nicht zuletzt ist auch der Prozessstarter **Artikel übertragen** sehr wichtig für dich, wenn du deine Produkte auf Marktplätzen oder über andere Shopsysteme verkaufst.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **Adressen zum Shop exportieren **| shopexport_adressexport | Exportiert Adressen in die angebundenen Shops. Der Export von Adressen zu Shops ist nicht für alle Shopschnittstellen möglich. Damit der Export erfolgt, müssen in der Shopschnittstelle unter ** Adressenübertragung** die Adressen hinzugefügt werden, die übertragen werden sollen. Der manuelle Adressexport muss in der Shopschnittstelle aktiviert sein. Beachte, dass die Adresse im Adressstamm eine E-Mail-Adresse benötigt. |
| **Amazon **| amazon | Dieser Prozessstarter übernimmt folgende Aufgaben: - Berichte von Amazon abholen und verarbeiten (z.B. Zahlungsberichte und Lagerzahlenberichte)<br>- Versandrückmeldung<br>- Lagerzahlenrückmeldung<br>- Anfragen von Xentral an Amazon bei der Artikelanlage 🚨** Warnung:** Dieser Prozessstarter sollte nicht häufiger als einmal in 10 Minuten ausgeführt werden, da Amazon die Anfragen unter Umständen nicht schneller verarbeiten kann. |
| **Artikel übertragen **| artikeluebertragen | Exportiert alle Artikel in den Shop, die im Menü ** Einstellungen > Verkaufen > Shops/Marktplätze > Shops & Marktplätze Übersicht > Shop auswählen > Tab: Artikel Übertragung** in die Liste geladen wurden. Dieser Prozessstarter prüft, ob sich Artikel in der Liste befinden und überträgt diese. |
| **Artikelimport **| getarticles | Importiert nach und nach alle Artikel aus einem Online-Shop bzw. aktualisiert diese, nachdem der Import dort per Klick auf die Schaltfläche ** Artikelliste abholen** angestoßen wurde (nicht für alle Shopschnittstellen verfügbar). |
| **Auftragsimport aus dem Shop/Shopimporter** | shopimport | Dieser Prozessstarter ermöglicht das automatisches Abholen von Aufträgen z.B: aus Online-Shops oder anderen angebundene Systemen. Achtung Dieser Prozessstarter blockiert den manuellen Import von Aufträgen. Wir empfehlen, das Intervall für die Ausführung des Prozessstarters so zu wählen, dass er nicht durchgehend läuft, sofern du die Möglichkeit haben möchtest, Aufträge auch zeitweise manuell zu importieren. Der Prozessstarter wird automatisch aktiviert, sobald mindestens ein Shop auf automatisch abholen umgestellt wird. |
| **Bereitstellung Artikelfeed Manomano** | artikelfeed_manomano | Dieser Prozessstarter baut aus dem Artikelstamm von Xentral heraus eine CSV-Datei auf, in der später alle Artikel enthalten sind, die eine Manomano-Verknüpfung unter Artikel → Online Shop Optionen haben, den Lagerzahlensync erlauben und nicht gelöscht oder gesperrt sind. Die CSV-Datei legt der Prozessstarter dann im in der Shopschnittstelle eingestellten Pfad ab. Von dort kann Manomano die CSV-Datei abholen. |
| **eBay Stapelverarbeitung** | ebay_bulkjobs | Fasst die angefallenen Änderungen/Requests als Job zusammen und schickt diese an eBay. Du kannst per Logging [in der eBay App](https://help.xentral.com/hc/de/articles/18589749660316#UUID-e409be78-b9ce-0186-b03a-a98c9ec90f3c) prüfen, für welchen Artikel welcher Lagerbestand gemeldet wurde und ob die Meldung erfolgreich war. |
| **Shopware6 Stapelverarbeitung** | shopware6_bulkjob | Synchronisiert Lagerzahlen und Preise asynchron, wenn die Artikelübertragung in der Shopimporter-Schnittstelle deaktiviert ist.Weitere Informationen findest du [in diesem Artikel](https://help.xentral.com/hc/de/articles/360016719820#UUID-4a0d0976-28d7-3aa2-53a5-6a84179395cc). |
| **Lagerzahlen Shop Synchronisation** | lagerzahlen | Einstellungen für die automatische Synchronisierung der Lagerzahlen für Online-Shops. Dieser Prozessstarter meldet Lagerzahlen in einem festen Rhythmus an den Shop zurück. Der Online-Shop verringert meist seine Lagerzahl bei eingehenden Bestellungen von Kunden selbständig. Xentral vergleicht die zuletzt gemeldete Lagerzahl mit der des Shops. Bei Differenzen wird die neue Lagerzahl angepasst. Dabei wird die verkaufbare Menge des Artikels aus dem Artikelstamm übertragen und somit alle Reservierungen berücksichtigt. Wenn die Lagermenge aller Artikel auf einmal neu übertragen werden soll, dann kannst du im Modul[Übertragungen](https://help.xentral.com/hc/de/articles/360016738020#UUID-72f37f06-2871-0785-7286-1f7a2707c88d) den Lagerzahlencache wieder leeren. |
| **Online Shop Hintergrundtasks **| onlineshops_tasks | Dieser Prozessstarter ist nach der Anbindung von Online-Shops relevant und übernimmt folgende Aufgaben: - Artikelliste importieren<br>- Kategoriebaum importieren Wird in einem Importer der Artikelbaum übertragen oder die Artikelliste abgeholt, dann werden diese Aufgaben in die Warteschlange der Datenbanktabelle namens ** onlineshops_tasks** übertragen. Der Prozessstarter arbeitet die Tabelle ab und führt unerledigte Tasks aus. |
| **Shop Rückmeldungen** | shop_rueckmeldungen | Meldet den Auftragsstatus und ggf. die Tracking-Nummer des Versanddienstleisters von versendeten Aufträgen zurück an den Online-Shop, aus dem sie importiert wurden. |
| **Shopimport alte Aufträge **| shopimport_auftragarchiv | Holt nach und nach alte Aufträge aus einem angebundenen Online-Shop) ab, wenn die Abholung dort über die Schaltfläche ** Alte Aufträge importieren** angestoßen wurde. Bitte beachte, dass die Abholung alter Aufträge nicht in allen von Xentral angebotenen Shop-Schnittstellen möglich ist. |
| **Shopimport Unbezahlte Aufträge prüfen** | shopimport_checkorder | Dieser Prozessstarter prüft, ob die Verkaufsabwicklung bei eBay nachträglich abgeschlossen wurde. |
| **Spryker Stapelverarbeitung** | spryker_task | Meldet aktualisierte Auftragsstatus, die Tracking-Nummern versandter Lieferungen sowie Lagerzahlen der Artikel an den Shop zurück. |

### Prozessautomatisierung für Belege

Xentral bietet dir verschiedene Möglichkeiten, um den Import, die Erzeugung, die Stapelverarbeitung und die Archivierung von Belegen zu automatisieren. Alle verfügbaren Prozessstarter für die Erledigung dieser Aufgaben findest du in der Tabelle.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **Belege Import** | belegeimport | Importiert alte Belege (Aufträge, Lieferscheine, Rechnungen usw.) per CSV in Xentral. |
| **Bestellungen automatisch abschließen **| bestellungabschliessen | Wenn die Option ** Bestellungen automatisch abschließen **im Menü ** Einstellungen > Administration > Systemeinstellungen **aktiviert ist, prüft der Prozessstarter die offenen Bestellungen. Falls Bestellungen gefunden werden, deren Artikel bereits vollständig geliefert wurden, erhalten diese den Status ** abgeschlossen**. |
| **Dokumente Stapelverarbeitung** | documentbatches | Führt die Stapelverarbeitung von Aufträgen zu Rechnungen aus. |
| **PDF Archivierung** | pdfarchiv_app | Archivierung der Dokumente, wie z.B. aller Rechnungen oder aller Gutschriften. Die Funktion erstellt einen Ordner mit allen Belegen aus Xentral in diesem Zeitraum, der im Anschluss zum Download angeboten wird. |
| **Zahlungseingang (Liveimport)** | zahlungseingang | Ermöglicht nach erfolgreicher Geschäftskontenanbindung den Liveimport der Kontoaktivitäten automatisiert auszulösen (außer bei CSV-Importen). Die Einstellung kann pro Geschäftskonto erfolgen. Weitere Informationen zu Geschäftskonten findest du [in diesem Artikel](https://help.xentral.com/hc/de/articles/360016722680#UUID-96599490-8dbc-54ef-b3f3-ea8e27cc732e). |

### Prozessautomatisierung für Artikel, Lagerwert, Produktion und Dropshipping

Lagerbestände und andere wichtige Werte für die Logistik ändern sich oft sogar minütlich. Um den Überblick zu behalten und stets mit aktuellen Zahlen und Prozessen zu arbeiten, kannst du ebenfalls verschiedene Prozessstarter nutzen. Sie übernehmen die Aktualisierung von Bestandsdaten, die Berechnung von Lagerwerten und Produktionen und weitere Aufgaben für dich.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **Artikel Cache **| artikelcache | Aktualisiert an mehreren Stellen die Bestandsdaten in Xentral, wie z.B. die Anzeige der optional einstellbaren Spalte ** Lager verfügbar** in der Artikelübersicht. Darüber hinaus werden auch Bestandsanzeigen in der Auftragsübersicht aktualisiert. |
| **Dropshipping Lager** | dropshippinglager | Überprüft im Hintergrund automatisch die offenen Aufträge auf Artikel, die sich in einem [Dropshipping-Lager](https://help.xentral.com/hc/de/articles/360016758979#UUID-2dbb103d-9ae5-275c-6b9f-e296851589d1) befinden. Werden Aufträge gefunden, so wird automatisch ein Teilauftrag daraus erstellt. |
| **Importvorlage **| importvorlage | Führt das Modul ** Importvorlage** mit den darin enthaltenen vordefinierten Importvorlagen aus. |
| **Lagerwert Berechnung **| lagerwert | Schreibt den Lagerbestand für alle Lagerartikel pro Tag fest, sodass diese im Bereich ** Lagerbestandsberechnung** eingesehen werden können. |
| **Produktion neu berechnen** | produktion_berechnen | Berechnet anhand von aktuellen Zahlen die Produktion neu. |

### Prozessautomatisierung für Buchhaltung, Steuern, Währung und Berichtswesen

Egal, ob du in Xentral mit Aboläufen arbeitest, Währungskurse zuverlässig auf dem neuesten Stand halten möchtest oder Zahlungseingänge auf deinen Geschäftskonten unkompliziert importieren möchtest - auch hier hast du mithilfe verschiedener Prozessstarter die Möglichkeit, deine Abläufe so weit wie möglich zu automatisieren.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **Abolauf Hintergrundtask** | rechnungslauf | Startet den Abolauf als Hintergrundtask. |
| **Abolauf Manuell **| rechnungslauf_manual | Arbeitet die ausgelösten Rechnungsläufe schrittweise ab (ähnlich wie der Prozessstarter ** Autoversand manuell**). Im Standardprozess landen die Aboläufe zunächst in der Warteschlange und werden nach und nach von diesem Prozessstarter abgewickelt. Ist die Anzahl der Aboläufe gering, kann dieser Prozessstarter auch deaktiviert werden, um den Prozess zu beschleunigen. |
| **Berichte FTP Übertragung (neues Modul)**| report_transfer_ftp | Versendet regelmäßig Berichte per FTP, die für die FTP Übertragung markiert sind. 💬** Anmerkung:** Dieser Prozessstarter kann nur in Verbindung mit dem neuen Berichte-Modul verwendet werden. Weitere Informationen dazu findest du in diesem Artikel. |
| **Mahnwesen-Check** | mahnwesencheck | Dieser Prozessstarter führt regelmäßige Vorab-Berechnungen durch, um einen Timeout-Fehler beim Starten des Mahnwesens zu vermeiden. Wir empfehlen die Nutzung dieses Prozessstarters, wenn du besonders viele Rechnungen in kurzer Zeit ausstellst oder für den klassischen E-Commerce mit vielen, kleinen und schnelldrehenden Produkten. |
| **Überzahlte Rechnungen** | ueberzahlterechnungen | Auflistung und Berechnung aller Rechnungen, die überzahlt worden sind. |
| **Umsatzstatistik **| umsatzstatistik | Erstellung und Berechnung umfangreicher Umsatzstatistiken im Menü ** Berichtswesen > Umsatzstatistiken**. |
| **Waehrung ECB Kurse **| abholenwaehrung | Dieser Prozessstarter ruft die von der EZB herausgegebenen aktuellen Währungskurse für Währungen ab, die du im Modul ** Währung Umrechnung** angelegt hast. |
| **Zahlungseingang** | zahlungseingang | Dieser Prozessstarter löst nach erfolgreicher Geschäftskontenanbindung den Liveimport der Kontoaktivitäten automatisiert aus (außer bei CSV-Importen). Die Einstellung kann pro Geschäftskonto erfolgen. Weitere Informationen zu Geschäftskonten findest du [in diesem Artikel](https://help.xentral.com/hc/de/articles/360016722680#UUID-96599490-8dbc-54ef-b3f3-ea8e27cc732e). |

### Prozessautomatisierung für den E-Mail-Versand

Die folgenden Prozessstarter erlauben dir, genau zu steuern, welche E-Mails zu welchem Zeitpunkt an deine Kunden versendet werden. So kannst du beispielsweise den Versand von Zahlungserinnerungen an deine Kunden vollständig automatisieren. Auch in deinem Tagesgeschäft kannst du diese Prozessstarter sinnvoll nutzen, indem du Bestellvorschläge automatisiert per E-Mail versendest, deine Mitarbeiter an bestehende Aufgaben oder Wiedervorlagen erinnerst oder E-Mails deiner Kunden automatisch in das XentralTicketsystem importieren lässt.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **Aufgaben Erinnerung **| aufgabenmails | Einstellungen für die automatische E-Mail Erinnerungsfunktion für Aufgaben im Menü ** Team > Aufgaben**. |
| **Bestellvorschlag Mail** | bestellvorschlagemail | Überprüft, für welche Produktionslinie nachbestellt werden muss und versendet diese als Vorschlag per E-Mail. |
| **Emails abholen **| emailbackup | Einstellungen für das automatische Abholen von E-Mails und Senden von automatischen Antworten im Menü ** Einstellungen > Grundeinstellungen > E-Mail > E-Mail Konten**. |
| **Folgebestätigung **| folgebestaetigung | Dieser Prozessstarter wird zu einer fest eingestellten Uhrzeit durchgeführt und versendet eine automatische E-Mail an Kunden, wenn die Ware noch nicht versendet wurde. Die Folgebestätigung ist ein eigener Typ in den Geschäftsbriefvorlagen und wird im Modul ** Geschäftsbrief Vorlagen **definiert. Weiterhin muss im Modul ** E-Mail-Accounts **eine E-Mail-Adresse hinterlegt sein, die E-Mails versenden kann. Bei dieser Adresse muss SMTP aktiviert sein und die entsprechenden Einstellungen ausgefüllt werden. Diese Adresse muss mit der Standard E-Mail-Adresse in den Grundeinstellungen identisch sein. Der auf der Geschäftsbriefvorlage ausgegebene Liefertermin bezieht sich auf den im Auftrag gesetzten Wunsch ** Liefertermin **. Potentielle Liefertermine aus Bestellungen werden hierbei nicht berücksichtigt. Die Folgebestätigung kann pro Projekt aktiviert werden. Öffne dazu das Menü ** Einstellungen > Grundeinstellungen > Projekte > Projekt öffnen > Tab: Logistik/Versand > Bereich: Optionen **und aktiviere die Option ** Folgebestätigung **. 🚨** Warnung:** Dieser Prozessstarter funktioniert nur, wenn du in den Einstellungen die Art Uhrzeit auswählst. Eine periodische Ausführung ist nicht möglich. |
| **Tickets **| tickets | Dieser Prozessstarter importiert E-Mails automatisch in das Ticketsystem im Menü ** Team > Tickets **. Die E-Mail-Accounts für das Ticketsystem legst du im Menü ** Einstellungen > Grundeinstellungen > E-Mail > E-Mail Konten** an. |
| **Tickets (GoogleMail)**| tickets_google | Dieser Prozessstarter importiert GoogleMail-Tickets automatisch in das Ticketsystem im Menü ** Team > Tickets **. Die E-Mail-Accounts für das Ticketsystem legst du im Menü ** Einstellungen > Grundeinstellungen > E-Mail > E-Mail Konten** an. |
| **Versandmails und Rückmeldung** | versandmailsundrueckmeldung | Schließt Lieferscheine ab und versendet die dazugehörigen E-Mails an die Kunden. |
| **Wiedervorlage Erinnerung** | wiedervorlage | Erinnert deine Mitarbeiter intern an Wiedervorlagen. |
| **Zahlungsavis Mailversand** | zahlungsavis_mailausgang | Verschickt zu versendende Zahlungsavis aus der Übersicht, die als Alternative zum Druck zu einer internen Liste hinzugefügt werden. |
| **Zahlungsmail **| zahlungsmail | Versendet nach der eingestellten Anzahl an Tagen automatisch Zahlungserinnerungen. Dieser Prozessstarter ist standardmäßig so eingestellt, dass nach 6 Tagen die erste E-Mail und nach 11 Tagen die zweite E-Mail an deine Kunden versendet wird, soweit noch kein Zahlungseingang stattgefunden hat. Diese Zeitabstände kannst du je nach deinen Wünschen im Menü ** Buchhaltung > Mahnwesen > Tab: Einstellungen **anpassen. Beachte außerdem folgende Voraussetzungen, damit dieser Prozessstarter einwandfrei funktioniert und die E-Mails zuverlässig verschickt werden: - Die betroffenen Aufträge müssen über die Zahlungsart ** Vorkasse **verfügen<br>- Im Menü ** Einstellungen > Grundeinstellungen > Projekte > Projekt öffnen > Tab: Grundeinstellungen > Bereich: Buchhaltung **muss die Option ** Zahlungsmail **aktiviert sein<br>- In den Kundenstammdaten oder am Auftrag muss eine E-Mail-Adresse des Kunden enthalten sein<br>- Im Modul ** Geschäftsbriefvorlagen **wurde eine E-Mail-Vorlage vom Typ ** ZahlungMIss** definiert und gespeichert |

### System, Systeminformation Prozessautomatisierung

InXentral tragen spezifische Prozessautomatisierungen zur Optimierung der Systemüberwachung und Datenintegrität bei. Der Prozessstarter **SystemHealth ** spielt eine zentrale Rolle, indem er den Zustand deines Systems kontinuierlich überwacht und Fehler in Übertragungen oder beim Ausdruck von Picklisten identifiziert. Der Prozessstarter**Doppelte Nummern prüfen** wiederum stellt sicher, dass keine doppelten Kunden-, Artikel- oder Rechnungsnummern vorliegen. Dabei werden gefundene Duplikate meldet, um deren Korrektur zu erleichtern.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **Backup** | backup | Lässt regelmäßig ein Backup von Xentral im Hintergrund durchführen. |
| **Bereiniger** | cleaner | Bereinigt nicht mehr benötigte Systemdateien aus Xentral. |
| **Doppelte Nummern prüfen **| doppeltenummerncheck | Prüft regelmäßig, ob es in Xentral doppelte Kunden-, Artikel-, oder Rechnungs-/Gutschriftennummern gibt. Wurden doppelte Nummern gefunden, so wird oben in Xentral eine rote Warnmeldung mit einem Link ins Modul ** Doppelte Nummern** angezeigt, damit du die Doppelung manuell korrigieren kannst. |
| **FTP-Backup** | ftpbackup | Automatisches Starten des FTP-Backups. |
| **Log Cleaner** | log_cleaner | Bereinigt die Log-Tabellen. |
| **Supersearch Index-Diff** | supersearch_index_diff | Befüllt den Index der Suche. |
| **Supersearch Index-Full** | supersearch_index_full | Befüllt den Index der Suche. |
| **SystemHealth **| systemhealth | Überprüft den Gesundheitszustand des Systems anhand der im Modul ** System Status** aufgeführten Faktoren. |

### Prozessautomatisierung für externe Tools

Prozessautomatisierungen in Xentral vereinfachen die Interaktion mit spezialisierten externen Diensten, um deine Geschäftsabläufe effektiver zu gestalten. Um nur einige Beispiele zu nennen: Mit dem Prozessstarter **HubSpot Data Sync ** kannst du deine Kundeninformationen im CRM automatisch aktualisieren, während der Prozessstarter**Taxdoo sync** die Übertragung von Auftragsdaten für steuerliche Zwecke automatisiert. Diese Integrationen helfen dir, deine Systeme synchron zu halten und die Arbeitslast durch Automatisierung zu reduzieren.

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| **AmaInvoice** | amainvoice | Startet den Abolauf als Hintergrundtask. |
| **Bereitstellung Artikelfeed Manomano** | artikelfeed_manomano | Dieser Prozessstarter baut aus dem Artikelstamm von Xentral heraus eine CSV-Datei auf, in der später alle Artikel enthalten sind, die mit Manomano verknüpft sind. Die CSV-Datei legt der Prozessstarter dann im in der Shopschnittstelle eingestellten Pfad ab. Von dort kann Manomano die CSV-Datei abholen. |
| **Dataprotect** | dataprotect_delete | Asynchrones Hochladen der Dateien. In der Regel heißen diese DATANORM.001, DATANORM.002,... und DATPREIS.001, DATPREIS.002 usw. |
| **HubSpot Data Sync** | hubspot_pull_contacts | Dieser Prozessstarter ermöglicht die Synchronisation und den Datenaustausch zwischen [HubSpot](https://help.xentral.com/document/preview/14035#UUID-42ab0725-e13a-7adb-2ce9-05d3e8e016d8) und Xentral. Er unterstützt den Import neuer oder aktualisierter Kontakte und Adressen von HubSpot in Xentral sowie den Export von Daten von Xentral zu HubSpot. Wenn der Deal-Sync aktiviert ist, werden deine freigegebenen Aufträge als gewonnene Deals an HubSpot übertragen. Die Synchronisation erfolgt standardmäßig einmal täglich, kann aber je nach Bedarf auf 1-3 Mal täglich angepasst werden. Für sofortige Aktualisierungen kannst du jederzeit im HubSpot-Modul die Schaltfläche für den manuellen Import nutzen. |
| **Internetmarke Produktliste aktualisieren** | internetmarke | Aktualisiert in der eingestellten Periode die Produktliste und Portopreise der Deutschen Post für die Schnittstelle zur Internetmarke. |
| **Openstreetmap **| openstreetmap | Füllt die Felder in den Geodaten im Menü ** Verkaufen > Adresse > Adresse öffnen > Tab: Sonstige Daten**. |
| **Paketmarken Tracking Download** | wgettracking | Versucht, Tracking-Informationen direkt bei DHL anzufragen und in Xentral zu übernehmen. |
| **Paqato sync **| paqato | Führt zu Paqato gehörende Prozesse aus und sorgt für den fehlerfreien Betrieb des Moduls. Bei Fragen rund um das Modul ** Paqato** wende dich bitte [direkt an Paqato](https://www.paqato.com/kontakt/). |
| **Pipedrive Process Queues **| pipedrive_process | Arbeitet Queue für das Modul ** Pipedrive** ab. |
| **SevenSenders Tracking Aktualisierung** | sevensenders | Aktualisiert das Tracking bei Sendungen von SevenSenders. |
| **Taxdoo sync** | taxdoo | Überträgt Aufträge in der eingestellten Periode an Taxdoo, wenn die Übertragung in der Taxdoo-Schnittstelle angestoßen wurde. |

### Sonstige Prozessautomatisierung

| Prozessstarter | Parameter | Prozessautomatisierung |
| --- | --- | --- |
| Chat Benachrichtigung | chat | Sendet E-Mail-Benachrichtigungen bei nicht gelesenen Chatnachrichten. |
| Einzelversandübergabe | singleshipment | Scannt alle Aufträge, die noch nicht manuell verschickt wurden, wenn diese einen korrespondierenden Eintrag in der singleshipment_order Tabelle haben. |
| Google Kalender Import | google_calendar_import | Führt regelmäßig einen großen Import durch, bei dem alle Termine der letzten Woche und der nächsten 3 Wochen importiert werden. |
| Kalender Erinnerung | kalender | Verschickt bei Durchlauf eine Erinnerung an alle Benutzer, die in einem gleich anstehenden Kalendereintrag hinterlegt sind. Im Kalendereintrag kannst du die Option **Erinnerung** aktivieren, damit für diesen Eintrag Erinnerungen versendet werden. |