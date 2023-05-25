#商品の定義
product = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

#商品を出力＆投入金額入力を貰う
for key, value in product.items(): 
    print(key+":"+str(value)+"円")
entry_money = int(input("投入金額を入力してください"))

#入力戻し関数
def reenter():
    entry_money = 0
    entry_money = int(input("投入金額を入力してください"))

#一番低い商品の金額
lowest_amount = sorted(product.values())[0]

#5円玉、1円玉使用不可
if str(entry_money)[-1] == "1" or str(entry_money)[-1] == "5":
    print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
    reenter()
#一万円超える場合
elif 10000 < entry_money:
    print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
    reenter()
#最低金額より投入金額が低い場合
elif lowest_amount > entry_money:
    print("{0}円では購入できる商品がありません。再度投入金額を入力してください".format(entry_money))
    reenter()
#最低金額 <= 投入金額
elif lowest_amount <= entry_money:
    choice = input("何を購入しますか（商品名/cancel）")
    #商品の選択
    if choice == "":
        pass
    #注文のキャンセル
    elif choice == "cancel":
        pass







