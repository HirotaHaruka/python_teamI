import sys
from decimal import Decimal, ROUND_HALF_UP

#駅名をキーとした東京からの距離を格納した辞書を生成
sta_dict = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}


args = sys.argv           #コマンドライン引数(第2引数:出発駅、第3引数:到着駅)

dep_sta = args[1]         #出発駅
arr_sta = args[2]         #到着駅
distance = 0              #距離


try:
    #出発駅と到着駅の東京駅からの距離を比較して距離の差を求める
    if sta_dict[dep_sta] > sta_dict[arr_sta]:
        distance = sta_dict[dep_sta] - sta_dict[arr_sta]
    else:
        distance = sta_dict[arr_sta] - sta_dict[dep_sta]

    #Decimal().quantize()で値を丸めて標準出力する
    print(Decimal(str(distance)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), end="")

#のぞみの停車駅以外が引数に与えられた場合の例外処理
except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")