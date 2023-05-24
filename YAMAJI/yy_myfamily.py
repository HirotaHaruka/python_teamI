# 派生クラスを利用した自己紹介
import yy_introfamily
import sys
args = sys.argv

# コマンドライン入力の受け取り
name = args[1]
age = args[2]
cat_name = args[3]

# 自己紹介インスタンスの作成
my_intro = yy_introfamily.IntroFam(name, age)
print(my_intro.name_out())
print(my_intro.age_out())
print(my_intro.cat_out(cat_name))
