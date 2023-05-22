import sys

args = sys.argv
input1 = int(args[1]) #1番目のコマンドライン引数
input2 = int(args[2]) #2番目のコマンドライン引数
input3 = int(args[3]) #3番目のコマンドライン引数

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

calcvalue(input1)
calcvalue(input2)
calcvalue(input3)