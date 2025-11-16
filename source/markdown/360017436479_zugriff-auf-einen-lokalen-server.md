> **Wichtig**
>
> **End-of-Life für On-Premise-Instanzen**
>
> Ende März 2023 beenden wir die Unterstützung von Xentral-Instanzen, die „On-Premise“ von unseren Kunden selbst gehostet werden. Wir empfehlen dir daher, deine Xentral-Instanz in unsere Cloud zu migrieren. Kontaktiere uns gerne jederzeit unteraccount@xentral.com, um diesbezügliche Fragen zu klären oder einen Termin für deine Migration zu buchen. Alternativ kannst du weitere Informationen aufunserer Websiteoder inunserer Communityfinden.
>
> Beachte bitte, dass wir Ende März 2023 jegliche Supportleistungen für On-Premise-Instanzen beenden. Wir stellen dann keine weiteren Bug-Fixes oder Updates mehr zur Verfügung. Außerdem wird es keine weitere Open-Source-Version mehr geben.

Um über die Ferne auf den lokalen Server zugreifen zu können, wird die IP Adresse der aktuellen Netzwerkverbindung von dem Standort, an dem der Server steht, benötigt. Da sich diese IP Adresse in der Regel bei klassischen Internetverbindungen regelmäßig ändert, wird ein DNS-Eintrag, der immer bei einem Verbindungsaufbau der z.B. Fritzbox geändert wird, benötigt.

## DNS Dienst

Gute Erfahrungen hat xentral mit folgenden Diensten gemacht:

- https://www.dnshome.de/ (Kostenlos)
- http://dyn.com/remote-access/ (Kostenpflichtig - erst registrieren und dann in dem Account auf kostenpflichtigen Account wechseln)

Es ist sich bei den Diensten mit der Wunschdomain zu registrieren. Dort befinden sich auch meist die Anleitungen für den Router. Manchmal heißen die Felder leicht anders. Im wesentlichen muss man meist eine URL, einen Benutzername und ein Passwort angeben. Notfall kurz verschiedene Konstellationen einfach testen.

## Portweiterleitung

Um auf den lokalen Server über das Internet zugreifen zu können, wird eine Portweiterleitung benötigt. D.h. normalerweise läuft der Webserver ohne Verschlüsselung auf Port 80 und mit Verschlüsselung auf Port 443. In dem Router kann die Portweiterleitungen eingestellt werden (bitte suchen wo das Wort steht). Dort ist der Quellport anzugeben, also mit dem Port mit dem zugegriffen wird - also 80 oder 443. Und dann wird eine Ziel IP Adresse und einen Ziel Port benötigt. Die Ziel IP Adresse ist die des Servers. Und Port 80 oder 443. Nach dem Speichern sollte mit der eingerichteten Domain auf xentral zugegriffen werden können. Soll der Zugriff für die Wartung bzw. Entwicklung auf den Server ebenfalls möglich sein, muss hier noch der Port 22 ebenfalls eingetragen werden. Dies kann wie folgt in der Fritzbox eingerichtet werden:

![Zugriff-auf-lokalen-Server-1.png](https://help.xentral.com/hc/article_attachments/4996368334492)

Im Anschluss ist xentral die angezeigte MyFritz-Adresse samt Passwort und Benutzer mitzuteilen, damit xentral per SSH helfen kann. Beispiel für eine HTTP bzw. HTTPS Weiterleitung:

![Zugriff-auf-lokalen-Server-2.png](https://help.xentral.com/hc/article_attachments/4996368358172)

![Zugriff-auf-lokalen-Server-3.png](https://help.xentral.com/hc/article_attachments/4996422373148)