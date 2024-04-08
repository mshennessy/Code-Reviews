


#Initialise Lists
peopleList=[]
heightsList=[]

# Boolean finished controls while loop
finished = False
while not finished:
    #makes input neat and capitalised
    person=input("Enter a name: ")
    capPerson = person.capitalize()
    
    #checks if the name is already entered
    if peopleList.count(capPerson)>0:
        print("Name already entered.")
        continue
    #adds name to list if new
    else:
        peopleList.append(capPerson)
    
    #checks if a name was entered before asking for height
    if len(person) > 0:
        #turns input into a float to allow decimals
        height = float(input("Enter their height: "))
        heightsList.append(height)
    #if no name was entered loop ends
    else:
        finished = True

#prints names and heights neatly in organised columns
print("Name\tHeight")
for i in range(len(heightsList)):
    print(peopleList[i], "\t", heightsList[i])
    i+=1
    
#function which finds the tallest person 
def findTallest(heights):
    tallestHeight = max(heights)
    index = heights.index(tallestHeight)
    return peopleList[index]
    
#prints who the tallest person is
tallest = findTallest(heightsList)
print(tallest, "is the tallest person")
    






