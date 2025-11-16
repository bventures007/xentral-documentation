#!/usr/bin/env python3
"""
HTML to Markdown Batch Converter
Konvertiert alle HTML-Dateien aus source/original/ zu Markdown-Dateien in markdown/

Dieses Tool:
1. Löscht alle bestehenden .md Dateien im markdown/ Ordner
2. Durchgeht alle HTML-Dateien in markdown/original/
3. Konvertiert sie mit der bestehenden html_to_markdown.py Funktionalität
4. Erstellt entsprechende .md Dateien im markdown/ Ordner
5. Zeigt Progress-Informationen und Statistiken an
"""

import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple
from tqdm import tqdm

# Import der bestehenden Konvertierungsfunktion
sys.path.append(str(Path(__file__).parent / 'source'))
from html_to_markdown import html_to_markdown


class HTMLToMarkdownConverter:
    def __init__(self):
        """
        Initialisiert den HTML to Markdown Batch Converter.
        """
        # Verzeichnisse definieren
        self.base_dir = Path(__file__).parent
        self.markdown_dir = self.base_dir / "source"
        self.original_html_dir = self.markdown_dir / "original"
        self.output_markdown_dir = self.markdown_dir / "markdown"
        
        # Statistiken initialisieren
        self.stats = {
            'files_found': 0,
            'files_converted': 0,
            'files_failed': 0,
            'files_deleted': 0,
            'conversion_errors': []
        }
        
        print(f"HTML to Markdown Batch Converter")
        print(f"=" * 50)
        print(f"Eingabe-Verzeichnis: {self.original_html_dir}")
        print(f"Ausgabe-Verzeichnis: {self.output_markdown_dir}")
        print(f"Markdown-Ordner: {self.markdown_dir}")

    def validate_directories(self) -> bool:
        """
        Überprüft, ob die erforderlichen Verzeichnisse existieren.
        
        Returns:
            True wenn alle Verzeichnisse vorhanden sind, False sonst
        """
        if not self.original_html_dir.exists():
            print(f"✗ Fehler: Verzeichnis {self.original_html_dir} existiert nicht!")
            return False
        
        if not self.markdown_dir.exists():
            print(f"✗ Fehler: Verzeichnis {self.markdown_dir} existiert nicht!")
            return False
        
        # Output-Verzeichnis erstellen falls es nicht existiert
        self.output_markdown_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"✓ Verzeichnisse validiert")
        return True

    def clear_existing_markdown_files(self) -> None:
        """
        Löscht alle bestehenden .md Dateien im markdown/ Ordner (nicht in Unterordnern).
        """
        print("\nLösche bestehende Markdown-Dateien...")
        
        # Nur .md Dateien direkt im markdown/ Ordner löschen
        md_files = list(self.markdown_dir.glob('*.md'))
        
        if not md_files:
            print("  Keine .md Dateien zum Löschen gefunden")
            return
        
        for md_file in md_files:
            try:
                md_file.unlink()
                self.stats['files_deleted'] += 1
                print(f"  ✓ Gelöscht: {md_file.name}")
            except Exception as e:
                print(f"  ✗ Fehler beim Löschen von {md_file.name}: {e}")
        
        print(f"✓ {self.stats['files_deleted']} Markdown-Dateien gelöscht")

    def find_html_files(self) -> List[Path]:
        """
        Findet alle HTML-Dateien im original/ Verzeichnis.
        
        Returns:
            Liste aller gefundenen HTML-Dateien
        """
        print("\nSuche HTML-Dateien...")
        
        html_files = list(self.original_html_dir.glob('*.html'))
        html_files.sort()  # Alphabetisch sortieren für konsistente Reihenfolge
        
        self.stats['files_found'] = len(html_files)
        print(f"✓ {len(html_files)} HTML-Dateien gefunden")
        
        if len(html_files) == 0:
            print("  Keine HTML-Dateien zum Konvertieren gefunden!")
        
        return html_files

    def convert_html_to_markdown(self, html_file: Path) -> Tuple[bool, str]:
        """
        Konvertiert eine einzelne HTML-Datei zu Markdown.
        
        Args:
            html_file: Pfad zur HTML-Datei
            
        Returns:
            Tuple (success: bool, error_message: str)
        """
        try:
            # Output-Dateiname erstellen (gleiche Namenskonvention)
            markdown_filename = f"{html_file.stem}.md"
            output_path = self.output_markdown_dir / markdown_filename
            
            # HTML-Datei lesen
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # HTML zu Markdown konvertieren mit bestehender Funktion
            markdown_content = html_to_markdown(html_content)
            
            # Markdown-Datei schreiben
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            return True, ""
            
        except Exception as e:
            error_msg = f"Fehler bei {html_file.name}: {str(e)}"
            return False, error_msg

    def convert_all_files(self, html_files: List[Path]) -> None:
        """
        Konvertiert alle HTML-Dateien zu Markdown mit Progress-Anzeige.
        
        Args:
            html_files: Liste der zu konvertierenden HTML-Dateien
        """
        if not html_files:
            return
        
        print(f"\nStarte Konvertierung von {len(html_files)} Dateien...")
        start_time = time.time()
        
        # Progress Bar für die Konvertierung
        with tqdm(html_files, desc="Konvertiere HTML zu Markdown", unit="Datei") as pbar:
            for html_file in pbar:
                # Aktuellen Dateinamen in der Progress Bar anzeigen
                pbar.set_postfix({"Datei": html_file.name[:30] + "..." if len(html_file.name) > 30 else html_file.name})
                
                success, error_msg = self.convert_html_to_markdown(html_file)
                
                if success:
                    self.stats['files_converted'] += 1
                    # Kurze Bestätigung (nicht für jede Datei einzeln)
                else:
                    self.stats['files_failed'] += 1
                    self.stats['conversion_errors'].append(error_msg)
                    print(f"\n  ✗ {error_msg}")
                
                # Kurze Pause um Terminal-Output lesbar zu halten
                time.sleep(0.01)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n✓ Konvertierung abgeschlossen in {duration:.2f} Sekunden")

    def print_detailed_errors(self) -> None:
        """
        Gibt detaillierte Fehlermeldungen aus, falls vorhanden.
        """
        if self.stats['conversion_errors']:
            print(f"\n{'='*50}")
            print("DETAILLIERTE FEHLERMELDUNGEN:")
            print(f"{'='*50}")
            for i, error in enumerate(self.stats['conversion_errors'], 1):
                print(f"{i}. {error}")

    def print_summary(self) -> None:
        """
        Gibt eine ausführliche Zusammenfassung der Konvertierung aus.
        """
        print(f"\n{'='*50}")
        print("KONVERTIERUNGS-ZUSAMMENFASSUNG")
        print(f"{'='*50}")
        print(f"HTML-Dateien gefunden:        {self.stats['files_found']:>6}")
        print(f"Erfolgreich konvertiert:      {self.stats['files_converted']:>6}")
        print(f"Fehlgeschlagen:               {self.stats['files_failed']:>6}")
        print(f"Alte .md Dateien gelöscht:    {self.stats['files_deleted']:>6}")
        print(f"{'='*50}")
        
        # Erfolgsrate berechnen
        if self.stats['files_found'] > 0:
            success_rate = (self.stats['files_converted'] / self.stats['files_found']) * 100
            print(f"Erfolgsrate:                  {success_rate:>5.1f}%")
        else:
            print(f"Erfolgsrate:                    0.0%")
        
        # Status-Meldung
        if self.stats['files_failed'] == 0:
            print(f"\n🎉 Alle Dateien erfolgreich konvertiert!")
        elif self.stats['files_converted'] > 0:
            print(f"\n⚠️  Konvertierung mit {self.stats['files_failed']} Fehlern abgeschlossen")
        else:
            print(f"\n❌ Konvertierung fehlgeschlagen - keine Dateien konvertiert")
        
        # Ausgabe-Informationen
        if self.stats['files_converted'] > 0:
            print(f"\n📁 Markdown-Dateien gespeichert in:")
            print(f"   {self.output_markdown_dir}")
        
        # Detaillierte Fehler anzeigen
        if self.stats['files_failed'] > 0:
            self.print_detailed_errors()

    def run(self) -> None:
        """
        Führt den kompletten Batch-Konvertierungsprozess aus.
        """
        try:
            # 1. Verzeichnisse validieren
            if not self.validate_directories():
                return
            
            # 2. Bestehende .md Dateien löschen
            self.clear_existing_markdown_files()
            
            # 3. HTML-Dateien finden
            html_files = self.find_html_files()
            
            if not html_files:
                print("\n❌ Keine HTML-Dateien gefunden - Abbruch")
                return
            
            # 4. Alle Dateien konvertieren
            self.convert_all_files(html_files)
            
            # 5. Zusammenfassung ausgeben
            self.print_summary()
            
        except KeyboardInterrupt:
            print("\n\n❌ Konvertierung durch Benutzer abgebrochen")
            self.print_summary()
        except Exception as e:
            print(f"\n❌ Unerwarteter Fehler: {e}")
            self.print_summary()


def main():
    """
    Hauptfunktion - Startet die Batch-Konvertierung von HTML zu Markdown.
    """
    converter = HTMLToMarkdownConverter()
    converter.run()


if __name__ == "__main__":
    main()
