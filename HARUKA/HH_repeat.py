import sys

num = int(sys.argv[1])
s = 0
while True:
    s += num
    if s == 100:
        print("Just 100!", end="")
        break
    elif s > 100:
        print("Over!", end="")
        break
    
if 100 % num == 0:
    print("Just 100!", end="")
else:
    print("Over!", end="")