import sys
num = int(sys.argv[1])
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')
    
print('偶数' if num % 2 == 0 else '奇数' , end="")