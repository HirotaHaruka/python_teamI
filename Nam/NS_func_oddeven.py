import sys
args = sys.argv

num = []
for i in args[1:]:
    num.append(int(i))

def calcvalue(*num):
    for i in num:
        if i % 2 == 1:
            print(str(i)+"は変数")
        elif i % 2 == 0:
            print(str(i)+"は偶数")

calcvalue(num[])