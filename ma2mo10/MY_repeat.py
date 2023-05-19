import sys

args = sys.argv
input = int(args[1])    #入力値
sum = 0                 #合計値

#繰り返し足し算
while sum < 100: sum = sum + input

#100ちょうどなら"Just 100!"、超えていれば"Over!"を表示
if sum == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")