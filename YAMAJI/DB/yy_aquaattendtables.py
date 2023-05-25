import sys
from sqlalchemy import Column, String, Date, Integer
from DB.yy_database import Base
from DB.yy_database import ENGINE

# テーブル：Holidayの定義
class AttendNum(Base):
    __tablename__ = 'attendnum'
    entry_date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    adult = Column('adult', Integer)
    child = Column('child', Integer)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind = ENGINE)

if __name__ == "__main__":
    main(sys.argv)
