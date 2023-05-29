# 入力 : ランキング順位
# 表示 : 入力順位の人口の多い国
import sys
rank_num = int(sys.argv[1])
cou =  ["China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]

print(cou[rank_num - 1], end="")