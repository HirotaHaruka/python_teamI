from datetime import date
from MY_database import session
from MY_tables import Holiday

result = session.query(Holiday).filter_by(holi_date=date(2024, 1, 1)).delete()

session.commit()