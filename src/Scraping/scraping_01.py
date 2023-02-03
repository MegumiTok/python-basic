import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        # urlopen関数はウェブサイトヘのリクエストを行います。
        # 実行すると、 Responseオブジェクトが返され、この中にHTMLと、追加情報が格納されています。 
        r = urllib.request.urlopen(self.site)
        # response.readメソッドを呼ぶと、HTMLデータがResponseオブジェクトから返されます。
        # URLのウエブサイトから取得し たすべてのHTMLデータが、html変数に入っています。
        html = r.read()

        # 第二引数でHTMLをパースしてほしいことを伝えている
        sp = BeautifulSoup(html, "html.parser")
        
        # BeautifulSoupオブジェクトは、HTMLをパースする手間のかかる仕事をすべてやってくれます。
        # find_allメソッドはイテラブルなオブジェクトで、個々の要素はtagオブジェクト
        # このforループを回すたびに、変数tagに新しいTag のオブジェクトが代入されます
        
        # for tag in sp.find_all("a"):  #<a></a>タグをすべて集めて返す
        #     print(tag.get('href'))
        
                
news ="http://abehiroshi.la.coocan.jp/"
Scraper(news).scrape()
            