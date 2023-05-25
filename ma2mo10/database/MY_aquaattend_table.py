import sys
from sqlalchemy import Column, String, Date, Integer
from MY_database import Base
from MY_database import ENGIN


class Aquaattend(Base):
    __tablename__ = 'aquaattend'
    entry_date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    adult = Column('adult', Integer)
    child = Column('child', Integer)

def main(args):
    Base.metadata.create_all(bind=ENGIN)




if __name__ == "__main__":
    main(sys.argv)