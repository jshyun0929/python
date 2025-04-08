i, k, dan = 0, 0, ""

for i in range(2, 10):
    dan = dan + (" # {}단 # ".format(i))

print(dan)

for i in range(1,10):
    dan = ""
    for k in range(2, 10):
        dan = dan + (" {0}X {1}= {2:<2}".format(k, i, k*i))
    print(dan)
