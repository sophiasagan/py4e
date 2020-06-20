#inside
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)
#outside


Object is a bit of self-contained code and data
Class - a template - general characteristics
method or message - a defined capability of a class
field or attribute - a bit of data in a class
object or instance - a particular instance of a class

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
an = PartyAnimal()

an.party()
an.party()
an.party()

So far 1
So far 2
So far 3

print("Type", type (an))
print("Dir", type(an))

Type <class '_main_.PartyAnimal'>
Dir ['_class_', ... 'party', 'x']

Object Life Cycle


Inheritance
When we make a new class - we can reuse an existing
class and inherit all the capabilities of an existing class
and then add our own little bit to make our new class

Another form of store and reuse
Write once - reuse many times
The new class (child) has all the capabilities of the old class (parent)
 - and then some more

 Subclasses are specialized version of parent classes ex - mammal - animals - dog

 class PartyAnimal:
     x = 0
     name = ""
     def _init_(self, nam):
         self.name = nam
         print(self.name, "constructed")

def party(self) :
    self.x = self.x + 1
    print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
