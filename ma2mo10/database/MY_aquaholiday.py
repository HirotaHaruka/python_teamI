from datetime import datetime
import sys
from MY_database import session
from MY_tables import Holiday


args = sys.argv


dt = datetime.strptime(args[1], '%Y%m%d') #文字列をdatetime型に変換
adult_num = int(args[2])                  #大人の人数
child_num = int(args[3])                  #子供の人数

#料金の合計を計算する関数
def aquacalc(dt, adult_num, child_num):
    d_of_t_w = dt.strftime('%a') #曜日
    
    holiday = session.query(Holiday.holi_text).filter_by(holi_date=dt).first()
    
    #土曜か日曜なら休日料金、平日なら通常料金を返す
    if (d_of_t_w == "Sat" or d_of_t_w == "Sun") or holiday.holi_text is not None:
        return (adult_num * 2400) + (child_num * 1500)
    else:
        return (adult_num * 2000) + (child_num * 1200)
    
#合計金額の表示
print(aquacalc(dt, adult_num, child_num), end="")