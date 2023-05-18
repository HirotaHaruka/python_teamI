import random
n = random.randint(5, 30)
kion = n
if kion >= 15:
    print(f'今日は{n}度です。冷たいお茶を出します。')
else:
    print(f'今日は{n}度です。熱いお茶を出します。')