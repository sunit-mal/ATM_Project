#   Window - 1

class User:
    def Run():
        import tkinter as tkk

        def ExsistingUser():
            root.destroy()
            from Login import LoginPageForExsistingUser as p
            p.Run()
        def NewUser():
            root.destroy()
            from Login import LoginPageForNewUser as o
            o.Run()
        root=tkk.Tk()
        root.title("User Type")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('.\download.ico')

        tkk.Button(root,text="New User", height=3, width=40, bd=5, font=("Helvetica"),command=NewUser).place(x=140,y=320)
        tkk.Button(root,text="Existing User", height=3, width=40, bd=5, font=("Helvetica"),command=ExsistingUser).place(x=700,y=320)
    

        tkk.mainloop()

# User.Run()
