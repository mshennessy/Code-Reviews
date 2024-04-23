# GH 2003 triangles b
# Student No (or name): ______________

testData=[[3,4,5],[2.3,2.3,2.7],[3.5,3.5,3.5],[2.9,1.5,0.8]]
def isATriangle(side1,side2,side3,triangle):
    if side1+side2 >= side3 and side1+side3 >= side2 and side2+side3 >= side1:
        print("These sides can form a valid triangle")
        triangle = True
    else:
        print("Not a triangle")
        triangle = False
        return
def triangleType(side1,side2,side3,triType):
    if side1 == side2 and side2 == side3:
        triType = Equilateral
        print("This is an Equilateral triangle")
    elif side1 == side2 or side2 ==side3 or side1 == side3:
        print("This is an isosceles triangle")
    else:
        triType = scalene
        print("This is a scalene triangle")

def triangleType(side1,side2,side3,triType):
    if side1 == side2 and side2 == side3:
        triType = Equilateral
        print("This is an Equilateral triangle")
    elif side1 == side2 or side2 ==side3 or side1 == side3:
        print("This is an isosceles triangle")
    else:
        triType = scalene
        print("This is a scalene triangle")
        
print("Testing sides",testData[0])
isATriangle(side1,side2,side3,triangle)
if triangle == True:
    triangleType(side1,side2,side3,)
elif triType == scalene:
    rightAngleCheck(side1,side2,side3)
    
print("Testing sides",testData[1])
isATriangle(side1,side2,side3,triangle)
if triangle == True:
    triangleType(side1,side2,side3,)
elif triType == scalene:
    rightAngleCheck(side1,side2,side3)
    
print("Testing sides",testData[2])
isATriangle(side1,side2,side3,triangle)
if triangle == True:
    triangleType(side1,side2,side3,)
elif triType == scalene:
    rightAngleCheck(side1,side2,side3)
    
print("Testing sides",testData[3])
isATriangle(side1,side2,side3,triangle)
if triangle == True:
    triangleType(side1,side2,side3,)
elif triType == scalene:
    rightAngleCheck(side1,side2,side3)


