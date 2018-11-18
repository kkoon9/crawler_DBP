class DotaxCrawling():

    keyword = ""
    maxPageNum = 1
    pageNum = 1
    searchCount = 1
    absoluteUrl = []
    text = []
    keyword = ""
    searchUrl = "http://cafe984.daum.net/_c21_/cafesearch?grpid=mEr9&fldid=&pagenum=" + str(pageNum) + "&listnum=20&item=subject&head=&query=" + keyword + "&attachfile_yn=&media_info=&viewtype=all&searchPeriod=all&sorttype=0&nickname="

    def __init__(self):
        # 변하지 않는 변수들은 init에 선언
        self.id = 'ID'  # cafe id

        self.pw = 'PW'  # cafe pw

        self.delay = 2  # time.sleep()에 쓰이는 delay(초)

        self.loginUrl = 'https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fcafe984.daum.net%2F_c21_%2Fhome%3Fgrpid%3DmEr9&category=cafe&t__nil_navi=login'