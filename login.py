from sre_constants import SUCCESS
from tkinter import *
from tkinter import messagebox
from turtle import color
def login():
    username=entry1.get()
    password=entry2.get()
    # if(username==" " or password==" "):
    #     messagebox.showinfo("blank not allowed")
    # else:
abhi=Tk()
abhi.title("Login")
abhi.geometry("1280x720")
abhi.configure(bg='lightblue')
abhi.resizable(False, False)
abhi.iconbitmap('./download.ico')
global entry1
global entry2
Label(abhi,text="Username:", font=("Times New Roman", 40)).place(x=200,y=80)
Label(abhi,text="Password:", font=("Times New Roman", 40)).place(x=200,y=240)
entry1=Entry(abhi,bd=7, font=("Times New Roman", 30))
entry1.place(x=600,y=85)
entry2=Entry(abhi,bd=7, show='*',font=("Times New Roman", 30))
entry2.place(x=600,y=245)
Button(abhi,text="Login", height=3, width=25, bd=6, font=("Helvetica")).place(x=600,y=560)
Button(abhi,text="Back",height=3,width=25,bd=6,font=("Helvetica")).place(x=950,y=560)
mainloop()

