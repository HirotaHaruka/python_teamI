from ven_DB_c import Mst_Merchandise
import sys
import os
sys.path.append(os.pardir)
from datetime import date
sys.path.append(os.pardir)
from database import session

#登録するデータの上書き
def Mst_Merchandise_update_name(id_n, name_str):
    mst_merchandise = session.query(
        Mst_Merchandise).filter_by(id=id_n).first()
    mst_merchandise.name = name_str
    session.add(mst_merchandise)
    #コミット
    session.commit()
    
def Mst_Merchandise_update_price(id_n, price_n):
    mst_merchandise = session.query(
        Mst_Merchandise).filter_by(id=id_n).first()
    mst_merchandise.price = price_n
    session.add(mst_merchandise)
    #コミット
    session.commit()
def Mst_Merchandise_insert(id_n, name_str, price_n):
    mst_merchandise = Mst_Merchandise(
        id = int(id_n),
        name = name_str,
        price = price_n
    )
    #Insertの処理
    session.add(mst_merchandise)
    #コミット
    session.commit()
#登録情報の閲覧
def Mst_Merchandise_select():
    mst_merchandise = session.query(Mst_Merchandise).all()
    return mst_merchandise