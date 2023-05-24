import sys
import introduce
args = sys.argv

intr = introduce.intro('廣田遼', '25')
print(intr.name_out())
print(intr.age_out())

class AddCatName(introduce.intro):
    def __init__(self, name, age, catname):
        super().__init__(name, age)
        self.catname = catname
    def cat_out(self):
        cattxt = f'飼い猫の名前は{self.catname}です。'
        return cattxt

intr2 = AddCatName('廣田遼', '25', 'ミケ')
print(intr2.name_out())
print(intr2.age_out())
print(intr2.cat_out())

