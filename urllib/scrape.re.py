import re
from html import unescape

with open('DOTAX_url_meta.html') as f:
    html = f.read()

# re.findall()을 사용해 다이소와 관련된 HTML을 추출한다.
for partial_html in re.findall(r'<td class="subject searchpreview_subject">.*?</td>', html, re.DOTALL):
    # 게시물의 url 추출
    url = re.search(r'<a href="/_c21_/(.*?)</a>', partial_html).group(1)
    print(url)
    print('---')
