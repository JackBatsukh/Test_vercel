from tkinter import *
root = Tk()
root.title("hello world")
root.geometry('350x300')
x = Label(root, text="Test program")
x.pack()
b = Button(root,text = "click me", width=25, command=root.destroy)
b.pack()
root.mainloop()