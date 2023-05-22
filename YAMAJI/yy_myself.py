# 自己紹介を行う処理
import yy_introduce
import sys
args = sys.argv

# コマンドライン入力の受け取り
name = args[1]
age = args[2]

# 自己紹介インスタンスの作成
my_intro = yy_introduce.Intro(name, age)
print(my_intro.name_out())
print(my_intro.age_out())
