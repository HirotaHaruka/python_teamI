# 日付によって変わる料金計算
import datetime
import sys
args = sys.argv

# コマンドライン入力の受け取り
visiting_date_str = args[1]
adl_num = int(args[2])
chil_num = int(args[3])

# 文字型を日付型に変更
visiting_date = datetime.datetime.strptime(visiting_date_str,"%Y%m%d")

# 曜日ごとの料金
workday_adl_fee = 2000
holiday_adl_fee = 2400
workday_chil_fee = 1200
holiday_chil_fee = 1500

# 曜日を計算
weekday = visiting_date.strftime("%a")
if weekday == "Sat" or weekday == "Sun":
    fee = holiday_adl_fee * adl_num + holiday_chil_fee * chil_num
else:
    fee = workday_adl_fee * adl_num + workday_chil_fee * chil_num
print(fee, end="")