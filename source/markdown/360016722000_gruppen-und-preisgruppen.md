Mithilfe des Moduls **Gruppen** kannst du in Xentral verschiedene Kunden und ihre Adressen zusammenfassen, zum Beispiel zur Vergabe gruppenspezifischer Preise oder Zahlungsbedingungen. Dabei gibt es zwei verschiedene Arten von Gruppen, die sich nach ihren Anwendungsfällen unterscheiden und in diesem Artikel beschrieben werden.

Gruppen kannst du für folgende Anwendungsfälle nutzen:

- Erstellung von Preisgruppen zur automatischen Rabattierung von Artikeln für bestimmte Kunden
- Preisgruppen erlauben in Kombination mit Online-Shops die Steuerung der zu übertragenden Preise
- Erstellung von Personengruppen zur Zusammenfassung verschiedener Adressen
- Pflege unterschiedlicher Verkaufspreise pro Gruppe

## Anwendungsfälle für Gruppen

Reguläre Gruppen dienen vor allem als Filter für gruppenspezifische Preise. Im Nachfolgenden findest du eine Auflistung der wichtigsten Module in Xentral, in denen du nach Gruppen filtern kannst.

- **Verkaufen > Adressen ** (Tab ** Übersicht**)
- **Verkaufen > Adressen ** (Tab ** Adressfilter**)
- **Verkaufen > Artikel > Artikel öffnen ** (Tab ** Einkauf **und Tab ** Verkauf**)

## Neue Gruppe anlegen

Gehe wie folgt vor, um eine neue Gruppe anzulegen.

1. Nutze die Smart Search, um das Modul **Gruppen** zu öffnen.
1. Klicke oben rechts auf **+ NEU**.
1. Nimm die Einstellungen für die Gruppe vor. Die folgende Tabelle enthält weitere Informationen zu den verfügbaren Einstellungen.
1. Klicke auf **Speichern**.

## Neue Preisgruppe anlegen

Wenn du beim[Anlegen einer Gruppe](#UUID-6fdd729a-0775-56f2-2827-7de59018e2a4_id_360016722000_id_toc-0)die Art **Preisgruppen** auswählst, stehen dir einige zusätzliche Einstellungsfelder zur Verfügung. Im Folgenden findest du genauere Informationen zu diesen Optionen.

| Einstellung | Erläuterung |
| --- | --- |
| **Grundrabatt **| Gib den Grundrabatt ** in %**ein. Dieser Grundrabatt wird im Kundenbeleg direkt in der Spalte ** Rabatt **angezeigt. Dieser Rabatt wird auch angewendet, wenn du bereits kundenspezfiische Preise über eine reguläre Gruppe (Auswahl der Art ** Gruppen** bei der Anlage) vergeben hast. |
| **Zahlungszieltage **| Gib das Zahlungsziel ** in Tagen** an, das für diese Preisgruppe gelten soll. Diese Information wird dann im Kundenbeleg entsprechend angezeigt. |
| **Skonto **| Gib den Skonto-Satz ** in %** an, der für diese Preisgruppe gelten soll. Diese Information wird dann im Kundenbeleg entsprechend angezeigt. |
| **Skonto Tage **| Gib die erlaubten ** Tage** für das Skonto an, die für diese Preisgruppe gelten sollen. Diese Information wird dann im Kundenbeleg entsprechend angezeigt. |
| **Porto frei aktiv** | Aktiviere diese Option, um ab einem bestimmten Auftragswert keine Versandkosten mehr in Rechnung zu stellen. |

## Adressen zu Gruppen hinzufügen

Nachdem du wie oben beschrieben Gruppen angelegt hast, fügst du diesen Gruppen die gewünschten Adressen hinzu. Dies können je nach Anwendungsfall Adressen deiner Kunden, aber auch Adressen von Lieferanten oder Mitarbeitern sein.

Gehe wie folgt vor, um Adressen manuell zu Gruppen hinzuzufügen.

1. Öffne das Menü **Verkaufen > Adressen**.
1. Öffne die gewünschte Adresse.
1. Öffne das Tab **Gruppen**.
1. Aktiviere die Checkbox links neben der gewünschten Gruppe, um die Adresse der Gruppe hinzuzufügen.

Wenn du eine größere Anzahl von Adressen hast, die du bestimmten Gruppen zuordnen möchtest, kannst du dafür einen CSV-Import nutzen. Weitere Informationen dazu findest du[in diesem Artikel](https://help.xentral.com/hc/de/articles/4539258872604#UUID-249d2cf9-7cac-e9fb-dbb9-48533915e23b).

## Praxisbeispiel: Versandkosten ab bestimmtem Auftragswert erlassen

Im Folgenden wird anhand eines Praxisbeispiels beschrieben, wie du mithilfe einer Gruppe der Art **Preisgruppe** ab einem Auftragswert von 50,00 € automatisch die Versandkosten aus einem Auftrag entfernen kannst.

1. Öffne das Menü **Einstellungen > Administration > Systemeinstellungen**.
1. Aktiviere im Bereich **Belege ** die Option **Porto berechnen**.
1. Klicke auf **Speichern**.
1. Nutze die Smart Search, um das Modul **Gruppen** zu öffnen.
1. Erstelle eine neue Gruppe der Art **Preisgruppe**. Vergib eine eindeutige Bezeichnung für die Preisgruppe, z.B. "Versandkostenfrei ab 50 €". Füge der Preisgruppe anschließend die gewünschten Adressen deiner Kunden hinzu.
1. Falls noch nicht vorhanden: Lege einen so genannten Portoartikel an. Aktiviere in den Stammdaten dieses Artikels zwingend die Option **Artikel ist Porto**.
1. Kontrolliere die Einstellungen der Adressen, die du der Preisgruppe hinzugefügt hast: Die Option **Zahlungskonditionen festschreiben ** im Tab **Zahlungskonditionen/Besteuerung ** der Adresse darf**nicht** aktiviert sein, da andernfalls die Einstellungen der Preisgruppe ignoriert werden.

Legst du nun einen Auftrag an, in dem ein Portoartikel erhalten ist, werden die Versandkosten für den Auftrag ab einem Netto-Warenwert von 50,00 € automatisch auf 0 gesetzt.