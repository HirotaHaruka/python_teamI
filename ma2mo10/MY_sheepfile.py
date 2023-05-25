import sys

args = sys.argv
filename = "../../files/sheep.txt"      #ファイル名

sheep = int(args[1])        #ひつじの数

with open(filename, mode="w", encoding="utf-8") as f:
#開始値0から終了値sheep
    for i in range(0, sheep):
        f.write("ひつじが{0}匹".format(i+1))