from tkinter import *

# print(dir(tkinter.Tk))

win = Tk(screenName=None, baseName=None, className='Tk', useTk=1)

win.geometry("1080x720")

c = Checkbutton(win, text="Check1")
c.pack()

c2 = Checkbutton(win, text="Check2")
c2.pack()

win.mainloop()
