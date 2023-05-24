# 自動販売機のお釣りの計算を行う

# 商品のリスト
vending_items = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
change_digits = [5000, 2000, 1000, 500, 100, 50, 10]

# おつりを表記する処理
def out_change(possession_money):
    print("おつり")
    for i in change_digits:
        digits = possession_money // i
        if digits != 0:
            possession_money -= i * digits
            if i >= 1000:
                print(f"{i}円札：{digits}枚")
            else:
                print(f"{i}円玉：{digits}枚")

# 購入のメインプログラム
def vendingMachine():
    # 初期入力の処理
    while True:
        possession_money = int(input("投入金額を入力してください："))
        # 投入金額による分岐処理
        if possession_money >= min(vending_items.values()):
            break
        elif possession_money > 10000:
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください。")
        elif possession_money % 10 != 0:
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください。")
        elif possession_money >= min(vending_items.values()):
            print(f"{possession_money}円では購入できる商品がありません。再度購入金額を入力してください。")
        else:
            print("入力が不正な値です。")
    
    # 購入処理
    while True:
        # 商品表の出力
        for key, i in vending_items.items():
            print(key + "：" + str(i) + "円")

        buy_item = input("何を購入しますか(商品名/cancel)：")

        if buy_item == "cancel":
            # 購入キャンセル
            out_change(possession_money)
            break
        elif buy_item in vending_items and possession_money >= vending_items[buy_item]:
            # 購入
            print(buy_item)
            possession_money -= vending_items[buy_item]
            # まだ購入できる場合
            if possession_money >= min(vending_items.values()):
                print(f"残高：{possession_money}円")
                continue_flag = input("続けて購入しますか(Y/N)：")
                if continue_flag == "Y":
                    continue
                elif continue_flag == "N":
                    out_change(possession_money)
                    break
            # 残高が足りない場合
            elif possession_money < min(vending_items.values()):
                out_change(possession_money)
                break
            # 残高が0になった場合
            elif possession_money == 0:
                break
        # 残高より高い商品を購入しようとした場合
        elif possession_money < vending_items[buy_item]:
            print("投入金額が不足しています。")
            
vendingMachine()