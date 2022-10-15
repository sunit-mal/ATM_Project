class collectmoney:
    def play():
        import tkinter as tk
     #window 15
        root=tk.Tk()
        root.title('window 15')
        root.geometry("1280x720")
        # root.iconbitmap('./download.ico')
        root.resizable(False, False)
        root.configure(bg='lightblue')

        #   funtion key

        tk.Label(root, text=" Please Collect Your Money ", fg='blue', font=("Times New Roman", 50)).place(x=280, y=300)
        
        tk.Button(root,text="ok",height=3,width=20,bd=6,font=("Times New Roman", 15,"bold"),command="").place(x=1000,y=600)

        tk.mainloop()

collectmoney.play()