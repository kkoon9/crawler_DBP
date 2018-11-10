# Library
 크롤링을 위해 사용 가능한 라이브러리를 소개한다.

## bs4
 - BeautiulSoup : 기억하기 쉬운 단순한 API가 특징이다.

 ~~~py
 # bs4 모듈에서 BeautifulSoup 클래스 읽기
 from bs4 import BeautifulSoup

 # BeautifulSoup()에는 파일 이름, URL 지정 불가
 # 그렇기 때문에 open() 을 사용한다.
 # BeautifulSoup()의 두 번째 매개변수에는 파서의 종류를 지정한다.
 with open('URL') as f:
     soup = Beautiful(f, 'html.parser')

# 태그 이름을 가진 속성을 추출 가능
soup.<태그이름>
# type()를 통해 요소도 알 수 있다.
type(soup.<태그이름>)

# select() 메서드로 CSS selector와 일치하는 요소를 추출 가능하다.
soup.select('tbody > tr > td.subject.searchpreview_subject')
 ~~~
 