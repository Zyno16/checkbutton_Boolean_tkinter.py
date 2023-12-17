from tkinter import *
form =Tk()
form.geometry("700x500")
v =BooleanVar()
cb = Checkbutton(form,text="i agree",variable = v)
cb.pack()
def f():
    print(v.get())
Button(form,text="ok",command = f).pack()



form.mainloop()
