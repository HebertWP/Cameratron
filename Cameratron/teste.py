from tkinter import *

def callback():
        print ("clicked!")
b = Button(text="click me", command=callback)
b.pack()
mainloop()
