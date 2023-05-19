# 【世界人口ランキング】
# ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
 
# ■ 入力する値
# 知りたい順位の値(a)                     例）５
 
# ■ 期待する出力
# 第5位の国名                                     例）Pakistan
 
# ■ 実行例
# > python population.py 5             ：第2引数に5を設定
# > Pakistan                                      ：出力結果
     
# ■ 条件
# ・第2引数は0 以上、 10以下の数値とする
 
# ■ 作成のヒント
# ・出力結果には、改行コードを含まない


import sys
args = sys.argv

rank = int(args[1])

kuni = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(kuni[rank-1], end="")