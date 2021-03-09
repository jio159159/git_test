from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from bs4 import BeautifulSoup
import time

def missed_call(Pn):
    # 스팸 번호 스캔할 주소
    URL = "http://www.missed-call.com/"

    ######옵션 설정######
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    options.add_argument('disable-gpu')    # GPU 사용 안함
    options.add_argument('lang=ko_KR')    # 언어 설정
    driver = webdriver.Chrome('/Users/Public/chromedriver_win32/chromedriver', options=options) # chromedriver경로 자기 pc에 맞게끔 바꿔주셈
    ####################

    driver.get(URL)
    driver.find_element_by_name('pnum').send_keys(Pn)     # 번호 입력 하는 단계
    driver.find_element_by_xpath('//*[@id="submitButton"]').click() # 입력한 번호 검색 단계
    
    # 번호 검색 후 잠시 대기
    time.sleep(0.1)
    req = driver.page_source
    
    # BeautifulSoup을 사용해 웹 페이지 분석
    soup = BeautifulSoup(req, 'html.parser')
    
    # span이라는 class의 id 내용을 Spam_Lookup에 저장
    Spam_Lookup = soup.find('span', id='result_is_spam')
    
    # Spam_Lookup text로 출력하는 내용을 Spam_Level에 저장
    Spam_Level = Spam_Lookup.text
    
    # Spam__Level에서 숫자만 출력해서 str을 int로 바꿔서 Spam__Number로 저장
    Spam_Number = int(Spam_Level[-2:-1])
    
    # 0단계에서 2단계까지는 정상 3단계 이후로는 스팸번호로 저장
    if Spam_Number < 3 :
        result = 0  #정상
    else :
        result = 1  #악성
    return result
