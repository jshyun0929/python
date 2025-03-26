base = int(input("입력 진수 결정 (16/10/8/2) :"))
num = input("값 입력 :")

if base == 16 :
    a = int(num, 16)
if base == 10 :
    a = int(num)
if base == 8 :
    a = int(num, 8)
if base == 2 :
    a = int(num, 2)

print("16진수 ==>", hex(a))
print("10진수 ==>", a)
print("8진수 ==>", oct(a))
print("2진수 ==>", bin(a))