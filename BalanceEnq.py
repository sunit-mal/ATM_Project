class balanceenq:
    def Run():
        import tkinter as tk

        root = tk.Tk()
        root.title("Balance")
        root.geometry("1280x720")
        root.configure(bg='lightblue')
        root.resizable(False, False)
        root.iconbitmap('./download.ico')

        tk.Label(root, text="YOUR BALANCE IS:", fg='blue',font=("Times New Roman", 50)).place(x=380, y=270)
        tk.Button(root, text="OK", height=3, width=20, bd=5, font=("Times New Roman", 15, "bold"),command="").place(x=1000, y=590)

        tk.mainloop()
balanceenq.Run()
