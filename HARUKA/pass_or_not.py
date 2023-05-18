import sys
args = [int(i) for i in sys.argv[1:4] ]
flag = 0
if sum(args) >= 220 or min(args) >= 70:
    flag = 1
if args[0] < 50 or args[1] < 50 or args[2] < 50:
    flag = 0
if flag == 1:
    print('合格',end="")
else:
    print('不合格',end="")