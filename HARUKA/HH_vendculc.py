buy = str(input("あなたが欲しい商品は？:"))
hinmoku = ('お茶', 'コーヒー', 'ソーダ', 'コーンポタージュ')
dic = {
    'お茶'              :   110,
    'コーヒー'          :   100,
    'ソーダ'            :   160,
    'コーンポタージュ'   :   130,
}
def buy_drink(money):
    """挿入されている金額から購入の是非を聞く関数"""
    while True:
        can_buy = ()
        for i in hinmoku:
            if dic[i] <= money:
                can_buy.append(i)
        if len(can_buy) == 0:
            print(f'{money}円では購入できる商品がありません。再度投入金額を入力してください。')
            continue
        while True:
            for i in can_buy:
                print(f'{i} ： {dic[i]}円')
            b = input('何を購入しますか？(商品名/cancel):')
            if b =='cancel':
                print('お金を返金します。')
                return
            elif  not b in can_buy:
                print('選択された商品はありません。')
                print('再度選択してください。')
                continue
            
        else:
            money -= dic[b]
            print(f'残金：{money}円')
            do_buy = input('続けて購入しますか(Y/N) :')
        if do_buy == 'N':
            break
    return money


def vendculc():
    buy = str(input("あなたが欲しい商品は？:"))
    if not buy in hinmoku:
        print('そのような商品はありません。')
        return

    while True:
        try :
            mony = int(input('投入金額を入力してください'))
            if mony >= 10000:
                print('10,000円を超える金額は投入できません。再度投入金額を入力してください。')
                continue
            if mony % 10 != 0:
                print('1円、5円玉は使用できません。再度投入金額を入力してください。')
                continue
        except:
            print('お金が正しく入力されませんでした。')
            continue
        can_buy = ()
        for i in hinmoku:
            if dic[i] <= mony:
                can_buy.append(i)
        if len(can_buy) == 0:
            print(f'{mony}円では購入できる商品がありません。再度投入金額を入力してください。')
            continue
        
        money = buy_drink(money)
        
        if do_buy == 'Y':
            while True:
                can_buy = ()
                for i in hinmoku:
                    if dic[i] <= mony:
                        can_buy.append(i)
                if len(can_buy) == 0:
                    print(f'{mony}円では購入できる商品がありません。再度投入金額を入力してください。')
                    continue
                while True:
                    for i in can_buy:
                        print(f'{i} ： {dic[i]}円')
                    b = input('何を購入しますか？(商品名/cancel):')
                    if b =='cancel':
                        print('お金を返金します。')
                        return
                    elif  not b in can_buy:
                        print('選択された商品はありません。')
                        print('再度選択してください。')
                        continue
                    
                else:
                    money -= dic[b]
                    print(f'残金：{mony}円')
                    do_buy = input('続けて購入しますか(Y/N) :')
                if do_buy == 'N':
                    break
        
        print('おつり')
            
            
        
can_buy = ()
for i in hinmoku:
    if dic[i] <= mony:
        can_buy.append(i)
if len(can_buy) >= 1:
    for i in can_buy:
        print(f'{i} ： {dic[i]}円')
    b = input('何を購入しますか？(商品名/cancel):')
else: print('購入できる商品がありません')
if b =='cancel' or not b in can_buy:
    # return money
else:
    m = money - dic[b]
    