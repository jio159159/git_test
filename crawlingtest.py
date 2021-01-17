import requests
from bs4 import BeautifulSoup

def get_html(url): # requests묘듈 공식 홈페이지에 나와있는 내용 
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

URL = "http://www.missed-call.com/"
html = get_html(URL) # 함수 호출
soup = BeautifulSoup(html, 'html.parser')

#c1 = soup.find_all("table",{"class": "CB_Table"})
#print(c1)
#print(soup.find_all("th"))
#print(soup.th)
for x in range(0,1):
    print(soup.select(".CB_Table")[x].get_text()) # CB_Table 안에있는 내용들을 택스토로 출력한다.
