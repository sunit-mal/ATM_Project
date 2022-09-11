# Window - 0

class WelcomePlay:
    def Run():
        import tkinter as tk
        
        root=tk.Tk()
        root.iconbitmap('./download.ico')
        root.resizable(False, False)
        root.configure(bg='lightblue')
        root.title('Welcome')
        root.geometry("1280x720")

        tk.Label(root, text="WELCOME", fg='blue', font=("Times New Roman", 70)).place(x=400, y=200)
        tk.Button(root,text="NEXT",height=2,width=20,bd=5,font=("Times New Roman", 15,"bold"),command="").place(x=950,y=560)

        tk.mainloop()

WelcomePlay.Run()