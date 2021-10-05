from tkinter import *
from tkinter import font
import os, time

win = Tk()
win.minsize(200, 40)
win.maxsize(200, 40)
win.attributes('-topmost', 1)

font = font.Font(family="DisposableDroid BB", size=30)

def start_py():
	os.system("python ./main.py")
	return

btn = Button(win, text='START', command=start_py)
btn.config(width=100, font=font, relief=FLAT, activebackground='#f02468', activeforeground='white', bg='#3df2a4', fg='#323232')
btn.pack()

win.mainloop()