# GH 2003 triangles b
# Student No (or name):


#test data
testData=[[3,4,5],[2.3,2.3,2.7],[3.5,3.5,3.5],[2.9,1.5,0.8]]
#func to check triangles
def isATriangle(a,b,c):
    if ((a+b) > c) and ((a+c) > b) and ((b+c) > a):
        #return true or false
        return True

    else:
        return False
    
#triangletype function
def triangleType(a,b,c):
    #equalaterial
    if (a == b) and (b == c) and (a == c):
        print('This triangle is an equalaterial triangle')
    #isoceles
    elif (a == b) or (b == c) or (a == c):
        print('This triangle is an isosceles triangle')
    #scalene
    else:
        print('This triangle is a scalene triangle')
        rightTri1 = a**2 + b**2
        rightTri2 = c**2
        if rightTri1 == rightTri2:
            print('This triangle is a right Angled triangle')




#for loop to test all data
for i in range(len(testData)):
    #assigning values for data
    tester = testData[i]
    test1 = tester[0]
    test2 = tester[1]
    test3 = tester[2]
                        
    #running function if is a triangle
    triangle = isATriangle(test1,test2,test3)
    
    if triangle == True:
        # valid triangle
        print('These sides can form a valid triangle')
        typeTri = triangleType(test1,test2,test3)
        print('')
        print(f"Testing sides {tester}")
        

    else:
        #not valid
        print('Not a triangle') 
    
        
    


#triangle valid function
 