


#Initialise Lists
peopleList=[]
heightsList=[]

# Boolean finished controls while loop/ Asks for names and then capitalizes them
finished = False
while not finished:
    person=str(input("Enter a name"))
    capital=person.capitalize()
    
#checks for duplicates
    if peopleList.count(capital)>0:
       print("They are already in the list")
       peopleList.append(capital)
    
    
#ends code if no user is entered   
    if person == "":
        finished = True
        break

#height input and changes it to a float
    height=float(input("Enter their height"))
    heightsList.append(height)
    
        
#prints list of names and heights
print("Name \t Height")
for i in range(peopleList):
    print(peopleList[i], "\t", heightsList[i])
    
    
#function to find the tallest person in the list   
def findTallest(heightsList):
    tallestPerson = max(heightsList)
    print(tallestPerson)








