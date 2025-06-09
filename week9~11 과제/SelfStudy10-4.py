from tkinter import *
from tkinter import messagebox

##함수 선언 부분##
def shift_left(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")

def shift_right(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")

def shift_up(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")

def shift_down(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")

##메인 코드 부분##
window = Tk()

window.bind("<Shift-Down>", shift_down)
window.bind("<Shift-Up>", shift_up)
window.bind("<Shift-Right>", shift_right)
window.bind("<Shift-Left>", shift_left)

window.mainloop()