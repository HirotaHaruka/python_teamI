import sys
num = int(sys.argv[1])
n = int(num//2)
l = []

for i in range(2,n):
    if num % i == 0:
        while True:
            num = num/i
            l.append(i)
            if num % i != 0:
                break
    if num < i :
        break
if len(l) >=2:
    print(l,end="")
else:
    print([num], end="")