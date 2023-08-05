raduis=int(input("Enter raduis"))
def circleArea(Raduis):
    Area =  3.14*(Raduis**2)
    print( "Area=",Area)
    if Area >= 10:
        print("Area is big")
    elif Area >0 & Area <10:
        print("small")
    else:
        print("invalid")
   # print(Condition(Area))
print(circleArea(raduis))
side=int(input("Enter side"))
def squareArea (Side):
  Area =(Side ** 2)
  print(  "Area=", Area)
  if Area >=10 :
   print("Area is big")
  elif Area>0 & Area<10 :
    print("small")
  else:
    print("invalid")
 # print(Condition(Area))
print(squareArea(side))
Height=int(input("Enter height"))
Base=int(input("Enter base"))

def TriangleArea(Height,Base):
  Area= 0.5 * Height * Base
  print( "Area= ",Area)
 # print(Condition(Area))
  if Area >= 10:
    print("Area is big")
  elif Area > 0 & Area < 10:
    print("small")
  else:
    print("invalid")

print(TriangleArea(Height,Base))

def Condition (Area):
    if Area>=10 :
        print("Area is big")
    elif Area>0 & Area<10 :
        print("small")
    else:
        print("invalid")