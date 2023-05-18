import sys

args = sys.argv

sum = 0 #合計値
input1 = args[1] #一番目の引数
input2 = args[2] #二番目の引数
input3 = args[3] #三番目の引数

#合計を求める
sum = int(input1) + int(input2) + int(input3)

print(sum, end="")