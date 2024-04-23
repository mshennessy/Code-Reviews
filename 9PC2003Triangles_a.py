# GH 2003 triangles
# Student No (or name): 

def isATriangle(a,b,c): #(iv) start
    if a + b > c:
        print("These sides can form a valid triangle")
    elif a + c > b:
        print("These sides can form a valid triangle")
    elif b + c > a:
        print("These sides can form a valid triangle") #(iv) end

print("Enter the lengths of each line")
side1 = input("Enter side 1:")
side2 = input("Enter side 2:")#(i)
side3 = input("Enter side 3:")#(i)

if side1 + side2 > side3:#(ii) start
    print("These sides can form a valid traingle")
elif side1 + side3 > side2:
    print("These sides can form a valid traingle")
elif side2 + side3 > side1:
    print("These sides can form a valid traingle") #(ii) end
