import sys
args = sys.argv

station1 = args[1]
station2 = args[2]

info = {'東京':0.00 ,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}

result = info[station1]-info[station2]

if result < 0:
    result *= -1 

print(format(result, '.2f'), end="")
