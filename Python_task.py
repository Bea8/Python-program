import math

#Triangle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height)/2



#Square
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2



#Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



#Ellipse
class Ellipse:
    def __init__(self, majAxis, minAxis):
        self.majAxis = majAxis
        self.minAxis = minAxis

    def area(self):
        return math.pi * self.majAxis * self.minAxis



#Cube
class Cube:
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * (self.edge ** 2)

    def volume(self):
        return self.edge ** 3



#Pyramid
class Pyramid:
    def __init__(self, baseArea, sideArea, height):
        self.baseArea = baseArea
        self.sideArea = sideArea
        self.height = height

    def area(self):
        return self.baseArea + self.sideArea

    def volume(self):
        return(self.baseArea * self.height)/3


#Calculations based on user input
print("Triangle --- 1")
print("Square ---- 2")
print("Rectangle ---- 3")
print("Ellipse ---- 4")
print("Cube ---- 5")
print("Pyramid ---- 6")

choice = raw_input("Calculate areas and volumes. Choose from the menu above: ")


if choice == "1":
    a = int(input("Enter base of triangle: "))
    b = int(input("Enter height of triangle: "))
    obj = Triangle(a, b)
    print("The area of the triangle is: " + str(obj.area()))
elif choice == "2":
    a = int(input("Enter length of square's side: "))
    obj = Square(a)
    print("The area of the square is: " + str(obj.area()))
elif choice == "3":
    a = int(input("Enter width of rectangle: "))
    b = int(input("Enter height of rectangle: "))
    obj = Rectangle(a, b)
    print("The area of the rectangle is: " + str(obj.area()))
elif choice == "4":
    a = int(input("Enter length of the major axis: "))
    b = int(input("Enter length of the minor axis: "))
    obj = Ellipse(a, b)
    print("The area of the ellipse is: " + str(obj.area()))
elif choice == "5":
    a = int(input("Enter length of cube's edge: "))
    obj = Cube(a)
    print("The area of the cube is: " + str(obj.area()) + " and the volume of the cube is: " + str(obj.volume()))
elif choice == "6":
    a = int(input("Enter base area of pyramid: "))
    b = int(input("Enter side area of pyramid: "))
    c = int(input("Enter height of pyramid: "))
    obj = Pyramid(a, b, c)
    print("The area of the pyramid is: " + str(obj.area()) + " and the volume of the pyramid is: " + str(obj.volume()))
