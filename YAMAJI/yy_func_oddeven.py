# 関数を用いて偶数・奇数の判定を行う
import sys
args = sys.argv

#関数を定義
def calcvalue(num):
    #余りを算出
    mod = num % 2

    #余りの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

# コマンドラインで指定された引数の数に合わせて反復処理
for num in args[1:]:
    calcvalue(int(num))