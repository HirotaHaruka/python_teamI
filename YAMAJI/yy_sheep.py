# 引数で受け取った数まで羊を数える
import sys
args = sys.argv

# 整数の受け取り
input_num = int(args[1])

for i in range(input_num):
    print(f"ひつじが{i + 1}匹")
