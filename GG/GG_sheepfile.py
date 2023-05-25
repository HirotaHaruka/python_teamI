import os
import sys
args = sys.argv

#引数を変数に代入
max = int(args[1]) 

#0から変数の数値まで繰り返す
# for i in range(0, max):
#     i = i + 1
#     # print("ひつじが" + str(i) + "匹" )

#テキストファイルを開く
with open("../../files/sheepfile.txt", "w", encoding="utf-8") as f:
    #テキストファイルに書き込む
    for i in range(0, max):
        i = i + 1
        # print("ひつじが" + str(i) + "匹" )
        f.write("ひつじが" + str(i) + "匹\n" )


#os.path.joinを利用して相対パスを生成する
#相対パス(..../files/path.png)となる
# path = os.path.join("..", "..", "files", "sheepfile.txt")

