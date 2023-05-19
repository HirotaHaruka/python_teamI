import sys
args = sys.argv

#引数を変数に代入
plus = int(args[1]) 

sum = 0

while sum <= 100: 
    sum = sum + plus

    if sum == 100:
        print("Jusut 100!") 
        break

else:
    print("Over!")