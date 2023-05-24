from datetime import date
import sys
args = sys.argv

#週末計算
a = args[1]
year = a[:4]
month = a[4:6]
day = a[6:8]

dt = date(int(year), int(month), int(day))
day = dt.strftime("%a")

b = int(args[2]) #大人の人数
c = int(args[3]) #子供の人数

workday_adult = 2000
weekend_adult = 2400
workday_kid = 1200
weekend_kid = 1500

if day == "Sat" or day == "Sun":
    result = b * weekend_adult + c * weekend_kid
    print(result, end="")
else:
    result = b * workday_adult + c * workday_kid
    print(result, end="")