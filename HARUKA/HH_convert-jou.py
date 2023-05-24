def convert_jou(jou, unit="江戸間"):
    if unit == "江戸間":
        base = 0.88 * 1.76
    elif unit == "京間":
        base = 0.955 * 1.91
    elif unit == "中京間":
        base = 0.91 * 1.82
    m2 = jou * base
    s = f"{unit}で{jou}畳は{m2}㎡"
    print(s)
    

convert_jou(6, "江戸間")
convert_jou(6, "京間")
convert_jou(6)