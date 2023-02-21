from Graphics.rectangle import*
from Graphics.circle import*
from Graphics.threeDgraphics.cuboid import*
from Graphics.threeDgraphics.sphere import*
l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
print("area of rectangle=",RectArea(l,b))
print("perimeter of rectangle=",RectPerimeter(l,b))

r=int(input("enter the radius of circle:"))
print("area of circle=",CirArea(r))
print("perimeter of circle=",CirPerimeter(r))

l1=int(input("enter the length of cuboid:"))
b1=int(input("enter the breadth of cuboid:"))
h1=int(input("enter the height of cuboid:"))
print("area of cuboid=",area(l1,b1,h1))
print("perimeter of cuboid=",perimeter(l1,b1,h1))


r=int(input("enter the radius of sphere:"))
print("area of sphere=",SpArea(r))
print("perimeter of sphere=",SpPerimeter(r))

