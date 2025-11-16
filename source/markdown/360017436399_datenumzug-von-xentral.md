> **Wichtig**
>
> **End-of-Life für On-Premise-Instanzen**
>
> Ende März 2023 beenden wir die Unterstützung von Xentral-Instanzen, die „On-Premise“ von unseren Kunden selbst gehostet werden. Wir empfehlen dir daher, deine Xentral-Instanz in unsere Cloud zu migrieren. Kontaktiere uns gerne jederzeit unteraccount@xentral.com, um diesbezügliche Fragen zu klären oder einen Termin für deine Migration zu buchen. Alternativ kannst du weitere Informationen aufunserer Websiteoder inunserer Communityfinden.
>
> Beachte bitte, dass wir Ende März 2023 jegliche Supportleistungen für On-Premise-Instanzen beenden. Wir stellen dann keine weiteren Bug-Fixes oder Updates mehr zur Verfügung. Außerdem wird es keine weitere Open-Source-Version mehr geben.

## Serverumzug

Zum Umzug des Servers als Gesamtsystem ist der Artikel "[Serverumzug von xentral zu xentral](https://help.xentral.com/hc/articles/360018524479#UUID-f0aa2bc6-d019-74a9-1053-60e773da2da7)" zu beachten.

### Vorbereitungen

> **Anmerkung**
>
> Um die folgenden vorhandenen Terminal Befehle ausführen zu können, kann es nötig sein "sudo" davor zu schreiben, um Zugriff zu erhalten

- Exportieren des Datenbank Dump vom alten System:
  - entweder über **Administration > System > Backup > System-Backup herunterladen > Backup erstellen**

- oder den userdata Ordner aus /var/www/html/wawision/ über ssh kopieren, falls das System-Backup zu groß ist
- Die heruntergeladenen Dateien mit z.B.: scp -r /Pfad/Datei benutzer@dnsname:Pfad auf den neuen Server kopieren
- Über ssh auf dem neuen Server anmelden z.B.: ssh benutzer@dnsname
- Den vorhandenen userdata Ordner in /var/www/html/wawision umbenennen z.B. in userdata
- Neuen userdata Ordner nach /var/www/html/wawision verschieben
- Im userdata Ordner sind Unterordner in denen wiederum Unterordner mit dem Namen der alten Datenbank existieren. Diese Ordner müssen in den neuen Datenbanknamen umbenannt werden.
- **Meistens sind folgende Ordner betroffen:**

- Ordner dms
  - Ordner emailbackup (falls vorhanden)
  - Ordner pdfarchiv
  - Ordner pdfmirror
- Falls weitere Ordner vorhanden sind, müssen diese überprüft werden ob sich in den Unterordnern Unterordner mit alten Datenbanknamen befinden und umbenannt werden. Vorhandene Dateien mit dem Datenbanknamen im Namen müssen ebenfalls umbenannt werden, wie z.B. das Briefpapier.

### Datenbank einspielen

IT Kenntnisse sind dafür zwingend erforderlich!

> **Warnung**
>
> Bei Unkenntnis können Datenverluste erzeugt werden. xentral übernimmt dafür keine Gewähr.

- Datenbank (extra exportieren oder im über die Oberfläche erstellten System-Backup vorhanden) am neuen Server einspielen mit z.B.:
  mysql -u benutzername -p use NameDerNeuenDatenbank; source Pfad/DateinameDerZuImportierendenDatenbank;

  **Beispiel:**

- In der conf/user.inc.php muss die neue Datenbankverbindung und der Pfad zum userdata Ordner eingetragen werden
- Um die Datenbank zu aktualisieren, muss noch php upgradedbonly.php ausgeführt werden **Besonderheiten beim Wechsel zwischen MariaDB und MySql.** Unter Umständen können Views beim Ex- und Import der Datenbank in diesem Fall verloren gehen. Nach einem Update des Systems sind die Views wieder verfügbar. Bei einem Wechsel der von MariaDB zu MySQL oder umgekehrt kann aber das erneute Einspielen eines Scriptes notwendig werden.

Bitte beachten, dass im untenstehenden Code Datenbankbenutzer angepasst werden muss:

```'DEFINER=` xentral `@` localhost`'
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT*/;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS*/;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION*/;
/*!40101 SET NAMES utf8*/;

Substitute structure of the view 'documents

CREATE TABLE IF NOT EXISTS `vouchers ` (` id` int(11)
, `address` int(11)
, `date` date
, `document number` varchar(255)
, `status` varchar(64)
, `country` varchar(255)
, `type` varchar(10)
, `sales_net` decimal(19,2)
, `revenue_net` decimal(19,2)
, `coverage_contribution` decimal(11,2)
, `commission_sum` decimal(11,2)
, `sales_id` int(11)
, `group` int(11)
);
-- --------------------------------------------------------

 Substitute structure of the view `voucher_total

CREATE TABLE IF NOT EXISTS `vouchertotal ` (` id` int(11)
, `address` int(11)
, `date` date
, `document number` varchar(255)
, `status` varchar(64)
, `country` varchar(255)
, `type` varchar(12)
, `net_sales` varchar(23)
, `sales_gross` varchar(23)
, `revenue_net` varchar(21)
, `coverage_contribution` varchar(13)
, `commission_total` varchar(13)
, `salesid` varchar(11)
, `group` varchar(11)
, `project` varchar(222)
);
-- --------------------------------------------------------

--
-- proxy structure of view `belegeregs`
--
CREATE TABLE IF NOT EXISTS `belegeregs ` (` id` int(11)
, `address ` int(11)`date` date
, `document number` varchar(255)
, `status` varchar(64)
, `country` varchar(255)
, `type` varchar(10)
, `sales_net` decimal(19,2)
, `revenue_net` decimal(19,2)
, `coverage_contribution` decimal(11,2)
, `commission_sum` decimal(11,2)
, `sales_id` int(11)
, `group` int(11)
, `project` varchar(222)
);
-- --------------------------------------------------------

--
-- structure of the view `vouchers
--
DROP TABLE IF EXISTS `vouchers`;

CREATE ALGORITHM=UNDEFINED DEFINER=`xentral `@` localhost `SQL SECURITY DEFINER VIEW` vouchers `AS select` invoice `. ` id `AS` id `, ` invoice `. ` address `AS` address `, ` invoice `. ` date `AS` date `, ` invoice `. ` legnr `AS` legnr `, ` invoice `. ` status `AS` status `, ` invoice `. ` country `AS` country `, ` invoice `AS` type `, ` invoice `. ` sales_net `AS` sales_net `, ` invoice `. ` revenue_net `AS` revenue_net `, ` invoice `. ` coverage_contribution `AS` coverage_contribution `, ` invoice `. ` commission_sum `AS` commission_sum `, ` invoice `. ` salesid `AS` salesid `, ` invoice `. ` group `AS` group `from` invoice `where (` invoice `. ` status `<> 'created') union all select` credit `. ` id `AS` id `, ` credit `. ` address `AS` address `, ` credit `. ` date `AS` date `, ` credit `. ` voucher_no `AS` voucher_no `, ` credit `. ` status `AS` status `, ` credit `. ` country `AS` country `,'credit` AS `type`,(` credit `. ` sales_net `*-(1)) AS` sales_net *-1 `,(` credit `. ` erloes_net `*-(1)) AS` revenue_net *-1 `,(` credit `. ` contribution_to_coverage `*-(1)) AS` coverage_contribution *-1 `,(` credit_statement `. ` commission_sum `*-(1)) AS` commission_sum*-1 `, ` gutschrift `. ` vertriebid `AS` vertriebid `, ` gutschrift `. ` group `AS` group `from` gutschrift `where (` gutschrift `. ` status` <> 'created');

-- --------------------------------------------------------

--
-- structure of the view `voucher_total
--
DROP TABLE IF EXISTS `voucher total`;

CREATE ALGORITHM=UNDEFINED DEFINER=`xentral `@` localhost `SQL SECURITY DEFINER VIEW` vouchertotal `AS select` invoice `. ` id `AS` id `, ` invoice `. ` address `AS` address `, ` invoice `. ` date `AS` date `, ` invoice `. ` invoice `AS` invoice `, ` invoice `. ` status `AS` status `, ` invoice `. ` country `AS` country `, ` invoice `AS` type `, ` invoice `. ` sales_net `AS` sales_net `, ` invoice `. ` debit `AS` sales_gross `, ` invoice `. ` sales_net `AS` sales_net `, ` invoice `. ` contribution `AS` contribution `, ` invoice `. ` commission_sum `AS` commission_sum `, ` invoice `. ` salesid `AS` salesid `, ` invoice `. ` group `AS` group `, ` invoice `. ` project `AS` project `from` invoice `union all select` credit `. ` id `AS` id `, ` credit `. ` address `AS` address `, ` credit `. ` date `AS` date `, ` credit `. ` voucher_no `AS` voucher_no `, ` credit `. ` status `AS` status `, ` credit `. ` country `AS` country `,'credit` AS `type`,(` credit `. ` sales_net `*-(1)) AS` sales_net *-1 `,(` credit `. ` debit `*-(1)) AS` sales_gross *-1 `,(` credit `. ` erloes_net `*-(1)) AS` revenue_net *-1 `,(` credit `. ` contribution_to_coverage `*-(1)) AS` coverage_contribution *-1 `,(` credit_statement `. ` commission_sum `*-(1)) AS` commission_sum*-1 `, ` credit `. ` salesid `AS` salesid `, ` credit `. ` group `AS` group `, ` credit `. ` project `AS` project `from` credit `union all select` order `. ` id `AS` id `, ` order `. ` address `AS` address `, ` order `. ` date `AS` date `, ` order `. ` voucher `AS` voucher `, ` order `. ` status `AS` status `, ` order `. ` country `AS` country `,'order` AS `type`, ` order `. ` sales_net `AS` sales_net `, ` order `. ` total `AS` sales_gross `, ` order `. ` revenue_net `AS` revenue_net `, ` order `. ` coverage_contribution `AS` coverage_contribution `, ` order `. ` commission_sum `AS` commission_sum `, ` order `. ` salesid `AS` salesid `, ` order `. ` group `AS` group `, ` order `. ` project `AS` project `from` order `union all select` order `. ` id `AS` id `, ` order `. ` address `AS` address `, ` order `. ` date `AS` date `, ` order `. ` order_id `AS` order_id `, ` order `. ` status `AS` status `, ` order `. ` country `AS` country `, ` order `AS` type `, ` order `. ` total `AS` sales_net `, ` order `. ` total `AS` sales_gross `,'0' AS` erloes_net `,'0' AS` coverage `,'0' AS` commission_total `,'0' AS` salesid `,'0' AS` group `, ` order `. ` project `AS` project `from` order `union all select` delivery_note `. ` id `AS` id `, ` delivery_note `. ` address `AS` address `, ` delivery note `. ` date `AS` date `, ` delivery note `. ` document number `AS` document number `, ` delivery note `. ` status `AS` status `, ` delivery note `. ` country `AS` country `, ` delivery note `AS` type `, ` 0 `AS` sales_net `, ` 0 `AS` sales_gross `, ` 0 `AS` erloes_net `, ` 0 `AS` coverage_contribution `, ` 0 `AS` commission_total `, ` 0 `AS` salesid `, ` 0 `AS` group `, ` delivery note `. ` project `AS` project `from` delivery note`;

-- --------------------------------------------------------

--
-- structure of the view `belegeregs`
--
DROP TABLE IF EXISTS `belegeregs`;

CREATE ALGORITHM=UNDEFINED DEFINER=`xentral `@` localhost `SQL SECURITY DEFINER VIEW` documents `AS select` invoice `. ` id `AS` id `, ` invoice `. ` address `AS` address `, ` invoice `. ` date `AS` date `, ` invoice `. ` documents `AS` documents `, ` invoice `. ` status `AS` status `, ` invoice `. ` country `AS` country `, ` invoice `AS` type `, ` invoice `. ` sales_net `AS` sales_net `, ` invoice `. ` revenue_net `AS` revenue_net `, ` invoice `. ` coverage_contribution `AS` coverage_contribution `, ` invoice `. ` commission_sum `AS` commission_sum `, ` invoice `. ` salesid `AS` salesid `, ` invoice `. ` group `AS` group `, ` invoice `. ` project `AS` project `from` invoice `union all select` credit `. ` id `AS` id `, ` credit `. ` address `AS` address `, ` credit_credit `. ` date `AS` date `, ` credit_credit `. ` voucher_no `AS` voucher_no `, ` credit_credit `. ` status `AS` status `, ` credit_credit `. ` country `AS` country `,'credit_credit` AS `type`,(` credit_credit `. ` sales_net `*-(1)) AS` sales_net *-1 `,(` credit `. ` erloes_net `*-(1)) AS` revenue_net *-1 `,(` credit `. ` contribution_to_coverage `*-(1)) AS` coverage_contribution *-1 `,(` credit_statement `. ` commission_sum `*-(1)) AS` commission_sum*-1 `, ` credit `. ` salesid `AS` salesid `, ` credit `. ` group `AS` group `, ` credit `. ` project `AS` project `from` credit`;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT*/;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS*/;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION*/;

```

### Finale Anpassungen

- Über die Oberfläche von xentral sollte noch ein Update durchgeführt werden, genaueres siehe "Zugang zum Updateserver"
- Zum Schluss muss der Webserver auf den userdata Ordner zugreifen können. Dies geschieht mit chown -R www-data:www-data *
- Um zu überprüfen ob der Webserver auf den userdata Ordner zugreifen kann, kann über die Oberfläche von xentral eine Datei bei einem Artikel oder einer Adresse hochgeladen und anschließend wieder heruntergeladen werden. Hat die Datei eine Größe von 0 Byte stimmen vermutlich die Rechte nicht. Kann die Datei allerdings geöffnet werden, hat alles geklappt.

## Datenumzug für ein Testsystem

Eine Kopie auf ein bestehendes neues Testsystem verläuft im Grunde genauso wie ein Datenumzug des Live-Systems auf einen anderen Server.

Folgendes muss hierbei zusätzlich beachtet und eingestellt werden:Erklärung:

- Wenn die DB kopiert und sich anschließend angemeldet wird, steckt die alte "Lizenz+Schluessel" (also die Zugangsdaten zum Updateserver) in den Firmendaten.
- D.h. es muss dann vorab per phpmyadmin die neue "Lizenz+Schluessel" für das Testsystem eingespielt werden.
- In der Tabelle Firmendaten können die über den phpmyadmin auch ausgetauscht werden.
- Update dein System anschließend über die Oberfläche auf [[http://url/update.php]]