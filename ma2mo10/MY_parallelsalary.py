import MY_func_salary as salary     #MY_func_salaryの呼び出し

#calcsalaryの呼び出し
print("支給額:{0}、税額:{1}".format(*(salary.calcsalary(100000))))
print("支給額:{0}、税額:{1}".format(*(salary.calcsalary(1000000))))
print("支給額:{0}、税額:{1}".format(*(salary.calcsalary(1200000))))