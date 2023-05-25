import sys
import os
args = sys.argv
sheep = int(args[1])

with open("../../files/sheep.txt", mode="w", encoding="utf-8") as f:
    
    for i in range(1, sheep+1):
        f.write("ひつじが"+str(i)+"匹")
        continue

