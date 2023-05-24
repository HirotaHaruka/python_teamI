# import sys
# args = sys.argv

# num = []
# for i in args[1:]:
#     num.append(int(i))

# def calcvalue(*num):
#     for i in num:
#         if i % 2 == 1:
#             print(str(i)+"は変数")
#         elif i % 2 == 0:
#             print(str(i)+"は偶数")

# calcvalue(num[])

import sys
args = sys.argv

def calcvalue(num):
    for i in range(len(num)):
        if num[i] % 2 == 1:
            print(str(num[i])+"は奇数")
        elif num[i] % 2 == 0:
            print(str(num[i])+"は偶数")

num = []

for i in range(len(sys.argv)):
    if i == 0:
        continue
    num.append(int(args[i]))


calcvalue(num)
