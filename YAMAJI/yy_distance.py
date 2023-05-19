# 辞書型で要素の参照と演算
from decimal import Decimal, ROUND_HALF_UP

import sys
args = sys.argv

# 地名の受け取り
place1 = args[1]
place2 = args[2]

distance_list = {'東京':0.00, '品川':6.78, '新横浜':25.54, 
                 '名古屋':342.02,'京都':476.31, '新大阪':515.35}


print('{:.2f}'.format(abs(distance_list[place1] - distance_list[place2])),end="")