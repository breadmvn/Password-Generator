import random
import string
import tkinter
m = tkinter.Tk()
def randstring(size=15, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def create_message():
    global genm2
    genm2 = tkinter.Message(m, text=randstring(), width=105, wrap=None)
    genm2.pack()

genm = randstring()
genm2 = tkinter.Message(m, text=genm, width=105 ,wrap=None)
genm2.config(wrap=None)
genm2.place(x=20, y=-55)
genm2.pack()
button = tkinter.Button(m, text='Generate', width=25, command=create_message)
button.pack()
m.mainloop()
