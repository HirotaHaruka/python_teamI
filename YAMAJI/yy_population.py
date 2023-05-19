# 引数のインデックスの要素を出力
import sys
args = sys.argv

# 順位の受け取り
idx_ranking = int(args[1])

population_ranking_list = ("China", "India", "U.S.A", "Indonesia", 
                           "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(population_ranking_list[idx_ranking - 1], end="")