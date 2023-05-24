import NS_func_salary
import sys
args = sys.argv

salary1 = int(args[1])
salary2 = int(args[2])
salary3 = int(args[3])

salary = [salary1,salary2,salary3]

i=0
for i in salary: 
    tax, payment = NS_func_salary.calcsalary(i)
    print("給与:"+str(i)+"支給額:"+str(payment)+"、税額:"+str(tax))
