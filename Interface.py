import manga
from tkinter import filedialog
import os
import tkinter as tk
num=0
def files():
    address=tk.Tk()
    address.withdraw()
    curdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=address, initialdir=curdir, title='選擇資料夾儲存位置')
    if len(tempdir) > 0:
        print ("目前檔案位置: %s" % tempdir)
    return tempdir
def output():
    manga.num(e.get(),files())
window = tk.Tk()
window.title('漫畫下載器')
window.configure(background='black')
height_label = tk.Label(window, text='漫畫號碼：').pack(side=tk.LEFT)
e = tk.Entry(window)
e.pack(side=tk.LEFT)
tk.Button(window, text='確定',command=output).pack(side=tk.LEFT)
window.mainloop()