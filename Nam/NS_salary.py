from decimal import Decimal, ROUND_HALF_UP

import sys
args = sys.argv

#引数を変数に代入
salary = int(args[1])

if salary <= 1000000 :
    tax=salary*0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding = ROUND_HALF_UP)
    print("支給額:"+str(salary-tax)+"、税額:"+str(tax), end="")
else:
    over_mill = salary - 1000000
    over_mill = over_mill * 0.2
    over_mill = over_mill + 100000
    over_mill = Decimal(str(over_mill)).quantize(Decimal("0"), rounding = ROUND_HALF_UP)
    print("支給額:"+str(salary-over_mill)+"、税額:"+str(over_mill), end="")

