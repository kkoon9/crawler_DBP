# -*- coding: utf-8 -*-

# InitSpider : parse를 오버라이드해서 parse 실행전에 다른 작업들을 하게 해준다.

import scrapy

from scrapy.spiders.init import InitSpider 

from scrapy.http import Request, FormRequest

from scrapy.spiders import Rule, BaseSpider

# LinkExtractor is faster (it's lxml-backed) than SgmLinkExtractor and Python3 compatible.

from scrapy.linkextractors import LinkExtractor

 

"""

참고 사이트 : vnthf.logdown.com/posts/2016/03/18/650623

크롤링 시작되면 initRequest 메소드가 제일 먼저 불린다. 여기서 로그인 할 페이지와 실행될 메소드를 지정해준다.

login 메소드에서는 FormRequest를 이용해서 해당 페이지에서 submit요청을 보내도록 한다.

요청이 끝나면 check_login_response가 불리는데 여기서 로그인이 제대로 되었는지 확인하면 된다. [response 이용]

로그인이 제대로 되었다면 initialized에서 초기화하고 parse이 불릴 것이다.

"""

 

class DotaxSpider(InitSpider):

    # Spider의 이름을 설정한다. Spider를 실행할 때 사용된다.

    name = "dotax"

    # 크롤링 대상 도메인 리스트를 지정

    allowed_domains = ["cafe984.daum.net/_c21_/home?grpid=mEr9"]

    # 로그인 url

    login_page ="https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fcafe984.daum.net%2F_c21_%2Fhome%3Fgrpid%3DmEr9&category=cafe&t__nil_navi=login"

    

    # 속성에는 크롤링을 시작할 URL 목록을 리스트 또는 튜플 형식으로 지정한다.

    start_urls = ['http://cafe984.daum.net/_c21_/cafesearch?grpid=mEr9&fldid=&pagenum=&listnum=20&item=subject&head=&query=한국사람&attachfile_yn=&media_info=&viewtype=all&searchPeriod=all&sorttype=0&nickname=']

 

    rules = (

        Rule(LinkExtractor(allow=()),

            callback = 'parse', follow=True),

    )

 

    # 크롤링 시작하게 되면 처음으로 불리는 메소드

    def init_request(self):

        return Request(url = self.login_page, callback=self.login)

 

    def login(self, response):

        print("===================[login]==================")

        obj = {

            'id': 'ID'

            ,'pw ': 'PW'

        }

        return FormRequest.from_response(response,

            formdata=obj,

            callback=self.check_login_response)

 

    def check_login_response(self, response):

        print("===================[check_login_response]==================")

        print("current URL : "+ response.url)

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        return self.initialized();

 

    def initialized(self):

        print("===================[initialized]==================")

        return Request(url=self.start_urls,callback=self.parse)

 

    # 추출한 웹 페이지 처리를 위한 콜백 함수

    def parse(self, response):

        print("===================[parse]==================")

        # 매개변수로 CSS selector를 입력하면 SelectorList 객체를 반환하여 리스트로 만들어 반

        link = response.css('tbody >tr > td.subject.searchpreview_subject > a::attr("href")').extract()

        

        # '#'을 속성으로 하는 href 속성이 있으므로 filter()를 이용하여 제거해준다.

        link = filter(lambda x : x != "#", link)

 

        for url in link:

            yield scrapy.Request(response.urljoin(url), self.parse_topics)

 

 

    def parse_topics(self, response):

        text = response.css('tbody > tr > td > p::text').extract()

        text = list(text)

        print(text)
        