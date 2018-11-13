from selenium import webdriver

from bs4 import BeautifulSoup

"""

참고 사이트 : https://blog.naver.com/PostView.nhn?blogId=popqser2&logNo=221229125022&parentCategoryNo=&categoryNo=23&viewDate=&isShowPopularPosts=true&from=search 

"""

class DotaxCrawling():

    def __init__(self):

        self.id = 'ID' # cafe id

        self.pw = 'PW'   # cafe pw

        self.delay = 3         # implicily_wait()에 쓰이는 delay(초)

        self.keyword = "다이소" # 검색할 keyword

        # driver를 사용하기 위한 settings
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        return self.login()
 

    def login(self):



        driver.get('https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fcafe984.daum.net%2F_c21_%2Fhome%3Fgrpid%3DmEr9&category=cafe&t__nil_navi=login')

        

        driver.implicitly_wait(self.delay)

 

        driver.find_element_by_name('id').send_keys(self.id)

        driver.find_element_by_name('pw').send_keys(self.pw)

        driver.find_element_by_xpath('.//*[@id="loginBtn"]').click()

 

if __name__ == '__main__':

    DotaxCrawling().init()