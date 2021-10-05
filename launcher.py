import manga    #漫畫下載模組
import eel    #視窗模組
import tkinter as tk    #檔案選擇視窗
from tkinter import filedialog
import os

def files():    #檔案選擇視窗
    address = tk.Tk()
    address.withdraw()
    curdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=address, initialdir=curdir, title="選擇資料夾儲存位置")
    return tempdir

@eel.expose
def download(number):   #漫畫下載
    if number.isdigit():
        tempdir = files()
        if tempdir:
            manga.num(number, tempdir)
        else:
            print("請選擇需儲存的資料夾")
    else:
        print("請輸入正確的編號")
eel.init("gui")    # 網頁的資料夾
eel.start("index.html", size = (450, 250), port = 8763)    # 視窗大小，port 參數