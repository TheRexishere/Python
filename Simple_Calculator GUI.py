import tkinter as tk
from tkinter import *

b=str()

rt=Tk()

rt.title("Simple Calculator")

rt.geometry("300x150")

enter= StringVar()

entry= Entry(rt,width='5',textvariable=enter ,font=('Courier',25))
entry.place(x=100,y=10)

def put_data(a):
    global b
    b+=a
    enter.set(b)
    
def get_sol():
    enter.set(eval(b))
    
def clear():
    entry.delete(0,5)
    global b
    b=''
    
but1= Button(rt,text="1",fg='red',width='10',height='1',command=lambda:put_data('1'))
but1.place(x=40,y=60)

but2= Button(rt,text="2",fg='red',width='10',height='1',command=lambda:put_data('2'))
but2.place(x=40,y=85)

but3= Button(rt,text="3",fg='red',width='10',height='1',command=lambda:put_data('3'))
but3.place(x=40,y=110)

butx= Button(rt,text="*",fg='red',width='10',height='1',command=lambda:put_data('*'))
butx.place(x=190,y=110)

butx= Button(rt,text="=",fg='red',width='10',height='1',command=lambda:get_sol())
butx.place(x=190,y=85)

butx= Button(rt,text="AC",fg='red',width='10',height='1',command=lambda:clear())
butx.place(x=190,y=60)


rt.mainloop()