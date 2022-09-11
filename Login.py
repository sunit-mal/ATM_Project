# Window 2 & 3

# Window - 2
class LoginPageForExsistingUser:
    def Run():
        import tkinter as tk

        root=tk.Tk()
        root.title("Login")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')
        UserId = tk.StringVar()
        Password = tk.StringVar()

        tk.Label(root,text="User Id:", font=("Times New Roman", 30)).place(x=200,y=80)
        tk.Label(root,text="Password:", font=("Times New Roman", 30)).place(x=200,y=240)
        tk.Entry(root,bd=4,textvariable= UserId,width=30, font=("Times New Roman", 30)).place(x=600,y=85)
        tk.Entry(root,bd=4,textvariable= Password,width=30, show='*',font=("Times New Roman", 30)).place(x=600,y=245)
        tk.Button(root,text="Next", height=2, width=20, bd=5, font=("Times New Roman", 15,"bold"),command="").place(x=650,y=560)
        tk.Button(root,text="Back",height=2,width=20,bd=5,font=("Times New Roman", 15,"bold"),command="").place(x=950,y=560)

        tk.mainloop()

# Window - 3
class LoginPageForNewUser:
    def Run():
        import tkinter as tkk
        
        root=tkk.Tk()
        root.title("Login")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')
        UserId = tkk.StringVar()
        Password = tkk.StringVar()

        tkk.Label(root,text="User Id:", font=("Times New Roman", 30)).place(x=200,y=80)
        tkk.Label(root,text="Password:", font=("Times New Roman", 30)).place(x=200,y=240)
        tkk.Entry(root,bd=7,textvariable= UserId,width=30, font=("Times New Roman", 30)).place(x=600,y=85)
        tkk.Entry(root,bd=7,textvariable= Password,width=30, show='*',font=("Times New Roman", 30)).place(x=600,y=245)
        tkk.Button(root,text="Next", height=2, width=20, bd=5, font=("Times New Roman", 15,"bold"),command="").place(x=650,y=560)
        tkk.Button(root,text="Back",height=2,width=20,bd=5,font=("Times New Roman", 15,"bold"),command="").place(x=950,y=560)
        
        tkk.mainloop()

LoginPageForExsistingUser.Run()
# LoginPageForNewUser.Run()
