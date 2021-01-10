from urllib import request      #URL을 읽어오는 모듈
from bs4 import BeautifulSoup   #HTML 과 XML 파일로부터 데이터 수집하는 라이브러리  



# 네이버 사이트에 요청
source = request.urlopen("http://www.missed-call.com/")

#BeautifulSoup을 사용해 웹 페이지를 분석
soup =  BeautifulSoup(source, "html.parser")

#print(soup.text) #전체내용 텍스트로 나타낸것

#a = soup.select(" .new_search_box")

#print(a)

#b = soup.find_all("tr")
#print(b)
#c = soup.find("table",{"class": "CB_Table"}).find_all("tr")
c1 = soup.find("table",{"class": "CB_Table"})
print(c1)
#result = soup.findAll('input',{"name": "pnum"})

#print(result[0].get('value'))


