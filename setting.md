# Ubuntu 16.04 초기 환경설정

## vim 설치
- 기존의 vi 에디터의 상위 호환인 vim 에디터를 사용한다.
> 1. sudo apt-get update
> 2. sudo apt-get install vim
- 출처: http://jerrystyle.tistory.com/3

### apt-get update 중 error
> 1. sub-process returned an error code 발생하면
> 2. sudo apt-get remove libappstream3를 하면 해결된다.
 
## 한글 설치
- 크롤링을 위해서는 한글 설치는 필수사항이다.
> 1. sudo apt-get install fcitx-hangul
> 2. System Settings - Language Support - 언어팩 팝업창이 뜨면 '설치' 선택 - Keybord input method system 항목을 fcitx로 변경 - reboot
> 3. System Settings - Keyboard - Shortcuts 탭 Typing - 모든 항목 Disabled - Compose Key 항목을 Right Alt로 변경 - Switch to next source를 Alt+ 한/영키 누르기
> 4. 오른쪽 상단 상태바에서 fcitx 아이콘 선택 - Configure Current Input Method에서 + 버튼을 눌러 Hangul 항목 추가 - Global Config 탭에서 Trigger Input Method 항목을 한/영 키로 설정
- 출처 : http://snowdeer.github.io/linux/2018/01/21/ubuntu-16p04-install-korean-keyboard/

## 파이썬 설치
- 출처 : https://askubuntu.com/questions/849190/python-3-4-on-ubuntu-16-04/849217

## 크롬 설치
- 출처 : http://snowdeer.github.io/linux/2018/02/02/ubuntu-16p04-install-chrome/

### dpkg error 해결 방법
> 1. sudo dpkg --configure -a
> 2. sudo apt-get -f install
 
