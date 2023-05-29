#import datatime
from datetime import datetime

#引数設定
import sys
args = sys.argv

#引数をdatetime型に置き換える
dt = datetime.strptime(args[1], '%Y%m%d') 

#変数に引数を代入
adult = int(args[2])
child = int(args[3])

#変数にdatetimeを入れる
weekday = dt.strftime("%a")

#土日の判定を行い合計金額を計算
if weekday == "Sat" or weekday == "Sun":
    sum = 2400 * adult + 1500 * child
    print(sum)
else:
    sum = 2000 * adult + 1200 * child
    print(sum)