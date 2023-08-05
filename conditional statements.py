def checkArea(Area):
    if Area >= 10:
        print("Area is bigger than 10")
    elif 0 < Area < 10:
        print("Smaller than 10")
    else:
        print("Invalid")

Radius = int(input("Enter radius: "))
def circleArea(Radius):
    Area = 3.14 * (Radius ** 2)
    print("Area=", Area)
    checkArea(Area)
    return Area

circleArea(Radius)

Side = int(input("Enter side: "))

def squareArea(Side):
    Area = (Side ** 2)
    print("Area=", Area)
    checkArea(Area)

squareArea(Side)

Height = int(input("Enter height: "))
Base = int(input("Enter base: "))

def TriangleArea(Height, Base):
    Area = 0.5 * Height * Base
    print("Area= ", Area)
    checkArea(Area)

TriangleArea(Height, Base)
