# XPath(XML Path Language)
- XML의 특정 요소를 지정할 때 사용하는 언어
- ex) //body/h1 라고 지정하면 body 요소의 직접적인 자식 중에 h1 태그를 선택

# CSS 선택자
 - CSS로 요소를 디자인할 때 사용하는 표기 방법
 - ex) body > h1 라고 표기하면 body 요소의 직접적인 자식 중에 h1 태그를 선택

 # XPath와 CSS선택자 비교

대상 요소         | XPath| CSS선택자
------|---------|----------
title 요소 | //title | title
body 요소의 후손 중 h1 요소 | //body//h1 | body h1
body 요소의 자식 중 h1 요소 | //body/h1  | body > h1
body 요소 내부의 모든 자식 요소 | //body/* | body > *

# 라이브러리의 XPath와 CSS 선택자 지원 상태

라이브러리    | 종류  | XPath | CSS 선택자
-----------------| ------------| ----|-----
ElementTree  | 표준 라이브러리 | △(XPath 1.0의 서브셋) | X
lmxl + cssselect | 서드파티 | O | O
Beautiful Soup | 서드파티 | X | △
pyquery | 서드파티 | X | O

## Tip
- 웹 브라우저에서 XPath와 CSS 선택자를 쉽게 추출 가능
- 마우스 오른쪽 클릭 - 컨텍스트 메뉴에서 [검사] - [Copy] - [Copy Xpath] or [Copy Selector]
