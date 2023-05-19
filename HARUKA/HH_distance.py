import sys
s = sys.argv[1]
f = sys.argv[2]
dic_station = {
    '東京'      : 0.00, 
    '品川'      : 6.78,
    '新横浜'    : 25.54,
    '名古屋'    : 342.02,
    '京都'      : 476.31,
    '新大阪'    : 515.35 
}

dis = dic[s] - dic[f]
if dis < 0: dis *= -1
print(dis, end="")