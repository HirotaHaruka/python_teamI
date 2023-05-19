# 3教科の点数から合否を判定する
import sys
args = sys.argv

score_math = int(args[1])
score_jp = int(args[2])
score_en = int(args[3])

# 1科目も50点未満がない
if score_math >= 50 and score_jp >= 50 and score_en >= 50:
    # 3教科とも70点以上
    if score_math >= 70 and score_jp >= 70 and score_en >= 70:
        print("合格", end="")
    #　合計点数が220点以上 
    elif score_math + score_jp + score_en >= 220:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")