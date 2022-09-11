#   Window - 7

class Withdrawl:
    def Run():
        import tkinter as tkk

        root=tkk.Tk()
        root.title("Withdrawl")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')

        tkk.Label(root,text="Amount:", font=("Times New Roman", 40)).place(x=200,y=153)
        
        tkk.Entry(root,bd=4, font=("Times New Roman", 30)).place(x=600,y=153)

        tkk.Button(root,text="Home", height=3, width=25, bd=5, font=("Helvetica")).place(x=145,y=560)
        tkk.Button(root,text="Clear", height=3, width=25, bd=5, font=("Helvetica")).place(x=650,y=560)
        tkk.Button(root,text="Next",height=3,width=25,bd=5,font=("Helvetica")).place(x=950,y=560)

        tkk.mainloop()

Withdrawl.Run()
