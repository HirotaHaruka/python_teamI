from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    if salary <= 1000000 :
        tax=salary*0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding = ROUND_HALF_UP)
        return tax, salary-tax
    else:
        over_mill = salary - 1000000
        over_mill = over_mill * 0.2
        over_mill = over_mill + 100000
        over_mill = Decimal(str(over_mill)).quantize(Decimal("0"), rounding = ROUND_HALF_UP)
        return over_mill, salary-over_mill

