import sys
import os
from sqlalchemy import Column, String, Integer, Date, VARCHAR
sys.path.append(os.pardir)
from database import Base
from database import ENGINE

class Mst_Merchandise(Base):#商品マスタ
    __tablename__ = 'mst_merchandise'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))
    price = Column('price', Integer)
    
class Tbl_Stock(Base): # 商品在庫テーブル
    __tablename__ = 'tbl_stock'
    id = Column('id', String(10),  primary_key = True)
    stock = Column('stock', Integer)

class Tbl_Money(Base): # 貨幣格納テーブルの設定
    __tablename__ = 'tbl_money'
    price = Column('price', Integer,  primary_key = True)
    number = Column('number', Integer)
    

class Tbl_Message(Base): # メッセージテーブルの設定
    __tablename__ = 'vendcul_message'
    seq = Column('seq', Integer,  primary_key = True)
    message = Column('message', String(100))
    datetime = Column('datetime', Date)




def main(args):
    """メイン関数"""
    Base.metadata.create_all(bind=ENGINE)
    
if __name__ == "__main__":
    main(sys.argv)