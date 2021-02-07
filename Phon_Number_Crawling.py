from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from bs4 import BeautifulSoup
import time

# 스팸 번호 스캔 주소
URL = "http://www.missed-call.com/"

# Phon Number 입력
Pn = '01049192952'
######옵션 설정######
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
options.add_argument('disable-gpu')    # GPU 사용 안함
options.add_argument('lang=ko_KR')    # 언어 설정
driver = webdriver.Chrome('/Users/Public/chromedriver_win32/chromedriver', options=options)
####################

driver.get(URL)
driver.find_element_by_name('pnum').send_keys(Pn)     # 번호 입력
driver.find_element_by_xpath('//*[@id="submitButton"]').click() # 입력한 번호 검색
# 폰 번호 스캔 후 3초간 대기
time.sleep(3)

req = driver.page_source
# BeautifulSoup을 사용해 웹 페이지 분석
soup = BeautifulSoup(req, 'html.parser')
# span이라는 class의 id 내용을 Spam_Lookup에 저장
Spam_Lookup = soup.find('span', id='result_is_spam')
# Spam_Lookup text로 출력하는 내용을 Spam_Level에 저장
Spam_Level = Spam_Lookup.text

# 전체 출력
#print(Spam_Level)

# 레벨만 출력
print(Spam_Level[-7: ])
