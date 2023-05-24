from datetime import date
from MY_database import session
from MY_tables import Holiday

holiday = session.query(Holiday).filter_by(holi_date=date(2024, 1, 1)).first()

holiday.holi_text = "元旦"
session.add(holiday)
session.commit()