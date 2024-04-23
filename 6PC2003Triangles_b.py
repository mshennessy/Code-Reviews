# GH 2003 triangles b
# Student No (or name):

testData=[[3,4,5],[2.3,2.3,2.7],[3.5,3.5,3.5],[2.9,1.5,0.8]]

# GH 2003 triangles
# Student No (or name): Cillian Whalley

side_list = []
counter = 0

#checks if triangle can be valid and returns value
def side_checker(side_list):
    if (side_list[0]+side_list[1]) > side_list[2] and (side_list[0]+side_list[2]) > side_list[1] and (side_list[2]+side_list[1]) > side_list[0] :
        print("These sides can form a valid triangle")
        valid_triangle = True
    else:
        print("These sides cannot form a valid triangle")
        valid_triangle = False
    return valid_triangle

#compares sides from sidelist to assess type
def type_checker(side_list):
    if side_list[0] == side_list[1] == side_list[2]:
        return("equilateral")
    elif side_list[0] == side_list[1] or side_list[0] == side_list[2] or side_list[1] == side_list[2]:
        return("isoceles")
    else:
        return("scalene")

#sees if it is right angle
def r_angle_checker(side_list):
    if (side_list[0]**2 + side_list[1]**2) == side_list[2]**2 or (side_list[0]**2 + side_list[2]**2) == side_list[1]**2 or (side_list[1]**2 + side_list[2]**2) == side_list[0]**2:
        print("And it's a right angle!")
    else:
        print("Not right angle")

#COMMENTED OUT - DATA PROVIDED in part (b)
'''
#gets values for triangle sides from user, checks them & appends them to list if valid
print("Enter the lengths of each line")
for i in range(3):
    counter += 1
    print("Enter side", counter)
    side_candidate = input("")
    try:
        try:
            side_candidate = int(side_candidate)
        except:
            side_candidate = float(side_candidate)
        print("Valid")
        side_list.append(side_candidate)
    except:
        print("Not valid, enter another")
        asking_for_valid = True
        while asking_for_valid == True:
            side_candidate = input("Enter another please.")
            try:
                try:
                    side_candidate = int(side_candidate)
                except:
                    side_candidate = float(side_candidate)
                side_list.append(side_candidate)
                asking_for_valid = False
            except:
                print("Invalid again.")
'''
        
#runs through list of lists to check each list as its own triangle        
for side_list in testData:
    triangle_type = ''
    print(f"Testing {side_list}")
    if side_checker(side_list) == True:
        triangle_type = type_checker(side_list)
        print("Triangle type is:",triangle_type)
        if type_checker(side_list).lower() == 'scalene':
            r_angle_checker(side_list)
    print("\n")



