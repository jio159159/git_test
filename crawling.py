from urllib import request
from bs4 import BeautifulSoup

# 네이버 사이트에 요청
source = request.urlopen("http://www.missed-call.com/")

#BeautifulSoup을 사용해 웹 페이지를 분석
soup = BeautifulSoup(source, "html.parser")

a = soup.select(" .new_search_box")
print(a)