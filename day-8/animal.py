class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound


class Dog(Animal):
    def __init__(self,name,sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"{self.name} makes a {self.sound}.")

class Cat(Animal):
    def __init__(self,name,sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"{self.name} makes a {self.sound}.")

class Dog_override(Animal):
    def __init__(self,name,sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"{self.name} barks loudly!")        


d1 = Dog("Buddy", "barks")  
d1.make_sound()  

c1 = Cat("Whiskers", "meows")
c1.make_sound()

d2 = Dog_override("Rex", "barks")
d2.make_sound()

for x in (d1,c1):
    x.make_sound()