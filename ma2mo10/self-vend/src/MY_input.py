#入力関係のモジュール
from MY_return_change import changecalc, changedisplay

def input_money():
   '''入力金額を受け取る関数'''
   LIMIT_MONEY = 10000  #投入金額の上限
   MIN_PRICE = 100      #最小の商品価格
   money = int(input("投入金額を投入して下さい"))

   #条件に合致する場合に例外処理を行う
   while True:
      if money > LIMIT_MONEY:
         money = int(input(f"{LIMIT_MONEY}円を超える金額は投入できません。再度投入金額を入力してください"))
      elif money % 2 != 0:
         money = int(input("1円玉、5円玉は使用できません。再度投入金額を入力してください"))
      elif money < MIN_PRICE:
         money = int(input(f"{money}円では購入できる商品がありません。再度投入金額を入力してください"))
      else:
         #moneyの値が正常ならmoneyをreturnする
         return money


def input_item(money, item_dict):
   '''商品名の入力を受け取る関数'''
   item_name = input("何を購入しますか（商品名/cancel）")

   #cancelが入力された場合お釣りを返す
   while True:
      if item_name == "cancel":
         changedisplay(changecalc(money))
         return ""
      elif item_name in item_dict:
         item_name = input("商品名が間違っています。正しい商品名を入力してください")
      else:
         return item_name
   

