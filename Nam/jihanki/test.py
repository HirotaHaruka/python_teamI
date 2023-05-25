#商品の定義
product = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

# #商品を出力＆投入金額入力を貰う
# for key, value in product.items(): 
#     print(key+":"+str(value)+"円")
# entry_money = int(input("投入金額を入力してください"))

for i in range(len(product)-1):
    print(product[i])