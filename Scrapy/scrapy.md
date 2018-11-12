# Scrapy
 - 효율적인 크롤링/스크레이핑을 할 수 있다.
 - scrapy는 lxml을 기반으로 만들어졌다.

## Spider
- scrapy를 사용하면 Spider라는 이름의 클래스를 만들게 된다.
- Spider 클래스에 크롤링 처리와 스크레이핑 처리를 작성한다.
- 명령어를 실행할 때에는 scrapy.cfg가 있는 디렉터리에서 한다.
~~~py
$ scrapy startproject [Name]
$ tree [Name]
Name
    Name
        __init.py      # Scrapy 프로젝트는 파이썬 모듈
        items.py       # Item 정의 파일
        pipelines.py
        settings.py
        spiders
            __init.py
    scrapy.cfg
~~~

### items.py
- Spider가 추출할 데이터를 저장할 객체이다.
- 여러 종류의 데이터를 추출했을 때 클래스를 기반으로 객체 판별할 수 있다.
- 미리 정의한 필드에 데이터를 입력하므로, 필드 이름을 잘못 적는 실수를 줄일 수 있다.
- 메서드를 정의할 수 있다.

### Spider 만들기
- <b>scrapy genspider</b> 명령어를 사용하면 템플릿을 기반으로 Spider 생성 가능하다.
- 첫 번째 매개변수 : Spider의 이름
- 두 번째 매개변수 : 도메인 이름을 지정한다.
