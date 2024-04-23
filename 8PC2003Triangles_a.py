# GH 2003 triangles
# Student No (or name):
def isATriangle(a,b,c):
    #defining the function to be called 
    if  a + b > c or a + c > b or b + c > a:
     print("These sides can form a vaild triangle ")
     #checks to see if the inputs can form a triangle
     return True
    #returns a Boolean if true
    else:
     print("Not a triangle")
     return False
    # if the numbers cannot make a triangle then returns false
    #returns a boolean 

def checkingtype(a,b,c):
    if a == b and b == c:
        #checking what type of triangle the data makes 
        print("This is an isosceles triangle")
    elif a == b or a == c or b == c :
        print("this is an Isosceles triangle")
    elif a != b and b != c:
        print("This is a scalene triangle")
        rightanglecheck = (a*a + b*b )
       #applying the pythagras formula 
        if rightanglecheck == c*c:
            print("This triangle is right-angled")
            #checks if a right angled triangle 
       
    

print("Enter the lengths of each line")

side1 = float(input("Enter side 1:"))
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))
#user inputs for the sides of the triangles 
isATriangle(side1, side2, side3)
checkingtype(side1, side2, side3)
#calling the functions defined earlier and useing the user's inputed data 
#if  side1 + side2 > side3 or side1 + side3 > side2 or side2 + side3 > side1: