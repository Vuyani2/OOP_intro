class Shapes :
    def __init__(self,type , name,size, side):
        self.type = type
        self.name = name
        self.size = size
        self.side = side


    def area(self):
        print("I am a : "+self.type + "\n" +
              "I am a : " + self.name +"\n"+
              "My size is : " + self.size + "\n"+
              "My Side is : "+ self.side)
obj_shape = Shapes("Circle", "Coin", "5cm","4")
obj_shape.area()

class Circle(Shapes):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        Area_circle = 3.14*(self.radius)**2
        return Area_circle
obj_coin= Circle(5)
print(obj_coin.area())

#Area of a triangle
class Triangle(Shapes):
    def __init__(self, height, base):
        self.height= height
        self.base=base

    def area(self):
        Area_Triangle = 0.5*(self.base*self.height)
        return Area_Triangle

Obj_Pyramid = Triangle(5,4)
print(Obj_Pyramid.area())

#Area of a Rectangle
class Rect(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        Area_Rect = self.length*self.width
        return Area_Rect
obj_laptop = Rect(4, 5)
print(obj_laptop.area())

#Area of a Square
class Square(Shapes):
    def __init__(self, side):
        self.side = side
    def area(self):
        Area_Square = self.side**2
        return Area_Square
Obj_Cube = Square(5)
print(Obj_Cube.area())
