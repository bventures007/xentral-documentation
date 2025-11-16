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

Die Adapterbox ist ein kleiner Server, der als Verbindungsstück zwischen xentral und Hardware dient. Um eine Verbindung von xentral mit einem externen Gerät (Etikettendrucker, Waage, Bondrucker, Kassendisplays etc.) herzustellen, benötigst du eine Adapterbox als kleinen "Zwischen-Server".

Aus technischen Gründen ist dazu derzeit ein Raspberry Pi bis max. Version 3B notwendig.

Sobald du die Adapterbox erworben hast, kannst du diese mit folgenden Schritten konfigurieren:

1. Schließe die Adapterbox an einen Monitor sowie an eine Tastatur und Maus an. Stelle außerdem sicher, dass eine Internetverbindung besteht.
1. Installiere das Betriebssystem und bestätige den darauffolgenden Hinweis mitOK.
1. Navigiere aufLX Terminal(Taskleiste dunkles Icon) und gib folgende Befehle ein. Dann bestätige diese jeweils mit der ENTER Taste:
  Die echo-Befehle dienen mit Ausnahme des letzten Aufrufs nur der Anschaulichkeit.

Wenn die Ausführung des Skripts nicht funktionieren sollte, musst du ggf. noch die PHP-Version mit dazugehörigen Extensions installieren und aktivieren.

**Installation php **```sudo apt -y install php php-common```** Installation PHP-Extension**```sudo apt -y install php-cli php-fpm php-json php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath```

Warte, bis die Aufforderung kommt, eine Seriennummer einzugeben. Gib eine 9-stellige Nummer ein und bestätige mit der ENTER Taste - diese Seriennummer wird dann später in xentral gebraucht. Die Box schaltet sich danach automatisch aus. Die Adapterbox ist nun konfiguriert und du kannst mit dem nächsten Schritt beginnen.

> **Anmerkung**
>
> Sollte dein Drucker nicht drucken, dann stelle den Treiber von cpcl auf zpl (Zebra zb 230) um. Weitere Informationen findest du auf diesen Seiten:
>
> - https://supportcommunity.zebra.com/s/article/CPCL-Manual-for-Zebra-Mobile-Printers?language=de
> - https://supportcommunity.zebra.com/s/article/ZPL-Command-Information-and-DetailsV2?language=de
> - https://webcache.googleusercontent.com/search?q=cache:lNK8FCp4gMsJ:https://community.xentral.com/hc/de/community/posts/360010646660-Adapterbox-einrichten-auf-PI+&cd=1&hl=de&ct=clnk&gl=de