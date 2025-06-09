from tkinter import *
from time import *

## 전역 변수 선언 부분 ##
fnameList = ["dog-3343_256.gif", "dog-15_256.gif", "dog-7011_256.gif", "cat-5873_256.gif", "cat-6139_256.gif", "cat-6147_256.gif", "cat-8915_256.gif", "dog-4480_256.gif", "happy-cat-8738_256.gif"]
photoList = [None] * 9
num = 0

## 함수 선언 부분 ##
def clickNext():
    global num
    num +=1
    if num > 8:
        num = 0
    photo = PhotoImage(file="C:\\Users\\znfpf\\OneDrive\\바탕 화면\\python_programming\\WindowProgramming\\" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    fileLabel.configure(text=fnameList[num])
def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="C:\\Users\\znfpf\\OneDrive\\바탕 화면\\python_programming\\WindowProgramming\\"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    fileLabel.configure(text=fnameList[num])

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨번 보기")
btnPrev = Button(window, text= "<< 이전", command= clickPrev)
btnNext = Button(window, text= "다음 >>", command= clickNext)
photo = PhotoImage(file="C:\\Users\\znfpf\\OneDrive\\바탕 화면\\python_programming\\WindowProgramming\\"+fnameList[0])
pLabel = Label(window, image=photo)
fileLabel = Label(window, text=fnameList[0])

btnPrev.place(x=200, y=10)
btnNext.place(x=450, y=10)
fileLabel.place(x=300, y=10)
pLabel.place(x=15, y=50)

window.mainloop()