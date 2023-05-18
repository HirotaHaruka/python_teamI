# カラットからグラムに返還する
# 返還もとになる値
per_ct = 0.2
# ユーザから入力を得る
user = float(input("何カラットですか？"))
# user = input("何カラットですか？")
g = user * per_ct
# 結果を表示
print(f"{user}カラット = {g}グラム")
