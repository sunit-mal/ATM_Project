# Window - 0

class WelcomePlay:
    def Run():
        import tkinter as tk
        from PIL import Image,ImageTk
        
        def next():
            root.destroy()
            from SignType import User as i
            i.Run()

        root=tk.Tk()
        root.resizable(False, False)
        # root.configure(bg='lightblue')
        root.title('Welcome')
        root.geometry("1280x720")
        root.iconbitmap('.\download.ico')

        img= Image.open('Background.jpg')
        img_file= img.resize((1280,720), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(img_file)
        bgl = tk.Label(root,image=bg,bd=0)
        bgl.place(x=0, y=0, width=1280,height=720)

        tk.Label(root, text="WELCOME", fg='blue', font=("Times New Roman", 70)).place(x=400, y=200)
        tk.Button(root,text="NEXT",height=2,width=20,bd=5,font=("Times New Roman", 15,"bold"),command=next).place(x=950,y=560)
        
        tk.mainloop()


WelcomePlay.Run()