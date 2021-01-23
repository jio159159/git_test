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
print(Spam_Lookup)
from html_table_parser import parser_functions as parser
html_table = parser.make2d(Spam_Lookup)
#print(html_table)
import pandas as pd
df=pd.DataFrame(html_table[2:], columns=html_table[0])
#print(df.head())
print(df)
#c1 = soup.find_all("table",{"class": "CB_Table"})
#print(c1)
#print(soup.find_all("th"))
#print(soup.th)
