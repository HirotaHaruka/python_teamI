from ven_DB_c import Tbl_Stock
import sys
import os
sys.path.append(os.pardir)
from datetime import date
from database import session

#登録するデータの上書き
def Tbl_Money_update(id_n, stock_n):
    tbl_stock = session.query(Tbl_Stock).filter_by(id=id_n).first()
    tbl_stock.stock = int(stock_n)
    session.add(tbl_stock)
    #コミット
    session.commit()

#登録情報の閲覧
def tbl_select():
    tbl_stock = session.query(Tbl_Stock).all()
    return tbl_stock

def Tbl_Money_insert(id_n, stock_n):
    tbl_stock = Tbl_Stock(
        id = int(id_n),
        stock = stock_n
    )
    #Insertの処理
    session.add(tbl_stock)
    #コミット
    session.commit()