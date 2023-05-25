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
holiday_list = session.query(Holiday.holi_date).filter_by(holi_date = dt).count()
print(holiday_list)

