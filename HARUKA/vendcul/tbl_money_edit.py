from ven_DB_c import Tbl_Money
import sys
import os
sys.path.append(os.pardir)
from datetime import date
from database import session

#登録するデータの上書き
def Tbl_Money_update(price_n, num_n):
    tbl_money = session.query(Tbl_Money).filter_by(price=price_n).first()
    tbl_money.number = int(num_n)
    session.add(tbl_money)
    #コミット
    session.commit()

#登録情報の閲覧
def tbl_select(price_n):
    tbl_money = session.query(Tbl_Money.number).filter_by(price=price_n).all()
    return tbl_money

def tbl_money_insert(price_n, num_n):
    tbl_money = Tbl_Money(
        price = int(price_n),
        number = num_n,
    )
    #Insertの処理
    session.add(tbl_money)
    #コミット
    session.commit()
