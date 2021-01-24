import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def get_html(url): # requests모듈 공식 홈페이지에 나와있는 내용 
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

URL = "http://www.missed-call.com/"
html = get_html(URL) 
soup = BeautifulSoup(html, 'html.parser')
Spam_Lookup = soup.find("table", attrs={"class": "CB_Table"})

#------------------------
number = '010-4919-2952'
session=requests.session()
res=session.get(URL, params = number)
res.raise_for_status()
print(res.headers)
#------------------------

#-------------------------------------------------------
#parser_function으로 텍스트만 불러오고 pandas로 데이터프레임 형태로 만듦
from html_table_parser import parser_functions as parser
import pandas as pd
html_table = parser.make2d(Spam_Lookup)
df=pd.DataFrame(html_table[2:], columns=html_table[0])
print(df)

