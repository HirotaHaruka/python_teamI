# 英文と取り出したい単語の位置を入力し、指定した位置の単語を出力するプログラムを作成せよ
 
# ■ 入力する値
# 英文と取り出したい単語の位置          例）“I am human” 2
 
# ■ 期待する出力
# 指定した位置の単語                               例）am
 
# ■ 実行例
# > python splittext.py “I am human” 2       ：第2引数に英文、第3引数に取出位置を設定
# > am                                       ：第3引数に設定した位置の単語を出力

import sys
args = sys.argv

input1 = args[1]
input2 = int(args[2])

result = input1.split()

print(result[input2-1])
