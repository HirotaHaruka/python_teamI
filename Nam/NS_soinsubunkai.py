import sys
args = sys.argv

num = args[1]
x = 2
a = []

while (int(num) != 1):
    if(int(num) % x == 0):
        num = int(num) // x
        a.append(x)
    else:
        x = x + 1


print(a)