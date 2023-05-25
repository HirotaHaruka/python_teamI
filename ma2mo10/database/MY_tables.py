import sys
from sqlalchemy import Column, String, Date, Integer
from MY_database import Base
from MY_database import ENGIN

class Holiday(Base):
    __tablename__ = 'holyday'
    holi_date = Column('holi_date', Date, primary_key = True)
    holi_text = Column('holi_text', String(20))

def main(args):
    Base.metadata.create_all(bind=ENGIN)

if __name__ == "__main__":
    main(sys.argv)