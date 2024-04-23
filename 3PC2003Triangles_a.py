# GH 2003 triangles
# Student No (or name): 

    #part (iv)
#function to return boolean value
#def isATriangle(a,b,c):
    #if a + b > c and b + c >a and a + c >b:
        #print("True")
    #else:
        #print("False")
    #part(v)
# function to test kind of triangle it is
#def triangleType(a,b,c):
   # if a + b > c and b + c >a and a + c >b:
       # print("These sides form a valid triangle")
       # if a+b+c == a*3:
       #     print("Equilateral")
      #  elif a+b == a*2 or b+c == b*2 or a+c == c*2:
         #   print("Isocelles")
      #  else:
           # print("Scalene")
   # else:
     #   print("These sides don't form a valid triangle")
#function to test if triangle is right angle
def findScalene(a,b,c):
    if a + b > c and b + c >a and a + c >b and a != b or c and b!= c:
        print("Scalene")
        if a*a + b*b == c*c:
            print("Right angle triangle")
    
#inputs of values of sides    
print("Enter the lengths of each line")
    #part (i)
side1 = float(input("Enter side 1:"))
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))
    #part(ii),(iii)
#tests if triangle is valid
if side1 + side2 > side3 and side2 + side3 >side1 and side1 + side3 >side2:
   print("These sides can form a valid triangle")
else:
   print("These sides cannot form a valid triangle")

#part (iv)
#isATriangle(side1,side2,side3)
#part (v)
#triangleType(side1,side2,side3)
# part (vi)
findScalene(side1,side2,side3)

