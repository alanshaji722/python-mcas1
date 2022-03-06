#Alan Shaji
#21MCA002

from graphics import rectangle
from graphics import circle
from graphics.threedpackage.cuboid import *

#*********rectangle********
num1=int(input("enter length of rectangle:"))
num2=int(input("enter breadth of rectangle:"))
res1=rectangle.area(num1,num2)
print("area of rectangle:",res1)
res2=rectangle.perimeter(num1,num2)

print("perimeter of rectangle:",res2)


#*********circle********

rad=int(input("enter radius of circle:"))
res3=circle.area(rad)
print("area of circle:",res3)
res4=circle.perimeter(rad)

print("perimeter of circle:",res4)

#*********cuboid********

l=int(input("enter length of cuboid:"))
b=int(input("enter breadth of cuboid:"))
h=int(input("enter hieght of cuboid:"))

res3=area(l,b,h)
print("area of cuboid:",res3)
res2=perimeter(l,b)
print("perimeter of cuboid:",res2)

#*********sphere********
from graphics.threedpackage.sphere import *
r=int(input("enter radius of sphere"))


res4=area(r)
print("area of sphere:",res4)

res5=perimeter(r)
print("perimeter of sphere:",res5)