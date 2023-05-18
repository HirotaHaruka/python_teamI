import sys
# コマンドライン引数の取得
args = sys.argv

# 引数の取得
input1 = args[1]
input2 = args[2]
input3 = args[3]

ans = int(input1) + int(input2) + int(input3)

print(str(ans), end="")