inFp = None
inList, inStr = [], ""
line_num = 0

inFp = open("C:\\Users\\znfpf\\OneDrive\\바탕 화면\\python_programming\\과제모음\\week9~10 과제\\text1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList:
    line_num += 1
    print("%d: %s"%(line_num, inStr), end="")

inFp.close()