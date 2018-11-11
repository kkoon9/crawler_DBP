import requests
import lxml.html

def main():
    """
    크롤러의 메인 처리
    """
    # 여러 페이지에서 크롤링할 것이므로 Session을 사용한다.
    session = requests.Session()

    # scrape_list_page() : 제너레이터를 추출
    response = session.get('http://cafe984.daum.net/_c21_/cafesearch?grpid=mEr9&fldid=&pagenum=&listnum=20&item=subject&head=&query=%EB%8B%A4%EC%9D%B4%EC%86%8C&attachfile_yn=&media_info=&viewtype=all&searchPeriod=all&sorttype=0&nickname=')
    urls = scrape_list_page(response)
    for url in urls:
        print(url)
        print('----')
    
def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('tbody > tr > td.subject.searchpreview_subject > a'):
        if a == '#':
            continue
        url = a.get('href')
        # yield 구문으로 제너레이터의 요소 반환
        yield url

<<<<<<< HEAD
if __name__ == '__main__':
    main()
=======
for a in root.cssselect('tbody > tr > td.subject.searchpreview_subject > a'):
    if a == '#':
    continue
    url = a.get('href')
    print(url)
    print('----')
>>>>>>> 7a02f7694b9283e8070d7f55c2fd15bd5bf07989
