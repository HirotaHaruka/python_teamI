import sys

args = sys.argv

sheep = int(args[1])        #ひつじの数

#開始値0から終了値sheep
for i in range(0, sheep):
    print("ひつじが{0}匹".format(i+1))