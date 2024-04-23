# GH 2003 triangles
# Student No (or name): ____________
def tri_check(sideA,sideB,sideC):
    is_triangle=False
    if sideA+sideB>sideC and sideA+sideC>sideB and sideB+sideC>sideA:
        is_triangle=True
        print ("Is a triangle")
    else:
            print("Not a triangle")
    if is_triangle==True:
        #This only checks the type of triangle we are given if it is proven to form a triangle
        tri_type(sideA, sideB, sideC)
            
def tri_type(sideA, sideB,sideC):
    if sideA==sideB and sideC:
        print("This is equilateral")
    elif sideA==sideB and sideA!=sideC or sideA==sideC and sideA != sideB or sideB==sideC and sideB != sideA:
        print("Is an isosceles triangle")
    elif sideA!=sideB or sideC and sideB!=sideC:
        print("Is a scalene triangle")
        right_angle_check(sideA, sideB, sideC)
    
def right_angle_check(sideA,sideB,sideC):
    #a squared+b squared= c squared
    if sideA*sideA + sideB*sideB ==sideC*sideC:
        print("Is a right angle triangle")
    else:
        print("Is not a right angle triangle")
        
     

print("Enter the lengths of each line")
#asking for side values
sideA = float(input("Enter side A:"))
sideB = float(input("Enter side B:"))
sideC = float(input("Enter side C:"))
tri_check(sideA, sideB, sideC)




