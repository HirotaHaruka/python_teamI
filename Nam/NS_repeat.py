# 入力した値を繰り返して足し算し、
# 合計がちょうど100になった場合は「Just 100!」と表示して終了し、
# 100を超えた場合は「Over!」と表示して終了するプログラムを作成せよ
 
# ■ 入力する値
# 1つの整数                                    例）15
 
# ■ 期待する出力
# 繰り返し足し算した結果          例）Over!
 
# ■ 実行例
# > python repeat.py 15              ：第2引数に15を設定
# > Over!                                        ：出力結果

import sys
args = sys.argv

number = int(args[1])

resultsum = 0

while resultsum<100:
    resultsum = resultsum + number

if resultsum == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")