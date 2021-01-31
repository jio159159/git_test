import requests
import time

# 바이러스토탈 API Key
my_apikey = '27628eca814cabdf7a5f2623028af4d67e7ae6977ead1dcae981044c64a64841'
# 점검 대상 URL
my_url = 'https://m.blog.naver.com/carpediem-s/221720902886'

# 바이러스토탈 URL 스캔 주소
url_scan = 'https://www.virustotal.com/vtapi/v2/url/scan'
scan_params = {'apikey': my_apikey, 'url': my_url}
scan_response = requests.post(url_scan, data=scan_params)

# URL 스캔 시작
print('Virustotal URL SCAN START (60 Seconds Later) : ', my_url, '\n')

# URL 스캔 후 1분 대기
time.sleep(60)

# 바이러스토탈 URL 점검 결과 주소
url_report = 'https://www.virustotal.com/vtapi/v2/url/report'
report_params = {'apikey': my_apikey, 'resource': my_url}
report_response = requests.get(url_report, params=report_params)

# 점검 결과 데이터 추출
report = report_response.json()
report_scan_date = report.get('scan_date')
report_scan_result = report.get('scans')
report_scan_venders = list(report['scans'].keys())

num = 1
count = 0       #clean site 개수
count2 = 0      #unrated site 개수
# URL 점검 결과 리포트 조회하기
# 점검 완료 메시지
print(report.get('verbose_msg'), '\n')
time.sleep(1)

# 스캔 결과 데이터만 보기
print('Scan Date (UTC) : ', report_scan_date)

for vender in report_scan_venders:
    outputs = report_scan_result[vender]
    outputs_keys = report_scan_result[vender].get('result')
    print('No', num, 'Vender Name :', vender, ', Scan Result :', outputs_keys)
    num = num + 1
    if outputs_keys == 'clean site' :       #clean site 개수
        count = count + 1
    if outputs_keys == 'unrated site' :     #unrated site 개수
        count2 = count2 + 1
       
print('clean site = ' ,+count, end=' ,')
print(' unrated site = ' ,+count2)