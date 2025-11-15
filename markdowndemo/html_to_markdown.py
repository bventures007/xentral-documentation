#!/usr/bin/env python3
"""
HTML to Markdown Converter
Konvertiert HTML-Dateien aus dem original/ Ordner zu Markdown im markdown/ Ordner
"""

import os
import sys
from pathlib import Path
from bs4 import BeautifulSoup
import re

def clean_text(text):
    """Bereinigt Text von überschüssigen Whitespaces"""
    if not text:
        return ""
    # Mehrfache Leerzeichen/Zeilenumbrüche reduzieren
    text = re.sub(r'\s+', ' ', text.strip())
    return text

def clean_markdown_spacing(markdown):
    """Bereinigt überflüssige Leerzeichen vor Satzzeichen und fügt sie nach Formatierungen hinzu wo nötig"""
    if not markdown:
        return ""
    
    # URLs und spezielle Inhalte in eckigen Klammern schützen
    protected_content = []
    def protect_urls(match):
        protected_content.append(match.group(0))
        return f"__PROTECTED_{len(protected_content)-1}__"
    
    # URLs in Links schützen
    markdown = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', protect_urls, markdown)
    
    # 1. ZUERST: Leerzeichen INNERHALB von Formatierungen entfernen (kritisch für Markdown!)
    # Das ist das wichtigste - ** text ** -> **text** (sonst funktioniert Markdown nicht)
    
    # Mehrfache Durchläufe für hartnäckige Fälle
    for _ in range(5):  # 5 Durchläufe um alle Varianten zu erwischen
        # ** text ** -> **text** (alle Varianten, auch komplexere)
        markdown = re.sub(r'\*\*\s+([^*\n]+?)\s+\*\*', r'**\1**', markdown)
        markdown = re.sub(r'\*\*\s+([^*\n]+?)\*\*', r'**\1**', markdown)  # ** text**
        markdown = re.sub(r'\*\*([^*\n]+?)\s+\*\*', r'**\1**', markdown)  # **text **
        
        # Spezielle Fälle: ** Text**word -> **Text** word, aber auch ** Text** genannt -> **Text** genannt
        markdown = re.sub(r'\*\*\s*([^*\n]+?)\s*\*\*([a-zA-ZÄÖÜäöüß])', r'**\1** \2', markdown)
        markdown = re.sub(r'\*\*\s*([^*\n]+?)\s*\*\*(\s)', r'**\1**\2', markdown)  # Leerzeichen erhalten
        
        # * text * -> *text* (alle Varianten)
        markdown = re.sub(r'\*\s+([^*\n]+?)\s+\*', r'*\1*', markdown)
        markdown = re.sub(r'\*\s+([^*\n]+?)\*', r'*\1*', markdown)  # * text*
        markdown = re.sub(r'\*([^*\n]+?)\s+\*', r'*\1*', markdown)  # *text *
        
        # ` code ` -> `code` (alle Varianten)
        markdown = re.sub(r'`\s+([^`\n]+?)\s+`', r'`\1`', markdown)
        markdown = re.sub(r'`\s+([^`\n]+?)`', r'`\1`', markdown)  # ` code`
        markdown = re.sub(r'`([^`\n]+?)\s+`', r'`\1`', markdown)  # `code `
    
    # 2. Leerzeichen vor Formatierungen hinzufügen (nach Wörtern und Satzzeichen)
    before_formatting_patterns = [
        # Nach Wörtern/Zahlen - nur wenn KEIN Leerzeichen davor ist
        (r'([a-zA-ZÄÖÜäöüß0-9])\*\*([^*\n]+)\*\*', r'\1 **\2**'),
        (r'([a-zA-ZÄÖÜäöüß0-9])\*([^*\n]+)\*', r'\1 *\2*'),
        (r'([a-zA-ZÄÖÜäöüß0-9])`([^`\n]+)`', r'\1 `\2`'),
        # Nach Satzzeichen - nur wenn KEIN Leerzeichen davor ist
        (r'([,.;:!?])\*\*([^*\n]+)\*\*', r'\1 **\2**'),
        (r'([,.;:!?])\*([^*\n]+)\*', r'\1 *\2*'),
        (r'([,.;:!?])`([^`\n]+)`', r'\1 `\2`'),
    ]
    
    for pattern, replacement in before_formatting_patterns:
        markdown = re.sub(pattern, replacement, markdown)
    
    # 3. Leerzeichen nach Formatierungen hinzufügen, wo sie fehlen
    after_formatting_patterns = [
        # Vor Wörtern/Zahlen - nur wenn KEIN Leerzeichen danach ist
        (r'\*\*([^*\n]+)\*\*([a-zA-ZÄÖÜäöüß0-9])', r'**\1** \2'),
        (r'\*([^*\n]+)\*([a-zA-ZÄÖÜäöüß0-9])', r'*\1* \2'),
        (r'`([^`\n]+)`([a-zA-ZÄÖÜäöüß0-9])', r'`\1` \2'),
        # Vor Klammern
        (r'\*\*([^*\n]+)\*\*(\()', r'**\1** \2'),
        (r'\*([^*\n]+)\*(\()', r'*\1* \2'),
        (r'`([^`\n]+)`(\()', r'`\1` \2'),
        # Vor > (Blockquote) - KEIN Leerzeichen hinzufügen
        (r'\*\*([^*\n]+)\*\*(>)', r'**\1**\2'),
        (r'\*([^*\n]+)\*(>)', r'*\1*\2'),
        (r'`([^`\n]+)`(>)', r'`\1`\2'),
    ]
    
    for pattern, replacement in after_formatting_patterns:
        markdown = re.sub(pattern, replacement, markdown)
    
    # 4. WICHTIG: Leerzeichen vor Satzzeichen entfernen - NACH der Formatierung
    # Das muss nach den Formatierungs-Fixes kommen
    punctuation_patterns = [
        (r' +,', r','),     # space, -> ,
        (r' +\.', r'.'),    # space. -> .
        (r' +;', r';'),     # space; -> ;
        (r' +:', r':'),     # space: -> :
        (r' +!', r'!'),     # space! -> !
        (r' +\?', r'?'),    # space? -> ?
        (r' +\)', r')'),    # space) -> )
        (r' +\]', r']'),    # space] -> ]
        (r' +\}', r'}'),    # space} -> }
    ]
    
    for pattern, replacement in punctuation_patterns:
        markdown = re.sub(pattern, replacement, markdown)
    
    # 5. Leerzeichen zwischen Wörtern wiederherstellen wo sie fehlen
    word_spacing_patterns = [
        # Xentral-spezifische Probleme
        (r'\b([a-z]{2,})(Xentral)', r'\1 \2'),
        (r'(Xentral)([a-z]{2,})', r'\1 \2'),
        # Andere häufige Zusammenschreibungen
        (r'\b([a-z]{2,})(Profile|Picklisten)', r'\1 \2'),
        (r'(Profile|Picklisten)([a-z]{2,})', r'\1 \2'),
    ]
    
    for pattern, replacement in word_spacing_patterns:
        markdown = re.sub(pattern, replacement, markdown)
    
    # 6. Überflüssige Leerzeichen nach Formatierungen vor Satzzeichen entfernen
    formatting_punctuation_patterns = [
        (r'\*\* +([.,:;!?)])', r'**\1'),  # **text ** . -> **text**.
        (r'\* +([.,:;!?)])', r'*\1'),     # *text * . -> *text*.
        (r'` +([.,:;!?)])', r'`\1'),      # `code ` . -> `code`.
        # Spezielle Fälle mit direkten Folgezeichen
        (r'\*\* +(\*\*)', r'** \1'),      # ** text ****other** -> **text** **other**
        (r'\*\* +(oder|und|als|im|zu|von)', r'** \1'),  # **text **oder -> **text** oder
    ]
    
    for pattern, replacement in formatting_punctuation_patterns:
        markdown = re.sub(pattern, replacement, markdown)
    
    # 7. WICHTIG: Listen korrekt von vorangehendem Text trennen
    # Das muss vor der Wiederherstellung geschützter Inhalte passieren
    markdown = re.sub(r'(\*\*[^*\n]+\*\*)\s*(\d+\.)', r'\1\n\n\2', markdown)  # **Text** 1. -> **Text**\n\n1.
    markdown = re.sub(r'(\*\*[^*\n]+\*\*)\s*(-)', r'\1\n\n\2', markdown)      # **Text** - -> **Text**\n\n-
    
    # 8. Geschützte Inhalte wiederherstellen
    for i, content in enumerate(protected_content):
        markdown = markdown.replace(f"__PROTECTED_{i}__", content)
    
    # 9. Mehrfache Leerzeichen reduzieren (außer am Zeilenanfang für Einrückung)
    markdown = re.sub(r'(?<!^)(?<!  ) {2,}', ' ', markdown, flags=re.MULTILINE)
    
    return markdown

def process_list(element, level=0):
    """Konvertiert HTML-Listen zu Markdown mit verbesserter Formatierung"""
    markdown = ""
    indent = "  " * level  # 2 Leerzeichen pro Ebene
    
    for li in element.find_all('li', recursive=False):
        # Alle Paragraphen in diesem List-Item sammeln
        paragraphs = li.find_all('p', recursive=False)
        
        if paragraphs:
            # Erster Paragraph als Haupt-List-Item
            first_p = paragraphs[0]
            first_text = ""
            for child in first_p.children:
                first_text += process_element_inline(child)
            
            first_text = clean_text(first_text)
            if first_text:
                if element.name == 'ol':
                    markdown += f"{indent}1. {first_text}\n"
                else:
                    markdown += f"{indent}- {first_text}\n"
            
            # Weitere Paragraphen als eingerückte Fortsetzung
            for p in paragraphs[1:]:
                p_text = ""
                for child in p.children:
                    p_text += process_element_inline(child)
                
                p_text = clean_text(p_text)
                if p_text:
                    markdown += f"{indent}   {p_text}\n\n"
        else:
            # Falls keine Paragraphen, normaler Text
            text_parts = []
            for content in li.children:
                if content.name == 'ul' or content.name == 'ol':
                    continue
                elif hasattr(content, 'get_text'):
                    text_parts.append(content.get_text(strip=True))
                elif isinstance(content, str):
                    text_parts.append(content.strip())
            
            text = clean_text(' '.join(text_parts))
            if text:
                if element.name == 'ol':
                    markdown += f"{indent}1. {text}\n"
                else:
                    markdown += f"{indent}- {text}\n"
        
        # Verschachtelte Listen verarbeiten - auch in itemizedlist divs
        # 1. Direkte Listen
        for nested in li.find_all(['ul', 'ol'], recursive=False):
            markdown += process_list(nested, level + 1)
        
        # 2. Listen in itemizedlist divs (DocBook-Struktur)
        itemizedlist_divs = li.find_all('div', class_='itemizedlist', recursive=False)
        for div in itemizedlist_divs:
            nested_lists = div.find_all(['ul', 'ol'], recursive=False)
            for nested in nested_lists:
                markdown += process_list(nested, level + 1)
    
    return markdown

def process_element_inline(element):
    """Verarbeitet Inline-Elemente für bessere Formatierung"""
    if isinstance(element, str):
        text = element.strip()
        if text:
            # Prüfe ursprüngliches Element für führende/folgende Leerzeichen
            leading_space = ""
            trailing_space = " "
            
            # Wenn das Original-Element mit Leerzeichen beginnt/endet, beibehalten
            if len(element) > len(text):
                if element.startswith(' ') or element.startswith('\n') or element.startswith('\t'):
                    leading_space = " "
                if element.endswith(' ') or element.endswith('\n') or element.endswith('\t'):
                    trailing_space = " "
            
            return leading_space + text + trailing_space
        return ""
    
    if element.name in ['strong', 'b']:
        text = clean_text(element.get_text())
        return f"**{text}** " if text else ""
    
    if element.name in ['em', 'i']:
        text = clean_text(element.get_text())
        return f"*{text}* " if text else ""
    
    if element.name == 'code':
        text = element.get_text()
        return f"`{text}` " if text else ""
    
    # Span-Elemente mit Formatierung verarbeiten
    if element.name == 'span':
        classes = element.get('class', [])
        if 'bold' in classes:
            # Suche nach strong/b Elementen in span
            strong_elem = element.find(['strong', 'b'])
            if strong_elem:
                text = clean_text(strong_elem.get_text())
                # Prüfe ob nach dem span ein Leerzeichen folgt (durch nächstes Sibling)
                return f"**{text}** " if text else ""
        
        # Normale span - Inhalt rekursiv verarbeiten
        result = ""
        for child in element.children:
            result += process_element_inline(child)
        # Bei spans immer ein Leerzeichen anhängen, da sie oft vor nachfolgendem Text stehen
        return result + " " if result.strip() else ""
    
    # Links verarbeiten
    if element.name == 'a':
        href = element.get('href', '')
        classes = element.get('class', [])
        
        # Text aus den Kindelementen extrahieren (um Formatierung zu erhalten)
        link_text = ""
        for child in element.children:
            link_text += process_element_inline(child)
        link_text = link_text.strip()
        
        if not link_text:
            link_text = clean_text(element.get_text())
        
        if href and link_text:
            # Interne xref-Links zu Markdown-Anker-Links konvertieren
            if href.startswith('#') and 'xref' in classes:
                # UUID in normalen Anker umwandeln
                if 'section-idm' in href:
                    # Titel aus dem title-Attribut extrahieren
                    title = element.get('title', '')
                    if title:
                        # Titel zu URL-Fragment machen (lowercase, Leerzeichen zu -)
                        anchor = title.lower().replace(' ', '-').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                        return f"[{link_text}](#{anchor}) "
                return f"[{link_text}]({href}) "
            else:
                return f"[{link_text}]({href}) "
        elif link_text:
            return link_text + " "
    
    # Für alle anderen Elemente, Text extrahieren
    return clean_text(element.get_text()) + " " if hasattr(element, 'get_text') else ""

def process_table(table):
    """Konvertiert HTML-Tabelle zu Markdown mit Formatierungserhaltung"""
    markdown = "\n"
    
    # Tabellenheader
    headers = []
    header_row = table.find('tr')
    if header_row:
        for th in header_row.find_all(['th', 'td']):
            # Formatierung in Header-Zellen verarbeiten
            cell_content = ""
            for child in th.children:
                cell_content += process_element_inline(child)
            headers.append(clean_text(cell_content) if cell_content.strip() else clean_text(th.get_text()))
    
    if headers and any(h for h in headers):
        markdown += "| " + " | ".join(headers) + " |\n"
        markdown += "| " + " | ".join(['---'] * len(headers)) + " |\n"
    
    # Tabellenzeilen (skip erste Zeile wenn sie Header enthielt)
    rows = table.find_all('tr')
    start_idx = 1 if headers and any(h for h in headers) else 0
    
    for row in rows[start_idx:]:
        cells = []
        for td in row.find_all(['td', 'th']):
            # Formatierung in Tabellenzellen verarbeiten
            cell_content = ""
            
            # Sammle alle Teile der Zelle
            cell_parts = []
            
            # Verarbeite alle Kinder der Zelle
            for child in td.children:
                if hasattr(child, 'name') and child.name == 'div' and any(cls in child.get('class', []) for cls in ['tip', 'important', 'warning', 'note']):
                    # Info-Box gefunden - als kompaktes Inline-Element hinzufügen
                    box_classes = child.get('class', [])
                    if 'tip' in box_classes:
                        emoji = "💡"
                        box_type = "Tipp"
                    elif 'important' in box_classes:
                        emoji = "⚠️"
                        box_type = "Wichtig"
                    elif 'warning' in box_classes:
                        emoji = "🚨"
                        box_type = "Warnung"
                    elif 'note' in box_classes:
                        emoji = "💬"
                        box_type = "Anmerkung"
                    else:
                        emoji = "ℹ️"
                        box_type = "Info"
                    
                    # Titel extrahieren
                    title_elem = child.find(['h3', 'h4', 'h5'], class_='title')
                    if title_elem:
                        title_text = clean_text(title_elem.get_text())
                        # Title Element für Content-Extraktion entfernen
                        title_elem_copy = title_elem.extract()
                    else:
                        title_text = box_type
                    
                    # Content extrahieren (nach dem Entfernen des Titels)
                    content_text = clean_text(child.get_text())
                    
                    # Info-Box als kompaktes Inline-Element hinzufügen
                    compact_info = f"{emoji} **{title_text}:** {content_text}"
                    cell_parts.append(compact_info)
                elif hasattr(child, 'name') and child.name == 'div' and 'itemizedlist' in child.get('class', []):
                    # DocBook itemizedlist - Listen in Tabellenzellen
                    list_elem = child.find(['ul', 'ol'])
                    if list_elem:
                        list_content = process_list_in_table_cell(list_elem)
                        if list_content.strip():
                            cell_parts.append(list_content.strip())
                elif hasattr(child, 'name') and child.name in ['ul', 'ol']:
                    # Direkte Listen in Tabellenzellen
                    list_content = process_list_in_table_cell(child)
                    if list_content.strip():
                        cell_parts.append(list_content.strip())
                elif child.name == 'p':
                    # Normaler Paragraph
                    p_content = ""
                    for grandchild in child.children:
                        p_content += process_element_inline(grandchild)
                    # Nur führende/abschließende Leerzeichen entfernen, aber Zwischen-Leerzeichen beibehalten
                    p_content_cleaned = re.sub(r' {2,}', ' ', p_content).strip()
                    if p_content_cleaned:
                        cell_parts.append(p_content_cleaned)
                elif isinstance(child, str):
                    text = child.strip()
                    if text:
                        cell_parts.append(text)
                else:
                    # Andere Elemente
                    content = process_element_inline(child)
                    if content.strip():
                        cell_parts.append(content.strip())
            
            # Alle Teile zusammenfügen
            if cell_parts:
                cell_content = ' '.join(cell_parts)
            else:
                cell_content = clean_text(td.get_text())
            
            # Fix für fehlendes Leerzeichen nach **text** (alle Varianten)
            cell_content = re.sub(r'\*\*\s*([^*]+)\*\*([a-zA-ZäöüÄÖÜß])', r'**\1** \2', cell_content)
            
            # Pipe-Zeichen in Zellen escapen
            cell_content = cell_content.replace('|', '\\|')
            cells.append(cell_content)
        
        if cells:
            markdown += "| " + " | ".join(cells) + " |\n"
    
    markdown += "\n"
    return markdown

def process_list_in_table_cell(list_element):
    """Verarbeitet Listen innerhalb von Tabellenzellen - kompakte Darstellung mit korrekten Leerzeichen"""
    result = ""
    
    for li in list_element.find_all('li', recursive=False):
        # List-Item Inhalt verarbeiten
        li_content = ""
        
        # Alle Paragraphen und Text im List-Item sammeln
        for child in li.children:
            if isinstance(child, str):
                text = child.strip()
                if text:
                    li_content += text + " "
            elif child.name == 'p':
                # Paragraph-Inhalt mit Inline-Formatierung verarbeiten
                p_content = ""
                for p_child in child.children:
                    p_content += process_element_inline(p_child)
                # Entferne nur mehrfache Leerzeichen, aber behalte Einzelleerzeichen
                p_content = re.sub(r' {2,}', ' ', p_content.strip())
                if p_content:
                    li_content += p_content + " "
            elif child.name in ['strong', 'b']:
                # Fett markierte Texte mit korrekten Leerzeichen
                text = clean_text(child.get_text())
                if text:
                    li_content += f"**{text}** "
            elif child.name in ['em', 'i']:
                # Kursive Texte mit korrekten Leerzeichen
                text = clean_text(child.get_text())
                if text:
                    li_content += f"*{text}* "
            elif child.name == 'code':
                # Code mit korrekten Leerzeichen
                text = child.get_text()
                if text:
                    li_content += f"`{text}` "
            elif hasattr(child, 'children'):
                # Verschachtelte Elemente rekursiv verarbeiten mit process_element_inline
                for nested_child in child.children:
                    li_content += process_element_inline(nested_child)
            elif hasattr(child, 'get_text'):
                text = clean_text(child.get_text())
                if text:
                    li_content += text + " "
        
        # Entferne nur führende Leerzeichen, aber behalte die abschließenden
        li_content = li_content.strip()
        if li_content:
            if list_element.name == 'ol':
                result += f"• {li_content}<br>"
            else:
                result += f"• {li_content}<br>"
    
    return result.rstrip('<br>')

def process_info_box(element):
    """Konvertiert Xentral Info-Boxen (tip, important, warning, note) zu Markdown"""
    box_type = ""
    if 'tip' in element.get('class', []):
        box_type = "**Tipp**"
    elif 'important' in element.get('class', []):
        box_type = "**Wichtig**"
    elif 'warning' in element.get('class', []):
        box_type = "**Warnung**"
    elif 'note' in element.get('class', []):
        box_type = "**Anmerkung**"
    else:
        box_type = "**Info**"
    
    # Titel der Box
    title_elem = element.find(class_='title')
    if title_elem:
        title_text = clean_text(title_elem.get_text())
        # Title element entfernen, damit es nicht doppelt erscheint
        title_elem.decompose()
    else:
        title_text = ""
    
    # Inhalt der Box strukturell verarbeiten (um iframes etc. zu erfassen)
    def process_box_content(elem):
        """Verarbeitet Inhalt einer Info-Box rekursiv"""
        if isinstance(elem, str):
            text = elem.strip()
            return text
        
        if not hasattr(elem, 'name'):
            return ""
        
        # YouTube iframe erkennen
        if elem.name == 'iframe':
            src = elem.get('src', '')
            if 'youtube.com' in src or 'youtu.be' in src:
                return f"\n**[YouTube Video]({src})**\n"
        
        # Absätze
        if elem.name == 'p':
            content = ""
            for child in elem.children:
                content += process_box_content(child)
            text = clean_text(content)
            if text:
                return text + "\n"
            return ""
        
        # Text-Formatierung
        if elem.name in ['strong', 'b']:
            text = clean_text(elem.get_text())
            return f"**{text}** " if text else ""
        
        if elem.name in ['em', 'i']:
            text = clean_text(elem.get_text())
            return f"*{text}* " if text else ""
        
        if elem.name == 'code':
            text = elem.get_text()
            return f"`{text}` " if text else ""
        
        # Listen
        if elem.name in ['ul', 'ol']:
            result = ""
            for li in elem.find_all('li', recursive=False):
                li_content = ""
                for child in li.children:
                    li_content += process_box_content(child)
                li_content = clean_text(li_content)
                if li_content:
                    result += f"- {li_content}\n"
            return result
        
        # DocBook/HTML-spezifische Strukturen - itemizedlist
        if elem.name == 'div' and 'itemizedlist' in elem.get('class', []):
            # Direkt die <ul> darin verarbeiten
            ul_elem = elem.find('ul')
            if ul_elem:
                return process_box_content(ul_elem)
            return ""
        
        # Für alle anderen Elemente, rekursiv durch Kinder gehen
        result = ""
        if hasattr(elem, 'children'):
            for child in elem.children:
                result += process_box_content(child)
        
        return result
    
    markdown = f"\n> {box_type}\n>\n"
    if title_text and title_text not in box_type:
        markdown += f"> **{title_text}**\n>\n"
    
    # Inhalt strukturell verarbeiten - jedes Child einzeln
    first_content = True
    for child in element.children:
        if child == title_elem:  # Titel überspringen
            continue
            
        child_content = process_box_content(child)
        if child_content.strip():
            # Trennzeile zwischen verschiedenen Inhaltsbereichen
            if not first_content:
                markdown += ">\n"
            
            # Listen haben bereits korrekte Zeilenumbrüche
            if child_content.startswith('- '):
                # Das ist eine Liste - jede Zeile einzeln mit > prefix
                for line in child_content.strip().split('\n'):
                    line = line.strip()
                    if line:
                        markdown += f"> {line}\n"
            else:
                # Normaler Text - als zusammenhängender Block
                text_lines = child_content.strip().split('\n')
                for line in text_lines:
                    line = line.strip()
                    if line:
                        markdown += f"> {line}\n"
            
            first_content = False
    
    markdown += "\n"
    return markdown

def html_to_markdown(html_content):
    """Konvertiert HTML-Inhalt zu Markdown - Verbesserte Version"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Erweiterte Suche nach dem Hauptinhalt
    content_div = soup.find('div', class_='zendesk-article-content')
    if not content_div:
        content_div = soup.find('div', class_='content')
    if not content_div:
        # DocBook-spezifische Strukturen
        content_div = soup.find('div', class_='section')
    if not content_div:
        content_div = soup.body or soup
    
    markdown_parts = []
    images_found = []
    
    def process_element(element, depth=0):
        """Verarbeitet ein HTML-Element rekursiv - Verbesserte Version"""
        if not element:
            return ""
        
        # String-Inhalte direkt verarbeiten
        if isinstance(element, str):
            text = element.strip()
            return text
        
        # YouTube iframe erkennen
        if element.name == 'iframe':
            src = element.get('src', '')
            if 'youtube.com' in src or 'youtu.be' in src:
                return f"\n**[YouTube Video]({src})**\n\n"
        
        # Alle Bilder erfassen (auch in verschachtelten Strukturen)
        if element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '')
            if src:
                images_found.append(src)
                # Bildpfad anpassen
                if src.startswith('../images/'):
                    src = src.replace('../images/', 'images/')
                elif src.startswith('images/'):
                    src = src  # Bereits korrekt
                else:
                    # Relative Pfade zu images/ konvertieren
                    if '/' in src and not src.startswith('http'):
                        src = f"images/{src.split('/')[-1]}"
                return f"![{alt}]({src})\n\n"
        
        # Verbesserte Info-Boxen-Erkennung
        classes = element.get('class', [])
        if element.name == 'div' and any(cls in classes for cls in ['tip', 'important', 'warning', 'note']):
            return process_info_box(element)
        
        # Überschriften (auch DocBook h1-h6)
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            text = clean_text(element.get_text())
            if text:
                return f"\n{'#' * level} {text}\n\n"
        
        # DocBook-spezifische Titel-Strukturen
        if element.name == 'div' and 'titlepage' in classes:
            title_elem = element.find(['h1', 'h2', 'h3', 'h4'])
            if title_elem:
                level = 2  # Default zu h2
                if title_elem.name:
                    level = int(title_elem.name[1])
                text = clean_text(title_elem.get_text())
                if text:
                    return f"\n{'#' * level} {text}\n\n"
        
        # Paragraphen mit verbesserter Formatierung
        if element.name == 'p':
            # Inline-Formatierung verarbeiten
            content = ""
            for child in element.children:
                content += process_element(child, depth + 1)
            
            content = content.strip()
            if content:
                return f"{content}\n\n"
        
        # Listen verbessert mit besserer Formatierung
        if element.name in ['ul', 'ol']:
            return process_list(element) + "\n"
        
        # Verbesserte Tabellen-Verarbeitung
        if element.name == 'table':
            return process_table(element)
        
        # Links
        if element.name == 'a':
            href = element.get('href', '')
            text = clean_text(element.get_text())
            if href and text:
                return f"[{text}]({href})"
            elif text:
                return text
        
        # Text-Formatierung - nur wenn nicht bereits inline verarbeitet
        if element.name in ['strong', 'b']:
            text = clean_text(element.get_text())
            if text:
                return f"**{text}** "
        
        if element.name in ['em', 'i']:
            text = clean_text(element.get_text())
            if text:
                return f"*{text}* "
        
        # Span-Elemente mit bold class
        if element.name == 'span':
            classes = element.get('class', [])
            if 'bold' in classes:
                # Suche nach strong/b Elementen in span
                strong_elem = element.find(['strong', 'b'])
                if strong_elem:
                    text = clean_text(strong_elem.get_text())
                    return f"**{text}** " if text else ""
            
            # Normale span - Inhalt rekursiv verarbeiten
            result = ""
            for child in element.children:
                result += process_element(child, depth + 1)
            return result
        
        # Code
        if element.name == 'code':
            text = element.get_text()
            return f"`{text}` "
        
        if element.name == 'pre':
            text = element.get_text()
            return f"\n```\n{text}\n```\n\n"
        
        # Blockquote
        if element.name == 'blockquote':
            text = clean_text(element.get_text())
            lines = text.split('\n')
            quoted_lines = [f"> {line}" for line in lines if line.strip()]
            return '\n'.join(quoted_lines) + '\n\n'
        
        # Zeilenumbrüche
        if element.name == 'br':
            return "\n"
        
        # DocBook mediaobject (enthält Bilder in Tabellen)
        if element.name == 'div' and 'mediaobject' in classes:
            # Suche nach img-Tags in der gesamten mediaobject-Struktur
            img_tags = element.find_all('img')
            result = ""
            for img in img_tags:
                processed_img = process_element(img, depth + 1)
                if processed_img:
                    result += processed_img
            return result
        
        # Tabellen in DocBook (oft nur Container für Bilder)
        if element.name == 'table' and any(cls in classes for cls in ['image-viewport']):
            # Suche nach img-Tags in der Tabelle
            img_tags = element.find_all('img')
            result = ""
            for img in img_tags:
                processed_img = process_element(img, depth + 1)
                if processed_img:
                    result += processed_img
            # Falls keine Bilder, normale Tabellen-Verarbeitung
            if not result:
                return process_table(element)
            return result
        
        # DocBook-spezifische Strukturen durchlaufen
        if element.name == 'div' and any(cls in classes for cls in ['section', 'sub-topic', 'procedure', 'itemizedlist', 'titlepage']):
            result = ""
            if hasattr(element, 'children'):
                for child in element.children:
                    child_result = process_element(child, depth + 1)
                    if child_result.strip():
                        # Für Listen-Container (procedure) sicherstellen, dass Listen korrekt getrennt werden
                        if 'procedure' in classes and child.name == 'ol':
                            result += "\n" + child_result + "\n"
                        else:
                            result += child_result
            return result
        
        # Prozeduren und Schritte (DocBook)
        if element.name == 'ol' and 'procedure' in classes:
            return "\n" + process_list(element) + "\n"
        
        # Standard-Verarbeitung für alle anderen Elemente
        result = ""
        if hasattr(element, 'children'):
            for child in element.children:
                result += process_element(child, depth + 1)
        
        return result
    
    # Hauptinhalt verarbeiten - alle Kinder durchlaufen
    processed_content = process_element(content_div)
    
    # Debug: Gefundene Bilder ausgeben
    if images_found:
        print(f"Gefundene Bilder: {len(images_found)}")
        for img in images_found:
            print(f"   - {img}")
    
    # Markdown bereinigen
    markdown = processed_content
    
    # Intelligente Leerzeichen-Bereinigung
    markdown = clean_markdown_spacing(markdown)
    
    # Mehrfache Leerzeilen reduzieren
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    # Leere Zeilen am Anfang/Ende entfernen
    markdown = markdown.strip()
    
    return markdown

def convert_html_file(input_path, output_path):
    """Konvertiert eine HTML-Datei zu Markdown"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        markdown_content = html_to_markdown(html_content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Konvertiert: {input_path} → {output_path}")
        return True
        
    except Exception as e:
        print(f"Fehler bei {input_path}: {e}")
        return False

def main():
    """Hauptfunktion"""
    script_dir = Path(__file__).parent
    original_dir = script_dir / 'original'
    markdown_dir = script_dir / 'markdown'
    
    # Markdown-Ordner erstellen falls nicht vorhanden
    markdown_dir.mkdir(exist_ok=True)
    
    # Alle HTML-Dateien im original Ordner finden
    html_files = list(original_dir.glob('*.html'))
    
    if not html_files:
        print("Keine HTML-Dateien im original/ Ordner gefunden")
        return
    
    success_count = 0
    total_count = len(html_files)
    
    print(f"Konvertiere {total_count} HTML-Datei(en)...")
    
    for html_file in html_files:
        # Output-Dateiname: .html → .md
        markdown_file = markdown_dir / f"{html_file.stem}.md"
        
        if convert_html_file(html_file, markdown_file):
            success_count += 1
    
    print(f"\nKonvertierung abgeschlossen: {success_count}/{total_count} Dateien erfolgreich")
    
    if success_count > 0:
        print(f"Markdown-Dateien gespeichert in: {markdown_dir}")

if __name__ == "__main__":
    main()