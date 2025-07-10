import random
import string
import tkinter
m = tkinter.Tk()
jms = 0
def change(val):
    global jms
    jms = int(val)
w2 = tkinter.Scale(m, from_=1, to=30, orient=tkinter.HORIZONTAL, command=change, length=300)
w2.place(x=100, y=135)
def randstring(size=jms, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
label = tkinter.Label(m, text=randstring(jms))
label.place(x=165, y=205)
def generate_new_string():
    new_str = randstring(jms)
    label.config(text=new_str)
def copy_to_clipboard():
    m.clipboard_clear()
    m.clipboard_append(
        label.cget("text").strip()
    )
    m.update()
copy_button = tkinter.Button(m, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.place(x=100, y=250)
button = tkinter.Button(m, text="Generate", command=generate_new_string)
button.place(x=100, y=200)
m.geometry("500x500")
m.title("Password Generator")
m.mainloop()