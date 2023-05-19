# 動物の名前リストを定義し、以下の順で操作した結果のリストを出力するプログラムを作成せよ
# ①     第2引数で設定した要素の位置に、第3引数の動物名を挿入する
# ②     リストの最後の要素を削除する
# ③     リストを昇順に並べ替える
 
# 【動物の名前リスト】
#   "giraffe", "tiger", "zebra", "elephant", "lion"
 
# ■ 入力する値
# 挿入箇所の整数（a）と挿入する動物名         例）1 buffalo
 
# ■ 期待する出力
# 操作した結果のリスト                                        例）['buffalo', 'elephant', 'giraffe', 'tiger', 'zebra']
 
# ■ 実行例
# > python animallist.py 1 buffalo                        ：第2引数に1、第3引数にbuffaloを設定
# > ['buffalo', 'elephant', 'giraffe', 'tiger', 'zebra']    ：出力結果
     
# ■ 条件
# ・第2引数は0 以上、 5以下の数値とする
 
# ■ 作成のヒント
# ・出力結果には、改行コードを含まない
import sys
args = sys.argv

num = int(args[1])
ani = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animals.insert(num, ani)


animals.pop()
animals.sort()

print(animals, end="")





