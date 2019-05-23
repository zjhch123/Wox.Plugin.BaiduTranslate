import http.client
import json
import re
import urllib
import webbrowser

from wox import Wox

class HelloWorld(Wox):
    def bd_api(self, q):
        word = q.lower()
        url = "/sug?kw={}".format(urllib.parse.quote(word), safe=":/?=&")

        try:
            conn = http.client.HTTPSConnection("fanyi.baidu.com")
            conn.request("GET", url)
            res = conn.getresponse()
            if res.code == 200:
                return json.loads(res.read().decode("utf-8"))
        except Exception:
            pass
        finally:
            if conn:
                conn.close()

    def query(self, query):
        q = query.strip()

        if not q:
            return [{
                "Title": '请输入单词',
                "SubTitle": '',
                "IcoPath":"./Images/icon.png"
            }]

        results = []
        translatedResule = self.bd_api(q)
        data = translatedResule['data']

        if re.search('[\u4e00-\u9fa5]', q):
            lan = '#zh/en'
        else:
            lan = '#en/zh'

        for d in data:
            openURL = 'http://fanyi.baidu.com/%s/%s' % (lan, d['k'])
            results.append({
                "Title": d['v'],
                "SubTitle": d['k'],
                "IcoPath":"./Images/icon.png",
                'JsonRPCAction': {
                    'method': 'detail',
                    'parameters': [openURL]
                }
            })
        
        return results

    def detail(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    HelloWorld()