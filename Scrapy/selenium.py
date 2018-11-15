from selenium import webdriver

from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait

import time

"""
참고 사이트 : https://blog.naver.com/PostView.nhn?blogId=popqser2&logNo=221229125022&parentCategoryNo=&categoryNo=23&viewDate=&isShowPopularPosts=true&from=search 
"""


# webdriver를 사용하기 위한 settings

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-infobars")


class DotaxCrawling():

    def __init__(self):
        self.id = 'ID'  # cafe id

        self.pw = 'PW'  # cafe pw

        self.delay = 3  # implicitly_wait()에 쓰이는 delay(초)

        self.driver = webdriver.Chrome('C:\chromedriver')

        self.keyword = "다이소"  # 검색할 keyword

        self.searchUrl = "http://cafe984.daum.net/_c21_/cafesearch?grpid=mEr9&fldid=&pagenum=&listnum=20&item=subject&head=&query=" + self.keyword + "&attachfile_yn=&media_info=&viewtype=all&searchPeriod=all&sorttype=0&nickname="

        self.loginUrl = 'https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fcafe984.daum.net%2F_c21_%2Fhome%3Fgrpid%3DmEr9&category=cafe&t__nil_navi=login'

    def login(self):
        print("=============login start===========")

        self.driver.get(self.loginUrl)
        time.sleep(self.delay) # delay 초만큼 대기

        self.driver.find_element_by_id('id').send_keys(self.id)

        self.driver.find_element_by_id('inputPwd').send_keys(self.pw)

        self.driver.find_element_by_id('inputPwd').submit()

        time.sleep(self.delay)
        return self.search()

    def search(self):
        print("=============search start===========")
        self.driver.get(self.searchUrl)
        time.sleep(self.delay)

        html = self.driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        print("=============search finish===========")

if __name__ == '__main__':
    DotaxCrawling().login()