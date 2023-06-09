import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別 (果物類 or 酒類 or 麺類)
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く

hinmoku_cate = {"果物類":fruits,"酒類":alcohol,"麺類":noodles}

for hinmoku_key in hinmoku_cate[hm_class]:
    hinmoku[hinmoku_key] = hinmoku[hinmoku_key]-price_down
    if hinmoku[hinmoku_key] <= 0 : hinmoku[hinmoku_key] = 1



print(hinmoku, end="")