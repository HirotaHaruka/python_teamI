# 偶数と奇数を判別するプログラム
import sys
args = sys.argv[1]

input_num = int(args)

if input_num % 2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")