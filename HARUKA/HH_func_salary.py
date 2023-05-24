
def func_s(salary): # 給与を入力として 給与、支給額、税額を出力する。
    if salary <= 1000000:
        tax = salary * 0.1
    else:
        tax = (salary - 1000000)*0.2 + 100000

    from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

    tax = Decimal(str(tax)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    return tax