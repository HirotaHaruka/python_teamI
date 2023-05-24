import sys
from datetime import date
args = sys.argv
year, month, day = int(args[1][:4]),int(args[1][4:6]),int(args[1][6:]) #年月日に分割
dt = date(year, month, day)
adult_num = int(args[2]) #　大人の人数
child_num = int(args[3]) #　子供の人数
rest_d = ['Sun', 'Sat']
flag_day = 0
if dt.strftime("%a") in rest_d: flag_day = 1 #休日かを判定
fee = 0
if flag_day == 1: #平日か休日化で料金の計算を分岐
    fee = adult_num * 2400 + child_num * 1500
else:
    fee = adult_num * 2000 + child_num * 1200
print(fee, end="")
