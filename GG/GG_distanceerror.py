import sys
args = sys.argv

#引数を変数に代入
list = {'東京': 0.00,'品川': 6.78,'新横浜': 25.54,'名古屋': 342.02,'京都': 476.31,'新大阪': 515.35}

start = str(args[1])
goal = str(args[2])


try:
    list[start]

    if list[start] > list[goal]:
        distance = list[start] - list[goal]
        print(format(distance, '.2f'), end="")

    else:
        distance = list[goal] - list[start]
        print(format(distance, '.2f'), end="")
except KeyError:
    print("のぞみの停車駅を引数に設定してください")