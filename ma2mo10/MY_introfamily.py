import MY_introduce

class IntroFam(MY_introduce.Intro):
    def __init__(self, name, age, cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name

    def cat_out(self):
        cat_name_txt = "飼い猫の名前は、" + self.cat_name + "です"
        return cat_name_txt