import sys
args = sys.argv

#引数を変数に代入

population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

i = int(args[1])

print(population[i-1], end="")