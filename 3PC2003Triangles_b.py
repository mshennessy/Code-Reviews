# GH 2003 triangles b
# Student No (or name):

testData=[[3,4,5],[2.3,2.3,2.7],[3.5,3.5,3.5],[2.9,1.5,0.8]]
#function to test what kind of triangle        
def triangleType(a,b,c):
   if a + b > c and b + c >a and a + c >b:
       #tests if triangle is equilateral
    print("These sides form a valid triangle")
    if a+b+c == a*3:
        print("Equilateral")
        #tests if triangle is isocelles
    elif a+b == a*2 or b+c == b*2 or a+c == c*2:
        print("Isocelles")
        #test if the triangle is a right angle
    else:
        print("Scalene")
        if a*a + b*b == c*c:
            print("Right angle triangle")
   else:
        print("These sides don't form a valid triangle")
#You choose which list to review            
testdata = int(input("Pick list 0,1,2,3"))
print("Testing list",testData[testdata])
#retreives values from said list
side1 = float(testData[testdata].pop(0))
side2 = float(testData[testdata].pop(0))
side3 = float(testData[testdata].pop(0))
#part (v)
triangleType(side1,side2,side3)


    
    

