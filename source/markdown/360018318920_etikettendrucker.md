## Etikettendrucker druckt mit falschem Papierformat (AS)

**Vorsicht**: das folgende funktioniert nicht immer zu 100 %: Könnt Ihr bitte unter CUPS die Höhe und Breite in mm einstellen, da gibt es anscheinend Schwierigkeiten:
![](images/?name=inline-1095086172.png)

​

Das wäre der richtige Treiber, der derzeit verwendet wird?

![](images/?name=inline696177635.png)

​

Falls nicht, bitte noch den Treiber umstellen.

In den Einstellungen im Etikettendrucker in xentral darf kein Format eingestellt sein, sonst klappt die Übertragung des Formates auch nicht.

Zusätzliche Information zum Thema Etikett, bei Etikett Typ1 kann auch die Breite eingestellt werden, das kann man mit dem Befehl:

```width="40"```Das könnte entsprechend so aussehen:```<barcode y="1" x="3" size="8" width="40" type="1">{NUMMER}</barcode>```