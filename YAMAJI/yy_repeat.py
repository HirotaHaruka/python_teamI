# 引数で受け取った整数を100を超えるまで加算
import sys
args = sys.argv

# 整数の受け取り
input_num = int(args[1])
result = 0

# 入力値の繰り返し加算
while result < 100:
    result += input_num

# 結果の出力
if result == 100:
    print("Just 100!", end="")
else:
    print("Over!",end="")