import sys

args = sys.argv

animalist = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animal_index = int(args[1])
animal_name = args[2]

animalist.insert(animal_index, animal_name)

del animalist[-1]
animalist.sort()

print(animalist, end="")