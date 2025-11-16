#!/usr/bin/env python3
"""
Markdown to HTML Generator
 
Dieses Tool konvertiert alle Markdown-Dateien aus dem markdown/ Ordner zu HTML im source/generated/ Ordner.
Es verwendet die bestehende MultiMarkdown-Funktionalität und erstellt eine komplette HTML-Dokumentation.
"""

import os
import sys
import shutil
import time
from pathlib import Path
from typing import List, Dict, Tuple
from tqdm import tqdm

# Import der bestehenden convert_markdown_file Funktionalität
sys.path.append(str(Path(__file__).parent / 'source'))
from markdown_to_html import convert_markdown_file


class MarkdownToHTMLGenerator:
    def __init__(self):
        """
        Initialisiert den Markdown zu HTML Generator.
        """
        # Verzeichnisse definieren
        self.base_dir = Path(__file__).parent
        self.markdown_base_dir = self.base_dir / "source"
        self.markdown_dir = self.markdown_base_dir / "markdown"  # Die .md Dateien liegen in markdown/markdown/
        self.generated_dir = self.markdown_base_dir / "generated"
        self.generated_images_dir = self.generated_dir / "images"
        self.original_images_dir = self.markdown_base_dir / "original" / "images"
        
        # Statistiken initialisieren
        self.stats = {
            'markdown_files_found': 0,
            'html_files_generated': 0,
            'conversion_errors': 0,
            'images_copied': 0,
            'image_copy_errors': 0,
            'total_processing_time': 0.0
        }
        
        print(f"Markdown zu HTML Generator")
        print(f"=" * 50)
        print(f"Quell-Verzeichnis: {self.markdown_dir}")
        print(f"Ziel-Verzeichnis: {self.generated_dir}")
        print(f"Bilder-Quelle: {self.original_images_dir}")
        print(f"Bilder-Ziel: {self.generated_images_dir}")
        print()

    def clear_generated_directory(self) -> None:
        """
        Löscht alle Dateien im generated/ Ordner (HTML-Dateien und Bilder komplett leeren).
        """
        print("🧹 Bereinige generated/ Ordner...")
        
        try:
            if self.generated_dir.exists():
                # Alle HTML-Dateien löschen
                html_files = list(self.generated_dir.glob('*.html'))
                for html_file in html_files:
                    try:
                        html_file.unlink()
                        print(f"  ✓ HTML gelöscht: {html_file.name}")
                    except Exception as e:
                        print(f"  ✗ Fehler beim Löschen von {html_file.name}: {e}")
                
                # Images-Ordner komplett leeren
                if self.generated_images_dir.exists():
                    try:
                        shutil.rmtree(self.generated_images_dir)
                        print(f"  ✓ Bilder-Ordner geleert: {self.generated_images_dir}")
                    except Exception as e:
                        print(f"  ✗ Fehler beim Leeren des Bilder-Ordners: {e}")
                
                print("✅ Generated-Ordner bereinigt")
            else:
                print("💡 Generated-Ordner existiert noch nicht")
                
        except Exception as e:
            print(f"✗ Fehler bei der Ordner-Bereinigung: {e}")
        
        print()

    def setup_directories(self) -> None:
        """
        Erstellt die notwendigen Verzeichnisse.
        """
        print("📁 Erstelle Verzeichnisse...")
        
        try:
            # Generated-Hauptordner erstellen
            self.generated_dir.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ Created: {self.generated_dir}")
            
            # Images-Unterordner erstellen
            self.generated_images_dir.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ Created: {self.generated_images_dir}")
            
            print("✅ Verzeichnisse erstellt")
            
        except Exception as e:
            print(f"✗ Fehler beim Erstellen der Verzeichnisse: {e}")
            raise
        
        print()

    def find_markdown_files(self) -> List[Path]:
        """
        Findet alle Markdown-Dateien im markdown/ Ordner (nur .md Dateien, nicht aus Unterordnern).
        
        Returns:
            Liste aller gefundenen Markdown-Dateien
        """
        print("🔍 Suche Markdown-Dateien...")
        
        if not self.markdown_dir.exists():
            print(f"✗ Markdown-Verzeichnis nicht gefunden: {self.markdown_dir}")
            return []
        
        # Nur .md Dateien direkt im markdown/ Ordner (nicht in Unterordnern)
        markdown_files = [f for f in self.markdown_dir.glob('*.md') if f.is_file()]
        
        self.stats['markdown_files_found'] = len(markdown_files)
        
        if markdown_files:
            print(f"✅ {len(markdown_files)} Markdown-Dateien gefunden")
            for md_file in sorted(markdown_files)[:5]:  # Ersten 5 anzeigen
                print(f"  📄 {md_file.name}")
            if len(markdown_files) > 5:
                print(f"  ... und {len(markdown_files) - 5} weitere")
        else:
            print("⚠️  Keine Markdown-Dateien gefunden")
        
        print()
        return sorted(markdown_files)

    def copy_images(self) -> None:
        """
        Kopiert Bilder von markdown/original/images/ nach markdown/generated/images/.
        """
        print("🖼️  Kopiere Bilder...")
        
        if not self.original_images_dir.exists():
            print(f"💡 Bilder-Quellordner existiert nicht: {self.original_images_dir}")
            print()
            return
        
        # Alle Bild-Dateien finden
        image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.webp', '*.bmp', '*.tiff']
        image_files = []
        
        for extension in image_extensions:
            image_files.extend(self.original_images_dir.glob(extension))
        
        if not image_files:
            print("💡 Keine Bilder zum Kopieren gefunden")
            print()
            return
        
        print(f"📸 {len(image_files)} Bilder gefunden")
        
        # Bilder kopieren mit Progress Bar
        copied_count = 0
        error_count = 0
        
        for image_file in tqdm(image_files, desc="Kopiere Bilder", unit="Datei"):
            try:
                destination = self.generated_images_dir / image_file.name
                shutil.copy2(image_file, destination)
                copied_count += 1
                
            except Exception as e:
                print(f"  ✗ Fehler beim Kopieren von {image_file.name}: {e}")
                error_count += 1
        
        self.stats['images_copied'] = copied_count
        self.stats['image_copy_errors'] = error_count
        
        if copied_count > 0:
            print(f"✅ {copied_count} Bilder erfolgreich kopiert")
        if error_count > 0:
            print(f"⚠️  {error_count} Bilder konnten nicht kopiert werden")
        
        print()

    def convert_markdown_to_html(self, markdown_files: List[Path]) -> None:
        """
        Konvertiert alle Markdown-Dateien zu HTML unter Verwendung der bestehenden Funktionalität.
        
        Args:
            markdown_files: Liste der zu konvertierenden Markdown-Dateien
        """
        if not markdown_files:
            print("⚠️  Keine Markdown-Dateien zum Konvertieren")
            return
        
        print(f"🔄 Konvertiere {len(markdown_files)} Markdown-Dateien zu HTML...")
        print()
        
        success_count = 0
        error_count = 0
        
        # Konvertierung mit Progress Bar
        for markdown_file in tqdm(markdown_files, desc="Konvertiere Dateien", unit="Datei"):
            try:
                # Ziel-HTML-Datei bestimmen (gleiche Namenskonvention: 12345_title.md -> 12345_title.html)
                html_filename = f"{markdown_file.stem}.html"
                html_path = self.generated_dir / html_filename
                
                # Bestehende convert_markdown_file Funktion verwenden
                conversion_success = convert_markdown_file(markdown_file, html_path)
                
                if conversion_success:
                    success_count += 1
                    print(f"  ✅ {markdown_file.name} → {html_filename}")
                else:
                    error_count += 1
                    print(f"  ✗ Fehler bei: {markdown_file.name}")
                    
            except Exception as e:
                error_count += 1
                print(f"  ✗ Unerwarteter Fehler bei {markdown_file.name}: {e}")
        
        self.stats['html_files_generated'] = success_count
        self.stats['conversion_errors'] = error_count
        
        print()
        if success_count > 0:
            print(f"✅ {success_count} HTML-Dateien erfolgreich generiert")
        if error_count > 0:
            print(f"⚠️  {error_count} Konvertierungen fehlgeschlagen")
        print()

    def generate_index_html(self) -> None:
        """
        Erstellt eine Index-HTML-Datei mit Links zu allen generierten HTML-Dateien.
        """
        print("📋 Erstelle Index-Datei...")
        
        try:
            # Alle generierten HTML-Dateien finden
            html_files = sorted(self.generated_dir.glob('*.html'))
            
            if not html_files:
                print("💡 Keine HTML-Dateien für Index gefunden")
                return
            
            # Index-HTML erstellen
            index_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xentral Dokumentation - Übersicht</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fafafa;
            color: #333;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .stats {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .file-list {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .file-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #e2e8f0;
            transition: background-color 0.2s;
        }}
        .file-item:hover {{
            background-color: #f7fafc;
        }}
        .file-item a {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }}
        .file-item a:hover {{
            text-decoration: underline;
        }}
        .file-info {{
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📚 Xentral Dokumentation</h1>
        <p>Generierte HTML-Dokumentation aus Markdown-Dateien</p>
    </div>
    
    <div class="stats">
        <h2>📊 Statistiken</h2>
        <p><strong>Generiert am:</strong> {time.strftime('%d.%m.%Y %H:%M:%S')}</p>
        <p><strong>Markdown-Dateien gefunden:</strong> {self.stats['markdown_files_found']}</p>
        <p><strong>HTML-Dateien generiert:</strong> {self.stats['html_files_generated']}</p>
        <p><strong>Bilder kopiert:</strong> {self.stats['images_copied']}</p>
        <p><strong>Verarbeitungszeit:</strong> {self.stats['total_processing_time']:.2f} Sekunden</p>
    </div>
    
    <div class="file-list">
        <h2>📄 Verfügbare Dokumente ({len(html_files)})</h2>
"""
            
            # Links zu allen HTML-Dateien hinzufügen
            for html_file in html_files:
                # Titel aus Dateiname ableiten
                title = html_file.stem.replace('_', ' ').replace('-', ' ').title()
                
                # Datei-Info (Größe, Datum) ermitteln
                try:
                    file_stat = html_file.stat()
                    file_size_kb = file_stat.st_size / 1024
                    file_date = time.strftime('%d.%m.%Y', time.localtime(file_stat.st_mtime))
                    file_info = f"{file_size_kb:.1f} KB • {file_date}"
                except:
                    file_info = "Info nicht verfügbar"
                
                index_content += f"""
        <div class="file-item">
            <a href="{html_file.name}">{title}</a>
            <span class="file-info">{file_info}</span>
        </div>"""
            
            index_content += """
    </div>
</body>
</html>"""
            
            # Index-Datei speichern
            index_path = self.generated_dir / "index.html"
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
            
            print(f"✅ Index erstellt: {index_path}")
            
        except Exception as e:
            print(f"✗ Fehler beim Erstellen der Index-Datei: {e}")
        
        print()

    def print_final_summary(self) -> None:
        """
        Gibt eine finale Zusammenfassung aller Operationen aus.
        """
        print("=" * 50)
        print("🎉 KONVERTIERUNG ABGESCHLOSSEN")
        print("=" * 50)
        print()
        
        print("📊 STATISTIKEN:")
        print(f"  • Markdown-Dateien gefunden: {self.stats['markdown_files_found']}")
        print(f"  • HTML-Dateien generiert: {self.stats['html_files_generated']}")
        print(f"  • Konvertierungsfehler: {self.stats['conversion_errors']}")
        print(f"  • Bilder kopiert: {self.stats['images_copied']}")
        print(f"  • Bild-Kopierfehler: {self.stats['image_copy_errors']}")
        print(f"  • Gesamtzeit: {self.stats['total_processing_time']:.2f} Sekunden")
        print()
        
        print("📁 OUTPUT-VERZEICHNISSE:")
        print(f"  • HTML-Dateien: {self.generated_dir}")
        print(f"  • Bilder: {self.generated_images_dir}")
        print()
        
        if self.stats['html_files_generated'] > 0:
            print("🌐 NÄCHSTE SCHRITTE:")
            print(f"  • Öffnen Sie {self.generated_dir / 'index.html'} in Ihrem Browser")
            print("  • Die HTML-Dateien können direkt verwendet werden")
            print()
        
        # Erfolgsrate berechnen
        if self.stats['markdown_files_found'] > 0:
            success_rate = (self.stats['html_files_generated'] / self.stats['markdown_files_found']) * 100
            if success_rate == 100:
                print("✅ Alle Dateien erfolgreich konvertiert!")
            elif success_rate >= 80:
                print(f"✅ {success_rate:.1f}% erfolgreich konvertiert")
            else:
                print(f"⚠️  Nur {success_rate:.1f}% erfolgreich konvertiert")
        
        print()

    def run(self) -> None:
        """
        Führt den kompletten Markdown-zu-HTML-Generierungsprozess aus.
        """
        start_time = time.time()
        
        try:
            # 1. Generated-Ordner leeren
            self.clear_generated_directory()
            
            # 2. Verzeichnisse erstellen
            self.setup_directories()
            
            # 3. Markdown-Dateien finden
            markdown_files = self.find_markdown_files()
            
            if not markdown_files:
                print("🚫 Keine Markdown-Dateien gefunden. Prozess beendet.")
                return
            
            # 4. Bilder kopieren
            self.copy_images()
            
            # 5. Markdown zu HTML konvertieren
            self.convert_markdown_to_html(markdown_files)
            
            # 6. Index-HTML erstellen
            self.generate_index_html()
            
            # 7. Zeitmessung
            end_time = time.time()
            self.stats['total_processing_time'] = end_time - start_time
            
            # 8. Finale Zusammenfassung
            self.print_final_summary()
            
        except KeyboardInterrupt:
            print("\n⏹️  Prozess durch Benutzer abgebrochen")
        except Exception as e:
            print(f"\n❌ Unerwarteter Fehler: {e}")
            raise


def main():
    """
    Hauptfunktion - Startet den Markdown-zu-HTML-Generator.
    """
    try:
        generator = MarkdownToHTMLGenerator()
        generator.run()
        
    except KeyboardInterrupt:
        print("\nProzess abgebrochen.")
    except Exception as e:
        print(f"Kritischer Fehler: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
