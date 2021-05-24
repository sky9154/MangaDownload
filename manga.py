import urllib.request as ur
import urllib
import requests
import os
import time
import random
from bs4 import BeautifulSoup as bs
def num(num,address):
    os.chdir(address)
    class nhview:
        def __init__(self):
            self.name = ""
            self.origin = ""

        def randombook(self):
            self.name = str(random.randint(1, 400000))

        def checklink(self):
            headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
            }
            self.origin = "https://nhentai.net/g/" + self.name + "/"      #轉換成網址
            resp = requests.get(self.origin, headers = headers)
            if resp.status_code == 200:
                print("號碼：" + self.name)
                print("連線成功")
                return True
            else:
                print("號碼：" + self.name)
                print("連線代碼：" + str(resp.status_code))
                print("連線錯誤，請重新輸入")
                return False

        def setlink(self):
            self.name = num

        def setsail(self):
            headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
            }
            for i in range(1,10000):
                url = self.origin + str(i)
                nowpath = os.path.abspath('./' + self.name)        #獲取當前路徑

                try:
                    req = ur.Request(url=url,headers=headers)
                    result = ur.urlopen(req).read().decode('utf-8')
                except urllib.error.URLError as e:
                    print(e.reason)
                    print("下載完成")
                    break
                else:
                    if not os.path.isdir(nowpath):
                        print("新增資料夾。")
                        os.mkdir(nowpath)
                    html = bs(result)
                    img = html.select('section#image-container img')[0]
                    imgurl = img.get('src')
                    ur.urlretrieve(imgurl, os.path.join(nowpath, str(i) + '.jpg'), reporthook=None, data=None)
                    print("已增加第" + str(i) + "頁。")
                    time.sleep(0.5)

        def start(self):
            self.setlink()

            while True:
                if self.checklink() == True:
                    break
            else:
                    self.setlink()
        
            self.setsail()

    nh = nhview()
    nh.start()