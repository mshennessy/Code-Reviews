# GH 2003 triangles
# Student No (or name): 


print("Enter the lengths of each line")

#user inputs
side1 = float(input("Enter side 1:"))
#part i & iii
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))



#part ii & iv
#triangle valid function
def isATriangle(a,b,c):
    #ensuring triangle is valid
    if ((a+b) > c) and ((a+c) > b) and ((b+c) > a):
        #triangle valid
        return True
    
    else:
        #traingle NOT valid
        return False
        
#triangletype function
#part v & vi
def triangleType(a,b,c):
    #equalaterial triangle
    if (a == b) and (b == c) and (a == c):
        print('This triangle is an equalaterial triangle')
    #triangle isoselces
    elif (a == b) or (b == c) or (a == c):
        
        print('This triangle is an isosceles triangle')
    else:
        #part vi
        #triangle scalene or not
        print('This triangle is a scalene triangle')
        #sqauring both and comparing
        rightTri1 = a**2 + b**2
        rightTri2 = c**2
        #check if right angled or not
        if rightTri1 == rightTri2:
            print('This triangle is a Right-Angled triangle')
        
        
#part iv
triangle = isATriangle(side1,side2,side3)
#if the triangle is valid
if triangle == True:
    
    print('These sides can form a valid triangle')
    #part v
    typeTri = triangleType(side1,side2,side3)
    
    
#if triangle not valid
else:
    #part iii
    print('Not a triangle')    
