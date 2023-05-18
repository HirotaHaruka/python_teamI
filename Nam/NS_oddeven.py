import sys
args = sys.argv

number = float(args[1])

if number % 2 == 0:
    print("偶数")
else:
    print("奇数")