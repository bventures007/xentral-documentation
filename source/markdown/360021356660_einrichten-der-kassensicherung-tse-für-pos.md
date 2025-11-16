Die Technische Sicherungseinrichtung (TSE) zur Kasse im Xentral ERP-System (sog. Point-of-Sale “POS”) kann in wenigen Schritten durch den Anwender selbst eingerichtet werden. Die gesetzliche Anforderung schreibt vor, dass dabei jedes Kassensystem einzeln erfasst/ registriert wird. Das Modul ist nur für Kunden in Deutschland (KassenSichV) relevant.

> **Anmerkung**
>
> Bitte setze dich mit deinem xentral-Ansprechpartner in Verbindung und teile die exakte Anzahl deiner POS mit, damit die Kollegen entsprechende Einstellungen im System hinterlegen können und die Einrichtung deines xentral-Systems reibungslos geschehen kann.Da die Kassensicherung erst ab Version 20.3 enthalten sein wird, sprich bitte dies ggf. an, falls du nicht sicher bist, ob deine aktuelle Lizenz die Nutzung dieser Version erlaubt (z. B. Kauflizenz nur bis Version 20.2)

## Voraussetzungen

1. Xentral Cloud-Kunde (ggf. ist ein Wechsel auf die Xentral Cloud notwendig)
1. Benötigte Anzahl POS-Lizenzen geordert (eine pro betriebenes Kassensystem)
1. POS im Xentral-System eingerichtet

## Fiskaly Modul in Xentral installieren und einrichten

Gehe in deinen xentral Appstore oder über die SuperSearch und suche nach dem Modul “Fiskaly Anbindung”.

### Neue Organisation anlegen

Neue Organisation per Button rechts anlegen

![SetupTSE1.png](https://help.xentral.com/hc/article_attachments/19053523569052)

Mache nun Grundangaben zur Organisation. Hier müssen die Adressangaben des Firmensitzes bzw. des Kassenstandorts gepflegt werden.

Klicke auf den Button Anlegen/Speichern. Die Organisation erschein nun in der Liste der Organisationen.

### Zusätzlich Organisationen anlegen (optional)

Du kannst weitere Organisationen anlegen, wenn du z.B. verschiedene Betriebsstätten hast, d.h. unterschiedliche Orte, an welchen eine oder mehrere Kassen betrieben werden.

### TSE einrichten

Wechsle nun in den Reiter TSE. Lege hier über den Button *Neue TSE einrichten* eine neue TSE an.

![SetupTSE2.png](https://help.xentral.com/hc/article_attachments/19053462439324)

Gib nun das Xentral Projekt/ POS an, für welche du die TSE erstellen möchte, sowie die Organisation/ Standort der Kasse (die im vorherigen Schritt angelegten Organisationen). Die unteren beiden Felder frei lassen, diese füllen sich im Folgeschrittautomatisch. Klicke auf Neue TSE und bestätige im darauffolgenden Fenster das Anlegen.

Damit werden automatisch TSE und Client hinterlegt.

![SetupTSE3.png](https://help.xentral.com/hc/article_attachments/19053462442908)

## Projekteinstellungen

Gehe in die POS Einstellungen zu Stammdaten -> Projekt -> Einstellungen -> POS Einstellungen.

![SetupTSE4.png](https://help.xentral.com/hc/article_attachments/19053462445084)

Die Adresse muss zwingend im Bereich *Bondrucker* hinterlegt sein.

- Bei Rechnungsausdruck immer auch Quittung ausdrucken: Option kann aktiviert sein.
- QR-Code drucken: Option kann aktiviert sein. Falls ein echter Bondrucker im Einsatz ist (“Adapterbox” Modul genutzt), ist dieser hier aktiviert. Falls kein Bondrucker genutzt wird, ist TSE/ Bon-Erzeugung(PDF) trotzdem immer wirksam

## Anträge und Stellungnahmen für das Finanzamt

Zum Stichtag 31.03.2021 für die Umsetzung der Kassensicherung (TSE) gabe es noch keinen finalen Stand. Unklarheiten, die der Gesetzgeber selbst bisher nicht auflösen konnte, verhindern die Bereitstellung der finalen Lösung gegenwärtig noch für alle Crypto-Service-Providers (CSPs), auf die sich Anbieter wie xentral ERP weiter stützen können bzw. müssen.

Nach Rücksprache mit dem CSP unserer Wahl, der im ständigen Austausch steht mit den Landesministerien bzw. dem Bundesministerium für Finanzen, den Finanzämtern, sowie dem Bundesamt für Sicherheit in der Informationstechnik (BSI), befinden sich diese maßgeblichen Behörden noch in Klärung zu einigen offenen Punkten. Wir empfehlen dir in jedem Fall dringend, den Individualantrag nach §148 Abgabenordnung (Ao) ggf. zusammen mit deinem Steuerberater auszufüllen und an das zuständiges Finanzamt zu senden (zusammen mit Stellungnahme fiskaly, Stellungnahme xentral, Schreiben an Länder, Zertifizierung fiskaly), um gegen evtl. Strafen vorzubeugen.

- [Allgemeiner Antrag § 148 AO](https://hl.t.hubspotemail.net/e2t/tc/VWXZT04q_cKKW2htd3z1lYNWPW31NlPp4pRB6qN5_C1nk5kbVBV3Zsc37CgTFQW4qYv6n6y8BY3W7FXL3n2r1nXVMf273q-HWG5W2RyhHf8gdcJRW14GXKF5DjQmRW8gHz4z6CKCyJW6LrDfk7Xx55wW6zdY5M8HZ52vW2zTf5F2_wzWfW9c4tmd9c0wMWW8KRMw718sVDCW4QWZDG9jW2Q4VVG2lz6-CD9sW1x8H_x5nZck1W4chXPt71KQ_9W1NGQGY3_j6Q9W23vBCN15m3vHVKVJlp9c5zWnW2yK_Lw2j3VdgW2RYGFX3dDDqkW7v_s5G1x3jTSVTZmmT4PNbxgW4xRClS4t4-q_W64tSlw3dhCbnVlCj3D86LQt2W8z6jp97pz_mLW7xkqp_1J_fFpW6v1ytY1ttGXRW5rLh5h5bxscSW275Cwl958Q14W5Hq2JB3F-zVvW5YHr5x7ZPMY2W8-xGC04qW7gpW5NJn2C1qpFVmW4__V2C1stl9WVRftGH4PFkhXW8JVMyl5txb5sW73KKJf6tZsDvW5tZbfL2wJ5MFW3VVJ3f7tkfT0W6P16qQ10dl4XW6FgjCc4SQ-Yq3hCF1)
- [Zertifikat fiskaly GmbH](https://hl.t.hubspotemail.net/e2t/tc/VWXZT04q_cKKW2htd3z1lYNWPW31NlPp4pRB6qN5_C1nk3lGnpV1-WJV7CgNK6W5rt9RS3gqNDQW6mrXRj62dVcGVLQQDQ1cc1M3W7vsjj174pZbcN7H-xCn15_wsW53LWhy7kXqq6W7Y4vj24cdRWMW12bsTv8TQh0xW2mF1JB17Fx1_VFbklg32s41wW1tDXbR5VDnyNW5ssKhX3VTtgLV2L6zd2G8lnYW2bTdf93qKHygW7Q7kSk1PDYXFW3lwly95_C83fW8RB0Fp6GwcTfW4yTJXB1p83sgW1-CsGZ5zpKyLW6--4lr4CkHpRW4zZrTV1ZDKs6W46MTMb5gX-65W53NF0h4P8XYBW70WqYB7JtgCfW1mrSNS3xc8qTW93sFM7714_B23fkh1)
- [Schreiben an die Bundesländer TSE Anlage](https://hl.t.hubspotemail.net/e2t/tc/VWXZT04q_cKKW2htd3z1lYNWPW31NlPp4pRB6qN5_C1mL5kbT_V3Zsc37CgzJLW3wZB0C27y0lvW5l094v2hDwPwW6_pwjH7Fv7qcW2ScPMb56ZCY8W98ygnn6SSKMPN3-9w-nNnH5MN4F9PTdmpj7_W93RHs8675gZMN3MMjnY6b8L-VR_6bS4kFjcKW7QQB3D2W8C2gW6cmTKn5ZrVZ2W7qnx1X5Dhm1DVTfCGY2yK96bW8ZdJyJ71NtzPW69JyHg4F40NBN8bFsYjkS3_SW43WDgB8h2B5TW2HN6JY31ttpKW3pvLN32HhVGgW3fWkSD6fMr0FW8tLxBh62SR6WW3stGfS2HjbVnW51Fm1q6tHB4GVGKqBh35rFdDW1VFDvb4Tf4wcW6Q1lVg316CJ1W4GtrNv3NjmCnW9hsM8r181SsGW64yHJM5Q3PgqN17bnYBwC2gBW58cQzN7Wdgm3VkJlH47YfjmfW8G52td58hlQHW3B5fh14CDtPpW8hVyFv6bnJcjW6y7r85626gKgV715QW8nYJnJ3hhw1)
- [Stellungnahme Zertifizierung fiskaly](https://hl.t.hubspotemail.net/e2t/tc/VWXZT04q_cKKW2htd3z1lYNWPW31NlPp4pRB6qN5_C1lS5kbT5V3Zsc37CgCPHW4LpVpf1c2yLsW2_7tgT5QkYZ7W56kwGk31Fh9JW1XM21r4YRyyyM3gH1Yds5mFW4JqCdx1-7v8YW81lMYW4-JSzsW8-3FCG54n5pVW4kWg-58wJsSXW3HVKB44dK8fHW1jyJbG7j0Q8cW2l-SZ-8mVl52W4N7TFJ7zG4ZLW5yqsgB2vJzcXW4-FPsK1HCPnCW6WY86w8nGST_W6gD7Fb7By3yMN2W2X23vGf64W9hLGXW5-3TQvW3hsRgQ8-QY85W3nSXT1516KxTW2r38xT1FT2g0VdKCw51zjf74W3vJ1Fk10JJCCW3lpM533XlGg2W44F7gV3QwwPqW6DPddB8CGZFhW8YVWCQ8hvhtxW2cp9c03stSFDW3jMX8W4gK7J8W3lRQfn6jKnBwVsM25k43w6ST39Rv1)
- [Statement Kassenhersteller](https://hl.t.hubspotemail.net/e2t/tc/VWXZT04q_cKKW2htd3z1lYNWPW31NlPp4pRB6qN5_C1nk3lGnpV1-WJV7CgJMYW7Dx7VM2z1_f_W25q8HC7H4LrKW7N6K3M8Gh2DmW2D5BvV4Dz-r1W6n96SS57HKJSW9cxY_-3CZTSbW1M4QGQ5Jjxw5MqvYpjFLYPZW4zqcPw8nj4JSW2xHmP44JpxyRW4YFT8B2k1sl-W5XyYV87Vmp5mW2zZVlW1VrhMlW5_7VVZ6zrQS9N2g7QJ6w3qCtN42NwGVGQ19xW86yTPT8PNtlKW4y2WWf6Qv2N3VLvlH013x2-dW11Gwh-6ZN-SzW10lnp-2qb-BLW417gx13yyvfjW42Vkxg1x6lh2W4Fc_1m3b6tJGW4b0Trn1Ny-sxVC00WG4ftqs7388-1)

## FAQ

### Wie melde ich mein Xentral POS-Kassensystem und die TSE korrekt beim Finanzamt an? (07/2025)

Ab dem 1. Januar 2025 gilt in Deutschland die gesetzliche Pflicht, jedes elektronische Kassensystem inklusive der zugehörigen technischen Sicherheitseinrichtung (TSE) beim zuständigen Finanzamt zu melden (§ 146a Abs. 4 AO). Diese Regelung betrifft auch Nutzer:innen von Xentral POS.

Da Xentral POS mit der zertifizierten Fiskaly Cloud-TSE arbeitet, sind die für die Meldung erforderlichen Angaben (z. B. Seriennummer des POS-Systems und der TSE) nicht direkt in der Oberfläche sichtbar. **Bitte kontaktiere unser Support-Team, um die entsprechenden Daten rechtzeitig und vollständig zu erhalten.**

Für Kassensysteme, die bereits vor dem 1. Januar 2025 im Einsatz sind, muss die Meldung bis spätestens 31. Juli 2025 erfolgen. Wichtig: Die Verantwortung für die fristgerechte Meldung liegt beim Unternehmen, also bei dir als Betreiber des Kassensystems.

Die Zertifizierungs-ID der eingesetzten TSE (Fiskaly Cloud-TSE) findest du hier:[BSI-Zertifikat einsehen](https://www.bsi.bund.de/SharedDocs/Zertifikate_TR/Technische_Sicherheitseinrichtungen/BSI-K-TR-0403-2021.html).

*Weitere Informationen zur Meldung und eine Ausfüllhilfe stellt das Bundesfinanzministerium auf seinen Seiten zur Verfügung.*

### Kann ich immer noch Pflichtfelder ab 250 EUR Kleinbetrag mit Dummy-Angaben bei fiskaly "kurzschließen"?

Ja, das "Kurzschließen" mit den Dummy-Angaben funktioniert nach wie vor.

Weitere Informationen dazu findest du hier:

[https://developer.fiskaly.com/](https://developer.fiskaly.com/)

[https://developer.fiskaly.com/api/dsfinvk/v0/](https://developer.fiskaly.com/api/dsfinvk/v0/)

### Kann ich die von fiskaly angebotene Lösung für AT nutzen?

Nein, das ist aktuell leider nicht möglich.

### Wie gelange ich zu den archivierten Kassenbons?

Grundsätzlich archivieren wir alle Transaktionen und Datenexporte wie die DSFinV-K. Aus diesen Daten kannst du dann die Kassenbons rekonstruieren.

Die Kassenbons an sich archivieren wir aber nicht. Du kannst sie dennoch ggf. in deinem System archivieren.

### In welcher einheitlichen Schnittstelle kann ich im Falle einer Betriebsprüfung dem Prüfer die Daten in fiskaly zur Verfügung stellen?

Grundsätzlich ist diese einheitliche Schnittstelle in den offiziellen DSFinV-K Dokumenten definiert. Welche standardisierte Prüfsoftware von den Finanzverwaltungen zur Prüfung der Datensätze benutzt wird, ist Stand heute noch nicht final. Wende dich dazu an dein zuständiges Finanzamt. Informationen findest du[hier](https://www.bzst.de/SharedDocs/Downloads/DE/Aussenpruefung/dsfinv_k_v_2_2.zip;jsessionid=14CBEEE96B86556DA54BDD979AE898CC.live6831?__blob=publicationFile&v=4).