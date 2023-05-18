import sys

args = sys.argv

if int(args[1]) % 2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")
