from tkinter import Menu


class Transaction_Menu:
    def Money():
        import tkinter as tkk

        root=tkk.Tk()
        root.title("Transaction Menu")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')

        tkk.Button(root,text="Balance Enquiry", height=3, width=40, bd=5, font=("Helvetica")).place(x=50,y=100)
        tkk.Button(root,text="Deposit",height=3,width=40,bd=5,font=("Helvetica")).place(x=50,y=400)
        tkk.Button(root,text="Cash Withdrawl", height=3, width=40, bd=5, font=("Helvetica")).place(x=850,y=100)
        tkk.Button(root,text="Pin Change",height=3,width=40,bd=5,font=("Helvetica")).place(x=850,y=400)
        tkk.Button(root,text="Home",height=3,width=25,bd=5,font=("Helvetica")).place(x=515,y=600)

        tkk.mainloop()

Transaction_Menu.Money()