import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類のkeyの集まりをタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類のkeyの集まりをタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類のkeyの集まりをタプルで定義

#第二引数で受け取ったカテゴリの判別
#categoly_itemsにfruits、alcohol、noodlesのいずれかを代入　以降categly_itemsをkeyの集まりとして使う
if hm_class == "果物類":
    categoly_items = fruits
elif hm_class == "酒類":
    categoly_items = alcohol
elif hm_class == "麺類":
    categoly_items = noodles

#タプルに格納されているkeyをもとに値引き処理を行う
for item in categoly_items:
    hinmoku[item] = hinmoku[item] - price_down
    if hinmoku[item] <= 0 : hinmoku[item] = 1      #0円以下になった場合の処理

print(hinmoku, end="")