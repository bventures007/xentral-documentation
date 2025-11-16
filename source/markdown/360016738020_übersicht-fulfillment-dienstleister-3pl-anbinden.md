Du arbeitest mit einem Fulfillment- oder Logistik-Dienstleister zusammen? Dann bist du in diesem Abschnitt genau richtig. Dieser Themenbereich enthält nützliche Schritt-für-Schritt-Anleitungen und Tipps, um die Zusammenarbeit mit deinem Fulfillment-Dienstleister zuverlässig in Xentral abzubilden.

## Was ist Fulfillment?

Der Begriff **Fulfillment ** bezeichnet die komplette Auftragsabwicklung - vom Auftragseingang bis zum Versand der Ware an deine Endkunden. Natürlich kannst du dich um all diese Arbeitsschritte selbst kümmern. Je nach Geschäftsmodell macht es Sinn, diese Prozesse auszulagern. Dafür gibt es eine große Auswahl an Fulfillment- und Logistikdienstleistern, die genau diese Teile deines Business für dich übernehmen. Je nach deinen Bedürfnissen kümmern sich diese Unternehmen also um die Lagerung, Kommissionierung, Verpackung und den Versand der Ware. Einige Anbieter übernehmen sogar das Retourenmanagement für dich. So funktionieren diese Unternehmen wie eine Schnittstelle zwischen dir und deinen Endkunden, weshalb dieser Geschäftsbereich auch unter dem Begriff**Third Party Logistics (3PL)** bekannt ist.

Das folgende Schaubild zeigt, wie die Anbindung eines solchen Fremdsystems mit der Auftragsabwicklung in Xentral ineinander greift:

![fulfillment_process_xentral.jpg](https://help.xentral.com/hc/article_attachments/19492844110108)

## Was ist das Übertragungen Modul?

Für die Kommunikation mit Fulfillment-Dienstleistern und anderen Fremdsystemen beinhaltet Xentral das Modul **Übertragungen**. Du benötigst dieses Modul für den Datenaustausch mit dem Fulfillment-Dienstleister. In der Regel werden alle notwendigen Daten wie Aufträge, Artikel, Lagerbestände über einen gemeinsamen Server zwischen dir und dem System deines Fulfillment-Dienstleisters ausgetauscht. Um diesen Datenaustausch einzurichten, sind einige[vorbereitende Einstellungen in Xentral](https://help.xentral.com/hc/de/articles/360018710420#UUID-c30cbf74-515e-8daf-43ca-5b5693f1f4fc)notwendig. Sobald diese Schritte erledigt sind, erledigen sich der Datenaustausch und die entsprechenden Logistikprozesse fast von allein. Mithilfe vielfältiger Einstellungsmöglichkeiten und der[Übersicht über den laufenden Datenaustausch](https://help.xentral.com/hc/de/articles/16164850902428#UUID-2e4e5ae1-18e2-8825-e29e-b9ecc181152a_id_ArbeitenmitdembertragungenModul-bertragungenmitdemMonitorberwachen)inXentral behältst du im Tagesgeschäft die Kontrolle über deine Warenbewegungen und den Status deiner Lieferungen.

> **Tipp**
>
> In den folgenden Artikeln findest du alle notwendigen Informationen, um direkt mit der Einrichtung und anschließenden Verwendung des Übertragungen Moduls zu starten:
>
> - 3PL: Vorbereitende Einstellungen für Fulfillment-Anbindungen (Übertragungen)
> - 3PL: Arbeiten mit dem Übertragungen Modul (Fulfillment-Anbindung)
> - 3PL: Praxisbeispiele für Fulfillment-Anbindungen (Übertragungen)
> - 3PL: Technische Grundlagen und Beispieldateien (Übertragungen)

## Die wichtigsten technischen Daten auf einen Blick

Das Übertragungen Modul von Xentral unterstützt eine Vielzahl möglicher Übertragungsarten und Dateiformate. Im Folgenden haben wir eine Liste der wichtigsten technischen Eckdaten zusammengestellt.

Folgende Übertragungsarten kannst du mit dem Übertragungen Modul in Xentral zu nutzen:

- FTP
- FTPS
- SFTP
- E-Mail

> **Wichtig**
>
> Stelle vor der Verwendung eines SFTP-Servers fest, dass die Serverkonfiguration diebenötigten Kryptoalgorithmenunterstützt. Halte je nach Situation Rücksprache mit deinem Systemadministrator oder deinem Fulfillment-Dienstleister, um diese Anforderung abzuklären.

Das Modul **Übertragungen ** enthält eine Vielzahl an möglichen Dateiformaten, die du für die Datenübertragung nutzen kannst. Bei der Zusammenarbeit kommen in der Mehrzahl der Anwendungsfälle die Formate **CSV ** und**XML** zur Anwendung. Im Folgenden findest du eine Liste der Dateiformate, die standardmäßig bereitgestellt werden.

> **Tipp**
>
> Halte Rücksprache mit dem XentralSupport, falls du dich für weitere Formate interessierst oder individuelle Anwendungsfälle umsetzen möchtest.

- PDF
- XML
- XML mit integriertem PDF (Base64-kodiert)
- XML und PDF in separaten Dateien
- CSV
- API
- App4sales
- Brickfox (weitere Informationen unter [info@brickfox.com](mailto:info@brickfox.com))
- DS
- EDI
- EDI (Sport2000)
- [Netstock](https://help.xentral.com/hc/de/articles/360016773679#UUID-ad413078-1edd-453e-f3fe-4766f7663cac)
- [Opentrans](https://help.xentral.com/document/preview/13973#UUID-c2b2b6f0-47b6-af28-e735-f59eda454bb1)
- Pixi
- [Smarty](https://help.xentral.com/hc/de/articles/4402393972242#UUID-46ee1d66-3282-cf80-dd01-5634ee9c3c56)

> **Anmerkung**
>
> Du interessierst dich für fortgeschrittene Anwendungsfälle oder möchtest die Strukturen innerhalb des Datenaustausches selbstständig anpassen? Mit den entsprechenden technischen Kenntnissen kannst du den Datenaustausch zu einem hohen Grad individualisieren. Schau dir dazu unsere Informationen zu **Smarty** an:
>
> - Smarty Einführung
> - Smarty Felddefinitionen
> - Smarty im Übertragungen Modul