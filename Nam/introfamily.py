import introduce

class IntroFam(introduce.Intro):
    def __init__(self, name, age, catN):
        super().__init__(name, age)
        self.cat = catN

    def cat_out(self):
        nametxt = "飼い猫の名前は" + self.cat + "です"
        return nametxt