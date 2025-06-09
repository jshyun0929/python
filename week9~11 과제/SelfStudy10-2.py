from tkinter import *
import random

## 전역 변수 선언 부분 ##
btnList = [None] * 9
fnameList = ["dog-3343_256.gif", "dog-15_256.gif", "dog-7011_256.gif", "cat-5873_256.gif", "cat-6139_256.gif", "cat-6147_256.gif", "cat-8915_256.gif", "dog-4480_256.gif", "happy-cat-8738_256.gif"]
photoList = [None] * 9
i,k = 0,0
xPos, Ypos = 0,0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("201x210")
random.shuffle(fnameList)

for i in range(0, 9):
    photoList[i] = PhotoImage(file="C:\\Users\\znfpf\\OneDrive\\바탕 화면\\python_programming\\WindowProgramming\\" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0,3):
        btnList[num].place(x = xPos, y = Ypos)
        num += 1
        xPos += 70
    xPos = 0
    Ypos +=70

window.mainloop()
