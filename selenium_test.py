import requests
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/Public/chromedriver_win32/chromedriver')



URL = "http://www.missed-call.com/"
driver.implicitly_wait(3)
driver.get(URL)
driver.find_element_by_name('pnum').send_keys('01049192952')
driver.find_element_by_xpath('//*[@id="submitButton"]').click()
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
Spam_Lookup = soup.find("table", attrs={"class": "CB_Table"})
print(Spam_Lookup)


from html_table_parser import parser_functions as parser
import pandas as pd
html_table = parser.make2d(Spam_Lookup)
df=pd.DataFrame(html_table[2:], columns=html_table[0])
#print(df)

