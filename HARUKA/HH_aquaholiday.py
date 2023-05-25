import sys
from datetime import date
from datetime import date
from database import session 
from tables import Holiday
from sqlalchemy import Column, String, Integer, Date


holiday_list = session.query(Holiday.holi_date).all()

holi_list = [] #祝日の月日を取得
for i in holiday_list:
    l = str(i).split(',')
    holi_day = int(l[-2][:-1])
    holi_month = int(l[-3])
    holi_list.append([holi_month, holi_day])

args = sys.argv
year, month, day = int(args[1][:4]),int(args[1][4:6]),int(args[1][6:]) #年月日に分割
dt = date(year, month, day)
adult_num = int(args[2]) #　大人の人数
child_num = int(args[3]) #　子供の人数
rest_d = ['Sun', 'Sat']
flag_day = 0
if dt.strftime("%a") in rest_d: flag_day = 1 #休日かを判定
elif [month, day] in holi_list: flag_day = 1 #祝日考慮
fee = 0
if flag_day == 1: #平日か休日化で料金の計算を分岐
    fee = adult_num * 2400 + child_num * 1500
else:
    fee = adult_num * 2000 + child_num * 1200
print(dt.strftime("%a"))
print(fee, end="",)

