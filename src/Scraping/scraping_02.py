# requestsでHTMLをダウンロードしてBeautiful Soup で解析して任意の情報を取り出せる
import requests
from bs4 import BeautifulSoup
  
URL = "http://abehiroshi.la.coocan.jp/"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify())