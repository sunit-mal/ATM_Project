class OTPGENERATOR:
    def Run(num,passw):
        import tkinter as tk

        def verifing():
            print(num,passw)
            otp = OTPNumber.get()
            if (otp == str(num)):
                from openpyxl import Workbook, load_workbook
                wb = load_workbook('DataBase.xlsx')
                ws = wb['LoginInfo']
                ws[f'B{2}'] = passw
                wb.save('DataBase.xlsx')
                root.destroy()
                # print(varificationcode,passw)
            else:
                OTPNumber.set('')

        root=tk.Tk()
        root.title("OTPGENERATOR")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        # root.iconbitmap('./download.ico')
        OTPNumber = tk.StringVar()

        tk.Label(root,text="ENTER OTP ", font=("Times New Roman", 30)).place(x=200,y=260)
        tk.Entry(root,bd=4,textvariable= OTPNumber,width=20, font=("Times New Roman", 30)).place(x=600,y=270) 
        tk.Button(root,text="Done", height=2, width=20, bd=5, font=("Times New Roman", 15,"bold"),command=verifing).place(x=650,y=460)
        
        tk.mainloop()

# OTPGENERATOR.Run(2121,'sunit')


