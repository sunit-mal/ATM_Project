class existinguserblancecredited:
    def play():
        import tkinter as tk
     #window 13
        def ok():
            root.destroy()
            from SignType import User as s
            s.Run()

        root=tk.Tk()
        root.title('existing user')
        root.geometry("1280x720")
        # root.iconbitmap('./download.ico')
        root.resizable(False, False)
        root.configure(bg='lightblue')

        #   funtion key

        tk.Label(root, text=" Thank You ", fg='blue', font=("Times New Roman", 50)).place(x=480, y=200)
        tk.Label(root, text=" Your Balance is Successfully Credied ", fg='blue', font=("Times New Roman", 50)).place(x=120, y=300)
        tk.Button(root,text="ok",height=3,width=20,bd=6,font=("Times New Roman", 15,"bold"),command=ok).place(x=1000,y=600)

        tk.mainloop()

existinguserblancecredited.play()