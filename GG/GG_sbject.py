import sys
args = sys.argv

#引数を変数に代入
ma = int(args[1])
jp = int(args[2])
en = int(args[3])

sum = ma + jp + en

if (ma >= 70 and jp >=70 and en >=70)or(sum >= 220)and(ma >= 50 and jp >= 50 and en >= 50):
    print("合格", end="")
else:
    print("不合格", end="")