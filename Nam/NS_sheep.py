# 「ひつじが1匹」、「ひつじが2匹」・・・「ひつじがn匹」と入力した整数の回数分繰り返すプログラムを作成せよ
 
# ■ 入力する値
# 1つの整数                                                                           例）1
 
# ■ 期待する出力
# 引数に設定した回数「ひつじがn匹」を出力する       例）ひつじが1匹
 
# ■ 実行例
# > python sheep.py 3                    ：第2引数に3を設定
# > ひつじが1匹                              ：出力結果
# > ひつじが2匹                              ：出力結果
# > ひつじが3匹                              ：出力結果
     
# ■ 条件
# 1 ≦ a ≦ 200

import sys
args = sys.argv

sheep = int(args[1])

for i in range(1, sheep+1):
    print("ひつじが"+str(i)+"匹")
    continue

