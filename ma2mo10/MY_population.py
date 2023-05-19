import sys

args = sys.argv
country_index = int(args[1])
country_taple = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(country_taple[country_index-1], end="")