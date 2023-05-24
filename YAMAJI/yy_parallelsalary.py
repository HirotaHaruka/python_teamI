# func_salaryを使って、給与の支給額を計算するプログラム
import yy_func_salary as func_salary
import yy_func_salary
import sys
args = sys.argv

# 複数入力について支給額と税金を計算
for salary in args[1:]:
    tax_amount, payment_amount = func_salary.calcsalary(int(salary))
    print(f"給与:{salary}、支給額:{payment_amount}、税額:{tax_amount}")
