
from HH_func_salary import func_s
import sys
args = [int(i) for i in sys.argv[1:]]

for i in args:
    tax = func_s(i)
    print(f'給与:{i}、支給額:{i-tax}、税額:{tax}')
