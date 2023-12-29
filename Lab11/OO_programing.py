

class Dog:
    species = "Canis familiares"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    #Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound='Arf'):
        return super().speak(sound) #Very important "super()"!!


# d1 = Dog('REx', 4)
# print(d1.speak("Houhou hou"))
#
# miles = JackRussellTerrier('Miles', 4)
#
# print(miles.speak())

###################################

class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
    def __str__(self):
        return "Color: R={0:d}, G={1:d}, B={2:d}".format (self._red,
                                                  self._green, self._blue)


c = Color(15, 35, 3)
print(c)

### Encapsulation !!!:
"""
Using OOP in Python, we can restrict access to methods 
and variables. This prevents data from direct modification 
which is called encapsulation. In Python, we denote private 
attributes using underscore as the prefix i.e single _ or double __.
"""

class Computer:
    "This's a computer class"
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()

print(c.__doc__)

#####################################

# INHERITANCE:
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+ str(i+1)+":")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3) # We can write down here: super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)

# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

# MULTIPLE INHERITANCE


# Operator-OVERLOADING

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2)