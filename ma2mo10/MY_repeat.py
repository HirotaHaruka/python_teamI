import sys

args = sys.argv
input = int(args[1])
sum = 0

while sum < 100: sum = sum + input

if sum == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")