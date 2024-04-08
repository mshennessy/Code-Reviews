

#Create function
def findTallest():
    
    

#Initialise Lists
peopleList=[]
heightsList=[]

# Boolean finished controls while loop
finished = False
while not finished:
    person=input("Enter a name")
#capitalize the input
    person.capitalize()
#append the names to peopleList and heightsList
    """peopleList = peopleList.append(person)"""
#Ask user their height
    height=input("Enter a height")
    """heightsList = heightsList.append(height)"""
#Check for duplicates
    """if person == person:
        print("They are already in the list")"""
#When user doesnt enter anything the loop ends
    if person == (''):
        break
#append the names to peopleList and heightsList
"""peopleList = peopleList.append(person)
heightsList = heightsList.append(height)"""


#Create headings 
print('Name',' ',' ',' ','Height')
#create loop
for i in range peopleList.count():
    print(peopleList,' ',' ',' ',heightsList,\n)
    findTallest()
    





    






