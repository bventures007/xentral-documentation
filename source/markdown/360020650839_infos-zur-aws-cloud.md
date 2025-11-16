Xentral bietet seine Cloudservices über Amazon Web Services (AWS) an. DieXentralCloud Server stehen in Frankfurt am Main.

> **Anmerkung**
>
> DieXentralCloud ist zur Ausführung der Software vorgesehen.Xentral stellt keinen Server, auf dem du Dateien per XentralÜbertragungsmodul ablegen kannst und von dem dann andere Programme diese Daten abfragen können. Dazu brauchst du einen separaten FTP Server, auf den auch der Fulfiller zugreifen kann.

Unsere Tarife bieten eine garantierte Erreichbarkeit von 99,5% pro Jahr (EC2 SLA von AWS). Sie bieten Support für den Betrieb durch Xentral und ein Rechenzentrum in Frankfurt, das nach ISO 27001 und ISO 27018 zertifiziert ist (Amazon AWS).

> **Anmerkung**
>
> Aus Leistungs- und Sicherheitsgründen ist der Zugriff auf lokale Serververzeichnisse oder auf die Datenbank nicht möglich.

## Hinweise zum Datenschutz

AlleXentralClouds unterliegen einem strengen Sicherheitskonzept. Die Server der Kunden haben keinerlei direkte Verbindung mit dem Internet. Sie befinden sich in sogenannten VPC (VPN) Zonen und haben keine festen IP-Adressen. Der Zugriff erfolgt nur per https über einen Loadbalancer, der wiederum außer https keinerlei anderes Traffic annimmt. So sind die Server gut vor Hackerangriffen geschützt. Die Datenbanken haben zudem auch keinen Netzwerkport offen, sondern sind nur für die lokale PHP Software erreichbar. Außerdem werden die Server nach außen durch die Firewall gesichert.

Um dich vor Datenverlust zu schützen, findet ein tägliches Backup der Instanzen statt. Dieses kann bis zu sieben Tage im Nachhinein wieder hergestellt werden.

## FAQ

### Wie gehe ich vor, wenn die AWS Cloud nicht erreichbar ist?

Wenn die Cloud Instanz nicht erreichbar ist, kann das daran liegen, dass dein Update nicht sauber durchgelaufen ist.

Gehe wie folgt vor:

1. Rufe in diesem Fall folgende Seite auf: MEINEURL/update.php. Statt "MEINEURL" gibst du deine URL ein.
1. Logge dich ein und führe das Update nochmal durch. Danach sollte die Instanz wieder aufrufbar sein.

### Kann ich auf die Datenbank zugreifen, wenn das Hosting direkt bei Xentral ist?

Nein, das ist nicht möglich. Aus Sicherheitsgründen und zum Schutz der Datenintegrität können wir dir keinen Zugang zur Datenbank geben. Allerdings kannst du in deinem Xentral System im Modul "Datenbank Ansicht" (Mein Bereich > Meine Appsoder über die Super Search) die Daten aus deiner Datenbank einsehen.

### Kann ich auf der Cloud Daten aus Xentral löschen lassen?

Nein, das ist nicht möglich. Grund dafür ist, dass die Datenintegrität sonst nicht mehr gewährleistet werden kann.

### Kann die URL meiner Xentral-Instanz individualisiert werden?

Nein, das ist leider nicht möglich. Aus Sicherheitsgründen bieten wir keine Individualisierung an.

### Wie komme ich an die IP Adresse für die Xentral Cloud?

Aufgrund von frei skalierbaren Ressourcen in unserer Cloud, können wir die IP Adresse der Cloud nicht herausgeben. Wenn es keinen anderen Weg gibt, außer einem Whitelisting der IP, dann musst du im Access log des Servers, zu welchem du transferieren möchtest, untersuchen und so die aktuelle IP in Erfahrung bringen.

> **Anmerkung**
>
> Es kann sein, dass sich pro Request die IP ändert - je nach Auslastung auf unserer Cloud.

Dieser Prozess sollte bestmöglich automatisiert sein, da diese IP sich oft ändern kann (pro Request).

### Wie gehe ich vor, wenn mein Xentral System nicht erreichbar ist und ich 500, 502, oder 504 Fehlermeldungen erhalte?

- Wenn dein Xentral System auf unserer Cloud liegt, wende dich bitte an unseren Support über das Support Ticketsystem.
- Wenn dein Xentral System auf einem eigenen Server betrieben wird, wende dich an deinen Administrator.

### Wie gehe ich bei der technischen Fehlermeldung "Xentral: Es ist ein unerwarteter Fehler aufgetreten” vor?

1. Führe erneut ein Update über deineurl.xentral.biz/update.php durch.
1. Sollte das Problem nach einem Update weiterhin bestehen und die Fehlermeldung wieder erscheinen, wende dich über das Ticketsystem an unseren Support.