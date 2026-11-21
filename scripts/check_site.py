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
expected=sum(1 for p in root.rglob('*.html') if not any(part in ('_site', '_layouts', 'vendor', '.jekyll-cache') for part in p.relative_to(root).parts)) + int((root/'index.md').exists())
assert report['pages']==expected,(report['pages'],expected)
(root/'reports').mkdir(exist_ok=True)
(root/'reports/link-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:len(v) if isinstance(v,list) else v for k,v in report.items()}))
assert not report['forbidden_urls'], 'Site URLs still depend on a host/root'
assert not report['forms'], 'Review remaining forms'
