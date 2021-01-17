import requests

url = 'https://www.virustotal.com/vtapi/v2/url/scan'
params = {'apikey': '27628eca814cabdf7a5f2623028af4d67e7ae6977ead1dcae981044c64a64841', 'url':'https://m.blog.naver.com/carpediem-s/221720902886'}
response = requests.post(url, data=params)
print(response.json())
