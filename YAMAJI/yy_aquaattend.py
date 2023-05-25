import sys
sys.path.append("./DB")
import datetime
from yy_database import session
from yy_aquaattendtables import AttendNum
args = sys.argv

# コマンドライン入力の受け取り
visiting_date_str = args[1]
adl_num = int(args[2])
chil_num = int(args[3])

# 文字型を日付型に変更
visiting_date = datetime.datetime.strptime(visiting_date_str,"%Y%m%d")

# 同じ来場日に来た組数を検索
seq_num = session.query(AttendNum).filter_by(entry_date = visiting_date).count()

# DBに登録
attendnum = AttendNum(
    entry_date = visiting_date,
    seq = seq_num + 1,
    adult = adl_num,
    child = chil_num
)

session.add(attendnum)

session.commit()