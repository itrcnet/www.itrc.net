"""Audit local build paths and report missing content without hiding failures."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
root=Path(__file__).resolve().parents[1]
site=root/'_site'
report={'pages':0,'missing_links':[],'missing_assets':[],'forbidden_urls':[],'forms':[]}
class Audit(HTMLParser):
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='form': report['forms'].append({'page':str(rel),'action':a.get('action','')})
  for attr in ('href','src','poster','action'):
   u=a.get(attr,'')
   if not u:continue
   parts=urlsplit(u)
   if u.startswith('/') or parts.hostname in ('www.itrc.net','itrc.net'):
    report['forbidden_urls'].append({'page':str(rel),'url':u})
   if parts.scheme or parts.netloc or not parts.path:continue
   p=(page.parent/unquote(parts.path)).resolve()
   if not p.is_file() and not (p/'index.html').is_file():
    kind='missing_links' if tag=='a' else 'missing_assets'
    report[kind].append({'page':str(rel),'url':u,'target':str(p.relative_to(site.resolve()))})
for page in site.rglob('*.html'):
 rel=page.relative_to(site);text=page.read_text()
 assert text.startswith('<!DOCTYPE html>'),rel
 assert '{{' not in text and '{% raw %}' not in text,rel
 assert '[su_spoiler' not in text,rel
 Audit().feed(text); report['pages']+=1
expected=sum(1 for p in root.rglob('*') if p.is_file() and p.suffix in ('.html', '.md') and p.name != 'README.md' and not p.is_relative_to(root/'meet/sample') and not any(part in ('_site', '_layouts', '_includes', 'vendor', '.jekyll-cache', 'reports', 'scripts', '.git') for part in p.relative_to(root).parts))
assert report['pages']==expected,(report['pages'],expected)
class FragmentIndex(HTMLParser):
 def __init__(self, text):
  super().__init__(); self.ids=set(); self.links=[]; self.feed(text)
 def handle_starttag(self, tag, attrs):
  a=dict(attrs)
  if a.get('id'): self.ids.add(a['id'])
  if tag=='a' and a.get('name'): self.ids.add(a['name'])
  if tag=='a' and a.get('href'): self.links.append(a['href'])
  if tag=='meta' and a.get('http-equiv','').lower()=='refresh':
   value=a.get('content','')
   if 'url=' in value.lower(): self.links.append(value.split('=',1)[1])
indices={p.resolve():FragmentIndex(p.read_text()) for p in site.rglob('*.html')}
report['missing_fragments']=[]
report['missing_redirects']=[]
for page, data in indices.items():
 for url in data.links:
  u=urlsplit(url)
  if u.scheme or u.netloc: continue
  dest=(page.parent/unquote(u.path)).resolve() if u.path else page
  if dest.is_dir(): dest=dest/'index.html'
  if not dest.is_file():
   report['missing_redirects'].append({'page':str(page.relative_to(site.resolve())),'url':url})
  elif u.fragment and dest in indices and unquote(u.fragment) not in indices[dest].ids:
   report['missing_fragments'].append({'page':str(page.relative_to(site.resolve())),'url':url})
(root/'reports').mkdir(exist_ok=True)
(root/'reports/link-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:len(v) if isinstance(v,list) else v for k,v in report.items()}))
assert not report['forbidden_urls'], 'Site URLs still depend on a host/root'
assert not report['forms'], 'Review remaining forms'

assert not report["missing_links"] and not report["missing_assets"], "Missing local targets"
assert not report["missing_fragments"] and not report["missing_redirects"], "Missing anchors or redirect targets"

assert not (site/"meet/sample").exists(), "Editing samples must not be published"
