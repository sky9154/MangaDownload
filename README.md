# 漫畫下載器
**利用 Python 網路爬蟲，爬取 [<font color="red">nhentai.net</font>](https://nhentai.net) 的漫畫，並且下載到指定資料夾**
深度使用 <font color="#333333">**nhentai**</font> 這個網站有數年之久，雖然與 E / Ex-hentai 兩者相較之下，資源沒那麼豐富，搜尋功能也不如其他兩個網站，唯一的優點就是閱讀起來方便非常多，在各種平台皆有可供閱讀的軟體，不過要保存漫畫，除了一張一張的慢慢下載，就只剩下使用 BitTorrent 來保存到本地端了，也就有了這個應用程式，來下載整個漫畫。
## 前置作業
### 1.安裝必要項目
先查看 `install.bat` 的內容，如果檔案內的 Python 第三方套件，你已經安裝過的話，可以把已安裝的套件移除
install.bat 內容：
```
pip install requests
pip install urllib3
pip install beautifulsoup4
pip install Eel
```
例如你已經安裝過 Eel 了，就可以把 `pip install Eel` 給移除掉在雙擊 `install.bat` ，即可安裝必要的項目

### 2.安裝漫畫下載器
從 [Github](https://github.com/sky9154/MangaDownload) 上進行手動下載，或是使用 git 下載完整程式碼：
```
git clone https://github.com/sky9154/MangaDownload.git
```
## 如何使用
### 1. 開啟程式：
使用 CMD 視窗輸入下列指令：
```
cd 程式所在的資料夾
python3 launcher.py
```
### 2-1. 輸入漫畫編號：
點擊 `Search` 後將會建立以編號命名的資料夾並將漫畫存入其中

![](https://i.imgur.com/Qfv5bPs.png)
### 2-2. 隨機下載漫畫：
點擊 `Random` 後將會隨機下載漫畫

![](https://i.imgur.com/usxvjMz.png)
## 完整程式執行過程
### 編號下載

![](https://i.imgur.com/tibhkGE.gif)
### 隨機下載

![](https://i.imgur.com/gBkqYQJ.gif)