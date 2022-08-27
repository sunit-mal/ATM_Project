import io
import openpyxl


from tkinter import *
from NewUserData import NewUser as r1
from NewUserData import existingUser as r2
from openpyxl import Workbook, load_workbook


class main:
    def run():
        def create():
            root.destroy()
            r1.dataInser()

        # def encrypt():
        #     exit()    

        def search():
            root.destroy()
            r2.dataCheck()
            print(r2.Password)

        wb = load_workbook('DataBase.xlsx')
        ws1 = wb['Login Info']
        # Window ready code :
        root = Tk()
        root.geometry("700x438")
        root.maxsize(700, 438)
        root.minsize(700, 438)
        root.title('Login Page')
        root.iconbitmap('Custom-Icon-Design-Pretty-Office-11-Coins.ico')
        root.config(bg='#B0CFDE')

        my_label = Label(root, text='Welcome  To  My  Project', font=(
            'Times New Roman', 18,'bold'),bg ='#B0CFDE',fg='#EC0000').place(x=220, y=100)
        NewUser_Button = Button(root, text="New User",
                                command=create).place(x=200, y=250)
        ExistingUser_Button = Button(
            root, text="Exesting User", command=search).place(x=400, y=250)

        # ext_btn = Button(root, text='Exit',width=7,bg='green',fg='white',font=('Times new roman',10,'bold'), command=encrypt)
        # ext_btn.place(x=600, y=350)
        

        
        root.mainloop()

 


try:
    main.run()
except:
    print("")
