import requests
import lxml.html

response = requests.get('http://cafe984.daum.net/_c21_/cafesearch?grpid=mEr9&fldid=&pagenum=&listnum=20&item=subject&head=&query=%EB%8B%A4%EC%9D%B4%EC%86%8C&attachfile_yn=&media_info=&viewtype=all&searchPeriod=all&sorttype=0&nickname=')
root = lxml.html.fromstring(response.content)

for a in root.cssselect('tbody > tr > td.subject.searchpreview_subject > a'):
    url = a.get('href')
    print(url)
    print('----')
