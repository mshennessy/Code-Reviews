


#Initialise Lists
peopleList = []
heightsList = []

# Function finds tallest person - part(g)
def find_tallest():
    # Initalising both tallest height as the first in the list
    tallestH = heightsList[0]
    # Iterates through the index of heightsLists and checks if previous height is greater
    # Reassigns the variable if it is greater, alongside setting the tallest person with said height
    for i in range(len(heightsList)):
        if heightsList[i] > tallestH:
            tallestH = heightsList[i]
            tallestP = peopleList[i]
    # Finally prints who the tallest person is
    print("The tallest person is " + tallestP )
    


# Boolean finished controls while loop
finished = False
while not finished:
    # Input gets name from the user
    person = input("Enter a name: ").capitalize() # - part(d)
    # If input is blank then the loop is cut - part (a)
    if person == "":
        finished = True
    # Checks if the entered name is already in the List - part(f)
    elif peopleList.__contains__(person):
        print("They are already in the List!")
    # Adds the name to the List and asks for their corresponding height
    else:
        peopleList.append(person) # - part (b)
        height = float(input("Enter their height: ")) # - part (c)
        heightsList.append(height)


#print(peopleList, heightsList) - testing what the list looked like

# Creates the two heading, two tabs appart - part (e)
print("Name\t\tHeight")
# Iterates through and prints the name and the corresponding height, also two tabs apart
for i in range(len(peopleList)):
    print(peopleList[i] + "\t\t" + str(heightsList[i]))

# Calls the function to find tallest person
find_tallest()





        
    






