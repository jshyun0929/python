inFp, outFp = None, None
fName1, fName2, inStr = "", "", ""

fName1 = input("소스 파일명을 입력하세요 : ")
fName2 = input("타깃 파일명을 입력하세요 : ")
inFp = open(fName1, "r", encoding="UTF8")
outFp = open(fName2, "w", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---파일 복사 성공---")
