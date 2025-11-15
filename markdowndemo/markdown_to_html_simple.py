#!/usr/bin/env python3
"""
Verbesserter Markdown to HTML Converter
Konvertiert Markdown-Dateien aus dem markdown/ Ordner zu HTML im generated/ Ordner
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

def process_text_formatting(text, in_table_cell=False):
    """Verarbeitet Text-Formatierung (Bold, Italic, Links)"""
    
    # YouTube-Videos erkennen und als iframe einbetten - VOR normaler Link-Verarbeitung
    def convert_youtube_link(match):
        link_text = match.group(1)
        url = match.group(2)
        
        # Prüfe ob es ein YouTube-Link ist (verschiedene Formate)
        if 'youtube.com/embed/' in url or 'youtu.be/' in url or 'youtube.com/watch' in url:
            # Extrahiere Video-ID
            video_id = None
            if 'youtube.com/embed/' in url:
                video_id = url.split('youtube.com/embed/')[1].split('?')[0]
            elif 'youtu.be/' in url:
                video_id = url.split('youtu.be/')[1].split('?')[0]
            elif 'youtube.com/watch?v=' in url:
                video_id = url.split('v=')[1].split('&')[0]
            
            if video_id:
                # Erstelle iframe-Einbettung wie im Original
                return f'''<div class="mediaobject">
<div class="video-container">
<div class="videoobject"><iframe allowfullscreen="true" frameborder="0" src="https://www.youtube.com/embed/{video_id}" style="" title="{link_text}"><!-- iframe instead of embed for d:videodata --></iframe></div>
</div>
</div>'''
        
        # Kein YouTube-Link - normaler Link
        return f'<a href="{url}">{link_text}</a>'
    
    # YouTube-Links und normale Links verarbeiten
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', convert_youtube_link, text)
    
    # Bold text **text** oder __text__
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    
    # Italic text *text* oder _text_
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    
    # Code `code`
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    return text

def process_cell_content(cell_content):
    """Verarbeitet Zelleninhalt - erkennt Info-Boxen und andere Formatierungen"""
    if not cell_content.strip():
        return ''
    
    content = cell_content.strip()
    
    # Suche nach kompakten Inline-Info-Box Pattern im Zellinhalt
    # Pattern: "normaler text 💬** Anmerkung:** inhalt" oder "normaler text 💡** Tipp:** inhalt" etc.
    info_box_patterns = [
        (r'(.*?)💬\*\*\s*Anmerkung:\*\*(.*)', 'note', '💬 <strong>Anmerkung:</strong>'),
        (r'(.*?)💡\*\*\s*Tipp:\*\*(.*)', 'tip', '💡 <strong>Tipp:</strong>'),
        (r'(.*?)⚠️\*\*\s*Wichtig:\*\*(.*)', 'important', '⚠️ <strong>Wichtig:</strong>'),
        (r'(.*?)🚨\*\*\s*Warnung:\*\*(.*)', 'warning', '🚨 <strong>Warnung:</strong>')
    ]
    
    for pattern, box_type, box_prefix in info_box_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            normal_text = match.group(1).strip()
            box_content = match.group(2).strip()
            
            result = ""
            
            # Verarbeite normalen Text
            if normal_text:
                result += process_text_formatting(normal_text) + " "
            
            # Füge Info-Box als kompakte Inline-Darstellung hinzu
            if box_content:
                result += f'<span class="inline-{box_type}">{box_prefix} {process_text_formatting(box_content)}</span>'
            
            return result
    
    # Keine Info-Box gefunden - normale Verarbeitung
    return process_text_formatting(content)

def simple_markdown_to_html(markdown_content):
    """Verbesserter Markdown zu HTML Parser"""
    lines = markdown_content.split('\n')
    html_lines = []
    in_table = False
    in_list = False
    in_ordered_list = False
    in_blockquote = False
    table_rows = []
    list_level = 0
    
    def process_table():
        """Verarbeitet gesammelte Tabellenzeilen zu korrektem HTML"""
        if not table_rows:
            return []
        
        result = ['<table>']
        
        # Erste Zeile als Header (wenn nicht leer)
        first_row = table_rows[0]
        if any(cell.strip() for cell in first_row):
            result.append('<thead>')
            result.append('<tr>')
            for cell in first_row:
                processed_cell = process_cell_content(cell)
                result.append(f'<th>{processed_cell}</th>')
            result.append('</tr>')
            result.append('</thead>')
            body_start = 1
        else:
            body_start = 0
        
        # Rest als Body
        if len(table_rows) > body_start:
            result.append('<tbody>')
            for row in table_rows[body_start:]:
                # Leere Zeilen überspringen
                if not any(cell.strip() for cell in row):
                    continue
                result.append('<tr>')
                for cell in row:
                    processed_cell = process_cell_content(cell)
                    result.append(f'<td>{processed_cell}</td>')
                result.append('</tr>')
            result.append('</tbody>')
        
        result.append('</table>')
        return result
    
    def close_lists():
        """Schließt offene Listen"""
        nonlocal in_list, in_ordered_list
        result = []
        if in_ordered_list:
            result.append('</ol>')
            in_ordered_list = False
        elif in_list:
            result.append('</ul>')
            in_list = False
        return result
    
    def close_blockquote():
        """Schließt offene Blockquote"""
        nonlocal in_blockquote
        if in_blockquote:
            in_blockquote = False
            return ['</div>']
        return []
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Tabellen-Verarbeitung
        if '|' in line and line.strip().startswith('|'):
            # Andere Strukturen schließen
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(cells)
            i += 1
            continue
        else:
            # Tabelle beenden wenn wir nicht mehr in einer Tabelle sind
            if in_table:
                html_lines.extend(process_table())
                in_table = False
                table_rows = []
        
        # Überschriften - mehrere ### für verschiedene Levels
        if line.startswith('#### '):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            text = line[5:].strip()
            html_lines.append(f'<h4>{process_text_formatting(text)}</h4>')
        elif line.startswith('### '):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            text = line[4:].strip()
            html_lines.append(f'<h3>{process_text_formatting(text)}</h3>')
        elif line.startswith('## '):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            text = line[3:].strip()
            html_lines.append(f'<h2>{process_text_formatting(text)}</h2>')
        elif line.startswith('# '):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            text = line[2:].strip()
            html_lines.append(f'<h1>{process_text_formatting(text)}</h1>')
        
        # Bilder
        elif line.strip().startswith('!['):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line.strip())
            if img_match:
                alt_text = img_match.group(1)
                src = img_match.group(2)
                html_lines.append(f'<img src="{src}" alt="{alt_text}" style="max-width: 100%; height: auto;" />')
        
        # Info-Boxen (Blockquotes) - Erweiterte Erkennung
        elif line.startswith('> **Tipp**') or line.startswith('> 💡'):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            html_lines.append('<div class="tip"><h3 class="title">Tipp</h3>')
            in_blockquote = True
        elif line.startswith('> **Wichtig**') or line.startswith('> ⚠️'):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            html_lines.append('<div class="important"><h3 class="title">Wichtig</h3>')
            in_blockquote = True
        elif line.startswith('> **Warnung**') or line.startswith('> 🚨'):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            html_lines.append('<div class="warning"><h3 class="title">Warnung</h3>')
            in_blockquote = True
        elif line.startswith('> **Anmerkung**') or line.startswith('> 💬'):
            html_lines.extend(close_lists())
            html_lines.extend(close_blockquote())
            html_lines.append('<div class="note"><h3 class="title">Anmerkung</h3>')
            in_blockquote = True
        elif line.startswith('>') and line != '>':
            content = line[1:].strip()
            if content:
                # Prüfe ob es eine Liste in der Blockquote ist
                if content.startswith('- '):
                    # Ungeordnete Liste in Blockquote
                    list_item = content[2:].strip()
                    html_lines.append(f'<ul><li>{process_text_formatting(list_item)}</li></ul>')
                elif re.match(r'^\d+\.\s', content):
                    # Geordnete Liste in Blockquote
                    list_item = re.sub(r'^\d+\.\s', '', content)
                    html_lines.append(f'<ol><li>{process_text_formatting(list_item)}</li></ol>')
                else:
                    # Normaler Paragraph in Blockquote
                    html_lines.append(f'<p>{process_text_formatting(content)}</p>')
        elif line == '>':
            # Leere Blockquote-Zeile
            pass
        elif in_blockquote and not line.startswith('>'):
            # Blockquote beenden
            html_lines.extend(close_blockquote())
        
        # Nummerierte Listen - Mit erweiteter Verarbeitung von Fortsetzungstexten und Unterlisten
        elif re.match(r'^\d+\.\s', line.strip()):
            html_lines.extend(close_blockquote())
            if not in_ordered_list:
                html_lines.extend(close_lists())
                html_lines.append('<ol>')
                in_ordered_list = True
            
            # Listeninhalt sammeln (inkl. eingerückter Fortsetzungszeilen und Unterlisten)
            text = re.sub(r'^\d+\.\s', '', line.strip())
            list_content = [process_text_formatting(text)]
            
            # Schaue nach, ob nachfolgende Zeilen eingerückt sind (gehören zum Listenelement)
            j = i + 1
            nested_list_items = []
            while j < len(lines):
                next_line = lines[j].rstrip()
                if next_line.strip() == '':
                    # Leerzeile - schaue weiter
                    j += 1
                    continue
                elif next_line.strip().startswith('- ') and (next_line.startswith('  ') or next_line.startswith('\t')):
                    # Eingerückte Unterliste - sammeln
                    nested_item = next_line.strip()[2:].strip()  # Remove "- "
                    nested_list_items.append(process_text_formatting(nested_item))
                    j += 1
                elif (next_line.startswith('   ') or next_line.startswith('\t')) and not re.match(r'^\d+\.\s', next_line.strip()) and not next_line.strip().startswith('- '):
                    # Eingerückte Zeile - gehört zur Liste
                    indented_text = next_line.strip()
                    if indented_text:
                        list_content.append(f'<p>{process_text_formatting(indented_text)}</p>')
                    j += 1
                else:
                    # Keine eingerückte Zeile mehr - Liste beenden
                    break
            
            # Unterliste hinzufügen wenn vorhanden
            if nested_list_items:
                nested_ul = '<ul>' + ''.join(f'<li>{item}</li>' for item in nested_list_items) + '</ul>'
                list_content.append(nested_ul)
            
            # Alle Inhalte als ein Listenelement zusammenfassen
            if len(list_content) == 1:
                html_lines.append(f'<li>{list_content[0]}</li>')
            else:
                html_lines.append(f'<li><p>{list_content[0]}</p>{"".join(list_content[1:])}</li>')
            
            # Index vorspringen
            i = j - 1
        
        # Ungeordnete Listen
        elif line.strip().startswith('- '):
            html_lines.extend(close_blockquote())
            if not in_list:
                html_lines.extend(close_lists())
                html_lines.append('<ul>')
                in_list = True
            
            text = line.strip()[2:].strip()
            html_lines.append(f'<li>{process_text_formatting(text)}</li>')
        
        # Leerzeilen
        elif line.strip() == '':
            # Leerzeilen schließen Listen NICHT mehr automatisch
            if not in_blockquote and not in_table and not in_list and not in_ordered_list:
                html_lines.append('<br>')
        
        # Normale Paragraphen
        else:
            if line.strip():
                # Prüfe ob wir in einer Liste sind und der Text eingerückt ist
                if (in_ordered_list or in_list) and (line.startswith('   ') or line.startswith('\t')):
                    # Text ist eingerückt - gehört vermutlich zur Liste, wird aber hier übersprungen
                    # da er bereits oben in der Listen-Verarbeitung behandelt wurde
                    pass
                else:
                    # Normaler Paragraph - Listen schließen
                    html_lines.extend(close_lists())
                    html_lines.extend(close_blockquote())
                    html_lines.append(f'<p>{process_text_formatting(line)}</p>')
        
        i += 1
    
    # Alle offenen Strukturen schließen
    html_lines.extend(close_lists())
    html_lines.extend(close_blockquote())
    if in_table:
        html_lines.extend(process_table())
    
    return '\n'.join(html_lines)

def create_simple_html(title, content, timestamp):
    """Erstellt ein HTML-Dokument mit dem gleichen Styling wie das Original"""
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Picklisten-Profile - Xentral Dokumentation</title>
    
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
                max-width: 100%;
                height: auto;
                border-radius: 5px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                margin: 15px 0;
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
            
            /* Inline Info-Boxen für Tabellenzellen */
            .content .inline-note, .content .inline-tip, .content .inline-important, .content .inline-warning {{
                display: inline-block;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.9em;
                margin: 2px 0;
                border-left: 3px solid;
            }}
            
            .content .inline-note {{
                background: #e6f3ff;
                border-left-color: #4a90e2;
                color: #1a365d;
            }}
            
            .content .inline-tip {{
                background: #e6ffee;
                border-left-color: #38a169;
                color: #1a202c;
            }}
            
            .content .inline-important {{
                background: #fff7e6;
                border-left-color: #ed8936;
                color: #1a202c;
            }}
            
            .content .inline-warning {{
                background: #ffe6e6;
                border-left-color: #e53e3e;
                color: #1a202c;
            }}
            
            /* YouTube Video Styling */
            .content .mediaobject {{
                margin: 20px 0;
                text-align: center;
            }}
            
            .content .video-container {{
                position: relative;
                padding-bottom: 56.25%; /* 16:9 aspect ratio */
                height: 0;
                overflow: hidden;
                max-width: 100%;
                background: #f0f0f0;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            
            .content .videoobject iframe {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border-radius: 8px;
            }}
        </style>
        
</head>
<body>
    <div class="header">
        <h1>Picklisten-Profile</h1>
        <p>Artikel-ID: 360016722600 | Kategorie: Logistik und Warenausgang</p>
    </div>
    
    
        <div class="breadcrumbs">
            <a href="../index.html">🏠 Startseite</a> 
            &raquo; 
            <a href="../index.html#logistik-und-warenausgang">Logistik und Warenausgang</a>
            &raquo; 
            <strong>Picklisten-Profile</strong>
        </div>
        
    
    <a href="../index.html" class="back-to-index">← Zurück zur Übersicht</a>
    
    <div class="content">
        {content}
    </div>
    
    <div class="footer">
        <p>Erstellt am: {timestamp} | 
        Quelle: <a href="https://help.xentral.com/hc/de/articles/360016722600-Picklisten-Profile">Zendesk-Artikel</a></p>
    </div>
</body>
</html>"""

def convert_markdown_file(input_path, output_path):
    """Konvertiert eine Markdown-Datei zu HTML"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Markdown zu HTML konvertieren
        html_content = simple_markdown_to_html(markdown_content)
        
        # Timestamp für Footer
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
        
        # HTML erstellen
        full_html = create_simple_html("Picklisten-Profile", html_content, timestamp)
        
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
    original_images_dir = script_dir / 'images'
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