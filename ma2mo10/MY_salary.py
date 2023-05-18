import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv
MILLION = 1000000
total_salary = int(args[1]) #給与
tax = 0                     #税額
salary = 0                  #支給額

if total_salary > MILLION:
    tax = int(Decimal(str(((total_salary - MILLION) * 0.2) + (MILLION * 0.1))).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
else:
    tax = int(Decimal(str(total_salary * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

salary = int(total_salary - tax)
print("支給額:{0}、税額:{1}".format(salary, tax), end="")