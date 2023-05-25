import MY_display_item as MYdisp

def main():
    #商品リストを定義
    item_dict = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
    #商品リストを表示
    item_name = MYdisp.display_item(item_dict)

    #item_nameが空ならcancelされたので終了
    if item_name == []:
        return 
        


if __name__ == "__main__":
    main()