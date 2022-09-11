# Window - 12

class ThakyouPlay:
    def play():
        import tkinter as tk

        root=tk.Tk()
        root.title('Thank You')
        root.geometry("1280x720")
        root.iconbitmap('./download.ico')
        root.resizable(False, False)
        root.configure(bg='lightblue')

        #   funtion key

        tk.Label(root, text="Thank You Visit Again", fg='blue', font=("Times New Roman", 50)).place(x=380, y=270)
        tk.Button(root,text="ok",height=3,width=20,bd=6,command="").place(x=1000,y=490)

        tk.mainloop()

ThakyouPlay.play()