## Multi-Order-Picking Kistennummer Etikett (AB, 21.04.21)

- es gibt keine direkte Möglichkeit diese "einfach" für x Kisten zu drucken
- ggf. über ein externes Onlinetool einfacher
- zwei Möglichkeiten (eher Workarounds):

1.) Über Modul Etikettendrucker

![](images/?name=inline1888049325.png)

​

Hier den Code pro Etikett folgendermaßen angeben

```<label>  <barcode y="1" x="4" size="8" type="1">WAWISION_1</barcode>  <line x="8" y="11" size="4">WAWISION_1</line></label>```

Also WAWISION_1, WAWISION_2,... pro Etikett muss man den Code ändern und Drucken.

Type=1 wichtig, dass "_" für den Barcode funktioniert.

![](images/?name=inline-1902449215.png)

​

2.) Man legt die Kisten kurzfristig als Lagerregale an (also bei 20 Kisten => 20 Lagerregale), erstellt ein Etikettenlayout für Lageretiketten und nutzt dann den Etikettendruck. Ggf. diesen Weg nicht in den Helpdesk aufnehmen.

![](images/?name=inline-348275336.png)

​