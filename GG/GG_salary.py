import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

#引数を変数に代入
salary = int(args[1])

salaryover = salary - 100000

tax = salaryover * 0.2
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

sumtax = tax + 10

sumsalary = salary - tax

if (salary > 1000000):
    print("支給額：" + sumsalary, ",税額：" + sumtax)
else:
    print("支給額：" + sumsalary, ",税額：" + salary * 0.1)