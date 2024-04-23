# GH 2003 triangles
# Student No (or name): _____________

#asks user to input three sides
#assigns each side to a variable
print("Enter the lengths of each line")
side1 = float(input("Enter side 1:"))
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))
triangle = True
#triType = nothing
#defines function and inputs parameters
#checks if it is a triangle
#prints yes if it is
#no if its not
#sets triangle to true if it is and false if its not
#returns values
def isATriangle(side1,side2,side3,triangle):
    if side1+side2 >= side3 and side1+side3 >= side2 and side2+side3 >= side1:
        print("These sides can form a valid triangle")
        triangle = True
    else:
        print("Not a triangle")
        triangle = False
        return
    
def triangleType(side1,side2,side3,):
    if side1 == side2 and side2 == side3:
        triType = Equilateral
        print("This is an Equilateral triangle")
    elif side1 == side2 or side2 ==side3 or side1 == side3:
        print("This is an isosceles triangle")
    else:
        #triType = scalene
        print("This is a scalene triangle")
        
def triangleType(side1,side2,side3):
    if side1 == side2 and side2 == side3:
        triType = Equilateral
        print("This is an Equilateral triangle")
    elif side1 == side2 or side2 ==side3 or side1 == side3:
        print("This is an isosceles triangle")
    else:
        #triType = scalene
        print("This is a scalene triangle")
        
    


#calls and prints the outcome of the function
isATriangle(side1,side2,side3,triangle)
if triangle == True:
    triangleType(side1,side2,side3)
elif triType == scalene:
    rightAngleCheck(side1,side2,side3)
    


    

