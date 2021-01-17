import requests
from bs4 import BeautifulSoup

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

URL = "http://www.missed-call.com/"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')
a = soup.select(".CB_Table")

for b in a:
    print(b.select_one(".th").get_text()
          +". "
          + b.select_one(".td").get_text())
#c1 = soup.find_all("table",{"class": "CB_Table"})
#print(c1)
#print(soup.find_all("th"))
#print(soup.th)
#for x in range(0,1):
#    print(soup.select(".CB_Table")[x].get_text())
