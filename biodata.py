class BioData:
    def bio():
        import tkinter as tkk

        root=tkk.Tk()
        root.title("Bio Data")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')

        tkk.Label(root,text="Name:", font=("Times New Roman", 40)).place(x=200,y=150)
        tkk.Label(root,text="Mobile No:", font=("Times New Roman", 40)).place(x=200,y=255)
        tkk.Label(root,text="Email:", font=("Times New Roman", 40)).place(x=200,y=360)
        tkk.Entry(root,bd=4, font=("Times New Roman", 30)).place(x=600,y=150)
        tkk.Entry(root,bd=4,font=("Times New Roman", 30)).place(x=600,y=255)
        tkk.Entry(root,bd=4, font=("Times New Roman", 30)).place(x=600,y=360)
        tkk.Button(root,text="Clear", height=3, width=25, bd=5, font=("Helvetica")).place(x=650,y=560)
        tkk.Button(root,text="Next",height=3,width=25,bd=5,font=("Helvetica")).place(x=950,y=560)
        tkk.mainloop()

BioData.bio()