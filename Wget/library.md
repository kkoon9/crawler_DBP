# Library
 크롤링을 위해 사용 가능한 라이브러리를 소개한다.

## Wget
- HTTP or FTP 통신을 사용해 Server에서 file이나 Content를 다운로드할 때 사용하는 소프트웨어(다운로더) 
- Wget의 옵션

옵션      | 설명
----------|--------------
-O <file>  | file에 저장한다.
-c         | 이전 상태에서 계속 이어서 파일을 다운로드
-r         | 링크를 재귀적으로 돌면서 다운로드
-l depth   | 재귀적으로 다운로드할 때 depth 지정 
-w seconds | 다운로드 간격을 seconds 초로 지정
-np        | 재귀적으로 다운로드할 때 부모 디렉터리는 크롤링 x
-I <list>  | 재귀적으로 다운로드할 때 list에 포함돼 있는 디렉터리만 돈다.
-N         | 파일이 변경되었을 때만 다운로드한다.

### 다음카페 DOTAX의 홈페이지를 Wget를 이용하여 크롤링해보았다.
'$ wget -r -np -w 1 -l 1 --restrict-file-names=nocontrol cafe984.daum.net/_c21_/home?grpid=mEr9'
- tree를 통해 결과물을 확인할 수 있다.
'tree cafe984.daum.net/'
![tree 결과](/tree결과.JPG)
