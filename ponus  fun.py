
raduis=int(input("Enter raduis"))
def squareAreaAndPerimeter(raduis):
    Perimeter=2*3.14*raduis
    Area= 2*3.14*raduis*raduis
    return print("perimeter:",Perimeter,", Area:",Area)

(squareAreaAndPerimeter(raduis))
print('****************************')
height=int(input("Enter height"))
base=int(input("Enter base"))
hypo=int(input("Enter hypo"))

def TriangleAreaAndPerimeter(height,base,hypo):
 Perimeter=base+height+hypo
 Area= 0.5*height*base
 return print("perimeter:",Perimeter,", Area:",Area)



(TriangleAreaAndPerimeter(height,base,hypo))
