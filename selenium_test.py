import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Phon Number 입력
num = '15881688'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('/Users/Public/chromedriver_win32/chromedriver', options=options)
#driver = webdriver.Chrome('/Users/Public/chromedriver_win32/chromedriver')

URL = "http://www.missed-call.com/"
driver.implicitly_wait(3)
driver.get(URL)
driver.find_element_by_name('pnum').send_keys(num)
driver.find_element_by_xpath('//*[@id="submitButton"]').click()
a= driver.find_element_by_id('result_is_spam')
print(a)
#req = driver.page_source
time.sleep(3)
#soup = BeautifulSoup(req, 'html.parser')
#Spam_Lookup = soup.find_all('span',class_='spam_warning2')
#Spam_Lookup = soup.find("table", attrs={"class": "CB_Table"})
#print(Spam_Lookup)
#parser_function으로 텍스트만 불러오고 pandas로 데이터프레임 형태로 만듦
#from html_table_parser import parser_functions as parser
#import pandas as pd
#html_table = parser.make2d(Spam_Lookup)
#df=pd.DataFrame(html_table[2:], columns=html_table[0])
#print(df)
#driver.close()
