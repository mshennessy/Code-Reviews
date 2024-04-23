# GH 2003 triangles b
# Student No (or name): 

def isATriangle(a,b,c):
    if a + b > c and b + c > a and a + c > b:
        #if sides are part of a triangle return boolean value True
        return True
    else:
        #if sides are not part of a triangle return boolean value False
        return False

def isRightAngle(sideA,sideB,sideC):
    #checking if a^2 + b^2 = c^2
    if sideA**2 + sideB**2 == sideC**2 or sideB**2 + sideC**2 == sideA**2 or sideA**2 +sideC**2 == sideB**2:
        print("And it is a Right Angled Triangle\n")

def triangleType(a,b,c):
    if a == b == c:
        #if all sides are equal
        print("This is an equilateral triangle\n")
    elif a == b or a == c or b == c:
        #if two of the sides are equal
        print("This is an isosceles triangle\n")
    else:
        #if none of the sides are equal
        print("This is a scalene triangle")
        #checking if the scalene triangle is right angled
        isRightAngle(a,b,c)


testData=[[3,4,5],[2.3,2.3,2.7],[3.5,3.5,3.5],[2.9,1.5,0.8]]

# taking each list out of testData and testing if they are triangles

for i in testData:
    print(f'Testing sides {i}')
    side1 = i[0]
    side2 = i[1]
    side3 = i[2]

    if isATriangle(side1, side2, side3):
        print("These sides form a valid triangle")
        #getting the triangle type
        triangleType(side1, side2, side3)
    else:
        #if sides 1 and 2 are not greater than side 3 or side 2 and 3 are not greater than side 1 or side 1 and 3 are not greater than side 2
        print("Not a triangle\n")

