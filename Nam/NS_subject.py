import sys
args = sys.argv

#引数を変数に代入
input1 = args[1]
input2 = args[2]
input3 = args[3]

math = int(input1)
japanese = int(input2)
english = int(input3)

sum=math+japanese+english

if (sum >=220) or (math >= 70 and japanese >= 70 and english >= 70) and not( math < 50 and japanese < 50 and english < 50):
    print("合格", end="")
else:
    print("不合格", end="")


