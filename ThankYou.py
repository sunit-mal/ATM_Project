# Window - 12

# Window - 12

class ThakyouPlay:
    def play():
        import tkinter as tk
        from PIL import Image,ImageTk

        root=tk.Tk()
        root.title('Thank You')
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

        tk.Label(root, text="Thank You Visit Again", fg='blue', font=("Times New Roman", 50)).place(x=380, y=270)
        tk.Button(root,text="ok",height=3,width=20,bd=6,font=("Times New Roman", 15,"bold"),command="").place(x=1000,y=600)

        tk.mainloop()

# ThakyouPlay.play()