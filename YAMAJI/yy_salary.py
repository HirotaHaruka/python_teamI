# 給与から税額と支給額を計算する
# 四捨五入のために、モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv

# 給与の入力
salary = int(args[1])

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
print("支給額:{0}、税額:{1}".format(payment_amount, tax_amount), end="")