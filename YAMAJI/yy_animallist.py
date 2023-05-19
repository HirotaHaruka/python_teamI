# リストの挿入、削除、並び替え
import sys
args = sys.argv

# 動物名の受け取り
idx_delete_animal = int(args[1])
input_animal = args[2]

animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animal_list.insert(idx_delete_animal, input_animal)
animal_list.pop()
animal_list.sort()

print(animal_list, end="")