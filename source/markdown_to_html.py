#!/usr/bin/env python3
"""
Markdown to HTML Converter (MultiMarkdown)
Konvertiert Markdown-Dateien aus dem markdown/ Ordner zu HTML im generated/ Ordner
Verwendet die MultiMarkdown-Bibliothek für erweiterte Markdown-Features
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
import markdown

def preprocess_malformed_markdown(markdown_content):
    """Bereinigt häufige Markdown-Formatierungsfehler"""
    
    # UMFASSENDE BOLD-TEXT BEREINIGUNG - alle ** Varianten behandeln
    
    # 1. Zuerst alle malformed patterns normalisieren
    # ** text** -> **text**
    markdown_content = re.sub(r'\*\* ([^*]+?)\*\*', r'**\1**', markdown_content)
    # **text ** -> **text**
    markdown_content = re.sub(r'\*\*([^*]+?) \*\*', r'**\1**', markdown_content)
    # ** text ** -> **text**
    markdown_content = re.sub(r'\*\* ([^*]+?) \*\*', r'**\1**', markdown_content)
    
    # 2. Spezielle Tabellen-Patterns
    markdown_content = re.sub(r'\*\*([^*]+?) \*\*\|', r'**\1**|', markdown_content)
    markdown_content = re.sub(r'\|\*\* ([^*]+?)\*\*', r'|**\1**', markdown_content)
    
    # 3. KRITISCH: Alle ** patterns finden und durch HTML mit korrekten Leerzeichen ersetzen
    def fix_bold_patterns(text):
        # Alle ** Patterns sammeln und durch <strong> mit Spacing ersetzen
        patterns_to_fix = [
            # Wort**text**Wort -> Wort <strong>text</strong> Wort
            (r'([a-zA-ZÄÖÜäöüßА-я0-9])\*\*([^*\n]+?)\*\*([a-zA-ZÄÖÜäöüßА-я0-9])', r'\1 <strong>\2</strong> \3'),
            # Wort**text** -> Wort <strong>text</strong>
            (r'([a-zA-ZÄÖÜäöüßА-я0-9])\*\*([^*\n]+?)\*\*', r'\1 <strong>\2</strong>'),
            # **text**Wort -> <strong>text</strong> Wort
            (r'\*\*([^*\n]+?)\*\*([a-zA-ZÄÖÜäöüßА-я0-9])', r'<strong>\1</strong> \2'),
            # Standard patterns (mit Leerzeichen drum herum)
            (r'\*\*([^*\n]+?)\*\*', r'<strong>\1</strong>'),
            # Malformed patterns die übrig bleiben könnten
            (r'\*\* ([^*\n]+?)\*\*', r'<strong>\1</strong>'),
            (r'\*\*([^*\n]+?) \*\*', r'<strong>\1</strong>'),
            (r'\*\* ([^*\n]+?) \*\*', r'<strong>\1</strong>'),
        ]
        
        for pattern, replacement in patterns_to_fix:
            text = re.sub(pattern, replacement, text)
        
        return text
    
    # Wende die Funktion auf den gesamten Inhalt an
    markdown_content = fix_bold_patterns(markdown_content)
    
    # Fix malformed lists in table cells: convert • bullets and <br> tags to HTML lists
    # Since MultiMarkdown doesn't handle markdown lists well in table cells, we'll use HTML
    def fix_table_cell_lists(match):
        cell_content = match.group(0)
        
        # Check if this cell contains bullet points with <br> tags
        if '•' in cell_content and '<br>' in cell_content:
            # Split the cell content by pipes to isolate the problematic cell
            parts = cell_content.split('|')
            
            for i, part in enumerate(parts):
                if '•' in part and '<br>' in part:
                    # Split by <br> to get individual bullet items
                    items = re.split(r'<br\s*/?>', part)
                    
                    # Process each item and build HTML list
                    list_items = []
                    non_list_content = []
                    
                    for item in items:
                        item = item.strip()
                        if item.startswith('•'):
                            # Convert bullet to HTML list item
                            clean_item = item[1:].strip()  # Remove •
                            if clean_item:
                                list_items.append(f'<li>{clean_item}</li>')
                        elif item:
                            # Keep non-bullet content as is
                            non_list_content.append(item)
                    
                    # Combine non-list content and HTML list
                    if list_items and non_list_content:
                        # Mix of regular content and list
                        html_list = '<ul>' + ''.join(list_items) + '</ul>'
                        parts[i] = ' '.join(non_list_content) + ' ' + html_list
                    elif list_items:
                        # Only list items
                        html_list = '<ul>' + ''.join(list_items) + '</ul>'
                        parts[i] = html_list
                    elif non_list_content:
                        # Only non-list content
                        parts[i] = ' '.join(non_list_content)
            
            return '|'.join(parts)
        
        return cell_content
    
    # Apply the fix to table cells that contain • and <br>
    markdown_content = re.sub(
        r'\|[^|]*?•[^|]*?<br>[^|]*?\|',
        fix_table_cell_lists,
        markdown_content,
        flags=re.DOTALL
    )
    
    # Fix tables with empty headers - specific to this document format
    # Pattern: | | | followed by table rows without separators
    def fix_empty_header_tables(match):
        empty_header = match.group(1)  # | | |
        table_content = match.group(2)  # Rest of table rows
        
        # Create proper markdown table with header separators
        # First, create header separators based on content
        lines = table_content.strip().split('\n')
        if lines:
            # Use first content row to determine column count
            first_row = lines[0]
            col_count = len([cell for cell in first_row.split('|') if cell.strip()])
            
            # Create separator line
            if col_count >= 2:
                separator = '| ' + ' | '.join(['---'] * col_count) + ' |'
                
                # Rebuild table with proper headers
                header = '| ' + ' | '.join([''] * col_count) + ' |'  # Empty header cells
                return header + '\n' + separator + '\n' + table_content
        
        return match.group(0)  # Return unchanged if can't process
    
    # Apply the fix
    markdown_content = re.sub(
        r'(\|\s*\|\s*\|\s*\n)((?:\|[^|\n]*\|[^|\n]*\|[^\n]*\n?)+)',
        fix_empty_header_tables,
        markdown_content,
        flags=re.MULTILINE
    )
    
    return markdown_content

def parse_markdown_to_html(markdown_content):
    """MultiMarkdown zu HTML Parser mit erweiterten Features"""
    
    # Vorverarbeitung um malformed markdown syntax zu bereinigen
    processed_content = preprocess_malformed_markdown(markdown_content)
    
    # MultiMarkdown-Konfiguration
    md = markdown.Markdown(
        extensions=[
            'tables',           # Tabellen-Unterstützung
            'toc',             # Inhaltsverzeichnis
            'fenced_code',     # Code-Blöcke mit ```
            'codehilite',      # Syntax-Highlighting
            'attr_list',       # Attribute für HTML-Elemente
            'def_list',        # Definitionslisten
            'footnotes',       # Fußnoten
            'md_in_html',      # Markdown in HTML-Blöcken
            'sane_lists',      # Bessere Listen-Verarbeitung
            'smarty',          # Smarte Anführungszeichen
            'wikilinks'        # Wiki-Style Links
        ],
        extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'use_pygments': False  # Disable to avoid dependency issues
            },
            'toc': {
                'permalink': True,
                'baselevel': 1
            }
        }
    )
    
    # Markdown zu HTML konvertieren
    html_content = md.convert(processed_content)
    
    # Nachverarbeitung für Info-Boxen
    html_content = postprocess_info_boxes(html_content)
    
    return html_content

def postprocess_info_boxes(html_content):
    """Nachverarbeitung für Info-Boxen - konvertiert blockquotes mit Emojis zu styled divs"""
    
    # Pattern für Info-Box-Blockquotes mit Emojis
    patterns = [
        (r'<blockquote>\s*<p><strong>💡.*?Tipp.*?</strong></p>(.*?)</blockquote>', 'tip', 'Tipp'),
        (r'<blockquote>\s*<p><strong>⚠️.*?Wichtig.*?</strong></p>(.*?)</blockquote>', 'important', 'Wichtig'),
        (r'<blockquote>\s*<p><strong>🚨.*?Warnung.*?</strong></p>(.*?)</blockquote>', 'warning', 'Warnung'),
        (r'<blockquote>\s*<p><strong>💬.*?Anmerkung.*?</strong></p>(.*?)</blockquote>', 'note', 'Anmerkung'),
        # Auch ohne ** um die Titel
        (r'<blockquote>\s*<p>💡.*?Tipp.*?</p>(.*?)</blockquote>', 'tip', 'Tipp'),
        (r'<blockquote>\s*<p>⚠️.*?Wichtig.*?</p>(.*?)</blockquote>', 'important', 'Wichtig'),
        (r'<blockquote>\s*<p>🚨.*?Warnung.*?</p>(.*?)</blockquote>', 'warning', 'Warnung'),
        (r'<blockquote>\s*<p>💬.*?Anmerkung.*?</p>(.*?)</blockquote>', 'note', 'Anmerkung'),
    ]
    
    for pattern, box_type, title in patterns:
        def replace_info_box(match):
            content = match.group(1).strip()
            return f'<div class="{box_type}"><h3 class="title">{title}</h3>{content}</div>'
        
        html_content = re.sub(pattern, replace_info_box, html_content, flags=re.DOTALL | re.IGNORECASE)
    
    return html_content

def escape_html(text):
    """Escapet HTML-Zeichen"""
    if not isinstance(text, str):
        return str(text)
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#x27;'))

def get_html_template():
    """Gibt das HTML-Template zurück"""
    return """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Xentral Dokumentation</title>
    
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
        .breadcrumbs {{
            background: white;
            padding: 10px 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            font-size: 14px;
        }}
        .breadcrumbs a {{
            color: #667eea;
            text-decoration: none;
        }}
        .breadcrumbs a:hover {{
            text-decoration: underline;
        }}
        .content {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        .content h1, .content h2, .content h3, .content h4 {{
            color: #2d3748;
            margin-top: 2em;
            margin-bottom: 1em;
        }}
        .content h1 {{ font-size: 2em; border-bottom: 3px solid #667eea; padding-bottom: 10px; }}
        .content h2 {{ font-size: 1.5em; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px; }}
        .content h3 {{ font-size: 1.25em; color: #4a5568; }}
        .content img {{
            max-width: 800px;
            width: auto;
            height: auto;
            border-radius: 5px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            margin: 15px 0;
            display: block;
        }}
        
        /* Responsive images on smaller screens */
        @media (max-width: 900px) {{
            .content img {{
                max-width: 100%;
            }}
        }}
        .content pre {{
            background: #f7fafc;
            border: 1px solid #e2e8f0;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            font-family: 'Monaco', 'Consolas', monospace;
        }}
        .content code {{
            background: #f7fafc;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 0.9em;
        }}
        .content blockquote {{
            border-left: 4px solid #667eea;
            margin: 20px 0;
            padding: 10px 20px;
            background: #f8f9ff;
            border-radius: 0 5px 5px 0;
        }}
        .content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        .content th, .content td {{
            border: 1px solid #e2e8f0;
            padding: 12px;
            text-align: left;
        }}
        .content th {{
            background: #f7fafc;
            font-weight: 600;
        }}
        .content ul, .content ol {{
            padding-left: 25px;
            margin: 15px 0;
        }}
        .content li {{
            margin: 5px 0;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 14px;
        }}
        .back-to-index {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            margin-bottom: 20px;
            transition: background-color 0.3s;
        }}
        .back-to-index:hover {{
            background: #5a67d8;
            color: white;
        }}
        
        /* Xentral bunte Info-Boxen (wie im Original) */
        .content .note, .content .tip, .content .important, .content .warning {{
            margin: 20px 0;
            padding: 16px 20px;
            border-radius: 8px;
            border-left: 5px solid;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            position: relative;
        }}
        
        /* Anmerkung - Blaue Box */
        .content .note {{
            background: linear-gradient(135deg, #e6f3ff 0%, #f0f8ff 100%);
            border-left-color: #4a90e2;
            color: #1a365d;
        }}
        .content .note .title {{
            color: #2b6cb0;
            font-weight: 600;
            margin: 0 0 10px 0;
            font-size: 1em;
            display: flex;
            align-items: center;
        }}
        .content .note .title::before {{
            content: "💬";
            margin-right: 8px;
            font-size: 1.1em;
        }}
        
        /* Tipp - Grüne Box */
        .content .tip {{
            background: linear-gradient(135deg, #e6ffee 0%, #f0fff4 100%);
            border-left-color: #38a169;
            color: #1a202c;
        }}
        .content .tip .title {{
            color: #2f855a;
            font-weight: 600;
            margin: 0 0 10px 0;
            font-size: 1em;
            display: flex;
            align-items: center;
        }}
        .content .tip .title::before {{
            content: "💡";
            margin-right: 8px;
            font-size: 1.1em;
        }}
        
        /* Wichtig - Orange Box */
        .content .important {{
            background: linear-gradient(135deg, #fff7e6 0%, #fffaf0 100%);
            border-left-color: #ed8936;
            color: #1a202c;
        }}
        .content .important .title {{
            color: #c05621;
            font-weight: 600;
            margin: 0 0 10px 0;
            font-size: 1em;
            display: flex;
            align-items: center;
        }}
        .content .important .title::before {{
            content: "⚠️";
            margin-right: 8px;
            font-size: 1.1em;
        }}
        
        /* Warnung - Rote Box */
        .content .warning {{
            background: linear-gradient(135deg, #ffe6e6 0%, #fff0f0 100%);
            border-left-color: #e53e3e;
            color: #1a202c;
        }}
        .content .warning .title {{
            color: #c53030;
            font-weight: 600;
            margin: 0 0 10px 0;
            font-size: 1em;
            display: flex;
            align-items: center;
        }}
        .content .warning .title::before {{
            content: "🚨";
            margin-right: 8px;
            font-size: 1.1em;
        }}
        
        /* Box-Inhalte */
        .content .note p, .content .tip p, .content .important p, .content .warning p {{
            margin: 8px 0;
            line-height: 1.5;
        }}
        
        .content .note p:last-child, .content .tip p:last-child,
        .content .important p:last-child, .content .warning p:last-child {{
            margin-bottom: 0;
        }}
        
        /* Listen in Boxen */
        .content .note ul, .content .tip ul, .content .important ul, .content .warning ul,
        .content .note ol, .content .tip ol, .content .important ol, .content .warning ol {{
            margin: 10px 0;
            padding-left: 20px;
        }}
        
        .content .note li, .content .tip li, .content .important li, .content .warning li {{
            margin: 4px 0;
        }}
    </style>
    
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p>Generiert aus Markdown | Kategorie: Demo</p>
    </div>
    
    <div class="breadcrumbs">
        <a href="../index.html">🏠 Startseite</a> 
        &raquo; 
        <a href="../index.html#demo">Demo</a>
        &raquo; 
        <strong>{title}</strong>
    </div>
    
    <a href="../index.html" class="back-to-index">← Zurück zur Übersicht</a>
    
    <div class="content">
        {content}
    </div>
    
    <div class="footer">
        <p>Generiert am: {timestamp} | 
        Quelle: Markdown zu HTML Konvertierung</p>
    </div>
</body>
</html>"""

def convert_markdown_file(input_path, output_path):
    """Konvertiert eine Markdown-Datei zu HTML"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Titel aus Dateiname ableiten
        title = input_path.stem.replace('_', ' ').replace('-', ' ').title()
        
        # Markdown zu HTML konvertieren
        html_content = parse_markdown_to_html(markdown_content)
        
        # Timestamp für Footer
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
        
        # HTML-Template verwenden
        template = get_html_template()
        full_html = template.format(
            title=title,
            content=html_content,
            timestamp=timestamp
        )
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"✅ Konvertiert: {input_path} → {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Fehler bei {input_path}: {e}")
        return False

def main():
    """Hauptfunktion"""
    script_dir = Path(__file__).parent
    markdown_dir = script_dir / 'markdown'
    generated_dir = script_dir / 'generated'
    
    # Generated-Ordner erstellen falls nicht vorhanden
    generated_dir.mkdir(exist_ok=True)
    
    # Bilder-Ordner im generated-Ordner erstellen und Bilder kopieren
    generated_images_dir = generated_dir / 'images'
    generated_images_dir.mkdir(exist_ok=True)
    
    # Bilder von original/images nach generated/images kopieren
    original_images_dir = script_dir / 'original' / 'images'
    if original_images_dir.exists():
        import shutil
        for image_file in original_images_dir.glob('*'):
            if image_file.is_file():
                shutil.copy2(image_file, generated_images_dir / image_file.name)
        print(f"📸 Bilder kopiert nach {generated_images_dir}")
    
    # Alle Markdown-Dateien im markdown Ordner finden
    markdown_files = list(markdown_dir.glob('*.md'))
    
    if not markdown_files:
        print("❌ Keine Markdown-Dateien im markdown/ Ordner gefunden")
        return
    
    success_count = 0
    total_count = len(markdown_files)
    
    print(f"🔄 Konvertiere {total_count} Markdown-Datei(en)...")
    
    for markdown_file in markdown_files:
        # Output-Dateiname: .md → .html
        html_file = generated_dir / f"{markdown_file.stem}.html"
        
        if convert_markdown_file(markdown_file, html_file):
            success_count += 1
    
    print(f"\n✅ Konvertierung abgeschlossen: {success_count}/{total_count} Dateien erfolgreich")
    
    if success_count > 0:
        print(f"📁 HTML-Dateien gespeichert in: {generated_dir}")

if __name__ == "__main__":
    main()