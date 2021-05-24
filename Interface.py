import manga
import tkinter
from tkinter import filedialog
import os
root = tkinter.Tk()
root.withdraw()
def files():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='選擇資料夾儲存位置')
    if len(tempdir) > 0:
        print ("目前檔案位置: %s" % tempdir)
    return tempdir
files= files()
num=input()
manga.num(num,files)