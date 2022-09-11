#   Window - 8

class pin_chnage:
    def Run():
        import tkinter as tk

        root=tk.Tk()
        root.title("Pin change")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')
        OldPassword = tk.StringVar()
        NewPassword = tk.StringVar()

        tk.Label(root,text="Enter new password:", font=("Times New Roman", 30)).place(x=200,y=80)
        tk.Label(root,text="Confiem password:", font=("Times New Roman", 30)).place(x=200,y=240)
        tk.Entry(root,bd=4,textvariable= OldPassword,width=30, font=("Times New Roman", 30)).place(x=600,y=85)
        tk.Entry(root,bd=4,textvariable= NewPassword,width=30, show='*',font=("Times New Roman", 30)).place(x=600,y=245)
        tk.Button(root,text="Next", height=2, width=20, bd=5, font=("Times New Roman", 15,"bold"),command="").place(x=650,y=560)
        

        tk.mainloop()


pin_chnage.Run()