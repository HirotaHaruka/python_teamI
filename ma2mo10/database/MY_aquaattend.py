from datetime import date
from MY_database import session
from MY_aquaattend_table import Aquaattend
import sys
from datetime import datetime


args = sys.argv

dt = datetime.strptime(args[1], '%Y%m%d') #文字列をdatetime型に変換
adult_num = int(args[2])                  #大人の人数
child_num = int(args[3])                  #子供の人数

#Tabel内に存在する同じ日数をカウント
entry_dt_cnt = session.query(Aquaattend).filter_by(entry_date=dt).count()

aquaattend = Aquaattend(
    entry_date = dt,
    seq = entry_dt_cnt + 1,
    adult = adult_num,
    child = child_num
)

session.add(aquaattend)
session.commit()