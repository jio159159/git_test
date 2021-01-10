from bs4 import BeautifulSoup as bs

import requests



MEMBER_DATA = {

    'pnum': '01049192952',

  
}



# 하나의 세션(Session) 객체를 생성해 일시적으로 유지합니다.

with requests.Session() as s:

    # 로그인 페이지로의 POST 요청(Request) 객체를 생성합니다.

    request = s.post('http://www.missed-call.com/', data=MEMBER_DATA)


#print(request.text)
