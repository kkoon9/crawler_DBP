# Library
 크롤링을 위해 사용 가능한 라이브러리를 소개한다.

 ## requests
 - 인간을 위한 HTTP라는 캐치프레이즈를 가지고 있다.
 - HTTP 헤더 추가 혹은 Basic 인증 등을 쉽게 할 수 있는 인터페이스를 제공한다.

 ~~~py
 import requests # 라이브러리를 읽어 들인다.
 r = requests.get('url') # get() 함수로 웹 페이지를 추출
 type(r) # get() 함수의 반환값은 Response 자료형
 r.status_code # status_code 속성으로 HTTP 상태 코드를 확인
 r.headers['content-type'] # headers 속성으로 HTTP 헤더를 딕셔너리로 추출
 r.encoding # encoding 속성으로 HTTP 헤더를 기반으로 인코딩을 추출
 r.text # text 속성으로 str 자료형으로 디코딩된 응답 본문을 추출
 
 # 요청에 추가할 HTTP 헤더는 키워드 매개변수 headers에 딕셔너리로 지정
 r = requests.get('url', headers={'user-agent' : '~~~'})
 # Basic 인증은 키워드 매개변수 auth로 지정
 r = requests.get('url', auth=('ID','PW'))
 ~~~

 - 응답 본문이 gzip 형식 또는 Deflate 형식으로 압축되어 있어도 자동으로 해석해준다.

 - json() 메서드가 있어서 JSON 형식의 응답을 디코더해서 dict 또는 list를 추출할 수 있다.

 - 여러 개의 페이지를 연속으로 크롤링할 때에는 Session 객체를 사용하면 효과적이다.
