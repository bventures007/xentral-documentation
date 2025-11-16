> **Wichtig**
>
> **Legacy-Modul**
>
> Das in diesem Artikel beschriebene Modul wurde als Legacy-Modul gekennzeichnet. Dies bedeutet Folgendes:
>
> - Wir entwickeln keine neue Funktionalitäten oder beheben Bugs für dieses Modul.
> - Das Modul ist in Xentral-Instanzen nicht mehr verfügbar, die nach dem 28. Sept. 2022 erstellt wurden. Dies gilt sowohl für Demo-Instanzen als auch für lizenzierte Instanzen. Solltest du als Neukunde spezielle Anforderungen haben, die nur durch dieses Modul erfüllbar wären, kontaktiere bitte unser Kundensupport-Team, um mögliche Lösungen zu besprechen.
>
> Für weitere Informationen siehe auchWarum stuft Xentral einige Module als veraltet ein (Legacy-Module) und was bedeutet das für dich?

Über App Center → Datanorm finden Sie eine Anwendung, mit deren Hilfe es möglich ist, Daten im DATANORM-Format zu importieren. Eingelesen werden können Dateien der Datanorm-Versionen 4 und 5. Das Modul kann konkret Artikel, Ein- und Verkaufspreise importieren.

In dem Dateiformat bildet jede Zeile eine Informationseinheit. Der Buchstabe am Beginn der Zeile gibt Auskunft darüber was für Informationen das sind. Das Modul befindet sich noch im Aufbau, deswegen können derzeit noch nicht alle Zeilentypen verarbeitet werden. Über Anregungen was euch noch fehlt freuen wir uns immer!

Verarbeitet werden können folgende Zeilentypen:

- V - Vorlaufsatz
- A - Hauptsatz 1 (Artikelsatz A)
- B - Hauptsatz 2 (Artikelsatz B)
- P - Preisänderungssatz
- D - Dimensionssatz
- T - Langtextsatz
- E - Einfügetextsatz (gibt es nur in Version 4)

Über die Oberfläche des Moduls, werden derzeit die Dateien (in der Regel heißen diese DATANORM.001, DATANORM.002,... und DATPREIS.001, DATPREIS.002,...) hochgeladen. Die eigentliche Verarbeitung geschieht dann im Hintergrund asynchron über Cronjobs.

Beim Import ist es grundlegend, das eine Datei mit A-Typen importiert wird. Die Reihenfolge in der Dateien hochgeladen werden ist egal, die App versucht immer erst A-Typen zu importieren.