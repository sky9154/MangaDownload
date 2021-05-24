#-----------------------模組-----------------------

import manga                              #漫畫下載模組
from tkinter import filedialog     #檔案選擇視窗
import tkinter as tk                    #視窗模組

#-----------------------副程式---------------------

def files():    #檔案選擇視窗
    address=tk.Tk()
    address.withdraw()
    curdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=address, initialdir=curdir, title='選擇資料夾儲存位置')
    if len(tempdir) > 0:
        print ("目前檔案位置: %s" % tempdir)
    return tempdir

def output():   #漫畫下載
    manga.num(e.get(),files())

#-----------------------視窗參數-------------------

window = tk.Tk()
window.title('漫畫下載器')  #標題
window.configure(background='black') #背景顏色
window.resizable(0,0)   #固定大小
window.geometry("+500+100")    #開啟座標

#-----------------------視窗元件-------------------

label = tk.Label(window, text='漫畫編號：')
label.configure(font=("Arial"))
e = tk.Entry(window,font="Arial",bd=1)
label.pack(side=tk.LEFT)
e.pack(side=tk.LEFT)
tk.Button(window,text='確定',command=output).pack(side=tk.LEFT)

#-----------------------啟動視窗-------------------

window.mainloop()