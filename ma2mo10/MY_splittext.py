import sys

args = sys.argv
text = args[1]                #文章
word_num = int(args[2])       #何番目か

#空白文字で分割
text_list = text.split()

print(text_list[word_num-1], end="")