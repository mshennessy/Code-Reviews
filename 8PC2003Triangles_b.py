# GH 2003 triangles b
# Student No (or name): 
def trianglefunction(list):
    #definning the function
    a = list[0]
    b = list[1]
    c = list[2]
    #appending the values from the list to values for calculations 
    print("testing sides ", list)
    if  a + b > c or a + c > b or b + c > a:
     print("These sides can form a vaild triangle ")
     #checks to see if the triangle is a triangle
    else:
     print("Not a triangle")
     #if not a triangle then prints that it isnt 
    
#checking to see what type if triangle it is 
    if a == b and b == c:
        print("This is an isosceles triangle")
        
    elif a == b or a == c or b == c :
        print("this is an Isosceles triangle")
    elif a != b and b != c:
        print("This is a scalene triangle")
        #using a pythagras' formula to see if it is a right angled triangle 
        rightanglecheck = (a*a + b*b )
       # print(rightanglecheck)
        #print(c*c)
        if rightanglecheck == c*c:
            print("And it is triangle is right-angled")
       
testData=[[3,4,5],[2.3,2.3,2.7],[3.5,3.5,3.5],[2.9,1.5,0.8]]
#the test data 

test1 = testData[0]
test2 = testData[1]
test3 = testData[2]
test4 = testData[3]
#putting all of the data from test data into seperate values so the can be called individualy 
trianglefunction(test1)
print("")
print("")
trianglefunction(test2)
print("")
print("")
trianglefunction(test3)
print("")
print("")
trianglefunction(test4)
#calling the function to test the data 







