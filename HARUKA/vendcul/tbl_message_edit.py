from ven_DB_c import Tbl_Message
import sys
import os
sys.path.append(os.pardir)
from datetime import date
from database import session

#登録するデータの編集
def tbl_insert(seq_num, message_str, datetime_d):
    tbl_message = Tbl_Message(
        seq = int(seq_num),
        message = message_str,
        datetime = datetime_d
    )
    #Insertの処理
    session.add(tbl_message)
    #コミット
    session.commit()

#登録情報の閲覧
def tbl_select():
    tbl_message = session.query(Tbl_Message).all()
    return tbl_message