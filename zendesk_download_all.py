#!/usr/bin/env python3
"""
Zendesk HTML Analyzer

Dieses Skript lädt alle Artikel aus Zendesk herunter und analysiert den rohen HTML-Inhalt.
Es erstellt umfassende Analysen aller HTML-Strukturen, CSS-Klassen und Elemente.
Die Ergebnisse werden als JSON-Report, Markdown-Summary und Beispiele-Ordner ausgegeben.
"""

import os
import re
import json
import time
import hashlib
import urllib.parse
from pathlib import Path
from typing import List, Dict, Optional, Set, Any, Tuple
from collections import defaultdict, Counter
import requests
from bs4 import BeautifulSoup, NavigableString
from tqdm import tqdm
from dotenv import load_dotenv
from PIL import Image
import io
import concurrent.futures
from threading import Lock

# .env Datei laden
load_dotenv()


class HTMLAnalyzer:
    def __init__(self):
        """
        Initialisiert den HTML Analyzer mit Konfiguration aus .env Datei.
        """
        # Konfiguration aus .env laden
        self.subdomain = os.getenv('ZENDESK_SUBDOMAIN')
        self.email = os.getenv('ZENDESK_EMAIL')
        self.api_token = os.getenv('ZENDESK_API_TOKEN')
        self.locale = os.getenv('ZENDESK_LOCALE', 'de')
        self.base_url_env = os.getenv('ZENDESK_BASE_URL')
        
        # Validierung der Konfiguration
        if not all([self.subdomain, self.email, self.api_token]):
            raise ValueError("Zendesk-Konfiguration unvollständig! Prüfen Sie die .env Datei.")
        
        # Base URL bestimmen
        if self.base_url_env:
            self.base_url = f"{self.base_url_env}/api/v2"
        else:
            self.base_url = f"https://{self.subdomain}.zendesk.com/api/v2"
        
        # HTTP Session konfigurieren
        self.session = requests.Session()
        self.session.auth = (f"{self.email}/token", self.api_token)
        
        # Ausgabeverzeichnisse für markdown erstellen (umbenannt von markdowndemo)
        self.markdown_dir = Path("source")
        self.original_html_dir = self.markdown_dir / "original"
        self.downloaded_images_dir = self.markdown_dir / "original" / "images"
        
        # Backward compatibility - output_dir wird noch verwendet
        self.output_dir = self.markdown_dir  # Fallback für Legacy-Code
        self.examples_dir = self.original_html_dir  # Nicht verwendet, aber für Kompatibilität
        
        # Ordner leeren bevor Download startet
        self.clear_directories()
        
        # Ordner erstellen
        self.original_html_dir.mkdir(parents=True, exist_ok=True)
        self.downloaded_images_dir.mkdir(parents=True, exist_ok=True)
        
        # Analyse-Datenstrukturen initialisieren
        self.analysis_data = {
            'metadata': {
                'zendesk_subdomain': self.subdomain,
                'locale': self.locale,
                'analysis_timestamp': None,
                'total_articles_analyzed': 0,
                'total_html_length': 0,
                'total_images_found': 0,
                'total_images_downloaded': 0,
                'total_images_failed': 0,
                'total_image_size_bytes': 0
            },
            'html_tags': defaultdict(int),
            'css_classes': defaultdict(int),
            'css_ids': defaultdict(int),
            'html_attributes': defaultdict(lambda: defaultdict(int)),
            'image_formats': defaultdict(int),
            'image_sources': defaultdict(int),
            'image_dimensions': defaultdict(int),
            'image_file_sizes': defaultdict(int),
            'image_download_status': defaultdict(int),
            'link_types': defaultdict(int),
            'table_structures': defaultdict(int),
            'list_structures': defaultdict(int),
            'code_structures': defaultdict(int),
            'special_structures': defaultdict(int),
            'text_formatting': defaultdict(int),
            'media_elements': defaultdict(int),
            'form_elements': defaultdict(int),
            'semantic_elements': defaultdict(int)
        }
        
        # Beispiele für verschiedene Strukturtypen
        self.examples = defaultdict(list)
        self.max_examples_per_type = 5
        
        # Bild-Download-Konfiguration
        self.download_timeout = 30
        self.max_concurrent_downloads = 5
        self.download_lock = Lock()
        self.image_url_mapping = {}  # Original URL -> Lokaler Pfad
        self.processed_image_hashes = set()  # Vermeidung von Duplikaten
        
        print(f"HTML Analyzer Konfiguration geladen:")
        print(f"  Subdomain: {self.subdomain}")
        print(f"  E-Mail: {self.email}")
        print(f"  Locale: {self.locale}")
        print(f"  Base URL: {self.base_url}")
        print(f"  Ausgabeverzeichnis: {self.output_dir}")
        print(f"  Bild-Download-Verzeichnis: {self.downloaded_images_dir}")

    def clear_directories(self) -> None:
        """
        Löscht alle HTML-Dateien und Bilder in den Zielordnern.
        """
        import shutil
        
        print("Lösche vorhandene Dateien...")
        
        # Original HTML-Ordner leeren
        if self.original_html_dir.exists():
            for file in self.original_html_dir.glob('*.html'):
                try:
                    file.unlink()
                    print(f"  Gelöscht: {file}")
                except Exception as e:
                    print(f"  Fehler beim Löschen von {file}: {e}")
        
        # Images-Ordner leeren
        if self.downloaded_images_dir.exists():
            try:
                shutil.rmtree(self.downloaded_images_dir)
                print(f"  Ordner geleert: {self.downloaded_images_dir}")
            except Exception as e:
                print(f"  Fehler beim Leeren von {self.downloaded_images_dir}: {e}")
        
        print("Ordner bereinigt.")

    def get_all_sections(self) -> List[Dict]:
        """
        Holt alle Sektionen aus der Zendesk Knowledge Base.
        
        Returns:
            Liste aller Sektionen
        """
        sections = []
        url = f"{self.base_url}/help_center/{self.locale}/sections.json"
        
        while url:
            try:
                response = self.session.get(url)
                response.raise_for_status()
                data = response.json()
                
                sections.extend(data['sections'])
                url = data.get('next_page')
                
                # Rate limiting respektieren
                time.sleep(0.1)
                
            except requests.exceptions.RequestException as e:
                print(f"Fehler beim Abrufen der Sektionen: {e}")
                break
                
        return sections

    def get_articles_in_section(self, section_id: int) -> List[Dict]:
        """
        Holt alle Artikel einer bestimmten Sektion.
        
        Args:
            section_id: ID der Sektion
            
        Returns:
            Liste aller Artikel in der Sektion
        """
        articles = []
        url = f"{self.base_url}/help_center/{self.locale}/sections/{section_id}/articles.json"
        
        while url:
            try:
                response = self.session.get(url)
                response.raise_for_status()
                data = response.json()
                
                articles.extend(data['articles'])
                url = data.get('next_page')
                
                # Rate limiting respektieren
                time.sleep(0.1)
                
            except requests.exceptions.RequestException as e:
                print(f"Fehler beim Abrufen der Artikel für Sektion {section_id}: {e}")
                break
                
        return articles

    def get_article_content(self, article_id: int) -> Optional[Dict]:
        """
        Holt den vollständigen Inhalt eines Artikels.
        
        Args:
            article_id: ID des Artikels
            
        Returns:
            Artikel-Daten mit vollständigem Inhalt
        """
        try:
            url = f"{self.base_url}/help_center/{self.locale}/articles/{article_id}.json"
            response = self.session.get(url)
            response.raise_for_status()
            
            time.sleep(0.1)  # Rate limiting
            return response.json()['article']
            
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Abrufen des Artikels {article_id}: {e}")
            return None

    def _create_safe_filename(self, url: str, article_id: int = None) -> str:
        """
        Erstellt einen sicheren Dateinamen aus einer URL.
        
        Args:
            url: Original-URL des Bildes
            article_id: ID des Artikels (optional)
            
        Returns:
            Sicherer Dateiname
        """
        try:
            # URL parsen und Dateiname extrahieren
            parsed_url = urllib.parse.urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            # Wenn kein Dateiname vorhanden, einen generieren
            if not filename or '.' not in filename:
                url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
                # Versuche Dateiformat aus URL zu ermitteln
                if '.png' in url.lower():
                    filename = f"image_{url_hash}.png"
                elif '.jpg' in url.lower() or '.jpeg' in url.lower():
                    filename = f"image_{url_hash}.jpg"
                elif '.gif' in url.lower():
                    filename = f"image_{url_hash}.gif"
                elif '.svg' in url.lower():
                    filename = f"image_{url_hash}.svg"
                elif '.webp' in url.lower():
                    filename = f"image_{url_hash}.webp"
                else:
                    filename = f"image_{url_hash}.png"  # Default
            
            # Dateiname bereinigen
            filename = re.sub(r'[^\w\s.-]', '', filename)
            filename = re.sub(r'[-\s]+', '-', filename)
            filename = filename.strip('-')
            
            # Präfix mit Artikel-ID hinzufügen wenn vorhanden
            if article_id:
                filename = f"{article_id}_{filename}"
            
            return filename
            
        except Exception as e:
            # Fallback: Hash der URL als Dateiname
            url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
            prefix = f"{article_id}_" if article_id else ""
            return f"{prefix}image_{url_hash}.png"

    def _get_image_hash(self, image_data: bytes) -> str:
        """
        Erstellt einen Hash für Bilddaten zur Duplikatserkennung.
        
        Args:
            image_data: Binäre Bilddaten
            
        Returns:
            SHA256-Hash der Bilddaten
        """
        return hashlib.sha256(image_data).hexdigest()

    def _analyze_image_properties(self, image_data: bytes, file_path: Path) -> Dict[str, Any]:
        """
        Analysiert Eigenschaften eines heruntergeladenen Bildes.
        
        Args:
            image_data: Binäre Bilddaten
            file_path: Pfad zur gespeicherten Datei
            
        Returns:
            Dictionary mit Bildeigenschaften
        """
        properties = {
            'file_size_bytes': len(image_data),
            'file_size_kb': round(len(image_data) / 1024, 2),
            'width': None,
            'height': None,
            'format': None,
            'mode': None
        }
        
        try:
            # PIL verwenden für Bildanalyse
            with Image.open(io.BytesIO(image_data)) as img:
                properties['width'] = img.width
                properties['height'] = img.height
                properties['format'] = img.format
                properties['mode'] = img.mode
                
                # Kategorien für Statistiken
                dimensions_key = f"{img.width}x{img.height}"
                self.analysis_data['image_dimensions'][dimensions_key] += 1
                
                # Dateigröße-Kategorien
                size_kb = round(len(image_data) / 1024, 2)
                if size_kb < 10:
                    size_category = "under_10kb"
                elif size_kb < 50:
                    size_category = "10-50kb"
                elif size_kb < 100:
                    size_category = "50-100kb"
                elif size_kb < 500:
                    size_category = "100-500kb"
                else:
                    size_category = "over_500kb"
                
                self.analysis_data['image_file_sizes'][size_category] += 1
                
        except Exception as e:
            print(f"Fehler bei der Bildanalyse für {file_path}: {e}")
            
        return properties

    def _download_image(self, url: str, article_id: int, article_title: str) -> Optional[Dict[str, Any]]:
        """
        Lädt ein Bild herunter und speichert es lokal.
        
        Args:
            url: URL des Bildes
            article_id: ID des Artikels
            article_title: Titel des Artikels
            
        Returns:
            Dictionary mit Download-Informationen oder None bei Fehler
        """
        try:
            # Bilder direkt in images-Ordner speichern
            article_dir = self.downloaded_images_dir
            article_dir.mkdir(parents=True, exist_ok=True)
            
            # Absoluten URL erstellen falls nötig
            if url.startswith('//'):
                url = 'https:' + url
            elif url.startswith('/'):
                # Relative URL zu Zendesk-Domain ergänzen
                if self.base_url_env:
                    base_domain = self.base_url_env.replace('/api/v2', '')
                else:
                    base_domain = f"https://{self.subdomain}.zendesk.com"
                url = base_domain + url
            
            # Bild herunterladen
            response = requests.get(url, timeout=self.download_timeout, stream=True)
            response.raise_for_status()
            
            image_data = response.content
            
            # Duplikatsprüfung
            image_hash = self._get_image_hash(image_data)
            if image_hash in self.processed_image_hashes:
                with self.download_lock:
                    self.analysis_data['image_download_status']['duplicate_skipped'] += 1
                return None
            
            self.processed_image_hashes.add(image_hash)
            
            # Sicheren Dateinamen erstellen
            filename = self._create_safe_filename(url, article_id)
            file_path = article_dir / filename
            
            # Datei speichern
            with open(file_path, 'wb') as f:
                f.write(image_data)
            
            # Bildanalyse
            properties = self._analyze_image_properties(image_data, file_path)
            
            # Mapping speichern (relativer Pfad zu markdown)
            relative_path = str(file_path.relative_to(self.markdown_dir))
            self.image_url_mapping[url] = relative_path
            
            # Statistiken aktualisieren
            with self.download_lock:
                self.analysis_data['metadata']['total_images_downloaded'] += 1
                self.analysis_data['metadata']['total_image_size_bytes'] += len(image_data)
                self.analysis_data['image_download_status']['success'] += 1
            
            return {
                'original_url': url,
                'local_path': relative_path,
                'filename': filename,
                'article_id': article_id,
                'article_title': article_title,
                'properties': properties,
                'download_timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except requests.exceptions.Timeout:
            with self.download_lock:
                self.analysis_data['image_download_status']['timeout'] += 1
                self.analysis_data['metadata']['total_images_failed'] += 1
            print(f"Timeout beim Download: {url}")
            return None
            
        except requests.exceptions.RequestException as e:
            with self.download_lock:
                self.analysis_data['image_download_status']['http_error'] += 1
                self.analysis_data['metadata']['total_images_failed'] += 1
            print(f"HTTP-Fehler beim Download von {url}: {e}")
            return None
            
        except Exception as e:
            with self.download_lock:
                self.analysis_data['image_download_status']['other_error'] += 1
                self.analysis_data['metadata']['total_images_failed'] += 1
            print(f"Allgemeiner Fehler beim Download von {url}: {e}")
            return None

    def _download_images_batch(self, image_urls: List[Tuple[str, int, str]]) -> List[Dict[str, Any]]:
        """
        Lädt mehrere Bilder parallel herunter.
        
        Args:
            image_urls: Liste von Tupeln (url, article_id, article_title)
            
        Returns:
            Liste der erfolgreich heruntergeladenen Bilder
        """
        downloaded_images = []
        
        if not image_urls:
            return downloaded_images
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_concurrent_downloads) as executor:
            # Futures für alle Downloads erstellen
            future_to_url = {
                executor.submit(self._download_image, url, article_id, article_title): url
                for url, article_id, article_title in image_urls
            }
            
            # Ergebnisse sammeln mit Progress Bar
            for future in tqdm(concurrent.futures.as_completed(future_to_url),
                             total=len(future_to_url),
                             desc="Lade Bilder herunter",
                             leave=False):
                try:
                    result = future.result()
                    if result:
                        downloaded_images.append(result)
                except Exception as e:
                    url = future_to_url[future]
                    print(f"Fehler beim Download von {url}: {e}")
        
        return downloaded_images

    def analyze_html_content(self, html_content: str, article_title: str = "", article_id: int = None) -> List[Tuple[str, int, str]]:
        """
        Extrahiert nur Bild-URLs für Download - alle anderen Analysen auskommentiert.
        
        Args:
            html_content: HTML-Inhalt des Artikels
            article_title: Titel des Artikels
            article_id: ID des Artikels
            
        Returns:
            Liste von Tupeln (url, article_id, article_title) für Bild-Download
        """
        image_urls_for_download = []
        
        if not html_content:
            return image_urls_for_download
        
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # NUR Bilder analysieren und URLs für Download sammeln
            image_urls_for_download = self._analyze_images(soup, article_title, article_id)
            
            # # ALLE ANDEREN ANALYSEN AUSKOMMENTIERT:
            # # HTML-Tags analysieren
            # self._analyze_html_tags(soup)
            #
            # # CSS-Klassen und IDs analysieren
            # self._analyze_css_classes_and_ids(soup)
            #
            # # HTML-Attribute analysieren
            # self._analyze_html_attributes(soup)
            #
            # # Links analysieren
            # self._analyze_links(soup, article_title)
            #
            # # Tabellen analysieren
            # self._analyze_tables(soup, article_title)
            #
            # # Listen analysieren
            # self._analyze_lists(soup, article_title)
            #
            # # Code-Strukturen analysieren
            # self._analyze_code_structures(soup, article_title)
            #
            # # Spezielle Strukturen analysieren
            # self._analyze_special_structures(soup, article_title)
            #
            # # Text-Formatierung analysieren
            # self._analyze_text_formatting(soup)
            #
            # # Media-Elemente analysieren
            # self._analyze_media_elements(soup, article_title)
            #
            # # Form-Elemente analysieren
            # self._analyze_form_elements(soup)
            #
            # # Semantische Elemente analysieren
            # self._analyze_semantic_elements(soup)
            #
            # # HTML-Länge zur Gesamtstatistik hinzufügen
            # self.analysis_data['metadata']['total_html_length'] += len(html_content)
            
        except Exception as e:
            print(f"Fehler bei der Bild-Extraktion: {e}")
        
        return image_urls_for_download

    def _analyze_html_tags(self, soup: BeautifulSoup) -> None:
        """Analysiert alle HTML-Tags im Dokument"""
        for element in soup.find_all():
            tag_name = element.name.lower()
            self.analysis_data['html_tags'][tag_name] += 1

    def _analyze_css_classes_and_ids(self, soup: BeautifulSoup) -> None:
        """Analysiert CSS-Klassen und IDs"""
        for element in soup.find_all():
            # CSS-Klassen
            classes = element.get('class', [])
            if isinstance(classes, list):
                for css_class in classes:
                    self.analysis_data['css_classes'][css_class] += 1
            
            # CSS-IDs
            element_id = element.get('id')
            if element_id:
                self.analysis_data['css_ids'][element_id] += 1

    def _analyze_html_attributes(self, soup: BeautifulSoup) -> None:
        """Analysiert HTML-Attribute"""
        for element in soup.find_all():
            tag_name = element.name.lower()
            for attr_name, attr_value in element.attrs.items():
                self.analysis_data['html_attributes'][tag_name][attr_name] += 1

    def _analyze_images(self, soup: BeautifulSoup, article_title: str, article_id: int = None) -> List[Tuple[str, int, str]]:
        """
        Analysiert Bild-Elemente und sammelt URLs für Download.
        
        Args:
            soup: BeautifulSoup-Objekt
            article_title: Titel des Artikels
            article_id: ID des Artikels
            
        Returns:
            Liste von Tupeln (url, article_id, article_title) für Download
        """
        images = soup.find_all('img')
        image_urls_for_download = []
        
        for img in images:
            src = img.get('src', '')
            alt = img.get('alt', '')
            
            # Bildstatistiken aktualisieren
            self.analysis_data['metadata']['total_images_found'] += 1
            
            # Bildformat und Quelle ermitteln
            if src:
                # URL-Struktur analysieren
                if 'zendesk.com' in src:
                    self.analysis_data['image_sources']['zendesk_hosted'] += 1
                elif src.startswith('http'):
                    self.analysis_data['image_sources']['external'] += 1
                elif src.startswith('data:'):
                    self.analysis_data['image_sources']['base64_embedded'] += 1
                    # Base64-Bilder werden nicht heruntergeladen
                    continue
                elif src.startswith('//'):
                    self.analysis_data['image_sources']['protocol_relative'] += 1
                elif src.startswith('/'):
                    self.analysis_data['image_sources']['relative'] += 1
                else:
                    self.analysis_data['image_sources']['other'] += 1
                
                # Dateiformat aus URL ermitteln
                format_detected = False
                for fmt in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp', '.tiff']:
                    if fmt in src.lower():
                        self.analysis_data['image_formats'][fmt] += 1
                        format_detected = True
                        break
                
                if not format_detected:
                    self.analysis_data['image_formats']['unknown'] += 1
                
                # URL für Download sammeln (außer base64)
                if not src.startswith('data:') and article_id:
                    image_urls_for_download.append((src, article_id, article_title))
            
            # Beispiel speichern
            self._save_example('images', str(img), article_title)
        
        return image_urls_for_download

    def _analyze_links(self, soup: BeautifulSoup, article_title: str) -> None:
        """Analysiert Links und deren Typen"""
        links = soup.find_all('a')
        
        for link in links:
            href = link.get('href', '')
            
            if href:
                if href.startswith('http'):
                    if 'zendesk.com' in href:
                        self.analysis_data['link_types']['zendesk_internal'] += 1
                    else:
                        self.analysis_data['link_types']['external'] += 1
                elif href.startswith('#'):
                    self.analysis_data['link_types']['anchor'] += 1
                elif href.startswith('mailto:'):
                    self.analysis_data['link_types']['email'] += 1
                elif href.startswith('tel:'):
                    self.analysis_data['link_types']['telephone'] += 1
                else:
                    self.analysis_data['link_types']['relative'] += 1
            else:
                self.analysis_data['link_types']['empty_href'] += 1
            
            # Beispiel speichern
            self._save_example('links', str(link), article_title)

    def _analyze_tables(self, soup: BeautifulSoup, article_title: str) -> None:
        """Analysiert Tabellen-Strukturen"""
        tables = soup.find_all('table')
        
        for table in tables:
            # Tabellen-Struktur analysieren
            has_thead = bool(table.find('thead'))
            has_tbody = bool(table.find('tbody'))
            has_tfoot = bool(table.find('tfoot'))
            
            structure_key = f"thead:{has_thead}_tbody:{has_tbody}_tfoot:{has_tfoot}"
            self.analysis_data['table_structures'][structure_key] += 1
            
            # Anzahl Spalten und Zeilen
            rows = table.find_all('tr')
            if rows:
                first_row = rows[0]
                cols = len(first_row.find_all(['td', 'th']))
                self.analysis_data['table_structures'][f'columns_{cols}'] += 1
                self.analysis_data['table_structures'][f'rows_{len(rows)}'] += 1
            
            # Beispiel speichern
            self._save_example('tables', str(table), article_title)

    def _analyze_lists(self, soup: BeautifulSoup, article_title: str) -> None:
        """Analysiert Listen-Strukturen"""
        # Ungeordnete Listen
        ul_lists = soup.find_all('ul')
        for ul in ul_lists:
            items = ul.find_all('li', recursive=False)  # Nur direkte Kinder
            self.analysis_data['list_structures'][f'ul_items_{len(items)}'] += 1
            self._save_example('unordered_lists', str(ul), article_title)
        
        # Geordnete Listen
        ol_lists = soup.find_all('ol')
        for ol in ol_lists:
            items = ol.find_all('li', recursive=False)
            self.analysis_data['list_structures'][f'ol_items_{len(items)}'] += 1
            self._save_example('ordered_lists', str(ol), article_title)
        
        # Definitionslisten
        dl_lists = soup.find_all('dl')
        for dl in dl_lists:
            dt_count = len(dl.find_all('dt'))
            dd_count = len(dl.find_all('dd'))
            self.analysis_data['list_structures'][f'dl_dt_{dt_count}_dd_{dd_count}'] += 1
            self._save_example('definition_lists', str(dl), article_title)

    def _analyze_code_structures(self, soup: BeautifulSoup, article_title: str) -> None:
        """Analysiert Code-Strukturen"""
        # Inline-Code
        code_elements = soup.find_all('code')
        for code in code_elements:
            if code.parent and code.parent.name == 'pre':
                self.analysis_data['code_structures']['code_blocks'] += 1
            else:
                self.analysis_data['code_structures']['inline_code'] += 1
            self._save_example('code_elements', str(code), article_title)
        
        # Pre-Blöcke
        pre_elements = soup.find_all('pre')
        for pre in pre_elements:
            self.analysis_data['code_structures']['pre_blocks'] += 1
            self._save_example('pre_blocks', str(pre), article_title)

    def _analyze_special_structures(self, soup: BeautifulSoup, article_title: str) -> None:
        """Analysiert spezielle HTML-Strukturen wie Notizen, Warnungen etc."""
        # Divs mit speziellen Klassen
        divs = soup.find_all('div')
        
        special_classes = ['note', 'warning', 'info', 'tip', 'alert', 'callout', 'highlight']
        
        for div in divs:
            classes = div.get('class', [])
            if isinstance(classes, list):
                for special_class in special_classes:
                    if any(special_class in cls.lower() for cls in classes):
                        self.analysis_data['special_structures'][f'div_class_{special_class}'] += 1
                        self._save_example(f'special_div_{special_class}', str(div), article_title)
                        break
        
        # Blockquotes
        blockquotes = soup.find_all('blockquote')
        for blockquote in blockquotes:
            self.analysis_data['special_structures']['blockquotes'] += 1
            self._save_example('blockquotes', str(blockquote), article_title)

    def _analyze_text_formatting(self, soup: BeautifulSoup) -> None:
        """Analysiert Text-Formatierungs-Elemente"""
        formatting_tags = ['b', 'strong', 'i', 'em', 'u', 'mark', 'del', 'ins', 'sub', 'sup', 'small']
        
        for tag in formatting_tags:
            elements = soup.find_all(tag)
            if elements:
                self.analysis_data['text_formatting'][tag] += len(elements)

    def _analyze_media_elements(self, soup: BeautifulSoup, article_title: str) -> None:
        """Analysiert Media-Elemente"""
        # Videos
        videos = soup.find_all('video')
        for video in videos:
            self.analysis_data['media_elements']['video'] += 1
            self._save_example('videos', str(video), article_title)
        
        # Audio
        audios = soup.find_all('audio')
        for audio in audios:
            self.analysis_data['media_elements']['audio'] += 1
            self._save_example('audio', str(audio), article_title)
        
        # Iframes (oft für eingebettete Inhalte)
        iframes = soup.find_all('iframe')
        for iframe in iframes:
            src = iframe.get('src', '')
            if 'youtube' in src:
                self.analysis_data['media_elements']['iframe_youtube'] += 1
            elif 'vimeo' in src:
                self.analysis_data['media_elements']['iframe_vimeo'] += 1
            else:
                self.analysis_data['media_elements']['iframe_other'] += 1
            self._save_example('iframes', str(iframe), article_title)

    def _analyze_form_elements(self, soup: BeautifulSoup) -> None:
        """Analysiert Formular-Elemente"""
        form_tags = ['form', 'input', 'textarea', 'select', 'button', 'label', 'fieldset', 'legend']
        
        for tag in form_tags:
            elements = soup.find_all(tag)
            if elements:
                self.analysis_data['form_elements'][tag] += len(elements)

    def _analyze_semantic_elements(self, soup: BeautifulSoup) -> None:
        """Analysiert semantische HTML5-Elemente"""
        semantic_tags = ['header', 'nav', 'main', 'section', 'article', 'aside', 'footer', 
                        'figure', 'figcaption', 'details', 'summary', 'time']
        
        for tag in semantic_tags:
            elements = soup.find_all(tag)
            if elements:
                self.analysis_data['semantic_elements'][tag] += len(elements)

    def _save_example(self, category: str, html_snippet: str, article_title: str) -> None:
        """
        Speichert ein HTML-Beispiel für eine bestimmte Kategorie.
        
        Args:
            category: Kategorie des Beispiels
            html_snippet: HTML-Code-Snippet
            article_title: Titel des Artikels
        """
        if len(self.examples[category]) < self.max_examples_per_type:
            self.examples[category].append({
                'html': html_snippet,
                'source_article': article_title,
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            })


    def analyze_all_articles(self) -> Dict[str, int]:
        """
        Lädt alle Artikel aus der Zendesk Knowledge Base herunter und analysiert sie.
        Lädt auch alle gefundenen Bilder herunter.
        
        Returns:
            Statistiken über den Analyse-Prozess
        """
        stats = {
            'sections_processed': 0,
            'articles_analyzed': 0,
            'articles_failed': 0
        }
        
        # Liste aller Bild-URLs für Batch-Download
        all_image_urls = []
        
        print("\nLade Sektionen...")
        sections = self.get_all_sections()
        
        if not sections:
            print("Keine Sektionen gefunden!")
            return stats
            
        print(f"Gefunden: {len(sections)} Sektionen")
        
        # Durch alle Sektionen iterieren
        for section in tqdm(sections, desc="Verarbeite Sektionen"):
            section_name = section.get('name', 'Unbekannte_Sektion')
            section_id = section.get('id')
            
            print(f"\nVerarbeite Sektion: {section_name}")
            
            # Artikel in dieser Sektion abrufen
            articles = self.get_articles_in_section(section_id)
            
            if not articles:
                print(f"Keine Artikel in Sektion '{section_name}' gefunden")
                continue
                
            print(f"Gefunden: {len(articles)} Artikel in '{section_name}'")
            
            # Durch alle Artikel in der Sektion iterieren
            for article_summary in tqdm(articles, desc=f"Artikel in {section_name}", leave=False):
                article_id = article_summary.get('id')
                article_title = article_summary.get('title', 'Unbekannter Titel')
                
                # Vollständigen Artikel-Inhalt abrufen
                full_article = self.get_article_content(article_id)
                if not full_article:
                    stats['articles_failed'] += 1
                    print(f"✗ Fehler beim Abrufen: {article_title}")
                    continue
                
                # HTML-Inhalt aus dem Artikel extrahieren
                body = full_article.get("body", "")
                
                # HTML-Inhalt analysieren und speichern
                try:
                    # Original HTML speichern
                    self.save_original_html(article_id, article_title, body, full_article)
                    
                    # HTML-Inhalt analysieren und Bild-URLs sammeln
                    image_urls = self.analyze_html_content(body, article_title, article_id)
                    all_image_urls.extend(image_urls)
                    
                    stats['articles_analyzed'] += 1
                    print(f"✓ Analysiert: {article_title} ({len(image_urls)} Bilder gefunden)")
                except Exception as e:
                    stats['articles_failed'] += 1
                    print(f"✗ Fehler bei der Analyse: {article_title} - {e}")
            
            stats['sections_processed'] += 1
        
        # Bild-Downloads starten
        if all_image_urls:
            print(f"\nStarte Download von {len(all_image_urls)} Bildern...")
            downloaded_images = self._download_images_batch(all_image_urls)
            print(f"✓ Erfolgreich heruntergeladen: {len(downloaded_images)} Bilder")
            
            # Bild-Download-Report speichern
            # self.save_image_download_report(downloaded_images)
        else:
            print("\nKeine Bilder zum Download gefunden.")
        
        # Metadaten aktualisieren
        self.analysis_data['metadata']['analysis_timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S')
        self.analysis_data['metadata']['total_articles_analyzed'] = stats['articles_analyzed']
        
        return stats

    def save_json_report(self) -> None:
        """Speichert den Analyse-Report als JSON-Datei"""
        # Defaultdicts zu normalen Dicts konvertieren für JSON-Serialisierung
        json_data = {}
        for key, value in self.analysis_data.items():
            if isinstance(value, defaultdict):
                if key == 'html_attributes':
                    # Nested defaultdict behandeln
                    json_data[key] = {k: dict(v) for k, v in value.items()}
                else:
                    json_data[key] = dict(value)
            else:
                json_data[key] = value
        
        report_path = self.output_dir / "html_analysis_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        print(f"JSON-Report gespeichert: {report_path}")

    def save_markdown_summary(self) -> None:
        """Speichert eine menschenlesbare Zusammenfassung als Markdown"""
        summary_content = "# Zendesk HTML-Analyse Zusammenfassung\n\n"
        
        # Metadaten
        metadata = self.analysis_data['metadata']
        summary_content += f"**Analyse-Zeitpunkt:** {metadata['analysis_timestamp']}\n"
        summary_content += f"**Zendesk Subdomain:** {metadata['zendesk_subdomain']}\n"
        summary_content += f"**Locale:** {metadata['locale']}\n"
        summary_content += f"**Analysierte Artikel:** {metadata['total_articles_analyzed']}\n"
        summary_content += f"**Gesamt HTML-Länge:** {metadata['total_html_length']:,} Zeichen\n"
        
        # Bild-Statistiken
        summary_content += f"**Bilder gefunden:** {metadata['total_images_found']}\n"
        summary_content += f"**Bilder erfolgreich heruntergeladen:** {metadata['total_images_downloaded']}\n"
        summary_content += f"**Bilder fehlgeschlagen:** {metadata['total_images_failed']}\n"
        if metadata['total_image_size_bytes'] > 0:
            size_mb = metadata['total_image_size_bytes'] / (1024 * 1024)
            summary_content += f"**Gesamte Bildgröße:** {size_mb:.2f} MB\n"
        summary_content += "\n"
        
        # Bild-Statistiken detailliert
        if metadata['total_images_found'] > 0:
            summary_content += "## 📸 Bild-Analyse\n\n"
            
            # Bild-Quellen
            if self.analysis_data['image_sources']:
                summary_content += "### Bild-Quellen\n\n"
                for source, count in sorted(self.analysis_data['image_sources'].items(), key=lambda x: x[1], reverse=True):
                    summary_content += f"- {source}: {count:,}\n"
                summary_content += "\n"
            
            # Bild-Formate
            if self.analysis_data['image_formats']:
                summary_content += "### Bild-Formate\n\n"
                for fmt, count in sorted(self.analysis_data['image_formats'].items(), key=lambda x: x[1], reverse=True):
                    summary_content += f"- `{fmt}`: {count:,}\n"
                summary_content += "\n"
            
            # Bild-Dimensionen (Top 10)
            if self.analysis_data['image_dimensions']:
                summary_content += "### Häufigste Bild-Dimensionen (Top 10)\n\n"
                sorted_dimensions = sorted(self.analysis_data['image_dimensions'].items(), key=lambda x: x[1], reverse=True)
                for dimension, count in sorted_dimensions[:10]:
                    summary_content += f"- {dimension}: {count:,}\n"
                summary_content += "\n"
            
            # Dateigrößen-Kategorien
            if self.analysis_data['image_file_sizes']:
                summary_content += "### Dateigrößen-Verteilung\n\n"
                for size_cat, count in sorted(self.analysis_data['image_file_sizes'].items(), key=lambda x: x[1], reverse=True):
                    summary_content += f"- {size_cat}: {count:,}\n"
                summary_content += "\n"
            
            # Download-Status
            if self.analysis_data['image_download_status']:
                summary_content += "### Download-Status\n\n"
                for status, count in sorted(self.analysis_data['image_download_status'].items(), key=lambda x: x[1], reverse=True):
                    summary_content += f"- {status}: {count:,}\n"
                summary_content += "\n"
        
        # HTML-Tags
        if self.analysis_data['html_tags']:
            summary_content += "## HTML-Tags\n\n"
            sorted_tags = sorted(self.analysis_data['html_tags'].items(), key=lambda x: x[1], reverse=True)
            for tag, count in sorted_tags[:20]:  # Top 20
                summary_content += f"- `{tag}`: {count:,}\n"
            summary_content += "\n"
        
        # CSS-Klassen
        if self.analysis_data['css_classes']:
            summary_content += "## CSS-Klassen (Top 20)\n\n"
            sorted_classes = sorted(self.analysis_data['css_classes'].items(), key=lambda x: x[1], reverse=True)
            for css_class, count in sorted_classes[:20]:
                summary_content += f"- `.{css_class}`: {count:,}\n"
            summary_content += "\n"
        
        # Link-Typen
        if self.analysis_data['link_types']:
            summary_content += "## Link-Typen\n\n"
            for link_type, count in sorted(self.analysis_data['link_types'].items(), key=lambda x: x[1], reverse=True):
                summary_content += f"- {link_type}: {count:,}\n"
            summary_content += "\n"
        
        # Tabellen-Strukturen
        if self.analysis_data['table_structures']:
            summary_content += "## Tabellen-Strukturen\n\n"
            for structure, count in sorted(self.analysis_data['table_structures'].items(), key=lambda x: x[1], reverse=True):
                summary_content += f"- {structure}: {count:,}\n"
            summary_content += "\n"
        
        # Listen-Strukturen
        if self.analysis_data['list_structures']:
            summary_content += "## Listen-Strukturen\n\n"
            for structure, count in sorted(self.analysis_data['list_structures'].items(), key=lambda x: x[1], reverse=True):
                summary_content += f"- {structure}: {count:,}\n"
            summary_content += "\n"
        
        # Code-Strukturen
        if self.analysis_data['code_structures']:
            summary_content += "## Code-Strukturen\n\n"
            for structure, count in sorted(self.analysis_data['code_structures'].items(), key=lambda x: x[1], reverse=True):
                summary_content += f"- {structure}: {count:,}\n"
            summary_content += "\n"
        
        # Spezielle Strukturen
        if self.analysis_data['special_structures']:
            summary_content += "## Spezielle Strukturen\n\n"
            for structure, count in sorted(self.analysis_data['special_structures'].items(), key=lambda x: x[1], reverse=True):
                summary_content += f"- {structure}: {count:,}\n"
            summary_content += "\n"
        
        summary_path = self.output_dir / "html_analysis_summary.md"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        print(f"Markdown-Summary gespeichert: {summary_path}")

    def save_examples(self) -> None:
        """Speichert HTML-Beispiele in separaten Dateien"""
        for category, examples in self.examples.items():
            if not examples:
                continue
            
            category_dir = self.examples_dir / category
            category_dir.mkdir(exist_ok=True)
            
            for i, example in enumerate(examples):
                example_file = category_dir / f"example_{i+1}.html"
                
                # HTML-Beispiel mit Metadaten
                content = f"""<!-- HTML-Beispiel für Kategorie: {category} -->
<!-- Quell-Artikel: {example['source_article']} -->
<!-- Zeitpunkt: {example['timestamp']} -->

{example['html']}
"""
                
                with open(example_file, 'w', encoding='utf-8') as f:
                    f.write(content)
        
        print(f"HTML-Beispiele gespeichert in: {self.examples_dir}")

    def save_original_html(self, article_id: int, article_title: str, html_body: str, full_article: Dict) -> None:
        """
        Speichert den originalen HTML-Inhalt eines Artikels für späteren Vergleich.
        
        Args:
            article_id: ID des Artikels
            article_title: Titel des Artikels
            html_body: HTML-Inhalt des Artikels
            full_article: Vollständige Artikel-Daten aus der API
        """
        try:
            # Sicheren Dateinamen erstellen
            safe_title = re.sub(r'[^\w\s-]', '', article_title)
            safe_title = re.sub(r'[-\s]+', '-', safe_title)
            safe_title = safe_title.strip('-').lower()[:50]  # Max 50 Zeichen
            
            if not safe_title:
                safe_title = f"artikel_{article_id}"
            
            filename = f"{article_id}_{safe_title}.html"
            filepath = self.original_html_dir / filename
            
            # HTML-Datei mit Metadaten erstellen
            html_content = f"""<!DOCTYPE html>
<html lang="{self.locale}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article_title}</title>
    <!--
    Zendesk Original HTML Export
    Artikel-ID: {article_id}
    Titel: {article_title}
    URL: {full_article.get('html_url', 'N/A')}
    Erstellt: {full_article.get('created_at', 'N/A')}
    Aktualisiert: {full_article.get('updated_at', 'N/A')}
    Draft: {full_article.get('draft', False)}
    User Segment ID: {full_article.get('user_segment_id', 'None')}
    Section ID: {full_article.get('section_id', 'N/A')}
    Export-Zeitpunkt: {time.strftime('%Y-%m-%d %H:%M:%S')}
    -->
</head>
<body>
    <div class="zendesk-article-content">
        {html_body if html_body else '<p>Kein HTML-Inhalt vorhanden</p>'}
    </div>
</body>
</html>"""
            
            # Datei speichern
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
                
        except Exception as e:
            print(f"Fehler beim Speichern des Original-HTML für Artikel {article_id}: {e}")

    def save_original_html_index(self) -> None:
        """Erstellt eine Index-Datei für alle gespeicherten Original-HTML-Dateien"""
        try:
            index_content = f"""# Zendesk Original HTML Index

Gesamt analysierte Artikel: {self.analysis_data['metadata']['total_articles_analyzed']}
Analyse-Zeitpunkt: {self.analysis_data['metadata']['analysis_timestamp']}
Zendesk Subdomain: {self.analysis_data['metadata']['zendesk_subdomain']}

## Gespeicherte HTML-Dateien

"""
            
            # Alle HTML-Dateien im original_html Verzeichnis auflisten
            html_files = sorted(self.original_html_dir.glob("*.html"))
            
            for html_file in html_files:
                # Artikel-ID aus Dateiname extrahieren
                article_id = html_file.name.split('_')[0]
                index_content += f"- [{html_file.name}](./{html_file.name}) (Artikel-ID: {article_id})\n"
            
            index_path = self.original_html_dir / "README.md"
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
                
            print(f"Original-HTML Index erstellt: {index_path}")
            
        except Exception as e:
            print(f"Fehler beim Erstellen des HTML-Index: {e}")

    def save_image_download_report(self, downloaded_images: List[Dict[str, Any]]) -> None:
        """
        Speichert einen detaillierten Report über heruntergeladene Bilder.
        
        Args:
            downloaded_images: Liste der erfolgreich heruntergeladenen Bilder
        """
        try:
            # JSON-Report für heruntergeladene Bilder
            image_report = {
                'metadata': {
                    'total_downloaded': len(downloaded_images),
                    'total_found': self.analysis_data['metadata']['total_images_found'],
                    'total_failed': self.analysis_data['metadata']['total_images_failed'],
                    'total_size_bytes': self.analysis_data['metadata']['total_image_size_bytes'],
                    'total_size_mb': round(self.analysis_data['metadata']['total_image_size_bytes'] / (1024 * 1024), 2),
                    'download_timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                },
                'url_mapping': self.image_url_mapping,
                'downloaded_images': downloaded_images,
                'statistics': {
                    'formats': dict(self.analysis_data['image_formats']),
                    'sources': dict(self.analysis_data['image_sources']),
                    'dimensions': dict(self.analysis_data['image_dimensions']),
                    'file_sizes': dict(self.analysis_data['image_file_sizes']),
                    'download_status': dict(self.analysis_data['image_download_status'])
                }
            }
            
            # JSON-Report speichern
            image_report_path = self.output_dir / "image_download_report.json"
            with open(image_report_path, 'w', encoding='utf-8') as f:
                json.dump(image_report, f, indent=2, ensure_ascii=False)
            
            print(f"Bild-Download-Report gespeichert: {image_report_path}")
            
            # Markdown-Index für heruntergeladene Bilder erstellen
            # self.save_image_index()
                
        except Exception as e:
            print(f"Fehler beim Speichern des Bild-Download-Reports: {e}")

    def save_image_index(self) -> None:
        """Erstellt eine Index-Datei für alle heruntergeladenen Bilder"""
        try:
            index_content = f"""# Heruntergeladene Bilder Index

Gesamt gefundene Bilder: {self.analysis_data['metadata']['total_images_found']}
Erfolgreich heruntergeladen: {self.analysis_data['metadata']['total_images_downloaded']}
Fehlgeschlagen: {self.analysis_data['metadata']['total_images_failed']}
Gesamtgröße: {round(self.analysis_data['metadata']['total_image_size_bytes'] / (1024 * 1024), 2)} MB
Download-Zeitpunkt: {time.strftime('%Y-%m-%d %H:%M:%S')}

## Bilder nach Artikel

"""
            
            # Alle Artikel-Verzeichnisse durchsuchen
            article_dirs = sorted([d for d in self.downloaded_images_dir.iterdir() if d.is_dir() and d.name.startswith('article_')])
            
            for article_dir in article_dirs:
                article_id = article_dir.name.replace('article_', '')
                image_files = list(article_dir.glob('*'))
                
                if image_files:
                    index_content += f"### Artikel {article_id}\n\n"
                    for image_file in sorted(image_files):
                        relative_path = image_file.relative_to(self.downloaded_images_dir)
                        # Bildgröße ermitteln
                        try:
                            size_kb = round(image_file.stat().st_size / 1024, 2)
                            index_content += f"- ![{image_file.name}](./{relative_path}) ({size_kb} KB)\n"
                        except:
                            index_content += f"- ![{image_file.name}](./{relative_path})\n"
                    index_content += "\n"
            
            # URL-Mapping hinzufügen
            if self.image_url_mapping:
                index_content += "## URL-Mapping\n\n"
                index_content += "| Original URL | Lokaler Pfad |\n"
                index_content += "|--------------|---------------|\n"
                for original_url, local_path in sorted(self.image_url_mapping.items()):
                    # URLs kürzen für bessere Lesbarkeit
                    short_url = original_url[:60] + "..." if len(original_url) > 60 else original_url
                    index_content += f"| {short_url} | {local_path} |\n"
            
            index_path = self.downloaded_images_dir / "README.md"
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
                
            print(f"Bild-Index erstellt: {index_path}")
            
        except Exception as e:
            print(f"Fehler beim Erstellen des Bild-Index: {e}")


def main():
    """
    Hauptfunktion - Lädt Konfiguration aus .env und startet die HTML-Analyse.
    """
    print("Zendesk HTML Analyzer")
    print("=" * 50)
    
    try:
        # Analyzer initialisieren (lädt automatisch .env)
        analyzer = HTMLAnalyzer()
        
        # Analyse starten
        print("\nStarte HTML-Analyse...")
        start_time = time.time()
        
        stats = analyzer.analyze_all_articles()
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Statistiken ausgeben
        print("\n" + "=" * 50)
        print("HTML-Analyse abgeschlossen!")
        print(f"Dauer: {duration:.2f} Sekunden")
        print(f"Sektionen verarbeitet: {stats['sections_processed']}")
        print(f"Artikel analysiert: {stats['articles_analyzed']}")
        print(f"Fehler: {stats['articles_failed']}")
        
        # # ALLE REPORT-ERSTELLUNGEN AUSKOMMENTIERT:
        # print("\nErstelle Analyse-Reports...")
        # analyzer.save_json_report()
        # analyzer.save_markdown_summary()
        # analyzer.save_examples()
        # analyzer.save_original_html_index()
        
        print(f"\nHTML-Download abgeschlossen!")
        print(f"HTML-Dateien wurden in '{analyzer.original_html_dir}' gespeichert.")
        if analyzer.analysis_data['metadata']['total_images_downloaded'] > 0:
            print(f"Heruntergeladene Bilder wurden in '{analyzer.downloaded_images_dir}' gespeichert.")
            print(f"Gesamt: {analyzer.analysis_data['metadata']['total_images_downloaded']} Bilder ({round(analyzer.analysis_data['metadata']['total_image_size_bytes'] / (1024 * 1024), 2)} MB)")
        
    except ValueError as e:
        print(f"Konfigurationsfehler: {e}")
        print("Bitte prüfen Sie die .env Datei.")
    except KeyboardInterrupt:
        print("\nAnalyse durch Benutzer abgebrochen.")
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")


if __name__ == "__main__":
    main()
