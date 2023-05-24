from datetime import date
import sys
from datetime import date
from database import session
from database import Base
from database import ENGINE
from tables import Holiday
from aqua_db import Attendnum
import pymysql
args = sys.argv

#週末計算
a = args[1]
year = a[:4]
month = a[4:6]
day = a[6:8]

dt = date(int(year), int(month), int(day))
day = dt.strftime("%a")

#
i=1
holiday_list = session.query(Holiday.holi_date).filter_by(holi_date = dt).count()

i = holiday_list+1


b = int(args[2]) #大人の人数
c = int(args[3]) #子供の人数

workday_adult = 2000
weekend_adult = 2400
workday_kid = 1200
weekend_kid = 1500
#

#

if day == "Sat" or day == "Sun" or session.query(Holiday.holi_date).filter_by(holi_date = dt).all():
    result = b * weekend_adult + c * weekend_kid
    attendnum = Attendnum(
        entry_date = dt,
        seq = int(i),
        adult = int(b),
        child = int(c)
    )
    session.add(attendnum)
    session.commit()
    print(result, end="")
else:
    result = b * workday_adult + c * workday_kid
    attendnum = Attendnum(
        entry_date = dt,
        seq = int(i),
        adult = int(b),
        child = int(c)
    )
    session.add(attendnum)
    session.commit()
    print(result, end="")

