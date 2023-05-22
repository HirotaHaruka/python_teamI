# 飼い猫の名前を出力するクラス
import yy_introduce

class IntroFam(yy_introduce.Intro):
    def cat_out(self, cat_name):
        self.cat_name = cat_name
        cattxt = "飼い猫の名前は、" + cat_name + "です。"
        return cattxt