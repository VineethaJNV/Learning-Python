#Showing essential features, showing only output

#Abstract classes are used

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Lion roars")

class Cow(Animal):
    def make_sound(self):
        print("Moo ")


l = Lion()
l.make_sound()

c = Cow()
c.make_sound()
    