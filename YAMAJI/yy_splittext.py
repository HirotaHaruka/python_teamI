# 入力された文字列のn語目を出力
import sys
args = sys.argv

# 文字列とnの受け取り
sentens = args[1]
split_num = int(args[2])

print(sentens.split()[split_num - 1], end="")