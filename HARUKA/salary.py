import sys
salary = int(sys.argv[1])
if salary <= 1000000:
    tax = salary * 0.1
else:
    tax = (salary - 1000000)*0.2 + 100000

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

tax = Decimal(str(tax)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(f'支給額:{salary-tax}、税額:{tax}',end="")