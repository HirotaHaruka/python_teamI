import sys
args = sys.argv

char = str(args[1])
i = int(args[2])

char = char.split()

print(char[i-1], end="")