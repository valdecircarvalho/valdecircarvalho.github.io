import json
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://valdecir.com/'
LANGS = {'en': BASE+'index.html', 'pt-BR': BASE+'index-ptbr.html', 'x-default': BASE+'index.html'}

class Page(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.tags = []
        self.feed((ROOT / filename).read_text())
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
    def attrs(self, tag, **filters):
        return [a for t, a in self.tags if t == tag and all(a.get(k) == v for k,v in filters.items())]

class SiteTests(unittest.TestCase):
    def test_sitemap_canonical_content_and_reciprocal_languages(self):
        root = ET.parse(ROOT/'sitemap.xml').getroot()
        ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9', 'h':'http://www.w3.org/1999/xhtml'}
        urls = root.findall('s:url', ns)
        self.assertEqual([u.find('s:loc',ns).text for u in urls], list(dict.fromkeys(LANGS.values())))
        for url in urls:
            self.assertEqual({a.attrib['hreflang']:a.attrib['href'] for a in url.findall('h:link',ns)}, LANGS)
            page = Page(url.find('s:loc',ns).text.removeprefix(BASE))
            self.assertEqual(page.attrs('link', rel='canonical')[0]['href'], url.find('s:loc',ns).text)
            self.assertEqual({a['hreflang']:a['href'] for a in page.attrs('link', rel='alternate')}, LANGS)

    def test_error_pages_not_indexable_or_language_equivalents(self):
        for name in ('404.html','404-ptbr.html'):
            page = Page(name)
            self.assertIn('noindex', page.attrs('meta',name='robots')[0]['content'])
            self.assertEqual(page.attrs('link',rel='alternate'), [])

    def test_person_identity_matches_visible_profile(self):
        import re
        for filename in ('index.html','index-ptbr.html'):
            html = (ROOT/filename).read_text()
            data = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',html,re.S)[1])
            self.assertEqual(data['@type'], 'ProfilePage')
            self.assertEqual(data['url'], BASE+filename)
            person = data['mainEntity']
            self.assertEqual(person['@id'], BASE+'#person')
            self.assertEqual(person['url'], BASE+'index.html')
            self.assertIn(person['name'], html.split('</head>')[1])
            self.assertNotIn('alumniOf',person)

    def test_portuguese_logo_preserves_language(self):
        html = (ROOT/'index-ptbr.html').read_text()
        self.assertIn('<a href="index-ptbr.html">',html.split('class="ds-logo"')[1].split('</div>')[0])

    def test_internal_assets_and_links_exist(self):
        from urllib.parse import urlsplit, unquote
        for filename in ROOT.glob('*.html'):
            page = Page(filename.name)
            for tag, attrs in page.tags:
                for key in ('href','src'):
                    href = attrs.get(key,'')
                    url = urlsplit(href)
                    if href and not url.scheme and not url.netloc and url.path:
                        self.assertTrue((ROOT/unquote(url.path).lstrip('/')).exists(), f'{filename.name}: {href}')

if __name__ == '__main__':
    unittest.main()
