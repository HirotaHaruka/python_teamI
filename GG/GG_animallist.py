import sys
args = sys.argv

#引数を変数に代入

animallist = ["giraffe", "tiger", "zebra", "elephant", "lion"]

print(animallist)

animallist.insert(int(args[1]), args[2])

del animallist[-1]

animallist.sort()

print(animallist, end="")