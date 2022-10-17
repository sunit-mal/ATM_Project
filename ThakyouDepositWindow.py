    #window 14,13
    
class ThankYouWWindows:
    def play():
        import tkinter as tk
        from PIL import Image,ImageTk

        def backHome():
            root.destroy()
            from SignType import User as H
            H.Run()

        root=tk.Tk()
        root.title('New user')
        root.geometry("1280x720")
        root.iconbitmap('./download.ico')
        root.resizable(False, False)
        root.configure(bg='lightblue')
        img= Image.open('Background.jpg')
        img_file= img.resize((1280,720), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(img_file)
        bgl = tk.Label(root,image=bg,bd=0)
        bgl.place(x=0, y=0, width=1280,height=720)

        #   funtion key

        tk.Label(root, text=" Thank You ", fg='blue', font=("Times New Roman", 50)).place(x=480, y=200)
        tk.Label(root, text=" Your Balance is Successfully Credied ", fg='blue', font=("Times New Roman", 50)).place(x=120, y=300)
        tk.Button(root,text="ok",height=3,width=20,bd=6,font=("Times New Roman", 15,"bold"),command=backHome).place(x=1000,y=600)

        tk.mainloop()

# ThankYouWWindows.play()