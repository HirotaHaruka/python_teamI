import os
import qrcode

path = os.path.join("..", "..", "files", "mynavi-qrcode.png") #pathの生成

#QRコードを生成する
img = qrcode.make("https://www.mynavi.jp/")
#画像を保存
img.save(path)