from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:\\Users\\znfpf\\OneDrive\\바탕 화면\\python_programming\\WindowProgramming\\dog-15_256.gif")
photo2 = PhotoImage(file = "C:\\Users\\znfpf\\OneDrive\\바탕 화면\\python_programming\\WindowProgramming\\dog-3343_256.gif")
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()