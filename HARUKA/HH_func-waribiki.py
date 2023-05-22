def calcValue(who, hour, count, value):
    """あるスーパーの割引きを計算する関数"""
    info = "割引なし"
    # 14時に商品を3つ以上で1割引
    if (hour == 14) and (count >= 3):
        value *= 0.9
    # 15時に商品を5つ以上で2割引
    elif (hour == 15) and (count >= 5):
        value *= 0.8
        info = "2割引"
    # 結果を表示
    value = int(value)
    print(f"{who}さんは{info}={value}")

calcValue("A", 15, 3, 1200)
calcValue("B", 14, 5, 2000)
calcValue("C", 15, 8, 5400)
help(calcValue)