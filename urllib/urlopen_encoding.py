import sys
from urllib.request import urlopen
f = urlopen('http://cafe984.daum.net/_c21_/cafesearch?grpid=mEr9&fldid=&pagenum=&listnum=20&item=subject&head=&query=%EB%8B%A4%EC%9D%B4%EC%86%8C&attachfile_yn=&media_info=&viewtype=all&searchPeriod=all&sorttype=0&nickname=')

# HTTP 헤더를 기반으로 인코딩 방식을 추출한다. [ Default : utf-8 ]
encoding = f.info().get_content_charset(failobj="utf-8")
text = f.read().decode(encoding)

print(text)
