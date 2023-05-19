import math


class AreaPerimeter:

    @staticmethod
    def triangle():
        side_1 = float(input("Enter the first side \n"))
        side_2 = float(input("Enter the second side\n"))
        side_3 = float(input("Enter the third side\n"))
        semiPerimeter = (side_1+side_2+side_3) / 2
        area = math.sqrt(semiPerimeter* (semiPerimeter - side_1) * (semiPerimeter - side_2) * (semiPerimeter - side_3))
        perimeter = side_1+side_2+side_3
        return area, perimeter

    @staticmethod
    def square():
        side = float(input("Enter the side\n"))
        area = side * side
        perimeter = 4 * side
        return area, perimeter

    @staticmethod
    def rectangle():
        l, b = map(int, input("Enter length and breadth\n").split())
        area = l * b
        perimeter = 2 * (l + b)
        return area, perimeter


def circle():
    radius = float(input("Enter the radius\n"))
    area = 3.14 * (radius * radius)
    perimeter = 2 * 3.14 * radius
    return area, perimeter


name_shape = input("Enter the shape\n1.Circle\n2.Triangle\n3.Square\n4.Rectangle\n")
shape_obj = AreaPerimeter()

while True:
    if name_shape == "1":
        print(circle())
        break
    elif name_shape == "2":
        print(shape_obj.triangle())
        break
    elif name_shape == "3":
        print(shape_obj.square())
        break
    elif name_shape == "4":
        print(shape_obj.rectangle())
        break
    else:
        print("This shape is not supported")
        break
