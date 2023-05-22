class intro():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def name_out(self):
        nametxt = f"私の名前は{self.name}です。"
        return nametxt
    
    def age_out(self):
        agetxt = f"私の年は{self.age}です。"
        return agetxt
    