import requests

url = 'https://www.virustotal.com/vtapi/v2/url/report'
params = {'apikey': '27628eca814cabdf7a5f2623028af4d67e7ae6977ead1dcae981044c64a64841', 'resource':'cc023ce87637a887d689757ed1c28f01b8c0124af524c6183d25cf16f1031b32-1610886756'}
response = requests.get(url, params=params)
print(response.json())