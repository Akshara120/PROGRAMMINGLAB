'''#11. Write lambda functions to find area of square, rectangle and triangle.
l= int(input("Enter the length of rectangle:"))
b= int(input("Enter the breadth of rectangle:"))
are = lambda x,y:x*y
print("Area of Rectangle:",are(l,b))

h= int(input("Enter the height of Trinagle:"))
b2= int(input("Enter the breadth of Trinangle:"))
art = lambda x,y:.5*x*y
print("Area of Triangle:",art(b,h))

a= int(input("Enter length of square:"))
sqar = lambda x:x*x
print("Area of Square:",sqar(a))'''

#11. Write lambda functions to find area of square, rectangle and triangle
l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breath of the rectangle:"))
h=int(input("enter height of the triangle:"))
ar=lambda x,y: x*y
asq=lambda x: x*x
at=lambda x,y:0.5*x*y
print("area of rectangle:",ar(l,b))
print("area of square:",asq(l))
print("area of triangle:",at(b,h))