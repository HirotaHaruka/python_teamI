import random
kino = random.randint(5, 30) # ランダムに5~30の整数を表示

if kino >= 15: # 15を境に条件分岐
    print(f'今日は{kino}度です。冷たいお茶を出します。')
else:
    print(f'今日は{kino}度です。熱いお茶を出します。')