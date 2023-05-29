# 引数で受け取った数まで羊を数え、テキストファイルに出力
import sys
import os
sys.path.append("/../../files")
args = sys.argv

# 整数の受け取り
input_num = int(args[1])

file_name = "../../files/sheep.txt"
# with open(file_name, mode = "w") as f:
#     for i in range(input_num):
#         f.write(f"ひつじが{i + 1}匹\n")
#     print(len(f))

line_num = 0
with open(file_name, mode = "r") as f:
    for line_num, _ in enumerate(f):
        pass

with open(file_name, mode = "a") as f:
    for i in range(input_num):
        f.write(f"ひつじが{i + 1 + line_num}匹\n")