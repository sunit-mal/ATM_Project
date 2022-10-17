#   Window - 8

class pin_chnage:
    def Run(Usernum):
        import tkinter as tk
        from PIL import Image,ImageTk

        def next():
            newpass= NewPassword.get()
            reenter = reenterPassword.get()
            if(newpass == reenter):
                root.destroy()
                from OTPSend import VarificationCheck as o
                o.send(Usernum,newpass)
            else:
                tk.Label(root,text="Re-Enter Password", font=("Times New Roman", 30)).place(x=200,y=20)
            NewPassword.set("")
            reenterPassword.set('')
            
        root=tk.Tk()
        root.title("Pin change")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')
        img= Image.open('Background.jpg')
        img_file= img.resize((1280,720), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(img_file)
        bgl = tk.Label(root,image=bg,bd=0)
        bgl.place(x=0, y=0, width=1280,height=720)
        reenterPassword = tk.StringVar()
        NewPassword = tk.StringVar()

        tk.Label(root,text="Enter new password:", font=("Times New Roman", 30)).place(x=200,y=80)
        tk.Label(root,text="Confirm password:", font=("Times New Roman", 30)).place(x=200,y=240)
        tk.Entry(root,bd=4,textvariable= NewPassword,width=30,show='*', font=("Times New Roman", 30)).place(x=600,y=85)
        tk.Entry(root,bd=4,textvariable= reenterPassword,width=30, show='*',font=("Times New Roman", 30)).place(x=600,y=245)
        tk.Button(root,text="Next", height=2, width=20, bd=5, font=("Times New Roman", 15,"bold"),command=next).place(x=650,y=560)
        
        tk.mainloop()


# pin_chnage.Run(3)