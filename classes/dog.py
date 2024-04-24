from classes.mammal import Mammal
#py imports from wherever this file is we import
class Dog(Mammal):

    def __init__(self, name, rested, is_good=True):
        super().__init__(name=name,rested=rested)
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name}, rested={self.rested}, is_good={self.is_good})"

    def make_sound(self):
        return "generic Dog sound"

    def sleep(self):
        super().sleep()
        print("snore")
        
    def take_a_nap(self):
        super().sleep()
        print("snore")


    def run_around(self):
        super().run_around()
        print("pant")