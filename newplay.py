from tkinter import * 
win = Tk()
win.title("Haihoang")
win.geometry("800x700")

win['bg'] = "blue"
win.attributes('-topmost', False)

name = Label(win, text = "Hello world", font = ("Times New Roman", 14), bg = "blue", fg = "white")
name.place(x = 30, y = 10)
win.mainloop()

