import MY_func_salary as salary     #MY_func_salaryの呼び出し
import sys

args = sys.argv

salary1 = int(args[1])
salary2 = int(args[2])
salary3 = int(args[3])

#calcsalaryの呼び出し
print("支給額:{0}、税額:{1}".format(*(salary.calcsalary(salary1))))
print("支給額:{0}、税額:{1}".format(*(salary.calcsalary(salary2))))
print("支給額:{0}、税額:{1}".format(*(salary.calcsalary(salary3))))