#   Window - 5

class Transaction_Menu:
    def Run():
        import tkinter as tkk

        def Withdrawl():
            root.destroy()
            from WithdrawlPage import Withdrawl as w
            w.Run()
        def PinChange():
            root.destroy()
            from PinChange import  pin_chnage as w
            w.Run()

        def BalanceEnq():
            root.destroy()
            from BalanceEnq import balanceenq as w
            w.run()
        def Deposit():
            root.destroy()
            from Deposit import DepositNewUser as w 
            w.run() 
        def Home():
            root.destroy()
            from Welcome import WelcomePlay as w 
            w.run()        

        root=tkk.Tk()
        root.title("Transaction Menu")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')

        tkk.Button(root,text="Balance Enquiry", height=3, width=40, bd=5, font=("Helvetica"),command=BalanceEnq).place(x=50,y=100)
        tkk.Button(root,text="Deposit",height=3,width=40,bd=5,font=("Helvetica"),command=Deposit).place(x=50,y=400)
        tkk.Button(root,text="Cash Withdrawl", height=3, width=40, bd=5, font=("Helvetica") ,command=Withdrawl).place(x=850,y=100)
        tkk.Button(root,text="Pin Change",height=3,width=40,bd=5,font=("Helvetica"),command=PinChange).place(x=850,y=400)
        tkk.Button(root,text="Home",height=3,width=25,bd=5,font=("Helvetica"),command=Home).place(x=515,y=600)

        tkk.mainloop()

Transaction_Menu.Run()