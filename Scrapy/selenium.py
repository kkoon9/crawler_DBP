from selenium import webdriver

from bs4 import BeautifulSoup
'''
 chrome is being controlled by automated test software 오류
 오류 해결을 위한 코드 8~12줄
'''
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://cafe984.daum.net/_c21_/home?grpid=mEr9')

delay = 1

driver.implicitly_wait(delay)

 

driver.find_element_by_xpath('//*[@id="loginout"]').click()