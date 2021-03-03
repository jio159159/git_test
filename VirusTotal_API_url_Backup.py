import requests
import time

# 바이러스토탈 API Key
my_apikey = '27628eca814cabdf7a5f2623028af4d67e7ae6977ead1dcae981044c64a64841'
# 점검 대상 URL
#my_url = 'http://27.208.8.213:36612/Mozi.m'
my_url = input()
# 바이러스토탈 URL 스캔 주소
url_scan = 'https://www.virustotal.com/vtapi/v2/url/scan'
scan_params = {'apikey': my_apikey, 'url': my_url}
scan_response = requests.post(url_scan, data=scan_params)

# URL 스캔 시작
print('Virustotal URL SCAN START : ', my_url, '\n')

# URL 스캔 후 1분 대기
time.sleep(0.1)

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
count = 0       
count2 = 0   
count3 = 0
count4 = 0  

# 스캔 결과 데이터만 보기
print('Scan Date (UTC) : ', report_scan_date)
print('---------------------------------------')

for vender in report_scan_venders:
    outputs = report_scan_result[vender]
    outputs_keys = report_scan_result[vender].get('result')
    #print('No', num, 'Vender Name :', vender, ', Scan Result :', outputs_keys)
    #num = num + 1
    if outputs_keys == 'clean site' :       #clean site 개수
        count = count + 1
    if outputs_keys == 'unrated site' :     #unrated site 개수
        count2 = count2 + 1
    if outputs_keys == 'malicious site' :
        count3 = count3 + 1
    if outputs_keys == 'malware site' :
        count4 = count4 + 1

# clean site 총개수와 unrated site 총개수 출력
print('clean site = ' ,+count, end=' ,')
print(' unrated site = ' ,+count2)
print('malicious site =' ,+count3, end=' ,')
print(' malware site =' ,+count4)

# malicious site 나 malware site가 하나라도 존재할경우 악성URL 그 외 정상URL
if count3 > 0 or count4 > 0:
    print('악성URL')
else :
    print('정상URL')