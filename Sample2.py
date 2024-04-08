

#Initialise Lists
peopleList=[]
heightsList=[]

# Boolean finished controls while loop
finished = False
while not finished:
    person=input("Enter a name")
    height=input("Enter their height")
    
#while loop ends when user hits enter 
    if person == (""):
        finished = True
#Checking for duplicate names
if person != person:
    finished = True
    if person == person:
        finished = False
        print("They are already in this List")
        
#append the people and their heights to the lists
peopleList.append(person)
heightsList.append(height)

#Making so the name's first letter is capitalized 
person.capitalize()

#print the headings 
print("Name", "Height")
#Creating a for loop to print the list of names
#int(person)
for i in range (len(peopleList)):
    print(peopleList)
#Creating a new for loop to print the list of heights
#int(height)
for i in range (len(heightsList)):
    print(heightsList)
   
#Finding the tallest person
#findTallest = max(heightsList):
   # print("The tallest person is", findTallest )
    

    
    

    






