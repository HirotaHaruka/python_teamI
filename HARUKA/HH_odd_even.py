import sys

num = [int(i) for i in sys.argv[1:]]

for i in num:
    if i % 2 == 0:
        print(f'{i}は偶数')
    else:
        print(f'{i}は奇数')