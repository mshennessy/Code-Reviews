# GH 2003 triangles
# Student No (or name): 
#function for checking if its a triangle
def isATriangle(a,b,c):
    if a+b > c:
        return True
    elif a+c > b:
        return True
    elif b+c > a:
        return True
    else:
        return False
#function for checking triangle
def trianlge_type(a,b,c):
    if a==b and b==c:
        print("these form a equilateral triangle")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("these form a isosceles")
    else:
        print("These form a scalene")
        scalene(a,b,c)
#func for checking if its right angled  
def scalene(a,b,c):
    if a**2+b**2==c**2:
        print("triangle is right angled")
    elif a**2+c**2==b**2:
        print("triangle is right angled")
    elif c**2+b**2==a**2:
        print("triangle is right angled")
    else:
        print("triangle is not right angled")

print("Enter the lengths of each line")
side1 = float(input("Enter side 1:"))
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))
#added 2 sides
#added in float before input
if isATriangle(side1,side2,side3) ==True:
    print("These sides form a valid triangle")
    trianlge_type(side1,side2,side3)
else:
    print("These sides dont form a valid triangle")