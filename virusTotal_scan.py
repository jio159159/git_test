import requests

url = 'https://www.virustotal.com/vtapi/v2/url/scan'
params = {'apikey': '27628eca814cabdf7a5f2623028af4d67e7ae6977ead1dcae981044c64a64841', 'url':'https://m.blog.naver.com/carpediem-s/221720902886'}
res = requests.post(url, data=params)
#print(res.json())
from html_table_parser import parser_functions as parser
import pandas as pd
html_table = parser.make2d(res)
df=pd.DataFrame(html_table[2:], columns=html_table[0])
print(df)