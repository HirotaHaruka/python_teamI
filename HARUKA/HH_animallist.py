import sys
num, animal = int(sys.argv[1]), str(sys.argv[2])

l = ["giraff", "tiger", "zebra", "elephant", "lion"]

l.insert(num, animal)
l = l[:-1]
l.sort()

print(l,end='')


