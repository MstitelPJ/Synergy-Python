from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')


def clicked():
    print('Clicked')


# btn = Button(root, text="Кнопка", command=clicked, font="Arial 20 italic")
# btn = Button(root, text="Кнопка", command=clicked, font=("Comic Sans MS", 20))
btn = Button(root, text="Кнопка 1\n22", justify=LEFT)
btn.configure(width=20)
# btn['font'] = 'Arial 15'
btn.pack()



root.mainloop()