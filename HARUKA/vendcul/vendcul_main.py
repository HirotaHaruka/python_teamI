import sys
import os
sys.path.append(os.pardir)
from datetime import date
from database import session
import get_DB
import edit_DB
import tbl_message_edit
import datetime
class vendculc():
    def __init__(self):
        self.buy = []
        
    def getmoney(self):
        self.money_num = int(input('投入金額を入力してください'))
        return self.money_num
    
    def juge_money(self):
        try :
            if self.money_num >= 10000:
                print('10,000円を超える金額は投入できません。再度投入金額を入力してください。')
                return False
            if self.money_num % 10 != 0:
                print('1円、5円玉は使用できません。再度投入金額を入力してください。')
                return False
        except:
            print('お金が正しく入力されませんでした。')
            return False
        return True
    
    def true_get_money(self):
        juge = False
        while not juge:
            vendculc.getmoney(self)
            juge = vendculc.juge_money(self)
        return
    
    def buy_drink(self):
        while True: # 金額が最低の商品以上かつ続けて購入する気があるなら繰り返す
            can_buy = []
            for i in self.hinmoku:
                if self.ven_dic[i] <= self.money_num:
                    if self.id_stock_cnt[int(self.name_id[i])] >= 1:
                        can_buy.append(i)
            if len(can_buy) == 0:
                print(f'{self.money_num}円では購入できる商品がありません。再度投入金額を入力してください。')
                break
            while True: # 何を購入するかの処理
                juge1 = vendculc.Which_buy(self, can_buy)
                if juge1: break
                else: continue
            if self.b == 'cancel': #cancelなら購入履歴とお金を返す
                return self.money_num, self.buy
            # 購入処理
            self.money_num -= self.ven_dic[self.b]
            print(f'残金：{self.money_num}円')
            self.buy.append(self.b)
            juge2 = vendculc.JugeConte(self) #続けて買うかの処理
            if juge2: continue
            else: break
        return
        
    def JugeConte(self): # 続けて購入するかの是非を問う
        while True:
            do_buy = input('続けて購入しますか(Y/N) :')
            if do_buy == 'N': break
            elif do_buy == 'Y': break
            else:
                print('YかNを入力してください。')
                continue
        if do_buy == 'Y':return True
        else: return False
    
    def Which_buy(self, can_buy):
        for i in can_buy:
            print(f'{i} ： {self.ven_dic[i]}円')
        self.b = input('何を購入しますか？(商品名/cancel):')
        if self.b =='cancel':
            print('お金を返金します。')
            return True
        elif  not self.b in can_buy:
            print('選択された商品はありません。')
            print('再度選択してください。')
            return False
        else:
            print(f"{self.b}を購入します")
            self.id_stock_cnt[int(self.name_id[self.b])] -= 1
            return True
    
    def Change_money(self):
        C_list = []
        C_pattern = [5000, 1000, 500, 100, 50, 10]
        for i in C_pattern:
            C_list.append(self.money_num//i)
            self.money_num %= i
        print('おつり')
        for ids,i in enumerate(C_pattern):
            if C_list[ids] != 0:
                self.price_cnt[i] = int(self.price_cnt[i]) - int(C_list[ids])
                if i >= 1000:  
                    print(f'{i}円札：{C_list[ids]}枚')
                else:
                    print(f'{i}円玉：{C_list[ids]}枚')
                    
    def get_ven_dics(self):
        name_id, id_price, price_cnt, id_stock_cnt = get_DB.main()
        self.name_id = name_id
        self.id_price = id_price
        self.price_cnt = price_cnt
        self.id_stock_cnt = id_stock_cnt
        self.ven_dic = {}
        self.hinmoku = []
        for key,value in name_id.items():
            self.ven_dic[key] = id_price[value]
            self.hinmoku.append(key)
    
    def edit_DB(self):
        edit_DB.main(self.id_stock_cnt, self.price_cnt)
        for key,value in self.price_cnt.items():
            if value <= 9:
                try:
                    seq = tbl_message_edit.tbl_select()[-1].seq
                except:
                    seq = 0
                message = f'{key}のお金が{value}個しかないです。'
                dt_now =  datetime.datetime.now()
                tbl_message_edit.tbl_insert(seq+1, message, dt_now)
        
    def main(self):
        vendculc.true_get_money(self)#投入された金額が正しいか
        vendculc.get_ven_dics(self)#データベースから情報を抽出
        vendculc.buy_drink(self)#飲み物を購入する処理
        vendculc.Change_money(self)#おつりを計算する処理
        vendculc.edit_DB(self)#データベースの更新
        return 
