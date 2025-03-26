select = int(input("1.입력한 수식 계산 2.두 수 사이의 합계 :"))

if select == 1:
    cal = input("*** 수식을 입력하세요")
    print(cal, "결과는", eval(cal), "입니다")
elif select == 2:
    num1 = int(input("*** 첫번째 숫자를 입력하세요"))
    num2 = int(input("*** 두번째 숫자를 입력하세요"))
    a = (num2 - num1 + 1)*(num1 + num2)/2
    print(num1, "+...+", num2, "는", a, "입니다")
else:
    print("1또는2만 입력해주세요")

