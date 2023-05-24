# QRコードの出力
import os
import qrcode
import sys

args = sys.argv

# コマンドライン入力の受け取り
qr_url = args[1]
file_name = args[2]

# QRコードの保存先のパス
path = os.path.join("..", "..", "files", file_name)

# QRコードを生成
img = qrcode.make(qr_url)

img.save(path + ".png")