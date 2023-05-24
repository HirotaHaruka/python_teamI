from datetime import date
from MY_database import session
from MY_tables import Holiday

holiday = Holiday(
    holi_date = date(2024, 1, 1),
    holi_text = "お正月"
)

session.add(holiday)
session.commit()