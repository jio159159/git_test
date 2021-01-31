from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출

from bs4 import BeautifulSoup
import time
import pandas as pd

# url
URL = "http://www.missed-call.com/"

# Phon Number 입력
num = '02-2138-0619'
#옵션 설정
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
options.add_argument('disable-gpu')    # GPU 사용 안함
options.add_argument('lang=ko_KR')    # 언어 설정
driver = webdriver.Chrome('/Users/Public/chromedriver_win32/chromedriver', options=options)

driver.get(URL)


driver.find_element_by_name('pnum').send_keys(num)
driver.find_element_by_xpath('//*[@id="submitButton"]').click()
time.sleep(3)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
#Spam_Lookup = soup.find("table", attrs={"class": "CB_Table"})
Spam_Lookup = soup.find('span', id='result_is_spam')
print(Spam_Lookup.text)
#trs = Spam_Lookup.find_all('tr')
#for x in enumerate(trs):
#    tds = x.find.all('td').text

#print(tds)


