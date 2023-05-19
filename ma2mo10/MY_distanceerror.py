import sys
from decimal import Decimal, ROUND_HALF_UP

station = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}
args = sys.argv

station_name1 = args[1]
station_name2 = args[2]
distance = 0

try:
    if station[station_name1] > station[station_name2]:
        distance = station[station_name1] - station[station_name2]
    else:
        distance = station[station_name2] - station[station_name1]


    print(Decimal(str(distance)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), end="")

except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")