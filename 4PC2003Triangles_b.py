

testData=[[3,4,5],[2.3,2.3,2.7],[3.5,3.5,3.5],[2.9,1.5,0.8]]


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

#added 2 sides
#added in float before input
#removed inputs
for l in testData:
    if isATriangle(testData[0],testData[1],testData[2]) ==True:
        print("These sides form a valid triangle")
        trianlge_type(testData[0],testData[1],testData[2])
    else:
        print("These sides dont form a valid triangle")
#edited code to test values from a list
#did not know how to seperate lists from lists within lists