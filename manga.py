import urllib.request as ur
import urllib
import requests
import os
import time
import random
from bs4 import BeautifulSoup as bs


def num(num):
    class nhview:
        def __init__(self):
            self.name = ""
            self.origin = ""

        def random(self):
            self.name = str(random.randint(1, 400000))

        def sao(self):
            self.name = str(345545)

        def checklink(self):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
            }
    # 將輸入的號碼轉換成網址
            self.origin = "https://nhentai.net/g/" + self.name + "/"
            resp = requests.get(self.origin, headers=headers)
            if resp.status_code == 200:
                print("號碼：" + self.name)
                print("連線成功")
                return True
            else:
                print("號碼：" + self.name)
                print("連線代碼：" + str(resp.status_code))
                print("連線錯誤，請重新輸入")
                return False
    # 輸入號碼

        def setlink(self):
            while True:
                self.name = num
                if len(self.name) <= 6:
                    break
                else:
                    print("輸入錯誤")

            if self.name == "?":
                self.random()
            if self.name == "c8763":
                self.sao()

        def setsail(self):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
            }
            for i in range(1, 2):
                url = self.origin + str(i)
    # 新增資料夾
                nowpath = os.path.abspath('./demo')

                try:
                    req = ur.Request(url=url, headers=headers)
                    result = ur.urlopen(req).read().decode('utf-8')
                except urllib.error.URLError as e:
                    print(e.reason)
                    print("下載完成")
                    break
                else:
                    if not os.path.isdir(nowpath):
                        print("新增資料夾："+self.name)
                        os.mkdir(nowpath)
                    html = bs(result)
                    img = html.select('section#image-container img')[0]
                    imgurl = img.get('src')
                    ur.urlretrieve(imgurl, os.path.join(
                        nowpath,'MangaIMG.jpg'), reporthook=None, data=None)

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