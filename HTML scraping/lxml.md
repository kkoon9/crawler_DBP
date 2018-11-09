# Library
 크롤링을 위해 사용 가능한 라이브러리를 소개한다.

## lxml
 - libxml2와 libxslt를 사용한 C 확장 라이브러리
 - $ sudo apt-get install -y libxml2-dev libxslt-dev libpython3-dev zlib1g-dev
 - $ pip install lxml
 - $ pip install cssselect

 ### scrape_by_lxml.py
 - 다이소라는 키워드가 <b></b> [굵게] 태그에 싸여있어서 크롤링에 어려움을 겪고 있다. 해결방법을 찾아야 한다.
 