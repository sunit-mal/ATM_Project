class User:
    def UserType():
        import tkinter as tkk

        root=tkk.Tk()
        root.title("User Type")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')

        tkk.Button(root,text="New User", height=3, width=50, bd=5, font=("Helvetica")).place(x=140,y=320)
        tkk.Button(root,text="Existing User", height=3, width=50, bd=5, font=("Helvetica")).place(x=700,y=320)
       

        tkk.mainloop()

User.UserType()
