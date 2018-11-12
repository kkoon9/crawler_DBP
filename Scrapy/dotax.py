# -*- coding: utf-8 -*-

import scrapy

 

 

class DotaxSpider(scrapy.Spider):

    # Spider의 이름을 설정한다. Spider를 실행할 때 사용된다.

    name = "dotax"

    

    # 크롤링 대상 도메인 리스트를 지정

    allowed_domains = ["http://cafe984.daum.net/_c21_/home?grpid=mEr9"]

    

    # 속성에는 크롤링을 시작할 URL 목록을 리스트 또는 튜플 형식으로 지정한다.

    start_urls = ['http://cafe984.daum.net/_c21_/cafesearch?grpid=mEr9&fldid=&pagenum=&listnum=20&item=subject&head=&query=%EB%8B%A4%EC%9D%B4%EC%86%8C&attachfile_yn=&media_info=&viewtype=all&searchPeriod=all&sorttype=0&nickname=']

 

    # 추출한 웹 페이지 처리를 위한 콜백 함수

    def parse(self, response):

        # 매개변수로 CSS selector를 입력하면 SelectorList 객체를 반환하여 리스트로 만들어 반

        link = response.css('tbody >tr > td.subject.searchpreview_subject > a::attr("href")').extract()

        

        # '#'을 속성으로 하는 href 속성이 있으므로 filter()를 이용하여 제거해준다.

        link = filter(lambda x : x != "#", link)

 

        link = list(link)