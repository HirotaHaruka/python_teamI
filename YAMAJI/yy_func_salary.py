# 給与と支給額を計算する関数
from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    # 税率の変わる境界の値段
    border_tax = 1000000
    # 境界以下の場合の税率
    per_tax_l = 0.1
    # 境界より多い場合の税率
    per_tax_h = 0.2


    if salary <= border_tax:
        tax_amount = salary * per_tax_l
    else:
        tax_amount = (salary - border_tax) * per_tax_h + border_tax * per_tax_l

    # 税率の四捨五入
    tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding="ROUND_HALF_UP")
    payment_amount = salary - tax_amount

    return tax_amount, payment_amount