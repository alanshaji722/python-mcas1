#Alan Shaji
#21MCA002

x=int(input("enter the length of the square : "))
square = lambda x: x ** 2
print("square: ",square(x))
l=int(input("enter the length of the rectangle: "))
b=int(input("enter the breadth of the rectangle: "))
area = lambda l,b : l * b
print("area of the rectangle: ",area(l,b))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
t = lambda b,h : 0.5 * l * b
print("area of triangle : ",t(b,h))
