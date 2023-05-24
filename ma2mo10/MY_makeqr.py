import os
import qrcode

path = os.path.join("..", "..", "files", "mynavi-qrcode.png") #pathの生成

img = qrcode.make("https://www.mynavi.jp/")
img.save(path)