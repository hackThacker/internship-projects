import re
import quopri

with open(r"\Day-2\email.txt", "rb") as f:
    raw = f.read()

# Decode quoted-printable (turns =3D into =)
text = quopri.decodestring(raw).decode("utf-8", errors="ignore")

# 1. Extract http/https links
pattern_urls = r'\bhttps?://[^\s\'"<>]+'
urls = re.findall(pattern_urls, text)

# 2. Extract <a href=...>
pattern_href = r'<a\s+[^>]*href=["\']?([^"\'\s>]+)'
hrefs = re.findall(pattern_href, text, flags=re.IGNORECASE)

# Combine + clean
all_links = urls + hrefs
cleaned = [u.rstrip(').,"\'>') for u in all_links]

for u in sorted(set(cleaned)):
    print(u)
