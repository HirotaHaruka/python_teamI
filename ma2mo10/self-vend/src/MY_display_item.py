#商品の表示や何を購入するかの入力受付に関するモジュール
import MY_input as MYin

def display_item(item_dict:dict) -> str:
    #商品リストを表示
    for item in item_dict:
        print(f"{item}：{item_dict[item]}円")

    #金額の入力を受け付ける
    money = MYin.input_money()
    #商品名/cancelの入力を受け付ける
    item_name = MYin.input_item(money, item_dict)

    return item_name
