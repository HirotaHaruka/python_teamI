import MY_input as MYin

#商品リストを定義
item_dict = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

#商品リストを表示
for item in item_dict:
    print(f"{item}：{item_dict[item]}円")

#金額の入力を受け付ける
money = MYin.input_money()
#商品名/cancelの入力を受け付ける
item_name = input("何を購入しますか（商品名/cancel）")

#cancelが入力された場合お釣りを返す
if item_name == "cancel":
    pass
else:
    pass
