import qrcode
import os

#os.path.joinを利用して相対パスを生成する
#相対パス(..../files/path.png)となる
path = os.path.join("..", "..", "files", "path.png")

img = qrcode.make("https://student.redesigner.jp/students/da6e22a8d96e5ba279290990284817b8")

#pngファイルの作成
img.save(path)