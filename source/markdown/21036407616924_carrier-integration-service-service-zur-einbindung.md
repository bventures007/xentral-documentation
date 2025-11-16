Mit dem Carrier Integration Service können Partner eigene Versanddienstleister (Carrier) direkt mit Xentral integrieren. Dies ermöglicht Unternehmen, maßgeschneiderte Logistiklösungen zu schaffen und spezifische Anforderungen an Versand, Steuerregeln und internationale Lieferungen abzubilden.

## Überblick & Möglichkeiten der Carrier-Integration

Es gibt zwei Wege, um Carrier ausserhalb des Xentral Standards zu integrieren:

- **API-Integration** (Direkte Anbindung über individuelle Schnittstellen)
- **Connect-Integration** (Geplante Erweiterung für native Carrier-Implementierungen in Xentral)

Beide Methoden ermöglichen es, Versandlabel zu generieren, Carrier-Services zu nutzen und Xentral um individuelle Versandoptionen zu erweitern.

### Achtung

Die Carrier-Integration deckt nicht alle Felder und Anforderungen sämtlicher Usecases ab. Je nach Zielsetzung – ob lediglich ein Versandlabel erzeugt oder ein komplexerer Prozess abgebildet werden soll – kann es notwendig sein, bestimmte Systemwerte an anderer Stelle über die API abzurufen.

Du solltest im Vorfeld entscheiden, ob du den gewünschten Workflow eher mit Connect innerhalb des Frameworks modellieren oder stattdessen ein eigenes Konstrukt über die API umsetzen möchtest. Beide Ansätze sind möglich – abhängig vom konkreten Usecase, aber auch davon, welche Technologie dir als Developer mehr liegt.

## Technischer Ablauf einer Carrier-Integration

Ein neu angebundener Carrier verhält sich wie ein bestehender Xentral-Carrier:

- **Authentifizierung** – Partner-Credentials werden hinterlegt, um die Carrier-API anzusprechen.
- **Konfiguration** – Nach der Authentifizierung werden Carrier-spezifische Felder automatisch geladen (z. B. Versandlabel-Optionen, Altersprüfung, zusätzliche Services).
- **Aufruf des Partner-Services** – Xentral sendet eine Anfrage an den Partner-Service, dieser generiert die Versanddaten (z. B. für UPS, Post Swiss).
- **Rückgabe der Versandinformationen** – Das Label und Tracking-Informationen werden an Xentral übermittelt und für den Kunden verfügbar gemacht.

Je nach Carrier können unterschiedliche Services (z. B. Expressversand, internationale Optionen) hinterlegt werden.

> **Anmerkung**
>
> In der Xentral Entwicklerdokumentation findest du alle Informationen zurCarrier-Integration.

## Nutzung für Endkunden

Sobald ein Partner einen Carrier erfolgreich integriert hat, funktioniert dieser nahtlos in Xentral:

- Carrier kann in Verkaufsaufträgen als Versanddienstleister gewählt werden.
- Automatische Label-Erstellung & Tracking-Informationen sind möglich.
- Je nach Anwendungsfall kann der Partner weitere Carrier-spezifische Funktionen bereitstellen.

Kunden, die einen bestimmten Carrier wünschen, können diesen über einen Partner-Request anfragen oder im Xentral Marketplace nach einer passenden Lösung suchen.

## Connect-Integration für eine skalierbare Lösung

> **Anmerkung**
>
> Während aktuell individuelle API-Integrationen umgesetzt werden, wird die Carrier-Integration mit Connect in Q2 getestet. Ziel ist es, dass Carrier direkt in Xentral als native Lösung eingebunden werden können, ohne manuelle Konfiguration von Service-URLs und Tokens.
>
> Dies bedeutet:
>
> - Bessere Skalierbarkeit für Partner
> - Einheitliche Carrier-Verwaltung in Xentral
> - Integration über den Xentral Marketplace

## Entwicklung & Zeithorizont (Stand 06/2025)

- Manuelle API-Integration ist bereits möglich – erste Carrier können in wenigen Wochen angebunden werden.
- Connect-Integration & native Carrier sind für Ende Q2/Q3 geplant.

### Achtung

Die Implementierung einer neuen Carrier-Anbindung erfordert technisches Know-how und kann je nach Komplexität variieren. Ein detailliertes Kickoff-Gespräch hilft, den Aufwand realistisch einzuschätzen.

## Fazit: Carrier-Service für Partner & Kunden

- Partner können eigene Carrier über API oder Connect in Xentral integrieren.
- Kunden erhalten eine erweiterte Carrier-Auswahl & flexible Versandoptionen.
- Die zukünftige Integration in den Xentral Marketplace erleichtert die Verwaltung und Nutzung.

> **Anmerkung**
>
> 🚀 Interesse an einer eigenen Carrier-Anbindung? Jetzt mit Xentral oder einem Partner abstimmen!