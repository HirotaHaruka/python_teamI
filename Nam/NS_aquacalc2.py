import sys
from datetime import date
from database import session
from tables import Holiday
from aqua_db import Attendnum

#週末計算（引数（文字列）を割る）
# a = args[1]
# year = a[:4]
# month = a[4:6]
# day = a[6:8]

args = sys.argv
dt = date(args[1], '%Y%m%d')
day = dt.strftime("%a")

i=1
#祝日が重複した数＋i＝連番
holiday_list = session.query(Holiday.holi_date).filter_by(holi_date = dt).count()
i = holiday_list+1

#重複したdate数＋i＝連番
entryDate_list = session.query(Attendnum.entry_date).filter_by(entry_date = dt).count()
i = entryDate_list+1

adult_num = int(args[2]) #大人の人数
child_num = int(args[3]) #子供の人数

#料金変数宣言
workday_adult = 2000
weekend_adult = 2400
workday_kid = 1200
weekend_kid = 1500

#週末＆祝日の場合、週末料金を算出し、データをDBに入れる
if day == "Sat" or day == "Sun" or session.query(Holiday.holi_date).filter_by(holi_date = dt).all():
    result = adult_num * weekend_adult + child_num * weekend_kid
    attendnum = Attendnum(
        entry_date = dt,
        seq = int(i),
        adult = int(adult_num),
        child = int(child_num)
    )
    session.add(attendnum)
    session.commit()
    print(result, end="")
#平日の料金算出、データをDBに入れる
else:
    result = adult_num * workday_adult + child_num * workday_kid
    attendnum = Attendnum(
        entry_date = dt,
        seq = int(i),
        adult = int(adult_num),
        child = int(child_num)
    )
    session.add(attendnum)
    session.commit()
    print(result, end="")

