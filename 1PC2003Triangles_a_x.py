# GH 2003 triangles
# Student No (or name): 

#(iv)
def isATriangle(a,b,c):
    if a + b > c and b + c > a and a + c > b:
        #if sides are part of a triangle return boolean value True
        return True
    else:
        #if sides are not part of a triangle return boolean value False
        return False

#(vi)
def isRightAngle(sideA,sideB,sideC):
    #checking if a^2 + b^2 = c^2
    if sideA**2 + sideB**2 == sideC**2 or sideB**2 + sideC**2 == sideA**2 or sideA**2 +sideC**2 == sideB**2:
        print("This triangle is right-angled")

#(v)
def triangleType(a,b,c):
    if a == b == c:
        #if all sides are equal
        print("This is an equilateral triangle")
    elif a == b or a == c or b == c:
        #if two of the sides are equal
        print("This is an isosceles triangle")
    else:
        #if none of the sides are equal
        print("This is a scalene triangle")
        #checking if the scalene triangle is right angled
        isRightAngle(a,b,c)



print("Enter the lengths of each line")
#all inputs turned into floats so user can enter numbers between whole numbers
#(iii)
side1 = float(input("Enter side 1:"))
#(i)
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))

#(ii)
#same as isATriangle function just not a function
'''
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("These sides form a valid triangle")
else:
    print("Not a triangle")
'''

if isATriangle(side1, side2, side3):
    print("These sides form a valid triangle")
    #getting the triangle type by sending the values for the sides into the function
    triangleType(side1, side2, side3)
else:
    #if sides 1 and 2 are not greater than side 3 or side 2 and 3 are not greater than side 1 or side 1 and 3 are not greater than side 2
    print("Not a triangle")
