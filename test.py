'''
Descripttion: 
version: 
Author: yangxi
Date: 2023-09-25 17:11:19
LastEditors: yangxi
LastEditTime: 2023-10-08 16:20:05
'''
from tkinter import *
root = Tk()
root.geometry("300x300") 
root.title("tkinter")  #设置标题
root.iconbitmap('bitbug_favicon.ico')  #设置图标，仅支持.ico文件
l = Label(root,width=20,height=3,text="1",fg="red",font=('楷体',10),bg="white")
l.pack()
l.config(text="策划")
img = PhotoImage(file='1.png')
Im = Label(root,image=img)
Im.pack()
root.update()  #一定要刷新界面，否则打印出的值是1
print("当前窗口的宽度为",root.winfo_width())
print("当前窗口的高度为",root.winfo_height())
root.mainloop()