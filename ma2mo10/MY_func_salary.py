from decimal import Decimal, ROUND_HALF_UP

def calcsalary(total_salary):
    MILLION = 1000000
    tax = 0                     #税額
    salary = 0                  #支給額

    if total_salary > MILLION:
        tax = int(Decimal(str((total_salary - MILLION) * 0.2)) + Decimal(str(MILLION * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
    else:
        tax = int(Decimal(str(total_salary * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

    salary = int(total_salary - tax)
    
    return salary, tax